"""Classify disorder sites in deposited models. Site = one free variable linking PART 1/2 atoms.
Types: subst (minor atom of another element within 0.3 A of a major atom), discrete (no bond from
disordered heavy atoms to PART 0), group_small (<=4 heavy atoms per part), group_large (>4)."""
import sys, json, collections
sys.path.insert(0, sys.argv[1] + '/tools')
import xtal_lib as X
from cctbx import xray

def sites_of(model):
    by = collections.defaultdict(lambda: {1: [], -1: []})
    for a in model.atoms:
        if a['part'] <= 0: continue
        m = int(abs(a['occ_code']) // 10)
        if m < 2: continue
        by[m][1 if a['occ_code'] > 0 else -1].append(a)
    return by

def classify(path):
    model = X.Model(open(path).read())
    parts = sorted(set(a['part'] for a in model.atoms))
    if any(p < 0 for p in parts): return dict(ok=False, why='negative PART')
    if any(p > 2 for p in parts): return dict(ok=False, why='>2 parts')
    if model.unsupported(): return dict(ok=False, why='unsupported ' + ' '.join(model.unsupported()))
    xs = xray.structure.from_shelx(file=open(path))
    if len(xs.scatterers()) != len(model.atoms): return dict(ok=False, why='atom count mismatch')
    lab = {id(a): k for k, a in enumerate(model.atoms)}
    els = [a['el'] for a in model.atoms]
    sites = []
    for m, sides in sites_of(model).items():
        hv = {s: [a for a in sides[s] if a['el'] != 'H'] for s in (1, -1)}
        if not hv[1] or not hv[-1]: continue
        occ = {s: sum(a['occ'] for a in hv[s]) / len(hv[s]) for s in (1, -1)}
        minor = 1 if occ[1] < occ[-1] else -1
        mi, ma = hv[minor], hv[-minor]
        sc = xs.scatterers()
        subst = any(min_d < 0.3 and b['el'] != a['el'] for a in mi for b in ma
                    for min_d in [X.min_image_dist(xs, sc[lab[id(a)]].site, sc[lab[id(b)]].site)])
        dis_idx = set(lab[id(a)] for a in mi + ma)
        ordered = [k for k, a in enumerate(model.atoms) if a['part'] == 0 and a['el'] != 'H']
        attached = any(X.min_image_dist(xs, sc[i].site, sc[j].site) < X.COV.get(els[i], 1.5) + X.COV.get(els[j], 1.5) + 0.45
                       for i in dis_idx for j in ordered)
        typ = 'subst' if subst else ('group_small' if len(mi) <= 4 else 'group_large') if attached else 'discrete'
        sites.append(dict(fv=m, type=typ, minor_occ=round(occ[minor], 3), n_minor=len(mi), n_major=len(ma),
                          minor=[a['label'] for a in mi], major=[a['label'] for a in ma], minor_sign=minor,
                          minor_xyz=[list(sc[lab[id(a)]].site) for a in mi], minor_el=[a['el'] for a in mi]))
    if not sites: return dict(ok=False, why='no heavy-atom free-variable site (H-only or PART without FVAR)')
    if any(a['part'] > 0 and int(abs(a['occ_code']) // 10) < 2 and a['el'] != 'H' for a in model.atoms):
        return dict(ok=False, why='PART atoms with fixed/non-FVAR occupancy')
    big = max(sites, key=lambda s: s['n_minor'])
    return dict(ok=True, sites=sites, type=big['type'], n_sites=len(sites))

if __name__ == '__main__':
    P = sys.argv[1]; out = {}
    for d in json.load(open(P + '/disordered.json')):
        i = d['id']
        try: out[i] = classify(P + '/work/%s/model.res' % i)
        except Exception as e: out[i] = dict(ok=False, why='error %s %s' % (type(e).__name__, str(e)[:80]))
        o = out[i]; out[i]['R1'] = d['R1']
        print(i, o['type'] if o['ok'] else 'EXCLUDED', o.get('why', ''), [(s['type'], s['n_minor'], s['minor_occ']) for s in o.get('sites', [])])
    json.dump(out, open(P + '/classes.json', 'w'), indent=1)
    c = collections.Counter(o['type'] for o in out.values() if o['ok']); print(c, 'included', sum(c.values()))
