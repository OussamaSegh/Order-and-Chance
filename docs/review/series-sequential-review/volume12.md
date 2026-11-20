# Volume 12 — Random Motion

**Score: 9/10.**

Kolmogorov–Chentsov, the Paley–Wiener and Karhunen–Loève series, Lévy’s modulus, the joint reflection principle, quadratic variation, Itô’s formula, Lévy’s characterisation, Dambis–Dubins–Schwarz, Tanaka’s formula, Girsanov for bounded drift, the Black–Scholes PDE, the Bessel hitting threshold, Dyson’s non-collision from a simple spectrum, Lévy–Itô, Wigner’s semicircle, the GOE edge bound \(e^{-nt^2/4}\), the number variance of the circular ensemble, the matrix-tree theorem, and the upper bound \(\log|Z_n|\le(1+\varepsilon)\log n\) were checked step by step. The numbers that were recomputed match the page, including Catalan moments, \(\mathbb E|B_t|=\sqrt{2t/\pi}\), the Cameron–Martin factor \((\cosh\lambda t)^{-1/2}\), the call formula, Kesten’s \(\sqrt{2k-1}/k\), \(\sqrt{\log 1000}/\pi\approx0.84\), the free-group return \(p_{100}\approx2.45\times10^{-9}\), \(\operatorname{Var}\log|Z_{50}|\approx2.74\), and the half-moment constant \(5.39\ldots<5.4\). The score is 9 because the theorems hold and the four slips are local. No numbered statement was found false.

**Counts.** 0 critical, 0 major, 4 minor. No prerequisite issue.

**How this was read.** Book order in `volume12-random-motion/main.tex`: preface, Gaussian Processes and the Birth of Brownian Motion, The Fine Structure of a Brownian Path, Continuous Martingales, The Itô Integral, Brownian Motion and Analysis, Stochastic Differential Equations, Markov Processes and Lévy Processes, Random Walks on Networks and Groups, Random Matrices I: The Semicircle, Random Matrices II: The Unitary Group, Log-Correlated Fields and the Largest Values (which inputs `brw-halfmoment.tex`), the spectral appendix, then About the Cover. The blurb and `kdp.md` were read with the preface. Every exercise was read, including its hint and its solution. There are 143 exercises. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. Proofs are dense, in the same register as Volumes 9–11. Quoted results (Novikov, Tracy–Widom, Füredi–Komlós, Bai–Yin, Mehta’s spacing density, Knight, the reverse Burkholder–Davis–Gundy inequality, non-integer squared Bessel processes) are marked in the chapter where they occur. The one admitted theorem is the second-order maximum of \(\log|Z_n|\), as the preface says. Montgomery’s formula is labelled as proved in Volume 14 and used as a premise nowhere.

## Issues

