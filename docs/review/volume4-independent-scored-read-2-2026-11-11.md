# Volume 4, *Chance: The Logic of Uncertainty* — independent scored read 2

**Referee report, 11 November 2026.** Read against `main` at `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f` and the GitHub release `books` of the same day (print PDF, reading PDF, EPUB). The comparison with the earlier scored read is a later section of this file and was written only after the scorecard and issue log below were committed.

The intended reader is the one named in the preface: a motivated reader who has finished Volumes 1–3, with proofs that are supposed to use only high-school mathematics and Volume 1. Scores are 0–10. A 10 is reserved for work that would not embarrass Feller’s Volume I, Grimmett–Stirzaker, Durrett, or Tao on the same point. Numerical checks are not proofs; they are listed separately from the arguments that were read.

Printed folios below are those of `Volume.4.-.Chance.-.Print.pdf`. On the pages that were checked, the printed folio is the PDF page number minus 12 (PDF page 14 is printed page 2; PDF page 282 is printed page 270).

## How this was read

Source files under `volume4-chance/` that `main.tex` inputs, including `chapters/ch05-geometric.tex`. Figures were opened when a caption made a numerical or geometric claim, and several were compared with the print PDF. Volume 1’s `main.tex` was used to fix chapter numbers (the language chapter is Chapter 0, calculus is Chapter 8, inequalities Chapter 9, probability Chapter 10). Specific Volume 1 passages were opened only to test citations that the Volume 4 text treats as premises. Downstream citations of Volume 4 labels were sampled in Volumes 5, 11, 12 and 15, not read as books.

Classical statements were checked against the sources named in the “Sources consulted” section, and against direct recomputation. No earlier Volume 4 review, handoff, plan file, or Volume 4 pull-request discussion was opened before the scorecard and issue log were committed.

## Scorecard

Dimensions: **(a)** correctness, **(b)** rigor, **(c)** prerequisite discipline, **(d)** clarity, **(e)** pedagogy, **(f)** exercises, **(g)** figures, **(h)** voice, **(i)** notation, **(j)** layout as rendered.

| Chapter | a | b | c | d | e | f | g | h | i | j |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 Games to probability spaces | 9 | 8 | 9 | 8 | 9 | 9 | 8 | 9 | 9 | 9 |
| 2 Random variables and laws | 9 | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 9 | 8 |
| 3 Generating functions | 9 | 8 | 9 | 7 | 8 | 8 | 8 | 8 | 9 | 8 |
| 4 Concentration and laws of large numbers | 9 | 8 | 8 | 8 | 9 | 8 | 8 | 8 | 9 | 8 |
| 5 Continuous chance | 9 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 |
| 6 Why the bell curve appears | 9 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 9 | 8 |
| 7 Entropy, codes, typical sequences | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 9 | 8 |
| 8 Random walks | 9 | 8 | 8 | 8 | 9 | 7 | 8 | 8 | 9 | 8 |
| 9 Markov chains and mixing | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 9 | 8 |
| 10 The Poisson clock | 8 | 7 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 11 Martingales | 8 | 8 | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 8 |
| 12 Brownian motion | 8 | 5 | 7 | 7 | 7 | 7 | 7 | 8 | 7 | 8 |
| 13 The probabilistic method | 9 | 8 | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 8 |
| 14 Random graphs | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| B Extremal problems and Ramsey theory | 8 | 6 | 8 | 7 | 7 | 7 | 8 | 8 | 8 | 8 |

Exercise scores from Chapter 7 onward are not certificates of every solution. The solutions that were recomputed are named under “Verified correct”. The rest are listed under “Not reviewed”, and those `(f)` scores are capped for that reason.

### Chapter notes

**Chapter 1.** The ballot count, the Catalan bijection, the Tuesday-boy count \(13/27\), the \(n\)-door host, Penney’s HHH-against-THH race, and the pairwise-dice example were checked and are right. Bertrand’s pages in the *Comptes Rendus* match the 1887 notes. The outer-content arguments for infinite heads and for the end of Penney’s game stay inside the cylinders they name. The boy-or-girl pointing paragraph is correct and harder than it needs to be: “the pointed boy is the older child” is not “the older child is a boy”, and the text does say so, but a reader who knows the \(1/2\) variant will have to read it twice. Layout of the chapter opener (printed p. 2) is clean.

**Chapter 2.** The Poisson limit, the cycle mean \(1/k\), \(H_{52}\), the coupon mean and variance, the empty-box identities, quicksort’s \(2(n+1)H_n-4n\), and the prisoners’ \(1-(H_{100}-H_{50})=0.31182\ldots\) were recomputed. The fixed-point Poisson limit uses Volume 1’s derangement series and the bound \(|D_n/n!-e^{-1}|\le 1/(n+1)!\), which is in Volume 1’s probability chapter. The phrase “union bound in Chapter 1” (issue V4R2-02) points at a tool Chapter 1 never names.

**Chapter 3.** Extinction as the smallest root of \(s=f(s)\), the binary and critical examples, the cobweb values \(11/32\), \(809/2048\), \(11/16\), \(809/1024\), the Catalan equation, and the first-passage probability \(\min(1,p/q)\) check. The term-by-term derivative of a probability generating function is written with a dominated tail, which is the right standard and a steep hill for the stated reader. That is why clarity is 7, not because the argument is wrong.

**Chapter 4.** Hoeffding’s \(1/8\), the exponent \(-2t^2/\sum(b_i-a_i)^2\), Chebyshev’s \(1/40\), \(e^{-20}=2.061\ldots\times 10^{-9}\), \((0.371)^{20}=2.440\ldots\times 10^{-9}\), the binomial tail \(1.364\ldots\times 10^{-10}\) (about fifteen times smaller than Hoeffding), \(D(0.6\|1/2)=0.020135\ldots\), and the Bernstein value \(3/16\) were recomputed. Kolmogorov’s three-step check \(1/2\le 3/4\) is right. The bounded strong law’s gap estimate and Bernstein’s Weierstrass proof close. The figure label \(0.188\) is the disclosed rounding of \(0.1875\), and on printed p. 69 it sits clear of the curves.

