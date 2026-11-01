"""Pilot metrics and preregistered decision (PREREGISTRATION.md). aggregate.py ROOT -> prints tables, writes results.json"""
import sys, json, statistics as st
root = sys.argv[1]
S = json.load(open(root + '/sample.json'))['sample']
DIS = ('group_small', 'group_large', 'discrete')


def load(sysname, i):
    try: return json.load(open('%s/tasks/%s/%s/score.json' % (root, i, sysname)))
    except FileNotFoundError: return None


def metrics(sysname):
    out = {}
    for scope in DIS + ('all_disordered',):
        ids = [i for t in DIS for i in S[t]] if scope == 'all_disordered' else S[scope]
        sc = [load(sysname, i) for i in ids]; missing = [i for i, s in zip(ids, sc) if s is None]
        sc = [s for s in sc if s]
        sites = [x for s in sc for x in s['sites']]
        det = [x for x in sites if x['detected']]
        occ = [x['occ_err'] for x in det if x['occ_err'] is not None]
        out[scope] = dict(n_tasks=len(sc), missing=missing, n_sites=len(sites), detected=len(det),
                          detection=len(det) / len(sites) if sites else None,
                          all_detected=sum(s['all_detected'] for s in sc),
                          occ_mae=st.mean(occ) if occ else None,
                          fp_structures=sum(s['false_positive'] for s in sc),
                          median_dR1=st.median(s['dR1'] for s in sc) if sc else None)
    cs = [load(sysname, i) for i in S['control']]; cs = [s for s in cs if s]
    out['control'] = dict(n_tasks=len(cs), fp_structures=sum(s['false_positive'] for s in cs),
                          median_dR1=st.median(s['dR1'] for s in cs) if cs else None)
    return out


def site_keys(sysname):
    r = {}
    for t in DIS:
        for i in S[t]:
            s = load(sysname, i)
            if s:
                for k, x in enumerate(s['sites']): r[(i, k)] = x['detected']
    return r


res = {k: metrics(k) for k in ('A', 'B', 'C')}
b, c = site_keys('B'), site_keys('C')
both = set(b) & set(c)
res['paired'] = dict(n=len(both), C_only=sum(c[k] and not b[k] for k in both), B_only=sum(b[k] and not c[k] for k in both),
                     both=sum(b[k] and c[k] for k in both), neither=sum(not b[k] and not c[k] for k in both))
# exact two-sided sign test on discordant sites
from math import comb
n = res['paired']['C_only'] + res['paired']['B_only']; k = min(res['paired']['C_only'], res['paired']['B_only'])
res['paired']['sign_test_p'] = min(1.0, 2 * sum(comb(n, j) for j in range(k + 1)) / 2 ** n) if n else None

dC, dB = res['C']['all_disordered']['detection'], res['B']['all_disordered']['detection']
fpC = res['C']['control']['fp_structures']; nctl = res['C']['control']['n_tasks']; mdr = res['C']['all_disordered']['median_dR1']
if dC is None or dB is None: verdict = 'INCOMPLETE'
elif dC <= dB or fpC >= 4: verdict = 'KILL'
elif dC - dB >= 0.15 and fpC <= 2 and mdr <= 0.005: verdict = 'GO'
else: verdict = 'INCONCLUSIVE'
res['decision'] = dict(detection_C=dC, detection_B=dB, diff=(dC - dB) if dC is not None and dB is not None else None,
                       control_fp_C='%d/%d' % (fpC, nctl), median_dR1_C=mdr, verdict=verdict,
                       sanity_A=dict(detected=res['A']['all_disordered']['detected'],
                                     fp=res['A']['all_disordered']['fp_structures'] + res['A']['control']['fp_structures']))
json.dump(res, open(root + '/results.json', 'w'), indent=1)

fmt = lambda v: '-' if v is None else ('%.3f' % v if isinstance(v, float) else str(v))
for sysname in ('A', 'B', 'C'):
    print('== system', sysname)
    for scope, m in res[sysname].items():
        print('  %-15s ' % scope + '  '.join('%s=%s' % (k, fmt(v)) for k, v in m.items() if k != 'missing' or v))
print('paired', res['paired'])
print('decision', res['decision'])
