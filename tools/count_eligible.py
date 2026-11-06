"""Round-2 eligibility count (read-only; select.py is frozen for the pilot and is not changed).
count_eligible.py ROOT POOL LOG   same rule as select.py: |ref R1 - deposited R1| <= 0.010, A dR1 >= 0.002,
an ERROR or Timeout in LOG is ineligible."""
import sys, os, json, collections
root, pool, log = sys.argv[1], sys.argv[2], sys.argv[3]
pool = json.load(open(root + '/' + pool)); errs = {l.split()[0] for l in open(root + '/' + log) if ' ERROR ' in l}
c = collections.defaultdict(collections.Counter); elig = collections.defaultdict(list)
for i, t in sorted(pool.items()):
    d = root + '/tasks/' + i
    if not os.path.exists(d + '/ref.json') or (t != 'subst' and t != 'group_small' and not os.path.exists(d + '/A/stats.json')):
        c[t]['error' if i in errs else 'not run'] += 1; continue
    ref = json.load(open(d + '/ref.json')); dep = float(str(json.load(open(d + '/truth.json'))['deposited_R1']).split('(')[0])
    if abs(ref['R1'] - dep) > 0.010: c[t]['R1 mismatch'] += 1; continue
    a = json.load(open(d + '/A/stats.json'))
    if a['R1'] - ref['R1'] < 0.002: c[t]['low signal'] += 1; continue
    c[t]['eligible'] += 1; elig[t].append(i)
for t in c: print(t, dict(c[t]))
json.dump(elig, open(root + '/eligible_%s.json' % os.path.splitext(os.path.basename(sys.argv[2]))[0].replace('pool_', ''), 'w'), indent=1)
