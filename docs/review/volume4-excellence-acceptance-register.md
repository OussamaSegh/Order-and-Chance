# Volume 4 — excellence acceptance register

**State:** PHASE 2 SOURCE-MATHEMATICS PASS / PHASE 3 BOOK-WIDE QA IN_PROGRESS. Overall excellence and release gates are not closed. Phase 3 tracking is GitHub issue [#139](https://github.com/OussamaSegh/Order-and-Chance/issues/139). The Phase 3 baseline is merged `main` `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f` (PR #137). Do not read a Phase 3 gate as passed unless the handoff cites examined evidence. At the merged `main` of PR #136 (`070b9e00a5afadbe3d4153339cfd99cd72329d24`), sole-validator source acceptance covers **127/127 labeled mathematical proof-bearing assertions and 107/107 exercise/hint/solution triples**, including the Chapter 12 signoff merged in #135. The whole-book 41-figure mathematical-semantic, reading/pedagogy, full cross-volume graph, final-candidate and external print/device/release gates are **not** automatically passed. The author appointed GPT-6 as sole mathematical validator on 9 November 2026; external mathematical signoff is not required. **Created:** 8 November 2026.
**Plan:** [Volume 4 excellence execution plan](../plan/volume4-excellence-execution-plan-2026-11-08.md).
**Planning baseline:** `main` `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`. This is **not** a final candidate SHA.
**Important:** Historical reviews exist in `volume4-chapter-issue-log.md`, `volume4-coverage-2026-11-08.md` and other review documents. Nothing below erases their work or treats their past source/CI signoffs as acceptance of a new revision.

## Rules for updating

- Record only explicitly scoped proof-level evidence from source reading, independent-method calculation, or tested correction. No external mathematical referee is required; self-review is not called independent.
- Allowed statuses: `UNASSESSED`, `ASSIGNED`, `IN_PROGRESS`, `AWAITING_REVIEW`, `BLOCKED`, `PASS`, `N/A (reason)`.
- Claim-level `PASS` needs an exact source SHA, sole validator identity (ChatGPT GPT-6), validation date, actual reasoning or counterexample, and issue disposition. Full chapter `PASS` requires all claims and solutions reviewed. A writer's own review is not independent, and must be marked sole-validator.
- Retire duplicate historical findings with a source explanation; keep an old review signoff only if the file and relevant proof dependencies were unchanged and the exact scope still applies.
- A passed build confirms compilation/publishing checks, not theorem correctness, mathematical pedagogy, a physical Kindle, or KDP approval.
- Prefer stable theorem/exercise labels, not historical line numbers.
- If source changes after signoff, record whether the change invalidates the prior signoff and recheck as needed.
- Final acceptance is per book at one pinned candidate SHA. A chapter-by-chapter collection of passing old commits is not automatically a current-book approval.

## A. Triage and quality gates

| Work item | Owner | Status | Exact SHA / evidence / blocker |
| --- | --- | --- | --- |
| A-01 Baseline manifest and native artifacts | INT | IN_PROGRESS | Main after merged #135 and #136: `070b9e00a5afadbe3d4153339cfd99cd72329d24`. At exact final PR #135 head `199ef70b50333da61e6cc6aeb9b8fbc74eb91ef5`, Build books 42705781455 and native Volume 4 QA 42705781178 both SUCCESS. At exact final PR #136 head `5d12f8e1fdc423dae9e8ccf2f1325a848817007b`, Build books 42723990278 (including all six changed books and site) and native QA 42723990578 both SUCCESS. Phase 3 rechecked merged main `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f`: Build books [42736422791](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42736422791) SUCCESS (list job 616 tests OK, 32 skipped; book rebuild skipped because the library fingerprint was unchanged from `070b9e00`; site job validated all fifteen cached volumes and uploaded the Pages artifact). Native QA was not dispatched on that SHA (Actions write permission denied). `volume4-chance` and `common` are byte-identical to native QA [42723990578](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42723990578). Release candidate and author publication signoff remain separate. See the Phase 3 section below. |
| A-02 Reconcile historical issue logs | INT + MATH | IN_PROGRESS | Source-fixed findings V4-P2-001..007 documented in `volume4-phase2-proof-audit-2026-11-08.md` and `volume4-phase2-continuation-2026-11-08.md`. Historical Grok chapter review blobs do not match current sources; see continuation ledger identity table. |
| A-03 Lock numbering/prerequisite/figure semantics | INT | IN_PROGRESS | Four parts, 14 printed chapters, Appendix B; 107 exercise/hint/solution ID triples and 41 figure source paths verified structurally at PR #118. No new route or protected V1–V3 modifications. |
| B-01 Fourier uniqueness cutoff | MATH + PROOF | PASS | Source repair in #116 and two-sided inversion interval cutoffs fixed in #125. GPT-6 sole-validator complete Chapter 6 proof and exercise reread in merged #133 at pinned blob `8b1863f270060898cb28eaa9eb3672b18fdd8847`, including `thm:inversion`. Finite tests supplement proof review; broader pedagogical/figure gates separate. |
| B-02 Riffle-shuffle rounding + numeric claim audit | MATH | IN_PROGRESS | Exact 52-card distances corrected in #116. Additional independently reproduced 1,000-coin tail, Ramsey alteration, crossing count and Huffman block code in new Phase 2 finite-exercise ledger. Still not a full numerical audit. |
| B-03 Full mathematical audit | MATH | PASS | Source-locked GPT-6 sole-validator reread covers **127/127 labeled mathematical proof-bearing claims and 107/107 complete exercise/hint/solution triples** across printed Chapters 1–14 and Appendix B. Historical merged #126–#133, #130–#132 covered 115/127 and 100/107; final 12 labeled proofs, one unlabeled variation corollary, and 7 triples from Chapter 12 signed in merged #135 at TeX blob `7c576031edc38e04019336de0a0a1a1bfefeb2b1`. Each chapter's ledger lists claim-level reasoning and source identities. PASS here means **source-level named mathematics** only, not full 41-figure visual/semantic, independent reader, entire Volumes 5–15 prerequisite graph or print/device/author acceptance. |
| B-04 Fix/review all correctness findings | PROOF + MATH | PASS | All presently confirmed source-level V4 mathematical P0/P1 proof corrections were integrated through #134; the final source-locked Chapter 12 sole-validator reread in #135 passed both required final-head CI checks and was merged. In addition, open downstream mathematical scope dependencies were repaired in merged #136 (18 findings DEP-12..29, with a strict-supremum Borel–Cantelli proof repair). **This is not an exhaustive certification of every other volume or figure.** New concrete counterexamples must be opened and corrected, not waived by this scope-limited PASS. |
| B-05 Prerequisite + downstream citation graph | DEP | IN_PROGRESS | The V4 local proof order and Volume 1 boundary were mapped; #123 repaired a Volume 12 Brownian measurability prerequisite. Merged #136 repaired **18** separately reasoned downstream claims/citations DEP-12..29 in actual unpublished Volumes 6,7,11,12,15. Its exact final-head six-volume Build books 42723990278 and native V4 QA 42723990578 completed SUCCESS. This is targeted correction evidence, **not** exhaustive Volumes 5–15 cross-volume semantic graph acceptance. Published Volumes 1–3 unchanged. |
| C-01 Teaching architecture and concrete examples | TEACH | UNASSESSED | No artificial padding. |
| C-02 Chapter 6 main/deeper route | TEACH + MATH | UNASSESSED | Mathematical proofs/solutions were accepted in merged #133; the separate first-reader navigation, teaching/figure comprehension and deeper-route readability test are not yet performed. |
| C-03 Dense proof navigation Ch 5/11/12 | TEACH | UNASSESSED | Rigor and hypotheses preserved. |
| C-04 Caveat, duplication, solution economy | TEACH | UNASSESSED | Remove only redundant material. |
| C-05 Two reader-comprehension tests | READ | UNASSESSED | Include source location and retest result. |
| E-01 Four part transitions/syntheses | TEACH | UNASSESSED | Mathematics-specific rather than templates. |
| E-02 Final V5 handoff and whole-book ending | TEACH | UNASSESSED | No added 15th chapter. |
| E-03 Grading and solutions audit | TEACH + READ | IN_PROGRESS | **107/107 complete exercise/hint/solution triples** now have source-locked sole-validator mathematical PASS, including the seven Chapter 12 triples added in merged #135 (successful native QA 42705781178, Build books 42705781455). Difficulty grading, independent solve-without-hints reader testing, narrative teaching and final combined-candidate checks remain open. The mathematically complete triples do not make the separate reader/teaching gate PASS. |
| E-04 Figure/alt/caption checks | FIG | IN_PROGRESS | Inspected PR #121 actual native EPUB: 41 embedded plates at 1800px, 41 HTML references with descriptive nonempty alt; reviewed 41-plate visual contact sheet and selected plates at full resolution. In actual print PDF 40 captions searchable plus Figure 13.1 visibly present on rasterized page 254. Detailed mathematical figure-by-figure semantics and real reader/device audits still open. |
| F-01 Reproducible final build and workflows | PUB | IN_PROGRESS | After owner resolved GitHub billing issue #138, exact PR #135 final head `199ef70b50333da61e6cc6aeb9b8fbc74eb91ef5` passed Build books 42705781455 and native QA 42705781178. Exact final #136 head `5d12f8e1fdc423dae9e8ccf2f1325a848817007b` passed Build books 42723990278 for Volumes 4,6,7,11,12,15 plus site, and Volume 4 native QA 42723990578. Register-only #137 prior head `4c6b3339de57482c05b88303568ed824d357ca7c` passed Build books 42715300093, **but this updated register has a new head requiring a new check**. Main-push production and final release-candidate pin/digest parity are not yet signed off. |
| F-02 All-page PDF/EPUB/device/print QA | PUB + FIG | BLOCKED | Actual PR #121 print PDF inspected programmatically on all 285 pages: no text blocks out of page; 40 searchable captions plus rasterized Figure 13.1 visually verified on page 254, and actual 41 EPUB plates reviewed in contact sheet. Still no *individual every-page high-resolution* visual signoff, real-device EPUB/print proof or KDP vendor approval. |
| F-03 Volumes 5–15 regression | DEP | IN_PROGRESS | Merged #123 repaired Brownian measurability and phantom exercise-part references in Volume 12. Merged #136 resolves **18** separately reasoned downstream mathematical proof, numbering and scope errors (DEP-12..29), with source tests and exact final-head Build books SUCCESS for all modified Volumes 6,7,11,12,15 and V4. The remaining Volumes 5–15 reference/prerequisite graph has not been exhaustively assessed, and other unpublished volumes were not all rebuilt. |
| F-04 Sole-validator mathematics + author release acceptance | INT | IN_PROGRESS | As of merged #135 and #136, GPT-6 sole-validator source-level named mathematics is accepted **127/127 labeled proof claims and 107/107 exercise triples** at pinned, unchanged V4 manuscript blobs; no external mathematical referee required. Full 41-figure mathematical semantics, readability/pedagogy, physical print/EPUB/device, full dependency graph, exact merged-main candidate production QA and **explicit author publication approval** remain pending. Source signoff is not a publication go/no-go. |

## B. Chapter-by-chapter acceptance register

| Printed chapter | Source path | Math referee | Beginner/voice reviewer | Figure, exercise and solution audit | Exact checked SHA / evidence |
| --- | --- | --- | --- | --- | --- |
| Preface / bookends | `volume4-chance/chapters/preface.tex`, `blurb.tex`, `about-the-cover.tex` | UNASSESSED | UNASSESSED | UNASSESSED | Reconcile prior PF-10 and historical logs. |
| 1 — Games to spaces | `ch01-counting.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on exact blob `ef5b5ac00bb5f137f4f8cb9934a41c3422984a01`: four proof labels and eight statement/hint/solution triples, each reasoned in `volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md`; reader and figure semantics separate. |
| 2 — Random variables | `ch02-discrete.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator GPT-6 mathematical PASS on exact blob `921ea590d21af564a636dbcce53a73f7ee6cc61b`: all seven proof labels and eight exercise/hint/solution triples independently re-examined. See `volume4-phase2-sole-validator-ch2-ch7-appendix-b-signoff-2026-11-09.md`. Figure semantics, teaching and candidate recheck pending. |
| 3 — Generating functions | `ch03-generating.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on exact blob `10c1ebdc486ca82ec335654bbacc8cfa6ad0ae76`: seven proof labels and eight statement/hint/solution triples; exact reasoning in `volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md`; reader and figure semantics separate. |
| 4 — Concentration | `ch04-inequalities.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on exact blob `9501619f8494005eb2c50d0d689541332ea04289`: 6 proof assertions +6 full exercise triples; detailed reasoning and source-lock regression in `volume4-phase2-sole-validator-ch1-ch3-ch4-signoff-2026-11-09.md` (#127). Reader and figures separate. |
| 5 — Continuous chance | `ch05-continuous.tex`, included `ch05-geometric.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on blobs `4d2221df7adeb926d46c7526faa7829a77645db9` and `2bc6858a1cb598473be2f233ae5ed6b05ff0e93e`: 11 proof labels +9 complete exercise triples, detailed in `volume4-phase2-sole-validator-ch5-ch13-ch14-signoff-2026-11-09.md` (#128). Figure semantic review separate. |
| 6 — Bell curve | `ch06-clt.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS in merged PR #133: all 14 proof-bearing labels (including unnumbered-type theorem/corollary environments), all 8 full exercise triples, pinned Git blob `8b1863f270060898cb28eaa9eb3672b18fdd8847`. Fourier inversion and Lindeberg proof scope documented in `volume4-phase2-sole-validator-ch6-signoff-2026-11-09.md`; figures and teaching separate. |
| 7 — Entropy/codes | `ch07-entropy.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator GPT-6 mathematical PASS on exact blob `25330e7046f0b585bef9ebffb1408bc907c109df`: all eight proof labels and six exercise/hint/solution triples re-examined. See pinned audit ledger. Figure semantics, teaching and candidate recheck pending. |
| 8 — Random walks | `ch07-walks.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS in merged #130, actual blob `8b64abc66f79ccbc792906fbfa9ba50e9ab3e890`: all 9 named proofs and all 8 exercise triples. See `volume4-phase2-sole-validator-ch8-ch10-signoff-2026-11-09.md`; visual/reader gates separate. |
| 9 — Markov/mixing | `ch08-markov.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS in merged #131, actual blob `ddfc2e52756052755a0d26437b782f104c069a3f`: 10 proofs and 9 full exercise/hint/solution triples including exact riffle computations and finite mixing. Reader/figure semantics separate. |
| 10 — Poisson clock | `ch09-poisson.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS in merged #130, blob `6de4e7e1fd5c6369d553e45190e54807c553a743`: 13 source proofs, 8 complete exercise triples, with independent exact finite case checks. Earlier nonexplosion correction #118 included. Separate reader/visual gates remain. |
| 11 — Martingales | `ch10-martingales.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS in merged #132 at blob `319d07e1e851eb821d34d21535315ec7b35d77b3`: 11 named proofs and 5 complete triples; explicitly verifies finite interval atom condition and Pólya urn construction after #124 and source-locked regressions. Full-filtration theorem is not attributed to V4; downstream correction in open #136. |
| 12 — Brownian motion | `ch11-brownian.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS for all **12 labeled proofs**, extra **unlabeled variation corollary** and **7 complete exercise triples** on exact unchanged source blob `7c576031edc38e04019336de0a0a1a1bfefeb2b1`, after #134 quadratic-variation repair. The source-locked reasoning/tests were merged in #135 at `1778324959ba8e7d027cd5384d9ccdc9065fec20`, with Build books 42705781455 SUCCESS and native QA 42705781178 SUCCESS on the exact PR head. Reader test, 41-figure semantics and physical/device QA remain separate. |
| 13 — Probabilistic method | `ch12-method.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on exact blob `7bb8f4a676a46524817beb217d04f18ad6317a21`: six proof labels and six exercise/hint/solution triples, including local lemma dependency graph and crossing lemma; see `volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md`. |
| 14 — Random graphs | `ch14-graphs.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator mathematical PASS on exact blob `a494b82eee49bc1ed43d43b9b74894ed821706d4`: two proof labels and six exercise/hint/solution triples, including subcritical domination and partial supercritical lower bound; see `volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md`. |
| Appendix **B** — Extremal problems | `extremal.tex` | PASS | UNASSESSED | IN_PROGRESS | Sole-validator GPT-6 mathematical PASS on exact blob `3899f21ebcc1a05e68cd545cdb96e103d215ffad`: seven proof labels and all five exercise/hint/solution triples. General Ramsey/van der Waerden/ERK proofs checked, separate finite enumeration in #119. Figure semantics, teaching and candidate recheck pending. |

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

The grade is **diagnostic, not an automatic “10/10.”** The sole mathematical validator records precise evidence at the same candidate SHA. Beginner/production checks are separate tasks, not mandatory second mathematical referees.

| Dimension | Math reviewer 1–5 + evidence | Reader reviewer 1–5 + evidence | Blocking finding? |
| --- | --- | --- | --- |
| Correctness | Pending | Pending | Unknown |
| Prerequisite integrity | Pending | Pending | Unknown |
| Teachability | Pending | Pending | Unknown |
| Examples and exercises | Pending | Pending | Unknown |
| Whole-book coherence | Pending | Pending | Unknown |
| Voice and editorial economy | Pending | Pending | Unknown |
| Figures and production readability | Pending | Pending | Unknown |

**Go/no-go:** `NOT EVALUATED`. An open P0 forces `NO GO`. Sole-validator whole-book exact-commit mathematical validation and author release authorization are mandatory; an external mathematical signature is not required.


## E. Phase 2 reconciliation after PR #118 (8 November 2026)

**Current integration baseline:** `main` merge commit `5dbcb7d1ef26a95b79febce95893d7d7f3f6d640`, integrating [PR #118](https://github.com/OussamaSegh/Order-and-Chance/pull/118) from head `f01eb4915fe66643cc6b7eb072f6534796e83dc6`. [PR #117](https://github.com/OussamaSegh/Order-and-Chance/pull/117) was merged at `8f559f6c03e21adbb1a2eddb7f34a46e17adfb3a`.

**Source-fixed but still AWAITING_REVIEW:** V4-P2-001 exponential fourth-moment prerequisite, -002 Markov gcd dependency, -003 Pólya Taylor remainder, -004 delta-method exercise domain, -005 drifted-Brownian counterexample to the old centred-covariance equivalence (P0), -006 within-copy Brownian increment independence, -007 Poisson nonexplosion countable intersection. Full statements, locations, tests and source-level evidence appear in the two Phase 2 ledgers. No one who authored these changes is recorded as an independent referee.

**Automated results at exact PR #118 head:** protected Build books run [42529223697](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42529223697) completed SUCCESS (549 passed, 32 skipped; site SUCCESS; publish SKIPPED). Native QA [42529223645](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42529223645) completed SUCCESS, including print/EPUB/reader production, 285-page interior and both print preflights. Eleven math regression tests, three figure-source data tests and one 127-claim adjacency test are included in the successful suite. `PASS` for those specific automated checks is not a mathematical release verdict.

**Additional scoped evidence in this follow-up PR:** two exhaustive finite enumerations confirm the Appendix B small cases: a triangle-free two-colouring exists on `K5` (12 of 1,024 edge-colourings), none on `K6` (0 of 32,768); a three-term-AP-free two-colouring exists on `[8]` (6 of 256), none on `[9]` (0 of 512). These are independent arithmetic computations, **not** a named external proof referee. CI status for this follow-up must be verified at its final head before integration.

**Historical source identity:** the continuation ledger compares seven historic Grok-reviewed source blobs with the current files, finding no exact matches for those checked samples. A historical signoff is not transferable merely because the chapter title is unchanged.

**Blocked acceptance:** complete adversarial reproof of all 14 printed chapters and Appendix B at actual blobs; independent signoff on changed P0/P1 passages; all 107 exercises, hints and solutions checked mathematically; 41 figures visually and semantically inspected in PDF/EPUB; remaining prerequisite and Volumes 5–15 dependency audit; beginner/voice assessments; physical-device/all-page production and author approval. Do not convert any of these to `PASS` from CI or a structural test.


## Phase 2 continuation — 9 November 2026

**Verified working baseline:** main merge `0c097e7a1041cfc647cf79b7dd3e3000a93aeec4` from PR #119. Build books [42532424808](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42532424808) and Volume 4 native QA [42532424809](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42532424809) both completed successfully at head `44bb31c6dc43247723339c0cacc3a051e210abe5`; 551 tests passed with 32 skips. A merge-only commit does not alter their tree when the compare endpoint reports no changed files.

**New, not independently approved:** V4-P2-008 `prop:bmgauss` had not explicitly derived joint Gaussianity of all observations in the converse and did not clearly reduce arbitrary disjoint intervals to a common Gaussian endpoint grid. V4-P2-009 `thm:polyaurn` inferred the limit distribution function from continuous test expectations without giving the needed continuous indicator cutoff argument in the book's interval framework. Both have minimal source fixes plus two regression tests, documented in [volume4-phase2-proof-completion-2026-11-09.md](volume4-phase2-proof-completion-2026-11-09.md). Distinct reviewer signoff and exact new-PR CI must be checked; these items are **SOURCE-FIXED / AWAITING_REVIEW**, not `PASS`.

**Acceptance remains blocked:** A mathematical author/self-audit and green builds cannot stand in for a different mathematical referee. The 14-chapter plus Appendix B proof review, 107 full exercises, 41 rendered figures, dependency checks, reading/physical publication and author approval gates remain open. The current PR does not change Volumes 1–3.


## F. Author-directed sole-validator policy (9 November 2026)

The author appoints **ChatGPT GPT-6 as the only mathematical validator**. This supersedes all earlier demands for an external, distinct or independent referee in this file and historical ledgers. Their historical findings remain useful; those old *referee requirements* do not remain release gates.

**VERIFIED** means a named claim has been re-examined at a specific source blob, with mathematical reasoning, counterexample testing or independent-method calculations logged. **CORRECTION REQUIRED** means a concrete fault has been demonstrated. **NOT YET REVIEWED** means no substantive mathematical check for the named scope. Self-review must be transparently labelled; passing tests or compilation is never sufficient for a mathematical finding to be verified. Chapter and whole-volume approval require review of every theorem, proof, example, exercise/hint/solution and the mathematics of figures, not a sample.

**First scoped verified claim:** Chapter 11 `thm:monkey`, baseline TeX blob `7cbc0f7a749af5fbf16ee17455ff1bd9fe7ff291`. The sole validator directly inspected the casino/optional-stopping proof (bounded stopped wealth, passage through bounded times, completed-prefix/suffix overlaps) and independently computed the wait through an absorbing-prefix Markov chain over exact fractions, without using the martingale formula. Results: ABRACADABRA over 26 letters equals 26^11+26^4+26 = 3,670,344,487,444,778; fair-coin HT equals 4 and HH equals 6. Regression added in `tools/test_volume4_pattern_waiting.py`.

**New source clarification:** `def:stopping` called a future-dependent random clock a stopping time, then denied it was one. It now correctly calls this a random time and gives the one-step fair-sign counterexample `{tau<=0}={X_1=-1}`, not determined by the time-0 partition. This fixes explanatory wording, not a false theorem; a regression checks the actual two-outcome event.

**Still unfinished:** whole-book sole-validator review of 14 printed chapters plus Appendix B, 107 exercises/solutions, mathematical correctness of 41 figures, prerequisite graph, print/EPUB/device visual checks and author release authorization. Release status remains NOT EVALUATED.


## Phase 2 independent finite mathematics and native figure audit — 9 November 2026

**Sole-validator status remains IN_PROGRESS.** Targeted mathematical evidence: nine new exhaustive/independent exact-arithmetic tests at tools/test_volume4_phase2_independent_finite_exercises.py; local run 9/9 passed. Detailed conditions, exact results and deliberately limited signoff scope recorded at [volume4-phase2-finite-math-and-artifact-audit-2026-11-09.md](volume4-phase2-finite-math-and-artifact-audit-2026-11-09.md).

**Evidence not inferred from green CI:** Downloaded production ZIP artifact 13658514107 from native QA run 42584550749, visually inspected a contact sheet of all 41 actual EPUB plates and detailed selected originals; all 41 EPUB HTML image references have nonempty descriptive alt. Read the 285-page actual print PDF's text blocks and detected no outside-page blocks. Printed Figure 13.1 is present, visibly, on a *rasterized* page 254; PDF text search alone misleadingly finds only 40 figure captions. This reconciles 41 figures without a source correction.

**Not certified:** mathematical validity of all 127 proof-bearing assertions and all 107 exercise/hint/solution triples; full high-resolution semantic figure review; cross-volume downstream dependencies and complete prerequisite graph. The nine new unit tests provide finite independent evidence, not a formal theorem verifier. External mathematical refereeing is no longer required; the author's separate publication authorization remains distinct.


## Phase 2 downstream logical prerequisite V4-P2-011 — 9 November 2026

Source finding, proof and regression documented in [volume4-phase2-downstream-brownian-prerequisite-2026-11-09.md](volume4-phase2-downstream-brownian-prerequisite-2026-11-09.md). In Volume 12's Brownian path chapter, source claimed nonexistent parts (a) and (c) of Volume 4 Exercise 12.3. The (c) conclusion is proved in the *whole* Volume 4 zero-set exercise solution, so its pointer is corrected. The alleged (a) joint-measurability fact was **not** proved by Volume 4: Volume 12 now supplies a self-contained product-measurability argument by left-dyadic step approximations to continuous Brownian paths before invoking Tonelli in ex:fast. This is a mathematical prerequisite repair, not a cover design or stylistic edit.

Do not mark all Volumes 5–15 references reviewed because one phantom subpart family is now guarded. Phase 2 full mathematical acceptance remains IN_PROGRESS under the author-designated sole-validator model. Neither external referees nor green builds may waive genuine unexamined mathematics.


## Phase 2 exact-source mathematical signoffs: 9 November 2026

Source-level sole-validator mathematical PASS now covers **22 labelled proofs and 19 exercise/hint/solution triples** across printed Chapters **2**, **7**, and **Appendix B** at the three exact TeX blob hashes in [the independent mathematical audit](volume4-phase2-sole-validator-ch2-ch7-appendix-b-signoff-2026-11-09.md). The record provides claim-level arguments, each exercise identifier, validator, date, source identity, and disposition. None of these sources was edited in the audit PR. No external referee is required by the author's appointment, but this is a sole-validator review and must not be misrepresented as independent third-party signoff.

At that historical #126 snapshot this covered neither the **then-remaining 105 proof-bearing assertions and 88 exercise triples** nor per-figure visual-semantic and reader checks. The Math-referee cells show PASS only for the three verified blobs, while the combined figure/exercise audit stays IN_PROGRESS because figure accessibility and real-device rendering have not passed. Full candidate release signoff remains blocked on all remaining gates and author publication authority.


## Phase 2 sole-validator claim-level mathematics for Chs 1, 3, 13 and 14 (2026-11-09)

Pinned full source mathematical audit: [volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md](volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md). Four chapters exactly audited for 19 printed named proof-bearing assertions and 28 full exercise/hint/solution triples with per-label mathematical reasoning, issue boundary and SHA; added to the prior 22/19 yields **41/127 proof claims and 47/107 exercise triples** at their exact read blobs. **Not Phase 2 completion:** 86 proof claims and 60 exercise triples remain outside these signoffs, and figure-semantic, downstream reference, and final pinned-book candidate gates remain OPEN. The mathematics of unreviewed material is not certified by compilation or enumerating finite examples. Sole validator GPT-6; no external referee.


## Phase 2 integration reconciliation after PRs #127 and #128 (9 November 2026)

The protected published Volumes 1–3 remain untouched. On main `045eb0c58b8d9d8b5486284ba1a4fd6ea37516a7`, PRs #126–#128 collectively accept **58 of 127** proof-bearing assertions and **62 of 107** complete exercise/hint/solution triples, on exact source blob hashes with substantive reasoning and source-lock tests. See [Chapters 1, 3 and 4](volume4-phase2-sole-validator-ch1-ch3-ch4-signoff-2026-11-09.md), [Chapters 5, 13 and 14](volume4-phase2-sole-validator-ch5-ch13-ch14-signoff-2026-11-09.md), [Chapters 2, 7 and Appendix B](volume4-phase2-sole-validator-ch2-ch7-appendix-b-signoff-2026-11-09.md) and supplementary [Chapters 1, 3, 13 and 14 per-claim reasoning](volume4-phase2-sole-validator-ch1-ch3-ch13-ch14-2026-11-09.md).

Remaining named mathematical scope: **69 proof-bearing assertions and 45 exercise/hint/solution triples in printed Chapters 6, 8, 9, 10, 11 and 12.** Separate individual figures, cross-volume prerequisites, full final-head regression/production acceptance and author release authority remain open. Passing Builds for PRs #127/#128 verifies the exact technical trees, not unreviewed mathematics. GPT-6 is the sole mathematical validator; no external referee is required.


## Phase 2 source-mathematics integration — 10 November 2026

**Confirmed merged main:** `070b9e00a5afadbe3d4153339cfd99cd72329d24`, following accepted [#135](https://github.com/OussamaSegh/Order-and-Chance/pull/135) merge `1778324959ba8e7d027cd5384d9ccdc9065fec20` and [#136](https://github.com/OussamaSegh/Order-and-Chance/pull/136) merge `070b9e00a5afadbe3d4153339cfd99cd72329d24`. The mathematical source of printed Chapter 12 remains exact Git blob `7c576031edc38e04019336de0a0a1a1bfefeb2b1` after both integrations. Published Volumes 1–3 were not changed by either PR. This register update is still proposed in PR #137 and requires its own exact-head CI.

**Source-locked sole-validator result, not a third-party refereeing claim:** 127 of 127 proof-bearing printed assertions, all 107 exercise statement/hint/solution triples, and the additional unlabeled variation corollary received substantive case-by-case mathematical examination at exact manuscript blob hashes recorded in the chapter ledgers. The 12 remaining Chapter 12 labels and seven triples were accepted in #135 (plus independent finite arithmetic corroborations). Review includes real source mathematics; test counts and compilation alone are **not** mathematical proofs.

**Confirmed final-head production evidence:** #135 Build books [42705781455](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42705781455), native QA [42705781178](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42705781178) **SUCCESS**; #136 Build books [42723990278](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42723990278), native QA [42723990578](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42723990578) **SUCCESS**. #136 Build books actually completed and passed for changed Volumes 4, 6, 7, 11, 12, 15 and site. #137's prior unmodified head had a successful Build books [42715300093](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42715300093); this new acceptance update needs its **own** successful workflow. GitHub runner failures from billing (issue #138) have been resolved and are **not** a remaining technical impediment. Main merge commit's own production run and digest parity must be checked if elevated to final release candidate.

**Downstream mathematical repairs are merged, but graph coverage is not total:** #136's 18 source-verified repairs DEP-12..29 include corrected printed theorem numbering; a newly justified bounded optional-stopping lemma for the general Brownian filtration, without abusing V4's finite-partition restriction; a local Kolmogorov independent-series proof using the **strict supremum** event in a valid continuity-from-below/Borel–Cantelli step; and a correct Bernoulli Cramér rate-function argument instead of a non-existent V4 Theorem 4.7. These corrections are in the *unpublished* Volumes 6,7,11,12,15, leaving Volumes 1–3 intact. No complete Volumes 5–15 citation/semantic graph acceptance is asserted.

**Remaining gates are independent:** Each of 41 figures needs a claim-to-rendered-graphic semantic check at release candidate; first-reader pedagogical passes, numerical/graded exercises and full-page high-resolution print/EPUB/device accessibility checks remain to be recorded; whole-book/whole-library final SHA artifact parity and explicit publisher/author go-no-go remain outstanding. An author's publication authorization cannot be inferred from mathematics or CI, and there is no external mathematical referee gate under the author's sole-validator instruction. The editorial acceptance register therefore remains **IN_PROGRESS**, even though the named Phase 2 manuscript-mathematics ledger is complete.

## Phase 3 book-wide QA — opened 10 November 2026

Tracker: issue [#139](https://github.com/OussamaSegh/Order-and-Chance/issues/139). Handoff: [docs/handoffs/volume4-phase3.md](../handoffs/volume4-phase3.md). Validator for this phase: the designated validator (an AI reviewer). This is not independent external refereeing. PR #137 is merged; the paragraph above that still calls it proposed records the file as written before that merge.

| Gate | Status | Evidence |
| --- | --- | --- |
| 3A Integration | IN_PROGRESS | Build books 42736422791 on exact main `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f` succeeded. The `build` matrix was skipped because `changed` was empty. Native production QA has not run on that SHA. Workflow dispatch returned HTTP 403. A later PR that touches `volume4-chance` or `tools` is the available way to obtain a fresh native run. |
| 3B Figures | IN_PROGRESS | Source audit of the 41 referenced plates is in [volume4-phase3-figure-audit-2026-11-10.md](volume4-phase3-figure-audit-2026-11-10.md). Three ink-word defects (charcoal called blue) are corrected in the Phase 3 branch. Rendered PDF/EPUB inspection of the corrected plates is not yet recorded. Thirty-odd unused figure files are outside the inventory. |
| 3C Pedagogy | UNASSESSED | Not yet reviewed in this phase. Phase 2 mathematical signoff is not a teaching signoff. |
| 3D Dependencies | IN_PROGRESS | DEP-12..29 remain intact (12+3 unit tests OK). Volumes 1–3 are unchanged from the parent of #136. Critical downstream citation defects in unpublished Volumes 5, 6 and 11 are recorded in [volume4-phase3-dependency-audit-2026-11-10.md](volume4-phase3-dependency-audit-2026-11-10.md) and stay open proposals. |
| 3E Production | UNASSESSED | No fresh native artifact on the Phase 3 head. No physical device was used. |
| 3F Release candidate | UNASSESSED | No candidate manifest. Author publication approval is not requested and is not granted. |
