# Case 03: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (2)

- C906 Ueq 0.261
- perturbed seed 1: atoms moved up to 0.21 Å

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C901–C26 | 1.774 | 1.54 | covalent sum | – |  |
| C901–C902 | 1.491 | 1.54 | covalent sum | – |  |
| C906–C904 | 1.478 | 1.54 | covalent sum | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| C901 | 2 | 0.248 | 0.0640 | iso |
| C906 | 2 | 0.248 | 0.2610 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.052 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| C901 | 4.8 | – | – | – |  |
| C906 | 3.2 | – | – | – |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.248.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0463 | 0.1225 | 0.248 | 0.21 | – |
| perturbed seed 2 | 0.0463 | 0.1226 | 0.248 | 0.11 | – |
| RIGU + SIMU on the anisotropic candidate atoms | not available (not run: fewer than two candidate atoms are anisotropic) |||||
