# Volume 6 review loop — handoff

Fresh agents continue from this file alone. The book sources live in `volume6-crossroads/`. The intent note is `docs/plan/book-06.md`. Do not edit book source on the tracker branch.

Reviewed base: `1ccf4e181833cf50bb569e31f0e986124ed579b0` (`origin/main` on 28 November 2026). Volume 6 at that SHA is the text scored below.

- Tracker PR: https://github.com/OussamaSegh/Order-and-Chance/pull/314 (draft), branch `review/v6-loop-tracker`. The head is the tip of that branch.
- Round-1 review PR: https://github.com/OussamaSegh/Order-and-Chance/pull/315 (draft), head `797e63664cc972e362af575ec143f3464475e752`, branch `review/v6-round1`, file `docs/review/volume6-round1-review.md`.

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
| 1 | `1ccf4e181833cf50bb569e31f0e986124ed579b0` | 9/10 | https://github.com/OussamaSegh/Order-and-Chance/pull/315 head `797e63664cc972e362af575ec143f3464475e752` | second review recorded; 001–004 confirmed false positives |

Score reason, short: the numbered theorems that were checked (Mertens, Dirichlet, Newman and the prime number theorem, the zero-free constant, the explicit formula, Selberg, Brun, Erdős–Kac, the modular identities) held. The round-1 note first said 8/10, with five majors. Four of those majors were a chapter-count error: Volume 1 starts at Chapter 0, and those citations are already right. They are withdrawn. One major remains, the wrong factor of \(\xi\) in a solution, and six minors remain. No broken main theorem was found.

## Fix PRs

| Issue | PR | Head SHA | Status |
| --- | --- | --- | --- |
| V6-R1-001 | — | — | false positive, confirmed: Volume 1, Theorem 9.4 is Cauchy–Schwarz |
| V6-R1-002 | — | — | false positive, confirmed: Volume 1, Theorem 9.3 is AM–GM |
| V6-R1-003 | — | — | false positive, confirmed: Volume 1, Theorem 3.8 is the extreme-value theorem |
| V6-R1-004 | — | — | false positive, confirmed: Volume 1, Proposition 7.4 is the Vandermonde determinant |
| V6-R1-005 | https://github.com/OussamaSegh/Order-and-Chance/pull/316 | `c8133214f6d4b78f7a8e57be295182d414a9cf0c` | approve |
| V6-R1-006 | https://github.com/OussamaSegh/Order-and-Chance/pull/317 | `9ebe8e6cfa22c830c574a8542547adb06a485320` | approve |
| V6-R1-007 | https://github.com/OussamaSegh/Order-and-Chance/pull/318 | `da5a229c57eabd4dc2cc1df2b64e16b11c7edfcd` | approve |
| V6-R1-008 | https://github.com/OussamaSegh/Order-and-Chance/pull/319 | `33df0274f64a59a82af25c4a66f79d87741714e3` | approve |
| V6-R1-009 | https://github.com/OussamaSegh/Order-and-Chance/pull/320 | `96fae45769cc1fa6220daab1ef597364cf40ae45` | changes made |
| V6-R1-010 | https://github.com/OussamaSegh/Order-and-Chance/pull/321 | `b401cc6c9bc899633cdd8ccc7976ba957005c19e` | approve |
| V6-R1-011 | https://github.com/OussamaSegh/Order-and-Chance/pull/322 | `1f71bb5029783fe35b6d560284e0de3d9cccd876` | approve |

No merge SHA exists. CI on these heads was not inspected.

V6-R1-001 through V6-R1-004 were checked against Volume 1 and not edited. The second reviewer counted the same shared counter in `main.tex` order and confirms those four identifications. Volume 1 was not edited. `volume1-first-principles/main.tex` sets the chapter counter to \(-1\) before the language chapter, so that chapter is Chapter 0. Theorem, proposition, lemma, corollary, definition, and example share one counter. In `main.tex` order: the extreme-value theorem is item 3.8 of the sequences chapter (a continuous function on a segment attains its supremum and its infimum); AM–GM is Theorem 9.3 and Cauchy–Schwarz is Theorem 9.4 of the inequalities chapter; the Vandermonde determinant is Proposition 7.4 of the linear-algebra chapter. The same numbers are already cited elsewhere: Volume 7 cites Theorem 9.4 for the case \(p=2\) and Theorem 9.6 for Hölder; Volume 11 cites Theorem 3.10 for Rolle; Volumes 9 and 10 cite Proposition 7.4 for Vandermonde; Volume 3 cites Theorem 6.4 for d'Alembert–Gauss. The round-1 numbers are that count with every chapter shifted up by one.

