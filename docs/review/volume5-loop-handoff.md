# Volume 5 review loop — handoff

This file is the state of the Volume 5 fix-and-review loop. A later agent can continue from this file and from the tracking pull request alone.

## Rules

- Keep Volume 4 as it stands. Do not edit `volume4-chance/`.
- Do not start a new Volume 5 review beyond this loop. Stop at **10/10** or after **round 6**, whichever comes first.
- Independent full review, with a regression check of every passage changed by #302, #303, and #304, and of every later fix.
- Small fix pull requests. Each one carries a distinct second-reviewer note under `docs/review/`.
- Squash-merge only when every non-skipped check is green on the exact reviewed head: `gh pr merge --squash --match-head-commit <SHA>`.
- Do not weaken a proof silently. Do not change numbered-statement numbers. Do not change caption or diagram typography. No releases. No force-push of `main`.
- Score out of 10. Critical = false statement or broken proof. Major = genuine gap or a wrong citation of a needed result. Minor = local slip or a missing one-line reason. 10/10 means nothing open.

## Repository

- Repo: `OussamaSegh/Order-and-Chance`
- Loop base when this handoff was opened: `337b1230584fea95ffb538cdbeb373c0fe2d2113`
- Volume 5 source order: `volume5-calculation/main.tex`. `bbp-borwein.tex` is included from the integrals chapter.

## Already on main before this resumed loop

| Item | PR | Merge SHA |
| --- | --- | --- |
| Round-1 review, 7/10 (0 critical, 2 major, 8 minor) | #298 | `2b3a8dfe8c0a28f5025d55ec01562f20570ce17f` |
| Eight one-line gaps | #304 | `39d89e64f7af507193108a94bce3b84ba179874d` |
| FFT length and wrapped index | #302 | `41356cffdca1bab001548c45b91ef6fae74eed7c` |
| Binary-digit blocks by exponent | #303 | `1b17516df6edd3edfefa813dbc6a24cd2c856c07` |

Those three fixes were re-read in round 2. All ten repaired passages hold. Regression count: 0.

## Round 2

**Score: 8/10.** 0 critical, 0 major, 4 minor. Draft review: #311.

The four gaps were fixed in #312, squash-merged as `1ccf4e181833cf50bb569e31f0e986124ed579b0` from head `4c8762e01c5d1fc57cb1262821c306b6f5cdadf9`. Second reading: `docs/review/volume5-round2-fix-second-review-2026-11-28.md`.

## Round 3

**Score: 10/10.** 0 critical, 0 major, 0 minor. Regressions: 0. The loop stops here. Draft review to be linked from the tracker comment.

## Next step

None. Volume 5 is 10/10 on main at `1ccf4e181833cf50bb569e31f0e986124ed579b0`. Do not open another fix. Do not edit Volume 4.

Tracker pull request: #310.

## Do not

- Edit Volume 4.
- Close or reopen Volume 5 review logs that are already on main.
- Upload to KDP or make a release.
