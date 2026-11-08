# Volume 4 — Phase 2 proof-completeness repairs (9 November 2026)

**Baseline main:** 0c097e7a1041cfc647cf79b7dd3e3000a93aeec4 (merged PR #119).
**Implementation branch:** audit/volume4-phase2-gaussian-polya-proof-2026-11-09.

**Status:** Two omissions identified and source-repaired. Both need distinct exact-source mathematical review. This is a focused author/assistant audit, not independent whole-book acceptance.

## Confirmed findings

| ID | Source and stable label | Mathematical problem | Repair and regression | Disposition |
| --- | --- | --- | --- | --- |
| V4-P2-008 / P1 proof incomplete | Printed Chapter 12, volume4-chance/chapters/ch11-brownian.tex, prop:bmgauss | After PR #118's missing-centring fix, the converse showed the covariance but did not explicitly prove joint Gaussianity of the entire observation vector from independent normal increments. One-dimensional normal marginals alone are insufficient. The forward direction likewise needed the common-grid reduction for arbitrary disjoint intervals. | For an ordered grid 0=t0<t1<...<tm, independent centred normal differences Δi make every observation Bt_j a partial sum, hence the entire observation vector a lower-triangular linear image of independent normals: jointly centred Gaussian. Conversely, a jointly Gaussian vector makes successive differences jointly Gaussian; their off-diagonal covariances vanish under the min(s,t) kernel, and Gaussian-vector independence applies. Any finite disjoint intervals use a common endpoint grid. New regression independently checks exact grid and interval covariance arithmetic and the crucial source argument. | SOURCE-FIXED; INDEPENDENT EXACT-BLOB REFEREE PENDING |
| V4-P2-009 / P1 unproved last inference | Printed Chapter 11, volume4-chance/chapters/ch10-martingales.tex, thm:polyaurn | The proof established expectation equality for every continuous test function, then asserted the limit had uniform distribution without deriving the resulting indicator/CDF law inside the book's restricted interval model. | Explicit continuous lower/upper trapezoid cutoffs squeeze the indicator of [0,x]. Their integrals bound P(M∞≤x) by x−η and x+η. Taking η→0 and handling x=0,1 proves the entire CDF. New regression independently checks every finite n≤20 colour-sequence mass, the grid CDF, and cutoff sandwiches at n=128/1024. | SOURCE-FIXED; INDEPENDENT EXACT-BLOB REFEREE PENDING |

## Technical interpretation

The Gaussian proposition still explicitly requires *centred* normal increments. A drift W_t+ct remains a counterexample to any version omitting that assumption. The new argument repairs the joint-Gaussian implication, not the already corrected hypothesis.

In the urn theorem, for 0<x<1 and 0<η<min(x,1−x), the continuous lower cutoff is 1 up to x−η and decreases to 0 at x; the upper cutoff is 1 up to x and decreases to 0 at x+η. Their expectations equal their Riemann integrals, yielding x−η≤P(M∞≤x)≤x+η. At zero the upper one-sided cutoff forces a zero atom, and at one the almost-sure limit remains in [0,1].

## Targeted adjacent source audit (not exhaustive)

Read and checked the actual source passages for Brownian existence, covariance equivalence, quadratic variation, dyadic expansion, restart and reflection; martingale square-mean convergence, Pólya urn and almost-sure convergence; Fourier inversion and Lindeberg; Poisson arrivals/nonexplosion; finite-chain aperiodicity and the probabilistic-method local lemma; and Appendix B exact finite cases. The two identified proof omissions above were the confirmed repairable gaps in this pass. Other unsampled steps and all exact-source independent review remain open. A passage not listed is not represented as checked.

The existing exact Appendix B finite enumerations, figure-data tests, historical proof-structure tests and previous V4-P2-001..007 corrections remain unchanged.

## Verification and release boundary

New tests: tools/test_volume4_math_proof_completion.py (two test cases). They check arithmetic and required proof steps, not a formal proof checker. The full Build books unit suite, native PDF/print/EPUB/reader QA and site workflow must pass at the final PR head before merge. The exact SHA, run IDs, test results, print interior, references and print preflights must be recorded from observed logs, not predicted here.

**Outstanding, not certified:** independent mathematical referee at the final unchanged source blobs for all 14 printed chapters and Appendix B, particularly V4-P2-005..009; all 107 exercise statements/hints/solutions independently checked; all 41 figures visually and mathematically checked in PDF and EPUB; prerequisite and Volumes 5–15 dependency review; whole-book pedagogical review; physical-device/print proof and author release signoff. Historical review blobs sampled in PR #118 do not match the current files. Neither the correcting assistant nor passing CI constitutes an independent mathematical referee.

**Protected content:** Volumes 1–3, chapter order, theorem/exercise labels and Appendix B structure unchanged.
