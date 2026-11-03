"""Objective evidence sheets for the adjudication cases (post-hoc). The same checks run on every case, and no verdict is given.

evidence.py ROOT case OUT NN   writes OUT/caseNN/evidence.md and evidence.json
evidence.py ROOT index OUT     writes OUT/EVIDENCE.md (one line per case)

Reads only OUT/caseNN/{deposited,candidate}.{res,hkl} and stats.json, never _key.json, so the checks are blind
to which system made the candidate.
"""
import sys, os, json, random, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
from adjudicate import diff_map
from cctbx import adptbx

LIGHT = {'H', 'B', 'C', 'N', 'O', 'F', 'SI', 'P', 'S', 'CL'}
BOND_TOL = 0.45        # A above the covalent-radius sum that still counts as a bond
BOND_DEV_PARTNER = 0.10  # A deviation from the partner's matching bond that is flagged
BOND_DEV_COV = 0.25      # A deviation from the covalent-radius sum that is flagged (no partner)
PARTNER_MAX = 2.5        # A: a same-element atom of the other part this close counts as the partner
HIRSHFELD = 0.005      # A^2 difference in mean-square displacement along a bond that is flagged
RIPPLE = (0.5, 1.4)    # A from an atom heavier than Cl where Fourier ripples sit
PERTURB = 0.10         # A random displacement of the candidate atoms for the stability check


def cart(uc, f): return uc.orthogonalize(f)


def u_cart(uc, a):
    if len(a['u']) != 6: return None
    U11, U22, U33, U23, U13, U12 = a['u']
    return adptbx.u_cif_as_u_cart(uc, (U11, U22, U33, U12, U13, U23))


def msda(uc6, n):
    U11, U22, U33, U12, U13, U23 = uc6
    return (U11 * n[0] ** 2 + U22 * n[1] ** 2 + U33 * n[2] ** 2 + 2 * (U12 * n[0] * n[1] + U13 * n[0] * n[2] + U23 * n[1] * n[2]))


def part_ok(p, q): return p == 0 or q == 0 or p == q


def partners_of(m, xs, labels):
    """Nearest same-element atom of the other part (both candidate atoms) within PARTNER_MAX."""
    at = [a for a in m.heavy() if a['label'] in labels]; out = {}
    for a in at:
        c = [(X.min_image_dist(xs, X.frac_xyz(a), X.frac_xyz(b)), b) for b in at if b['label'] != a['label'] and b['el'] == a['el'] and b['part'] != a['part']]
        if c:
            d, b = min(c, key=lambda t: t[0])
            if d <= PARTNER_MAX: out[a['label']] = (b, d)
    return out


def neighbours(m, xs, a):
    fa = X.frac_xyz(a); out = []
    for b in m.heavy():
        if b['label'] == a['label'] or not part_ok(a['part'], b['part']): continue
        d = X.min_image_dist(xs, fa, X.frac_xyz(b)); ref = X.COV.get(a['el'], 1.4) + X.COV.get(b['el'], 1.4)
        if d <= ref + BOND_TOL: out.append((b, d, ref))
    return out


