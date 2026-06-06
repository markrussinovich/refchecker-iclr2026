#!/usr/bin/env python3
"""Build an overview JSON for hallucinated references in awarded papers."""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "_workspace" / "overview" / "awarded_paper_hallucinated_references.json"


@dataclass(frozen=True)
class AwardRow:
    conference: str
    year: int
    title: str
    award: str
    link: str
    details_path: Path


def normalize_title(title: str) -> str:
    title = html.unescape(title or "")
    title = unicodedata.normalize("NFKD", title)
    title = "".join(ch for ch in title if not unicodedata.combining(ch))
    title = title.lower().replace("&", " and ")
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def canonical_url(url: str) -> str:
    url = html.unescape(url or "").strip()
    url = url.split("#", 1)[0]
    url = re.sub(r"[?&]t=[^&]+$", "", url)
    return url.rstrip("/")


def url_variants(url: str) -> set[str]:
    clean = canonical_url(url)
    if not clean:
        return set()
    variants = {clean}
    if clean.startswith("http://"):
        variants.add("https://" + clean[len("http://") :])
    elif clean.startswith("https://"):
        variants.add("http://" + clean[len("https://") :])
    return variants


def load_award_rows() -> list[AwardRow]:
    rows: list[AwardRow] = []
    for path in sorted((ROOT / "conferences").glob("*/*/*-awarded-details.txt")):
        conference = path.parts[-3]
        year = int(path.parts[-2])
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                title = (row.get("Title") or "").strip()
                award = (row.get("Award/Nomination") or "").strip()
                link = (row.get("Link") or "").strip()
                if title and award:
                    rows.append(AwardRow(conference, year, title, award, link, path))
    return rows


def scan_report_path(conference: str, year: int) -> Path:
    return ROOT / "_workspace" / f"{conference}{year}" / "results" / "scan_report.json"


def load_scan_report(conference: str, year: int) -> dict[str, Any]:
    with scan_report_path(conference, year).open(encoding="utf-8") as f:
        return json.load(f)


def papers_list(report: dict[str, Any]) -> list[dict[str, Any]]:
    papers = report.get("papers") or []
    if isinstance(papers, dict):
        return list(papers.values())
    return list(papers)


