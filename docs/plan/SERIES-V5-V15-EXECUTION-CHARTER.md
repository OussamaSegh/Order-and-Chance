# Volumes 5–15 — execution charter and acceptance gates

> **Historical record. Not the plan.** This document is kept as it was written, for the record of how the plan was reached. It is superseded by the [definitive master plan for Volumes 5–15](MASTER-PLAN-V5-V15.md), which rules on every question raised here. Section 2 of the master plan lists which of this document's recommendations were accepted and which were rejected. Do not act on a recommendation below without checking it there.

**Status:** Proposed implementation standard, accompanying PR #150's detailed diagnostic review. This is a *plan*, not evidence that the manuscripts have been corrected or their proofs independently verified.

**Scope:** Volumes 5–15 of *Order and Chance*. Preserve published Volumes 1–3 and the currently completed Volume 4 text. Keep the existing 15-volume sequence, titles, subtitles, six-part series division, and the central question: how can primes obey rigid laws while displaying randomness? Any future change to that canon needs an explicit decision record, not an incidental chapter move.

**Companion documents:** [Independent architectural review](SERIES-PLAN-REVIEW-2026-11.md), [series master content plan](SERIES-CONTENT-PLAN.md), per-volume specifications (book-05.md through book-15.md), [series catalog](../../common/series-catalog.json), and each volume's actual main.tex. The architectural review diagnoses *what* must change; this charter defines *how to execute, verify, and accept it*. The main.tex input closure is the truth about what prints; a plan or orphan file is not a printed chapter.

## 1. Decisions recommended now

| Issue | Recommended disposition | Non-negotiable condition |
| --- | --- | --- |
| Volume 5's Hardy–Ramanujan and Waring chapters | **Resolve before Volume 5 release.** Prefer relocating the two advanced circle-method excursions to an optional later reading path after their prerequisites, rather than inflating Volume 5. If retained in Volume 5, provide self-contained proofs of the inputs and place them *after* the Fourier/transform chapters. | These currently rely on **future Volume 6** results: Hardy–Ramanujan explicitly uses the eta transformation; Waring invokes sums-of-minima bounds, and also cites later Volume 5 Fourier inversion. Merely labelling the future result does not make a complete Volume 5 proof. |
| Volume 8's semicircle and sine kernel | Move the two chapters into Volume 12's final random-matrix block; retarget citations. After the move, change Volume 12 Part III's catalog name from “Networks” to “Networks and Random Matrices” and regenerate metadata from the catalog. | The sine-kernel proof needs Volume 9's Weyl/correlation work and Volume 11's Lyapunov theorem; those cannot be ordinary premises in Volume 8. |
| Haar/Fourier theory on Q_p in Volume 8 | Move the Q_p-specific section and related exercises to Volume 13 **after** construction of Q_p; leave the general Haar theory in Volume 8. | No move may break the proof, labels, exercises, or local/global normalization conventions of Tate's chapter. |
| Linear-algebra reprise in Volume 8 | Keep only load-bearing operator theory on the sequential path. Make the reprise optional, clearly marked and independently navigable; do not delete its distinct results by assumption. | Check internal citations and page budget after the move, including what *actually prints* in all formats. |
| Quadratic number theory in Volume 13 | Choose one canonical proof of unique ideal factorization; recast the other development as illustrative worked examples. | Construct a theorem-by-theorem equivalence table before removing any proof; retain exercises, variants, and prerequisites. |
| Volume 14's numerical prime-gap bound | Keep Maynard's **proved** criterion and any documented exact rational witness. Move the 600 claim to a clearly *externally sourced/quoted* remark unless its full finite certificate is printed or reproducibly archived and validated. | Do not present an unprinted computational witness as an independently proved bound. |
| Volume 13 Chebotarev | Make the proved Dirichlet-density scope explicit; label natural density as not proved here without the needed analytic input. | No downstream claim may quietly upgrade the density notion. |
| Volume 15 | Keep the printed fourteen-chapter core and its Maier/Selberg synthesis; do not reintroduce the twenty-four unreferenced tour/workshop files by default. | Audit actual proof hypotheses and dependence; the existence of a proof environment is **not** mathematical validation. |

