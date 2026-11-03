# Case 01

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0670 | 0.0607 |
| wR2 | 0.1983 | 0.1847 |
| GooF | 1.07 | 0.99 |
| parameters | 505 | 514 |
| largest Fo−Fc peak (e/Å³) | 1.54 | 0.83 |
| deepest hole (e/Å³) | -0.81 | -0.78 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
9 extra parameters, R ratio 1.0733, p = 1.6e-221.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.085 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| C26A | C | 1 | 0.704 | 0.0528 | 0.27 | 3.1 | C26 0.09 |
| C26B | C | 2 | 0.296 | 0.0590 | 0.22 | 2.6 | C26 0.51 |
| C27B | C | 2 | 0.296 | 0.0726 | 1.41 | 16.7 | H24 0.31 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
