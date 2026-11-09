# Case 05: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (5)

- C30–C29 rigid-bond test 0.0225
- C32–C33 rigid-bond test 0.0125
- C33–C32 rigid-bond test 0.0125
- N901–C902 short contact
- C904 Ueq 1.000

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C30–C29 | 1.389 | 1.422 | partner C906 | 0.0225 | rigid-bond test 0.0225 |
| C30–C31 | 1.458 | 1.422 | partner C906 | 0.0024 |  |
| C31–C30 | 1.458 | 1.392 | partner C907 | 0.0024 |  |
| C31–C32 | 1.381 | 1.392 | partner C907 | 0.0025 |  |
| C32–C31 | 1.381 | 1.382 | partner C908 | 0.0025 |  |
| C32–C33 | 1.383 | 1.382 | partner C908 | 0.0125 | rigid-bond test 0.0125 |
| C33–C28 | 1.394 | 1.416 | partner C909 | 0.004 |  |
| C33–C32 | 1.383 | 1.416 | partner C909 | 0.0125 | rigid-bond test 0.0125 |
| C904–C903 | 1.707 | 1.54 | covalent sum | – |  |
| C904–C905 | 1.631 | 1.54 | covalent sum | – |  |
| C904–N902 | 1.613 | 1.48 | covalent sum | – |  |
| C906–C29 | 1.431 | 1.424 | partner C30 | – |  |
| C906–C907 | 1.413 | 1.424 | partner C30 | – |  |
| C907–C906 | 1.413 | 1.419 | partner C31 | – |  |
| C907–C908 | 1.371 | 1.419 | partner C31 | – |  |
| C908–C907 | 1.371 | 1.382 | partner C32 | – |  |
| C908–C909 | 1.394 | 1.382 | partner C32 | – |  |
| C909–C28 | 1.439 | 1.389 | partner C33 | – |  |
| C909–C908 | 1.394 | 1.389 | partner C33 | – |  |
| N901–C902 | 0.884 | 1.48 | covalent sum | – | short contact |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| C30 | 1 | 0.632 | 0.0533 | 1.09 |
| C906 | 2 | 0.368 | 0.0490 | iso |
| C31 | 1 | 0.632 | 0.0556 | 1.12 |
| C907 | 2 | 0.368 | 0.0508 | iso |
| C32 | 1 | 0.632 | 0.0586 | 1.07 |
| C908 | 2 | 0.368 | 0.0578 | iso |
| C33 | 1 | 0.632 | 0.0459 | 1.08 |
| C909 | 2 | 0.368 | 0.0445 | iso |
| N901 | 2 | 0.418 | 0.1218 | iso |
| C904 | 2 | 0.418 | 1.0000 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.096 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| C30 | -0.1 | C906 | 0.39 | 0.1 |  |
| C906 | 2.7 | C30 | 0.39 | 0.1 |  |
| C31 | 2.3 | C907 | 0.57 | 0.3 |  |
| C907 | 6.5 | C31 | 0.57 | 0.3 |  |
| C32 | 4.1 | C908 | 0.7 | -0.0 |  |
| C908 | 9.6 | C32 | 0.7 | -0.0 |  |
| C33 | 1.5 | C909 | 0.6 | -2.6 |  |
| C909 | 7.3 | C33 | 0.6 | -2.6 |  |
| N901 | -0.6 | – | – | – |  |
| C904 | -0.9 | – | – | – |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.368.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0535 | 0.1554 | 0.366 | 0.04 | – |
| perturbed seed 2 | 0.0535 | 0.1553 | 0.369 | 0.04 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0534 | 0.1552 | 0.37 | 0.00 | – |
