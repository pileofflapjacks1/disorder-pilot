# Case 15: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (4)

- S1–C8 -0.23 Å vs partner S901
- S2–C8 -0.15 Å vs partner S902
- S901–C8 +0.23 Å vs partner S1
- S902–C8 +0.23 Å vs partner S2

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C9–S2 | 1.820 | 1.75 | partner C901 | 0.0001 |  |
| C9–C10 | 1.534 | 1.506 | partner C901 | 0.0001 |  |
| C901–S902 | 1.750 | 1.82 | partner C9 | – |  |
| C901–C10 | 1.506 | 1.534 | partner C9 | – |  |
| S1–C8 | 1.666 | 1.892 | partner S901 | 0.0074 | -0.23 Å vs partner S901 |
| S2–C8 | 1.720 | 1.874 | partner S902 | 0.0058 | -0.15 Å vs partner S902 |
| S2–C9 | 1.820 | 1.874 | partner S902 | 0.0001 |  |
| S901–C8 | 1.892 | 1.666 | partner S1 | – | +0.23 Å vs partner S1 |
| S902–C8 | 1.998 | 1.77 | partner S2 | – | +0.23 Å vs partner S2 |
| S902–C901 | 1.750 | 1.77 | partner S2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| S1 | 1 | 0.944 | 0.0505 | 3.3 |
| S901 | 2 | 0.056 | 0.0122 | iso |
| S2 | 1 | 0.905 | 0.0428 | 2.71 |
| S902 | 2 | 0.095 | 0.0158 | iso |
| C9 | 1 | 0.905 | 0.0440 | 2.63 |
| C901 | 2 | 0.095 | 0.0170 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.128 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| S1 | 2.7 | S901 | 0.58 | 3.3 |  |
| S901 | 6.7 | S1 | 0.58 | 3.3 |  |
| S2 | 3.3 | S902 | 0.47 | 3.6 |  |
| S902 | 5.7 | S2 | 0.47 | 3.6 |  |
| C9 | 1.4 | C901 | 0.37 | 1.2 |  |
| C901 | 0.5 | C9 | 0.37 | 1.2 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.056.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0613 | 0.1672 | 0.101 | 0.18 | – |
| perturbed seed 2 | 0.0613 | 0.1671 | 0.099 | 0.17 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0606 | 0.1660 | 0.056 | 0.02 | – |
