# Volume 6 review loop — handoff

Fresh agents continue from this file alone. The book sources live in `volume6-crossroads/`. The intent note is `docs/plan/book-06.md`. Do not edit book source on the tracker branch.

Round 1 reviewed `1ccf4e181833cf50bb569e31f0e986124ed579b0`. Round 2 reviewed `614400b0061f715658cee0266f0b5b07640a7c77`, which is `origin/main` after the seven fix merges. Volume 6 at that SHA is the text scored in round 2.

- Tracker PR: https://github.com/OussamaSegh/Order-and-Chance/pull/314 (draft), branch `review/v6-loop-tracker`. The head is the tip of that branch.
- Round-1 review PR: https://github.com/OussamaSegh/Order-and-Chance/pull/315 (draft), head `797e63664cc972e362af575ec143f3464475e752`, branch `review/v6-round1`, file `docs/review/volume6-round1-review.md`.
- Round-2 review PR: https://github.com/OussamaSegh/Order-and-Chance/pull/323 (draft), head `6f6d501532670cd3c6e2ee1ac185fd5084678dd7`, branch `review/v6-round2`, file `docs/review/volume6-round2-review.md`. The first posting, head `0219f8a105140fa118d5d6b0066ae7bd06509c58`, said 10/10. The second, head `6909a9f82090c034858fb469fd7d56f73ad8cdb3`, said 9/10 with two minors.

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
| 1 | `1ccf4e181833cf50bb569e31f0e986124ed579b0` | 8/10 | https://github.com/OussamaSegh/Order-and-Chance/pull/315 head `797e63664cc972e362af575ec143f3464475e752` | first posting; the same note then corrected the score to 9/10 |
| 2 | `614400b0061f715658cee0266f0b5b07640a7c77` | 9/10 | https://github.com/OussamaSegh/Order-and-Chance/pull/323 head `6f6d501532670cd3c6e2ee1ac185fd5084678dd7` | six minors open; the first posting said 10/10 |

Score reason, short. Round 1 first said 8/10, with five majors and six minors. Four majors were a chapter-count error: Volume 1 starts at Chapter 0, and those citations were already right. They were withdrawn. The corrected note on #315 scores the volume 9/10: one major, the wrong factor of \(\xi\) in a solution, and six minors. No broken main theorem was found. Those seven fixes are merged. Round 2 first said 10/10, with no regression in the seven fixes. Later checks found six minor slips, so the corrected score is 9/10. No numbered theorem is among them. Round 2 did not run `./build.sh`.

## Fix PRs

| Issue | PR | Head SHA | Status |
| --- | --- | --- | --- |
| V6-R1-001 | — | — | false positive, confirmed: Volume 1, Theorem 9.4 is Cauchy–Schwarz |
| V6-R1-002 | — | — | false positive, confirmed: Volume 1, Theorem 9.3 is AM–GM |
| V6-R1-003 | — | — | false positive, confirmed: Volume 1, Theorem 3.8 is the extreme-value theorem |
| V6-R1-004 | — | — | false positive, confirmed: Volume 1, Proposition 7.4 is the Vandermonde determinant |
| V6-R1-005 | https://github.com/OussamaSegh/Order-and-Chance/pull/316 | `c8133214f6d4b78f7a8e57be295182d414a9cf0c` | merged `07ee61e6c6bb6054eb6abe9e9f595a1d83dd0df1` |
| V6-R1-006 | https://github.com/OussamaSegh/Order-and-Chance/pull/317 | `9ebe8e6cfa22c830c574a8542547adb06a485320` | merged `6f48c1a6d2d821e8bf737552af9c21e682ba9767` |
| V6-R1-007 | https://github.com/OussamaSegh/Order-and-Chance/pull/318 | `da5a229c57eabd4dc2cc1df2b64e16b11c7edfcd` | merged `e89e3e81a1504cf15738158c0502d4e8b16c1cc0` |
| V6-R1-008 | https://github.com/OussamaSegh/Order-and-Chance/pull/319 | `33df0274f64a59a82af25c4a66f79d87741714e3` | merged `807bc0b5bceb26936c1841e0bdc8b6ea514296b6` |
| V6-R1-009 | https://github.com/OussamaSegh/Order-and-Chance/pull/320 | `96fae45769cc1fa6220daab1ef597364cf40ae45` | merged `d7a6b91136588cee99c00d177bd82a14154a4393` |
| V6-R1-010 | https://github.com/OussamaSegh/Order-and-Chance/pull/321 | `b401cc6c9bc899633cdd8ccc7976ba957005c19e` | merged `8dd2da41f42f20dfdbe5d47c14911b7eb378effb` |
| V6-R1-011 | https://github.com/OussamaSegh/Order-and-Chance/pull/322 | `1f71bb5029783fe35b6d560284e0de3d9cccd876` | merged `614400b0061f715658cee0266f0b5b07640a7c77` |

