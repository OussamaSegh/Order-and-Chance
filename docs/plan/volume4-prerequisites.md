# Volume 4 prerequisite register

The reader has Volumes 1–3 only. A row is a tool the new Volume 4 uses. “Source” is the place that actually proves it, checked in the manuscript, not inferred from a title. “Bridge” is empty when that source is enough at the strength we use.

Volume 1 chapter numbers below are the printed numbers: Language is Chapter 0 because `main.tex` sets the counter to \(-1\) before it. Calculus is the chapter *Differential and Integral Calculus*. First Probability is the last numbered chapter of Volume 1.

## From Volume 1, used as proved

| Tool | First use in the new Volume 4 | Source | What the source gives | Bridge |
| --- | --- | --- | --- | --- |
| Sets, quantifiers, induction, proof by bijection | Ch. 1 | Vol. 1, Ch. 0, *The Language of Mathematics* | The working language | None |
| Binomial theorem, binomial coefficients, \(\sum k\), \(\sum k^2\) | Ch. 1 | Vol. 1, *Sums, Binomials and Induction* | Identities with proofs | None |
| Inclusion–exclusion | Ch. 1 exercises, Ch. 2 | Vol. 1, `thm:incexc` in *Counting and Discrete Reasoning* | The counting form | None |
| Catalan paths as a count | Ch. 1, Exercise 1.7, proved again from the ballot theorem | Vol. 1 counting exercise on paths that stay under the diagonal | A count, not the probability form | Ballot theorem is proved in Vol. 4 before the exercise |
| Sequences, limits, \(e^x\), \(\ln\), comparison, absolute convergence, rearrangements of nonnegative series | Ch. 1 onward | Vol. 1, *Sequences, Series and Limits* | Those theorems, including Bolzano–Weierstrass in \(\mathbb R\) and the intermediate-value theorem | Bolzano–Weierstrass in the simplex \(\mathbb R^d\) is proved in Vol. 4, Ch. 8, from the one-dimensional case |
| \(1-x\le e^{-x}\), Jensen, Cauchy–Schwarz, Hölder | Ch. 1, Ch. 4 | Vol. 1, `prop:convex`, `thm:jensen`, `thm:cs` | Proved for the stated domains | None |
| One-variable derivative and Riemann integral, fundamental theorem, substitution, integration by parts, improper integrals, Taylor with Lagrange remainder | Ch. 5 (Buffon and continuous calculus) | Vol. 1, *Differential and Integral Calculus* | One-variable theory. The Gaussian integral is proved there **without** polar coordinates | Iterated integrals on rectangles, and the two changes of variables Vol. 4 needs, are proved in Ch. 5 |
| Stirling \(n!\sim\sqrt{2\pi n}(n/e)^n\) | Ch. 6 local theorem | Vol. 1, `thm:stirling` | The limit with the constant | None |
| \(\int_{-\infty}^{\infty}e^{-x^2/2}\,\mathrm dx=\sqrt{2\pi}\) | Ch. 5, normal density | Vol. 1, `prop:gaussianintegral`, scaled | The value | The normal **density** is defined in Vol. 4 |
| Finite probability, conditional probability, Bayes, mutual vs pairwise independence, expectation, linearity, indicators, variance, covariance | Ch. 1, as a reminder with citations, then used | Vol. 1, *First Probability*, `prop:proba` | Finite spaces | Countable spaces are in the same chapter; infinite sequences of trials are not. Vol. 4 builds them |
| Bernoulli, binomial, hypergeometric, uniform on \(\{1,\ldots,n\}\) | Ch. 2 | Vol. 1, `prop:laws` | Masses, means, variances | Poisson **limit** of the binomial is not in Vol. 1. The Poisson **masses** are an example there. The limit is proved in Vol. 4 |
| Markov, Chebyshev, weak law for pairwise i.i.d. with finite variance | Ch. 4, cited, then sharpened | Vol. 1, `thm:chebyshev`, `thm:wlln` | The finite-\(n\) inequalities | Chernoff, Hoeffding, Borel–Cantelli, and a strong law are new |
| Geometric waiting, tail sum \(\mathbb E T=\sum_{j\ge0}P(T>j)\), Poisson mean and variance | Ch. 2 | Vol. 1, *Waiting times* | Countable spaces with an absolutely convergent series of masses. Explicitly **not** an infinite sequence of trials | Coupon collector is an exercise in Vol. 1. Vol. 4 proves it in the text |
| Spectral theorem for real symmetric matrices, orthogonal projection | Ch. 6, Gaussian vectors | Vol. 1, `thm:spectral`, `thm:gramschmidt` | Proved. The linear-algebra chapter says later exercises that need the spectral theorem should say so. Vol. 4 says so at the first use | None |
| Complex numbers and roots of unity | Only if a walk on roots of unity is stated | Vol. 1, *Complex Numbers and Roots of Unity* | The algebra | The old workshop problem `pb:rootwalk` is off the logical path, so this row is unused by the main text |
| Orders, Dilworth, Sperner | Not used | Vol. 1, *Orders* | Already moved out of Volume 4 | Do not bring the appendix back |