**Chapter 5.** Gaussian mean \(0\), variance \(1\), tail \(\int_x^\infty e^{-t^2/2}\,dt\le x^{-1}e^{-x^2/2}\), Buffon’s \(2\ell/(\pi d)\), Bertrand’s \(1/3\), \(1/2\), \(1/4\), order-statistic density and mean \(k/(n+1)\), and the Cantor series were checked. Box–Muller’s Jacobian cancellation is right. The rectangle-probability argument that follows is long, and the factors \(9\) and \(18\) in the boundary cover were not re-derived from a grid drawing; they are arranged so that the error tends to \(0\). Rigor is 7 because that cover was not audited line by line, not because a false identity was found.

**Chapter 6.** Dice variance \(35/12\), standard deviation \(\sqrt{3500/12}\approx 17.078\), \(z=\sqrt{60/7}\), and the chain proving \(\phi(x)/x<0.002\) all hold, and the text is explicit that \(0.002\) does not bound the dice. Hoeffding’s \(e^{-2}\) for the dice does. The local theorem’s constant \(\sqrt{2/(\pi n)}\) matches the usual lattice form, and the Stirling expansion’s \(\delta^2\) coefficient was recomputed. The smooth cutoff \(q(u)=1-35u^4+84u^5-70u^6+20u^7\) has vanishing derivatives through order \(3\) at \(0\) and \(1\). \(P(H\ge 60)\) for a hundred fair tosses is \(0.02844\ldots\), and \(1-\Phi(1.9)=0.02872\ldots\). \(\mathbb E|Z|^3=2\sqrt{2/\pi}\). The Bernoulli representation of the number of cycles is the standard insertion coupling and is proved. Lindeberg’s general replacement was read at the third-moment bound and at the passage from smooth tests to distribution functions, not at every clipping estimate.

**Chapter 7.** Gibbs, Kraft, Shannon’s \(H\le L<H+1\), the chain rule, relative entropy, and the Huffman merge were read. The dyadic tree has entropy and mean length \(7/4\). For masses \(1/2,1/3,1/6\) the Shannon length is \(5/3\), the Huffman length is \(3/2\), and the mutual-information example is strictly less than \(1/12\), as computed from \(3^{12}=531441>524288=2^{19}\). The Chebyshev guarantee \(n\ge 89\) for the coin of heads probability \(1/10\) at tolerance \(1/2\) is a correct sufficient bound.

**Chapter 8.** Reflection, fair and biased ruin, the figure values \(1/5\) and \(16/31\), Pólya’s one- and two-dimensional reductions, the arcsine identities \(P(L_{2n}=2k)=u_{2k}u_{2n-2k}\) and the limit \((2/\pi)(\arcsin\sqrt b-\arcsin\sqrt a)\), and the central-binomial lower bound’s role were checked. The three-and-higher-dimensional estimate is the right Gaussian bound \((4\pi d/n)^{d/2}\). The constants \(A\) and \(B\) in the biased ruin formula are not written out (issue V4R2-03). The \(d\)-dimensional integral is used before an iterated-integral sentence is given (issue V4R2-04).

**Chapter 9.** The three-state matrix, \(\pi=(2/7,3/7,2/7)\), \(P^2(1,3)=1/6\), and total variation \(2/7\) from the start at state \(1\) check. Top-to-random, the Bayer–Diaconis probabilities, and the total-variation distances for \(52\) cards were recomputed from the Eulerian numbers. Rounded to three decimals they are \(1.000\) (four times), \(0.924\), \(0.614\), \(0.334\), \(0.167\), \(0.085\), \(0.043\), matching both the text and Bayer–Diaconis, *Ann. Appl. Probab.* 2 (1992), Table 1. The \(k=4\) value before rounding is \(0.9999995334\), so the warning that \(d_k<1\) is right. The rising-sequence mean \((n+1)/2\) and the Chebyshev window \(20\) to \(33\) for \(n=52\) check: \(53/675<0.079\).

**Chapter 10.** Memorylessness, the exponential moments \(k!/\lambda^k\), the Poisson probabilities, and the colouring lemma were read and are the standard facts. The joint density on the simplex is obtained by one-variable substitutions rather than a cited change-of-variables theorem. The rest of the chapter, including M/M/1 and the exercises, was not recomputed line by line, which caps (a), (b) and (f).

**Chapter 11.** Optional stopping for a bounded time is the right martingale identity, and the first hit of \(+1\) is a genuine counter-example to dropping the bound: the ruin comparison gives \(P(\tau=\infty)\le 1/(N+1)\). The two extra sufficient conditions are proved by returning to \(\tau\wedge n\). The monkey argument stops at a bounded time and uses the deterministic bound \(11\cdot 26^{11}\). Later exercises were not all recomputed.

**Chapter 12.** The Lévy midpoint formula has the Brownian-bridge variance \(2^{-(n+1)}\), and the threshold arithmetic \(a_n^2/(2\sigma^2)=2n\) is right, so the union bound is \(O(2^n e^{-2n})\). The citation of the Borel–Cantelli lemma for those normal thresholds does not meet the lemma’s hypotheses (issue V4R2-01). The reflection proof then equates the two halves \(\{B_t<a\}\) and \(\{B_t>a\}\) by pointing at a compact-box estimate that was written for continuous test functions (issue V4R2-10). The classical identities are the right ones. Those two unfinished steps are why rigor is 5. The covariance \(\min(s,t)\) for centred independent Gaussian increments is correct. Quadratic variation does write the rectangle pullback before Chebyshev. The restart proposition, from the dyadic times \(\tau_n\) onward, does pass bounded continuous test functions; the one-sentence claim for a fixed time just above that argument does not.

**Chapter 13.** The symmetric local lemma is in the form \(ep(d+1)\le 1\), and the bound \(e<3\) is proved from \(n!\ge 2^{n-1}\) with a strict step at \(n=3\). The crossing inequality \(\operatorname{cr}(G)\ge m^3/(64n^2)\) for \(m\ge 4n\) is the standard deletion-plus-sampling bound, and \(190^3/(64\cdot 400)=267+119/128\), hence \(\operatorname{cr}(K_{20})\ge 268\), is exact. Turán’s twin-class argument in Appendix B was read; the rest of the appendix’s exercises were not.

