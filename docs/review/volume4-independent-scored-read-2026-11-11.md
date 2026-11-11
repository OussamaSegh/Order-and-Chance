# Volume 4 independent scored read

**Book.** *Order and Chance*, Volume 4, *Chance: The Logic of Uncertainty*, SEGHAIER Oussama, first edition, 2026.
**Source.** `main` at `2a86cafc` (11 November 2026), directory `volume4-chance`.
**Rendered copies.** GitHub release `books` (published 2026-11-10): `Volume.4.-.Chance.-.Print.pdf` (291 pages, 513 × 738 pt), `Volume.4.-.Chance.pdf` (292 pages, 504 × 720 pt), `Volume.4.-.Chance.epub` (19 MB).
**Reader assumed.** A motivated reader who has high-school mathematics and Volume 1, as the preface states.
**Calibration.** A 10 is a chapter I would hand a student in place of the corresponding part of Feller, Grimmett–Stirzaker, Durrett, or Tao, with nothing to repair. A proof that does not reach its stated conclusion cannot score above 6 on rigor, even when the statement is the right classical theorem.

Printed folios below are the arabic page numbers in the print PDF. In this build, print-PDF page index = printed folio + 12, from Chapter 1 (folio 2 is print-PDF page 14) through About the Cover (folio 279 is print-PDF page 291).

This file’s scores and issue log were written before any comparison with `docs/review/volume4-successor-review-2026-11-10.md`. The comparison is the last section.

## What the book is

`main.tex` builds fourteen chapters and one appendix.

| Printed | File | Title |
| --- | --- | --- |
| 1 | `ch01-counting.tex` | From Games to Probability Spaces |
| 2 | `ch02-discrete.tex` | Random Variables and Their Laws |
| 3 | `ch03-generating.tex` | Generating Functions and Random Families |
| 4 | `ch04-inequalities.tex` | Concentration and the Laws of Large Numbers |
| 5 | `ch05-continuous.tex` plus `ch05-geometric.tex` | Continuous Chance |
| 6 | `ch06-clt.tex` | Why the Bell Curve Appears |
| 7 | `ch07-entropy.tex` | Entropy, Codes and Typical Sequences |
| 8 | `ch07-walks.tex` | Random Walks |
| 9 | `ch08-markov.tex` | Markov Chains and Mixing |
| 10 | `ch09-poisson.tex` | The Poisson Clock |
| 11 | `ch10-martingales.tex` | Martingales and Fair Games |
| 12 | `ch11-brownian.tex` | Brownian Motion |
| 13 | `ch12-method.tex` | The Probabilistic Method |
| 14 | `ch14-graphs.tex` | Random Graphs and the Search for Structure |
| B | `extremal.tex` | Extremal Problems and Ramsey Theory |

`chapters/gilmer.tex` is not input. It is not part of the printed book.

There are 107 exercises. Each has a hint and a solution. I checked the label match with a script: no exercise lacks a hint or a solution, and no solution points at a missing exercise.

## Scorecard

Dimensions: (a) correctness, (b) rigor, (c) prerequisite discipline, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography as rendered.

| Chapter | a | b | c | d | e | f | g | h | i | j |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 Games to spaces | 9 | 8 | 9 | 8 | 8 | 9 | 8 | 9 | 9 | 8 |
| 2 Laws | 9 | 8 | 9 | 8 | 8 | 8 | 8 | 9 | 9 | 8 |
| 3 Generating functions | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 4 Concentration | 9 | 8 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 5 Continuous chance | 8 | 6 | 8 | 7 | 7 | 8 | 8 | 8 | 8 | 8 |
| 6 Bell curve | 8 | 5 | 6 | 6 | 7 | 7 | 8 | 8 | 8 | 7 |
| 7 Entropy | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 8 Random walks | 9 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 |
| 9 Markov chains | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 10 Poisson clock | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 11 Martingales | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 |
| 12 Brownian motion | 8 | 7 | 8 | 7 | 7 | 7 | 7 | 8 | 8 | 8 |
| 13 Probabilistic method | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 7 |
| 14 Random graphs | 8 | 7 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| Appendix B | 8 | 8 | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 |

### Chapter 1

(a) The ballot count is the classical \((a-b)/(a+b)\). I recomputed the binomial difference and the cases \(a=2,b=1\) and \(a=3,b=1\). The Tuesday-boy count is \(13/27\), the Penney race HHH against THH is \(1/8\), and the \(n\)-door host calculation gives \(1/n\) and \((n-1)/n\). Bertrand’s pages (CR 105 (1887), 369 and 436–437) and Renault, *Amer. Math. Monthly* 115 (2008), 358–363, match the citations I checked.
(b) Outer content is used as a countable cover, but Definition 1.3 does not say the cover is countable. The “infinitely many zeros” half of Proposition 1.6 argues about a set that the chosen expansion never produces.
(c) Volume 1, Chapters 9 and 10, are the right chapters for the tangent bound and for finite probability. I checked those chapter numbers against `volume1-first-principles/main.tex`.
(d) The host problem begins at line 206 with no sentence that names it. A reader who has not memorised Volume 1’s three doors has to guess the experiment.
(e) The coin-label trap, the ballot picture, and the Tuesday grid are in the right order. The infinite-sequence model is motivated by the preface’s endless tails.
(f) All eight solutions match the statements. The birthday comparison \(365\ln 2=252.9987\ldots\) and \(22/365=0.06027\ldots\) are right. The Catalan bijection agrees with the ballot theorem.
(g) `figures/ch01-ballot.tex` draws the dashed path first to \(+1\) and the solid path first to \(-1\), which is what the caption of Figure 1.2 says. I read that TikZ file. I did not redraw the digit or Tuesday plates.
(h) The voice is the series voice: short sentences, a named sample space, no stock opener.
(i) Cylinders, outer content, and strict leadership are used consistently after they are defined.
(j) The chapter opener (folio 2) and the ballot page (folio 7) are clean in the print PDF. Margins sit inside the trim.

### Chapter 2

(a) Poisson’s limit, \(H_{52}=4.53804\ldots\), the coupon mean \(nH_n\), the variance formula, fixed-point variance \(1\), quicksort \(2(n+1)H_n-4n\), and the prisoners’ success probability \(1-(H_{100}-H_{50})=0.31182\ldots\) all recomputed. The binomial mass at zero for \(n=20\), \(p=1/10\), is \(0.12158\), and \(e^{-2}=0.13534\), as the text says.
(b) The birthday-waiting solution is a real Riemann-sum argument and the limit \(\sqrt{\pi N/2}\) is the right one. The passage from a fixed window \(A\) to \(A\to\infty\) is written as a sketch of liminf and limsup, not as those words. The monotone-covariance factor \(2\) is asserted rather than expanded.
(c) Derangements are cited as Volume 1, Chapter 2, and the integral test as Chapter 3. Both numbers are right.
(d) The law-versus-variable distinction is taught on four coin outcomes before any limit. The birthday solution is harder than the star rating suggests, but it is still readable if the reader has the tail-sum identity.
(e) Cycles by hand on \(S_3\) (\(11/6=H_3\)) sit next to the general count. The coupon stages for three types add to \(11/2\).
(f) Eight solutions, including the reservoir induction and the Poisson factorial moments. I checked those two by hand.
(g) The Poisson-bar caption’s \(k=0\) values match a direct evaluation. I did not compare every bar height with a fresh plot.
(h) Same voice as Chapter 1.
(i) Geometric waiting is the trial of the first success, consistently.
(j) No layout fault found on the pages I opened in this chapter.

### Chapter 3

