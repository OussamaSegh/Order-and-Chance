# Volume 5 independent re-read, 13 November 2026

Independent scored reading of *Order and Chance*, Volume 5, *Calculation: From Formula to Insight*, on `main` at `f10e4c99`. The built files are the GitHub release `books` republished from that commit: reading PDF (356 pages, 7 × 10 in), print PDF (355 pages, 7.125 × 10.25 in), and EPUB (26.1 MB).

The reader in view is a motivated high-school student who will work. Scores are 0–10. A 10 would be a chapter I could not fault against a book at the level of Courant–Robbins, Spivak, Niven–Zuckerman, Artin, or Tao’s *Analysis I*. I did not give one.

Printed folios below are the arabic folios of the reading PDF (the print PDF carries the same folios; it has no cover). File lines are the source on `f10e4c99`.

The scores and the issue log were written before any earlier Volume 5 review, fix PR, or file under `review/` was opened.

## How the book is built

`volume5-calculation/main.tex` prints thirteen chapters in three parts.

| Part | Chapters | Reading folio of the opener |
| --- | --- | --- |
| I. Series and Products | 1 Finite calculus, 2 Generating functions, 3 Series and products | 2, 21, 63 |
| II. Integrals and Transforms | 4 Integration, 5 Gamma and Beta, 6 Fourier series, 7 DFT and FFT, 8 Fourier transform, 9 Complex analysis | 79, 101, 121, 143, 164, 181 |
| III. The Zeta Function | 10 Zeta, 11 Asymptotics, 12 Hardy–Ramanujan, 13 AGM | 215, 235, 261, 279 |

Index folio 338, sources 344, about the cover 346. Waring’s problem is not a chapter. The BBP series is a section of Chapter 4 (`bbp-borwein.tex` is input from `ch04-integrals.tex`). The eta transformation is proved in Chapter 12 from the pentagonal theorem, Poisson summation, and the identity theorem, and the proof cites nothing after Volume 5.

## Scorecard

Rows are chapters. Columns: (a) correctness, (b) rigor, (c) prerequisites, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography as rendered.

| Ch | a | b | c | d | e | f | g | h | i | j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 Finite calculus | 9 | 8 | 9 | 9 | 9 | 8 | 8 | 9 | 9 | 9 |
| 2 Generating functions | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 3 Series and products | 9 | 8 | 9 | 9 | 9 | 8 | 8 | 8 | 9 | 9 |
| 4 Integration | 9 | 8 | 9 | 8 | 9 | 8 | 8 | 9 | 8 | 8 |
| 5 Gamma and Beta | 8 | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 8 | 8 |
| 6 Fourier series | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 7 DFT and the FFT | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 8 Fourier transform | 8 | 8 | 9 | 8 | 8 | 8 | 8 | 8 | 9 | 8 |
| 9 Complex analysis | 8 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 |
| 10 Zeta | 9 | 8 | 9 | 9 | 9 | 8 | 8 | 9 | 9 | 8 |
| 11 Asymptotics | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 12 Hardy–Ramanujan | 8 | 8 | 9 | 7 | 8 | 8 | 8 | 8 | 8 | 8 |
| 13 AGM | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |

### Why these chapter scores

**Chapter 1 (folios 2–20).** Bernoulli numbers use \(B_1=-\frac12\), and the values through \(B_{12}=-\frac{691}{2730}\) match the recurrence. Faulhaber’s formula gives \(\sum_{k<1000}k^5=166\,167\,083\,333\,250\,000\), and the tenth powers of \(1\) through \(1000\) are the 32-digit number on the opener. The formal-power-series language is introduced before Chapter 2 defines it at length; the local rules are enough for the proofs, which is why rigor is 8 rather than 9.

**Chapter 2 (folios 21–62).** Franklin’s involution for the pentagonal theorem is written with the exceptional cases separated, and the signs match the product \(1-x-x^2+x^5+x^7-\cdots\). Twenty-eight exercises follow. I recomputed Dobinski’s exercise only as a citation target, not every solution, so the exercise score stays at 7.

**Chapter 3 (folios 63–78).** \(\zeta(2k)=(-1)^{k+1}B_{2k}(2\pi)^{2k}/(2(2k)!)\) gives \(\pi^2/6\), \(\pi^4/90\), \(\pi^6/945\), \(\pi^8/9450\). Niven’s argument that \(\pi^2\) is irrational closes: the integral is a positive integer and is eventually smaller than 1. The Viète polygon areas 2, \(2\sqrt2\), and about 3.06 are right. The \(\zeta(5)\) sentence is the reason this chapter is not a 9 on voice; see V5-5.

**Chapter 4 (folios 79–100).** The BBP identity \(\pi=4S_1-2S_4-S_5-S_6\) survives the substitutions and the partial fractions. At \(d=999999\) the hexadecimal digits are `26C65E52`, and at \(d=10^6\) they are `6C65E52`, as the text says. The Borwein fraction equals the deficit formula exactly, and the deficit is \(2.31\times10^{-11}\). Dominated convergence is stated for continuous integrands on intervals, which is what the later chapters use.

