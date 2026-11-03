"""Blinded adjudication packs for false positives that lower R1 (post-hoc; not part of the preregistered scoring).

adjudicate.py ROOT build OUT        assigns blinded case numbers (seeded) and writes OUT/_key.json
adjudicate.py ROOT case OUT NN      refines deposited + candidate for case NN and writes OUT/caseNN/
adjudicate.py ROOT index OUT        writes OUT/README.md summary table and OUT/decisions.csv
"""
import sys, os, json, random, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X
from cctbx import maptbx
from cctbx.array_family import flex
from scipy.stats import f as fdist

CASES = [('2312969', 'B'), ('2312969', 'C'), ('2312879', 'C'), ('2312981', 'C'), ('2312281', 'C'), ('2312661', 'B'),
         ('2312661', 'C'), ('2312115', 'C'), ('2243569', 'B'), ('2243801', 'B'), ('2312471', 'C')]
SEED = 20261101


def diff_map(r):
    """Fo-Fc map built the same way as xtal_lib.diff_peaks; returns (map, rms)."""
    obs = r.obs.average_bijvoet_mates() if r.obs.anomalous_flag() else r.obs
    fc = obs.structure_factors_from_scatterers(r.xs, algorithm='direct').f_calc()
    k = r.ls.scale_factor()
    fo = flex.sqrt(flex.double([max(v, 0) for v in obs.data()]) / k)
    fmod = flex.abs(fc.data()); ok = fmod > 1e-6
    fo, fmod, fc = fo.select(ok), fmod.select(ok), fc.select(ok)
    ratio = (fo - fmod) / fmod
    coeff = fc.customized_copy(data=fc.data() * flex.complex_double(ratio, flex.double(ratio.size(), 0)))
    fft = coeff.fft_map(resolution_factor=1 / 4.0, symmetry_flags=maptbx.use_space_group_symmetry)
    fft.apply_volume_scaling()
    m = fft.real_map_unpadded()
    return m, flex.mean_sq(m.as_1d()) ** 0.5


def hamilton(ref, cand):
    """Hamilton R-ratio test of the candidate's extra parameters, on wR2 (F^2): an approximation of the F-based test."""
    b = cand.npar - ref.npar; dof = cand.n_obs - cand.npar
    ratio = ref.wr2 / cand.wr2
    if b <= 0 or ratio <= 1: return dict(b=b, ratio=round(ratio, 4), p=None)
    F = (ratio ** 2 - 1) * dof / b
    return dict(b=b, ratio=round(ratio, 4), F=round(F, 2), p=float(fdist.sf(F, b, dof)))


def build_case(root, out, nn):
    key = json.load(open(out + '/_key.json')); i, system = key[nn]
    d = root + '/tasks/' + i; cd = '%s/case%s' % (out, nn); os.makedirs(cd, exist_ok=True)
    truth = open(d + '/truth.res').read()
    soft = [l for l in X.logical_lines(truth) if X.keyword(l).split('_')[0] in ('EADP', 'EXYZ', 'SAME')]
    truth = '\n'.join(l for l in X.logical_lines(truth) if l not in soft) + '\n'
    hkl = d + '/input/data.hkl'
    ref = X.refine(truth, hkl, cd + '/_ref_run.res')
    cand = X.refine(open(d + '/%s/final.res' % system).read(), hkl, cd + '/_cand_run.res')
    for name, r in (('deposited', ref), ('candidate', cand)):
        open('%s/%s.res' % (cd, name), 'w').write(r.model_text); shutil.copy(hkl, '%s/%s.hkl' % (cd, name))
    for f in ('_ref_run.res', '_cand_run.res'):
        if os.path.exists(cd + '/' + f): os.remove(cd + '/' + f)
    fp = json.load(open(d + '/%s/score.json' % system))['fp_atoms']
    cm = X.Model(cand.model_text); uc = cand.xs.unit_cell()
    m, rms = diff_map(ref)
    rows = []
    for a in cm.heavy():
        if a['label'] not in fp: continue
        site = X.frac_xyz(a)
        rho = m.eight_point_interpolation(site)
        near = X.nearest_atoms(ref.xs, site, k=1)
        rows.append(dict(label=a['label'], el=a['el'], part=a['part'], occ=round(a['occ'], 3),
                         ueq=round(X.ueq_and_axes(uc, a)[0], 4), rho=round(rho, 2), rho_sigma=round(rho / rms, 1),
                         nearest_deposited=(ref.xs.scatterers()[near[0][0]].label if near else None), dist=(round(near[0][1], 2) if near else None)))
    pk_ref, rms_ref, hole_ref = X.diff_peaks(ref, n=5)
    pk_c, rms_c, hole_c = X.diff_peaks(cand, n=5)
    stats = dict(case=nn, n_obs=cand.n_obs, ref=dict(R1=ref.r1, wR2=ref.wr2, gof=ref.gof, npar=ref.npar, top_peak=pk_ref[0]['height'] if pk_ref else None, hole=hole_ref, rms=rms_ref),
                 cand=dict(R1=cand.r1, wR2=cand.wr2, gof=cand.gof, npar=cand.npar, top_peak=pk_c[0]['height'] if pk_c else None, hole=hole_c, rms=rms_c),
                 hamilton=hamilton(ref, cand), nested=json.load(open(d + '/truth.json'))['control'], atoms=rows)
    json.dump(stats, open(cd + '/stats.json', 'w'), indent=1)
    L = ['# Case %s' % nn, '',
         'Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.', '',
         '| | deposited | candidate |', '|---|---|---|']
    for k, lab in (('R1', 'R1'), ('wR2', 'wR2'), ('gof', 'GooF'), ('npar', 'parameters'), ('top_peak', 'largest Fo−Fc peak (e/Å³)'), ('hole', 'deepest hole (e/Å³)')):
        fmt = '%d' if k == 'npar' else '%.4f' if k in ('R1', 'wR2') else '%.2f'
        L.append('| %s | %s | %s |' % (lab, fmt % stats['ref'][k] if stats['ref'][k] is not None else '–', fmt % stats['cand'][k] if stats['cand'][k] is not None else '–'))
    h = stats['hamilton']
    L += ['', '**Hamilton R-test** (on wR2, an approximation; %s):' % ('the candidate extends the deposited model, so the models are nested' if stats['nested'] else '**not nested**: the deposited model already contains other disorder, so treat this as indicative only'),
          '%d extra parameters, R ratio %.4f, %s.' % (h['b'], h['ratio'], ('p = %.2g' % h['p']) if h.get('p') is not None else 'no improvement to test'), '',
          '**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model\'s difference map (map rms %.3f e/Å³):' % rms, '',
          '| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |', '|---|---|---|---|---|---|---|---|']
    for r_ in rows:
        L.append('| %s | %s | %d | %.3f | %.4f | %.2f | %.1f | %s %s |' % (r_['label'], r_['el'], r_['part'], r_['occ'], r_['ueq'], r_['rho'], r_['rho_sigma'], r_['nearest_deposited'], r_['dist']))
    L += ['', 'Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).', '']
    open(cd + '/case.md', 'w').write('\n'.join(L))
    print(nn, 'done', flush=True)