Paths are relative to `volume12-random-motion/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V12-001 | `chapters/ch02-paths.tex:170` and `:183` | reference | minor | “by Tonelli: \(\mathbb E\lambda(\mathcal Z)=\int_0^\infty P(B_t=0)\,dt=0\) (Volume 4, Exercise 12.3).” Later: “A non-empty closed set without isolated points is uncountable (Volume 4, Exercise 12.3, where this consequence is proved).” | Volume 4, Exercise 12.3 (`ex:zeros`) proves that the zero set on \([0,1]\) has outer length zero, and its solution says the argument avoids Tonelli. The integral in Volume 12 is a correct application of Tonelli from Volume 7. The same exercise proves that this zero set is uncountable by injecting binary sequences into it; it does not state the abstract perfect-set theorem. Cite Tonelli for the integral, and cite the exercise for the outer-length proof and for the uncountability of \(\mathcal Z\). |
| V12-002 | `chapters/ch01-gaussian.tex:135–136`, proof of `thm:kolmcont` | math | minor | “For \(n\ge m\) let \(s_n=2^{-n}\lfloor 2^ns\rfloor\). Each coordinate of \(2^ns_n\) and \(2^nt_n\) differs by at most \(1\), because the coordinates of \(2^ns\) and \(2^nt\) differ by at most \(1\); so \(s_m,t_m\) are neighbours.” | If \(|t-s|\le2^{-m}\) and \(n>m\), then \(|2^n(t-s)|\) can exceed \(1\). The floors at level \(m\) do differ by at most \(1\), and that is the only comparison the chaining uses. Restrict the sentence to \(n=m\). |
| V12-003 | `chapters/ch06-sde.tex:614–615`, solution of `ex:nonunique` | exercise | minor | “it is the drift \(3x^{1/3}\) that is not Lipschitz at \(0\), exactly as in the deterministic example \(x'=3x^{2/3}\), which has the solutions \(0\) and \(t^3\).” | The equation \(x'=3x^{2/3}\) is the classical one with those two solutions, and \(2/3\) is the exponent of the diffusion coefficient. The drift that fails the Lipschitz test in the stochastic equation is \(3x^{1/3}\). Name that ordinary equation, or say that the diffusion coefficient is the classical non-Lipschitz example. The conclusion, that Yamada’s drift hypothesis is the one that fails, is right. |
| V12-004 | `chapters/ch05-analysis.tex:539`, solution of `ex:v12girsanovL2` | exercise | minor | “The first is a true exponential martingale with expectation \(1\) by the bounded-drift Girsanov argument applied to \(2\theta\).” | Proposition `prop:expmartgen` gives a positive local martingale, hence a supermartingale of mean at most \(1\). That is enough for \(\mathbb EZ_T^2\le e^{C^2T}\). The martingale property of the exponential for \(2\theta\) is what the \(L^2\) bound is being used to reach, so the solution should not call it already proved. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map is the eleven chapters and the appendix in `main.tex` order. The next volume is the arithmetic that begins when unique factorisation fails. The stated prerequisites are Volumes 4, 7, 8, 9 and 11. About the Cover is one planar path stopped on leaving the unit circle, and it names Wiener’s 1923 construction. The jacket’s “one marked exception” is the second-order maximum admitted as `thm:cuemax`. No notebook is promised. Selberg’s law for \(\log|\zeta|\) is deferred to Volume 15, which is where the series plan puts it.

### Chapter 1

Kolmogorov’s extension to an arbitrary index, existence of Gaussian processes, the Kolmogorov–Chentsov chaining, Brownian Hölder regularity of every order below \(1/2\), both Fourier bases, Lévy’s maximal inequality, the Gaussian-maximum bound, uniform convergence of the Wiener and Karhunen–Loève series, the Wiener integral, and the Mandelbrot–Van Ness representation of fractional Brownian motion were checked. The neighbour count \((2^n+1)^d3^d\) and the Hölder constant \(c_\gamma=1+2/(2^\gamma-1)\) match the union bound. The trace of \(\min(s,t)\) is \(1/2\), and the first Karhunen–Loève eigenvalue \(4/\pi^2\) is \(8/\pi^2\approx81\%\) of that trace. \(\operatorname{Cov}(X_1,X_2-X_1)=\frac12(2^{2H}-2)\). All twelve exercises were read. \(\sum n^{-2}\pi^{-2}=1/6\), \(\int_0^1(1-t)^2\,dt=1/3\), and \(\mathbb E\int_0^1(B_t-tB_1)^2\,dt=1/6\). The false quantifier in V12-002 is not used.

### Chapter 2

Blumenthal’s zero–one law, oscillation at zero, the tail law and \(\sup B=+\infty\), Lévy’s modulus with constant \(\sqrt2\), the joint density of \((M_t,B_t)\), the zero set, and Taylor’s dimension bound were checked. The hit probability is \(\frac4\pi\sqrt{h/a}\). The record set has dimension \(1/2\); the matching lower bound for the zero set is deferred to Chapter 4 and then proved there. All eleven exercises were read. The no-zero probability is \(\frac2\pi\arcsin\sqrt{a/b}\). The bridge maximum has distribution function \(1-e^{-2a^2}\). The hitting density is \(a(2\pi)^{-1/2}t^{-3/2}e^{-a^2/(2t)}\). The two citations in V12-001 are the slips.

### Chapter 3

The Brownian filtration, continuous-time Doob and optional stopping, \(L^2\) convergence, quadratic variation for a bounded martingale and then by localisation, the bracket, and the exponential martingale were checked. The fourth-moment bound in `lem:fourth` is \(48C^4\). \(\mathbb Ee^{-\mu\tau_a}=e^{-a\sqrt{2\mu}}\). The maximum of \(B_t-\mu t\) is exponential with mean \(1/(2\mu)\). Wald’s identities hold when \(\mathbb E\tau<\infty\). The median of \(e^{B_t-t/2}\) at \(t=8\) is \(e^{-4}\approx0.018\). All twelve exercises were read. The exit from \((-a,b)\) has mean \(ab\) and probability \(a/(a+b)\). \(\mathbb E\tau^2=\frac53 a^4\) for the two-sided exit of \((-a,a)\). \(\mathbb E(B_t^2-t)^2=2t^2\) and \(\mathbb E\mathcal E_t^2=e^{\lambda^2 t}\).

### Chapter 4

The Kunita–Watanabe inequality, the Itô isometry, Riemann sums, Itô’s formula, Lévy’s characterisation, the exponential tail \(e^{-a^2/(2c)}\), Dambis–Dubins–Schwarz, Burkholder’s constant \(C_p\), Tanaka’s formula, Skorokhod’s lemma, and Lévy’s identification of \((|B|,L)\) with \((M-B,M)\) were checked. The zero set then has Hausdorff dimension \(1/2\). All twelve exercises were read. \(\operatorname{Var}\int_0^t s\,dB_s=t^3/3\), \(\operatorname{Var}\int_0^t B\,dB=t^2/2\), and \(\langle\int_0^t 2s\,dB\rangle=4t^3/3\). \(\mathbb EL_t=\sqrt{2t/\pi}\).

### Chapter 5

The heat equation, Feynman–Kac, the Cameron–Martin identity \(b=\lambda\tanh\lambda t\) and \(a=(\cosh\lambda t)^{-1/2}\), Girsanov for bounded drift, the mean-value property, Kakutani’s solution of the Dirichlet problem, the cone condition, the annulus exit probabilities, recurrence in the plane and transience in dimension \(d\ge3\), and Lévy’s conformal invariance were checked. \(P_x(T_r<\infty)=(r/|x|)^{d-2}\). All eleven exercises were read. \(\mathbb E_x\tau=(R^2-|x|^2)/d\). The drifted maximum formula matches the reflection computation, and its limit as \(T\to\infty\) for \(\mu<0\) is \(e^{2\mu a}\). The strip rate is \(\pi^2/(8a^2)\). V12-004 is the slip in the Girsanov exercise.

### Chapter 6

Picard’s iteration with \(L=2(T+4)K^2\), the Markov property, Yamada–Watanabe, Ornstein–Uhlenbeck, geometric Brownian motion, the Black–Scholes PDE and the replication identity, the squared Bessel scale function, and Dyson’s equation from a simple spectrum were checked, including the trace computation that produces the drift \(1/(\lambda_i-\lambda_k)\) and McKean’s bound \(n^2-\frac12 S\). The entrance from a repeated eigenvalue is marked as not proved. All thirteen exercises were read. The gap of a \(2\times2\) Hermitian Brownian motion, divided by \(\sqrt2\), is a Bessel process of dimension \(3\). Euler–Maruyama has strong order \(1/2\), and the geometric-Brownian example has mean-square error at least a constant times \(h\). The stationary law in the Ornstein–Uhlenbeck figure is \(N(0,1/2)\), and \(\pm2/\sqrt2\) is two standard deviations. V12-003 is the slip.

### Chapter 7

Dynkin’s formula, the martingale problem for \(\frac12\Delta\), Poisson random measures, the Lévy generator, and both directions of Lévy–Itô were checked, including the recipe that reads jumps from dyadic increments. The \(\frac12\)-stable subordinator has Laplace exponent \(\sqrt{2\lambda}\) and Lévy density \((2\pi)^{-1/2}x^{-3/2}\). The mean number of excursions longer than \(x\) before height \(a\) is \(a\sqrt{2/(\pi x)}\). The inverse local time has the same law. All twelve exercises were read. The Gamma subordinator has Laplace exponent \(\log(1+\lambda)\). A symmetric stable process has a finite mean exactly for \(\alpha>1\). Subordination of Brownian motion by \(T_a\) is Cauchy.

### Chapter 8

The electrical dictionary, Thomson, Rayleigh, the commute identity, recurrence by infinite resistance, Lyons, Nash–Williams, Pólya on \(\mathbb Z^2\) and \(\mathbb Z^d\), and Kesten’s spectral radius \(\sqrt{2k-1}/k\) were checked. Volume 8, Theorem 7.5 is the Kesten–McKay law, and Volume 8, Theorem 6.4 is Alon–Boppana, as the chapter says. All twelve exercises were read. The hypercube resistance satisfies \(nR(0\leftrightarrow\mathbf 1)\to2\), and the commute time is asymptotic to \(2^{n+1}\). On \(F_2\), \(p_{100}\approx2.45\times10^{-9}\), against \((\sqrt3/2)^{100}\approx5.7\times10^{-7}\) and \(p_{100}(\mathbb Z^2)\approx6\times10^{-3}\).

### Chapter 9

The Catalan moments of the semicircle, the walk count, Wigner’s theorem in probability and almost surely, the Stieltjes identification, Marchenko–Pastur, Sudakov–Fernique, the GOE bound \(\mathbb E\lambda_{\max}\le2\) and \(P(\lambda_{\max}\ge2+t)\le e^{-nt^2/4}\), and the spiked outlier \(\theta+1/\theta\) were checked. Tracy–Widom, Füredi–Komlós and Bai–Yin are marked as not proved. All fourteen exercises were read. The fourth-moment count is \(2n^3+5n^2+5n\), so \(\mathbb Em_n(4)\to2\). The semicircle’s second moment is \(1\) and its sixth moment is \(C_3=5\). The file of the eigenvalue histogram records extremes \(-1.9893\) and \(1.9784\), both within \(0.05\) of \(\pm2\).

### Chapter 10

The Bernoulli representation of an eigenvalue count, the number-variance formula, the Costin–Lebowitz–Soshnikov CLT, the sine kernel, the gap expansion, the Keating–Snaith moments, and the central limit theorem for \(\log|\det(I-U)|\) were checked against the Volume 9 inputs named in the reminder (Haar uniqueness 8.3, Heine 8.13, correlations 8.15, Dyson 8.16) and against Hadamard as Volume 8, Theorem E.5. For an arc that expects \(1000\) eigenvalues, \(\sqrt{\log 1000}/\pi\approx0.84\). All twelve exercises were read. \(\mathbb E|\det(I-U)|^2=n+1\). \(\operatorname{Var}\log|Z_{50}|\approx2.745\), printed \(2.74\). The ratio of characteristic polynomials tends to \(e^{i\pi x}\sin(\pi x)/(\pi x)\).

### Chapter 11

The branching-random-walk speed, the log-correlation of \(\log|Z_n|\), the \(L^2\) phase of Gaussian multiplicative chaos, Bernstein’s inequality with constant \(e\), and the upper bound on the maximum were checked. The admitted second-order theorem is stated with its sources and is not used to prove an earlier result. The half-moment section gives \(\mathbb EW_n^{1/2}\le C n^{-1/4}\) with \(C=\sum_L\sqrt{2L+2}\,e^{-L/2}=5.39\ldots<5.4\), from the ballot bound \((2L+2)n^{-1/2}\) and the tail \(e^{-(L+1)}\). All thirteen exercises were read. For \(n=1000\), \(\log n-\frac34\log\log n\approx5.46\), as the caption says. The free-energy threshold \(c^*=\sqrt{2\log2}\) and the second-moment bound for \(\beta^2<\log2\) match the calculation.

### Appendix

The Laplacian identity \(x^{\mathsf T}Lx=\sum_{uv}(x_u-x_v)^2\), Rayleigh’s quotient, the matrix-tree theorem, Kirchhoff’s product formula, Cayley’s \(n^{n-2}\), the hypercube count \(2^{2^n-n-1}\prod_j j^{\binom nj}\), and the BEST theorem were checked. \(Q_3\) has \(384\) spanning trees and the Petersen graph has \(2000\). \(K_4\) has \(16\) spanning trees, twelve paths and four stars. All nine exercises were read. \(\tau(K_{m,n})=m^{n-1}n^{m-1}\), \(\tau(P_3)=1\), \(\tau(K_3)=3\), and \(\tau(C_n)=n\). The de Bruijn count is \((q!)^{q^{n-1}}/q^n\).

## Not checked

The \(1000\times1000\) Gaussian matrix behind the semicircle histogram was not rebuilt; the extremes recorded in the figure file were compared with the caption. The sample maximum \(5.62\) of \(\log|Z_{1000}|\) and the printed range \(0.31\) to \(0.44\) for the mean excess were not recomputed. Other figure seeds were checked through the stated parameters and the captions, not by regenerating the pictures. The quoted theorems named above were not proved again. The book was not typeset in this pass.
