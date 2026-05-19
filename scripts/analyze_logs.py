import re, glob, os, subprocess

def parse_log(path):
    try:
        with open(path, 'r', errors='ignore') as f:
            content = f.read()
    except: return None

    papers_list = re.findall(r'Papers processed:\s+(\d+)', content)
    refs_list = re.findall(r'References processed:\s+(\d+)', content)
    # Search for lines like 'real 1234.56' or 'real 12m34.567s'
    reals = re.findall(r'real\s+([0-9mhsm. ]+)', content)

    if not papers_list or not reals:
        return None

    p = int(papers_list[-1])
    # Total references processed:
    r_matches = re.findall(r'References processed:\s+(\d+)', content)
    r = int(r_matches[-1]) if r_matches else 0
    t_str = reals[-1].strip()

    seconds = 0
    if 'm' in t_str:
        m_match = re.search(r'(\d+)m', t_str)
        s_match = re.search(r'([\d.]+)s', t_str)
        if m_match: seconds += float(m_match.group(1)) * 60
        if s_match: seconds += float(s_match.group(1))
    else:
        try: seconds = float(t_str)
        except: return None

    return {'p': p, 'r': r, 's': seconds}

logs = glob.glob('_workspace/*/logs/run*.log')
results = []
for l in logs:
    res = parse_log(l)
    if res:
        res['name'] = '/'.join(l.split('/')[-3:])
        results.append(res)

# Current NeurIPS 2025 calculation
try:
    with open("_workspace/neurips2025/results/scan_report.checkpoint.jsonl", 'rb') as f:
        cp_count = sum(1 for _ in f)
    papers_now = cp_count - 1699
    # Read refs from checkpoint lines
    # (Simplified: just estimate or use 0 if too slow to parse)
    out = subprocess.check_output(["ps", "-p", "1668223", "-o", "times="], stderr=subprocess.DEVNULL).decode().strip()
    elapsed = int(out)
    if papers_now > 0 and elapsed > 0:
        results.append({'name': 'neurips2025/CURRENT', 'p': papers_now, 'r': 0, 's': elapsed, 'is_curr': True})
except: pass

print(f"{'Run Name':<45} | {'Paps':>5} | {'P/hr':>7} | {'S/Pap':>6} | {'R/hr':>7}")
print("-" * 80)
final = []
for r in results:
    ph = r['p'] / (r['s']/3600)
    sp = r['s'] / r['p']
    rh = r['r'] / (r['s']/3600)
    final.append((ph, r, sp, rh))

for ph, r, sp, rh in sorted(final, key=lambda x: x[0], reverse=True):
    mark = "*" if r.get('is_curr') else " "
    name = r['name'][-44:]
    print(f"{mark}{name:44} | {r['p']:5d} | {ph:7.1f} | {sp:6.1f} | {rh:7.1f}")
