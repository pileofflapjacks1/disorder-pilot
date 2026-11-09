# Case 11: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (1)

- N2–C21 rigid-bond test 0.0060

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| N2–C8 | 1.409 | 1.446 | partner N901 | 0.0008 |  |
| N2–C15 | 1.371 | 1.446 | partner N901 | 0.0012 |  |
| N2–C21 | 1.449 | 1.446 | partner N901 | 0.006 | rigid-bond test 0.0060 |
| N901–C8 | 1.446 | 1.409 | partner N2 | – |  |
| N901–C15 | 1.445 | 1.409 | partner N2 | – |  |
| N901–C903 | 1.478 | 1.409 | partner N2 | – |  |
| O2–C15 | 1.230 | 1.283 | partner O901 | 0.0042 |  |
| O901–C15 | 1.283 | 1.23 | partner O2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O2 | 1 | 0.858 | 0.0534 | 2.06 |
| O901 | 2 | 0.142 | 0.0476 | iso |
| N2 | 1 | 0.727 | 0.0407 | 1.85 |
| N901 | 2 | 0.273 | 0.0454 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.052 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O2 | 0.3 | O901 | 0.69 | -5.9 |  |
| O901 | 3.6 | O2 | 0.69 | -5.9 |  |
| N2 | 0.9 | N901 | 0.57 | -6.0 |  |
| N901 | -1.9 | N2 | 0.57 | -6.0 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.142.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0434 | 0.1227 | 0.146 | 0.06 | – |
| perturbed seed 2 | 0.0438 | 0.1239 | 0.147 | 0.07 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0406 | 0.1151 | 0.142 | 0.00 | – |
