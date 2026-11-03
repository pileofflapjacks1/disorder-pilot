# Case 11: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (5)

- O1–C21 +0.10 Å vs partner O1B
- O1B–C20 -0.13 Å vs partner O1
- O2–C20 rigid-bond test 0.0066
- C22B/C23 split by 1.68 Å (large for a disorder split)
- GooF falls from 1.05 to 0.68 with the deposited weighting scheme

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C21–O1 | 1.494 | 1.43 | covalent sum | 0.0002 |  |
| C21–C22 | 1.513 | 1.484 | partner C24B | 0.0 |  |
| C21–C23 | 1.505 | 1.484 | partner C24B | 0.0023 |  |
| C21–C24 | 1.525 | 1.484 | partner C24B | 0.0019 |  |
| C21B–O1B | 1.502 | 1.494 | partner C21 | – |  |
| C21B–C22B | 1.503 | 1.513 | partner C21 | – |  |
| C21B–C23B | 1.523 | 1.513 | partner C21 | – |  |
| C21B–C24B | 1.484 | 1.513 | partner C21 | – |  |
| C22–C21 | 1.513 | 1.484 | partner C24B | 0.0 |  |
| C22B–C21B | 1.503 | 1.505 | partner C23 | – |  |
| C23–C21 | 1.505 | 1.503 | partner C21B | 0.0023 |  |
| C23B–C21B | 1.523 | 1.505 | partner C23 | – |  |
| C24–C21 | 1.525 | 1.484 | partner C24B | 0.0019 |  |
| C24B–C21B | 1.484 | 1.513 | partner C21 | – |  |
| O1–C20 | 1.321 | 1.39 | partner O1B | 0.0029 |  |
| O1–C21 | 1.494 | 1.39 | partner O1B | 0.0002 | +0.10 Å vs partner O1B |
| O1B–C20 | 1.277 | 1.408 | partner O1 | – | -0.13 Å vs partner O1 |
| O1B–C21B | 1.502 | 1.408 | partner O1 | – |  |
| O2–C20 | 1.230 | 1.186 | partner O2B | 0.0066 | rigid-bond test 0.0066 |
| O2B–C20 | 1.186 | 1.23 | partner O2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O1 | 1 | 0.807 | 0.0246 | 1.9 |
| O2 | 1 | 0.807 | 0.0384 | 3.39 |
| C21 | 1 | 0.807 | 0.0310 | 2.39 |
| C22 | 1 | 0.807 | 0.0424 | 2.97 |
| C23 | 1 | 0.807 | 0.0456 | 2.64 |
| C24 | 1 | 0.807 | 0.0394 | 2.05 |
| O1B | 2 | 0.193 | 0.0245 | iso |
| O2B | 2 | 0.193 | 0.0316 | iso |
| C21B | 2 | 0.193 | 0.0284 | iso |
| C22B | 2 | 0.193 | 0.0500 | iso |
| C23B | 2 | 0.193 | 0.0438 | iso |
| C24B | 2 | 0.193 | 0.0485 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.065 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O1 | 1.5 | O1B | 0.65 | -4.8 |  |
| O2 | 3.6 | O2B | 0.92 | -9.2 |  |
| C21 | 1.9 | C24B | 0.71 | 0.9 |  |
| C22 | -2.9 | C24B | 1.54 | -0.1 |  |
| C23 | -0.7 | C21B | 0.91 | 2.1 |  |
| C24 | -2.5 | C24B | 1.03 | -3.8 |  |
| O1B | 6.3 | O1 | 0.65 | -4.8 |  |
| O2B | 18.0 | O2 | 0.92 | -9.2 |  |
| C21B | 14.4 | C21 | 0.85 | -0.8 |  |
| C22B | 18.0 | C23 | 1.68 | -2.6 |  |
| C23B | 17.6 | C23 | 1.0 | 0.1 |  |
| C24B | 4.7 | C21 | 0.71 | 0.9 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.193.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0252 | 0.0688 | 0.192 | 0.02 | – |
| perturbed seed 2 | 0.0252 | 0.0688 | 0.193 | 0.02 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0251 | 0.0687 | 0.193 | 0.00 | – |
