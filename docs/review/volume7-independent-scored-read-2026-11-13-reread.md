# Volume 7 independent re-read after fixes

Independent scored read of *Order and Chance*, Volume 7, *Spaces: Topology, Measure and Limits*, as it stands on `main` at `f10e4c99` (13 November 2026). The published files used are the GitHub release `books` (published 2026-11-13T01:47:12Z): reading PDF `Volume.7.-.Spaces.pdf` (276 pages, 7 × 10 in, PDF 1.5, created 2026-11-13) and print PDF `Volume.7.-.Spaces.-.Print.pdf` (275 pages, 7.125 × 10.25 in, PDF 1.3), together with the EPUB (18.8 MB). Printed folios in the body sit 13 below the reading-PDF page index: reading page 15 is printed page 2, the opening of Chapter 1.

The scorecard and the issue log were written, and committed, before any Volume 7 review note, handoff, or earlier pull-request discussion was opened. The comparison at the end was written after that commit.

The reader assumed here is someone who has worked through Volumes 1–6. The prose is aimed at that reader, not at a student opening this book from high-school mathematics alone.

## Scorecard

Columns: (a) mathematical correctness, (b) rigor, (c) prerequisite discipline, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography as rendered. A 10 would mean the item is genuinely without fault at the standard of Courant–Robbins, Spivak, or Tao’s *Analysis I* on the material it treats. Scores reflect what was re-proved, not a general impression. Where a chapter was only sampled, the justification says so, and the unread proofs are listed under Not reviewed.

| Chapter | a | b | c | d | e | f | g | h | i | j |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 Sets, Choice and the Real Numbers | 9 | 8 | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 8 |
| 2 Metric Spaces and Completeness | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 9 | 8 |
| 3 Topological Spaces | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 4 Compactness | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 8 |
| 5 Baire’s Theorem | 9 | 8 | 8 | 8 | 9 | 7 | 8 | 9 | 8 | 8 |
| 6 The Jordan Curve Theorem | 8 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 |
| 7 Measures | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 8 The Lebesgue Integral | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 9 Product Measures and Change of Variables | 9 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 |
| 10 \(L^p\) Spaces | 8 | 8 | 8 | 8 | 8 | 6 | 7 | 8 | 8 | 8 |
| 11 Differentiation and Radon–Nikodym | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 12 Measures on Metric Spaces | 8 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 |
| 13 Almost every number | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 8 | 8 |

There is no appendix. `jordan-polygon.tex` is the first section of Chapter 6, and its three numbered statements are Theorems and Lemmas 6.1–6.3.

### Why these scores

**Chapter 1 (printed pp. 2–23).** The construction of \(\mathbb N\), \(\mathbb Z\), and \(\mathbb R\) was re-read line by line, including Peano, recursion, the field and order axioms for the Cauchy reals, the least-upper-bound bisection, uniqueness of a complete ordered field, Cantor, Schröder–Bernstein, and Zorn. The square-root gap in \(\mathbb Q\), the Calkin–Wilf values \(q_1,\ldots,q_{10}\), and the index \(q_{43}=\frac{13}{5}\) were recomputed and match the solutions. Rigor is 8 because the bisection says \(2^{-k}\to 0\) “by Archimedes” without writing \(2^k\ge k\), and several ring axioms for \(\mathbb Z\) are declared to be identities in \(\mathbb N\). The field of fractions of \(\mathbb Z\) is referred to Volume 3, Chapter 6, which does construct \(\operatorname{Frac} R\); the local verifications are the same shape as the integer ones. Voice is the best in the book.

**Chapter 2 (printed pp. 24–45).** Completion by the Kuratowski embedding, the Cauchy-sequence model of \(\mathbb Q_p\), the digit expansion, compactness of \(\mathbb Z_p\), the series for \(\exp\), \(\cos\), \(\sin\), and the construction of \(\pi\) were checked. The bound \(\cos 2\le -\frac13\) and \(\sin t>t-\frac{t^3}6\) on \((0,2]\) are the right alternating-series estimates. The Dottie number \(0.7390851332\ldots\) is the fixed point of cosine. \(5^{10}=9765625\), so “nearly ten million” is fair. Theorem 2.16(f), the length of the arc \(e^{it}\), is the one forward reference inside the chapter; it is disclosed and is not used in (a)–(e). Hutchinson’s theorem is Banach’s theorem on the hyperspace, and the reduction is correct. Not every exercise solution was re-derived.

**Chapter 3.** Sampled: the recovery of the intermediate-value theorem from connectedness (Corollary 3.12), path-connectedness of open sets in a normed space by polygonal paths (Proposition 3.14), and the topologist’s sine curve. Proposition 3.14 is what Volume 9 cites for polygonal paths, and it says that. The rest of the chapter, including the quotient constructions and Tietze’s proof, was not re-proved line by line, so the scores stay at 8 rather than 9.

**Chapter 4 (compactness from printed p. 63).** The equivalence of compactness, sequential compactness, and complete total boundedness, including the Lebesgue number (Theorem 4.8), was checked, as were Fermat–Rolle–mean value (Theorem 4.10), Tychonoff via Zorn (Theorem 4.11), the homeomorphism of the Cantor space with the middle-thirds set, and Stone–Weierstrass with the bound \(se^{-ns/2}\le\frac2{en}\). Exercise 4.6 is Bernstein’s proof and Exercise 4.7 is Lebesgue’s space-filling curve, which is what Volumes 9 and 11 cite. Arzelà–Ascoli’s proof was not re-read line by line.

