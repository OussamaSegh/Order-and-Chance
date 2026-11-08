# Volume 4 — Excellence plan and agent execution contract

**Status:** Proposed plan only; no manuscript changes or acceptance asserted.  
**Prepared:** 8 November 2026.  
**Repository baseline at planning:** `main` `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`; [Volume 4 rewrite PR #111](https://github.com/OussamaSegh/Order-and-Chance/pull/111) was merged on 8 November 2026.  
**Companion tracker:** [Volume 4 excellence acceptance register](../review/volume4-excellence-acceptance-register.md).

## 0. Objective and meaning of “10/10”

Make **Volume 4: Chance — The Logic of Uncertainty** a mathematical book that is exceptionally correct, teachable, memorable, coherent with Volumes 1–3, and professionally publishable. “10/10” is an editorial aspiration, **not a score an agent can certify**. Earn it through evidence rather than cosmetic changes or self-awarded ratings.

A release candidate must demonstrate all six qualities:

| Quality | Required evidence |
| --- | --- |
| Mathematical reliability | Every statement, numerical example, exercise and solution independently checked at an identified source commit; no unresolved correctness blockers. |
| Prerequisite integrity | Every non-elementary premise either proved earlier on the reading path or cited to an actually proved earlier result; no later-volume result silently imported. |
| Pedagogical clarity | Serious-beginner read-throughs can identify the question, intuition, definitions, pivotal proof step and payoff of every chapter, including the hardest ones. |
| Narrative coherence | Four parts and fourteen chapters lead from modeling randomness to discovering deterministic structure; bridges and ending genuinely synthesize, not merely announce. |
| Economy and voice | No redundant defensive disclaimers, repetitive proofs, filler, jargon without explanation or generic AI-sounding prose; full rigor remains. |
| Production quality | Exact-revision PDF, print, EPUB and online-reader checks; every page and figure actually reviewed at readable resolution, not just contact sheets. |

**Release rule:** All blocking issues closed, all chapter signoffs independently evidenced, production artifacts inspected, and final author/editor approval recorded. A perfect score is never a substitute for these gates.

## 1. Authority, invariants, and scope

Read these in order before touching text:

1. `AGENTS.md`, `docs/WRITING-STYLE.md`, `docs/agents/mathematician-writer.md`, `docs/SERIES-STRUCTURE.md`.
2. `docs/plan/book-04.md`, `docs/plan/volume4-prerequisites.md`, `docs/plan/volume4-citation-migration.md`.
3. `volume4-chance/main.tex`, the preface, all 14 included chapters, `ch05-geometric.tex`, Appendix `extremal.tex`, blurb and cover note.
4. Existing findings: `docs/review/volume4-chapter-issue-log.md`, `volume4-v4-01-18-2026-11-08.md`, `volume4-line-review-2026-11-08.md`, `volume4-coverage-2026-11-08.md`, `volume4-native-page-ledger.md`, `volume4-preface-pf10-2026-11-08.md`, and `volume4-substantive-depth-backlog.md`. These are historical evidence, **not** a blank slate or blanket acceptance.

**Locked unless the author explicitly changes the contract:**

- Exactly **four parts, fourteen numbered chapters**, in the order of `volume4-chance/main.tex`, plus **Appendix B**. Do not renumber the appendix to A merely because it is the only appendix; its B designation protects downstream references.
- Preserve proved depth: CLT/Lindeberg, entropy/coding, Pólya recurrence, card shuffling, Poisson process, martingales, Brownian construction, probabilistic method, random graphs. **Do not** solve density by deleting real mathematics.
- Maintain theorem labels and downstream contract, especially Theorem 6.8 (inversion), 6.10 (Lindeberg), 11.9 (Doob), 11.10 (Azuma), 12.4 (Brownian existence), 12.12 (reflection), Lemma 10.5 (colouring) and Exercise 13.4 (crossing). Cross-check printed numbering when labels move.
- Published Volumes 1–3 are **read-only**. If a published-volume error is suspected, record it separately for the owner; do not silently edit their source. Cross-volume citation adjustments in later unpublished volumes need a separate justified PR.
- Preserve approved series typography, covers, the Galton motif, design palette, 7×10 trim, KDP bleed/export policy, ISBN/listing requirements, artifact names and protected Volume 3 conceptual gate. No font files, cover templates or shared publishing code touched without an explicit, tested dependency.
- Owner's **latest** page guidance in `docs/plan/book-04.md`: ideal **300–600 pages**, maximum 600, **300 is not a minimum**, and pagination is not a license to pad, squeeze or omit proofs. Historical 400–500 and 260–290 numbers are superseded.
- Prerequisite wording needs **reconciliation**: `docs/plan/book-04.md` says Volume 1 alone is on the main proof path, while the preface calls high school plus Volumes 1–3 the prerequisites. Review the actual dependency map and seek owner signoff for any changed reader-facing promise; do not silently lower or raise the bar.
- Use the single house style `docs/WRITING-STYLE.md`; do not invent a competing style guide or rewrite cover copy as a proxy for manuscript editing.

This planning PR is **documentation only**. Agents implementing it should open separately scoped PRs, not commit their rewrites onto the planning branch.

## 2. Team roles, ownership and strict independence

| Role / agent | Responsibility | May sign off? |
| --- | --- | --- |
| **Integrator / managing editor (INT)** | Maintain dependency graph and acceptance register, assign non-overlapping file ownership, rebase on current `main`, route disputes, merge approved PRs. | Integration completeness only; not their own mathematical work. |
| **Independent mathematical referee (MATH)** | Hostile line-by-line reproof of theorem statements, lemmas, examples, exercises, hints and solutions; verify finite/infinite interchanges and constants. | Mathematical gate for a commit they did **not** author. |
| **Proof repair writer (PROOF)** | Fix findings with minimal diffs, preserve labels, add precise proof tests and counterexample checks. | Never self-sign off repairs. |
| **Prerequisite/cross-volume auditor (DEP)** | Verify earlier proofs, label/order map, Volume 1–3 boundary and Volumes 5–15 downstream references. | Dependency gate if not their own fixes. |
| **Teaching editor (TEACH)** | Improve worked small cases, proof-roadmaps, transitions, essential/deeper routes, exercise scaffolding and chapter consolidation. | Reader-quality review of another agent's prose only. |
| **Beginner-reader tester (READ)** | Attempt exercises without seeing solutions; mark first unexplained symbols and places where insight disappears. | Comprehension gate as a genuinely different reader. |
| **Illustration/accessibility editor (FIG)** | Inspect each included figure, true numbers/units, simulation vs schematic labels, alt text and print/EPUB legibility. | Visual gate only on an independently inspected render. |
| **Production/release engineer (PUB)** | Build, compare, and inspect source/reading PDF/KDP print/EPUB/reader at a pinned SHA; no skipped checks. | Production gate on the exact released artifacts. |

One person or model can work in multiple roles across unrelated chapters, **but the author of a change cannot serve as its independent referee**. Existing reviewer records remain valid only for the exact reviewed source and claimed scope. An old signed-off file may stay closed if its contents and dependencies have not changed; otherwise determine whether targeted recheck or full reread is required. Do not invent a reviewer identity or say a physical Kindle/KDP proof was checked unless it was.

For each implementation PR: one named chapter/file owner; a separate reviewer; stable issue IDs; exact commit SHA; reproducer or derivation; evidence of the rerun; consequences for other chapters; clear before/after explanation. The integrator prevents overlapping edits to the same `.tex` file.

## 3. Execution order and hard gates

### Phase A — Baseline and triage (before rewrites)

**A-01 / INT — Capture reproducible baseline.** Record current `main` SHA, input file list in `main.tex`, chapter/section labels, native build SHA, print-interior count, EPUB assets, figure manifest and cross-volume references. Build on **the SHA actually being reviewed**, not historical PR #111 CI. Preserve logs, artifact digests and screenshots. A passing old run cannot sign off a changed book.

**A-02 / INT+MATH — Reconcile existing logs.** Classify every relevant open historical issue as *fixed-and-independently-verified*, *source-fixed-but-unverified*, *open*, *stale* or *duplicate*. Use current file content and Git history to avoid undoing previously repaired proofs. Do **not** import old page counts or claimed closed gates mechanically. Put residual blockers in the companion register and cross-link original issue IDs.

**A-03 / INT — Freeze manuscript semantics.** Take a label/contents snapshot. Any proposed new chapter, reordered part, appendix rename or loss of a named theorem requires owner approval before coding. Pure editorial changes may rearrange material *inside* a chapter when label and prerequisite contracts survive.

**Exit A:** documented exact baseline, no ambiguity over which outstanding issues remain, and PR assignments that do not overlap.

### Phase B — Mathematical and logical reliability (highest priority)

**B-01 / MATH+PROOF — Verify and repair the Chapter 6 Fourier uniqueness cutoff.** In `ch06-clt.tex` around `thm:inversion`, the passage from compactly supported tests to bounded uniformly continuous tests bounds a large-window cutoff error using `P(|X|>A-1)+P(|σZ|>1)` and then says *both* terms become small as `A` grows. The second term does not depend on `A`. Confirm the argument and repair with a genuinely growing Gaussian-tail threshold, or an equivalent rigorous two-stage limit. Test an arbitrary heavy-tailed law such as Cauchy and verify no finite-moment assumption was imported. Retain the stronger theorem and its label. **A prose-level assurance is not a proof.**

**B-02 / MATH — Check all numerical and linguistic precision claims.** In `ch08-markov.tex` the 52-card riffle-shuffle table gives distances `1` for `k≤4` while describing numbers rounded to three decimals. Establish the finite exact distances and print **“rounds to 1.000”**, not literal equality, wherever appropriate; compare numerical evaluations with the Bayer–Diaconis formula. Check all other decimal-only claims, normal constants, binomial counts, coverage statements, tail bounds and captions.

**B-03 / MATH — Adversarial entire-book mathematical audit.** Re-read the actual inclusion order, all statements and proofs, the preface claims, Appendix B and **every** exercise/hint/solution. Build a theorem- and exercise-level ledger. High-risk checks: tails and countable events on the digit model; nonlinear limits and swaps of expectations/integrals; special parameters at 0/1; CLT assumptions and characteristic functions; typical-set quantifier order; recurrence and hitting times; Doeblin and strong stationary times; Poisson conditional laws and the two-sided bus distinction; optional stopping and unbounded times; Brownian construction, restart, quadratic variation, dyadic remainder and almost-sure claims; dependency graphs in the local lemma; graph exploration stochastic domination. Reproduce small finite examples directly or with independently checked short code. Don't mark a theorem correct just because the proof sounds plausible.

**B-04 / PROOF+MATH — Resolve findings and recheck.** Patch minimal mathematical defects first (P0 = false theorem/incorrect proof/dependency; P1 = ambiguous equality/hypothesis; P2 = unnecessary wording). Each fix must have a separately recorded full proof or counterexample and the independent referee's review at the new SHA. No stylistic rewriting during the repair if it makes the mathematical diff harder to inspect.

**B-05 / DEP — Verify the prerequisite graph.** Check the first use of every advanced fact against the printed order, Volume 1 proof, or current earlier Volume 4 chapter. Validate `docs/plan/volume4-prerequisites.md` against text, not intent. Volumes 2–3 may provide context but may not be silently essential if Volume 1-only main path is retained. Explicitly tag previews of Volumes 7, 11, 12 as **not used in proofs**. Review special cases where finite probability/finite partitions are generalized to continuous or countable models. Compare downstream uses in Volumes 5–15 without editing V1–V3.

**Exit B:** zero open P0 correctness/dependency issues; independent referee evidence for every mathematical change and for unchanged chapters covered by an exact-source review; no unexplained assumptions.

### Phase C — Pedagogy, chapter by chapter, without deleting depth

**C-01 / TEACH — Establish a consistent teaching shape.** Every major chapter has: (i) an actual question in ordinary language; (ii) one small solved instance; (iii) intuitive obstruction; (iv) definitions and precise theorem; (v) a sentence describing the key proof idea *before* technical details; (vi) a worked payoff/limitation; (vii) graded exercises and an end-of-chapter “What you can now do” synthesis with **specific mathematics**. Avoid mechanical repeated templates, hollow summaries and extra page count for its own sake.

**C-02 / TEACH+MATH — Rebuild Chapter 6's reader path, not its content.** Lead with a concrete coin/dice or sample-mean example, normalization by `√n`, the Gaussian mechanism and the classical CLT. Put a worked finite-`n` check close to the result and distinguish ordinary CLT from local asymptotics. Present Fourier inversion and Lindeberg with purpose, prerequisites, short navigational signposts and a clearly flagged deeper route; consider an internal appendix/optional section **within Chapter 6** without changing external theorem numbers. Contrast a heavy-tailed failure (Cauchy), a finite-variance success and a nonidentical triangular-array condition. Have a fresh beginner attempt the essential route before approving. Make formal proof *easier to traverse*, not weaker.

**C-03 / TEACH — Reduce technical-wall fatigue in Chapters 5, 11 and 12.** For the continuous-integral toolkit, bounded/square-integrable martingale convergence and Brownian Lévy construction, state the mathematical job, key estimate, and exact scope before several pages of proof. Move repetitious justifications to a clearly marked lemma or explanation **only if prerequisites and proof completeness survive**. Keep continuous-time conditional-expectation and Itô claims honestly deferred. Distinguish “reader should understand” from “reader may study the full proof” without assuming an unproved theorem in the essential path.

**C-04 / TEACH — Tighten recurring caveats and repeated examples.** Inventory all phrases “not a simulation,” “not a claim,” “not exact,” “not a proof,” and “later volume.” Keep necessary caveats at points of genuine confusion; remove duplicates that no longer teach. In captions, identify the pictured object/scale and what is proved instead of narrating verification history. Replace repeated exercise-solution reproofs with concise derivations *only where the solution remains self-contained for the assigned question*. Preserve explicit exceptions where they are mathematically central.

**C-05 / READ — Run two reading tests.** (1) An attentive high-school-plus-Volume-1 reader tries the opening and Chapter 6 main route, with no university probability training. (2) A motivated reader attempts selected exercises and explains entropy, mixing, inspection paradox, martingale stopping and Brownian quadratic variation back in their own words. For every failure, capture the exact location, missing concept and repair; rerun the same task on the revised source. Readers may rely on Volumes 2–3 context only where the contract permits.

**Exit C:** the main theorem route is intelligible without skipping an unproved dependency; serious-beginner reader reports are issue-driven and closed; new sections contain concrete insight rather than padding.

### Phase D — Chapter-specific tasks in publication order

The table gives **targeted improvements**, not blanket assertions that these areas are defective. Apply only where the baseline audit demonstrates a real need.

| ID | Chapter / actual source | Agent job | Evidence and acceptance |
| --- | --- | --- | --- |
| D-01 | 1 — `ch01-counting.tex` | Confirm the infinity-of-tosses motivation, explicit cylinders and probability-zero distinction; verify the ballot/conditioning examples and two-child/Monty variants. | Beginner can compute a finite model and explain what the infinite event adds; no imported countable-additivity theorem. |
| D-02 | 2 — `ch02-discrete.tex` | Compare fixed points, permutation cycles, empty boxes and coupon collector without collapsing law/mean/variance; verify exact small-`n` examples. | At least one clean numerical worked example per major tool, plus reviewed solutions. |
| D-03 | 3 — `ch03-generating.tex` | Show concretely what a PGF calculates that direct counting does not; make extinction and Catalan steps visible. | Reader derives a mass/mean from a PGF and understands the extinction fixed point and its hypotheses. |
| D-04 | 4 — `ch04-inequalities.tex` | Keep a single comparison of Markov/Chebyshev/Chernoff/Hoeffding on the *same event*; illuminate Borel–Cantelli and strong law; retain Bernstein–Weierstrass payoff. | Assumptions and meaningful numeric bounds independently checked. |
| D-05 | 5 — `ch05-continuous.tex` + included `ch05-geometric.tex` | Make density vs distribution, changes of variables, Bertrand models, Buffon needle and Box–Muller readable; tame derivation overload. | Precise sample-space assumptions for geometric probabilities, labeled Jacobian/integral domains and clean figure captions. |
| D-06 | 6 — `ch06-clt.tex` | **Flagship teaching refactor** and Fourier repair, Lindeberg depth route, normal approximations and heavy-tail comparison. | Three independently solved test scenarios; mathematical and beginner-reader signoffs; labels stable. |
| D-07 | 7 — `ch07-entropy.tex` | Preserve the strong narrative from surprise to Kraft/Shannon/Huffman, KL, mutual information and block coding; trim arithmetic detours that serve only decimals. | Reader can encode/decode a concrete law, calculate expected lengths and state exactly what typicality guarantees. |
| D-08 | 8 — `ch07-walks.tex` | Keep reflection, ruin, visits/Pólya, arcsine and electrical analogy connected; contrast exact finite paths and asymptotics. | Independent small-path enumeration and correct restart/absorption/hitting-time distinction. |
| D-09 | 9 — `ch08-markov.tex` | Clarify stationary vs mixing, periodicity, coupling and strong stationary time; make riffle rounding precise. | Recompute 3-state row/TV and 52-card shuffle figures; preserved total-variation definitions and sharp-vs-bound distinction. |
| D-10 | 10 — `ch09-poisson.tex` | Protect the especially strong exponential-clock narrative; distinguish one-sided/two-sided inspection; give thinning/queue calculation context. | Verified conditional arrival-time and age/residual distributions, exact rate units and queue stability restriction. |
| D-11 | 11 — `ch10-martingales.tex` | Preserve finite-partition conditional expectation and stopping warnings; improve navigation through Doob, Azuma, convergence, patterns and urns. | Reader can diagnose a wrong optional-stopping argument; full independent convergence-proof audit. |
| D-12 | 12 — `ch11-brownian.tex` | Explain the Lévy midpoint construction visually, incremental independence, quadratic variation, nowhere differentiability and precise Itô preview. | Random/analytical path figure semantics distinguished; no unjustified continuous-filtration theorem. |
| D-13 | 13 — `ch12-method.tex` | Strengthen “average → existence” payoff, alteration/local lemma/second moment, and crossing-number argument. | Finite colouring and graph arithmetic independently reproduced; joint dependency definition correct. |
| D-14 | 14 — `ch14-graphs.tex` | Give a satisfying distinction between subcritical result, partial supercritical exercise and triangle threshold; preserve exact limits proved. | Clear final synthesis and justified Volume 5 transition, no claim of unproved giant component. |
| D-B | Appendix B — `extremal.tex` | Audit Turán, Ramsey, Schur, sunflower, EKR, van der Waerden and exercises; improve its framing as an optional deterministic complement. | Appendix remains B with all downstream references valid; figures and proof counts independently checked. |
| D-F | Front/back matter — `preface.tex`, `blurb.tex`, `about-the-cover.tex` | Align promise, prerequisites and book actually delivered; check reader entry, opening figure alt, jacket and cover-note facts. | No cross-volume contradiction; specific, accurate copy in house voice. |

### Phase E — Finish the book as a book

**E-01 / TEACH — Add specific consolidation without a 15th chapter.** A short, useful end-of-part recap or connective paragraph at each of four part boundaries; use one problem that links adjacent techniques (for example PGFs → laws, concentration → entropy, walks → mixing, martingale/continuous motion → probabilistic existence). Cross-references must name the actual result and be tested against current `main.tex` numbering.

**E-02 / TEACH — Give the ending weight.** At the end of Chapter 14 (or an **unnumbered** afterword if the owner approves), answer the book's initial coin question in mature terms, identify four things the reader learned to do (model/count, predict averages, track evolving chance, prove existence) with specific examples, and hand off accurately to *Volume 5: Calculation — From Formula to Insight*. Keep it short and original; do not append a generic inspirational conclusion.

**E-03 / TEACH+READ — Exercise architecture.** Verify every question uses only earlier material or explicitly marks an advanced bridge. Retain full solutions, but repair solution-to-question mismatches and differentiate `★` check, `★★` combination and `★★★` genuine investigation. For each chapter have a separate reader attempt at least one problem per present difficulty class before reading its hint. Record time/point of first blockage but do not use speed as a pass/fail measure.

**E-04 / FIG — Figure, caption and accessibility sweep.** For **each included** figure check mathematical state, palette semantics, labels/units, provenance (sample vs exact vs schematic), legibility in native 7×10 print and Kindle-scale EPUB, contextual alt text, and absence of clipped labels. The existing preface-alt fix and `ch05-geometric.tex` inclusion require actual rebuilt EPUB verification. Orphan figure files need not be deleted merely because they are unused. No cover redesign in this plan.

**Exit E:** a coherent first-to-last reading, no stale reference/figure semantics, and independent reader and production-figure signoff.

### Phase F — Native artifacts, release and author acceptance

**F-01 / PUB — On an exact final candidate SHA, run** `python3 -m unittest discover -s tools -p test_epub.py`, `./build.sh volume4-chance`, the repository's `Volume 4 native production QA` workflow, and the full `Build books` workflow/protected Volume 3 conceptual gate where changes trigger it. Test all modified helpers, including any dedicated KDP/EPUB preflight. Record exact workflow URL, artifact IDs, source SHA, test output, content hashes, page count and failures, not a generic “CI passed.” Since a docs-only PR does not trigger `volume4-qa.yml`, dispatch or require it when source changes are integrated.

**F-02 / PUB+FIG — Physical-layout inspection.** Review **every reading PDF and print-interior page at legible resolution**, matched by actual printed/physical page mapping; verify crosslinks, headings, text order, theorem labels, all math, figure labels and contrast, full-bleed dividers, facing-page bleed orientation, typography and printer rasterization. Contact sheets or automated word bounds alone are insufficient. Independently inspect EPUB on an actual supported device/reader for formula baseline, responsive figures, informative alt and navigation. Retain actual KDP proof feedback as a separate vendor gate; do not label a simulator as KDP acceptance.

**F-03 / DEP — Cross-volume regression.** Scan links and theorem labels in Volumes 5–15 that cite Volume 4. If migration is necessary, do a separately reviewed minimal PR; **never silently adjust published V1–V3**. Recheck external book references, bibliography and author/date assertions against primary sources when uncertain. Preserve Appendix B and the citation migration map.

**F-04 / INT — Final acceptance.** Freeze the candidate SHA. Collect independent mathematical signoff for each chapter, proof repairs, prerequisites, teaching/voice, reader test, source/figure accessibility, native artifact review, cross-volume impact and vendor status. Check the companion register has no invented or inherited acceptance. Publish only after the author agrees the trade-offs and unresolved nonblockers are acceptable.

**Exit F:** exact artifact/commit evidence, zero blocker rows, explicit author go/no-go. Otherwise the book stays a candidate.

## 4. Merge batches and dependencies

Work in this order; these are **separate implementation PRs**:

1. **`V4-B0` — correctness hotfixes:** B-01/B-02 and any discovered P0 math defects; include focused independent proofs and tests. Merge before large prose rewrites.
2. **`V4-B1` — dependency and numbering audit:** B-03/B-05, with issues filed rather than speculative rewrites. No source edits to V1–V3.
3. **`V4-C6` — Chapter 6 teaching redesign:** C-02 + D-06; mathematical reviewer and novice reader must both pass.
4. **`V4-C1` — Parts I–II teaching:** D-01..D-05 and D-07, nonoverlapping chapter PRs. Follow the chapter's input order.
5. **`V4-C2` — Part III teaching:** D-08..D-12, nonoverlapping chapter PRs; higher-priority martingale/Brownian audit before simplification.
6. **`V4-C3` — Part IV, appendix and bookends:** D-13, D-14, D-B, D-F, E-01..E-03.
7. **`V4-PUB` — Figures and release audit:** E-04, F-01..F-04 and only the minimal defects those gates reveal.

Integrate chapter PRs one at a time onto current `main`; all dependent downstream tests rerun after each changed proof/label. Do not force-push another agent's branch or merge in a way that discards independent review. A PR may be deferred or removed if its intervention does not demonstrably improve reading or correctness.

## 5. Required template for implementation PRs

Use these exact headings in each implementation PR:

- **Scope and issue IDs:** narrow paths, baseline SHA, intended readers; state what will **not** change.
- **Mathematical change:** theorem/label, old failure, minimal correct replacement, proof or independent recomputation, assumptions and edge cases.
- **Teaching change:** reader problem observed, text/figure/exercise changed, evidence that the concept is clearer without reduced depth.
- **Dependency and citation impact:** earlier sources, later volume references, numbering/appendix, published V1–V3 invariant.
- **Validation:** unit/number checks, build command, **exact tested SHA**, CI artifact and page evidence when relevant.
- **Independent review:** named distinct reviewer, SHA, all findings and disposition; never self-sign.
- **Residual concerns:** measurable open questions; release blockers conspicuous.

An issue entry must include `ID | severity | chapter/path + stable label | exact claim or reproducer | discovered SHA | fix SHA | test/evidence | independent reviewer | disposition`. Classify:
- **P0/blocker:** false claim, proof gap, incorrect assumption, missing prerequisite, broken math or unreadable production element;
- **P1/major:** confusing core exposition, misleading number/caption, missing pivotal step, wrong exercise level or consequential cross-volume mismatch;
- **P2/polish:** redundant caveat, awkward prose, redundant derivation or minor figure refinement.

Do not declare an issue “resolved” merely because someone changed a sentence. It is resolved when the change passes a **fresh, distinct** review at the new SHA.

## 6. Final independent scorecard (not an automatic score)

Have **at least two genuinely independent whole-book readers**: one mathematical and one pedagogical. Each assigns a supported 1–5 grade on **correctness, prerequisite integrity, teachability, examples, coherence, voice/economy and visual/production quality**; scores require page/label evidence, not a feeling. If either finds a P0, release fails regardless of average. Repeat any failed category after repair on the new exact source.

The editorial aspiration is for both reviewers to find each category exceptional (5/5) with no substantive blocker. This is the closest useful operational meaning of “10/10”; a subjective perfect rating is **never guaranteed**.

## 7. Explicit non-goals

No new volume, no reordering 14 approved chapters, no “Appendix A correction,” no page-padding, no generic expansion to reach 400 pages, no removal of mathematically ambitious material just to shorten proofs, no blanket conversion to measure-theoretic prerequisites, no rewriting V1–V3, no cover redesign, no KDP acceptance claims from a local build, no fake reader tests, no untracked “AI reviewer passed” assertions, and no release without independent exact-commit verification.
