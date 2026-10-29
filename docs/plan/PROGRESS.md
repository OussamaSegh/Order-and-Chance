# Implementation tracker

This is the execution list for Edition 1. The reasoning lives in [SERIES-CONTENT-PLAN.md](SERIES-CONTENT-PLAN.md) and the chapter plans beside it. Titles and subtitles are frozen. Part names stay the catalog's, except the two renames in steps 4 and 7.

Paths below are the directories on `main` after step 0. The retired names (`tome0-mathematical-maturity`, `tome9-higher-structures`, `tome14-order-and-chance`, and the other pre-renumbering stems) are gone.

| Book | Directory |
| --- | --- |
| 1 First Principles | `tome1-first-principles` |
| 2 The Integers | `tome2-integers` |
| 3 Symmetry | `tome3-symmetry` |
| 4 Chance | `tome4-chance` |
| 5 Calculation | `tome5-calculation` |
| 6 Crossroads | `tome6-crossroads` |
| 7 Spaces | `tome7-spaces` |
| 8 Analysis | `tome8-analysis` |
| 9 Shapes | `tome9-shapes` |
| 10 Abstraction | `tome10-abstraction` |
| 11 Randomness | `tome11-randomness` |
| 12 Random Motion | `tome12-random-motion` |
| 13 Arithmetic | `tome13-arithmetic` |
| 14 The Primes | `tome14-primes` |
| 15 Order and Chance | `tome15-order-and-chance` |

## Resume protocol

1. Read this file. Find the first step whose status is not DONE.
2. If that step is IN REVIEW or IN PROGRESS, open its PR link. Continue that branch. Do not open a second PR for the same step.
3. If that step is TODO, search the open pulls for its id (for example `step 4`) before creating a branch. If a branch or PR already exists, use it.
4. Do the step. In the same PR, set this row to IN REVIEW, fill the PR link, and leave merge sha and date blank.
5. The editor marks the row DONE, with the merge sha and the date, after the PR merges. If the editor has not done that when the next step starts, the next step's PR marks the previous row DONE from the merge commit.
6. Do not start step \(n+1\) while step \(n\) is TODO, IN PROGRESS, or IN REVIEW.
7. Do not edit a book a later step has not reached, and do not reopen a move this file marks DONE.
8. Leave the repaired proofs alone. They are listed under "Already repaired" in the series plan. The exception is the second reading of three squares, which is part of step 4.

A step is one PR. It is one book, or one move between books. Acceptance always includes `git diff --check` and `./build.sh` on every stem the step touches.

## Steps

### 0. Merge PR #26 renumbering + final titles

- **Status:** DONE
- **Depends on:** none
- **Books and files:** the whole catalog. New stems `tome1-first-principles` through `tome15-order-and-chance`. `common/series-catalog.json`, `docs/SERIES-STRUCTURE.md`.
- **Acceptance:** Books 1–15 use the frozen titles. There is no P1 volume. Book 6 is Crossroads, *Arithmetic Meets Analysis*. The old problem book's problems are appended to Books 1–6.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/26
- **Merge sha:** 68aff65f87b4e37a5c0e45d4d866842897749c5c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the renumbering.

### 1. Merge this plan

- **Status:** IN REVIEW
- **Depends on:** 0
- **Books and files:** `docs/plan/` only. No manuscript.
- **Acceptance:** `SERIES-CONTENT-PLAN.md`, `book-01.md` through `book-15.md`, and this file are on `main`. Part names in the plan are the catalog's. The two proposed renames are marked as proposals.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/27
- **Merge sha:**
- **Date:**
- **Notes:** This PR. The editor marks it DONE after merge.

### 2. Spaces: conditional expectation, and the almost-every chapter

- **Status:** TODO
- **Depends on:** 1
- **Books and files:** `tome7-spaces`. Promote conditional expectation, including the tower property, from the exercise in `chapters/ch10-radon.tex` to a numbered theorem. Retitle `chapters/ch12-harder.tex` to Almost every number, still inside Measures on Spaces.
- **Acceptance:** Books 11 and 12 can cite the tower as a theorem of Book 7. The problem chapter's title is no longer "Harder problems". `./build.sh tome7-spaces`.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Do this before any edit to Randomness or Random Motion.

### 3. Orders, from Chance to First Principles

- **Status:** TODO
- **Depends on:** 2
- **Books and files:** `tome4-chance/chapters/orders.tex` moves into `tome1-first-principles`, inside Algebra, Limits and Functions. Appendix B of Chance stays.
- **Acceptance:** Dilworth, Sperner, and partial orders are in Book 1. Book 4's Random Structures no longer contains that appendix. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 4. Hidden worlds, from The Integers to Arithmetic

- **Status:** TODO
- **Depends on:** 3
- **Books and files:** `tome2-integers` (`ch11-algebraic.tex`, `ch12-ideals.tex`, `ch12-padic.tex`) and `tome13-arithmetic`. Hensel's lemma for a congruence stays in Book 2. One section keeps \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). While Arithmetic is open, read the repaired three-squares test in `ch07-hasse.tex` once.
- **Acceptance:** Those three chapters are in Book 13's Number Fields and Local and Global parts. Book 2 still proves Pell, the Gaussian integers, and reciprocity. Apply the proposed part rename in `common/series-catalog.json`: Book 2, Part IV, **Equations and Characters**. Regenerate the series files from that catalog. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** This is the only PR that renames Book 2's part.

