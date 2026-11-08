# Volume 4 — excellence acceptance register

**State:** IN_PROGRESS; Phase 2 mathematical acceptance BLOCKED (independent exact-source review outstanding). **Created:** 8 November 2026.  
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
| A-01 Baseline manifest and native artifacts | INT | IN_PROGRESS | Phase 1 PR #116 baseline, PR #117 and PR #118 source inventory; both exact-head PR #118 workflows succeeded at `f01eb4915fe66643cc6b7eb072f6534796e83dc6` (runs 42529223645 and 42529223697). No pinned final release candidate. |
| A-02 Reconcile historical issue logs | INT + MATH | IN_PROGRESS | Source-fixed findings V4-P2-001..007 documented in `volume4-phase2-proof-audit-2026-11-08.md` and `volume4-phase2-continuation-2026-11-08.md`. Historical Grok chapter review blobs do not match current sources; see continuation ledger identity table. |
| A-03 Lock numbering/prerequisite/figure semantics | INT | IN_PROGRESS | Four parts, 14 printed chapters, Appendix B; 107 exercise/hint/solution ID triples and 41 figure source paths verified structurally at PR #118. No new route or protected V1–V3 modifications. |
| B-01 Fourier uniqueness cutoff | MATH + PROOF | AWAITING_REVIEW | Ch. 6 `thm:inversion` repair recorded in Phase 1 PR #116 and regression suite. Independent exact-current-blob reproof pending. |
| B-02 Riffle-shuffle rounding + numeric claim audit | MATH | IN_PROGRESS | 52-card rounded-distance ambiguity corrected in Phase 1 PR #116. Whole-book numerical audit and external recheck remain incomplete. |
| B-03 Full mathematical audit | MATH | BLOCKED | 127 theorem/lemma/proposition proof-environment adjacency checks and 107 exercise ID triples are structural only; not every proof, all 107 complete solutions, or all 41 figures independently evaluated. See both Phase 2 ledgers. |
| B-04 Fix/review all correctness findings | PROOF + MATH | BLOCKED | Seven new Phase 2 findings source-fixed: #117 V4-P2-001..004; #118 V4-P2-005..007 (including P0 drift counterexample). Required separate mathematical referee has not signed off repaired source; absence of other P0s unproven. |
| B-05 Prerequisite + downstream citation graph | DEP | IN_PROGRESS | Targeted V1/Markov/Taylor dependency repairs in #117; entire printed-order graph and downstream Volumes 5–15 references require independent verification. Volumes 1–3 untouched. |
| C-01 Teaching architecture and concrete examples | TEACH | UNASSESSED | No artificial padding. |
| C-02 Chapter 6 main/deeper route | TEACH + MATH | UNASSESSED | Reader test and independent math audit required. |
| C-03 Dense proof navigation Ch 5/11/12 | TEACH | UNASSESSED | Rigor and hypotheses preserved. |
| C-04 Caveat, duplication, solution economy | TEACH | UNASSESSED | Remove only redundant material. |
| C-05 Two reader-comprehension tests | READ | UNASSESSED | Include source location and retest result. |
| E-01 Four part transitions/syntheses | TEACH | UNASSESSED | Mathematics-specific rather than templates. |
| E-02 Final V5 handoff and whole-book ending | TEACH | UNASSESSED | No added 15th chapter. |
| E-03 Grading and solutions audit | TEACH + READ | UNASSESSED | Exact problem-to-solution alignment. |
| E-04 Figure/alt/caption checks | FIG | IN_PROGRESS | Three source-data tests: 2,920 urn samples, nine reflection pairs, 10-edge K5 colouring. All-41 native visual, captions and alternate EPUB rendering review outstanding. |
| F-01 Reproducible final build and workflows | PUB | IN_PROGRESS | Exact PR #118 head `f01eb4915fe66643cc6b7eb072f6534796e83dc6`: native production QA run 42529223645 SUCCESS; protected Build books run 42529223697 SUCCESS (549 passed, 32 skipped; site succeeded, publish skipped). Integrated by merge `5dbcb7d1ef26a95b79febce95893d7d7f3f6d640`. Not final-release-SHA acceptance. |
| F-02 All-page PDF/EPUB/device/print QA | PUB + FIG | BLOCKED | Automated 285-page interior, layout and preflights passed at PR #118 exact head; no every-page print/PDF/EPUB independent inspection, physical device proof or KDP signoff. |
| F-03 Volumes 5–15 regression | DEP | UNASSESSED | Downstream citation and dependency audit still required; no published V1–V3 source changes. |
| F-04 Final independent + author acceptance | INT | BLOCKED | No distinct named mathematical referee at the current exact source blobs; author/release signoffs absent. Corrected source and green CI cannot satisfy this gate. |

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
| 10 — Poisson clock | `ch09-poisson.tex` | AWAITING_REVIEW | UNASSESSED | IN_PROGRESS | V4-P2-001 (#117) and V4-P2-007 (#118) repaired; current blob must be independently rechecked. |
| 11 — Martingales | `ch10-martingales.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 12 — Brownian motion | `ch11-brownian.tex` | AWAITING_REVIEW | UNASSESSED | IN_PROGRESS | V4-P2-005 and V4-P2-006 repaired in #118; current blob must be independently rechecked. |
| 13 — Probabilistic method | `ch12-method.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| 14 — Random graphs | `ch14-graphs.tex` | UNASSESSED | UNASSESSED | UNASSESSED | — |
| Appendix **B** — Extremal problems | `extremal.tex` | UNASSESSED | UNASSESSED | IN_PROGRESS | Two new exhaustive finite enumerations check `R(3,3)=6` and `W(3,2)=9` (new test file; new PR CI must pass). Does not certify appendix proofs or five solutions. |

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


## E. Phase 2 reconciliation after PR #118 (8 November 2026)

**Current integration baseline:** `main` merge commit `5dbcb7d1ef26a95b79febce95893d7d7f3f6d640`, integrating [PR #118](https://github.com/OussamaSegh/Order-and-Chance/pull/118) from head `f01eb4915fe66643cc6b7eb072f6534796e83dc6`. [PR #117](https://github.com/OussamaSegh/Order-and-Chance/pull/117) was merged at `8f559f6c03e21adbb1a2eddb7f34a46e17adfb3a`.

**Source-fixed but still AWAITING_REVIEW:** V4-P2-001 exponential fourth-moment prerequisite, -002 Markov gcd dependency, -003 Pólya Taylor remainder, -004 delta-method exercise domain, -005 drifted-Brownian counterexample to the old centred-covariance equivalence (P0), -006 within-copy Brownian increment independence, -007 Poisson nonexplosion countable intersection. Full statements, locations, tests and source-level evidence appear in the two Phase 2 ledgers. No one who authored these changes is recorded as an independent referee.

**Automated results at exact PR #118 head:** protected Build books run [42529223697](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42529223697) completed SUCCESS (549 passed, 32 skipped; site SUCCESS; publish SKIPPED). Native QA [42529223645](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42529223645) completed SUCCESS, including print/EPUB/reader production, 285-page interior and both print preflights. Eleven math regression tests, three figure-source data tests and one 127-claim adjacency test are included in the successful suite. `PASS` for those specific automated checks is not a mathematical release verdict.

**Additional scoped evidence in this follow-up PR:** two exhaustive finite enumerations confirm the Appendix B small cases: a triangle-free two-colouring exists on `K5` (12 of 1,024 edge-colourings), none on `K6` (0 of 32,768); a three-term-AP-free two-colouring exists on `[8]` (6 of 256), none on `[9]` (0 of 512). These are independent arithmetic computations, **not** a named external proof referee. CI status for this follow-up must be verified at its final head before integration.

**Historical source identity:** the continuation ledger compares seven historic Grok-reviewed source blobs with the current files, finding no exact matches for those checked samples. A historical signoff is not transferable merely because the chapter title is unchanged.

**Blocked acceptance:** complete adversarial reproof of all 14 printed chapters and Appendix B at actual blobs; independent signoff on changed P0/P1 passages; all 107 exercises, hints and solutions checked mathematically; 41 figures visually and semantically inspected in PDF/EPUB; remaining prerequisite and Volumes 5–15 dependency audit; beginner/voice assessments; physical-device/all-page production and author approval. Do not convert any of these to `PASS` from CI or a structural test.
