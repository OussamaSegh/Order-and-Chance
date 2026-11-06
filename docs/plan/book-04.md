# Book 4 — Chance

*The Logic of Uncertainty.*

**Element.** A probability is a model you choose before you compute. Once the model is written, the load of a sum, a wait, or a path is a theorem.

**Source.** `volume4-chance`. Fourteen chapters in four parts, and Appendix B (extremal problems). Owner approval of 6 November 2026. The citation migration is `docs/plan/volume4-citation-migration.md`. The sections after the chapter list below are the earlier twelve-chapter notes; where they disagree with this list, this list wins.

## Architecture

| Part | Question | Chapters |
| --- | --- | --- |
| I. The Language of Chance | How do we describe a random experiment? | 1 From Games to Probability Spaces; 2 Random Variables and Their Laws; 3 Generating Functions and Random Families |
| II. The Laws of Uncertainty | Why does randomness become predictable? | 4 Concentration and the Laws of Large Numbers; 5 Continuous Chance; 6 Why the Bell Curve Appears; 7 Entropy, Codes and Typical Sequences |
| III. Chance in Motion | What changes when randomness evolves in time? | 8 Random Walks; 9 Markov Chains and Mixing; 10 The Poisson Clock; 11 Martingales and Fair Games; 12 Brownian Motion |
| IV. Chance Reveals Structure | Can chance prove a deterministic theorem? | 13 The Probabilistic Method; 14 Random Graphs and the Search for Structure |

Bertrand's paradox and Buffon's needle are in Chapter 5. Entropy is Chapter 7, not a section of Chapter 4. The Volume 5 handoff is at the end of Chapter 14. Lindeberg remains Theorem 6.10. Colouring is Lemma 10.5. Brownian existence is Theorem 12.4 and reflection is Theorem 12.12. Crossing is Exercise 13.4.

## Promise

Counting settles a question only after the experiment is named. The same rules produce the law of large numbers, the central limit theorem, the convergence of a finite Markov chain, a martingale stopped at a bounded time, and a Brownian path built from explicit Gaussians. The Gaussian integral of Volume 1 becomes the law of one coordinate, and then the shape of a sum of many small independent pieces. The probabilistic method turns an expectation into a proof that an object exists. That move is the one Volumes 14 and 15 use when they talk about the primes.

## Prerequisites

Volume 1, as proved there: counting and inclusion–exclusion, sequences and series, one-variable calculus, Stirling’s formula, the Gaussian integral, Jensen and Cauchy–Schwarz, finite and countable probability, Markov, Chebyshev, the weak law, and the spectral theorem for real symmetric matrices. Volumes 2 and 3 are not a step on the main path. Measure theory is not a prerequisite and is not an unproved lemma. What this book needs beyond Volume 1 is built in the chapter that uses it. The register lists every row.

## Earlier twelve-chapter notes

The part names and chapter blurbs below this heading are the previous contract. They are kept so the old-to-new notes remain readable. They are not the contents of `main.tex`.

## Parts (superseded)

| Part | Name | Chapters |
| --- | --- | --- |
| I | Discrete Probability | 1–4 |
| II | Limit Theorems | 5–6 |
| III | Random Structures | 7–12 and the extremal appendix |

### Chapter 1. Counting and Paradoxes

**Question.** When is a uniform count the right model, and what does one uniform number on \([0,1]\) already contain?

**Uses.** Volume 1 finite probability, inclusion–exclusion, one-variable integration.

**Introduces.** Binary digits as fair bits; outer content; almost sure as outer content zero. Bertrand’s three experiments. The ballot theorem. Buffon’s needle for \(\ell\le d\).

**Practice.** Own birthday, two children, repeated tests, Penney’s game, the \(n\)-door host, pairwise versus mutual independence, Dyck paths from the ballot theorem (Exercise 1.7).

**Why here.** Infinite sequences of trials are the one object Volume 1 explicitly postponed. Everything later that says “almost surely” points back to this section.

### Chapter 2. Discrete Random Variables

**Question.** How do you compute an average without listing the law?

**Uses.** Chapter 1 and Volume 1’s linearity, classical finite laws, geometric and Poisson masses.

**Introduces.** The Poisson limit of the binomial. The harmonic mean of the number of cycles. The coupon collector as a theorem.

**Practice.** Exercise 2.6 keeps the long-cycle probability \(H_{2n}-H_n\to\ln 2\) and the hundred prisoners.

