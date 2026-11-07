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
| One-variable derivative and Riemann integral, fundamental theorem, substitution, integration by parts, improper integrals, Taylor with Lagrange remainder | Ch. 1 (Buffon), Ch. 5 | Vol. 1, *Differential and Integral Calculus* | One-variable theory. The Gaussian integral is proved there **without** polar coordinates | Iterated integrals on rectangles, and the two changes of variables Vol. 4 needs, are proved in Ch. 5 |
| Stirling \(n!\sim\sqrt{2\pi n}(n/e)^n\) | Ch. 6 local theorem | Vol. 1, `thm:stirling` | The limit with the constant | None |
| \(\int_{-\infty}^{\infty}e^{-x^2/2}\,\mathrm dx=\sqrt{2\pi}\) | Ch. 5, normal density | Vol. 1, `prop:gaussianintegral`, scaled | The value | The normal **density** is defined in Vol. 4 |
| Finite probability, conditional probability, Bayes, mutual vs pairwise independence, expectation, linearity, indicators, variance, covariance | Ch. 1, as a reminder with citations, then used | Vol. 1, *First Probability*, `prop:proba` | Finite spaces | Countable spaces are in the same chapter; infinite sequences of trials are not. Vol. 4 builds them |
| Bernoulli, binomial, hypergeometric, uniform on \(\{1,\ldots,n\}\) | Ch. 2 | Vol. 1, `prop:laws` | Masses, means, variances | Poisson **limit** of the binomial is not in Vol. 1. The Poisson **masses** are an example there. The limit is proved in Vol. 4 |
| Markov, Chebyshev, weak law for pairwise i.i.d. with finite variance | Ch. 4, cited, then sharpened | Vol. 1, `thm:chebyshev`, `thm:wlln` | The finite-\(n\) inequalities | Chernoff, Hoeffding, Borel–Cantelli, and a strong law are new |
| Geometric waiting, tail sum \(\mathbb E T=\sum_{j\ge0}P(T>j)\), Poisson mean and variance | Ch. 2 | Vol. 1, *Waiting times* | Countable spaces with an absolutely convergent series of masses. Explicitly **not** an infinite sequence of trials | Coupon collector is an exercise in Vol. 1. Vol. 4 proves it in the text |
| Spectral theorem for real symmetric matrices, orthogonal projection | Ch. 6, Gaussian vectors; Ch. 8 only if a quadratic form appears | Vol. 1, `thm:spectral`, `thm:gramschmidt` | Proved. The linear-algebra chapter says later exercises that need the spectral theorem should say so. Vol. 4 says so at the first use | None |
| Complex numbers and roots of unity | Only if a walk on roots of unity is stated | Vol. 1, *Complex Numbers and Roots of Unity* | The algebra | The old workshop problem `pb:rootwalk` is off the logical path, so this row is unused by the main text |
| Orders, Dilworth, Sperner | Not used | Vol. 1, *Orders* | Already moved out of Volume 4 | Do not bring the appendix back |

## From Volume 2

The main path does not need a theorem of Volume 2. Primes and congruences are not a step in any proof. A remark may point at the primes as a later use of Borel–Cantelli; the remark is not a premise.

## From Volume 3

Permutations are treated as bijections of a finite set, which Volume 1 already counts. The character theory of \(S_n\), Jordan form, and Perron’s theorem for positive matrices are **not** used. Finite Markov convergence is proved by coupling. The riffle-shuffle cutoff of Bayer–Diaconis is not claimed as a theorem. Rising sequences of a random permutation are counted directly.

## Taught in Volume 4 before use