**Chapter 14.** The subcritical bound was checked through \(\rho=ce^{1-c}\) and the special case \(c=1/2\), where \(e^{1/2}<7/4\) is deduced from the Chapter 13 bound \(e<3\) and from \((7/4)^2>3\). The chapter does not claim a giant-component theorem; it says the survival probability is a candidate and that the limit of the fraction is not proved. That matches the promise at the end of Chapter 3. The triangle second-moment argument was read through the covariance cases. Its exercises were not recomputed.

**Appendix B.** The opening says it is lettered B, and the counter is set that way in `main.tex`. Turán’s \(T(6,2)\) counts, \(9\) against \(8\), match the figure. The index entries B.1 through B.7 match the numbered theorems. The finite van der Waerden induction is a real proof. The word “Equivalently” in front of the infinite form is not: only the finite-to-infinite direction is proved (issue V4R2-11). The complementary-pair solution is right for \(k\ge 2\) and, at \(k=1\), the construction is exactly the stars (issue V4R2-12). Euler’s formula for a connected plane graph says each new edge is drawn inside a face and does not say why both ends lie on one face (issue V4R2-13). Ramsey, Schur, the sunflower, and the Erdős–Ko–Rado argument itself were not re-proved line by line.

### Whole-book scores

| Item | Score | Why |
| --- | ---: | --- |
| Structure and arc | 8 | Four parts do the job the preface names: a sample space, limit theorems, processes, then existence proofs that use randomness. Entropy sits in the second part rather than with coding as a separate book, which is a reasonable choice. Appendix B is a combinatorics appendix after the probabilistic method, and the letter B with no A is explained in the appendix itself. |
| Continuity with Volumes 1–3 | 8 | Volume 1 chapter numbers used as premises match `volume1-first-principles/main.tex`. The derangement error, Chebyshev, the Poisson masses, \(1-x\le e^{-x}\), and the Gaussian integral are in the chapters cited. The preface’s claim that no proof cites a theorem of Volume 2 or Volume 3 survived the passes that were made; permutations are built from counting, not from a citation of the symmetry volume. |
| Preparation for Volumes 5–15 | 8 | The shared theorem counter reproduces every index number that was checked, including Lindeberg as Theorem 6.10, the classical CLT as Corollary 6.11, inversion as Theorem 6.8, Gaussian vectors as Theorem 6.14, the arcsine limit as Theorem 8.8, and reflection of Brownian motion as Theorem 12.12. Volume 11’s citations of Theorems 8.6 and 8.8, Volume 12’s citation of Theorem 6.14, and Volume 5’s Exercises 1.7, 2.3, 2.6, 2.7, 3.7 and 6.5 point at the statements those labels have. One tools-line gloss is loose (issue V4R2-06). |
| Delivery of the title and subtitle | 9 | The subtitle is earned. Sample spaces are fixed before fractions, and the book keeps saying which approximation is not a bound. The bell curve, the quincunx, and the strong law are the same moral told three ways. |
| Front and back matter, index, bibliography | 7 | The preface is a model of the house voice and states the prerequisite contract. The bibliography entries that were checked (Bertrand, André, Bayer–Diaconis, Galton’s quincunx dates) are real. The index is accurate and is not a page index: thirty-odd names point at theorem numbers. `kdp.md` is a little more rhetorical than the interior. |
| Print PDF | 9 | The release print file has 299 pages, every page \(513\times 738\) pt, PDF 1.3, empty metadata, and no outline. No text word came within 4 pt of the media box. The Part I opener is charcoal to the sampled edges. The chapter opener, the Galton photograph, the Bernstein figure, and Appendix B were inspected and are readable. |
| EPUB | 8 | The release EPUB is about 19 MB. Plates are PNG, almost all 1800 pixels wide, with `width:100%` and `height:auto`. Inline mathematics carries an em width and an em `vertical-align`. No SVG plates were present. It was not read on a Paperwhite. |

### Overall

**8/10.**

The book is a serious elementary probability course that, on the arguments and numbers checked here, tells the truth and usually shows the step. It is not flawless, and it is not yet something to hand a reader as finished in the Brownian chapter. The existence proof calls the Borel–Cantelli lemma for events outside the class the lemma was given, and the reflection proof treats half-line indicators as if they were the continuous test functions of the restart argument. The later chapters are also harder than the preface’s audience sentence suggests, even though the missing theorems (Lévy’s continuity theorem, Itô’s formula, a general Fubini theorem, uniform integrability) are named and, in the proofs that were read, not used as steps.