(a) Extinction is the smallest root of \(s=f(s)\), with the one-child law excluded, and the binary example at \(p=2/3\) gives \(\eta=1/2\). The Catalan generating function recovers \(C_n\). I read the extinction proof line by line.
(b) The sentence “so \(\eta_n=f(\eta_{n-1})\)” skips \(P(Z_n=0\mid Z_1=k)=\eta_{n-1}^k\). The rest of the fixed-point argument, including \(m=1\), is complete. The symbol \(S_N\) on line 251 is never defined.
(c) The exercise that writes \(\binom{-1/2}{j}\) uses a symbol the book has not defined. The solution’s falling product is the ordinary one and the identity checks.
(d) The cobweb and the three-child critical example earn their place. The bridge to Chapter 14 says every component “has order \(\log n\)”, which is stronger than Theorem 14.1’s \(O(\log n)\) upper bound.
(e) A family with mean \(4/3\) that still dies with probability \(1/2\) is the right surprise before the theorem.
(f) The eight solutions I spot-checked through the extinction and Poisson-sum identities are consistent with the statements. I did not recompute every coefficient in the binomial series exercise by hand; the ratio \(a_n/a_{n-1}=2(2n-1)/n\) is the standard one.
(g) I did not redraw the cobweb. The numerical cobweb values quoted in the source for the \(p=2/3\) iteration are consistent with iterating \(f\).
(h) Plain and concrete, with one undefined symbol in an exercise.
(i) The stray \(S_N\) is the notation fault.
(j) The extinction section (folio 47) is ordinary body text. No collision seen.

### Chapter 4

(a) Hoeffding’s constant \(e^{-2t^2/D}\) is the right one. For a fair coin, \(t=100\) and \(n=1000\) give \(e^{-20}=2.061\times 10^{-9}\). The exact tail \(\sum_{k\ge 600}\binom{1000}{k}2^{-1000}=1.364\times 10^{-10}\). Borel–Cantelli and the bounded strong law are the classical statements, with the finite-mean strong law correctly left to Volume 11.
(b) The moment-generating product is justified by “the finite sum that defines each expectation” (line 71) while the theorem allows a countable model. The nonnegative double-sum principle from Volume 1 would close it. The second Borel–Cantelli write-up stops the induction at the first complement.
(c) Markov and Chebyshev are Volume 1, Chapter 10. Weierstrass is Theorem 4.6, which is the number Volume 6 cites.
(d) The chapter keeps saying which bound is a proof and which number is only a limit. That is the right kind of clarity.
(e) Three fair steps make Kolmogorov’s inequality \(3/4\) against a probability \(1/2\). Bernstein’s \(3/16\) at \(n=4\) is exact.
(f) Exercise 4.6’s solution proves \(P(R_n<(1-\varepsilon)\log_2 n)\to 0\). Convergence in probability needs the closed event \(R_n\le(1-\varepsilon)\log_2 n\). When the threshold is an integer those differ by one atom. The result is true; the write-up misses the atom.
(g) I checked the Chernoff and Bernstein numbers in the text, not every plotted vertex.
(h) Direct, no filler.
(i) The two Borel–Cantelli halves are labelled, and the finite-cylinder warning is kept.
(j) Solutions around folio 72 are unbroken.

### Chapter 5

(a) Bertrand’s three probabilities \(1/3\), \(1/2\), \(1/4\) and Buffon’s \(2\ell/(\pi d)\) are the classical values. The Gaussian integral is taken from Volume 1, Chapter 8, which does contain \(\int_0^\infty e^{-u^2}\,du=\sqrt\pi/2\). Means of the min and max of two uniforms are \(1/3\) and \(2/3\).
(b) This is the first chapter whose main construction does not close. Theorem 5.10 computes the joint integral of a continuous test function, then says a test function is not yet a rectangle probability, and finishes by asserting that the curved boundary has covers of arbitrarily small \((r,\theta)\)-area. That covering is not proved. The generalised-inverse sentence at line 295 asserts \(Q(u)\le x\) if and only if \(u\le F(x)\) and does not prove it. Proposition 5.8 only treats a strictly increasing \(F\).
(c) Fubini is proved for continuous functions on a compact rectangle and is not pretended to be Tonelli. Volume 7 is named as the owner of the general theorem and is not used as a premise.
(d) Densities are motivated by area. The Box–Muller geometry is clear until the last paragraph of the proof.
(e) The tent that keeps area 1 is the right warning before dominated convergence.
(f) The nine exercises match their solutions in labels. The Cauchy and Cantor exercises are the right edge cases. I checked the Cantor lengths \((2/3)^n\) and the tent area \(1\).
(g) The polar-cell caption matches the area \((r\Delta r+\tfrac12(\Delta r)^2)\Delta\theta\) in the proof. I did not inspect every plate pixel by pixel.
(h) The voice holds. The Box–Muller proof gets denser than the surrounding prose.
(i) The letter \(a\) is both a radius and, elsewhere, a ballot count. The polar proposition warns the reader. Acceptable.
(j) Folio 88, where the rectangle step sits, is ordinary text. No overflow found.

### Chapter 6

