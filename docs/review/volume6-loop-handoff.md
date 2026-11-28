# Volume 6 review loop — handoff

Fresh agents continue from this file alone. The book sources live in `volume6-crossroads/`. The intent note is `docs/plan/book-06.md`. Do not edit book source on the tracker branch.

Reviewed base: `1ccf4e181833cf50bb569e31f0e986124ed579b0` (`origin/main` on 28 November 2026). Volume 6 at that SHA is the text scored below. Round-1 write-up: branch `review/v6-round1`, file `docs/review/volume6-round1-review.md`.

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
| 1 | `1ccf4e181833cf50bb569e31f0e986124ed579b0` | 8/10 | `review/v6-round1` (`docs/review/volume6-round1-review.md`) | open; no fix PRs yet |

Score reason, short: the numbered theorems that were checked (Mertens, Dirichlet, Newman and the prime number theorem, the zero-free constant, the explicit formula, Selberg, Brun, Erdős–Kac, the modular identities) held. Five major defects are false cross-references or a false factor in a solution. Six minors are local. No broken main theorem was found. Details and the list of unchecked work are in the round-1 review.

## Fix PRs

| PR | Issue ids | Head SHA | Merge SHA | Second review | CI |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

No fix PR has been opened. No merge SHA exists.

## CI runs

None for this loop. Round 1 did not run `./build.sh`, did not compile Volume 6, and did not wait on GitHub Actions. Do not treat a missing run as a pass.

## Open issues

All of these are open. Lines are in the source at the base SHA above.

| Id | Severity | Location | Problem |
| --- | --- | --- | --- |
| V6-R1-001 | major | `volume6-crossroads/chapters/ch12-modular.tex:1499` | Tools cite Volume 1, Theorem 9.4 as Cauchy–Schwarz. Item 9.4 is the Wallis product. Cauchy–Schwarz is Theorem 10.4. |
| V6-R1-002 | major | `volume6-crossroads/chapters/ch12-modular.tex:1691` | Tools cite Volume 1, Theorem 9.3 as AM–GM. Theorem 9.3 is l'Hôpital. AM–GM is Theorem 10.3. |
| V6-R1-003 | major | `volume6-crossroads/chapters/ch12-modular.tex:2233` | Extreme-value citation Volume 1, Theorem 3.8 does not exist. The theorem is 4.8. Repeated at line 2246. |
| V6-R1-004 | major | `volume6-crossroads/chapters/ch12-modular.tex:2410` | Tools cite Volume 1, Proposition 7.4 for Vandermonde determinants. Item 7.4 is d'Alembert–Gauss. Vandermonde is Proposition 8.4. |
| V6-R1-005 | major | `volume6-crossroads/chapters/ch06-zeros.tex:759` | Solution says the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. That factor vanishes only at 0 and 1. The pole cancels a zero of \(\zeta\). |
| V6-R1-006 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:183` | Jensen proof calls a neighborhood of the closed disc "slightly smaller". |
| V6-R1-007 | minor | `volume6-crossroads/chapters/ch06-zeros.tex:401` | Says the integral of \(\xi'/\xi\) is real. It is purely imaginary; the count \(2\pi N(T)\) is the imaginary part. |
| V6-R1-008 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:588` | From an \(o(x/\log^2 x)\) error the solution claims an \(O(1/\log^2 x)\) term. The hypothesis gives \(o(1/\log x)\). |
| V6-R1-009 | minor | `volume6-crossroads/chapters/ch05-pnt.tex:196` | Caption says the shaded block has area independent of \(x\). The Euclidean area grows like \(x^2\). The scale-free quantity is the weighted integral. |
| V6-R1-010 | minor | `volume6-crossroads/chapters/ch08-sieves.tex:655` | Says \(\omega(u)/e^{-\gamma}\) tends to infinity as \(u\to 1\). It tends to \(e^{\gamma}\). |
| V6-R1-011 | minor | `volume6-crossroads/chapters/ch10-random.tex:599` | Calls the factor \(1/3\) the cost of independence. Independence costs \(4/9\). The factor \(1/3\) is the distinct-class cost, and that is the comparison that doubles the weight. |

Counts: 0 critical, 5 major, 6 minor.

## Exact next step

Open fix PRs for issues V6-R1-001, V6-R1-002, V6-R1-003, V6-R1-004, V6-R1-005, V6-R1-006, V6-R1-007, V6-R1-008, V6-R1-009, V6-R1-010, and V6-R1-011.

Each fix PR should be small, should name the issue ids it closes, and should not edit volumes other than 6. After a fix PR is open, a different reviewer writes a note and an issue log under `docs/review/`, then the squash merge is allowed only when CI is green on that exact head. Then start round 2 from the new `main` SHA.