def index(root, out):
    key = json.load(open(out + '/_key.json'))
    L = ['# Adjudication: false positives that lower R1', '',
         '**Post-hoc.** This review was not part of the preregistered scoring and cannot change the pilot verdict. It feeds into the design of the next round.', '',
         'Each case is a structure in which one system modelled disorder that the published model does not have, and the result has a lower R1 than the published model. Case numbers are shuffled, and the folders do not say which system (rules or agent) made the candidate or whether the structure was a control. The key is in `_key.json`; open it only after you have filled in `decisions.csv`.', '',
         '**Blinding limits.** Atom labels like `C901` come from the rule-based system, and only controls are nested, so the `nested` column tells you which cases are controls. Try to judge the density and geometry, not the labels.', '',
         '**Negative extra parameters** in a non-nested case mean the published model has more parameters, because it models other disorder that the candidate does not; no test is computed. A negative ρ/rms means the candidate placed an atom where the published model\'s difference map has a hole.', '',
         '**Evidence sheets:** `EVIDENCE.md` and `caseNN/evidence.md` hold the computed checks (geometry against the other part, rigid-bond test, ADPs, map density and midpoints, Fourier-ripple distances, stability). Read them alongside Olex2; they flag things to look at and give no verdicts.', '',
         'For each case: open `caseNN/deposited.res` and `caseNN/candidate.res` in Olex2 (each has its `.hkl` beside it), read `caseNN/case.md`, then record a verdict in `decisions.csv`: `real` (genuine disorder the depositors missed), `overfit` (extra parameters fitting noise), `artefact` (density from absorption, series termination, twinning and so on), or `unsure`.', '',
         '| case | ΔR1 (cand − dep) | extra params | Hamilton p | nested | FP atoms | max ρ/rms at FP atoms |', '|---|---|---|---|---|---|---|']
    csv = ['case,verdict,confidence_1to3,notes']
    for nn in sorted(key):
        p = '%s/case%s/stats.json' % (out, nn)
        if not os.path.exists(p): L.append('| %s | not built | | | | | |' % nn); continue
        s = json.load(open(p)); h = s['hamilton']
        L.append('| [%s](case%s/case.md) | %+.4f | %d | %s | %s | %d | %s |' % (nn, nn, s['cand']['R1'] - s['ref']['R1'], h['b'],
                 ('%.2g' % h['p']) if h.get('p') is not None else '–', 'yes' if s['nested'] else 'no', len(s['atoms']),
                 ('%.1f' % max(a['rho_sigma'] for a in s['atoms'])) if s['atoms'] else '–'))
        csv.append('%s,,,' % nn)
    L += ['', 'The Hamilton test uses wR2 on F², not the F-based R of the original test, so its p values are approximate. Most cases add many parameters against thousands of reflections, so they can pass the test easily; treat a passing p as necessary, not sufficient.', '']
    open(out + '/README.md', 'w').write('\n'.join(L))
    if not os.path.exists(out + '/decisions.csv'): open(out + '/decisions.csv', 'w').write('\n'.join(csv) + '\n')


if __name__ == '__main__':
    root, cmd, out = sys.argv[1], sys.argv[2], sys.argv[3]
    if cmd == 'build':
        os.makedirs(out, exist_ok=True)
        order = list(CASES); random.Random(SEED).shuffle(order)
        json.dump({'%02d' % (k + 1): c for k, c in enumerate(order)}, open(out + '/_key.json', 'w'), indent=1)
        print(' '.join('%02d' % (k + 1) for k in range(len(order))))
    elif cmd == 'case': build_case(root, out, sys.argv[4])
    elif cmd == 'index': index(root, out)
