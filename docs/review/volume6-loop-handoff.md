# Volume 6 review loop — handoff

Fresh agents continue from this file alone. The book sources live in `volume6-crossroads/`. The intent note is `docs/plan/book-06.md`. Do not edit book source on the tracker branch.

Reviewed base: `1ccf4e181833cf50bb569e31f0e986124ed579b0` (`origin/main` on 28 November 2026). Volume 6 at that SHA is the text scored below.

- Tracker PR: https://github.com/OussamaSegh/Order-and-Chance/pull/314 (draft), branch `review/v6-loop-tracker`. The head is the tip of that branch.
- Round-1 review PR: https://github.com/OussamaSegh/Order-and-Chance/pull/315 (draft), head `430f6426c9edef495fadc707bf34a2e66413e14b`, branch `review/v6-round1`, file `docs/review/volume6-round1-review.md`.

## Goal

Bring Volume 6 to 10/10. The loop is: review, then small fix PRs, then a distinct second reviewer for each fix (a note and an issue log under `docs/review/`), then a SHA-guarded squash merge on green CI of the exact reviewed head, then a fresh re-review. At most 6 rounds.

## Rules

- Never fabricate a check, a build, or a CI result. Say what was not checked.
- Never weaken a proof silently.
- Keep theorem numbering stable. If a number must move, update cross-references across the whole series in the same change.
- Do not change caption or diagram typography. Wording and numbers in captions may change.
- Keep numerical checks separate from proofs.
- No releases, no KDP uploads, and no force-push to `main`.
- Do not edit other volumes. Volumes 1–3 are published and locked. Volume 4 stays untouched. Wrong Volume 1 numbers in Volume 6 are fixed by correcting the citation in Volume 6, not by renumbering Volume 1.

## Round and score

| Round | Base SHA | Score | Review | Status |
| --- | --- | --- | --- | --- |
| 1 | `1ccf4e181833cf50bb569e31f0e986124ed579b0` | 8/10 | https://github.com/OussamaSegh/Order-and-Chance/pull/315 head `430f6426c9edef495fadc707bf34a2e66413e14b` | fix PRs open for 005–011; 001–004 not changed |

Score reason, short: the numbered theorems that were checked (Mertens, Dirichlet, Newman and the prime number theorem, the zero-free constant, the explicit formula, Selberg, Brun, Erdős–Kac, the modular identities) held. The round-1 note called five majors false cross-references or a false factor, and six minors local. The fixer rechecked the four Volume 1 citations and did not change them; see the fix table. No broken main theorem was found. Details and the list of unchecked work are in the round-1 review.

## Fix PRs

| Issue | PR | Head SHA | Status |
| --- | --- | --- | --- |
| V6-R1-001 | — | — | not fixed: Volume 1, Theorem 9.4 is Cauchy–Schwarz |
| V6-R1-002 | — | — | not fixed: Volume 1, Theorem 9.3 is AM–GM |
| V6-R1-003 | — | — | not fixed: Volume 1, Theorem 3.8 is the extreme-value theorem |
| V6-R1-004 | — | — | not fixed: Volume 1, Proposition 7.4 is the Vandermonde determinant |
| V6-R1-005 | https://github.com/OussamaSegh/Order-and-Chance/pull/316 | `4e5e9f9b39eeb2512d2dbeaab38981d85fed4f61` | awaiting second review |
| V6-R1-006 | https://github.com/OussamaSegh/Order-and-Chance/pull/317 | `69509de69e9dabd20543172ac7109c4255eaf410` | awaiting second review |
| V6-R1-007 | https://github.com/OussamaSegh/Order-and-Chance/pull/318 | `bc259a0714c97849c2954ca15623574e8f5c786b` | awaiting second review |
| V6-R1-008 | https://github.com/OussamaSegh/Order-and-Chance/pull/319 | `fdb78a6986ab4083b86acb80e3bf06e1c766feb4` | awaiting second review |
| V6-R1-009 | https://github.com/OussamaSegh/Order-and-Chance/pull/320 | `2ee2109c21a35258c477003d752082b404a36cfc` | awaiting second review |
| V6-R1-010 | https://github.com/OussamaSegh/Order-and-Chance/pull/321 | `8165cac2c8e21fb7e641cbe78d3464fb93b5e041` | awaiting second review |
| V6-R1-011 | https://github.com/OussamaSegh/Order-and-Chance/pull/322 | `1b4174929a3440a3ae9d9fb0e5b8f07b6740f1fb` | awaiting second review |