**Chapter 5.** Baire’s theorem for complete metric spaces and for locally compact Hausdorff spaces, the Takagi difference quotients \(s_{k+1}-s_k=\pm 1\), and the Banach–Mazurkiewicz argument (\(E_n\) closed, empty interior, covering one-sided derivatives) were checked and are correct. Weierstrass’s condition \(ab>1+\frac{3\pi}2\), with Hardy’s \(ab\ge 1\) marked as quoted, is stated accurately; the figure \(a=\frac12\), \(b=3\) meets Hardy and not Weierstrass. The phrase “length zero” for the Cantor set (printed p. 86) is ahead of the definition of measure, though Chapter 4 already warns that Chapter 7 makes the phrase precise.

**Chapter 6.** The polygonal parity at a vertex (same side: contribution \(0\) or \(2\); opposite sides: contribution \(1\); the extension of \(\pi\) uses nearby points off the bad lines, so the raw count through the vertex is not required to match) and the degree-2 graph of sides and sectors were followed and are correct. The winding-number lemmas, the retraction formula for Brouwer, and Maehara’s crossing map \(F\) (which does land on the boundary of the square, because \(N=\|h-v\|_\infty\)) were re-derived. The four steps of the Jordan proof close. Clarity is 7: the choice of subarc from \(l\) to \(m\), and which path is claimed to miss \(J_s\), asks more of the reader than the surrounding chapters. Numbering with the polygon file included is 6.1 polygons, 6.4 continuous argument, 6.5 winding number, 6.6 its properties, 6.7 Brouwer, 6.8 crossing, 6.9 arcs, 6.10 Jordan. That is what Volumes 8 and 9 cite.

**Chapter 7.** Dynkin, uniqueness, Carathéodory’s criterion, and the extension theorem were read. The case \(\mu^*(A_n)=\infty\) is separated before the \(\varepsilon\)-covers. The characterisation of Lebesgue measure really is a sandwich between dyadic boxes. Vitali’s set sits in \([-1,2]\), and a finite positive translation-invariant measure on all sets is impossible. The hyperplane cover \(\varepsilon\sum_k 2^{-k}(2k)^{d-1}\) is a null cover. Borel’s normal-number theorem and the digit lemmas were not re-proved.

**Chapter 8.** Monotone convergence, Fatou, and dominated convergence were not re-copied line by line. Vitali’s convergence theorem, the parameter theorem, and the statement of Lebesgue’s criterion were read. The factor \(2g\) on a complex difference quotient is a valid bound (real and imaginary parts), looser than \(\sqrt2\,g\). Exercise 8.8 is the Riemann–Lebesgue lemma, which is what Volume 15 cites.

**Chapter 9.** Tonelli and Fubini, for \(\sigma\)-finite measures, are the standard reductions to indicators, simple functions, and monotone convergence; the hypotheses are stated and used. The matrix with \(1\) on the diagonal and \(-1\) on the superdiagonal has row sums \(0\) and iterated column sum \(1\). The diagonal against counting measure gives \(1\) one way and \(0\) the other. The elementary-matrix proof that \(\lambda(T(A))=|\det T|\,\lambda(A)\), the cube estimate, and the four steps of the change-of-variables theorem were checked; the Jacobian identity for polar coordinates in the plane is \(r\). The ball volumes \(2\), \(\pi\), \(\frac43\pi\), \(\frac{\pi^2}2\) in dimensions \(1\) through \(4\) match \(\pi^{d/2}/\Gamma(\frac d2+1)\). In dimension \(100\), \(\pi^{50}/50!\approx 2.37\times 10^{-40}\) (the text’s \(2.4\times 10^{-40}\)), the cube \([-1,1]^{100}\) has volume \(2^{100}\approx 1.27\times 10^{30}\), the ball’s fraction of that cube is about \(1.9\times 10^{-70}\) (the text’s \(2\times 10^{-70}\)), \(0.9^{100}\approx 2.66\times 10^{-5}\), and \(\sqrt{100/3}\approx 5.77\). The Gaussian density formula was re-derived from the change of variables. Clarity is 7 because the dyadic decomposition and the passage from cubes to Borel sets are packed into two paragraphs.

**Chapter 10.** Young, Hölder, and Minkowski were sampled at the normalisation step. Riesz–Fischer (Theorem 10.4) includes the almost-everywhere subsequence, which is the fact Volume 8’s Bergman-space solution cites as “Chapter 10”. Theorem 10.10 states norm convergence of an approximate identity only for \(1\le p<\infty\). Exercise 10.2(b) and its solution drop that restriction (V7-5). The sentence after Theorem 10.5 applies Jensen’s inequality to \(t\mapsto t^{q/p}\) at the endpoint \(0\), which the stated hypotheses exclude; the norm comparison itself is the Hölder inclusion already proved (V7-6). The exercise score is 6 because the solution asserts a false limit.

