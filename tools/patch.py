import sys
p = sys.argv[1]; s = open(p).read()
s = s.replace("""def minor_occ(xs):
    occ = [s.occupancy for s in xs.scatterers() if s.occupancy < 0.999 and s.scattering_type != 'H']
    return round(min(occ), 3) if occ else None""", """def occs(xs):
    return [(s.label, s.occupancy) for s in xs.scatterers() if s.scattering_type != 'H']""")
s = s.replace("r0 = ls.r1_factor(cutoff_factor=2)[0]; o0 = minor_occ(m.xray_structure)", "r0 = ls.r1_factor(cutoff_factor=2)[0]; o0 = occs(m.xray_structure)")
s = s.replace("return r0, r1, o0, minor_occ(m.xray_structure), it.n_iterations, nrest", """o1 = occs(m.xray_structure)
    dmax = max(abs(a[1] - b[1]) for a, b in zip(o0, o1))
    return r0, r1, dmax, None, it.n_iterations, nrest""")
s = s.replace("minor occ %s->%s' % ('RESTR' if restrained else 'UNRESTR', r0, r1, n, o0, o1)", "max dOcc %.3f' % ('RESTR' if restrained else 'UNRESTR', r0, r1, n, o0)")
open(p, 'w').write(s)
