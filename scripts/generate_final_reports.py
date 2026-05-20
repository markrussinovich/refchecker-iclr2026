#!/usr/bin/env python3
"""Generate tracked final reports from completed workspace scan reports."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import generate_hallucination_report as hallucination_report
import generate_overview_hallucination_rate_chart as overview_report


ROOT = Path(__file__).resolve().parent.parent
CONFERENCE_DIR_RE = re.compile(r"^([a-z-]+)(20\d{2})$")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def completed_scan_reports(
    workspace_dir: Path,
    *,
    include_empty: bool = False,
) -> list[tuple[str, str, Path]]:
    scan_reports: list[tuple[str, str, Path]] = []
    for conference_dir in sorted(workspace_dir.iterdir()):
        match = CONFERENCE_DIR_RE.fullmatch(conference_dir.name)
        if not match:
            continue

        report_path = conference_dir / "results" / "scan_report.json"
        if not report_path.exists():
            continue

        scan_report = load_json(report_path)
        summary = scan_report.get("summary") or {}
        if not include_empty and int(summary.get("records_written") or 0) <= 0:
            print(f"Skipping {conference_dir.name}: records_written=0")
            continue

        conference, year = match.groups()
        scan_reports.append((conference, year, report_path))
    return scan_reports


def generate_conference_report(
    conference: str,
    year: str,
    scan_report_path: Path,
    reports_dir: Path,
) -> None:
    output_dir = reports_dir / conference / year
    output_dir.mkdir(parents=True, exist_ok=True)
    hallucination_report.main(
        [
            "--conference",
            conference,
            "--year",
            year,
            "--input",
            str(scan_report_path),
            "--output",
            str(output_dir / "hallucination_report.md"),
            "--chart",
            str(output_dir / "hallucination_count_distribution.png"),
        ]
    )


def generate_overview(workspace_dir: Path, reports_dir: Path) -> None:
    output_dir = reports_dir / "overview"
    output_dir.mkdir(parents=True, exist_ok=True)
    points = overview_report.scan_points(workspace_dir)
    overview_report.render_paper_chart(points, output_dir / "papers_with_ge2_flags_by_year.png")
    overview_report.write_data_table(points, output_dir / "papers_with_ge2_flags_by_year.csv")
    overview_report.render_reference_chart(points, output_dir / "hallucinated_reference_rate_by_year.png")
    overview_report.write_reference_data_table(
        points,
        output_dir / "hallucinated_reference_rate_by_year.csv",
    )
    overview_report.render_academic_reference_chart(
        points,
        output_dir / "academic_paper_hallucinated_reference_rate_by_year.png",
    )
    overview_report.write_academic_reference_data_table(
        points,
        output_dir / "academic_paper_hallucinated_reference_rate_by_year.csv",
    )
    print(f"Wrote {output_dir / 'papers_with_ge2_flags_by_year.png'}")
    print(f"Wrote {output_dir / 'papers_with_ge2_flags_by_year.csv'}")
    print(f"Wrote {output_dir / 'hallucinated_reference_rate_by_year.png'}")
    print(f"Wrote {output_dir / 'hallucinated_reference_rate_by_year.csv'}")
    print(f"Wrote {output_dir / 'academic_paper_hallucinated_reference_rate_by_year.png'}")
    print(f"Wrote {output_dir / 'academic_paper_hallucinated_reference_rate_by_year.csv'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace-dir",
        type=Path,
        default=ROOT / "_workspace",
        help="Workspace directory containing conference scan folders.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=ROOT / "reports",
        help="Tracked reports output directory.",
    )
    parser.add_argument(
        "--include-empty",
        action="store_true",
        help="Include scan reports with records_written=0.",
    )
    parser.add_argument(
        "--skip-overview",
        action="store_true",
        help="Do not regenerate reports/overview artifacts.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    workspace_dir = args.workspace_dir.resolve()
    reports_dir = args.reports_dir.resolve()
    reports = completed_scan_reports(workspace_dir, include_empty=args.include_empty)

    for conference, year, scan_report_path in reports:
        generate_conference_report(conference, year, scan_report_path, reports_dir)

    if not args.skip_overview:
        generate_overview(workspace_dir, reports_dir)

    print(f"generated_report_count {len(reports)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())