(a) The statements are the right ones: fourth-moment strong law, Glivenko–Cantelli for a continuous distribution function, inversion when the characteristic function is integrable, Lindeberg’s condition, the classical CLT, the local de Moivre–Laplace formula at \(p=1/2\), and Slutsky’s lemma for a constant limit. One hundred dice have standard deviation \(\sqrt{3500/12}=17.078\ldots\), and \((400-350)\) is \(\sqrt{60/7}=2.9277\ldots\) standard deviations. \(P(H\ge 60)=0.0284439\ldots\) and \(1-\Phi(2)=0.022750\ldots\). The printed \(0.02872\ldots\) for \(1-\Phi(1.9)\) is a rounding; the value is \(0.02871655\ldots\), so the leading digits are \(0.02871\).
(b) Two proofs that the chapter needs do not reach their conclusions. Lines 221–225 state \(\varphi_{X+Y}=\varphi_X\varphi_Y\) for the Chapter 5 copies and cite Proposition 6.x (the unnumbered product proposition), whose hypotheses are monotone or finite-bit factors. Cosine and sine of \(tQ(u)\) are bounded and not monotone. The same factorisation is invoked for the joint Gaussian transform at lines 572–575. Lindeberg’s swap (lines 426–431) replaces \(f'(A)\) by a cylinder average and says the average exists as a Fubini integral on a large box. The errors from clipping, unread bits, and non-rectangular images are not estimated. Line 118 states \(Q^2-(Q^{(M)})^2=Q^2\) on \(\{|Q|>M\}\). The clip is \(\pm M\), so the difference is \(Q^2-M^2\). The limit used afterwards still goes to zero, because \(Q^2-M^2\le Q^2\). The normal transform’s ODE is solved without the integrating-factor line that would give uniqueness. Glivenko–Cantelli cites the strict inverse proposition for a theorem that assumes only continuity; the identity it needs is the generalised one, which is true and unproved.
(c) Lévy’s continuity theorem is named and left to Volume 11. That deferral is honest. The solution of Exercise 6.2 then quotes “Volume 1’s weak law” for the average of \(Y_i^2\). Volume 1’s weak law is Chebyshev for pairwise independent variables, and that chapter says its arguments use finite sums. A quantile with only a fourth moment is outside that proof. The fourth-moment strong law of this chapter would need an eighth moment of \(Y\). The limit is true. This solution does not prove it.
(d) The dice page is a model of how to talk about a limit. The Lindeberg proof is not something the intended reader can check.
(e) The warning that \(0.002\) is not a proved bound on a hundred dice, while \(e^{-2}\) is, is the best pedagogical paragraph in the chapter.
(f) Slutsky’s solution for a constant, including the sign change when \(c<0\), is complete. The confidence solution is not. The cycle CLT is a fair three-star use of Lindeberg once the smooth-test theorem is granted.
(g) The dice figure’s \(2.93\) matches \(\sqrt{60/7}\). The Galton photograph is credited in the caption and in `photos/CREDITS.md`.
(h) The prose around the examples is human. The proof prose is a compressed research argument.
(i) Modes of convergence are defined before they are used. The unnumbered product proposition is easy to confuse with a numbered one.
(j) Print folio 248 (Figure 13.1, which belongs to Chapter 13) is a single 4200 × 6000 image. The words are legible. They are no longer vector text. See issue V4-20.

### Chapter 7

(a) For a symbol of probability \(1/10\), \(H=\log_2 10-(9/5)\log_2 3=0.46899\ldots\), so “about \(0.469\)” is fair. The comparisons that avoid a calculator (\(8<10\), \(2^{10}>1000\), \(2^3<9\), \(2^8>243\)) are right. I did not re-expand every Huffman merge by hand. The lengths reported for the worked merge, \(107/36\) and \(107/72\), satisfy \(107/72<3/2<5/3\).
(b) Gibbs, Kraft, Shannon’s \(H\le L<H+1\), and the typical-set bounds are proved from the finite alphabet. I read the statements and the numerical checks, not every inequality line.
(c) Nothing here requires a later volume. Chebyshev is already in Volume 1.
(d) The biased coin’s wasted bits are a concrete opening.
(e) One coin, then blocks, then a code. That order is right.
(f) Six exercises, hints, and solutions match. The typical-count bound \(H-\varepsilon-1/n<\log_2|T_n|/n\le H+\varepsilon\) is the right shape.
(g) The prefix tree and the typical-coin plate are present in the EPUB at full width. I did not audit every label against the TikZ.
(h) Plain.
(i) Entropy is in bits, and the later natural-unit remark in Volume 15 is compatible with that choice.
(j) No fault seen on the pages I sampled from the surrounding chapters. I did not photograph an entropy page.

### Chapter 8

(a) Reflection, gambler’s ruin, Pólya’s theorem, and the arcsine limit are the classical theorems, and Theorem 8.8 is the arcsine limit that Volume 15 cites. The fair duration \(k(N-k)\) and the exit time \(R^2\) are right. I checked the first-return identity \(f_{2m}=u_{2m}/(2m-1)\) from the ballot count in the proof.
(b) Line 279 says the binomial ratio \(\binom{2m}{m}/\binom{2m-2}{m-1}=(4m-2)/m\) “gives” \(u_{2m-2}-u_{2m}=u_{2m}/(2m-1)\). The ratio is right, and so is the probability identity, but the powers of \(4\) contribute another factor \(1/4\). The uniqueness proof for harmonic functions says a path to \(a\) forces the boundary value. The first boundary vertex on that path might be \(b\). Both boundary values are zero, so the contradiction survives.
(c) The local theorem is this book’s Theorem 6.12, and the Fourier integral uses Volume 1’s Gaussian integral and Taylor remainder. I did not re-derive the three-dimensional Green-function estimate term by term.
(d) The one-dimensional pictures are clear. The higher-dimensional Fourier bound is a hard read, which is honest about what it is doing.
(e) Ruin is computed before it is abstracted. The electrical reading is an exercise, not a substitute for the probability.
(f) Eight exercises, with the ballot walk and the exit time tied to theorems that exist.
(g) The reflection caption’s path is the one the proof reflects. I did not remeasure every TikZ coordinate.
(h) Concrete, with a drunkard’s home only in the jacket copy, not as a substitute for Pólya.
(i) \(u_{2m}\) and \(f_{2m}\) stay distinct.
(j) Clean on the pages I opened.

### Chapter 9

(a) Stationary distribution, total variation, top-to-random, and the \(a\)-shuffle model are in place. Theorem 9.6 really does say that the total-variation distance is at most \(P(\tau>t)\), which is the fact later volumes quote. For \(n=3\), the mean \(11/2\) matches three geometric stages. I did not recompute the seven-shuffle distance \(0.334\) from the Bayer–Diaconis sum.
(b) Proposition 9.11 uses \(\ln(1-x)\ge -x-x^2\) on \([0,1/2]\). The inequality is true: \(f(x)=\ln(1-x)+x+x^2\) has \(f(0)=0\) and \(f'(x)=x(1-2x)/(1-x)\ge 0\) there. Chapter 2’s integral bound is the weaker \(\le x+2x^2\) and does not yield the coefficient \(1\). The derivative check is not in the proof.
(c) The sharp random-transposition window is named as a Volume 11 theorem and is not used. The coupon bound \(1-1/n\le e^{-1/n}\) is Volume 1, Chapter 10.
(d) The periodic Ehrenfest chain, whose distance stays \(1/2\), shows why aperiodicity is a hypothesis.
(e) Top-to-random is built as a coupon collector the reader has already proved. Riffle shuffles come after that, not before.
(f) Nine exercises. Random-to-top is Exercise 9.6, the number Volume 15 cites.
(g) The riffle figure says the distances are the exact finite sum. I did not replot it.
(h) Direct.
(i) Total variation is one half of \(\ell^1\), used consistently.
(j) Folio 184 is ordinary text.

### Chapter 10

(a) Memorylessness, thinning, superposition, the inspection paradox, Le Cam’s bound, and the M/M/1 mean \(\rho/(1-\rho)\) are the right theorems. At \(\rho=1/2,9/10,99/100\) the means are \(1,9,99\). The rate-\(1/10\) story (mean wait 10, mean covering gap 20) matches the length bias.
(b) Proposition 10.1 begins “\(G(0)=1\)”. From \(G(0)=G(0)^2\) one only gets \(G(0)\in\{0,1\}\). The law \(T=0\) almost surely is continuous, multiplicative, and finite, and it is not exponential. The hypothesis \(T>0\) can be read as ruling that law out, but the proof never says so. The gamma density on the simplex is derived by one-variable substitutions and does not pretend to be a general change of variables.
(c) Optional stopping is not used to compute the emptiness time. The text says the drift computation is one-step compensation. Volume 7’s Tonelli theorem is not a premise.
(d) The bus story at the opening is the right question, and the answer is the length bias rather than a slogan.
(e) Exponential, then the process, then the passenger, then the queue. That order teaches.
(f) Eight exercises. The Erlang mean \(2/\lambda\) and the conditional first-arrival mean \(t/(n+1)\) are right.
(g) The clock and queue figures are in the EPUB as full-width plates. I did not audit their labels.
(h) The opening is a person waiting for a bus. The proofs stay plain.
(i) Rate \(\lambda\) is used both as the exponential rate and as the Poisson rate, which is the point of the chapter.
(j) Folio 192 is ordinary text.

### Chapter 11

(a) Optional stopping is stated with three sufficient conditions, not as an unbounded slogan. The unit-gain martingale has infinite mean time. ABRACADABRA’s mean for a 26-letter alphabet is \(26^{11}+26^4+26=3670344487444778\), which is what the text computes from borders of lengths \(1\), \(4\), and \(11\). Fair-coin HT and HH have means \(4\) and \(6\). Pólya’s urn is uniform on \(\{0,\ldots,n\}\).
(b) I read the statements and the numerical checks. I did not re-expand every upcrossing inequality or the \(L^2\) maximal inequality line by line. The hypotheses I did read are the ones the applications use.
(c) Uniform integrability is left to Volume 11, in so many words, at the end of the \(L^2\) section. Theorem 11.12 is the finite-partition \(L^2\) theorem, which is what Volume 15 contrasts with the general filtration.
(d) The doubling strategy is a finite calculation before the theorem. That is clearer than starting from the definition.
(e) A stopped game the reader can count (16 paths) comes before Azuma and the pattern theorem.
(f) Five exercises, all solved. Fewer than the early chapters, and enough to cover stopping, Azuma, and a pattern.
(g) The upcrossing and Pólya plates are present. I did not count the twenty paths in the figure myself.
(h) Plain.
(i) Finite partitions are not quietly upgraded to continuous-time histories.
(j) No fault seen in the sample.

### Chapter 12

(a) Covariance \(\min(s,t)\), quadratic variation, the reflection principle, and the hitting-time tail are the standard facts. The text does not call the dyadic sum a stochastic integral. Volume 12 is named as the owner of Itô’s formula. I checked the two-step hedge \(4/3\) arithmetic as reported and the scaling \(T_a\stackrel{d}{=}a^2/B_1^2\).
(b) The Lévy construction and the strong-Markov approximation are long. I read the statements and the places where a later volume is deferred. I did not re-estimate every Gaussian tail in the existence proof.
(c) The deferrals are real. A reader is not told that this chapter contains Itô’s formula.
(d) Scaling and the nowhere-differentiable statement are motivated. The existence proof is the hardest stretch in the book after Lindeberg.
(e) The chapter knows it is a first construction, not a course on stochastic calculus.
(f) Seven exercises, including the bridge and the zero set. I did not re-solve each one.
(g) One reflection plate. Thin, for a chapter about paths.
(h) The prose keeps the limit of what was proved.
(i) Brownian motion is defined before the scaling properties.
(j) No separate layout fault found.

### Chapter 13

(a) Erdős’s Ramsey bound, the symmetric local lemma under \(ep(d+1)\le 1\), the second-moment bound, and the crossing lemma \(\operatorname{cr}(G)\ge m^3/(64n^2)\) for \(m\ge 4n\) are right. I checked the arithmetic: \(190^3/(64\cdot 400)=267+119/128\), so \(\operatorname{cr}(K_{20})\ge 268\). Three coins give \(\mathbb E[X^2]=3\) and ratio \(3/4\) against the truth \(7/8\). Euler’s inequality \(e\le 3v-6\) for a simple plane graph, connected or not, is proved, including the matching case.
(b) The crossing proof uses the weak deletion bound \(m-3n\), which is valid because \(m-(3n-6)\ge m-3n\) and a crossing number is nonnegative. The constant \(64\) comes out of \(p=4n/m\) correctly. The local-lemma numerical step \(e/4<3/4\) uses \(e<3\), which Volume 1’s series gives.
(c) Cauchy–Schwarz is Volume 1, Chapter 9. No later volume is a premise.
(d) Deletion and sampling are distinguished in a sentence after the \(K_{20}\) numbers. That sentence is needed, and it is there.
(e) A mean below 1, then a mean that stays constant, then a drawing. Good order.
(f) Exercise 13.4 is the crossing lemma later volumes cite, and the proposition in the text already proves the same bound. Six exercises, all solved.
(g) Figure 13.1, the complementary 5-cycles, is the right picture for \(R(3,3)=6\). I read the rendered page.
(h) Plain, and the five-cycle calculation is a check rather than a boast.
(i) Crossing number is a count of pairs, defined before the inequality.
(j) The page of Figure 13.1 is the rasterized print page. See V4-20.

### Chapter 14

(a) Theorem 14.1 is an \(O(\log n)\) upper bound for \(c<1\), not a giant-component theorem. The tree count \(k^{k-2}\) and the factor \(\rho=ce^{1-c}<1\) are right. Triangle means of order \(c^3/6\) are the standard first moment. I read the opening of the proof and the bound
\[
\mathbb E[N_k]\le\frac{n}{ck^2}(ce^{1-c})^k\exp(ck^2/n).
\]
(b) The exploration that controls components larger than \(n^{1/3}\) is part of the proof. I did not re-expand every branching-process comparison in the exercises.
(c) Extinction is Chapter 3’s theorem, already proved. The chapter does not import a later random-graph theorem.
(d) The opening states the \(c<1\) theorem in one sentence. The \(c>1\) direction is an exercise that asks only for a positive lower bound on one vertex, which matches what is proved.
(e) Existence in Chapter 13, typical structure here. The handoff to Volume 5 names the subtitle *From Formula to Insight*.
(f) Six exercises. The giant-component exercise is honestly a lower bound. A reader who wants the full phase transition will not find it, and the book does not pretend otherwise.
(g) One exploration plate. Enough for the branching picture, thin for the phase transition.
(h) Plain.
(i) \(G(n,p)\) is defined before the theorems.
(j) The chapter opener (folio 257) is a normal chapter page.

### Appendix B

(a) Turán’s theorem, Ramsey, Schur, the sunflower bound, Erdős–Ko–Rado, and van der Waerden are the right theorems. \(T(6,2)\) has \(9\) edges and the \(2\)–\(4\) split has \(8\). \(R(3,3)=6\). Theorem B.7 is van der Waerden, the number Volume 14 cites. I did not re-enumerate all \(512\) colourings of \(\{1,\ldots,9\}\).
(b) The arguments are counting arguments. The small Schur and van der Waerden cases are finite checks.
(c) The appendix says it does not use a later volume. The counting it uses is in this book and in Volume 1.
(d) The opening example is small enough to count.
(e) It is a genuine appendix: the main path does not depend on it, and later volumes can cite it.
(f) Five exercises, solved.
(g) The balance figure for \(T(6,2)\) matches the \(9\) against \(8\) count.
(h) The sentence “There is no Appendix A” is an editor speaking, not a teacher. The mathematics around it is fine.
(i) The numbers are B.1, B.2, …, as the text warns.
(j) Folio 268 is a clean chapter opener. The blank pages before Parts III and IV are intentional recto part pages. They are not faults.

## Whole-book scores

| Item | Score | Why |
| --- | ---: | --- |
| Structure and arc | 8 | Four parts, from a named sample space to a structure theorem, is a real arc. Chapter 14 is thinner than Chapter 13. The single appendix is lettered B. |
| Continuity with Volumes 1–3 | 8 | Proofs cite Volume 1 by the right chapter numbers and do not cite Volume 2 or 3 as premises. The preface’s claim that every step is in Volume 1 or here is stronger than Chapters 5 and 6. |
| Preparation for Volumes 5–15 | 8 | Seventy-one distinct citations of the form “Volume 4, Theorem/Proposition/Lemma/Corollary/Exercise/Definition \(n.k\)” all resolve to an item of that kind with that number. Spot-checks of Hoeffding (4.2), Borel–Cantelli (4.4), Weierstrass (4.6), Buffon (5.12), inversion (6.8), Lindeberg (6.10), Slutsky (Exercise 6.1), Gibbs (7.1), reflection (8.1), the arcsine limit (8.8), top-to-random (9.6), the crossing exercise (13.4), and van der Waerden (B.7) match the statements those later pages use. I did not re-read every later paragraph. |
| Title and subtitle | 8 | The book is about what a probability model licenses. Entropy, fair games, and existence proofs earn “the logic of uncertainty”. The bell curve is a limit, and the book sometimes remembers that. |
| Front matter, back matter, index, bibliography | 5 | The preface, the part pages, and About the Cover are real. Each chapter has a short source list, and the ballot and Galton citations I checked are accurate. There is no index and no collected bibliography. The KDP description contradicts the preface. |
| Print PDF | 8 | 291 pages, each \(7.125\times 10.25\) in, PDF 1.3, empty metadata, no annotations, embedded EB Garamond, Garamond-Math, Cormorant Garamond, and Fira Sans. Part openers are full-bleed charcoal. Folio 248 is a 600 ppi raster of a whole text page. |
| EPUB | 8 | 19 MB, under the 50 MB cap. Forty-one plates, each 1800 or 1801 pixels wide, with `width:100%` and `height:auto`. Inline mathematics carries an em width and an em `vertical-align`. No SVG plates. I did not read it on a Kindle. |

## Overall

**Score: 7 out of 10.**

This is a serious first course, written in the series voice, with complete solutions and with foundations that are often more careful than the jacket suggests. Chapters 1 through 4, the walk and shuffle chapters, and the probabilistic method are in good shape. The chapter the title promises, on why the bell curve appears, does not finish its two main arguments: multiplying characteristic functions of the continuous copies, and swapping one coordinate in Lindeberg’s proof. Those gaps sit under the preface’s sentence that every step is proved in this volume or in Volume 1.

I would not recommend the book as it stands. I would recommend it after the four mathematical repairs in V4-01 through V4-04, and after the jacket copy is made to agree with the preface.

## Issue log

Severity: **critical** means a false theorem a later chapter or a later volume would inherit as a falsehood; **major** means a stated proof does not reach its conclusion, or a reader-facing claim about the book is false; **minor** means a local slip whose repair is a sentence or two and whose conclusion survives.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V4-01 | `ch06-clt.tex:221–225` and `:572–575`; print folio about 110; unnumbered product proposition before Theorem 6.4, and Theorem 6.14 | Rigor | major | The product proposition factors a bounded monotone function, or a finite-bit function, of one uniform block. The text then says cosine and sine of \(tQ(u)\) are bounded, and concludes that characteristic functions of the Chapter 5 copies multiply. Boundedness is not the hypothesis. The same step produces \(\mathbb E\exp(it\cdot AZ)=\exp(-\tfrac12\|A^{\mathsf T}t\|^2)\). | Prove the product for a bounded uniformly continuous function of one block by dyadic steps, the way the bounded strong law already approximates a monotone function, and cite that lemma at both places. |
| V4-02 | `ch06-clt.tex:426–431`; print folio about 119; Theorem 6.10 | Rigor | major | Lindeberg’s proof says the cylinder average of \(H=f'(A)\) exists by Fubini on a large box and that the unread bits average to zero against the dyadic steps of the remaining uniform. The errors (clip, tails, non-rectangular image of \(A\)) are not estimated. The classical conclusion, Corollary 6.11, is reached only after this step. | Write the approximation with an explicit \(\varepsilon\): clip, freeze the first \(m\) digits, and bound the difference between \(H\) and its cylinder average before sending \(m\to\infty\). |
| V4-03 | `ch05-continuous.tex:345–349`; print folio 88; Theorem 5.10 | Rigor | major | After the test-function formula, the proof says a continuous \(q\) is not a rectangle probability, then asserts that the boundary of the \((r,\theta)\) region has covers of arbitrarily small area and concludes that \(X\) and \(Y\) are independent standard normals. | Prove that a finite union of smooth curves in the \((r,\theta)\) rectangle has content zero, or obtain the rectangle probabilities from the test-function formula by the same cutoff argument the chapter already uses for disks. |
| V4-04 | `ch06-clt.tex:696–703`; print folio about 129; solution of Exercise 6.2 | Prerequisites | major | The solution says a finite fourth moment makes \(Y_i^2\) eligible for Volume 1’s weak law. Volume 1’s weak law (`ch09-probability.tex`, the weak-law theorem) is Chebyshev, and that chapter says its proofs use finite sums. The fourth-moment strong law here would need \(\mathbb E[Y_1^8]\). | Prove Markov’s inequality from the integral definition in Chapter 5, then Chebyshev for the average of \(Y_i^2\). The sample mean itself already converges almost surely by Theorem 6.4. |
| V4-05 | `preface.tex:26`; `blurb.tex:1`; `kdp.md:7` | Front matter | major | The preface and the blurb say every step used in a proof is proved in this volume or in Volume 1. The KDP description says some measure-theoretic foundations are labelled and proved in a later volume. Chapters 5 and 6 do not meet the preface, and they do not label the missing steps as deferred. | Pick one contract. Either close V4-01 through V4-04, or name those steps as deferred and make the preface, the blurb, and `kdp.md` say the same thing. |
| V4-06 | `ch06-clt.tex:118`; inside the unnumbered product proposition | Correctness of a proof line | minor | On \(\{\|Q\|>M\}\) the clip is \(\pm M\), so \(Q^2-(Q^{(M)})^2=Q^2-M^2\), not \(Q^2\). The integral of the difference still tends to 0. | Replace the equality by \(0\le Q^2-(Q^{(M)})^2\le Q^2\). |
| V4-07 | `ch06-clt.tex:406`; print folio 118 | Numerical | minor | \(1-\Phi(1.9)=0.02871655\ldots\). The text prints \(0.02872\ldots\). The same paragraph’s \(0.02275\ldots\) and \(0.02844\ldots\) are truncated leading digits, so the ellipsis here is a different convention. | Print \(0.02872\), without the ellipsis, or print \(0.02871\ldots\). |
| V4-08 | `ch09-poisson.tex:17–20`; print folio 192; Proposition 10.1 | Rigor | minor | \(G(0)=G(0)^2\), so \(G(0)\in\{0,1\}\). The law \(T=0\) almost surely satisfies the written hypotheses if “\(T>0\)” is only a name, and it is not exponential. | Say that \(T>0\) almost surely forces \(G(0)=1\), and exclude \(G(0)=0\). |
| V4-09 | `ch03-generating.tex:251`; print folio 47 | Notation | minor | The sentence mentions events \(\{S_N>k\}\). No \(S_N\) is defined in the chapter. | Delete the symbol, or define it. |
| V4-10 | `ch03-generating.tex:253` | Cross-reference | minor | “Every component has order \(\log n\)” is stronger than Theorem 14.1, which is an upper bound of \(A\log n\). Isolated vertices have size 1. | Say “size \(O(\log n\)”. |
| V4-11 | `ch04-inequalities.tex:371–380`; print folio about 72; solution of Exercise 4.6 | Rigor | minor | The lower tail proved is \(P(R_n<s)\to 0\) with \(s=\lceil(1-\varepsilon)\log_2 n\rceil\). If \((1-\varepsilon)\log_2 n\) is an integer, convergence in probability still needs \(P(R_n=s)\to 0\). | Run the same block estimate at threshold \(\lfloor(1-\varepsilon/2)\log_2 n\rfloor\), or note that a single integer in the far lower tail has probability going to 0. |
| V4-12 | `ch04-inequalities.tex:71`; Theorem 4.2 | Rigor | minor | The product of moment generating functions is justified by expanding “the finite sum that defines each expectation”, while the theorem allows a countable model. | Cite the nonnegative double-sum principle from Volume 1, Chapter 10. |
| V4-13 | `ch08-markov.tex:314`; print folio about 184; Proposition 9.11 | Rigor | minor | \(\ln(1-x)\ge -x-x^2\) on \([0,1/2]\) is used and not proved. It is true, and Chapter 2’s bound does not imply it. | Add the derivative check of \(f(x)=\ln(1-x)+x+x^2\). |
| V4-14 | `ch01-counting.tex:84–86` and `:107–112`; print folio 3; Definition 1.3 and Proposition 1.6 | Rigor | minor | Outer content is an infimum of sums, without the word “countable”. The second half of the infinitely-many-digits proof describes the dyadic rationals, which the chosen expansion writes with a tail of zeros. | Say the covers are countable. Say the chosen expansion never ends in all ones, so the bad set for zeros is empty. |
| V4-15 | `ch01-counting.tex:206`; print folio about 10 | Clarity | minor | The \(n\)-door host appears with no name and no sentence linking it to the Tuesday-boy discussion. | One sentence: this is the host who opens doors, the experiment of Volume 1’s three doors, now with \(n\) doors. |
| V4-16 | `main.tex` has no index and no bibliography; the print PDF has neither word | Back matter | minor | Sources are per chapter. A 279-page book with 107 exercises has no index. | Add an index of theorems and a merged source list. Do not invent page numbers for journals. |
| V4-17 | `extremal.tex:9` and `main.tex:46`; print folio 268 | Structure | minor | `\setcounter{chapter}{1}` after `\appendix` makes the only appendix print as Appendix B. The text tells the reader there is no Appendix A. Later volumes cite Appendix B, so the letter is load-bearing. | Leave the letter if later volumes already depend on it. The sentence in the book can say “the appendix is lettered B” without the apology. |
| V4-18 | `ch06-clt.tex:240`; Proposition 6.7 | Rigor | minor | \(\varphi'(t)=-t\varphi(t)\) with \(\varphi(0)=1\) is said to have the solution \(e^{-t^2/2}\). Uniqueness is the integrating factor \((\varphi(t)e^{t^2/2})'=0\), which the inversion proof writes later for a different integral. | Add that one line here. |
| V4-19 | `ch06-clt.tex:181`; Theorem 6.5 | Prerequisites | minor | Glivenko–Cantelli assumes a continuous distribution function and cites the strict-increase inverse proposition. A flat stretch is outside that proposition. The indicator identity for the generalised inverse is what the proof uses, and line 295 asserts it without a proof. | Prove the generalised-inverse identity in Chapter 5 and cite that sentence. |
| V4-20 | Print folio 248 (print-PDF page 260); Figure 13.1 | Typography | minor | The page is one DeviceRGB image, 4200 × 6000 pixels, about 590 ppi. Text does not extract. The render is legible: the 5-cycles, the star sum \(7/4\), and Theorem 13.3 are there. It is the transparency flatten of a page that contains a figure. | Keep the figure opaque so the text around it stays vector, or accept a single raster page and say so in the production notes. |
| V4-21 | `ch05-continuous.tex:295` | Rigor | minor | “Right-continuity gives \(Q(u)\le x\) exactly when \(u\le F(x)\)” is stated, not proved. | Two lines: if \(F(x)<u\), right-continuity keeps \(F\) below \(u\) on a short interval to the right of \(x\), so the infimum exceeds \(x\). |
| V4-22 | `ch07-walks.tex:279`; Theorem 8.6 | Rigor | minor | The binomial ratio equals \((4m-2)/m\). The probability ratio \(u_{2m}/u_{2m-2}\) also divides by 4. The identity \(u_{2m-2}-u_{2m}=u_{2m}/(2m-1)\) is true after that factor. | Point at the factor \(1/4\) already used when \(u_{2m}\) is defined. |
| V4-23 | `ch07-walks.tex:309`; Proposition 8.7 | Rigor | minor | “Repeating along a path to \(a\) forces \(d(a)=M\).” The mean-value property stops at the first boundary vertex, which may be \(b\). Both boundary values are 0, so uniqueness stands. | Say the first boundary vertex on the path equals \(M\), and both boundary values are 0. |

No critical issue. Five major, eighteen minor.

## Verified correct

These are checks I did, or numerical evaluations I ran. A numerical check is not a proof. Where a subagent read a stretch, I still opened the cited lines before putting the point in the issue log or in this list.

**Recomputed.**

- \(H_{52}=4.53804\ldots\), \(\ln 53=3.97029\ldots\), \(1+\ln 52=4.95124\ldots\).
- \(22/365=0.06027\ldots\), and \(365\ln 2=252.9987\ldots\), so \(253/365>\ln 2\).
- \(H_{100}-H_{50}=0.68817\ldots\), success probability \(0.31182\ldots\).
- \((0.9)^{20}=0.12158\), \(e^{-2}=0.13534\).
- \((0.98)^{100}=0.13262\), and the printed bounds \(e^{-2.02083}<(0.98)^{100}<e^{-2.02}\) hold. The explicit gap bound at \(\lambda=2\), \(n=100\), is \(0.00282\), and the gap is \(0.00272\).
- \(e^{-20}=2.061\times 10^{-9}\). The upper binomial tail from 600 to 1000 out of 1000 fair trials is \(1.364\times 10^{-10}\).
- One hundred dice: variance \(3500/12\), standard deviation \(17.078\ldots\), threshold \(400\) at \(\sqrt{60/7}=2.9277\ldots\).
- \(P(H\ge 60)\) for a fair hundred tosses is \(0.02844\ldots\); \(1-\Phi(2)=0.02275\ldots\); \(1-\Phi(1.9)=0.02872\) to five decimals, not as a truncation.
- Quicksort at \(n=2\) is one comparison; the formula \(2(n+1)H_n-4n\) gives \(1\). At \(n=3\) it gives \(8/3\).
- Fixed-point variance: \(n\) variances sum to \(1-1/n\), and the covariances sum to \(1/n\).
- Coupon variance at \(n=2\) is \(2\), and at \(n=3\) is \(27/4\).
- Ballot algebra: \(\binom{n-1}{a-1}-\binom{n-1}{a}=(k/n)\binom{n}{a}\).
- Catalan: \(\frac1{2n+1}\binom{2n+1}{n}=\frac1{n+1}\binom{2n}{n}\).
- Aces: \((4/52)(3/51)=1/221\), and \(3/51=1/17\).
- Entropy \(\log_2 10-(9/5)\log_2 3=0.46899\ldots\).
- Crossing: \(190^2=36100\), \(36100\cdot 190=6859000\), \(25600\cdot 267=6835200\), remainder \(119/128\).
- Ramsey alteration: \(\binom{33}{7}/2^{20}=4.074\ldots\), so some colouring of \(K_{33}\) has at most four monochromatic \(K_7\)’s and at least 29 vertices remain.
- \(\binom{27}{7}=888030<2^{20}=1048576<\binom{28}{7}=1184040\).
- ABRACADABRA: \(26^{11}+26^4+26=3670344487444778\).
- M/M/1 means at \(\rho=1/2,9/10,99/100\) are \(1,9,99\).
- First-return ratio: \(\binom{2m}{m}/\binom{2m-2}{m-1}=(4m-2)/m\), and after the factor \(1/4\) one gets \(u_{2m}/u_{2m-2}=(2m-1)/(2m)\).
- \(\ln(1-x)+x+x^2\) is nonnegative on \([0,1/2]\) because its derivative is \(x(1-2x)/(1-x)\).

**Proofs I read through.**

- Binary digits, outer content, the run of heads, and the ballot theorem, including the edge \(b=0\).
- The boy–girl and Tuesday counts, the Penney race, the \(n\)-door host, pairwise dice, aces, and the Catalan bijection, including the solutions.
- Poisson limit of binomial laws, the integral bound on \(-\ln(1-x)\), cycles, coupon stages and variance, empty boxes.
- Records, fixed points, quicksort’s recurrence, Poisson factorial moments, reservoir sampling, the prisoners’ cycles, and the sum of two Poissons.
- Extinction, including \(m<1\), \(m=1\) with \(P(X=1)<1\), and the deterministic one-child and two-child edges.
- Hoeffding’s statement and the optimisation \(-\lambda t+\lambda^2 D/8\). The runs solution, including the integer-threshold gap.
- Continuous Fubini on a rectangle, independent uniforms from disjoint bit blocks, the ordered pair of two uniforms, Box–Muller through the gap in V4-03, and the statement of dominated convergence for continuous integrands.
- The characteristic-function section, the inversion proof’s organisation, Lindeberg’s statement and the swap, the passage from smooth tests to distribution functions by the cutoff \(q(u)=1-35u^4+84u^5-70u^6+20u^7\), the local theorem’s Stirling algebra as far as \(n\cdot 2\delta^2=(2k-n)^2/(2n)\), the cycle embedding, and the Gaussian-vector factorisation.
- Slutsky’s solution for a constant, including \(c<0\). The confidence solution’s appeal to Volume 1.
- Top-to-random, including the reversed coupon stages and \(d(t)\le P(\tau>t)\). The untouched-card lower bound, except the missing derivative.
- Memorylessness, as far as the unjustified \(G(0)=1\).
- The crossing lemma, Euler’s inequality for a disconnected simple plane graph, and the second-moment bound via Cauchy–Schwarz.
- The opening of the subcritical component bound.
- The harmonic-function uniqueness paragraph.
- The first-return calculation that uses the ballot theorem.

**Citations checked against a source I opened.**

- Bertrand, CR 105 (1887), 369, and André, same volume, 436–437. Renault, *Amer. Math. Monthly* 115 (2008), 358–363. The book’s distinction, that André’s correspondence was not the geometric reflection, matches Renault’s paper.
- Galton’s quincunx: manufactured 1873, shown at the Royal Institution on 27 February 1874, described in *Natural Inheritance* (1889). UCL’s record dates the instrument to 1873. The cover note’s dates agree. “Twelve rows” describes the cover drawing, not the historical machine.
- Volume 1 chapter numbers used by this book: Chapter 2 counting, Chapter 3 sequences and the integral test, Chapter 7 linear algebra, Chapter 8 calculus, Chapter 9 inequalities, Chapter 10 probability. I checked these against `volume1-first-principles/main.tex`.
- Volume 1’s weak-law theorem and the sentence that those arguments use finite sums.
- Seventy-one distinct downstream number-citations, by script, against the numbered environments in reading order. Zero mismatches of kind or number.

**Rendered pages I looked at.**

Print folios: the preface opening, a blank verso, the Part I charcoal page, the Chapter 1 opener, the ballot page, the About the Cover page, the Appendix B opener, and folio 248 (the rasterized local-lemma page). Part openers are full-page charcoal to the bleed edge. The print file has no annotations and no document metadata. Page size is \(513\times 738\) pt on all 291 pages.

## Not reviewed

- I did not re-prove Volume 1. I checked the statements this book cites, not the proofs behind them.
- I did not line-check every estimate in the three-dimensional walk, the Lévy construction, the \(L^2\) martingale maximal inequality, or the exploration process past the first-moment bound.
- I did not recompute the Bayer–Diaconis distances for 52 cards, or redraw every TikZ plate. Unused figure files that no chapter inputs were not reviewed as printed figures.
- `chapters/gilmer.tex` is not in the book. I checked only that `main.tex` does not input it, and that the constant arithmetic \(1-1/c=(1-\ln 2)/2\) with \(c=2/(1+\ln 2)\) is right. I did not audit that draft’s entropy inequalities.
- Journal pages I did not open: Poisson 1837, Goncharov 1942 and 1944, Feller’s chapter numbers, Chebyshev 1867, Hoeffding 1963, Borel 1909, Cantelli 1917, Bernstein 1912, Shannon 1948, Penney 1969. The ballot and Galton citations above are the ones I did open.
- I did not read the EPUB on a Kindle Paperwhite. I checked file size, plate pixel width, CSS, and the em baseline on a sample of inline images.
- I did not re-read every paragraph of Volumes 5–15 that cites Volume 4. I checked the numbering of all 71 distinct numbered citations and the content of the sample listed above.
- Historical priority of the ballot theorem before Bertrand (Whitworth, 1878) is not a claim the book makes. I did not treat the omission as an error.

## Comparison with the earlier review

This section was written after the scores and the issue log above. The file compared is `docs/review/volume4-successor-review-2026-11-10.md`. Its first pass is dated 10 November 2026, on `b5543de6`. A second pass in the same file reads later repairs (pull requests 152–155) and says nothing in that pass needs an author decision.

The repairs I re-opened are still in the tree, and several of them hold.

- Theorem 9.9 now says each arrangement with \(r\) rising sequences has probability \(Q_a\). The ambiguous event-reading is gone.
- Theorem 10.8 computes the joint density of the ring time and the surviving residual. It no longer cites memorylessness at a deterministic time for that step.
- Theorem 11.12 truncates before it passes the square to the limit, and it says it is not using continuity from below on a general space.
- Proposition 12.11 writes a compact-box and Gaussian-tail limit from the dyadic hitting time to the hitting time. I did not rebuild every test function in that argument.
- The Pólya ball-separation uses \(\pi>2\), which Volume 1 gives, rather than an unproved \(\pi>3\).
- The blurb names Volume 1 only. Volume 3’s two forward pointers say Chapter 9. Volume 12 cites Theorem 12.9 for nowhere-differentiability.
- Appendix B is still lettered B, and `gilmer.tex` is still outside the book. Both choices match what the later volumes cite.

### What that review missed

These are in the issue log above and are not in its table, its second-pass sign-off, or its “not re-opened” list.

- **V4-01.** The product proposition that the second pass signs off factors monotone or finite-bit functions. Lines 221–225 cite it for \(\cos(tQ(u))\) and \(\sin(tQ(u))\), which are not monotone, and the Gaussian-vector transform repeats the factorisation. The second pass describes the proposition’s hypotheses accurately and does not notice this use.
- **V4-03.** Box–Muller’s test-function calculation is followed by an unproved claim that the curved boundary has covers of arbitrarily small area. The earlier review checked the factor \(r\) and the cancellation to \(\phi(x)\phi(y)\). It did not flag the step from a test function to a rectangle probability.
- **V4-04.** The solution of Exercise 6.2 invokes Volume 1’s weak law for the average of \(Y_i^2\). That law, as proved in Volume 1, is a finite-sum Chebyshev argument. The fourth-moment strong law of this chapter would need an eighth moment.
- **V4-05, the listing half.** `kdp.md` still says some measure-theoretic foundations are labelled and proved in a later volume. The preface and the repaired blurb say the opposite. The earlier review compared the blurb with the preface and stopped.
- **V4-07.** \(1-\Phi(1.9)\) is printed as \(0.02872\ldots\). The value is \(0.02871655\ldots\).
- **V4-09 and V4-10.** An undefined \(S_N\), and a bridge that says every component “has order \(\log n\)” where Theorem 14.1 proves an \(O(\log n)\) upper bound.
- **V4-11.** The longest-run solution misses the atom when \((1-\varepsilon)\log_2 n\) is an integer.
- **V4-15.** The \(n\)-door host is not named.
- **V4-16 and V4-20.** There is no index and no collected bibliography. Print folio 248 is a single 600 ppi image of a text page. The earlier review did not open the PDF or the EPUB.
- **V4-18, V4-19, V4-22, V4-23.** Uniqueness for the normal characteristic function is not written. Glivenko–Cantelli cites the strictly increasing inverse. One sentence in the arcsine proof omits the factor \(1/4\). The harmonic-function maximum may meet \(b\) before \(a\).

Its “not re-opened” list already names two items I logged: Hoeffding’s “finite sum” wording (V4-12) and the birthday solution’s missing liminf and limsup. Those are still in the source. It also notes that memorylessness skips \(G(1)=G(1/q)^q\). That skip is still there, and it is separate from V4-08, which is the unjustified line \(G(0)=1\).

### What it marks fixed, and is not

The second pass marks the Lindeberg half of M1 as repaired, with one residual: the cylinder average of \(f'(A)\) is said to be a Fubini integral on a large box, and “it does not write a separate \(\varepsilon\) line for that tail.” That residual is V4-02. It is the step Corollary 6.11 uses. The same paragraph then says nothing in the pass needs an author decision. The missing estimate is still a major gap. I do not count the fourth-moment expansion for a bounded monotone clip as unfixed. That half of the repair is a real argument, apart from the next sentence.

The same sign-off describes the clip by the bound \(|Q-Q^{(M)}|\le Q^2/M\) and “the tail of a convergent improper integral.” Line 118, inside that argument, says \(Q^2-(Q^{(M)})^2=Q^2\) on the tail. The clip is \(\pm M\), so the difference is \(Q^2-M^2\). The limit still vanishes. The sentence the second pass treats as the repair is not the sentence on the page.

The preface’s contract is treated, in the first summary and again after the blurb repair, as matched by the proofs. After V4-01 through V4-04 it is not. The blurb repair itself is real: the blurb now names Volume 1, as m9 asked.

I did not find a regression in the Bayer–Diaconis sentence, the superposition residual, the \(\pi>2\) comparison, the Chapter 9 pointers in Volume 3, or the Theorem 12.9 pointer in Volume 12. Those repairs are still doing the job the second pass describes.

## Final status, 11 November 2026

Every finding below was repaired on `main` after a second reading of the diff. Numbered theorems, sections, and exercises were not renumbered. Volumes 1 and 2 were not edited. The Volume 3 manuscript was not edited. Four pull requests refreshed the Volume 3 seam digest because that ledger hashes four Volume 4 files by byte. The digest moved with the file. No Volume 3 classification was reassigned.

| Finding | Severity | Fix | Residual doubt |
| --- | --- | --- | --- |
| V4-01 | major | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). The product proposition now factors any finite product of bounded functions that are uniformly continuous on compact subintervals of \((0,1)\), by freezing the ends and passing to dyadic steps. Cosine and sine of a continuous quantile, including \(\Phi^{-1}\), are in that class. Gaussian vectors use the same product. | The identity is not claimed for an arbitrary measurable function. The theorems that use it do not need that wider class. |
| V4-02 | major | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). Lindeberg's swap clips every block, replaces the clips by dyadic steps, and writes the Lipschitz errors before the limits. A normal summand is realised as \(\Phi^{-1}\) of a fresh uniform. | None for the stated model. The argument does not repeat a separate Box–Muller cylinder estimate, because the quantile realisation is the one the proof uses. |
| V4-03 | major | [#163](https://github.com/OussamaSegh/Order-and-Chance/pull/163). Each side of the rectangle is cut into arc-length pieces of diameter \(L/n\), covered by \((r,\theta)\) squares, and priced by the maximum of the product density times the area. | The factor \(9\) from the \(3\times 3\) enlargement is a convenient upper bound, not a sharp area. The limit only needs that the cover's probability tends to \(0\). |
| V4-04 | major | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). Exercise 6.2 uses Theorem 6.4 for the sample mean. The squares are split into monotone pieces, the product proposition gives the variance, and Chebyshev is applied to a clipped square. | The expectation of that clipped square is the finite-bit limit the product proposition already takes. It is not a new integral theorem. |
| V4-05 | major | [#170](https://github.com/OussamaSegh/Order-and-Chance/pull/170). The preface, the blurb, and `kdp.md` say that every proof step is in this volume or in Volume 1, and that a later volume's theorem is named and not used as a step. | None. The sentence is true of the text on `main` after #163 and #164. |
| V4-06 | minor | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). On the tail, \(Q^2-(Q^{(M)})^2=Q^2-M^2\). | None. |
| V4-07 | minor | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). The tail beyond \(1.9\) standard deviations is printed as \(0.02872\), without an ellipsis. | None. \(0.02872\) is the five-digit rounding of \(0.02871655\ldots\). |
| V4-08 | minor | [#167](https://github.com/OussamaSegh/Order-and-Chance/pull/167). \(G(0)=G(0)^2\), the zero law is excluded, and the rational powers are written before continuity. | None. |
| V4-09 | minor | [#161](https://github.com/OussamaSegh/Order-and-Chance/pull/161). The events are \(\{Z_n>0\}\). | None. |
| V4-10 | minor | [#161](https://github.com/OussamaSegh/Order-and-Chance/pull/161). The bridge says size \(O(\log n)\). | None. |
| V4-11 | minor | [#162](https://github.com/OussamaSegh/Order-and-Chance/pull/162). When \((1-\varepsilon)\log_2 n\) is an integer, the blocks are rerun at \(\varepsilon/2\). | None. |
| V4-12 | minor | [#162](https://github.com/OussamaSegh/Order-and-Chance/pull/162). The countable case cites the nonnegative double-sum principle of Volume 1, Chapter 10. | None. |
| V4-13 | minor | [#166](https://github.com/OussamaSegh/Order-and-Chance/pull/166). The derivative of \(\ln(1-x)+x+x^2\) is checked on \([0,1/2]\). | None. |
| V4-14 | minor | [#160](https://github.com/OussamaSegh/Order-and-Chance/pull/160). Outer content is an infimum of countable covers, and a tail of ones cannot occur. | None. |
| V4-15 | minor | [#160](https://github.com/OussamaSegh/Order-and-Chance/pull/160). The host is named as Volume 1's door experiment. | None. |
| V4-16 | minor | [#171](https://github.com/OussamaSegh/Order-and-Chance/pull/171). The bibliography repeats the chapter source lists. The index points at the existing theorem numbers. | Locators are theorem numbers, not page numbers. The EPUB is built from the source, not from the aux file, so a page number would not survive. |
| V4-17 | minor | [#168](https://github.com/OussamaSegh/Order-and-Chance/pull/168). The appendix says it is lettered B. The letter stays, because later volumes cite Theorem B.7. | None. |
| V4-18 | minor | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164). The integrating factor shows that \(\varphi'(t)=-t\varphi(t)\) and \(\varphi(0)=1\) force \(\varphi(t)=e^{-t^2/2}\). | None. |
| V4-19 | minor | [#164](https://github.com/OussamaSegh/Order-and-Chance/pull/164), using the identity proved in [#163](https://github.com/OussamaSegh/Order-and-Chance/pull/163). Glivenko–Cantelli cites the right-continuity argument, so a flat stretch is allowed. | None. |
| V4-20 | minor | [#169](https://github.com/OussamaSegh/Order-and-Chance/pull/169). The pale edges are opaque mixtures of the series colours with white. The build of that head reported 291 print pages and 0 pages flattened. | The final page count is the one in the `books` release built from the merge of every repair, not this intermediate 291. |
| V4-21 | minor | [#163](https://github.com/OussamaSegh/Order-and-Chance/pull/163). Right-continuity gives \(Q(u)\le x\) if and only if \(u\le F(x)\). | None. |
| V4-22 | minor | [#165](https://github.com/OussamaSegh/Order-and-Chance/pull/165). The ratio includes the factor \(1/4\) from the powers of \(2\). | None. |
| V4-23 | minor | [#165](https://github.com/OussamaSegh/Order-and-Chance/pull/165). The maximum meets the first boundary vertex, which may be either marked point. | None. |