No merge SHA exists. CI on these heads was not inspected.

V6-R1-001 through V6-R1-004 were checked against Volume 1 and not edited. `volume1-first-principles/main.tex` sets the chapter counter to \(-1\) before the language chapter, so that chapter is Chapter 0. Theorem, proposition, lemma, corollary, definition, and example share one counter. In `main.tex` order: the extreme-value theorem is item 3.8 of the sequences chapter (a continuous function on a segment attains its supremum and its infimum); AM–GM is Theorem 9.3 and Cauchy–Schwarz is Theorem 9.4 of the inequalities chapter; the Vandermonde determinant is Proposition 7.4 of the linear-algebra chapter. The same numbers are already cited elsewhere: Volume 7 cites Theorem 9.4 for the case \(p=2\) and Theorem 9.6 for Hölder; Volume 11 cites Theorem 3.10 for Rolle; Volumes 9 and 10 cite Proposition 7.4 for Vandermonde; Volume 3 cites Theorem 6.4 for d'Alembert–Gauss. The round-1 numbers are that count with every chapter shifted up by one.

## CI runs

None for this loop. Round 1 did not run `./build.sh`, did not compile Volume 6, and did not wait on GitHub Actions. The fixer did not run `./build.sh` either, and did not wait on Actions for the fix PRs. Do not treat a missing run as a pass.

## Open issues

Lines below are in the source at the base SHA above. V6-R1-001 through V6-R1-004 are not defects: the citations match Volume 1. V6-R1-005 through V6-R1-011 have fix PRs awaiting a second review.

| Id | Severity | Location | Problem | Status |
| --- | --- | --- | --- | --- |
| V6-R1-001 | major | `volume6-crossroads/chapters/ch12-modular.tex:1499` | Tools cite Volume 1, Theorem 9.4 as Cauchy–Schwarz. That citation is right. The round-1 count had shifted the chapters up by one. | not a defect |
| V6-R1-002 | major | `volume6-crossroads/chapters/ch12-modular.tex:1691` | Tools cite Volume 1, Theorem 9.3 as AM–GM. That citation is right. | not a defect |
| V6-R1-003 | major | `volume6-crossroads/chapters/ch12-modular.tex:2233` | Tools cite Volume 1, Theorem 3.8 for the extreme-value theorem, including the tools line at 2246. That citation is right. | not a defect |
| V6-R1-004 | major | `volume6-crossroads/chapters/ch12-modular.tex:2410` | Tools cite Volume 1, Proposition 7.4 for Vandermonde determinants. That citation is right. | not a defect |
| V6-R1-005 | major | `volume6-crossroads/chapters/ch06-zeros.tex:759` | Solution says the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. That factor vanishes only at 0 and 1. The pole cancels a zero of \(\zeta\). | awaiting second review |
| V6-R1-006 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:183` | Jensen proof calls a neighborhood of the closed disc "slightly smaller". | awaiting second review |
| V6-R1-007 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:401` | Says the integral of \(\xi'/\xi\) is real. It is purely imaginary; the count \(2\pi N(T)\) is the imaginary part. | awaiting second review |
| V6-R1-008 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:588` | From an \(o(x/\log^2 x)\) error the solution claims an \(O(1/\log^2 x)\) term. The hypothesis gives \(o(1/\log x)\). | awaiting second review |
| V6-R1-009 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:196` | Caption says the shaded block has area independent of \(x\). The Euclidean area grows like \(x^2\). The scale-free quantity is the weighted integral. | awaiting second review |
| V6-R1-010 | minor | `volume6-crossroads/chapters/ch08-sieves.tex:655` | Says \(\omega(u)/e^{-\gamma}\) tends to infinity as \(u\to 1\). It tends to \(e^{\gamma}\). | awaiting second review |
| V6-R1-011 | minor | `volume6-crossroads/chapters/ch10-random.tex:599` | Calls the factor \(1/3\) the cost of independence. Independence costs \(4/9\). The factor \(1/3\) is the distinct-class cost, and that is the comparison that doubles the weight. | awaiting second review |

Round 1 counted 0 critical, 5 major, 6 minor. After the citation check, 001–004 drop out. One major (005) and six minors remain, each with a fix PR.

## Exact next step

Distinct second reviewer reviews each fix PR and adds docs/review/volume6-r1-NNN-review.md.
