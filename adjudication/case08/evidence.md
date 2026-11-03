# Case 08: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (8)

- C20–O2 rigid-bond test 0.0061
- C20–C19 rigid-bond test 0.0079
- C21–C22 rigid-bond test 0.0147
- C902–C22 +0.42 Å vs partner C21
- O1–C20 -0.12 Å vs partner O901
- O2–C20 rigid-bond test 0.0061
- O901–C902 +0.11 Å vs partner O1
- GooF falls from 1.05 to 0.78 with the deposited weighting scheme

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C20–O1 | 1.297 | 1.271 | partner C901 | 0.0042 |  |
| C20–O2 | 1.257 | 1.271 | partner C901 | 0.0061 | rigid-bond test 0.0061 |
| C20–C19 | 1.518 | 1.532 | partner C901 | 0.0079 | rigid-bond test 0.0079 |
| C21–O1 | 1.498 | 1.43 | covalent sum | 0.0004 |  |
| C21–C22 | 1.512 | 1.513 | partner C904 | 0.0147 | rigid-bond test 0.0147 |
| C21–C23 | 1.505 | 1.513 | partner C904 | 0.0016 |  |
| C21–C24 | 1.513 | 1.513 | partner C904 | 0.0039 |  |
| C23–C21 | 1.505 | 1.548 | partner C902 | 0.0016 |  |
| C24–C21 | 1.513 | 1.513 | partner C904 | 0.0039 |  |
| C901–O901 | 1.317 | 1.277 | partner C20 | – |  |
| C901–O902 | 1.226 | 1.277 | partner C20 | – |  |
| C901–C19 | 1.532 | 1.518 | partner C20 | – |  |
| C902–O901 | 1.508 | 1.498 | partner C21 | – |  |
| C902–C22 | 1.931 | 1.512 | partner C21 | – | +0.42 Å vs partner C21 |
| C902–C903 | 1.548 | 1.512 | partner C21 | – |  |
| C902–C904 | 1.475 | 1.512 | partner C21 | – |  |
| C903–C902 | 1.548 | 1.505 | partner C23 | – |  |
| C904–C902 | 1.475 | 1.512 | partner C21 | – |  |
| C904–C22 | 1.550 | 1.512 | partner C21 | – |  |
| O1–C20 | 1.297 | 1.412 | partner O901 | 0.0042 | -0.12 Å vs partner O901 |
| O1–C21 | 1.498 | 1.412 | partner O901 | 0.0004 |  |
| O2–C20 | 1.257 | 1.226 | partner O902 | 0.0061 | rigid-bond test 0.0061 |
| O901–C901 | 1.317 | 1.397 | partner O1 | – |  |
| O901–C902 | 1.508 | 1.397 | partner O1 | – | +0.11 Å vs partner O1 |
| O902–C901 | 1.226 | 1.257 | partner O2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O1 | 1 | 0.811 | 0.0249 | 1.98 |
| O901 | 2 | 0.189 | 0.0249 | iso |
| O2 | 1 | 0.811 | 0.0388 | 3.38 |
| O902 | 2 | 0.189 | 0.0298 | iso |
| C20 | 1 | 0.811 | 0.0267 | 1.5 |
| C901 | 2 | 0.189 | 0.0104 | iso |
| C21 | 1 | 0.811 | 0.0312 | 2.4 |
| C902 | 2 | 0.189 | 0.0261 | iso |
| C23 | 1 | 0.811 | 0.0465 | 2.67 |
| C903 | 2 | 0.189 | 0.0445 | iso |
| C24 | 1 | 0.811 | 0.0394 | 2.11 |
| C904 | 2 | 0.189 | 0.0511 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.065 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O1 | 1.5 | O901 | 0.66 | -4.8 |  |
| O901 | 6.9 | O1 | 0.66 | -4.8 |  |
| O2 | 3.6 | O902 | 0.92 | -9.2 |  |
| O902 | 18.2 | O2 | 0.92 | -9.2 |  |
| C20 | 0.1 | C901 | 0.23 | 0.3 |  |
| C901 | 0.4 | C20 | 0.23 | 0.3 |  |
| C21 | 1.9 | C904 | 0.72 | 0.9 |  |
| C902 | 13.9 | C21 | 0.84 | -1.1 |  |
| C23 | -0.7 | C902 | 0.92 | 2.3 |  |
| C903 | 17.3 | C23 | 0.99 | -0.1 |  |
| C24 | -2.6 | C904 | 1.01 | -3.8 |  |
| C904 | 4.8 | C21 | 0.72 | 0.9 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.189.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0288 | 0.0790 | 0.191 | 0.07 | – |
| perturbed seed 2 | 0.0288 | 0.0790 | 0.191 | 0.07 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0287 | 0.0789 | 0.19 | 0.05 | – |
