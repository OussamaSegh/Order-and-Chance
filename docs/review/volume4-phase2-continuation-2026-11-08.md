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

The earlier eight focused Phase 1/Phase 2 regression methods remain. `tools/test_volume4_route.py` still checks the four parts, fourteen printed chapters, Appendix B, labels/references, 107 exercise-hint-solution triples and 41 figure source paths. Those are **structural checks**, not proofs that the individual solutions or drawn figures are mathematically correct.

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

## Merge/release gates and scope

- Preserve published Volumes 1–3, unchanged part/chapter/Appendix B ordering, stable labels, the cover and native styling.
- Verify the native and protected full-build workflows **on the final exact PR SHA**, including all 11 focused mathematical tests after this addition and 5 route tests. Record observed (not assumed) results and artifact digest in the PR.
- **Independent mathematical referee review remains required for the new P0/P1 findings and for the 14 chapters/Appendix B.** The author/writer's source read cannot fill that role, even if every regression test is green.
- An exercise's matching label and a figure's existence do **not** certify its answer or its geometry. An independent proof review of all 107 exercise solutions and visual inspection of all 41 figures is still uncompleted.
- The Volume 4 roadmap register's wider reader, prerequisites, Volumes 5–15 downstream reference, source/figure provenance and production signoffs are separately open. Do not call Phase 2 complete or Volume 4 mathematically accepted based on this focused implementation.
- A PR containing the corrections may be considered for integration as a narrowly scoped hotfix **after code review and required CI**, as PR #117 was, but it must not be labelled complete Phase 2 acceptance.

## Release decision

**Phase 2 mathematical acceptance: BLOCKED / AWAITING INDEPENDENT REVIEW.** There is no evidence to promote any unreviewed whole-book chapter or all-exercise/figure gate to `PASS`. The new false theorem has been repaired in source; the corrected theorem itself still needs external independent signoff on its final blob.