def build_indices(papers: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_url: dict[str, dict[str, Any]] = {}
    by_title: dict[str, dict[str, Any]] = {}
    for paper in papers:
        for variant in url_variants(str(paper.get("source_url") or "")):
            by_url.setdefault(variant, paper)
        title_key = normalize_title(str(paper.get("source_title") or ""))
        if title_key:
            by_title.setdefault(title_key, paper)
    return by_url, by_title


def fetch_page(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def source_candidates_from_virtual_page(url: str, page: str) -> list[str]:
    candidates: list[str] = []
    candidates.extend(match.group(0) for match in re.finditer(r"https://openreview\.net/forum\?id=[A-Za-z0-9_-]+", page))
    candidates.extend(match.group(0) for match in re.finditer(r"https?://[^\"'<>\s]+\.pdf", page))

    for match in re.finditer(r"https?://proceedings\.mlr\.press/v(\d+)/([A-Za-z0-9_-]+)\.html", page):
        volume, slug = match.groups()
        candidates.append(f"https://proceedings.mlr.press/v{volume}/{slug}/{slug}.pdf")
        candidates.append(f"http://proceedings.mlr.press/v{volume}/{slug}.html")

    for match in re.finditer(
        r"https://proceedings\.neurips\.cc/paper_files/paper/(\d+)/hash/([a-f0-9]+)-Abstract([^\"'<>\s]*)\.html",
        page,
        flags=re.IGNORECASE,
    ):
        year, digest, suffix = match.groups()
        suffix = suffix or ""
        candidates.append(f"https://proceedings.neurips.cc/paper_files/paper/{year}/file/{digest}-Paper{suffix}.pdf")

    for match in re.finditer(r"/media/PosterPDFs/NeurIPS%20(\d{4})/([a-f0-9]{32})", page, flags=re.IGNORECASE):
        year, digest = match.groups()
        if int(year) <= 2021:
            candidates.append(f"https://papers.nips.cc/paper_files/paper/{year}/file/{digest}-Paper.pdf")
        candidates.append(f"https://proceedings.neurips.cc/paper_files/paper/{year}/file/{digest}-Paper-Conference.pdf")
        candidates.append(f"https://proceedings.neurips.cc/paper_files/paper/{year}/file/{digest}-Paper.pdf")

    # Some virtual pages are already the source page or contain relative PDF/media links.
    if "neurips.cc/virtual/" in url:
        for match in re.finditer(r"/media/PosterPDFs/NeurIPS%20(\d{4})/([a-f0-9]{32})", page, flags=re.IGNORECASE):
            year, digest = match.groups()
            candidates.append(f"https://papers.nips.cc/paper_files/paper/{year}/file/{digest}-Paper.pdf")

    return list(dict.fromkeys(canonical_url(candidate) for candidate in candidates if candidate))


def alternate_virtual_urls(url: str) -> list[str]:
    match = re.search(r"/virtual/(\d{4})/(poster|oral)/(\d+)", url)
    if not match:
        return []
    year, kind, event_id_text = match.groups()
    event_id = int(event_id_text)
    base = url[: match.start()] + f"/virtual/{year}"
    candidates = []
    if kind == "oral":
        candidates.extend([f"{base}/poster/{event_id - 1}", f"{base}/poster/{event_id}"])
    else:
        candidates.extend([f"{base}/oral/{event_id + 1}", f"{base}/oral/{event_id}"])
    return candidates


def resolve_award_paper(
    award: AwardRow,
    by_url: dict[str, dict[str, Any]],
    by_title: dict[str, dict[str, Any]],
    page_cache: dict[str, str],
) -> tuple[dict[str, Any] | None, str, list[str]]:
    for variant in url_variants(award.link):
        if variant in by_url:
            return by_url[variant], "award_link", [variant]

    title_key = normalize_title(award.title)
    if title_key in by_title:
        return by_title[title_key], "award_title", []

    candidates: list[str] = []
    if "/virtual/" in award.link:
        for virtual_url in [award.link, *alternate_virtual_urls(award.link)]:
            try:
                page = page_cache.setdefault(virtual_url, fetch_page(virtual_url))
                candidates.extend(source_candidates_from_virtual_page(virtual_url, page))
            except (urllib.error.URLError, TimeoutError, ValueError):
                continue
            for candidate in candidates:
                for variant in url_variants(candidate):
                    if variant in by_url:
                        return by_url[variant], "virtual_page_source_link", candidates
    return None, "unmatched", candidates


def is_likely_hallucinated_record(record: dict[str, Any]) -> bool:
    assessment = record.get("hallucination_assessment") or {}
    if isinstance(assessment, dict) and assessment.get("verdict") == "LIKELY":
        return True
    details = str(record.get("error_details") or "")
    return "Likely hallucinated" in details or "🚩" in details


def paper_match_keys(paper: dict[str, Any]) -> tuple[str, str]:
    return str(paper.get("source_paper_id") or ""), canonical_url(str(paper.get("source_url") or ""))


def record_match_keys(record: dict[str, Any]) -> tuple[str, str]:
    return str(record.get("source_paper_id") or ""), canonical_url(str(record.get("source_url") or ""))


def build_overview() -> dict[str, Any]:
    award_rows = load_award_rows()
    grouped_awards: dict[tuple[str, int], list[AwardRow]] = defaultdict(list)
    for row in award_rows:
        grouped_awards[(row.conference, row.year)].append(row)

    page_cache: dict[str, str] = {}
    paper_entries: list[dict[str, Any]] = []
    unmatched_awards: list[dict[str, Any]] = []

    for conference, year in sorted(grouped_awards):
        report_path = scan_report_path(conference, year)
        if not report_path.exists():
            for award in grouped_awards[(conference, year)]:
                unmatched_awards.append(unmatched_entry(award, "missing_scan_report", []))
            continue

        report = load_scan_report(conference, year)
        papers = papers_list(report)
        by_url, by_title = build_indices(papers)

        resolved: list[tuple[AwardRow, dict[str, Any], str, list[str]]] = []
        key_to_indexes: dict[tuple[str, str], list[int]] = defaultdict(list)
        for award in grouped_awards[(conference, year)]:
            paper, resolved_via, candidates = resolve_award_paper(award, by_url, by_title, page_cache)
            if not paper:
                unmatched_awards.append(unmatched_entry(award, resolved_via, candidates))
                continue
            index = len(resolved)
            resolved.append((award, paper, resolved_via, candidates))
            key_to_indexes[paper_match_keys(paper)].append(index)

        references_by_index: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for record in report.get("records") or []:
            if not is_likely_hallucinated_record(record):
                continue
            indexes = key_to_indexes.get(record_match_keys(record))
            if not indexes:
                continue
            for index in indexes:
                references_by_index[index].append(record)

        for index, (award, paper, resolved_via, candidates) in enumerate(resolved):
            refs = references_by_index.get(index, [])
            paper_entries.append(
                {
                    "conference": conference.upper() if conference != "usenix-security" else "USENIX Security",
                    "conference_slug": conference,
                    "year": year,
                    "award": award.award,
                    "award_title": award.title,
                    "award_link": award.link,
                    "resolved_via": resolved_via,
                    "resolved_candidate_links": candidates,
                    "scan_report": str(report_path.relative_to(ROOT)),
                    "paper_check_summary": paper,
                    "source_paper_id": paper.get("source_paper_id"),
                    "source_title": paper.get("source_title"),
                    "source_authors": paper.get("source_authors"),
                    "source_year": paper.get("source_year"),
                    "source_url": paper.get("source_url"),
                    "likely_hallucinated_reference_count": len(refs),
                    "likely_hallucinated_references": refs,
                }
            )

    summary = {
        "award_detail_files_processed": len(list((ROOT / "conferences").glob("*/*/*-awarded-details.txt"))),
        "awarded_entries_seen": len(award_rows),
        "awarded_entries_matched_to_scan": len(paper_entries),
        "unmatched_awarded_entries": len(unmatched_awards),
        "awarded_entries_with_likely_hallucinated_references": sum(
            1 for entry in paper_entries if entry["likely_hallucinated_reference_count"] > 0
        ),
        "likely_hallucinated_references": sum(
            entry["likely_hallucinated_reference_count"] for entry in paper_entries
        ),
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "papers": paper_entries,
        "unmatched_awards": unmatched_awards,
    }


def unmatched_entry(award: AwardRow, reason: str, candidates: list[str]) -> dict[str, Any]:
    return {
        "conference": award.conference,
        "year": award.year,
        "title": award.title,
        "award": award.award,
        "link": award.link,
        "details_path": str(award.details_path.relative_to(ROOT)),
        "reason": reason,
        "resolved_candidate_links": candidates,
    }


def main() -> int:
    overview = build_overview()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(overview, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = overview["summary"]
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")
    print(
        "Matched {awarded_entries_matched_to_scan}/{awarded_entries_seen} awarded entries; "
        "{awarded_entries_with_likely_hallucinated_references} papers have "
        "{likely_hallucinated_references} LIKELY hallucinated references.".format(**summary)
    )
    if summary["unmatched_awarded_entries"]:
        print(f"Unmatched awarded entries: {summary['unmatched_awarded_entries']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())