I would recommend the book to the reader the preface describes after that citation is repaired and after the reflection limit in Theorem 12.12 is written for the indicators, not only for continuous test functions. I would not recommend it as-is.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V4R2-01 | `volume4-chance/chapters/ch11-brownian.tex:63-66`, Theorem 12.4, printed p. 230 | rigor | major | The existence proof bounds level-\(n\) midpoint displacements by a normal threshold \(a_n\) and invokes Theorem 4.4(a). That lemma is stated for events that are finite unions of half-open intervals in the Chapter 1 digit model. A normal threshold of a coordinate built from infinitely many bits is not such a union, and the proof does not reduce it to one. The Gaussian tail and the union bound \(O(2^n e^{-2n})\) are themselves in order: \(\sigma^2=2^{-(n+1)}\) and \(a_n^2/(2\sigma^2)=2n\). | Before citing Theorem 4.4, record that each threshold is a pair of intervals in its own uniform coordinate, that those sets are squeezed by the cylinder argument of Proposition 5.6, and that countable subadditivity applies to those covers. Alternatively prove the Borel–Cantelli half again for this class. |
| V4R2-02 | `volume4-chance/chapters/ch02-discrete.tex:110`, printed p. 22 | citation | minor | The boundary case \(np_n\to 0\) uses “the union bound in Chapter 1”. Chapter 1 proves inclusion–exclusion for three events and countable subadditivity of outer content. It does not name a finite union bound. The inequality \(P(\text{some success})\le np_n\) is true by the finite additivity Volume 1 supplies. | Point at Volume 1’s finite additivity, or state the finite union bound once in Chapter 1. |
| V4R2-03 | `volume4-chance/chapters/ch07-walks.tex:81`, Theorem 8.2, printed p. 157 | rigor | minor | After the characteristic equation \(pr^2-r+q=0\), the proof says the general solution is \(A+B(q/p)^k\) and that the boundary values fix \(A\) and \(B\). The displayed formula is the right one, and the figure’s \(16/31\) matches it at \(p=2/3\), \(N=5\), \(k=1\). The two lines that produce \(A\) and \(B\) are not written. | Solve \(h_0=0\) and \(h_N=1\) in three lines. |
| V4R2-04 | `volume4-chance/chapters/ch07-walks.tex:205-208`, Theorem 8.5 | rigor | minor | For \(d\ge 3\) the return probability is an integral of \(\phi(\theta)^n\) over \([-\pi,\pi]^d\). Proposition 5.4 is Fubini on a rectangle. The proof treats the cube integral as already defined. Iterating the one-variable integral of a continuous function would close it; that sentence is missing. Chapter 10 is more careful: the gamma-density lemma refuses to cite the rectangle proposition in dimension \(n\ge 3\). | One sentence: integrate one coordinate at a time. |
| V4R2-05 | `volume4-chance/chapters/ch04-inequalities.tex:391`, sources of Chapter 4, printed p. 73 | bibliography | minor | Shannon’s 1948 paper is listed among the sources of the concentration chapter. That chapter does not use entropy. Chapter 7 cites the same paper for the quantity it defines. | Drop the Shannon item from Chapter 4’s list, and leave it on Chapter 7. |
| V4R2-06 | `volume5-calculation/chapters/ch12-agm.tex:1028` (downstream of this book) | cross-volume citation | minor | A tools line sends the reader to “Volume 4, Chapter 8 (periodic chains)”. Chapter 8 is the walk chapter. The period of an irreducible chain is defined in Chapter 9, and the cycle \(1\to 2\to\cdots\to n\to 1\) is Exercise 9.9. The calculation in that Volume 5 solution uses independence from Chapter 2, which is the right pointer; the parenthetical “periodic chains” is not. | Retarget the parenthetical to Chapter 9, or delete it if the solution does not use it. |
| V4R2-07 | `volume4-chance/about-the-cover.tex:6`, printed p. 287; cover of the reading PDF | figures | minor | The colophon’s dates match the sources consulted: the machine was built in 1873, shown at the Royal Institution on 27 February 1874, and described in *Natural Inheritance* (1889). Stigler records 17 pin rows on the 1873 machine. The sentence “Twelve rows of pins” describes this cover, which is a computed drawing, and the next sentence calls the drawing Galton’s quincunx. A reader can take the twelve rows as a count of the historical machine. | Say that the drawing has twelve rows and that Galton’s 1873 machine is a different object with more rows. |
| V4R2-08 | `volume4-chance/chapters/index.tex`, printed pp. 285–286 | back matter | minor | Every index number that was checked against the shared theorem counter is right, from Theorem 1.7 through Theorem B.7. The index has no page numbers and only the named theorems. A reader who remembers “coupon collector” finds Theorem 2.5; a reader who remembers a word that is not on the list does not. | Keep the theorem numbers and add page numbers, or say in the preface that the list is a theorem finder rather than an index. |
| V4R2-09 | `volume4-chance/kdp.md:3-9` | voice | minor | The listing names the law of large numbers, the central limit theorem, walks, Markov chains, Poisson processes, martingales, Brownian motion and the probabilistic method, which is what a blurb should do. “Climbs to the theorems” and “a drunk bird may get lost forever” are louder than the interior. The interior itself does not use the banned house-voice phrases. The same paragraph attaches “Prussian cavalry kicked by horses” to Poisson processes. Those counts are the Poisson distribution of rare events, not a point process on the line. | Bring the listing down to the register of `blurb.tex`. Name the horse-kick counts as the Poisson law, and keep the process for the clock and the queue. |
| V4R2-10 | `volume4-chance/chapters/ch11-brownian.tex:296-298`, Theorem 12.12, printed p. 239 | rigor | major | On \(\{\tau_n=s\}\) the increment \(B_t-B_s\) is symmetric about \(0\), so \(B_t\) is symmetric about \(B_s\), not about \(a\). Continuity gives \(B_{\tau_n}\to a\), but \(B_{\tau_n}\ne a\) at finite \(n\). The proof equates \(\{B_t<a\}\) and \(\{B_t>a\}\) “with the same compact-box estimate” as Proposition 12.11. That estimate is for a bounded continuous function of the increment vector. The half-line indicators are discontinuous, and the window of width \(2|B_{\tau_n}-a|\) is not estimated. The conclusions \(P(M_t\ge a)=2(1-\Phi(a/\sqrt t))\), the hitting density, and \(\mathbb E[\tau_a]=\infty\) are the classical ones. From the dyadic times \(\tau_n\) onward, Proposition 12.11 itself does pass bounded continuous test functions. | Bound \(P(\tau_a\le t,\, B_t<a)-P(\tau_a\le t,\, B_t>a)\) by the probability that \(B_t\) falls between \(a\) and the reflection of that threshold through \(B_{\tau_n}\), and send \(n\to\infty\). |
| V4R2-11 | `volume4-chance/chapters/extremal.tex:131`, Theorem B.7, printed p. 275 | correctness | minor | The finite van der Waerden statement is proved by the induction that follows. “Equivalently” also claims the converse of the infinite form. The proof’s first paragraph shows only that the finite statement implies the infinite one: one colour is reused for infinitely many lengths. The converse needs a compactness argument that is not given. | Delete “Equivalently” and say that the infinite form follows from the finite one. |
| V4R2-12 | `volume4-chance/chapters/extremal.tex:227`, solution of the complementary-pair exercise, printed p. 279 | correctness | minor | For \(n=2k\) the count \(\tfrac12\binom{2k}{k}=\binom{2k-1}{k-1}\) is right, and for \(k\ge 2\) the construction is not a star. For \(k=1\) the same construction is exactly the two stars, each of size \(1\). The sentence says the construction gives many maximum intersecting families besides the stars, with no restriction on \(k\). | Restrict the non-uniqueness sentence to \(k\ge 2\). |
| V4R2-13 | `volume4-chance/chapters/ch12-method.tex:141`, Proposition 13.5, printed p. 253 | rigor | minor | A tree is given one face, and each added edge is said to split a face. The identity \(v-e+f=2\) and the later bound \(e\le 3v-6\), including the disconnected case, then follow. The write-up does not say why the new edge’s endpoints lie on the boundary of a single face of the embedding already drawn. | One sentence: in the current plane graph the two ends lie on one face, and the edge is drawn in that face. |
| V4R2-14 | `volume4-chance/chapters/ch10-martingales.tex:306`, Theorem 11.13, printed p. 222 | rigor | minor | \(M_n\) is uniform on the \(n+1\) points \(\{1/(n+2),\ldots,(n+1)/(n+2)\}\), so \(\mathbb E[g(M_n)]=(1/(n+1))\sum g(k/(n+2))\). That is \((n+2)/(n+1)\) times a Riemann sum of mesh \(1/(n+2)\) that omits an interval of width \(1/(n+2)\). Both factors tend to \(1\), so the limit \(\int_0^1 g\) is right. The distribution-function count in the next sentences identifies the uniform law without this sentence. \(\mathbb E[M_n]=1/2\) and \(\mathbb E[M_n^2]=(2n+3)/(6(n+2))\to 1/3\). | Write the factor \((n+2)/(n+1)\), or rely on the counting argument already in the proof. |
| V4R2-15 | `volume4-chance/chapters/ch11-brownian.tex:279`, Proposition 12.11 | notation | minor | The deterministic bound on the test function is named \(B\) in a proof where \(B\) is the process. | Call the bound \(\beta\). |
| V4R2-16 | `volume4-chance/chapters/ch11-brownian.tex:12` | citation | minor | “The normal distribution of Chapter 6” points at the central limit theorem. The density, the tail, and Box–Muller are in Chapter 5. Later citations of those labels still resolve. | Point at Chapter 5 for the law. |

