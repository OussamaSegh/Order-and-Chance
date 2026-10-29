# Book 12 — Random Motion

*The Geometry of Random Paths.*

**Element.** The circulation. Paths with no tangent, and spectra that move and refuse to collide.

**On disk.** Volume 11, `tome11-motion`. Twelve chapters, then `chapters/spectral.tex` and `chapters/moments.tex`. About 228 pages. The October review scored it 8.

## Promise

Brown's pollen, Einstein's explanation, Wiener's curve. This floor builds that curve and the calculus it requires, then puts the motion to work: stochastic differential equations, Lévy processes, random walks on networks, expander graphs and their Riemann hypothesis, and random matrices. The sine kernel for a random unitary matrix is a theorem. Montgomery's theorem for the zeros is cited to Book 14. The identification of the two is a conjecture, drawn on the wall and not proved. The graph-theoretic Riemann hypothesis is the rehearsal.

## Prerequisites

Book 4's Brownian motion and Book 11's Donsker theorem, Gaussian concentration, and Stein's lemma. Book 7's Prokhorov theorem and Radon–Nikodym derivative. Book 8's Plancherel theorem. Book 9's Weyl integration formula, the finite-\(n\) circular ensemble. Book 6's zero-counting is a dictionary, not a proof reproduced here.

## How the subtitle is delivered

The parts keep their catalog names. *The Geometry of Random Paths* is what the chapters that stay actually study.

Brownian Motion is the path: its construction, its fine structure, and the analysis it performs. Stochastic Calculus is the calculus along that path, including Dyson Brownian motion, because those eigenvalues move. Networks and Random Matrices, in the catalog, holds the walks on graphs and then the random-matrix chapters. The walks deliver the subtitle. The still spectra do not.

## Proposed part-name change

**Networks and Random Matrices** becomes **Networks**. Expanders, the semicircle, and the sine kernel move to Book 8, Spectral Theory. What remains is Chapter 8 and the resistance and matrix-tree half of the spectral appendix.

**Moves.** These deliver *Operators, Spectra and Transforms*, or the meeting in Book 15. They do not deliver the geometry of a random path.

| Material | File | Where it goes |
| --- | --- | --- |
| Expanders, Ramanujan graphs, Ihara's zeta, the graph-theoretic Riemann hypothesis | `ch09-expanders.tex`, and Theorems A.9–A.11 in `spectral.tex` | Book 8, Spectra |
| The semicircle, Marchenko–Pastur, the sine kernel, Keating–Snaith's moments | `ch10-semicircle.tex`, `ch11-cue.tex` | Book 8, Spectra. Book 14 and Book 15 cite them there. |
| The zeta narrative and the off-line mean square as a story about zeros | `moments.tex` | Book 15, the meeting of the spectrum and the zeros. The moment-method semicircle goes to Book 8 with the semicircle theorem. |
| The conjecture for the maximum of \(\log\|\zeta\|\) | the last section of `ch12-logcorrelated.tex` | Book 15. The branching random walk, which is a path, stays here. |

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Brownian Motion | 1, 2, and 5 |
| II | Stochastic Calculus | 3, 4, 6, 7, and the branching-random-walk chapter |
| III | Networks and Random Matrices | Chapter 8 and the path half of Appendix A. The matrix chapters move. The proposed name is Networks. |

---

The chapter notes follow the manuscript's file order. Chapters marked MOVE leave this book. What stays is the geometry of a random path.

### Part I. Brownian Motion

#### Chapter 1. Gaussian Processes and the Birth of Brownian Motion

**Status.** KEEP — `tome11-motion/chapters/ch01-gaussian.tex` (571 lines).

**Hook.** A random function is a family of random numbers, one for each time. Kolmogorov showed that a consistent choice of the finite collections, with a moment bound, has a continuous version.

**Synopsis.** Gaussian processes, Kolmogorov's continuity criterion, Brownian motion as a Fourier series, the Wiener integral, and fractional Brownian motion. Book 4 constructed Brownian motion by Lévy's midpoint method. This chapter constructs it as a Gaussian process and names the criterion that makes the path continuous. Fractional Brownian motion is the one-parameter deformation, not a second theory of finance.

**Proved.** Kolmogorov–Chentsov. Existence of a continuous Brownian motion as a Gaussian process. The Wiener integral for deterministic integrands in \(L^2\).

