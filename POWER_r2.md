# Round 2: chance of GO before spending on C (exploratory)

*2026-11-09. Not preregistered, and it changes nothing in the protocol. It is meant to inform the decision whether to spend about $85–160 on C runs. Script: `tools/power_r2.py` (20,000 simulations per cell, seed 20261109). Output: `power_r2.json`.*

## Setup

- **B is fixed at its actual round-2 outcomes.** B is the best baseline, with a site detection rate of 0.42–0.44 depending on n.
- **C is simulated from pilot data only,** with the uncertainty in those estimates carried through.
- **Two scenarios for detection:**
  - **transfer:** C keeps its pilot rate conditional on B: 6/9 sites where B detected, 14/27 where B missed. C therefore gains on the easier round-2 tasks.
  - **fixed:** C detects each site at its pilot rate of 20/36, whatever B does. This is pessimistic.
- **Control false positives:** C's pilot rate of 3/10. All three were adjudicated `unsure` or `overfit`, so none would be excused under D2 option a. On pilot evidence, options a and b give the same answer.
- **Median ΔR1:** a bootstrap of C's pilot values.
- **Task handling:** the rule suggested for the amendment: drop the 2 unscoreable tasks, and count B's crash as zero detections.

## Result

| Scenario | n per type | C needs (B + 0.15) | P(detection margin met) | **GO** | INCONCLUSIVE | KILL |
|---|---|---|---|---|---|---|
| transfer | 10 | 0.59 | 0.48 | **0.08** | 0.40 | 0.52 |
| transfer | 15 | 0.59 | 0.43 | **0.10** | 0.42 | 0.47 |
| transfer | 20 | 0.57 | 0.51 | **0.13** | 0.43 | 0.44 |
| fixed | 10 | 0.59 | 0.42 | **0.05** | 0.39 | 0.55 |
| fixed | 15 | 0.59 | 0.37 | **0.08** | 0.42 | 0.50 |
| fixed | 20 | 0.57 | 0.44 | **0.11** | 0.45 | 0.45 |

## What drives it: control false positives, not detection

- **Detection is a coin flip.** Expected C is about 0.57–0.58, right at the bar, so the detection margin is met about 40–50% of the time.
- **The control rule is what sinks GO.** With C's pilot false-positive rate of about 0.3, the ≤ 20% bar is passed only 28–37% of the time. The ≥ 40% KILL line is crossed 38–44% of the time, and that accounts for nearly all of the KILL probability. Detection almost never falls to B's level or below.

The result depends almost entirely on C's true control false-positive rate. Chance of passing the ≤ 20% bar, and of crossing the ≥ 40% KILL line, at a fixed true rate:

| True control FP rate | n = 10 | n = 15 | n = 20 |
|---|---|---|---|
| 0.1 | pass 0.93 / kill 0.01 | 0.94 / 0.00 | 0.96 / 0.00 |
| 0.2 | 0.68 / 0.12 | 0.65 / 0.06 | 0.63 / 0.03 |
| 0.3 (pilot) | 0.38 / 0.35 | 0.30 / 0.28 | 0.24 / 0.23 |

## Reading

1. **At pilot behaviour, round 2 is likely to end INCONCLUSIVE or KILL, not GO** (GO at 5–13%). Spending $85–160 to confirm that has limited value, unless the aim is a clean, published negative result. That aim fits the project's thesis, so it's a legitimate reason to spend.
2. **The open question is C's control false-positive rate, not detection.**
   - One of the pilot's three control false positives (2312879) was partly a harness `undo` error, which is now fixed. Simulated GO with the control false-positive rate held fixed (8,000 simulations):

     | True control FP rate | Scenario | n = 10 | n = 15 | n = 20 |
     |---|---|---|---|---|
     | 0.2 | transfer | 0.15 | 0.22 | 0.27 |
     | 0.2 | fixed | 0.10 | 0.16 | 0.23 |
     | 0.1 | transfer | 0.20 | 0.32 | 0.43 |
     | 0.1 | fixed | 0.14 | 0.23 | 0.35 |

     Even in the best case, n = 10 rarely gives GO: the sign test seldom reaches p < 0.05 on about 30 sites. **If you spend at all, n = 20 is worth the extra cost.**
   - The two baselines alone flag 15–25% of the round-2 controls, and every one of those false positives lowers R1. So these controls may have real unmodelled disorder, which no rule can tell from invention. That makes the adjudication batch you have now informative. If many baseline control false positives turn out `real`, option a would help C. If they're `overfit` or `unsure`, the 20% bar is probably unreachable for any system that models disorder actively.
3. **The cheap next step is your adjudication verdicts,** before any spending. A smaller paid step is to run C on the 20 controls only (about $40–50). That measures the quantity that decides the outcome. If C is above 40% there, the agent angle is killed without paying for the 60 disordered tasks. **Caution:** this changes the staging order, and C's control results would then be known before n and D2 are fixed, so D1 and D2 must be recorded first.
4. **Limits.**
   - The model treats sites as independent, but sites within one task are not.
   - The pilot conditional rates rest on 36 sites.
   - The median-ΔR1 bootstrap assumes C behaves as it did on the pilot.