## From Volume 2

The main path does not need a theorem of Volume 2. Primes and congruences are not a step in any proof. A remark may point at the primes as a later use of Borel–Cantelli; the remark is not a premise.

## From Volume 3

Permutations are treated as bijections of a finite set, which Volume 1 already counts. The character theory of \(S_n\), Jordan form, and Perron’s theorem for positive matrices are **not** used. Finite Markov convergence is proved by coupling. The riffle-shuffle cutoff of Bayer–Diaconis is not claimed as a theorem. Rising sequences of a random permutation are counted directly.

## Taught in Volume 4 before use — current fourteen-chapter edition

This table uses **printed chapter numbers**, not historical source filenames. The source chapter file `ch07-walks.tex` prints as Chapter 8, `ch08-markov.tex` as Chapter 9, `ch09-poisson.tex` as Chapter 10, and so forth. Where later volumes carry older references, audit the actual citation separately; a planning table does not fix published text.

| Tool | Proved/taught in current V4 | Used later | Required limit of the claim |
| --- | --- | --- | --- |
| Infinite fair-bit stream, finite cylinders and outer content | Ch. 1 | Ch. 4 Borel–Cantelli; Ch. 5 countable uniforms; Ch. 6 strong law; Ch. 12 Brownian construction | Does not assume a general measure-extension theorem |
| Ballot theorem | Ch. 1 | Ch. 1, Exercise 1.7; Ch. 8 walk reflection | Finite path counting |
| Bertrand models and Buffon's needle for \(\ell\le d\) | **Ch. 5** (nested `ch05-geometric.tex`) | Later geometric probability references | Not in Ch. 1; models distinguish three ways to select a chord |
| Absolute convergence of countable expectations | Ch. 2 | PGFs, Poisson limit | Nonnegative vs absolutely summable assumptions matter |
| Poisson limit of binomial laws | Ch. 2 | **Ch. 10** Poisson process | Poisson masses were already introduced in V1 |
| Cycle counts \(H_n\), coupon collector \(nH_n\) | Ch. 2 | **Ch. 9** top-to-random | Don't confuse cycle mean with record indicators |
| Probability generating functions, Galton–Watson extinction | Ch. 3 | Ch. 3 exercises; Ch. 14 graph comparison | Extinction root and its degeneracies proved |
| Binomial series \((1-4x)^{-1/2}\) | Ch. 3, Exercise 3.7 | Volume 5 | Coefficient identity proved in solution |
| Chernoff/Hoeffding, Borel–Cantelli, strong law for bounded independent variables | Ch. 4 | Ch. 6; Ch. 12 dyadic construction; later volumes | Distinguish bound, limit and a.s. statement |
| Bernstein-polynomial Weierstrass proof | Ch. 4 | Volume 6 | Main theorem on a compact interval |
| Distribution functions/densities, quantiles, integral bounds, finite rectangle Fubini, Box–Muller | Ch. 5 | Ch. 6 Gaussian; Ch. 10 continuous gaps; Ch. 12 independent normal increments | No imported general Fubini–Tonelli theorem |
| Modes of convergence, Slutsky and fourth-moment strong law | Ch. 6, Exercise 6.1 for Slutsky | Later analysis/probability | The fourth-moment theorem does not imply the general first-moment SLLN |
| Fourier uniqueness/inversion, characteristic functions | Ch. 6, Theorem 6.8 (`thm:inversion`) | Later probability | No Lévy continuity theorem assumed |
| Lindeberg CLT and classical finite-variance CLT | Ch. 6, Theorem 6.10 (`thm:lindeberg`) | Volume 11 | C³ smooth-test form and explicit distribution-function sandwich |
| Local de Moivre–Laplace, Gaussian vectors | Ch. 6 | Ch. 12 Brownian; later approximations | Stirling and spectral theorem are V1 results |
| Entropy, Gibbs/KL, Kraft, Huffman, typical sequences, block codes | **Ch. 7** | Later coding/information sections | Shannon entropy no longer belongs to Ch. 4 |
| Walk reflection, gambler's ruin, recurrence/Pólya, discrete arcsine, finite resistor networks | **Ch. 8** | Later walks; Ch. 9 chains | The main-walk chapter is not Ch. 7 |
| Dirichlet's principle / effective resistance problem | Ch. 8, Exercise **8.8** (`ex:electric`) | Later electrical-network references | Former “Exercise 7.8” contract was superseded |
| Finite Markov mixing via coupling, stationary law, TV; top-to-random stationary time | **Ch. 9** | Later chains/shuffling | Top-to-random Exercise **9.6**, not 8.6 |
| Bayer–Diaconis exact riffle-shuffle formula | Ch. 9, `thm:bayerdiaconis` | Historical seven-shuffle explanation | Finite exact formula and three-decimal values; do not claim literal \(d_k=1\) |
| Rising-sequence mean and variance | Ch. 9, Exercise **9.8** (`ex:risingmean`) | Later permutation examples | Former “Exercise 8.8” contract was superseded |
| Exponential clock, Poisson counts, thinning, inspection paradox and M/M/1 | **Ch. 10** | Later stochastic-process work | One-sided and stationary two-sided clocks must be distinguished |
| Poisson independent colouring | Ch. **10**, Lemma **10.5** (`lem:colouring`) | Later volumes | Former “Lemma 9.5” numbering is stale |
| Finite-partition martingales, bounded stopping, Doob, Azuma, convergence | **Ch. 11** | Later general martingale theory | General sigma-algebra/continuous-filtration results not imported |
| Brownian motion via dyadic Lévy construction and reflection | **Ch. 12**, Theorems **12.4** and **12.12** (`thm:levy`, `thm:reflection`) | Later continuous martingales | Independent Gaussian increments, not a general Itô integral |
| First/second moment methods, local lemma, Euler/crossing lemma | **Ch. 13**, Exercise **13.4** (`ex:crossing`) | Volumes 14–15 | Euler is established before the crossing exercise |
| \(G(n,c/n)\), subcritical component upper bound and triangle thresholds | **Ch. 14** | Final Volume 5 handoff | Does not claim the complete supercritical giant-component theorem |
| Turán, Ramsey, Schur, EKR and finite van der Waerden | **Appendix B** | Later-extremal references | Appendix stays **B**, not A |

