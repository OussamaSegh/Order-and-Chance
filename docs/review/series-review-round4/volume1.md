# Volume 1 — First Principles

**Score: 8/10.**

The round-3 repairs are still the proofs they were written to be. Euclid’s lemma, the Catalan first return, the least positive zero of cosine, d’Alembert–Gauss, the spectral theorem, the Gaussian integral, Minkowski, and Bertrand’s ballot theorem were read as proofs and hold. What remains is eight places where a true sentence does not yet show the one comparison it uses.

**Counts.** 0 critical, 0 major, 8 minor. `V1-R4-001` through `V1-R4-003` and `V1-R4-101` through `V1-R4-105`.

**Round-3 follow-up.** 19 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume1-first-principles/main.tex`, on main at `e5a2a929`. Every chapter file was read, including exercises, hints, solutions, and captions. Each new row below was opened at the cited line. No full LaTeX build was run.

## Issues

Paths are relative to `volume1-first-principles/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V1-R4-001 | `chapters/ch01-sums.tex:605` | minor | “The only multiple of \(b\) strictly between \(-b\) and \(b\) is \(0\).” | If \(b\mid m\) and \(\lvert m\rvert<b\), write \(m=bt\). Then \(\lvert t\rvert\ge 1\) forces \(\lvert m\rvert\ge b\), so \(t=0\). Chapter 0 wrote this for \(b=2\). |
| V1-R4-002 | `chapters/ch01-sums.tex:953` | minor | “A sum of one odd integer and some even integers is odd.” | Write \(L/2^s=2s+1\) and each other term \(L/k=2t_k\). The sum is \(2(\cdots)+1\). |
| V1-R4-003 | `chapters/ch05-sequences-series.tex:1244` | minor | “Both \(f\) and \(g\) are positive and decreasing on \([2,\infty)\).” | The integral test needs the decrease. The derivatives are negative for \(t\ge 2\), and they are not written. The antiderivatives \(\ln\ln t\) and \(-1/\ln t\) are the same derivatives run backwards. |
| V1-R4-101 | `chapters/ch06-integrals-taylor.tex:436` and `:442` | minor | “The exponential then beats the power, so \(t^{x-1}e^{-t/2}\to 0\).” | After \((\ln t)/t\to 0\), the exponent is \(t\bigl((x-1)(\ln t)/t-1/2\bigr)\to-\infty\). The solution of `ex:xnex` already writes this comparison. The Gamma proof still uses the slogan. |
| V1-R4-102 | `chapters/ch06-integrals-taylor.tex:358` | minor | “These follow from the sign of the derivative of \(\ln(1+u)-u\) and \(\ln(1-u)+u\).” | The derivative of \(u-\ln(1+u)\) is \(u/(1+u)\ge 0\). The mean-value clause makes that function non-decreasing, and it vanishes at \(0\). The second inequality is the same clause for \(-\ln(1-u)-u\). |
| V1-R4-103 | `chapters/ch04-inequalities.tex:479` | minor | “As \(p\to+\infty\), the factor \(\lambda_{i_0}^{1/p}\) tends to \(1\).” | Write \(\lambda^{1/p}=\exp((\ln\lambda)/p)\to\exp(0)=1\). |
| V1-R4-104 | `chapters/ch02-complex-roots.tex:985` | minor | “so \(m\) is even, and in fact \(2n\) divides \(m\).” | The text already has \(n\mid m\) and \(2\mid m\), with \(n\) odd. Euclid’s lemma gives \(2n\mid m\). |
| V1-R4-105 | `chapters/ch06-integrals-taylor.tex:945` | minor | “In each class, toggling one fixed lamp pairs every even configuration with an odd one. Each of the eight triples of class parities therefore occurs equally often.” | The three classes are disjoint. Toggling a lamp in one class changes only that class’s parity, so the three pairings are independent. |

## Round-3 follow-up

All nineteen repairs were re-opened. The prime factors lie in \(\{2,\ldots,n-1\}\). The product \(k(k-1)\) is even by the even/odd split. Division by \(3\) uses the three remainders. The count of multiples in `ex:phi` uses the valuation test on \(n\). The Catalan return step is north, and the shift is stated for lattice points. The Fibonacci gcd names why a common divisor of the product divides \(F_n\). d’Alembert’s supremum cites the extreme-value theorem. Cosine on \([0,\pi]\) applies the mean-value clause to \(-\cos\). A positive value at the infimum makes \(\alpha+\delta\) a greater lower bound. The integrand \(t^{-\alpha}\) is shown non-increasing before the integral test. The bisection figure follows the sentence that \(\sqrt3\) exists. The half-angle step keeps the absolute value until the angle is placed in \((0,\pi/2)\). Condensation names the derivative and the increasing exponential. The Lucas name is not used before the field guide. The eigenvector is a nonnegative column summing to \(1\). The coprime-pair sentence is a count. The order-2 integral remainder gives \(e^t\ge t^2/2\). The limit \(A^ne^{-A}\to 0\) uses \(\ln A\le 4A^{1/4}\). The normal-moment substitution writes the three constant factors.

## Not checked

- A LaTeX build, so printed page numbers were not seen.
- EPUB rendering.
- Portrait files and primary memoirs.
