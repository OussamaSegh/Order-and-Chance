# Volume 4 — excellence acceptance register

**State:** Unassessed / not approved. **Created:** 8 November 2026.  
**Plan:** [Volume 4 excellence execution plan](../plan/volume4-excellence-execution-plan-2026-11-08.md).  
**Planning baseline:** `main` `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`. This is **not** a final candidate SHA.  
**Important:** Historical reviews exist in `volume4-chapter-issue-log.md`, `volume4-coverage-2026-11-08.md` and other review documents. Nothing below erases their work or treats their past source/CI signoffs as acceptance of a new revision.

## Rules for updating

- Update this file **only with independently substantiated facts** from a scoped implementation PR; put a link in the evidence cell.
- Allowed statuses: `UNASSESSED`, `ASSIGNED`, `IN_PROGRESS`, `AWAITING_REVIEW`, `BLOCKED`, `PASS`, `N/A (reason)`.
- `PASS` needs the *exact source SHA*, distinct named reviewer, date, explicit checked claim and issue dispositions. A writer's own review is not independent.
- Retire duplicate historical findings with a source explanation; keep an old review signoff only if the file and relevant proof dependencies were unchanged and the exact scope still applies.
- A passed build confirms compilation/publishing checks, not theorem correctness, mathematical pedagogy, a physical Kindle, or KDP approval.
- Prefer stable theorem/exercise labels, not historical line numbers.
- If source changes after signoff, record whether the change invalidates the prior signoff and recheck as needed.
- Final acceptance is per book at one pinned candidate SHA. A chapter-by-chapter collection of passing old commits is not automatically a current-book approval.

## A. Triage and quality gates

| Work item | Owner | Status | Exact SHA / evidence / blocker |
| --- | --- | --- | --- |
| A-01 Baseline manifest and native artifacts | INT | UNASSESSED | Baseline planning SHA is not a build. |
| A-02 Reconcile historical issue logs | INT + MATH | UNASSESSED | Link statuses; do not re-open settled issues by assumption. |
| A-03 Lock numbering/prerequisite/figure semantics | INT | UNASSESSED | Record owner decisions for any exception. |
| B-01 Fourier uniqueness cutoff | MATH + PROOF | UNASSESSED | Inspect `ch06-clt.tex` at `thm:inversion`: Gaussian tail threshold fixed at 1 is not controlled by `A→∞`. |
| B-02 Riffle-shuffle rounding + numeric claim audit | MATH | UNASSESSED | `ch08-markov.tex`: determine where “1” means a number rounded to 1.000. |
| B-03 Full mathematical audit | MATH | UNASSESSED | All 14 chapters, hints, solutions, appendix, bookends. |
| B-04 Fix/review all correctness findings | PROOF + MATH | UNASSESSED | No P0 may remain. |
| B-05 Prerequisite + downstream citation graph | DEP | UNASSESSED | Published V1–V3 remain read-only. |
| C-01 Teaching architecture and concrete examples | TEACH | UNASSESSED | No artificial padding. |
| C-02 Chapter 6 main/deeper route | TEACH + MATH | UNASSESSED | Reader test and independent math audit required. |
| C-03 Dense proof navigation Ch 5/11/12 | TEACH | UNASSESSED | Rigor and hypotheses preserved. |
| C-04 Caveat, duplication, solution economy | TEACH | UNASSESSED | Remove only redundant material. |
| C-05 Two reader-comprehension tests | READ | UNASSESSED | Include source location and retest result. |
| E-01 Four part transitions/syntheses | TEACH | UNASSESSED | Mathematics-specific rather than templates. |
| E-02 Final V5 handoff and whole-book ending | TEACH | UNASSESSED | No added 15th chapter. |
| E-03 Grading and solutions audit | TEACH + READ | UNASSESSED | Exact problem-to-solution alignment. |
| E-04 Figure/alt/caption checks | FIG | UNASSESSED | Check each **included** figure in native formats. |
| F-01 Reproducible final build and workflows | PUB | UNASSESSED | Record source SHA, run IDs, hashes, logs. |
| F-02 All-page PDF/EPUB/device/print QA | PUB + FIG | UNASSESSED | Contact sheets do not count as all-page inspection. |
| F-03 Volumes 5–15 regression | DEP | UNASSESSED | Separate approved PR for consequential fixes. |
| F-04 Final independent + author acceptance | INT | UNASSESSED | Unmergeable release gate until evidence exists. |

## B. Chapter-by-chapter acceptance register

