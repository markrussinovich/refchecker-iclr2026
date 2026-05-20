import json
import collections

def analyze_json(path, year):
    with open(path, 'r') as f:
        data = json.load(f)
    
    summary = data.get('summary', {})
    papers = data.get('papers', [])
    
    print(f"\n--- Analysis for {year} ---")
    print(f"Summary: {summary}")
    
    flagged_counts = []
    likely_counts = []
    total_refs = summary.get('total_references_processed', 0)
    
    total_used_regex = 0
    total_used_unreliable = 0

    for p in papers:
        # Check extraction flags in flags list if available, or paper level
        # Based on typical schema, extraction flags might be in each reference or summary.
        # Let's check a few papers for these flags.
        p_flagged = p.get('flagged_records', 0)
        flagged_counts.append(p_flagged)
        
        # Calculate likely hallucinated per paper
        p_likely = 0
        for ref in p.get('references', []):
            if ref.get('verdict') == 'LIKELY':
                p_likely += 1
            if ref.get('used_regex_extraction'):
                total_used_regex += 1
            if ref.get('used_unreliable_extraction'):
                total_used_unreliable += 1
        likely_counts.append(p_likely)

    dist = collections.Counter(flagged_counts)
    print(f"Distribution of flagged_records per paper: {dict(sorted(dict(dist).items()))}")
    
    n = len(papers)
    for i in [1, 2, 3]:
        count = sum(1 for c in flagged_counts if c >= i)
        print(f"Papers with >= {i} flags: {count} ({count/n*100:.2f}%)")
        
    print(f"Total refs: {total_refs}")
    total_flags = sum(flagged_counts)
    print(f"Flagged/ref rate: {total_flags/total_refs*100:.2f}% ({total_flags}/{total_refs})")
    
    print(f"Extraction flags: used_regex_extraction={total_used_regex}, used_unreliable_extraction={total_used_unreliable}")

    # Top 20 papers by LIKELY count or flag count
    paper_stats = []
    for p, likely, flagged in zip(papers, likely_counts, flagged_counts):
        paper_stats.append({
            'title': p.get('source_title'),
            'likely': likely,
            'flagged': flagged
        })
    
    top_20 = sorted(paper_stats, key=lambda x: (x['likely'], x['flagged']), reverse=True)[:20]
    print("\nTop 20 papers by LIKELY/flag count:")
    for i, p in enumerate(top_20, 1):
        print(f"{i}. {p['title']}: LIKELY={p['likely']}, Flagged={p['flagged']}")

def analyze_checkpoint(path, year):
    print(f"\n--- Checkpoint Analysis for {year} ---")
    assessed_refs = 0
    verdicts = collections.Counter()
    
    try:
        with open(path, 'r') as f:
            for line in f:
                record = json.loads(line)
                if 'verdict' in record:
                    assessed_refs += 1
                    verdicts[record['verdict']] += 1
        
        print(f"Assessed refs: {assessed_refs}")
        for v in ['LIKELY', 'UNLIKELY', 'UNCERTAIN']:
            print(f"{v}: {verdicts[v]}")
        
        # Since we don't have total_refs here easily, we'll wait for the json info if possible
        # but can show ratios relative to assessed.
        if assessed_refs > 0:
            print(f"Likely/assessed: {verdicts['LIKELY']/assessed_refs*100:.2f}%")
    except FileNotFoundError:
        print("Checkpoint file not found.")

def main():
    paths = {
        '2024': {
            'json': '_workspace/usenix-security2024/results/scan_report.json',
            'checkpoint': '_workspace/usenix-security2024/results/scan_report.checkpoint.jsonl'
        },
        '2025': {
            'json': '_workspace/usenix-security2025/results/scan_report.json',
            'checkpoint': '_workspace/usenix-security2025/results/scan_report.checkpoint.jsonl'
        }
    }
    
    for year in ['2024', '2025']:
        analyze_json(paths[year]['json'], year)
        analyze_checkpoint(paths[year]['checkpoint'], year)

if __name__ == "__main__":
    main()