**Chapter 11.** Hahn, Radon–Nikodym (the \(\varepsilon\)-improvement of a maximal density), Lebesgue decomposition, the three-part corollary, Vitali covering with the factor \(3^d\), the maximal inequality, differentiation of measures, Lebesgue’s theorem on monotone functions, the fundamental theorem for absolute continuity, conditional expectation, and the tower property were checked. The die example is right: odds average to \(3\), evens to \(4\), and the mean is \(\frac72\). The maximal function of \(\mathbf 1_{[-1,1]}\) is \(1\) on \((-1,1)\), \(\frac12\) at the endpoints, and \(\frac1{|x|+1}\) for \(|x|\ge 1\), as the caption says. Girsanov is named as belonging to Volume 12 and is not used.

**Chapter 12.** Kolmogorov’s extension (tight inner compacts, diagonal extraction, contradiction to \(C_k\downarrow\varnothing\)) was checked, including the estimate \(\mu_0(C_k\setminus D_k)<\frac\delta2\). The Cantor-dimension arithmetic \(3^s=2\) and \(\frac12\le\mathcal H^s(C)\le 1\) is correct; the exact value \(1\) is quoted and unused. Hausdorff measure as a Borel measure, and \(\mathcal H^d=c_d\lambda_d\), are marked quoted from Falconer and are not used. Portmanteau’s five equivalences and the layer-cake identity were checked. The Riesz-representation inequality chain was expanded and matches. Prokhorov’s proof on \(\mathbb R^d\) was only sampled. The carpet caption \(\frac{\log 8}{\log 3}\approx 1.893\) is right (\(\log 8/\log 3\approx 1.8928\)).