No critical issue: nothing checked here is a false theorem whose repair would change a stated constant, a distribution, or a limit. Two proofs do not reach the sentence they treat as the last step. Those are V4R2-01 and V4R2-10. The stated conclusions of both are the classical ones.

## Verified correct

These were read and, where a number appears, recomputed. A check of a number is not a check of the surrounding proof; both are marked.

**Front matter.** Preface coin \(2^{-n}\); prerequisite paragraph; four-part map. Blurb’s list of theorems against the chapter titles. About the Cover dates against Stigler (2010) and the 1874 Royal Institution lecture. `kdp.md` against the contents. Bibliography items 1–4 against Bertrand’s note (CR 105 (1887), 369), André’s note (same volume, 436–437), and Renault’s account that André’s bijection is not the geometric reflection.

**Chapter 1.** Definition of the doubling map; \(u=5/8=0.101_2\); Proposition 1.2; outer content and subadditivity; the run-of-heads example; Proposition 1.6; Theorem 1.7, including the binomial algebra and the check \(a=2,b=1\); the inclusion–exclusion example \(7/8\); both boy-girl counts, including the pointing model; the \(n\)-door calculation; Exercises 1.1–1.8 and their solutions, including \(22/365=0.06027\ldots\), \(365\ln 2=252.9987\ldots\), \(12/(52\cdot 51)=1/221\), and the Catalan identity.

**Chapter 2.** Poisson limit proof; binomial and Poisson masses at \(n=20,p=1/10\), \(k=0\): \(0.12158\) and \(0.13534\); the integral bounds for \((0.98)^{100}\) and the gap \(0.00272\) against the upper bound \(0.00282\); cycle mean; \(H_{52}=4.538\ldots\) inside \(\ln 53\) and \(1+\ln 52\); coupon mean and variance, including the checks at \(n=2\) and \(n=3\); empty boxes; quicksort solution; prisoners, \(H_{100}-H_{50}=0.68817\ldots\); factorial moments of the Poisson law; reservoir sampling; the sum of independent Poissons.

**Chapter 3.** Generating-function derivative and mean propositions, read through; the random-sum numerical example \(11/16\), \(1/4\), \(1/16\); extinction theorem, including the critical and supercritical cases and the one-child exception; Examples 3.9 and 3.10; Catalan recurrence and generating function; thinning; first-passage solution; the binomial-series solution; the near-critical Poisson branching asymptotic \(\rho\sim 2(c-1)\), as an expansion, not as a numerical table.

**Chapter 4.** Hoeffding’s lemma, including the identity for \(L''\); Hoeffding’s inequality; the fair-coin numbers in the first two examples; Kolmogorov’s inequality and the eight-outcome check; both Borel–Cantelli halves and the repeated-digit counter-example; the bounded strong law; Bernstein’s proof of Weierstrass and the value \(3/16\); the run-length solution; the other five exercise solutions at the level of their displayed algebra.

**Chapter 5.** Density of \(\sqrt U\); Gaussian moments and tail; exponential mean; continuous Fubini on a rectangle; polar area element; independent uniforms; order statistics of two and of \(n\) samples; inverse distribution function; dominated convergence for continuous integrands; Box–Muller up to the Jacobian identity (the boundary-cover constants were not re-derived); Bertrand’s three models; Buffon’s needle; the nine exercise solutions in the chapter.

**Chapter 6.** Opening dice arithmetic; the inequality chain for \(\phi(x)/x\); \(P(H\ge 60)\), \(1-\Phi(2)\), \(1-\Phi(1.9)\); local theorem constant and the \(\delta\)-expansion; cycle-to-Bernoulli proposition; Gaussian-vector characteristic function and the rotation argument, read once; third-moment example and Exercise 6.7; the Cauchy characteristic function \(e^{-|t|}\) in the solution of the Cauchy exercise, read once; Exercise 6.5’s conclusion \(1/2\). The cutoff polynomial’s derivatives were checked with a direct expansion.