Each row’s head SHA is the head GitHub reports for that merged PR, and it matches the second-review head. Each merge SHA is that PR’s merge commit. `origin/main` is `614400b0061f715658cee0266f0b5b07640a7c77`, the #322 squash. This update did not re-read the Actions logs. The merger’s tracker comments name a successful `build (volume6-crossroads)` on each reviewed head and a skipped `publish`.

V6-R1-001 through V6-R1-004 were checked against Volume 1 and not edited. The second reviewer counted the same shared counter in `main.tex` order and confirms those four identifications. Volume 1 was not edited. `volume1-first-principles/main.tex` sets the chapter counter to \(-1\) before the language chapter, so that chapter is Chapter 0. Theorem, proposition, lemma, corollary, definition, and example share one counter. In `main.tex` order: the extreme-value theorem is item 3.8 of the sequences chapter (a continuous function on a segment attains its supremum and its infimum); AM–GM is Theorem 9.3 and Cauchy–Schwarz is Theorem 9.4 of the inequalities chapter; the Vandermonde determinant is Proposition 7.4 of the linear-algebra chapter. The same numbers are already cited elsewhere: Volume 7 cites Theorem 9.4 for the case \(p=2\) and Theorem 9.6 for Hölder; Volume 11 cites Theorem 3.10 for Rolle; Volumes 9 and 10 cite Proposition 7.4 for Vandermonde; Volume 3 cites Theorem 6.4 for d'Alembert–Gauss. The round-1 numbers are that count with every chapter shifted up by one.

## CI runs

Round 1, the fixer, the second reviewer, and the round-2 reviewer did not run `./build.sh`. The seven fix PRs’ runs, as named for this update, are `46157051597`, `46157052642`, `46157053523`, `46157052117`, `46157051401`, `46157052179`, and `46157053076`. Each is reported green, with `publish` skipped. This handoff update did not open those logs. Do not treat an unread log as a pass.

## Open issues

Six, all minor, in `volume6-crossroads/` at `614400b0061f715658cee0266f0b5b07640a7c77`.

| Id | Severity | Location | Problem | Status |
| --- | --- | --- | --- | --- |
| V6-R2-001 | minor | `volume6-crossroads/chapters/ch12-modular.tex:2139` | The idea for `pb:twosquares` says \(F^2=\zeta(s)L(s,\chi_4)\). The identity in the problem multiplies by \((1-2^{-s})^{-1}\prod_{p\equiv3\pmod4}(1-p^{-2s})^{-1}\), about \(2.336\) at \(s=1\). | open |
| V6-R2-002 | minor | `volume6-crossroads/chapters/ch12-modular.tex:2318` | The solution gives \((\psi(x)-x)/\log x\) the \(66\,112\) sign changes below \(10^8\). That count is the one the problem states for \(\Pi(x)-\operatorname{li}(x)\). The count for \(\psi(x)-x\) is \(65\,162\). | open |
| V6-R2-003 | minor | `volume6-crossroads/chapters/ch02-averages.tex:283` | Cramér’s constant is written \(0.6543\ldots\). It is \(0.65428397\ldots\). | open |
| V6-R2-004 | minor | `volume6-crossroads/chapters/ch01-mertens.tex:681` | The ratio at \(1000\) is written \(0.996133\ldots\). It is \(0.99613283\ldots\). The four-decimal value \(0.9961\) is right. | open |
| V6-R2-005 | minor | `volume6-crossroads/figures/ch01-tenfactorial.tex:19` | The upper block on the prime \(3\) uses the dark ink of multiples of \(p^3\). That block is \(\lfloor 10/9\rfloor=1\), the multiples of \(p^2\). | open |
| V6-R2-006 | minor | `volume6-crossroads/chapters/ch03-characters.tex:241` | The beauty note says \(r(n)\) counts ideals for a general real character. For the character modulo \(12\) induced by \(\chi_{-4}\), \(r(3)=1\), and no ideal of \(\mathbb Q(i)\) has norm \(3\). | open |

