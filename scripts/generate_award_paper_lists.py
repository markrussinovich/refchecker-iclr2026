#!/usr/bin/env python3
"""Generate award-paper URL lists for checked conference runs."""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import unicodedata
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
JINA_PREFIX = "https://r.jina.ai/http://r.jina.ai/http://"

CHECKED_RUNS = [
    ("iclr", 2021),
    ("iclr", 2022),
    ("iclr", 2023),
    ("iclr", 2024),
    ("iclr", 2025),
    ("iclr", 2026),
    ("icml", 2021),
    ("icml", 2022),
    ("icml", 2023),
    ("icml", 2024),
    ("icml", 2025),
    ("icml", 2026),
    ("neurips", 2021),
    ("neurips", 2022),
    ("neurips", 2023),
    ("neurips", 2024),
    ("neurips", 2025),
    ("usenix-security", 2021),
    ("usenix-security", 2022),
    ("usenix-security", 2023),
    ("usenix-security", 2024),
    ("usenix-security", 2025),
]

AWARD_WORDS = (
    "award",
    "awards",
    "best",
    "outstanding",
    "distinguished",
    "honorable",
    "honourable",
    "runner",
    "nominee",
    "nominated",
    "candidate",
    "finalist",
)


@dataclass(frozen=True)
class AwardEntry:
    title: str
    award: str
    link: str


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", errors="replace")


def normalize_title(title: str) -> str:
    title = html.unescape(title)
    title = unicodedata.normalize("NFKD", title)
    title = "".join(ch for ch in title if not unicodedata.combining(ch))
    title = title.lower()
    title = title.replace("&", " and ")
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def ascii_slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in text if not unicodedata.combining(ch)).encode("ascii", "ignore").decode("ascii")


def report_path(conference: str, year: int) -> Path:
    return ROOT / "_workspace" / f"{conference}{year}" / "results" / "scan_report.json"


def conference_dir(conference: str, year: int) -> Path:
    return ROOT / "conferences" / conference / str(year)


def load_scan_papers(conference: str, year: int) -> list[dict]:
    with report_path(conference, year).open(encoding="utf-8") as f:
        data = json.load(f)
    papers = data["papers"]
    if isinstance(papers, dict):
        return list(papers.values())
    return list(papers)


def build_title_index(conference: str, year: int) -> dict[str, dict]:
    index: dict[str, dict] = {}
    for paper in load_scan_papers(conference, year):
        title = paper.get("source_title") or ""
        key = normalize_title(title)
        if key and key not in index:
            index[key] = paper
    return index


class AwardTableParser(HTMLParser):
    def __init__(self, year: int):
        super().__init__(convert_charrefs=True)
        self.year = year
        self.rows: list[dict] = []
        self.in_tr = False
        self.td_index = -1
        self.in_a = False
        self.current: dict | None = None
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "tr":
            self.in_tr = True
            self.td_index = -1
            self.current = {"labels": [], "title": "", "href": ""}
        elif self.in_tr and tag == "td":
            self.td_index += 1
            self.text_parts = []
        elif self.in_tr and tag == "div" and self.td_index == 0:
            self.text_parts = []
        elif self.in_tr and tag == "a" and self.td_index >= 1:
            href = attrs_dict.get("href") or ""
            if f"/virtual/{self.year}/" in href and re.search(r"/(poster|oral)/\d+", href):
                self.in_a = True
                self.text_parts = []
                if self.current and not self.current["href"]:
                    self.current["href"] = href

    def handle_data(self, data: str) -> None:
        if not self.in_tr:
            return
        if self.td_index == 0 or self.in_a:
            self.text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if not self.in_tr:
            return
        if tag == "div" and self.td_index == 0:
            label = clean_space("".join(self.text_parts))
            if label:
                self.current["labels"].append(label)
            self.text_parts = []
        elif tag == "a" and self.in_a:
            title = clean_space("".join(self.text_parts))
            if title and self.current and not self.current["title"]:
                self.current["title"] = title
            self.in_a = False
            self.text_parts = []
        elif tag == "tr":
            if self.current:
                labels = [label for label in self.current["labels"] if is_award_label(label)]
                if labels and self.current["title"] and self.current["href"]:
                    self.current["labels"] = labels
                    self.rows.append(self.current)
            self.in_tr = False
            self.current = None
            self.td_index = -1


