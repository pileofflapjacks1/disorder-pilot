"""Exploratory (not preregistered): chance of GO / INCONCLUSIVE / KILL for round 2, before spending on C.

power_r2.py ROOT [SIMS]   prints a table and writes power_r2.json

Fixed: B's actual round-2 site outcomes on the first n tasks per type (B is the best baseline at every n).
Simulated: C, from pilot data only, with parameter uncertainty (a fresh Beta draw per simulation, uniform prior):
  - 'transfer'   C's pilot detection rate conditional on B: P(C | B detected) from 6/9, P(C | B missed) from 14/27.
                 Assumes C keeps its pilot advantage where B fails, so C gains when tasks get easier for B.
  - 'fixed'      C detects each site at its pilot rate (20/36) regardless of B: the agent does not get better
                 on easier tasks. Pessimistic.
  - control FPs  C's pilot rate, 3/10. All three were adjudicated 'unsure' or 'overfit', so none would be excused
                 under D2 option a; on pilot evidence, options a and b give the same result.
  - median dR1   bootstrap of C's 29 pilot disordered-task dR1 values.
Task handling (the rule suggested for the pre-C amendment): 2240538 and 2241940 dropped for every system; B's
crash on 2243293 counts as zero detections. Sites are treated as independent (sites in one task are not).
"""
import sys, json, random, statistics as st
from math import comb
root = sys.argv[1]; SIMS = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
S = json.load(open(root + '/sample_r2.json'))['sample']; DIS = ('group_small', 'group_large', 'discrete')
DROP = {'2240538', '2241940'}
pilot = json.load(open(root + '/sample.json'))['sample']
c_dr1 = [json.load(open('%s/tasks/%s/C/score.json' % (root, i)))['dR1'] for t in DIS for i in pilot[t]]


def b_sites(n):
    out = []
    for t in DIS:
        for i in S[t][:n]:
            if i in DROP: continue
            sc = json.load(open('%s/tasks/%s/B/score.json' % (root, i)))
            if 'error' in sc: out += [False] * len(json.load(open('%s/tasks/%s/truth.json' % (root, i)))['sites'])
            else: out += [x['detected'] for x in sc['sites']]
    return out, sum(1 for t in DIS for i in S[t][:n] if i not in DROP)


def sign_p(k, m):
    return sum(comb(k + m, j) for j in range(k, k + m + 1)) / 2 ** (k + m) if k + m else 1.0


def sim(n, scen, rng):
    b, ntask = b_sites(n); res = dict(GO=0, INCONCLUSIVE=0, KILL=0); diffs = []
    for _ in range(SIMS):
        if scen == 'transfer': p1, p0 = rng.betavariate(7, 4), rng.betavariate(15, 14)
        else: p1 = p0 = rng.betavariate(21, 17)
        c = [rng.random() < (p1 if x else p0) for x in b]
        diff = (sum(c) - sum(b)) / len(b); diffs.append(diff)
        p = sign_p(sum(x and not y for x, y in zip(c, b)), sum(y and not x for x, y in zip(c, b)))
        q = rng.betavariate(4, 8); fp = sum(rng.random() < q for _ in range(n)) / n
        med = st.median(rng.choice(c_dr1) for _ in range(ntask))
        go = diff >= 0.15 and p < 0.05 and fp <= 0.20 and med <= 0.005
        res['GO' if go else 'KILL' if diff <= 0 or fp >= 0.40 else 'INCONCLUSIVE'] += 1
    out = {k: v / SIMS for k, v in res.items()}
    out.update(B_rate=sum(b) / len(b), n_sites=len(b), GO_needs_C=sum(b) / len(b) + 0.15,
               median_diff=st.median(diffs), p_detection_bar=sum(d >= 0.15 for d in diffs) / SIMS)
    return out


if __name__ == '__main__':
    rng = random.Random(20261109); R = {}
    print('%-9s %3s %6s %7s %9s %7s %6s %6s %6s' % ('scenario', 'n', 'sites', 'B rate', 'C needs', 'P(det)', 'GO', 'INC', 'KILL'))
    for scen in ('transfer', 'fixed'):
        for n in (10, 15, 20):
            r = sim(n, scen, rng); R['%s_n%d' % (scen, n)] = r
            print('%-9s %3d %6d %7.3f %9.3f %7.2f %6.2f %6.2f %6.2f' % (scen, n, r['n_sites'], r['B_rate'], r['GO_needs_C'],
                  r['p_detection_bar'], r['GO'], r['INCONCLUSIVE'], r['KILL']))
    json.dump(R, open(root + '/power_r2.json', 'w'), indent=1)