The round-1 rows below are closed. V6-R1-001 through V6-R1-004 were false positives. V6-R1-005 through V6-R1-011 are merged. The note on each fix is `docs/review/volume6-r1-NNN-review.md`. For V6-R1-009 the figure node text changed from “fixed area” to “grows like \(x^2\)”, without a change of font, size, or position. Line numbers below are the pre-fix lines.

| Id | Severity | Location | Problem | Status |
| --- | --- | --- | --- | --- |
| V6-R1-001 | major | `volume6-crossroads/chapters/ch12-modular.tex:1499` | Tools cite Volume 1, Theorem 9.4 as Cauchy–Schwarz. That citation is right. The round-1 count had shifted the chapters up by one. | confirmed false positive |
| V6-R1-002 | major | `volume6-crossroads/chapters/ch12-modular.tex:1691` | Tools cite Volume 1, Theorem 9.3 as AM–GM. That citation is right. | confirmed false positive |
| V6-R1-003 | major | `volume6-crossroads/chapters/ch12-modular.tex:2233` | Tools cite Volume 1, Theorem 3.8 for the extreme-value theorem, including the tools line at 2246. That citation is right. | confirmed false positive |
| V6-R1-004 | major | `volume6-crossroads/chapters/ch12-modular.tex:2410` | Tools cite Volume 1, Proposition 7.4 for Vandermonde determinants. That citation is right. | confirmed false positive |
| V6-R1-005 | major | `volume6-crossroads/chapters/ch06-zeros.tex:759` | Solution says the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. That factor vanishes only at 0 and 1. The pole cancels a zero of \(\zeta\). | merged |
| V6-R1-006 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:183` | Jensen proof calls a neighborhood of the closed disc "slightly smaller". | merged |
| V6-R1-007 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:401` | Says the integral of \(\xi'/\xi\) is real. It is purely imaginary; the count \(2\pi N(T)\) is the imaginary part. | merged |
| V6-R1-008 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:588` | From an \(o(x/\log^2 x)\) error the solution claims an \(O(1/\log^2 x)\) term. The hypothesis gives \(o(1/\log x)\). | merged |
| V6-R1-009 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:196` | Caption says the shaded block has area independent of \(x\). The Euclidean area grows like \(x^2\). The scale-free quantity is the weighted integral. | merged |
| V6-R1-010 | minor | `volume6-crossroads/chapters/ch08-sieves.tex:655` | Says \(\omega(u)/e^{-\gamma}\) tends to infinity as \(u\to 1\). It tends to \(e^{\gamma}\). | merged |
| V6-R1-011 | minor | `volume6-crossroads/chapters/ch10-random.tex:599` | Calls the factor \(1/3\) the cost of independence. Independence costs \(4/9\). The factor \(1/3\) is the distinct-class cost, and that is the comparison that doubles the weight. | merged |

Round 1 first counted 0 critical, 5 major, 6 minor, and the note then withdrew 001–004. The remaining one major and six minors are merged. Round 2 first counted 0 critical, 0 major, 0 minor, and 0 regressions in #316–#322. The corrected count is 0 critical, 0 major, 6 minor.

## Exact next step

Open small fix PRs for V6-R2-001 through V6-R2-006, against `614400b0061f715658cee0266f0b5b07640a7c77`. Do not reopen V6-R1-001–004. Do not edit book source on this tracker branch. For V6-R2-005, change only the fill of that one rectangle.
