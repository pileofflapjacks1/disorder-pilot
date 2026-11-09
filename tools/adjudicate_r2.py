"""Round-2 blinded adjudication packs (PREREGISTRATION_round2.md, Scoring and staging step 3).

Uses the frozen pilot code without changing it: case folders come from adjudicate.build_case and evidence sheets
from evidence.build. Only the case list, the seed and the README wording are new.

adjudicate_r2.py ROOT build        writes adjudication_r2/_key.json (case -> [task id, system]), prints case numbers
adjudicate_r2.py ROOT case NN      builds adjudication_r2/caseNN/ (models, hkl, case.md, stats.json, evidence.md)
adjudicate_r2.py ROOT index        writes adjudication_r2/README.md, EVIDENCE.md and a blank decisions.csv

Batch 1 (baselines; built 2026-11-08, before any C run): every false-positive structure with dR1 < 0 in the
round-2 sample (all 20 per type, dev tasks excluded) from
  - B2: preregistered;
  - B: an extension, added because B turned out to be the best baseline (RESULTS_r2_baselines.md). Decided before
    any verdict was given; it is recorded in the pre-C amendment.
Cases are sorted, then shuffled with SEED. C's false positives become batch 2 after C runs, numbered on from the
last batch-1 case and shuffled with their own seed, so batch-1 verdicts are given without seeing any C model.
"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adjudicate as ADJ
import evidence as EV

SEED = 20261109
root, cmd = sys.argv[1], sys.argv[2]; out = root + '/adjudication_r2'


def batch1():
    s = json.load(open(root + '/sample_r2.json'))['sample']; cases = []
    for sy in ('B2', 'B'):
        for t in sorted(s):
            for i in s[t]:
                p = '%s/tasks/%s/%s/score.json' % (root, i, sy)
                if not os.path.exists(p): continue
                sc = json.load(open(p))
                if 'error' not in sc and sc['false_positive'] and sc['dR1'] < 0: cases.append((i, sy))
    return sorted(cases)


if cmd == 'build':
    os.makedirs(out, exist_ok=True)
    assert not os.path.exists(out + '/_key.json'), 'key exists; refusing to reshuffle'
    order = batch1(); random.Random(SEED).shuffle(order)
    json.dump({'%02d' % (k + 1): c for k, c in enumerate(order)}, open(out + '/_key.json', 'w'), indent=1)
    print(' '.join('%02d' % (k + 1) for k in range(len(order))))
elif cmd == 'batch2':
    # C's R1-lowering false positives on the sample tasks it has run (dev and dropped tasks excluded), appended to
    # the key after the existing cases, shuffled with SEED2 + the number of cases already in the key (so a
    # controls-first batch 2a and a later 2b are each reproducible). Adds blank rows to decisions.csv.
    SEED2 = 20261110; DROP = {'2240538', '2241940'}
    key = json.load(open(out + '/_key.json')); have = set(tuple(v) for v in key.values())
    s = json.load(open(root + '/sample_r2.json'))['sample']; new = []
    for t in sorted(s):
        for i in s[t]:
            p = '%s/tasks/%s/C/score.json' % (root, i)
            if i in DROP or not os.path.exists(p): continue
            sc = json.load(open(p))
            if 'error' not in sc and sc['false_positive'] and sc['dR1'] < 0 and (i, 'C') not in have: new.append((i, 'C'))
    new = sorted(new); random.Random(SEED2 + len(key)).shuffle(new); start = len(key)
    for k, c in enumerate(new): key['%02d' % (start + k + 1)] = list(c)
    json.dump(key, open(out + '/_key.json', 'w'), indent=1)
    with open(out + '/decisions.csv', 'a') as f:
        for k in range(len(new)): f.write('%02d,,,\n' % (start + k + 1))
    print('added', ' '.join('%02d' % (start + k + 1) for k in range(len(new))) or 'nothing')
elif cmd == 'case':
    ADJ.build_case(root, out, sys.argv[3]); EV.build(out, sys.argv[3])
elif cmd == 'index':
    ADJ.index(root, out); EV.index(out)
    N1 = sum(1 for v in json.load(open(out + '/_key.json')).values() if v[1] != 'C')
    L =open(out + '/README.md').read().split('\n')
    head = ['# Round-2 adjudication: false positives that lower R1', '',
            '**Preregistered** (`PREREGISTRATION_round2.md`). Under option a of rule D2, a control false positive judged `real` does not count against the agent; every other verdict, `unsure` included, counts.', '',
            'Each case is a structure in which a system modelled disorder that the published model does not have, and the result has a lower R1 than the published model. Case numbers are shuffled, and the folders do not say which system made the candidate or whether the structure was a control. The key is in `_key.json`. **Do not open it** until every row of `decisions.csv` has a verdict.', '',
            '**Batches.** Cases 01–%02d (batch 1) come from the rule-based baselines only. Any later cases (batch 2) come from the agent, and they were added after batch 1\'s verdicts were due, so being in batch 2 reveals the system. The same structure can appear more than once, once per system. Judge each case on its own.' % N1, '',
            '**Blinding limits.** Rule-made atom labels (`C901` and so on) show that a model came from a rule system. Only controls are nested, so the `nested` column tells you which cases are controls. Try to judge the density and geometry, not the labels.', '']
    start = next(k for k, l in enumerate(L) if l.startswith('**Negative extra parameters**'))
    open(out + '/README.md', 'w').write('\n'.join(head + L[start:]))
    ev = open(out + '/EVIDENCE.md').read().replace('*Post-hoc, computed,', '*Computed,', 1)
    open(out + '/EVIDENCE.md', 'w').write(ev)
