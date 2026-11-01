"""System B: fixed-rule disorder modelling (no LLM). Rules frozen in PREREGISTRATION.md.
system_b.py ROOT ids...  reads tasks/<id>/input/model_refined.res (= A), writes tasks/<id>/B/final.res + log.json"""
import sys, os, json, statistics, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
from cctbx import uctbx
from cctbx.eltbx import tiny_pse

Z = lambda el: tiny_pse.table(el.capitalize()).atomic_number()


def blocks(model):
    """Map heavy-atom label -> list of line indices of its riding-H block (AFIX n ... AFIX 0)."""
    out = {}
    for k, a in enumerate(model.atoms):
        if a['el'] == 'H': continue
        i = a['idx'] + 1; blk = []
        if i < len(model.lines) and X.keyword(model.lines[i]) == 'AFIX' and model.lines[i].split()[1] != '0':
            j = i + 1
            while j < len(model.lines) and X.keyword(model.lines[j]) != 'AFIX': j += 1
            blk = list(range(i, j + 1)) if j < len(model.lines) else []
        out[a['label']] = blk
    return out


def candidates(model, peaks, rms, uc, xs):
    heavy = model.heavy(); ueqs = {a['label']: X.ueq_and_axes(uc, a)[0] for a in heavy}
    med = statistics.median(ueqs.values()); thr = max(5 * rms, 0.35)
    strong = [p for p in peaks if p['height'] >= thr]
    cand = {}
    for a in heavy:
        if Z(a['el']) > 17 or a['afix'] != 0: continue
        near = [p for p in strong if 0.4 <= X.min_image_dist(xs, X.frac_xyz(a), p['site']) <= 1.3]
        if ueqs[a['label']] > 2 * med or near:
            cand[a['label']] = dict(peak=max((p['height'] for p in near), default=0), ueq_ratio=ueqs[a['label']] / med)
    return cand, strong, thr


def clusters(model, cand, xs):
    labs = list(cand); pos = {a['label']: X.frac_xyz(a) for a in model.atoms}; el = {a['label']: a['el'] for a in model.atoms}
    adj = {l: set() for l in labs}
    for i, a in enumerate(labs):
        for b in labs[i + 1:]:
            if X.min_image_dist(xs, pos[a], pos[b]) < X.COV.get(el[a], 1.5) + X.COV.get(el[b], 1.5) + 0.45: adj[a].add(b); adj[b].add(a)
    seen, out = set(), []
    for l in labs:
        if l in seen: continue
        comp, stack = [], [l]
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen.add(x); comp.append(x); stack += adj[x]
        out.append(comp)
    key = lambda c: (max(cand[l]['peak'] for l in c), max(cand[l]['ueq_ratio'] for l in c))
    return sorted(out, key=key, reverse=True)


