#!/usr/bin/env python3
"""Prepare and finalize ICLR 2026 checkpoint refreshes."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "iclr2026"
WORKSPACE_DIR = ROOT / "_workspace"
CHECKPOINT = DATA_DIR / "scan_report.checkpoint.jsonl"
STATS = DATA_DIR / "v1" / "full_stats.json"
INPUT_LIST = WORKSPACE_DIR / "iclr2026_scan_checkpoint_inputs.txt"
LIKELY_LIST = WORKSPACE_DIR / "iclr2026_current_likely_papers.txt"
TOP5_REPORT = WORKSPACE_DIR / "iclr2026_top5_likely_references.md"
CURRENT_TOP5_REPORT = WORKSPACE_DIR / "iclr2026_current_top5_likely_references.md"
DEFAULT_CACHE_DIR = Path("/datadrive/refcheckercache/cache")


def load_checkpoint(path: Path = CHECKPOINT) -> list[dict]:
    rows_by_index: dict[int, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            rows_by_index[int(row["index"])] = row
    return [rows_by_index[index] for index in sorted(rows_by_index)]


def write_checkpoint(rows: list[dict], path: Path = CHECKPOINT) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in sorted(rows, key=lambda item: int(item["index"])):
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def likely_errors(row: dict) -> list[dict]:
    return [
        error
        for error in row.get("errors", [])
        if (error.get("hallucination_assessment") or {}).get("verdict") == "LIKELY"
    ]


def paper_id_from_spec(spec: str) -> str | None:
    match = re.search(r"[?&]id=([^&]+)", spec or "")
    return match.group(1) if match else None


def prepare(cache_dir: Path) -> None:
    rows = load_checkpoint()
    flagged = [row for row in rows if likely_errors(row)]
    if not flagged:
        print("No LIKELY hallucination flags found in checkpoint.")
        return

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = CHECKPOINT.with_suffix(CHECKPOINT.suffix + f".bak-{timestamp}")
    shutil.copy2(CHECKPOINT, backup)

    WORKSPACE_DIR.mkdir(exist_ok=True)
    INPUT_LIST.write_text(
        "".join(f"{row['input_spec']}\n" for row in rows),
        encoding="utf-8",
    )
    LIKELY_LIST.write_text(
        "".join(f"{row['input_spec']}\n" for row in flagged),
        encoding="utf-8",
    )

    flagged_indexes = {int(row["index"]) for row in flagged}
    write_checkpoint([row for row in rows if int(row["index"]) not in flagged_indexes])

    removed = 0
    missing = 0
    for row in flagged:
        paper_id = row.get("paper_id") or paper_id_from_spec(row.get("input_spec", ""))
        bib_path = cache_dir / f"openreview_{paper_id}" / "bibliography.json"
        if bib_path.exists():
            bib_path.unlink()
            removed += 1
        else:
            missing += 1

    print(f"Flagged papers: {len(flagged)}")
    print(f"Checkpoint backup: {backup}")
    print(f"Rerun input list: {INPUT_LIST}")
    print(f"Flagged-only list: {LIKELY_LIST}")
    print(f"Cached bibliographies removed: {removed}; missing: {missing}")
    print(f"Checkpoint entries kept for resume: {len(rows) - len(flagged)}")


def markdown_escape(value) -> str:
    text = "" if value is None else str(value)
    text = text.replace("|", "\\|")
    return re.sub(r"\s+", " ", text).strip()


def corrected_citation(error: dict) -> str:
    for key in ("ref_corrected_plaintext", "ref_standard_format", "ref_verified_url", "ref_url_correct"):
        value = error.get(key)
        if value:
            return markdown_escape(value)
    return "Not available"


def raw_reference(error: dict) -> str:
    original = error.get("original_reference") or {}
    return markdown_escape(error.get("ref_raw_text") or original.get("raw_text") or error.get("ref_title") or "")


def assessment_text(error: dict) -> str:
    assessment = error.get("hallucination_assessment") or {}
    return markdown_escape(assessment.get("explanation") or "")


def write_stats_and_report(rows: list[dict]) -> None:
    verdicts = Counter()
    error_types = Counter()
    likely_rows = []

    for row in rows:
        row_likely = likely_errors(row)
        if row_likely:
            likely_rows.append((row, row_likely))
        for error in row.get("errors", []):
            assessment = error.get("hallucination_assessment") or {}
            verdicts[assessment.get("verdict") or "NO_ASSESSMENT"] += 1
            error_types[error.get("error_type") or "unknown"] += 1

    stats = {
        "generated_at": datetime.now(timezone.utc).replace(tzinfo=None).isoformat(),
        "source": "data/iclr2026/scan_report.checkpoint.jsonl",
        "note": "Current checkpoint aggregate after rerunning papers with LIKELY hallucination flags.",
        "total_papers": len(rows),
        "total_references": sum(int(row.get("references_processed") or 0) for row in rows),
        "total_likely": sum(len(errors) for _, errors in likely_rows),
        "papers_with_likely": len(likely_rows),
        "verdict_distribution": dict(verdicts),
        "error_type_distribution": dict(error_types),
    }
    STATS.parent.mkdir(exist_ok=True)
    STATS.write_text(json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    ranked = sorted(
        likely_rows,
        key=lambda item: (-len(item[1]), item[0].get("title") or "", item[0].get("paper_id") or ""),
    )[:5]

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# ICLR 2026 Papers With the Most Likely References",
        "",
        "Source: `data/iclr2026/scan_report.checkpoint.jsonl`",
        f"Generated: {generated}",
        "",
        "This report ranks papers in the current checkpoint by the number of references whose `hallucination_assessment.verdict` is `LIKELY`.",
        f"The checkpoint currently contains {len(rows)} paper records after refreshing cached bibliographies for papers with LIKELY flags.",
        "",
        "## Top 5 Summary",
        "",
        "| Rank | Paper | URL | Likely refs | References processed | Errors | Warnings | Info | Unverified | Fatal error |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for rank, (row, errors) in enumerate(ranked, 1):
        title = markdown_escape(row.get("title") or "Untitled")
        paper_id = markdown_escape(row.get("paper_id") or "")
        url = markdown_escape(row.get("source_url") or row.get("input_spec") or "")
        lines.append(
            f"| {rank} | {title} (`{paper_id}`) | {url} | {len(errors)} | "
            f"{row.get('references_processed', 0)} | {row.get('total_errors_found', 0)} | "
            f"{row.get('total_warnings_found', 0)} | {row.get('total_info_found', 0)} | "
            f"{row.get('total_unverified_refs', 0)} | {row.get('fatal_error', False)} |"
        )

    for rank, (row, errors) in enumerate(ranked, 1):
        title = markdown_escape(row.get("title") or "Untitled")
        lines.extend([
            "",
            f"## {rank}. {title}",
            "",
            f"- Paper ID: `{markdown_escape(row.get('paper_id') or '')}`",
            f"- URL: {markdown_escape(row.get('source_url') or row.get('input_spec') or '')}",
            f"- Likely references: {len(errors)}",
            f"- References processed: {row.get('references_processed', 0)}",
            f"- Errors: {row.get('total_errors_found', 0)}",
            f"- Warnings: {row.get('total_warnings_found', 0)}",
            f"- Info findings: {row.get('total_info_found', 0)}",
            f"- Unverified references: {row.get('total_unverified_refs', 0)}",
            f"- arXiv / non-arXiv / other references: {row.get('total_arxiv_refs', 0)} / {row.get('total_non_arxiv_refs', 0)} / {row.get('total_other_refs', 0)}",
            f"- Fatal error: {row.get('fatal_error', False)}",
            "",
            "| # | Full raw reference | Correct citation if available | LLM judge evaluation text |",
            "|---:|---|---|---|",
        ])
        for index, error in enumerate(errors, 1):
            lines.append(
                f"| {index} | {raw_reference(error)} | {corrected_citation(error)} | {assessment_text(error)} |"
            )

    report_text = "\n".join(lines).rstrip() + "\n"
    TOP5_REPORT.write_text(report_text, encoding="utf-8")
    CURRENT_TOP5_REPORT.write_text(report_text, encoding="utf-8")
    print(f"Stats written: {STATS}")
    print(f"Top-5 report written: {TOP5_REPORT}")
    print(f"Current top-5 report written: {CURRENT_TOP5_REPORT}")
    print(f"Likely references: {stats['total_likely']} across {stats['papers_with_likely']} papers")


def finalize() -> None:
    rows = load_checkpoint()
    write_stats_and_report(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    subparsers.add_parser("finalize")
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(args.cache_dir)
    elif args.command == "finalize":
        finalize()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())