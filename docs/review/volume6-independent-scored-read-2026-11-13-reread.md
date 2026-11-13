# Volume 6, *Crossroads*: independent scored re-read

**Referee.** Fresh read of `main` at `f10e4c99` (13 November 2026). The `books` release is the same commit. This report was written before any Volume 6 review file, handoff, or earlier pull-request discussion was opened. The comparison with those documents is a later section and is not part of the scores below.

**Book.** *Order and Chance*, Volume 6, *Crossroads: Arithmetic Meets Analysis*. SEGHAIER Oussama. First edition, 2026. Source `volume6-crossroads/`. Reading PDF `Volume.6.-.Crossroads.pdf` (300 pages, 7 × 10 in, cover included). Print PDF `Volume.6.-.Crossroads.-.Print.pdf` (299 pages, 7.125 × 10.25 in). EPUB `Volume.6.-.Crossroads.epub` (23 MB).

**Reader assumed.** A reader who has worked through Volumes 1–5, so complex analysis, characters, and the elementary prime estimates are already in hand. The prose is still judged against the series voice: a friend teaching, one step at a time.

**What was read.** The preface, all twelve chapters including exercises, hints, and the solutions of Chapters 1–3 and 9 in full, the statements of every exercise in Chapters 4–12, a sample of the Chapter 12 closing-problem solutions, every figure caption against its numerical claim where a number is printed, the chapter sources, the index, the blurb, the KDP description, and About the Cover. The reading PDF was opened on the part opener, the Chebyshev figure, the prime-number figure, and the index. The print PDF was checked for page size and for charcoal reaching the edge of the part opener. The EPUB was checked for plate CSS and inline-math baseline, not on a Kindle.

**Outside checks actually used.** Every number below that is called recomputed was computed in this reading (sieve or quadrature), not copied from the book. Gap records were checked against Tomás Oliveira e Silva’s table of gaps below \(4\cdot 10^{18}\) (`https://sweet.ua.pt/tos/gaps.html`) and the maximal-gap list at `http://primerecords.dk/primegaps/maximal.htm`. The first mod-4 crossing was checked against Leech’s 1957 note and OEIS A007351 / A038691. The density \(0.9959\ldots\) was checked against Rubinstein and Sarnak, *Experimental Mathematics* 3 (1994), as quoted in the literature (GRH and linear independence). Back-references into Volumes 1–5 were checked by counting numbered environments in `main.tex` order, and the load-bearing statements (Volume 2, Theorems 2.2 and 2.4; Volume 5, Theorem 12.4; Volume 4, Theorems 4.2 and 4.4; Volume 1, Theorems 9.3 and 9.4) were read.

## 1. Chapter scores

Dimensions: (a) correctness, (b) rigor, (c) prerequisites, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography. Ten is reserved for work with nothing left to fix.

| Ch | Chapter | a | b | c | d | e | f | g | h | i | j |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Mertens’s theorems | 9 | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 9 |
| 2 | Averages | 9 | 8 | 8 | 8 | 8 | 8 | 9 | 8 | 7 | 9 |
| 3 | Characters and \(L\)-functions | 9 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 9 |
| 4 | Dirichlet’s theorem | 9 | 9 | 8 | 8 | 9 | 8 | 9 | 9 | 8 | 9 |
| 5 | The prime number theorem | 9 | 9 | 9 | 8 | 9 | 8 | 9 | 8 | 8 | 9 |
| 6 | The zeros of zeta | 8 | 8 | 8 | 7 | 7 | 8 | 7 | 8 | 8 | 9 |
| 7 | The explicit formula | 9 | 8 | 9 | 8 | 9 | 8 | 8 | 8 | 8 | 9 |
| 8 | Sieves | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 9 |
| 9 | Erdős–Kac | 9 | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 8 | 9 |
| 10 | Random models | 9 | 8 | 8 | 8 | 9 | 8 | 9 | 9 | 8 | 9 |
| 11 | Exponential sums | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 9 |
| 12 | Modular forms | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 6 | 8 |

**Chapter 1.** The three Mertens theorems, the corrected liminf/limsup sandwich (Corollary 1.4), and \(M+H=\gamma\) were read line by line. Recomputed: \(\psi(3000)/3000=1.000365\), \(\theta(3000)/3000=0.97745\); \(R(10^3)=-1.298\), \(R(10^5)=-1.329\), \(R(10^7)=-1.3324\); the sum of reciprocals to \(10^7\) sits \(0.261507\) above \(\log\log\), within \(10^{-5}\) of \(M\). Abel summation is stated with the boundary term and used correctly at \(y=1\) and \(y=2\).

**Chapter 2.** Wintner, the three mean-value error terms, the hyperbola identity, and the \(\tau_3\) main term were checked. The coefficient \(3\gamma-1\) comes out of the two logarithmic sums. Recomputed for \(n\le 10^6\): mean of \(\tau\) is \(13.970\), median \(8\), proportion with at least \(14\) divisors is \(0.343\), and \(\tau(720720)=240\). The lattice count \(359/576\) is exact.

