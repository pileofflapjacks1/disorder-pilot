"""System B2: round-2 rule-based baseline (no LLM). B (system_b.py, frozen for the pilot) plus fixes for its
documented failures (RESULTS_B.md, "Where the rules fail") and plausibility gates on every accepted split.
Tuned only on the pilot sample + dev tasks; frozen before any round-2 task is run.

Changes from B:
  1. Peak window 0.4-1.6 A (B: 0.4-1.3), the range CrystalPilot's candidate generator uses (idea only; no code
     taken).
  2. Ripple filter: peaks within RIPPLE_MAX of an atom heavier than Cl are ignored (B spent its tries there).
  3. Up to MAX_TRIES clusters (B: 3).
  4. The minor part gets no riding H (B copied them, which crashed the engine on AFIX bond-count mismatches).
  5. Acceptance gates, added to B's R1/wR2/occupancy/NPD rule:
     - minor occupancy >= OCC_MIN;
     - geometry: at most GEOM_MAX_FRAC of the split atoms' bonds flagged by evidence.geometry;
     - ADPs: minor-part Ueq within [0.005, UEQ_MAX_RATIO x median heavy-atom Ueq];
     - stability: re-refined from occupancy 0.5 instead of 0.7, the minor occupancy moves by <= OCC_STAB.
  6. MINOR_U='simu': a SIMU restraint over each split, its minor copies and their bonded neighbours, the usual
     crystallographer's restraint on a minor part (default 'free' = no ADP restraint, as in B).
system_b2.py ROOT ids...  reads tasks/<id>/input/model_refined.res (= A), writes tasks/<id>/B2/final.res + log.json
"""
import sys, os, json, statistics, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
import system_b as B
import evidence as E

P = dict(WIN=(0.4, 1.6), RIPPLE_MAX=1.3, MAX_TRIES=5, OCC_MIN=0.08, GEOM_MAX_FRAC=0.25, UEQ_MAX_RATIO=3.0, OCC_STAB=0.10, MINOR_U='free')
if os.environ.get('B2_PARAMS'): P.update(json.loads(os.environ['B2_PARAMS']))
P['WIN'] = tuple(P['WIN'])


def ripple(peak, heavy_sites, xs):
    return any(X.min_image_dist(xs, s, peak['site']) < P['RIPPLE_MAX'] for s in heavy_sites)


def candidates(model, peaks, rms, uc, xs):
    heavy = model.heavy(); ueqs = {a['label']: X.ueq_and_axes(uc, a)[0] for a in heavy}
    med = statistics.median(ueqs.values()); thr = max(5 * rms, 0.35)
    hz = [X.frac_xyz(a) for a in heavy if B.Z(a['el']) > 17]
    strong = [p for p in peaks if p['height'] >= thr and not ripple(p, hz, xs)]
    lo, hi = P['WIN']; cand = {}
    for a in heavy:
        if B.Z(a['el']) > 17 or a['afix'] != 0: continue
        near = [p for p in strong if lo <= X.min_image_dist(xs, X.frac_xyz(a), p['site']) <= hi]
        if ueqs[a['label']] > 2 * med or near:
            cand[a['label']] = dict(peak=max((p['height'] for p in near), default=0), ueq_ratio=ueqs[a['label']] / med)
    return cand, strong, thr, med


