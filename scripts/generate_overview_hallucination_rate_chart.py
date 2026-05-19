#!/usr/bin/env python3
"""Generate overview charts for hallucinated-reference rates."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "_workspace" / "overview" / "papers_with_ge2_flags_by_year.png"
DEFAULT_REFERENCE_OUTPUT = ROOT / "_workspace" / "overview" / "hallucinated_reference_rate_by_year.png"
CONFERENCE_DIR_RE = re.compile(r"^(iclr|icml|neurips)(\d{4})$")
FLAG_THRESHOLD = 2
CHATGPT_RELEASE_DATE = date(2022, 11, 30)

# Full-paper submission deadlines, used as the timeline position for each accepted-paper corpus.
SUBMISSION_DEADLINES: dict[tuple[str, int], date] = {
    ("ICLR", 2021): date(2020, 10, 2),
    ("ICML", 2021): date(2021, 2, 4),
    ("ICLR", 2024): date(2023, 9, 28),
    ("ICML", 2024): date(2024, 2, 1),
    ("ICLR", 2025): date(2024, 10, 1),
    ("ICML", 2025): date(2025, 1, 30),
    ("ICLR", 2026): date(2025, 9, 24),
    ("NEURIPS", 2021): date(2021, 5, 28),
    ("NEURIPS", 2024): date(2024, 5, 22),
    ("NEURIPS", 2025): date(2025, 5, 15),
    ("NEURIPS", 2026): date(2026, 5, 6),
}


@dataclass(frozen=True)
class ConferencePoint:
    conference: str
    year: int
    total_papers: int
    papers_with_flags: int
    total_references: int
    hallucinated_references: int

    @property
    def submission_deadline(self) -> date:
        try:
            return SUBMISSION_DEADLINES[(self.conference, self.year)]
        except KeyError as error:
            raise ValueError(f"Missing submission deadline for {self.conference} {self.year}") from error

    @property
    def paper_rate(self) -> float:
        return self.papers_with_flags / self.total_papers * 100

    @property
    def reference_rate(self) -> float:
        return self.hallucinated_references / self.total_references * 100


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def scan_points(workspace_dir: Path) -> list[ConferencePoint]:
    points: list[ConferencePoint] = []
    for conference_dir in sorted(workspace_dir.iterdir()):
        match = CONFERENCE_DIR_RE.match(conference_dir.name)
        if not match:
            continue

        report_path = conference_dir / "results" / "scan_report.json"
        if not report_path.exists():
            continue

        report = load_json(report_path)
        papers = report.get("papers") or []
        if not papers:
            continue

        summary = report.get("summary") or {}
        total_papers = int(summary.get("total_papers_processed") or len(papers) or 0)
        total_references = int(summary.get("total_references_processed") or 0)
        hallucinated_references = int(summary.get("flagged_records") or 0)
        papers_with_flags = sum(
            1
            for paper in papers
            if int(paper.get("flagged_records") or paper.get("hallucinated_refs_count") or 0)
            >= FLAG_THRESHOLD
        )
        if total_papers <= 0:
            continue

        conference, year = match.groups()
        conference = conference.upper()
        parsed_year = int(year)
        if (conference, parsed_year) not in SUBMISSION_DEADLINES:
            raise ValueError(f"Missing submission deadline for {conference} {parsed_year}")

        points.append(
            ConferencePoint(
                conference=conference,
                year=parsed_year,
                total_papers=total_papers,
                papers_with_flags=papers_with_flags,
                total_references=total_references,
                hallucinated_references=hallucinated_references,
            )
        )

    return points


def render_timeline_chart(
    points: list[ConferencePoint],
    output_path: Path,
    *,
    title: str,
    ylabel: str,
    rate_attr: str,
) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt

    if not points:
        raise ValueError("No completed scan reports found with reference totals.")

    conferences = ["ICML", "ICLR", "NEURIPS"]
    colors = {"ICML": "#4C78A8", "ICLR": "#F58518", "NEURIPS": "#54A24B"}
    markers = {"ICML": "o", "ICLR": "s", "NEURIPS": "^"}

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    for conference in conferences:
        conference_points = sorted(
            (point for point in points if point.conference == conference),
            key=lambda point: point.submission_deadline,
        )
        if not conference_points:
            continue

        x_values = [point.submission_deadline for point in conference_points]
        y_values = [getattr(point, rate_attr) for point in conference_points]
        ax.plot(
            x_values,
            y_values,
            color=colors[conference],
            marker=markers[conference],
            linewidth=2.4,
            markersize=7,
            label=conference,
        )
        label_y_offset = 11 if conference == "ICLR" else 13
        for point in conference_points:
            point_rate = getattr(point, rate_attr)
            ax.annotate(
                f"{point_rate:.2f}%",
                (point.submission_deadline, point_rate),
                textcoords="offset points",
                xytext=(0, label_y_offset),
                ha="center",
                fontsize=9,
                color="#333333",
            )

    ax.set_title(
        title,
        fontsize=15,
        fontweight="600",
        color="#333333",
        pad=14,
    )
    ax.set_xlabel("Full-paper submission deadline", fontsize=11, color="#333333", labelpad=8)
    ax.set_ylabel(ylabel, fontsize=11, color="#333333", labelpad=8)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.tick_params(axis="both", colors="#333333", labelsize=10)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.7, alpha=0.85)
    ax.set_axisbelow(True)
    ax.margins(x=0.07, y=0.18)
    ax.set_ylim(bottom=0)
    ax.axvline(
        CHATGPT_RELEASE_DATE,
        color="#666666",
        linestyle="--",
        linewidth=1.3,
        alpha=0.85,
    )
    ax.annotate(
        "ChatGPT release\nNov 30, 2022",
        xy=(CHATGPT_RELEASE_DATE, 0.98),
        xycoords=("data", "axes fraction"),
        xytext=(6, 0),
        textcoords="offset points",
        ha="left",
        va="top",
        fontsize=9,
        color="#555555",
    )

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color("#BBBBBB")
    ax.spines["bottom"].set_color("#BBBBBB")
    ax.legend(frameon=False, loc="upper left")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, facecolor="white")
    plt.close(fig)


def render_paper_chart(points: list[ConferencePoint], output_path: Path) -> None:
    render_timeline_chart(
        points,
        output_path,
        title="Papers With At Least 2 Hallucination Flags",
        ylabel="Papers with >=2 flags (%)",
        rate_attr="paper_rate",
    )


def render_reference_chart(points: list[ConferencePoint], output_path: Path) -> None:
    render_timeline_chart(
        [point for point in points if point.total_references > 0],
        output_path,
        title="Hallucinated Reference Rate",
        ylabel="Hallucinated references (%)",
        rate_attr="reference_rate",
    )


def write_data_table(points: list[ConferencePoint], output_path: Path) -> None:
    lines = [
        "conference,year,submission_deadline,total_papers,papers_with_ge2_flags,paper_rate_percent"
    ]
    for point in sorted(points, key=lambda item: item.submission_deadline):
        lines.append(
            f"{point.conference},{point.year},{point.submission_deadline.isoformat()},"
            f"{point.total_papers},"
            f"{point.papers_with_flags},{point.paper_rate:.6f}"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_reference_data_table(points: list[ConferencePoint], output_path: Path) -> None:
    lines = [
        "conference,year,submission_deadline,total_references,hallucinated_references,hallucination_rate_percent"
    ]
    for point in sorted(points, key=lambda item: item.submission_deadline):
        if point.total_references <= 0:
            continue
        lines.append(
            f"{point.conference},{point.year},{point.submission_deadline.isoformat()},"
            f"{point.total_references},"
            f"{point.hallucinated_references},{point.reference_rate:.6f}"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an overview chart of papers with at least two hallucination flags by year."
    )
    parser.add_argument(
        "--workspace-dir",
        type=Path,
        default=ROOT / "_workspace",
        help="Workspace directory containing conference scan folders.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output PNG path.",
    )
    parser.add_argument(
        "--data-output",
        type=Path,
        default=DEFAULT_OUTPUT.with_suffix(".csv"),
        help="Output CSV path for chart data.",
    )
    parser.add_argument(
        "--reference-output",
        type=Path,
        default=DEFAULT_REFERENCE_OUTPUT,
        help="Output PNG path for the reference-rate chart.",
    )
    parser.add_argument(
        "--reference-data-output",
        type=Path,
        default=DEFAULT_REFERENCE_OUTPUT.with_suffix(".csv"),
        help="Output CSV path for reference-rate chart data.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    points = scan_points(args.workspace_dir)
    render_paper_chart(points, args.output)
    render_reference_chart(points, args.reference_output)
    write_data_table(points, args.data_output)
    write_reference_data_table(points, args.reference_data_output)
    print(f"Wrote {args.output}")
    print(f"Wrote {args.data_output}")
    print(f"Wrote {args.reference_output}")
    print(f"Wrote {args.reference_data_output}")


if __name__ == "__main__":
    main()