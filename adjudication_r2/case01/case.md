# Case 01

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0616 | 0.0590 |
| wR2 | 0.2115 | 0.2050 |
| GooF | 1.05 | 1.01 |
| parameters | 545 | 536 |
| largest Fo−Fc peak (e/Å³) | 1.28 | 0.55 |
| deepest hole (e/Å³) | -0.61 | -0.62 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-9 extra parameters, R ratio 1.0319, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.097 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| O8 | O | 1 | 0.878 | 0.0257 | 0.25 | 2.6 | O8 0.02 |
| O903 | O | 2 | 0.122 | 0.0492 | 0.84 | 8.7 | O8 0.72 |
| C36 | C | 1 | 0.878 | 0.0237 | 0.04 | 0.5 | C36 0.0 |
| C903 | C | 2 | 0.122 | 0.0831 | 0.69 | 7.0 | C36 1.01 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