**Chapter 3.** Landau’s argument for a real zero at \(s=1\), and Dirichlet’s finite formula for \(L(1,\chi)\), were checked, including the branch of \(\log(1-e^{ix})\) and the worked values \(\pi/4\), \(\pi/(3\sqrt 3)\), and \((2/\sqrt 5)\log\phi\). Gauss sums for \(\chi_{-4}\) and \(\chi_{-3}\) match the text.

**Chapter 4.** The proof from \(L(1,\chi)\ne 0\) is the standard one and the hypotheses are in place. Recomputed at \(x=10^6\): the two mod-\(3\) weighted sums sit at \(-1.187\) and \(-0.512\), and \(L'/L(1,\chi_{-3})=0.368\). The race caption (ten ties from \(5\) to \(26921\), a single lead for class \(1\) on \(26861\le x<26863\)) matches a direct count and Leech.

**Chapter 5.** Newman’s contour, the identity \(G(z)=-(Z'/Z+1)/s\), the monotone lemma, and the passage to \(\pi(x)\) were checked. Recomputed: \(\pi(10^8)=5761455\), \(\pi\log x/x=1.06130\), and \(\mathrm{Li}(10^8)-\pi(10^8)=753.3\) with \(\mathrm{Li}\) from \(2\). The chapter says, correctly, that this argument gives no error term.

**Chapter 6.** The constant \(7/8\) in \(N(T)\) is the Gamma phase plus the pole, and the arithmetic checks. The zero-free squeeze really does give \(1-\beta\ge 1/(14A'\log|t|)\). Borel–Carathéodory and the constants \(17\) and \(129\) in the local lemma follow from the Cauchy estimates written on the page. The moving proportions of zeros on the critical line are in a remark and labelled as quotations. Complex Stirling itself was used, not re-derived from the first line.

**Chapter 7.** The explicit formula has the classical shape, including \(-\log 2\pi\) and \(-\frac12\log(1-x^{-2})\). Von Koch’s three-way equivalence was checked in both directions that the text proves; the form proved for \(\psi\) is \(O(\sqrt x\log^2 x)\), which is the honest one. The bias identity does not use the functional equation; the wave reading is marked admitted and pointed at Volume 13, Chapter 12. Recomputed: class \(1\) leads at exactly \(3406\) integers up to \(10^7\), first at \(26861\); the largest ratio \(|\psi(x)-x|/(\sqrt x\log^2 x)\) on real \(x\in[73.2,10^7]\) is \(0.03653\).

**Chapter 8.** Selberg’s diagonalisation, the bound \(|\lambda_d|\le 1\), Brun–Titchmarsh with the factor \(2\) on short intervals (and the separate arithmetic-progression constant, sent to an exercise), and Brun’s \(O(x/\log^2 x)\) for twins were checked. The proof’s constant is about \(64\), as the remark says. Recomputed: \(\pi_2(10^7)=58980\), and \(2C_2\int_2^{10^7}dt/\log^2 t=58754\).

**Chapter 9.** Turán–Kubilius is the right variance, the moment comparison with the coin model is correct for \(z^k\ll N\), and the passage back from \(\omega_z\) to \(\omega\) has an error \(o(\sqrt{\log\log x})\). Recomputed: the proportion of \(n\le 10^7\) with \(\omega(n)\le\log\log 10^7\) is \(0.320\). The boxed moment lemma uses the symbol \(m_k\) defined earlier as the Gaussian moments; the box itself does not repeat that sentence.

**Chapter 10.** Both Borel–Cantelli halves of Cramér’s gap theorem were checked, including the weakening \(e^{-(1-\varepsilon)}\ge e^{-1}\). Maier is a remark, headed as quoted, and Buchstab is pointed at a problem that proves the range \(u\le 3\) and at Volume 15 for the rest. Recomputed near \(10^9\): a million bins of length \(21\) have mean \(1.013\) and variance \(0.788\). The ratios \(354/\log^2 p=0.72\), \(1132/\log^2 p=0.92\), and \(1476/\log^2 p=0.84\) match the published gap starts.

**Chapter 11.** The geometric-sum bound, the Pólya–Vinogradov estimate \(\sqrt q(1+\log q)\), and the exponent \(1/(2\sqrt e)=0.3032\ldots\) were checked. Weyl differencing and the van der Corput derivative tests were read; they are classical and the hypotheses are stated, but not every \(\varepsilon\) was recomputed. The single curlicue plate was not audited coordinate by coordinate.

**Chapter 12.** Both halves of the fundamental domain are proved (Theorem 12.2). The Fourier coefficients of \(E_4,E_6,E_8,E_{12}\), the identity \(\sigma_7(2)=129=9+120\), and the congruence modulo \(691\) (the arithmetic \(65520\equiv -125\), \(432000\equiv 125\)) were checked. Siegel’s contour for \(\eta\) was checked through the residues and the limit \(4\log y\). The letter \(q=e^{2\pi i\tau}\) is announced in the first page. The thirty-nine closing problems were not certified one by one; that is why the exercise score stays at \(7\).

## 2. Whole-book scores

| Item | Score | Why |
| --- | --- | --- |
| Structure and arc | 8 | Three parts and twelve chapters, in the order the blueprint freezes: Mertens through Dirichlet and Newman, then zeros and the explicit formula, then sieves, Erdős–Kac, Cramér, exponential sums, and one modular exhibit. The closing-problem list makes the volume 299 interior pages, well above the blueprint’s 190–220. |
| Continuity with Volumes 1–5 | 8 | The load-bearing citations that were opened say what the proof uses: Volume 2, Theorems 2.2 and 2.4; Volume 5, Proposition 10.6 and Theorem 12.4; Volume 4, Theorems 4.2 and 4.4; Volume 1, Theorems 9.3 and 9.4. Two facts are used unproved, and both uses are labelled admitted. |
| Preparation for later volumes | 7 | Most numbered citations that were checked resolve: Theorem 5.5 is the prime number theorem, Theorem 6.9 carries the \(7/8\), Theorem 7.8 is the error term, Theorem 7.10 is von Koch, Theorem 10.7 is Gallagher, Theorem 11.11 is Pólya–Vinogradov, Theorems 12.1 and 12.2 are the generators and the fundamental domain, Exercise 12.42 is Gauss reduction of positive definite forms. One citation in Volume 8 points at the wrong chapter. |
| Title and subtitle | 9 | *Arithmetic Meets Analysis* is the catalog subtitle, and it is what the book does: every chapter puts an arithmetic object on one side and an analytic machine on the other. The preface states the series question in the form this volume can answer, and marks Maier as the first crack. |
| Front matter, index, bibliography | 7 | The preface is accurate, including the two admitted facts. Each chapter has a sources list with real papers. The index is a selective list of named statements, with working page numbers, not a subject index. The blurb is a little ahead of what is proved. |
| Print PDF | 9 | 299 pages, each \(513\times 738\) pt. Text stays off the outer six points. The part opener is charcoal, \((20,20,21)\), through the outer edge and the corners. Folios, running heads, and the design-5e boxes match the pages that were opened. |
| EPUB | 8 | Plates are PNG with `width:100%`, `max-width:100%`, `height:auto`. Inline formulas are PNG with width and `vertical-align` in em. No SVG plates. The file is 23 MB. It was not opened on a Paperwhite. |

## 3. Overall

**Overall score: 8.2 / 10.**

**Verdict.** The flagship chain is real mathematics, written so that a reader can check it: no zero on \(\operatorname{Re}s=1\), Newman’s theorem, the prime number theorem, the zero count with the constant \(7/8\), a classical zero-free region, the explicit formula, von Koch, Selberg, Brun, Erdős–Kac, Cramér’s model, and \(E_4^2=E_8\) with the congruence modulo \(691\). The numbers that were recomputed agree with the page. I would recommend the twelve chapters to a reader who has finished Volumes 1–5.

I would not call the volume finished as a reference. The same letter \(\tau\) is the divisor function in Chapter 2 and Ramanujan’s function in Chapter 12, with no warning. The index will not find the fundamental domain or the congruence. The jacket says the \(4n+3\) primes lead most of the time, and that every theorem is proved in full; the \(99.59\%\) is a conditional quotation, and several deep statements are remarks. Those are revisions, not a reason to distrust the proofs.

## 4. Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V6-1 | `volume6-crossroads/chapters/ch02-averages.tex:10` and `ch12-modular.tex:10` | Notation | major | Chapter 2 sets \(\tau(n)\) as the number of divisors and uses it through \(\tau_3\) and \(\tau_k\). Chapter 12 sets \(\tau(n)\) as Ramanujan’s coefficient, \(q-24q^2+252q^3-\cdots\), and never says that this is a different function. A reader who remembers Chapter 2 will misread \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\). | In the first paragraph of Chapter 12, say that this \(\tau\) is not the divisor function of Chapter 2, and keep \(d(n)\) or \(\tau\) for one of them only. |
| V6-2 | `volume8-analysis/chapters/ch09-expanders.tex:316` | Downstream citation | major | The sentence says the Riemann hypothesis implies the prime number theorem with error \(O(\sqrt x\log x)\), and cites Volume 6, Chapter 5. Chapter 5, after Theorem 5.5 (`ch05-pnt.tex:233–236`), says the proof gives no error term, and places von Koch’s \(O(\sqrt x\log x)\) for \(\pi(x)\) as a historical statement whose proof is not in that chapter. The equivalence proved in this volume is Theorem 7.10: the hypothesis is equivalent to \(\psi(x)=x+O(\sqrt x\log^2 x)\), and to \(O(x^{1/2+\varepsilon})\). | Point the expander chapter at Theorem 7.10, and say which of the two error shapes is meant. |
| V6-3 | `volume6-crossroads/blurb.tex:6` and `kdp.md:5–7` | Jacket | minor | Both say the book explains why primes \(4n+3\) lead most of the time, and that every theorem is proved in full. In the book the count up to \(26861\) is unconditional (Chapter 4, Figure 4.2; Chapter 7, the paragraph before Proposition 7.11). The figure \(99.59\%\) is Rubinstein–Sarnak, under GRH and linear independence, and is labelled as such (`ch07-explicit.tex:351–354`). Deligne, Maier, the class-number formula, and the Vinogradov–Korobov region are remarks. The preface draws this line; the jacket does not. | On the jacket, say that the lead is explained, and that the percentage is conditional. Keep “every theorem is proved” only if “theorem” means a numbered statement that is not a remark. |
| V6-4 | `volume6-crossroads/chapters/index.tex:1–66` | Index | minor | The index is a list of some named statements. Page numbers that were checked against the reading PDF are right (Proposition 1.2 is on printed page 4; Abel summation, Lemma 1.1, is on page 3). Theorem 12.2 (fundamental domain, both halves), Theorem 12.9 (dimensions), and Corollary 12.11 (the congruence modulo \(691\)) are not in the list. Neither are \(\mathrm{Li}\), Siegel zero, or the Meissel–Mertens constant, except where a theorem heading happens to carry the name. | Add the statements a reader will look up, or say in the headnote that the list is only the named theorems and is not complete. |
| V6-5 | `volume6-crossroads/chapters/ch12-modular.tex:379` | Handoff | minor | “Volume 14 starts where this volume stops: the classical zero-free region, Selberg’s sieve, and Weyl sums.” Those three are theorems of this volume (Theorems 6.12, 8.2, 11.4 and 11.7). Volume 14’s preface says this volume ended with the prime number theorem, its error term, and the first sieves, and that Volume 14 begins with zeros off the line, Bombieri–Vinogradov, and the circle method. | Name what Volume 14 adds: a stronger zero-free input used for short intervals, Bombieri–Vinogradov, and exponential sums over primes. |
| V6-6 | `volume6-crossroads/chapters/ch09-erdoskac.tex:108` and `:158–167` | Rigor | minor | Line 108 defines \(m_k\) as the Gaussian moments. Lemma 9.6 then says: if \(\mathbb E[Y_N^k]\to m_k\) for every \(k\), then \(Y_N\) tends to \(\Phi\). Read alone, the box is false for a general limit sequence \(m_k\). The proof uses \(\frac{m_{2j}}{(2j)!}=\frac1{2^j j!}\), which is the Gaussian relation, and the paragraph above the lemma says “moments of a standard Gaussian”. | Put “where \(m_k\) are the Gaussian moments above” in the statement of Lemma 9.6. |
| V6-7 | `volume6-crossroads/chapters/ch01-mertens.tex:12–14` and `:236–237` | Pedagogy | minor | The opening says the independence heuristic is wrong by twelve percent, forever. \(2e^{-\gamma}-1=0.12292\), so twelve percent is a rounding. The beauty box compares the product with \(1/\log n\) by quoting the prime number theorem, which is proved in Chapter 5. The box is a preview, not a premise of Chapter 1, but it is not labelled as one. | Write \(12.3\%\), or “about twelve percent”, and one clause that the comparison waits for Chapter 5. |
| V6-8 | `volume6-crossroads/chapters/ch01-mertens.tex:287–301` | Exercises | minor | The cycle exercise is marked \(\star\star\). The solution is the factorial-moment proof that \((C_1,\ldots,C_k)\) tends to independent Poissons, plus Arratia–Tavaré. That is a \(\star\star\star\) argument for this place in the book. The mathematics of the solution is right: the count of lists is \(n!/\bigl((n-M)!\prod j^{m_j}\bigr)\), and the probability of a fixed list is \((n-M)!/n!\). | Mark it \(\star\star\star\), or move the inclusion-exclusion to a hint and keep the comparison with Mertens as the \(\star\star\) part. |
| V6-9 | `volume6-crossroads/chapters/ch02-averages.tex:231–236` | Quoted result | minor | After the proved bound for \(\tau_3\), the text states \(\sum_{n\le x}\tau_k(n)=xP_k(\log x)+O(x^{1-1/k}\log^{k-2}x)\) with leading coefficient \(1/(k-1)!\). Exercise 2.8 proves the main term only, with the weaker error \(O_k(x\log^{k-2}x)\). The sharper exponent is not proved on the page and is not marked as quoted. The constant term of \(P_3\) in the next sentence is marked as a quotation from Titchmarsh. | Mark the Piltz error as quoted, or stop at the error the exercise proves. |
| V6-10 | `volume6-crossroads/chapters/ch04-dirichlet.tex:142–144` | Heuristic | minor | The remark says that passing from \(\psi\) to \(\pi\) subtracts about \(\sqrt x/\log x\) from class \(1\), and that under the Riemann hypothesis for \(L(s,\chi_{-4})\) the error in the prime number theorem for progressions is of the same size, so the subtraction is visible. The square contribution is the right order. The hypothesis makes the error in \(\pi(x;4,a)\) of size \(O(\sqrt x\log x)\), larger than \(\sqrt x/\log x\) by two powers of \(\log x\). The lead is a shift of a distribution, which is what the next sentence attributes to Rubinstein and Sarnak. The count up to \(60\,000\) is unaffected. | Say the square term is smaller than the conditional error by logarithmic factors, so the lead is a bias of logarithmic density, not a pointwise comparison of sizes. |

No critical issue. Nothing in the flagship chain was found false.

## 5. Verified correct

These were checked in the source, not merely recognised as familiar. A numerical check is not a proof; both are recorded where both were done.

**Chapter 1.** Lemma 1.1 (Abel), including the cancellation of the \(p=2\) boundary term in the proof of \(M+H=\gamma\). Proposition 1.2 against Volume 2, Theorem 2.4(i), \(\prod_{p\le x}p<4^x\), and the paragraph after it for the upper bound on \(\pi\). Theorem 1.3. Corollary 1.4 in the form \(\liminf \theta(x)/x\le 1\le\limsup\theta(x)/x\). Theorems 1.5 and 1.6, including the constant \(M=1-\log\log 2+\int_2^\infty R(t)/(t\log^2 t)\,dt\). The values in Figures 1.1 and 1.2 and in the beauty box, as recomputed above. Exercise 1.6, the bound \(\bigl|\sum_{n\le x}\mu(n)/n\bigr|\le 1\).

**Chapter 2.** Wintner’s theorem under \(\sum |h(d)|/d<\infty\). The means \(6/\pi^2\), \(6/\pi^2\), and \(\pi^2/6\). The sums of \(\varphi\) and \(\sigma\), with main terms \(3x^2/\pi^2\) and \(\pi^2 x^2/12\). The squarefree count \(6x/\pi^2+O(\sqrt x)\). The coprime-pair formula \(C(x)=2\sum_{b\le x}\varphi(b)-1\). The \(\tau_3\) asymptotic. The Stieltjes evaluation \(3\gamma^2-3\gamma-3\gamma_1+1=0.4863\) with \(\gamma_1=-0.0728\), quoted and unused, recomputed from the public constants. The census of \(\tau(n)\) for \(n\le 10^6\).

**Chapter 3.** Orthogonality is Proposition 3.1; the non-vanishing is Theorem 3.8; Dirichlet’s formula is Theorem 3.10; Leibniz is Example 3.11. These numbers match the later volumes that cite them. The real-character proof via \(\sum r(n)n^{-1/2}=\infty\). The odd and even formulae, and the three numerical values in Figure 3.2.

**Chapter 4.** Theorem 4.1. The mod-\(3\) limits in Figure 4.1, to the digits printed. The race in Figure 4.2, including the ten ties.

**Chapter 5.** Theorem 5.2 (the \(3\)-\(4\)-\(1\) inequality). Theorem 5.3 (Newman), including \(|K|=e^{xT}2|x|/R^2\) on \(|z|=R\) and the bound \(2B/R\). Theorem 5.5, with \(g(0)=-1-\gamma\). Theorem 5.7, \(\sum\mu(n)/n=0\), and the partial sums \(A(10^4)=-0.00208\), \(A(10^6)=0.000201\), \(A(10^7)=0.000102\). Theorem 5.8, the filtering step. Figure 5.1, including \(\mathrm{Li}(10^8)-\pi(10^8)=753\).

**Chapter 6.** The phase \(\alpha(T)/\pi+1=\frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78+O(1/T)\). Theorem 6.9. The zero-free region, existence of \(c\), with the factor \(14A'\) as derived. Lemma 6.5 and the constants in Lemma 6.6. The quotations of Levinson, Conrey, and Pratt–Robles–Zaharescu–Zeindler are labelled as quotations; the fractions \(1/3\), \(2/5\), and \(5/12\) are the results those papers announce.

**Chapter 7.** Theorem 7.5 and Corollary 7.6. Theorem 7.8 and Corollary 7.9. Theorem 7.10, all three directions written in the text. Proposition 7.11, unconditional. The first zero \(1/2+6.0209i\) of \(L(s,\chi_{-4})\) agrees with Leech’s \(6.020948\). Schoenfeld’s shape \(\frac1{8\pi}\sqrt x\log^2 x\) for \(x\ge 73.2\), and the ratio \(0.0365\), recomputed as a maximum over real \(x\) of the step function \(\psi\). The bound \(|\psi(x)-x|/\sqrt x<0.81\) on \([10^3,10^7]\) holds; the maximum found is \(0.803\).

**Chapter 8.** Theorem 8.2. Lemma 8.3, \(G(y)\ge\log y\). Theorem 8.4, the short-interval ratio, and the remark that an interval of length \(N=x^{1/k}\) is bounded by \(2k\) times the prime-number density. Theorem 8.5 and Corollary 8.6. Theorem 8.8, constant \(\pi N+1/\delta\), with the sharp constant quoted and unused. Figure 8.1.

**Chapter 9.** The statement of Theorem 9.7, the truncation \(z=x^{1/(\log\log x)^{1/4}}\), and the proportion \(0.32\) at \(10^7\). The identity \(2^\omega=\mu^2*\mathbf 1\), used from Chapter 2.

**Chapter 10.** Definition 10.1. Theorems 10.2 and 10.4. The singular series for twins, \(2C_2=1.3203\ldots\). Theorem 10.7 is the seventh numbered statement of the chapter and is Gallagher’s average, as Volume 14 cites it. Maier’s remark states both the limsup and the liminf, for every \(\lambda>1\), and does not pretend to prove them. The constant \(\gamma+\log 2\pi-1=1.415\). The three gap records and their ratios to \(\log^2 p\).

**Chapter 11.** Lemma 11.1. Theorem 11.11. The exponent in Theorem 11.12.

**Chapter 12.** Proposition 12.1 and Theorem 12.2, both halves. The Bernoulli evaluations of \(E_4,E_6,E_8,E_{12}\). Corollary 12.10 at \(n=2\). Corollary 12.11. Theorem 12.7’s second proof, through the residue computation that produces \((\ast)\). The warning about \(q\). Volume 5, Theorem 12.4, is the transformation of \(\eta\) (the fourth numbered statement of Volume 5, Chapter 12, which is `hardy-ramanujan.tex`).

**Downstream citations that resolve.** Volume 7, Theorem 5.5. Volume 9, Proposition 12.1 and Theorem 12.2. Volume 13, Theorem 3.5 for \(|\tau(\chi)|=\sqrt q\), and Exercise 12.42 for \(a\le\sqrt{|D|/3}\). Volume 14, Theorem 8.4, Theorem 10.7, and equation (8.1), which is the only displayed equation of Chapter 8 and is the large-sieve sum over \(a/q\). Volume 15, Theorem 7.8 for \(\psi(x)=x+O(xe^{-c\sqrt{\log x}})\), and Example 3.11 for \(L(1,\chi_{-4})=\pi/4\). Volume 12’s citation of \(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78+O(\log T)\) matches Theorem 6.9.

## 6. Not reviewed

- A line-by-line re-derivation of complex Stirling (Theorem 6.1). It was used as a cited input to \(N(T)\) and to the left half-plane, and the consequences that were checked are consistent with it.
- Every exercise solution in Chapters 4–8 and 10–11. The statements were read. The solutions of Chapters 1–3 and 9 were read in full.
- The thirty-nine closing problems in Chapter 12, beyond the statements and a few solutions (the energy bound, Beukers’s integral for \(\zeta(2)\), and the statement of Euler’s polynomial). A false final answer could still be sitting in that list.
- Coordinate-level checks of the TikZ plates other than the numerical captions that were recomputed. The Chebyshev and prime-number plates were looked at in the PDF; the curves match the captions.
- The EPUB on a Kindle Paperwhite. The file was inspected for the pipeline rules only.
- Proofs, inside Volumes 1–5, of the theorems this volume cites. The cited statements were checked for number, kind, and, in the load-bearing cases, for the claim. Their proofs were not re-audited.
- A page-by-page search of all 300 reading pages for a split box or a collision. The pages opened were clean, text did not enter the outer eight points, and the print part opener bleeds. That is not a certificate for every page.
- Volume 8 and Volume 9 were not reread as books. Their citations of Volume 6 were grepped on current `main` and checked against the numbered statements. Volume 8’s expander chapter is the mismatch in V6-2. Volume 9 cites Proposition 12.1 and Theorem 12.2 for the generators and the first half of the fundamental domain, and still cites Volume 13, Theorem 17.1, for the boundary identification. Theorem 12.2(b) of this volume now proves that half as well. The Volume 9 pointer is not wrong, but it is no longer the only place the fact lives.

## 7. Plan, for scope only

Read against `docs/plan/book-06.md` and the Volume 6 section of the master plan (twelve chapters, three parts, numbering frozen). The book matches that shape. The fundamental domain has both halves. The bias identity is admitted. The transformation of \(\eta\) cites Volume 5. Maier is a remark. The proportions of zeros are quoted. Buchstab is not claimed as a theorem of the sieve chapter; a problem proves it for \(u\le 3\) and sends the rest to Volume 15. The catalog subtitle is *Arithmetic Meets Analysis*, and that is the subtitle on the title page.

The blueprint’s page target, 190–220, is not met. The interior print PDF has 299 pages. The extra length is the closing-problem list, which the chapter tells the reader they may skip.

## 8. Comparison with the earlier report

Written after the scores and the issue log above were committed (`a30616f9`). The earlier report is the draft pull request #205, `docs/review/volume6-independent-scored-read-2026-11-12.md`. The fix log is `docs/review/volume5-volume6-fixes-review-2026-11-12.md`, which records pull requests #208–#210. Each earlier issue was re-opened in the current source. “Fixed” means the defect described there is gone, and the new sentence was read.

| ID | Severity then | Now |
| --- | --- | --- |
| V6-01 | minor | Fixed. The primes to \(10^7\) are said to give eight digits, \(0.26149721\), and the next digit is said to move. The partial sum is \(0.2614972158\). |
| V6-02 | minor | Fixed. The remark after Theorem 5.7 says Exercise 7.3 proves one direction, and that the converse is quoted from Titchmarsh, Chapter 14. |
| V6-03 | minor | Fixed. The proof of Lemma 9.6 says the Taylor remainder is uniform for \(\lvert t\rvert\le A\), which is the hypothesis Volume 4 asks for. |
| V6-04 | minor | Fixed. Definition 10.1 builds the variables by successive splittings of \([0,1]\). |
| V6-05 | minor | Fixed. “Landscape” is gone from Chapter 12. |
| V6-06 | minor | Fixed in the sense asked. A section “Closing problems” follows Exercise 12.6, and the chapter says a reader may stop there. The list is still why the book is long. |
| V6-07 | minor | Fixed. About the Cover separates the proved Farey gaps from the quotation that ties a discrepancy to the Riemann hypothesis. |
| V6-08 | minor | Fixed. Volume 14 now cites Theorems 3.6, 3.8 and 5.2 for continuation and non-vanishing on \(\operatorname{Re}s=1\). |
| V6-09 | minor | Fixed. The Roth solution cites Theorem 8.4, with \(1+o(1)\). |
| V6-10 | minor | Fixed. The large-sieve chapter cites Volume 5, Proposition 10.2, for uniqueness of Dirichlet coefficients. |
| V6-11 | minor | Fixed. Volume 7’s problem chapter cites its own chapters for Borel–Cantelli, Baire, and Lebesgue density. It does not attribute them to Volume 6. |
| V6-12 | minor | Fixed. Volume 15 ties the constant that bears on Siegel zeros to the progression inequality of Exercise 8.4, and states the short-interval ratio \(2k\). |
| V6-13 | minor | Fixed. Volume 13 says the product, not Theorem 12.7, shows that \(\Delta\) has no zeros, and cites Theorem 12.9(c) for \(\dim M_4=1\). |
| V6-14 | minor | Not a defect. The vertical Stirling formula is printed as (6.1) on the reading PDF, page 102 of that file. Equations are numbered by chapter. The citation in Volume 14 was already right. The suggested change to equation (1) would have been a new error. The fix log left it, correctly. |
| V6-15 | minor | Fixed. Proposition 1.2(b) prints \(2\log 4\). |
| V6-16 | minor | Fixed. The write-up of the cycle exercise divides by \(n!\). |
| V6-17 | minor | Fixed. At \(x=10^9\) the solution says \(3.3\) with \(M\), and \(3.0\) for the main term alone. |
| V6-18 | minor | Fixed. The missing piece of \(\int e^{-u}\log u\,du\) over \((0,\delta\log 2)\) is estimated. |
| V6-19 | minor | Fixed. The caption says \(0.308\) is the difference of the two higher-power contributions. Recomputed, that difference to \(10^6\) is \(0.307\). |
| V6-20 | minor | Fixed. The race caption says the \(99.59\%\) is conditional, and the remark names the hypotheses. |
| V6-21 | minor | Fixed. The opening cites Theorem 2.4 for the product and the lower bound, and the paragraph after it for \(\pi(x)<\sqrt x+2\ln 4\cdot x/\ln x\). |
| V6-22 | minor | Fixed. The visible-point solution names Euclid’s lemma from Volume 2, Chapter 1. |
| V6-23 | minor | Fixed. Schur (1912) is existence; Murty (1988) is the converse. |
| V6-24 | minor | Fixed. The solution writes the reciprocity sign and the cancellation against \(\bigl(\frac{-1}{p}\bigr)\). |
| V6-25 | major | Fixed. The opening lists the product, the count, and the critical line. Infinitude is separated from the hypothesis and proved as a corollary. The years 1893 and 1905 match that order. |
| V6-26 | major | Fixed. The opening display is the formula for \(\psi_0\), with the symmetric limit, and it says the proof gives Corollary 7.6. The half-step \(\frac12\log p\) at a prime is stated. |
| V6-27 | minor | Fixed. The series is \(-\frac{L'}{L}(1,\chi_{-4})=-0.24561\). The closed form stays positive. |
| V6-28 | minor | Fixed. The solution says one \(\varepsilon\) gives only \(\beta\le\frac12+\varepsilon\), and the hypothesis for every \(\varepsilon\) gives \(\beta\le\frac12\). |
| V6-29 | minor | Fixed. Littlewood’s infinitude of lead changes is no longer said to rest on the conditional display. |
| V6-30 | minor | Fixed in the conclusion, with one leftover in the display. The sentence before the estimate uses \(\log(T+2)\), and the next sentence takes the ratio \(\log T/\log(T+2)\to 1\) and the factor \(\frac12\) before choosing \(c\). The aligned bound on the same page (`ch07-explicit.tex:243`) still writes \(e^{-c_1\log x/\log T}\). For a general \(T\ge 3\) that exponential is smaller than the one just proved; \(\log(T+2)<2\log T\) is what justifies a factor \(\frac12\), and that factor is restored before the theorem is stated. The error term \(xe^{-c\sqrt{\log x}}\) stands. |
| V6-31 | minor | Fixed. The sum is over \(\gamma\neq 0\), and the positive frequencies are named as such. |
| V6-32 | minor | Fixed. The caption says the ordinates are computed sign changes of \(Z(t)\). |
| V6-33 | minor | Fixed. The text says about \(11\%\) of the main term, and \(12\%\) of \(x/\log x\). |
| V6-34 | minor | Fixed. The range of \(m\) is the \(N+H-1\) integers from \(2-H\) to \(N\), and each \(z_n\) appears \(H\) times. |
| V6-35 | minor | Fixed. The Graham–Ringrose factors are restored. The remark stays quoted. |
| V6-36 | minor | Fixed. Proposition 6.7 is cited for the standard normal, and \(sZ\) supplies the variance. |
| V6-37 | minor | Fixed. The odd harmonic sum is written as \(\frac12\log Y+O(1)\). |
| V6-38 | minor | Fixed. Exercise 8.4 requires \(x/q\ge 3\), and says the factor is an asymptotic as \(x/q\to\infty\). |
| V6-39 | minor | Fixed. That exercise uses \(\log\). |
| V6-40 | minor | Fixed. The solution says the model and the primes disagree, and that Maier’s theorem is quoted. |
| V6-41 | minor | Fixed. Montgomery–Vaughan, the sharp large-sieve constant, Baker–Harman–Pintz, and the 2018 gap bound sit in remarks. |
| V6-42 | minor | Fixed. The opening says Ramanujan proved the congruence, and that multiplicativity and the bound were conjectures. |
| V6-43 | minor | Fixed. The two solutions, and the central-binomial solution beside them, take a finite sum up to a fixed \(K\) and then a tail. |

The fix log’s verdicts match this table, with one qualification. V6-30 is fixed as a theorem: the constant \(c\) is chosen after the ratio of the logarithms is absorbed. The intermediate display still has the old denominator \(\log T\). V6-14 is the one place the earlier report itself was wrong, and the fix log said so.

Two further sentences in Chapter 7, both low, were not in that log. At `ch07-explicit.tex:352`, “that density is a consequence of the formula above” attaches the Rubinstein–Sarnak density for \(\pi(x;4,3)-\pi(x;4,1)\) to the conditional approximation for the \(\theta\)-race. The hypotheses are named in the same paragraph; the passage from \(\theta\) to \(\pi\) is not. In the solution of the bias exercise (`ch07-explicit.tex:491`), “oscillations of the same size without a preferred sign” does not follow from the unconditional prime-power identity. The identity, the handicap \(\sqrt x\), and the four numerical values at \(10^6\) are right. Neither sentence changes a numbered theorem, so they stay out of the score.

**Nothing found that the fixes introduced.** The repaired sentences that were re-read — the constant \(2\log 4\), the division by \(n!\), \(\psi_0\) in the opening display, the range of \(m\) in van der Corput’s inequality, the sign of \(L'/L\), and the tail split in the closing problems — say what the repairs claimed. The zero-free repair put \(\log(T+2)\) in the sentence and in the choice of \(c\), and left \(\log T\) in the display between them. That is an incomplete edit, not a new false theorem.

**What the earlier report and the fix log did not record.** These are the issues in the log above. They are not regressions of the November fixes.

- V6-1. The letter \(\tau\) is the divisor function in Chapter 2 and Ramanujan’s function in Chapter 12, with no warning. The earlier report checked both theorems and did not flag the clash.
- V6-2. Volume 8’s expander chapter still cites Chapter 5 for an error \(O(\sqrt x\log x)\) under the Riemann hypothesis. The downstream fix corrected V6-08 through V6-13 and did not touch this sentence. Chapter 5 says it gives no error term.
- V6-3. The blurb and the KDP text still say the \(4n+3\) primes lead most of the time, and that every theorem is proved in full. The earlier report repaired About the Cover (V6-07) and the race caption (V6-20). It did not read the jacket against the conditional density.
- V6-4. The index is a selective list. The earlier report did not ask whether Theorem 12.2 or the congruence modulo \(691\) can be found from it. The page numbers that are printed were checked here and are right.
- V6-5. The last page of Chapter 12 names the zero-free region, Selberg’s sieve, and Weyl sums as where Volume 14 starts. Those are theorems of this volume. Volume 14’s preface describes a different starting point.
- V6-6. Lemma 9.6’s box still does not say that \(m_k\) are the Gaussian moments defined above it. V6-03 fixed the dominated-convergence step. The box was left as a general implication, which it is not.
- V6-9 and V6-10. The Piltz error after the \(\tau_3\) theorem is stated as if it were proved here, and the mod-\(4\) remark says the square correction and the conditional error are the same size. Neither was in the earlier log. A second reading of those two paragraphs is what put them in.

The earlier report was the more thorough pass on exercise solutions in Chapters 5–12. This re-read confirms that those repairs hold, and does not repeat a line-by-line audit of every closing-problem solution. The two major defects it found, the misnamed Riemann hypothesis and the explicit formula written for \(\psi\) instead of \(\psi_0\), are repaired.