**Chapter 7.** Entropy arithmetic for \(p=1/10\); Gibbs; the two-toss typical set; Kraft; Shannon; the dyadic tree; the \(1/2,1/3,1/6\) comparison; chain rule; relative entropy; mutual information, including \(I<1/12\); Huffman’s induction, read once.

**Chapter 8.** Reflection theorem and the height list in the caption of the reflection figure; ruin probabilities and \(16/31\); fair duration \(k(N-k)\) as the stated formula; Pólya in dimensions \(1\) and \(2\), and the Gaussian integral in dimension \(d\ge 3\); last-visit theorem, including \(f_{2m}=u_{2m}/(2m-1)\) and the \(n=2\) count \(3/8,1/4,3/8\); arcsine limit as a Riemann-sum argument.

**Chapter 9.** Three-state example; period lemma; the Bayer–Diaconis formula and the \(52\)-card distances, recomputed from the Eulerian triangle (the sum of the Eulerian numbers is \(52!\)); top-to-random’s coupon bound; the untouched-card lower bound’s algebra \(1-6/\mathbb E[U_t]\).

**Chapter 10.** Memorylessness; exponential moments; Poisson counts at rate \(1\), \(t=1\); colouring lemma’s multinomial cancellation.

**Chapter 11.** Definitions of conditional expectation were not all re-audited. Optional stopping, the first-win counter-example, the two extra hypotheses, and the bounded-time step in the monkey theorem were read. Pólya’s urn is a martingale on the interval partitions, the colour probabilities \(1/(n+1)\) are right, and the limit is uniform by the counting argument. The Riemann-sum sentence for \(\mathbb E[g(M_n)]\) omits the factor \((n+2)/(n+1)\) (issue V4R2-14). The limit still holds.

**Chapter 12.** Covariance proposition; midpoint variance; the threshold \(a_n\); the \(L^2\) half of quadratic variation, including the rectangle pullback and Chebyshev; the restart argument from the dyadic times \(\tau_n\), including the continuous test functions; the reflection identities as classical statements, not as a finished limit. The Borel–Cantelli citation and the indicator limit are the issues above, not verified applications. The hitting density’s differentiation and the divergence of \(\mathbb E[\tau_a]\) were checked as calculus, given the distribution function.

**Chapter 13.** The bound \(e<3\); the crossing-number arithmetic; the Euler inequality for a possibly disconnected plane graph, including the case split on component sizes. The connected induction assumes a new edge splits a face; that geometric step is the minor issue above.

**Chapter 14.** Subcritical first-moment bound and the \(c=1/2\) estimate \(n(7/8)^{k-1}\); the triangle covariances for disjoint edges and for an edge in common.

**Index.** The shared counter (theorem, proposition, lemma, corollary, definition, example) was run on every file `main.tex` inputs, in order. Each index line matches that numbering. Exercise numbers 1.7, 2.3, 2.6, 2.7, 3.7 and 6.5 match the downstream calls that were looked up.

**Production.** Print PDF geometry, metadata, and a sample of pages (cover of the reading PDF, print pp. 2, 69, 103, 230’s PDF page, 270, 285, and the Part I opener). EPUB stylesheet, absence of SVG plates, plate pixel widths, and the em baseline on the first chapter’s formulas. All 107 exercise environments in the input chapters have a matching hint and a matching solution; there are no duplicate exercise labels. `gilmer.tex` is not input.

**Volume 1 checks used as premises.** Chapter order. Derangement series and the alternating bound \(1/(n+1)!\). Chebyshev and the Poisson masses in the probability chapter. The three-label coin picture in that chapter, which Chapter 1 of this book reuses. Rearrangement is in the inequalities chapter.

## Not reviewed

- Line-by-line reading of every estimate inside Lindeberg’s replacement (Chapter 6), past the third-moment bound, the smooth cutoff, and the passage to distribution functions.
- The Box–Muller boundary cover’s numerical factors, past the Jacobian identity and the fact that the errors are sent to \(0\).
- Most exercise solutions in Chapters 7–14 and Appendix B. The statements were seen when they sat next to a theorem that was read; the write-ups were not recomputed.
- Markov-chain convergence and coupling from the end of the existence proof onward; stationary existence was read through the Cesàro argument’s first display only.
- M/M/1, inspection, thinning, and superposition beyond the colouring lemma.
- Martingale upcrossings, the \(L^2\) theorem, Pólya’s urn, and almost-sure convergence, beyond the optional-stopping block.
- Nowhere differentiability of Brownian paths, beyond the statement. Quadratic variation and the reflection principle were read after the first scorecard; the reflection gap is V4R2-10, and the \(L^2\) half of quadratic variation includes the rectangle pullback before Chebyshev.
- Ramsey, Schur, the sunflower, Erdős–Ko–Rado, and van der Waerden in Appendix B, beyond Turán and the index numbers.
- `volume4-chance/chapters/gilmer.tex`. It is not in `main.tex` and not in the released PDF. It was not reviewed as part of the book.
- The notebooks under `python/volume4/`. The preface does not send the reader to them, and they are not part of the printed book.
- A Paperwhite reading of the EPUB. The file was inspected structurally.
- Every Volume 1 citation. Only the ones used as a premise in an argument under review were opened.
- Volumes 5–15 except for the label checks named above.
- A physical copy of Feller, Grimmett–Stirzaker, Durrett, or Tao. Calibration used those books as the standard they are, and the classical checks used the papers and translations named below.

## Sources consulted

