import sys, re, json, math
from cctbx import xray
from cctbx.array_family import flex
from iotbx.shelx import hklf
import smtbx.refinement
from smtbx.refinement import constraints, least_squares
from scitbx.lstbx import normal_eqns_solving
RESTR = ('DFIX', 'DANG', 'FLAT', 'CHIV', 'SADI', 'SIMU', 'DELU', 'RIGU', 'ISOR', 'SAME')
def strip_restraints(text):
    out, cont = [], False
    for line in text.splitlines():
        if cont: cont = line.rstrip().endswith('='); continue
        if line.split()[:1] and line.split()[0].upper().split('_')[0] in RESTR:
            cont = line.rstrip().endswith('='); continue
        out.append(line)
    return '\n'.join(out) + '\n'
import iotbx.shelx.parsers as _sp

def _occ_free_vars_fixed(self):
    # cctbx 2025.11 bug: the upstream loop reuses `i` for the scatterer index, so the
    # slice affine_occupancies[i:i+2] pairs the wrong atoms after the first pair.
    # Tie every member of a free-variable group to the group's first atom instead.
    if not self.builder_does_occupancy_pair_affine_constraint: return
    for free_var_idx, members in self.occupancies_depending_on_free_variable.items():
        if len(members) < 2: continue
        a, b, i0 = members[0]
        for a1, b1, i1 in members[1:]:
            self.builder.add_occupancy_pair_affine_constraint(
                scatterer_indices=(i0, i1), linear_form=((1 / a, -1 / a1), b - b1))

for _name in dir(_sp):
    _cls = getattr(_sp, _name)
    if isinstance(_cls, type) and 'process_occupancies_depending_on_free_variable' in vars(_cls):
        _cls.process_occupancies_depending_on_free_variable = _occ_free_vars_fixed

P = sys.argv[1]; mode = sys.argv[2]; ids = sys.argv[3:]
meta = {d['id']: d for d in json.load(open(P + '/disordered.json'))}

def load_obs(res, hkl_path, cs, wl):
    obs = hklf.reader(file_object=open(hkl_path)).as_miller_arrays(crystal_symmetry=cs)[0]
    anom = not cs.space_group().is_centric()
    obs = obs.customized_copy(anomalous_flag=anom).merge_equivalents().array()
    omit = set(tuple(int(v) for v in mm.groups()) for mm in re.finditer(r'^OMIT\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s*$', res, re.M | re.I))
    if omit: obs = obs.select(flex.bool([tuple(h) not in omit and tuple(-x for x in h) not in omit for h in obs.indices()]))
    m = re.search(r'^SHEL\s+(\S+)\s+(\S+)', res, re.M | re.I)
    if m: obs = obs.resolution_filter(d_max=float(m.group(1)), d_min=float(m.group(2)))
    m = re.search(r'^OMIT\s+(-?[\d.]+)\s+([\d.]+)\s*$', res, re.M | re.I)
    s_lim, tt = (float(m.group(1)), float(m.group(2))) if m else (-2.0, 180.0)
    obs = obs.select(obs.data() >= s_lim * obs.sigmas())
    if tt < 180: obs = obs.resolution_filter(d_min=wl / (2 * math.sin(math.radians(tt / 2))))
    return obs