**Chapter 13 (printed pp. 229–258).** The convergence half of Khinchin, the distortion inequality, the constant
\[
c=2\sum_{k\ge 1}\frac1{k\sqrt{k+1}}=4.368019\ldots
\]
(the solution’s \(4.3680\ldots\), and \(<4.4\)), the comparison \((2c)^2<77<e^5\), and the block estimate with ratio \(<150\) were recomputed. Euler’s continued fraction is marked quoted. The nine solutions of \(\bigl|e-\frac pq\bigr|<\frac1{q^2\log q}\) for \(q\ge 2\) were checked against \(e\) at precision above \(2\log_{10} q\): they are \(\frac52,\frac62,\frac83,\frac{11}4,\frac{19}7,\frac{193}{71},\frac{2721}{1001},\frac{49171}{18089},\frac{1084483}{398959}\), and the next convergent of the same shape (\(q=10391023\)) already has ratio \(1.07>1\). For \(q\ge 8\) the target is stricter than Legendre’s \(\frac1{2q^2}\), so every solution is a convergent; for \(2\le q<8\) every nearby numerator was tested. The product \(\lvert\hat\mu(1)\rvert=\prod_{k\ge 1}\lvert\cos(2\pi/3^k)\rvert=0.371437\ldots\). The golden-ratio histogram claim is exact: of the \(2000\) odd and \(2000\) even exponents from \(1\) to \(4000\), the fractional parts fall in \((0,0.05)\) or \((0.95,1)\) except for \(n=1,3,5\) and \(n=2,4,6\), hence \(1997\) in each end bin. The cylinder length \(\frac1{q_n(q_n+q_{n-1})}\) is proved inside the solution of Problem 13.3(a), via \(\int_0^1\lvert\psi'\rvert\), although the problem statement does not ask for it. Jarník’s prime-counting step cites Volume 6, Theorem 5.5, which is the prime-number theorem. Lévy’s constant and Khinchin’s constant are quoted and unused. Pedagogy is 7: the chapter is a problem set at the Crossroads standard, and the Jarník construction is a thicket even though the estimates check.

### Whole book

| Item | Score | Justification |
| --- | ---: | --- |
| Structure and arc | 9 | Three parts do the three jobs in the subtitle: the line, distances, and topology through Jordan; measure through \(L^p\); then weak convergence, dimension, and one problem chapter on almost every real. The last page of Chapter 12 hands the reader to Chapter 13 by name, and Chapter 13 hands the reader to *Analysis*. |
| Continuity with Volumes 1–6 | 9 | The preface table was checked against the earlier books. Volume 5, Chapters 3 and 4, admit Tonelli and point at Theorem 9.5. Volume 5, Chapter 5, names Fubini and the change of variables and does not prove them. Volume 5, Chapter 6, cites Theorem 7.11 for the volume of a bounded convex set. Volume 5, Chapter 9, quotes the Jordan theorem and does not use it. Volume 4, Chapter 5, proves continuous Fubini on a rectangle and names the general theorem. Volume 6, Chapter 12, admits one use of Tonelli. Volume 2, Theorem 9.2 and Lemma 9.4, are the convergent-error formula and the best-approximation lemma that Chapter 13 quotes. Volume 5, Theorem 6.13, is Weyl’s criterion. Volume 3, Chapter 6, is the field of fractions. |
| Preparation for later volumes | 8 | Numbered citations that later volumes actually print were matched against the counters, including the shift caused by inserting Jordan as Chapter 6. Fubini is Theorem 9.6, the change of variables is Theorem 9.8, Radon–Nikodym is Theorem 11.4, conditional expectation and the tower property are Theorems 11.16 and 11.17, Prokhorov is Theorem 12.7, Kolmogorov is Theorem 12.8, Stone–Weierstrass is Theorem 4.19, and the Jordan theorem is Theorem 6.10. The statements say what the later books claim. The one soft spot is Problem 13.3(a), below. Not every one of the hundred-plus later citations was opened. |
| Delivery of the title and subtitle | 9 | *Spaces*, and *Topology, Measure and Limits*: limits are constructed twice (reals, then metric completion, including \(\mathbb Q_p\)); topology runs through Jordan; measure runs through Radon–Nikodym and weak convergence, which is a limit of measures. The cover is the Cantor function over the Cantor set, and both are studied. |
| Front matter, index, sources | 8 | The preface is a real map, and its debt table is accurate on the citations that were opened. The index is a theorem index: the printed numbers were regenerated from the source, including `jordan-polygon.tex`, and they match the index entries that were compared (Jordan 6.1–6.10, Fubini 9.6, conditional expectation 11.16, tower 11.17, Kolmogorov 12.8, and the Chapter 1–5 names). It is not a subject index. Sources sit at the end of each chapter and name editions and years; there is no collected bibliography. About the Cover matches the printed front: the Cantor function through its iterates, eight stages of the Cantor set underneath. |
| Print PDF | 8 | 275 pages, every page \(513\times 738\) pt. Trim is \(504\times 720\) pt with \(9\) pt at top and bottom and on the outside edge, mirrored: odd pages bleed on the right, even pages on the left. Print page 13, the part opener, is charcoal \((20,20,21)\) at the four corners and at the mid-edges, so the bleed is ink rather than white padding. Reading and print agree on the part titles. The release metadata records `interior_pages` 275 and `kdp_pages` 276. Not every page was compared visually with the reading PDF. |
| EPUB | 8 | 18.8 MB, under the 50 MB cap. Plates are PNG, \(1800\) or \(1801\) pixels wide, with `width:100%`, `max-width:100%`, and `height:auto` on the `img`. Inline mathematics is a transparent PNG whose width and `vertical-align` are in em. Fonts are the bundled EB Garamond, Cormorant Garamond, and Fira Sans. It was not read on a Paperwhite. |

### Overall

**8.** The book does what its preface promises: it builds the line, pays the named debts of Volumes 4, 5, and 6, and leaves conditional expectation, Fubini, Prokhorov, and Kolmogorov in the forms later volumes cite. The theorems that were re-proved — the reals, Zorn, \(\mathbb Q_p\), \(\pi\), Baire, Takagi, Jordan’s polygonal case and Maehara’s argument, Carathéodory, the Lebesgue sandwich, Tonelli and Fubini, the ball, Radon–Nikodym, the tower property, Kolmogorov, the Cantor dimension, and Khinchin’s constants — are correct. The faults found are small and local. Clarity drops in the change-of-variables proof, in Maehara’s path-chasing, and in the Jarník construction, which is why the score is not 9.

I would recommend the book, as it stands, to a reader who has finished Volume 6. The nine items below are worth repairing. One of them, in an exercise solution, asserts a false limit. None of them makes a numbered theorem false.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V7-1 | `volume7-spaces/chapters/ch02-metric.tex:341` and `:374–376`. Theorem 2.16(f), printed p. 34. | Prerequisite | minor | Part (f) defines the length of \(t\mapsto e^{it}\) as \(\int_0^\theta\lvert\gamma'\rvert\) and identifies \(\pi\) with half the perimeter. The proof says this integral is the one Volume 1 admitted, and that Theorem 8.10 builds it, and that (a)–(e) do not use it. A reader of Chapter 2 does not yet have that integral. | Move (f) to a remark placed after Theorem 8.10, or say in the statement of Theorem 2.16 that the length clause waits for that theorem. |
| V7-2 | `volume7-spaces/chapters/ch12-harder.tex:45–46`, problem statement at `:85–89`, solution at `:483–487`. Problem 13.3(a), printed p. 229. Also `volume11-randomness/chapters/from-volume7-problems.tex` (the length \(1/(q_n(q_n+q_{n-1}))\)). | Citation | minor | The introduction says Problem 13.3(a) proves the cylinder length. The problem asks for the distortion inequality \(\frac12\lambda(B)\le\lambda(I\cap G^{-n}B)/\lambda(I)\le 2\lambda(B)\). The length is derived in the solution, as \(\int_0^1\lvert\psi'\rvert=1/(q_n(q_n+q_{n-1}))\), and it is correct, but it is not a question the problem asks. Volume 11 cites “Problem 13.3(a)” for that length. | Add one sentence to Problem 13.3(a) asking for the endpoints and the length, which the solution already proves. |
| V7-3 | `volume7-spaces/chapters/ch12-harder.tex:639`. Solution of Problem 13.7 (Jarník–Besicovitch), printed p. 245. | Citation | minor | The tools line names “mass distribution principle, Prokhorov”. The write-up uses the mass distribution principle, Carathéodory’s extension, and Volume 6, Theorem 5.5. It does not use Prokhorov. | Delete Prokhorov from that tools line. |
| V7-4 | `volume7-spaces/chapters/ch05-baire.tex:37`. Printed p. 86. | Prerequisite | minor | The Cantor set is called nowhere dense because it has “length zero”, before length is a defined measure. Chapter 4 does say that \(C_n\) has total length \((2/3)^n\) and that Chapter 7 makes “length zero” precise, but Chapter 5 does not point there. | Replace the parenthesis with “it contains no interval; Chapter 4” or with a pointer to that sentence. |
| V7-5 | `volume7-spaces/chapters/ch09-lp.tex:267` and the solution at `:347`. Exercise 10.2(b). | Exercises | minor | The exercise asks, for \(f\in L^p(\mathbb R)\), that \(f*G_t\to f\) in \(L^p\) as \(t\to 0\). The solution cites Theorem 10.10. That theorem gives the norm limit only for \(1\le p<\infty\). At \(p=\infty\) it fails: if \(f=\mathbf 1_{[0,\infty)}\), then \(f*G_t\) is the distribution function of \(\mathcal N(0,2t)\), and \(\|f*G_t-f\|_\infty=\frac12\) for every \(t>0\). The heat equation in the same part is unaffected. | Restrict the norm limit to \(1\le p<\infty\). |
| V7-6 | `volume7-spaces/chapters/ch09-lp.tex:126`, the sentence after Theorem 10.5. | Rigor | minor | Jensen is stated for a convex function on an open interval, and for integrands with values in that interval. The next sentence applies it to \(\varphi(t)=t^{q/p}\) and to \(\lvert f\rvert^p\), which takes the value \(0\). The comparison \(\|f\|_p\le\|f\|_q\) on a probability space is true: it is the case \(\mu(E)=1\) of the Hölder inclusion a few lines earlier. | Apply the theorem to \(\lvert f\rvert^p+\varepsilon\) and let \(\varepsilon\downarrow 0\), or cite the inclusion already proved. |
| V7-7 | `volume7-spaces/chapters/ch07-integral.tex:224–225`, caption of Figure 8.2. | Figures | minor | For \(g_n=\sqrt n\,\mathbf 1_{]0,1/n[}\), the set \(\{g_n>M\}\) is the whole spike when \(\sqrt n>M\) and is empty otherwise. The tail integral therefore equals \(1/\sqrt n\) in the first case and \(0\) in the second, so it is at most \(1/M\). The caption writes \(\int_{\{g_n>M\}}g_n\le 1/\sqrt n\le 1/M\). The second comparison fails whenever \(n<M^2\): for \(n=1\) and \(M=2\), \(1/\sqrt n=1>1/2\). The family is still uniformly integrable. | Say the tail equals \(1/\sqrt n\) when \(\sqrt n>M\) and equals \(0\) otherwise, hence is at most \(1/M\). |
| V7-8 | `volume7-spaces/chapters/ch07-integral.tex:414`, solution of Exercise 8.2. | Exercises | minor | For \(k=1\) the two intervals are \([0,1/2]\) and \([1/2,1]\). They are both \(1\) at \(x=1/2\), and at every other \(x\) one of them is \(0\). The sentence says that generation has no zero. The \(k\ge 2\) counting already shows that \((f_n(x))\) takes both values infinitely often, so the sequence still diverges at every \(x\). This is what remained of V7-36 after the repair that moved the both-values claim to \(k\ge 2\). | Say that generation has no zero only at \(x=1/2\). |
| V7-9 | `volume7-spaces/chapters/ch07-integral.tex:456`, solution of Exercise 8.7. | Exercises | minor | The identity \(\int_{\mathbb R}e^{-x^2}e^{itx}\,dx=\sqrt\pi\,e^{-t^2/4}\) is true: \(I(t)=\int_0^\infty e^{-x^2}\cos(tx)\,dx=\frac{\sqrt\pi}2 e^{-t^2/4}\), the sine factor is odd, and the cosine factor is even, so the full integral is \(2I(t)\). The solution says this because “the integrand is even in \(x\)”. The map \(x\mapsto e^{itx}\) is not even. | Drop “even” and split the integrand into cosine and sine. |

No critical or major fault was found in the statements and proofs that were re-derived. That is a claim about those arguments, not about the pages listed under Not reviewed.

## Verified correct

Recomputed or re-proved, and believed correct:

- Peano, recursion, and the semiring laws for \(\mathbb N\) (`ch01-sets.tex`, Theorems 1.2 and 1.3, Proposition 1.4). The ordered-pair argument and the construction of \(\mathbb Z\) as a domain.
- Theorem 1.10: \(\mathbb R\) as Cauchy classes is an Archimedean ordered field, complete, with the least-upper-bound property. The inverse of a non-null class, density of \(\mathbb Q\), and the bisection.
- Theorem 1.11: uniqueness of a complete ordered field, including the construction of square roots used to show a field morphism is order-preserving.
- Cantor’s theorem, Schröder–Bernstein, and \(\lvert\mathbb R\rvert=\lvert\mathcal P(\mathbb N)\rvert\). The injection \(\mathcal P(\mathbb N)\to[0,1]\) by \(\sum 2\cdot 3^{-n-1}\) differs by at least \(3^{-n-1}\).
- Zorn’s lemma from the axiom of choice, by \(g\)-sets, and the equivalence with well-ordering.
- Solutions of Exercises 1.1 (no rational square root of 2, via \(\phi(q)=\frac{2q+2}{q+2}\)), 1.9 and 1.10 (Calkin–Wilf: \(q_1,\ldots,q_{10}\) and \(q_{43}=\frac{13}{5}\); binary \(43=101011\) matches the path).
- Completion, \(\mathbb Q_p\), digits, and sequential compactness of \(\mathbb Z_p\) (Theorem 2.10, Corollary 2.11).
- Theorem 2.16(a)–(e): the series for \(\exp\), \(\cos 2<0\), and \(\pi/2\in(0,2)\). The fixed point of cosine begins \(0.7390851332\).
- Theorem 4.8, including the Lebesgue number, and Theorem 4.10 (mean value). Tychonoff’s proof by a maximal family with the finite-intersection property. Stone–Weierstrass, real and complex forms.
- Baire’s theorem. Takagi’s non-differentiability: on the dyadic interval of length \(2^{-k}\) the difference quotient is a sum of \(k\) terms \(\pm 1\), and consecutive quotients differ by \(\pm 1\). Banach–Mazurkiewicz.
- Polygonal Jordan (Theorem 6.1), winding numbers (Lemma 6.4, Definition 6.5, Proposition 6.6), Brouwer’s retraction formula, Maehara’s crossing lemma, and the four steps of Theorem 6.10.
- Carathéodory extension, including the infinite outer-measure case, and the dyadic sandwich for Lebesgue measure (Theorem 7.11). Vitali (Theorem 7.15).
- Tonelli and Fubini under \(\sigma\)-finiteness (Theorems 9.5 and 9.6), the matrix counterexample, and the counting-measure diagonal. Linear images (Theorem 9.7). Change of variables (Theorem 9.8). Ball volume (Theorem 9.11), including the numerical checks in dimension \(100\). Gaussian densities (Theorem 9.12).
- Radon–Nikodym, the tower property (Theorems 11.16 and 11.17), the maximal function of \(\mathbf 1_{[-1,1]}\), and the fundamental theorem for absolute continuity.
- Kolmogorov’s extension (Theorem 12.8). Cantor dimension \(\frac{\log 2}{\log 3}\), with \(\frac12\le\mathcal H^s(C)\le 1\) (Theorem 12.11). Portmanteau.
- Khinchin’s constant \(c=4.368019\ldots\), the nine approximations to \(e\), \(\lvert\hat\mu(1)\rvert=0.371437\ldots\), and the golden-ratio bin counts \(1997\) and \(1997\). The bounds \(\frac{\log 2}{2\log\varphi}=0.72021\ldots\) and \(\frac{\log 2}{2\log(1+\sqrt 2)}=0.39322\ldots\). Dimension of \(B_{1/3}\) is \(H(\frac13)/\log 2\approx 0.918\).
- Downstream numbers that were opened and matched: Volume 8’s Theorems 9.6, 9.7, 9.8, 7.5, 4.19, 4.11, 10.4, 11.4, 12.3, 12.7, 6.10, Definition 6.5, Proposition 6.6, Problem 13.16; Volume 9’s Proposition 3.14, Theorem 4.8 (Lebesgue number), Exercises 4.6 and 4.7; Volume 11’s Theorems 11.17, 12.7, 12.8, 8.16, 7.5; Volume 12’s Theorems 12.8 and 9.12 and Lemma 12.10; Volume 15’s Exercise 8.8 (Riemann–Lebesgue) and Corollary 4.20.

Sources actually used for the checks: the source of Volumes 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, and 15 as cited above; direct numerical recomputation (Python, `Decimal` at precision past \(2\log_{10} q\) for the approximations to \(e\)); the classical statements of the ball volume, the Cantor–Lebesgue function’s Fourier product, Legendre’s theorem on convergents, and Hardy’s condition for the Weierstrass function, compared with the text. Historical dates that the book itself anchors (Dedekind’s 24 November 1858 in the preface of *Stetigkeit*, the Cantor–Dedekind letter of 29 June 1877, Hilbert’s hotel via Kragh) were not re-opened in the library; they are quoted from the book’s own source notes.

## Not reviewed

- Line-by-line reading of every exercise solution in Chapters 2–12. Chapters 1 and 13 were read in full, including solutions of the problems named above; the remaining solutions of Chapter 13 (in particular Eggleston, Koksma’s integral estimate, and the Bernstein set) were not re-derived.
- Arzelà–Ascoli’s proof, the proof of Borel normality, the proofs of monotone convergence, Fatou, and dominated convergence as written, the section lemmas that feed Tonelli, and Prokhorov’s argument past the tightness reduction. A second pass of Chapter 10, after the scorecard was committed, checked Theorem 10.10 and Exercises 10.1 and 10.2; that pass is what produced V7-5 and V7-6. A second pass of Chapters 7 and 8 checked the outer-measure construction, Vitali, the binary digits, normality, monotone convergence, Fatou, dominated convergence, the Riemann criterion, and uniform integrability, and produced V7-7, V7-8 and V7-9. The remaining \(L^p\) exercise solutions were not all re-derived.
- Every later-volume citation. The search covered Volumes 8–15 for “Volume 7” and “Volume~7”; the numbered sample above was checked, not the whole hit list.
- A page-by-page visual pass of all 276 reading pages and all 275 print pages. Sampled: the cover, the three part openers (reading pages 14, 130, 206, all full charcoal), the Chapter 1 opener, print page 13 (charcoal at the bleed edge), and a text-block scan that found no line within \(0.5\) in of the trim. EPUB structure, plate sizes, and CSS were checked; a Kindle device was not.
- The sixteen-digit value \(0.5312805062772051\ldots\) given for \(\dim_H E_{\{1,2\}}\) as a spectral radius. The two bounds around it were checked; the eigenvalue was not.
- Richardson’s table behind “\(D\approx 1.25\)” for the west coast of Britain. The sentence is the standard citation of Mandelbrot’s 1967 paper, which the sources name; the table was not recomputed.
- `docs/plan/MASTER-PLAN-V5-V15.md` was read from the head of PR #157 for scope only (the Volume 7 paragraph, decisions D-14, D-15, D-17). `docs/plan/book-07.md` was read for scope. Against that scope the book does the following, and the mismatches are the plan’s, not silent omissions: Jordan is Chapter 6, so Fubini, Radon–Nikodym, Riesz, Prokhorov, and Kolmogorov are numbered 9.6, 11.4, 12.3, 12.7, and 12.8 rather than the 8.6, 10.4, 11.3, 11.7, and 11.8 of the blueprint; conditional expectation and the tower property are Theorems 11.16 and 11.17; the infinite outer-measure case is separated; Hausdorff’s Borel property is quoted and unused; the ergodic problems are named as living in Volume 11 and are not premises here; \(\mathbb Z_p\) is compact; the last chapter is titled “Almost every number”. The blueprint’s sentence that the cover is the Sierpiński carpet is stale: the approved cover, the colophon, and the preface are the Cantor function over the Cantor set, and the carpet is Figure 12.1 and Exercise 12.2, with dimension \(\frac{\log 8}{\log 3}\).

## Comparison with the earlier report

Written after the scorecard and the issue log above were committed. The documents opened for this section are the report on draft PR #207 (`docs/review/volume7-independent-scored-read-2026-11-12.md`, branch `cursor/volume7-independent-scored-read-2709`) and `docs/review/volume7-fixes-review-2026-11-12.md` on `main`. The fix pull requests #208–#215 were not used as a source of mathematical claims; the book was.

The 12 November report scored the book 8, with preparation for later volumes at 7 and front matter at 6, and logged 38 issues: six major (V7-01 through V7-06) and thirty-two minor (V7-07 through V7-38). The fixes note marks every one of them Accept. Each was checked again against the current manuscript.

### Really fixed

All six majors are gone.

- V7-01. The third column of the debts table is `\raggedright` in every row (`preface.tex:35–42`). The numbers are no longer justified into the next row.
- V7-02. The layer-cake identity is proved in the text immediately before the portmanteau theorem (`ch11-metricmeasures.tex:96–99`), for a simple function and then by monotone convergence. The step \((e)\Rightarrow(a)\) cites that paragraph. The exercise remains, and it is no longer the only proof.
- V7-03. Haar uniqueness cites Volume 7, Theorem 7.5 (`volume8-analysis/chapters/ch08-haar.tex:67`), which is uniqueness on a \(\pi\)-system.
- V7-04. Hausdorff–Young cites Proposition 10.6 for the density of simple functions (`volume8-analysis/chapters/ch05-fourier.tex:201` and `:209`). Proposition 9.6 remains Fubini.
- V7-05. The winding number in Volume 9 is “Definition 6.5, after Lemma 6.4” (`volume9-shapes/chapters/ch03-forms.tex:347`). Item 6.1 is still the polygonal theorem.
- V7-06. `chapters/index.tex` is input from `main.tex`. The printed numbers were regenerated from the source, including the three statements in `jordan-polygon.tex`, and they match the index.

The minors are gone as specified, and the repairs that were re-derived are right.

- V7-07, V7-23, V7-24, V7-25. Square roots in the uniqueness proof name \(h=\min\bigl(1,(x-s^2)/(2s+2)\bigr)\) and the symmetric estimate; \(x=0\) is the zero of a field morphism. Density shifts by a natural number \(N\) with \(N+nx>0\). The Cauchy approximation uses \(1/(k+1)\). “Finite” and “infinite” are proved before the enumeration of an infinite subset of \(\mathbb N\).
- V7-08. Part (f) of Theorem 2.16 now says the integral is the one Volume 1 admitted and that Theorem 8.10 builds it, and that (a)–(e) do not use it. That is one of the two repairs the report allowed. The clause is still stated in Chapter 2. That residual is V7-1 above; it is not a new false formula.
- V7-09. The nine pairs, including \((6,2)\), were recomputed. The next convergent of the same shape has ratio \(1.07>1\). Legendre does not delete \(6/2\), because \(\lvert e-3\rvert>1/8\).
- V7-10. The value-net is a \(2\varepsilon\)-net, and the three terms are \(<\varepsilon\), \(<2\varepsilon\), and \(<\varepsilon\), so the display \(<4\varepsilon\) is the sum of those three. The converse, from an \(\varepsilon\)-net of functions, is still \(<3\varepsilon\).
- V7-11. \(\operatorname{Log}\) on \(\{\operatorname{Re}>0\}\) is defined from Theorem 2.16(e), with argument in \((-\pi/2,\pi/2)\).
- V7-12. Injectivity of \((m,n)\mapsto 2^m3^n\) is proved from “\(3^t\) is odd”, without Volume 2.
- V7-13. The coordinate hyperplane is covered. The rotation is named as a fact of Chapter 9 and is not used for the faces.
- V7-14. Hardy’s \(ab\ge 1\) is marked quoted. The figure is \(a=\frac12\), \(b=3\).
- V7-15. All thirteen source lists have `\addcontentsline`.
- V7-16. Problems 13.4 and 13.8 are marked with three stars.
- V7-17. The text prints \(0.9^{100}\approx 2.7\times 10^{-5}\). The value is \(2.656\times 10^{-5}\).
- V7-18. The manifold chapter cites Theorem 7.10 for a cover by cubes.
- V7-19. The interval containing \(a\) is cut at its right endpoint.
- V7-20. The homeomorphism is the bijection from the compact quotient \(\mathbb R/\mathbb Z\) onto \(S^1\). The maps from \([0,1]\) are said not to be bijective.
- V7-21. The winding proof of the fundamental theorem of algebra uses both \(R>1\) and \(R>\sum\lvert c_j\rvert\), which the hypothesis supplies.
- V7-22. The first step of the curve \(c=0\) in `figures/ch04-equicont.tex` runs from \((1.500,0)\) to \((1.520,0.010)\), slope \(\frac12\).
- V7-26. The Calkin–Wilf solution says “the first ten nodes”, and that four levels would be fifteen.
- V7-27. The Babylonian caps are rounded up: \(0.122\), \(0.0053\), \(1.0\times 10^{-5}\), \(3.6\times 10^{-11}\), \(4.6\times 10^{-22}\). The text says 23 matching decimals.
- V7-28. The thick arrows off \(C\) run downward, and the label is \(h=g^{-1}\).
- V7-29. An empty factor makes the product empty, and the proof stops.
- V7-30. The polyline passes through \((\pm 1,\frac12)\) and sits at height \(1\) on the open interval. The caption says so. The value \(\frac1{|x|+1}\) for \(\lvert x\rvert\ge 1\) was recomputed.
- V7-31. Nonnegativity is applied to \(\lvert X\rvert+X\) and to \(\lvert X\rvert-X\).
- V7-32. Ulam’s proof writes \(\mu\bigl(A\setminus(C\cap K)\bigr)<2\varepsilon\).
- V7-33. The rays \(]a,\infty[\) and \(]-\infty,b[\) are in the distribution-function argument.
- V7-34. \(\psi(1)=1/\log 3\) and \(\psi(2)=1/(4\log 3)\), so \(f(1)=f(2)=f(3)\).
- V7-35. The Jarník measure is the equal-mass assignment, extended by Carathéodory. The write-up says why normalised Lebesgue measure on \(E_k\) does not give equal masses.
- V7-36. Both values of the typewriter are claimed from generation \(k\ge 2\). The sentence that remains, “that generation has no zero”, is still too wide: only \(x=1/2\) sees no zero when \(k=1\). That leftover is V7-8. The divergence at every \(x\) is unaffected.
- V7-37. Either norm zero is the case \(0\cdot\infty=0\).
- V7-38. The marker \(2\) is no longer at \((0.62,0.62)\). It is at \((0.52,0.78)\) in `figures/ch09-balls.tex`.

The fixes note’s Accept on V7-08 is fair relative to the option that report allowed. It is the one item I would not call gone without a remainder.

### Not introduced by the fixes

No repaired argument that was re-derived is now false. The \(4\varepsilon\) sum, the nine approximations to \(e\), the equal-mass measure, the swapped values of \(\psi(1)\) and \(\psi(2)\), the logarithm on the half-plane, and the maximal-function polyline were checked as mathematics, not only as text that had changed. The new index does not carry a wrong printed number among the entries compared with the counters.

The name Prokhorov in the tools line of the Jarník solution (V7-3) was already in that line before the November edits. The edit of 12 November only changed “Volume 7, Chapter 12” to a chapter reference. It is an old loose tag, not a regression.

### What the 12 November report did not log

These were in the book before the fixes as well, except the leftover sentence in V7-8. V7-1 is the remainder of V7-08. V7-2, V7-3 and V7-4 were already in the manuscript the 12 November report read. V7-5 and V7-6 were also already there: the heat-kernel sentence is from the rewrite of 12 November (`604f29ea`), before the scored-read repairs, and the Jensen sentence is older. V7-7 and V7-9, the spike caption and the word “even” in the Gaussian solution, were in that manuscript and were not logged. V7-8 is the one sentence the repair of V7-36 left behind: the both-values claim was correctly moved to \(k\ge 2\), and “that generation has no zero” stayed, though it is true only at \(x=1/2\).

- The cylinder length \(\frac1{q_n(q_n+q_{n-1})}\) is attributed to Problem 13.3(a). The problem asks for the distortion inequality. The length is proved in the solution, and Volume 11 cites the problem for it (V7-2).
- The Jarník tools line names Prokhorov, which that write-up does not use (V7-3).
- Chapter 5 still calls the Cantor set a set of “length zero” before length is a measure (V7-4). Chapter 4 already says that Chapter 7 makes the phrase precise; Chapter 5 does not point there.
- Exercise 10.2(b) asks for \(L^p\) convergence of the heat kernel for every \(p\), including \(p=\infty\), where the limit fails (V7-5).
- The sentence after Theorem 10.5 applies Jensen on a closed endpoint the theorem excludes (V7-6). The inequality it wants is already proved by Hölder.
- The caption of the escaping spikes writes \(1/\sqrt n\le 1/M\) for every \(n\) (V7-7). The tail is still at most \(1/M\), so the family is uniformly integrable.
- The Gaussian characteristic-function identity in Exercise 8.7 is right, and the reason given for it, that \(e^{itx}\) is even, is not (V7-9).

The 12 November report’s own comparison, with the October review and the rewrite handoff, is about the book before these fixes. The three wrong citations and the missing index it said those documents had missed are the majors above, and they are fixed. I did not reopen that October review or the handoff for a second census.
