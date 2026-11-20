# Volume 15 — Order and Chance

**Score: 8/10.**

Maier’s theorem, Selberg’s central limit theorem, Selberg–Delange, Kubilius’s model, the form factor, the mean square of \(\zeta\), Bohr–Jessen, the \(U^2\) count and the limit law of the prime race were checked step by step. The recomputed numbers match the page, including \(\delta=0.08607\), \(6/\pi^2=0.6079\), \(e^\gamma/2=0.8905\), the Buchstab table, the Selberg–Delange ratios \(1.034\), \(1.080\), \(1.454\) at \(10^7\), \(V=0.1556\), \(\mathfrak S_3=1.3203\), and the variance \(\frac12\sum_p\sum_k k^{-2}p^{-1.4k}=0.530\). The score is 8 because the slips are local: a Gamma index in the ledger, an identity in the Erdős–Kac bookkeeping that is still \(o(\sqrt{\log\log x})\), a sieve factor written as \(2\), and a handful of citations. No stated theorem fails.

**Counts.** 0 critical, 0 major, 11 minor. One prerequisite issue, `V15-003`.

**How this was read.** Book order in `volume15-order-and-chance/main.tex`: preface, The Anatomy of an Integer, Models of the Primes, Divisors, Random Multiplicative Functions, Short Intervals, Sieves, Class Groups, Ranks, Random Matrices and the Zeros, Moments, Values, Pseudorandomness, The Prime Race, The Meeting, then About the Cover. The blurb and `kdp.md` were read with the preface. Every exercise was read, including its hint and its solution. There are 164 exercises. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. Proofs are dense, in the same register as Volumes 11 and 14. Sathe–Selberg uniform in \(k\), Ingham’s fourth moment, Keating–Snaith for \(k\ge3\), Davenport–Heilbronn, Bhargava–Shankar, Goldfeld, the Poonen–Rains heuristic, Green–Tao, van der Corput’s three-prime asymptotic, Littlewood’s sign changes, and the numerical densities \(0.9959\) and \(0.9990\) are marked as quoted or as numerical evaluations. Results that need the Riemann hypothesis, the generalised Riemann hypothesis, linear independence of the ordinates, or the Hardy–Littlewood conjectures say so in their headings.

## Issues

