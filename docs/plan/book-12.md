# Volume 12 — Random Motion

*The Geometry of Random Paths.*

**Status of this file.** Blueprint of Volume 12 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification, which sent the random-matrix chapters to Volume 8. Decision D-16 brings them back. Chapter numbers below are the numbers after that decision. No proof named here has been verified.

**Series part.** IV. Randomness. **Directory.** `volume12-random-motion`.

## Central question

What does a random path look like, what calculus does it obey, and what happens when the thing that moves at random is a spectrum?

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 4 | Gaussian vectors, discrete martingales, Markov chains, electrical intuition |
| Volume 7 | Kolmogorov extension, Radon–Nikodym, Prokhorov, \(L^2\) |
| Volume 8 | Hilbert space and orthonormal bases; Plancherel; Hoffman–Wielandt and Courant–Fischer (Chapter 3); the graph spectra of Chapters 5–7 |
| Volume 9 | Haar measure on \(U(n)\), Weyl's integration formula, Heine's identity, the finite-\(n\) correlation functions (Chapter 8) |
| Volume 10 | Moments of traces of random unitary matrices (Chapter 11) |
| Volume 11 | Donsker; martingale convergence; the strong Markov property; Stein's lemma; Gaussian concentration; Lyapunov's theorem; Cramér–Wold |

**Admitted, discharged later.** Montgomery's theorem on pairs of zeros, stated in Chapter 10 for comparison with the sine kernel; proved in Volume 14, Chapter 14, under the Riemann hypothesis and on a limited range. No proof in this volume uses it.

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Brownian Motion** | | |
| 1 | Gaussian Processes and the Birth of Brownian Motion | `ch01-gaussian.tex` | Keep |
| 2 | The Fine Structure of a Brownian Path | `ch02-paths.tex` | Keep |
| | **Part II. Stochastic Calculus** | | |
| 3 | Continuous Martingales | `ch03-martingales.tex` | Keep |
| 4 | The Itô Integral | `ch04-ito.tex` | Keep |
| 5 | Brownian Motion and Analysis | `ch05-analysis.tex` | Keep |
| 6 | Stochastic Differential Equations | `ch06-sde.tex` | Keep |
| 7 | Markov Processes and Lévy Processes | `ch07-levy.tex` | Keep |
| | **Part III. Networks and Random Matrices** | | |
| 8 | Random Walks on Networks and Groups | `ch08-networks.tex` | Keep |
| 9 | Random Matrices I: The Semicircle | `ch10-semicircle.tex` | Returns from Volume 8 |
| 10 | Random Matrices II: Unitary Matrices and the Zeros of Zeta | `ch11-cue.tex` | Returns from Volume 8 |
| 11 | Log-Correlated Fields and the Largest Values | `ch12-logcorrelated.tex`, `brw-halfmoment.tex` | Moved from Part II to the end |
| | **Appendix** | | |
| A | Spectral Graph Theory | `spectral.tex` | Keep |

**Part name.** The third part is "Networks and Random Matrices". The catalog currently says "Networks"; it changes back in the pull request that moves the chapters.

