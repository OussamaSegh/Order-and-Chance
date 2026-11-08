# Volume 4 — Phase 2 continuation: Gaussian centring, independent blocks, and nonexplosion

**Date:** 8 November 2026. **Base:** `main` `8f559f6c03e21adbb1a2eddb7f34a46e17adfb3a`, containing merged Phase 2 focused correction PR #117. **Implementation branch:** `audit/volume4-phase2-completion-review-2026-11-08`.

**Status: new source-level corrections; NOT completed Phase 2 acceptance.** This audit is carried out by the correcting assistant. It is not a second independent referee, external reviewer, production-device inspection, or approval for publication. The separate Phase 2 partial ledger in `docs/review/volume4-phase2-proof-audit-2026-11-08.md` remains authoritative for the previously audited scope and residual work. PR #115's plan and acceptance register still need to be reconciled with these exact source revisions.

## Newly verified findings

| ID and severity | Exact target | Counterexample or missing implication | Disposition |
| --- | --- | --- | --- |
| **V4-P2-005 / P0** | Printed Ch. 12 `ch11-brownian.tex`, `prop:bmgauss` (covariance equivalence) | The theorem asserted that independent **normal increments with variances** `t-s` imply **centred** Gaussian finite-dimensional distributions. This is **false**: for a Brownian motion `W` and `c ≠ 0`, `X_t=W_t+ct` has continuous paths, independent normal increments, increment variance `t-s`, and covariance `min(s,t)`, but `E[X_t]=ct≠0`. Variances and covariances do not specify the means. | **Source-corrected:** require *centred* normal increments `B_t-B_s ~ N(0,t-s)`. Explain the drift counterexample in the chapter. The proof's converse already relies on centred increments and is valid with the corrected hypothesis. **Independent exact-head rereview pending.** |
| **V4-P2-006 / P1** | Printed Ch. 12 `ch11-brownian.tex`, extension from `[0,1]` to `[0,∞)` immediately after `thm:levy` | The original sentence claimed that increments on disjoint time intervals "use disjoint blocks." This is false for two disjoint intervals inside the same unit-time copy. Independence of *uniform blocks* only handles different copies. | **Source-corrected:** split finite disjoint intervals at integer boundaries. Within a copy, independence is already proved for disjoint Brownian increments; between distinct copies, independence follows from disjoint uniform streams. Combining these gives joint independence of all disjoint full-line increments. **Independent exact-head rereview pending.** |
| **V4-P2-007 / P1** | Printed Ch. 10 `ch09-poisson.tex`, paragraph after `def:pp`, citing `thm:uniform` | The proof showed that `N(t)` is finite a.s. **for each fixed `t`** and immediately concluded `T_n→∞` a.s. The conclusion needs one common probability-one event for unbounded time. | **Source-corrected:** intersect the probability-one finite-count events at positive integer times. If `T_n` did not tend to infinity, infinitely many arrivals would occur by some integer time, contradicting that intersection. No general unproved uncountable intersection is needed. **Independent exact-head rereview pending.** |

The Gaussian counterexample can be independently checked with finite-dimensional arithmetic: for `X_t=W_t+ct`, `E[X_sX_t]=min(s,t)+c²st`; subtracting `E[X_s]E[X_t]=c²st` gives the same covariance `min(s,t)`, while `E[X_t]=ct`. In particular the previously stated covariance **and the correct increment variances are insufficient without zero means**.

## Regression coverage added

`tools/test_volume4_math_audit.py` now checks:

1. `prop:bmgauss` requires centred increments and explicitly names `N(0,t-s)`, with a drift counterexample and finite-dimensional covariance arithmetic.
2. The full-time Brownian extension explicitly distinguishes increments inside one unit copy from increments in distinct independent copies.
3. Poisson nonexplosion invokes the countable intersection over positive integer observation times.

The earlier eight focused Phase 1/Phase 2 regression methods remain, and `tools/test_volume4_proof_structure.py` now checks that all **127 previously indexed proof-bearing statements** across the sixteen included chapter/Appendix TeX sources have an adjacent nonempty `proof` environment before the next statement or section. This is a **structural-only** assertion and cannot identify missing logical steps, incorrect examples or false conclusions. `tools/test_volume4_route.py` still checks the four parts, fourteen printed chapters, Appendix B, labels/references, 107 exercise-hint-solution triples and 41 figure source paths. Those are **structural checks**, not proofs that the individual solutions or drawn figures are mathematically correct.

## Focused additional source rereads, not falsely marked complete

Following PR #117 I re-opened source sections and relevant exercises in the current `main` versions of:

- Printed **Ch. 1**: eight exercise statements, hints and worked solutions; including the birthday/conditioning/ballot and Monty Hall counts.
- Printed **Ch. 3**: Galton–Watson generating-function fixed-point, supercritical and critical boundary cases, and sample cobweb arithmetic.
- Printed **Ch. 5**: independent digit-stream construction, ordered uniforms, inverse CDF and bounded quantile approximation.
- Printed **Ch. 8**: Pólya Fourier estimate, first-return and discrete arcsine identities, and local-binomial limit.
- Printed **Ch. 10**: Poisson arrival-count, finite fourth moment, thinning, queues and selected stopping-time arguments; the new nonexplosion gap above.
- Printed **Ch. 11**: conditional expectation on finite partitions, optional stopping, Doob/Azuma, gambler pattern waiting, urns, square-mean and a.s. convergence.
- Printed **Ch. 12**: dyadic Lévy construction, variance/covariance equivalence, scaling/inversion, quadratic variation, finite observation, hitting/restart and reflection; the two new issues above.
- Printed **Ch. 13**: alteration, local lemma, second moment, planar crossing estimates and some explanatory numerical examples.
- Printed **Ch. 14**: subcritical component exploration, triangle second moments and six detailed worked solutions, including the supercritical finite-size lower bound.
- **Appendix B**: Turán, finite Ramsey, Schur, sunflower, Erdős–Ko–Rado, two-colour 3-AP and general van der Waerden constructions, plus example statements.

These were **targeted checks**, and some readings used the pre-fix `main` blob rather than the eventual final PR commit. They are recorded as research coverage, not independent, exhaustive, exact-final-commit signoff. Other printed chapters and material not described here retain their statuses in the previous Phase 2 ledger.

Selected TikZ source/caption comparisons included Brownian reflection, Pólya urn simulations, subcritical exploration, and Ramsey colouring. Source-level inspection does **not** replace page-by-page PDF and EPUB image inspection; no all-41-figures visual signoff is asserted.

## Historical independent-review source-identity check

The older `docs/review/volume4-chapter-issue-log.md` records separate Grok-4.7 mathematical rereads at prior commits, but the exact chapter bytes may have changed since then. On the current branch, a GitHub blob-SHA comparison against the historical reviewed refs gave:

| Historical printed location | Prior reviewed ref | Historical source blob | Current source blob | Exact identity? |
| --- | --- | --- | --- | --- |
| Ch. 3, generating | `12ac5f42` | `dd9635c3b8e62709bdd8b2bf2aa66637814f7619` | `10c1ebdc486ca82ec335654bbacc8cfa6ad0ae76` | No |
| Ch. 5, continuous | `3558c741` | `8d56ff5bd132854ed7e4ed19eca3745be26edf26` | `4d2221df7adeb926d46c7526faa7829a77645db9` | No |
| Ch. 5, geometric include | `3558c741` | `dfdec38d92a38231d1725723b85964f895d2809f` | `2bc6858a1cb598473be2f233ae5ed6b05ff0e93e` | No |
| Ch. 7, entropy | `26cb0760` | `19001aeab88b64ce0c169700f91288aa94a05e85` | `25330e7046f0b585bef9ebffb1408bc907c109df` | No |
| Ch. 8, walks | `52f0b87f` | `5207c3054ab613cab740118f083b4076f6d5a1ea` | `8b64abc66f79ccbc792906fbfa9ba50e9ab3e890` | No |
| Ch. 10, Poisson | `52f0b87f` | `c127a763657c7ff9989d8325aecbaa7e859134a2` | `6de4e7e1fd5c6369d553e45190e54807c553a743` | No |
| Ch. 11, martingales | `541f0273` | `771a9686c9ed876c333e78c76e92b60b54f4fb96` | `200c6c79d56493bde6e1433719181df94f96b66b` | No |

These are comparisons of **actual GitHub file blobs**, not of approximate dates or chapter titles. A changed blob does not prove the old mathematics is now wrong; it means an old exact-source signoff cannot simply be transferred to the current PR without reviewing the intervening diff and checking premise dependencies. This is one reason the independent Phase 2 exit remains genuinely unresolved.

## Merge/release gates and scope

- Preserve published Volumes 1–3, unchanged part/chapter/Appendix B ordering, stable labels, the cover and native styling.
- Verify the native and protected full-build workflows **on the final exact PR SHA**, including all 11 focused mathematical tests after this addition and 5 route tests. Record observed (not assumed) results and artifact digest in the PR.
- **Independent mathematical referee review remains required for the new P0/P1 findings and for the 14 chapters/Appendix B.** The author/writer's source read cannot fill that role, even if every regression test is green.
- An exercise's matching label and a figure's existence do **not** certify its answer or its geometry. An independent proof review of all 107 exercise solutions and visual inspection of all 41 figures is still uncompleted.
- The Volume 4 roadmap register's wider reader, prerequisites, Volumes 5–15 downstream reference, source/figure provenance and production signoffs are separately open. Do not call Phase 2 complete or Volume 4 mathematically accepted based on this focused implementation.
- A PR containing the corrections may be considered for integration as a narrowly scoped hotfix **after code review and required CI**, as PR #117 was, but it must not be labelled complete Phase 2 acceptance.

## Release decision

**Phase 2 mathematical acceptance: BLOCKED / AWAITING INDEPENDENT REVIEW.** There is no evidence to promote any unreviewed whole-book chapter or all-exercise/figure gate to `PASS`. The new false theorem has been repaired in source; the corrected theorem itself still needs external independent signoff on its final blob.
