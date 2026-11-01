import sys, os, json, gemmi
P = sys.argv[1]; rows = json.load(open(P + '/survey.json'))
dis = [r for r in rows if r.get('groups') and r.get('partial') and r.get('res')]
out = []
for r in dis:
    i = r['id']; path = P + '/data/cif/%s/%s/%s/%s.cif' % (i[0], i[1:3], i[3:5], i)
    b = gemmi.cif.read(path).sole_block()
    res = gemmi.cif.as_string(b.find_value('_shelx_res_file')); hkl = gemmi.cif.as_string(b.find_value('_shelx_hkl_file'))
    d = P + '/work/' + i; os.makedirs(d, exist_ok=True)
    open(d + '/model.res', 'w').write(res); open(d + '/data.hkl', 'w').write(hkl)
    up = res.upper()
    flags = [k for k in ('TWIN', 'BASF', 'EXTI', 'SWAT', 'ABIN', 'HKLF 5', 'SUMP', 'FREE', 'DFIX', 'SADI', 'SIMU', 'RIGU', 'DELU', 'ISOR', 'EADP', 'SAME', 'FLAT', 'AFIX 6', 'AFIX 13', 'AFIX 137') if k in up]
    out.append({'id': i, 'R1': r['R1'], 'groups': r['groups'], 'partial': r['partial'], 'flags': flags})
json.dump(out, open(P + '/disordered.json', 'w'), indent=0)
for o in out: print(o['id'], o['R1'], 'parts', o['groups'], 'partial', o['partial'], ' '.join(o['flags']))