- J. Bertrand, Solution d’un problème, *Comptes Rendus* 105 (1887), 369, English text at `webspace.ship.edu/msrenault/ballotproblem/EnglishBertrand.pdf`.
- D. André, Solution directe du problème résolu par M. Bertrand, *Comptes Rendus* 105 (1887), 436–437, English text on the same site. André’s bijection is not a geometric reflection; the book’s historical sentence agrees with that translation and with M. Renault, *Amer. Math. Monthly* 115 (2008), as described on Renault’s ballot-problem page.
- D. Bayer and P. Diaconis, Trailing the dovetail shuffle to its lair, *Ann. Appl. Probab.* 2 (1992), Table 1, from the copy at `stat.berkeley.edu/~aldous/157/Papers/bayer_diaconis.pdf`. The distances \(1.000,1.000,1.000,1.000,0.924,0.614,0.334,0.167,0.085,0.043\) are that table.
- S. M. Stigler, Darwin, Galton and the Statistical Enlightenment, *Statistical Science* 25 (2010), on the 1873 machine, the 1874 Royal Institution lecture, and 17 pin rows; Galton, *Natural Inheritance* (1889), for the description of the quincunx.
- Volume 1 of this series, as cited above, for the premises this volume says it uses.
- Direct recomputation in Python (`math`, `lgamma`, exact Eulerian numbers, integer binomial coefficients) for every decimal named in “Verified correct”.

## Comparison with the earlier scored read

This section was written after the scorecard and the issue log above were committed, in `9b0b4684`. The file compared is `docs/review/volume4-independent-scored-read-2026-11-11.md`. Its scorecard and issue log judge the book before the repairs in its Final status table. That table says V4-01 through V4-23 were repaired on `main`. The scores in this report are of `8b8a5be3`, which already contains those repairs. The comparison is therefore between a pre-repair scorecard and a post-repair reading, not between two readings of one unchanged text.

### Scores, dimension by dimension

Overall: 7 then, 8 now.

| Chapter | Earlier a–j | This reading a–j | What moved |
| --- | --- | --- | --- |
| 1 | 9 8 9 8 8 9 8 9 9 8 | 9 8 9 8 9 9 8 9 9 9 | Pedagogy and layout up one. The same proofs. |
| 2 | 9 8 9 8 8 8 8 9 9 8 | 9 8 8 8 9 8 8 9 9 8 | Prerequisites down one for the unnamed “union bound in Chapter 1”. Pedagogy up one. |
| 3 | 9 8 8 8 8 8 8 8 8 8 | 9 8 9 7 8 8 8 8 9 8 | Prerequisites and notation up, because the undefined \(S_N\) is gone. Clarity down one: the generating-function derivative is still a steep proof. |
| 4 | 9 8 9 8 8 8 8 8 8 8 | 9 8 8 8 9 8 8 8 9 8 | Notation up. Prerequisites down one against their 9; the digit-model warning is honest, and I did not give 9. |
| 5 | 8 6 8 7 7 8 8 8 8 8 | 9 7 8 7 8 8 8 8 8 8 | Correctness and rigor up. The rectangle cover that was V4-03 is now written. |
| 6 | 8 5 6 6 7 7 8 8 8 7 | 9 7 8 7 8 8 8 8 9 8 | The largest rise. Rigor was 5 because the product of characteristic functions and the Lindeberg swap did not close. Both arguments are now on the page. Prerequisites were 6 because Exercise 6.2 used Volume 1’s weak law outside that law’s finite-sum proof; the solution now uses Theorem 6.4 and a clipped square. |
| 7 | 8 8 8 8 8 8 8 8 8 8 | 9 8 8 8 8 7 8 8 9 8 | Correctness and notation up one. Exercises down one because I did not recompute every solution. |
| 8 | 9 7 8 7 8 8 8 8 8 8 | 9 8 8 8 9 7 8 8 9 8 | Rigor, clarity, pedagogy, and notation up. Exercises down one for the same coverage reason. |
| 9 | 8 7 8 8 8 8 8 8 8 8 | 9 8 8 8 8 7 8 8 9 8 | Correctness and rigor up. I recomputed the 52-card distances; that review did not. |
| 10 | 8 7 8 8 8 8 8 8 8 8 | 8 7 8 8 8 7 7 8 8 8 | Exercises and figures down one. I did not recompute M/M/1. |
| 11 | 8 7 8 7 8 8 8 8 8 8 | 8 8 8 7 8 7 7 8 8 8 | Rigor up one on the optional-stopping block. Exercises and figures down. |
| 12 | 8 7 8 7 7 7 7 8 8 8 | 8 5 7 7 7 7 7 8 7 8 | Rigor down by two. The Lévy construction’s call on Theorem 4.4 is V4R2-01, and the reflection limit is V4R2-10. That review did not line-check this construction. Notation down one because a deterministic bound is named \(B\) inside the proof. |
| 13 | 9 8 8 8 8 8 8 8 8 7 | 9 8 8 7 8 7 7 8 8 8 | Layout up. The full-page raster of the local-lemma page is gone. Clarity, exercises, and figures down one on coverage. |
| 14 | 8 7 8 8 8 7 7 8 8 8 | 8 8 8 8 8 7 7 8 8 8 | Rigor up one. The \(O(\log n)\) bridge is now what Theorem 14.1 proves. |
| B | 8 8 9 8 8 8 8 7 8 8 | 8 6 8 7 7 7 8 8 8 8 | Voice up: the appendix no longer apologises that there is no Appendix A. Rigor is 6 after a second look at Theorem B.7: “Equivalently” claims a converse that is not proved. |

Whole-book: structure 8 against 8; continuity 8 against 8; preparation 8 against 8; title 9 against 8; front and back matter 7 against 5; print PDF 9 against 8; EPUB 8 against 8. The front-matter rise is the index, the collected bibliography, and a listing that now says the same thing as the preface. Their print file had 291 pages and a raster text page at folio 248. The release I opened has 299 pages, and no page is a text page replaced by one large image.

### What that review missed

These are in the issue log above and are not in its issue log or its Final status table.

