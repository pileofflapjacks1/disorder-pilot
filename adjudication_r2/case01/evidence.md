# Case 01: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (2)

- C36–C37 rigid-bond test 0.0081
- O903–C5 +0.17 Å vs partner O8

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C36–O7 | 1.424 | 1.452 | partner C903 | 0.0027 |  |
| C36–O8 | 1.391 | 1.452 | partner C903 | 0.0007 |  |
| C36–C37 | 1.536 | 1.628 | partner C903 | 0.0081 | rigid-bond test 0.0081 |
| C903–O7 | 1.491 | 1.407 | partner C36 | – |  |
| C903–O903 | 1.414 | 1.407 | partner C36 | – |  |
| C903–C37 | 1.628 | 1.536 | partner C36 | – |  |
| O8–C5 | 1.394 | 1.49 | partner O903 | 0.0047 |  |
| O8–C36 | 1.391 | 1.49 | partner O903 | 0.0007 |  |
| O903–C5 | 1.565 | 1.392 | partner O8 | – | +0.17 Å vs partner O8 |
| O903–C903 | 1.414 | 1.392 | partner O8 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O8 | 1 | 0.878 | 0.0257 | 1.76 |
| O903 | 2 | 0.122 | 0.0492 | iso |
| C36 | 1 | 0.878 | 0.0237 | 1.78 |
| C903 | 2 | 0.122 | 0.0831 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.097 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O8 | 2.6 | O903 | 0.73 | -2.7 |  |
| O903 | 8.7 | O8 | 0.73 | -2.7 |  |
| C36 | 0.5 | C903 | 1.01 | -1.7 |  |
| C903 | 7.1 | C36 | 1.01 | -1.7 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.122.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0590 | 0.2051 | 0.128 | 0.03 | – |
| perturbed seed 2 | 0.0590 | 0.2051 | 0.127 | 0.03 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0590 | 0.2050 | 0.122 | 0.00 | – |
