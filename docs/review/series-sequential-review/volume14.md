# Volume 14 — The Primes

**Score: 7/10.**

Carlson’s density bound, Siegel’s theorem, the fundamental lemma, Bombieri–Vinogradov, Vinogradov’s exponential sum, the three-primes asymptotic, Hua’s bound \(G(k)\le\max(4k,2^k+1)\), Maynard’s ratio \(M_{582}>4\), and Hardy’s theorem on the critical line were checked step by step. The recomputed numbers match the page, including the class-number bounds \(3.323,4.643,6.860,12.025,16.166,28.828\), the Artin proportions \(0.37391,0.37411,0.39394,0.37449\) at \(10^7\), the partial product \(P=0.374640\), the gap \(5167-587=4580\) and the value \(M_{582}=4.000347\), the ratio \(1417255/708216\), and the singular series \(2.301,1.534,1.416,1.370\). The score is 7 because the written estimate in Hooley’s proof is too large to prove the theorem, and the blurb lists a quoted theorem among the complete proofs.

**Counts.** 0 critical, 2 major, 6 minor. No prerequisite issue.

**How this was read.** Book order in `volume14-primes/main.tex`: preface, Zeros and Primes in Short Intervals, Siegel’s Theorem, Sieves and the Parity Problem, The Large Sieve and Bombieri–Vinogradov, Exponential Sums over Primes, Waring’s Problem, Three Primes, Small Gaps between Primes, Bounded Gaps between Primes, Halász’s Theorem, Sums and Products, Roth’s Theorem, Gowers Norms and the Green–Tao Theorem, The Critical Line, then About the Cover. The blurb and `kdp.md` were read with the preface. Every exercise was read, including its hint and its solution. There are 136 exercises. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. Proofs are dense, in the same register as Volumes 11 and 13. The Vinogradov–Korobov zero-free region, Chen’s theorem, the Vinogradov mean value theorem, Weil’s bound, Zhang’s theorem, the Matomäki–Radziwiłł theorem, Freiman’s theorem, the polynomial Freiman–Ruzsa theorem, the theorems of Szemerédi and of Kelley and Meka, the higher Gowers inverse theorem, the Green–Tao theorem, and a positive proportion of zeros on the critical line are marked as quoted. Results that need the Riemann hypothesis, the generalised Riemann hypothesis, or a level of distribution past \(\frac12\) say so in their headings. The Siegel–Walfisz constant is marked ineffective wherever it is inherited.

## Issues

