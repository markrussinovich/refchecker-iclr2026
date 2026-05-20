import json
import math

def load_data(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def analyze_year(data, exclude_url=None):
    # data is a dict with 'papers' key which contains paper details
    papers_list = []
    # If standard scan_report.json structure: { "papers": [ { "url": ..., "references": [...] }, ... ] }
    all_papers = data.get('papers', [])
    
    all_refs_count = 0
    total_likely = 0
    papers_ge_1 = 0
    papers_ge_2 = 0
    papers_ge_3 = 0
    likely_counts = []
    refs_per_paper = []
    error_types = {}
    assessed_refs = 0

    for paper_data in all_papers:
        paper_url = paper_data.get('url', '')
        if exclude_url and (exclude_url in paper_url):
            continue
        
        refs = paper_data.get('references', [])
        num_refs = len(refs)
        refs_per_paper.append(num_refs)
        all_refs_count += num_refs
        
        likely_in_paper = 0
        for ref in refs:
            # Check likely_hallucinated or flags
            is_likely = ref.get('likely_hallucinated', False)
            if is_likely:
                likely_in_paper += 1
                et = ref.get('error_type', 'Unknown')
                error_types[et] = error_types.get(et, 0) + 1
            
            verdict = ref.get('verdict')
            if verdict is not None:
                assessed_refs += 1

        likely_counts.append(likely_in_paper)
        total_likely += likely_in_paper
        if likely_in_paper >= 1: papers_ge_1 += 1
        if likely_in_paper >= 2: papers_ge_2 += 1
        if likely_in_paper >= 3: papers_ge_3 += 1
        
        papers_list.append({
            'url': paper_url,
            'likely_count': likely_in_paper,
            'refs': num_refs
        })

    num_papers = len(papers_list)
    dist = {}
    for c in likely_counts:
        dist[c] = dist.get(c, 0) + 1
    
    top_10 = sorted(papers_list, key=lambda x: x['likely_count'], reverse=True)[:10]

    mean_refs = sum(refs_per_paper) / num_papers if num_papers > 0 else 0
    sorted_refs = sorted(refs_per_paper)
    mid = num_papers // 2
    if num_papers == 0:
        median_refs = 0
    elif num_papers % 2 != 0:
        median_refs = sorted_refs[mid]
    else:
        median_refs = (sorted_refs[mid-1] + sorted_refs[mid]) / 2

    return {
        'num_papers': num_papers,
        'total_refs': all_refs_count,
        'total_likely': total_likely,
        'papers_ge_1': papers_ge_1,
        'papers_ge_2': papers_ge_2,
        'papers_ge_3': papers_ge_3,
        'dist': dist,
        'mean_refs': mean_refs,
        'median_refs': median_refs,
        'assessed_refs': assessed_refs,
        'likely_rate': total_likely / assessed_refs if assessed_refs > 0 else 0,
        'error_types': error_types,
        'top_10': top_10
    }

def prop_diff_ci(p1, n1, p2, n2):
    diff = p1 - p2
    # Guard against p=0 or p=1
    se = math.sqrt(max(0, p1*(1-p1)/n1 + p2*(1-p2)/n2))
    z = 1.96 
    return diff, se, (diff - z*se, diff + z*se)

data24 = load_data('_workspace/usenix-security2024/results/scan_report.json')
data25 = load_data('_workspace/usenix-security2025/results/scan_report.json')

res24 = analyze_year(data24)
res25 = analyze_year(data25)
res24_excl = analyze_year(data24, exclude_url='usenixsecurity24-thompson')

print("--- USENIX Security 2024 ---")
for k in ['num_papers', 'total_refs', 'total_likely', 'papers_ge_1', 'papers_ge_2', 'papers_ge_3', 'mean_refs', 'median_refs', 'assessed_refs', 'likely_rate']:
    print(f"{k}: {res24[k]}")
print(f"Distribution: {dict(sorted(res24['dist'].items()))}")
print("Error Types:", res24['error_types'])
print("Top 10 Papers:")
for p in res24['top_10']: print(f"  {p['likely_count']} - {p['url']}")

print("\n--- USENIX Security 2025 ---")
for k in ['num_papers', 'total_refs', 'total_likely', 'papers_ge_1', 'papers_ge_2', 'papers_ge_3', 'mean_refs', 'median_refs', 'assessed_refs', 'likely_rate']:
    print(f"{k}: {res25[k]}")
print(f"Distribution: {dict(sorted(res25['dist'].items()))}")
print("Error Types:", res25['error_types'])
print("Top 10 Papers:")
for p in res25['top_10']: print(f"  {p['likely_count']} - {p['url']}")

print("\n--- 2024 EXCLUDING USENIXSECURITY24-THOMPSON ---")
for k in ['num_papers', 'total_refs', 'total_likely', 'likely_rate']:
    print(f"{k}: {res24_excl[k]}")

print("\n--- Comparison (2024 - 2025) ---")
r24_ge2 = res24['papers_ge_2'] / res24['num_papers']
r25_ge2 = res25['papers_ge_2'] / res25['num_papers']
diff_ge2, se_ge2, ci_ge2 = prop_diff_ci(r24_ge2, res24['num_papers'], r25_ge2, res25['num_papers'])
print(f"Diff papers >= 2: {diff_ge2:.4f} (SE: {se_ge2:.4f}, 95% CI: [{ci_ge2[0]:.4f}, {ci_ge2[1]:.4f}])")

diff_lr, se_lr, ci_lr = prop_diff_ci(res24['likely_rate'], res24['assessed_refs'], res25['likely_rate'], res25['assessed_refs'])
print(f"Diff likely ref rate: {diff_lr:.4f} (SE: {se_lr:.4f}, 95% CI: [{ci_lr[0]:.4f}, {ci_lr[1]:.4f}])")