**Why here.** Generating functions need a law to transform. Tails need a mean and a variance.

### Chapter 3. Generating Functions

**Question.** What does the function \(\mathbb E[s^X]\) know about a sum, and about a family name that may die out?

**Uses.** Power series and the intermediate-value theorem from Volume 1. Independence from Chapter 2.

**Introduces.** Probability generating functions, random sums, the extinction probability of a Galton–Watson process, the Catalan generating function.

**Practice.** Exercise 3.7 is the series for \((1-4x)^{-1/2}\).

**Why here.** The walk’s first-step equation in Chapter 7 is the same functional equation in another set of clothes.

### Chapter 4. Inequalities, Large Numbers and Entropy

**Question.** How small is a deviation, and does the average settle on almost every sequence?

**Uses.** Volume 1’s Markov, Chebyshev, weak law, and Jensen. The coin space of Chapter 1.

**Introduces.** Chernoff and Hoeffding. Both Borel–Cantelli lemmas. The strong law for bounded variables. Bernstein’s proof of Weierstrass’s theorem. Entropy of a finite alphabet and typical sequences.

**Practice.** A numerical tail for \(\mathrm{Bin}(1000,\tfrac12)\) beside the exact value. One independent Borel–Cantelli example.

**Why here.** The central limit theorem explains the shape. These inequalities do not need the shape, and the strong law needs Borel–Cantelli before Chapter 6.

### Chapter 5. Continuous Probability Done Properly

**Question.** A uniform point of \([0,1]\) equals \(\tfrac12\) with probability 0. What is an expectation, if it is no longer a sum?

**Uses.** Volume 1’s Riemann integral and Gaussian integral. The bit construction of Chapter 1.

**Introduces.** Distribution functions and densities. Iterated integrals of continuous functions. The changes of variables used for polar coordinates and for ordered arrival times. Independent normals from inverse distribution functions. Dominated convergence for continuous integrands. Box–Muller.

**Practice.** Exercise 5.7 is the Cantor distribution: continuous, singular, supported on a set of length zero.

**Why here.** Chapter 6’s bell curve is this density. The title stays, because “Chapter 5” in later volumes means this material. The chapter does not call a Riemann theorem Lebesgue’s.

### Chapter 6. Convergence and the Central Limit Theorem

**Question.** A hundred dice have mean 350. What is a usable estimate for the probability that the sum exceeds 400, given that \(6^{100}\) outcomes will not be listed?

**Uses.** Stirling and Taylor from Volume 1. Chapters 4 and 5. The spectral theorem, cited, for Gaussian vectors.

**Introduces.** Convergence in probability, almost surely, and in distribution. The fourth-moment strong law. Glivenko–Cantelli. Characteristic functions, in the direction later volumes quote. Lindeberg’s swapping theorem, as formal environment 6.10. The local de Moivre–Laplace theorem.

**Practice.** Exercise 6.1 is Slutsky. Exercise 6.7 is the Gaussian limit for the number of cycles.

**Why here.** This is the shape the cover draws. Random walks in the next chapter are sums of this kind.

### Chapter 7. Random Walks

**Question.** On the line, a walk returns. In space, it may leave and never come back. Which dimension is the change?

**Uses.** The ballot theorem, Stirling’s local estimate, Chapter 6.

**Introduces.** Reflection and the maximum. The discrete arcsine law. Gambler’s ruin. Pólya’s theorem. Harmonic functions on a finite graph.

**Practice.** Exercise 7.8 is the electrical network of the walk.

**Why here.** Markov chains are walks on a finite graph with unequal rates. Brownian motion is what the scaled walk is trying to become.

### Chapter 8. Markov Chains

**Question.** When does repeating a shuffle wash out the starting order, and how do you prove it without listing the group?

**Uses.** Finite matrices from Volume 1. Bolzano–Weierstrass in \(\mathbb R\), extended in this chapter to the simplex. Coupling. Chapter 2’s coupon collector.

**Introduces.** Irreducibility, period, stationary distributions, total variation, convergence of a finite irreducible aperiodic chain.

**Practice.** Exercise 8.6 is top-to-random. Exercise 8.8 is the mean and variance of the number of rising sequences.

**Why here.** The Poisson process is the continuous-time cousin. The chain is still finite, so no general ergodic theorem is required.

### Chapter 9. Poisson Processes

