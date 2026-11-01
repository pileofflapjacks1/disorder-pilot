import sys, time; sys.path.insert(0, sys.argv[1] + '/tools')
import xtal_lib as X
P = sys.argv[1]
for i in sys.argv[2:]:
    d = P + '/work/' + i; t0 = time.time()
    r = X.refine(open(d + '/model.res').read(), d + '/data.hkl', d + '/t.res')
    open(d + '/t_out.res', 'w').write(r.model_text)
    r2 = X.refine(r.model_text, d + '/data.hkl', d + '/t2.res', cycles=5)
    pk, rms, hole = X.diff_peaks(r2, n=5)
    print(i, 'R1 %.4f wR2 %.4f gof %.2f npar %d it %d | rerefine R1 %.4f it %d | %.0fs' % (r.r1, r.wr2, r.gof, r.npar, r.n_iter, r2.r1, r2.n_iter, time.time() - t0))
    print('  rms %.3f hole %.2f peaks' % (rms, hole), ['%.2f@%s' % (p['height'], p['near'][0] if p['near'] else '') for p in pk])