def clean_space(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def is_award_label(label: str) -> bool:
    lowered = label.lower()
    if "test of time" in lowered:
        return False
    return any(word in lowered for word in AWARD_WORDS)


def parse_virtual_awards(conference: str, year: int) -> list[AwardEntry]:
    if conference == "iclr" and year == 2021:
        return parse_iclr_2021_static_awards()
    if conference == "iclr" and year == 2025:
        return parse_iclr_blog_awards(
            "https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/"
        )
    if conference == "iclr" and year == 2026:
        return parse_iclr_blog_awards("https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/")
    page = fetch_text(f"https://{conference}.cc/virtual/{year}/awards_detail")
    parser = AwardTableParser(year)
    parser.feed(page)
    title_index = build_title_index(conference, year)
    by_title_award: dict[tuple[str, str], AwardEntry] = {}
    for row in parser.rows:
        title = clean_space(row["title"])
        key = normalize_title(title)
        paper = title_index.get(key)
        if paper:
            link = paper.get("source_url") or ""
            output_title = paper.get("source_title") or title
        else:
            link = f"https://{conference}.cc{row['href']}"
            output_title = title
        award = "; ".join(dict.fromkeys(clean_space(label) for label in row["labels"]))
        if link:
            by_title_award[(normalize_title(output_title), award)] = AwardEntry(output_title, award, link)
    return sorted(by_title_award.values(), key=lambda entry: (entry.award.lower(), entry.title.lower()))


def parse_iclr_blog_awards(url: str) -> list[AwardEntry]:
    page = fetch_text(f"{JINA_PREFIX}{url}")
    entries: list[AwardEntry] = []
    current_award = ""
    for line in page.splitlines():
        line = clean_space(line)
        if line.startswith("#") and "Outstanding Paper" in line:
            current_award = "Outstanding Paper"
            continue
        if line.startswith("#") and "Honorable Mention" in line:
            current_award = "Honorable Mention"
            continue
        if not current_award:
            continue
        match = re.search(r"(?:\*\s+)?\[(.+?)\]\((https://openreview\.net/forum\?id=[^)]+)\)", line)
        if not match:
            continue
        title = clean_space(match.group(1)).rstrip(".")
        entries.append(AwardEntry(title, current_award, match.group(2)))
    return entries


def parse_iclr_2021_static_awards() -> list[AwardEntry]:
    titles = [
        "Beyond Fully-Connected Layers with Quaternions: Parameterization of Hypercomplex Multiplications with 1/n Parameters",
        "Complex Query Answering with Neural Link Predictors",
        "EigenGame: PCA as a Nash Equilibrium",
        "Learning Mesh-Based Simulation with Graph Networks",
        "Neural Synthesis of Binaural Speech From Mono Audio",
        "Optimal Rates for Averaged Stochastic Gradient Descent under Neural Tangent Kernel Regime",
        "Rethinking Architecture Selection in Differentiable NAS",
        "Score-Based Generative Modeling through Stochastic Differential Equations",
    ]
    title_index = build_title_index("iclr", 2021)
    entries: list[AwardEntry] = []
    for title in titles:
        paper = title_index.get(normalize_title(title))
        if not paper:
            continue
        entries.append(AwardEntry(paper.get("source_title") or title, "Outstanding Paper", paper.get("source_url") or ""))
    return entries


def usenix_slug(year: int) -> str:
    return f"usenixsecurity{str(year)[2:]}"


def parse_usenix_award_titles(year: int) -> list[tuple[str, str]]:
    url = f"{JINA_PREFIX}https://www.usenix.org/conference/{usenix_slug(year)}/technical-sessions"
    lines = [clean_space(line) for line in fetch_text(url).splitlines()]
    entries: list[tuple[str, str]] = []
    for index, line in enumerate(lines):
        lowered = line.lower()
        if "distinguished paper award winner" not in lowered:
            continue
        award = line
        title = ""
        for candidate in reversed(lines[max(0, index - 8) : index]):
            if is_usenix_title_candidate(candidate):
                title = candidate
                break
        if not title:
            for candidate in lines[index + 1 : min(len(lines), index + 8)]:
                if is_usenix_title_candidate(candidate):
                    title = candidate
                    break
        if title:
            entries.append((title, award))
    return list(dict.fromkeys(entries))


def is_usenix_title_candidate(line: str) -> bool:
    if not line or len(line) < 8:
        return False
    lowered = line.lower()
    reject_fragments = (
        "available media",
        "show details",
        "hide details",
        "long presentation",
        "short presentation",
        "track ",
        "ballroom",
        "session chair",
        "distinguished",
        "winner",
        "university",
        "universiteit",
        "universitat",
        "universität",
        "institute",
        "institut",
        "college",
        "school of",
        "center for",
        "centre for",
        "google",
        "microsoft",
        "facebook",
        "amazon",
        "eth zurich",
        "epfl",
        "cispa",
        "kaist",
        "inria",
        "imec",
        "ku leuven",
        "cornell",
        "tel aviv",
        "ucla",
        "uc ",
        "research",
        "laboratory",
        " lab",
        " labs",
    )
    if any(fragment in lowered for fragment in reject_fragments):
        return False
    if ";" in line:
        return False
    if line.count(",") >= 3:
        return False
    return True


def extract_pdf_metadata(pdf_path: Path) -> tuple[str, str]:
    try:
        result = subprocess.run(
            ["pdftotext", "-f", "1", "-l", "1", str(pdf_path), "-"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "", ""
    lines = [clean_space(line) for line in result.stdout.splitlines()]
    lines = [line for line in lines if line]
    presentation_slug = ""
    for line in lines:
        match = re.search(r"https://www\.usenix\.org/conference/[^/]+/presentation/([^\s]+)", line)
        if match:
            presentation_slug = match.group(1).strip().strip("/")
            break
    skip_prefixes = (
        "proceedings of",
        "usenix security",
        "copyright",
        "isbn",
        "open access",
    )
    candidates: list[str] = []
    for line in lines[:30]:
        lowered = line.lower()
        if any(lowered.startswith(prefix) for prefix in skip_prefixes):
            continue
        if line.startswith("http") or lowered.startswith("this paper is included"):
            break
        if candidates and line.count(",") >= 2:
            break
        if re.search(
            r"\b(university|universiteit|universitat|universität|institute|institut|laboratory|college|"
            r"school|google|microsoft|facebook|amazon|research|eth zurich|epfl|cispa|kaist|inria)\b",
            lowered,
        ):
            break
        candidates.append(line)
    return clean_space(" ".join(candidates)), presentation_slug


def usenix_pdf_prefix(year: int) -> str:
    if year in (2021, 2022):
        return f"sec{str(year)[2:]}"
    return f"usenixsecurity{str(year)[2:]}"


def build_usenix_pdf_title_index(year: int) -> dict[str, dict]:
    cache_pdfs = sorted((ROOT / "_workspace" / f"usenix-security{year}" / "fresh_cache").glob("url_*/paper.pdf"))
    accepted_path = conference_dir("usenix-security", year) / f"usenix-security-{year}-accepted.txt"
    accepted_urls = set(accepted_path.read_text(encoding="utf-8").splitlines())
    prefix = usenix_pdf_prefix(year)
    index: dict[str, dict] = {}
    for pdf_path in cache_pdfs:
        title, presentation_slug = extract_pdf_metadata(pdf_path)
        if not presentation_slug:
            continue
        link = f"https://www.usenix.org/system/files/{prefix}-{presentation_slug}.pdf"
        if link not in accepted_urls:
            fallback_link = f"https://www.usenix.org/system/files/{prefix}-{ascii_slug(presentation_slug)}.pdf"
            if fallback_link not in accepted_urls:
                continue
            link = fallback_link
        key = normalize_title(title)
        if key and key not in index:
            index[key] = {"title": title, "link": link}
    return index


def parse_usenix_awards(year: int) -> list[AwardEntry]:
    title_index = build_usenix_pdf_title_index(year)
    entries: list[AwardEntry] = []
    for title, award in parse_usenix_award_titles(year):
        paper = find_usenix_title_match(title, title_index)
        if paper:
            entries.append(AwardEntry(paper["title"], award, paper["link"]))
        else:
            entries.append(AwardEntry(title, award, ""))
    entries = [entry for entry in entries if entry.link]
    return sorted(dict.fromkeys(entries), key=lambda entry: entry.title.lower())


def find_usenix_title_match(title: str, title_index: dict[str, dict]) -> dict | None:
    key = normalize_title(title)
    if key in title_index:
        return title_index[key]
    for candidate_key, paper in title_index.items():
        if len(candidate_key) >= 24 and (candidate_key in key or key in candidate_key):
            return paper
    return None


def write_outputs(conference: str, year: int, entries: list[AwardEntry]) -> None:
    out_dir = conference_dir(conference, year)
    out_dir.mkdir(parents=True, exist_ok=True)
    base = f"{conference}-{year}-awarded"
    url_path = out_dir / f"{base}.txt"
    details_path = out_dir / f"{base}-details.txt"
    url_path.write_text("".join(f"{entry.link}\n" for entry in entries), encoding="utf-8")
    lines = ["Title\tAward/Nomination\tLink"]
    lines.extend(f"{entry.title}\t{entry.award}\t{entry.link}" for entry in entries)
    details_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    for conference, year in CHECKED_RUNS:
        if not report_path(conference, year).exists():
            continue
        if conference == "usenix-security":
            entries = parse_usenix_awards(year)
        else:
            entries = parse_virtual_awards(conference, year)
        write_outputs(conference, year, entries)
        print(f"{conference} {year}: {len(entries)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())