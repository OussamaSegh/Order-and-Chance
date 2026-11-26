# Volume 1 round-3 fix, second review — 26 November 2026

Independent reading of the Volume 1 fix at `6701f05ecb5e45c9c174b7d8111d420eb44cae39`, on `cursor/fix-v1-round3-3de4`, based on `main` at `68261d60`. The first commit was `8c4c3881`. The corrections below are the later commit. The reader of this note did not write the first commit.

## Verdicts

**Correctness.** The first commit left four defects, listed below. After `6701f05e`, each of `V1-R3-001` through `V1-R3-019` is fixed in the sentence the round-3 log named, and the repair uses only a result already proved before that sentence. The second reading of the correction commit closed all four defects and found no new false step.

**Dropped or weakened proofs.** No numbered proof was shortened. The binomial identity for `(X^3-X)/6` remains the first proof that the polynomial is integer-valued. The division argument is an additional proof of the same conclusion. The name `L_n` was removed from the Fibonacci solution; the identity `F_{2n}=F_n(F_{n+1}+F_{n-1})` is unchanged. The beauty note now counts coprime pairs instead of speaking of equal chances. That is the change `V1-R3-011` asked for.

**Labels.** Compared with `68261d60`, the TeX files under `volume1-first-principles/` have the same `\label` names. No numbered environment was added or removed. The bisection figure file is byte-for-byte the file at `68261d60`. Its environment now follows the sentence that produces positive square roots. The caption text is unchanged.

**Caption and diagram typography.** No font, weight, colour, or coordinate in a plate changed.

**Voice.** The new sentences name the object and the step. The banned fillers do not appear in the diff.

## Findings, closed in `6701f05e`

| ID | Location | Problem | Fix |
| --- | --- | --- | --- |
| SR-001 | `ch02-counting.tex`, solution of `ex:catalan` (c) | The point before the return was given as `y=x-1` before the return step was shown to be north. The shift was said to send the region `y<x` to `y\le x`, which fails off the lattice. | An east step onto `(k+1,k+1)` would start at `(k,k+1)`, where `y=x+1`. The coordinates are integers, so `y<x` means `y\le x-1`, and the shift sends those points into `y\le x`. |
| SR-002 | `ch05-sequences-series.tex`, solution of `ex:nested` | The sentence put the cosine value in `(0,\pi/2)`. The absolute value needs the angle there. | The angle `\pi/2^{n+2}` lies in `(0,\pi/2)`, and the zero argument before `prop:sincmp` gives `\cos>0` on `[0,\pi/2)`. |
| SR-003 | `ch05-sequences-series.tex`, solution of `ex:condensation` | A non-decreasing logarithm was treated as a non-decreasing denominator. The condensed sequence `v_k` was still only asserted to be monotone. | The exponential, already proved strictly increasing, carries the logarithm to the denominator. The derivative of the logarithm of the denominator of `v_k` is positive for large `k`. |
| SR-004 | `ch06-integrals-taylor.tex`, solution of `ex:xnex` | `\ln u\le u` does not give `(\ln A)/A\to 0`. The comparison `\exp y<\delta` did not name `\exp(\ln\delta)=\delta`. | The sequences chapter gives `\ln u\le u-1`, hence `\ln A\le 4A^{1/4}` and `(\ln A)/A\le 4A^{-3/4}\to 0`, as in the proof of `prop:gammafn`. |

## Issue-by-issue

| ID | Where the repair sits |
| --- | --- |
| V1-R3-001 | `ch01-sums.tex`, the prime-factor example. A positive divisor and its positive cofactor both lie in `\{2,\ldots,n-1\}`. |
| V1-R3-002 | `ch01-sums.tex`, the odd block. Chapter 0 writes `k` even or odd, and in each case `k(k-1)` has a factor `2`. |
| V1-R3-003 | `ch01-sums.tex`, the sum workshop and the solution of `ex:intpoly`. The division proposition gives the three remainders modulo `3`. Euclid's lemma lifts divisibility by `2` and by `3` to divisibility by `6`. |
| V1-R3-004 | `ch02-counting.tex`, solution of `ex:phi`. Every prime in `n` has exponent at least `1`, so `P_I` divides `n` and the count of multiples is exact. |
| V1-R3-005 | `ch02-counting.tex`, solution of `ex:catalan` (c). Closed by SR-001. |
| V1-R3-006 | `ch01-sums.tex`, solution of `ex:fibgcd`. A common divisor of the product and of `F_n` divides `F_n`. |
| V1-R3-007 | `ch03-polynomials.tex`, `thm:dalembert`. The extreme-value theorem bounds the continuous function on `[0,1]`. |
| V1-R3-008 | `ch02-complex-roots.tex`. `prop:sincmp` is proved in the sequences chapter and does not use this paragraph. The mean-value clause is applied to `-\cos`. |
| V1-R3-009 | `ch05-sequences-series.tex`, the least positive zero. A positive value at `\alpha` makes `\alpha+\delta` a greater lower bound. |
| V1-R3-010 | `ch05-sequences-series.tex`, Riemann's series. The derivative `-\alpha t^{-\alpha-1}` is negative, so the integrand is non-increasing. |
| V1-R3-011 | `ch03-polynomials.tex`, the beauty note. The proportion is a count of ordered pairs divided by `N^2`. |
| V1-R3-012 | `ch05-sequences-series.tex`. The sentence that `\sqrt{3}` exists stands before the bisection figure. The figure file is untouched. |
| V1-R3-013 | `ch05-sequences-series.tex`, solution of `ex:nested`. Closed by SR-002. |
| V1-R3-014 | `ch05-sequences-series.tex`, solution of `ex:condensation`. Closed by SR-003. |
| V1-R3-015 | `ch07-linear-algebra.tex`, solution of `ex:fibch`. The factor is `F_{n+1}+F_{n-1}`. The name `L_n` is not used. |
| V1-R3-016 | `ch07-linear-algebra.tex`, the beauty note and the chapter bridge. The eigenvector is a nonnegative column summing to `1`. |
| V1-R3-017 | `ch06-integrals-taylor.tex`, solution of `ex:lhopital`. The order-2 integral remainder is nonnegative for `t>0`. |
| V1-R3-018 | `ch06-integrals-taylor.tex`, solution of `ex:xnex`. Closed by SR-004. |
| V1-R3-019 | `ch06-integrals-taylor.tex`, solution of `ex:gammahalf`. The factors `2^n`, `\sqrt{2}` and `2(2\pi)^{-1/2}` are written, and the powers of `2` multiply to `2^{-n}`. |

## What this review did not check

- A LaTeX build. XeLaTeX is not installed in the review environment, so printed page numbers and overfull boxes were not seen.
- EPUB rendering and Kindle alt text.
- Proofs the diff does not touch, beyond the sentences needed to see that each repair cites an earlier result.
