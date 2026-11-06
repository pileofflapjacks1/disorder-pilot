# Skeptic calibration: results (2026-11-05)

The plan and decision rule are in `PLAN.md`, written before the run. The skeptic's verdicts and reasoning are in `skeptic_verdicts.csv`.

**Outcome by the frozen rule: usable only as a flag for expert review, never as an automatic filter.**
- Reject agreement met the bar for trust (9/11 against ≥ 9/11).
- But there was **one dangerous miss**, and the rule for trust allows none.

| Metric | Result | Bar for trust |
|---|---|---|
| Exact agreement (4 categories) | 6/11 | – |
| Reject agreement (overfit/artefact vs real/unsure) | **9/11**, Cohen's κ = 0.61 | ≥ 9/11 ✓ |
| Dangerous misses (skeptic `real`, expert `overfit`) | **1** (case 11) | 0 ✗ |

| Case | Expert | Skeptic | Agree on reject? |
|---|---|---|---|
| 01 | unsure | real | yes |
| 02 | unsure | artefact | **no** |
| 03 | unsure | unsure | yes |
| 04 | overfit | overfit | yes |
| 05 | overfit | overfit | yes |
| 06 | overfit | artefact | yes |
| 07 | overfit | overfit | yes |
| 08 | unsure | real | yes |
| 09 | overfit | overfit | yes |
| 10 | overfit | overfit | yes |
| 11 | overfit | real | **no** (dangerous miss) |

**Reading:**

- **The skeptic agrees with the expert on every clear case.** Each of the expert's five clear-cut rejections (04, 05, 07, 09, 10) got the same rejection. For case 06 the skeptic chose `artefact` rather than `overfit`, but both reject the candidate.
- **The disagreements fall on the borderline structures.**
  - **Case 11 (the dangerous miss):** the expert's own note says the deposited model looks only "a little better" and the candidate "looks pretty good".
  - **Case 02:** the skeptic called `artefact` where the expert was unsure. The sealed literature report, read after both sets of verdicts were recorded, also points to an absorption or ripple artefact for this structure.
  - **Cases 01 and 08:** the skeptic called both `real` where the expert was unsure. The literature partly supports case 01: the paper describes the agent's split.
- **The skeptic says `real` more readily than the expert.** It did so in 3 of 11 cases; the expert never did. Two of those three (cases 08 and 11) are the same ester group in one control structure, modelled once by each system. An automated skeptic would therefore let some of the false positives the expert rejects through. That is exactly the failure that blocked GO in the pilot.

**Compared with cifaudit,** where the model's judgement disagreed with the expert's (κ = −0.18), agreement here is much better. Two differences may explain it: these questions are narrower (one candidate split, with computed evidence attached), and every case comes with quantitative checks.

**Implication for round 2:** a skeptic step can be built, but its output must go to a human. Use it to rank or flag candidate splits, and to explain the evidence, not to approve or reject them automatically. Any automatic use would first need validation on a larger expert-labelled set than these 11 cases.

**Limits:**
- n = 11, with only two expert classes present.
- One skeptic run, and one expert.
- The skeptic saw only the computed evidence; the expert also used Olex2 and the figures.
- The skeptic and the agent under test are the same model family.
