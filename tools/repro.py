import sys, re, math, json
from cctbx.array_family import flex
import iotbx.shelx
from iotbx.shelx import hklf
P = sys.argv[1]; ids = sys.argv[2:]
meta = {d['id']: d for d in json.load(open(P + '/disordered.json'))}
def run(i):
    d = P + '/work/' + i; res = open(d + '/model.res').read()
    from cctbx import xray; xs = xray.structure.from_shelx(file=open(d + "/model.res"))
    wl = float(re.search(r'^CELL\s+(\S+)', res, re.M | re.I).group(1))
    xs.set_inelastic_form_factors(photon=wl, table='sasaki')
    m = re.search(r'^EXTI\s+(\S+)', res, re.M | re.I); exti = float(m.group(1)) if m else 0.0
    omit = set(tuple(int(v) for v in mm.groups()) for mm in re.finditer(r'^OMIT\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)', res, re.M | re.I))
    m = re.search(r'^SHEL\s+(\S+)\s+(\S+)', res, re.M | re.I); shel = (float(m.group(1)), float(m.group(2))) if m else None
    obs = hklf.reader(file_object=open(d + '/data.hkl')).as_miller_arrays(crystal_symmetry=xs.crystal_symmetry())[0]
    obs = obs.select(obs.indices() != (0, 0, 0)) if False else obs
    anom = not xs.space_group().is_centric()
    obs = obs.customized_copy(anomalous_flag=anom).merge_equivalents().array()
    if omit:
        keep = flex.bool([tuple(h) not in omit and tuple(-x for x in h) not in omit for h in obs.indices()]); obs = obs.select(keep)
    if shel: obs = obs.resolution_filter(d_max=shel[0], d_min=shel[1])
    m = re.search(r'^OMIT\s+(-?[\d.]+)\s+([\d.]+)\s*$', res, re.M | re.I)
    s_lim, tt_lim = (float(m.group(1)), float(m.group(2))) if m else (-2.0, 180.0)
    obs = obs.select(obs.data() >= s_lim * obs.sigmas())
    if tt_lim < 180: obs = obs.resolution_filter(d_min=wl / (2 * math.sin(math.radians(tt_lim / 2))))
    fc = obs.structure_factors_from_scatterers(xs, algorithm='direct').f_calc()
    fc2 = flex.pow2(flex.abs(fc.data()))
    if exti:
        s2t = flex.sin(2 * flex.asin(flex.double(wl / (2 * x) for x in obs.d_spacings().data())))
        fc2 = fc2 / flex.sqrt(1 + 0.001 * exti * fc2 * wl ** 3 / s2t)
    I, sI = obs.data(), obs.sigmas()
    k = flex.sum(I * fc2) / flex.sum(fc2 * fc2)
    fo = flex.sqrt(flex.double([max(v, 0) for v in I])); fcs = flex.sqrt(k * fc2)
    gt = I > 2 * sI
    r1 = flex.sum(flex.abs(fo - fcs).select(gt)) / flex.sum(fo.select(gt))
    return r1, obs.size(), gt.count(True), anom, exti
out = []
for i in ids:
    try:
        r1, n, ngt, anom, exti = run(i); dep = float(meta[i]['R1'])
        out.append((i, dep, r1)); print('%s deposited R1 %.4f  cctbx R1 %.4f  diff %+.4f  refl %d (gt %d) anom=%s EXTI=%s' % (i, dep, r1, r1 - dep, n, ngt, anom, exti))
    except Exception as e:
        print(i, 'ERROR', type(e).__name__, str(e)[:150])
