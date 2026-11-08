# Volume 4 coverage restoration and self-review — 8 November 2026

This note records a writer self-check on branch `cursor/volume4-rewrite-ee7f`. It is not an independent second review. The same pass wrote the new proofs and then reread them.

## What was added, and why

Later volumes were citing results the rewritten Volume 4 did not contain. Those results were proved again inside Volume 4, in the finite-partition and digit-model language of the current chapters. Existing printed numbers that later books already matched were not moved: Lindeberg stays Theorem 6.10, Doob stays Theorem 11.9, Azuma stays Theorem 11.10, colouring stays Lemma 10.5, reflection stays Theorem 12.12, and the two-colour three-term progression stays Theorem B.7’s predecessor Theorem B.6.

The characteristic-function fact that distributional convergence passes to characteristic functions is still proved. It is now an unnumbered `theoremx`, so the inversion theorem can be Theorem 6.8.

## What this pass actually re-read

- The new inversion argument: Gaussian integral by differentiation under the integral, smoothing by an independent Box–Muller normal, uniqueness by trapezoidal test functions, and the Cauchy transform read backwards from the Laplace density.
- The extended Doob argument, including the stopped-sum form `λ P(Y* ≥ λ) ≤ E[Y_n 1_{Y* ≥ λ}]` and Ville’s bound for a nonnegative supermartingale.
- The `L^2` proof: orthogonal increments, a summable maximal subsequence with `r_{n_j} ≤ 2^{-4j}`, and the square of the telescoping series via Cauchy–Schwarz. No appeal to an unproved completeness theorem for `L^2`.
- Pólya’s urn: the explicit probability `1/(n+1)`, the martingale check, and the identification of the almost-sure limit by continuous test functions.
- The discrete arcsine package: reflection giving `P(M_n ≥ a) = P(S_n ≥ a) + P(S_n > a)`, the nonnegative-path probability `u_{2m}`, the first-return convolution, Chung–Feller by induction, and the Riemann-sum limit on an interval bounded away from `0` and `1`.
- The central-binomial induction `u_{2m} ≥ 1/(2√m)`.
- Bayer–Diaconis: the descent-boundary count and the stable-sort composition. The distances for 52 cards were recomputed from the Eulerian numbers and the binomial formula; three-decimal rounding gives `1, 1, 1, 1, 0.924, 0.614, 0.334, 0.167, 0.085, 0.043`.
- Untouched-card mean, nonpositive covariance, and the Chebyshev lower bound `1 - 6e^{1-2c}`.
- Van der Waerden by colour focusing, including the focus bound `a+(k-1)d ≤ 2W(k-1,r)`.
- The Brownian hitting density obtained by differentiating `2(1-Φ(a/√t))`, and the divergence of `E[τ_a]` by comparison with `t^{-1/2}`.

## What was not re-proved line by line in this pass

Chapters 1–5, 7, 10, 13 and 14, and the earlier parts of Chapters 6, 8, 9, 11 and 12, were not given a fresh line-by-line hostile reading in this pass. Earlier writer logs on this branch record those passes. They remain writer self-checks. No independent reviewer has signed the book.

The almost-sure `L^1` argument uses an outer-content form of Fatou for bounded truncations. The estimate that a late oscillation sits inside a late upcrossing is the step a second reader should press first.

## Citation edits

Only the citation phrase was changed in Volumes 6–15, and only where the old number was false after the restoration. Volumes 1–3 were not edited. The Volume 3 conceptual snapshot was refreshed because it stores the hash of `volume4-chance/chapters/ch08-markov.tex`. The coupling passage that snapshot was written to guard, formerly lines 170–214, was not rewritten; the file hash changed because the riffle section was added later in the chapter. All 120 prior conceptual statuses were left in place.

## Not claimed

No physical Kindle, Moon+ Reader, or other device was used. A native PDF and EPUB inspection, if recorded with the build, is a screen inspection of the exported files.
