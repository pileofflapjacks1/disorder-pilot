# Disorder pilot — week-1 go/no-go checks (2026-10-31)

Env: uv venv Python 3.12, cctbx-base 2025.11 (PyPI), gemmi 0.7.5. Scripts in tools/.

## 1. Data
- COD hkl module: 59,290 reflection files (56,624 in 2xxxxxx = IUCr journals).
- 300 newest 2xxxxxx entries with hkl (journal years 2020-2026): 230 embed _shelx_res_file + _shelx_hkl_file.
- 78 disordered (non-zero disorder group + partial occupancy); 66 of those embed .res (restraints available).
- Quirks: embedded hkl has a leading blank line; TEMP lines carry esds "20(2)" that iotbx rejects. tools/clean.py fixes both.

## 2. R1 recomputation (deposited model vs deposited data, no refinement)
10 disordered, no TWIN/HKLF5/ABIN. Applied OMIT s/2theta, SHEL, EXTI, sasaki f'/f''.
9/10 within 0.2% absolute R1; 2312741 +0.78% (cctbx gt R1 0.0444 ~= SHELXL all-data R1 0.0440 — unexplained).

## 3. Refinement parity (smtbx LM, 15 cycles, from deposited .res)
| id | dep R1 | restrained | unrestrained | max dOcc (restr) |
|---|---|---|---|---|
| 2312720 | 0.0336 | 0.0336 | 0.0336 | 0.046 |
| 2312754 | 0.0949 | 0.0939 | 0.0914 | 0.196 |
| 2312741 | 0.0366 | 0.0375 | 0.0383 | 0.147 |
| 2312780 | 0.0267 | DIVERGED (17.4) | 0.0295 | — |
| 2312781 | 0.0226 | 0.0246 | 0.0243 | 0.015 |
| 2312760 | 0.0251 | 0.0324 | 0.0323 | 0.000 |
| 2312762 | 0.0560 | CRASH (AFIX 13 connectivity, C12) | CRASH | — |
| 2312703 | 0.0469 | 0.0479 | 0.0479 | 0.000 |
| 2312715 | 0.0304 | 0.0348 | 0.0348 | 0.020 |
| 2312739 | 0.0334 | 0.0369 | 0.0357 | 0.001 |

7/10 within 0.5% R1. Failures: 1 divergence, 1 parser crash, EXTI structures worse.
Known causes: smtbx model.least_squares() ignores parsed EXTI (dummy extinction); SAME not supported;
iteration cap 15 hit (not converged). Occupancy drifts up to 0.2 from deposited even with restraints.

## Verdict
Data GO. R1 recomputation GO. Refinement engine CONDITIONAL — fix EXTI, damping/shift limits,
iterations, AFIX handling; re-test to 9/10 before building systems. Score every system against the
deposited model re-refined in the SAME engine (neutralises engine bias); do not score occupancy
against deposited values until drift is explained.

## 4. Engine fixes (tools/refine2.py) and re-test
Fixes: (a) f'/f'' were zero in smtbx refinement -> set_inelastic_form_factors(sasaki) from CELL wavelength;
(b) EXTI parsed but never used -> shelx_extinction_correction passed to reparametrisation, refined;
(c) reflections filtered/merged as SHELXL (OMIT s/2theta, SHEL, OMIT hkl; Friedel kept for acentric);
(d) DFIX/DANG free-variable targets (e.g. DFIX 41) were read literally as 41 A -> resolved from FVAR;
(e) AFIX 13 on a PART 0 atom bonded to both disorder parts crashed -> that H fixed at deposited position (logged);
(f) CCTBX BUG: iotbx/shelx/parsers.py process_occupancies_depending_on_free_variable reuses loop variable `i`
    for the scatterer index, so free-variable occupancy groups of >2 atoms link the wrong atoms. Monkeypatched;
(g) damped, shift-limited solver, 40 cycles.

| id | dep R1 | restrained R1 (diff) | max dOcc restr | unrestr dOcc |
|---|---|---|---|---|
| 2312720 | 0.0336 | 0.0336 (-0.0000) | 0.001 | 0.001 |
| 2312754 | 0.0949 | 0.0894 (-0.0055) | 0.084 | 0.120 |
| 2312741 | 0.0366 | 0.0367 (+0.0001) | 0.011 | 0.012 |
| 2312780 | 0.0267 | 0.0273 (+0.0006) | 0.007 | 0.150 |
| 2312781 | 0.0226 | 0.0231 (+0.0005) | 0.006 | 0.003 |
| 2312760 | 0.0251 | 0.0253 (+0.0002) | 0.000 | 0.000 |
| 2312762 | 0.0560 | 0.0562 (+0.0002) | 0.033 | 0.082 |
| 2312703 | 0.0469 | 0.0475 (+0.0006) | 0.000 | 0.000 |
| 2312715 | 0.0304 | 0.0311 (+0.0007) | 0.001 | 0.001 |
| 2312739 | 0.0334 | 0.0348 (+0.0014) | 0.012 | 0.010 |

Gate (9/10): PASS. 9/10 within 0.15% R1 and 0.033 occupancy. Outlier 2312754 uses EADP+SAME, which smtbx
ignores SILENTLY (also SUMP). Of 66 candidates, 23 use EADP/SAME/SUMP, 12 twin/mask, 35 clean.
Design rules: reject or translate unsupported instructions (never silently drop); restraints are needed
(unrestrained occupancy drifts up to 0.15).
