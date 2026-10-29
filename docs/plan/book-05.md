# Book 5 — Calculation

*From Formula to Insight.*

**Element.** The scaffolding. The instruments by which a later floor can measure a span: series, products, integrals, the Fourier transform, and the zeta function.

**On disk.** Volume 4, `tome4-calculation`. Twelve chapters. About 178 pages in the 7×10 table. The October review scored it 8. The factor \(\tfrac12\) in the functional equation is now the correct sentence in `ch10-zeta.tex`.

## Promise

Some results are exact values: \(\sum 1/n^2=\pi^2/6\), Wallis's product, the Gaussian integral, \(\zeta(-1)=-1/12\). Others are approximations so good they are a structure of their own: Stirling's series, the arithmetic–geometric mean. The floor builds the tools Book 6 spends. Zeta is born here, with its functional equation. The primes are not yet counted.

## Prerequisites

Book 1's calculus and series. Book 3's finite abelian characters, for the discrete Fourier transform. Fubini–Tonelli for general integrands is the only admitted fact, labelled, and rarely used: Chapter 4 proves Fubini for continuous functions on rectangles. Book 7 discharges the admission.

## How the subtitle is delivered

The subtitle is a motion: from formula to insight. Every chapter that stays starts with a formula and ends with what the formula means. No chapter is only a technique list.

| Chapter | Formula | Insight |
| --- | --- | --- |
| 1 Finite calculus | Power sums | There is a method, not a formula to memorise |
| 2 Generating functions | A series | A recurrence is a rational function |
| 3 Products | Sine, cotangent, \(\zeta(2k)\) | The same function is a sum over its poles |
| 4–5 Integrals and Gamma | Euler's integral | The factorial is the unique log-convex interpolation |
| 6–8 Fourier | A coefficient | A sum can be a wave, and Poisson summation fixes a sign |
| 9 Residues | A contour integral | A real integral was a residue |
| 10 Zeta | The Euler product | The functional equation, and the trivial zeros placed |
| 11 Asymptotics | A divergent series | An approximation with a remainder is still an equality |
| 12 The AGM | The iteration | Digits double, and an elliptic integral is the reason |

**Receives.** The Hardy–Ramanujan formula for \(p(n)\), moved from Book 14, joins Series and Products: it is the insight the partition generating function was built for. Waring's problem for large \(s\) joins the same part. Book 14 keeps only the three-prime theorem. The BBP series, moved from the old workshop, joins Series and Products as a formula that extracts a digit. No chapter of this book fails the subtitle. No part is renamed.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Series and Products | 1–3, plus the partition asymptotic, Waring for large \(s\), and the BBP series |
| II | Integrals and Transforms | 4–9 |
| III | The Zeta Function | 10–12 |

---

### Part I. Series and Products

#### Chapter 1. Finite Calculus

**Status.** KEEP — `tome4-calculation/chapters/ch01-finite.tex` (632 lines). The double mention of Bernoulli's *Ars Conjectandi* can be cut in a sentence-level pass. It is not a mathematical repair.

**Hook.** Everyone knows \(1+\cdots+n=n(n+1)/2\). What is \(1^5+\cdots+n^5\), and is there a method that finds it?

**Synopsis.** The difference operator, summation by parts, Stirling numbers, Bernoulli numbers, and Newton's series. Sums of powers are the worked thread. This is Book 1's finite differences, now a calculus.

**Proved.** The expression of a power sum in Bernoulli numbers, of the strength the chapter states. Summation by parts in the finite form Book 6's partial summation will recognise.

**Examples.** \(1^5+\cdots+n^5\), from the method. One Bernoulli number by the von Staudt–Clausen theorem, if the chapter proves it; otherwise a computed \(B_{12}\).

**Figures.** Two.

#### Chapter 2. Generating Functions as a Computing Tool

**Status.** KEEP — `chapters/ch02-generating.tex` (572 lines).

**Hook.** Wilf's clothesline: a generating function hangs a sequence up where one can see it.