**Chapter 5 (folios 101–120).** The ball volumes \(V_n=\pi^{n/2}/\Gamma(n/2+1)\), \(V_5=8\pi^2/15\approx5.264\), and \(V_{20}\approx0.026\) are right, and the surface-area solution correctly finds the maximum at the sphere in \(\mathbb R^7\). The lemniscate evaluation \(\int_0^1(1-r^4)^{-1/2}\,dr=\Gamma(1/4)^2/(4\sqrt{2\pi})\) matches the AGM formula in Chapter 13. I did not re-line the whole Bohr–Mollerup proof.

**Chapter 6 (folios 121–142).** Gibbs’ constant \((2/\pi)\mathrm{Si}(\pi)=1.17897\ldots\), an overshoot of about 0.179 on a jump of height 2, is the classical value. Weyl’s criterion is Theorem 6.13 and the sequence \((n\alpha)\) is Corollary 6.14; both are what Volume 6 quotes. Siegel’s exercise admits the volume of a convex body and names Volume 7, Theorem 7.11, which is Lebesgue measure.

**Chapter 7 (folios 143–163).** The FFT recurrence \(M(n)=2M(n/2)+n/2\) is \(\frac n2\log_2 n\) multiplications and \(n\log_2 n\) additions, and the text says “at most.” Figure 7.2 puts the spectral lines at bins 5 and 12, which are the two tones in the caption. I did not recompute a length-8 transform by hand.

**Chapter 8 (folios 164–180).** The transform is \(\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,dx\), with inversion \(f(x)=\int\hat f(\xi)e^{2\pi ix\xi}\,d\xi\) and \(\widehat{\hat f}(x)=f(-x)\). The Gaussian \(e^{-\pi x^2}\) is its own transform. Poisson summation and \(\vartheta(1/t)=\sqrt t\,\vartheta(t)\) are Theorem 8.9 and Corollary 8.10. The Gauss-sum evaluation \(G(n)=\frac{1+i}{2}(1+i^{-n})\sqrt n\) is the classical one, and the Fresnel value \(\int_0^\infty u^{-1/2}e^{iu}\,du=\sqrt\pi\,e^{i\pi/4}\) is right. The letter \(\vartheta\) is reserved for Jacobi and \(\theta\) for Chebyshev, which is the notation the later volumes need.

