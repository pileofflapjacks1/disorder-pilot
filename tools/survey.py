import sys, os, gemmi, json
root = sys.argv[1]; rows = []
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith('.cif'): continue
        p = os.path.join(dp, f)
        try: doc = gemmi.cif.read(p)
        except Exception as e: rows.append({'id': f[:-4], 'err': str(e)[:60]}); continue
        b = doc.sole_block() if len(doc) == 1 else doc[0]
        g = lambda t: b.find_value(t)
        grp = b.find_values('_atom_site_disorder_group'); occ = b.find_values('_atom_site_occupancy')
        groups = sorted(set(x for x in grp if x not in ('.', '?'))) if grp else []
        partial = sum(1 for x in occ if x not in ('.', '?') and gemmi.cif.as_number(x) < 0.999) if occ else 0
        rows.append({'id': f[:-4], 'year': g('_journal_year'), 'res': g('_shelx_res_file') is not None,
            'hkl_emb': g('_shelx_hkl_file') is not None, 'groups': groups, 'partial': partial,
            'R1': g('_refine_ls_R_factor_gt'), 'wR2': g('_refine_ls_wR_factor_ref'),
            'prog': (g('_computing_structure_refinement') or '')[:40], 'blocks': len(doc)})
json.dump(rows, open(sys.argv[2], 'w'), indent=0)
ok = [r for r in rows if 'err' not in r]
dis = [r for r in ok if r['groups'] and r['partial']]
print('parsed', len(ok), 'errors', len(rows) - len(ok))
print('years', sorted(set(r['year'] for r in ok if r['year'])))
print('with embedded .res', sum(r['res'] for r in ok), ' embedded .hkl', sum(r['hkl_emb'] for r in ok))
print('disordered (nonzero group + partial occ)', len(dis), ' of those with .res', sum(r['res'] for r in dis))
print('multi-block files', sum(r['blocks'] > 1 for r in ok))
