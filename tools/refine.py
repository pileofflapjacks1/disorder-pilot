import sys, re, json, os, io
import smtbx.refinement
from scitbx.lstbx import normal_eqns_solving
P = sys.argv[1]; ids = sys.argv[2:]
meta = {d['id']: d for d in json.load(open(P + '/disordered.json'))}
RESTR = ('DFIX', 'DANG', 'FLAT', 'CHIV', 'SADI', 'SIMU', 'DELU', 'RIGU', 'ISOR', 'SAME')
def strip_restraints(text):
    out, cont = [], False
    for line in text.splitlines():
        if cont: cont = line.rstrip().endswith('='); continue
        if line.split()[:1] and line.split()[0].upper().split('_')[0] in RESTR:
            cont = line.rstrip().endswith('='); continue
        out.append(line)
    return '\n'.join(out) + '\n'
def occs(xs):
    return [(s.label, s.occupancy) for s in xs.scatterers() if s.scattering_type != 'H']
def refine(i, restrained):
    d = P + '/work/' + i; tag = 'r' if restrained else 'u'
    txt = open(d + '/model.res').read()
    if not restrained: txt = strip_restraints(txt)
    open(d + '/run_%s.res' % tag, 'w').write(txt)
    m = smtbx.refinement.model.from_shelx(ins_or_res=d + '/run_%s.res' % tag, hkl=d + '/data.hkl', strictly_shelxl=False)
    ls = m.least_squares(); ls.build_up()
    r0 = ls.r1_factor(cutoff_factor=2)[0]; o0 = occs(m.xray_structure)
    it = normal_eqns_solving.levenberg_marquardt_iterations(ls, n_max_iterations=15, gradient_threshold=1e-6, step_threshold=1e-6)
    ls.build_up()
    r1 = ls.r1_factor(cutoff_factor=2)[0]
    nrest = ls.restraints_manager.n_restraints() if hasattr(ls.restraints_manager, 'n_restraints') else '?'
    o1 = occs(m.xray_structure)
    dmax = max(abs(a[1] - b[1]) for a, b in zip(o0, o1))
    return r0, r1, dmax, None, it.n_iterations, nrest
for i in ids:
    dep = float(meta[i]['R1']); line = '%s dep R1 %.4f' % (i, dep)
    for restrained in (True, False):
        try:
            r0, r1, o0, o1, n, nr = refine(i, restrained)
            line += ' | %s start %.4f -> %.4f (%d it) max dOcc %.3f' % ('RESTR' if restrained else 'UNRESTR', r0, r1, n, o0)
        except Exception as e:
            line += ' | %s ERROR %s %s' % ('RESTR' if restrained else 'UNRESTR', type(e).__name__, str(e)[:90])
    print(line, flush=True)
