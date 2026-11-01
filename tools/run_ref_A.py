"""Reference (deposited model re-refined in the shared engine) and System A (refine the stripped model as is).
run_ref_A.py ROOT ids...  writes tasks/<id>/ref.json and tasks/<id>/A/final.res"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xtal_lib as X

root = sys.argv[1]
for i in sys.argv[2:]:
    d = root + '/tasks/' + i; t0 = time.time()
    if os.path.exists(d + '/ref.json') and os.path.exists(d + '/A/stats.json'): continue
    try:
        truth = open(d + '/truth.res').read()
        soft = [l for l in X.logical_lines(truth) if X.keyword(l).split('_')[0] in ('EADP', 'EXYZ', 'SAME')]
        truth = '\n'.join(l for l in X.logical_lines(truth) if l not in soft) + '\n'
        if os.path.exists(d + '/ref.json'):
            r = None; ref = json.load(open(d + '/ref.json'))
        else:
            r = X.refine(truth, d + '/input/data.hkl', d + '/_ref.res')
            ref = dict(approx=bool(soft), R1=r.r1, wR2=r.wr2, gof=r.gof, npar=r.npar, n_iter=r.n_iter, fixedH=r.fixedH)
            json.dump(ref, open(d + '/ref.json', 'w'))
        os.makedirs(d + '/A', exist_ok=True)
        a = X.refine(open(d + '/input/model.res').read(), d + '/input/data.hkl', d + '/A/_run.res')
        open(d + '/A/final.res', 'w').write(a.model_text)
        open(d + '/input/model_refined.res', 'w').write(a.model_text)
        json.dump(dict(R1=a.r1, wR2=a.wr2, npar=a.npar, n_iter=a.n_iter), open(d + '/A/stats.json', 'w'))
        print(i, 'ref R1 %.4f wR2 %.4f | A R1 %.4f wR2 %.4f (dR1 %+.4f) | %.0fs' % (ref['R1'], ref['wR2'], a.r1, a.wr2, a.r1 - ref['R1'], time.time() - t0), flush=True)
    except Exception as e:
        print(i, 'ERROR %s: %s' % (type(e).__name__, str(e)[:150]), flush=True)
