"""Calibrate B2's acceptance gates (post hoc, 2026-11-06).

Positives: the minor parts of the deposited (expert) disorder models, read as published from tasks/<id>/truth.res
  (no re-refinement, so stripped restraints cannot distort them). Only pilot tasks that can never enter round 2
  are used: the pilot sample and dev tasks, and the pilot's ineligible and low-signal tasks (sample.json).
Negatives: the candidate splits the expert judged `overfit` in the blinded adjudication (adjudication/decisions.csv).

calibrate_gates.py ROOT   writes calibration/gates_features.json and prints pass rates over a threshold grid.
"""
import sys, os, io, json, csv, statistics, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
import evidence as E
from cctbx import xray

root = sys.argv[1]
TOLS = (0.10, 0.15, 0.20, 0.25, 0.30)


def features(text, minor, major):
    m = X.Model(text); xs = xray.structure.from_shelx(file=io.StringIO(text)); uc = xs.unit_cell()
    med = statistics.median(X.ueq_and_axes(uc, a)[0] for a in m.heavy()); npd = set(X.npd_atoms(m, uc))
    at = {a['label']: a for a in m.heavy()}; mi = [at[l] for l in minor if l in at]
    f = dict(n_minor=len(mi), min_occ=min(a['occ'] for a in mi), npd=any(a['label'] in npd for a in mi),
             max_ueq_ratio=max(X.ueq_and_axes(uc, a)[0] / med for a in mi),
             min_ueq=min(X.ueq_and_axes(uc, a)[0] for a in mi), geom={})
    for t in TOLS:
        E.BOND_DEV_PARTNER = t; E.BOND_DEV_COV = t + 0.15
        bonds, _ = E.geometry(m, xs, set(minor) | set(major))
        mb = [b for b in bonds if b['a'] in minor and 'rigid-bond' not in b.get('flag', '')]
        f['geom'][str(t)] = round(sum('flag' in b for b in mb) / len(mb), 3) if mb else 0.0
    E.BOND_DEV_PARTNER, E.BOND_DEV_COV = 0.10, 0.25
    return f


if __name__ == '__main__':
    s = json.load(open(root + '/sample.json'))
    ids = sorted(set(i for k in ('sample', 'dev', 'ineligible', 'low_signal') for t, v in s[k].items() if t != 'control' for i in v))
    pos = []
    for i in ids:
        d = root + '/tasks/' + i; info = json.load(open(d + '/truth.json')); text = open(d + '/truth.res').read()
        for k, site in enumerate(info['sites']):
            try: pos.append(dict(id=i, site=k, type=site['type'], **features(text, site['minor'], site['major'])))
            except Exception as e: print('skip', i, k, type(e).__name__, str(e)[:80])
    neg = []
    for row in csv.DictReader(open(root + '/adjudication/decisions.csv')):
        if row['verdict'] != 'overfit': continue
        cd = root + '/adjudication/case' + row['case']; st = json.load(open(cd + '/stats.json'))
        minor = [a['label'] for a in st['atoms'] if a['occ'] < 0.5]; major = [a['label'] for a in st['atoms'] if a['occ'] >= 0.5]
        neg.append(dict(case=row['case'], **features(open(cd + '/candidate.res').read(), minor, major)))
    os.makedirs(root + '/calibration', exist_ok=True)
    json.dump(dict(pos=pos, neg=neg), open(root + '/calibration/gates_features.json', 'w'), indent=1)
    print('positives (deposited sites)', len(pos), 'negatives (expert-overfit splits)', len(neg))
    rows = []
    for occ, ur, t, g in itertools.product((0.05, 0.08), (3, 4, 5, 99), TOLS, (0.25, 0.34, 0.5, 1.01)):
        ok = lambda f: f['min_occ'] >= occ and not f['npd'] and f['min_ueq'] >= 0.005 and f['max_ueq_ratio'] <= ur and f['geom'][str(t)] <= g
        rows.append((sum(map(ok, pos)) / len(pos), sum(not ok(f) for f in neg), occ, ur, t, g))
    print('pos_pass  neg_rejected  occ_min  ueq_ratio_max  bond_tol  geom_frac_max')
    for r in sorted(rows, key=lambda r: (-r[1], -r[0]))[:25]: print('%.2f      %d/%d          %.2f     %-5s          %.2f      %.2f' % (r[0], r[1], len(neg), *r[2:]))