Paths are relative to `volume14-primes/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V14-001 | `chapters/ch03-sieves.tex:414–416`, proof of `thm:hooley` | math | major | “\(M_1\le\sum_{\xi_1<q\le\xi_2}\pi_q(x)\le\operatorname{li}(x)\sum_{q>\xi_1}\frac1{q(q-1)}+O(\xi_2\sqrt x\log x)=O(x/\log^2x)\).” | With \(\xi_2=\sqrt x/\log^2x\), the error is \(\xi_2\sqrt x\log x=x/\log x\), the same size as \(A\operatorname{li}(x)\). The written bound does not prove \(N(x)=A\operatorname{li}(x)+O(x\log\log x/\log^2x)\). Replace \(\xi_2\) by \(\pi(\xi_2)\ll\xi_2/\log\xi_2\), which is Volume 6, Proposition 1.2, and restores \(O(x/\log^2x)\). |
| V14-002 | `blurb.tex:1–2` | reference | major | “with complete proofs: … Gowers norms and the Green–Tao theorem, Hardy’s theorem…” | Theorem `thm:greentao` is marked quoted, and the preface lists it among the theorems that are not proved. Drop Green–Tao from the list of complete proofs, as `kdp.md` does with its short list of quoted theorems. |
| V14-003 | `chapters/ch02-siegel.tex:209` | reference | minor | “for \(0<\varepsilon<\frac1{11}\), \(L(1,\chi)\ge\frac{0.655\,\varepsilon}{q^\varepsilon}\) for all real primitive \(\chi\) modulo \(q\ge\max(e^{1/\varepsilon},e^{11.2})\) … (Exercise `ex:ineffective`).” | Tatuzawa’s range is \(0<\varepsilon<1/11.2\). The constant \(0.655\) is not in the exercise, which explains only why Siegel’s \(c(\varepsilon)\) cannot be computed. Cite Tatuzawa’s paper, and keep the exercise for the ineffectivity. |
| V14-004 | `chapters/ch02-siegel.tex:300` | math | minor | “An effective lower bound, growing like \(\log\|d\|\) up to a factor smaller than any power of \(\log\|d\|\), came only in 1983–1986.” | Goldfeld’s theorem, once Gross and Zagier supply a triple zero, is \(h(d)\gg_\varepsilon(\log\|d\|)^{1-\varepsilon}\). The factor lost is a positive power of \(\log\|d\|\), which may be taken arbitrarily small. |
| V14-005 | `chapters/ch03-sieves.tex:215`, proof of `lem:zetaline` | math | minor | “since \(3\le\|t\|-\frac14\le\|\operatorname{Im}s'\|\le\|t\|+1\le\|t\|^2\), so (a) bounds \(\zeta\) there.” | For \(\|t\|\) near \(3\), the circle of radius \(1/(4\log\|t\|)\) meets \(\|\operatorname{Im}s'\|<3\), where (a) is not stated. Extend (a) down to \(\|t\|\ge2\), which the same estimate gives, before invoking Cauchy. |
| V14-006 | `chapters/ch03-sieves.tex:128`, proof of `thm:fl` | math | minor | “the case already proved, at \((z',s_0)\), gives \(S\le2XV(z')\).” | At the threshold \(s_0=\log(6/v)\), the relative error \(Ce^{-s_0}\) is \(2\), so the bound already proved is \(3XV(z')\). The final constant still exists; replace \(2\) by \(3\). |
| V14-007 | `chapters/ch03-sieves.tex:546`, solution of `ex:sg` | math | minor | “by Corollary `cor:parity`, a sieve can give an upper bound of the right order … but never a single pair.” | The corollary forbids a sieve proof that the integers contain primes. The think box above it says that the same obstruction for twins needs Chowla’s conjecture and is not proved. The Sophie Germain pairs are in that second case. |
| V14-008 | `chapters/ch04-largesieve.tex:249` | math | minor | “Each of the about \(\frac{Q^2}2\) terms in the sum is the square of a deviation.” | The number of terms is \(\sum_{q\le Q}\varphi(q)\sim\frac3{\pi^2}Q^2\), about \(0.304\,Q^2\). The typical size \(\sqrt{(x/q)\log x}\) is unchanged. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map is the fourteen chapters in `main.tex` order. The bound \(4580\), the quoted records \(600\) and \(246\), and the list of quoted theorems match the chapters. The interval \(]x,x+x^{0.76}]\) is a case of Corollary `cor:hoheisel`. About the Cover is the path of \(\zeta(\frac12+it)\) from height \(10\) to \(42\), and it names Riemann’s memoir of 1859. No notebook is promised. V14-002 is the blurb’s overclaim.

### Chapter 1

Ingham’s machine, the mean-value lemma, the short Dirichlet polynomial for \(\zeta\), the mollified mean square, and Carlson’s exponent \(4\sigma(1-\sigma)\) were checked, including the disc geometry \(R-r'\ge\eta/3\) and the dyadic sum. All ten exercises were read. \(4\cdot0.9\cdot0.1=0.36\), \(8/9<17/18\), and \(10^{-2/5}\approx0.398107\). The gap after \(436\,273\,009\) is \(282\), so there are \(281\) composites, and \((\log p)^2\approx395.8\). Volume 6, Theorem 6.3 is Jensen, Theorem 6.9 is \(N(T)\), Corollary 6.10 is the unit interval, Theorem 6.12 is the classical zero-free region, Theorem 7.5 is the explicit formula, and Exercise 6.6 is the formula for \(\zeta\). Exercise 7.4 is Cramér’s \(\sqrt x\log^3x\). The curves in `figures/ch01-density.tex`, `figures/v14c01-cost.tex` and `figures/v14c01-theta.tex` match the exponents they name.

### Chapter 2

The \(3\)-\(4\)-\(1\) zero-free region, Page’s repulsion, Estermann’s proof of Siegel’s theorem, and Siegel–Walfisz were checked. The class-number formula used is Volume 13, Theorems 11.9 and 11.10, and \(h(-p)=\sqrt p\,L(1,\chi_p)/\pi\). All ten exercises were read. The upper bounds at \(p=7,11,19,43,67,163\) are \(3.323,4.643,6.860,12.025,16.166,28.828\). The partial sum of \(\chi_4\) through \(19\) lies between \(0.760\) and \(0.764\). Volume 6, Lemma 6.6 is the local zero lemma, Proposition 6.11 is the local formula for \(\zeta'/\zeta\), and Theorem 7.8 is \(\psi(x)=x+O(xe^{-c\sqrt{\log x}})\). V14-003 and V14-004 are the slips.

### Chapter 3

Bonferroni’s truncation, the fundamental lemma, Selberg’s parity example, and the Liouville bound with exponent \(1/10\) were checked. All ten exercises were read. \(e^\gamma/2\) lies between \(0.89053\) and \(0.89055\). The product through \(p=7\) is \(175/256\). Among the primes \(p\le10^7\), the proportions for primitive roots \(2,3,5,10\) are \(0.373907,0.374111,0.393935,0.374494\), and \(P=0.374640\) for the twenty-five primes \(q\le100\). The rough-number ratios at \(x=10^7\) are \(0.954\) at \(u=2\), \(0.935\) near \(u=2.1\), and \(1.005\) near \(u=3\), and they stay within \(3\cdot10^{-4}\) of \(1\) for \(u\ge3.5\). Volume 13, Theorem 4.18 is the decomposition group, Corollary 7.5 is cyclotomic ramification, and Theorem 11.23 is Chebotarev in Dirichlet density. V14-001, V14-005, V14-006 and V14-007 are the slips.

### Chapter 4

The multiplicative large sieve, Vaughan’s identity, the bilinear form, the main estimate, Bombieri–Vinogradov, the Barban–Davenport–Halberstam variance, and Linnik’s non-residue theorem were checked. All eleven exercises were read. Hooley’s constant is \(4.17046\ldots\), the product through \(p=19\) is \(1.92315\), and \(\sum p_k/2^k=3.67464\ldots\). Among the \(78497\) odd primes below \(10^6\), the mean of \(n_2(p)\) is \(3.646\), the maximum is \(n_2(366791)=43\), and the proportion with \(n_2(p)=p_k\) stays within \(1.2\%\) of \(2^{-k}\) for \(k\le8\). At \(x=e^{60}\) and \(A=1\), \(3<e^{30}/60^7<4\). \(\zeta(2)\zeta(3)/\zeta(6)=1.94360\). Volume 6, (8.1) is the arithmetic large sieve, Theorem 8.8 is the large sieve, and Theorem 8.10 is Montgomery’s form. Volume 11, Corollary 12.18 is Dickman’s theorem. V14-008 is the slip.

### Chapter 5

Dirichlet’s approximation, Vinogradov’s bound, the major-arc lemma, the Kloosterman moments, and Salié’s evaluation were checked. All ten exercises were read. \(p^2-p-1=19\) and \(2p^3-3p^2-3p-1=159\) at \(p=5\), and the four sums are \((3-\sqrt5)/2\), \(-(1+\sqrt5)\), \(\sqrt5-1\) and \((3+\sqrt5)/2\), with square sum \(19\). The moment bound is the smaller one exactly for \(p<8\). Volume 6, Lemma 11.1, Lemma 11.6 and Theorem 11.4 are the citations used, and Theorem 3.5 is the Gauss sum. Volume 5, Theorem 6.13 is Weyl’s criterion.

### Chapter 6

Weyl differencing, Hua’s lemma, the singular integral, the lifting of \(k\)-th powers, and the bound of \(4k-1\) local summands were checked. All ten exercises were read. \(\Gamma(3/2)^5/\Gamma(5/2)=\pi^2/24\), and \((\pi^2/24)n^{3/2}\) is \(0.411,3.290,11.103\) at \(n=1,4,9\). The only nineteen fourth powers that sum to \(79\) are four sixteens and fifteen ones. For \(p=3\) and \(n=1\), the congruence of four squares has \(24=27-3\) solutions. Volume 5, Theorem 5.11 is the Beta integral, Proposition 5.2 is \(\Gamma(x+1)=x\Gamma(x)\), and Proposition 5.12 is \(\Gamma(1/2)=\sqrt\pi\).

### Chapter 7

The singular series, the minor-arc saving, and the count of triples were checked. All eight exercises were read. For odd \(N\), \(1\le\mathfrak S(N)\le4\). The values at \(N=1,9,15,105\) are \(2.301,1.534,1.416,1.370\). The partial product for \(\mathfrak S(9)\) through \(p=19\) is \(1.53354\). \(\binom{9}2=36\) and \(10^2/2=50\). The factor at \(3\) drops the series by \(2/3\).

### Chapter 8

The comparison \(S_2-\rho S_1\), the one-variable ratio \(2k(2\ell+1)/((\ell+1)(k+2\ell+1))<4\), and the conditional bound \(20\) were checked. All nine exercises were read. For \(k=7\) and \(\ell=1\) the ratio is \(42/20=2.1\), and \(2/\theta<2.1\) once \(\theta>20/21\). The five primes above \(5\) run from \(7\) to \(19\), and the ten primes above \(10\) run from \(11\) to \(43\). Volume 6, Theorem 10.7 is Gallagher’s average of the singular series. Zhang’s theorem is quoted.

### Chapter 9

The product test, Chebyshev’s bound, the parameters \(A=7\), \(T=39\), \(k=582\), and the symmetric-polynomial ratio for \(k=5\) were recomputed. All ten exercises were read. \(M_{582}\ge4.000347>4\). The \(582\) primes from \(587\) to \(5167\) are an admissible tuple of diameter \(4580\). The integrals of Maynard’s polynomial are \(I_5=29509/1222452000\) and \(\sum J=40493/838252800\), and their ratio is \(1417255/708216\). The threshold \(\theta>0.99942\) then gives the gap \(12\). The records \(600\) and \(246\) are quoted, and the text says the certificates are not printed.

### Chapter 10

The distance \(\mathbb D\), Halász’s inequality, Delange’s theorem, Wirsing’s theorem, and the deduction \(\sum_{n\le x}\mu(n)=o(x)\) were read, and the exercises were checked. All nine exercises were read. \(\sum_{p\le20}2/p\) lies between \(2.904\) and \(2.914\), and \((1+m)e^{-m}\) decreases on \(m\ge0\). The Matomäki–Radziwiłł theorem is quoted. The Plancherel step in the body of Halász’s inequality was not recomputed from Volume 8 line by line.

### Chapter 11

Ruzsa’s triangle inequality, Petridis’s proof of Plünnecke–Ruzsa, the Balog–Szemerédi–Gowers theorem, Szemerédi–Trotter, and Elekes’s deduction were read. All ten exercises were read. For \(A=\{1,2,4\}\), \(|A+A|=6\) and \(|A\cdot A|=5\). The energy of an interval of length \(n\) is \((2n^3+n)/3\). The grid of \(k^3\) lines gives \(k^4=2^{-2/3}|\mathcal P|^{2/3}|\mathcal L|^{2/3}\) incidences. Freiman’s theorem and the polynomial inverse theorem are quoted.

### Chapter 12

The counting lemma, the density increment, Roth’s iteration, and Behrend’s sphere were read. All nine exercises were read. At \(N=10^6\), \(500/\log\log N>185\), so the printed threshold gives no information. A \(3\)-AP in the base-\(3\) set of digits \(0,1\) forces equal digits. Kelley–Meka and Szemerédi’s theorem for every length are quoted.

### Chapter 13

The \(U^2\) inverse theorem, the generalised von Neumann inequality, and the \(W\)-trick were read. All ten exercises were read. \(\varphi(6)/6=1/3\) and \(\varphi(30)/30=4/15\). A linear phase has \(U^1\) norm \(0\) and \(U^k\) norm \(1\) for \(k\ge2\). The factor of the singular series at \(p=2\) for length \(3\) is \(2\). The inverse theorem and the Green–Tao theorem are quoted. V14-002 is the blurb’s claim that this theorem is proved in full.

### Chapter 14

The cosine transform of \(\Xi\), the vanishing of the derivatives of \(\theta\) at \(i\), Hardy’s moment contradiction, the derivative test, the length-\(t\) formula for \(\zeta\), and Hilbert’s inequality were checked. Montgomery’s pair correlation was read under the Riemann hypothesis it assumes. All ten exercises were read. The moment limits are \((-1)^n\pi\cos(\pi/8)/4^n\), and \(\sum_{n\le10}1/n=7381/2520\). The proportion theorems, the approximate functional equation, and the Riemann–Siegel formula are quoted.

## Not checked

The book was not typeset. Figures were read from the TikZ sources and the captions. The plotted sums in `fig:bv` and `fig:bdh`, the fast-Fourier ratios for \(R(N)\), the five-squares correlation \(0.993\) and mean ratio \(0.93\), the Kloosterman histogram at \(p=100003\), and the \(20000\) samples in `fig:chance` were not recomputed. Hardy’s identity was not evaluated to twenty digits. The quoted theorems named above were not proved again. The Plancherel constant in Halász’s inequality was not rederived from Volume 8.
