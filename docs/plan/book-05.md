# Volume 5 — Calculation

*From Formula to Insight.*

**Status of this file.** Blueprint of Volume 5 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification of this volume, which described a twelve-chapter manuscript that no longer exists. Chapter numbers below are the numbers after decisions D-10 and D-11 are applied. No proof named here has been verified.

**Series part.** II. Bridges. **Directory.** `volume5-calculation`.

## Central question

When does a formula explain something? Each chapter starts from a formula a reader can compute with and ends with the reason it is true. The volume builds the instruments Volume 6 spends on the primes, and it ends with one symmetry used twice: once for \(\zeta\), once for partitions.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 1 | Calculus, series, complex numbers, linear algebra, inequalities |
| Volume 2 | Arithmetic functions, quadratic residues, continued fractions (in examples and in the Gauss sum) |
| Volume 3 | Characters of finite abelian groups, for the discrete Fourier transform |
| Volume 4 | Generating functions of distributions, the Gaussian, in examples |

**Admitted, discharged later.** Tonelli's theorem for non-negative functions, used in Chapter 3 and labelled there; proved in Volume 7, Chapter 9. Chapter 4 proves Fubini for continuous functions on rectangles, which covers every other use.

No other statement of a later volume is used. After this plan the volume contains no citation of Volume 6 as a premise.

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Series and Products** | | |
| 1 | Finite Calculus | `ch01-finite.tex` | Keep |
| 2 | Generating Functions as a Computing Tool | `ch02-generating.tex` | Keep. Owns Euler's pentagonal theorem |
| 3 | Classic Series and Infinite Products | `ch03-series.tex` | Keep |
| | **Part II. Integrals and Transforms** | | |
| 4 | Integration Techniques | `ch04-integrals.tex`, `bbp-borwein.tex` | Keep, with the BBP section where it is |
| 5 | The Gamma and Beta Functions | `ch05-gamma.tex` | Keep |
| 6 | Fourier Series | `ch06-fourier.tex` | Keep |
| 7 | The Discrete Fourier Transform and the FFT | `ch07-fft.tex` | Keep |
| 8 | The Fourier Transform and Poisson Summation | `ch08-transform.tex` | Keep |
| 9 | Complex Analysis for Computing | `ch09-complex.tex` | Keep |
| | **Part III. The Zeta Function** | | |
| 10 | The Zeta Function | `ch10-zeta.tex` | Keep |
| 11 | Asymptotics | `ch11-asymptotics.tex` | Keep |
| 12 | The Hardy–Ramanujan Formula | `hardy-ramanujan.tex` | Relocate from Part I. Rewrite one lemma (D-10) |
| 13 | The Arithmetic–Geometric Mean | `ch12-agm.tex` | Keep, with its closing problems |

**Leaves the volume.** Waring's Problem (`waring.tex`) goes to Volume 14, Chapter 6 (D-11).

**Effect on numbering.** Today the two circle-method chapters are Chapters 4 and 5, so Integration Techniques is Chapter 6 and The Zeta Function is Chapter 12. After the move every chapter from Integration Techniques to Asymptotics drops by two. Volumes 6, 8, 9, 13, 14 and 15 cite those chapters by number. This is why the citations are migrated to labels first (master plan, Phase 0).

## Essential definitions and results

Difference operator and Bernoulli numbers. Formal power series and the partition generating function. Infinite products and the cotangent expansion. The Gamma function. Fourier coefficients, the discrete transform, the Fourier transform on \(\mathbb R\). Holomorphic functions, residues, the identity theorem. Dirichlet series and \(\zeta\). Asymptotic expansions.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Euler's pentagonal number theorem | `thm:pentagonal` | 2 |
| The sine product and \(\zeta(2k)\) | | 3 |
| Bohr–Mollerup; reflection and duplication; Stirling for \(\Gamma\) | | 5 |
| Fejér; Parseval; Weyl's equidistribution criterion | | 6 |
| Fourier inversion; Poisson summation; the theta relation; the sign of the Gauss sum | `thm:ftinversion`, `thm:poisson`, `cor:theta`, `thm:gausssign` | 8 |
| Cauchy's formula; the identity theorem; the residue theorem | `thm:identity`, `thm:residue` | 9 |
| Euler product; functional equation of \(\zeta\); values at negative integers | `thm:eulerproduct`, `thm:functional`, `thm:zetaneg` | 10 |
| Euler–Maclaurin; Laplace's method; a transfer theorem | `thm:eulermaclaurin`, `thm:laplace`, `thm:transfer` | 11 |
| \(\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)\) | new | 12 |
| \(p(n)\sim\dfrac{1}{4n\sqrt3}\,e^{\pi\sqrt{2n/3}}\) | `thm:hr` | 12 |
| Gauss's theorem on the arithmetic–geometric mean; Brent–Salamin | | 13 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| Rademacher's exact formula for \(p(n)\) (`thm:rademacher`) | Quoted |
| Tonelli's theorem | Admitted, proved in Volume 7 |
| Any numerical zero of \(\zeta\) | A computation, with its source |

