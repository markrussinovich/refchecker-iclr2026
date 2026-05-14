#!/usr/bin/env python3
"""Generate compact hallucinated-reference reports from RefChecker scan JSON.

The output format matches the workspace-level ICLR hallucination reports:

* compact summary table
* exact-count distribution table
* papers with three or more LIKELY references
* distribution chart with bars and cumulative-percentage line
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.replace("|", "\\|")
    return re.sub(r"\s+", " ", text).strip()


def workspace_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def paper_count(paper: dict[str, Any]) -> int:
    return int(paper.get("flagged_records") or paper.get("hallucinated_refs_count") or 0)


def paper_total_refs(paper: dict[str, Any]) -> int:
    return int(
        paper.get("total_records")
        or paper.get("total_references")
        or paper.get("references_processed")
        or 0
    )


def normalize_paper(paper: dict[str, Any]) -> dict[str, Any]:
    return {
        "paper_id": paper.get("source_paper_id") or paper.get("paper_id") or "",
        "title": paper.get("source_title") or paper.get("title") or "",
        "url": paper.get("source_url") or paper.get("url") or "",
        "total_references": paper_total_refs(paper),
        "hallucinated_refs_count": paper_count(paper),
    }


def summary_from_scan_report(scan_report: dict[str, Any]) -> dict[str, Any]:
    papers = [normalize_paper(paper) for paper in scan_report.get("papers", [])]
    distribution = Counter(
        paper["hallucinated_refs_count"]
        for paper in papers
        if paper["hallucinated_refs_count"] > 0
    )
    likely_count = sum(count * papers_at_count for count, papers_at_count in distribution.items())
    papers_with_likely = sum(distribution.values())
    papers_3_plus = sum(
        papers_at_count for count, papers_at_count in distribution.items() if count >= 3
    )

    return {
        "papers": papers,
        "total_papers": len(papers),
        "distribution": distribution,
        "likely_count": likely_count,
        "papers_with_likely": papers_with_likely,
        "papers_3_plus": papers_3_plus,
    }


def summary_from_hallucinated_references(data: dict[str, Any]) -> dict[str, Any]:
    papers = []
    for paper_id, paper in data.get("papers", {}).items():
        count = int(paper.get("likely_count") or len(paper.get("references", [])) or 0)
        papers.append(
            {
                "paper_id": paper_id,
                "title": paper.get("title") or "",
                "url": paper.get("url") or "",
                "total_references": int(paper.get("total_references") or 0),
                "hallucinated_refs_count": count,
            }
        )

    distribution = Counter(
        paper["hallucinated_refs_count"]
        for paper in papers
        if paper["hallucinated_refs_count"] > 0
    )
    likely_count = sum(count * papers_at_count for count, papers_at_count in distribution.items())
    papers_with_likely = sum(distribution.values())
    papers_3_plus = sum(
        papers_at_count for count, papers_at_count in distribution.items() if count >= 3
    )
    source_summary = data.get("summary") or {}
    total_papers = int(
        source_summary.get("total_papers_scanned")
        or source_summary.get("total_papers_processed")
        or source_summary.get("total_papers")
        or len(papers)
    )

    return {
        "papers": papers,
        "total_papers": total_papers,
        "distribution": distribution,
        "likely_count": likely_count,
        "papers_with_likely": papers_with_likely,
        "papers_3_plus": papers_3_plus,
    }


def summarize_report(data: dict[str, Any]) -> dict[str, Any]:
    papers = data.get("papers")
    if isinstance(papers, list):
        return summary_from_scan_report(data)
    if isinstance(papers, dict):
        return summary_from_hallucinated_references(data)
    raise ValueError("Input JSON must contain a 'papers' list or object.")


def render_chart(summary: dict[str, Any], *, conference: str, year: str, output_path: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    distribution: Counter[int] = summary["distribution"]
    if not distribution:
        return

    x_values = sorted(distribution)
    paper_counts = [distribution.get(value, 0) for value in x_values]
    positions = np.arange(len(x_values))
    total_papers = max(1, int(summary.get("total_papers") or sum(distribution.values())))
    threshold_pct = [
        sum(papers_at_count for count, papers_at_count in distribution.items() if count >= value)
        / total_papers
        * 100
        for value in x_values
    ]

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    bar_color = "#4C78A8"
    line_color = "#F58518"
    grid_color = "#D9D9D9"
    text_color = "#333333"

    bars = ax.bar(positions, paper_counts, color=bar_color, edgecolor="white", linewidth=0.8, width=0.72)
    for bar, value in zip(bars, paper_counts):
        if value == 0:
            continue
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + max(paper_counts) * 0.012,
            f"{value}",
            ha="center",
            va="bottom",
            fontsize=10,
            color=text_color,
        )

    ax2 = ax.twinx()
    ax2.plot(positions, threshold_pct, color=line_color, marker="o", linewidth=2.0, markersize=5)
    ax2.set_ylim(0, max(5, max(threshold_pct) * 1.15))
    ax2.set_ylabel("Papers with >= N flags (%)", fontsize=11, color=text_color)
    ax2.tick_params(axis="y", colors=text_color, labelsize=10)

    ax.set_title(
        f"Distribution of Hallucinated References Per {conference.upper()} {year} Paper",
        fontsize=15,
        fontweight="600",
        color=text_color,
        pad=14,
    )
    ax.set_xlabel("Hallucinated references per paper", fontsize=11, color=text_color, labelpad=8)
    ax.set_ylabel("Number of papers", fontsize=11, color=text_color, labelpad=8)
    ax.set_xticks(positions)
    ax.set_xticklabels([str(value) for value in x_values])
    ax.tick_params(axis="both", colors=text_color, labelsize=10)
    ax.grid(axis="y", color=grid_color, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#BBBBBB")
    ax.spines["bottom"].set_color("#BBBBBB")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_color("#BBBBBB")

    ax.legend([bars, ax2.lines[0]], ["Papers", "Papers with >= N flags (%)"], frameon=False, loc="upper right")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, facecolor="white")
    plt.close(fig)


def render_report(
    summary: dict[str, Any],
    *,
    conference: str,
    year: str,
    source_path: Path,
    output_path: Path,
    chart_name: str,
) -> None:
    distribution: Counter[int] = summary["distribution"]
    ranked_papers = sorted(
        [paper for paper in summary["papers"] if paper["hallucinated_refs_count"] >= 3],
        key=lambda paper: (-paper["hallucinated_refs_count"], paper["paper_id"]),
    )

    lines: list[str] = [
        f"# {conference.upper()} {year} Hallucinated Reference Report",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        f"Source: `{workspace_path(source_path)}`",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Hallucinated references | {summary['likely_count']:,} |",
        f"| Papers with hallucinated references | {summary['papers_with_likely']:,} |",
        f"| Papers with >=3 hallucinated references | {summary['papers_3_plus']:,} |",
        "",
        "## Distribution",
        "",
        f"![Distribution of hallucinated references per {conference.upper()} {year} paper]({chart_name})",
        "",
        "| Hallucinated refs | Papers with exactly this count |",
        "|---:|---:|",
    ]

    for count in range(1, max(distribution, default=0) + 1):
        papers_at_count = distribution.get(count, 0)
        if papers_at_count == 0:
            continue
        lines.append(f"| {count} | {papers_at_count:,} |")

    lines.extend([
        "",
        "## Papers With >=3 Hallucinated References",
        "",
        "| Rank | Hallucinated refs | Paper ID | Title | Total references | OpenReview |",
        "|---:|---:|---|---|---:|---|",
    ])

    for rank, paper in enumerate(ranked_papers, start=1):
        paper_id = md_escape(paper["paper_id"])
        title = md_escape(paper["title"])
        url = paper["url"]
        link = f"[link]({url})" if url else ""
        lines.append(
            f"| {rank} | {paper['hallucinated_refs_count']} | `{paper_id}` | {title} | "
            f"{paper['total_references']} | {link} |"
        )

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conference", required=True, help="Conference name, e.g. icml or iclr.")
    parser.add_argument("--year", required=True, help="Conference year, e.g. 2025.")
    parser.add_argument("--input", type=Path, help="Path to scan_report.json or hallucinated_references.json.")
    parser.add_argument("--scan-report", type=Path, help="Deprecated alias for --input.")
    parser.add_argument("--output", type=Path, required=True, help="Markdown report output path.")
    parser.add_argument("--chart", type=Path, required=True, help="PNG chart output path.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    input_path = args.input or args.scan_report
    if input_path is None:
        raise SystemExit("error: one of --input or --scan-report is required")
    scan_report = load_json(input_path)
    summary = summarize_report(scan_report)
    render_chart(summary, conference=args.conference, year=args.year, output_path=args.chart)
    render_report(
        summary,
        conference=args.conference,
        year=args.year,
        source_path=input_path,
        output_path=args.output,
        chart_name=args.chart.name,
    )
    print(f"Wrote {args.output}")
    print(f"Wrote {args.chart}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())