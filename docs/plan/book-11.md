# Volume 11 — Randomness

*Martingales, Limits and Ergodicity.*

**Status of this file.** Blueprint of Volume 11 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. Chapter numbers below are the numbers after decision D-26 is applied. No proof named here has been verified.

**Series part.** IV. Randomness. **Directory.** `volume11-randomness`.

## Central question

What survives when the hypotheses of Volume 4 fail? When there is no variance, when the event is rare, when the variables depend on each other, or when there is no randomness at all, only one system watched for a long time.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 4 | All of it: independence, the laws of large numbers, characteristic functions, the central limit theorem, discrete martingales, Markov chains, a first Brownian motion |
| Volume 7 | Measure, conditional expectation and the tower property, Prokhorov, Kolmogorov extension, \(L^p\) |
| Volume 8 | Hilbert space, the mean ergodic theorem, compact operators (for Furstenberg's proof) |
| Volume 10 | Characters of the symmetric group, used only in Chapter 13 |
| Volumes 2, 5, 6 | Continued fractions; Fourier series and Stirling; Erdős–Kac as a statement for comparison |

A reader may begin this volume after Volume 8. Volumes 9 and 10 are needed only for Chapter 13, and the preface says so.

**Admitted, discharged later.** The Selberg–Delange formula, used in Chapter 11 to describe the number of prime factors of a random integer; proved in Volume 15, Chapter 3. The chapter's own theorems about mod-\(\varphi\) convergence do not depend on it.

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Invariance Principles** | | |
| 1 | Independence and Zero–One Laws | `ch01-zero-one.tex` | Keep |
| 2 | Laws of Large Numbers | `ch02-lln.tex` | Keep |
| 3 | Weak Convergence and Donsker's Theorem | `ch03-donsker.tex` | Keep |
| 4 | The Central Limit Theorem, Sharpened | `ch04-clt.tex` | Keep |
| | **Part II. Stable Laws** | | |
| 5 | Infinitely Divisible and Stable Laws | `ch05-stable.tex` | Keep |
| 6 | Stein's Method | `ch06-stein.tex` | Keep |
| 7 | Large Deviations | `ch07-ldp.tex` | Keep |
| 8 | Concentration of Measure | `ch08-concentration.tex` | Keep |
| | **Part III. Martingales and Ergodic Theory** | | |
| 9 | Martingales II: Closing the Circle | `ch09-martingales.tex` | Keep |
| 10 | Ergodic Theory | `ch10-ergodic.tex` | Keep |
| 11 | Mod-\(\varphi\) Convergence | `ch11-modphi.tex` | Keep; one label |
| 12 | Random Permutations and the Poisson–Dirichlet Law | `ch12-permutations.tex` | Keep |
| 13 | Shuffling Cards | `shuffling.tex`, `riffle-cutoff.tex` | Moved before the problem chapter |
| 14 | Sums of Random Pieces (problems) | `ch13-harder.tex` | Now last. Receives problems from Volume 7 |

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Kolmogorov's zero–one law; Hewitt–Savage; convergence of random series | | 1 |
| Etemadi's strong law; the three-series theorem | | 2 |
| Lévy's continuity theorem; Cramér–Wold; Skorokhod embedding; Donsker's invariance principle; the arcsine law | `thm:levycont`, `cor:cramerwold`, `thm:donsker` | 3 |
| Lindeberg–Feller; Lyapunov; Berry–Esseen; a local limit theorem | `thm:feller`, `cor:lyapunov`, `thm:berryesseen` | 4 |
| Lévy–Khintchine; symmetric stable laws and their domains of attraction | | 5 |
| Stein's lemma; a central limit theorem with a rate; Chen–Stein | `lem:stein` | 6 |
| Cramér; Sanov for a finite alphabet; Varadhan's lemma for sample means | | 7 |
| Efron–Stein; McDiarmid; Gaussian concentration; Talagrand's inequality | `thm:gaussconc` | 8 |
| Uniformly integrable martingales; Lévy's upward and downward theorems; de Finetti; Kakutani's dichotomy | | 9 |
| Poincaré recurrence; Birkhoff's ergodic theorem; the Gauss map is ergodic; Roth's theorem by Furstenberg's correspondence | `thm:birkhoff`, `thm:gaussergodic`, `thm:roth`, `thm:double` | 10 |
| Mod-\(\varphi\) convergence implies a central and a local limit theorem | | 11 |
| Cycle structure of a random permutation; the Poisson–Dirichlet limit; Dickman's function | | 12 |
| The upper bound lemma; cutoff for random transpositions; the Bayer–Diaconis formula; cutoff for riffle shuffles at \(\tfrac32\log_2n\) | `thm:ds`, `cor:cutoff`, `thm:bd`, `cor:riffle` | 13 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| The Selberg–Delange formula (Chapter 11) | Admitted, proved in Volume 15 |
| Donsker's theorem for the empirical process | Not proved. The remark on Kolmogorov–Smirnov says so |
| Non-symmetric stable laws; the triangular-array converse | Quoted |
| Bahadur–Rao; Sanov beyond a finite alphabet | Quoted |
| Szemerédi's theorem beyond length three | Quoted |
| The prime-factor analogue of the Poisson–Dirichlet law (Billingsley) | Stated here with its source; Volume 15, Chapter 1 treats friable integers |

## Climax

Donsker's theorem in Part I: every random walk, seen from far away, is the same curve. Then Chapter 10: Birkhoff's theorem, and Furstenberg's proof that a set of positive density contains three terms in progression, a theorem about integers proved with no randomness in its statement and probability in its proof. Volume 14 proves it again by Fourier analysis, and each chapter names the other.

## Motivation and history

Kolmogorov, Lévy, Khinchin, Donsker and Erdős–Kac's invariance, Stein's 1972 lecture, Cramér and the insurers, Talagrand, de Finetti, Boltzmann and Birkhoff, Gauss's letter to Laplace on continued fractions, Furstenberg, Diaconis at the card table.

## Examples and exercises

Random signs on the harmonic series; the St Petersburg game; the Cauchy law; birthday problems by Chen–Stein; a longest increasing subsequence; the digits of a continued fraction; seven shuffles.

Seven exercises per chapter at three levels. Chapter 14 is the problem chapter: local limit theorems, signed sums, Bernoulli convolutions, real roots of random polynomials, and now the ergodic problems on continued fractions that arrive from Volume 7.

## Figures and experiments

A rescaled walk against Brownian motion; stable densities; the total-variation cutoff curve for riffle shuffles, computed exactly from Bayer–Diaconis; frequencies of continued-fraction digits against Gauss's law. Scripts and seeds in the ledger.

## Changes from the current manuscript

**Preserve.** All fourteen chapters.

**Relocate.** Shuffling Cards before the problem chapter. Into Chapter 14: the problems of Volume 7's "Almost every number" that use the Gauss map or Birkhoff's theorem (D-15), as a section on continued fractions.

**Rewrite.** Chapter 10 states von Neumann's mean ergodic theorem, which Volume 8, Chapter 2 proves: cite it. Chapter 11: the description of a uniform integer is headed as a corollary of an admitted formula.

**Label.** The statements in the table above.

**Remove.** Stale chapter numbers for Volume 14's Roth chapter (it is Chapter 12 after this plan).

**Missing.** One sentence each in Chapters 10 and 12 pointing to the arithmetic returns: Volume 6's Erdős–Kac and Volume 14's Roth.

## Links

**From Volume 10.** The symmetric group, for one chapter. The preface makes the change of subject explicit.
**To Volume 12.** Donsker, the strong Markov property, martingale convergence, Stein's lemma and Gaussian concentration (for the semicircle), Lyapunov's theorem and Cramér–Wold (for the unitary ensemble).
**To Volume 14.** The ergodic proof of Roth, for comparison.
**To Volume 15.** Berry–Esseen, mod-\(\varphi\) convergence, the Poisson–Dirichlet law. Volume 15 proves Selberg–Delange without using Chapter 11's corollary.

## Size

About 7,950 source lines, plus the problems arriving from Volume 7. **Estimate, not measured:** 230–260 printed pages.

## Mathematical risks

1. The circle with Volume 15: `ra-selbergdelange.tex` cites "Volume 11, Chapter 11". Confirm it is a comparison and not a premise (master plan, PR 2.10).
2. Furstenberg's proof: the compact and weakly mixing parts, and the correspondence principle.
3. Skorokhod embedding and the modulus comparison in Donsker's theorem.
4. Berry–Esseen: the constant claimed.
5. Riffle cutoff: the asymptotics of the Bayer–Diaconis formula.
6. Chapter 14's solutions against rule R1; they cite Volumes 8, 10 and 13.

## Acceptance requirements

- Structure equals the table above.
- The only forward reliance is the admitted Selberg–Delange formula, labelled, with a ledger row.
- Verification records for: `thm:levycont`, `thm:donsker`, `thm:feller`, `thm:berryesseen`, `lem:stein`, `thm:gaussconc`, `thm:birkhoff`, `thm:gaussergodic`, `thm:roth`, `thm:ds`, `cor:cutoff`, `thm:bd`, `cor:riffle`, Lévy–Khintchine, Cramér.
- Every label Volume 12 cites resolves.
- The ten editorial standards of the master plan, section 6.5.