def split(model_text, cluster, peaks, xs, uc, fv_index, start_occ=0.7):
    """B's split with the B2 window, no riding H on the minor part, and a chosen starting occupancy."""
    lo, hi = P['WIN']
    m = X.Model(model_text); atoms = {a['label']: a for a in m.atoms}; blk = B.blocks(m)
    used = set(); minor_pos = {}
    for lab in sorted(cluster, key=lambda l: -X.ueq_and_axes(uc, atoms[l])[0]):
        p0 = X.frac_xyz(atoms[lab])
        opts = [(p['height'], k) for k, p in enumerate(peaks) if k not in used and lo <= X.min_image_dist(xs, p0, p['site']) <= hi]
        if opts:
            k = max(opts)[1]; used.add(k)
            best = min((X._min_image(uc, p0, op * peaks[k]['site']), op * peaks[k]['site']) for op in xs.space_group().all_ops())
            minor_pos[lab] = ('peak', [b + round(a - b) for a, b in zip(p0, best[1])])
    mode = 'peak' if len(minor_pos) >= len(cluster) / 2 else 'adp'
    shifts = {}
    for lab in cluster:
        a = atoms[lab]; p0 = X.frac_xyz(a)
        if mode == 'peak' and lab in minor_pos: continue
        ueq, w, v = X.ueq_and_axes(uc, a)
        if v is None: d_cart = (0.3, 0, 0)
        else:
            delta = min(max(w[0] - w[1], 0.002) ** 0.5, 0.6); d_cart = tuple(float(x) * delta for x in v[:, 0])
        df = uc.fractionalize(d_cart)
        minor_pos[lab] = ('adp', [x + y for x, y in zip(p0, df)]); shifts[lab] = [x - y for x, y in zip(p0, df)]
    used_labels = set(a['label'].upper() for a in m.atoms); counters = {}
    def newlab(el):
        n = counters.get(el, 0)
        while True:
            n += 1; c = '%s%d' % (el.capitalize(), 900 + n if len(el) == 1 else 90 + n)
            if c.upper() not in used_labels: counters[el] = n; used_labels.add(c.upper()); return c
    code = 10 * fv_index + 1
    out = []; skip = set(i for l in cluster for i in blk[l]); minor_names = {}
    for k, line in enumerate(m.lines):
        if k in skip: continue
        a = next((a for a in m.atoms if a['idx'] == k), None)
        if a is None or a['label'] not in cluster:
            out.append(line); continue
        lab = a['label']; t = line.split()
        out += ['PART 1', X.fmt_atom(lab, int(t[1]), shifts.get(lab, X.frac_xyz(a)), code, a['u'])]
        for h in (m.lines[i] for i in blk[lab]):
            if X.keyword(h) == 'AFIX': out.append(h); continue
            ht = h.split(); ht[5] = '%.5f' % code; out.append(' '.join(ht))
        ml = newlab(a['el']); minor_names[lab] = ml
        out += ['PART 2', X.fmt_atom(ml, int(t[1]), minor_pos[lab][1], -code, [X.ueq_and_axes(uc, a)[0]]), 'PART 0']
    pos = {a['label']: X.frac_xyz(a) for a in m.atoms}; el = {a['label']: a['el'] for a in m.atoms}
    sadi = []; nbr = set()
    for a in m.heavy():
        for lab in cluster:
            b = a['label']
            if b == lab: continue
            dd = uc.length([p - q for p, q in zip(pos[b], pos[lab])])
            if dd < X.COV.get(el[b], 1.5) + X.COV.get(el[lab], 1.5) + 0.45:
                if b in cluster:
                    if b < lab: sadi.append('SADI 0.02 %s %s %s %s' % (b, lab, minor_names[b], minor_names[lab]))
                else: sadi.append('SADI 0.02 %s %s %s %s' % (b, lab, b, minor_names[lab])); nbr.add(b)
    if P['MINOR_U'] == 'simu':  # similar-ADP restraint over the split atoms, their minor copies and their neighbours
        sadi.append('SIMU 0.04 0.08 1.7 ' + ' '.join(sorted(set(cluster) | set(minor_names.values()) | nbr)))
    final = []
    for line in out:
        if X.keyword(line) == 'FVAR':
            fv = line.split()[1:]
            while len(fv) < fv_index - 1: fv.append('0.5')
            fv.append('%.2f' % start_occ); final += sadi + ['FVAR ' + ' '.join(fv)]
        else: final.append(line)
    return '\n'.join(final) + '\n', mode, minor_names


