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
| 12 Brownian motion | 8 | 6 | 7 | 7 | 7 | 7 | 7 | 8 | 8 | 8 |
| 13 The probabilistic method | 9 | 8 | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 8 |
| 14 Random graphs | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| B Extremal problems and Ramsey theory | 8 | 7 | 8 | 7 | 7 | 7 | 8 | 8 | 8 | 8 |

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

**Chapter 12.** The Lévy midpoint formula has the Brownian-bridge variance \(2^{-(n+1)}\), and the threshold arithmetic \(a_n^2/(2\sigma^2)=2n\) is right, so the union bound is \(O(2^n e^{-2n})\). The citation of the Borel–Cantelli lemma for those normal thresholds does not meet the lemma’s hypotheses (issue V4R2-01). That is the lowest rigor score in the book. The covariance \(\min(s,t)\) for centred independent Gaussian increments is correct.

**Chapter 13.** The symmetric local lemma is in the form \(ep(d+1)\le 1\), and the bound \(e<3\) is proved from \(n!\ge 2^{n-1}\) with a strict step at \(n=3\). The crossing inequality \(\operatorname{cr}(G)\ge m^3/(64n^2)\) for \(m\ge 4n\) is the standard deletion-plus-sampling bound, and \(190^3/(64\cdot 400)=267+119/128\), hence \(\operatorname{cr}(K_{20})\ge 268\), is exact. Turán’s twin-class argument in Appendix B was read; the rest of the appendix’s exercises were not.

**Chapter 14.** The subcritical bound was checked through \(\rho=ce^{1-c}\) and the special case \(c=1/2\), where \(e^{1/2}<7/4\) is deduced from the Chapter 13 bound \(e<3\) and from \((7/4)^2>3\). The chapter does not claim a giant-component theorem; it says the survival probability is a candidate and that the limit of the fraction is not proved. That matches the promise at the end of Chapter 3. The triangle second-moment argument was read through the covariance cases. Its exercises were not recomputed.

**Appendix B.** The opening says it is lettered B, and the counter is set that way in `main.tex`. Turán’s \(T(6,2)\) counts, \(9\) against \(8\), match the figure. The index entries B.1 through B.7 match the numbered theorems. Ramsey, Schur, the sunflower, Erdős–Ko–Rado and van der Waerden were not re-proved line by line.

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

The book is a serious elementary probability course that, on the arguments and numbers checked here, tells the truth and usually shows the step. It is not flawless, and it is not yet something to hand a reader as finished at the Brownian existence proof: that proof calls the Borel–Cantelli lemma for events outside the class the lemma was given. The later chapters are also harder than the preface’s audience sentence suggests, even though the missing theorems (Lévy’s continuity theorem, Itô’s formula, a general Fubini theorem, uniform integrability) are named and, in the proofs that were read, not used as steps.

I would recommend the book to the reader the preface describes after that citation is repaired. I would not recommend it as-is.

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
| V4R2-09 | `volume4-chance/kdp.md:3-9` | voice | minor | The listing names the law of large numbers, the central limit theorem, walks, Markov chains, Poisson processes, martingales, Brownian motion and the probabilistic method, which is what a blurb should do. “Climbs to the theorems” and “a drunk bird may get lost forever” are louder than the interior. The interior itself does not use the banned house-voice phrases. | Bring the listing down to the register of `blurb.tex`, which already names the ballot theorem, Hoeffding, Pólya, and the probabilistic method in plain sentences. |

No critical issue: nothing checked here is a false theorem whose repair would change a stated constant, a distribution, or a limit.

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

**Chapter 11.** Definitions of conditional expectation were not all re-audited. Optional stopping, the first-win counter-example, the two extra hypotheses, and the bounded-time step in the monkey theorem were read.

**Chapter 12.** Covariance proposition; midpoint variance; the threshold \(a_n\). The Borel–Cantelli citation is the issue above, not a verified application.

**Chapter 13.** The bound \(e<3\); the crossing-number arithmetic; the Euler inequality for a possibly disconnected plane graph, including the case split on component sizes.

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
- Brownian quadratic variation, nowhere differentiability, and the reflection principle, beyond the existence and covariance propositions.
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

Reserved for the comparison written after this scorecard and issue log were committed.
