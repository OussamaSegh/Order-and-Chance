# Volume 4 citations in Volumes 5–15

Authority is the printed order in `volume4-chance/main.tex` at `c13f836a`, with theorem-class environments sharing one counter per chapter and exercises on their own counter. Appendix B is the extremal chapter: `\appendix` then `\setcounter{chapter}{1}` then `\chapter`. Filenames are not the printed numbers. The old map that calls walks Chapter 7 is not used as a substitution table.

This file records the sweep. It is not a production acceptance. A distinct review of the mapping has not yet been returned. Volumes 1–3 were not edited.

## Printed homes used

| Current number | What the sentence is about |
| --- | --- |
| Theorem 4.2 | Hoeffding |
| Theorem 4.3 | Kolmogorov's inequality for bounded digit-block summands |
| Theorem 4.4 | Borel--Cantelli |
| Theorem 4.5 | Strong law, bounded case |
| Theorem 4.6 | Weierstrass, via Bernstein |
| Lemma 4.1 | Hoeffding's lemma |
| Theorem 5.9 | Dominated convergence for continuous integrands |
| Theorem 5.12 | Buffon's needle |
| Definition 6.1 | Convergence in distribution means the distribution functions converge at continuity points |
| Proposition 6.13 | Cycle count as independent Bernoulli$(1/k)$ summands |
| Proposition 2.3 | Fixed points tend to Poisson, with the inclusion--exclusion count |
| Theorem 6.10 | Lindeberg. Unchanged |
| Corollary 6.11 | Classical central limit theorem. Unchanged |
| Theorem 6.14 | Gaussian vectors |
| Exercise 6.1 | Slutsky. Unchanged |
| Exercise 6.4 | Cauchy characteristic function $e^{-\lvert t\rvert}$ |
| Exercise 6.5 | Poisson median tends to $1/2$. Unchanged |
| Exercise 6.8 | Cycle count is asymptotically normal |
| Proposition 7.1 | Gibbs |
| Theorem 8.1 | Reflection, including $P(M_n\ge a)=P(S_n\ge a)+P(S_n>a)$ |
| Theorem 8.2 | Gambler's ruin |
| Proposition 8.4 | Expected visits $1/(1-f)$, infinite exactly when the walk returns almost surely |
| Theorem 8.5 | Pólya |
| Theorem 8.6 | Last visit, and the first-return probabilities $f_{2m}=u_{2m-2}-u_{2m}$ |
| Proposition 8.7 | Harmonic hitting probabilities |
| Exercise 8.8 | Voltage reading of that harmonic function |
| Exercise 9.6 | Top-to-random |
| Exercise 9.9 | Mean and variance of the number of rising sequences |
| Theorem 9.6 | Top-to-random: the deck at the coupon time is uniform, and the distance is at most the tail |
| Lemma 10.5 | Colouring |
| Theorem 10.4 | Conditional uniformity of Poisson arrivals |
| Theorem 10.12 | Le Cam |
| Theorem 11.3 | Optional stopping at a bounded time |
| Theorem 11.5 | Upcrossings |
| Theorem 11.9 | Azuma, one-sided |
| Definition 11.2 | Martingale on finite partitions |
| Definition 12.1 | Brownian motion |
| Proposition 12.2 | Covariance $\min(s,t)$ |
| Theorem 12.4 | Lévy's existence |
| Proposition 12.5 | Scaling $c^{-1/2}B_{ct}$ and the inversion $tB_{1/t}$ |
| Theorem 12.7 | Quadratic variation |
| Theorem 12.10 | No finite derivative |
| Theorem 12.13 | Reflection: the maximum has the law of $\lvert B_t\rvert$ |
| Exercise 12.3 | Zero set |
| Exercise 13.4 | Crossing lemma |
| Chapter 3 | Catalan recurrence and the count of plane trees, written in the section, not as a numbered proposition |

Chebyshev's inequality and the weak law for uncorrelated variables are Volume 1, Chapter 10. The old pointers called them Volume 4, Proposition 4.1 or Theorem 4.2.

## Left unchanged on purpose

These sentences still name a result the current book does not prove. Changing the number would point at a different theorem. They are blockers, not silent edits.

- Fourier inversion as a numbered theorem. Current Theorem 6.8 is convergence of characteristic functions, not the inversion formula.
- The integral arcsine limit. Theorem 8.6 is the exact last-visit identity, and the chapter says the integral limit is not claimed.
- $P(S_1\ge0,\ldots,S_{2n}\ge0)=u_{2n}$ as a numbered theorem.
- $B_t^2-t$ as a numbered martingale proposition. The old tag Proposition 11.11 was left in the Donsker reminder.
- Almost-sure and $L^2$ convergence of an $L^2$-bounded martingale, including the identification $M_n=\mathbb E[M_\infty\mid\mathcal F_n]$. The chapter stops at a square-mean Cauchy criterion.
- Doob's inequality in the form $\lambda P(X^*\ge\lambda)\le\mathbb E X_n$ and $\mathbb E(X^*)^2\le4\mathbb E X_n^2$. Theorem 11.8 is the $L^2$ maximal inequality $P(\max\lvert X_k\rvert\ge a)\le\mathbb E[X_n^2]/a^2$.
- Uniform integrability, Pólya's urn, the mean waiting time 6 for HH, and the bounded-difference inequality with the factor 2, as numbered theorems.
- The general conditional expectation on a $\sigma$-algebra, and "taking out what is known" as a separate proposition. Definition 11.1 is the finite-partition formula.
- The riffle model, the $a$-shuffle formula, composition of riffles, the distances 0.614 and 0.334, monotonicity of total variation, the untouched-card lower bound for random transpositions, and the eigenvalue computation for the lazy cycle. None of these is a numbered result in the current Chapter 9.
- Full van der Waerden. Theorem B.6 is two colours and progressions of length three.
- Cayley's formula as a theorem of the probabilistic-method chapter.
- The general Bernoulli rate function $I_p$ as a numbered theorem. Chapter 4 computes the fair-coin exponent in an unnumbered example.
- Joint measurability of $(t,\omega)\mapsto B_t$ as part (a) of the zero-set exercise. Exercise 12.3 has no parts.

Kolmogorov's inequality is now cited as Theorem 4.3. That theorem assumes bounded summands built from digit blocks. Downstream sentences that apply it to unbounded variables still overshoot the hypotheses.