## Climax

Chapters 10 and 12 together. Poisson summation gives the theta relation, and the theta relation gives the functional equation of \(\zeta\). The same summation, applied to the pentagonal series, gives the transformation of \(\eta\), and with the saddle point of Chapter 11 that gives the size of \(p(n)\). The chapter says this in its first paragraph: one symmetry, two formulas.

## Motivation and history

Euler's evaluations, Fourier's heat, Gauss's diary entry on the arithmetic–geometric mean, Riemann's 1859 memoir, and Hardy and Ramanujan's 1918 paper with MacMahon's table of \(p(200)\). Each chapter opens with the formula and a named person; each quotation and date has a source in the chapter's "Sources".

## Examples and exercises

Every chapter computes before it proves: a power sum, a recurrence solved by partial fractions, \(\zeta(4)\), a Frullani integral, \(\Gamma(\tfrac12)\), a Gibbs overshoot, a length-8 transform, a Gaussian's transform, one real integral by residues, \(\zeta(-1)\), \(H_n\) to four terms, \(p(100)\) against the asymptotic, \(M(1,\sqrt2)\).

Exercises at three levels in every chapter. Chapters 4, 7 and 9 each gain one exercise of the hardest level. The closing problems of Chapter 13 are kept as the volume's problem set and each states the chapters it uses.

## Figures and experiments

Two or three figures per chapter. Required new figure: the ratio of \(p(n)\) to the Hardy–Ramanujan main term for \(n\le 1000\). Printed numerical values (digits of \(\pi\) from Brent–Salamin, \(p(200)\), any zero of \(\zeta\)) are traced in the numerical-claims ledger.

## Changes from the current manuscript

**Preserve.** Chapters 1–11 and 13 as written.

**Relocate.** `hardy-ramanujan.tex` from Part I to Part III. `waring.tex` to Volume 14.

**Rewrite.** In Chapter 12, the lemma that transforms the partition generating function (`lem:ptrans`) currently cites Volume 6 for the transformation of \(\eta\). Replace the citation by a proof: logarithmic derivative or, preferably, the pentagonal theorem (Chapter 2) written as a theta series, Poisson summation (Chapter 8) for \(\tau=it\), and the identity theorem (Chapter 9) to extend to the half-plane.

**Remove.** References to a "Problem Book". The stale chapter numbers inside the two relocated chapters. Legendre's use of the letter \(\Lambda\). An unproved claim about smooth cutoffs of \(\sum n\) in Chapter 10, unless it is proved.

**Missing.** The proof above. One sentence in Chapter 9 and one in Volume 8, Chapter 14, saying which complex analysis each owns. A sentence at the first use of \(\vartheta\) and of the completed zeta fixing the letters (master plan, section 4.5).

## Links

**From Volume 4.** Characteristic and generating functions become transforms.
**To Volume 6.** Residues, the functional equation, Poisson summation, Euler–Maclaurin, the Gauss sum. Volume 6 cites the \(\eta\) transformation from Chapter 12.
**To Volume 7.** The admitted Tonelli theorem is the debt Volume 7 pays first.
**To Volume 8.** Fourier series and the residue calculus are the base of the second analysis course.

## Size

About 10,450 source lines after Waring leaves. **Estimate, not measured:** 280–320 printed pages. The closing problems of Chapter 13 are about 1,600 of those lines.

## Mathematical risks

1. The new proof of the \(\eta\) transformation: the branch of the square root, the convergence of the pentagonal series as a theta series, the passage from the imaginary axis to the half-plane.
2. Chapter 12 after relocation must use nothing proved only in the chapter that leaves. The two chapters currently share a setting.
3. The minor-arc estimate of Hardy–Ramanujan: confirm the bound is proved for the whole circle and not only near \(q=1\).
4. Chapter 8's inversion theorem: the class of functions must be stated and must be the class Chapter 12 and Volume 6 use.

## Acceptance requirements

- Structure equals the table above. No citation of Volume 6 or later remains except the admitted Tonelli theorem, labelled.
- Verification records for: `thm:pentagonal`, `thm:poisson`, `thm:gausssign`, `thm:residue`, `thm:functional`, `thm:eulermaclaurin`, the new \(\eta\) theorem, `thm:hr`.
- The transformation of \(\eta\) checked numerically at three values of \(\tau\), recorded in the ledger.
- Every later volume's citations of this volume resolve by label after the renumbering.
- The ten editorial standards of the master plan, section 6.5.
