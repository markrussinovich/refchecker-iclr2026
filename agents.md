# Agent Instructions for ICLR 2026 Reference Analysis Project

This document contains instructions for working with this repository, including PDF generation and data file information.

## Prerequisites

Ensure the following tools are installed:
- `pandoc` (for Markdown to HTML conversion)
- `weasyprint` Python package (for HTML to PDF conversion)
- `beautifulsoup4` Python package (for HTML post-processing to fix table column widths)

```bash
pip install weasyprint beautifulsoup4
```

## CSS Style File

First, create the CSS file at `/tmp/pdf-style.css` with the following content:

```css
body {
    font-family: "Latin Modern Roman", "LM Roman 10", "Computer Modern", "Times New Roman", serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 2em;
    font-size: 11pt;
    line-height: 1.6;
}

h1 {
    font-size: 1.5em;
    font-weight: bold;
    text-align: left;
    margin-bottom: 0.1em;
    font-family: "Latin Modern Roman", "LM Roman 10", "Computer Modern", "Times New Roman", serif;
}

/* Subtitle (h2) immediately after main title: close the gap */
h1 + h2 {
    margin-top: 0.1em;
    margin-bottom: 0.2em;
}

/* Style the author line that comes after h1 */
h1 + p {
    text-align: center;
    font-size: 1em;
    margin-top: 0;
    margin-bottom: 0.2em;
}

/* Style the date line that comes after author */
h1 + p + p {
    text-align: center;
    font-size: 0.95em;
    margin-top: 0;
    margin-bottom: 0.5em;
    font-style: italic;
}

/* Style the horizontal rule after date */
h1 + p + p + hr {
    margin-top: 1em;
    margin-bottom: 1.5em;
}

h2 {
    font-size: 1.3em;
    font-weight: bold;
    margin-top: 1.5em;
    font-family: "Latin Modern Roman", "LM Roman 10", "Computer Modern", "Times New Roman", serif;
}

h3 {
    font-size: 1.1em;
    font-weight: bold;
    font-family: "Latin Modern Roman", "LM Roman 10", "Computer Modern", "Times New Roman", serif;
}

/* Figures: constrain to fit within a single page */
img {
    max-width: 100%;
    max-height: 550px;
    width: auto;
    height: auto;
    display: block;
    margin: 1em auto;
    page-break-inside: avoid;
}

/* Keep figures and their captions together */
p:has(> img) {
    page-break-inside: avoid;
}

table {
    font-size: 0.85em;
    border-collapse: collapse;
    margin: 1em auto;
    width: 100%;
    table-layout: fixed;
}

th, td {
    border: 1px solid #ccc;
    padding: 2px 5px;
    vertical-align: top;
    text-align: left;
    line-height: 1.3;
    overflow-wrap: break-word;
    word-break: normal;
}

th {
    background-color: #f5f5f5;
    font-weight: bold;
}

/* Prevent table rows from breaking across pages */
tr {
    page-break-inside: avoid;
}

/* Keep table headers with the first rows */
thead {
    display: table-header-group;
}

/* Keep section headings with following content */
h2, h3 {
    page-break-after: avoid;
}

/* Keep paper heading + "Paper:" line + table start together */
h3 + p {
    page-break-after: avoid;
}
h3 + p + table {
    page-break-before: avoid;
}

code {
    font-family: "Latin Modern Mono", "LM Mono 10", "Courier New", monospace;
    font-size: 0.9em;
}

/* Hide the document title */
header {
    display: none;
}

.title {
    display: none;
}

/* Links styling */
a {
    color: #1a0dab;
    text-decoration: none;
}

@page {
    margin: 2cm;
    @bottom-center {
        content: "ICLR 2026 Reference Review";
        font-size: 9pt;
        font-family: "Latin Modern Roman", "LM Roman 10", "Times New Roman", serif;
    }
    @bottom-right {
        content: counter(page);
        font-size: 9pt;
        font-family: "Latin Modern Roman", "LM Roman 10", "Times New Roman", serif;
    }
}
```

## Generation Commands