**Synopsis.** Formal power series, the analytic tools the chapter needs, rational series and linear recurrences, exponential generating functions, and partitions. The partition function is introduced. Book 14's circle method proves the Hardy–Ramanujan asymptotic. This chapter does not. The exercise that states the asymptotic in its solution should say the proof is Book 14's.

**Proved.** The rational generating function of a linear recurrence. The pentagonal-number theorem, if the file proves it; the inventory's series chapter is the other candidate, and only one of them should own the proof.

**Examples.** A linear recurrence solved by a partial fraction. One partition identity checked for small \(n\).

**Figures.** Two.

#### Chapter 3. Classic Series and Infinite Products

**Status.** KEEP — `chapters/ch03-series.tex` (437 lines).

**Hook.** \(\pi^2/6=1+\frac14+\frac19+\frac1{16}+\cdots\), and the Wallis product beside it.

**Synopsis.** Infinite products, the partial fractions of the cotangent, the sine product, Euler's evaluation of \(\zeta(2k)\), and Niven's proof that \(\pi^2\) is irrational. \(\zeta(2k)\) is the theorem Book 6 cites by number. The cotangent expansion is the first time a function is a sum over its poles, which Book 6's explicit formula will do for \(\zeta'/\zeta\).

**Proved.** The sine product. \(\zeta(2k)\) as a rational multiple of \(\pi^{2k}\). Niven's theorem.

**Examples.** \(\zeta(2)\) and \(\zeta(4)\) written as fractions times powers of \(\pi\). One partial product of the sine, compared with the function.

**Figures.** Two.

### Part II. Integrals, Fourier and Complex Analysis

#### Chapter 4. Integration Techniques

**Status.** KEEP — `chapters/ch04-integrals.tex` (383 lines). A three-star exercise is worth adding; the review noted the chapter has none. That is an EXPAND of the exercise set, not of the theory.

**Hook.** Feynman, learning integrals from a book his physics teacher gave him, and the trick of differentiating under the sign.

**Synopsis.** Parameters on a compact interval, improper integrals, differentiation under the integral sign, Frullani, and Dirichlet's integral. The chapter proves Fubini for continuous functions on rectangles and labels anything beyond that.

**Proved.** Differentiation under the integral sign for continuous integrands on compact intervals, and the improper cases the chapter justifies. Frullani's formula. Dirichlet's discontinuous integral, if it is the evaluation the file gives.

**Examples.** One parameter integral computed by differentiating under the sign, with the justification on the page. A Frullani evaluation.

**Figures.** Two.

#### Chapter 5. The Gamma and Beta Functions

**Status.** KEEP — `chapters/ch05-gamma.tex` (539 lines). Artin's proof of the Beta integral is used because it avoids the Fubini–Tonelli change of variables. The text should keep saying why.

**Hook.** The factorial is a function on the integers. Euler asked for the curve through those points.

**Synopsis.** Euler's integral, Bohr–Mollerup, Stirling for the Gamma function, the Beta integral, reflection, duplication, and the volume of the unit ball. Bohr–Mollerup is why Book 1's convexity selected this interpolation. The volume of the ball tending to zero is a fact Book 7's change of variables will meet again.

**Proved.** Bohr–Mollerup. The reflection and duplication formulas. Stirling's formula for \(\Gamma\), with the remainder the chapter controls. The volume of the Euclidean unit ball.

**Examples.** \(\Gamma(1/2)=\sqrt\pi\). The volume of the ball in dimensions 2, 3, and a large \(n\) where it is small.

**Figures.** Three.

#### Chapter 6. Fourier Series

**Status.** KEEP — `chapters/ch06-fourier.tex` (548 lines).

**Hook.** Fourier, on the study of nature as a source of analysis. The chapter then proves the theorems.

**Synopsis.** Coefficients and best approximation, Dirichlet's theorem, Fejér, Parseval, the Gibbs phenomenon, equidistribution, several variables, and the isoperimetric inequality. Weyl's criterion is the theorem Book 6 and Book 15's bias computation can quote. Equidistribution is the first time a sequence on the circle is shown to be uniform by exponential sums.

