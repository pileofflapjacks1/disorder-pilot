# Adjudication: false positives that lower R1

**Post-hoc.** This review was not part of the preregistered scoring and cannot change the pilot verdict. It feeds into the design of the next round.

Each case is a structure in which one system modelled disorder that the published model does not have, and the result has a lower R1 than the published model. Case numbers are shuffled, and the folders do not say which system (rules or agent) made the candidate or whether the structure was a control. The key is in `_key.json`; open it only after you have filled in `decisions.csv`.

**Blinding limits.** Atom labels like `C901` come from the rule-based system, and only controls are nested, so the `nested` column tells you which cases are controls. Try to judge the density and geometry, not the labels.

**Negative extra parameters** in a non-nested case mean the published model has more parameters, because it models other disorder that the candidate does not; no test is computed. A negative ρ/rms means the candidate placed an atom where the published model's difference map has a hole.

**Evidence sheets:** `EVIDENCE.md` and `caseNN/evidence.md` hold the computed checks (geometry against the other part, rigid-bond test, ADPs, map density and midpoints, Fourier-ripple distances, stability). Read them alongside Olex2; they flag things to look at and give no verdicts.

For each case: open `caseNN/deposited.res` and `caseNN/candidate.res` in Olex2 (each has its `.hkl` beside it), read `caseNN/case.md`, then record a verdict in `decisions.csv`: `real` (genuine disorder the depositors missed), `overfit` (extra parameters fitting noise), `artefact` (density from absorption, series termination, twinning and so on), or `unsure`.

| case | ΔR1 (cand − dep) | extra params | Hamilton p | nested | FP atoms | max ρ/rms at FP atoms |
|---|---|---|---|---|---|---|
| [01](case01/case.md) | -0.0063 | 9 | 1.6e-221 | no | 3 | 16.7 |
| [02](case02/case.md) | -0.0158 | 7 | 2.7e-56 | yes | 2 | 16.7 |
| [03](case03/case.md) | -0.0015 | 3 | 2.3e-65 | yes | 2 | 10.2 |
| [04](case04/case.md) | -0.0003 | -25 | – | no | 2 | 3.8 |
| [05](case05/case.md) | -0.0069 | -15 | – | no | 1 | -3.3 |
| [06](case06/case.md) | -0.0018 | 13 | 1e-114 | no | 4 | 7.2 |
| [07](case07/case.md) | -0.0008 | -55 | – | no | 1 | -1.1 |
| [08](case08/case.md) | -0.0106 | 25 | 0 | yes | 12 | 18.2 |
| [09](case09/case.md) | -0.0047 | -40 | – | no | 1 | 0.5 |
| [10](case10/case.md) | -0.0036 | -6 | – | no | 6 | 7.3 |
| [11](case11/case.md) | -0.0142 | 28 | 0 | yes | 12 | 18.0 |

The Hamilton test uses wR2 on F², not the F-based R of the original test, so its p values are approximate. Most cases add many parameters against thousands of reflections, so they can pass the test easily; treat a passing p as necessary, not sufficient.
