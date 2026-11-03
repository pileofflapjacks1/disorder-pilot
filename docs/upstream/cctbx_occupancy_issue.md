# Issue for cctbx/cctbx_project

Filed 2026-11-02 as https://github.com/cctbx/cctbx_project/issues/1284

**Title:** `iotbx.shelx` parser: free-variable occupancy groups of more than 2 atoms are constrained incorrectly

**Version:** cctbx-base 2025.11 (PyPI), Python 3.12, macOS. The code is in `iotbx/shelx/parsers.py`, `atom_parser.process_occupancies_depending_on_free_variable` (around line 449).

## Summary
In SHELX, a free variable can control more than two atoms: for example `31` on every atom of one disorder part and `-31` on every atom of the other. For such a group the parser adds pairwise affine constraints between neighbours in the member list (1–2, 2–3, 3–4, …). After refinement with smtbx, some members end up with the occupancy of the *other* part, so the result breaks the SHELX meaning of the instruction.

## Reproduction
- **Structure:** COD 2312780 (CC0), using the `.res` and `.hkl` embedded in its CIF. Free variable 3 links `C4 31`, `H1 31` (riding) and `C5 -31`, `H2 -31` (riding).
- **Refinement:** `smtbx.refinement.model.from_shelx(...)`, then `constraints.reparametrisation` and Levenberg–Marquardt, 40 cycles. The run is otherwise identical in both columns.

| atom (SHELX code) | deposited (SHELXL) | upstream | patched (below) |
|---|---|---|---|
| C4 (31) | 0.905 | 0.888 | 0.898 |
| H1 (31) | 0.905 | 0.888 | 0.898 |
| C5 (−31) | 0.095 | 0.112 | 0.102 |
| **H2 (−31)** | **0.095** | **0.888** | **0.102** |
| R1 | – | 0.0282 | 0.0273 |

Upstream, H2 comes out at the occupancy of the +31 part, even though its code is −31. With the patch, every member follows its own sign.

## Upstream code
```python
for i in range(len(affine_occupancies) - 1):
  (a, b, i), (a1, b1, i1) = affine_occupancies[i:i+2]
  self.builder.add_occupancy_pair_affine_constraint(
    scatterer_indices=(i, i1),
    linear_form=((1/a, -1/a1), b - b1))
```
The loop variable `i` is rebound to the scatterer index inside the body. That is confusing, but Python rebinds `i` from `range` on each iteration, so it is not the cause. The faulty result seems to come from the *chain* of pairwise constraints that share a scatterer (2–3 then 3–4). We have not traced exactly how the reparametrisation resolves that chain.

## Fix that works for us
Link every member to the first member, a star instead of a chain:
```python
def process_occupancies_depending_on_free_variable(self):
  if not self.builder_does_occupancy_pair_affine_constraint: return
  for free_var_idx, members in six.iteritems(self.occupancies_depending_on_free_variable):
    if len(members) < 2: continue
    a, b, i0 = members[0]
    for a1, b1, i1 in members[1:]:
      self.builder.add_occupancy_pair_affine_constraint(
        scatterer_indices=(i0, i1), linear_form=((1/a, -1/a1), b - b1))
```

## Where we found it
We hit this while building a disorder benchmark on COD structures. Across 10 test structures, the patch (together with other engine fixes) brought re-refinement within 0.0015 R1 and 0.033 occupancy of the deposited SHELXL results in 9 of 10 cases. Before filing, check the open issues for a duplicate. On 2026-11-01, a GitHub search for `process_occupancies_depending_on_free_variable` found none.
