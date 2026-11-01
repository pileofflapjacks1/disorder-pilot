"""Shared library for the disorder pilot: SHELX .res parsing/writing, smtbx refinement, difference maps.

Engine fixes from week 1 (tools/refine2.py) are carried over: sasaki f'/f'', EXTI, SHELXL-style
reflection filtering, free-variable DFIX/DANG targets, AFIX fallback, and the cctbx occupancy-link patch.
"""
import re, math
from cctbx import xray, adptbx, maptbx
from cctbx.array_family import flex
from iotbx.shelx import hklf
import smtbx.refinement
from smtbx.refinement import constraints, least_squares
from scitbx.lstbx import normal_eqns_solving
import iotbx.shelx.parsers as _sp


def _occ_free_vars_fixed(self):
    # cctbx 2025.11 bug: the upstream loop reuses `i` for the scatterer index, so the
    # slice affine_occupancies[i:i+2] pairs the wrong atoms after the first pair.
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

RESTR = ('DFIX', 'DANG', 'FLAT', 'CHIV', 'SADI', 'SIMU', 'DELU', 'RIGU', 'ISOR', 'SAME', 'BUMP', 'NCSY')
# smtbx silently ignores these; the pilot rejects them instead (week-1 design rule)
UNSUPPORTED = ('EADP', 'SAME', 'SUMP', 'TWIN', 'BASF', 'ABIN', 'SWAT', 'EXYZ', 'NCSY', 'FREE', 'SPEC', 'BLOC', 'HFIX', 'RTAB')
# instructions dropped when tasks are generated: output/listing only, no effect on the model
COSMETIC = ('ACTA', 'CONF', 'BOND', 'LIST', 'MORE', 'FMAP', 'PLAN', 'BIND', 'HTAB', 'MPLA', 'SIZE', 'TEMP', 'REM',
            'WPDB', 'L.S.', 'CGLS', 'ZERR', 'GRID', 'EQIV', 'MERG', 'OMIT_', 'DAMP', 'STIR', 'TITL', 'CONN')
CARD = ('CELL', 'LATT', 'SYMM', 'SFAC', 'UNIT', 'DISP', 'OMIT', 'SHEL', 'WGHT', 'EXTI', 'FVAR', 'HKLF', 'END', 'ANIS', 'PART', 'AFIX', 'RESI')
COV = {'H': 0.32, 'B': 0.85, 'C': 0.77, 'N': 0.71, 'O': 0.66, 'F': 0.64, 'SI': 1.17, 'P': 1.10, 'S': 1.04, 'CL': 0.99,
       'BR': 1.14, 'I': 1.33, 'SE': 1.17, 'AS': 1.21, 'GE': 1.22, 'SN': 1.40, 'TE': 1.37}


# ---------------------------------------------------------------- .res text handling
def logical_lines(text):
    """Join SHELX '=' continuation lines; returns list of strings (one per instruction/atom)."""
    out, buf = [], None
    for ln in text.splitlines():
        if buf is not None:
            buf += ' ' + ln.strip()
        else:
            buf = ln.rstrip()
        if buf.rstrip().endswith('=') and not buf.upper().startswith(('REM', 'TITL')):
            buf = buf.rstrip()[:-1]
            continue
        out.append(buf); buf = None
    if buf is not None: out.append(buf)
    return out


def keyword(line):
    t = line.split()
    return t[0].upper() if t else ''


def is_atom_line(line, sfac_n):
    t = line.split()
    if len(t) < 5 or keyword(line) in CARD + RESTR + UNSUPPORTED + COSMETIC: return False
    if keyword(line).split('_')[0] in RESTR: return False
    try:
        k = int(t[1]); [float(x) for x in t[2:5]]
    except ValueError:
        return False
    return 1 <= k <= sfac_n


