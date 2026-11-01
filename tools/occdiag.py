import sys, re, importlib.util
P = sys.argv[1]; i = sys.argv[2]
spec = importlib.util.spec_from_file_location('r2', P + '/tools/refine2.py'); r2 = importlib.util.module_from_spec(spec)
sys.argv = ['x', P, 'damp']; spec.loader.exec_module(r2)
import smtbx.refinement
res = open(P + '/work/%s/model.res' % i).read()
fv = res and re.search(r'^FVAR\s+(.*)$', res, re.M | re.I).group(1)
print('FVAR', fv)
codes = {}
for ln in res.splitlines():
    t = ln.split()
    if len(t) >= 6 and re.match(r'^[A-Za-z]', t[0]) and t[0].upper() not in ('FVAR','AFIX','PART','REM','SFAC','UNIT','CELL','ZERR','LATT','SYMM','DFIX','SADI','SIMU','RIGU','DELU','ISOR','EQIV','HTAB','CONF','BOND','WGHT','EXTI','FMAP','PLAN','LIST','L.S.','ACTA','SIZE','TEMP','OMIT','SHEL','HKLF','END','TITL','MORE','DANG','FLAT','EADP','SAME','SUMP','FREE','ANIS','MPLA','SWAT','BASF','TWIN','ABIN','CHIV','BIND'):
        try: codes[t[0].upper()] = float(t[5])
        except ValueError: pass
r0 = r2.occs  # placeholder
import smtbx.refinement as sr
orig = r2.refine
def refine_capture(i, restrained, cycles=40):
    d = P + '/work/' + i
    out = orig(i, restrained, cycles)
    return out
# rerun manually to access structure
d = P + '/work/' + i
m0 = sr.model.from_shelx(ins_or_res=d + '/run2_r.res', hkl=d + '/data.hkl', strictly_shelxl=False)
before = {s.label.upper(): s.occupancy for s in m0.xray_structure.scatterers()}
grads = {s.label.upper(): s.flags.grad_occupancy() for s in m0.xray_structure.scatterers()}
print('atoms with refinable occupancy flag:', sum(grads.values()), 'of', len(grads))
weird = [(k, codes.get(k), round(before[k], 3)) for k in before if k in codes and abs(codes[k]) > 15 and abs(codes[k]) < 20]
print('occupancy codes not 1x/2x/-2x (sample):', sorted(set(round(c) for c in codes.values() if abs(c) >= 20))[:20])
print('first partial atoms:', [(k, codes.get(k), round(v, 3)) for k, v in before.items() if v < 0.999][:12])
