# Volume 6 — Crossroads

**Score: 8/10.**

Mertens’s three theorems, the divisor and totient averages, non-vanishing of \(L(1,\chi)\), Dirichlet’s theorem, Newman’s proof of the prime number theorem, the classical zero-free region, the explicit formula, Selberg’s sieve, Brun–Titchmarsh, the Erdős–Kac theorem, Cramér’s gap theorem, Gallagher’s average, Weyl’s inequality, Pólya–Vinogradov, and the dimension count that gives Ramanujan’s congruence and the multiplicativity of \(\tau(n)\) are proved. The constants that were recomputed match the page. The score is 8 because the slips are local: a mis-pointed citation, a constant named inside an error term that still contains it, one contour limit left unnamed, and the exercise grade `[Journey]`. No numbered theorem is false, and no proof uses a tool the earlier volumes have not given. Two facts are admitted, each in one place, and the preface names both.

**Counts.** 0 critical, 0 major, 10 minor. Ten issues, `V6-001` through `V6-010`. No prerequisite issue.

**How this was read.** Book order in `volume6-crossroads/main.tex`: preface, Counting Primes (Chapters 1–5), Zeros and Explicit Formulas (6–7), Sieves and Randomness (8–12), then the index, the sources, and About the Cover. The blurb and `kdp.md` were read with the preface. Every chapter file was read, including every exercise, hint, and solution. The shared counter was counted in source order. The index numbers match that count, including Exercise 5.1 and Section 3.5.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. The repeated slip is the exercise grade `[Journey]`, which the box prints in place of the stars. It occurs fifteen times, and it is V6-001. Two sentences begin with “Moreover” (`chapters/ch05-pnt.tex:228`, `chapters/ch10-random.tex:140`), and the solution of `pb:erdosnp` uses “one must” twice.

## Issues