**Why this order.** Chapter 11 studies the maximum of the characteristic polynomial of a random unitary matrix and cites the unitary chapter eleven times. It must follow Chapter 10. Chapter 6 proves that the eigenvalues of a Hermitian Brownian motion never collide (Dyson's Brownian motion) and points ahead to the random-matrix chapters; with those chapters back in this volume the pointer is again internal.

**How the subtitle is delivered.** Parts I and II are the path and its calculus. Part III is motion on a graph, then a spectrum that Chapter 6 already showed moving as a diffusion, then a field whose extreme values are found by following a branching path. The random matrices are in this volume because their eigenvalues are the random paths of Chapter 6 seen at one time.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Kolmogorov–Chentsov continuity; existence of Brownian motion; the Wiener integral | | 1 |
| Blumenthal's zero–one law; Lévy's modulus; the reflection principle; the dimension of the zero set | | 2 |
| Doob's inequalities in continuous time; quadratic variation | | 3 |
| The Itô integral; Itô's formula; Lévy's characterisation; Dambis–Dubins–Schwarz; Burkholder's inequality; Tanaka's formula | | 4 |
| Feynman–Kac; Girsanov for bounded drift; Cameron–Martin; the Dirichlet problem; conformal invariance | `thm:girsanov` | 5 |
| Existence and uniqueness for Lipschitz equations; Yamada–Watanabe; Dyson's Brownian motion without collisions | `thm:dyson` | 6 |
| Generators and Dynkin's formula; the Lévy–Itô decomposition | | 7 |
| Thomson's principle; Rayleigh monotonicity; the commute time identity; Nash-Williams; Kesten's theorem on the free group | `thm:kesten` | 8 |
| Wigner's semicircle law; Marchenko–Pastur; an outlier of a spiked matrix | | 9 |
| The sine kernel for the circular unitary ensemble; Gaussian limits for traces; the central limit theorem for \(\log\lvert\det\rvert\); Keating–Snaith's moments at integer exponents | `thm:sinekernel`, `thm:logclt` | 10 |
| Speed of the branching random walk; the characteristic polynomial is log-correlated; the upper bound for its maximum | | 11 |
| The matrix-tree theorem; the BEST theorem | | A |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| Tightness of the centred maximum of \(\log\lvert Z_n\rvert\) (`thm:cuemax`) | Admitted, with source |
| The Fyodorov–Hiary–Keating conjecture for \(\zeta\), and the theorems towards it | Quoted |
| Montgomery's theorem | Admitted, proved in Volume 14 under the Riemann hypothesis |
| The identification of zeros of \(\zeta\) with eigenvalues | Conjecture. Never a theorem |
| Tracy–Widom; bulk universality; the gap probability formula | Quoted |
| Novikov's condition | Quoted |
| Dyson's Brownian motion started from a multiple eigenvalue | Not proved |

## Climax

Itô's formula for Part II. For the volume, Chapter 10: the pair correlation of the eigenvalues of a random unitary matrix is \(1-\bigl(\tfrac{\sin\pi u}{\pi u}\bigr)^2\), a theorem, placed beside Montgomery's formula for the zeros of \(\zeta\), which Volume 14 will prove on a limited range. The volume ends in Chapter 11 on the question of how large such a function gets.

## Motivation and history

Brown, Einstein, Bachelier, Wiener; Itô and Doeblin's sealed envelope; Kakutani's drunk man and drunk bird; Pólya's walk; Wigner's nuclei; the conversation of Dyson and Montgomery at tea in 1972; Keating and Snaith. Each sourced.

## Examples and exercises

Brownian scaling; \(\int B\,\mathrm dB\); the Ornstein–Uhlenbeck process; exit from an annulus; recurrence of the plane and transience of space by resistances; a 2×2 Hermitian Brownian motion whose eigenvalues repel; the semicircle from 200 coin-toss matrices; \(1,2,42,24024\). Seven to nine exercises per chapter at three levels.

## Figures and experiments

A Brownian path at three scales; eigenvalue paths under Dyson's motion; the histogram of a Wigner matrix against the semicircle; nearest-neighbour spacings of sampled unitary eigenvalues beside spacings of computed zeros of \(\zeta\), captioned as an observation; a branching random walk. Scripts, seeds and the source of the zeros in the ledger.

## Changes from the current manuscript

**Preserve.** Chapters 1–8 and the appendix.

**Relocate.** `ch10-semicircle.tex` and `ch11-cue.tex` from Volume 8. `ch12-logcorrelated.tex` from Part II to the end of Part III.

**Rewrite.** The joins: the preface and Chapter 11 cite "Volume 8" for the unitary chapter; these become internal references. Chapter 9's reminder of Stein's lemma and Gaussian concentration becomes two backward citations of Volume 11. Chapter 6's remark that the eigenvalues started from zero have the Gaussian unitary density "which Chapter 10 studies" is corrected or headed as not proved.

**Label.** The table above. In Chapter 7, the measurability of jump counts used by the Lévy–Itô decomposition is written out or the theorem's heading says it is used.

**Remove.** `moments.tex`, which nothing prints, after a written check that its unique content is in Volume 15's moments chapter or is deliberately dropped.

**Missing.** A sentence in Chapter 8 and one in the appendix saying which cites which. One paragraph at the end of Chapter 11 handing the question to Volume 13.

## Links

**From Volume 11.** Donsker's limit becomes the object of study.
**From Volumes 8, 9, 10.** The graph spectra, Weyl's formula, and the trace moments meet in Part III.
**To Volume 13.** The volume ends asking what kind of function \(\zeta\) is. Volume 13 answers with its family.
**To Volume 14.** The sine kernel, cited beside Montgomery's theorem.
**To Volume 15.** The sine kernel, the trace limits, Keating–Snaith's moments and the log-correlated maximum are the "chance" side of Volume 15's Part III. Volume 15 cites them here and does not reprove them.

## Size

About 6,270 source lines after the two chapters return. **Estimate, not measured:** 180–210 printed pages.

## Mathematical risks

1. The sine-kernel limit and the uniformity needed to pass from finite \(n\).
2. Keating–Snaith at integer exponents: the Selberg-type integral or the Toeplitz route actually used.
3. The semicircle proof uses Volume 8's Hoffman–Wielandt and Volume 11's concentration; hypotheses on the entries must match.
4. The Lévy–Itô measurability step.
5. Girsanov: the class of drifts.
6. Kesten's theorem here against the statement in Volume 8, Chapter 7.
7. The spiked-matrix remark that claims more than the proof gives.

## Acceptance requirements

- Structure equals the table above. The catalog part name is "Networks and Random Matrices".
- No premise from Volumes 13–15.
- Verification records for: existence of Brownian motion, Itô's formula, Lévy's characterisation, `thm:girsanov`, `thm:dyson`, Lévy–Itô, `thm:kesten`, the semicircle law, `thm:sinekernel`, `thm:logclt`, the Keating–Snaith moments, the matrix-tree theorem.
- Every citation of the returned chapters from Volumes 9, 14 and 15 resolves to this volume.
- Every sentence comparing zeros with eigenvalues is typed: theorem, observation, or conjecture.
- The ten editorial standards of the master plan, section 6.5.
