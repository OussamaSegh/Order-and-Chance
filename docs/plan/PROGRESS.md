# Volume 1 voice rewrite

This file is the live execution tracker for the Volume 1 rewrite. The book is `volume1-first-principles`. One chapter, or the named pair, is one pull request, written in the shared voice.

Cold-start snapshot: 2026-10-30, about 17:16 Europe/Paris, from Nori.

Standing series goal. When Volume 1 is done, the series continues with Volumes 2 through 15 in order, one volume after another, under the same house voice and the same bar: one chapter per pull request, and an independent review before every merge. That handoff is for another bot. Nori owns Volume 1 only. Volume 2 waits until every Volume 1 step in this file is DONE.

Nori owns the Volume 1 end-state: free to launch, review, and merge Volume 1. One chapter is one pull request. An independent review comes before every merge.

The remake runs from the start, in this order: cover, preface and language, sums, counting, sequences, orders, complex numbers, polynomials, linear algebra, calculus, inequalities, probability, field guide.

Each rewrite step is a profound pass, with liberty to reorder for clarity and to add figures, photos, history points, and math jokes that teach, not a thin copyedit. The mathematics stays correct.

The voice is [docs/WRITING-STYLE.md](../WRITING-STYLE.md), including the [Sound human](../WRITING-STYLE.md#sound-human) pass: a friend who loves mathematics, never AI-sounding. Run that pass before each chapter pull request, and again on each independent review. The house-voice rule merged in [#52](https://github.com/OussamaSegh/Order-and-Chance/pull/52) at `bc67b65fad39f1ecdfbe0228f7362070bb75211c` on 2026-10-30. The role is [docs/agents/mathematician-writer.md](../agents/mathematician-writer.md). The editor (Nori) reviews each Volume 1 pull request independently. After it merges, the next Volume 1 chapter starts.

Edition 1 catalog and content moves, old steps 0–21, are finished. They are kept in [Archive: Edition 1 plan (complete)](#archive-edition-1-plan-complete) at the bottom of this file. That archive is not the resume target.

Chapter order follows the `\input` order in `volume1-first-principles/main.tex`. Image credits are not a rewrite step. The cover note is step 0.

## Open pull requests

One pull request is open. It is the only Volume 1 rewrite work until it has squash-merged. Orders waits for it.

- **#55, sequences, step 4.** https://github.com/OussamaSegh/Order-and-Chance/pull/55. Branch `cursor/sequences-series-limits-802d`. Author agent `bc-3a95942d`. Independent review returned FIX (COMMENT posted). The FIX is applied. Head `638438ad450a05aa431ef7c31dc5e664a6d7387e`. Re-review is in flight. Must-fix in `ch05-sequences-series.tex`, now applied: the mathematics at lines 186–190, the duplicate at lines 852–854, the syllabus menu at line 863, and absolute convergence at line 34. Polish, now applied: the Zeno caption, the de Moivre sentence, and the hint that should point at `prop:early-ftc`. Fix agent `bc-5e590679` pushed onto this same branch and this same pull request. Do not open a new pull request. The branch is based on the counting rewrite `83dff2be79404b68ee6c45d620ee574432302c4e` and still needs #52, #53, #50, #51, and #54 (`0bbf558903e96149998a0d71c2e49b1a82a66544`) from `main`.

Queue after #55 has squash-merged: orders, complex numbers, polynomials, linear algebra, calculus (integrals and Taylor), inequalities, probability, field guide.

## Resume protocol

1. Read this file, including the open-pull-request list. Find the first Volume 1 rewrite step whose status is not DONE.
2. If that step is IN REVIEW or IN PROGRESS, continue its pull request. Do not open a second pull request for the same step. Step 4 is the open pull request. Continue it.
3. If that step is TODO, search the open pull requests for that chapter before creating a branch. If a branch or pull request already exists, use it.
4. One step is one pull request and one chapter file. Step 0 is the jacket: `blurb.tex`, `about-the-cover.tex`, `kdp.md`, and the Volume 1 entry in `common/cover-notes.json`. Step 1 is the preface and the language chapter together.
5. In the same pull request, set the row to IN REVIEW and fill the PR link. Leave the merge sha and the date blank until merge.
6. The editor marks the row DONE, with the merge sha and the date, after the pull request merges. If the editor has not done that when the next step starts, the next step's pull request fills the previous row from the merge commit.
7. Do not start step \(n+1\) while step \(n\) is TODO, IN PROGRESS, or IN REVIEW. Orders (step 5) starts only after step 4 has merged. Step 0 is DONE.
8. Acceptance always includes a match to `docs/WRITING-STYLE.md`, including the Sound human pass, fact-check notes in the pull request, and `git diff --check`. A chapter step also needs a Volume 1 typeset and layout check. Run `./build.sh volume1-first-principles`, or the equivalent XeLaTeX pass plus `tools/check_book_layout.py`, as the earlier chapter pull requests did. Step 0 checks the cover note (80 to 150 words), `python3 tools/series_cover.py --check`, and the back-cover measure.
9. Scope is the assigned file or files under `volume1-first-principles/`, plus the cover-note source when the step is the jacket, plus figures that a chapter needs. Do not edit other volumes in that pull request.

## Steps

### 0. Cover copy

- **Status:** DONE
- **Depends on:** none
- **Books and files:** `volume1-first-principles/blurb.tex`, `volume1-first-principles/about-the-cover.tex`, `volume1-first-principles/kdp.md`, and the Volume 1 text in `common/cover-notes.json`. The TeX colophon is generated from that JSON. `docs/COVER-NOTES.md` and `tools/assets/series/manifest.json` follow the cover check. Jacket copy only. No chapter rewrite.
- **Acceptance:** The jacket texts match `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. The cover note is 80 to 150 words. `python3 tools/series_cover.py --check` passes. The back-cover blurb fits the shared measure.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/54
- **Merge sha:** 0bbf558903e96149998a0d71c2e49b1a82a66544
- **Date:** 2026-10-30
- **Notes:** Squash-merged. Back cover and About the Cover. Agent `bc-74380fd7`. Do not open another jacket pull request.

### 1. Preface and language

- **Status:** DONE
- **Depends on:** 0
- **Books and files:** `volume1-first-principles/chapters/preface.tex` and `volume1-first-principles/chapters/ch00-language.tex`. Both files in one pull request.
- **Acceptance:** Both files match `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/51
- **Merge sha:** 1d97799a0e12a6b91f562dc7e88ad0ec4c788a3a
- **Date:** 2026-10-30
- **Notes:** Deepen pass, squash-merged. The first pass merged in https://github.com/OussamaSegh/Order-and-Chance/pull/43 at `0212bbee89ccb4e7fb291a2c20b18be724eb3949` on 2026-10-30. Do not open another preface pull request.

### 2. Sums, binomials, induction

- **Status:** DONE
- **Depends on:** 1
- **Books and files:** `volume1-first-principles/chapters/ch01-sums.tex`. Sums, binomials, induction.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/50
- **Merge sha:** 586f056b3fd86af06e8839c137c34d52f78d821e
- **Date:** 2026-10-30
- **Notes:** Deepen pass, squash-merged. The first pass merged in https://github.com/OussamaSegh/Order-and-Chance/pull/46 at `69d90ccedce7f02ac26b8737fd09a88bc8459215` on 2026-10-30. Do not open another sums pull request.

### 3. Counting and discrete reasoning

- **Status:** DONE
- **Depends on:** 2
- **Books and files:** `volume1-first-principles/chapters/ch02-counting.tex`. Counting and discrete reasoning.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/53
- **Merge sha:** fe390f2a814e84bac91a7bc3d3c1ee2495115e96
- **Date:** 2026-10-30
- **Notes:** Human-voice pass, squash-merged. The counting rewrite merged in https://github.com/OussamaSegh/Order-and-Chance/pull/47 at `83dff2be79404b68ee6c45d620ee574432302c4e` on 2026-10-30. Do not open another counting pull request.

### 4. Sequences, series, limits

- **Status:** IN REVIEW
- **Depends on:** 3
- **Books and files:** `volume1-first-principles/chapters/ch05-sequences-series.tex`. Sequences, series, limits. New figures: `figures/ch05-zeno.tex`, `figures/ch05-grandi.tex`, `figures/ch05-floor.tex`, `figures/ch05-integral.tex`, `figures/ch05-uniform.tex`.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/55
- **Merge sha:**
- **Date:**
- **Notes:** Independent review returned FIX (COMMENT posted). The FIX is applied. Head `638438ad450a05aa431ef7c31dc5e664a6d7387e`. Re-review is in flight. Author agent `bc-3a95942d`. Branch `cursor/sequences-series-limits-802d`. Must-fix in `ch05-sequences-series.tex`, now applied: the mathematics at lines 186–190, the duplicate at lines 852–854, the syllabus menu at line 863, and absolute convergence at line 34. Polish, now applied: the Zeno caption, the de Moivre sentence, and the hint that should point at `prop:early-ftc`. Fix agent `bc-5e590679` pushed onto this same branch and pull request #55. Do not open a new pull request. Profound pass: concrete partial sums first, the floor and the positive square root of 2 from completeness, new figures for Zeno, Grandi, the floor, the integral test, and uniform continuity. The branch still needs #52, #53, #50, #51, and #54 (`0bbf558903e96149998a0d71c2e49b1a82a66544`) from `main`.

### 5. Orders

- **Status:** TODO
- **Depends on:** 4
- **Books and files:** `volume1-first-principles/chapters/orders.tex`. Orders.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Orders. Next chapter after #55 has squash-merged.

### 6. Complex numbers and roots

- **Status:** TODO
- **Depends on:** 5
- **Books and files:** `volume1-first-principles/chapters/ch02-complex-roots.tex`. Complex numbers and roots.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Complex numbers and roots.

### 7. Polynomials

- **Status:** TODO
- **Depends on:** 6
- **Books and files:** `volume1-first-principles/chapters/ch03-polynomials.tex`. Polynomials.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Polynomials.

### 8. Linear algebra

- **Status:** TODO
- **Depends on:** 7
- **Books and files:** `volume1-first-principles/chapters/ch07-linear-algebra.tex`. Linear algebra.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Linear algebra.

### 9. Integrals and Taylor

- **Status:** TODO
- **Depends on:** 8
- **Books and files:** `volume1-first-principles/chapters/ch06-integrals-taylor.tex`. Integrals and Taylor.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Integrals and Taylor. This is the calculus step in the queue.

### 10. Inequalities

- **Status:** TODO
- **Depends on:** 9
- **Books and files:** `volume1-first-principles/chapters/ch04-inequalities.tex`. Inequalities.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Inequalities.

### 11. Probability

- **Status:** TODO
- **Depends on:** 10
- **Books and files:** `volume1-first-principles/chapters/ch09-probability.tex`. Probability.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Probability.

### 12. Field guide

- **Status:** TODO
- **Depends on:** 11
- **Books and files:** `volume1-first-principles/chapters/field-guide.tex`. Field guide, and the handoff to Volume 2.
- **Acceptance:** The chapter matches `docs/WRITING-STYLE.md`. Fact-check notes are in the pull request. `git diff --check`. Volume 1 typesets and the layout check passes.
- **PR:**
- **Merge sha:**
- **Date:**
- **Notes:** Field guide and the handoff to Volume 2.

## Archive: Edition 1 plan (complete)

Complete. Not the resume target. Edition 1 steps 0–21 below are finished. Their statuses are the historical record. Resume from the Volume 1 voice rewrite at the top of this file.

### Implementation tracker

This is the execution list for Edition 1. The reasoning lives in [SERIES-CONTENT-PLAN.md](SERIES-CONTENT-PLAN.md) and the chapter plans beside it. Titles and subtitles are frozen. Part names stay the catalog's, except the two renames in steps 5 and 8.

Paths below, and the paths in the other files under `docs/plan/`, are the directory names `volume1-first-principles` through `volume15-order-and-chance`. The retired names (`tome0-mathematical-maturity`, `tome9-higher-structures`, `tome14-order-and-chance`, and the other pre-renumbering stems) are gone. Step 2 does not revive them.

| Book | Directory |
| --- | --- |
| 1 First Principles | `volume1-first-principles` |
| 2 The Integers | `volume2-integers` |
| 3 Symmetry | `volume3-symmetry` |
| 4 Chance | `volume4-chance` |
| 5 Calculation | `volume5-calculation` |
| 6 Crossroads | `volume6-crossroads` |
| 7 Spaces | `volume7-spaces` |
| 8 Analysis | `volume8-analysis` |
| 9 Shapes | `volume9-shapes` |
| 10 Abstraction | `volume10-abstraction` |
| 11 Randomness | `volume11-randomness` |
| 12 Random Motion | `volume12-random-motion` |
| 13 Arithmetic | `volume13-arithmetic` |
| 14 The Primes | `volume14-primes` |
| 15 Order and Chance | `volume15-order-and-chance` |

### Retired resume protocol (Edition 1)

This protocol applied while Edition 1 was open. Do not resume from it.

1. Read this file. Find the first step whose status is not DONE.
2. If that step is IN REVIEW or IN PROGRESS, open its PR link. Continue that branch. Do not open a second PR for the same step.
3. If that step is TODO, search the open pulls for its id (for example `step 5`) before creating a branch. If a branch or PR already exists, use it.
4. Do the step. In the same PR, set this row to IN REVIEW, fill the PR link, and leave merge sha and date blank.
5. The editor marks the row DONE, with the merge sha and the date, after the PR merges. If the editor has not done that when the next step starts, the next step's PR marks the previous row DONE from the merge commit.
6. Do not start step \(n+1\) while step \(n\) is TODO, IN PROGRESS, or IN REVIEW.
7. Do not edit a book a later step has not reached, and do not reopen a move this file marks DONE.
8. Leave the repaired proofs alone. They are listed under "Already repaired" in the series plan. The exception is the second reading of three squares, which is part of step 5.

A step is one PR. A content step is one book, or one move between books. Step 2 is the rename: it touches every book and does not change the mathematics. Acceptance always includes `git diff --check` and `./build.sh` on every stem the step touches.

### Edition 1 steps

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

- **Status:** DONE
- **Depends on:** 0
- **Books and files:** `docs/plan/` only. No manuscript.
- **Acceptance:** `SERIES-CONTENT-PLAN.md`, `book-01.md` through `book-15.md`, and this file are on `main`. Part names in the plan are the catalog's. The two proposed renames are marked as proposals.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/27
- **Merge sha:** 2c5c7811f0d884dec5430b8facd7fc8a6e8b862c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the plan files.

### 2. Harmonize Tome to Volume

- **Status:** DONE
- **Depends on:** 1
- **Books and files:** the whole repository. Names only. No mathematical text, no title, no subtitle, and no part name.
  - Reader-visible text, covers, and spines: Tome becomes Volume, and tome becomes volume. Do not redraw artwork, frames, or any lettering that does not spell that word.
  - LaTeX macros: `\seriestome` becomes `\seriesvolume`, `\TOMENUM` becomes `\VOLUMENUM`, and `\TOMETITLE` becomes `\VOLUMETITLE`, including `common/frontmatter.tex`, `common/series.tex`, and the lines `tools/series_metadata.py` writes.
  - Directories: `tome1-first-principles` becomes `volume1-first-principles`, and the same replacement through `tome15-order-and-chance`. `python/tome1` through `python/tome15` become `python/volume1` through `python/volume15`.
  - `build.sh`, `tools/build_plan.py`, `.github/workflows/build.yml`, `.github/workflows/notebooks.yml`, and the `stem` fields in `common/series-catalog.json`. Shell variables, the workflow matrix key, and the build-plan field that are still named tome change with them.
  - PDF, EPUB, and release asset names, and the reader routes under `read/`, wherever they still contain `tome`. Public basenames that already read `Volume N - …` (`tools/PUBLISHING.md`) stay in that form.
  - The site and the download page, including `tools/site.py` and the `.tome` card class in `tools/site-template.html`.
  - The README and the docs.
  - Old download and reader URLs that used a `tome` stem keep working. There is no redirect table today; add one where a published URL used the old stem.
- **Acceptance:** `git diff --check`. A search for `tome` or `Tome` is empty except where the old spelling has to remain: step 0's record of the names PR #26 created, the retired-name list at the top of this file, this step's statement of those old names, and a redirect that names an old URL. The temporary sentences in `docs/plan/` that tell a reader to swap the prefix are removed once the directories exist. The catalog stems match the directories. `./build.sh` succeeds for every `volumeN-` stem. An old reader or download URL that used a `tome` stem still resolves. Cover artwork is the same picture.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/28
- **Merge sha:** 5266fdff2a92cc0ee18a3b708bf595f3096807bc
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do this before any content step. It supersedes the earlier rule that directory names and TeX macro names stayed `tome` while the English word was already Volume. Do not revive `tome0-mathematical-maturity`, `tome9-higher-structures`, `tome14-order-and-chance`, or the other pre-renumbering stems. The `volumeN-` paths in `docs/plan/` become directories when this step merges.

### 3. Spaces: conditional expectation, and the almost-every chapter

- **Status:** DONE
- **Depends on:** 2
- **Books and files:** `volume7-spaces`. Promote conditional expectation, including the tower property, from the exercise in `chapters/ch10-radon.tex` to a numbered theorem. Retitle `chapters/ch12-harder.tex` to Almost every number, still inside Measures on Spaces.
- **Acceptance:** Books 11 and 12 can cite the tower as a theorem of Book 7. The problem chapter's title is no longer "Harder problems". `./build.sh volume7-spaces`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/29
- **Merge sha:** 832e24bed70693dba9b3aa48fbdc9406062a1eb1
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do this before any edit to Randomness or Random Motion.

### 4. Orders, from Chance to First Principles

- **Status:** DONE
- **Depends on:** 3
- **Books and files:** `volume4-chance/chapters/orders.tex` moves into `volume1-first-principles`, inside Algebra, Limits and Functions. Appendix B of Chance stays.
- **Acceptance:** Dilworth, Sperner, and partial orders are in Book 1. Book 4's Random Structures no longer contains that appendix. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/30
- **Merge sha:** 3335f6f01eea9a77ea9774c7f93aac3e91d16825
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 5. Hidden worlds, from The Integers to Arithmetic

- **Status:** DONE
- **Depends on:** 4
- **Books and files:** `volume2-integers` (`ch11-algebraic.tex`, `ch12-ideals.tex`, `ch12-padic.tex`) and `volume13-arithmetic`. Hensel's lemma for a congruence stays in Book 2. One section keeps \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). While Arithmetic is open, read the repaired three-squares test in `ch07-hasse.tex` once.
- **Acceptance:** Those three chapters are in Book 13's Number Fields and Local and Global parts. Book 2 still proves Pell, the Gaussian integers, and reciprocity. Apply the proposed part rename in `common/series-catalog.json`: Book 2, Part IV, **Equations and Characters**. Regenerate the series files from that catalog. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/31
- **Merge sha:** 57ec8496f3afa57b505c1604f12ff1f7d18af141
- **Date:** 2026-10-29
- **Notes:** Squash-merged. This is the only PR that renames Book 2's part.

### 6. The adèles, from Analysis to Arithmetic

- **Status:** DONE
- **Depends on:** 5
- **Books and files:** `volume8-analysis/chapters/ch08-haar.tex` and `volume13-arithmetic` (local fields and Tate). Haar measure and Pontryagin duality stay in Fourier and Tauberian Methods.
- **Acceptance:** The construction of \(\mathbb Q_p\) and the adèles, beyond Haar measure, is in Book 13. Book 8 still states the duality it uses. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/32
- **Merge sha:** 921c260b7829a1bbd8947fe8e6d86423eb53c2a7
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not move Jordan or the Riemann mapping theorem in this PR.

### 7. Symmetry's extra linear algebra

- **Status:** DONE
- **Depends on:** 6
- **Books and files:** `volume3-symmetry` appendices, `volume8-analysis`, `volume10-abstraction`. Spectral theorem, SVD, graph spectra, matrix inequalities, linear dynamics, and the linear algebra that repeats Book 1 go to Analysis. Tensors go to Abstraction, Categories. Circulants, Perron roots of a symmetry, and the linear algebra method stay in Book 3.
- **Acceptance:** Book 3's contents are Groups, Rings and Polynomials, and Fields and Galois Theory, plus the appendices that still count by symmetry. Analysis and Abstraction build with the new files. No part rename.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/33
- **Merge sha:** b6e61fa17d66389b466c3fd6019cde5e5ef46e64
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 8. Still spectra, from Random Motion to Analysis

- **Status:** DONE
- **Depends on:** 7
- **Books and files:** `volume12-random-motion` (`ch09-expanders.tex`, `ch10-semicircle.tex`, `ch11-cue.tex`, the expander half of `chapters/spectral.tex`) and `volume8-analysis` Spectral Theory. Dyson Brownian motion stays in Stochastic Calculus. The zeta narrative in `moments.tex` stays until step 19.
- **Acceptance:** The semicircle, the sine kernel, and the graph-theoretic Riemann hypothesis are theorems of Book 8. Book 12's third part is walks on graphs, resistance, and the matrix-tree theorem. Apply the proposed part rename: Book 12, Part III, **Networks**. Regenerate the series files. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/34
- **Merge sha:** a4934a3358d481119923201228beeca6ccc6200f
- **Date:** 2026-10-29
- **Notes:** Squash-merged. This is the only PR that renames Book 12's part. Later books cite the sine kernel as Book 8. The branching random walk stays in Book 12, in Stochastic Calculus.

### 9. Jordan to Spaces, Riemann mapping to Shapes

- **Status:** DONE
- **Depends on:** 8
- **Books and files:** `volume8-analysis/chapters/ch09-complex.tex`, `volume7-spaces`, `volume9-shapes`. Phragmén–Lindelöf, Hadamard factorisation, and Dixon stay in Analysis.
- **Acceptance:** Jordan's theorem is in Metric and Topological Spaces. The Riemann mapping theorem is in Groups and Geometry. All three books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/35
- **Merge sha:** 4be04914e2d49400eb7482b46723653aca424b5c
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 10. Shapes: the connection pass

- **Status:** DONE
- **Depends on:** 9
- **Books and files:** `volume9-shapes`. Fold the Euclid appendix: Ceva and the Euler line into the transformations appendix; the rest of that appendix leaves the main text. Mark the general de Rham sentence as the punctured-plane case. Rename the second curvature chapter so it is not a second "Curvature". Point the cubic group law at Book 13.
- **Acceptance:** A reader of *The Geometry of Connection* does not meet a second chapter with the same title, or a Euclidean gallery that does not connect. `./build.sh volume9-shapes`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/36
- **Merge sha:** 5586cb822895f37682f988c513fd4e80e3c356e5
- **Date:** 2026-10-29
- **Notes:** Squash-merged. The unused Euclid chapter file is removed in Step 11. Do not re-implement the pass.

### 11. Formulas that are not primes

- **Status:** DONE
- **Depends on:** 10
- **Books and files:** `volume14-primes` (`ch06-partitions.tex`, the Waring half of `ch07-waring.tex`) and `volume5-calculation`, Series and Products. Three primes stays in Additive Problems and Bounded Gaps.
- **Acceptance:** The Hardy–Ramanujan asymptotic and Waring for large \(s\) are in Book 5. Book 14's part name stays Additive Problems and Bounded Gaps. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/38
- **Merge sha:** afd199cf1a46b91de37bc6a7cf62119442ce4acd
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not rename Book 14's part. Do not re-implement the move.

### 12. The shuffle cutoff, from Abstraction to Randomness

- **Status:** DONE
- **Depends on:** 11
- **Books and files:** `volume10-abstraction/chapters/ch10-shuffling.tex` and `volume11-randomness`, Martingales and Ergodic Theory. Retitle `volume11-randomness/chapters/ch13-harder.tex` to Sums of random pieces. The Fourier analysis of \(S_n\) stays in Representations.
- **Acceptance:** The cutoff is a theorem of Book 11. Book 10's part is still named Representations. Both books build. The tower property cited here is the theorem from step 3.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/39
- **Merge sha:** 7228f2d4a37363d3cdeb1576cc8be6fd73674e7e
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the move.

### 13. Say that the repeated theorems are returns

- **Status:** DONE
- **Depends on:** 12
- **Books and files:** `volume11-randomness` (Roth in the ergodic chapter; the mod-\(\varphi\) chapter) and `volume14-primes` (Roth). Each Roth introduction names the other proof. The mod-\(\varphi\) chapter labels Selberg–Delange as quoted from Book 15 until step 15, then the next edit of that sentence may name the chapter.
- **Acceptance:** A reader of either Roth proof is told the other exists. The uniform-integer mod-\(\varphi\) statement is not presented as proved in Book 11. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/40
- **Merge sha:** f28ae2b927d7fc922327922e3df83e6b1b1b8608
- **Date:** 2026-10-29
- **Notes:** Squash-merged. Do not re-implement the cross-references.

### 14. Abstraction: primary decomposition

- **Status:** DONE
- **Depends on:** 13
- **Books and files:** `volume10-abstraction`, in Commutative Algebra, before Dedekind domains.
- **Acceptance:** Primary decomposition and associated primes are a numbered section. Dedekind domains cite them. Book 13 is not rewritten to depend on them. `./build.sh volume10-abstraction`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/41
- **Merge sha:** 07992d9b6e133f0b5357f5baa76a613623b2acb3
- **Date:** 2026-10-29
- **Notes:** Squash-merged. The section is in `chapters/ch04-localisation.tex`, and Dedekind domains cite Theorem `thm:assprimes`. Book 13 was not rewritten.

### 15. Book 15: the chapters the series already quotes

- **Status:** DONE
- **Depends on:** 14
- **Books and files:** `volume15-order-and-chance` only. Finish The Question and the start of Arithmetic Statistics from `ra-largemoduli.tex`, `ra-gaps.tex`, `ra-additive.tex`, `ra-selbergdelange.tex`, and `ra-erdoskac.tex`, and Spectra's value-distribution chapter from `ra-bohrjessen.tex` and `ra-selberg.tex`. Shrink the second Erdős–Kac write-up to a comparison with Book 6. Gallagher's hypothesis stays in the heading of Maier's theorem.
- **Acceptance:** Buchstab, Maier, the Erdős–Rankin bound, Kubilius, Selberg–Delange, Bohr–Jessen, and Selberg's central limit theorem are proved in Book 15 and cited as such. Erdős–Kac is not founded a second time. `./build.sh volume15-order-and-chance`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done in this pull request. The quoted chapters are the live includes; the second Erdős–Kac write-up is a comparison with Volume 6. Gallagher's hypothesis stays in the heading. Merge sha left blank until this pull request merges. Interior XeLaTeX of Volume 15 was checked (three passes, references resolved, layout check passed). The full `./build.sh` press export was not finished.

### 16. Book 15: the five openings

- **Status:** DONE
- **Depends on:** 15, and step 8 for the sine kernel's address
- **Books and files:** `volume15-order-and-chance`: `ch05-short.tex`, `ch06-sieves.tex`, `ch08-ranks.tex`, `ch09-gue.tex`, `ch12-pseudorandom.tex`.
- **Acceptance:** Each file is a chapter, not a fifteen-line opening. Each cites a theorem from Books 6–14 and proves only the sentence those books did not prove. The form factor cites Book 8. Green–Tao stays quoted. `./build.sh volume15-order-and-chance`.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The five files are chapters. The form factor is proved here and cites Volume 8. Green–Tao is quoted. The pair-second-moment chapter proves the logarithmic term; the coefficient \(\gamma+\log 2\pi-1\) is identified through \(\zeta'(0)=-\frac12\log(2\pi)\), not expanded into a separate residue calculation.

### 17. Book 15: class groups, moments, and bias

- **Status:** DONE
- **Depends on:** 16
- **Books and files:** `volume15-order-and-chance`: Cohen–Lenstra (`ra-cohenlenstra.tex` and the cokernel argument in `ch05-sandpiles.tex`), moments (`ra-moments.tex`), bias (`ra-bias.tex`).
- **Acceptance:** The cokernel theorem lives in the class-group chapter, not in two chapters. The moments chapter either proves the approximate functional equation or marks every use of it. Chebyshev's bias names its hypotheses. The heuristic headings say heuristic. The book builds.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. Symmetric cokernels are proved once in the class-group chapter (`ra-symmoments.tex`). The sandpile tour is not in `main.tex`. The old file `ch05-sandpiles.tex` still contains that proof and is not included. Approximate-functional-equation uses are marked. The bias chapter names GRH and linear independence. The zeta-spacing picture in Spectra is a non-floating center, not a `figure`.

### 18. Park the workshop proofs that belong elsewhere

- **Status:** DONE
- **Depends on:** 17
- **Books and files:** `volume15-order-and-chance` and the destinations in `book-15.md`: BBP and Borwein integrals to `volume5-calculation`; Gilmer to `volume4-chance`; Mason–Stothers, polynomial Fermat, and the three-cubes identities to `volume13-arithmetic`; the polygonal Jordan theorem to `volume7-spaces`; Paley and Sylvester to `volume3-symmetry`; the branching-random-walk half-moment to `volume12-random-motion`.
- **Acceptance:** Each moved proof builds in its new book. Book 15 no longer contains a second copy. The reading method and the two projects are not deleted in this PR.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The proofs now live in Calculation, Chance, Arithmetic, Spaces, Symmetry, and Random Motion. The riffle cutoff is in Randomness. Those destinations were typeset with XeLaTeX. Book 15's `main.tex` no longer includes a second copy. The old workshop sources remain on disk and are not input.

### 19. The Research Workshop, reduced to the meeting

- **Status:** DONE
- **Depends on:** 18
- **Books and files:** `volume15-order-and-chance` only. Cut the tours listed in `book-15.md` (Collatz, the empty zeta pointer, Goldbach, the Riemann-hypothesis appendix, BSD, the randomness tour, the algebra tour, Curry–Howard, and the conjecture surveys already owned by Books 6 and 14). Keep the part name The Research Workshop. What remains is the reading method, practised on Maier or Selberg, and the two projects.
- **Acceptance:** Appendix E is gone. The part is still named The Research Workshop. The book builds, and a reader can see the meeting of structure and randomness in every chapter that remains.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The part is still The Research Workshop. What `main.tex` includes is the reading method and two projects (`ch14-meeting.tex`). The zeta narrative is in Spectra. `volume12-random-motion/chapters/moments.tex` is no longer input. The cut workshop files and conjecture appendices are still in the tree.

### 20. The leftover sentences

- **Status:** DONE
- **Depends on:** 19
- **Books and files:** `volume8-analysis` (the blurb matches the compact spectral theorem; the zeta-problem chapter is retitled), `volume14-primes` (the discriminant of \(\mathbb Q(\sqrt 2)\) points at Book 13's figure, not at the ramification theorem).
- **Acceptance:** The public blurb does not claim the unbounded spectral theorem. The primes citation resolves. Both books build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. The blurb states the compact spectral theorem. The former problem chapter is titled The values of zeta. The discriminant of $\mathbb Q(\sqrt 2)$ points at Volume 13's lattice. Volumes 8 and 14 were typeset with XeLaTeX.

### 21. The story pass

- **Status:** DONE
- **Depends on:** 20
- **Books and files:** the preface of each `volume1-first-principles` through `volume15-order-and-chance`. One paragraph names the series question and the floor's element. Part names are not edited again.
- **Acceptance:** A reader of any preface can say which floor this is and what the next floor takes up. No title or subtitle changes. The books whose prefaces changed still build.
- **PR:** https://github.com/OussamaSegh/Order-and-Chance/pull/44
- **Merge sha:** 6b6eda63a60723562e693a4794467ecbeef7722f
- **Date:** 2026-10-30
- **Notes:** Manuscript done. Each preface names the series question, this floor, and the next floor. No title or subtitle was changed. First-edition copy check passed on all fifteen volumes. Interior XeLaTeX was run for every volume whose body changed, not only the prefaces.