**Decision rule:** These are editorial defaults, not silent manuscript changes. Any choice that relocates chapters or changes catalog strings must be logged with alternatives, affected labels, rollback instructions, and author approval before implementation.

## 2. One auditable source of truth

Before editing prose, generate a baseline inventory from current main:

1. **Print closure:** For every Volume 5–15, recursively resolve main.tex includes and record included vs orphaned chapters, part/chapter order, labels, source hash, and cited volumes.
2. **Catalog:** Verify that all live display titles, subtitles, and part names agree with the canonical series-catalog JSON and generated subtitle files; report old/historical numbers separately.
3. **Prerequisite graph:** Record theorem-level edges as **proved premise**, **motivational preview**, **conditional/quoted input**, or **future discharge**. Only proved premises define the reading-order DAG. A future-discharge annotation, such as Volume 6's bias proposition awaiting Volume 13's Dirichlet functional equation, is **not** an ordinary Volume 13 → 6 prerequisite edge.
4. **Page baseline:** Typeset every *current* book with its production settings before setting page budgets. Report physical interior pages (including appendices/exercises) and, separately, sequential narrative pages. Source lines and October 2026 pages are not current measurements.
5. **Evidence ledger:** Create one record per load-bearing theorem/exercise: volume, chapter, label, precise statement and hypotheses, dependencies, status, proof reviewer evidence, numerical certificate if any, and downstream consumers. Include an explicit status for *quoted*, *conditional*, *sketched*, or *not independently checked*.

**Baseline deliverables:** a machine-readable volume/label/dependency manifest, a human-readable acceptance register, a measured page ledger, and a short drift report comparing each book-05…book-15 specification with main.tex. Preserve an immutable reference to the baseline commit.

## 3. Standards for a publishable theorem

Use **VERIFIED / CORRECTED / QUOTED / CONDITIONAL / SKETCH / BLOCKED / NOT REVIEWED**; never infer VERIFIED from a theorem name, label, compilation, or proof-environment presence.

A theorem reaches VERIFIED only when its statement and domain are checked; all assumptions are available earlier or proved locally; every nontrivial inference in the written proof is independently reproduced or checked; constants and endpoints are justified; cited lemmas support precisely the claimed strength; examples and exercises do not contradict the statement; and a reviewer records what was actually examined. For research-level material, compare to a primary source and audit what was compressed, including uniformities, exceptional cases, and ineffective constants.

For a numerical assertion, require a reproducible computation with source, parameters, precision, verification logic, result hash, and a human-readable mathematical explanation of why that computation proves the claim. A displayed decimal, screenshot, or named paper alone is not a finite certificate.

**Critical proof queue (minimum):**

- Volume 5: functional equation of zeta; Poisson summation; Gauss-sum sign; Hardy–Ramanujan and Waring's future-premise issue.
- Volume 6: Hadamard factorization, zero-free line/region, Newman–PNT, explicit formula, Erdős–Kac and the precise scope of the bias identity.
- Volumes 7–8: extension/conditional expectation/Prokhorov; compact spectral theorem, Wiener–Ikehara's hypotheses.
- Volumes 9–12: Weyl's formula; Peter–Weyl; Donsker and Lyapunov; Ito/Girsanov; Dyson noncollision from distinct initial eigenvalues; sine-kernel limit and moment estimates.
- Volume 13: unique ideal factorization, Hasse–Minkowski/three squares, Chebotarev scope, Tate for Q and its functional-equation corollary, Mordell–Weil.
- Volume 14: Bombieri–Vinogradov's complete chain, Maynard's optimization claim, critical-line claims, RH/range in Montgomery pair correlation.
- Volume 15: Gallagher input and Maier's theorem; Selberg's CLT, twisted moment estimates and exact hypotheses; all “proved” arithmetic-statistics claims used in the final synthesis.

Unit tests, LaTeX builds, reference tests, and plotted numerical examples are **supporting checks**, not substitutes for proof verification. If one agent alone validates, explicitly disclose that limitation; do not imply an external second referee exists.

## 4. Editorial and pedagogical acceptance for every volume

Each volume must have a one-paragraph **question**, a motivated entry from earlier volumes, a short list of **owned flagship theorems**, a clear climax, a truthful handoff, and no requirement to know an unproved future theorem. Advanced excursions may remain if clearly optional, but an asserted *complete proof* must still contain its full prerequisites.