## CI runs

None for this loop. Round 1 did not run `./build.sh`, did not compile Volume 6, and did not wait on GitHub Actions. The fixer did not run `./build.sh` either, and did not wait on Actions for the fix PRs. The second reviewer did not run `./build.sh`, did not compile Volume 6, and did not inspect Actions on the reviewed heads. Do not treat a missing run as a pass.

## Open issues

Lines below are in the source at the base SHA above. V6-R1-001 through V6-R1-004 are not defects: the citations match Volume 1. V6-R1-005 through V6-R1-011 have second-review verdicts in the fix-PR table. The note on each fix branch is `docs/review/volume6-r1-NNN-review.md`. For V6-R1-009 the caption fix stands, and the figure node text was changed from “fixed area” to “grows like \(x^2\)”. Font, size, and position were not changed.

| Id | Severity | Location | Problem | Status |
| --- | --- | --- | --- | --- |
| V6-R1-001 | major | `volume6-crossroads/chapters/ch12-modular.tex:1499` | Tools cite Volume 1, Theorem 9.4 as Cauchy–Schwarz. That citation is right. The round-1 count had shifted the chapters up by one. | confirmed false positive |
| V6-R1-002 | major | `volume6-crossroads/chapters/ch12-modular.tex:1691` | Tools cite Volume 1, Theorem 9.3 as AM–GM. That citation is right. | confirmed false positive |
| V6-R1-003 | major | `volume6-crossroads/chapters/ch12-modular.tex:2233` | Tools cite Volume 1, Theorem 3.8 for the extreme-value theorem, including the tools line at 2246. That citation is right. | confirmed false positive |
| V6-R1-004 | major | `volume6-crossroads/chapters/ch12-modular.tex:2410` | Tools cite Volume 1, Proposition 7.4 for Vandermonde determinants. That citation is right. | confirmed false positive |
| V6-R1-005 | major | `volume6-crossroads/chapters/ch06-zeros.tex:759` | Solution says the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. That factor vanishes only at 0 and 1. The pole cancels a zero of \(\zeta\). | approve |
| V6-R1-006 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:183` | Jensen proof calls a neighborhood of the closed disc "slightly smaller". | approve |
| V6-R1-007 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:401` | Says the integral of \(\xi'/\xi\) is real. It is purely imaginary; the count \(2\pi N(T)\) is the imaginary part. | approve |
| V6-R1-008 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:588` | From an \(o(x/\log^2 x)\) error the solution claims an \(O(1/\log^2 x)\) term. The hypothesis gives \(o(1/\log x)\). | approve |
| V6-R1-009 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:196` | Caption says the shaded block has area independent of \(x\). The Euclidean area grows like \(x^2\). The scale-free quantity is the weighted integral. | changes made |
| V6-R1-010 | minor | `volume6-crossroads/chapters/ch08-sieves.tex:655` | Says \(\omega(u)/e^{-\gamma}\) tends to infinity as \(u\to 1\). It tends to \(e^{\gamma}\). | approve |
| V6-R1-011 | minor | `volume6-crossroads/chapters/ch10-random.tex:599` | Calls the factor \(1/3\) the cost of independence. Independence costs \(4/9\). The factor \(1/3\) is the distinct-class cost, and that is the comparison that doubles the weight. | approve |

Round 1 counted 0 critical, 5 major, 6 minor. After the citation check, 001–004 drop out. One major (005) and six minors remain, each with a fix PR.

## Exact next step

Coordinator polls CI on each final head and squash-merges with SHA guard.
