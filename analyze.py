import json
import os
import sys
from collections import Counter

def get_stats(workspace):
    report_path = os.path.join("_workspace", workspace, "results", "scan_report.json")
    checkpoint_path = os.path.join("_workspace", workspace, "results", "scan_report.checkpoint.jsonl")
    
    if not os.path.exists(report_path):
        print(f"Report not found: {report_path}")
        return None

    with open(report_path, 'r') as f:
        report = json.load(f)

    summary = report.get('summary', {})
    papers_total = summary.get('total_papers_processed', 0)
    refs_total = summary.get('total_references_processed', 0)
    likely_flags = summary.get('flagged_records', 0)
    ref_flag_rate = (likely_flags / refs_total * 100) if refs_total > 0 else 0
    
    papers_list = report.get('papers', [])
    flagged_counts = [p.get('flagged_records', 0) for p in papers_list]
    
    num_papers_in_list = len(flagged_counts)
    if num_papers_in_list < papers_total:
        flagged_counts.extend([0] * (papers_total - num_papers_in_list))
    
    c = Counter(flagged_counts)
    d0 = c[0]
    d1 = c[1]
    d2 = c[2]
    d34 = c[3] + c[4]
    d5plus = sum(count for val, count in c.items() if val >= 5)
    
    ge2_papers = d2 + d34 + d5plus
    ge2_paper_rate = (ge2_papers / papers_total * 100) if papers_total > 0 else 0

    assessed_refs = 0
    likely_verdicts = 0
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    # The checkpoint might have 'references' or similar. 
                    # If this line was a failed one (fatal_error: true), we skip it.
                    if data.get('fatal_error'):
                         continue
                         
                    # The actual data is usually under some key. Let's look for any 'verdict'
                    # Actually, in some versions of the code, reports are saved Paper objects or similar.
                    # Based on standard structure:
                    for ref in data.get('processed_references', data.get('references', [])):
                        ha = ref.get('hallucination_assessment', {})
                        # Also check if it's nested or direct
                        verdict = ha.get('verdict')
                        if verdict:
                            assessed_refs += 1
                            if verdict == "likely":
                                likely_verdicts += 1
                except:
                    continue
                        
    assessed_ref_pct = (assessed_refs / refs_total * 100) if refs_total > 0 else 0
    likely_assessed_pct = (likely_verdicts / assessed_refs * 100) if assessed_refs > 0 else 0
    
    return {
        'papers': papers_total,
        'refs': refs_total,
        'likely_flags': likely_flags,
        'ref_flag_rate': ref_flag_rate,
        'ge2_papers': ge2_papers,
        'ge2_paper_rate': ge2_paper_rate,
        'assessed_refs': assessed_refs,
        'assessed_ref_pct': assessed_ref_pct,
        'likely_verdicts': likely_verdicts,
        'likely_assessed_pct': likely_assessed_pct,
        'dist': (d0, d1, d2, d34, d5plus)
    }

venues = [
    ('icml2024', 'icml2025'),
    ('neurips2024', 'neurips2025'),
    ('usenix-security2024', 'usenix-security2025')
]

all_stats = {}
for pair in venues:
    for v in pair:
        all_stats[v] = get_stats(v)

def print_stat(name, s):
    if not s:
        print(f"{name}: Missing report file")
        return
    print(f"{name}:")
    print(f"  Papers: {s['papers']}, Refs: {s['refs']}")
    print(f"  Likely Flags (Summary): {s['likely_flags']}, Ref Rate: {s['ref_flag_rate']:.2f}%")
    print(f"  Papers >=2: {s['ge2_papers']}, Ge2 Paper Rate: {s['ge2_paper_rate']:.2f}%")
    print(f"  Assessed Refs: {s['assessed_refs']} ({s['assessed_ref_pct']:.2f}% of total)")
    print(f"  Likely Verdicts (Checkpoint): {s['likely_verdicts']}, Likely/Assessed: {s['likely_assessed_pct']:.2f}%")
    print(f"  Distribution (0, 1, 2, 3-4, 5+): {s['dist']}")

for v24, v25 in venues:
    print_stat(v24, all_stats[v24])
    print_stat(v25, all_stats[v25])
    
    s24, s25 = all_stats[v24], all_stats[v25]
    if s24 and s25:
        print(f"Deltas {v24} -> {v25}:")
        d_papers = s25['papers'] - s24['papers']
        d_refs = s25['refs'] - s24['refs']
        d_flags = s25['likely_flags'] - s24['likely_flags']
        d_rate = s25['ref_flag_rate'] - s24['ref_flag_rate']
        d_ge2 = s25['ge2_papers'] - s24['ge2_papers']
        d_ge2_rate = s25['ge2_paper_rate'] - s24['ge2_paper_rate']
        print(f"  Papers: {d_papers:+}, Refs: {d_refs:+}")
        print(f"  Likely Flags: {d_flags:+}, Rate: {d_rate:+.2f}%")
        print(f"  Papers >=2: {d_ge2:+}, Rate: {d_ge2_rate:+.2f}%")
    print("-" * 40)