def geometry(m, xs, labels):
    """Bond lengths of candidate atoms, compared with the same-element bonds of the atom's other-part partner
    when it has one, otherwise with the covalent-radius sum (wider tolerance)."""
    uc = xs.unit_cell(); at = {a['label']: a for a in m.heavy()}; part = partners_of(m, xs, labels)
    bonds, flags = [], []
    for lab in sorted(labels):
        a = at.get(lab)
        if a is None: continue
        fa = X.frac_xyz(a)
        for b, d, cov in neighbours(m, xs, a):
            row = dict(a=lab, b=b['label'], d=round(d, 3))
            if lab in part:
                p = part[lab][0]
                ana = sorted(dd for bb, dd, _ in neighbours(m, xs, p) if bb['el'] == b['el'])
                if ana:
                    ref = (ana[(len(ana) - 1) // 2] + ana[len(ana) // 2]) / 2; row.update(expected=round(ref, 3), basis='partner %s' % p['label'])
                    if abs(d - ref) > BOND_DEV_PARTNER: row['flag'] = '%+.2f Å vs partner %s' % (d - ref, p['label'])
            if 'expected' not in row:
                row.update(expected=round(cov, 2), basis='covalent sum')
                if abs(d - cov) > BOND_DEV_COV: row['flag'] = '%+.2f Å vs covalent sum' % (d - cov)
            if d < 0.75 * cov: row['flag'] = 'short contact'
            ua, ub = u_cart(uc, a), u_cart(uc, b)
            dl = [x - y for x, y in zip(fa, X.frac_xyz(b))]; dl = [x - round(x) for x in dl]
            if ua and ub and abs(uc.length(dl) - d) < 0.05 and d > 0.5:
                v = cart(uc, dl); L = math.sqrt(sum(x * x for x in v)); n = [x / L for x in v]
                row['hirshfeld'] = round(abs(msda(ua, n) - msda(ub, n)), 4)
                if row['hirshfeld'] > HIRSHFELD and 'flag' not in row: row['flag'] = 'rigid-bond test %.4f' % row['hirshfeld']
            bonds.append(row)
            if 'flag' in row: flags.append('%s–%s %s' % (lab, b['label'], row['flag']))
    for lab, (p, d) in sorted(part.items()):
        if lab < p['label'] and d > 1.6: flags.append('%s/%s split by %.2f Å (large for a disorder split)' % (lab, p['label'], d))
    return bonds, flags


def adp(m, xs, labels):
    uc = xs.unit_cell(); rows, flags = [], []
    for a in m.heavy():
        if a['label'] not in labels: continue
        ueq, w, _ = X.ueq_and_axes(uc, a)
        r = dict(label=a['label'], part=a['part'], occ=round(a['occ'], 3), ueq=round(ueq, 4), iso=len(a['u']) != 6)
        if not r['iso']:
            r['aniso'] = round(w[0] / w[2], 2) if w[2] > 0 else None
            if min(w) <= 0: flags.append('%s NPD' % a['label'])
            elif r['aniso'] and r['aniso'] > 5: flags.append('%s very anisotropic (%.1f)' % (a['label'], r['aniso']))
        if ueq > 0.15: flags.append('%s Ueq %.3f' % (a['label'], ueq))
        if ueq < 0.005: flags.append('%s Ueq %.4f (very small)' % (a['label'], ueq))
        rows.append(r)
    return rows, flags


def mapcheck(cm, ref, labels):
    """Deposited-map density at each candidate atom, at the midpoint to its nearest same-element partner, and ripple distance."""
    m, rms = diff_map(ref); xs = ref.xs; rows, flags = [], []
    heavy_sites = [(s.label, s.site) for s in xs.scatterers() if s.scattering_type.upper() not in LIGHT]
    at = cm.heavy()
    for a in at:
        if a['label'] not in labels: continue
        f = X.frac_xyz(a); rho = m.eight_point_interpolation(f)
        r = dict(label=a['label'], rho_sigma=round(rho / rms, 1))
        partners = [(X.min_image_dist(xs, f, X.frac_xyz(b)), b) for b in at
                    if b['label'] != a['label'] and b['el'] == a['el'] and b['part'] != a['part'] and b['label'] in labels]
        if partners:
            d, b = min(partners, key=lambda t: t[0])
            if d <= PARTNER_MAX:
                fb = X.frac_xyz(b); dl = [x - y for x, y in zip(fb, f)]; dl = [x - round(x) for x in dl]
                mid = [x + y / 2 for x, y in zip(f, dl)]
                r.update(partner=b['label'], split=round(d, 2), mid_sigma=round(m.eight_point_interpolation(mid) / rms, 1))
        hd = [(X.min_image_dist(xs, f, s), l) for l, s in heavy_sites]
        if hd:
            d, l = min(hd)
            if RIPPLE[0] <= d <= RIPPLE[1]:
                r['ripple'] = '%s %.2f' % (l, d); flags.append('%s %.2f Å from heavy atom %s (Fourier-ripple distance)' % (a['label'], d, l))
        rows.append(r)
    return rows, flags, rms


def perturbed(text, labels, uc, seed):
    rng = random.Random(seed); m = X.Model(text)
    for a in m.atoms:
        if a['label'] not in labels: continue
        t = m.lines[a['idx']].split()
        v = [rng.gauss(0, 1) for _ in range(3)]; n = math.sqrt(sum(x * x for x in v))
        df = uc.fractionalize([PERTURB * x / n for x in v])
        xyz = [x + y if abs(x) < 5 else x for x, y in zip(a['xyz'], df)]
        m.lines[a['idx']] = X.fmt_atom(a['label'], int(t[1]), xyz, float(t[5]), a['u'])
    return m.text()


def restrained(text, labels):
    """RIGU + SIMU on the anisotropic candidate atoms; None when fewer than two are anisotropic."""
    m = X.Model(text)
    aniso = sorted(a['label'] for a in m.heavy() if a['label'] in labels and len(a['u']) == 6)
    if len(aniso) < 2: return None
    k = next(i for i, l in enumerate(m.lines) if X.keyword(l) == 'FVAR')
    names = ' '.join(aniso)
    m.lines[k + 1:k + 1] = ['RIGU ' + names, 'SIMU ' + names]
    return m.text()


def minor_occ(m, labels):
    occ = [a['occ'] for a in m.heavy() if a['label'] in labels]
    return round(min(occ), 3) if occ else None


def build(out, nn):
    cd = '%s/case%s' % (out, nn); st = json.load(open(cd + '/stats.json'))
    labels = set(a['label'] for a in st['atoms'])
    hkl = cd + '/candidate.hkl'
    ref = X.refine(open(cd + '/deposited.res').read(), cd + '/deposited.hkl', cd + '/_ev_ref.res')
    cand = X.refine(open(cd + '/candidate.res').read(), hkl, cd + '/_ev_cand.res')
    cm = X.Model(cand.model_text); uc = cand.xs.unit_cell()
    bonds, gflags = geometry(cm, cand.xs, labels)
    adps, aflags = adp(cm, cand.xs, labels)
    maps, mflags, rms = mapcheck(cm, ref, labels)
    base_occ = minor_occ(cm, labels); base_pos = {a['label']: X.frac_xyz(a) for a in cm.heavy() if a['label'] in labels}
    stab = []
    for name, text in (('perturbed seed 1', perturbed(cand.model_text, labels, uc, 1)),
                       ('perturbed seed 2', perturbed(cand.model_text, labels, uc, 2)),
                       ('RIGU + SIMU on the anisotropic candidate atoms', restrained(cand.model_text, labels))):
        if text is None:
            stab.append(dict(run=name, error='not run: fewer than two candidate atoms are anisotropic')); continue
        try:
            r = X.refine(text, hkl, cd + '/_ev_run.res'); m2 = X.Model(r.model_text)
            moved = max([X.min_image_dist(r.xs, base_pos[a['label']], X.frac_xyz(a)) for a in m2.heavy() if a['label'] in base_pos] or [0])
            stab.append(dict(run=name, R1=round(r.r1, 4), wR2=round(r.wr2, 4), minor_occ=minor_occ(m2, labels),
                             max_shift=round(moved, 2), npd=X.npd_atoms(m2, r.xs.unit_cell())))
        except Exception as e:
            stab.append(dict(run=name, error='%s: %s' % (type(e).__name__, str(e)[:120])))
    for f in ('_ev_ref.res', '_ev_cand.res', '_ev_run.res'):
        if os.path.exists(cd + '/' + f): os.remove(cd + '/' + f)
    sflags = []
    for s in stab:
        if 'error' in s: continue  # an engine failure or a skipped run is not evidence about the structure
        if base_occ is not None and s['minor_occ'] is not None and abs(s['minor_occ'] - base_occ) > 0.05:
            sflags.append('%s: minor occupancy %.3f → %.3f' % (s['run'], base_occ, s['minor_occ']))
        if s['max_shift'] > 0.2: sflags.append('%s: atoms moved up to %.2f Å' % (s['run'], s['max_shift']))
        if s['npd']: sflags.append('%s: NPD %s' % (s['run'], ' '.join(s['npd'])))
    gof = (st['ref']['gof'], st['cand']['gof'])
    oflags = ['GooF falls from %.2f to %.2f with the deposited weighting scheme' % gof] if gof[1] < 0.85 <= gof[0] else []
    ev = dict(case=nn, base_minor_occ=base_occ, bonds=bonds, adps=adps, maps=maps, map_rms=rms, stability=stab,
              flags=dict(geometry=gflags, adp=aflags, map=mflags, stability=sflags, other=oflags))
    json.dump(ev, open(cd + '/evidence.json', 'w'), indent=1)

    L = ['# Case %s: evidence sheet' % nn, '',
         '*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*', '']
    allf = sum(ev['flags'].values(), [])
    L += ['## Flags (%d)' % len(allf), ''] + (['- ' + f for f in allf] if allf else ['- none']) + ['']
    L += ['## Geometry of the candidate atoms', 'Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom\'s other-part partner (flagged above %.2f Å), or with the covalent-radius sum when there is no partner (flagged above %.2f Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above %.3f Å² are flagged.' % (BOND_DEV_PARTNER, BOND_DEV_COV, HIRSHFELD), '',
          '| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |', '|---|---|---|---|---|---|']
    L += ['| %s–%s | %.3f | %s | %s | %s | %s |' % (b['a'], b['b'], b['d'], b['expected'], b['basis'], b.get('hirshfeld', '–'), b.get('flag', '')) for b in bonds]
    L += ['', '## ADPs', 'Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².', '',
          '| atom | PART | occ | Ueq | U1/U3 |', '|---|---|---|---|---|']
    L += ['| %s | %d | %.3f | %.4f | %s |' % (a['label'], a['part'], a['occ'], a['ueq'], 'iso' if a['iso'] else a.get('aniso')) for a in adps]
    L += ['', '## Density in the deposited model\'s difference map', 'In multiples of the map rms (%.3f e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms %.1f–%.1f Å from an atom heavier than Cl sit at typical Fourier-ripple distances.' % (rms, RIPPLE[0], RIPPLE[1]), '',
          '| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |', '|---|---|---|---|---|---|']
    L += ['| %s | %.1f | %s | %s | %s | %s |' % (r['label'], r['rho_sigma'], r.get('partner', '–'), r.get('split', '–'), r.get('mid_sigma', '–'), r.get('ripple', '')) for r in maps]
    L += ['', '## Stability', 'The candidate re-refined twice from start positions displaced by %.2f Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: %s.' % (PERTURB, base_occ), '',
          '| run | R1 | wR2 | minor occ | max shift (Å) | NPD |', '|---|---|---|---|---|---|']
    for s in stab:
        L.append('| %s | not available (%s) |||||' % (s['run'], s['error'][:90]) if 'error' in s else '| %s | %.4f | %.4f | %s | %.2f | %s |' % (s['run'], s['R1'], s['wR2'], s['minor_occ'], s['max_shift'], ' '.join(s['npd']) or '–'))
    open(cd + '/evidence.md', 'w').write('\n'.join(L) + '\n')
    print(nn, 'done', len(allf), 'flags', flush=True)


def index(out):
    L = ['# Evidence sheets: summary', '',
         '*Post-hoc, computed, blind to which system made each candidate. These are flags to check in Olex2, not verdicts.*', '',
         '| case | ΔR1 | geometry | ADP | map (ripple) | stability | other | sheet |', '|---|---|---|---|---|---|---|---|']
    for nn in sorted(d[4:] for d in os.listdir(out) if d.startswith('case')):
        p = '%s/case%s/evidence.json' % (out, nn)
        if not os.path.exists(p): L.append('| %s | not built |||||||' % nn); continue
        e = json.load(open(p)); s = json.load(open('%s/case%s/stats.json' % (out, nn))); f = e['flags']
        L.append('| %s | %+.4f | %d | %d | %d | %d | %d | [evidence](case%s/evidence.md) |' % (nn, s['cand']['R1'] - s['ref']['R1'], len(f['geometry']), len(f['adp']), len(f['map']), len(f['stability']), len(f['other']), nn))
    L += ['', 'Counts are numbers of flags; read each sheet for what they are. A case with no flags still needs a look at the density and chemistry.', '']
    open(out + '/EVIDENCE.md', 'w').write('\n'.join(L))


if __name__ == '__main__':
    root, cmd, out = sys.argv[1], sys.argv[2], sys.argv[3]
    if cmd == 'case': build(out, sys.argv[4])
    else: index(out)
