"""Fixed views for the adjudication cases (post-hoc). The same recipe is used for every case and no key is read.

render.py ROOT OUT NN   writes OUT/caseNN/views.png: the Fo-Fc maps of the deposited and candidate models in one
plane through the candidate's extra atoms, with both models' atoms near that plane.
"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import xtal_lib as X
from adjudicate import diff_map

SLAB = 0.8        # A: atoms within this distance of the plane are drawn
STEP = 0.08       # A grid spacing of the map section
LEVELS = (3, 5, 8, 12, 18, 27)   # contour levels in multiples of the deposited map rms (same absolute values both panels)
POS, NEG, CAND = '#1b7f3b', '#c0392b', '#e08a00'


def near_image(f, f0):
    return [x - round(x - y) for x, y in zip(f, f0)]


def atoms_of(model, uc, f0):
    out = []
    for a in model.atoms:
        f = near_image(X.frac_xyz(a), f0)
        out.append(dict(label=a['label'], el=a['el'], part=a['part'], cart=np.array(uc.orthogonalize(f))))
    return out


def plane(points):
    c = points.mean(axis=0)
    if len(points) < 3: return c, np.eye(3)[:2]
    _, s, vt = np.linalg.svd(points - c)
    return c, vt[:2]


def section(m, uc, c, axes, half):
    n = int(2 * half / STEP) + 1; g = np.linspace(-half, half, n)
    Z = np.empty((n, n))
    for i, v in enumerate(g):
        for j, u in enumerate(g):
            p = c + u * axes[0] + v * axes[1]
            Z[i, j] = m.eight_point_interpolation(uc.fractionalize(tuple(p)))
    return g, Z


def draw(ax, g, Z, rms_ref, atoms, extra, c, axes, normal, title):
    lv = [k * rms_ref for k in LEVELS]
    ax.contour(g, g, Z, levels=lv, colors=POS, linewidths=0.8)
    ax.contour(g, g, Z, levels=[-x for x in reversed(lv)], colors=NEG, linewidths=0.8, linestyles='dashed')
    near = []
    for a in atoms:
        d = a['cart'] - c
        if abs(d @ normal) <= SLAB:
            near.append((a, d @ axes[0], d @ axes[1]))
    for k, (a, x, y) in enumerate(near):
        for b, x2, y2 in near[k + 1:]:
            if 'H' in (a['el'], b['el']) and a['el'] == b['el']: continue
            if not (a['part'] == 0 or b['part'] == 0 or a['part'] == b['part']): continue
            dist = np.linalg.norm(a['cart'] - b['cart'])
            if dist < X.COV.get(a['el'], 1.4) + X.COV.get(b['el'], 1.4) + 0.4:
                ax.plot([x, x2], [y, y2], color='#888888', lw=1.0, zorder=2)
    for a, x, y in near:
        if a['el'] == 'H':
            ax.plot(x, y, 'o', ms=3, color='#9a9a9a', zorder=3)
            ax.annotate(a['label'], (x, y), xytext=(3, -8), textcoords='offset points', fontsize=6, color='#6b6b6b')
        elif a['label'] not in extra:
            ax.plot(x, y, 'o', ms=6, color='#222222', zorder=3)
            ax.annotate(a['label'], (x, y), xytext=(4, 4), textcoords='offset points', fontsize=7, color='#222222')
    for lab, (x, y, inplane) in extra.items():
        ax.plot(x, y, 'D', ms=8, mfc='none', mec=CAND, mew=1.6, zorder=4)
        ax.annotate(lab + ('' if inplane else ' (off-plane)'), (x, y), xytext=(5, -10), textcoords='offset points', fontsize=7, color='#222222')
    half = g[-1]
    ax.set_xlim(-half, half); ax.set_ylim(-half, half); ax.set_aspect('equal')
    ax.set_xlabel('Å'); ax.set_ylabel('Å'); ax.set_title(title, fontsize=9)
    ax.tick_params(labelsize=7, colors='#555555')
    for s in ax.spines.values(): s.set_color('#bbbbbb')


def render(out, nn):
    cd = '%s/case%s' % (out, nn); st = json.load(open(cd + '/stats.json'))
    extra_labels = [a['label'] for a in st['atoms']]
    ref = X.refine(open(cd + '/deposited.res').read(), cd + '/deposited.hkl', cd + '/_rv_ref.res')
    cand = X.refine(open(cd + '/candidate.res').read(), cd + '/candidate.hkl', cd + '/_rv_cand.res')
    for f in ('_rv_ref.res', '_rv_cand.res'):
        if os.path.exists(cd + '/' + f): os.remove(cd + '/' + f)
    uc = cand.xs.unit_cell(); cm = X.Model(cand.model_text); dm = X.Model(ref.model_text)
    f0 = X.frac_xyz(next(a for a in cm.atoms if a['label'] == extra_labels[0]))
    catoms = atoms_of(cm, uc, f0); datoms = atoms_of(dm, uc, f0)
    xc = np.array([a['cart'] for a in catoms if a['label'] in extra_labels])
    pts = [p for p in xc]
    for a in datoms:
        if a['el'] != 'H' and min(np.linalg.norm(a['cart'] - p) for p in xc) < 1.8: pts.append(a['cart'])
    c, axes = plane(np.array(pts)); c = xc.mean(axis=0)
    normal = np.cross(axes[0], axes[1])
    half = max(3.0, max(np.linalg.norm((p - c) - ((p - c) @ normal) * normal) for p in xc) + 1.8)
    extra = {}
    for a in catoms:
        if a['label'] in extra_labels:
            d = a['cart'] - c; extra[a['label']] = (d @ axes[0], d @ axes[1], abs(d @ normal) <= SLAB)
    m_ref, rms_ref = diff_map(ref); m_c, _ = diff_map(cand)
    g, Zr = section(m_ref, uc, c, axes, half); _, Zc = section(m_c, uc, c, axes, half)
    fig, axs = plt.subplots(1, 2, figsize=(11, 5.6))
    draw(axs[0], g, Zr, rms_ref, datoms, extra, c, axes, normal, 'Deposited model: Fo−Fc (candidate extra atoms marked)')
    draw(axs[1], g, Zc, rms_ref, catoms, extra, c, axes, normal, 'Candidate model: Fo−Fc')
    handles = [Line2D([], [], color=POS, lw=1, label='Fo−Fc positive'), Line2D([], [], color=NEG, lw=1, ls='--', label='Fo−Fc negative'),
               Line2D([], [], marker='o', ls='', color='#222222', label='atom (non-H)'), Line2D([], [], marker='o', ls='', ms=3, color='#9a9a9a', label='H'),
               Line2D([], [], marker='D', ls='', mfc='none', mec=CAND, mew=1.6, label='candidate extra atom')]
    fig.legend(handles=handles, loc='lower center', ncol=5, fontsize=8, frameon=False)
    fig.suptitle('Case %s. Contours at ±%s × %.3f e/Å³ (rms of the deposited map) in both panels; atoms within %.1f Å of the plane.'
                 % (nn, ', '.join(str(k) for k in LEVELS), rms_ref, SLAB), fontsize=9)
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    fig.savefig(cd + '/views.png', dpi=130, facecolor='white')
    print(nn, 'rendered', flush=True)


if __name__ == '__main__':
    render(sys.argv[2], sys.argv[3])