**Chapter 9 (folios 181–214).** Cauchy’s theorem on a star-shaped set (Theorem 9.9) really does include \(F'=f\), which is what Volume 8 cites. The residue calculation \(\int_{-\infty}^\infty(1+x^4)^{-1}\,dx=\pi/\sqrt2\) is correct (\(\pi\sqrt2/2\) is the same number). The cotangent expansion on \(\mathbb C\) (Corollary 9.35) is the formula Volume 6 differentiates. The chapter is a full first course. A reader at the stated level will find the estimates dense, which is the clarity score of 7. I did not re-check every contour estimate.

**Chapter 10 (folios 215–234).** The completed function is \(\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), the pole has residue 1, and \(\xi(1-s)=\xi(s)\). The asymmetric form is the standard \(2(2\pi)^{-s}\cos(\pi s/2)\Gamma(s)\zeta(s)\). From it, \(\zeta(1-2k)=-B_{2k}/(2k)\), so \(\zeta(-1)=-\frac1{12}\), \(\zeta(-3)=\frac1{120}\), \(\zeta(-5)=-\frac1{252}\), \(\zeta(-7)=\frac1{240}\), and \(\zeta(0)=-\frac12\). The ten ordinates through \(49.77\) match the zeros to two decimals. The exponential smoothing \(\sum n e^{-n/N}=N^2-\frac1{12}+O(N^{-2})\) is right, and the claim about every smooth cutoff is explicitly not proved. The Gauss–Kuzmin constant in the journey exercise equals \(2\zeta(3)-\frac32\).

**Chapter 11 (folios 235–260).** Euler–Maclaurin’s first corrections are \(\frac12(f(b)-f(a))\), \(\frac1{12}(f'(b)-f'(a))\), \(-\frac1{720}(f'''(b)-f'''(a))\). The harmonic expansion through \(n^{-6}\) at \(n=10\) errs by \(4.09\times10^{-11}\) against \(H_{10}=7381/2520\); the text says \(4.1\times10^{-11}\), and the next term is \(4.2\times10^{-11}\). Stirling’s coefficients \(\frac1{12x}-\frac1{360x^3}+\frac1{1260x^5}-\frac1{1680x^7}\) are right, and the figure’s best errors \(10^{-3.5}\), \(10^{-6.4}\), \(10^{-12}\) are about half the smallest term at \(x=1,2,4\). A complex saddle for central binomial coefficients is present, as the master plan asked.

**Chapter 12 (folios 261–278).** The eta proof on the imaginary axis is a Gaussian Fourier transform, a shift, and a modulation; the cosine table for odd residues mod 12 produces the factor \(1/\sqrt t\), and the identity theorem spreads it to the half-plane. The branch \(\sqrt{-i\tau}\) is the principal root with positive real part. The table \(p(10)=42\), \(p(100)=190\,569\,292\), \(p(200)=3\,972\,999\,029\,388\), \(p(1000)=2.406\times10^{31}\), and the ratios \(0.873\), \(0.956\), \(0.969\), \(0.986\) match the pentagonal recurrence and \(\mathrm{HR}(n)\). \(\log P(0.99)=160.45\). Rademacher’s series is headed “quoted” and is not used later. The \(O(n^{-1/4})\) error is weaker than the true \(O(n^{-1/2})\), and the text says where the proof lost the factor. The five-stage write-up is correct as far as I checked and hard to read, which is the clarity score.

**Chapter 13 (folios 279–337).** \(\varpi=2.62205755429211981\ldots\) and \(M(1,\sqrt2)=\pi/\varpi=1.19814023473559220744\ldots\) to the digits shown. \(\Gamma(1/4)=(2\pi)^{3/4}/\sqrt{M(1,\sqrt2)}\) matches Euler’s integral. Brent–Salamin’s \(\pi_1=3.1405\ldots\), and the errors of \(\pi_2\) through \(\pi_8\) have decimal exponents \(-8.1\), \(-18.7\), \(-40.3\), \(-83.6\), \(-170.6\), \(-345.0\), \(-694.0\), inside the stated bounds. The chapter’s own exercises are five. Forty-one problems of the whole volume then follow, labelled as such. That set is why the exercise score is 7: it is not a path through the AGM, and I only sampled it (the prime-zeta values \(0.452247420041\) and \(0.452247414181\), difference \(5.86\times10^{-9}\), are right).

## Whole book

| Item | Score | Why |
| --- | --- | --- |
| Structure and arc | 9 | Three parts, from finite sums to the functional equation, a saddle, the partition asymptotic, and the AGM. The last chapter’s problem dump is labelled and does not break the arc. |
| Continuity with Volumes 1–4 | 8 | The numbered pointers I checked (Euler’s constant in Volume 1, Chapter 3; complex numbers in Chapter 5; calculus and Stirling in Chapter 8; Cauchy–Schwarz in Chapter 9; \(\sum_{d\mid n}\varphi(d)=n\) in Volume 2, Chapter 3; Gauss sums in Exercise 6.7; continued fractions in Chapter 9; Hoeffding in Volume 4, Chapter 4; random walks in Chapter 8) say what this volume uses. One pointer names the wrong chapter for independence (V5-6). |
| Preparation for later volumes | 8 | Volume 6’s reminders of the functional equation, the residue theorem, Weyl, Parseval, Stirling, the harmonic expansion, and Theorem 12.4 for \(\eta\) match the statements. One printed reminder in Volume 14 names the wrong corollary for the theta law (V5-1). Two further mismatches sit in Volume 15 files that `main.tex` does not print (V5-2, V5-3). |
| Title and subtitle | 9 | The subtitle is a motion from a formula to what it means, and each chapter I read does that: a method for power sums, a recurrence as a rational function, a function as a sum over its poles, a factorial picked out by log-convexity, a sign fixed by an integral, a real integral as a residue, \(-1/12\) as a constant term, an asymptotic with a remainder, partitions governed by \(\tau\mapsto -1/\tau\), and digits of \(\pi\) doubled by an elliptic integral. |
| Front matter, index, bibliography | 8 | The preface describes the thirteen chapters accurately. Its list of admitted facts is a little short (V5-4, V5-7). The sources name real books and papers; the 2026 \(\zeta(5)\) sentence needs a caveat (V5-5). The index entries I checked (Theorems 4.11, 6.11, 10.10, Corollary 8.10) point at the right folios. I did not check every index line. The blurb states what the volume proves and marks Rademacher as quoted. |
| Print PDF | 8 | Every page is 513 × 738 pt. A scan found no text or drawing outside the 7 × 10 trim, with 0.125 in bleed on the top, bottom, and outside edge only. Part openers are full charcoal. Sample chapter openers, the Stirling figure, and Figure 7.2 are clean. I did not turn all 355 pages by eye. |
| EPUB | 8 | 26.1 MB, no SVG plates, 37 plates whose PNG headers are about 1800 pixels wide, `width:100%` on plates, and 14,367 inline formulas with width and `vertical-align` in em. I did not read it on a Paperwhite. |

## Overall

**8.** I would recommend the volume to its reader as it stands. The flagship theorems I recomputed — Bernoulli and Faulhaber, the pentagonal signs, \(\zeta(2k)\), Niven, BBP, the Borwein deficit, the ball, Gibbs, the FFT count, Fourier inversion and the Gauss sum, the functional equation and the negative zeta values, Stirling’s series, the eta transformation, the Hardy–Ramanujan table, and Brent–Salamin — are right, and the proofs I followed state their hypotheses. It is not flawless: Chapters 9 and 12 are hard for the stated reader, a large exercise set was only sampled, and one printed later volume cites the theta transformation under the wrong number.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V5-1 | `volume14-primes/chapters/ch14-critical.tex:19` (Volume 14, opening reminder of the critical-line chapter). The statement it wants is Volume 5, Corollary 8.10, reading folio 169. | Cross-volume citation | major | The reminder says the theta law \(\theta(1/u)=\sqrt u\,\theta(u)\) is “Volume 5, Theorem 8.9 and Corollary 10.10.” Theorem 8.9 is Poisson summation. Number 10.10 is Theorem 10.10, \(\zeta(1-2k)=-B_{2k}/(2k)\), folio 221, not a corollary and not theta. The theta transformation is Corollary 8.10. The formula in the reminder is the right one; the number is not. | Cite Corollary 8.10. |
| V5-2 | `volume15-order-and-chance/chapters/conjectures-ch01-born.tex:229`. Not reached from Volume 15 `main.tex`. | Cross-volume citation | minor | The Dirichlet integral \(\int_0^\infty(\sin u)/u\,du=\pi/2\) is cited as Volume 5, Theorem 6.11. Theorem 6.11 is Parseval (folio 126). The integral is Theorem 4.11 (folio 84). Printed uses of 6.11 in Volumes 11 and 12 correctly say Parseval. | If the file is ever printed, cite Theorem 4.11. |
| V5-3 | `volume15-order-and-chance/chapters/ra-largemoduli.tex:24`. Not reached from Volume 15 `main.tex`. | Cross-volume citation | minor | Theorem 8.6 is quoted as \(f(u)=\int F(t)e^{-itu}\,dt\) with \(F(t)=\frac1{2\pi}\int f(u)e^{itu}\,du\). Volume 5’s Theorem 8.6 is the unitary convention: \(\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,dx\) and \(f(x)=\int\hat f(\xi)e^{2\pi ix\xi}\,d\xi\), so \(\widehat{\hat f}(x)=f(-x)\). Volume 13’s Tate reminder states that convention and cites 8.6 correctly. | Quote the \(2\pi\) convention, or name the change of normalization. |
| V5-4 | `volume5-calculation/chapters/preface.tex:25–28` | Admitted results | minor | The preface says the only unproved appeals are Tonelli in two exercises and the volume of a convex body in one exercise of Chapter 6, and that no theorem depends on them. Those three are real and correctly labelled (Volume 7, Theorems 9.5 and 7.11). A closing problem also admits Mertens’s third theorem (`ch12-agm.tex:760`) and a solution quotes the prime number theorem for a comparison (`ch12-agm.tex:2011`). Neither is a premise of a theorem. | Add those two appeals to the preface’s list, still as exercises. |
| V5-5 | `volume5-calculation/chapters/ch03-series.tex:229`, reading folio 68 | Attribution | minor | “Fauzan gave an argument in 2026 that \(\zeta(5)\) is irrational, and Hyman formalised it in the Archive of Formal Proofs (*Zeta_5_Irrational*, 26 October 2026).” The AFP entry of that date, by Alex Raymond Hyman, does formalise Aabir Fauzan’s Zenodo preprint. The verb is “gave an argument,” not “proved.” The sentence stands next to Apéry’s theorem and does not say that the source is an unrefereed preprint, or that the formalisation discharges numeric inequalities by approximation. | Call it a 2026 preprint, name the formalisation’s numeric oracle, and keep it out of the list of theorems the reader may quote. |
| V5-6 | `volume5-calculation/chapters/ch06-fourier.tex:367` | Prerequisite pointer | minor | “By independence (Volume 4, Chapter 8).” Independence of random variables is Volume 4, Chapter 2. The product of characteristic functions is used in Volume 4, Chapter 6, and the return-probability integral is in Chapter 8, *Random Walks*. The formula this example needs is in Chapter 8; the name “independence” points at the wrong chapter. | Cite Chapter 2 for independence and Chapter 8 for the return formula. |
| V5-7 | `volume5-calculation/chapters/ch05-gamma.tex:428–431`, exercise `pb:ncycles` | Admitted results | minor | The exercise says to take as known that the exterior powers of the reflection representation are irreducible and pairwise non-isomorphic, citing Fulton and Harris, Proposition 3.12. That is a quoted fact outside the series, and the preface’s list does not mention it. | Mark the sentence “quoted” and add it to the preface’s list of appeals that no theorem uses. |
| V5-8 | `volume11-randomness/chapters/ch09-martingales.tex:531`, solution of `ex:polyabeta` | Cross-volume citation | minor | The solution says Volume 5, Section 7.4, gives \(B(x,y)\) in general. Section 7.4 is “Exact transforms modulo a prime.” The Beta integral is Section 5.4, Theorem 5.11. The factorial form used in the same sentence is right. | Cite Section 5.4 or Theorem 5.11. |
| V5-9 | `volume5-calculation/chapters/ch12-agm.tex:1207`, tools line of `pb:noroots` | Prerequisite pointer | minor | The line gives Volume 4, Chapter 1, for inclusion–exclusion, derangements, and the binomial law. Inclusion–exclusion for probabilities is in that chapter. Derangements are Volume 1, Proposition 2.3. The binomial law is Volume 4, Chapter 2; Chapter 1 only says that chapter will take it up. | Split the pointer. |
| V5-10 | `volume5-calculation/chapters/ch07-fft.tex:667`, solution of `pb:newman` | Exercise | minor | Part (b) asks for the sum below \(4^k\), and the solution correctly gets \(2\cdot 3^{k-1}\). The next sentence sets that margin equal to \(3^k\). The sum is \(\frac23\cdot 3^k\). The exercise’s “order \(N^{\log 3/\log 4}\)” is the right claim; \(3^k=N^{\log 3/\log 4}\) is the size of the order, not the sum. | Say the sum is \(\frac23 N^{\log 3/\log 4}\). |
| V5-11 | `volume5-calculation/chapters/ch09-complex.tex:860`, solution of `ex:xn` | Exercise | minor | “Its integral tends to \(0\) as \(n\ge 2\).” The bound is \(\frac{2\pi R}{n(R^n-1)}\), which for each fixed \(n\ge 2\) tends to \(0\) as \(R\to\infty\). | Replace “as \(n\ge 2\)” with “for \(n\ge 2\), as \(R\to\infty\).” |
| V5-12 | Reading PDF, copyright page (folio iv) | Front matter | minor | The page says “ISBN (paperback): to be assigned.” Volume 5’s `main.tex` does not set a paperback ISBN. Volumes 2 and 3 do. | Put the assigned ISBN in the source when the author has one. |
| V5-13 | `volume5-calculation/chapters/ch06-fourier.tex:500`, exercise `pb:siegel`; reused at `ch12-agm.tex:555` | Notation | minor | The exercise writes \(e(-k\cdot x)\) and later solutions write \(e(-jk/n)\). Nothing in this volume, or in the shared preamble, defines \(e(t)=e^{2\pi it}\). The calculations are right once that shorthand is assumed. | Define it at the first use. |
| V5-14 | `volume5-calculation/chapters/ch05-gamma.tex:89–100`, Lemma on log-convex integrals | Rigor | minor | The proof applies the weighted AM–GM inequality at each \(t\) and integrates over an interval that may be improper. Both integrands are non-negative, so the inequality survives the limit of compact subintervals, but that sentence is not there. Bohr–Mollerup, the Beta integral, and duplication all use the lemma. The identities themselves are right. | Name the non-negative limit. |
| V5-15 | `volume5-calculation/chapters/ch02-generating.tex:655` and `:1400–1401`, exercise `pb:diehit` | Numerical | minor | The other roots of \(1-\frac16(z+\cdots+z^6)\) nearest the origin have modulus \(1.36939\ldots\), so \(\rho_0=1/1.36939\ldots=0.730250\ldots\). The exercise says every \(\rho>0.7302\) works. A \(\rho\) with \(0.7302<\rho\le\rho_0\) does not dominate the error. The solution’s “\(1.3694\), so \(\rho_0=0.7302\)” is the same rounding used as a threshold. | Print \(\rho_0\approx0.73025\) and require \(\rho>\rho_0\). |
| V5-16 | `volume5-calculation/chapters/ch03-series.tex:435–437`, solution of `ex:eirrational` (b) | Exercise | minor | The integer is \(aA_n+bn!+cC_n=-(ar_n+cs_n)\). The write-up shows \(0<ar_n+cs_n<1\), so the integer lies in \((-1,0)\). The last sentence calls that integer positive. The contradiction is already in the interval. | Say there is no integer strictly between \(-1\) and \(0\). |
| V5-17 | `volume5-calculation/chapters/ch02-generating.tex:216–218`, Example on merge sort | Pedagogy | minor | A merge costs at most \(n\) comparisons, and the next sentence says the worst-case cost satisfies \(T(n)=2T(n/2)+n\). The inequality that follows from “at most” is \(T(n)\le 2T(n/2)+n\). The solved formula \(T(n)=n\log_2 n+T(1)n\) is the solution of the equality, and it has the right leading term. | Write the inequality, or say the equality is the model being solved. |
| V5-18 | `volume5-calculation/chapters/ch02-generating.tex:280–281`, derangements | Rigor | minor | \(D_n=n!\sum_{k=0}^n(-1)^k/k!\) is the integer nearest to \(n!/e\) for every \(n\ge1\). The alternating tail after \(n\) has absolute value strictly less than \(1/(n+1)\le1/2\), which is why. That comparison is not on the page. | Write the tail bound. |
| V5-19 | `volume5-calculation/chapters/ch02-generating.tex:535–536`, exercise `pb:parts123` (c) | Exercise | minor | For perimeter \(2m\) the count equals \(a(m-3)\) when \(m\ge3\): the solution’s subtraction of \(1\) from each part needs a non-negative sum. For \(m<3\) there is no triangle, and \(a(m-3)\) is not defined. | Restrict to \(m\ge3\). |
| V5-20 | `volume5-calculation/chapters/ch11-asymptotics.tex:201–202` | Numerical | minor | The expansion of \(H_{10}\) through \(-\frac1{252n^6}\) is \(2.928968253927\ldots\). The printed digits \(2.928968253968\ldots\) are \(H_{10}=7381/2520\). They differ by \(4.09\times10^{-11}\), which is the error the sentence states as \(4.1\times10^{-11}\). A reader can take the printed string for the partial sum. | Print the partial sum, and say it differs from \(H_{10}\) by that amount. |

No issue in this log is critical. I did not find a false flagship statement in the thirteen chapters. V5-8 through V5-20 were checked after the first commit of this log. They do not change the scores: they are minor, and the exercise and citation scores were already held at 7 or 8 because the sets were only sampled.

## Verified correct

Numerical checks were done in Python with `mpmath` or exact fractions. A numerical check is not a proof. Where I also followed the argument, I say so.

- Bernoulli recurrence and \(B_1=-\frac12,B_2=\frac16,B_4=-\frac1{30},B_6=\frac1{42},B_8=-\frac1{30},B_{10}=\frac5{66},B_{12}=-\frac{691}{2730}\). Faulhaber for fifth powers and for tenth powers through \(n=1000\). The opening argument of the difference calculus (Theorem 1.1 and the falling-power basis) reads correctly.
- Pentagonal signs and the recurrence for \(p(n)\). Franklin’s pairing, including the two exceptional families, reads correctly on a full pass.
- \(\zeta(2k)\) and the four displayed values. Niven’s proof that \(\pi^2\) is irrational, including the bound. Viète’s areas. Wallis’s product as a corollary of the sine product, at the level of the statement.
- BBP partial fractions and the three integrals (logarithms cancel, the arctangent is \(\pi\)). Hexadecimal digits at positions \(10^6\) and \(10^6+1\). Borwein deficit fraction and \(2.31\times10^{-11}\). The probability statement of the Borwein theorem matches the simplex volume.
- Ball volumes, the maximum at dimension 5, and the sphere of largest area in \(\mathbb R^7\). \(\Gamma(1/4)\) via the lemniscate and the AGM. \(\varpi\) to 17 decimals.
- Gibbs constant and the location of the first maximum. Weyl’s criterion is the theorem Volume 6 cites, and \((n\alpha)\) is the next corollary.
- FFT operation counts. Figure 7.2’s spikes sit at frequencies 5 and 12.
- Fourier conventions, inversion, \(\widehat{\hat f}(x)=f(-x)\), the self-dual Gaussian, Poisson summation under the stated decay, and the theta transformation. The Gauss-sum cases mod 4. The Fresnel evaluation.
- Residue at the two upper poles of \(1/(1+z^4)\), equal to \(\pi/\sqrt2\). Star-shaped Cauchy includes \(F'=f\). Complex cotangent partial fractions agree with the form Volume 6 differentiates. Basel by residues: residue \(-\pi^2/3\) gives \(\sum_{n\ne0}n^{-2}=\pi^2/3\).
- Functional equation, residue 1, \(\zeta(0)=-\frac12\), trivial zeros, asymmetric form, and \(\zeta(1-2k)=-B_{2k}/(2k)\). Smoothed sums for \(k=0\) and \(k=1\), and the constant \(\zeta(-3)=\frac1{120}\) in the cubic smoothing. Ordinates to two decimals. Kuzmin’s contraction constant equals \(2\zeta(3)-3/2\).
- Euler–Maclaurin corrections, the harmonic expansion at \(n=10\), Stirling coefficients, the sign of the remainder (the comparison \(\rho_m=T_m+\rho_{m+1}\) with opposite signs), and the figure’s optimal errors.
- Eta transformation, including the Fourier-transform bookkeeping and the cosine signs. Hardy–Ramanujan table through \(n=1000\), \(\log P(0.99)\), and the shape of the main term \(e^{2a}/(4\sqrt3\,N')\). The major-arc and minor-arc inequalities I checked (the sine chord, the gain \(1/(80y)\), the Gaussian moments) support the \(O(n^{-1/4})\) conclusion. Rademacher is marked quoted.
- AGM of \(1\) and \(\sqrt2\), Legendre’s relation at \(k=1/\sqrt2\), Brent–Salamin partial errors through \(\pi_8\), and the pendulum lengthening of 18.0 percent at a right angle.
- Every one of the 165 exercises has a hint and a solution. Tonelli in Volume 7 is Theorem 9.5 (shared counter in the product-measure chapter). Lebesgue measure is Theorem 7.11.
- Volume 6’s citations of Theorems 3.7, 5.8, 5.14, 6.13, 8.14, 9.9, 9.15, 9.18, 9.26, 9.36, 9.37, 10.3, 10.8, 12.4, Propositions 10.1, 10.2, 10.6, Corollaries 4.5, 6.14, 9.35, 10.4, 10.9, 11.6, and Exercises 5.7, 6.5, 10.2, 10.3 say what those statements say. Volume 8’s use of Theorem 10.10 for \(\zeta(-1)^2=1/144\) is right. Volume 13’s Tate reminder of the \(2\pi\) convention is right. Volume 14’s display of \(\Lambda_\zeta(s)=-\frac1s-\frac1{1-s}+I(s)\) matches Theorem 10.8, because \(1/(s(s-1))=-1/s-1/(1-s)\).

Outside sources actually consulted: the AFP entry *Zeta_5_Irrational* (26 October 2026) and Fauzan’s Zenodo preprint for V5-5; the classical values of the zeros, Gibbs’ constant, the Glaisher–Kinkelin constant, and the Rademacher formula, against the statements as printed (the book’s Rademacher formula is the standard derivative form). Bernoulli, zeta, partitions, AGM, and BBP were recomputed rather than looked up.

## Not reviewed

- A line-by-line proof of every labelled statement. In particular I did not re-line Bohr–Mollerup, the whole of Fejér’s theorem, Laplace’s method past the statement and the figure, the transfer theorem, Goursat’s subdivision beyond the star-shaped conclusion, or every estimate in the five stages of the Hardy–Ramanujan proof. I checked the skeleton, the constants, and the inequalities named above.
- All 165 solutions. I checked that each exercise has a hint and a solution, and I recomputed the numerical solutions named in the chapter notes and in “Verified correct.”
- Every cross-volume sentence in Volumes 6–15. I extracted the numbered citations adjacent to “Volume 5” and checked kinds against a shared-counter numbering of this volume. I content-checked the reminders in Volumes 6, 8, 13, and 14 and the mismatches in V5-1–V5-3. Volume 9’s uses of Volume 5 that I saw are by chapter, not by a theorem number.
- Every index entry, every running head, and every one of the 355 print pages by eye. The margin scan and the sample pages are what the print score rests on.
- A Kindle Paperwhite. The EPUB checks are structural.
- KDP’s own acceptance of the file.
- Whether every historical date and quotation has a source beyond the ones I happened to know or looked up. The \(\zeta(5)\) sentence is the one I checked against a live page.

## Conformance to the plan

The manuscript matches the master plan’s decisions for this volume (the copy of `MASTER-PLAN-V5-V15.md` on the open plan PR, read only for structure): thirteen chapters, Hardy–Ramanujan as Chapter 12 in Part III with the eta transformation proved here, Waring removed, the BBP series left inside integration, a saddle-point example in the asymptotics chapter, \(\xi\) rather than \(\Lambda\) for the completed zeta, and \(\vartheta\) for Jacobi. Theorem 12.4 is what Volume 6 cites, and Volume 6 says its own argument is a second proof.

`docs/plan/book-05.md` on `main` is an older blueprint: twelve chapters, the partition asymptotic in Part I, and Waring still in this volume. The printed book does not follow that file. It follows the later decision.

## Comparison with the earlier scored read

This section was written after the scores and the issue log above were committed. The earlier report is the draft pull request #206, `docs/review/volume5-independent-scored-read-2026-11-12.md`, read at `8d2cab36`. It judged `604f29ea`. The fixes it asked for were reviewed in `docs/review/volume5-volume6-fixes-review-2026-11-12.md`. Each line below was checked in the current source, not taken from that second review’s “Accept.”

The earlier overall score was 7, with preparation for later volumes at 4, because the inversion theorem was boxed without continuity, the BBP digits were indexed wrong, and later volumes still used the pre-rewrite numbers, including a proof step in Volume 8 that cited Laplace’s method for the derivative of a path integral. Those three are repaired. This reading’s 8 is that repair, not a softer scale. Chapters 9 and 12 are still the hard ones, and the last chapter is still a coda with a problem warehouse attached.

### Earlier issues that are really fixed

| Earlier ID | What was wrong | Current state |
| --- | --- | --- |
| V5-C1 | Volume 8 cited Theorem 11.9 for \(F'=f\). That number was Laplace’s method. | `volume8-analysis/chapters/ch09-complex.tex` cites Theorem 9.9. That box is Cauchy’s theorem on a star-shaped set, and it includes \(F'=f\). |
| V5-M2 | Volume 15’s heuristics file cited Theorem 5.7 for Waring. There is no such theorem. | The sentence now says Waring’s problem is not a theorem of Volume 5. The file is still not in Volume 15’s `main.tex`. |
| V5-M3 | Volume 14 said this volume proves Hua’s lemma and uses it for Waring. | The sentence is gone from `ch05-expsums.tex`. |
| V5-M4 | `polyfermat.tex` said Volume 5 proved the Waring asymptotic. | It now says Waring is not a theorem of Volume 5. |
| V5-M5 | Volume 14 said this volume counts sums of powers by the circle method. | `three-primes.tex` says partitions only. |
| V5-M6 | Volume 9 cited “Appendix F” for Hurwitz. There is no appendix. | It cites Theorem 6.17, which is the isoperimetric inequality. |
| V5-M7 | Homology Cauchy and its neighbours were placed in “Volume 8, Chapter 14,” which that day was matrix inequalities. The subjects were Chapter 22. | On 13 November, pull request #212 made Volume 8 sixteen chapters and six appendices. Those subjects are now Chapter 14, `ch09-complex.tex`, and both sentences in this volume say Chapter 14. The pointer matches the book a reader can open. The intermediate repair to “Chapter 22” would be wrong today; it is not what is printed. |
| V5-M8 | The approximate-identity lemma and the inversion box omitted continuity, which the proof used. | Both now require continuity, and both say a jump is not in the class. Plancherel calls that inversion. |
| V5-M9 | The sentence after Heisenberg read the bound as a statement about variances. | The moments are said to be about the origin. The centred form is a separate shift, applied to \(g(x)=e^{-2\pi i\nu x}f(x+m)\). |
| V5-M10 | \(d=10^6\) was paired with the digit string `26C65E52`. | \(d=999999\) gives `26C65E52`, and \(d=10^6\) begins `6C65E52`. Recomputed. |
| V5-M11 | The parameter proof of the Gaussian integral was called the third, and Volume 4, Chapter 5, was said to have evaluated it by polar coordinates. | The text calls this the second proof and says Volume 4 takes the value from Volume 1. |
| V5-m1 | The FFT history named Juno’s orbit. | The orbit is Pallas. Juno’s eccentricity is kept as a dating clue. |
| V5-m2 | The Glaisher solution said the original partition had multiplicities at most 2. | It now says the original has multiplicities 4 and 3. |
| V5-m3 | \(H_0\) was used and not defined. | \(H_0=0\) is in the definition. |
| V5-m4 | \([n=0]\) was not defined. | The sentence that uses it defines it. |
| V5-m5 | The two pentagonal families were said to be disjoint with no check. | The rearrangement \((r+s)(3(r-s)-1)=0\) is in the proof. |
| V5-m6 | The Weyl caption stated the three-gap theorem. | That sentence is gone. |
| V5-m8 | Exercise `ex:eta` included the pole. | The identity is asked for \(\operatorname{Re}s>0\) with \(s\ne 1\). |
| V5-m9 | The ratio curve was labelled \(0.4432\) and the caption said \(0.4433\). | The curve node is \(0.4433\). |
| V5-m10 | The convex-volume admission named no theorem. | It names Volume 7, Theorem 7.11, which is Lebesgue measure. |
| V5-m11 | The blurb and the KDP text said every result is proved in full, and the KDP list skipped partitions. | Both say quoted results are marked, name Rademacher, and the KDP list names the Hardy–Ramanujan formula. |
| V5-m12 | The dominated-convergence counterexample mentioned only the missing dominant. | The solution says both hypotheses fail, and that the convergence is not uniform on \([0,1]\). |
| V5-m13 | The list \(i^{-n}=1,-i,-1,i\) was not in the order of the four cases. | The list is \(-i,-1,i,1\), in the order \(n\equiv 1,2,3,0\). |
| V5-m14 | No index and no collected bibliography. | There is an index (folio 338) and a Sources chapter (folio 344). The four index entries checked point at the right folios. |

V5-M1, the off-by-two in later volumes, is fixed in the printed reminders that were opened: Volume 6’s list in the verified section, Volume 8’s Theorem 9.9 and Theorem 10.10, Volume 9’s Theorem 6.17, Volume 13’s \(2\pi\) convention, and Volume 14’s formula for \(\Lambda_\zeta\). It is not fixed everywhere. The retarget itself wrote one wrong number into a printed book. That is V5-1.

V5-m7 is fixed in the sense the earlier report asked. The sentence no longer says the irrationality of \(\zeta(5)\) is unknown. It names Fauzan’s 2026 argument and Hyman’s formalisation of 26 October 2026, and it says this volume does not reproduce the argument. V5-5 is what that repair still does not say: the source is an unrefereed preprint, and the formalisation discharges numeric inequalities by approximation.

### Earlier issues that are not fixed

None of V5-C1 through V5-m14 is still present in the form the earlier report wrote down, except the two partials just named: V5-M1 left one printed wrong number, and V5-m7 left the caveat in V5-5.

### New problems the fixes introduced

Both lines were written by `df9b594d` on 12 November, “Retarget Volume 5 and Volume 6 citations in later volumes” (pull request #210). They were not in the manuscript the earlier report read.

- **V5-1**, printed. Volume 14’s critical-line reminder calls the theta law “Corollary 10.10.” The retarget’s own spot check had the right number for a different sentence: the theta transformation that makes a divisor error exponential is Corollary 8.10. Number 10.10 is \(\zeta(1-2k)=-B_{2k}/(2k)\).
- **V5-3**, not printed. The same commit states Theorem 8.6 in the convention \(F(t)=\frac1{2\pi}\int f(u)e^{itu}\,du\). Theorem 8.6 is the \(2\pi\) convention. Volume 13’s reminder, also part of that retarget, states the \(2\pi\) convention correctly.

### What the earlier report missed

- **V5-2.** `conjectures-ch01-born.tex:229` has cited Theorem 6.11 for \(\int(\sin u)/u\,du=\pi/2\) since 31 October. Theorem 6.11 is Parseval. The integral is Theorem 4.11. The file is not in Volume 15’s `main.tex`. The earlier report said it did not open every one of the 311 citations. The fix pass did not open this line either. It is not a new defect.
- **V5-6.** “By independence (Volume 4, Chapter 8)” in the random-walk example. Independence is Volume 4, Chapter 2. The return formula is in Chapter 8. The earlier chapter note on Fourier series did not flag it.
- **V5-7.** Exercise `pb:ncycles` quotes Fulton and Harris for the irreducibility of exterior powers. The earlier report did not re-solve that exercise, and the preface’s list of admissions still does not name it. V5-4 is the same preface sentence, which the earlier report called accurate after V5-m10 was only about the missing convex-volume number. Mertens, admitted in `pb:dickmanint`, is still outside that sentence. The earlier chapter note on the AGM recorded the admission and did not log it.

The earlier report’s comparison also said the handoff had missed the inversion class, the BBP index, Juno, the Glaisher sentence, \(H_0\), \([n=0]\), the pentagonal disjointness line, the three-gap caption, and the polar-coordinate attribution. Those are the items in the fixed table. It was right about them on 12 November. They are not still open.

The second review of the fixes accepted the retarget on a spot check and did not catch Corollary 10.10 or the \(1/2\pi\) formula. That is the gap between its “Accept” on V5-M1 and the current printed reminder in Volume 14.

A later pass over the same manuscript, after this comparison was drafted, added V5-8 through V5-20. None of them is in the 12 November issue log. V5-8 is another printed wrong number, in Volume 11: Section 7.4 for the Beta integral. V5-9, V5-10, and V5-11 are local slips in solutions. V5-12 is the unassigned paperback ISBN on folio iv. V5-13 is the undefined shorthand \(e(t)\) in the Siegel exercise. V5-14 is the missing sentence when the log-convexity lemma integrates over an improper interval. V5-15 through V5-19 are small slips in Chapters 2 and 3: a rounded spectral radius used as a strict threshold, a sign error in the last sentence of the proof that \(e\) is not quadratic, a merge-sort equality written after “at most,” the missing tail bound for derangements, and integer triangles of perimeter \(2m\) for \(m<3\). V5-20 is the \(H_{10}\) display: the printed digits are \(H_{10}\) itself, and the partial sum is smaller by the stated \(4.1\times10^{-11}\). They do not reopen a fixed item and they do not change the score.
