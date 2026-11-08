"""Plausible detection (proposed round-2 metric; rule written 2026-11-06 before it was computed for C).
With B2 v1's gates this failed calibration (12/38 deposited sites passed). With the v2 gates, 64/65 deposited sites
pass as published. It is a floor against non-physical models, not evidence that disorder is real; see RESULTS_B2.md.

A site scored `detected` by score.py is also `plausible` when its matched minor atoms, in the re-refined
submission, pass the same checks and thresholds as baseline B2's acceptance gates (tools/system_b2.py):
  - every matched minor atom: occupancy >= OCC_MIN, Ueq in [0.005, UEQ_MAX_RATIO x median heavy-atom Ueq], not NPD;
  - geometry: at most GEOM_MAX_FRAC of the matched minor atoms' bonds are flagged by evidence.geometry (bond
    length vs the same bond of the other-part partner, else vs the covalent sum; short contacts; rigid-bond test).
B2's occupancy-stability gate is not used: it needs a system-specific occupancy encoding.

plausible.py ROOT SYSTEM ids...   writes tasks/<id>/<SYSTEM>/plausible.json, prints one line per task
"""
import sys, os, json, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
import evidence as E
from score import frac, modelled_partials, MATCH
from system_b2 import P as B2
from cctbx import xray


def check(task_dir, refined):
    info = json.load(open(task_dir + '/truth.json')); sc = json.load(open(task_dir + '/' + SYS + '/score.json'))
    inp = X.Model(open(task_dir + '/input/model.res').read()); sub = X.Model(refined.model_text)
    xs = xray.structure.from_shelx(file=open(task_dir + '/truth.res')); uc = refined.xs.unit_cell()
    med = statistics.median(X.ueq_and_axes(uc, a)[0] for a in sub.heavy())
    parts = modelled_partials(sub, inp, xs); npd = set(X.npd_atoms(sub, uc))
    tpos = {a['label']: frac(a) for a in X.Model(open(task_dir + '/truth.res').read()).atoms}
    out = []
    for s, ss in zip(info['sites'], sc['sites']):
        row = dict(type=s['type'], detected=ss['detected'], plausible=False)
        if ss['detected']:
            minor = []
            for el, xyz in zip(s['minor_el'], s['minor_xyz']):
                c = [a for a in parts if X.min_image_dist(xs, frac(a), xyz) < MATCH]
                if c: minor.append(min(c, key=lambda a: X.min_image_dist(xs, frac(a), xyz)))
            major = [a for a in sub.heavy() if any(X.min_image_dist(xs, frac(a), tpos[l]) < MATCH for l in s['major'] if l in tpos)]
            ml = set(a['label'] for a in minor)
            bonds, _ = E.geometry(sub, refined.xs, ml | set(a['label'] for a in major))
            mb = [b for b in bonds if b['a'] in ml]; nf = sum('flag' in b for b in mb)
            geom = nf / len(mb) if mb else 0.0
            bad = [a['label'] for a in minor if a['occ'] < B2['OCC_MIN'] or a['label'] in npd
                   or not 0.005 <= X.ueq_and_axes(uc, a)[0] <= B2['UEQ_MAX_RATIO'] * med]
            row.update(geom_frac=round(geom, 3), n_bonds=len(mb), bad_atoms=bad,
                       plausible=geom <= B2['GEOM_MAX_FRAC'] and not bad)
        out.append(row)
    return dict(id=info['id'], type=info['type'], sites=out)


if __name__ == '__main__':
    root, SYS = sys.argv[1], sys.argv[2]
    for i in sys.argv[3:]:
        d = root + '/tasks/' + i; sd = d + '/' + SYS
        if not os.path.exists(sd + '/score.json'): print(i, 'NO SCORE'); continue
        try:
            r = X.refine(open(sd + '/final.res').read(), d + '/input/data.hkl', sd + '/_pl.res')
            res = check(d, r)
        except Exception as e:
            res = dict(id=i, error='%s: %s' % (type(e).__name__, str(e)[:120]))
        if os.path.exists(sd + '/_pl.res'): os.remove(sd + '/_pl.res')
        json.dump(res, open(sd + '/plausible.json', 'w'), indent=1)
        print(i, SYS, res.get('error') or ' '.join('%s%s' % ('P' if x['plausible'] else ('d' if x['detected'] else '.'), '' if x['plausible'] or not x['detected'] else str(x.get('bad_atoms', ''))[:40]) for x in res['sites']), flush=True)
