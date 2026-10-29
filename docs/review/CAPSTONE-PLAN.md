# Capstone plan: Volume 14, *Order and Chance*

This plan was written before the series was closed. The current catalog is
Volumes 0–14 plus Crossroads. Volume 14 is *Order and Chance: Where Number
Meets Randomness*. Part V and appendices A–L are inside that volume. There is
no separate workshop volume and no second or third problem book. Sentences
below that say the README still lists another title describe this plan’s
starting point, not the present tree.

*Where Number Meets Randomness.* This plan replaces the draft outline in the attached note and the unfinished book now on disk as `tome14-random` (*Random Arithmetic*, thirteen chapters, preface still “Preface to come”). It absorbs Volume 15, *The Research Workshop*, as Part V, and it assumes P2 and P3 will be folded into the main volumes by the restructuring already under way. It does not edit those sources.

The printed book follows the series rule: one mathematical story, exercises with hints and complete solutions, no promise of a notebook inside the text. The notebooks listed below are author-facing companions, one per chapter, in `python/tome14/`. They are experiments, not citations.

`common/series.tex` and the README still call this volume *Random Arithmetic* and still list Volume 15 as a separate book. `common/volume-subtitles.json` already has the subtitle *Where Number Meets Randomness*. The catalog has to be brought into line when the book is written. Until then, citations of “Volume 14” in Volumes 10 and 15 mean the draft, not this plan.

## What the draft already contains

The existing files are proofs, not an outline. They should be mined, not rewritten from a blank page, and they should not be copied in as chapters.

| Draft file | Use in this plan |
| --- | --- |
| `ch01-additive.tex`, Kubilius | The model half of Chapter 3. Do not reprint Volume 5’s Erdős–Kac. |
| `ch02-selbergdelange.tex` | The one analytic theorem Volume 10 already assigns to this volume. Prove it in Chapter 3. |
| `ch03-erdoskac.tex` | A comparison of proofs, one section, pointing at Volume 5, Chapter 9. |
| `ch04-anatomy.tex` | Dickman, friable integers: sections of Chapters 1 and 3. |
| `ch05-randommult.tex` | The Steinhaus and Rademacher models in Chapter 4. |
| `ch06-bohrjessen.tex`, `ch07-selberg.tex` | Chapter 11. These arguments are not in Volumes 0–13. |
| `ch08-moments.tex` | A bridge into Chapter 10. The characteristic-polynomial moments are already Volume 11, Chapter 11. |
| `ch09-bias.tex` | Chapter 13, beside Volume 5, Chapters 4 and 7. |
| `ch10-largemoduli.tex` | Only what is not already Bombieri–Vinogradov (Volume 13, Chapter 4). |
| `ch11-gaps.tex` | The working text of Chapter 2: Buchstab, Maier, and the Erdős–Rankin gap bound. Check the appeal to the draft’s own “Gallagher theorem” in `ch10-largemoduli.tex` before adopting it. |
| `ch12-polynomials.tex` | One section of Chapter 4 or an exercise. Random polynomials are not a chapter of this book. |
| `ch13-cohenlenstra.tex` | The moment calculations of Chapter 7. The heuristic stays a heuristic. |

## Shape of the book

Seventeen chapters and four appendices. Parts I–IV are the mathematics. Part V is the workshop, condensed from twelve chapters and twelve appendices to four chapters and four appendices. A chapter that only cites an earlier volume is too thin; a chapter that reproves Bombieri–Vinogradov or the sine kernel is too thick. The rule used below: prove a theorem here when Volumes 0–13 do not contain it and the argument is of a length this book can hold; state it when the proof is a paper, an admitted theorem, or a computation that is not on the page.

Standard references for the whole volume: Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*; Montgomery and Vaughan, *Multiplicative Number Theory I*; Granville’s notes on the distribution of primes; Soundararajan’s 2007 survey in *Equidistribution in Number Theory*.

### Dependency, in one table

| Chapter | Must already be theorems | Proved here | Stated, not proved |
| --- | --- | --- | --- |
| 1 | Vol. 5, Ch. 1–2, 9 | Normal orders, a precise meaning of “random-like” | Cramér’s model, in full |
| 2 | Vol. 5, Ch. 5 and 10; Vol. 13, Ch. 2–4 | Buchstab, Maier, Erdős–Rankin | Granville’s factor \(2e^{-\gamma}\); the FGKMT gap bound |
| 3 | Vol. 3, Ch. 6; Vol. 5, Ch. 9 | Turán–Kubilius, Kubilius, Selberg–Delange | — |
| 4 | Vol. 13, Ch. 10 | Steinhaus and Rademacher moments; Möbius against periodic sequences | Chowla; Sarnak beyond periodic sequences |
| 5 | Vol. 5, Ch. 10; Vol. 13, Ch. 1 | The second-moment calculation under Hardy–Littlewood, for pairs | Gallagher’s Poisson law (conditional); Montgomery–Soundararajan |
| 6 | Vol. 5, Ch. 8; Vol. 13, Ch. 3 | Inclusion–exclusion as expectation; parity in that language | Chen; any claim that the parity barrier is a theorem for twins |
| 7 | Vol. 12, Ch. 2–3 | The Cohen–Lenstra measure and its moments; one cokernel theorem | The heuristic for class groups; the 2-part |
| 8 | Vol. 12, Ch. 12 | The distribution of a random maximal isotropic subspace; 2-descent for one family | Goldfeld; Bhargava–Shankar; Poonen–Rains; BSD |
| 9 | Vol. 11, Ch. 11; Vol. 13, Ch. 14 | The comparison of the two form factors, on one page | GUE for \(\alpha\ge 1\); Odlyzko as a computation |
| 10 | Vol. 11, Ch. 11; Vol. 13, Ch. 14 | The dictionary between the two moment conjectures | Keating–Snaith for \(\zeta\); the CFKRS recipe |
| 11 | Vol. 4, Ch. 10; Vol. 5, Ch. 7; Vol. 10, Ch. 4 | Bohr–Jessen; Selberg’s approximation and his central limit theorem | The Fyodorov–Hiary–Keating conjecture |
| 12 | Vol. 13, Ch. 12–13 | The structure/randomness split on a Roth example, in this book’s language | Green–Tao |
| 13 | Vol. 5, Ch. 7 | The logarithmic-density computation under GRH and linear independence, or a clear citation if Volume 5 is judged to have proved it | Lemke Oliver–Soundararajan; Maier’s irregularities, by reference to Chapter 2 |
| 14–17 | Parts I–IV, as each project needs | The method pieces listed in Part V | The open problems those pieces sit beside |

## Part I. The question

### Chapter 1. Order and chance in the integers

**Aim.** Fix what “random-like” will mean for the rest of the book, before any model is built. A deterministic set can match the mean and the variance of a random model and still fail a short-interval test. The chapter ends with a list of statistics (normal order, Poisson counts, pair correlation, bias) that later chapters treat one at a time.

**Sections.**

1. Three deterministic sequences that look random: square-free integers, integers with a prime factor in \((y,z]\), and the primes. What is actually proved about each (Volume 5, Chapters 1 and 2).
2. Normal order. Turán’s second-moment bound for \(\omega(n)\) as a calculation, with the theorem postponed to Chapter 3. The distinction between normal order and almost-sure behaviour in a probability space.
3. Friable integers and the Dickman function, from the draft’s anatomy chapter, with the differential equation derived and the delay equation stated. Volume 10, Chapter 12, already meets Dickman through random permutations; cite it.
4. A glossary, one page: the statistics this book will use, each with the chapter that owns it and the volume that already proved the deterministic input.

**Prove.** The normal-order statement for \(\omega(n)\) can be quoted from Volume 5, Chapter 9, as the \(L^2\) half of Erdős–Kac, and re-proved in a page if the draft’s write-up is shorter. The Dickman delay equation for the continuous model.

**State.** Cramér’s model, as a definition, with the theorem-level consequences deferred to Chapter 2. Hardy–Littlewood, as a conjecture, one display.

**Draws on.** Volume 1, as it stands after the current rewrite: primes, arithmetic functions, and the statement of the fundamental theorem of arithmetic. Volume 3, Chapters 2 and 6: mean, variance, and what a central limit theorem says. Volume 5, Chapters 1 (Mertens), 2 (averages), and 9 (Erdős–Kac). Volume 10, Chapter 12 (permutations and Dickman).

**Figures.** A plot of \(\omega(n)\) against \(\log\log n\) up to \(10^5\), with the band of width \(\sqrt{\log\log n}\). The Dickman function \(\rho(u)\) on \([0,8]\), against the proportion of \(y\)-friable integers up to \(x\) for \(u=\log x/\log y\) in a short range.