- **V4R2-01.** Theorem 12.4 cites Theorem 4.4(a) for normal thresholds. That review’s “Not reviewed” list says the Lévy construction was not line-checked.
- **V4R2-02.** “The union bound in Chapter 1” is not a named result of Chapter 1.
- **V4R2-03.** Biased ruin states \(A+B(q/p)^k\) and does not solve for \(A\) and \(B\).
- **V4R2-04.** The walk in dimension \(d\ge 3\) integrates over a cube. The Fubini proposition is for a rectangle, and the proof does not say to iterate.
- **V4R2-05.** Shannon’s 1948 paper is still among the sources of the concentration chapter, which does not use entropy. The collected bibliography copies that list, so the item appears twice in the book’s source apparatus, once in the wrong chapter.
- **V4R2-06.** A Volume 5 tools line says “Chapter 8 (periodic chains)”. Their script checked numbered citations and would not have caught a parenthetical. The period is defined in Chapter 9.
- **V4R2-09.** After the listing was brought into line with the preface, the remaining sentences (“climbs to the theorems”, “a drunk bird”) are still louder than `blurb.tex`. The horse-kick counts are attached to the Poisson process. That is a voice note, not the contradiction they repaired.
- **V4R2-10.** Theorem 12.12 passes a continuous-test-function estimate to the indicators \(\{B_t<a\}\) and \(\{B_t>a\}\). Same unread stretch of the Lévy construction as V4R2-01.
- **V4R2-11 and V4R2-12.** Theorem B.7 says “Equivalently” for a converse it does not prove. The complementary-pair solution is false at \(k=1\).
- **V4R2-13.** Euler’s formula does not say why both ends of a new edge lie on one face.
- **V4R2-14.** The Pólya-urn average is \((n+2)/(n+1)\) times a Riemann sum. The uniform limit is proved by counting and does not need the loose sentence.
- **V4R2-15 and V4R2-16.** A bound is named \(B\) in the Brownian proof, and the opening points at Chapter 6 for the normal law.

The quadratic-variation complaint does not stand. The \(L^2\) argument writes the rectangle pullback, the quantile maps, and Chebyshev’s bound \(2t\cdot 2^{-n}/\varepsilon^2\). From the dyadic times \(\tau_n\) on, the restart proposition does pass bounded continuous test functions. The gap is the reflection step that treats indicators as if they were those test functions.

V4R2-07 is not something they missed. They wrote that “twelve rows” describes the cover drawing, not the 1873 machine, and they did not call it an error. I still think the colophon should say that in one clause. V4R2-08 is the residual they already printed under V4-16: the index points at theorem numbers, not pages.

### Fixes marked closed

I re-opened each row of the Final status table in the current source.

| Finding | Still closed? |
| --- | --- |
| V4-01 | Yes. The product proposition factors bounded maps that are uniformly continuous on compact subintervals of \((0,1)\). Cosine and sine of a continuous quantile, including \(\Phi^{-1}\), are put in that class before they are multiplied. |
| V4-02 | Yes. The Lindeberg swap clips, replaces clips by dyadic steps, and writes the Lipschitz errors before \(m\to\infty\) and \(K\to\infty\). |
| V4-03 | Yes. Each side of the rectangle is cut into arc-length pieces and covered by \((r,\theta)\) squares. The factor \(9\) is still only an upper bound, which is the residual they named. The errors are sent to \(0\). |
| V4-04 | Yes. The solution of Exercise 6.2 uses Theorem 6.4 for the sample mean and Chebyshev on a clipped square. It does not call Volume 1’s weak law. |
| V4-05 | Yes. The preface, `blurb.tex`, and `kdp.md` all say that a proof step is in this volume or in Volume 1, and that a later theorem is named and not used. |
| V4-06 | Yes. The tail identity is \(Q^2-(Q^{(M)})^2=Q^2-M^2\). |
| V4-07 | Yes. The continuity correction is printed as \(0.02872\), without an ellipsis. The value \(0.02871655\ldots\) rounds to that. |
| V4-08 | Yes. \(G(0)\in\{0,1\}\) is derived, the law \(T=0\) is excluded, and \(G(1/q)=e^{-\lambda/q}\) is written before continuity. |
| V4-09 | Yes. The bridge talks about \(\{Z_n>0\}\). There is no \(S_N\). |
| V4-10 | Yes. The bridge says size \(O(\log n)\), and Chapter 14 does not claim more. |
| V4-11 | Yes. When \((1-\varepsilon)\log_2 n\) is an integer, the blocks are rerun at \(\varepsilon/2\). I checked that step; it does what it claims. |
| V4-12 | Yes. The countable case of Hoeffding cites the nonnegative double-sum principle of Volume 1, Chapter 10. |
| V4-13 | Yes. \(f(x)=\ln(1-x)+x+x^2\) has \(f'(x)=x(1-2x)/(1-x)\ge 0\) on \([0,1/2]\). |
| V4-14 | Yes. Outer content is an infimum of countable covers, and a tail of chosen ones is empty because a remainder lies in \([0,1)\). |
| V4-15 | Yes. The host is named as Volume 1’s door experiment, now with \(n\) doors. |
| V4-16 | Yes, with the residual they stated. There is a bibliography and an index of theorem numbers. There are still no page numbers. That residual is V4R2-08. |
| V4-17 | Yes. The appendix says it is lettered B, without the apology. |
| V4-18 | Yes. \((\varphi(t)e^{t^2/2})'=0\) and \(\varphi(0)=1\) are written. |
| V4-19 and V4-21 | Yes. Chapter 5 proves \(Q(u)\le x\) if and only if \(u\le F(x)\) from right-continuity, and Glivenko–Cantelli cites that identity and allows a flat stretch. |
| V4-20 | Yes. The release print file has 299 pages. No page is a text page replaced by one image larger than the text block. The intermediate count 291 is not the file I opened. |
| V4-22 | Yes. The ratio \(u_{2m}/u_{2m-2}\) includes the factor \(1/4\). |
| V4-23 | Yes. The maximum is said to meet the first boundary vertex, which may be either marked point, and both boundary values are 0. |

No row in that table is still open as a failed repair. I did not find a regression in the repaired sentences: the new run-length case, the clip identity, the host sentence, the \(O(\log n)\) bridge, and the product proposition’s hypotheses match the jobs they are given. The Shannon item in the concentration chapter’s source list was copied into the collected bibliography; that is a preserved mis-filing, not a new false theorem introduced by the repair.