### 5. The adèles, from Analysis to Arithmetic

- **Status:** TODO
- **Depends on:** 4
- **Books and files:** `tome8-analysis/chapters/ch08-haar.tex` and `tome13-arithmetic` (local fields and Tate). Haar measure and Pontryagin duality stay in Fourier and Tauberian Methods.
- **Acceptance:** The construction of \(\mathbb Q_p\) and the adèles, beyond Haar measure, is in Book 13. Book 8 still states the duality it uses. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Do not move Jordan or the Riemann mapping theorem in this PR.

### 6. Symmetry's extra linear algebra

- **Status:** TODO
- **Depends on:** 5
- **Books and files:** `tome3-symmetry` appendices, `tome8-analysis`, `tome10-abstraction`. Spectral theorem, SVD, graph spectra, matrix inequalities, linear dynamics, and the linear algebra that repeats Book 1 go to Analysis. Tensors go to Abstraction, Categories. Circulants, Perron roots of a symmetry, and the linear algebra method stay in Book 3.
- **Acceptance:** Book 3's contents are Groups, Rings and Polynomials, and Fields and Galois Theory, plus the appendices that still count by symmetry. Analysis and Abstraction build with the new files. No part rename.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 7. Still spectra, from Random Motion to Analysis

- **Status:** TODO
- **Depends on:** 6
- **Books and files:** `tome12-random-motion` (`ch09-expanders.tex`, `ch10-semicircle.tex`, `ch11-cue.tex`, the expander half of `chapters/spectral.tex`) and `tome8-analysis` Spectral Theory. Dyson Brownian motion stays in Stochastic Calculus. The zeta narrative in `moments.tex` stays until step 18.
- **Acceptance:** The semicircle, the sine kernel, and the graph-theoretic Riemann hypothesis are theorems of Book 8. Book 12's third part is walks on graphs, resistance, and the matrix-tree theorem. Apply the proposed part rename: Book 12, Part III, **Networks**. Regenerate the series files. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** This is the only PR that renames Book 12's part. Later books cite the sine kernel as Book 8.

### 8. Jordan to Spaces, Riemann mapping to Shapes

- **Status:** TODO
- **Depends on:** 7
- **Books and files:** `tome8-analysis/chapters/ch09-complex.tex`, `tome7-spaces`, `tome9-shapes`. Phragmén–Lindelöf, Hadamard factorisation, and Dixon stay in Analysis.
- **Acceptance:** Jordan's theorem is in Metric and Topological Spaces. The Riemann mapping theorem is in Groups and Geometry. All three books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 9. Shapes: the connection pass

- **Status:** TODO
- **Depends on:** 8
- **Books and files:** `tome9-shapes`. Fold the Euclid appendix: Ceva and the Euler line into the transformations appendix; the rest of that appendix leaves the main text. Mark the general de Rham sentence as the punctured-plane case. Rename the second curvature chapter so it is not a second "Curvature". Point the cubic group law at Book 13.
- **Acceptance:** A reader of *The Geometry of Connection* does not meet a second chapter with the same title, or a Euclidean gallery that does not connect. `./build.sh tome9-shapes`.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 10. Formulas that are not primes

- **Status:** TODO
- **Depends on:** 9
- **Books and files:** `tome14-primes` (`ch06-partitions.tex`, the Waring half of `ch07-waring.tex`) and `tome5-calculation`, Series and Products. Three primes stays in Additive Problems and Bounded Gaps.
- **Acceptance:** The Hardy–Ramanujan asymptotic and Waring for large \(s\) are in Book 5. Book 14's part name stays Additive Problems and Bounded Gaps. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Do not rename Book 14's part.

### 11. The shuffle cutoff, from Abstraction to Randomness

- **Status:** TODO
- **Depends on:** 10
- **Books and files:** `tome10-abstraction/chapters/ch10-shuffling.tex` and `tome11-randomness`, Martingales and Ergodic Theory. Retitle `tome11-randomness/chapters/ch13-harder.tex` to Sums of random pieces. The Fourier analysis of \(S_n\) stays in Representations.
- **Acceptance:** The cutoff is a theorem of Book 11. Book 10's part is still named Representations. Both books build. The tower property cited here is the theorem from step 2.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 12. Say that the repeated theorems are returns

- **Status:** TODO
- **Depends on:** 11
- **Books and files:** `tome11-randomness` (Roth in the ergodic chapter; the mod-\(\varphi\) chapter) and `tome14-primes` (Roth). Each Roth introduction names the other proof. The mod-\(\varphi\) chapter labels Selberg–Delange as quoted from Book 15 until step 14, then the next edit of that sentence may name the chapter.
- **Acceptance:** A reader of either Roth proof is told the other exists. The uniform-integer mod-\(\varphi\) statement is not presented as proved in Book 11. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 13. Abstraction: primary decomposition

