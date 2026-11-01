import sys, os, re
for d in sys.argv[1:]:
    h = open(d + '/data.hkl').read().lstrip('\n'); open(d + '/data.hkl', 'w').write(h)
    r = open(d + '/model.res').read()
    r = re.sub(r'^(TEMP|SIZE)\b.*$', '', r, flags=re.M | re.I)
    open(d + '/model.res', 'w').write(r)
