# Case 06: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (16)

- Ag5–Ag2 rigid-bond test 0.0053
- Ag5–Ag6 -0.13 Å vs partner Ag5B
- Ag5–S1 +0.28 Å vs partner Ag5B
- Ag5–S3 +0.28 Å vs partner Ag5B
- Ag5–S5 +0.23 Å vs partner Ag5B
- Ag5B–S1 -0.22 Å vs partner Ag5
- Ag5B–S3 -0.33 Å vs partner Ag5
- Ag6–Ag2 +0.10 Å vs partner Ag6B
- Ag6–Ag3 rigid-bond test 0.0053
- Ag6–S2 +0.36 Å vs partner Ag6B
- Ag6–S4 +0.32 Å vs partner Ag6B
- Ag6–S5 +0.31 Å vs partner Ag6B
- Ag6B–S2 -0.33 Å vs partner Ag6
- Ag6B–S4 -0.30 Å vs partner Ag6
- Ag5B 0.54 Å from heavy atom AG5 (Fourier-ripple distance)
- Ag6B 0.75 Å from heavy atom AG6 (Fourier-ripple distance)

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| Ag5–Ag2 | 3.091 | 3.099 | partner Ag5B | 0.0053 | rigid-bond test 0.0053 |
| Ag5–Ag3 | 3.079 | 3.099 | partner Ag5B | 0.0048 |  |
| Ag5–Ag6 | 2.970 | 3.099 | partner Ag5B | 0.0044 | -0.13 Å vs partner Ag5B |
| Ag5–S1 | 2.534 | 2.256 | partner Ag5B | – | +0.28 Å vs partner Ag5B |
| Ag5–S3 | 2.533 | 2.256 | partner Ag5B | 0.0018 | +0.28 Å vs partner Ag5B |
| Ag5–S5 | 2.489 | 2.256 | partner Ag5B | 0.018 | +0.23 Å vs partner Ag5B |
| Ag5B–Ag2 | 3.138 | 3.079 | partner Ag5 | – |  |
| Ag5B–Ag3 | 3.061 | 3.079 | partner Ag5 | – |  |
| Ag5B–S1 | 2.311 | 2.533 | partner Ag5 | – | -0.22 Å vs partner Ag5 |
| Ag5B–S3 | 2.201 | 2.533 | partner Ag5 | – | -0.33 Å vs partner Ag5 |
| Ag6–Ag2 | 3.132 | 3.032 | partner Ag6B | 0.0055 | +0.10 Å vs partner Ag6B |
| Ag6–Ag3 | 3.098 | 3.032 | partner Ag6B | 0.0053 | rigid-bond test 0.0053 |
| Ag6–Ag5 | 2.970 | 3.032 | partner Ag6B | 0.0044 |  |
| Ag6–S2 | 2.532 | 2.174 | partner Ag6B | 0.001 | +0.36 Å vs partner Ag6B |
| Ag6–S4 | 2.492 | 2.174 | partner Ag6B | 0.0047 | +0.32 Å vs partner Ag6B |
| Ag6–S5 | 2.481 | 2.174 | partner Ag6B | 0.0098 | +0.31 Å vs partner Ag6B |
| Ag6B–Ag2 | 3.019 | 3.098 | partner Ag6 | – |  |
| Ag6B–Ag3 | 3.045 | 3.098 | partner Ag6 | – |  |
| Ag6B–S2 | 2.158 | 2.492 | partner Ag6 | – | -0.33 Å vs partner Ag6 |
| Ag6B–S4 | 2.189 | 2.492 | partner Ag6 | – | -0.30 Å vs partner Ag6 |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Ag5 | 1 | 0.911 | 0.0396 | 2.62 |
| Ag5B | 2 | 0.089 | 0.0555 | iso |
| Ag6 | 1 | 0.960 | 0.0416 | 2.72 |
| Ag6B | 2 | 0.040 | 0.0277 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.271 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Ag5 | -0.1 | Ag5B | 0.56 | -2.0 |  |
| Ag5B | 2.0 | Ag5 | 0.56 | -2.0 | AG5 0.54 |
| Ag6 | -0.0 | Ag6B | 0.75 | -0.6 |  |
| Ag6B | 7.2 | Ag6 | 0.75 | -0.6 | AG6 0.75 |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.04.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0381 | 0.1392 | 0.04 | 0.00 | – |
| perturbed seed 2 | 0.0381 | 0.1392 | 0.04 | 0.00 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0380 | 0.1388 | 0.04 | 0.00 | – |
