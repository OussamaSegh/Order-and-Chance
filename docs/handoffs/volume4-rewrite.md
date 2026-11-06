# Handoff: Volume 4 rewrite

## Latest checkpoint — 6 November 2026, native PDF of `7078dfe5`

**Preserved.** `f43088ac` is an ancestor. `origin/main` is `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6`. No other volume was edited. PR #111 stays draft.

**Chapter 2 voice, pushed SHA `7078dfe5012f4188fa7b13eebb073806f602f01f`.** Independent subagent composer-2.5, agent `bc-d2380e3f-fe74-5ab0-ac81-fbe223bfd8e8`, read that SHA with `git show` and passed the Sound human test. It reported no mathematical regression in the coupon mean, the record probability, the Poisson quotient, or the birthday bound. The full exercise-by-exercise mathematical recheck remains the one of the file in `34307b91`. The independent-review box stays open. Chapter 2 is not accepted: that box and the whole-book page-by-page certification are still open.

**Native build of that SHA.** GitHub Actions [run 42270414089](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42270414089) ran `./build.sh volume4-chance` and succeeded. Reading PDF `dist/Volume 4 - Chance.pdf`: **158 pages**, 504 × 720 pt, sha256 `cc995193c7302e46cbb08160a7785cc0149a6c97a9e1fec9e0976bf5c01faf2d`. Print interior `dist/kdp/Volume 4 - Chance - Print.pdf`: **157 pages**, 513 × 738 pt, sha256 `2a9edb5fd054616a8f66fd24ac86a8df8047f52ebfe33338a37c9460a0b06a25`. Chapter 2 figure pages of the reading PDF (pages 27 and 30) were inspected: charcoal binomial bars against rust Poisson bars, and the \(1/k\) curve through the cycle bars. Both figure logs wrote a one-page PDF with no error. Page 32 shows the empty-box proposition inside its frame. This is not a high-resolution inspection of all 158 pages. The count is 157 interior pages, still far below 400–500. The older 155-page count was `658af447`.

**Chapter 3.** A different composer-2.5 agent, `bc-4b9198e8-92b4-5e68-9eaa-8562741b5bfc`, read the chapter at `7078dfe5` and found no false statement. It re-read the Dyck sentence and the progeny sentence at pushed SHA `a6fa5066` and called both correct. Voice, native PDF, and chapter acceptance for Chapter 3 stay open.

**C-GROUP.** `Build books` still fails the protected Volume 3 conceptual snapshot. Do not edit Volume 3 or that snapshot.

**Exact next step.** Continue at Chapter 4, `volume4-chance/chapters/ch04-inequalities.tex`, with a full theorem and exercise recompute and a distinct reviewer of the pushed SHA. Do not tick Chapter 2 or Chapter 3 complete.

---

## Previous checkpoint — 6 November 2026, Chapter 2 mathematical review