def split(model_text, cluster, peaks, xs, uc, fv_index):
    m = X.Model(model_text); atoms = {a['label']: a for a in m.atoms}; blk = blocks(m)
    used = set(); minor_pos = {}
    for lab in sorted(cluster, key=lambda l: -X.ueq_and_axes(uc, atoms[l])[0]):
        p0 = X.frac_xyz(atoms[lab])
        opts = [(p['height'], k) for k, p in enumerate(peaks) if k not in used and 0.4 <= X.min_image_dist(xs, p0, p['site']) <= 1.3]
        if opts:
            k = max(opts)[1]; used.add(k)
            # pick the symmetry image of the peak closest to the atom
            best = min((X._min_image(uc, p0, op * peaks[k]['site']), op * peaks[k]['site']) for op in xs.space_group().all_ops())
            site = [b + round(a - b) for a, b in zip(p0, best[1])]
            minor_pos[lab] = ('peak', site)
    mode = 'peak' if len(minor_pos) >= len(cluster) / 2 else 'adp'
    shifts = {}
    for lab in cluster:
        a = atoms[lab]; p0 = X.frac_xyz(a)
        if mode == 'peak' and lab in minor_pos: continue
        ueq, w, v = X.ueq_and_axes(uc, a)
        if v is None: d_cart = (0.3, 0, 0); delta = 0.3
        else:
            delta = min(max(w[0] - w[1], 0.002) ** 0.5, 0.6); d_cart = tuple(float(x) * delta for x in v[:, 0])
        df = uc.fractionalize(d_cart)
        minor_pos[lab] = ('adp', [x + y for x, y in zip(p0, df)]); shifts[lab] = [x - y for x, y in zip(p0, df)]
    used_labels = set(a['label'].upper() for a in m.atoms); counters = {}
    def newlab(el):
        n = counters.get(el, 0)
        while True:
            n += 1; cand = '%s%d' % (el.capitalize(), 900 + n if len(el) == 1 else 90 + n)
            if cand.upper() not in used_labels: counters[el] = n; used_labels.add(cand.upper()); return cand
    code = 10 * fv_index + 1
    out = []; skip = set(i for l in cluster for i in blk[l]); minor_names = {}
    for k, line in enumerate(m.lines):
        if k in skip: continue
        a = next((a for a in m.atoms if a['idx'] == k), None)
        if a is None or a['label'] not in cluster:
            out.append(line); continue
        lab = a['label']; t = line.split()
        xyz = shifts.get(lab, X.frac_xyz(a))
        out += ['PART 1', X.fmt_atom(lab, int(t[1]), xyz, code, a['u'])]
        hl = [m.lines[i] for i in blk[lab]]
        def h_lines(sign, rename):
            res = []
            for h in hl:
                if X.keyword(h) == 'AFIX': res.append(h); continue
                ht = h.split(); ht[5] = '%.5f' % (sign * code)
                if rename: ht[0] = newlab('H')
                res.append(' '.join(ht))
            return res
        out += h_lines(1, False)
        ml = newlab(a['el']); minor_names[lab] = ml
        ueq = X.ueq_and_axes(uc, a)[0]
        out += ['PART 2', X.fmt_atom(ml, int(t[1]), minor_pos[lab][1], -code, [ueq])]
        out += h_lines(-1, True)
        out += ['PART 0']
    # FVAR and SADI restraints tying the two parts' bond lengths
    pos = {a['label']: X.frac_xyz(a) for a in m.atoms}; el = {a['label']: a['el'] for a in m.atoms}
    sadi = []
    for a in m.heavy():
        for lab in cluster:
            b = a['label']
            if b == lab: continue
            dd = uc.length([p - q for p, q in zip(pos[b], pos[lab])])
            if dd < X.COV.get(el[b], 1.5) + X.COV.get(el[lab], 1.5) + 0.45:
                if b in cluster:
                    if b < lab: sadi.append('SADI 0.02 %s %s %s %s' % (b, lab, minor_names[b], minor_names[lab]))
                else:
                    sadi.append('SADI 0.02 %s %s %s %s' % (b, lab, b, minor_names[lab]))
    final = []
    for line in out:
        if X.keyword(line) == 'FVAR':
            fv = line.split()[1:]
            while len(fv) < fv_index - 1: fv.append('0.5')
            fv.append('0.7'); final += sadi + ['FVAR ' + ' '.join(fv)]
        else: final.append(line)
    return '\n'.join(final) + '\n', mode, minor_names


def run(root, i):
    d = root + '/tasks/' + i; od = d + '/B'; os.makedirs(od, exist_ok=True); hkl = d + '/input/data.hkl'
    base = X.refine(open(d + '/input/model_refined.res').read(), hkl, od + '/_run.res', cycles=10)
    cur_text, cur = base.model_text, base
    peaks, rms, hole = X.diff_peaks(base, n=40)
    uc = base.xs.unit_cell(); xs = base.xs
    cand, strong, thr = candidates(X.Model(cur_text), peaks, rms, uc, xs)
    cl = clusters(X.Model(cur_text), cand, xs)[:3]
    log = dict(id=i, rms=rms, thr=thr, n_cand=len(cand), clusters=[], start=dict(R1=cur.r1, wR2=cur.wr2))
    fv_index = 2
    for c in cl:
        entry = dict(atoms=c)
        try:
            text, mode, names = split(cur_text, c, strong, xs, uc, fv_index)
            r = X.refine(text, hkl, od + '/_try.res')
            fv = X.fvar_values(r.model_text); occ_minor = 1 - fv[fv_index - 1]
            npd = X.npd_atoms(X.Model(r.model_text), r.xs.unit_cell())
            ok = r.wr2 <= 0.98 * cur.wr2 and r.r1 <= cur.r1 and 0.05 <= occ_minor <= 0.95 and not npd
            entry.update(mode=mode, R1=r.r1, wR2=r.wr2, minor_occ=occ_minor, npd=npd, accepted=ok)
            if ok: cur_text, cur = r.model_text, r; fv_index += 1
        except Exception as e:
            entry.update(error='%s: %s' % (type(e).__name__, str(e)[:120]), accepted=False)
        log['clusters'].append(entry)
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
            print(i, 'cand %d' % lg['n_cand'], ' '.join('[%s %s%s]' % (len(c['atoms']), 'ACC' if c['accepted'] else 'rej',
                  ' occ%.2f dwR2 %+.4f' % (c['minor_occ'], c['wR2'] - lg['start']['wR2']) if 'wR2' in c else ' ' + c.get('error', '')[:60]) for c in lg['clusters']),
                  '%.0fs' % (time.time() - t0), flush=True)
        except Exception as e:
            print(i, 'ERROR %s: %s' % (type(e).__name__, str(e)[:150]), flush=True)
