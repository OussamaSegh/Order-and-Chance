# Volume 4 Phase 2 — live downstream source-truth corrections

**Date:** 9 November 2026. **Mathematics:** author-designated sole validator GPT-6. **Baseline:** main merge commit `6a38fbe797c70181318770b7fd7134651bf78607`, after verified PRs #131–#134. This is a *targeted* audit of specific live downstream citations, **not** a claim that every reference across Volumes 5–15 was checked.

## Confirmed defects, evidence and minimal repairs

| ID | Actual live source | Defect against current printed Volume 4 | Resolution |
| --- | --- | --- | --- |
| DEP-12 | `volume11-randomness/chapters/shuffling.tex` | Intro credits a Broder-style random-transposition upper bound to Volume 4 Chapter 8; the actual Volume 4 Chapter 9 proves a lower bound (Proposition 9.11) and explicitly says the sharp window awaits Volume 11. The exercise cites nonexistent V4 Proposition 8.16. Multiple references misname printed Chapter 8 instead of 9 for shuffled decks. | Correct the introduction and chapter numbers; replace the nonexistent proposition by this chapter's own Fourier eigenvalue proposition and the regular representation identity \(\sum_\lambda(f^\lambda)^2=n!\). Exact bound derivation belongs to this chapter. |
| DEP-13 | `volume7-spaces/chapters/ch08-products.tex` | The text states that Volume 4 imported general Tonelli/Fubini as axiom (A2). Actual Volume 4 restricts the integral constructions to continuous rectangular cases and does not prove/import arbitrary product-measure Tonelli/Fubini. | State precisely the earlier restricted result and mark general Tonelli/Fubini as developed here. |
| DEP-14 | `volume6-crossroads/chapters/ch09-erdoskac.tex` | Exercise solution claims Berry–Esseen was stated in Volume 4, where it is absent; its full theorem and proof occur in live Volume 11 Chapter 4, label `thm:berryesseen`. | Credit Volume 11 Chapter 4; keep the independent arithmetic estimate and claimed source theorem. |
| DEP-15 | `volume11-randomness/chapters/ch08-concentration.tex` | Intro and reminder cite nonexistent Volume 4 Theorem 10.25 as the independent-coordinate bounded-difference inequality. Volume 4 instead proves *Azuma for bounded martingale increments* at Theorem 11.10. | Introduce coordinate revealing and Doob martingale `M_i=E[F|X_1,\ldots,X_i]`, observe `|M_i-M_(i-1)|\le c_i` from coordinatewise oscillation, apply Volume 4 Azuma on both signs to obtain `P(|F-EF|\ge t)\le2e^{-t²/(2Σ c_i²)}`. Justify general conditional expectations from Volume 7. This is an actual derivation, not a relabelled unproved theorem. |
| DEP-16 | `volume12-random-motion/chapters/ch03-martingales.tex` | Full-filtration, general `L²` bounded martingale convergence was attributed to Volume 4 Theorem 11.12, which is proved there **only on finite half-open interval atom partitions** (after PR #124). The same reminder called V4 Brownian quadratic variation valid for unspecified partitions, whereas V4 Theorem 12.7 proves the specified dyadic scheme and final short interval. | Derive the general integer-time convergence locally: `E M_n²` is bounded monotone, `E(M_n−M_m)²=E M_n²−E M_m²` makes `M_n` `L²`-Cauchy; `L²` boundedness gives UI, so Volume 11 Theorem 9.2 yields a.s. convergence and identifies the `L²` limit. Passing martingale expectations to that limit gives `M_n=E(M∞|F_n)`. The established continuous-time maximal bound completes this chapter's remaining argument. State the exact V4 dyadic quadratic variation scope. |


## Further confirmed live-reference defects (same review batch)

| ID | Actual live source | Incorrect attribution | Resolution |
| --- | --- | --- | --- |
| DEP-17 | `volume12-random-motion/chapters/spectral.tex` | Cayley's spanning-tree formula was credited to *Volume 4, Chapter 12*, which is Brownian Motion and contains no Cayley spanning-tree proof. | The current spectral chapter explicitly derives Cayley's formula from the matrix-tree eigenvalues. Credit this derivation, not the unrelated Volume 4 chapter. |
| DEP-18 | `volume6-crossroads/chapters/ch12-modular.tex` | The cross-volume tools note calls V4 Borel–Cantelli `Theorem 4.11`. The actual current source places it at `Theorem 4.4` (proved both first and second forms). | Correct 4.11 to 4.4, retaining Theorem 6.10 for Lindeberg. |
| DEP-19 | `volume15-order-and-chance/chapters/ch11-values.tex` | A complex random-Euler-product martingale uses the *general* probability-filtration `L²` theorem and credited Volume 4, Chapter 11 (where the theorem is proved only on finite half-open interval partitions). | Cite the general-filtration Volume 11 martingale theorem and the orthogonal-increment `L²` Cauchy criterion. |
| DEP-20 | `volume12-random-motion/chapters/ch12-logcorrelated.tex` | Another general `L²`-bounded martingale convergence claim is attributed directly to restricted V4 Theorem 11.12. | Cite Volume 11 Theorem 9.2 for a.s. general-filtration convergence and explain the `L²` upgrade from orthogonality. |


## Additional independent-series proof repair

| ID | Live downstream source | Defect | Correct mathematics |
| --- | --- | --- | --- |
| DEP-21 | `volume11-randomness/chapters/ch01-zero-one.tex`, `prop:l2series` | The proof simply invoked Volume 4 Theorem 11.12 for arbitrary independent mean-zero finite-variance summands, despite that V4 theorem being restricted to finite interval partitions. The reminder also cited obsolete Theorem 10.18. | Prove the full result directly: let `v_N=Σ_(k>N)E X_k²→0`; choose `N_j` with `v_(N_j)≤2^(-4j)`. The finite-tail Kolmogorov maximal inequality yields `P(sup_(m>N_j)|S_m-S_(N_j)|≥2^(-j))≤2^(-2j)` by probability continuity from below. Borel–Cantelli implies pathwise Cauchy convergence; exact increment orthogonality makes the partial sums `L²`-Cauchy and identifies the limit. This does not import the general-filtration L² theorem from Volume 4. |
| DEP-22 | `volume11-randomness/chapters/ch09-martingales.tex` | Two later Gaussian-series proof/hint uses of V4 Theorem 11.12 were similarly out of scope; introduction omitted the finite-partition qualification. | Use newly self-contained Chapter 1 `prop:l2series` for the independent centred Gaussian series with square-summable coefficients; qualify the V4 chapter-level introduction. |

Finite independent-sign maximal-event enumeration is included in the downstream regression file, supplementing the mathematical Kolmogorov/Borel–Cantelli proof and not substituting for it.

## Further exact-number correction

| ID | Live downstream source | Defect | Resolution |
| --- | --- | --- | --- |
| DEP-23 | `volume6-crossroads/chapters/ch10-random.tex`, Hawkins-sieve exercise tools | Invokes **Volume 4 Theorem 4.14** for conditional expectation and Jensen, but printed Volume 4 Chapter 4 has only six numbered proof statements (4.1–4.6). Jensen is proved earlier in Volume 1; finite-history conditional expectation is defined in Volume 4 Definition 11.1. | Correct the reading path to V4 Definition 11.1 for finite-history conditional expectation and Volume 1 for Jensen and harmonic numbers; add regression guarding the actual source and forbidding the imaginary theorem. |

## Verification and invariants

- Tests: `tools/test_volume4_phase2_downstream_source_truth.py` pins each concrete correction, verifies the cited general-filtration theorem actually exists in Volume 11, and independently enumerates small weighted-bit sums to check the bounded-differences tail against an Azuma upper bound. Finite tests are arithmetic corroboration, not unrestricted mathematical proof verification.
- Sources: actual included source files were checked against the `main.tex` inclusion order for Volumes 6, 7, 11 and 12; none of these is merely an unused historical draft.
- Correct *printed* V4 reference counts were checked directly in `volume4-chance/main.tex` and `common/interior-boxes.tex`: Theorem 4.2 Hoeffding, 4.3 Kolmogorov, 4.4 Borel–Cantelli, 4.5 bounded SLLN, 4.6 Weierstrass; 9.6 top-to-random, 9.11 untouched cards; 11.10 Azuma, 11.12 restricted convergence; 12.7 dyadic quadratic variation. The historical migration register includes superseded numbers and is not a source of truth when it contradicts current TeX.
- No changes to Volume 4 maths or published Volumes 1–3. All edits are narrowly scoped downstream unpublished sources and this audit/test evidence.
- **Remaining**: This is an identified-defect batch, not exhaustive signoff of the entire downstream citation graph. Exact-head full Build books and Volume 4 native QA are required before merge; any CI blocked by infrastructure should remain visibly blocked rather than represented as PASS. Production/figure/reader and final author release acceptance remain separate.
