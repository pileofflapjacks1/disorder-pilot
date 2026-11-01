import sys, importlib.util
P = sys.argv[1]
spec = importlib.util.spec_from_file_location('r2', P + '/tools/refine2.py'); r2 = importlib.util.module_from_spec(spec)
sys.argv = ['x', P, 'damp']; spec.loader.exec_module(r2)
for i in sys.argv_ids if False else ['2312762', '2312754']:
    r0, r1, n, dmax, ev = r2.refine(i, True)
    print(i, 'R1 %.4f it %d' % (r1, n))
    for lab, a, b in sorted(r2.LAST, key=lambda t: -abs(t[2] - t[1]))[:6]:
        print('   %-6s %.3f -> %.3f' % (lab, a, b))