**Examples.** The Fourier series of a Brownian bridge or of Brownian motion, with the covariance checked. One fractional path, as a picture, with the Hurst parameter named.

**Figures.** Two.

#### Chapter 2. The Fine Structure of a Brownian Path

**Status.** KEEP — `chapters/ch02-paths.tex` (397 lines).

**Hook.** Zoom in on a Brownian path and it looks the same: no tangent, the same jagged lace at every scale. The zoom has an exact cost.

**Synopsis.** Behaviour at time zero, Lévy's modulus of continuity, the maximum and the position, the zero set, and Hausdorff dimension one half. The zero set is the return of Book 7's dimension. A sentence cites the carpet's dimension as a different computation of the same kind of number.

**Proved.** Lévy's modulus. The law of the maximum. The zero set has dimension \(\tfrac12\).

**Examples.** A numerical modulus against \(\sqrt{2h\log(1/h)}\). The zeros of a discrete skeleton.

**Figures.** Two.

#### Chapter 5. Brownian Motion and Analysis

**Status.** KEEP — `chapters/ch05-analysis.tex` (476 lines). Girsanov is proved for bounded drift. Novikov's condition is stated and cited to Revuz–Yor. Cameron–Martin for deterministic shifts in \(L^2\) is proved by approximation. The citations stay.

**Hook.** Heat spreads as Brownian particles wander. A harmonic function is the average of its boundary values, seen by a wandering particle.

**Synopsis.** Feynman–Kac, Girsanov, harmonic functions, the Dirichlet problem, recurrence and transience by dimension, and conformal invariance in the plane. Recurrence by dimension returns Book 4's Pólya theorem for the continuous path. Conformal invariance is the joint into two-dimensional geometry, not a course in SLE.

**Proved.** The Feynman–Kac formula for the potentials the chapter treats. Girsanov for bounded drift. The Dirichlet solution by Brownian exit. Recurrence in dimensions 1 and 2, transience in dimensions \(\ge 3\).

**Examples.** A harmonic function recovered as an exit average. One Girsanov change with a constant drift, the case Black–Scholes uses.

**Figures.** One.

### Part II. Stochastic Calculus

#### Chapter 3. Continuous Martingales

**Status.** KEEP — `chapters/ch03-martingales.tex` (607 lines).

**Hook.** A fair game watched continuously carries its own clock, the quadratic variation, which ticks exactly when the path is moving.

**Synopsis.** Filtrations, stopping times, continuous martingales, local martingales, quadratic variation, and exponential martingales. Book 4 saw quadratic variation for Brownian motion. This chapter makes it the clock of every continuous martingale. Book 11's discrete martingales are the ancestor, cited.

**Proved.** Existence of quadratic variation for a continuous local martingale. The exponential martingale and its use for hitting times, under the hypotheses stated.

**Examples.** Brownian quadratic variation, recovered. One exponential martingale stopped at a bounded time.

**Figures.** Two.

#### Chapter 4. The Itô Integral

**Status.** KEEP — `chapters/ch04-ito.tex` (599 lines). The opening, Itô's left endpoint and Doeblin's envelope, stays. It is the right way into the definition.

**Hook.** A Brownian path has no derivative, so \(\int f(B_s)\,\mathrm dB_s\) makes no sense path by path. Itô made it make sense in \(L^2\).

**Synopsis.** The Kunita–Watanabe inequality, the integral of simple processes, localisation, Itô's formula, Lévy's characterisation, Burkholder's inequality, and Tanaka's formula with local time. Lévy's characterisation, that a continuous local martingale with quadratic variation \(t\) is Brownian motion, is the theorem that identifies the path. General predictable integrands and the full excursion measure are not claimed.

**Proved.** Construction of the Itô integral. Itô's formula. Lévy's characterisation. Tanaka's formula.

**Examples.** The three Riemann-sum conventions for \(\int B\,\mathrm dB\), and why the left endpoint gives \(\tfrac12(B_t^2-t)\). One application of Itô's formula to a named function.

**Figures.** Two.

#### Chapter 6. Stochastic Differential Equations

