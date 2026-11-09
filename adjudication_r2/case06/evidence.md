# Case 06: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (5)

- C28–C27 -0.20 Å vs partner C904
- C28–C29 -0.14 Å vs partner C904
- C29–C28 rigid-bond test 0.0057
- C904–C27 +0.31 Å vs partner C28
- C906–C25 +0.17 Å vs partner C30

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C28–C27 | 1.318 | 1.523 | partner C904 | 0.0181 | -0.20 Å vs partner C904 |
| C28–C29 | 1.381 | 1.523 | partner C904 | 0.0057 | -0.14 Å vs partner C904 |
| C29–C28 | 1.381 | 1.383 | partner C905 | 0.0057 | rigid-bond test 0.0057 |
| C29–C30 | 1.386 | 1.383 | partner C905 | 0.0046 |  |
| C30–C25 | 1.376 | 1.47 | partner C906 | 0.0006 |  |
| C30–C29 | 1.386 | 1.47 | partner C906 | 0.0046 |  |
| C903–C902 | 1.435 | 1.54 | covalent sum | – |  |
| C903–C42 | 1.430 | 1.54 | covalent sum | – |  |
| C904–C27 | 1.663 | 1.349 | partner C28 | – | +0.31 Å vs partner C28 |
| C904–C905 | 1.383 | 1.349 | partner C28 | – |  |
| C905–C904 | 1.383 | 1.383 | partner C29 | – |  |
| C905–C906 | 1.383 | 1.383 | partner C29 | – |  |
| C906–C25 | 1.556 | 1.381 | partner C30 | – | +0.17 Å vs partner C30 |
| C906–C905 | 1.383 | 1.381 | partner C30 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| C28 | 1 | 0.823 | 0.0657 | 2.94 |
| C904 | 2 | 0.177 | 0.0461 | iso |
| C29 | 1 | 0.823 | 0.0659 | 2.33 |
| C905 | 2 | 0.177 | 0.0459 | iso |
| C30 | 1 | 0.823 | 0.0516 | 1.32 |
| C906 | 2 | 0.177 | 0.0349 | iso |
| C903 | 2 | 0.131 | 0.0556 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.061 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| C28 | 1.1 | C904 | 0.6 | -2.4 |  |
| C904 | 1.0 | C28 | 0.6 | -2.4 |  |
| C29 | 3.4 | C905 | 0.71 | -4.2 |  |
| C905 | 4.1 | C29 | 0.71 | -4.2 |  |
| C30 | 2.0 | C906 | 0.53 | -1.2 |  |
| C906 | 1.3 | C30 | 0.53 | -1.2 |  |
| C903 | 2.4 | – | – | – |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.131.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0186 | 0.0487 | 0.131 | 0.02 | – |
| perturbed seed 2 | 0.0186 | 0.0487 | 0.131 | 0.02 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0186 | 0.0487 | 0.131 | 0.01 | – |