class Model:
    """A SHELX model as a list of logical lines; atoms are dicts referencing their line index."""

    def __init__(self, text):
        lines = logical_lines(text)
        end = next((i for i, l in enumerate(lines) if keyword(l) == 'HKLF'), len(lines))
        self.lines = lines[:end + 1] + ['END']
        self.parse()

    def parse(self):
        sfac = next(l for l in self.lines if keyword(l) == 'SFAC').split()[1:]
        self.sfac = [s.upper() for s in sfac if re.match(r'^[A-Za-z]{1,2}$', s)]
        fl = next((l for l in self.lines if keyword(l) == 'FVAR'), None)
        self.fvar = [float(x) for x in fl.split()[1:]] if fl else [1.0]
        self.cell = [float(x) for x in next(l for l in self.lines if keyword(l) == 'CELL').split()[1:8]]
        self.atoms = []; part = 0; afix = 0; resi = ''
        for i, l in enumerate(self.lines):
            k = keyword(l)
            if k == 'PART': part = int(l.split()[1])
            elif k == 'AFIX': afix = int(l.split()[1])
            elif k == 'RESI': resi = ' '.join(l.split()[1:3])
            elif is_atom_line(l, len(self.sfac)):
                t = l.split()
                a = dict(idx=i, label=t[0], el=self.sfac[int(t[1]) - 1], xyz=[float(x) for x in t[2:5]],
                         occ_code=float(t[5]) if len(t) > 5 else 11.0, u=[float(x) for x in t[6:12]] or [0.05],
                         part=part, afix=afix, resi=resi)
                a['occ'] = self.occ_value(a['occ_code'])
                self.atoms.append(a)
        return self

    def occ_value(self, code):
        c = abs(code); m = int(c // 10); p = c - 10 * m
        if m == 0: return code
        if m == 1: return p
        fv = self.fvar[m - 1] if m - 1 < len(self.fvar) else 1.0
        return p * fv if code > 0 else p * (1 - fv)

    def text(self):
        return '\n'.join(self.lines) + '\n'

    def heavy(self):
        return [a for a in self.atoms if a['el'] != 'H']

    def unsupported(self):
        return sorted(set(keyword(l) for l in self.lines if keyword(l).split('_')[0] in UNSUPPORTED or keyword(l) == 'HKLF' and l.split()[1:2] == ['5']))


def fmt_atom(label, sfac_idx, xyz, occ_code, u):
    s = '%-5s %d %10.6f %10.6f %10.6f %10.5f' % (label, sfac_idx, xyz[0], xyz[1], xyz[2], occ_code)
    s += ''.join(' %9.5f' % x for x in u)
    return s


# ---------------------------------------------------------------- geometry
def bonded_pairs(xs, els, tol=0.45):
    """Covalent contacts (i, j, d) incl. symmetry, from covalent radii; els = element per scatterer."""
    sc = xs.scatterers(); out = []
    for i in range(len(sc)):
        for j in range(i, len(sc)):
            d = min_image_dist(xs, sc[i].site, sc[j].site) if i != j else 9
            if 0.1 < d < COV.get(els[i], 1.5) + COV.get(els[j], 1.5) + tol: out.append((i, j, d))
    return out


# ---------------------------------------------------------------- refinement
def load_obs(res_text, hkl_path, cs, wl):
    obs = hklf.reader(file_object=open(hkl_path)).as_miller_arrays(crystal_symmetry=cs)[0]
    anom = not cs.space_group().is_centric()
    obs = obs.customized_copy(anomalous_flag=anom).merge_equivalents().array()
    omit = set(tuple(int(v) for v in mm.groups()) for mm in re.finditer(r'^OMIT\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s*$', res_text, re.M | re.I))
    if omit: obs = obs.select(flex.bool([tuple(h) not in omit and tuple(-x for x in h) not in omit for h in obs.indices()]))
    m = re.search(r'^SHEL\s+(\S+)\s+(\S+)', res_text, re.M | re.I)
    if m: obs = obs.resolution_filter(d_max=float(m.group(1)), d_min=float(m.group(2)))
    m = re.search(r'^OMIT\s+(-?[\d.]+)\s+([\d.]+)\s*$', res_text, re.M | re.I)
    s_lim, tt = (float(m.group(1)), float(m.group(2))) if m else (-2.0, 180.0)
    obs = obs.select(obs.data() >= s_lim * obs.sigmas())
    if tt < 180: obs = obs.resolution_filter(d_min=wl / (2 * math.sin(math.radians(tt / 2))))
    return obs


def resolve_fvar_targets(res):
    m0 = re.search(r'^FVAR\s+(.*)$', res, re.M | re.I)
    fv = [1.0] + ([float(x) for x in m0.group(1).split()[1:]] if m0 else [])
    def sub(mt):
        val = float(mt.group(2)); m = int(abs(val) // 10)
        if m < 2 or m > len(fv): return mt.group(0)
        p = abs(val) - 10 * m; d = p * fv[m - 1] if val > 0 else p * (fv[m - 1] - 1)
        return '%s %.4f' % (mt.group(1), abs(d))
    return re.sub(r'^((?:DFIX|DANG)(?:_\S+)?)\s+(-?\d+(?:\.\d*)?)(?=\s)', sub, res, flags=re.M | re.I)


def fix_afix_group(res, parent):
    lines = res.splitlines(); out = []; state = 0
    for ln in lines:
        tok = ln.split()
        if state == 0 and tok and tok[0].upper() == parent.upper(): state = 1
        elif state == 1 and tok[:1] and tok[0].upper() == 'AFIX' and tok[1] != '0': state = 2; continue
        elif state == 2:
            if tok[:1] and tok[0].upper() == 'AFIX': state = 3; continue
            if len(tok) >= 5:
                for k in (2, 3, 4): tok[k] = '%.6f' % (10 + float(tok[k]) % 10 if abs(float(tok[k])) > 5 else 10 + float(tok[k]))
                ln = ' '.join(tok)
        out.append(ln)
    return '\n'.join(out) + '\n'


AFIX_NEIGH = {1: 3, 2: 2, 4: 2, 3: 1, 13: 1, 8: 1, 14: 1, 15: 1, 9: 1, 12: 1, 16: 1}


def fix_bad_afix(res):
    """Riding-H groups whose parent no longer has the bond count the AFIX type needs (e.g. after a disordered
    neighbour was removed) are converted to fixed-coordinate H atoms. Returns text; FIXED_LOG lists parents."""
    from cctbx import xray as _x
    m = Model(res)
    xs = _x.structure.from_shelx(file=_lines(m.text()))
    els = [a['el'] for a in m.atoms]
    nb = [0] * len(m.atoms)
    for i, j, d in bonded_pairs_heavy(xs, els): nb[i] += 1; nb[j] += 1
    bad = []
    for k, a in enumerate(m.atoms):
        if a['el'] == 'H' or k + 1 >= len(m.atoms): continue
        h = m.atoms[k + 1]
        if h['el'] != 'H' or h['afix'] == 0: continue
        need = AFIX_NEIGH.get(h['afix'] // 10)
        if need is not None and nb[k] != need: bad.append(a['label'])
    global FIXED_LOG; FIXED_LOG = bad
    for lab in bad: res = fix_afix_group(res, lab)
    return res


def bonded_pairs_heavy(xs, els, tol=0.45):
    sc = xs.scatterers(); idx = [k for k, e in enumerate(els) if e != 'H']; out = []
    for p, i in enumerate(idx):
        for j in idx[p:]:
            d = min_image_dist(xs, sc[i].site, sc[j].site) if i != j else min_self_dist(xs, sc[i].site)
            if 0.1 < d < COV.get(els[i], 1.5) + COV.get(els[j], 1.5) + tol: out.append((i, j, d))
    return out


def min_self_dist(xs, a):
    uc = xs.unit_cell(); ops = xs.space_group().all_ops()[1:]
    return min([_min_image(uc, a, op * a) for op in ops] or [9])


class _lines:
    def __init__(self, t): self.t = t.splitlines(True)
    def __iter__(self): return iter(self.t)
    def readlines(self): return self.t
    def read(self): return ''.join(self.t)


class Result:
    pass


RIDING_M = (1, 2, 3, 4, 8, 9, 12, 13, 14, 15, 16)


def reissue_afix_after_part(text):
    """SHELXL lets riding H of both PARTs hang off one parent (AFIX 23 / PART 1 H H / [AFIX 23] PART 2 H H), with the
    pivot being the last non-H atom; cctbx takes the preceding atom as pivot, so the second group fails to parse.
    The second group's H are written as fixed-coordinate H at their deposited positions (logged in AFIX_FIXED_LOG);
    open riding groups are closed before the next non-H atom."""
    global AFIX_FIXED_LOG; AFIX_FIXED_LOG = []
    lines = text.splitlines()
    sl = next((l for l in lines if keyword(l) == 'SFAC'), '')
    sfac = [x.upper() for x in sl.split()[1:] if re.match(r'^[A-Za-z]{1,2}$', x)]
    out = []; code = 0; nh = 0; last_h = False; fixing = False
    for l in lines:
        k = keyword(l)
        riding = code and (code // 10) in RIDING_M
        if k == 'AFIX':
            c = int(float(l.split()[1]))
            if c and (c // 10) in RIDING_M and last_h:
                out.append('AFIX 0'); code = 0; fixing = True; continue
            code = c; nh = 0; fixing = False
        elif k == 'PART' and riding and nh:
            out.append('AFIX 0'); code = 0; fixing = True
        elif sfac and is_atom_line(l, len(sfac)):
            t = l.split()
            if sfac[int(t[1]) - 1] == 'H':
                nh += 1; last_h = True
                if fixing:
                    for q in (2, 3, 4):
                        v = float(t[q]); t[q] = '%.6f' % (v if abs(v) > 5 else 10 + v)
                    l = ' '.join(t); AFIX_FIXED_LOG.append(t[0])
            else:
                last_h = False; fixing = False
                if riding and nh: out.append('AFIX 0'); code = 0
            nh = nh if sfac[int(t[1]) - 1] == 'H' else 0
        out.append(l)
    return '\n'.join(out) + '\n'


def refine(res_text, hkl_path, workfile, cycles=40, damping=True):
    """Refine a res text with smtbx; returns Result with stats, the refined Model text and the ls object."""
    res_text = reissue_afix_after_part(res_text)
    model = Model(res_text)
    bad = model.unsupported()
    if bad: raise ValueError('unsupported instructions (smtbx would ignore them silently): ' + ' '.join(bad))
    res = resolve_fvar_targets(model.text())
    wl = model.cell[0]
    fixed = []
    for attempt in range(10):
        open(workfile, 'w').write(res)
        m0 = smtbx.refinement.model.from_shelx(ins_or_res=workfile, hkl=hkl_path, strictly_shelxl=False)
        try:
            constraints.reparametrisation(m0.xray_structure, m0.constraints, m0.connectivity_table); break
        except Exception as e:
            mt = re.search(r'involving (\S+?):', str(e))
            if not mt or mt.group(1) in fixed: raise
            fixed.append(mt.group(1)); res = fix_afix_group(res, mt.group(1))
    xs = m0.xray_structure; xs.set_inelastic_form_factors(photon=wl, table='sasaki')
    obs = load_obs(res, hkl_path, xs.crystal_symmetry(), wl)
    mm = re.search(r'^EXTI\s+(\S+)', res, re.M | re.I); ext = None
    if mm:
        ext = xray.shelx_extinction_correction(xs.unit_cell(), wl, value=float(mm.group(1))); ext.grad = True
    kw = dict(extinction=ext) if ext else {}
    rep = constraints.reparametrisation(xs, m0.constraints, m0.connectivity_table, **kw)
    ls = least_squares.crystallographic_ls(obs.as_xray_observations(), rep,
        restraints_manager=m0.restraints_manager, weighting_scheme=m0.weighting_scheme)
    ls.build_up()
    if damping:
        it = normal_eqns_solving.naive_iterations_with_damping_and_shift_limit(ls, n_max_iterations=cycles, gradient_threshold=1e-7, step_threshold=1e-7)
    else:
        it = normal_eqns_solving.levenberg_marquardt_iterations(ls, n_max_iterations=cycles, gradient_threshold=1e-7, step_threshold=1e-7)
    ls.build_up()
    r = Result()
    r.ls, r.xs, r.obs, r.ext, r.fixedH, r.n_iter = ls, xs, obs, ext, fixed, it.n_iterations
    r.r1 = ls.r1_factor(cutoff_factor=2)[0]
    r.wr2 = ls.wR2(); r.gof = ls.goof(); r.npar = ls.reparametrisation.n_independents
    r.n_obs = obs.size()
    r.model_text = write_back(model, xs, ext)
    return r


def write_back(model, xs, ext):
    """Write refined coordinates/ADPs/occupancies back into the res text (keeps AFIX/PART/restraints)."""
    uc = xs.unit_cell(); scs = xs.scatterers()
    if len(scs) != len(model.atoms):
        raise RuntimeError('scatterer/atom count mismatch %d vs %d' % (len(scs), len(model.atoms)))
    lines = list(model.lines)
    fv = list(model.fvar)
    for a, s in zip(model.atoms, scs):
        c = abs(a['occ_code']); m = int(c // 10); p = c - 10 * m
        if m >= 2 and p > 0 and m - 1 < len(fv):
            fv[m - 1] = s.occupancy / p if a['occ_code'] > 0 else 1 - s.occupancy / p
    fv[0] = 1.0  # overall scale is handled by smtbx internally; keep a placeholder
    for a, s in zip(model.atoms, scs):
        t = lines[a['idx']].split()
        xyz = [x + 10 if abs(o) > 5 else x for x, o in zip(s.site, a['xyz'])]
        if a['u'] and a['u'][0] < 0:
            u = a['u'][:1]
        elif s.flags.use_u_aniso():
            u = list(adptbx.u_star_as_u_cif(uc, s.u_star)); u = [u[0], u[1], u[2], u[5], u[4], u[3]]
        else:
            u = [s.u_iso]
        occ = a['occ_code']
        if int(abs(occ) // 10) == 0: occ = s.occupancy
        lines[a['idx']] = fmt_atom(t[0], int(t[1]), xyz, occ, u)
    for i, l in enumerate(lines):
        if keyword(l) == 'FVAR':
            lines[i] = 'FVAR ' + ' '.join('%.5f' % x for x in fv)
        if keyword(l) == 'EXTI' and ext is not None:
            lines[i] = 'EXTI %.6f' % ext.value
    return '\n'.join(lines) + '\n'


def diff_peaks(r, n=20, min_height=0.0):
    """Fo-Fc peaks (e/A^3) with their nearest atoms. Uses the refined scale, weighting-independent F map."""
    ls, xs, obs = r.ls, r.xs, r.obs
    if obs.anomalous_flag(): obs = obs.average_bijvoet_mates()
    fc = obs.structure_factors_from_scatterers(xs, algorithm='direct').f_calc()
    k = ls.scale_factor()
    fo = flex.sqrt(flex.double([max(v, 0) for v in obs.data()]) / k)
    fmod = flex.abs(fc.data())
    ok = fmod > 1e-6
    fo, fmod, fc = fo.select(ok), fmod.select(ok), fc.select(ok)
    ratio = (fo - fmod) / fmod
    coeff = fc.customized_copy(data=fc.data() * flex.complex_double(ratio, flex.double(ratio.size(), 0)))
    fft = coeff.fft_map(resolution_factor=1 / 4.0, symmetry_flags=maptbx.use_space_group_symmetry)
    fft.apply_volume_scaling()
    m = fft.real_map_unpadded()
    rms = flex.mean_sq(m.as_1d()) ** 0.5
    ps = fft.peak_search(parameters=maptbx.peak_search_parameters(peak_search_level=1, max_peaks=n * 4, interpolate=True,
                          min_distance_sym_equiv=0.5), verify_symmetry=False).all(max_clusters=n * 4)
    peaks = []
    labels = [s.label for s in xs.scatterers()]
    for site, h in zip(ps.sites(), ps.heights()):
        if h < min_height: continue
        near = nearest_atoms(xs, site, k=3)
        peaks.append(dict(site=tuple(site), height=h, near=[(labels[j], d) for j, d in near]))
        if len(peaks) >= n: break
    holes = flex.min(m.as_1d())
    return peaks, rms, holes


def nearest_atoms(xs, site, k=3, cutoff=3.5):
    best = sorted(((j, min_image_dist(xs, site, s.site)) for j, s in enumerate(xs.scatterers())), key=lambda t: t[1])
    return [b for b in best[:k] if b[1] < cutoff]


def _min_image(uc, a, b):
    d = [x - y for x, y in zip(a, b)]
    d = [x - round(x) for x in d]
    return uc.length(d)


def min_image_dist(xs, a, b):
    uc = xs.unit_cell()
    return min(_min_image(uc, a, op * b) for op in xs.space_group().all_ops())


def u_eigen(uc, u_cif6):
    """Principal values (descending) and vectors (fractional) of a SHELX-order Uij (U11 U22 U33 U23 U13 U12)."""
    import numpy as np
    U11, U22, U33, U23, U13, U12 = u_cif6
    u_cart = adptbx.u_cif_as_u_cart(uc, (U11, U22, U33, U12, U13, U23))
    M = np.array([[u_cart[0], u_cart[3], u_cart[4]], [u_cart[3], u_cart[1], u_cart[5]], [u_cart[4], u_cart[5], u_cart[2]]])
    w, v = np.linalg.eigh(M)
    order = w.argsort()[::-1]
    return w[order], v[:, order]


def ueq_and_axes(uc, a):
    """(Ueq, eigenvalues desc, eigenvectors cart) for an atom dict; iso atoms return (u, [u]*3, None)."""
    if len(a['u']) == 6:
        w, v = u_eigen(uc, a['u']); return float(sum(w) / 3), [float(x) for x in w], v
    u = a['u'][0]; return u, [u] * 3, None


def npd_atoms(model, uc):
    bad = []
    for a in model.heavy():
        ueq, w, _ = ueq_and_axes(uc, a)
        if (len(a['u']) == 6 and min(w) <= 0) or (len(a['u']) == 1 and a['u'][0] <= 0): bad.append(a['label'])
    return bad


def fvar_values(model_text):
    return Model(model_text).fvar


def frac_xyz(a):
    return [x - 10 if x > 5 else (x + 10 if x < -5 else x) for x in a['xyz']]