| Tool | Taught in | Used from | Notes |
| --- | --- | --- | --- |
| Binary digits of one uniform; finite-bit events; outer content; almost sure as outer content zero | Ch. 1 | Ch. 4 Borel–Cantelli, Ch. 5 independent sequences, Ch. 6 strong law, Ch. 11 Lévy’s construction | This replaces the old “admitted infinite product” |
| Ballot theorem | Ch. 1 | Ch. 1 Exercise 1.7, Ch. 7 reflection for the walk | |
| Buffon’s probability for \(\ell\le d\) | Ch. 1 | Cited by Vol. 9 as the needle case | The model (independent uniform position and angle) is stated as the experiment |
| Absolute convergence of expectations on countable spaces, beyond Vol. 1’s reminder | Ch. 2, short | Generating functions, Poisson limit | |
| Poisson limit of binomial laws | Ch. 2 | Ch. 9 | |
| Expected number of cycles \(H_n\), coupon collector \(nH_n\) | Ch. 2 | Ch. 8 top-to-random | |
| Probability generating functions, extinction of a Galton–Watson process | Ch. 3 | Ch. 3 exercises, Ch. 12 giant-component remark only as a pointer | The fixed-point argument uses the intermediate-value theorem and continuity of power series from Vol. 1 |
| Binomial series for \((1-4x)^{-1/2}\) | Ch. 3, Exercise 3.7 | Vol. 5 cites Exercise 3.7 | |
| Chernoff and Hoeffding | Ch. 4 | Vol. 5 and Vol. 6 cite Chapter 4 | |
| Borel–Cantelli, both lemmas, at the strength of finite-bit events | Ch. 4 | Strong law, Lévy construction, random graphs | |
| Strong law for bounded i.i.d. variables, and the fourth-moment strong law | Ch. 4 (bounded), Ch. 6 (fourth moment) | Vol. 7 cites a strong law in Chapters 4 and 6 | The first-moment strong law is not claimed. Volume 11 owns it |
| Bernstein polynomials and Weierstrass on a segment | Ch. 4 | Vol. 6 cites Weierstrass in Chapter 4 | |
| Shannon entropy for a finite alphabet, Gibbs’ inequality | Ch. 4 | Gilmer section if restored; otherwise the source-coding bound for a fair coin is the application | |
| Distribution functions, densities, expectation as an improper integral | Ch. 5 | Ch. 6–11 | |
| Iterated integrals of continuous functions on a rectangle, and Fubini in that class | Ch. 5 | Joint densities, Box–Muller, gaps of a Poisson process | Not a general Tonelli theorem |
| Inverse distribution function; countably many independent uniforms and normals | Ch. 5 | Ch. 9, Ch. 11 | |
| Dominated convergence for continuous integrands with a continuous integrable dominant | Ch. 5 | Differentiation under the integral in Ch. 6 | Not the Lebesgue theorem |
| Modes of convergence; Slutsky | Ch. 6, Exercise 6.1 is Slutsky | Vol. 8 and Vol. 15 cite Exercise 6.1 | |
| Lindeberg’s theorem for \(C^3\) test functions by swapping | Ch. 6, environment 6.10 | Vol. 11 cites Theorem 6.10 | Convergence of distribution functions is deduced by mollification, proved in the chapter |
| Characteristic functions, and the easy implication “convergence in distribution implies pointwise convergence of characteristic functions” | Ch. 6 | Vol. 11 cites that direction | Lévy’s continuity theorem is not claimed |
| Local de Moivre–Laplace; Stirling’s constant read back from the local theorem only as a check, not as a new proof of Stirling | Ch. 6 | Vol. 5 cites de Moivre–Laplace | Stirling itself stays Volume 1’s theorem |
| Gaussian vectors with a given covariance | Ch. 6 | Ch. 11 | Uses `thm:spectral` |
| Reflection, gambler’s ruin, discrete arcsine law, Pólya’s theorem | Ch. 7 | Vol. 12 cites Pólya in Chapter 7 | Dimension 2 uses the local binomial estimate from Ch. 6 |
| Dirichlet’s principle for a finite graph, as Exercise 7.8 | Ch. 7 | Vol. 12 cites Exercise 7.8 | Linear equations, Vol. 1 |
| Finite irreducible aperiodic chains: stationary law, total variation, coupling | Ch. 8 | Vol. 11 shuffling chapters cite Chapter 8 | |
| Top-to-random stationary time, Exercise 8.6; rising-sequence mean \((n+1)/2\) and variance \((n+1)/12\), Exercise 8.8 | Ch. 8 | Vol. 15 and Vol. 11 | |
| Exponential law, Poisson process, colouring lemma (environment 9.5), thinning, inspection paradox, M/M/1 | Ch. 9 | Vol. 12 cites Lemma 9.5 | |
| Conditional expectation given a finite partition; optional stopping under stated bounds; Doob’s inequality; Azuma | Ch. 10 | Vol. 11 cites discrete martingales; Vol. 15 cites \(L^2\) convergence for a bounded example | Uniform integrability and the general tower property over an arbitrary \(\sigma\)-algebra are Volume 7 / Volume 11 |
| Brownian motion by Lévy’s interpolation, environments 11.4 and 11.12 | Ch. 11 | Vol. 11 and Vol. 12 | Existence uses the Gaussians of Ch. 5 and Borel–Cantelli from Ch. 4. Itô’s integral as a process is Volume 12. A first dyadic Itô expansion is proved here and labelled as that |
| First and second moment methods, symmetric Lovász local lemma, Erdős’s Ramsey bound | Ch. 12 | The method is the handover to later probabilistic number theory | “With high probability” is defined before it is used |
| Euler’s formula for a connected plane graph, Turán, Ramsey, Schur | Appendix, and Euler before Exercise 12.4 | Exercise 12.4 is the crossing lemma, cited by Vol. 14 and Vol. 15 | Euler is proved in the appendix or in Ch. 12 before the exercise, not assumed |

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

## Exercise-number contract

These printed numbers are cited from later volumes. The new exercises in these slots must still prove the stated fact.

| Number | Fact the later books use |
| --- | --- |
| 1.7 | Catalan number \(C_n=\frac1{n+1}\binom{2n}n\) counts Dyck paths |
| 2.6 | A uniform permutation of \(2n\) elements has a cycle longer than \(n\) with probability \(H_{2n}-H_n\to\ln 2\). The hundred-prisoners strategy may stay in the same exercise |
| 3.7 | \(\binom{-1/2}{j}(-4)^j=\binom{2j}{j}\) and the series for \((1-4x)^{-1/2}\) |
| 5.7 | The Cantor distribution: continuous distribution function, singular, supported on the middle-thirds set |
| 6.1 | Slutsky’s lemma |
| 6.7 | Cycle count of a random permutation, centred by \(\ln n\) and scaled by \(\sqrt{\ln n}\), converges in law to \(N(0,1)\) |
| 7.8 | Voltages and effective resistance for the simple random walk on a finite connected graph |
| 8.6 | Top-to-random shuffle: a strong stationary time with the coupon-collector law, and the total-variation bound \(d(n\ln n+cn)\le e^{-c}\) |
| 8.8 | A uniform permutation has mean \((n+1)/2\) and variance \((n+1)/12\) rising sequences |
| 11.3 | Zeros of a Brownian path on \([0,1]\): closed, Lebesgue measure zero almost surely, \(0\) not isolated, hence uncountable |
| 12.4 | Crossing lemma: \(\operatorname{cr}(G)\ge m-3n\), and \(\operatorname{cr}(G)\ge m^3/(64n^2)\) when \(m\ge 4n\) |