## Explicitly off the logical path

| Item | Why |
| --- | --- |
| General Lebesgue measure, Vitali sets as a **construction we integrate**, Dynkin’s \(\pi\)-\(\lambda\) theorem as a working tool, Carathéodory extension | Not needed once probabilities are carried by intervals, finite-bit events, and continuous densities. Vitali’s negative statement may be told as a warning, with the axiom of choice named, and is not used to prove a positive theorem |
| Fubini–Tonelli for arbitrary nonnegative measurable functions | Replaced by iterated integrals of continuous functions, proved before use |
| Lévy’s continuity theorem, Berry–Esseen, Donsker’s theorem | Named, if at all, as belonging to Volume 11. Not a step |
| Itô integral | Volume 12. Chapter 11 stops at a dyadic expansion |
| Bayer–Diaconis seven-shuffle profile | Not proved. Top-to-random is proved. A sentence may quote the seven-shuffle story as history and must not use it as a lemma |
| Strong law from a first moment only | Volume 11 |
| The old `pb:*` workshop list | See the old-to-new map |
| Any theorem of Volumes 5–15 | A forward sentence may name the next question. It may not fill a gap |

## Current exercise-number contract (verified against `main.tex` order)

Later-volume citations must use the **current printed numbering** (not historical chapter filenames or the old twelve-chapter plan) and stable `\label` anchors. This register records current positions; it does not attest that Volumes 5–15 have already been migrated.

| Printed exercise / lemma | Stable label | Fact or use |
| --- | --- | --- |
| 1.7 | `ex:catalan` | Catalan number counts Dyck paths |
| 2.6 | `ex:prisoners` | Long-cycle probability \(H_{2n}-H_n\to\ln 2\); hundred-prisoners application |
| 3.7 | `ex:binseries` | \((1-4x)^{-1/2}\) coefficient identity |
| 5.7 | `ex:cantor` | Continuous singular Cantor law on middle-thirds set |
| 6.1 | `ex:slutsky` | Slutsky's lemma |
| **6.8** | `ex:cyclesclt` | Normal limit for centred/scaled permutation cycle count |
| **8.8** | `ex:electric` | Finite-graph effective resistance and harmonic voltages |
| **9.6** | `ex:toptorandom` | Top-to-random strong stationary time / coupon collector |
| **9.8** | `ex:risingmean` | Mean \((n+1)/2\), variance \((n+1)/12\), rising sequences |
| **10.5** (lemma) | `lem:colouring` | Independent Poisson colouring lemma |
| **12.3** | `ex:zeros` | Brownian zero set: closed, a.s. null, uncountable |
| **13.4** | `ex:crossing` | Crossing lemma \(\mathrm{cr}(G)\ge m-3n\), and \(\mathrm{cr}(G)\ge m^3/(64n^2)\) for \(m\ge4n\) |

**Unchanged protected theorem slots:** Theorem 6.8 (`thm:inversion`), Theorem 6.10 (`thm:lindeberg`), Theorem 11.9 (`thm:doob`), Theorem 11.10 (`thm:azuma`), Theorem 12.4 (`thm:levy`), Theorem 12.12 (`thm:reflection`), Appendix B. Update downstream citations through reviewed independent PRs; do not edit published Volumes 1–3.