- **Status:** TODO
- **Depends on:** 12
- **Books and files:** `tome10-abstraction`, in Commutative Algebra, before Dedekind domains.
- **Acceptance:** Primary decomposition and associated primes are a numbered section. Dedekind domains cite them. Book 13 is not rewritten to depend on them. `./build.sh tome10-abstraction`.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 14. Book 15: the chapters the series already quotes

- **Status:** TODO
- **Depends on:** 13
- **Books and files:** `tome15-order-and-chance` only. Finish The Question and the start of Arithmetic Statistics from `ra-largemoduli.tex`, `ra-gaps.tex`, `ra-additive.tex`, `ra-selbergdelange.tex`, and `ra-erdoskac.tex`, and Spectra's value-distribution chapter from `ra-bohrjessen.tex` and `ra-selberg.tex`. Shrink the second Erdős–Kac write-up to a comparison with Book 6. Gallagher's hypothesis stays in the heading of Maier's theorem.
- **Acceptance:** Buchstab, Maier, the Erdős–Rankin bound, Kubilius, Selberg–Delange, Bohr–Jessen, and Selberg's central limit theorem are proved in Book 15 and cited as such. Erdős–Kac is not founded a second time. `./build.sh tome15-order-and-chance`.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** The five openings are step 15. Do not write them here.

### 15. Book 15: the five openings

- **Status:** TODO
- **Depends on:** 14, and step 7 for the sine kernel's address
- **Books and files:** `tome15-order-and-chance`: `ch05-short.tex`, `ch06-sieves.tex`, `ch08-ranks.tex`, `ch09-gue.tex`, `ch12-pseudorandom.tex`.
- **Acceptance:** Each file is a chapter, not a fifteen-line opening. Each cites a theorem from Books 6–14 and proves only the sentence those books did not prove. The form factor cites Book 8. Green–Tao stays quoted. `./build.sh tome15-order-and-chance`.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 16. Book 15: class groups, moments, and bias

- **Status:** TODO
- **Depends on:** 15
- **Books and files:** `tome15-order-and-chance`: Cohen–Lenstra (`ra-cohenlenstra.tex` and the cokernel argument in `ch05-sandpiles.tex`), moments (`ra-moments.tex`), bias (`ra-bias.tex`).
- **Acceptance:** The cokernel theorem lives in the class-group chapter, not in two chapters. The moments chapter either proves the approximate functional equation or marks every use of it. Chebyshev's bias names its hypotheses. The heuristic headings say heuristic. The book builds.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 17. Park the workshop proofs that belong elsewhere

- **Status:** TODO
- **Depends on:** 16
- **Books and files:** `tome15-order-and-chance` and the destinations in `book-15.md`: BBP and Borwein integrals to `tome5-calculation`; Gilmer to `tome4-chance`; Mason–Stothers, polynomial Fermat, and the three-cubes identities to `tome13-arithmetic`; the polygonal Jordan theorem to `tome7-spaces`; Paley and Sylvester to `tome3-symmetry`; the branching-random-walk half-moment to `tome12-random-motion`.
- **Acceptance:** Each moved proof builds in its new book. Book 15 no longer contains a second copy. The reading method and the two projects are not deleted in this PR.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** One move, several destinations. No new mathematics.

### 18. The Research Workshop, reduced to the meeting

- **Status:** TODO
- **Depends on:** 17
- **Books and files:** `tome15-order-and-chance` only. Cut the tours listed in `book-15.md` (Collatz, the empty zeta pointer, Goldbach, the Riemann-hypothesis appendix, BSD, the randomness tour, the algebra tour, Curry–Howard, and the conjecture surveys already owned by Books 6 and 14). Keep the part name The Research Workshop. What remains is the reading method, practised on Maier or Selberg, and the two projects.
- **Acceptance:** Appendix E is gone. The part is still named The Research Workshop. The book builds, and a reader can see the meeting of structure and randomness in every chapter that remains.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Also move `moments.tex`'s zeta story into Book 15's Spectra chapter if step 7 left the file in Random Motion. Delete it from `tome12-random-motion`.

### 19. The leftover sentences

- **Status:** TODO
- **Depends on:** 18
- **Books and files:** `tome8-analysis` (the blurb matches the compact spectral theorem; the zeta-problem chapter is retitled), `tome14-primes` (the discriminant of \(\mathbb Q(\sqrt 2)\) points at Book 13's figure, not at the ramification theorem).
- **Acceptance:** The public blurb does not claim the unbounded spectral theorem. The primes citation resolves. Both books build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:**

### 20. The story pass

- **Status:** TODO
- **Depends on:** 19
- **Books and files:** the preface of each `tome1-first-principles` through `tome15-order-and-chance`. One paragraph names the series question and the floor's element. Part names are not edited again.
- **Acceptance:** A reader of any preface can say which floor this is and what the next floor takes up. No title or subtitle changes. The books whose prefaces changed still build.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Last step. P1 problems are not placed again.