**Status.** REVISE — `chapters/ch06-sde.tex` (639 lines). The theorem that Hermitian Brownian motion started with distinct eigenvalues never collides, and that the eigenvalues solve the \(\beta=2\) Dyson system, is a complete proof. The following remark, that from \(H_0=0\) the eigenvalues separate at once and \(\lambda(1)\) has the GUE joint density "which Chapter 10 studies", overclaims. Chapter 10 does not derive \(\prod_{i<j}|\lambda_i-\lambda_j|^2\exp(-\sum\lambda_i^2/2)\). State the entrance from a multiple eigenvalue as not proved.

**Hook.** A particle pushed by a force and kicked by noise. A price that grows and trembles. Eigenvalues that wander and repel.

**Synopsis.** Strong existence for Lipschitz coefficients, linear equations, Langevin and Black–Scholes, Bessel processes, Dyson Brownian motion for \(\beta=2\) from a simple spectrum, and Euler–Maruyama. Black–Scholes uses a constant drift, which Girsanov covers. Book 4's binomial limit is the elementary ancestor. This chapter is the continuous equation.

**Proved.** Strong existence and uniqueness for Lipschitz coefficients. The Black–Scholes price for constant coefficients. Bessel processes and the dimensions that hit zero. The Dyson system from a simple initial spectrum.

**Examples.** The numerical Black–Scholes data of Book 4, now as a solution of an SDE. One Euler–Maruyama path against the exact mean.

**Figures.** Two.

#### Chapter 7. Markov Processes and Lévy Processes

**Status.** REVISE — `chapters/ch07-levy.tex` (466 lines). Lévy–Itô, part (b), reduces the identification of the jump measure to the claim that jumps of a càdlàg path are a measurable function of the values at rational times. Write that measurability, or mark part (b) as using it.

**Hook.** A Markov process is a machine with no memory. Its generator is the instruction it executes at each instant.

**Synopsis.** Semigroups and generators, Poisson random measures, Lévy processes, and subordinators. The Lévy–Itô decomposition is the pathwise form of Book 11's Lévy–Khintchine formula. The chapter should say "pathwise form" in the heading.

**Proved.** The generator of Brownian motion and of a compound Poisson process. The Lévy–Itô decomposition, after the measurability line is written or labelled.

**Examples.** A compound Poisson process plus a Brownian motion, its Lévy triple read off. One subordinator.

**Figures.** One.

### Part III. Spectra of Graphs

#### Chapter 8. Random Walks on Networks and Groups

**Status.** KEEP — `chapters/ch08-networks.tex` (419 lines). The chapter rests on Appendix A. The appendix does not rest on the chapter, so the dependence is a citation, not a circle. Say that in the first paragraph.

**Hook.** A random walker on a graph and an electric current in a network of resistors solve the same equations.

**Synopsis.** Reversible walks, voltage, current, effective resistance, recurrence and transience by electricity, and walks on trees and groups. Pólya's theorem returns as a resistance computation. Kesten's theorem on walks on groups is the group form, if the file proves it.

**Proved.** The electrical interpretation of hitting probabilities and effective resistance. The recurrence criterion by resistance. Cheeger is Theorem A.9, the mixing lemma Lemma A.10, Alon–Boppana Theorem A.11, and those numbers match the appendix. This chapter cites them.

**Examples.** The infinite grid, recurrent, by a resistance estimate. One finite network with an explicit effective resistance.

**Figures.** One.

#### Chapter 9. Expanders and Ramanujan Graphs

**Status.** MOVE — `chapters/ch09-expanders.tex` (510 lines), to Book 8, Spectra. A Ramanujan graph is a spectrum with a zeta function. It is not the geometry of a random path. The mixing of a walk that uses a spectral gap stays in Chapter 8 as one theorem about paths.

**Hook.** A sparse graph in which every set has many neighbours, a walk that forgets its start in a few steps, and a zeta function whose zeros lie on a line.

**Synopsis.** The spectral gap and mixing, saving random bits, the spectral measure of the tree, Ihara's zeta function, the Riemann hypothesis for graphs, and Ramanujan graphs. What is proved is Sunada's eigenvalue form of the graph-theoretic Riemann hypothesis and the prime-number theorem for a non-bipartite Ramanujan graph. The constructions are described in remarks where the file describes them as remarks. This is the rehearsal: a zeta function, a prime-number theorem, a critical line, for a graph. Book 14's zeta is the number-theoretic original, not a corollary.