**Proved.** Fejér's theorem. Parseval for the class the chapter treats. Weyl's criterion. The isoperimetric inequality by Fourier series, if that is the proof in the file.

**Examples.** A square wave and its Gibbs overshoot. One equidistributed sequence and one that is not.

**Figures.** Three.

#### Chapter 7. The Discrete Fourier Transform and the FFT

**Status.** KEEP — `chapters/ch07-fft.tex` (384 lines). A three-star exercise is the same small EXPAND as in Chapter 4.

**Hook.** Strang, calling the FFT the most important numerical algorithm of a lifetime.

**Synopsis.** The discrete transform, convolution, the FFT, exact transforms modulo a prime, the discrete cosine transform, and Gauss sums as Fourier coefficients. This is Fourier analysis on \(\mathbb Z/n\mathbb Z\). Book 3 and Book 8 own the group-theoretic form. The FFT is the algorithm.

**Proved.** Inversion. The convolution theorem. The FFT's operation count. The evaluation of a quadratic Gauss sum up to sign, if the sign is Chapter 8's.

**Examples.** A length-8 transform by hand, or a transform modulo 17. One cyclic convolution.

**Figures.** Two.

#### Chapter 8. The Fourier Transform and Poisson Summation

**Status.** KEEP — `chapters/ch08-transform.tex` (497 lines). REVISE the first use of \(\theta\) if it denotes a Jacobi theta: Book 6 will take the letter. Call it \(\vartheta\), or warn in the sentence.

**Hook.** Gauss, having the results and not yet the path to them. Poisson summation is the path.

**Synopsis.** The transform, inversion, Plancherel in the form this chapter proves, the heat equation, Poisson summation, the sign of the quadratic Gauss sum, sampling, and uncertainty. The sign of the Gauss sum is a theorem Book 6 cites. Poisson summation is the member Book 13's Tate thesis will use on the adèles. The citation runs forward.

**Proved.** Inversion when both \(f\) and \(\hat f\) are integrable, or the class the chapter states. Poisson summation for Schwartz functions. The sign of the quadratic Gauss sum.

**Examples.** The Gaussian transforms to a Gaussian. One Poisson summation that recovers a theta identity.

**Figures.** Three.

#### Chapter 9. Complex Analysis for Computing

**Status.** KEEP — `chapters/ch09-complex.tex` (813 lines). This is a working course: Cauchy, residues, Rouché. Book 8 owns winding numbers, Jordan, Dixon, Phragmén–Lindelöf, and the Riemann mapping theorem. The two courses should say so, each in one sentence. A three-star exercise is worth adding.

**Hook.** Painlevé: the shortest path between two real truths often passes through the complex domain.

**Synopsis.** Holomorphic functions, Cauchy's theorem for the contours the chapter uses, Cauchy's formula, Laurent series, the residue theorem, real integrals, sums by residues, and the Gamma function in the complex plane. Residues are how \(\zeta(2k)\) and a rational integral can be the same method.

**Proved.** Cauchy's integral formula. The residue theorem for the contours stated. Rouché. The evaluation \(\int_{-\infty}^{\infty}(1+x^4)^{-1}\,\mathrm dx=\pi/\sqrt 2\).

**Examples.** That rational integral. One sum evaluated by residues, cotangents or a geometric kernel.

**Figures.** Three.

### Part III. The Zeta Function and Asymptotics

#### Chapter 10. The Zeta Function

**Status.** KEEP — `chapters/ch10-zeta.tex` (449 lines). The polar-term sentence is repaired. REVISE the claim that every smooth cutoff of \(\sum n\) has finite part \(-\frac1{12}\): prove it or delete it. At the first use of the completed zeta, say that Book 6 uses \(\Lambda\) for von Mangoldt and \(\theta\) for Chebyshev.

**Hook.** Riemann, setting aside the search for a proof that all the roots are real. The chapter proves the functional equation and does not pretend to prove the hypothesis.

