import sys, os, traceback; sys.path.insert(0, 'tools')
import xtal_lib as X
for i in sys.argv[2:]:
    d = 'tasks/' + i
    for f in (sys.argv[1].split(',')):
        try: r = X.refine(open(d + '/' + f).read(), d + '/input/data.hkl', d + '/_dbg.res', cycles=2); print(i, f, 'ok', round(r.r1, 4))
        except Exception as e: print(i, f, 'FAIL', type(e).__name__, str(e)[:300].replace('\n', ' ')); traceback.print_exc(limit=-3)
