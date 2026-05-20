#!/usr/bin/env python3
"""Regenerate README files and figure assets from the current report data."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "conferences" / "iclr" / "2026"
FIGURES_DIR = ROOT / "figures"
README_FULL = ROOT / "README.md"
README_ANON = ROOT / "README-anonymous.md"

FULL_STATS_PATH = DATA_DIR / "full_stats.json"
FULL_RESULTS_PATH = DATA_DIR / "full_results.json"
HALLUC_PATH = DATA_DIR / "hallucinated_references.json"


BLUE = "#5B8BA0"
TEAL = "#6BA292"
CORAL = "#C97064"
GOLD = "#D4A843"
SLATE = "#7A8B99"
SAGE = "#8CAA7E"
BG_COLOR = "#FAFAFA"
GRID_COLOR = "#E0E0E0"
TEXT_COLOR = "#333333"


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def pct(value: int, total: int, digits: int = 2) -> str:
    return f"{(value / total) * 100:.{digits}f}%"


def per_paper(value: int, total_papers: int) -> str:
    return f"{value / total_papers:.1f}"


def ratio_text(total: int, subset: int) -> str:
    if subset == 0:
        return "0"
    return str(round(total / subset))


def md_escape(value) -> str:
    if value is None:
        return ""
    text = str(value)
    text = text.replace("|", "\\|")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_explanation(value) -> str:
    text = md_escape(value)
    text = re.sub(r"\s+Totals:.*$", "", text)
    text = re.sub(r"\s+PHASE TIMING.*$", "", text)
    text = text.strip()
    if text and text[-1] not in ".!?)\"":
        text += " [source explanation truncated in JSON]"
    return text


def apply_style(ax, title: str = "", xlabel: str = "", ylabel: str = ""):
    ax.set_facecolor(BG_COLOR)
    ax.figure.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CCCCCC")
    ax.spines["bottom"].set_color("#CCCCCC")
    ax.tick_params(colors=TEXT_COLOR, labelsize=11)
    ax.yaxis.label.set_color(TEXT_COLOR)
    ax.xaxis.label.set_color(TEXT_COLOR)
    if title:
        ax.set_title(title, fontsize=15, fontweight="600", color=TEXT_COLOR, pad=14)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12, labelpad=8)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12, labelpad=8)
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.6)
    ax.set_axisbelow(True)


def compute_summary():
    stats = load_json(FULL_STATS_PATH)
    halluc = load_json(HALLUC_PATH)
    full = load_json(FULL_RESULTS_PATH)

    papers_by_id = full["papers"]
    flat_records = []
    ref_counts = []
    verdicts = Counter()
    likely_per_paper = Counter()
    url_split = Counter()

    for paper_id, paper in papers_by_id.items():
        refs = paper.get("references", [])
        ref_counts.append(len(refs))
        for ref in refs:
            flat_records.append((paper_id, paper, ref))
            assessment = ref.get("hallucination_assessment") or {}
            if assessment:
                verdict = assessment.get("verdict", "UNKNOWN")
                verdicts[verdict] += 1
                if verdict == "LIKELY":
                    likely_per_paper[paper_id] += 1
            else:
                verdicts["NO_ASSESSMENT"] += 1

            if ref.get("error_type") == "url":
                if (ref.get("ref_url_cited") or "").strip():
                    url_split["suboptimal_url"] += 1
                else:
                    url_split["no_url"] += 1

    verified_count = verdicts.get("NO_ASSESSMENT", 0)
    cleared_count = (
        verdicts.get("UNLIKELY", 0)
        + verdicts.get("VERIFIED_CLEAN", 0)
        + verdicts.get("NOT_HALLUCINATED", 0)
    )
    likely_count = verdicts.get("LIKELY", 0)
    uncertain_count = verdicts.get("UNCERTAIN", 0)

    top_papers = sorted(
        halluc["papers"],
        key=lambda paper: (-paper["hallucinated_refs_count"], paper["title"].lower()),
    )

    papers_3_plus = sum(1 for count in likely_per_paper.values() if count >= 3)
    papers_5_plus = sum(1 for count in likely_per_paper.values() if count >= 5)

    metadata_counts = {
        "No URL provided (available but omitted)": url_split["no_url"],
        "Multiple fields differ": stats["error_type_distribution"].get("multiple", 0),
        "Author name mismatches": stats["error_type_distribution"].get("author", 0),
        "Suboptimal URL (valid but not canonical)": url_split["suboptimal_url"],
        "Venue mismatches": stats["error_type_distribution"].get("venue", 0),
        "Unverified references": stats["error_type_distribution"].get("unverified", 0),
        "Year mismatches": stats["error_type_distribution"].get("year", 0),
        "Title mismatches": stats["error_type_distribution"].get("title", 0),
    }

    return {
        "stats": stats,
        "halluc": halluc,
        "papers_by_id": papers_by_id,
        "flat_records": flat_records,
        "ref_counts": ref_counts,
        "verdicts": verdicts,
        "likely_per_paper": likely_per_paper,
        "top_papers": top_papers,
        "papers_3_plus": papers_3_plus,
        "papers_5_plus": papers_5_plus,
        "verified_count": verified_count,
        "cleared_count": cleared_count,
        "likely_count": likely_count,
        "uncertain_count": uncertain_count,
        "metadata_counts": metadata_counts,
        "url_issue_total": url_split["no_url"] + url_split["suboptimal_url"],
    }


def generate_figures(summary):
    FIGURES_DIR.mkdir(exist_ok=True)

    total_refs = summary["stats"]["total_references"]
    total_papers = summary["stats"]["total_papers"]
    ref_counts = summary["ref_counts"]

    median_refs = int(np.median(ref_counts))
    mean_refs = float(np.mean(ref_counts))

    fig, ax = plt.subplots(figsize=(12, 5))
    bins = np.arange(0, max(ref_counts) + 3, 2)
    ax.hist(ref_counts, bins=bins, color=BLUE, edgecolor="white", linewidth=0.4, alpha=0.9)
    ax.axvline(median_refs, color=CORAL, linestyle="--", linewidth=1.6, label=f"Median: {median_refs}")
    ax.axvline(mean_refs, color=GOLD, linestyle="--", linewidth=1.6, label=f"Mean: {mean_refs:.1f}")
    apply_style(
        ax,
        title="Reference-Count Distribution Across ICLR 2026 Accepted Papers",
        xlabel="Number of references per paper",
        ylabel="Number of papers",
    )
    ax.set_xlim(0, 125)
    ax.legend(fontsize=11, frameon=False)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "ref_distribution.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4.8))
    categories = [
        "Verified\n(matched in DB)",
        "Cleared after\nassessment",
        "Flagged LIKELY\nhallucinated",
        "Uncertain",
    ]
    values = [
        summary["verified_count"],
        summary["cleared_count"],
        summary["likely_count"],
        summary["uncertain_count"],
    ]
    colors = [TEAL, BLUE, CORAL, GOLD]
    bars = ax.bar(categories, values, color=colors, width=0.58, edgecolor="white", linewidth=0.6)
    ax.set_yscale("log")
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value * 1.25,
            f"{value:,}\n({pct(value, total_refs)})",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="600",
            color=TEXT_COLOR,
        )
    apply_style(
        ax,
        title=f"Verification Outcomes - {total_refs:,} References",
        ylabel="Count (log scale)",
    )
    ax.grid(axis="x", visible=False)
    ax.set_ylim(10, summary["verified_count"] * 5)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "verification_outcomes.png", dpi=180)
    plt.close(fig)

    dist = Counter(summary["likely_per_paper"].values())
    x_values = sorted(dist)
    y_values = [dist[value] for value in x_values]
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(x_values, y_values, color=CORAL, edgecolor="white", linewidth=0.6, width=0.7, alpha=0.92)
    for bar, value in zip(bars, y_values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(y_values) * 0.02,
            str(value),
            ha="center",
            va="bottom",
            fontsize=12,
            fontweight="600",
            color=TEXT_COLOR,
        )
    apply_style(
        ax,
        title="Distribution of Hallucinated References Per Affected Paper",
        xlabel="Number of likely hallucinated references",
        ylabel="Number of papers",
    )
    ax.set_xticks(x_values)
    ax.text(
        0.97,
        0.95,
        (
            f"{summary['likely_count']} likely hallucinated refs across "
            f"{summary['stats']['papers_with_likely']} papers\n"
            f"({summary['stats']['papers_with_likely'] / total_papers * 100:.1f}% of accepted papers)"
        ),
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        color=SLATE,
        bbox={"boxstyle": "round,pad=0.4", "facecolor": "#F0F0F0", "edgecolor": "#DDDDDD", "linewidth": 0.6},
    )
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "tp_distribution.png", dpi=180)
    plt.close(fig)

    metadata_items = list(summary["metadata_counts"].items())
    labels = [label for label, _ in metadata_items]
    values = [value for _, value in metadata_items]
    colors = [BLUE, TEAL, CORAL, GOLD, SLATE, SAGE, "#8E7BAF", "#C78B8B"]

    fig, ax = plt.subplots(figsize=(10.5, 5))
    bars = ax.barh(range(len(labels)), values, color=colors[: len(labels)], height=0.62, edgecolor="white", linewidth=0.5)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=11)
    ax.invert_yaxis()
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_width() + max(values) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{value:,}",
            va="center",
            fontsize=10,
            color=TEXT_COLOR,
        )
    apply_style(
        ax,
        title="Metadata Discrepancy Types Across All References",
        xlabel="Count",
    )
    ax.grid(axis="x", color=GRID_COLOR, linewidth=0.6)
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "error_types.png", dpi=180)
    plt.close(fig)


def render_results_table(summary) -> str:
    total_refs = summary["stats"]["total_references"]
    rows = [
        ("Verified (matched in database)", summary["verified_count"]),
        ("Cleared after assessment", summary["cleared_count"]),
        ("Uncertain (insufficient signal)", summary["uncertain_count"]),
        ("**Flagged LIKELY hallucinated**", summary["likely_count"]),
    ]
    lines = ["| Outcome | Count | Percent |", "|---|---:|---:|"]
    for label, value in rows:
        lines.append(f"| {label} | {value:,} | {pct(value, total_refs)} |")
    return "\n".join(lines)


def render_metadata_table(summary) -> str:
    total_papers = summary["stats"]["total_papers"]
    lines = ["| Issue | Count | Per Paper (avg) |", "|---|---:|---:|"]
    for label, value in summary["metadata_counts"].items():
        lines.append(f"| {label} | {value:,} | {per_paper(value, total_papers)} |")
    return "\n".join(lines)


def render_top_papers_table(summary) -> str:
    rows = [paper for paper in summary["top_papers"] if paper["hallucinated_refs_count"] >= 5]
    lines = ["| Paper | OpenReview | Hallucinated Refs |", "|---|---|---:|"]
    for paper in rows:
        title = md_escape(paper["title"])
        url = paper["url"]
        paper_id = paper["paper_id"]
        count = paper["hallucinated_refs_count"]
        lines.append(f"| {title} | [{paper_id}]({url}) | {count} |")
    return "\n".join(lines)


def render_config_table(summary) -> str:
    total_refs = summary["stats"]["total_references"]
    lines = [
        "| Detail | Value |",
        "|---|---|",
        "| Tool | [RefChecker](https://github.com/markrussinovich/refchecker) v3.0.77 |",
        "| LLM (extraction + assessment) | Claude Sonnet 4.6 (with web search for assessment) |",
        "| Primary database | Semantic Scholar local snapshot (233M papers, 87 GB) |",
        "| Fallback APIs | CrossRef, DBLP, OpenAlex, OpenReview |",
        "| Papers downloaded | 5,355 |",
        f"| Papers processed | {summary['stats']['total_papers']:,} (7 failed - corrupt PDFs or missing bibliographies) |",
        f"| Total references extracted | {total_refs:,} |",
        "| LLM cost | ~$1,600 |",
        "| Total wall-clock time | ~12 hours |",
        "| Infrastructure | 3 machines x 10 workers |",
    ]
    return "\n".join(lines)


def render_appendix_a(summary) -> str:
    papers = [paper for paper in summary["top_papers"] if paper["hallucinated_refs_count"] >= 5]
    sections = [
        "## Appendix A: Papers with >=5 Hallucinated References",
        "",
        (
            f"Below are all {len(papers)} papers that contain 5 or more likely hallucinated references in the current scan. "
            "Each table keeps the cited title, cited authors, year, and full assessment text intact."
        ),
        "",
        "---",
        "",
    ]

    for index, paper in enumerate(papers, start=1):
        sections.append(
            f"### {index}. {md_escape(paper['title'])} ({paper['hallucinated_refs_count']} hallucinated refs)"
        )
        sections.append("")
        sections.append(f"**Paper:** [{paper['url']}]({paper['url']})")
        sections.append("")
        sections.append("| # | Cited Title | Fabricated Authors | Year | LLM Judge |")
        sections.append("|---|---|---|---:|---|")
        for row_index, ref in enumerate(paper["hallucinated_references"], start=1):
            title = md_escape(ref.get("ref_title", ""))
            authors = md_escape(ref.get("ref_authors_cited", ""))
            year = (ref.get("original_reference") or {}).get("year") or ref.get("ref_year_cited") or ""
            explanation = normalize_explanation(ref.get("hallucination_assessment", {}).get("explanation", ""))
            sections.append(f"| {row_index} | {title} | {authors} | {year} | {explanation} |")
        sections.append("")
        sections.append("---")
        sections.append("")

    return "\n".join(sections).rstrip() + "\n"


def build_full_readme(summary) -> str:
    total_refs = summary["stats"]["total_references"]
    total_papers = summary["stats"]["total_papers"]
    papers_with_likely = summary["stats"]["papers_with_likely"]
    likely_count = summary["likely_count"]
    median_refs = int(np.median(summary["ref_counts"]))
    mean_refs = np.mean(summary["ref_counts"])
    url_issue_total = summary["url_issue_total"]

    parts = [
        "# How Clean Are the References in ICLR 2026?",
        f"## A Full Scan of {total_refs:,} Citations",
        "",
        "Mark Russinovich",
        "",
        "---",
        "",
        (
            "With LLM-assisted writing becoming mainstream in research, a natural question is whether fake references are "
            "slipping into top-venue papers. [GPTZero's Hallucination Check](https://gptzero.me/news/iclr-2026/) sampled "
            "300 ICLR 2026 submissions and found 50 with at least one hallucinated citation. To get the full picture, I ran "
            "[RefChecker](https://github.com/markrussinovich/refchecker) against every accepted paper at ICLR 2026."
        ),
        "",
        (
            f"The short answer: **about 1 in {ratio_text(total_papers, papers_with_likely)} accepted papers contain at least one "
            f"likely fabricated reference.** Out of {total_papers:,} processed papers with {total_refs:,} total citations, "
            f"RefChecker flagged **{likely_count:,} likely hallucinations** across **{papers_with_likely:,} papers** "
            f"({papers_with_likely / total_papers * 100:.1f}%). Most likely hallucinations are still plausible-looking references whose author list, title, or "
            "identifier does not survive exact verification."
        ),
        "",
        "## RefChecker",
        "",
        (
            "[RefChecker](https://github.com/markrussinovich/refchecker) is an open-source tool for validating academic "
            "references. It extracts each bibliography entry from a PDF, parses the structured fields, and then checks the "
            "reference against multiple academic data sources."
        ),
        "",
        (
            "The verification pipeline works in layers. First, RefChecker tries to match each citation against Semantic Scholar, "
            "OpenAlex, and CrossRef using normalized title similarity and author-overlap checks. For references that still do not "
            "resolve cleanly, RefChecker applies deterministic filters and then sends the flagged subset to an LLM with web search "
            "access for a final hallucination assessment."
        ),
        "",
        (
            "For this scan, I used a local Semantic Scholar snapshot (233 million papers, 87 GB) as the primary database, with API "
            "fallbacks to CrossRef, DBLP, OpenAlex, and OpenReview. The LLM for both extraction and hallucination assessment was "
            "Claude Sonnet 4.6."
        ),
        "",
        "## The Dataset",
        "",
        (
            "RefChecker downloaded and extracted bibliographies from all 5,355 accepted ICLR 2026 papers on OpenReview. Seven could "
            f"not be processed, leaving {total_papers:,} papers with a combined {total_refs:,} references."
        ),
        "",
        (
            f"The typical paper cites about {mean_refs:.1f} references (median: {median_refs}), though some survey-style papers go "
            "well above 100 and a few short papers cite only one or two."
        ),
        "",
        "![Reference-count distribution across accepted papers](figures/ref_distribution.png)",
        "*Distribution of references per paper across the ICLR 2026 corpus.*",
        "",
        "## Results",
        "",
        render_results_table(summary),
        "",
        "![Verification outcomes](figures/verification_outcomes.png)",
        f"*Verification outcomes for all {total_refs:,} extracted references.*",
        "",
        (
            f"Most references ({summary['verified_count']:,}, or {pct(summary['verified_count'], total_refs)}) matched a known paper "
            f"directly in the citation databases. Another {summary['cleared_count']:,} references ({pct(summary['cleared_count'], total_refs)}) "
            "needed explicit assessment but were cleared as real. Only a small residual slice remained uncertain or likely fabricated."
        ),
        "",
        f"## Confirmed Hallucinations: {likely_count:,} References Across {papers_with_likely:,} Papers",
        "",
        (
            f"RefChecker flagged **{likely_count:,} references as LIKELY hallucinated** across **{papers_with_likely:,} papers** - "
            f"{papers_with_likely / total_papers * 100:.1f}% of accepted papers. Most affected papers have one or two likely "
            f"hallucinations; **{summary['papers_3_plus']} papers have 3 or more**, and **{summary['papers_5_plus']} papers have 5 or more**."
        ),
        "",
        (
            "The failures still cluster into two recognizable patterns. Some references point to real papers but attach the wrong author "
            "list, venue, or identifier. Others cannot be verified as written at all because the cited title, arXiv ID, DOI, or source "
            "type does not map to a real academic paper."
        ),
        "",
        "![Hallucinated references per affected paper](figures/tp_distribution.png)",
        "*Distribution of likely hallucinated references per affected paper.*",
        "",
        "### Papers with the Most Hallucinated References",
        "",
        (
            f"{summary['papers_5_plus']} papers have 5 or more likely hallucinated references. "
            "Those papers are listed below, and Appendix A expands each one into a full per-reference table."
        ),
        "",
        render_top_papers_table(summary),
        "",
        "## Metadata Quality",
        "",
        (
            "Hallucinated references draw the most attention, but the much larger practical problem is metadata quality. Across the "
            "corpus, tens of thousands of references have mismatched URLs, author strings, venues, years, or multiple fields at once."
        ),
        "",
        render_metadata_table(summary),
        "",
        "![Metadata discrepancy types](figures/error_types.png)",
        "*Distribution of metadata discrepancy types across all references.*",
        "",
        (
            f"URL issues alone affect {url_issue_total:,} references, or more than half the corpus. Of those, "
            f"{summary['metadata_counts']['No URL provided (available but omitted)']:,} omit an available URL entirely and "
            f"{summary['metadata_counts']['Suboptimal URL (valid but not canonical)']:,} point to a valid but non-canonical landing page. "
            f"That works out to roughly {url_issue_total / total_papers:.1f} URL-related issues per paper on average."
        ),
        "",
        "## What This Means",
        "",
        (
            f"A full scan of accepted ICLR 2026 papers now finds {likely_count:,} likely fabricated references across {papers_with_likely:,} papers - "
            f"about 1 in {ratio_text(total_papers, papers_with_likely)} accepted papers. That is a small fraction of all citations, but it is not a "
            "rare edge case at the paper level."
        ),
        "",
        (
            "The sharper operational issue is bibliographic hygiene. Metadata errors outnumber likely "
            "hallucinations by two orders of magnitude, which means reference verification is noisy even when no one fabricated a citation. "
            "Automated checks are cheap enough to run before publication, and the current data argue for doing exactly that."
        ),
        "",
        "## Scan Configuration and Runtime",
        "",
        render_config_table(summary),
        "",
        "## Data",
        "",
        "The raw outputs for the scan are available in the [`conferences/iclr/2026/`](conferences/iclr/2026/) directory:",
        "",
        f"- [`hallucinated_references.json`](conferences/iclr/2026/hallucinated_references.json) - All {likely_count:,} LIKELY-flagged references grouped by paper, including cited metadata and full assessment text",
        "- [`full_stats.json`](conferences/iclr/2026/full_stats.json) - Aggregate statistics for the full corpus scan",
        "- [`full_results.json`](conferences/iclr/2026/full_results.json) - Combined per-paper results across all processing shards",
        "",
        "---",
        "",
        render_appendix_a(summary).rstrip(),
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def build_anonymous_readme(summary) -> str:
    total_refs = summary["stats"]["total_references"]
    total_papers = summary["stats"]["total_papers"]
    papers_with_likely = summary["stats"]["papers_with_likely"]
    likely_count = summary["likely_count"]
    median_refs = int(np.median(summary["ref_counts"]))
    mean_refs = np.mean(summary["ref_counts"])
    url_issue_total = summary["url_issue_total"]

    parts = [
        "# How Clean Are the References in ICLR 2026?",
        f"## A Full Scan of {total_refs:,} Citations",
        "",
        "Anonymous",
        "",
        "---",
        "",
        (
            "With LLM-assisted writing becoming mainstream in research, a natural question is whether fake references are slipping into "
            "top-venue papers. To get the full picture, we ran RefChecker against every accepted paper at ICLR 2026."
        ),
        "",
        (
            f"The short answer: **about 1 in {ratio_text(total_papers, papers_with_likely)} accepted papers contain at least one likely "
            f"fabricated reference.** Out of {total_papers:,} processed papers with {total_refs:,} total citations, RefChecker flagged "
            f"**{likely_count:,} likely hallucinations** across **{papers_with_likely:,} papers** ({papers_with_likely / total_papers * 100:.1f}%)."
        ),
        "",
        "## RefChecker",
        "",
        (
            "RefChecker is an open-source tool for validating academic references. It extracts each bibliography entry from a PDF, "
            "parses the fields, and checks the result against multiple academic databases before escalating unresolved cases to an LLM "
            "with web search access."
        ),
        "",
        "## The Dataset",
        "",
        (
            f"RefChecker processed {total_papers:,} accepted ICLR 2026 papers and extracted {total_refs:,} references. "
            f"The typical paper cites about {mean_refs:.1f} references (median: {median_refs})."
        ),
        "",
        "![Reference-count distribution across accepted papers](figures/ref_distribution.png)",
        "*Distribution of references per paper across the ICLR 2026 corpus.*",
        "",
        "## Results",
        "",
        render_results_table(summary),
        "",
        "![Verification outcomes](figures/verification_outcomes.png)",
        f"*Verification outcomes for all {total_refs:,} extracted references.*",
        "",
        f"## Confirmed Hallucinations: {likely_count:,} References Across {papers_with_likely:,} Papers",
        "",
        (
            f"RefChecker flagged **{likely_count:,} references as LIKELY hallucinated** across **{papers_with_likely:,} papers** - "
            f"{papers_with_likely / total_papers * 100:.1f}% of accepted papers. Most affected papers have one or two likely "
            f"hallucinations; **{summary['papers_3_plus']} papers have 3 or more**, and **{summary['papers_5_plus']} papers have 5 or more**."
        ),
        "",
        "![Hallucinated references per affected paper](figures/tp_distribution.png)",
        "*Distribution of likely hallucinated references per affected paper.*",
        "",
        "## Metadata Quality",
        "",
        render_metadata_table(summary),
        "",
        "![Metadata discrepancy types](figures/error_types.png)",
        "*Distribution of metadata discrepancy types across all references.*",
        "",
        (
            f"URL issues alone affect {url_issue_total:,} references, or about {url_issue_total / total_refs * 100:.1f}% of the corpus. "
            f"That is roughly {url_issue_total / total_papers:.1f} URL-related issues per paper on average."
        ),
        "",
        "## State of Academic References",
        "",
        (
            f"The current results find likely fabricated references in about 1 in {ratio_text(total_papers, papers_with_likely)} accepted papers, "
            "and far larger volumes of ordinary metadata noise. Both problems are small enough to catch automatically and "
            "large enough to matter operationally."
        ),
        "",
        "## Scan Configuration and Runtime",
        "",
        render_config_table(summary),
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def main():
    summary = compute_summary()
    generate_figures(summary)
    README_FULL.write_text(build_full_readme(summary), encoding="utf-8")
    README_ANON.write_text(build_anonymous_readme(summary), encoding="utf-8")
    print("Regenerated figures, README.md, and README-anonymous.md")


if __name__ == "__main__":
    main()