The pipeline is three steps: (1) pandoc converts Markdown → HTML, (2) `scripts/fix_table_widths.py` post-processes the HTML to set correct column widths for each table (Pandoc generates equal-width columns by default, which causes wrapping in narrow columns), (3) WeasyPrint renders HTML → PDF.

### Generate Both at Once

```bash
# Create CSS file (copy content from the CSS Style File section above)
cat > /tmp/pdf-style.css << 'EOF'
[paste CSS content from above]
EOF

# Generate both PDFs
pandoc README.md -o /tmp/iclr_full.html --standalone --self-contained --css=/tmp/pdf-style.css --metadata title="" && \
python scripts/fix_table_widths.py /tmp/iclr_full.html && \
python -c "from weasyprint import HTML; HTML('/tmp/iclr_full.html').write_pdf('pdf/ICLR2026-Accepted-References.pdf')" && \
pandoc README-anonymous.md -o /tmp/iclr_anon.html --standalone --self-contained --css=/tmp/pdf-style.css --metadata title="" && \
python scripts/fix_table_widths.py /tmp/iclr_anon.html && \
python -c "from weasyprint import HTML; HTML('/tmp/iclr_anon.html').write_pdf('pdf/ICLR2026-Accepted-References-Anonymous.pdf')"
```

### Generate ICLR2026-Accepted-References.pdf only

```bash
pandoc README.md -o /tmp/iclr_full.html --standalone --self-contained --css=/tmp/pdf-style.css --metadata title="" && \
python scripts/fix_table_widths.py /tmp/iclr_full.html && \
python -c "from weasyprint import HTML; HTML('/tmp/iclr_full.html').write_pdf('pdf/ICLR2026-Accepted-References.pdf')"
```

### Generate ICLR2026-Accepted-References-Anonymous.pdf only

```bash
pandoc README-anonymous.md -o /tmp/iclr_anon.html --standalone --self-contained --css=/tmp/pdf-style.css --metadata title="" && \
python scripts/fix_table_widths.py /tmp/iclr_anon.html && \
python -c "from weasyprint import HTML; HTML('/tmp/iclr_anon.html').write_pdf('pdf/ICLR2026-Accepted-References-Anonymous.pdf')"
```

## PDF Formatting Features

The generated PDFs include:

- **arXiv-style formatting**: Serif fonts (Computer Modern/Times New Roman), 11pt font, appropriate line spacing
- **Left-aligned title**: Main `h1` heading left-aligned; the `h2` subtitle ("A Full Scan…") immediately follows with minimal vertical gap via the `h1 + h2` CSS rule
- **Author name**: Centered under title (Mark Russinovich for full version, Anonymous for anonymous version)
- **Date**: Centered and italicized under author name
- **Footer**: "ICLR 2026 Reference Review" centered at bottom of each page
- **Page numbers**: Right-aligned at bottom of each page
- **Responsive figures**: Images scale to fit page width while maintaining aspect ratio
- **No document title heading**: The pandoc-generated title element is hidden via CSS (`header { display: none }`)
- **No broken table rows**: `page-break-inside: avoid` on `tr` elements prevents rows from splitting across pages
- **Fixed table column widths**: `table-layout: fixed` is set in CSS; `scripts/fix_table_widths.py` post-processes the HTML to override Pandoc's default equal-width `<col>` elements with the correct proportions for each table (see Table Column Widths below)

## Table Column Widths

Pandoc generates equal-width `<col>` elements for all tables regardless of content. With `table-layout: fixed` this causes narrow columns (like `#` and `Year`) to be wastefully wide and wide columns (like `LLM Judge`) to be too narrow. The `scripts/fix_table_widths.py` script fixes this by identifying each table by its column count and first header text, then rewriting the `<col style="width: X%">` elements before WeasyPrint renders the PDF.

**Why `scripts/fix_table_widths.py` is needed (not just CSS):** CSS `col:nth-child()` selectors cannot distinguish between different tables, so there is no pure-CSS way to apply different widths to the `#` column in reference tables vs. the `Outcome` column in summary tables.

