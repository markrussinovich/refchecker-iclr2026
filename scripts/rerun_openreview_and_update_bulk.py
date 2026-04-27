#!/usr/bin/env python3
"""Rerun one or more OpenReview papers and surgically update bulk results.

For each OpenReview URL, this script removes the cached bibliography, runs
RefChecker with the ICLR defaults used for the bulk scan, replaces that paper's
records in the bulk JSON report, and optionally replaces the matching row in
the checkpoint JSONL file.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REFCHECKER_DIR = Path("/datadrive/refchecker")
DEFAULT_REFCHECKER_PYTHON = DEFAULT_REFCHECKER_DIR / ".venv" / "bin" / "python"
DEFAULT_BULK_RESULTS = ROOT / "data" / "iclr2026" / "scan_report.json"
DEFAULT_CHECKPOINT = ROOT / "data" / "iclr2026" / "scan_report.checkpoint.jsonl"
DEFAULT_CACHE_DIR = Path("/datadrive/refcheckercache/cache")
DEFAULT_DATABASE_DIR = Path("/datadrive/refcheckercache/db")
DEFAULT_MODEL = "gemini-3.1-flash-lite-preview"
DEFAULT_MAX_WORKERS = 6


def paper_id_from_openreview_url(openreview_url: str) -> str:
    match = re.search(r"[?&]id=([^&#]+)", openreview_url)
    if not match:
        raise ValueError(f"OpenReview URL does not contain an id query parameter: {openreview_url}")
    return match.group(1)


def maybe_paper_id_from_openreview_url(openreview_url: str) -> str | None:
    match = re.search(r"[?&]id=([^&#]+)", openreview_url or "")
    return match.group(1) if match else None


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    tmp_path = path.with_suffix(path.suffix + f".tmp-{os.getpid()}")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    tmp_path.replace(path)


def load_checkpoint(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_checkpoint(path: Path, rows: list[dict[str, Any]]) -> None:
    tmp_path = path.with_suffix(path.suffix + f".tmp-{os.getpid()}")
    with tmp_path.open("w", encoding="utf-8") as handle:
        for row in sorted(rows, key=lambda item: int(item.get("index", 0))):
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    tmp_path.replace(path)


def backup_path(path: Path) -> Path:
    return path.with_suffix(path.suffix + f".bak-{utc_timestamp()}")


def delete_cached_bibliography(cache_dir: Path, paper_id: str) -> bool:
    bib_path = cache_dir / f"openreview_{paper_id}" / "bibliography.json"
    if bib_path.exists():
        bib_path.unlink()
        return True
    return False


def active_refchecker_processes(report_path: Path) -> list[str]:
    try:
        proc = subprocess.run(
            ["pgrep", "-af", "run_refchecker.py"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        return []
    if proc.returncode not in (0, 1):
        return []
    report_text = str(report_path)
    current_pid = str(os.getpid())
    active = []
    for line in proc.stdout.splitlines():
        if line.startswith(current_pid + " "):
            continue
        if report_text in line:
            active.append(line)
    return active


def run_single_paper_scan(
    *,
    openreview_url: str,
    refchecker_dir: Path,
    python_executable: Path,
    cache_dir: Path,
    database_dir: Path,
    model: str,
    max_workers: int,
) -> tuple[dict[str, Any], dict[str, Any] | None]:
    with tempfile.TemporaryDirectory(prefix="refchecker-openreview-rerun-") as tmp:
        tmp_dir = Path(tmp)
        paper_list = tmp_dir / "paper-list.txt"
        report_file = tmp_dir / "scan_report.json"
        output_file = tmp_dir / "scan_errors.txt"
        paper_list.write_text(openreview_url + "\n", encoding="utf-8")

        env = os.environ.copy()
        env["REFCHECKER_KEEP_CHECKPOINT"] = "1"

        command = [
            str(python_executable),
            "run_refchecker.py",
            "--paper-list",
            str(paper_list),
            "--cache",
            str(cache_dir),
            "--database-dir",
            str(database_dir),
            "--llm-provider",
            "google",
            "--llm-model",
            model,
            "--hallucination-provider",
            "google",
            "--hallucination-model",
            model,
            "--report-file",
            str(report_file),
            "--report-format",
            "json",
            "--output-file",
            str(output_file),
            "--max-workers",
            str(max_workers),
        ]
        subprocess.run(command, cwd=refchecker_dir, env=env, check=True)

        checkpoint_path = report_file.with_suffix(".checkpoint.jsonl")
        checkpoint_rows = load_checkpoint(checkpoint_path)
        checkpoint_row = checkpoint_rows[0] if len(checkpoint_rows) == 1 else None
        if checkpoint_row is None:
            print("Temporary checkpoint row was not retained; will synthesize checkpoint update from JSON report")
        return load_json(report_file), checkpoint_row


def recompute_summary(payload: dict[str, Any]) -> None:
    papers = payload.get("papers") or []
    records = payload.get("records") or []
    likely_records = [
        record
        for record in records
        if (record.get("hallucination_assessment") or {}).get("verdict") == "LIKELY"
    ]
    paper_ids_with_records = {record.get("source_paper_id") for record in records if record.get("source_paper_id")}
    paper_ids_with_likely = {record.get("source_paper_id") for record in likely_records if record.get("source_paper_id")}

    summary = payload.setdefault("summary", {})
    summary["total_papers_processed"] = len(papers)
    summary["records_written"] = len(records)
    summary["papers_with_records"] = len(paper_ids_with_records)
    summary["flagged_records"] = len(likely_records)
    summary["flagged_papers"] = len(paper_ids_with_likely)
    summary["total_references_processed"] = sum(int(paper.get("total_records") or 0) for paper in papers)


def replace_bulk_report_paper(bulk_path: Path, single_payload: dict[str, Any], paper_id: str, *, dry_run: bool) -> None:
    payload = load_json(bulk_path)
    single_papers = single_payload.get("papers") or []
    if len(single_papers) != 1:
        raise RuntimeError(f"Expected one paper summary in rerun report, found {len(single_papers)}")
    replacement_paper = single_papers[0]
    replacement_records = [
        record for record in (single_payload.get("records") or [])
        if record.get("source_paper_id") == paper_id
    ]

    papers = payload.get("papers") or []
    paper_indexes = [
        index for index, paper in enumerate(papers)
        if paper.get("source_paper_id") == paper_id
    ]
    if len(paper_indexes) == 0:
        print(f"Bulk JSON does not contain {paper_id}; skipping bulk JSON replacement")
        return
    if len(paper_indexes) != 1:
        raise RuntimeError(f"Expected one paper summary for {paper_id} in {bulk_path}, found {len(paper_indexes)}")

    old_records = [
        record for record in (payload.get("records") or [])
        if record.get("source_paper_id") == paper_id
    ]
    print(
        f"Bulk JSON update for {paper_id}: records {len(old_records)} -> {len(replacement_records)}, "
        f"flagged {papers[paper_indexes[0]].get('flagged_records', 0)} -> {replacement_paper.get('flagged_records', 0)}"
    )
    if dry_run:
        return

    backup = backup_path(bulk_path)
    shutil.copy2(bulk_path, backup)
    print(f"Backed up bulk JSON: {backup}")

    papers[paper_indexes[0]] = replacement_paper
    payload["papers"] = papers
    payload["records"] = [
        record for record in (payload.get("records") or [])
        if record.get("source_paper_id") != paper_id
    ] + replacement_records
    payload["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    recompute_summary(payload)
    write_json(bulk_path, payload)


def count_rows_with_raw_type(records: list[dict[str, Any]], raw_type: str) -> int:
    count = 0
    for record in records:
        raw_errors = record.get("_original_errors") or []
        if any(
            item.get("error_type") == raw_type
            or item.get("warning_type") == raw_type
            or item.get("info_type") == raw_type
            for item in raw_errors
        ):
            count += 1
    return count


def count_raw_kinds(records: list[dict[str, Any]]) -> tuple[int, int, int]:
    errors = warnings = info = 0
    for record in records:
        for item in record.get("_original_errors") or []:
            if item.get("info_type"):
                info += 1
            elif item.get("warning_type"):
                warnings += 1
            elif item.get("error_type") and item.get("error_type") != "unverified":
                errors += 1
    return errors, warnings, info


def synthesize_checkpoint_row(
    *,
    old_row: dict[str, Any],
    single_payload: dict[str, Any],
    paper_id: str,
) -> dict[str, Any]:
    single_papers = single_payload.get("papers") or []
    if len(single_papers) != 1:
        raise RuntimeError(f"Expected one paper summary in rerun report, found {len(single_papers)}")
    replacement_paper = single_papers[0]
    replacement_records = [
        record for record in (single_payload.get("records") or [])
        if record.get("source_paper_id") == paper_id
    ]
    total_references_processed = (
        (single_payload.get("summary") or {}).get("total_references_processed")
        or replacement_paper.get("total_references_processed")
        or replacement_paper.get("references_processed")
        or replacement_paper.get("total_records")
        or len(replacement_records)
    )
    error_count, warning_count, info_count = count_raw_kinds(replacement_records)
    row = dict(old_row)
    row.update({
        "paper_id": paper_id,
        "title": replacement_paper.get("source_title") or old_row.get("title") or "",
        "source_url": replacement_paper.get("source_url") or old_row.get("source_url") or "",
        "references_processed": total_references_processed,
        "total_errors_found": error_count,
        "total_warnings_found": warning_count,
        "total_info_found": info_count,
        "total_unverified_refs": count_rows_with_raw_type(replacement_records, "unverified"),
        "errors": replacement_records,
        "fatal_error": False,
        "fatal_error_message": None,
    })
    return row


def replace_checkpoint_row(
    checkpoint_path: Path,
    replacement_row: dict[str, Any] | None,
    single_payload: dict[str, Any],
    paper_id: str,
    *,
    dry_run: bool,
) -> None:
    if not checkpoint_path.exists():
        print(f"Checkpoint not found, skipping: {checkpoint_path}")
        return
    rows = load_checkpoint(checkpoint_path)
    matches = [
        index for index, row in enumerate(rows)
        if row.get("paper_id") == paper_id or maybe_paper_id_from_openreview_url(row.get("input_spec", "")) == paper_id
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one checkpoint row for {paper_id} in {checkpoint_path}, found {len(matches)}")

    old_row = rows[matches[0]]
    updated = (
        dict(replacement_row)
        if replacement_row is not None
        else synthesize_checkpoint_row(old_row=old_row, single_payload=single_payload, paper_id=paper_id)
    )
    updated["index"] = old_row["index"]
    updated["input_spec"] = old_row["input_spec"]
    print(
        f"Checkpoint update for {paper_id}: errors {old_row.get('total_errors_found', 0)} -> "
        f"{updated.get('total_errors_found', 0)}, references {old_row.get('references_processed', 0)} -> "
        f"{updated.get('references_processed', 0)}"
    )
    if dry_run:
        return

    backup = backup_path(checkpoint_path)
    shutil.copy2(checkpoint_path, backup)
    print(f"Backed up checkpoint: {backup}")
    rows[matches[0]] = updated
    write_checkpoint(checkpoint_path, rows)


def update_one(args: argparse.Namespace, openreview_url: str) -> None:
    paper_id = paper_id_from_openreview_url(openreview_url)
    active = active_refchecker_processes(args.bulk_results)
    if active and not args.force_active_run:
        raise RuntimeError(
            "RefChecker appears to be actively using this bulk results file. "
            "Stop that run first or pass --force-active-run.\n" + "\n".join(active)
        )

    removed = delete_cached_bibliography(args.cache_dir, paper_id)
    print(f"{paper_id}: cached bibliography {'removed' if removed else 'not present'}")
    single_payload, checkpoint_row = run_single_paper_scan(
        openreview_url=openreview_url,
        refchecker_dir=args.refchecker_dir,
        python_executable=args.python_executable,
        cache_dir=args.cache_dir,
        database_dir=args.database_dir,
        model=args.model,
        max_workers=args.max_workers,
    )
    replace_bulk_report_paper(args.bulk_results, single_payload, paper_id, dry_run=args.dry_run)
    if args.checkpoint:
        replace_checkpoint_row(args.checkpoint, checkpoint_row, single_payload, paper_id, dry_run=args.dry_run)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("openreview_url", nargs="*", help="OpenReview forum URL(s) to rerun")
    parser.add_argument("--openreview-list", type=Path, help="File containing OpenReview URLs to rerun")
    parser.add_argument("--bulk-results", type=Path, default=DEFAULT_BULK_RESULTS)
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_CHECKPOINT)
    parser.add_argument("--refchecker-dir", type=Path, default=DEFAULT_REFCHECKER_DIR)
    parser.add_argument("--python-executable", type=Path, default=DEFAULT_REFCHECKER_PYTHON)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    parser.add_argument("--database-dir", type=Path, default=DEFAULT_DATABASE_DIR)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-workers", type=int, default=DEFAULT_MAX_WORKERS)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force-active-run", action="store_true")
    args = parser.parse_args()

    urls = list(args.openreview_url)
    if args.openreview_list:
        urls.extend(
            line.strip()
            for line in args.openreview_list.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    if not urls:
        parser.error("provide at least one OpenReview URL or --openreview-list")

    for url in urls:
        update_one(args, url)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)