**Exercises.** Six, in the series pattern. One-star: compute \(\omega(n)\) and \(\Omega(n)\) for \(n\le 30\) and see them differ. Two-star: the normal order of \(\log d(n)\), from Volume 5’s average of \(d(n)\). Three-star: derive \(\rho'(u)=-\rho(u-1)/u\) from the continuous friable model, including the value on \([0,1]\).

**Notebook.** `ch01-random-like`. Histogram of \(\omega(n)\) in dyadic segments, and a numerical Dickman function by the delay equation. The book text does not mention it.

**References.** Tenenbaum, Chapters I.3 and III.5. Granville, *The anatomy of integers and permutations* (for the parallel with Volume 10, not as a second foundation).

### Chapter 2. Models of the primes

**Aim.** Cramér’s model, the theorems it gets right, Maier’s theorem as a theorem of this book, and Granville’s repair as a conjecture with a precise prediction.

**Sections.**

1. The model: independent Bernoulli random variables with \(P(n\text{ prime})=1/\log n\) for \(n\ge 3\). Almost-sure consequences that are elementary probability (Volume 3, Chapter 4, the Borel–Cantelli lemmas): the prime-number theorem with probability 1, and the bound \(O((\log x)^{2+\varepsilon})\) on the gaps. Volume 5, Exercise on the short model, is the template.
2. What the model cannot see. The singular series, already Theorem (Gallagher) in Volume 5, Chapter 10: the average of \(\mathfrak S(H)\) tends to 1. State the Hardy–Littlewood conjecture and Gallagher’s conditional Poisson law in one page, and point at Chapter 5 for the variance.
3. Buchstab’s function, proved. Volumes 0–13 do not contain this theorem. Volume 5, `ch10-random.tex:275`, refers to it as already met in the sieve chapter; it is not defined there. Volume 13, Chapter 3, draws \(\omega(u)\) and proves the fundamental lemma for large \(u\). The draft’s `ch11-gaps.tex` proves \(\Phi(x,z)=\omega(u)\,x/\log z+O_U(x/\log^2 z)\) for \(u\le U\). Adopt that proof.
4. Maier’s theorem, proved, from the same draft chapter. The matrix of intervals at multiples of \(P(z)\). The draft’s write-up calls on a weighted prime-number theorem in arithmetic progressions (“Gallagher’s theorem” in the draft’s Chapter 10), arranged so that the modulus has no exceptional zero by deleting at most one prime. Replace that appeal by Volume 13’s Siegel–Walfisz or Bombieri–Vinogradov, or keep it and write the zero-free hypothesis in the statement. The limsup and liminf for every \(\lambda>1\). The same chapter of the draft proves the Erdős–Rankin lower bound \(G(X)\gg (\log X\log_2 X\log_4 X)/(\log_3 X)^2\). That proof is elementary once Buchstab and the prime-number theorem are known, and it belongs here.
5. Granville’s refinement: let the cutoff grow. State his prediction that \(\limsup(p_{n+1}-p_n)/(\log p_n)^2\ge 2e^{-\gamma}\). The stronger lower bound of Ford–Green–Konyagin–Maynard–Tao is quoted in the draft and uses either Green–Tao or Maynard’s weights; leave it quoted. One paragraph on Maynard’s bounded gaps (Volume 13, Chapter 9) as the opposite end of the same scale.

**Prove.** The Borel–Cantelli gap bound in the model. Buchstab’s theorem for \(u\) in a fixed range. Maier’s theorem. The Erdős–Rankin lower bound, in the form the draft proves. Name the ineffective constant if the argument uses Siegel–Walfisz.

**State.** Granville’s prediction \(\limsup(p_{n+1}-p_n)/(\log p_n)^2\ge 2e^{-\gamma}\). The Ford–Green–Konyagin–Maynard–Tao bound. The Hardy–Littlewood conjecture. Gallagher’s Poisson law, as a conditional theorem whose hypothesis is the uniform Hardy–Littlewood conjecture already written in Volume 5, Chapter 10. Do not drop the hypothesis.

**Draws on.** Volume 5, Chapters 5 and 10 (the prime-number theorem, Cramér’s model, Gallagher’s average of the singular series, and the sketch of Maier at lines 269–276, which this chapter replaces). Volume 13, Chapters 2 (Siegel–Walfisz), 3 (the fundamental lemma, as the large-\(u\) companion of Buchstab, not as a substitute), 4 (Bombieri–Vinogradov, if that is the form adopted), and 9 (bounded gaps). Volume 3, Chapter 4 (Borel–Cantelli). The draft file `tome14-random/chapters/ch11-gaps.tex`.

**Missing from Volumes 0–13.** Buchstab’s theorem, and a complete proof of Maier’s theorem. Do not cite Volume 5’s sketch, or its phrase “met in sieve theory,” as a theorem.

**Figures.** The Poisson histogram Volume 5 already draws near \(10^9\), redrawn with the variance defect marked, and a pointer to Chapter 13. A schematic of Maier’s matrix: rows are residue classes modulo \(P(z)\), and two rows whose Buchstab weights sit on opposite sides of 1.

**Exercises.** The model’s almost-sure short-interval count for \(\lambda>2\) (Volume 5’s exercise, rewritten so the solution lives here). A numerical Buchstab function. A three-star exercise: extract the limsup from the average over the arithmetic progression of starting points, with the ineffective constant left ineffective.

**Notebook.** `ch02-cramer-maier`. Sample the model up to \(10^6\) and compare gap statistics with the primes. Compute Buchstab’s function by its delay equation on a grid.

**References.** Cramér, *On the order of magnitude of the difference between consecutive prime numbers* (1936). Maier, *Primes in short intervals* (1985). Granville, *Harald Cramér and the distribution of prime numbers* (1995). Friedlander and Granville, for the variant with arithmetic progressions. Soundararajan’s survey, §§1–3.

### Chapter 3. Independent prime divisors

**Aim.** The Kubilius model, as a probability space in which the prime divisors are independent, and the Selberg–Delange theorem, which Volume 10, Chapter 11, already quotes from this volume. Erdős–Kac is a corollary, compared with the proof in Volume 5, not a second founding of the subject.

**Sections.**

1. Turán–Kubilius. The inequality \(\sum_{n\le x}|f(n)-A(x)|^2\ll x B(x)^2\) for a strongly additive \(f\), proved from the diagonal and off-diagonal sums. This is the \(L^2\) theorem of which Erdős–Kac is the distributional form.
2. The Kubilius model. The finite probability space of integers up to \(x\), and the comparison of an additive function with a sum of independent random variables, truncated at \(y=x^{1/\log\log x}\) or the draft’s cutoff. The total-variation bound, stated with its dependence on \(y\).
3. Erdős–Kac as a corollary, in two pages, then a comparison with Volume 5, Chapter 9: what the probabilistic proof makes visible (the Gaussian is the sum of the indicators) and what the Volume 5 proof makes visible (the moments and the characteristic functions). One proof is enough to cite later. This chapter owns the model; Volume 5 owns the first complete argument.
4. Selberg–Delange. The mean value of \(n^{-s}\) times a function of the shape \(u^{\Omega(n)}\) or, more generally, of a Dirichlet series \(\zeta(s)^z F(s)\) with \(F\) holomorphic and non-zero at \(s=1\). The theorem Volume 10 uses for the mod-Poisson residue of a uniform integer. Prove it from a Hankel contour and the expansion \((s-1)^{-z}\), using Volume 4’s Gamma function and Volume 7’s Mellin inversion. This is the saddle-point argument Volume 4 does not contain; keep it to this one contour.

**Prove.** Turán–Kubilius. The Kubilius comparison for strongly additive functions with \(B(x)\to\infty\) and a truncated second moment. Selberg–Delange in the form Volume 10 quotes. Erdős–Kac as a corollary.

**State.** The Kubilius fundamental lemma in its most general form (arbitrary multiplicative constraints). A remark can give the statement and send the details to Tenenbaum, if the chapter’s own truncation is enough for Erdős–Kac and for the applications in Chapter 4.

**Draws on.** Volume 3, Chapter 6 (characteristic functions and the central limit theorem by moments or by Lévy, whichever the write-up uses; Lévy’s continuity theorem is Volume 10, Chapter 3, and is available). Volume 4, Chapters 5 and 10 (Gamma, zeta). Volume 5, Chapter 9 (the theorem being re-derived). Volume 7, Chapter 10 (Mellin inversion). Volume 10, Chapter 11, is the client of Selberg–Delange and should be named in the introduction.

**Missing from Volumes 0–13.** Selberg–Delange, entirely. The Kubilius model as a named probability space. Turán–Kubilius may be implicit in Volume 5’s second-moment work; if a lemma there already has the inequality, cite it and spend the pages on the model.

**Figures.** The Kubilius space drawn as a product of local factors at the small primes, with the large prime drawn as a single biased coin. A plot of the distribution function of \((\omega(n)-\log\log n)/\sqrt{\log\log n}\) against \(\Phi\), up to \(10^6\).

**Exercises.** The Turán–Kubilius inequality for \(\Omega-\omega\). The total-variation distance for the truncated model at a numerical \(x\). A three-star exercise: deduce the mean of \(d_z(n)\) from Selberg–Delange and compare it with Volume 5’s elementary mean of \(d(n)\).

**Notebook.** `ch03-kubilius`. Sample the independent model and the integers side by side for \(\omega(n)\). Check the Selberg–Delange main term for \(d(n)/\log n\) numerically.

**References.** Kubilius, *Probabilistic Methods in the Theory of Numbers*. Tenenbaum, Chapter III.4. Elliott, *Probabilistic Number Theory*, for the historical line. Selberg and Delange for the mean-value theorem; Tenenbaum’s account is the one to follow.

## Part II. Arithmetic statistics

### Chapter 4. Random multiplicative functions

**Aim.** Steinhaus and Rademacher random multiplicative functions, the Möbius function as a point of the Rademacher model, and the two conjectures (Chowla, Sarnak) that say the point behaves like the model. Prove the comparisons that Halász’s theorem makes unconditional. State the rest.

**Sections.**

1. The two models. Steinhaus: \(f(p)\) uniform on the circle, extended multiplicatively. Rademacher: \(f(p)=\pm 1\) with equal probability. Compute the mean of \(|\sum_{n\le x}f(n)|^2\) and the almost-sure size. The draft’s `ch05-randommult.tex` is the start.
2. Möbius as a Rademacher function. What is proved: \(\sum_{n\le x}\mu(n)=o(x)\), from the prime-number theorem (Volume 5), and Halász’s theorem (Volume 13, Chapter 10) applied to a pretentious distance. Orthogonality of \(\mu\) against a periodic sequence, proved from the characters of Volume 5, Chapter 3.
3. Chowla’s conjecture, stated for the correlations of \(\mu\) at fixed shifts. The one-point case is the prime-number theorem. The two-point case is open. One theorem that is proved: the average of \(\mu(n)\mu(n+h)\) over \(h\) in a short range, if the draft or Volume 13 contains it; otherwise leave it as an exercise under a stated hypothesis.
4. Sarnak’s conjecture, stated for a deterministic sequence of zero topological entropy. Prove it for periodic sequences, which is Section 2. Say explicitly that nilsequences and the Möbius disjointness theorem of Green–Tao–Ziegler are not in this series. Volume 10’s ergodic theory reaches Furstenberg for three-term progressions and does not reach nilsystems.

**Prove.** Moment calculations for both random models. Möbius orthogonality for periodic sequences. The consequences of Halász that identify the distance of \(\mu\) from a character.

**State.** Chowla’s conjecture. Sarnak’s conjecture in the form that needs disjointness from nilsequences. Harper’s bounds on the sup-norm of a random multiplicative function, as a remark with a citation, unless the draft already proves a weaker moment that is worth keeping.

**Draws on.** Volume 2, Chapter 11, and Volume 5, Chapter 3 (characters). Volume 5, Chapter 5 (the prime-number theorem, for \(\sum\mu=o(x)\)). Volume 13, Chapter 10 (Halász, Delange, Wirsing). Volume 10, Chapter 10, only as the boundary of what ergodic theory in the series can say.

**Missing from Volumes 0–13.** The random-multiplicative models as a developed theory. Chowla and Sarnak are conjectures; stating them needs no missing lemma. Proving Sarnak for a nilsequence would need a theory this series does not have. Do not schedule that proof.

**Figures.** A Steinhaus partial sum in the complex plane, a random walk with dependent steps, against a Rademacher sum on the line. The partial sums of \(\mu(n)\) up to \(10^6\), on the scale \(\sqrt x\).

**Exercises.** The variance computation. Orthogonality against \(\mathbf 1_{n\equiv a\pmod q}\). A three-star exercise: show that Chowla for two points implies the prime-number theorem in a short arithmetic progression, and say where the converse fails.

**Notebook.** `ch04-mobiussim`. Sample a Rademacher multiplicative function and compare its partial sums with \(\mu\). Compute the pretentious distance from \(\mu\) to a few real characters up to a moderate \(x\).

**References.** Halász, *On the distribution of additive and multiplicative functions*. Granville and Soundararajan, the pretentious notes. Sarnak, *Three lectures on the Möbius function*. Harper, *Moments of random multiplicative functions*, as a pointer beyond the proved moments.

### Chapter 5. Primes in short intervals

**Aim.** Separate three statements that Volume 5, Chapter 10, puts in one narrative: the almost-everywhere short-interval prime-number theorem, Gallagher’s conditional Poisson law, and the Montgomery–Soundararajan variance. Prove the second-moment calculation for pairs under Hardy–Littlewood. Leave the Poisson law conditional.

**Sections.**

1. What zero density gives. Volume 13, Chapter 1: primes in every interval of length \(x^\theta\) for \(\theta>3/4\). Cite the theorem. Do not reprove Carlson’s estimate.
2. Almost all intervals. Selberg’s almost-everywhere result under the Riemann hypothesis, stated, with the range \(\lambda>2\). The unconditional almost-all theorem, if it is not in Volume 13, is a reasonable theorem to prove from the explicit formula (Volume 5, Chapter 7) and a mean square; if the argument exceeds a chapter, state it and prove the second-moment upper bound only.
3. Gallagher, carefully. The average of the singular series is a theorem (Volume 5). The Poisson law is a consequence of a uniform Hardy–Littlewood conjecture. Write the deduction for the second moment in full, as the exercise in Volume 5 asks, and state the higher moments under the same hypothesis.
4. The variance defect. Montgomery and Soundararajan: under the same uniform conjecture, the variance is \(\lambda\bigl(1-(\log h+c)/\log x\bigr)\) with \(c=\gamma+\log 2\pi-1\). Derive the constant from the secondary term \(-\frac12\log h\) already computed in Volume 5. Compare with the figure at \(10^9\).

**Prove.** The pair second moment under Hardy–Littlewood, including the constant in the variance. The deduction of the Poisson law from the uniform conjecture and Gallagher’s average, as a conditional theorem.

**State.** Montgomery–Soundararajan in full generality (all moments). The almost-everywhere theorem under RH, unless the section stays short enough to prove. Maier’s theorem is Chapter 2; this chapter only points at it as the reason the pointwise asymptotic fails for \(\lambda\) fixed.

**Draws on.** Volume 5, Chapters 7 and 10. Volume 13, Chapter 1. Volume 3, Chapter 9 (Poisson). The explicit formula’s error term must be the one Volume 5 actually proves, not a square-root error.

**Missing from Volumes 0–13.** A proof of the Montgomery–Soundararajan variance. The secondary term of Gallagher’s average is discussed in Volume 5 and is not isolated as a lemma with an error term strong enough for every moment. Prove the second moment. State the rest. Gallagher’s Poisson law is not missing as a statement; it is missing as an unconditional theorem, and it should remain conditional.

**Figures.** The Volume 5 histogram, with the predicted variance \(0.79\) drawn as an error bar. A plot of \((\pi(x+h)-\pi(x))/\mathrm{li}(x+h)-\mathrm{li}(x)\) for \(h=x^{0.1}\) and for \(h=(\log x)^2\), on a range where the second is noise.

**Exercises.** Recover \(\lambda\) as the mean from the diagonal of the pair sum. Compute \(c=\gamma+\log 2\pi-1\) numerically from the singular series. A three-star exercise: show that Maier’s theorem is compatible with the almost-everywhere asymptotic, by estimating the number of bad starting points.

**Notebook.** `ch05-short-intervals`. The histogram at several \(x\), and a running variance against the Montgomery–Soundararajan prediction.

**References.** Gallagher, *On the distribution of primes in short intervals* (1976). Montgomery and Soundararajan, *Primes in short intervals* (2004). Selberg’s 1943 paper for the conditional almost-all theorem. Volume 13 for the zero-density input.

### Chapter 6. Sieves as probability

**Aim.** Read inclusion–exclusion as an expectation, the Selberg sieve as a weighted second moment, and the parity barrier as a theorem about the Liouville function, already proved in Volume 13 and rephrased here. Resist the sentence “sieves cannot detect twins”: Volume 13 is careful, and this chapter should stay careful.

**Sections.**

1. The indicator of being coprime to \(P(z)\) as \(\sum_{d\mid P(z)}\mu(d)\mathbf 1_{d\mid n}\). Bonferroni’s inequalities as the partial expectations. The remainder when the sum is cut at \(d\le D\).
2. Selberg’s weights as the choice of a quadratic form. One page pointing at Volume 5, Chapter 8, where the optimisation is done, and a probabilistic reading of the same quadratic form: the weights are a projection.
3. The parity barrier. Volume 13, Chapter 3, proves that a sieve which does not see the Liouville function cannot tell the primes from the almost-primes. Reproduce the logical shape, not the combinatorial details. For twins, repeat Volume 13’s sentence: believed, not proved.
4. What a sieve can prove, a list with citations: Brun’s twin bound (Volume 5), Brun–Titchmarsh (Volume 5, after the prose repair in the review), Bombieri–Vinogradov (Volume 13), Maynard’s theorem in the form “\(M_k>4m\) and level \(\theta<1/2\) give \(m+1\) primes” (Volume 13). The bound \(600\) is cited only with the certificate, or not at all.

**Prove.** Bonferroni in probabilistic language. The equivalence, in one setting, between a sieve weight and an \(L^2\) projection. The parity obstruction for the integers, by citation plus a rewritten summary.

**State.** Chen’s theorem. The parity barrier for twins. Any sieve that produces primes on its own.

**Draws on.** Volume 3, Chapters 1 and 4 (inclusion, second moment). Volume 5, Chapter 8. Volume 13, Chapters 3, 4, and 9.

**Missing from Volumes 0–13.** Nothing this chapter needs in order to be honest. A proof of the parity barrier for twins is not available and should not be attempted.

**Figures.** The inclusion–exclusion partial sums for the count of primes up to \(10^4\), oscillating around \(\pi(10^4)\) and then leaving it when the parity wall is hit. A schematic of the Selberg weights \(\lambda_d\).

**Exercises.** Bonferroni on a small sieve of twins. The Selberg upper bound of \(2\) as a variational fact: any improvement inside the sieve’s class of weights would contradict the computation. A three-star exercise: translate Volume 13’s Liouville obstruction into the language of this chapter without adding a hypothesis.

**Notebook.** `ch06-sieve-expectation`. Partial inclusion–exclusion for \(\pi(x)\) and for \(\pi_2(x)\), showing the truncation.

**References.** Friedlander and Iwaniec, *Opera de Cribro*, Chapters 1 and 16, as the reference for the parity problem. Harman, *Prime-detecting Sieves*, for what lies beyond parity. Volume 13 is the internal source.

### Chapter 7. Random groups in arithmetic

**Aim.** The Cohen–Lenstra measure on finite abelian \(p\)-groups, its moments, and the heuristic that a class group is a random group for that measure. Prove the measure theory and one cokernel theorem. State the heuristic. The 2-part needs genus theory, which Volumes 0–13 do not contain; keep it separate.

**Sections.**

1. Finite abelian \(p\)-groups. Partitions, the automorphism group, the measure proportional to \(1/|\mathrm{Aut}(G)|\). Prove that the measure is finite (the Euler product \(\prod_{i\ge 1}(1-p^{-i})\)).
2. Moments. \(\mathbb E\#\mathrm{Sur}(G,A)=1\) for the Cohen–Lenstra measure, for each finite abelian \(p\)-group \(A\). The draft’s `ch13-cohenlenstra.tex` is the source. The dual form \(\mathbb E\#\mathrm{Hom}(G,\mathbb Z/p^k)\).
3. A theorem that matches the moment: the cokernel of a random symmetric matrix over \(\mathbb Z/p^k\), or over \(\mathbb F_q\). Volume 15, Chapter 5, proves \(\mathbb E\#\mathrm{Sur}(\mathrm{cok}\,M,G)\to|\wedge^2 G|\) and the corank chain. That argument moves here, shortened. It is a theorem about matrices, not about class groups.
4. The heuristic. State Cohen–Lenstra for the odd part of the class group of an imaginary quadratic field: the probability that the \(p\)-part is isomorphic to \(A\) is proportional to \(1/(|A|\,|\mathrm{Aut}(A)|)\). What Volume 12 proves: class groups are finite (Chapter 3), and the class-number formula (Chapter 8) ties \(h(-d)\) to \(L(1,\chi_{-d})\). What it does not prove: any moment of the class group. Siegel’s theorem (Volume 13, Chapter 2) says \(L(1,\chi)\gg_\varepsilon q^{-\varepsilon}\), ineffectively, which is the only proved constraint on how small \(h(-d)\) can be.
5. The 2-part, stated as a different measure (Cohen–Lenstra–Gerth), with a one-paragraph warning that genus theory is not in the series. Do not quote a 2-rank formula as a theorem of Volume 12.

**Prove.** Convergence of the measure. The moment calculation \(\mathbb E\#\mathrm{Sur}=1\). The cokernel theorem imported from the workshop.

**State.** The heuristic, labelled as a heuristic in the heading. The 2-part. Cohen–Martinet for higher degree, one remark.

**Draws on.** Volume 2, Chapters 6 and 7 (finitely generated modules, the classification of finite abelian groups). Volume 9, Chapter 5 (Dedekind domains, the class group as an object). Volume 12, Chapters 2, 3, and 8. Volume 13, Chapter 2 (Siegel). Volume 15, Chapter 5, until that chapter is moved.

**Missing from Volumes 0–13.** Genus theory. Any proved average of class groups. The cokernel calculation lives in Volume 15 and moves with Part V’s source; it is not a prerequisite from the earlier volumes, and this chapter should contain the proof rather than cite a book that this volume is absorbing.

**Figures.** The distribution of the 3-part of \(h(-d)\) for \(|d|\le 10^5\), against the Cohen–Lenstra prediction \(1-\prod_{i\ge 1}(1-3^{-i})\). A histogram of coranks of random \(n\times n\) matrices over \(\mathbb F_3\).

**Exercises.** Compute \(|\mathrm{Aut}(\mathbb Z/p\times\mathbb Z/p)|\) and the predicted probability. The moment for \(A=\mathbb Z/p\). A three-star exercise: show that the class-number formula plus Siegel’s bound does not determine the proportion of \(d\) with \(3\mid h(-d)\).

**Notebook.** `ch07-cohen-lenstra`. Class numbers via a small implementation of the class-number formula for fundamental discriminants, compared with the predicted proportions. Random cokernels over a finite field.

**References.** Cohen and Lenstra, *Heuristics on class groups of number fields* (1984). Cohen and Martinet for the generalisation. Washington, *Introduction to Cyclotomic Fields*, for genus theory, as the external reference the 2-part points to. Ellenberg–Venkatesh–Westerland, as a remark on the function-field theorem, not as a proof.

### Chapter 8. Ranks of elliptic curves

**Aim.** Say what is known, what is conjectured, and what this series can actually prove, about the rank of \(E(\mathbb Q)\). The proved core is short: Mordell’s theorem and one 2-descent, both in Volume 12, and a linear-algebra model of the Selmer group. The famous averages are stated.

**Sections.**

1. The rank. Volume 12, Chapter 12: \(E(\mathbb Q)\) is finitely generated. The descent for \(y^2=x^3-x\) and \(y^2=x^3-4x\), cited, with the Tate–Shafarevich group named as the gap between the Selmer bound and the rank.
2. A definition of the 2-Selmer group for the congruent-number curves, written out, because Volume 12 uses the descent without isolating the group. This is a construction, not a general theory of \(n\)-Selmer groups.
3. Goldfeld’s conjecture, stated: the average rank of the quadratic twists of a fixed elliptic curve is \(\frac12\). The root number. Volume 12, Chapter 9, shows that the root number of a real Dirichlet character is 1. The root number of an elliptic \(L\)-function is not a theorem of this series, because modularity is stated and not proved (Volume 12, Chapter 14). Define the root number for the congruent-number family by the explicit formula Volume 12 already uses, and state it in general.
4. The random model. Poonen–Rains: the \(p\)-Selmer group as the intersection of two random maximal isotropic subspaces of a quadratic space over \(\mathbb F_p\). Prove the linear algebra (dimensions, the probability that the intersection has dimension \(r\)). State the conjecture that this models \(\mathrm{Sel}_{p}(E)\).
5. Bhargava–Shankar, stated: the average of the 2-Selmer size is 3, and the average rank of elliptic curves over \(\mathbb Q\) is at most \(1.5\), in the sense of their ordering. One paragraph on why the proof is not attempted: it counts integral orbits for a coregular representation, which is a geometry-of-numbers argument far past Volume 12, Chapter 3.

**Prove.** The linear-algebra distribution of a random maximal isotropic intersection. The 2-Selmer group of \(y^2=x^3-x\), as a rewrite of Volume 12’s descent in the new language.

**State.** Goldfeld. Birch–Swinnerton-Dyer (already stated in Volume 12). Bhargava–Shankar. Poonen–Rains as a model, with the linear algebra proved and the arithmetic identification conjectural. Modularity.

**Draws on.** Volume 12, Chapters 7 (local–global for quadrics, the model for a Selmer condition), 9 (root numbers of characters), 12 (Mordell, descent), 13 (Hasse), and 14 (modular forms, \(L\)-functions, modularity stated). Volume 2, the linear-algebra appendices, for quadratic forms over finite fields. Volume 9, Chapter 7, only if a cocycle is written down; prefer the explicit descent.

**Missing from Volumes 0–13.** A general \(n\)-Selmer group. The canonical height as a proved quadratic form. Root numbers of elliptic \(L\)-functions. Integral-orbit counts in the sense of Bhargava. These are the reasons Sections 4 and 5 state their arithmetic conclusions. The linear algebra in Section 4 has no missing prerequisite.

**Figures.** Rank frequencies for the curves of conductor up to a few thousand, against \(\frac12\) and against the Poonen–Rains prediction for the 2-Selmer rank. The congruent-number curve and its 2-isogeny, a diagram.

**Exercises.** The 2-descent for one further curve of the family, with the rank found. The probability that two random maximal isotropics in a \(2n\)-dimensional space over \(\mathbb F_p\) meet in dimension \(r\), for \(n=2\). A three-star exercise: show that an average rank of \(\frac12\) is compatible with a positive proportion of curves of rank \(\ge 2\), and compute the constraint the Poonen–Rains model adds.

**Notebook.** `ch08-ranks`. A table of ranks and 2-Selmer sizes for the congruent-number twists \(y^2=x^3-n^2x\) with \(n\le 200\), using the descent the chapter proves, not a computer-algebra call the reader cannot see.

**References.** Silverman, *The Arithmetic of Elliptic Curves*, Chapters 8 and 10, for the Selmer group in general. Goldfeld, *Conjectures on elliptic curves* (1979). Bhargava and Shankar, the 2-Selmer paper. Poonen and Rains, *Random maximal isotropic subspaces and Selmer groups* (2012). The Birch–Swinnerton-Dyer survey of Wiles or Gross, as a guide to what is stated.

## Part III. Spectra

### Chapter 9. Random matrices and the zeros of zeta

**Aim.** Put on one page two theorems the series already contains, and draw the conjectural line between them. Do not reprove either theorem.

**Sections.**

1. The zeros. Volume 13, Chapter 14: under the Riemann hypothesis, Montgomery’s \(F(\alpha)\) equals \(|\alpha|\) for \(0\le\alpha\le 1-\varepsilon\), and the pair correlation of the zeros is the sine kernel on that range. Cite Theorem 14.15. State the conjecture for \(\alpha\ge 1\), which is the GUE form factor \(1\).
2. The matrices. Volume 8, Chapter 8, and Volume 11, Chapter 11: the circular unitary ensemble, the sine kernel as the scaled limit, the gap series. Cite them. One page deriving the form factor of the sine kernel from the determinant, so the reader sees the same function on both sides.
3. Odlyzko’s computation, as a figure and a discussion of what a histogram can and cannot show. The pair correlation at height \(10^{20}\) matches the sine kernel. A computation is not a proof, and the chapter should say what hypothesis the picture still uses (the Riemann hypothesis is used to number the zeros by their imaginary part).
4. The dictionary, a table: zero gaps, characteristic-polynomial gaps, the ranges where each side is a theorem.

**Prove.** The form-factor identity for the sine kernel, if Volume 11 cites it to Mehta rather than proving \(p(s)=\mathrm d^2E(0;s)/\mathrm ds^2\). The review found that identity cited, not proved. Either prove it here or label the picture as a consequence of a quoted formula. Do not present it as new research.

**State.** Montgomery’s conjecture for \(\alpha\ge 1\). The identification of the zeros with eigenvalues of a random matrix, as a conjecture. Quantum unique ergodicity, one remark, not a section.

**Draws on.** Volume 8, Chapter 8 (Weyl integration, Dyson). Volume 11, Chapter 11 (the sine kernel, Keating–Snaith’s moments as a forward pointer). Volume 13, Chapter 14 (Montgomery, the mean square, Hardy’s theorem). Volume 5, Chapters 6 and 7, for the explicit formula that Montgomery’s proof uses; the proof stays in Volume 13.

**Missing from Volumes 0–13.** Nothing required to state the conjecture, once the form-factor gap above is filled or cited. A proof of pair correlation for \(\alpha>1\) is not a realistic chapter.

**Figures.** Odlyzko’s pair correlation, recomputed at a height the notebook can reach (the first \(10^5\) zeros, if a zero table is generated, or a smaller set computed from the Riemann–Siegel formula Volume 13 already describes). The sine kernel and the GUE form factor on the same axes.

**Exercises.** Compute \(\int_0^1 F(\alpha)\,d\alpha\) under Montgomery’s theorem and under the conjecture, and interpret the difference. The two-point correlation of three eigenvalues, by hand. A three-star exercise: show that the range \(\alpha\le 1-\varepsilon\) sees only differences of size \(\ll (\log T)/1\), and say which prime sums in the explicit formula contribute.

**Notebook.** `ch09-pair-correlation`. A zero table and a histogram of normalised gaps, against the Gaudin density if the form factor has been integrated numerically, with the numerical integration labelled as such.

**References.** Montgomery, *The pair correlation of zeros of the zeta function* (1973). Odlyzko, *On the distribution of spacings between zeros of the zeta function* (1987). Mehta, *Random Matrices*, Chapter 5, for the form factor if it stays quoted. Katz and Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, as the conceptual reference, not as a source of proofs.

### Chapter 10. Moments of \(L\)-functions

**Aim.** Explain the Keating–Snaith conjecture and the CFKRS recipe as a machine that turns a random-matrix moment into a number-theoretic prediction. Prove the dictionary. Do not pretend the moments of \(\zeta\) on the critical line are known past the second.

**Sections.**

1. What is proved for \(\zeta\). Volume 13, Chapter 14: the mean square \(\frac1T\int_0^T|\zeta(\tfrac12+it)|^2\,\mathrm dt\sim\log(T/2\pi)\). The fourth moment is Ingham’s, quoted there. No higher moment is known. Say this in the first page.
2. What is proved for matrices. Volume 11, Chapter 11: the integer moments of \(|\det(I-U)|\) for Haar \(U\) in \(U(n)\), with the Barnes \(G\)-function leading coefficient. Cite the theorem. One computation of the second moment by hand, so the chapter is not only a citation.
3. The recipe, stated. The approximate functional equation is quoted in Volume 13, Chapter 14 (Hardy–Littlewood, marked quoted). The CFKRS recipe splits a moment into diagonal terms using that expansion and a random-matrix factor. Write the recipe for the second and fourth moments, where the answer can be checked against Ingham, and state it for the sixth. Label every step that uses the quoted approximate functional equation.
4. Families. One example: the family of Dirichlet \(L\)-functions at the central point, with the random-matrix symmetry type stated (unitary, orthogonal, symplectic) and not derived from a monodromy group. Katz–Sarnak is the citation.

**Prove.** The second-moment comparison: the random-matrix moment and the arithmetic second moment, side by side, with the arithmetic side cited from Volume 13. The formal CFKRS expansion for the fourth moment, marked as conditional on the approximate functional equation.

**State.** Keating–Snaith for \(\zeta(\tfrac12+it)\). The CFKRS conjectures for higher moments and for families. The approximate functional equation itself, unless a short proof from Volume 4’s functional equation and a smooth weight is added as an appendix to this chapter. A proof of the approximate functional equation is the one missing prerequisite worth adding, and it is a reasonable twenty-page job. If it is not added, the recipe remains a formal manipulation of a quoted formula.

**Draws on.** Volume 4, Chapter 10 (the functional equation, after the factor \(\frac12\) is repaired). Volume 11, Chapter 11. Volume 13, Chapter 14. Volume 12, Chapter 14, for the language of \(L\)-functions of modular forms, if a family of elliptic curves is mentioned; keep that mention inside the “stated” column.

**Missing from Volumes 0–13.** A proof of the approximate functional equation. Proofs of moments of \(\zeta\) past the second. Both are flagged. The chapter is honest without the first and much clearer with it. Higher moments are not a gap to be filled; they are open.

**Figures.** The partial integral of \(|\zeta(\tfrac12+it)|^2\) against \(\log(T/2\pi)\), the figure Volume 13 already has, cited. A plot of the Keating–Snaith leading coefficients for \(k=1,2,3,4\) against the proved or quoted arithmetic constants.

**Exercises.** The second moment of \(|\det(I-U)|\) for \(U(2)\), by hand. The diagonal contribution in the fourth-moment recipe. A three-star exercise: show where the approximate functional equation is used, by marking each line of the formal fourth-moment calculation.

**Notebook.** `ch10-moments`. Numerical fourth moment of \(\zeta\) up to a moderate height, against Ingham’s leading term, using the Riemann–Siegel formula as a quoted algorithm.

**References.** Keating and Snaith, *Random matrix theory and \(\zeta(1/2+it)\)* (2000). Conrey, Farmer, Keating, Rubinstein, and Snaith, *Integral moments of \(L\)-functions* (2005). Ingham for the fourth moment. Titchmarsh for the approximate functional equation, if it stays quoted.

### Chapter 11. Value distribution

**Aim.** The one analytic-probabilistic theorem this book should own: the distribution of \(\log\zeta(\sigma+it)\). Bohr–Jessen off the critical line, proved. Selberg’s central limit theorem on the critical line, proved, with the approximation of \(\log\zeta\) by a short Dirichlet polynomial written out. The draft’s Chapters 6 and 7 are the working text. Volumes 0–13 do not contain these proofs. Volume 15, Chapter 4, depends on them.

**Sections.**

1. The Euler product as a random variable, for \(\sigma>1/2\) fixed, \(\sigma\ne 1\). The finite product over \(p\le y\), the independence of \(\log(1-p^{-s})^{-1}\) when \(t\) is random, and the convergence that Bohr–Jessen prove. The characteristic function is an Euler product. Prove the existence of the limiting distribution of \(\log\zeta(\sigma+it)\).
2. The critical line. The approximation
   \[
   \log\bigl|\zeta(\tfrac12+it)\bigr|=\mathrm{Re}\sum_{p\le x}p^{-1/2-it}+O(1)
   \]
   in mean square, for \(x=T^{o(1)}\), on a set of \(t\in[T,2T]\) of measure \(T(1-o(1))\). This is the step Volume 15, Chapter 4, currently takes from the draft. Prove it from the explicit formula (Volume 5, Chapter 7) and a mean-value estimate for Dirichlet polynomials (Volume 13’s tools, or a direct \(L^2\) computation). Name every use of a zero-free region or of the Riemann hypothesis. The preferred target is an unconditional proof on a set of full measure, which is Selberg’s theorem; a proof under the Riemann hypothesis is acceptable if it is labelled in the heading.
3. The central limit theorem. The short sum is a sum of independent random variables in the \(t\)-aspect (Volume 10, Chapter 4, Berry–Esseen, if a rate is wanted; Volume 3, Chapter 6, if not). The variance is \(\frac12\log\log T\). Conclude Selberg’s theorem.
4. The maximum. State the Fyodorov–Hiary–Keating conjecture, and point at Volume 11, Chapter 12, where the random-matrix maximum is an admitted theorem. Do not claim the maximum of \(\log|\zeta|\) as a theorem.

**Prove.** Bohr–Jessen for fixed \(\sigma>1/2\). The mean-square approximation of \(\log|\zeta(\tfrac12+it)|\) by a short prime sum, with the hypotheses on the page. Selberg’s central limit theorem from that approximation.

**State.** The joint distribution at several heights (Volume 15, Chapter 4, can keep the multipoint argument, or this chapter can include the covariance and leave the application to Part V). Fyodorov–Hiary–Keating.

**Draws on.** Volume 4, Chapter 10. Volume 5, Chapters 6 and 7. Volume 7, Chapter 5 (Fourier analysis, for the characteristic functions). Volume 10, Chapters 1 and 4. Volume 11, Chapter 12, as the random-matrix analogue, not as a lemma. Volume 13, Chapter 14, for the mean square, which is a different theorem and should be distinguished in one sentence: a mean of \(|\zeta|^2\) is not a central limit theorem for \(\log|\zeta|\).

**Missing from Volumes 0–13.** The approximation lemma, and both limit theorems. This is the largest “prove” item in the book. The draft is the right starting point. A proof that quietly uses an unproved zero-density estimate is not acceptable; Volume 13’s proved zero-density theorems are the legal input.

**Figures.** The histogram of \(\log|\zeta(\tfrac12+it)|/\sqrt{\tfrac12\log\log T}\) at a fixed range, against the standard Gaussian. A picture of the Euler product’s partial sums in the complex plane for \(\sigma=0.8\) and for \(\sigma=\tfrac12\).

**Exercises.** The variance of \(\mathrm{Re}\,p^{-it}\) as \(t\) varies. Bohr–Jessen for the partial Euler product, which is elementary probability. A three-star exercise: the covariance \(\mathrm{Cov}(\log|\zeta(\tfrac12+it)|,\log|\zeta(\tfrac12+i(t+h))|)\) for \(h\) larger than \(1/\log T\) and for \(h\) smaller, which is the input Volume 15’s multipoint theorem uses.

**Notebook.** `ch11-selberg-clt`. The histogram, and a check of the short-sum approximation at a few hundred values of \(t\).

**References.** Bohr and Jessen, *Über die Werteverteilung der Riemannschen Zetafunktion* (1930, 1932). Selberg, *On the normal density of primes in small intervals, and the difference between consecutive primes* — and his paper on the distribution of \(\log\zeta\). Radziwiłł and Soundararajan, for a modern account of the central limit theorem. Laurincikas, *Limit Theorems for the Riemann Zeta-Function*, as the specialist reference.

## Part IV. Structure versus randomness

### Chapter 12. Pseudorandomness

**Aim.** The structure/randomness dichotomy, told once, on a theorem this series has already proved twice: Roth’s theorem. Green–Tao is stated, with the pieces Volume 13 proves listed and the pieces it quotes left quoted.

**Sections.**

1. Two proofs, one idea. Volume 10 proves Roth by ergodic theory. Volume 13 proves it by the density increment. This chapter does not give a third proof. It writes the dichotomy: a set is structured (it correlates with a character, or it is almost periodic) or it is random (its \(U^2\) norm is small), and in the random case the count of progressions matches the random model. The \(U^2\) inverse theorem is Volume 13, Chapter 13. Cite it.
2. Gowers norms, a reading guide to Volume 13, Chapter 13. The generalised von Neumann theorem, cited. The inverse theorem for \(U^{s+1}\), stated as quoted there.
3. The \(W\)-trick, in probabilistic language. The primes are not random in the sense of Chapter 1, because they are biased modulo small primes. After removing that bias, the weighted set is pseudorandom enough for a transference argument. Volume 13 proves the trick and quotes the transference. Reproduce the trick. State the transference.
4. Green–Tao, stated in a heading marked “quoted”. The singular series for prime progressions, which Volume 13 computes, can be proved here if it is not already a numbered theorem, or cited if it is. One paragraph: the capstone does not contain a proof of arbitrarily long arithmetic progressions of primes.

**Prove.** Nothing that Volume 13 has not already proved. The new text is the organisation and the probabilistic translation of the \(W\)-trick. If that seems too thin for a chapter, add a complete proof of the \(U^2\) case of the count of progressions in a set with small Gowers norm, written in the language of Chapters 1 and 6, citing Volume 13 for the inverse step. That is a rereading, and it is the right length.

**State.** Green–Tao. Szemerédi’s theorem. The inverse theorem for higher norms. The relative Szemerédi theorem.

**Draws on.** Volume 10, Chapter 10. Volume 13, Chapters 11, 12, and 13. Volume 7, Chapter 7 (Fourier analysis on finite abelian groups), which is the \(U^2\) language.

**Missing from Volumes 0–13.** The inverse theorem for \(U^{k}\), \(k\ge 3\), the linear forms condition, and the relative Szemerédi theorem. A proof of Green–Tao is not a chapter of this book. Scheduling one would be a different book.

**Figures.** A Bohr set, drawn on \(\mathbb Z/N\), beside a random subset of the same density, with the three-term progression counts compared. The \(W\)-trick as a thinning of the integers by the small primes.

**Exercises.** Compute the \(U^2\) norm of an interval and of a random set. The \(W\)-trick modulo \(6\), by hand, for a short interval of primes. A three-star exercise: show that the ergodic proof and the Fourier proof use the same dichotomy, by matching “compact” with “correlates with a character” in the length-three case.

**Notebook.** `ch12-structure`. Progression counts in a random subset of \(\{1,\ldots,N\}\) and in a geometric progression, at \(N=10^4\).

**References.** Tao and Vu, *Additive Combinatorics*, Chapters 10 and 11. Green and Tao, *The primes contain arbitrarily long arithmetic progressions* (2008), as the paper that is not proved here. Volume 13 is the internal source.

### Chapter 13. When order wins

**Aim.** The places where a random model is not just incomplete but biased: Chebyshev’s bias, Maier’s irregularities (by reference), and the Lemke Oliver–Soundararajan bias in consecutive primes.

**Sections.**

1. Chebyshev, unconditionally and conditionally. Volume 5, Chapter 7, proves
   \[
   \theta(x;4,3)-\theta(x;4,1)=\theta(\sqrt x)-\psi(x,\chi_{-4})+O(x^{1/3}\log x),
   \]
   after the review’s request that the functional equation of \(L(s,\chi)\) be cited to Volume 12 rather than assumed. The excess of primes \(3\pmod 4\) is then a statement about a character sum. Rubinstein and Sarnak: under the generalised Riemann hypothesis and linear independence of the zeros over \(\mathbb Q\), the logarithmic density of the set where the excess is positive exists and equals about \(0.9959\). Volume 5 states their theorem and attributes the proof. This chapter either proves the measure computation (the explicit formula plus an equidistribution of the torus \((\gamma\log x \bmod 2\pi)\)) or cites Volume 5 and adds the numerical torus integral as a fully written argument. The linear-independence hypothesis stays a hypothesis.
2. Maier, again, in one section. The model of Chapter 2 fails on intervals of length \((\log x)^\lambda\). Point at the theorem. Do not prove it twice. The lesson: the small primes are a structure, in the sense of Chapter 12, and the model that forgets them is the one that loses.
3. Consecutive residues. Lemke Oliver and Soundararajan: a prime \(p_n\equiv a\pmod{10}\) is less often followed by \(p_{n+1}\equiv a\pmod{10}\) than by the other residue classes. P1, Chapter 13, already quotes the figure \(17.7\%\) after a prime ending in 1. State the theorem. The proof uses a pretentious analysis of singular series beyond what Chapter 4 and Volume 13, Chapter 10, have set up as a general machine. Do not sketch it in a way that looks like a proof.

**Prove.** The logarithmic-density integral under GRH and linear independence, if Volume 5 has only the citation. The reduction of Chebyshev’s bias to \(\psi(x,\chi)\), by citation of the repaired Volume 5.

**State.** Lemke Oliver–Soundararajan. Granville’s gap prediction, already stated in Chapter 2, one sentence. Any bias that needs an unproved pair correlation of zeros in arithmetic progressions.

**Draws on.** Volume 5, Chapters 4 and 7. Volume 12, Chapter 9 (the functional equation of \(L(s,\chi)\), so that \(\psi(x,\chi)\) is available). Volume 13, Chapter 10, for the pretentious language used to explain, without proving, the consecutive-residue bias. P1, Chapter 13, for the numerical figure, which should be recomputed or cited precisely.

**Missing from Volumes 0–13.** A proof of the Lemke Oliver–Soundararajan theorem. A self-contained proof of the Rubinstein–Sarnak density, if Volume 5 only cites it; the prerequisites for that proof (the explicit formula, Weyl equidistribution from Volume 4, Chapter 6) are available, so this is a “prove” item, not a missing-prerequisite item. Maier’s theorem is Chapter 2 of this book, not a prerequisite from earlier volumes.

**Figures.** The race \(\pi(x;4,3)-\pi(x;4,1)\) up to \(10^6\), with the first crossing near \(26861\) marked (Volume 5 already discusses this crossing). The \(10\times 10\) matrix of consecutive residue frequencies modulo 10, with the diagonal visibly light.

**Exercises.** The bias modulo 3, the same shape as modulo 4. The torus integral for a single zero, which is elementary. A three-star exercise: show that the diagonal deficit modulo 10 is already visible in the singular series of the pair \((0,d)\) with \(10\mid d\), using only Volume 5’s singular series, and say why that computation is not yet the theorem.

**Notebook.** `ch13-bias`. The race up to \(10^7\), and the consecutive-residue matrix modulo 10 up to the first million primes.

**References.** Rubinstein and Sarnak, *Chebyshev’s bias* (1994). Lemke Oliver and Soundararajan, *Unexpected biases in the distribution of consecutive primes* (2016). Volume 5, Chapter 7.

## Part V. The research workshop

Volume 15 is twelve chapters and twelve appendices, about 9,700 lines, half of them tours of conjectures that Parts I–IV and Volumes 5, 11, 12, and 13 already own. Part V keeps the method: one problem followed through its life, a paper read in three passes, a formula found by machine and then proved, a heuristic separated from a theorem, a proof written so that the difficulty is visible. The target is four chapters and four appendices, on the scale of a part rather than a second book.

The first-edition rule still applies. Part V does not describe itself as a condensation, a former volume, or a companion. It is the last part of this book.

### What happens to each chapter of Volume 15

| Source | Decision | Why |
| --- | --- | --- |
| Ch. 1, How research works | Keep, as the spine of Chapter 14 | One problem’s life, including the two elementary steps of the 2026 dissociated-set argument. The density theorem stays unproved, and the heading must say so. |
| Ch. 2, How to read a paper | Keep, inside Chapter 14 | Three passes, and a shortcut that fails. This is the skill Part V is for. |
| Ch. 3, Shuffling | Merge into Chapter 14, one section | Volume 9 proves the cutoff. Keep the Bayer–Diaconis profile, which is not elsewhere. |
| Ch. 4, Selberg at many points | Cut the tour; keep the covariance as an exercise of Chapter 11 | The one-point theorem is Chapter 11. The multipoint limit is an exercise once the covariance is known. |
| Ch. 5, Random groups | Moved to Chapter 7 | The cokernel theorem is part of the Cohen–Lenstra chapter, not of the workshop. |
| Ch. 6, Better than square root | Cut, except one exercise | Harper’s theorem belongs with random multiplicative functions. The half-moment \(\mathbb E[W_n^{1/2}]\le Cn^{-1/4}\) can be an exercise in Chapter 14 if a project needs it. |
| Ch. 7, Experiments | Keep, as Chapter 15 | BBP and a full proof of LLL are not in Volumes 0–13. |
| Ch. 8, Heuristics | Keep, as Chapter 15 | Three cubes and Booker’s factorisation. Heath-Brown stays a conjecture. |
| Ch. 9, Formal proof | Keep, shortened, as Chapter 16 | Curry–Howard is unique in the series. The four historical stories become one page. |
| Ch. 10, Writing | Keep, as Chapter 16 | Jordan for polygons, after the cycle sentence is repaired, is the writing model. |
| Ch. 11, Problems to work on | Merge into Chapter 17 | Keep two problems as projects. Drop the tour of seven. |
| Ch. 12, Five projects | Merge into Chapter 17 | The project pattern stays. Two projects, both using tools the book has proved. |

### What happens to each appendix of Volume 15

| Appendix | Decision | Why |
| --- | --- | --- |
| A, Conjectures born and die | Merge: the Borwein theorem becomes Appendix A | Pólya, Mertens, and \(\pi(x)-\mathrm{li}(x)\) are Volume 5. The sinc integrals are a complete proof and a conjecture that died. |
| B, Twin primes and gaps | Cut | Volume 5, Chapter 8, and Volume 13, Chapters 8–9. |
| C, Goldbach | Cut | Schnirelmann is real, and Volume 13, Chapter 7, already proves three primes. A remark in Chapter 6 can point at Schnirelmann if the additive-basis idea is wanted; it should not be an appendix. |
| D, The Riemann hypothesis | Cut | Robin and Lagarias restate Volume 5, Chapters 6–7. |
| E, Random matrices and zeta | Cut | The file is a pointer to Volume 11, Appendix B, and Chapter 9 of this book replaces the pointer. |
| F, Collatz | Merge: Terras and the cycle bound become Appendix B | A complete argument, not in the main series. The surrounding narrative is cut. |
| G, Hadamard | Cut | Volume 2’s linear-algebra appendices cover the constructions that are theorems. |
| H, Points and distances | Merge: Gilmer’s inequality becomes Appendix C | Unit distances and the happy ending are Volume 3 and P1. Gilmer’s entropy argument is the piece to keep. |
| I, \(abc\) | Merge: Mason–Stothers becomes Appendix D | Polynomial Fermat is a theorem. The integer \(abc\) conjecture is one paragraph in Chapter 15, not a second heuristic chapter. |
| J, Birch–Swinnerton-Dyer | Cut | Volume 12, Chapters 12–14, and Chapter 8 of this book. |
| K, Randomness in the integers | Cut | Chowla, Sarnak, and Cohen–Lenstra are Chapters 4 and 7. |
| L, Open doors in algebra | Cut, except a remark | Inverse Galois needs Volume 12. Ax–Grothendieck over finite fields can be a remark in Chapter 16 if the formal-proof discussion wants one algebraic example; it should not be an appendix. |

### Chapter 14. Reading a proof that is not yet a theorem

**Aim.** One problem, dissociated sets, followed from the counting bound through a paper read in three passes, including a tempting estimate that fails. The Bayer–Diaconis profile as a second, shorter, reading.

**Sections.** The life of \(a(n)\), from Volume 15, Chapters 1 and 2, with the 2026 density theorem marked unproved in the statement. The three-pass method, applied once. The shuffle profile, cited against Volume 9’s cutoff so the reader sees what “reading a paper onto a book” means.

**Prove.** The counting bound, Moser’s variance, the Berry–Esseen bound with constant \(6.3\lambda\), and the Bayer–Diaconis limit \(d_n\to 1-2\Phi(-1/(4\sqrt 3\gamma))\).

**State.** The density theorem that would finish the 2026 construction.

**Draws on.** Volume 9, Chapter 10. Volume 3, Chapter 6 (Berry–Esseen is Volume 10, Chapter 4; cite it). Parts I–IV are not required, which is deliberate: a reader can use this chapter as a method even on earlier mathematics.

**Figures.** The Conway–Guy set, drawn. The total-variation distance for 52 cards at 5, 6, 7, and 8 shuffles, the numbers Volume 15 already computes (\(0.614\) after six, \(0.334\) after seven).

**Exercises.** Six, including one rewrite of a faulty shortcut, taken from Volume 15, Chapter 2.

**Notebook.** `ch14-reading`. The shuffle distance for \(n\le 52\), by the formula the chapter proves.

**References.** Keshav, *How to Read a Paper*. Dubroff–Fox–Xu, the note Chapter 2 reads. Bayer and Diaconis, *Trailing the dovetail shuffle to its lair* (1992).

### Chapter 15. From a computation to a conjecture

**Aim.** BBP and LLL, proved, then the three-cubes heuristic, with the conjecture labelled as a conjecture. This is the chapter that teaches the difference.

**Sections.** The BBP series and hexadecimal extraction. LLL with the factor \(2^{(n-1)/2}\), and what an integer relation certifies. Three cubes: the mod-9 obstruction, the polynomial families, local densities, Booker’s identity \(\Delta=(4(n-z^3)-d^3)/(3d)\). Heath-Brown’s logarithmic prediction, in a heading marked as a conjecture. Mason–Stothers is Appendix D; the integer \(abc\) conjecture is one paragraph here, as a heuristic of the same shape, not a theorem.

**Prove.** BBP. LLL’s guarantee. The local densities for \(p\equiv 2\pmod 3\). Booker’s identity.

**State.** Heath-Brown’s prediction. The integer \(abc\) conjecture.

**Draws on.** Volume 1, for cubes and congruences. Volume 4, for series. Volume 12, Chapter 6, for the local densities if they use \(p\)-adic solubility. No appeal to an unproved theorem of Parts I–IV.

**Missing from Volumes 0–13.** Nothing. These proofs are not in the earlier volumes, and they do not depend on missing machinery.

**Figures.** One hexadecimal extraction, digit by digit. A failed integer relation, from Volume 15’s list of coincidences that die, next to a relation LLL certifies.

**Exercises.** Extract one digit by hand. An LLL run small enough to do on paper. The mod-9 obstruction as a one-star exercise.

**Notebook.** `ch15-lll`. LLL on a short list of suspected relations, including one that fails.

**References.** Bailey, Borwein, and Plouffe (1997). Lenstra, Lenstra, and Lovász (1982). Booker and Sutherland, the three-cubes computations, as the source of the examples. Heath-Brown, as the conjecture.

### Chapter 16. Writing it down

**Aim.** The shape of a paper, one formal system, and one proof written so that a gap in a draft is visible and then closed. Jordan’s theorem for a simple polygon is that proof, after the cycle sentence in Volume 15 is repaired.

**Sections.** Three error stories, cut to one page. The polygon theorem, with the second cycle forced by walking the boundary rather than by a general fact about 2-regular graphs. Curry–Howard for the implicational fragment, and the failure of Peirce’s law, in the form Volume 15 proves. One page on what a formal proof certifies and what it does not.

**Prove.** Jordan for polygons. Soundness of the implicational calculus. That Peirce’s law is not provable there.

**State.** Nothing about modern proof assistants beyond what the proved calculus supports. A remark may name a system. It should not claim a formalisation the book does not contain.

**Draws on.** Volume 8, Chapter 6, only as a comparison: the topological Jordan theorem is a different proof, and the chapter should say so in one sentence.

**Figures.** A polygon and a ray, with the crossings counted. A derivation tree next to its type.

**Exercises.** The rewrite exercise Volume 15 already attaches to its own draft sentence. A small implicational derivation. A three-star exercise: find the gap in a supplied false proof of the polygon theorem, the gap being the one the review found.

**Notebook.** None. A notebook that “checks” a formal proof without a kernel teaches the wrong lesson. If a companion is wanted, it is a small verifier for the implicational calculus, and the chapter still does not mention it.

**References.** Volume 15’s own sources for the four formalisation stories, cut to citations. The *Curry–Howard correspondence* as treated in a short logic text (Sørensen and Urzyczyn, or Girard–Lafont–Taylor, the implicational fragment only).

### Chapter 17. Two projects

**Aim.** Leave the reader with work, not with a survey. Two projects, each with the tools named, the first step proved, and the open step stated.

**Suggested projects, chosen because their prerequisites are now in this book.**

1. **Short-interval Turán–Kubilius.** The inequality of Chapter 3 on \([x,x+y]\), from Volume 15, Chapter 12. The first step, the second-moment calculation when \(y\) is a power of \(x\), is an exercise-sized proof. The short-interval form is the project.
2. **A bias the model misses.** Take the consecutive-residue matrix of Chapter 13 for a modulus the notebook computed, and try to extract the diagonal deficit from the singular series alone, continuing the three-star exercise. The project is to say precisely which average of the singular series would imply the Lemke Oliver–Soundararajan theorem, and which average the series has actually proved.

Rejected as projects: anything that needs Green–Tao, modularity, Artin reciprocity, or the approximate functional equation, unless that formula has been proved in Chapter 10. A project whose first step is an admitted theorem teaches the wrong habit.

**Exercises.** Four, two on each project, graded as the first steps. The solutions prove those steps and stop at the open line, with the open line named.

**Notebook.** `ch17-projects`. Data for both projects: a short-interval \(\omega(n)\) sample, and one residue matrix.

## Appendices

**A. The Borwein integrals.** The complete argument from Volume 15, Appendix A: the integral equals \(\pi/2\) while \(\sum a_k\le 1\), and the first deficit is an explicit multiple of \(\varepsilon^7\). A conjecture that died, with the corpse on the page.

**B. Cycles of the Collatz map.** Terras’s theorem and the Farey bound of \(72\,057\,431\,991\) odd terms, from Volume 15, Appendix F. The shortcut map and the cycle equation. The narrative is cut to what the proofs need.

**C. Gilmer’s inequality.** The entropy argument and the constant \((1-\ln 2)/2\), from Volume 15, Appendix H. One application, stated as the consequence Gilmer drew, with the hypotheses matched to the proof.

**D. Mason–Stothers.** \(\max\deg\le n_0(abc)-1\), and Fermat’s last theorem for polynomials, from Volume 15, Appendix I, after the degree count at lines 110–112 is corrected. The integer conjecture stays in Chapter 15.

Each appendix has four exercises and no notebook.

## Prerequisites that Volumes 0–13 do not provide

These are the outline topics that cannot be cited backward. Each is given a decision.

| Topic | Status in Volumes 0–13 | Decision in this book |
| --- | --- | --- |
| Buchstab’s theorem | Named in Vol. 5, Ch. 10, and drawn in Vol. 13, Ch. 3; not proved | Prove in Ch. 2, from the draft’s `ch11-gaps.tex` |
| Maier’s theorem | Sketched in Vol. 5, Ch. 10, not proved | Prove in Ch. 2. The draft proves it; replace its private Gallagher input by Vol. 13 |
| Erdős–Rankin large gaps | Not in Vols. 0–13; proved in the draft | Prove in Ch. 2. State the FGKMT strengthening |
| Selberg–Delange | Quoted in Vol. 10, Ch. 11, assigned to Vol. 14 | Prove in Ch. 3 |
| Kubilius model | Not a named theorem | Prove in Ch. 3 |
| Selberg’s central limit theorem and the short-sum approximation of \(\log|\zeta|\) | Not proved; Vol. 15, Ch. 4, cites the draft | Prove in Ch. 11 |
| Bohr–Jessen | Not proved | Prove in Ch. 11 |
| Approximate functional equation | Quoted in Vol. 13, Ch. 14 | Prove in Ch. 10, or mark every use of it in the recipe as quoted |
| Chowla, Sarnak for nilsequences | Open; nilsequences are not in the series | State. Prove only the periodic case |
| Gallagher’s Poisson law | Conditional in Vol. 5, Ch. 10 | Keep the hypothesis. Prove the second moment under it |
| Montgomery–Soundararajan, all moments | Discussed, not proved | Prove the second moment. State the rest |
| Parity barrier for twins | Explicitly not a theorem in Vol. 13 | State |
| Genus theory, Cohen–Lenstra 2-part | Not developed | State the 2-part. Prove the odd-part measure |
| Class-group moments | Not proved | Heuristic, in a heading that says so |
| \(n\)-Selmer group in general | Not constructed; one descent is in Vol. 12 | Construct the 2-Selmer group for one family only |
| Root numbers of elliptic \(L\)-functions | Modularity is stated, not proved | Define them for the congruent-number family. State them in general |
| Bhargava–Shankar averages | Not proved; the orbit method is absent | State |
| Poonen–Rains | Not present | Prove the linear algebra. State the arithmetic model |
| Goldfeld, BSD | BSD is stated in Vol. 12 | State |
| Green–Tao, higher inverse theorems, relative Szemerédi | Quoted in Vol. 13, Ch. 13 | State. Do not schedule a proof |
| Lemke Oliver–Soundararajan | A figure in P1, not a proof | State |
| Rubinstein–Sarnak density | Cited in Vol. 5 | Prove the torus integral, under GRH and linear independence |
| GUE pair correlation for \(\alpha>1\) | Conjecture in Vol. 13 | State |
| Moments of \(\zeta\) past the second | Fourth moment quoted; higher open | State. The matrix moments are Vol. 11 |
| Fyodorov–Hiary–Keating | Not proved; the matrix maximum is admitted in Vol. 11 | State |
| Artin reciprocity | Admitted in Vol. 12 | Not used. Cohen–Lenstra does not need it |
| de Rham, the unbounded spectral theorem, primary decomposition | Gaps in Vols. 7–9 | Not used |

Nothing in Parts I–IV requires Volume 0 or Volume 1 beyond the elementary number theory those volumes are being rewritten to contain: divisibility, congruences, quadratic reciprocity, and the three-square obstruction modulo 8. When those rewrites land, the citations in Chapters 7, 8, and 15 should be rechecked. They should not be frozen against the present text of Volumes 0 and 1.

## Order of writing

1. Repair the Volume 4, 5, 7, and 12 errors in the series review before Chapter 11 cites the functional equation, Chapter 2 cites Bombieri–Vinogradov’s surrounding text, or Chapter 13 cites the bias identity.
2. Write Chapter 11 and Chapter 3 first, from the draft. They are the theorems other chapters and the old Volume 15 cite, and they are not in Volumes 0–13.
3. Write Chapter 2 (Maier) next. It is the first theorem whose proof is new rather than mined.
4. Write Chapters 7 and 8 together, so the word “heuristic” is used the same way for class groups and for ranks.
5. Write Chapters 9 and 10 as citations with a short proved spine, after deciding whether the approximate functional equation is proved or quoted.
6. Write Chapters 4, 5, 6, 12, and 13, which are mostly reorganisation of Volumes 5 and 13.
7. Condense Part V last, after Chapters 7 and 11 have absorbed the workshop arguments they need, so those arguments are not left in two places.
8. Only then delete `tome14-random` and `tome15-workshop` from the catalog, and point `common/series.tex`, the README, and the subtitle file at one book.

## What this book is not

It is not a second proof of the prime-number theorem, of Bombieri–Vinogradov, of the sine kernel, or of Roth’s theorem. It is not a proof of Green–Tao, of modularity, or of the moments of \(\zeta\) past the second. It is not twelve open-problem tours. It is the place where the series proves Maier, the Kubilius model, Selberg–Delange, and Selberg’s central limit theorem, states the statistical conjectures that sit on top of Volumes 11–13, and teaches a reader to tell those two kinds of statement apart.