Apply the following chapter-level test to every chapter, not merely to the preface: (a) clear motivation and context; (b) prerequisite box with stable labels, not fragile printed theorem numbers; (c) theorem–proof–worked-example progression; (d) at least one diagnostic example where hypotheses matter; (e) exercises graded from routine to synthesis, with checked solutions/hints; (f) explicit marking of conjectures, external results, and scope limitations; (g) figures only where they materially aid understanding, with truthful captions and accessible descriptions; (h) notation consistent with adjacent volumes; (i) a transition to the next chapter.

**Story continuity:** Track primes, the Gaussian, zeta, random walks, symmetry, the failure of unique factorization, spectral statistics, and the order/chance comparison across volumes. Each major return must add a *new insight*, not silently reproduce a proof. Volumes 7–10 need explicit thematic bridges so the central question does not disappear for four books. Volume 15 must answer the framing question with a distinction between theorems, heuristic models, and open conjectures—not an unsupported philosophical claim.

**Size rule:** Page targets in PR #150 are provisional narrative targets. Do not approve a volume because the narrative falls in a target range if exercises and appendices make the delivered book impractically long. Reconcile trim size, PDF page count, distribution constraints, figures, typography, and reader load from actual generated artifacts. Prefer removing redundancy over shrinking type or suppressing proofs.

## 5. Implementation sequence and hard gates

| Wave | Implementation | Exit gate |
| --- | --- | --- |
| **0 — baseline** | Generate print closure, theorem/label map, dependency types, actual PDFs/page counts, defect register; identify source-of-truth drift. | Every printed chapter classified; no fabricated counts or unlabelled dependency arrows. |
| **1 — bridge** | Volume 5 first; explicitly resolve Hardy–Ramanujan/Waring's Volume 6 dependencies and later internal references; audit zeta and transform proofs. Then audit Volume 6's flagship proofs, avoiding extra topics. | Volume 5 is sequentially teachable; Volume 6 has a proof-by-proof acceptance record for PNT and explicit formula. |
| **2 — foundations** | Validate Volume 7's measure/conditional expectation/Prokhorov. Reorganize Volume 8 so only earlier/local premises support its core; relocate Q_p and random matrices as decided. | Zero untyped **future proved-premise** edges in the Volume 5–8 main path; generated labels and PDFs build. |
| **3 — middle arc** | Check Volume 9's Weyl and geometry signposts; Volume 10's actual Dedekind/Peter–Weyl climax; Volume 11's probability hypotheses and cutoff; Volume 12's matrix return and Dyson caveat. | Volumes 9 and 11 really support Volume 12; no missing prerequisites or unlabelled matrix universality claims. |
| **4 — arithmetic/primes** | Consolidate Volume 13's quadratic path, migrate Q_p analysis, audit Chebotarev/Tate/curves. Audit Volume 14, especially Bombieri–Vinogradov and the Maynard numerical status. | Full proof ledger for every result Volumes 14–15 use; unproved extras honestly marked. |
| **5 — synthesis** | Audit Volume 15's reached files from first page through solutions; independently re-derive Maier and Selberg's argument; fix form-factor cross-references and close the narrative. | Central question answered on proved ground; all unresolved claims labelled; no orphan chapter accidentally included. |
| **6 — production** | Run all book builds, proof/solution regression checks, citation/reference checks, PDF/EPUB validation, print-page inspection, visual review, metadata/cover consistency, and end-to-end series navigation. | A reproducible release-candidate manifest for each volume with artifact hashes, known limitations, acceptance signoff, and no undisclosed blockers. |

Execute changes in small, reviewable PRs after the planning PR, preferably one volume or one cross-volume move per PR. Moves between Volumes 8 and 12 or 8 and 13 must update both endpoints atomically with corresponding citation/label checks. Merge only after scoped acceptance and regression checks. Record why a result is **quoted** rather than forcing a fabricated proof to hit a publication date.

**Critical path:** V5 → V6 → V7/V8 plus V9/V11 → V12 → V13/V14 → V15 → series-wide QA. Many audits can run in parallel, but no volume claims a theorem as already available before its owner has passed the relevant gate.

## 6. Per-volume deliverables