| Printed chapter | Source path | Math referee | Beginner/voice reviewer | Figure, exercise and solution audit | Exact checked SHA / evidence |
| --- | --- | --- | --- | --- | --- |
| Preface / bookends | `volume4-chance/chapters/preface.tex`, `blurb.tex`, `about-the-cover.tex` | UNASSESSED | UNASSESSED | UNASSESSED | Reconcile prior PF-10 and historical logs. |
| 1 — Games to spaces | `ch01-counting.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 2 — Random variables | `ch02-discrete.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 3 — Generating functions | `ch03-generating.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 4 — Concentration | `ch04-inequalities.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 5 — Continuous chance | `ch05-continuous.tex`, included `ch05-geometric.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 6 — Bell curve | `ch06-clt.tex` | UNASSESSED | UNASSESSED | UNASSESSED | B-01 check first. |
| 7 — Entropy/codes | `ch07-entropy.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 8 — Random walks | `ch07-walks.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 9 — Markov/mixing | `ch08-markov.tex` | UNASSESSED | UNASSESSED | UNASSESSED | B-02 check first. |
| 10 — Poisson clock | `ch09-poisson.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 11 — Martingales | `ch10-martingales.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 12 — Brownian motion | `ch11-brownian.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 13 — Probabilistic method | `ch12-method.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 14 — Random graphs | `ch14-graphs.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| Appendix **B** — Extremal problems | `extremal.tex` | UNASSESSED | UNASSESSED | UNASSESSED | Keep B, not A. |

All chapter paths above are relative to `volume4-chance/chapters/` unless written otherwise. Neither `UNASSESSED` nor em dash means “not reviewed historically”; each means **no evidence has yet been transferred and revalidated for this initiative**.

## C. Finding template (duplicate one row per issue)

| ID | Severity | File + stable label | Claim/counterexample or reader failure | Discovered SHA | Repair SHA/PR | Independent reviewer/date | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V4-EX-001 | P0/P1/P2 | `path` / `\label{...}` | Concrete finding, not “unclear” | SHA | SHA + link | reviewer + date | OPEN / RECHECK / CLOSED |

**Pre-triage candidates only, not certified current defects:**

- **`V4-X-FOR`**: Chapter 6 Fourier compact-support cutoff with non-growing `P(|σZ|>1)` term; independent math verification required.
- **`V4-X-RIF`**: Chapter 9 exact-vs-rounded riffle total-variation wording; numerical recomputation and precision repair required.

If either matches an existing finding in the historical ledger, use the established ID and link this one as an alias; do not create duplicate work.

## D. Production evidence per release candidate

| Gate | Required output | Status | Evidence/sha |
| --- | --- | --- | --- |
| Candidate source revision | Current commit SHA; full source inventory | UNASSESSED | — |
| EPUB unit tests | `python3 -m unittest discover -s tools -p test_epub.py` with Pandoc present | UNASSESSED | — |
| Full book build | `./build.sh volume4-chance` logs and checks | UNASSESSED | — |
| Volume 4 native QA | Exact GitHub Actions run and artifact digests | UNASSESSED | — |
| Full Build books/protected C-GROUP | Exact run/needed cross-volume gate | UNASSESSED | — |
| Native reading PDF + KDP print | All-page high-resolution inspection and provenance parity | UNASSESSED | — |
| EPUB/reader accessibility | Actual target reader/device, formula baseline, captions, alt, links | UNASSESSED | — |
| Cover and KDP metadata | Preserve approved cover; no unapproved modifications | UNASSESSED | — |
| KDP vendor proof/acceptance | Actual external acceptance/proof feedback, if available | UNASSESSED | — |
| Mathematical final referee | Entire current book, precise claims at candidate SHA | UNASSESSED | — |
| Pedagogical final referee | Entire current book, specific reader failures and retests | UNASSESSED | — |
| Author editorial approval | Explicit documented go/no-go | UNASSESSED | — |

## E. Final reviewer scorecard

The grade is **diagnostic, not an automatic “10/10.”** Two independent readers fill in evidence for all seven dimensions at the *same* candidate SHA.

| Dimension | Math reviewer 1–5 + evidence | Reader reviewer 1–5 + evidence | Blocking finding? |
| --- | --- | --- | --- |
| Correctness | Pending | Pending | Unknown |
| Prerequisite integrity | Pending | Pending | Unknown |
| Teachability | Pending | Pending | Unknown |
| Examples and exercises | Pending | Pending | Unknown |
| Whole-book coherence | Pending | Pending | Unknown |
| Voice and editorial economy | Pending | Pending | Unknown |
| Figures and production readability | Pending | Pending | Unknown |

**Go/no-go:** `NOT EVALUATED`. An open P0 forces `NO GO`, regardless of grades. Independent exact-commit rereview and author approval are mandatory before this can be changed to `GO`.
