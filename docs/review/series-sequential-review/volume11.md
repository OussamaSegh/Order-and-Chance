# Volume 11 — Randomness

**Score: 8/10.**

Kolmogorov’s zero–one law, Etemadi’s strong law, the three-series theorem, Donsker’s theorem, the Hartman–Wintner law, Lindeberg–Feller, Berry–Esseen with constant \(3.1\), the Lévy–Khintchine formula for the symmetric case, Stein’s Wasserstein bound, Cramér’s theorem, Sanov, the Curie–Weiss transition, Talagrand’s inequality, Johnson–Lindenstrauss, de Finetti, Kakutani, Ville, Birkhoff, Furstenberg’s proof of Roth, the Poisson–Dirichlet limit, and the transposition and riffle cutoffs were checked step by step. The numbers that were recomputed match the page, including the insurer’s gamma tail \(1.84\times10^{-15}\), the dice tilt at mean \(4.5\), Weldon’s grouped \(\chi^2\), the birthday and hash bounds, \(m^*(1.5)=0.859\), Lévy’s constant, \(\rho(3)\) by Simpson’s rule, and the twelve-uniform cosine. The score is 8 because the chapters are clean and the jacket is not: the blurb gives Birkhoff the three-term progressions, and the blurb and the listing say that one analytic-number-theory result is the only thing left unproved. No numbered theorem in the chapters was found false.

**Counts.** 0 critical, 2 major, 7 minor. One prerequisite issue, `V11-004`.

**How this was read.** Book order in `volume11-randomness/main.tex`: preface, Independence and Zero–One Laws, Laws of Large Numbers, Weak Convergence and Donsker’s Theorem, The Central Limit Theorem Sharpened, Infinitely Divisible and Stable Laws, Stein’s Method, Large Deviations, Concentration of Measure, Martingales II, Ergodic Theory, Mod-\(\varphi\) Convergence, Random Permutations and the Poisson–Dirichlet Law, Shuffling Cards (which inputs `riffle-cutoff.tex`), Sums of Random Pieces, then About the Cover. The blurb and `kdp.md` were read with the preface. Every exercise was read, including its hint and its solution. There are 166 exercises. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter. In the problem chapter the exercise name is Problem.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. The preface names the quoted theorems and sends Selberg–Delange to Volume 15. The one style fault is the dropped base of the logarithm in V11-007. Proofs are dense, in the same register as Volumes 9 and 10.

## Issues

