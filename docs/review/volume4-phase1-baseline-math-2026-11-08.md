# Volume 4 — Phase 1 baseline and first mathematical audit (8 November 2026)

**Status:** FIRST PASS / NOT ACCEPTED. The first native build succeeded at an earlier source commit of this same PR; newer source/test changes need exact-head reruns. No independent second reviewer, complete hostile proof reread, all-page human inspection, device check or press proof is claimed.

**Implementation branch:** `audit/volume4-phase1-baseline-math-2026-11-08`  
**Starting revision:** `main` at `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`.  
**Planning PR:** [#115 — Volume 4 excellence roadmap](https://github.com/OussamaSegh/Order-and-Chance/pull/115); this audit PR is a separate execution branch, not part of its unmerged changes.

## 1. Exact manuscript route and reproducible static baseline

`volume4-chance/main.tex` includes four parts, fourteen numbered chapters, Appendix **B** (via `\appendix` then `\setcounter{chapter}{1}`), and the About the Cover colophon. The included Chapter 5 file `ch05-continuous.tex` **nests** `\input{chapters/ch05-geometric}` at source line 364, so Bertrand's three experiments and Buffon's needle **are in the compiled book**. Earlier suspicion that the file was orphaned is false.

The following table was generated from GitHub's exact-file contents at the starting revision, counting physical source lines, `\label{...}` occurrences and local `\ref/\eqref/\pageref/\autoref` occurrences. The first-level route contains preface, 14 chapters, Appendix B and About the Cover; Chapter 5 adds the nested geometric file, and `blurb.tex` is tracked separately as jacket copy. **Nineteen text sources were scanned** (18 routed body/colophon plus blurb).

| Included text path under `volume4-chance/` | Lines | Labels | Local refs | `\fig` calls | E/H/S pairs |
| --- | ---: | ---: | ---: | ---: | ---: |
| `chapters/preface.tex` | 47 | 1 | 0 | 1 | 0 |
| `chapters/ch01-counting.tex` | 396 | 18 | 8 | 3 | 8 |
| `chapters/ch02-discrete.tex` | 556 | 20 | 11 | 4 | 8 |
| `chapters/ch03-generating.tex` | 498 | 22 | 24 | 4 | 8 |
| `chapters/ch04-inequalities.tex` | 393 | 15 | 12 | 3 | 6 |
| `chapters/ch05-continuous.tex` | 535 | 23 | 18 | 4 | 9 |
| `chapters/ch05-geometric.tex` (nested) | 89 | 4 | 2 | 2 | 0 |
| `chapters/ch06-clt.tex` | 785 | 26 | 58 | 3 | 8 |
| `chapters/ch07-entropy.tex` | 415 | 16 | 10 | 2 | 6 |
| `chapters/ch07-walks.tex` | 491 | 19 | 24 | 2 | 8 |
| `chapters/ch08-markov.tex` | 468 | 23 | 16 | 3 | 9 |
| `chapters/ch09-poisson.tex` | 426 | 25 | 26 | 3 | 8 |
| `chapters/ch10-martingales.tex` | 434 | 21 | 43 | 2 | 5 |
| `chapters/ch11-brownian.tex` | 414 | 21 | 33 | 1 | 7 |
| `chapters/ch12-method.tex` | 275 | 13 | 10 | 1 | 6 |
| `chapters/ch14-graphs.tex` | 304 | 9 | 13 | 1 | 6 |
| `chapters/extremal.tex` (Appendix B) | 240 | 15 | 6 | 2 | 5 |
| `about-the-cover.tex` | 7 | 0 | 0 | 0 | 0 |
| `blurb.tex` (jacket) | 2 | 0 | 0 | 0 | 0 |
| **Total** | **6,775** | **291** | **314** | **41** | **107** |

Source lines are **not** typeset pages. Every total counts syntactic occurrences, not mathematical acceptance.

Additional static source checks on that SHA:

- **291 distinct labels, zero duplicates.**
- **314 local `\ref`/`\eqref`/`\pageref`/`\autoref` uses, zero unresolved targets** among the included text sources. This is a narrow regular-expression check, not proof that all possible cross-volume/hyperlink references resolve in the published PDF.
- **107 distinct exercises**, with **107 matching hints and 107 matching solutions**, same IDs in chapter order, zero duplicates or orphan pairs. Exercise-star syntax was accounted for.
- **41 referenced TikZ `\fig` names, all 41 source files exist** under `volume4-chance/figures/`; the directory contains other unreferenced files. Neither existence nor a successful TeX parse establishes mathematical figure correctness, placement or accessibility.
- No change was made to part order, theorem labels, old published volumes, covers, Appendix B, page geometry or publishing scripts.

This source route is the **starting** version. Future agents must recompute these metrics on their precise review SHA rather than copying them as if current.

### Source-to-print naming map

Printed chapter 1 `ch01-counting`; 2 `ch02-discrete`; 3 `ch03-generating`; 4 `ch04-inequalities`; 5 `ch05-continuous` + nested `ch05-geometric`; 6 `ch06-clt`; 7 `ch07-entropy`; 8 `ch07-walks`; 9 `ch08-markov`; 10 `ch09-poisson`; 11 `ch10-martingales`; 12 `ch11-brownian`; 13 `ch12-method`; 14 `ch14-graphs`; Appendix **B** `extremal`. **Filenames are historical and must not be mistaken for printed chapter numbers.**

## 2. High-confidence mathematical findings and implemented corrections

These are **writer-side corrections at specific commits**, not independent-referee signoffs.

### V4-P1-001 — Fourier uniqueness cutoff has a nondecaying tail

**Where:** Printed Chapter 6, `ch06-clt.tex`, Theorem `thm:inversion` part (a), original source line ~297.  
**Severity:** P0 proof gap in the written uniqueness argument.  
**Starting claim:** Cut down a bounded uniformly continuous test function on \([-A,A]\); the discarded expectation is controlled by `P(|X|>A-1)+P(|σZ|>1)`, both said to be small for large \(A\). The Gaussian probability is **independent of \(A\)** at fixed \(\sigma>0\). No choice of large \(A\) proves it small.

**Correction commit:** `b22c0e6e29652a402ea31e492a89436d74c862d5`. Choose a continuous compact-support cutoff \(\chi_A\) equal to \(1\) on \([-A,A]\). For either \(W=X\) or \(W=Y\):
\[
\left|\mathbb E[g(W+\sigma Z)]-
 \mathbb E[(g\chi_A)(W+\sigma Z)]\right|
\le 2\|g\|_\infty
\Bigl(P(|W|>A/2)+P(|\sigma Z|>A/2)\Bigr).
\]
The union-bound inclusion is
\(\{|W+\sigma Z|>A\}
\subseteq\{|W|>A/2\}\cup\{|\sigma Z|>A/2\}\).
Both tails vanish for \(A\to\infty\), at any **fixed** \(\sigma>0\), without assuming \(E|W|<\infty\); a Cauchy law is allowed. The proof also explicitly chooses fresh Gaussian streams independent of **both** variables when comparing two laws, rather than declaring independence only from \(X\).

**Checks performed:** verified the event inclusion mathematically and against a finite integer grid; checked source uses the growing Gaussian threshold and preserves Theorem 6.8's statement. **Still needed:** independent proof-level reread of the complete smoothing, inversion and density argument, including the heavy-tailed case; native TeX and rendered formula QA.

### V4-P1-002 — The first four riffle distances are not exactly 1

**Where:** Printed Chapter 9, `ch08-markov.tex`, after `prop:rifflecompose` and Figure `fig:riffle`.  
**Severity:** P1 false literal equality / misleading caption.

The manuscript gave \(d_k=1\) for \(k\le4\) after saying the formula was rounded. For a \(52\)-card \(a\)-shuffle, the identity permutation has mass \(\binom{a+51}{52}/a^{52}>0\) and also uniform mass \(1/52!>0\). The two laws overlap, so their total-variation distance is **strictly less than 1** for \(k\ge1\), even if rounded to \(1.000\).

**Correction commit:** `aca23c1e982505dcc8ee7e0e7528d50f6b9a41a5`. The text now calls the first four numbers *three-decimal rounded values* and supplies the identity-deck overlap reason. The caption describes plotted values as computed from the exact sum, not mathematically exact \(1\)'s.

**Independent arithmetic performed here (writer-side, exact integer formula):** Eulerian recurrence on \(n=52\) with \(\sum_r A(52,r)=52!\), then
\[
d_k=\frac{\sum_{r=1}^{52}A(52,r)
 \left|\binom{2^k+52-r}{52}\,52!-(2^k)^{52}\right|}
 {2(2^k)^{52}\,52!}.
\]
For \(k=4\), \(d_4=0.9999995334313746494\ldots<1\). For \(k=5,6,7\), respectively: \(0.9237329294\ldots\), \(0.6135495966\ldots\), \(0.3340609995\ldots\). All \(k=1,\dots,10\) reproduce the book's printed three-decimal values.

**Still needed:** a genuinely distinct mathematical and caption reviewer; the updated caption needs native figure inspection.

### V4-P1-003 — Memorylessness proof compresses the degenerate case

**Where:** Printed Chapter 10, `ch09-poisson.tex`, `prop:memoryless`.  
**Severity:** P1 skipped logical step (not a false theorem).

The earlier argument said \(G(1)=1\Rightarrow G(n)=1\Rightarrow T\) is infinite. The statement about all real times also needs monotonicity and multiplicativity. `b5023a600dee1aac25c84d9b850d9bc86f42ac03` inserts: \(G(0)=G(1)=1\) and monotonicity give \(G(t)=1\) for \(0\le t\le1\); the functional equation extends that to all \(t\ge0\), contradicting non-infinity of \(T\). The theorem and model are unchanged.

**Still needed:** independent referee read of the full proof and its assumptions; a native build of the updated exact final SHA.

### V4-P1-004 — Strict Lindeberg threshold in the proof text

**Where:** Printed Chapter 6, `ch06-clt.tex`, proof of `thm:lindeberg`.  
**Severity:** P1 logical/notation precision (the theorem itself remains unchanged).

The argument splits the Taylor remainder into a small-increment term on `|x|≤ε` and a large-increment term on `|x|>ε`, correctly matching the theorem's strict Lindeberg condition. Its prose instead said the contributions with `|X|≥ε` tend to zero “by hypothesis.” At a fixed threshold the strict and non-strict indicators can differ (e.g. a fair sign with magnitude exactly `ε`), so that citation was imprecise. Commit `5e7b8c5403c55ae40a51268f8d4ba3fe252f2292` changes the sentence to `|X|>ε` and explicitly assigns equality to the small-increment term. The strict/no-strict endpoint example is protected by a new test, but an independent full proof reread remains pending.

### Regression coverage

`tools/test_volume4_math_audit.py` (commit `ac36e0b7bad91212add3eccc7cc5e732317930e8`) adds three standard-library regression tests:

1. Guards the corrected Chapter 6 expression, fresh independent noise, and triangle-inequality event inclusion.
2. Recomputes **all ten** published riffle distances from Eulerian integers and the exact rational total-variation formula; verifies exact \(0<d_k<1\), rounding and corrected caption wording.
3. Guards the now-explicit monotonicity step in Chapter 10.

The **three original mathematics regression tests passed** in GitHub's full test step on `5bbca61229075359a358ac079c1faa1e074ff7ed` (532 tests, 32 skipped in that revision). Since then a fourth Lindeberg endpoint test was added; this new head still needs its own test run. Tests supplement, not replace, mathematical review.

`tools/test_volume4_route.py` (added at `f0bfd68964bc972b520115978f9bf6ce3cf02994`) is a second suite: it resolves actual nested chapter `\\input` files, preserves the approved four parts and 14 chapters plus Appendix B, checks every label and local reference, enforces one hint and solution per exercise, and checks every included figure source. The suite adds four test methods. Its source-level checks cannot replace TeX compilation, independent proof review, or a human figure inspection.

## 3. Existing-review reconciliation (source of truth, not a reset)

| Existing record | What it establishes | What it does **not** establish / action |
| --- | --- | --- |
| [Merged rewrite PR #111](https://github.com/OussamaSegh/Order-and-Chance/pull/111), 8 Nov 2026 | The current fourteen-chapter manuscript and numerous accumulated rewrite/review commits are on `main`. | A merge does not independently certify all proofs or publishing artifacts. |
| `docs/review/volume4-chapter-issue-log.md` | Multiple specific examiner/model reads, repair SHAs, claims of chapter-scope closure; the top of the log contains newer results than its historical “Project-wide blockers” at the bottom. | **Do not treat the November 6 bottom section as current status**, and do not automatically mark past passes invalid. Recheck which reviewed blobs and dependencies still match. |
| `docs/review/volume4-v4-01-18-2026-11-08.md` | A source-side resolution account for eighteen named findings, including a prior Fourier inversion rewrite, Appendix B numbering, figure captions and EPUB image alt. | The Chapter 6 cutoff above survives that earlier rewrite; new finding V4-P1-001 is distinct. Source-side claims do not give independent complete reread. |
| `docs/review/volume4-coverage-2026-11-08.md`, `volume4-line-review-2026-11-08.md` | Specific writer-side inspections, protected cross-volume citation repairs, note that some proofs need an independent challenge. | They explicitly disclaim independent whole-book acceptance. |
| `docs/review/volume4-native-page-ledger.md` | Older exact native artifact at commit `e2b7fd9722b160dedd9e042ff09daea5c4698baa`: **225 print-interior pages** and 226 reading PDF pages, preliminary geometry and sample inspection. | **Not the page count for current `main` or this PR**. Its all-page high-resolution human inspection remains pending. Do not revive superseded 400–500 minimum. |
| `docs/review/volume4-preface-pf10-2026-11-08.md` | Source-side repair to preface figure caption/alternative text. | It explicitly requires regenerated EPUB, reading PDF and print PDF verification. |
| `docs/plan/book-04.md`, `volume4-prerequisites.md` | Owner-approved structure and prerequisite map, newer page policy: ideal 300–600, maximum 600, 300 **not a minimum**. | Preface wording (“Volumes 1–3”) vs Volume 1-only main proof route still warrants the prerequisite/reader-promise audit. |

**Protected invariants checked:** No modification of Volumes 1–3, Appendix B numbering, the four-part structure, cover asset files or publisher scripts. The three corrected chapter files preserve existing labels and theorem numbering; the Chapter 6 strict-threshold fix is an additional sentence correction in one of those files.

## 4. Coverage vs remaining work

**This pass is a reproducible structural check of all 14 chapters and a focused mathematical inspection/repair of four proof or precision sites. It is NOT a complete hostile line-by-line reread of every theorem and solution.** In particular:

| Area | Current disposition | Required next evidence |
| --- | --- | --- |
| Printed 1–5, 7–8, 11–14, Appendix B | Structural route/labels/exercise pairs/figure-file existence checked; old review logs available. | Transfer exact-source valid independent referee signoffs, then examine any gaps/revised dependencies. |
| Printed 6 | New Fourier cutoff repair, numerical/logic check, pending referee. | Full Chapter 6 theorem- and exercise-level independent audit with attention to Cauchy/no-moment smoothing and fourth-moment finite cylinders. |
| Printed 9 | Riffle numerical repair with exact recomputation, pending referee. | Whole Markov and shuffled-deck proof reread, caption check, card-count independent recomputation. |
| Printed 10 | Memorylessness proof clarification, pending referee. | Whole Poisson process/inspection/queue proof reread. |
| Cross-volume | No exported references rewritten; published V1–V3 untouched. | Full labels and prerequisite read of Volumes 5–15 and Volume 1-source dependency map. |
| Native artifacts | Native V4 build passed at PR commit `5bbca612...`; **283 print pages**. Newer head changes require reruns. Full protected workflow failed at Volume 3 C-GROUP despite its passing Python tests. | Inspect new artifacts at the exact final SHA; resolve protected gate via legitimate review, not bypass. |
| Audience and completion | No independent beginner reader or independent final referee. | Separate named reviewers; log issue dispositions by SHA, don't self-sign. |

### Next step after this PR

An integrator should **first obtain independent reviews of V4-P1-001 through V4-P1-004**, then work chapter by chapter against `docs/plan/book-04.md` and the current historical issue log. For every review pass, record its input SHA, file identity, checked exercises, figure inspection scope, findings and rechecks. Keep later teaching changes and production fixes in separate PRs; do not conflate this first proof hotfix with a 10/10 verdict.

## 5. Validation report for this PR

- **Checked:** exact `main` SHA, `main.tex` order and nested Chapter 5 inclusion; syntax labels/references, matching exercise-hint-solution IDs and inclusion of 41 existing figure sources; symbolic cutoff/event proof and survival-function gap; exact integer Eulerian computations for all ten riffle distances.
- **Changed:** `ch06-clt.tex`, `ch08-markov.tex`, `ch09-poisson.tex`, new `tools/test_volume4_math_audit.py`, new `tools/test_volume4_route.py`, and this note.
- **Proven workflow evidence on old PR SHA `5bbca61229075359a358ac079c1faa1e074ff7ed`:** [V4 native run 42515128377](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42515128377) **passed**: 14 EPUB tests, all native formats, 269 layout boxes without detected overflow or unresolved references, both print preflights, **283 print-interior pages**, page dimensions 513×738 pt. [Exact artifact 13631049521](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42515128377/artifacts/13631049521), ZIP SHA-256 `9a983a90c749223d4614f610d675e858484425f4422cee45ff29d6158194d2a5`. **These metrics apply only to that source SHA, not to subsequent modifications.**
- **Full workflow evidence on the same old SHA:** [Build books run 42515128385](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42515128385) ran **532 tests (32 skipped), all passed**, including the three initial V4 mathematics tests, before failing the protected Volume 3 conceptual-source/figure gate: `ValueError: Whole-volume conceptual source/figure drift: C-GROUP`. Build/site/publish jobs were skipped. This is an authentic blocker, not a publication pass; **do not weaken the guard or self-approve its review snapshot**.
- **Not yet performed:** tests and native build on the updated final PR head, all-page high-resolution print/reading comparison, actual Kindle/device check, KDP vendor feedback, distinct mathematical referee or complete chapter-by-chapter proof re-review.