**Proved.** The mixing bound from the spectral gap. The graph-theoretic Riemann hypothesis in the eigenvalue form the chapter proves. The prime-number theorem for a non-bipartite Ramanujan graph.

**Examples.** A small expander and its gap. One Ihara zeta, computed for a small graph.

**Figures.** One.

#### Appendix A. Spectral Graph Theory

**Status.** KEEP — `chapters/spectral.tex` (531 lines). REVISE only the position in the reader's mind: the moment method and the basic spectral facts are easier than Chapter 10, which quotes them. The file may stay an appendix if Chapters 8 and 9 cite it by number. The zeta narrative does not belong in this appendix. It belongs in Chapter 11 and in Book 15.

**Hook.** Kac: can one hear the shape of a drum?

**Synopsis.** The Laplacian, the matrix-tree theorem, Eulerian circuits, Cheeger's inequality, and expanders. The matrix-tree theorem is what a Crossroads Journey on uniform spanning trees needs. That Journey moves here, not into Book 4.

**Proved.** The matrix-tree theorem. Cheeger's inequality, Theorem A.9. The mixing lemma, Lemma A.10. Alon–Boppana, Theorem A.11.

**Examples.** A spanning-tree count by a determinant. One Cheeger cut.

**Figures.** Three.

### Part IV. Spectra of Matrices

#### Chapter 10. Random Matrices I: The Semicircle

**Status.** MOVE — `chapters/ch10-semicircle.tex` (452 lines), to Book 8, Spectra. Move the moment-method proof with it. The chapter currently uses the appendix's moment method and Theorem B.3 before the appendix has appeared. The outlier theorem for a spiked Wigner matrix is a complete secular-equation proof. The following remark says the Baik–Ben Arous–Péché transition has "the proof above, with the Marchenko–Pastur law in place of the semicircle". Replace that sentence: the sample-covariance spike is not derived here. Tracy–Widom stays a remark, with its tails, and the remark says the limit law is not proved in this book.

**Hook.** Fill a large symmetric matrix with coin tosses. The eigenvalues arrange themselves in a semicircle.

**Synopsis.** Almost-sure convergence to the semicircle, Stieltjes transforms, the Marchenko–Pastur law for \(\gamma\in(0,1)\), the largest eigenvalue, and a Wigner spike. The moment method, moved forward, is the elementary proof. The Stieltjes transform is the robust one. Universality in the bulk is not claimed.

**Proved.** The semicircle law, almost surely, by the method the chapter then contains. Marchenko–Pastur. The spiked Wigner outlier, by the secular equation.

**Examples.** A histogram of a coin-toss Wigner matrix against the semicircle. One spike, the eigenvalue pulled out of the bulk.

**Figures.** One, plus the moment-method picture if it moves with the proof.

#### Chapter 11. Random Matrices II: Unitary Matrices and the Zeros of Zeta

**Status.** MOVE — `chapters/ch11-cue.tex` (610 lines), to Book 8, Spectra. The sine kernel is a spectrum. Dyson Brownian motion, the path, stays in Chapter 6. Neither Tracy–Widom nor \(p(s)=\mathrm d^2E(0;s)/\mathrm ds^2\) is proved in this file. The identity is cited to Mehta. Montgomery's theorem is "proved in Book 14", and the cross-reference to that book's Theorem 14.15 matches. Keep it. The pair-correlation conjecture is labelled a conjecture. The stray capital in "Direct numerical experimentation" is a one-word repair.

**Hook.** Choose a unitary matrix at random and look at its eigenvalues on the circle. Then compute the zeros of zeta, high on the critical line. The spacings agree, as far as the picture can see.

**Synopsis.** Counting eigenvalues, the sine kernel as the scaled limit of Book 9's Weyl formula, the gap series, the characteristic polynomial, Keating–Snaith's integer moments, and the central limit theorem for \(\log|\det|\). The zeros of zeta are the last section, and they are a dictionary: what is a theorem about matrices, what Book 14 proves about zeros, and what is a conjecture. Book 15 puts the two form factors on one page and does not reprove either theorem.

**Proved.** The sine-kernel limit from Weyl's formula. The gap probabilities as a Fredholm series, up to the point where the file cites Mehta for the second derivative. The characteristic-polynomial factorisation. Keating–Snaith's integer moments, including \(42/9!=1/8640\). The central limit theorem for \(\log|\det|\).

