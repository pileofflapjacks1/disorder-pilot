# Case 03: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (5)

- Se1–O4 -0.25 Å vs partner Se1B
- Se1–O6 -0.27 Å vs partner Se1B
- Se1B–O2 +0.41 Å vs partner Se1
- Se1B–O4 +0.12 Å vs partner Se1
- Se1/Se1B split by 2.22 Å (large for a disorder split)

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| Se1–O4 | 1.643 | 1.898 | partner Se1B | 0.0 | -0.25 Å vs partner Se1B |
| Se1–O6 | 1.630 | 1.898 | partner Se1B | 0.0005 | -0.27 Å vs partner Se1B |
| Se1B–O2 | 2.043 | 1.636 | partner Se1 | – | +0.41 Å vs partner Se1 |
| Se1B–O4 | 1.753 | 1.636 | partner Se1 | – | +0.12 Å vs partner Se1 |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Se1 | 1 | 0.478 | 0.0099 | 3.36 |
| Se1B | 2 | 0.022 | 0.0068 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.338 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Se1 | -0.6 | Se1B | 2.22 | 0.3 |  |
| Se1B | 10.2 | Se1 | 2.22 | 0.3 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.022.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0164 | 0.0390 | 0.022 | 0.00 | – |
| perturbed seed 2 | 0.0164 | 0.0390 | 0.022 | 0.00 | – |
| RIGU + SIMU on the anisotropic candidate atoms | not available (not run: fewer than two candidate atoms are anisotropic) |||||