| Volume | Non-negotiable unique outcome | Specific blocker to clear |
| --- | --- | --- |
| 5 — Calculation | Zeta functional equation and usable analytic toolkit | Resolve direct dependence of Hardy–Ramanujan/Waring on Volume 6 and on later Volume 5 chapters |
| 6 — Crossroads | PNT, explicit formula, Erdős–Kac, with scope separated from heuristics | Independently verify compressed major proofs; preserve deferred functional-equation warning |
| 7 — Spaces | Measurable, topological, and conditional-expectation foundations | Confirm all later citations refer to genuinely proved general versions |
| 8 — Analysis | Operators, Fourier/Haar, and Tauberian methods without future premises | Remove relocated sine-kernel/Q_p dependencies; control oversized reprise |
| 9 — Shapes | Geometry and Weyl integration as a bridge | Check proof of Weyl/correlations and keep optional appendices off the prerequisite path |
| 10 — Abstraction | Dedekind and Peter–Weyl as algebraic tools | Correct obsolete shuffle-climax plan; check representation prerequisites |
| 11 — Randomness | Limit theorems, Donsker, ergodicity and transposition cutoff | Ensure correct conditional expectation and Lyapunov hypotheses |
| 12 — Random Motion | Stochastic calculus, Dyson caveat, semicircle and sine kernel | Verify moved proofs, distinct-spectrum scope, and citations to Volumes 9/11 |
| 13 — Arithmetic | One number-field narrative, class-number formula and Tate for Q | Deduplicate quadratic proofs; qualify natural-density Chebotarev |
| 14 — The Primes | Bombieri–Vinogradov and correctly delimited bounded-gaps/pair-correlation results | Validate full BV chain; reclassify or certify numerical witness for 600 |
| 15 — Order and Chance | Maier and Selberg as the meeting, with an honest final conclusion | Independent mathematical audit of both proofs; keep nonprinted tours out |

## 7. Definition of done and reporting

For each volume publish an **acceptance packet** containing: (1) baseline/commit and exact printed file closure; (2) complete flagship-theorem verification ledger and treatment of other claims; (3) exercise/solution coverage and sampled adversarial checks; (4) proof-to-prerequisite graph with zero unresolved forward *proved* edges; (5) notation/citation diff; (6) measured print and digital artifacts with hashes, page count, build logs, and visual QA; (7) editorial assessment of exposition and story; (8) explicit residual risks, quotations and conditions; (9) reviewer identity/method and author decision. A volume is done only when every acceptance gate is met or an exception is documented and approved.

**Truthfulness:** “Draft exists”, “LaTeX compiles”, “has a proof environment”, “passes structural tests”, “mathematically verified”, and “publication ready” are six different states. Keep them separate in PR descriptions, CI results, and release notes.

**Updating the old plan:** After the architectural decisions are accepted, revise SERIES-CONTENT-PLAN.md, book-05.md…book-15.md, and series metadata in their own scope-controlled implementation PR(s). The document in PR #150 is a diagnostic and should not become an accidental second conflicting canonical chapter map.

## 8. Immediate next PRs

1. **V5 forward-premise fix and preflight** — decide the placement of Hardy–Ramanujan and Waring; eliminate unproved Volume 6 premises from any Volume 5 required proof; verify the functional-equation chain.
2. **V6 mathematical acceptance** — independently audit Hadamard, PNT, zero-free results, explicit formula and Erdős–Kac; record conditions and update any overclaims.
3. **V8/V12 move and references** — return the two matrix chapters to Volume 12, change the part title *only after* the move, update cross-volume citations, and rebuild both books.
4. **V8/V13 Q_p move** — relocate local-field Haar/Fourier proofs and exercises after Q_p's construction; verify Tate's normalizations and build.
5. **V13/V14 scope gates** — one quadratic narrative; Chebotarev scope; verify BV and the Maynard numerical assertion before Volume 15 quotes either.
6. **V15 final synthesis** — full proofs and solutions audit, stable theorem links, and an end-to-end reader's route through the fifteen volumes.

Implementation PR descriptions must state **actual changes**, **mathematical evidence**, **tests/builds run**, **known limitations**, and **what remains**. Do not merge a planning document as a substitute for those implementation gates.
