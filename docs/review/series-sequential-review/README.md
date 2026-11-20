# Series sequential review

Review only. Notes live here. Book source is not edited on this branch.

Reading order is each volume’s `main.tex`. Scores use the scale in the volume files: critical means a false statement or a broken proof; major means a genuine gap, a substantive use before introduction, or a wrong citation of a needed result; minor means a local slip, a style fault, or a small clarity issue.

| Volume | Status |
| --- | --- |
| 1 First Principles | 7/10. 0 critical, 13 major, 78 minor. See [volume1.md](volume1.md). |
| 2 The Integers | 7/10. 0 critical, 4 major, 47 minor. See [volume2.md](volume2.md). |
| 3 Symmetry | 7/10. 0 critical, 4 major, 32 minor. See [volume3.md](volume3.md). |
| 4 Chance | 6/10. 1 critical, 10 major, 13 minor. See [volume4.md](volume4.md). |
| 5 Calculation | 7/10. 0 critical, 5 major, 18 minor. See [volume5.md](volume5.md). |
| 6 Crossroads | 8/10. 0 critical, 0 major, 10 minor. See [volume6.md](volume6.md). |
| 7 Spaces | 7/10. 0 critical, 1 major, 10 minor. See [volume7.md](volume7.md). |
| 8 Analysis | 8/10. 0 critical, 0 major, 11 minor. See [volume8.md](volume8.md). |
| 9 Shapes | 9/10. 0 critical, 0 major, 2 minor. See [volume9.md](volume9.md). |
| 10 Abstraction | 9/10. 0 critical, 0 major, 6 minor. See [volume10.md](volume10.md). |
| 11 Randomness | 8/10. 0 critical, 2 major, 7 minor. See [volume11.md](volume11.md). |
| 12 Random Motion | 9/10. 0 critical, 0 major, 4 minor. See [volume12.md](volume12.md). |
| 13 Arithmetic | 8/10. 0 critical, 1 major, 7 minor. See [volume13.md](volume13.md). |
| 14 The Primes | 7/10. 0 critical, 2 major, 6 minor. See [volume14.md](volume14.md). |
| 15 Order and Chance | not started |

The concept ledger is [CONCEPT-LEDGER.md](CONCEPT-LEDGER.md). Volume 1 is the first section. Later reviews append their own section and check new uses against earlier lines.

## Handoff (paused 2026-11-20, 06:40 Paris)

The chain stopped after Volume 13 at 86.8% of the weekly usage limit; Volume 14 was then run at the author's request (usage 89.4% after it). Volumes 1–14 are complete: each has its log, its ledger section and its status line above. Branch head before this update: `efcd5a9c`.

To continue:

1. Review Volume 15 on this branch. Volume 14 is recorded in [volume14.md](volume14.md). Use the brief in [briefs/series-review-v15.md](briefs/series-review-v15.md). The general form is [briefs/series-sequential-review-template.md](briefs/series-sequential-review-template.md).
2. After each volume, check that `volumeN.md` exists, that the ledger has a "Volume N" section, that every exercise was read, and that this table is updated.
3. Spot-check Volume 9. Its review ran in 25 minutes and found only 2 minor issues, so its depth is uncertain.
4. Then write a series summary and propose fixes: one small PR per volume, each with a distinct second reviewer and an issue log, merged by squash with `--match-head-commit` on green CI. No book source is changed before the author approves.
