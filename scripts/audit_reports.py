import json
import os
from collections import Counter

def audit_report(report_path, conf_name):
    print(f"--- Auditing {conf_name} ({report_path}) ---")
    if not os.path.exists(report_path):
        print(f"File {report_path} not found.")
        return

    with open(report_path, 'r') as f:
        data = json.load(f)

    summary = data.get('summary', {})
    print(f"Summary Fields:")
    for field in ['total_papers_processed', 'total_references_processed', 'flagged_records', 'flagged_papers', 'records_written']:
        print(f"  {field}: {summary.get(field)}")

    records = data.get('records', [])
    print(f"Actual records loaded: {len(records)}")

    paper_hallucination_counts = Counter()
    missing_assessment = 0
    hallucinated_records = []

    for rec in records:
        # Based on inspection, hallucinated records have 'is_likely_hallucination': True
        # Or alternatively error_type == 'hallucination'
        if rec.get('is_likely_hallucination') or rec.get('error_type') == 'hallucination':
            hallucinated_records.append(rec)
            p_id = rec.get('source_paper_id')
            paper_hallucination_counts[p_id] += 1

            # Assessment field in this schema
            assessment = rec.get('error_details') or rec.get('hallucination_explanation')
            if not assessment:
                 missing_assessment += 1

    p1 = sum(1 for c in paper_hallucination_counts.values() if c >= 1)
    p2 = sum(1 for c in paper_hallucination_counts.values() if c >= 2)
    p3 = sum(1 for c in paper_hallucination_counts.values() if c >= 3)

    print(f"Recomputed Paper Counts (Hallucinated):")
    print(f"  Papers with >=1 flags: {p1}")
    print(f"  Papers with >=2 flags: {p2}")
    print(f"  Papers with >=3 flags: {p3}")

    ref_total = summary.get('total_references_processed', 0)
    hallucination_rate = (len(hallucinated_records) / ref_total * 100) if ref_total > 0 else 0
    print(f"Recomputed Reference Hallucination Rate: {hallucination_rate:.2f}% (Found {len(hallucinated_records)} hallucinated records)")

    dist = Counter(paper_hallucination_counts.values())
    print(f"Distribution of flags per paper:")
    for k in sorted(dist.keys()):
        print(f"  {k}: {dist[k]}")

    print(f"Hallucinated records with missing/invalid assessment: {missing_assessment}")

    # Sample 8 records
    print(f"\nSample of 8 Hallucinated Records:")
    sorted_records = sorted(hallucinated_records, key=lambda x: (str(x.get('source_paper_id')), str(x.get('ref_title'))))
    for rec in sorted_records[:8]:
        p_id = rec.get('source_paper_id')
        p_title = rec.get('source_title', 'N/A')
        ref_title = rec.get('ref_title', 'N/A')
        year = rec.get('ref_year_cited', 'N/A')
        assessment = rec.get('error_details') or rec.get('hallucination_explanation') or ""
        print(f"  ID: {p_id} | Paper: {p_title[:40]}...")
        print(f"  Ref: {ref_title[:40]}... ({year})")
        print(f"  Note: {str(assessment)[:180]}...")
        print("-" * 20)
    print("\n" + "="*50 + "\n")

audit_report('_workspace/iclr2025/results/scan_report.json', 'ICLR 2025')
audit_report('_workspace/icml2025/results/scan_report.json', 'ICML 2025')