**Examples.** The \(2\times 2\) correlation, by hand. The moment \(42/9!\). A histogram of eigenvalue gaps against the sine kernel, labelled as a matrix computation.

**Figures.** One.

#### Chapter 12. Log-Correlated Fields and the Largest Values

**Status.** KEEP — `chapters/ch12-logcorrelated.tex` (445 lines). The tightness of \(\max\log|Z_n|-(\log n-\tfrac34\log\log n)\) is an admitted theorem, and the heading says so. Fyodorov–Hiary–Keating, for zeta, is not a theorem. Book 15 states it and points here for the matrix maximum.

**Hook.** How large does the characteristic polynomial of a random matrix get on the circle? How large does zeta get on a stretch of the critical line?

**Synopsis.** The branching random walk, log-correlated fields on the circle, multiplicative chaos, and the largest value of the characteristic polynomial. The branching-random-walk maximum \(c_*=\sqrt{2\log 2}\) is a theorem the exercises can own. The matrix maximum's second-order term is the admitted frontier. Zeta's maximum is a conjecture.

**Proved.** The branching-random-walk maximum of the strength the chapter proves. The first-order maximum of \(\log|Z_n|\), if that is what is proved; the second-order tightness stays admitted.

**Examples.** \(c_*=\sqrt{2\log 2}\), computed. One picture of a log-correlated field on the circle.

**Figures.** One.

#### Appendix B. Zeta and Random Matrices

**Status.** MOVE — `chapters/moments.tex` (506 lines). The moment-method semicircle goes to Book 8 with the semicircle theorem. The zeta story goes to Book 15, the meeting of structure and randomness. It does not stay here as a second telling, and it is not the geometry of a path. The mean square of \(\zeta(\sigma+it)\) for fixed \(\sigma>\tfrac12\) can stay as a lemma cited by Chapter 11, or move into that chapter's zeta section. Hardy–Littlewood and Ingham on the critical line stay quoted; Book 14 proves the critical-line mean square. The narrative that retells Chapter 11 is cut down to the citations. Book 15, Chapter 9, is the one-page comparison. This appendix does not remain a second telling.

**Hook.** Dyson, told a formula and answering that it was the pair correlation of eigenvalues.

**Synopsis.** After the move, what remains is the off-line mean square and a short pointer. The open doors are Book 15's, not a second workshop.

**Proved.** The mean square for \(\sigma>\tfrac12\) fixed, if it is not already a consequence of Book 5 and Book 6. Nothing about the critical line that Book 14 proves.

**Examples.** A numerical mean square off the line.

**Figures.** Two, if they still illustrate a theorem that remains.

## The old problem book

Book 6 is Crossroads. The old P1 problem book is removed by the renumbering branch. This plan does not place it again. Problems that cited the graph appendix follow the split: spectral gap and Ramanujan graphs to Book 8, the matrix-tree theorem stays with Networks.

## Owns, defers, hands forward

**Owns.** Kolmogorov continuity, Lévy's modulus, the Itô integral, Itô's formula, Lévy's characterisation, Girsanov for bounded drift, the Dirichlet problem, strong existence for Lipschitz SDEs, the Lévy–Itô decomposition after the measurability line, the electrical criterion, the graph-theoretic Riemann hypothesis in eigenvalue form, the semicircle, Marchenko–Pastur, a Wigner spike, the sine kernel, Keating–Snaith's integer moments, and the central limit theorem for \(\log|\det|\).

**Defers.** Novikov's condition, as a citation. Tracy–Widom. Bulk universality. \(p(s)=\mathrm d^2E(0;s)/\mathrm ds^2\), unless Book 15 proves the form-factor identity it needs. Montgomery's theorem (Book 14). The maximum of \(\log|\zeta|\) (stated in Book 15). The entrance of Dyson Brownian motion from a multiple eigenvalue.

**Hands forward.** The circulation. Book 14 proves the zero side of the picture this book drew. Book 15 refuses to prove either side again, and asks what the agreement means.

## Pages and effort

Baseline 228 pages. Target 230–250. Effort: moderate. The calculus can be taught as written. The work is the two overclaiming remarks, the Lévy–Itô measurability line, the semicircle's move, the Mehta sentence, and the thinning of Appendix B.
