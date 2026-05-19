import json
import os
import pandas as pd
from collections import Counter

reports = {
    "ICLR 2024": "_workspace/iclr2024/results/scan_report.json",
    "ICML 2024": "_workspace/icml2024/results/scan_report.json",
    "ICLR 2025": "_workspace/iclr2025/results/scan_report.json",
    "ICML 2025": "_workspace/icml2025/results/scan_report.json",
    "ICLR 2021": "_workspace/iclr2021/results/scan_report.json",
    "ICML 2021": "_workspace/icml2021/results/scan_report.json"
}

all_stats = []
paper_stats = {}

for conf, path in reports.items():
    if not os.path.exists(path): continue
    with open(path, 'r') as f:
        data = json.load(f)

    summary = data.get("summary", {})
    papers = data.get("papers", [])

    total_papers = summary.get("total_papers_processed", len(papers))
    total_refs = summary.get("total_references_processed", 0)
    records_written = summary.get("records_written", 0)

    flagged_refs_total = summary.get("flagged_records", 0)
    papers_with_flagged = []

    total_reason_counts = Counter()
    total_error_counts = Counter()

    for p in papers:
        flagged = p.get("flagged_records", 0)
        if flagged > 0:
            papers_with_flagged.append(flagged)

        # Aggregate from paper-level summaries
        for r, count in p.get("reason_counts", {}).items():
            total_reason_counts[r] += count
        for et, count in p.get("error_type_counts", {}).items():
            total_error_counts[et] += count

    stats = {
        "Conf": conf,
        "Papers": total_papers,
        "Refs": total_refs,
        "Refs/P": total_refs / total_papers if total_papers else 0,
        "RecW/Refs": records_written / total_refs if total_refs else 0,
        "Likely Refs": flagged_refs_total,
        "Likely Rate (%)": (flagged_refs_total / total_refs * 100) if total_refs else 0,
        "Likely P": len(papers_with_flagged),
        "P>=1 (%)": (len(papers_with_flagged) / total_papers * 100) if total_papers else 0,
        "P>=2": sum(1 for x in papers_with_flagged if x >= 2),
        "P>=3": sum(1 for x in papers_with_flagged if x >= 3),
    }
    all_stats.append(stats)
    paper_stats[conf] = papers_with_flagged

    print(f"\n--- {conf} ---")
    print(f"Likely per paper dist: {dict(sorted(Counter(papers_with_flagged).items()))}")
    print(f"Top Reasons: {dict(total_reason_counts)}")
    # Simplified reasoning bucket check
    buckets = Counter()
    for r, count in total_reason_counts.items():
        rk = "other"
        rl = r.lower()
        if any(x in rl for x in ["unverified", "not_found", "no_match"]): rk = "unverified/not found"
        elif "author" in rl: rk = "author metadata"
        elif "title" in rl: rk = "title/metadata"
        elif "year" in rl: rk = "year/metadata"
        buckets[rk] += count
    print(f"Reason Buckets: {dict(buckets)}")

df = pd.DataFrame(all_stats)
print("\nSummary Table:")
cols = ["Conf", "Papers", "Refs", "Refs/P", "RecW/Refs", "Likely Refs", "Likely Rate (%)", "Likely P", "P>=1 (%)", "P>=2", "P>=3"]
print(df[cols].to_string(index=False))

if "ICLR 2025" in paper_stats and "ICML 2025" in paper_stats:
    print("\n--- ICLR 2025 vs ICML 2025 Threshold Gap Analysis ---")
    for c in ["ICLR 2025", "ICML 2025"]:
        dist = Counter(paper_stats[c])
        total = next(s["Papers"] for s in all_stats if s["Conf"] == c)
        p2_total = sum(v for k,v in dist.items() if k >= 2)
        print(f"{c}: Total P>=2: {p2_total} ({p2_total/total*100:.2f}%)")
        print(f"  Exact 2: {dist[2]} ({dist[2]/total*100:.2f}%)")
        print(f"  Exact 3+: {sum(v for k,v in dist.items() if k >= 3)} ({sum(v for k,v in dist.items() if k >= 3)/total*100:.2f}%)")