**Current column width assignments** (in `scripts/fix_table_widths.py`):

| Table (identified by col count + first header) | Column widths |
|---|---|
| 5-col `#` — reference tables (# / Cited Title / Fabricated Authors / Year / LLM Judge) | 4% / 22% / 21% / 9% / 44% |
| 6-col `#` — Appendix B table (# / Fabricated Reference / Cited Authors / Year / Citing Paper / Assessment) | 4% / 15% / 14% / 8% / 22% / 37% |
| 3-col `Paper` — top offenders table (Paper / OpenReview / Hallucinated Refs) | 58% / 22% / 20% |
| 3-col `Outcome` — results summary (Outcome / Count / Percent) | 75% / 13% / 12% |
| 3-col `Issue` — metadata quality (Issue / Count / Per Paper (avg)) | 65% / 13% / 22% |
| 2-col `Detail` — scan config (Detail / Value) | 35% / 65% |

**Key constraints these widths satisfy:**
- `Year` column at 9% is wide enough for the "Year" header not to wrap on A4 with 2cm margins
- `Issue` column at 65% is wide enough for "Suboptimal URL (valid but not canonical)" (39 chars) not to wrap
- `Per Paper (avg)` column at 22% is wide enough for that header not to wrap
- `Outcome` column at 75% handles the longest outcome description without wrapping
- `LLM Judge` at 44% gives adequate space for the judge explanations

**If you add a new table to the Markdown**, add a corresponding entry to `COLUMN_WIDTHS` in `scripts/fix_table_widths.py` keyed by `(column_count, first_header_text)`.

## Appendix Content Fidelity

When regenerating `hallucinated_references.json`, `README.md`, `README-anonymous.md`, or the PDF appendices, preserve the full field values exactly as they appear in the source data.

- Never truncate cited paper titles.
- Never truncate cited author lists.
- Never truncate `hallucination_assessment.explanation` / `LLM Judge` text.
- If any appendix field is cut off in a derived artifact, repair it from the latest recheck output or cached LLM response before publishing regenerated READMEs or PDFs.

## Data Files

The repository stores conference input data under `conferences/<conference>/<year>/`.

### Data Files
- **`conferences/iclr/2026/iclr-2026-accepted.txt`** - List of ICLR 2026 accepted paper URLs
- **`conferences/iclr/2025/iclr-2025-accepted.txt`** - List of ICLR 2025 accepted paper URLs
- **`conferences/iclr/2024/iclr-2024-accepted.txt`** - List of ICLR 2024 accepted paper URLs
- **`conferences/iclr/2023/iclr-2023-accepted.txt`** - List of ICLR 2023 accepted paper URLs
- Other conference/year accepted lists follow the same layout, such as `conferences/aistats/2026/` and `conferences/icml/2025/`.

**Structure of `full_results.json`:**
```json
{
    "generated_at": "2026-04-13T05:23:57.704632",
    "summary": { "total_papers": 5348, "total_records": 180501 },
  "papers": {
    "paper_id": {
      "title": "Paper Title",
      "authors": "Author List",
      "year": 2025,
      "url": "https://openreview.net/...",
      "stats": { ... },
      "references": [ ... ]
    }
  }
}
```

## Markdown Files

- **`README.md`** - Full version with author name, all examples, and appendices
- **`README-anonymous.md`** - Anonymous version without specific paper mentions, author names, or appendices (suitable for blind review submissions)

## Troubleshooting

- If you get "xelatex not found" errors, use the pandoc → HTML → weasyprint → PDF pipeline shown above (not pandoc direct to PDF)
- If weasyprint is not installed: `pip install weasyprint`
- If beautifulsoup4 is not installed: `pip install beautifulsoup4`
- The CSS file is written to `/tmp/pdf-style.css` to avoid cluttering the repository; you can use any path as long as the `--css` argument matches
- If tables look wrong (columns too wide/narrow), check that `scripts/fix_table_widths.py` was run on the HTML before WeasyPrint; also verify the table's first header text matches an entry in `COLUMN_WIDTHS`