def resolve_fvar_targets(res):
    # SHELX DFIX/DANG target 10*m+p (|m|>1) means p*fv(m) (or p*(fv(m)-1) if negative); smtbx reads it literally
    fv = [1.0] + [float(x) for x in re.search(r'^FVAR\s+(.*)$', res, re.M | re.I).group(1).split()[1:]]
    def sub(mt):
        val = float(mt.group(2)); m = int(abs(val) // 10)
        if m < 2 or m > len(fv): return mt.group(0)
        p = abs(val) - 10 * m; d = p * fv[m - 1] if val > 0 else p * (fv[m - 1] - 1)
        return '%s %.4f' % (mt.group(1), abs(d))
    return re.sub(r'^((?:DFIX|DANG)(?:_\S+)?)\s+(-?\d+(?:\.\d*)?)(?=\s)', sub, res, flags=re.M | re.I)

def fix_afix_group(res, parent):
    # Replace the AFIX group riding on `parent` with H atoms at fixed (10+x) deposited coordinates
    lines = res.splitlines(); out = []; state = 0
    for ln in lines:
        tok = ln.split()
        if state == 0 and tok and tok[0].upper() == parent.upper(): state = 1
        elif state == 1 and tok[:1] and tok[0].upper() == 'AFIX' and tok[1] != '0': state = 2; continue
        elif state == 2:
            if tok[:1] and tok[0].upper() == 'AFIX': state = 3; continue
            if len(tok) >= 5:
                for k in (2, 3, 4): tok[k] = '%.6f' % (10 + float(tok[k]))
                ln = ' '.join(tok)
        out.append(ln)
    return '\n'.join(out) + '\n'

def occs(xs): return [s.occupancy for s in xs.scatterers() if s.scattering_type != 'H']

def refine(i, restrained, cycles=40):
    d = P + '/work/' + i; res = open(d + '/model.res').read()
    res = resolve_fvar_targets(res)
    if not restrained: res = strip_restraints(res)
    path = d + '/run2_%s.res' % ('r' if restrained else 'u')
    wl = float(re.search(r'^CELL\s+(\S+)', res, re.M | re.I).group(1))
    fixed = []
    for attempt in range(10):
        open(path, 'w').write(res)
        m0 = smtbx.refinement.model.from_shelx(ins_or_res=path, hkl=d + '/data.hkl', strictly_shelxl=False)
        try:
            constraints.reparametrisation(m0.xray_structure, m0.constraints, m0.connectivity_table); break
        except Exception as e:
            mt = re.search(r'involving (\S+?):', str(e))
            if not mt or mt.group(1) in fixed: raise
            fixed.append(mt.group(1)); res = fix_afix_group(res, mt.group(1))
    global FIXED; FIXED = fixed
    obs = load_obs(res, d + '/data.hkl', m0.xray_structure.crystal_symmetry(), wl)
    xs = m0.xray_structure; xs.set_inelastic_form_factors(photon=wl, table='sasaki')
    mm = re.search(r'^EXTI\s+(\S+)', res, re.M | re.I)
    ext = None
    if mm:
        ext = xray.shelx_extinction_correction(xs.unit_cell(), wl, value=float(mm.group(1))); ext.grad = True
    rep = constraints.reparametrisation(xs, m0.constraints, m0.connectivity_table, extinction=ext) if ext else \
          constraints.reparametrisation(xs, m0.constraints, m0.connectivity_table)
    ls = least_squares.crystallographic_ls(obs.as_xray_observations(), rep,
        restraints_manager=m0.restraints_manager, weighting_scheme=m0.weighting_scheme)
    o0 = occs(xs); ls.build_up(); r_start = ls.r1_factor(cutoff_factor=2)[0]
    if mode == 'lm':
        it = normal_eqns_solving.levenberg_marquardt_iterations(ls, n_max_iterations=cycles, gradient_threshold=1e-7, step_threshold=1e-7)
    else:
        it = normal_eqns_solving.naive_iterations_with_damping_and_shift_limit(ls, n_max_iterations=cycles, gradient_threshold=1e-7, step_threshold=1e-7)
    ls.build_up(); r_end = ls.r1_factor(cutoff_factor=2)[0]
    dmax = max(abs(a - b) for a, b in zip(o0, occs(xs)))
    global LAST; LAST = [(s.label, a, s.occupancy) for s, a in zip([s for s in xs.scatterers() if s.scattering_type != 'H'], o0)]
    return r_start, r_end, it.n_iterations, dmax, ext.value if ext else None

if __name__ == '__main__':
    for i in ids:
        dep = float(meta[i]['R1']); line = '%s dep %.4f' % (i, dep)
        for restrained in (True, False):
            tag = 'RESTR' if restrained else 'UNRES'
            try:
                r0, r1, n, dmax, ev = refine(i, restrained)
                line += ' | %s %.4f->%.4f (%+.4f) %dit dOcc %.3f%s%s' % (tag, r0, r1, r1 - dep, n, dmax, ' exti %.4f' % ev if ev is not None else '', ' fixedH:' + ','.join(FIXED) if FIXED else '')
            except Exception as e:
                line += ' | %s ERROR %s %s' % (tag, type(e).__name__, str(e)[:80])
        print(line, flush=True)