**Remote reference used before editing.** `origin/main` is `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6` (merge of PR #112, Kindle EPUB cover-page packaging). This branch was `511b694d8be1d3fb6af11324184c62c9ba20e701`. The two histories diverged at `28db77df`. Main's only new files are `docs/DESIGN.md`, `docs/reviews/volume1-kdp-epub-conversion-2026-11-06.md`, and the EPUB check/fix tests. A merge commit brought those in without touching the Volume 4 manuscript and without a conflict. Do not reset this branch to main.

**Chapter 2.** The post-fix author reread at `0e3e99b4` had not closed the mathematical box. A fresh pass of `volume4-chance/chapters/ch02-discrete.tex`, both included figures, and the Volume 1 sources those sentences cite, found three real gaps and then added the occupancy count the depth note asked for. The issue log entries are C2-08 through C2-12. The corrected chapter file is commit `34307b91566186e2a3ed98d45ec3dc7be2c7286e`.

**Distinct reviewer.** Independent subagent, model composer-2.5, agent `bc-d2380e3f-fe74-5ab0-ac81-fbe223bfd8e8`. It is not the writer. It read the chapter at `511b694d` and reported the false birthday bound at \(m=1\) and the missing \(p_n>0\) sentence. After the correction it re-read the whole chapter file in the working tree and reported those defects closed, with no new mathematical defect. It did **not** approve voice, a native PDF, or chapter acceptance. The independent-review checkbox stays **unchecked** until a reviewer signs the pushed SHA as such. Do not treat this recheck as that signature, and do not treat the writer's pass as independent.

**What this pass did not do.** No native `./build.sh volume4-chance` in this session. The last measured interior was 155 pages at `658af447`, before this chapter grew. Voice/reader pass of Chapter 2 is open. Chapters 3–14 and Appendix B are untouched in this session. The protected Volume 3 `C-GROUP` gate is unchanged. No other volume manuscript was edited. PR #111 stays draft.

**Voice edit after `34307b91`.** The reader pass rewrote the record solution, split the coupon-collector paragraph, and replaced two stiff openers. The mathematics is unchanged. Do not call Chapter 2 complete: the voice box waits on a reviewer of the pushed SHA of that edit, and the native PDF of that SHA has not been inspected. The 155-page count at `658af447` is earlier than `34307b91`.

**Exact next step.** Have a distinct reviewer read the pushed voice commit of `ch02-discrete.tex` and record the SHA. Inspect the native PDF of that same SHA, including the two Chapter 2 figures. Only then tick the voice and PDF boxes if they actually pass. Chapter 2 is not accepted while either box is open. After that, review Chapter 3, `volume4-chance/chapters/ch03-generating.tex`.

---

## Previous checkpoint — 6 November 2026, after `f7647627` (routed source expansion)

**Branch:** `cursor/volume4-rewrite-ee7f`, draft PR [#111](https://github.com/OussamaSegh/Order-and-Chance/pull/111). The issue log at `docs/review/volume4-chapter-issue-log.md`, through commit `f7647627b875714bd3776a5296748f26c3689c22`, is the definitive status for the newest mathematical edits. This handoff itself advances the branch SHA; verify the actual PR HEAD before the next edit. No merge, no force-push, no changes to another volume manuscript or reviewer approval.

**Most recent added substance:** Chapter 14 gained three exercises with full worked hints and solutions at `7c273b71`—triangle counts, component susceptibility, and the isolated-vertex threshold. The finite-history conditioning for its breadth-first argument was made explicit at `f7a4b507`. A schematic BFS layer diagram was added at `14e68f00` and integrated at `f5746d1e`; it represents no observed or simulated result and has NOT been visually compiled or verified. Appendix B gained the exact two-colour Schur threshold and complementary-pair Erdős–Ko–Rado extremal constructions, each as an exercise/hint/solution, at `f0738688`.

**Latest static audit after all additions:** **17 routed source files, 206 unique labels (zero duplicates), 166 local references (zero unresolved), 100 exercise statements, 100 matching hints, 100 matching solutions, 12 referenced TikZ figure source files (all 12 confirmed on branch)**. These numbers were recomputed after the Chapter 14 figure integration. The audit cannot establish a valid TeX build, readability, mathematical proof accuracy or a production-page count.

**Latest checked CI:** [GitHub Actions #1838](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42254537363), on `f0738688`: **528 unit tests OK, 31 skipped** and Volume 3 example checks passed, then **`Whole-volume conceptual source/figure drift: C-GROUP`** stopped the workflow. The native book-build, print/KDP, EPUB, site and publishing jobs were skipped. This is the inherited V3 approved-review snapshot including shared `common/cover-notes.json`. **Do not update or remove its manual review approval without separate authorized verification**. Later runs triggered by these new commits must be checked at their own HEAD and may expose additional blockers.

**Acceptance still open:** Current manuscript does not have a verified native PDF/EPUB/print/KDP/wrap, full page-by-page visual inspection, authentic photo/figure licence audit, complete human reader/voice pass, cross-volume migration fixes or 400–500-page production validation. The earlier 131–135-page one-pass XeLaTeX is not valid final evidence. Chapters 7–13 have targeted author corrections but still need a full clean post-fix proof/prerequisite/exercise/hint/solution reread. Chapter 6's finite-cylinder proof and Chapter 1's repaired run proof need adversarial rechecking. Chapter 14 and Appendix B are source-audited, but no independent reviewer has signed exact SHAs for ANY of the fourteen chapters. PR stays **draft and unmerged** until owner acceptance.

**Next practical step:** Recheck and test the new Chapter 14/Appendix exercises and native figures when the toolchain is available, then continue a systematic post-fix audit of Chapters 7–13 with prerequisite tracing; separately arrange an authorized V3 review-snapshot reconciliation to unblock builds. Keep the issue log, handoff, PR body and tests synchronized, and never interpret a skipped build as a pass.

---


## Most recent continuation — 6 November 2026, after `fc79b8fe` (Ch14 and Appendix B)

**Branch/PR:** `cursor/volume4-rewrite-ee7f`, draft [PR #111](https://github.com/OussamaSegh/Order-and-Chance/pull/111), not merged. The latest issue-log commit before this handoff was `fc79b8feac957cabc47daf32687a7a707f6d653a`; this handoff edit creates a newer commit. Always verify GitHub PR HEAD before editing to avoid overwriting later contributions. There has been no force-push or edit to another volume manuscript.

**Latest source edits (on branch, after the older checkpoint below):**

- Chapter 6, post-fix: `45fd45aa` and `9756f205` corrected a CDF atom-bound identity, CLT notation, a Gaussian joint-independence proof, and continuous-event Borel–Cantelli prerequisites. Issue-log entry `16419bd9`. **Especially challenge** the new finite-cylinder proof of outer content; author-level, not independently certified.
- Chapter 7: `edabf981` fixed the Gibbs entropy bound when the actual support is smaller than (m), and the one-symbol empty-codeword convention.
- Chapter 8: `8203834f` supplied the actual ballot/reflection bijection and repaired exercise wording.
- Chapter 9: `86f8cb14` gave the marked-bottom-card strong-stationary proof for top-to-random shuffling, including integer-time mixing.
- Chapter 10: `6d69c517` and `0604f711` added a native **schematic** arrival/thinning timeline in the text. A compiled page has **not** been inspected.
- Chapter 11: `5efbfe9c` closed the stopped-submartingale argument and expanded the bounded pattern-waiting exercise; retained the zero-increment Azuma exception.
- Chapter 12: `99f79545` specified partial dyadic partitions for every fixed time, and justified the entire Gaussian bridge's independence from its endpoint via finite vectors.
- Chapter 13: `a480bca2` justified the existence of primes congruent to (2) mod (3) and the four-endpoint general-position assumption in the crossing argument.
- Chapter 14: `74e94307` rechecked the complete 103-line chapter including both exercise/hint/solution pairs; the subcritical size bound now uses the optimized `a=c-1-ln c=-ln(ce^(1-c))>0` and explicit `e^a n^(1-aA)` decay.
- Appendix B: `0a7f9f3e` rechecked the complete 115-line source, all five theorems and three exercise/hint/solution pairs. Schur's proof now names a finite number-colouring threshold; sunflower induction states (s\ge1,k\ge2) and earns the maximal-disjoint-set count.
- Review evidence: `957bcac7`, `ec621482`, `fc79b8fe` updated the author defect ledger, source inventory and precise coverage language in `docs/review/volume4-chapter-issue-log.md`.

**Coverage precision:** The **Chapter 14 and Appendix B sources** were reread end-to-end at the current branch version. Chapters **7–13** had targeted mathematical/figure rechecks of the listed defects; their *complete* clean theorem-by-theorem and exercise-by-exercise post-fix audit remains OPEN. Chapter 6 author reread was logged, but its new cylinder argument requires an adversarial independent proof check. Chapters 2–5 had earlier source corrections and author rereads, but no native typography or distinct second-review approval. The repaired Chapter 1 infinitely-many-runs proof also remains to recheck. All independent-review gates are PENDING.

**Current static source validation:** Followed `volume4-chance/main.tex` through its fourteen chapters, preface, Appendix B and `about-the-cover.tex` (17 routed TeX files). Exactly **200 labels (no duplicate), 161 local references (zero missing), 95 exercise keys, 95 hints, 95 solutions (complete one-to-one), 11 distinct referenced TikZ figures (all 11 files fetched and present)** at this checkpoint. These figures have **not** been rendered; the checks do not cover cross-volume citations or dynamic TeX.

**CI verified at [run #1829](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42248963841), on `a480bca2`:** 528 Python unit tests OK (31 skipped), Volume 3 example checks PASS, then failed with `Whole-volume conceptual source/figure drift: C-GROUP`. Native book-build/site/publish jobs **skipped**, not passed. This is an intentional prior approved Volume 3 review snapshot including the shared `common/cover-notes.json` changed to rename a Volume 4 chapter. The mechanical regenerated inventory digest was fixed at `d9ff6659`; **do not falsify the separate manually reviewed V3 conceptual snapshot by writing a replacement approval hash**. Its recheck/authorization is a separate dependency. Later runs should be inspected at their own SHA.

**Highest-priority continuation:** (1) Finish a systematic, clean post-fix mathematical/exercise/hint/solution and prerequisite reread of Chapters **7–13** and revisit the **Chapter 6 continuous-event outer-content argument**. (2) Verify Chapter 1’s infinite-runs proof and all 14 chapters' transitions, preface, blurb, final Volume 5 bridge, and source-backed photo/design facts. (3) Obtain actual distinct second reviewers for exact pushed SHAs; record identity, evidence and closure; none are confirmed. (4) Resolve the Volume 3 snapshot integration gate only through separately authorized review, then run repository native `./build.sh volume4-chance`, reading PDF, print/KDP, EPUB and wrap with proper toolchain; visually inspect every page and record hashes. (5) Complete downstream citation migrations with separate authorization where other-volume edits would be required. (6) Address the **400–500-page approved target with real mathematical/teaching depth rather than filler**; there is no valid current production-page count. Keep PR draft and unmerged until all owner gates are truly met.

---


## Newest author-check checkpoint — 6 November 2026, Chapters 2–5 post-fix

**Last pushed issue-log SHA before this handoff:** `ecc1bc582b33b240b1a75107d52b7dc1844d8d31`. The complete SHA of the present handoff commit will be the next branch HEAD; inspect PR #111. This paragraph supersedes the older “next Chapter 3” instruction below.

**Further author-side mathematical work, all pushed:**

- **Chapter 2:** First mathematical/exercise repair sequence `01c85fbb`, `fe2136ce`, then source reread with finite-`N` birthday expectation and rare-trial boundary probes, logged at `0e3e99b4`. No new source flaw identified on reread; two figures still await native PDF inspection.
- **Chapter 3:** Post-fix full source read found endpoint continuity of the pgf unearned and a critical Galton–Watson hint suggesting singular implicit differentiation. Commit `f13c8aeaedc3d3cc4a8094a8b1fa5f4fbc688a0a` adds finite-tail continuity and correct Taylor-limit guidance. The issue log update `6b884a01` records C3-07 and a numeric fixed-point probe. Native family-tree figure not visually verified.
- **Chapter 4:** Post-fix source/exercise read found the longest-run solution's `floor` lower bound did not cover the real-valued event threshold, and the Markov equality exercise conflated fixed-mean and equality constructions. Commit `579a7438c8e9f90548e9bff6b6dcda8c4d2ef9c3` uses a `ceil` lower threshold with disjoint windows and separates the two questions. Issue C4-07 logged at `9b1c2b30`. Native Chernoff diagram not visually verified.
- **Chapter 5:** Post-fix reading corrected missing values of dyadic uniforms at the all-ones exceptional string and missing inverse-CDF value at `U=0`, despite each event having probability zero. Commit `d59b95f6070c63f4d7a48f71d219f851181e6560`, issue C5-08 logged at `ecc1bc58`. Earlier first-pass math and geometric exercises were inspected; **complete post-fix Chapter 5 mathematical/voice/native acceptance is not claimed**.

**Latest inspected CI:** [#1813](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42245333771) (on prior checkpoint `e1a6d934`) completed **failure**. Exactly 528 unit tests ran OK (31 skipped); V3 examples passed, but its protected conceptual snapshot again failed with `Whole-volume conceptual source/figure drift: C-GROUP`. The pipeline skipped reading/print/EPUB/website/publish jobs. New manuscript/handoff commits may trigger later runs with the same blocker. **Do not silently update the accepted V3 conceptual review snapshot to fake a green CI**, and do not modify other volumes. The earlier single generated supporting-source digest update `d9ff6659` is not a review approval.

**Exact next task:** Begin the **post-fix independent-from-previous-draft author critical mathematical/exercise/hint/solution pass of Chapter 6 `ch06-clt.tex`**, with special care for Lindeberg's Gaussian fourth-moment replacement and the explicit `C^3` cutoffs in `cor:clt`. Then continue in order through Chapters 7–14 and Appendix B. Recheck the Ch1 infinite-runs proof; Chapter 2 figure and Chapter 3/4/5 native visual checks remain open. Document every correction in `docs/review/volume4-chapter-issue-log.md` with a commit and exact recheck status. A separate actual second reviewer must still sign each chapter at its exact pushed SHA; **none is present**.

**Still required before acceptance:** all full reader/voice/style, primary-source photo/figure licences and native illustration checks; preface, blurb, V5 transition; downstream citation map and prerequisite audits; resolve the V3 review-snapshot CI dependency with separately authorized review; run the book's real `./build.sh volume4-chance` plus reading PDF/print/KDP/EPUB/wrap, inspect all pages and record hashes; substantively reach the approved 400–500-page target without padding; distinct reviewer acceptance for all fourteen chapters; truthfully tick PR gates and obtain owner acceptance. **No native V4 publication/build/complete chapter certification has occurred**, and PR #111 stays draft/unmerged.

---


## Latest checkpoint — 6 November 2026, after PR #111 CI runs #1807–#1810

**Work branch:** `cursor/volume4-rewrite-ee7f`. Started this continuation from `b8f98bc26885f59fd8061894093be970a11e42e2`. The review-log update `0e3e99b44239383105cdff4b6e513a5fbb1783df` is the latest known pushed commit before writing this checkpoint. This handoff edit adds its own commit; use the PR HEAD shown by GitHub as the final complete SHA. PR remains **draft, open, unmerged**. No force-push or other-volume manuscript edit.

**What has advanced:** First **author-side mathematical inspections** and corrective commits have now reached Chapters **2–14**, plus a Chapter 1 prerequisite repair and Appendix B. Chapters 2–5 are documented in detail in `docs/review/volume4-chapter-issue-log.md`, and Chapters 6–14/Appendix B now have individually traceable defect/commit entries there. Chapter **7 entropy** was materially expanded with a rigorous typical-set count, Kraft converse, block-code explanation, a code-tree diagram and additional fully worked exercises. Chapter 2 received a **post-fix author reread** and numerical birthday-limit tests at `0e3e99b4`.

**Chapter-specific pushed milestones, after the prior checkpoint:**

- Chapter 5: `b09ce014` and `7a70ac01` (bounded-law strong-law prerequisite, inverse quantile model, continuous integral proofs, Cantor exercise).
- Chapter 6: `c86b006f` (false Gaussian truncated-moment bound in Lindeberg, classical CLT test cutoffs, Glivenko–Cantelli prerequisite).
- Chapter 7: `0c61153e` and `a184391c` (prefix tree and expanded source-coding manuscript).
- Chapter 8: `aca08f93` (planar-return counting, Fourier torus second critical point, reflection and first-return formulas).
- Chapter 9: `bf8fa250` (left stationary distribution proof and correctly normalized Doeblin coupling).
- Chapter 10: `8f200c2f` (exact Le Cam Bernoulli/Poisson coupling, continuous-time queue and stationary-bus assumptions).
- Chapter 11: `45ad353c` (word-waiting optional stopping via bounded times, Azuma conditional calculation).
- Chapter 12: `0ed6a684`, `e09011fa` (valid nowhere-differentiability and Brownian time-inversion reasoning, random-time restart, zero-set and p-variation exercises).
- Chapter 13: `6f6bbd4c` (dependency-graph local lemma and exact crossing bound).
- Chapter 14: `4676780b` (uniform exploration-process tail for all subcritical component sizes and edge-probability domain).
- Appendix B: `f2fc8fa0` (Zykov tie case in Turán's theorem and correct circular-arc pairing in Erdős–Ko–Rado).
- Static scan: 203 unique Volume 4 LaTeX labels, 165 local `ref` calls, none missing or duplicated; every declared exercise has a matching hint and solution. This is source-level, **not** a native TeX test.

**Current CI findings — confirmed from GitHub Actions job logs, not inferred:**

1. Run [#1807](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42238510863) at `f2fc8fa0`: 528 Python tests with one error (stale `docs/COVER-NOTES.md`), 31 skipped; native build skipped.
2. Mechanical Vol. 4 cover-name synchronization: `465cb4c4` updated only the Volume 4 chapter title in `docs/COVER-NOTES.md`; `23b908ff` updated the two related generated hashes in `tools/assets/series/manifest.json`. No cover artwork was changed.
3. Run [#1809](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42244018735) at `23b908ff`: **all 528 Python tests OK** (31 skipped); next gate failed because the Volume 3 source inventory includes the hash of shared `common/cover-notes.json`.
4. `d9ff6659` mechanically updated that **one supporting-source digest only** in `review/volume3-internal/inventory.json`; no Volume 3 manuscript or review decision changed.
5. Run [#1810](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42244365867) at `d9ff6659`: **all 528 tests OK** (31 skipped), Volume 3 examples/checker pass, but `review/volume3-internal/check_global_ledgers.py` fails at **`Whole-volume conceptual source/figure drift: C-GROUP`**. Its manually reviewed snapshot includes the shared cover-notes source. This is an intentional evidence gate: **do not change `concepts.json` reviewed snapshot hash or its approval status without a genuinely authorized Volume 3 conceptual recheck**. Build, site and publishing jobs were skipped at this stage. Later checkpoints may rerun and reproduce the blocker; always inspect the new actual run.

**Native build:** There is still no fully mounted repository or working GitHub clone in this runtime; the GitHub connector can read/update files, but does not run `./build.sh`. The CI runner has not reached the V4 native build. No successful native PDF, EPUB, KDP or wrap check occurred in this continuation. The earlier one-pass 131–135-page XeLaTeX output had unresolved references and is **not** a verified reading or production PDF. The approved 400–500-page target remains **unmet and unmeasured on a valid book**; expand substance only, never pad.

**Review status and next action (do not skip):** No distinct second reviewer of any Chapter 1–14 has been identified or submitted an exact-commit report (PR reviewers list was empty). None of the independent-review, complete-chapter, reader/voice, full proofreading, native illustration or production boxes may be checked. Resume **next at the post-fix mathematical/prerequisite/exercise/hint/solution reread of Chapter 3, then Chapter 4, then Chapters 5–14 and Appendix B in print order**. Chapter 2 has already had the post-fix *author* reread documented at `0e3e99b4`; do not waste time starting it from scratch, but inspect its two TikZ figures in a native build. Recheck Chapter 1's infinitely-many-runs repair. Assign a different actual reviewer per chapter, record their identity, exact commit, comments and disposition in the issue log; self-review is not independent.

**Exactly what remains:** (1) Post-fix theorem/proof/example/exercise/hint/solution verification for Chapters 3–14 and Appendix B; further verification of Ch1/Ch2; full prerequisite/downstream citations. (2) Full reader, voice and native figure/photo provenance inspections for all chapters, preface, blurb and closing transition; increase substantive depth to the approved 400–500 pages without padding. (3) Authentic photo licences, creator/provenance and alt-text check. (4) Current migration map and external-volume citations (do not edit other volumes without authorization). (5) **Resolve CI blocker through separate authorized Volume 3 review-snapshot reconciliation**, without falsely transferring approvals; rerun full CI. (6) Native `./build.sh volume4-chance`, reading PDF, print/KDP, EPUB and wrap production, inspect every page, resolve warnings and record artifact paths/hash. (7) Genuine second reviewer of each chapter, logged and signed to exact pushed SHAs. (8) Close all PR checkboxes truthfully, keep PR unmerged until owner acceptance.

The rest of this handoff contains older chronological ledger entries. This checkpoint supersedes their historical “next Chapter 2” and “no Chapters 5–14 inspected” statuses.

---


## Continuation checkpoint — 6 November 2026, after `b8f98bc2`

**Checkpoint source:** GitHub PR #111 HEAD was `b8f98bc26885f59fd8061894093be970a11e42e2` when this continuation began. The branch then advanced with the pushed commits listed below, through the review-log update `fad70e7ed8d3b3248fa37ca8dd4e7493ebc700f2`. This handoff update itself is the final checkpoint commit; run `git rev-parse HEAD` or inspect PR #111 for its complete SHA. No force-push, merge, or out-of-scope volume edit occurred.

**What was actually done:** Full writer inspection of the Chapter 2 manuscript (the Poisson limit, fixed-point Poisson approximation, cycle mean, coupon collector, all eight exercise statements, hints, and solutions), then first author mathematical inspections of Chapters 3 and 4. Several substantive proof and modelling defects were found and repaired. **The independent second-review gate remains PENDING for every chapter. The post-fix critical reread, complete reader/voice passes, mathematical review of Chapters 5–14 and Appendix B, native PDF/EPUB/KDP builds and full-page visual verification are NOT complete.** Chapter 1's prior math self-signoff was challenged by a newly found gap; it requires recheck and distinct review.

**Pushed work, in order:**
- Chapter 2: `01c85fbb` (birthday asymptotic sum-of-squares estimate, Taylor upper bound and incorrect rounding, reservoir sampling, Quicksort); `0ba6e24d` (replace false straight-line figure with the reciprocal curve); `fe2136ce` (construct independent base-`r` coupon draws and correct the Poisson-addition hint).
- Chapter 1 prerequisite repair: `95c84ad2` (the original proof established at least one run, not infinitely many; now takes countable union over the last-run block index).
- Chapter 3: `7bb94ec9` (avoid false claim that an infinite countable product is countable, justify increasing extinction probability by first-extinction series, give finite-partial-sum proof and Poisson-Galton–Watson limit); `3e63117f` (new native tree diagram); `87699c36` (integrate figure and justify Catalan-series convergence).
- Chapter 4: `9cb2451d` (repair Borel–Cantelli's quantifiers and a false infinite-product construction in an exercise; mixed-radix cylinders make independent `1/n` and `1/n²` events exactly; correct scope of finite-digit strong law, degenerate Hoeffding cases, one-sided plot caption and tolerance step).
- Review evidence: `9fca158f` created **`docs/review/volume4-chapter-issue-log.md`**; `fad70e7e` added Chapters 3–4 findings. The log gives stable anchors, severity, resolutions, recheck status and PENDING independent-review entries for all 14 chapters.

**Actual tests in this continuation:** checked numerical identities with local Python (Poisson/binomial bars, Poisson rare-trial probability, `H_{52}`, prisoner survival, Gaussian tail/Chernoff/Hoeffding). The draft source, editor's repairs, and figure formulas were inspected. **No native PDF/EPUB/print build was run**. The GitHub connector can read and write branch files, but the container cannot resolve `github.com` for `git clone`/fetch, and no complete repo checkout or project toolchain is mounted. Prior one-pass 135-page XeLaTeX output is not a production build and not a final page count.

**Exact next step:** On the **latest remote HEAD of this branch**, begin the **post-fix mathematical/prerequisite/exercise/hint/solution recheck of Chapter 2** against `fe2136ce` plus the later commits. Recompute the finite-`N` birthday bounds, review the new base-`r` cylinder argument and examine both Chapter 2 figures in the actual native PDF. Record and fix any new issues. Then repeat the post-fix pass on Chapter 3 (`87699c36`) and Chapter 4 (`9cb2451d`), before continuing the first full mathematical and reader pass at **Chapter 5 — Continuous Chance**. Keep Chapter 1's repaired run proof in the prerequisite recheck. Follow Chapter 5 through Chapter 14 and Appendix B in printed order, one dedicated commit and push per completed writing/review milestone. A distinct independent reviewer must examine exact pushed SHAs of each chapter and log evidence before **any** acceptance box is checked.

**Remaining systemic actions:** finish rewriting/reader/style checks for 5–14 and Appendix B, inspect preface/blurb/ending and V5 bridge, document authentic photograph licence/creator and visual checks, close (or explicitly defer) the out-of-scope downstream citation repairs in `docs/plan/volume4-citation-migration.md`, perform the repository's native `./build.sh volume4-chance` and production checks in a toolchain-equipped checkout, inspect every generated PDF page and actual 400–500-page result, and obtain independent second reviews. Keep PR draft and unmerged; do not edit other volumes to conceal citation drift.

---

Status of this file: **living handoff**. It is updated on the rewrite branch and committed with each milestone. A later agent should resume from this file and the repository, without redoing finished milestones.

## Current contract (6 November 2026)

Fourteen chapters, four parts, as in `docs/plan/book-04.md`. Title page subtitle is **The Logic of Uncertainty**. Branch `cursor/volume4-rewrite-ee7f`, draft PR 111, do not merge, do not force-push, do not edit other volumes.

The twelve-chapter number freeze is withdrawn. Live citations that still use the old numbers are listed in `docs/plan/volume4-citation-migration.md`. That list is an integration gate, not a completed repair.

Restart: read this file, then `volume4-chance/main.tex`, then the migration document. Compile with `./build.sh volume4-chance` from the repository root after the TeX toolchain is present. Do not start a second branch.

## Status

Earlier milestone head `d07a4e33` (superseded by the continuation checkpoint above). The fourteen-chapter skeleton is in `volume4-chance/main.tex`. Title page subtitle is *The Logic of Uncertainty*.

Chapter 1 has a dedicated pushed commit `b267c681` and a mathematical second pass (definitions, ballot proof including `b=0`, digit cylinders, outer content, all eight exercises, hints, and solutions). Voice review of Chapter 1 is not done. No other chapter has a passed second pass. Repair commits, not acceptance: Chapter 2 `4d4c87c9` (Exercise 2.7 index shift), Chapter 3 `ebc3cd9b` (remark moved out of the extinction proof), Chapter 5 angle wording `3ab3ad32`, Chapter 7 exercise environment `62f02af4`, Chapter 8 last-visit identity `966843f6` (Theorem 8.5; the integral arcsine density is not claimed), Chapter 14 subcritical count `d07a4e33`.

One `xelatex -interaction=nonstopmode main.tex` in `volume4-chance` exited 0 and wrote `main.pdf` (131 pages) with undefined references, before the figures added after that pass. That is not `./build.sh`, not a print PDF, and not a page-count verdict. The planning range is **400–500 pages** (owner decision t67u/t68u, 6 November 2026). It replaces 260–290. Do not thin proofs to meet it, and do not pad chapters to meet it.

The owner execution contract is the section `OWNER_APPROVED_V4_CONTRACT` on draft PR 111, outside the agent body markers. Do not replace that section with a run summary. Update its checkboxes and evidence SHAs only when a subgate is actually done. `written` is not `verified`.

## Task and acceptance

Rebuild `volume4-chance/` as a complete replacement of *Chance: The Logic of Uncertainty*. The reader has finished Volumes 1–3 only. The book must be followable at that boundary, including exercises, hints, and solutions. Do not merge.

Acceptance, from the authoring brief:

1. Complete replacement LaTeX manuscript, then the reading PDF and the required production outputs.
2. Updated `docs/plan/book-04.md` and an old-to-new map.
3. Source-backed prerequisite register. Every missing dependency is taught in this volume before use, or kept off the logical path.
4. Exercises, hints, solutions, examples, and figures checked, with uncertainties named.
5. Change summary, source commit, artifact hashes, and the commands that actually ran.
6. One focused unmerged PR.
7. This handoff, current on the remote branch.

The work is **not** complete while any of those is still open. An outline is not the book.

## Canonical instructions

Read these before editing prose or mathematics:

- `docs/agents/mathematician-writer.md`
- `docs/WRITING-STYLE.md` (including Sound human, and the prerequisite contract)
- `AGENTS.md`
- `docs/design/interior.md` (design 5e; caption style stays as it is)
- `docs/SERIES-STRUCTURE.md`
- `common/series-catalog.json` (Volume 4 title *Chance*, subtitle *The Logic of Uncertainty*)
- `docs/plan/book-04.md` (rewritten with this project)
- `docs/plan/volume4-prerequisites.md`
- `docs/plan/volume4-old-to-new.md`
- `docs/plan/volume-citation-map.md` (later books cite Volume 4 by chapter and exercise **number**)

Do not invent a second style guide. First-edition copy: reader-facing text does not describe the book as a revision. No notebooks.

## Branch, base, PR

- Branch: `cursor/volume4-rewrite-ee7f`
- Base: `origin/main` at `28db77df` (the commit this branch was cut from).
- PR: draft, https://github.com/OussamaSegh/Order-and-Chance/pull/111 — do not merge.
- Do not force-push. Do not rewrite pushed history.

## How to resume

1. Check out `cursor/volume4-rewrite-ee7f` and pull it. Do not restart from `main` and do not re-audit finished chapters.
2. Read this file, then the prerequisite register and the old-to-new map.
3. Continue at **Exact next actions**. Do not rewrite a file whose ledger row says `written` unless a named defect says to.
4. After each coherent chapter or audit milestone: update this file, commit, and push the branch.
5. Before a long build, and before stopping, update this file and push.

## Ledger

Legend: `planned` means designed and not yet the manuscript. `written` means a fresh manuscript file is in the tree. `verified` means a human-style mathematical read of that file has been recorded, not merely that a compiler succeeded. A build passing is not mathematical verification.

| Item | State | Notes |
| --- | --- | --- |
| Instruction inventory | verified | Writer brief, style, series structure, design 5e, catalog, old book plan, Volume 1–3 actual theorems cited below |
| Prerequisite register | written | `docs/plan/volume4-prerequisites.md` |
| Old-to-new map | written | `docs/plan/volume4-old-to-new.md` |
| Content plan `docs/plan/book-04.md` | written | Replaces the keep-and-admit-measure plan |
| Preface | written | Not second-passed |
| Ch. 1 From Games to Probability Spaces | prior self-pass; repair pending recheck | `b267c681` earlier self-pass, `95c84ad2` fixes the infinitely-many-runs quantifier gap. Independent and voice review pending. |
| Ch. 2 Random Variables and Their Laws | author inspection + repairs, not independently verified | `4d4c87c9`, `01c85fbb`, `0ba6e24d`, `fe2136ce`; post-fix critical and native figure passes pending. |
| Ch. 3 Generating Functions and Random Families | author inspection + repairs | `ebc3cd9b`, `7bb94ec9`, `3e63117f` (figure), `87699c36`; post-fix review pending. |
| Ch. 4 Concentration and the Laws of Large Numbers | author inspection + repairs | Entropy removed to Chapter 7; `9cb2451d` repairs Borel–Cantelli and exercise model. Post-fix review pending. |
| Ch. 5 Continuous Chance | repair only | `3ab3ad32` fixes the Buffon angle to \([0,\pi]\). Bertrand and Buffon are in `ch05-geometric.tex`. Not second-passed |
| Ch. 6 Why the Bell Curve Appears | drafted | Lindeberg still the tenth numbered environment (Theorem 6.10). Not second-passed |
| Ch. 7 Entropy, Codes and Typical Sequences | repair only | `62f02af4` restores the exercise environment. Kraft and Shannon coding are drafted. Not second-passed |
| Ch. 8 Random Walks | repair only | `966843f6` adds Theorem 8.5, the exact last-visit identity. Integral arcsine law not claimed. Not second-passed |
| Ch. 9 Markov Chains and Mixing | drafted | Not second-passed |
| Ch. 10 The Poisson Clock | drafted | Colouring lemma is the fifth numbered environment (Lemma 10.5). Not second-passed |
| Ch. 11 Martingales and Fair Games | drafted | Not second-passed |
| Ch. 12 Brownian Motion | drafted | Existence is environment 4 (Theorem 12.4); reflection is environment 12 (Theorem 12.12). Not second-passed |
| Ch. 13 The Probabilistic Method | drafted | Crossing lemma is the fourth exercise (Exercise 13.4). Not second-passed |
| Ch. 14 Random Graphs and the Search for Structure | repair only | `d07a4e33` replaces the path count by isolated trees. Giant-component exercise claims a positive lower bound for one vertex, not a high-probability giant. Not second-passed |
| Appendix B Extremal and Ramsey | drafted | Counter still starts at 1 so the appendix prints as B. Not second-passed |
| Gilmer section | removed from the book | Not included. The file `gilmer.tex` remains unused |
| Workshop `pb:*` problems | removed from the logical path | Not cited outside this volume |
| Exercises, hints, solutions | written | Interface numbers checked by order in each chapter file |
| Figures | written | New TikZ plates for Chapters 1, 2, 4, 5, 6 |
| Voice pass | not started | Next, after a compile |
| Reader pass (Volumes 1–3 only) | partial | Mean-one extinction in Chapter 3 replaced by the series expansion. Exercise 2.7 still to be re-read against the built book |
| Build | not started | |

## Last completed milestone

**Chapter 1 mathematical second pass**, commit `b267c681`, pushed. The pass recomputed the ballot count (including `b=0`), the cylinder probabilities, the eight exercise solutions, and `365\ln 2=252.9987\ldots`. It did not review the TikZ of `figures/ch01-ballot.tex` as a drawing, and it did not sign the voice box.

## Current WIP

Chapter 2's first author mathematical read has identified and repaired errors, and the Chapter 3–4 first author inspections have been added. The precise next unfinished step is the **post-fix mathematical critical pass** of Chapter 2, then Chapters 3 and 4; next untouched chapter is **5 — Continuous Chance**. Do not mark chapters accepted because of repair commits, figure additions, or writer self-inspection. The log in `docs/review/volume4-chapter-issue-log.md` is now the anchor for findings. Independent review of every chapter is pending: no distinct reviewer has reported.

## Decisions already made

1. **Foundation.** Volume 1 already proves finite probability, countable nonnegative sums, geometric and Poisson masses, Markov, Chebyshev, the weak law, inclusion–exclusion, Catalan paths as a counting exercise, Stirling with constant \(\sqrt{2\pi}\), the Gaussian integral, one-variable calculus, Jensen, Cauchy–Schwarz, and the spectral theorem for real symmetric matrices (`thm:spectral`). Volume 4 cites these and does not pretend they were not taught. It does not lean on Volume 3’s Perron appendix; finite Markov chains are done by averaging and coupling.
2. **No silent measure theory.** Lebesgue measure on \(\mathbb R^d\), a general Fubini–Tonelli theorem, and an unconstructed infinite product are not used as proof steps. Infinite sequences of fair bits are built from the binary digits of one uniform on \([0,1]\), with probabilities of finite-bit events equal to lengths of intervals. Almost-sure statements are outer-content zero. Iterated integrals are proved for continuous functions on rectangles. A dominated-convergence theorem is proved for continuous integrands. Volume 5 already proves the continuous form it uses and only *mentions* a Lebesgue theorem in Volume 4; that mention will become slightly stale and is recorded under blockers. Volume 7 still constructs the general theory.
3. **Fourteen chapters.** The owner plan of 6 November 2026 replaced the twelve-chapter number freeze. The map of live citations that now point at the wrong number is `docs/plan/volume4-citation-migration.md`. Do not edit other volumes to hide those lines. Do not revert to twelve chapters.
4. **Numbers that are still true, and numbers that moved.** Lindeberg is still Theorem 6.10. Do not insert a numbered environment before it. Colouring is Lemma 10.5. Brownian existence is Theorem 12.4 and reflection is Theorem 12.12. Crossing is Exercise 13.4. Last visit is Theorem 8.5. `examplex` and `definitionx` do not use the shared counter. Inversion, the seven-shuffle profile, and van der Waerden are not theorems of this manuscript.
5. **Workshop problems `pb:*`.** They leave the reader’s path. Many of their old solutions use Fourier analysis, representation theory, or later-volume inequalities. They are not cited from other volumes. Techniques that belong to this book (moment method, Hoeffding, ballot, coupon collector, electrical networks for reversible walks) stay in the main exercises.
6. **Cover.** Do not redesign the Galton cover. About the Cover stays accurate if Chapter 6 is still the central limit theorem.
7. **Volumes 1–3 are immutable.** Do not edit them to make an audit pass.

## Unresolved

- Volume 5, `chapters/ch04-integrals.tex`, says Volume 4, Chapter 5 proved dominated convergence for the Lebesgue integral. After the rewrite, Chapter 5 proves it for continuous functions and names the boundary. The Volume 5 sentence is then historically stale. Do not edit Volume 5 unless a later instruction allows a one-line citation repair.
- Volume 7 says it discharges an “admitted fact (A1)” of the old Chapter 5. The new Chapter 5 constructs countable products of uniforms from one uniform, so that particular admission is no longer needed. Volume 7’s sentence is a pointer, not a false theorem.
- Exercise 11.3 in later citations uses the zero set of Brownian motion and a Fubini/Tonelli sentence. The new solution must prove Lebesgue measure of the zero set is almost surely zero using only the integral theorems proved in this volume, and must say so without calling the tool Tonelli if Tonelli is not proved.
- Gilmer’s frequency bound \((1-\ln 2)/2\) is a numerical value of that expression. The comparison is not proved in this volume, and `gilmer.tex` is not included.
- Downstream citation repairs are listed in `docs/plan/volume4-citation-migration.md`. Editing those other volumes needs an explicit instruction. The PR checklist was not patched in this turn: `update_pr` replaces the whole description and would move or drop the owner contract that sits outside the agent markers. The evidence to record, when a line-level edit is safe, is Chapter 1 written and math-checked at `b267c681`; title page checked in `main.tex`; repair SHAs `4d4c87c9`, `ebc3cd9b`, `3ab3ad32`, `62f02af4`, `966843f6`, `d07a4e33` with those boxes left open.

## Exact next actions

1. Finish **post-fix** Chapter 2 mathematical/exercise/figure reread, then complete the same gate for Chapters 3 and 4. Begin the uninspected chapter sequence at Chapter 5. Push each coherent chapter or fix milestone; do not repeat completed repairs. A repair commit does not check the mathematical box.
2. On the PR, edit evidence SHAs inside `OWNER_APPROVED_V4_CONTRACT` only. Do not delete or rewrite that section. Transient status goes inside the `CURSOR_AGENT_PR_BODY` markers.
3. After the manuscript passes are further along, run `./build.sh volume4-chance` from the repository root. Record the command, the exit code, and the page count. Do not call that an all-volume CI run. The planning range is 400–500 pages. Do not delete flagship proofs, and do not add filler, to land inside it.

## Independent review

Owner rule t71u, 6 November 2026. Each chapter needs a second reviewer who is not the writer. The writer's own reconstruction and critical re-read are self-checks. They are never an independent review, and they never check the independent-review box.

An independent-review record must name the reviewer, the pushed commit that was read, the date, the scope, and a log of findings with file, section, theorem or exercise, severity, fix commit, and what is still open. If no distinct reviewer has done that work, the gate stays **pending**. Do not invent a signoff. A chapter with an open mathematical or prerequisite defect is not accepted.

| Chapter | Writer self-check | Independent review |
| --- | --- | --- |
| 1 | Mathematical self-pass recorded at `b267c681` by the writing agent on 6 November 2026. Voice not done. The digit figure in `e76c6a8c` is not part of that pass. | **Pending.** No distinct reviewer. |
| 2–14, preface, appendix | Writer inspected and repaired Ch. 2–4 in this continuation, but post-fix critical passes remain open. Other chapters not second-passed. Earlier figure commits: Chapter 2 `3661489e`, Chapter 6 photograph `020a41b3`, Chapter 8 reflection `6bc1f755`; Chapter 3 tree `3e63117f`. | **Pending.** No distinct reviewer. |

No independent-review report exists. Nothing in this book has been accepted under t71u.

## Tests and builds actually run

- `xelatex -interaction=nonstopmode main.tex` in `volume4-chance`, log `/tmp/v4-xelatex-2.log`, exit 0, `main.pdf` 131 pages, undefined references (one pass). Not `./build.sh`. The PDF was not committed.
- A later pass, log `/tmp/v4-xelatex-3.log`, exit 0, 135 pages, still with undefined references. It includes the digit diagram, the computed binomial/Poisson bars, the reflection step, and the Galton-board photograph. Not `./build.sh`. Still far below 400 pages because the manuscript is unfinished, not because proofs were cut.
- Python: `22/365 = 0.0602739\ldots`, `365\ln 2 = 252.99872\ldots`, so `253/365>\ln 2` and `\exp(-253/365)<1/2`.

Earlier session checks, not re-run as a book test:

- \(\sum_{k=600}^{1000}\binom{1000}{k}/2^{1000} \approx 1.364\times 10^{-10}\) (log-gamma summation).
- Chernoff information bound at the same point: \(\exp(-1000 D(0.6\|0.5)) \approx 1.800\times 10^{-9}\), with \(D(0.6\|0.5)\approx 0.02014\).
- Hoeffding’s \(\exp(-20)\approx 2.061\times 10^{-9}\).
- \(H_{52}\approx 4.538\). \(1-(H_{100}-H_{50})\approx 0.3118\).
- \((1-\ln 2)/2 \approx 0.1534\).

## Artifacts

Uncommitted local `volume4-chance/main.pdf`, 131 pages, from the single XeLaTeX pass above. Not a release file. Production targets remain `dist/volume4-chance.pdf`, `dist/kdp/volume4-chance-print.pdf`, the EPUB, and the wrap, from `./build.sh volume4-chance`.

## Remaining validation

Everything in the ledger marked `planned` or `written` but not `verified`. Independent mathematical reading, layout, and the production build are all still open.