Paths are relative to `volume11-randomness/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V11-001 | `blurb.tex:6–7` | reference | major | “Birkhoff's ergodic theorem, which explains the digits of continued fractions and proves that dense sets of integers contain progressions.” | The preface, `kdp.md`, and Chapter 10 split the two theorems. Birkhoff gives the continued-fraction frequencies. Furstenberg’s double recurrence, with the correspondence principle, gives Roth’s theorem. Name Furstenberg for the progressions. |
| V11-002 | `blurb.tex:9` and `kdp.md:11` | reference | major | “Every result is proved in full, with one clearly marked exception from analytic number theory.” | The preface already lists the infinitesimal-array converse, the nonsymmetric stable classification, and the Selberg–Delange formula, and it says that other quoted results are marked in the text. Those marks include the Kolmogorov–Smirnov law and empirical Donsker, Shevtsova’s constant, the Bahadur–Rao asymptotic, the \(2\sqrt n\) and Tracy–Widom limits, Cameron–Martin, the Gauss–Kuzmin rate, Szemerédi’s theorem for longer progressions, de Bruijn’s asymptotic for \(\rho\), and the sharp \(ae^{-2c}\) transposition bound. Say that the exceptions are marked where they occur. The Selberg–Delange formula is the one deferred to Volume 15. |
| V11-003 | `kdp.md:5` | reference | minor | “Donsker's theorem turns every random walk into Brownian motion and gives, at no extra cost, the arcsine law and the law of the iterated logarithm.” | The arcsine law is the continuous-mapping corollary of Donsker. The law of the iterated logarithm is a separate almost-sure argument from the same Skorokhod embedding. The chapter introduction does not call it free. |
| V11-004 | `chapters/ch01-zero-one.tex:22–23` and `prop:l2series` at line 253 | prerequisite | minor | “Borel–Cantelli (Volume 4, Theorem 4.4)” is stated for a general sequence of events, both halves. “Kolmogorov's maximal inequality (Volume 4, Theorem 4.3), applied to the independent centred tail increments.” | Volume 4, Theorem 4.3 is Kolmogorov’s inequality for centred variables, each bounded and a function of its own finite digit block. Theorem 4.4 is Borel–Cantelli for finite unions of digit cylinders. The Rademacher series sits inside Theorem 4.3. The general \(L^2\) sum, the bounded truncations in the three-series theorem, and the divergent half for a general i.i.d. sequence do not. One sentence that the first-crossing argument, with the integral from Volume 7, removes the digit-block hypothesis, covers both citations. The algebra was read and is the standard one. |
| V11-005 | `chapters/ch01-zero-one.tex:183–186` and `figures/ch01-trichotomy.tex` | figure | minor | “Three random walks with Gaussian steps of variance \(1\) and means \(0.12\), \(0\) and \(-0.12\).” The horizontal ticks run to \(400\). | The file draws \(201\) points. Successive vertical steps are about \(0.03\), and the three paths end at \(2.00\), \(0.676\) and \(-1.515\). Four hundred steps of variance \(1\) have standard deviation \(20\), and a drift of \(0.12\) ends near \(48\). The three fates are visible. The caption’s means and variance are not the plotted steps. |
| V11-006 | `chapters/ch02-lln.tex:45–47` | reference | minor | For a finite mean, \(nP(\lvert X\rvert>n)\) and \(\frac1n\mathbb E[X^2\mathbf 1_{\lvert X\rvert\le n}]\) “both of which tend to \(0\) (Exercise `ex:feller`).” | `ex:feller` assumes \(xP(\lvert X\rvert>x)\to0\) and proves the weak law from that hypothesis. A finite mean implies the hypothesis, by the integral tail, and that step is not the exercise. |
| V11-007 | `chapters/ch02-lln.tex:230–231` | style | minor | “a game with infinite expectation still has a law of large numbers, at the scale \(n\log n\).” | The theorem, the introduction, and the figure use \(n\log_2 n\), and \(\log\) in this series is natural. \(S_n/(n\log n)\) tends to \(1/\log 2\). Write \(\log_2\). |
| V11-008 | `chapters/ch02-lln.tex:451`, solution of `ex:chungfuchs` | reference | minor | “Volume 4, Proposition 8.4 says the walk returns to \(0\) infinitely often.” | Proposition 8.4 is the visit formula for the simple symmetric walk: if \(f=1\), then the expected number of visits is infinite and the walk returns almost surely. The solution has just shown \(\sum P(S_n=0)=\infty\) for a general centred finite-variance walk on \(\mathbb Z\). Chapter 4’s reminder already says that the restart is all the argument uses. Say that. |
| V11-009 | `chapters/ch05-stable.tex:355–356`, caption of `fig:firstpassage` | figure | minor | “computed from \(P(\tau_n=k)=\frac nk P(S_k=n)\).” | The identity is the classical ballot count, and the mode and the infinite mean in the caption do not depend on the histogram. Volumes 1–11 prove the reflection principle and the ballot theorem, and they do not record this formula. Cite that argument. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map is the fourteen chapters in `main.tex` order, and it separates Birkhoff from Furstenberg. The next volume is the geometry of continuous random paths. The stated prerequisites are Volumes 4, 7 and 8, with the representation in the shuffling chapter after Volume 10. About the Cover is two hundred walks of \(240\) steps, the curves at \(\pm 2\sqrt{240}\), and Pólya’s recurrence on the line and in the plane against space. The jacket sentences in V11-001 and V11-002 are the faults. No notebook is promised.

### Chapter 1

The \(\pi\)-system lemma, grouping, Kolmogorov’s zero–one law, Hewitt–Savage with the \(4\varepsilon\) bound, the trichotomy, Ottaviani, Lévy’s equivalence of convergence in probability and almost sure convergence, the Paley–Zygmund bound \(P(T^2>\sigma^2/2)\ge1/12\), and the random harmonic series were checked. The distributional form of Lévy’s equivalence is marked as not proved. The numerical integral for the harmonic density matches Schmuland’s \(g(0)=0.2499943958\), and \(P(X\ge4)\approx2.0\times10^{-7}\). All eleven exercises were read. The fourth-moment ratio is at most \(2\), with equality exactly when the two nonzero coefficients have equal square. The dyadic signs are uniform on \([-1,1]\).

### Chapter 2

The triangular weak law, Feller’s St Petersburg theorem \(S_n/(n\log_2 n)\to1\) in probability, Etemadi, Kolmogorov’s lower inequality, the three-series theorem, Kronecker’s lemma, and \(N(t)/t\to1/\mu\) were checked, including the infinite-mean renewal by the earlier exercise. The St Petersburg tail bounds \(1/(2x)\le P(X>x)\le2/x\) and the truncated second moment \(\le2b\) match the proof. The renewal figure, lifetimes \(2,1,3,2\), has \(N(5)=2\). All eleven exercises were read. The Bernoulli cutoff tends to \(1-e^{-1}\). The fair lifetimes \(1\) and \(3\) have mean life \(2\), mean reward \(5\), and reward rate \(5/2\).

### Chapter 3

Lévy’s continuity theorem, Cramér–Wold, the multivariate CLT, continuous mapping, the strong Markov property, optional stopping for Brownian motion, the exit law \(P(B_\tau=b)=-a/(b-a)\) and \(\mathbb E\tau=-ab\), Skorokhod’s embedding with \(\mathbb E\tau=\mathbb EX^2\), Donsker’s theorem, the maximum, Chung–Feller, the arcsine law, and both laws of the iterated logarithm were checked. \(\sqrt{2\log\log10^6}\approx2.29\). The exit of \((-1,1)\) has mean \(1\) and variance \(2/3\). The area of the Brownian path has variance \(1/3\). All eleven exercises were read. The Kolmogorov–Smirnov series is marked as not proved.

### Chapter 4

The Lindeberg–Feller converse, Lyapunov’s condition, Esseen’s smoothing, the characteristic-function estimate, and the constant \(3.1\) were checked. The bracket is \(4/(3\sqrt\pi)+18/(\pi\sqrt{2\pi})\approx3.038\). The lattice lower bound uses Volume 4, Lemma 8.9, and gives \(C_0\ge0.35\). Weldon’s \(n=26306\) expectations round to the printed table; the merged \(\chi^2\) is \(35.494\) on \(10\) degrees of freedom, and the fitted statistic is \(8.180\) on \(9\). All eleven exercises were read. The rare array has characteristic function tending to \(e^{\cos t-1}\), not to a Gaussian. Shevtsova’s \(0.4748\) is quoted.

### Chapter 5

The continuous logarithm, Lévy–Khintchine, the triangular-array theorem in the direction that is proved, the symmetric stable laws, the symmetric domain of attraction, Schlömilch’s series, the hitting-time density, and the gambler’s wait were checked. The median constant \(1/(\Phi^{-1}(3/4))^2\approx2.20\) matches the printed \(2.2\). Cauchy returns \(e^{-\lvert t\rvert}\) with \(\kappa_1=\pi/2\). All eleven exercises were read. The array converse and the nonsymmetric stable formula are marked as quoted.

### Chapter 6

Stein’s lemma, the derivative bounds, the comparison \(d_K\le(2/\pi)^{1/4}\sqrt{d_W}\), the Wasserstein CLT with constant \(3\), the exchangeable-pair bound, and Chen–Stein were checked. For \(23\) birthdays the exact probability of no shared day is \(0.4927\), printed \(0.493\), and the bound is \(0.116\), printed \(0.12\). The near-birthday count for \(n=14\) is \(0.4625\), printed \(0.463\). The hash bounds at \(d=2^{32}\) match. The hypergeometric Wasserstein distance is about \(0.0167\), printed \(0.017\). All eleven exercises were read. Le Cam is Volume 4, Theorem 10.12.

### Chapter 7

The cumulant lemma, the rate function, Cramér’s theorem, the method of types, Sanov, Gibbs conditioning, Chernoff–Stein, Varadhan’s lemma, and the Curie–Weiss transition were checked. For \(100\) exponential claims, the probability of a total past \(200\) is \(1.844\times10^{-15}\), the exponential bound is \(4.72\times10^{-14}\), Bahadur–Rao gives \(1.88\times10^{-15}\), and \(1-\Phi(10)=7.62\times10^{-24}\). The dice tilt at mean \(4.5\) has \(\theta=0.371\) and rate \(0.178\), and \(P(\mathrm{sum}\ge450)=1.52\times10^{-9}\). \(m^*(1.5)=0.859\) and \(m^*(2)=0.958\). The coin relative entropies are \(0.0204\) and \(0.0201\), and the Chernoff information is \(0.00508\). All eleven exercises were read.

### Chapter 8

Efron–Stein, McDiarmid, the Gaussian log-Sobolev inequality, Herbst’s argument, the chi-square tails, Johnson–Lindenstrauss, and Talagrand’s induction were checked. For a million points and \(\varepsilon=0.1\) the dimension is at least \(11842\). A Gaussian vector in dimension \(10^6\) lies within \(3\) of its mean length, between \(999\) and \(1000\), with probability at least \(1-2e^{-9/2}>0.97\). All ten exercises were read. The longest-increasing-subsequence expectation is at most \(2e\sqrt n+1\). The limit \(2\sqrt n\) and the Tracy–Widom law are quoted.

### Chapter 9

Uniform integrability, Lévy’s upward and downward theorems, optional stopping, the backward proof of the strong law, de Finetti, Doob’s consistency, Kakutani, and Ville were checked. At European roulette, \((18/19)^{20}=0.339\), printed \(0.34\). The Beta mixture for Pólya’s urn matches the sequential probability. The Poisson affinity is \(e^{-(\sqrt\lambda-\sqrt\mu)^2/2}\). All eleven exercises were read. Volume 4, Theorem 11.5(2) is the optional-stopping criterion with finite mean time, and the fair-walk solution uses it correctly. Cameron–Martin is quoted.

### Chapter 10

Poincaré, Kac, von Neumann, the maximal lemma, Birkhoff, the Gauss measure, the continued-fraction statistics, and Furstenberg’s double recurrence through the compact and weakly mixing parts were checked. Lévy’s constant is \(\pi^2/(12\log 2)=1.18657\), and \(e^{2.373}=10.73\). The golden-ratio growth rate is \(\log\varphi=0.4812\). All eleven exercises were read. The mean return to HH is \(4\), and the Gauss tail of the first digit is \(\log_2(1+1/k)\), whose sum diverges. Szemerédi’s theorem for progressions longer than three, and the Gauss–Kuzmin rate, are quoted. The proof of Roth is Furstenberg’s, as the preface says.

### Chapter 11

Mod-Gaussian and mod-Poisson convergence, the cycle theorem, and the passage from the admitted Selberg–Delange formula to \(\omega(n)\) were checked. \(H_{10^6}\approx14.4\), \(e^{-\gamma}=0.561\), and \(e^{\gamma/2}/\sqrt\pi=0.753\). The product of the first nine primes is \(223092870>10^8\), so no integer up to \(10^8\) has nine distinct prime factors. All nine exercises were read. The uniform residue on \([- \sqrt3,\sqrt3]\) has fourth cumulant \(-6/5\), and the logarithmic expansion \(-t^4/(20k^2)\) matches. The Selberg–Delange formula itself is the admitted input.

### Chapter 12

Cauchy’s formula, the conditioning relation, the GEM coupling, the Poisson–Dirichlet limit, Dickman’s equation, and Billingsley’s theorem were checked. Simpson’s rule on \([2,3]\) gives \(\int g\approx0.14718\) and \(\rho(3)\approx0.0486\). The Golomb–Dickman constant is printed to ten digits, \(0.6243299885\), which matches the published expansion; the integral was not recomputed to that precision here. Two uniform points lie in the same cycle with probability \(1/2\), and \(\mathbb E\sum V_i^2=1/2\). The five types of a permutation of four elements have probabilities \(1/4\), \(1/3\), \(1/8\), \(1/4\), \(1/24\). All ten exercises were read. de Bruijn’s asymptotic is quoted.

### Chapter 13

The upper bound lemma, the transposition eigenvalues, the cutoff at \(\frac12 n\log n\), Bayer–Diaconis, Tanny’s theorem, and the Gaussian profile of the rising sequences were checked. For three cards, \(d(0)=5/6\) and \(d(1)=1/3\). The fixed-point mean is \(1+(n-1)(1-2/n)^t\). The riffle profile at the printed scales is \(2\Phi(1/2)-1\approx0.383\) and \(2\Phi(1/4)-1\approx0.197\). All ten exercises were read. The sharp \(ae^{-2c}\) bound is quoted. The character formula is the one proved in Volume 10.

### Chapter 14

All twenty-eight problems were read, with their hints and solutions. The pairwise Walsh sums are bounded and tend to \(0\) almost surely, while the normalized sum tends to \(0\) in probability. The lacunary variance is \(1/4\) in base \(2\) and \(1/6\) in base \(3\). The peak count has mean \((n-2)/3\) and variance \(2(n+1)/45\). The domino variance is \(1/(5\sqrt5)\), and the mean proportion is \((5-\sqrt5)/10\). Harper’s real-root decomposition and the variance identity \(\operatorname{Var}K_n=\operatorname{Var}M-1\) were checked. Twelve centred uniforms give \((2\sin\frac12)^{12}=0.603968\) against \(e^{-1/2}=0.606531\), and \(P(\lvert W\rvert>4)=1.705\times10^{-5}\). The Kolmogorov series at \(1.36\) is \(0.9505\) from one term on the left and \(0.9459+0.0046\) from two terms on the right. The square-walk Fourier bound tends to \(\frac12 e^{-\pi^2/5}=0.0695\).

## Not checked

Shevtsova’s constant \(0.4748\), the Watson–Pólya integral \(1.5163\ldots\) beyond the printed relation \(1-1/1.5163\), the birthday figure’s claim that the true error never exceeds \(0.011\) for every \(n\), and the Golomb–Dickman integral to ten digits were not recomputed. Weldon’s historical odds and Bernoulli’s count \(25550\) were not rebuilt from the binomial tail. The quoted theorems named in V11-002 were not proved again. Figure seeds other than the trichotomy coordinates were checked through the stated parameters and the captions, not by regenerating the pictures. The book was not typeset in this pass.