**Synopsis.** Dirichlet series, the Euler product, the strip \(\mathrm{Re}\,s>0\), Riemann's functional equation, the values at the negative integers, and a first look at the zeros. This is the birth of the character. Book 2 saw only the shadow \(6/\pi^2\). The trivial zeros are placed. The non-trivial zeros are described and not located.

**Proved.** The Euler product for \(\mathrm{Re}\,s>1\). The meromorphic continuation to \(\mathrm{Re}\,s>0\) with a simple pole of residue 1. The functional equation. \(\zeta(-1)=-\frac1{12}\) and \(\zeta(-3)=\frac1{120}\), from that equation. The trivial zeros.

**Examples.** \(\zeta(2)=\pi^2/6\) recovered from the functional equation and a value at a negative integer, or the direct Euler evaluation cited back to Chapter 3. One numerical zero, stated as a computation.

**Figures.** Two.

#### Chapter 11. Asymptotics

**Status.** KEEP — `chapters/ch11-asymptotics.tex` (621 lines). EXPAND by one complex saddle-point argument, so Book 14's circle method has a reference for the method's shape. Book 14 can stand without it; the joint is cleaner with it. Add a three-star exercise whose point is an error term.

**Hook.** Abel, calling divergent series an invention of the devil. The chapter then uses them with a remainder.

**Synopsis.** Asymptotic scales, Euler–Maclaurin, Stirling's series with the sign of the remainder, Laplace's method, and a transfer theorem for coefficients. Euler–Maclaurin is how Book 6 turns a sum over primes into an integral. Laplace's method is the real saddle. One complex saddle belongs beside it.

**Proved.** Euler–Maclaurin with a remainder. Stirling's series. Laplace's method for the integrals the chapter treats.

**Examples.** The expansion of \(H_n\). A Laplace integral with its first two terms and a remainder. The alternating remainder used to compute \(\log\Gamma\), which the chapter already explains.

**Figures.** Two.

#### Chapter 12. The Arithmetic–Geometric Mean

**Status.** KEEP — `chapters/ch12-agm.tex` (445 lines). Legendre's \(\Lambda(k)\) is renamed on the notation pass.

**Hook.** Gauss, the arithmetic–geometric mean of 1 and \(\sqrt 2\) to eleven decimals, and the demonstration still to write.

**Synopsis.** The AGM iteration, Gauss's theorem identifying it with an elliptic integral, the perimeter of an ellipse, Legendre's relation, and Brent–Salamin. Doubling the number of correct digits is the spectacle. Elliptic integrals are a pointer to Book 13's elliptic curves, not a theory of them.

**Proved.** Convergence of the iteration. Gauss's theorem. Brent–Salamin, or the form of Legendre's relation the chapter uses to compute \(\pi\).

**Examples.** \(M(1,\sqrt 2)\), with the digit counts. One ellipse perimeter.

**Figures.** Three.

## The old problem book

Book 6 is Crossroads, the analytic volume. The old P1 problem book is removed by the renumbering branch, which appends its problems to Books 1–6. This plan does not place them again. A problem that cites a chapter moved here follows that chapter.

## Owns, defers, hands forward

**Owns.** Finite calculus, generating functions, the sine and cotangent products, \(\zeta(2k)\), the Gamma function through Bohr–Mollerup, Fourier series through Fejér and Weyl, the FFT, Poisson summation and the sign of the Gauss sum, a residue calculus, the functional equation of zeta, Euler–Maclaurin, Laplace's method, the AGM.

**Defers.** The prime number theorem. Zero-free regions. Fubini–Tonelli in general. The spectral theorem for compact operators. The Riemann mapping theorem. The Hardy–Ramanujan asymptotic.

**Hands forward.** A reader who can evaluate a residue, quote the functional equation, apply Poisson summation, and expand a sum by Euler–Maclaurin. Book 6 starts from those instruments.

## Pages and effort

Baseline 178 pages. Target 190–220 if the saddle-point section is added. Effort: moderate. The functional equation is repaired. The remaining work is the cutoff claim, the notation warnings, one saddle, and three three-star exercises.