def gates(r, cluster, names, fv_index, med, text_half, hkl, od):
    """Plausibility gates on a refined split; returns (ok, details)."""
    m = X.Model(r.model_text); uc = r.xs.unit_cell(); occ_minor = 1 - X.fvar_values(r.model_text)[fv_index - 1]
    labels = set(cluster) | set(names.values())
    bonds, gflags = E.geometry(m, r.xs, labels)
    nb = sum(1 for b in bonds if b['a'] in labels); nf = sum(1 for b in bonds if b['a'] in labels and 'flag' in b)
    geom_frac = nf / nb if nb else 0.0
    mu = [X.ueq_and_axes(uc, a)[0] for a in m.heavy() if a['label'] in names.values()]
    ueq_ok = all(0.005 <= u <= P['UEQ_MAX_RATIO'] * med for u in mu)
    try:
        r2 = X.refine(text_half, hkl, od + '/_half.res'); occ2 = 1 - X.fvar_values(r2.model_text)[fv_index - 1]
    except Exception as e:
        occ2 = None
    stab = occ2 is not None and abs(occ2 - occ_minor) <= P['OCC_STAB']
    d = dict(geom_frac=round(geom_frac, 3), n_bonds=nb, ueq_minor=[round(u, 4) for u in mu], ueq_ok=ueq_ok,
             occ_from_half=None if occ2 is None else round(occ2, 3), stable=stab)
    return geom_frac <= P['GEOM_MAX_FRAC'] and ueq_ok and stab and occ_minor >= P['OCC_MIN'], d


def run(root, i):
    d = root + '/tasks/' + i; od = d + '/B2'; os.makedirs(od, exist_ok=True); hkl = d + '/input/data.hkl'
    base = X.refine(open(d + '/input/model_refined.res').read(), hkl, od + '/_run.res', cycles=10)
    cur_text, cur = base.model_text, base
    peaks, rms, hole = X.diff_peaks(base, n=40)
    uc = base.xs.unit_cell(); xs = base.xs
    cand, strong, thr, med = candidates(X.Model(cur_text), peaks, rms, uc, xs)
    cl = B.clusters(X.Model(cur_text), cand, xs)[:P['MAX_TRIES']]
    log = dict(id=i, params=P, rms=rms, thr=thr, n_cand=len(cand), clusters=[], start=dict(R1=cur.r1, wR2=cur.wr2))
    fv_index = 2
    for c in cl:
        entry = dict(atoms=c)
        try:
            text, mode, names = split(cur_text, c, strong, xs, uc, fv_index)
            r = X.refine(text, hkl, od + '/_try.res')
            occ_minor = 1 - X.fvar_values(r.model_text)[fv_index - 1]
            npd = X.npd_atoms(X.Model(r.model_text), r.xs.unit_cell())
            base_ok = r.wr2 <= 0.98 * cur.wr2 and r.r1 <= cur.r1 and 0.05 <= occ_minor <= 0.95 and not npd
            entry.update(mode=mode, R1=r.r1, wR2=r.wr2, minor_occ=occ_minor, npd=npd, base_ok=base_ok)
            ok = False
            if base_ok:
                half, _, _ = split(cur_text, c, strong, xs, uc, fv_index, start_occ=0.5)
                ok, g = gates(r, c, names, fv_index, med, half, hkl, od); entry['gates'] = g
            entry['accepted'] = ok
            if ok: cur_text, cur = r.model_text, r; fv_index += 1
        except Exception as e:
            entry.update(error='%s: %s' % (type(e).__name__, str(e)[:120]), accepted=False)
        log['clusters'].append(entry)
    for f in ('_run.res', '_try.res', '_half.res'):
        if os.path.exists(od + '/' + f): os.remove(od + '/' + f)
    open(od + '/final.res', 'w').write(cur_text)
    log['final'] = dict(R1=cur.r1, wR2=cur.wr2)
    json.dump(log, open(od + '/log.json', 'w'), indent=1)
    return log


if __name__ == '__main__':
    root = sys.argv[1]
    for i in sys.argv[2:]:
        t0 = time.time()
        try:
            lg = run(root, i)
            print(i, 'cand %d' % lg['n_cand'], ' '.join('[%d %s]' % (len(c['atoms']), 'ACC' if c['accepted'] else ('gate' if c.get('base_ok') else 'rej'))
                  for c in lg['clusters']), '%.0fs' % (time.time() - t0), flush=True)
        except Exception as e:
            print(i, 'ERROR %s: %s' % (type(e).__name__, str(e)[:150]), flush=True)