Paths are relative to `volume15-order-and-chance/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V15-001 | `chapters/ra-erdoskac.tex:11`, proof of `thm:erdoskac-cor` | math | minor | “\(\mathbb EW=\sum_{p\le y}1/p=\log\log y+O(1)=L-\log L+O(1)\).” | With \(y=x^{1/\log L}\), \(\log\log y=L-\log\log L\). The written error \(\log L-\log\log L\) tends to infinity. Both are \(o(\sqrt L)\), so \((\mathbb EW-L)/\sqrt L\to0\) and the limit still holds. |
| V15-002 | `chapters/ra-anatomy.tex:411`, solution of `ex:primepower` | exercise | minor | “In step 3, \(X=\pm Z\) always, and the gcd is \(1\) or \(n\): the method never succeeds.” | The algorithm says that outputs of steps 1 and 2 always succeed. For \(n=9\) and \(y=3\), step 1 returns the factor \(3\). The linear-algebra step has success probability \(0\) when \(r=1\). Say that. |
| V15-003 | `chapters/ra-anatomy.tex:314`, `ex:invtau` | prerequisite | minor | “Show, with Theorem `thm:sd`, that \(\sum_{n\le x}1/\tau(n)=Cx/\sqrt{\log x}\).” | Theorem `thm:sd`, Lemma `lem:eulerprod` and the region \(U\) are proved in Chapter 3. The multiplication-table section tells the reader to postpone Corollary `cor:bigomegasd`. This exercise does not. Add the same forward pointer. |
| V15-004 | `chapters/ra-gaps.tex:192`, proof of `lem:covering` | reference | minor | “\(p''\le2n\le2(x+e^{2x})\le e^{3x}\) by Bertrand’s postulate.” | Cite Volume 2, Theorem `thm:bertrand`: for \(n\ge1\) there is a prime in \((n,2n]\). |
| V15-005 | `chapters/ra-gaps.tex:205`, proof of `lem:siftedprimes` | math | minor | “The fundamental lemma with \(\kappa=2\), \(K=3\), \(s=10\) and \(D=w^{10}=\sqrt Y\) bounds the count by \(2YV(w)+\sum\tau(d)^2\).” | Volume 14, Theorem 3.4 gives the factor \(1+Ce^{-s}\), with \(C\) depending on \(\kappa\) and \(K\). The final lemma only needs some absolute constant. Replace \(2\) by \(1+C_{\mathrm{FL}}e^{-10}\). |
| V15-006 | `chapters/ra-additive.tex:106`, proof of `thm:kubilius` | math | minor | “With \(\log(1-t)^{-1}\le t+t^2\) for \(0\le t\le\frac12\) (and the factor at \(p=2\) bounded), the product is \(\ll\log y\).” | At \(p=3\) and \(y=3\), \(t=3^{\delta-1}\approx0.91>\frac12\), and \(\log(1-t)^{-1}>t+t^2\). At \(y=2\), \(\delta>1\) and the factor at \(2\) is not of this shape. For \(y\le y_0\) bound the tail directly: it is \(O(x^{-c})\). The comparison \(d_{TV}\ll e^{-u/4}\) still holds. |
| V15-007 | `chapters/ra-additive.tex:251` | reference | minor | “A probability law on \(\mathbb R\) splits uniquely as \(\mu=\mu_d+\mu_{sc}+\mu_{ac}\) (Volume 7, Theorem 11.5; the singular part then splits into its atoms and the rest).” | Theorem 11.5 is `thm:lebdecomp`, the two-part split. The three parts are Corollary `cor:threeparts`, 11.6, in `volume7-spaces/chapters/ch10-radon.tex`. |
| V15-008 | `chapters/ra-selbergdelange.tex:225`, `cor:omegasd` | reference | minor | “This is equation (11.1) of Volume 11.” | The formula is `eq:selbergdelange` in `volume11-randomness/chapters/ch11-modphi.tex`. Equations are numbered in one sequence, not by chapter, so the printed number is not (11.1). Cite the label. |
| V15-009 | `chapters/ch14-meeting.tex:34` | math | minor | “Selberg–Delange shows that the generating function of \(\omega(n)\) carries \(\frac1{\Gamma(z+1)}\).” | Corollary `cor:omegasd` has \(\frac{F(z)}{\Gamma(z)}\). At \(z=2\) the two factors are \(1\) and \(\frac12\). The summary row’s “factor \(\frac1\Gamma\)” is the right one. |
| V15-010 | `chapters/preface.tex:6` | reference | minor | “Where an earlier volume already contains the argument, it is cited and not repeated: … Erdős–Kac, and Roth.” | Theorem `thm:erdoskac-cor` proves Erdős–Kac again, and the chapter says so. Roth is only cited. Drop Erdős–Kac from the list of arguments that are not repeated. The blurb and `kdp.md` do not make this claim. |
| V15-011 | `chapters/ra-bohrjessen.tex:115`, caption of `fig:bohrjessen` | figure | minor | “the exact variance \(\frac12\sum_p\sum_k\frac1{k^2p^{1.4k}}\) is \(0.529\).” | The series sums to \(0.53016\ldots\). Three decimals give \(0.530\). The sample variances \(0.525\) and \(0.531\) were not recomputed. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map is the fourteen chapters in `main.tex` order, and the two projects are Proposition `prop:tkshort` and the singular-series average. Maier and Selberg are unconditional in the headings that prove them. About the Cover is the pair correlation of the first \(1{,}200\) zeros against \(1-(\sin(\pi x)/(\pi x))^2\), and it names Montgomery’s paper of 1973. No notebook is promised. V15-010 is the preface’s list.

### Chapter 1

Rankin’s trick, the smooth upper and lower bounds, Dixon’s algorithm, the arcsine law for the divisor proportion, and the multiplication-table bound were checked. All ten exercises were read. \(\delta=1-(1+\log\log2)/\log2=0.08607\). \(10^7\rho(7)=8.746\). \(\Psi(10^7,10)=2155\), and the Rankin ratios at \(x=10^7\) run from about \(2.69\) to \(21\). The mean of \(1/\tau(n)\) for \(n\le10^6\) is \(0.1508\), and \(C/\sqrt{\log(10^6)}=0.147\). The parenthetical \(\log\Psi(x,\log x)\sim(\log4)\log x/\log\log x\) is the Hildebrand–Tenenbaum saddle, with \(G(1)=\log4\). The multiplication table postpones Corollary `cor:bigomegasd` and is not circular. V15-002 and V15-003 are the slips.

### Chapter 2

Chernoff’s bound, the log-free density reductions, Gallagher’s theorem with the exceptional term, Buchstab’s identity and its sign changes, Maier’s matrix, and the Erdős–Rankin balance were checked. All fourteen exercises were read. \(e^{-\gamma}=0.56146\), and \(e^\gamma\omega(u)\) changes sign at \(1.781\), \(2.483\), \(3.227\), \(4.002\), \(4.786\), \(5.566\), \(6.351\), \(7.137\). For primes \(q\le3000\), the mean of \(P(q)/(q\log^2q)\) is \(1.030\), and the largest \(\log P/\log q\) is \(1.829\) at \(q=5\). Volume 14, Theorem 2.3 is the zero-free region, Theorem 2.4 is Landau–Page, Corollary 2.12 is Siegel–Walfisz, and Theorem 4.7 is Bombieri–Vinogradov. V15-004 and V15-005 are the slips.

### Chapter 3

Turán–Kubilius, the total-variation comparison, Erdős–Wintner, Lévy’s atoms, Jessen–Wintner, the Hankel contour, and the Selberg–Delange bookkeeping were checked. All eighteen exercises were read. The proportion of abundant \(n\le10^6\) is \(0.24755\), and the maximum of \(\sigma(n)/n\) is \(4.509\) at \(n=720720\). At \(x=10^7\) the Selberg–Delange ratios are \(1.034\), \(1.080\) and \(1.454\), and \(F(2)=6/\pi^2\). Landau’s constant satisfies \(b=G(1)/\sqrt\pi\). Volume 6, Theorem 9.7 is Erdős–Kac, and Theorem 1.5 is Mertens. Volume 4, Theorem 6.10 is Lindeberg. V15-001, V15-006, V15-007 and V15-008 are the slips.

### Chapter 4

Wintner’s square-root cancellation, the fourth-moment parametrisation, the conditional central limit theorem, the model forms of Chowla and Sarnak, Birch’s second-moment identity, and van der Waerden’s count of factor types were checked. All seventeen exercises were read. There are \(1{,}017{,}072=1009\times1008\) cubic curves over \(\mathbb F_{1009}\) in the second-moment count. \(\sum_{n\le10^7}(-1)^{\omega(n)}=-1650\). The Steinhaus fourth moment at \(10^6\) is \(16.29\,x^2\).

### Chapter 5

The singular series, the second-order pair expansion, and Gallagher’s passage from binomial moments to a Poisson law were checked. All nine exercises were read. With the twin-prime constant \(C_2=0.66016\), the pair-series residuals are \(1.8\), \(2.7\) and \(9.2\) at \(H=10^2\), \(10^3\) and \(10^4\). The constant \(\frac12(1-\gamma-\log2\pi)=-0.708\). Volume 6, Theorem 10.7 is Gallagher’s average of the singular series. The direct sums \(V(10^8,H)\) were not recomputed.

### Chapter 6

Bonferroni, Brun’s pure sieve, the failure at fixed \(u\), Selberg’s projection, and Schnirelmann’s basis were checked. All eleven exercises were read. At \(u=2\), \(e^\gamma/2=0.8905\), so the coin model is \(12.3\%\) too large. \(1/2+1/3+1/5+1/7=247/210>1\).

### Chapter 7

The moments of random cokernels, Friedman–Washington, Wood’s uniqueness theorem, and the symmetric moments were checked. All ten exercises were read. The Cohen–Lenstra constants are \(0.2888\), \(0.5601\) and \(0.7603\) at \(p=2,3,5\). \(|\operatorname{Aut}(\mathbb Z/9\mathbb Z)|=6\) and \(|\mathrm{GL}_2(\mathbb F_3)|=48\). The match with class groups, apart from the quoted \(3\)-torsion, is marked as a heuristic, and the \(2\)-part is excluded.

### Chapter 8

The alternating-matrix recursion, the Euler product for the Poonen–Rains probabilities, and the passage from Selmer averages to a rank bound were checked. All ten exercises were read. With \(P=\prod_{j\ge0}(1+2^{-j})\), the masses are \(0.210\), \(0.419\), \(0.280\), \(0.080\), and the tail is \(0.011\). The rank bounds \(3/2\), \(7/6\) and \(21/20\) match the moments. Bhargava–Shankar and Goldfeld are quoted.

### Chapter 9

The form factor was checked: \(\hat K(\alpha)=(1-|\alpha|)_+\), and the transform of \(\delta_0-K\) is \(|\alpha|\) on \(|\alpha|\le1\) and \(1\) outside. The closing sentence cites that second function, and it matches Theorem `thm:formfactor`. The mean square to the right of the line was checked. All twelve exercises were read. The transform of the tent is \(K\), by the integration by parts in `ex:v15-09-4`. Volume 12, Theorem 10.4 is the sine kernel, and Volume 14, Theorem 14.15 is Montgomery’s pair correlation. The Odlyzko histograms were not recomputed.

### Chapter 10

The reduction of the critical-line mean square to the twisted second moment was checked, including the cancellation of the two poles in \(\varepsilon\). The divisor-sum comparison \(\sum_{n\le x}d_k(n)^2/n\asymp(\log x)^{k^2}\) was checked. All ten exercises were read. Ingham’s fourth moment and Keating–Snaith for \(k\ge3\) are quoted. The moment-share sample at \(T=10^6\) was not recomputed.

### Chapter 11

Kronecker–Weyl for the primes, the mollified mean square, Bohr–Jessen, the support lemma, and Jessen–Wintner’s smooth density were checked. Selberg’s argument was checked through the four steps: the move off the line, the Gaussian prime sum, the mollifier, and the twisted second moment, including the parameter constraints \(W=o(\sqrt{L_2})\) and \(\delta\log X\to\infty\). All seventeen exercises were read. \(\frac12\log\log(10^{10})=1.568\), and \(\sigma_0=\frac12+1/\log(10^6)=0.572\). Volume 6, Lemma 9.6 is the moment comparison `lem:momentslaw`. Volume 4, Theorem 6.8 is the inversion formula. V15-011 is the slip. The \(8{,}000\)-point histogram and the window correlations were not recomputed.

### Chapter 12

The three expressions for the \(U^2\) norm, the count of three-term progressions, the random-set moment, and the local factors were checked. All ten exercises were read. For \(A=\{0,1,2\}\) in \(\mathbb Z_5\), \(\Lambda_3(A)=1/5\). \(\mathfrak S_3=1.3203\). The printed ratios \(59504/62140\), \(2856331/2890267\) and \(157300309/157968254\) are \(0.958\), \(0.988\) and \(0.996\). Volume 11, Theorem 10.15 is Roth, Lemma 10.17 is the compact part, Lemma 10.18 is almost periodicity, and Lemma 10.19 is the weakly mixing average. Green–Tao, van der Corput, and the inverse theorem are quoted. The progression counts themselves were not recomputed.

### Chapter 13

The explicit formula for \(L(s,\chi_{-4})\), the mean-square comparison of the race with its waves, and the identification of the limit law under GRH and LI were checked. All twelve exercises were read. \(V=\log(4/\pi)-\gamma+2L'/L(1)=0.1556\), so \(1-V/2=0.922\). The one-wave amplitude is \(2/|\rho_1|=0.331\), and six waves are the first partial sum that exceeds \(1\). The logarithmic-density oscillation tends to \(e/(e+1)=0.731\) and \(1/(e+1)=0.269\). The partial sum of \(L(\frac12,\chi_{-4})\) through \(2\cdot10^6\) is \(0.667\). Littlewood’s theorem and the value \(0.9959\) are quoted. The race up to \(10^9\) was not recomputed.

### Chapter 14

The ledger’s fourteen lines match the theorems they name, apart from V15-009. Proposition `prop:tkshort` was checked, including \(\mu_y\le\pi(y)/2\) and the error \(5\pi(y)^2\). All four exercises were read. \(2e^{-\gamma}-1=0.1229\). At \(x=100\), \(h=20\) and \(y=4\), the sum of squares is \(95/9\) and the bound is \(110/3\). At \(h=100\) and \(y=10\), \(\mu_y+5=6.176\le6.18\). The normal-order argument cuts \(\omega\) at \(\sqrt h\) and applies Chebyshev. Volume 6, Theorem 1.5 is Mertens, and Exercise 5.3 is \(M(x)=o(x)\).

## Not checked

The book was not typeset. Shared-counter numbers were read off the source in book order. Equation numbers were inferred from `common/preamble.tex`, which does not number equations by chapter.

Not recomputed: the short-interval sums \(V(10^8,H)\), the Maier matrix, the Steinhaus sample moments, the histogram of \(V(x)\), the Chebotarev bars, the Birch histogram beyond the count \(1{,}017{,}072\), the Odlyzko and Montgomery histograms, the \(1{,}200\) zeros on the cover, the \(8{,}000\)-point Selberg histogram, the window correlations \(0.95\) and \(0.98\), the moment-share sample at \(T=10^6\), the prime-progression counts in Chapter 12, and the race up to \(10^9\). TikZ paths were not replotted. Captions whose displayed numbers were recomputed are named in the chapters above.