Paths are relative to `volume6-crossroads/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V6-001 | `chapters/ch03-characters.tex:354` (`pb:primroot`); also `chapters/ch11-sums.tex` (`pb:erdosnp`, `pb:leastprimroot`) and `chapters/ch12-modular.tex` (`pb:beukersthree`, `pb:twosquares`, `pb:ramanujanE2`, `pb:landauzeros`, `pb:hearzeros`, `pb:cramersign`, `pb:selberg`, `pb:schur`, `pb:euler41`, `pb:hecke`, `pb:shifted`, `pb:romanoff`) | style | minor | The optional argument is `[Journey]`, which the exercise box prints in place of the stars. | The preface grades exercises \(\star\), \(\star\star\), and \(\star\star\star\). Give each of these fifteen the grade \(\star\star\star\), or say in the preface what Journey means. |
| V6-002 | `chapters/ch01-mertens.tex:40`; the reconciliation is `chapters/ch06-zeros.tex:330` | reference | minor | “\(\theta(x)=\sum_{p\le x}\log p\)”. | Volume 2 writes the same sum as \(\vartheta(x)\). Chapter 6 says the series keeps \(\theta\) for Chebyshev and \(\alpha\) for Hardy’s phase. Put that sentence at the definition in Chapter 1. |
| V6-003 | `chapters/ch01-mertens.tex:446` (`pb:poissoncycles`) | exercise | minor | “tends to \(e^{-H_{m-1}}\approx e^{-\gamma}/m\) as \(n\to\infty\)”. | The limit in \(n\) is \(e^{-H_{m-1}}\). The comparison with \(e^{-\gamma}/m\) is the further limit \(m\to\infty\). The solution already separates the two. Write them as two sentences in the exercise. |
| V6-004 | `chapters/ch02-averages.tex:263` | math | minor | “\(\gamma_1=-0.0728\ldots\) is the Stieltjes constant, the coefficient after \(\gamma\) in the expansion of \(\zeta\) at \(1\)”. | The value and the constant term \(3\gamma^2-3\gamma-3\gamma_1+1\) of \(P_3\) match the Stieltjes convention \(\zeta(s)=1/(s-1)+\sum (-1)^n\gamma_n(s-1)^n/n!\). The coefficient of \(s-1\) is \(-\gamma_1\). The sentence is quoted and unused. Say “Stieltjes constant”, and drop “the coefficient after \(\gamma\)”. |
| V6-005 | `chapters/ch02-averages.tex:530` (solution of `ex:nphi`) | reference | minor | “\(h\) is multiplicative (Volume 2, Proposition 4.3)”. | Proposition 4.3 says that a convolution of multiplicative functions is multiplicative. Here \(h=\mu^2/\varphi\). Both factors are multiplicative and \(\varphi\) never vanishes, so the quotient is multiplicative. Cite that, and keep the prime-power check that follows. |
| V6-006 | `chapters/ch02-averages.tex:575` (solution of `ex:twoomega`) | math | minor | “The constant in the next term can be named: it is \(Cx\) with \(C=\frac6{\pi^2}\bigl(2\gamma-1-2\zeta'(2)/\zeta(2)\bigr)=0.7869\ldots\)”. | The argument proves \(\sum_{n\le x}2^{\omega(n)}=(6/\pi^2)x\log x+O(x)\). That error still contains \(Cx\). The value \(0.7869\) matches the sum through \(10^6\). Derive the constant from the constant term of \(\sum_{n\le x}\mu^2(n)\), or leave it inside the \(O(x)\). |
| V6-007 | `chapters/ch03-characters.tex:204` (caption of `fig:lreal`) | figure | minor | “The even character \(\chi_5\) tends to \(0\) as \(\sigma\to 0\)”. | The four values at \(\sigma=1\) are proved. The limit at \(0\) is a numerical reading of the plate. The functional equation of \(L(s,\chi)\) is admitted only later, and no theorem uses it. Say that the curve is the partial sum of the series. |
| V6-008 | `chapters/ch07-explicit.tex:169` (`eq:zetaprime0`) | math | minor | “With \(B=\frac12\log(4\pi)-1-\gamma/2\) (Exercise `ex:digammahalf`), this is \(\log(2\pi)\)”. | The identity \(\zeta'/\zeta(0)=\log(2\pi)\) is used as a residue in the explicit formula. The value of \(B\) is computed in a later exercise, whose solution does not use this section. Move the evaluation of \(B\) before the residue, or quote it as the constant already fixed by \(\xi'/\xi\). |
| V6-009 | `chapters/ch12-modular.tex:240` (second proof of `thm:eta`) | math | minor | “Bounded convergence gives \(\int_C f_N\to 4\log y\)”. | On each compact subedge the integrand converges uniformly, and it is bounded on the whole contour by a constant independent of \(N\). That is Volume 5, Corollary 4.5, once the four vertices are cut out. Name the corollary and the cutoff. The identity \((\ast)\) and the transformation of \(\eta\) then stand. |
| V6-010 | `chapters/ch12-modular.tex:2183` (solution of `pb:landauzeros`) | math | minor | “No zero has \(0<\gamma\le 1\)”. | Chapter 6 records the first tabulated ordinate \(14.13\) and says the table is not recomputed. A zero of ordinate at most \(1\) would contribute \(O_x(1)\) to the sum, which the error \(O_x(\log^2 T)\) already contains. Say that, and keep the rectangle. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map matches the twelve chapters. It names the two admitted facts: the functional equation of a primitive \(L\)-function, used in one remark of Chapter 7 and in no theorem, and Tonelli’s theorem, used in the solution of `pb:beukersthree`. The blurb’s lead of the class \(4n+3\) up to \(26861\) is the finite race recomputed in Chapter 4: ten ties, and the difference \(-1\) only at \(26861\) and \(26862\). The figure \(99.59\%\) is labelled as Rubinstein–Sarnak. The three observations in `kdp.md` are the three patterns in the opening of Chapter 12. The class-number formula and the Vinogradov–Korobov shape are marked as quotations where they appear. About the Cover uses the Farey gaps proved in `pb:farey`, and it labels the Franel–Landau equivalence with the Riemann hypothesis as a quotation.

### Chapter 1

Abel summation. Chebyshev’s bounds, including \(\theta(x)<x\log 4\). Mertens’s three theorems, and the identity \(M+H=\gamma\), using \(\Gamma'(1)=-\gamma\) from Volume 5, Exercise 5.7. The liminf and limsup of \(\theta(x)/x\) are named in the right order. Recomputed: the product through \(p\le 1000\) is \(0.0810\); \(R(10^3)=-1.298\), \(R(10^5)=-1.329\), \(R(10^7)=-1.332\); \(\sum_{p\le 10^7}1/p-\log\log(10^7)=0.2615\); \(\theta(3000)/3000=0.977\) and \(\psi(3000)/3000=1.000\); \(\psi(10)=\log 2520=7.832\); \(\log 10!=15.104\). The plate uses charcoal for \(\theta\) and blue for \(\psi\). Index numbers 1.1 through 1.6 match.

### Chapter 2

Wintner’s mean-value theorem. The hyperbola method for \(\tau\) and \(\tau_3\). The error term for \(\varphi\), \(\sigma\), and the squarefree count. Recomputed: the visible proportion in the \(24\times 24\) square is \(359/576\); \(\sum_{n\le 30}\tau(n)=111\); \(\sum_{n\le 30}\tau_3(n)=276\) against main terms \(248.18\); the mean of \(\tau(n)\) to \(10^6\) is \(13.97\) and the median is \(8\); the mean of \(n/\varphi(n)\) to \(10^6\) is \(1.9436\); \(2x^{-2}\sum_{n\le 10^7}\mathrm{rad}(n)=0.7044\). The secondary constant of \(2^{\omega}\) is the subject of V6-006; the numerical value is right. Index numbers 2.1 through 2.10 match.

### Chapter 3

Orthogonality, the conductor, and \(|\tau(\chi)|=\sqrt q\) for a primitive character. Non-vanishing of \(L(1,\chi)\), by the product for a complex character and by the series of positive coefficients for a real character. Dirichlet’s formula for \(L(1,\chi)\). Recomputed: \(L(1,\chi_{-3})=\pi/(3\sqrt 3)=0.6046\), \(L(1,\chi_{-4})=\pi/4\), \(L(1,\chi_5)=(2/\sqrt 5)\log\varphi=0.4304\); the partial sum of \(\chi_{-4}\) through \(12\) is \(0.7440\); \(\tau(\chi_5)=\sqrt 5\). The limit in the caption of `fig:lreal` is V6-007. Index numbers 3.1 through 3.11 match, and Section 3.5 is the non-vanishing section.

### Chapter 4

Dirichlet’s theorem, the progression form of Mertens’s theorem, and the non-vanishing on the line \(\operatorname{Re}s=1\). The race modulo \(4\) up to \(60000\) was recomputed and matches the text. The class sums modulo \(3\) at \(10^6\) are \(-1.187\) and \(-0.512\). Index numbers 4.1 through 4.5 match.

### Chapter 5

The zero-free line by the weight \(3+4\cos+\cos 2\theta\). Newman’s contour, the monotone lemma, the prime number theorem, the Möbius series, and the prime number theorem in progressions. Recomputed: \(\pi(1000)=168\), \(1000/\log 1000=144.76\), \(\mathrm{Li}(1000)=176.56\); \(\pi(3\cdot 10^6)=216816\) and \(\mathrm{Li}(3\cdot 10^6)=216970\); \(p_{10^6}=15485863\). The comparison \(\mathrm{Li}(x)\sim x/\log x\) is Exercise `ex:li`, and the text points at it. Index numbers 5.1 through 5.8 match, and the logarithmic integral is Exercise 5.1.

### Chapter 6

Complex Stirling, Jensen, Borel–Carathéodory, the local-zero lemma with the constants \(17\) and \(129\), Hadamard’s product, \(N(T)=\alpha(T)/\pi+1+S(T)\), and the zero-free region of width \(1/(14A'\log|t|)\). The factor \(14\) is \(1/(4/7-1/2)\). The identity \(3+4\cos\theta+\cos 2\theta=2(1+\cos\theta)^2\) was checked. The main term of \(N(100)\) is \(29.00\). The Vinogradov–Korobov shape and the proportions of zeros on the critical line are labelled as quotations. Index numbers 6.1 through 6.12 match.

### Chapter 7

Perron’s formula, the explicit formula, the de la Vallée Poussin error, the von Koch equivalences, and the bias identity \(\theta(x;4,3)-\theta(x;4,1)=\theta(\sqrt x)-\psi(x,\chi_{-4})+O(x^{1/3}\log x)\). The residues at \(s=1\), at the zeros, at \(s=0\), and at the trivial zeros were checked. The value of \(B\) is V6-008. The functional equation of \(L(s,\chi)\) is admitted in one remark and is not used by a theorem. Index numbers 7.1 through 7.11 match.

### Chapter 8

Legendre’s formula, Selberg’s sieve with \(|\lambda_d|\le 1\), Brun–Titchmarsh with the factor \(2\), Brun’s theorem on twins, and both large sieves. Recomputed: \(\pi_2(10^7)=58980\), \(C_2=0.66016\), and \(2C_2\int_2^{10^7}dt/\log^2 t=58754\). The Buchstab values for \(u>3\) and Maier’s theorem are labelled as Volume 15. Index numbers 8.1 through 8.11 match.

### Chapter 9

The Turán–Kubilius inequality and the Erdős–Kac theorem, by truncation at \(z=x^{1/\beta}\) and the moment comparison. The Gaussian characteristic function is Volume 4, Proposition 6.7, and the inversion formula is Theorem 6.8(b). Recomputed through \(10^7\): the mean of \(\omega\) is \(3.013\), the variance is \(1.103\), and \(\log\log(10^7)=2.780\). Index numbers 9.1 through 9.7 match.

### Chapter 10

Cramér’s model as a cylinder model, so that Hoeffding (Volume 4, Theorem 4.2) and both halves of Borel–Cantelli (Theorem 4.4) apply. The prime number theorem and the gap theorem for the model. The singular series, Gallagher’s theorem, and the remark on Maier. Recomputed: \(\sum_{n=3}^{30}1/\log n=11.48\); the eight coin probabilities from \(3\) to \(10\) sum to \(4.695\); there are \(117207\) primes \(p\le 10^7\) with \(p+6\) prime. The Chinese remainder theorem is Volume 2, Theorem 3.5. Index numbers 10.1 through 10.7 match.

### Chapter 11

The geometric bound, van der Corput’s inequality and difference theorem, Weyl’s equidistribution of polynomials, the square inequality, Kusmin–Landau, the second-derivative test, equidistribution of \(n^c\) for non-integral \(c\in(0,2)\), Pólya–Vinogradov, and Vinogradov’s bound \(p^{1/(2\sqrt e)+\varepsilon}\) with \(1/(2\sqrt e)=0.3032\). The pentagon vertices match \(e(k/5)\). Weyl’s criterion is Volume 5, Theorem 6.13, and \(n\alpha\) is Corollary 6.14. The continued-fraction bound is Volume 2, Theorem 9.2. The count \(117207\) of prime pairs at distance \(6\) matches the solution of `ex:admissible`. Index numbers 11.1 through 11.12 match.

### Chapter 12

\(S\) and \(T\) generate \(\mathrm{SL}_2(\Z)\). The fundamental domain was checked on both the vertical sides and the arc, including the corners \(\rho\) and \(\rho+1\). The Fourier expansion of \(G_k\) matches Euler’s formula for \(\zeta(2k)\) from Volume 5, Theorem 3.7, and the cotangent expansion on \(\C\setminus\Z\) is Corollary 9.35. The coefficients are \(240\), \(-504\), \(480\), \(-264\), and \(65520/691\). Siegel’s contour was re-derived: the residues, the identity \((\ast)\), and \((-i\tau)^{12}=\tau^{12}\). The passage to the limit is V6-009. The dimension formula, \(E_4^2=E_8\), the congruence modulo \(691\) (with \(65520\equiv -125\) and \(432000\equiv 125\)), Hecke’s operators, and Mordell’s recursion were checked, including \(\tau(4)=-1472\), \(\tau(8)=84480\), and \(\tau(12)=-370944\). The list \(1,-24,252,-1472,4830,-6048,-16744,84480,-113643,-115920,534612,-370944\) is Ramanujan’s. Index numbers 12.1 through 12.14 match. Deligne’s bound, Sato–Tate, and modularity are in a remark marked as a preview of Volume 13.

The closing problems that were re-derived and hold: the squarefree-pair density, the energy bound \((\pi^2/12)N^2/\log N\), the divisor champion \(n_{1/3}=2520\) with \(d(n)/n^{1/3}=3.527\), the irrationality of \(\log 2\) and of \(\zeta(2)\) and \(\zeta(3)\) by Beukers (with \(9\tau^5<1\) and \(27(\sqrt 2-1)^4<1\)), the integral \(\int_0^1\{1/x\}^2\,dx=\log(2\pi)-\gamma-1\), the sums of primes and of \(P^+\), the constant \(C=\sum k^{-1}\log(1+1/k)\) in \(\log\tau(n!)\), Menon’s identity by Burnside’s lemma (Volume 3, Theorem 3.6), Rényi’s densities with \(2^kd_k\to 1/(4C_2)\), the Euler factors of the two-square series and \(K=C/\sqrt\pi\), Ramanujan’s differential equations, Schur’s determination of the sign of the Gauss sum, the \(3\)-\(4\)-\(1\) non-vanishing for Hecke’s \(L_k\), and the covering \(11\,184\,810=2\cdot 3\cdot 5\cdot 7\cdot 13\cdot 17\cdot 241\). Lindeberg’s theorem is Volume 4, Theorem 6.10. The non-vanishing \(L(1+it,\chi)\ne 0\) used for the angles of the Gaussian primes is Theorem `thm:line`.

## Not checked

These were not recomputed. Chapter 6 already says the zero ordinates are taken from tables.

- The partial sums of the explicit formula at \(x=10\), the Schoenfeld ratios on \([73.2,10^7]\), and the ordinates of \(L(s,\chi_{-4})\).
- The census of \(n(p)\) to \(10^8\), the record primitive roots to \(10^6\), the maximal character sum modulo \(1\,000\,003\), and the Sato–Tate histogram for \(p\le 50\,000\).
- \(\Psi(10^{12},1000)\), \(\sum_{p\le 10^7}p\), the count of sums of two squares to \(10^8\), the count of primitive roots \(2\) below \(10^7\), \(R_{10000}\), and the Romanoff proportions.
- The semiprime ratio and \(\mathrm{lcm}(1,\ldots,n)^{1/n}\) at \(n=10^8\).
- Portrait files against `photos/CREDITS.md` beyond the agreement of the captions, and the wording of the Jacobi and Dirichlet letters against the primary texts.