**Question.** Buses arrive at rate \(\lambda\). Why is the expected wait \(1/\lambda\), not half of that?

**Uses.** Chapter 5’s exponential density and the triangular change of variables. Chapter 2’s Poisson limit.

**Introduces.** Memorylessness. The Poisson process as exponential gaps. The colouring lemma, as formal environment 9.5. Thinning, superposition, the inspection paradox, Le Cam’s bound, the stationary mean of M/M/1 when the load is less than 1.

**Why here.** Martingales need a process that runs in time. The bus is the simplest one with a continuous clock.

### Chapter 10. Conditional Expectation and Martingales

**Question.** You have watched the tosses up to today. What is your estimate of tomorrow’s fortune, and when may you stop?

**Uses.** Finite partitions, Chapter 1’s sequences, orthogonal projection in \(\mathbb R^n\) from Volume 1.

**Introduces.** Conditional expectation given a finite partition. Martingales. Optional stopping under three stated conditions, and the walk that hits \(+1\) and breaks a careless use. Doob’s inequality. \(L^2\) convergence. Upcrossings. Azuma’s inequality.

**Practice.** The waiting time for ABRACADABRA.

**Why here.** Brownian motion is a continuous martingale. The optional-stopping habit has to be in the reader’s hands first, with a counter-example.

### Chapter 11. Brownian Motion

**Question.** Lévy’s broken line uses one normal random variable at each dyadic point. Does the uniform limit exist, and is the limit a Brownian motion?

**Uses.** Chapters 5, 6, and 10. Borel–Cantelli from Chapter 4.

**Introduces.** The definition by continuous paths and Gaussian increments. Lévy’s construction, as formal environment 11.4. Quadratic variation along dyadic partitions. The reflection principle, as formal environment 11.12. A dyadic Itô expansion. The binomial approximation of one Black–Scholes price, computed on a stated contract.

**Practice.** Exercise 11.3 is the zero set.

**Why here.** Volume 12 owns the integral. This chapter owes the path.

### Chapter 12. The Probabilistic Method

**Question.** How do you prove that a colouring or a graph exists when you cannot draw one?

**Uses.** Linearity, Chebyshev or the second moment, and the union bound. Euler’s formula, proved before the crossing lemma.

**Introduces.** The first and second moment methods, alteration, the symmetric Lovász local lemma, and the subcritical random graph. “With high probability”, defined in the chapter. Erdős’s bound \(R(k,k)>2^{k/2}\).

**Practice.** Exercise 12.4 is the crossing lemma.

**Why here.** The series returns to this move when a deterministic object is compared with a random model. The last pages name Volume 5, *Calculation: From Formula to Insight*, and one concrete object that book owns: a generating function used as a series, with a remainder.

### Appendix. Extremal Problems and Ramsey Theory

**Question.** Which patterns are forced once a graph or a colouring is large enough?

**Uses.** Double counting, the probabilistic method’s Ramsey bound, and nothing from Volumes 5–15.

**Introduces.** Turán’s theorem, Ramsey’s theorem, Schur, the sunflower lemma, and Katona’s proof of the Erdős–Ko–Rado theorem. Van der Waerden only with a complete proof.

**Why here.** It is the combinatorial wing of Chapter 12, not a second book on the primes.

## Owns, and what is left to later books

**Owns.** The bit model of repeated trials, conditioning as used above, the classical discrete laws and their Poisson limit, Galton–Watson extinction, Chernoff and Hoeffding, Borel–Cantelli, the strong law for bounded variables and under a fourth moment, densities and the continuous dominated-convergence theorem of Chapter 5, Lindeberg’s swapping theorem, Pólya’s theorem, finite Markov chains, the Poisson process, discrete martingales at the stated scope, Lévy’s Brownian motion, the probabilistic method, and the extremal appendix.

**Leaves to later books.** The first-moment strong law, Lévy’s continuity theorem, Berry–Esseen, Donsker’s theorem (Volume 11). Itô’s integral (Volume 12). The transposition cutoff and the riffle profile (Volumes 10, 11, and 15). General measure, general Fubini, and products of arbitrary probability spaces (Volume 7).

## Reading order

The order in `volume4-chance/main.tex` is the order of proof. An exercise may use the chapter it sits in and earlier chapters. It may not use a later chapter. A forward pointer inside an exercise is a sentence about where the idea returns, not a missing step.
