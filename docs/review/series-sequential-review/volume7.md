# Volume 7 — Spaces

**Score: 7/10.**

The real line, Banach’s theorem, the topology through Stone–Weierstrass, Baire’s theorem, the Jordan curve theorem, Lebesgue measure through conditional expectation, weak convergence, the dimension of the Cantor set, and Khinchin’s theorem are proved. The constants that were recomputed match the page. The score is 7 because the proof that the Cauchy classes form the field \(\Q_p\) cites a lemma whose written argument uses the order of \(\Q\). The bound the inverse needs is true, by the reverse triangle, and it is not the argument on the page. The other slips are local. No numbered statement was found false.

**Counts.** 0 critical, 1 major, 10 minor. Eleven issues, `V7-001` through `V7-011`. Three are prerequisite issues: `V7-005`, `V7-006`, `V7-007`.

**How this was read.** Book order in `volume7-spaces/main.tex`: preface, Metric and Topological Spaces (Chapters 1–6, the sixth being the Jordan curve theorem, which inputs `jordan-polygon.tex`), Measure and Integration (7–10), Measures on Spaces (11–13), then the index and About the Cover. The blurb and `kdp.md` were read with the preface. Every chapter file was read, including every exercise, hint, and solution. There are 169 exercises. The shared theorem counter was counted in source order, with the polygon section counted before the rest of Chapter 6. All 80 index numbers match that count. Exercises use a separate counter, restarted each chapter.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. “Moreover” occurs twice, inside proofs (`chapters/ch02-metric.tex:108`, `chapters/ch04-compact.tex:246`), not as a section opener. One sentence in a solution is broken by a comma, and that is V7-008.

## Issues

Paths are relative to `volume7-spaces/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V7-001 | `chapters/ch02-metric.tex:121` (`thm:Qp`) | math | major | “Parts (a) and (b) of Lemma `lem:cauchybasic` … and the bound \(\lvert x_n\rvert\ge\delta\) for large \(n\) in part (c), hold word for word … Their proofs used only the triangle inequality and multiplicativity.” | The written proof of (c) uses the order of \(\Q\): if \(x_m\ge\varepsilon\) then \(x_n>x_m-\delta\). That step is false for \(\lvert\cdot\rvert_p\). The inverse needs \(\lvert x_n\rvert\ge\lvert x_m\rvert-\lvert x_n-x_m\rvert\), which follows from the triangle inequality and is not written. Put that sentence in place of “word for word”. The rest of the field argument is the absolute-value estimate already given for \(\R\). |
| V7-002 | `chapters/ch03-topology.tex:281` | math | minor | “for instance a standard basis vector orthogonal to \(x\)”. | For \(x=(1,1)/\sqrt2\) neither standard basis vector is orthogonal to \(x\). Any third unit vector works. Orthogonality is not used. |
| V7-003 | `chapters/ch01-sets.tex:480` | math | minor | “The same maximality pattern shows … that every field has an algebraic closure.” | Krull’s theorem is Exercise `ex:krull`. Algebraic closure is not proved, not set as an exercise, and not marked quoted. It is not used again. Mark it quoted, or add the exercise. |
| V7-004 | `chapters/ch02-metric.tex:181` (`ex:cosfixed`) | math | minor | “\(\lvert\cos x-\cos y\rvert\le\sin 1\,\lvert x-y\rvert\) there … with \(\sin 1<0.85\)”. | The mean value theorem is Volume 1, which the preface assumes, and Chapter 4 proves it again. The number \(0.85\) is not derived. After Theorem `thm:exp` the alternating series gives \(\sin 1\le 1-1/6+1/120=0.8416\ldots<0.85\), and \(\sin 1<1\) is enough for a contraction. The example is not a premise of `thm:exp`. |
| V7-005 | `chapters/ch02-metric.tex:73` | prerequisite | minor | “The square root on \([0,1]\) is uniformly continuous and not Lipschitz.” | Uniform continuity of a continuous function on a compact interval is Heine’s theorem in Chapter 4. The elementary bound \(\lvert\sqrt x-\sqrt y\rvert\le\sqrt{\lvert x-y\rvert}\) is not written. The sentence is an example, not a premise. |
| V7-006 | `chapters/ch02-metric.tex:156` | prerequisite | minor | “The interval \([-1,1]\) is connected”. | The word is used before Chapter 3 defines it. The same paragraph does say that the names compact and locally compact come later. |
| V7-007 | `chapters/ch01-sets.tex:333` (`prop:countable`) | prerequisite | minor | “With countable choice: a countable union of countable sets is countable.” | Section `sec:choice` defines the axiom later in the chapter and points back at this line. Name the forward reference in the proposition. |
| V7-008 | `chapters/ch01-sets.tex:673` (solution of `ex:functions`) | style | minor | The display ends “\(=\mathfrak c\),” and the next sentence begins “The middle step”. | End the sentence after the display, or attach “where the middle step” to the display. |
| V7-009 | `chapters/ch03-topology.tex:267` | math | minor | “The same holds for the Cantor set.” | The components of \(\Q\) are points because an interval cannot sit inside \(\Q\). The same conclusion for \(C\) needs one sentence: once \(\lvert x-y\rvert>3^{-n}\), the two points lie in different intervals of stage \(n\). That separation is in the solution of Exercise `ex:cantorifs`, not in the sentence. |
| V7-010 | `chapters/ch12-harder.tex:472` (solution of `pb:khinchin`) | exercise | minor | “A numerical evaluation gives \(c=4.3680\ldots\). … \((2c)^2<77<e^5\).” | The problem states \(c<4.4\) as a fact to use. The partial sum through \(10^6\) is \(4.364\), and the tail is about \(0.004\), so the decimal is right. Replace the evaluation by a finite sum plus an integral. Any proved finite bound gives the exponential majorant. |
| V7-011 | `chapters/ch12-harder.tex:770` (solution of `pb:bernsteinset`) | exercise | minor | “If \(A\) were measurable, both \(A\cap[0,1]\) and \([0,1]\setminus A\) would be null.” | The next sentence treats the case of outer measure less than \(1\). The measurable case needs one more sentence: the two null pieces would make \([0,1]\) null. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map matches the thirteen chapters, and the debt table matches the theorems that clear it: least upper bound, \(\exp\) and \(\pi\), the Riemann integral of a continuous function, Tonelli, Fubini, change of variables, product measure, Lebesgue measure, and the Jordan curve theorem. The blurb and `kdp.md` list the same theorems. The carpet dimension in the listing is Exercise `ex:carpet`, and the quoted status of Hausdorff measure as a Borel measure matches Remark `rem:hausdorffquoted`. About the Cover is the Cantor function of Exercise `ex:devil`: constant on the removed intervals, which have full length once measure exists, and increasing on the null set \(C\). Volume 8, Chapter 8, does use the compactness of \(\Z_p\) from Corollary 2.11 to build Haar measure on \(\Q_p\). Volume 11, Chapter 10, proves the ergodic theorem and returns to the Gauss map for Lévy’s constant and Khinchin’s constant, as the leads in Chapter 13 say.

### Chapter 1

Peano, recursion, the semiring, the well-order, \(\Z\) and \(\Q\), the Cauchy reals, the least upper bound, uniqueness of a complete ordered field, countability, Cantor, Schröder–Bernstein, the continuum, Zorn, well-ordering, and a basis. The Calkin–Wilf enumeration begins \(1,1/2,2,1/3,3/2,2/3,3,1/4,4/3,3/5\), and the climb from \(13/5\) ends at index \(43\). The algebraic-closure sentence is V7-003. The choice phrase is V7-007. The broken sentence is V7-008. Index numbers 1.2 through 1.21 match the statements that are indexed.

### Chapter 2

Completion, the digit expansion of \(\Q_p\), sequential compactness of \(\Z_p\), Banach’s theorem, the series for \(\exp\), \(\cos\), \(\sin\) and \(\pi\), the Hausdorff metric, and Hutchinson. The transfer of Lemma `lem:cauchybasic`(c) is V7-001. The square-root sentence is V7-005, the word “connected” is V7-006, and \(\sin 1<0.85\) is V7-004. Recomputed: the Newton errors from \(x_0=2\) give \(x_5\) at least \(21\) correct digits; Hensel’s digits are \(2,1,2\), and \(57^2+1=26\cdot 125\); \(\varphi(1/3)=11/12\) and \(\varphi(-1)=1\); the Dottie number begins \(0.7390851332\). Ostrowski is quoted and unused. Index numbers 2.9 through 2.20 match.

### Chapter 3

Basis, product, quotient, \(\R/\Z\) and the circle, the intermediate value theorem from connectedness, the topologist’s sine curve, Urysohn’s function in a metric space, and Tietze. The sphere sentence is V7-002. The Cantor-set sentence is V7-009. The count of \(29\) topologies on a \(3\)-point set is \(19+9+1\). Exercise `ex:furstenberg` is the same topology as Volume 2, Exercise 2.8. Urysohn’s lemma for a general normal space is quoted from Munkres and unused. Index numbers 3.7, 3.12, 3.16 and 3.19 match.

### Chapter 4

Heine–Borel, equivalent norms, sequential compactness, Heine, the mean value theorem, Tychonoff, the Cantor set, Arzelà–Ascoli, and Stone–Weierstrass. The local convention \(\N=\{1,2,\ldots\}\) in the Cantor space is explicit. Bernstein’s variance \(x(1-x)/n\) was checked. Both \(y=0\) and \(y=t^2/4\) solve the Peano example. Kelley’s theorem that Tychonoff implies choice is quoted. Index numbers 4.4 through 4.20 match.

### Chapter 5

Baire for a complete metric space and for a locally compact Hausdorff space, the Takagi function, Banach–Mazurkiewicz, Baire class one, Liouville numbers, and a comeagre set of non-normal numbers. The null estimate \(10m/(n-2)\) was checked. The Khinchin scale in the paragraph after Theorem `thm:liouville` is the theorem proved in Chapter 13: infinitely often below \(1/(q^2\log q)\), and only finitely often below \(1/(q^2(\log q)^2)\). It is marked as a preview and is not a premise. Borel normality is likewise marked as a preview of Chapter 7. The Weierstrass series and Hardy’s bound \(ab\ge 1\) are quoted. Index numbers 5.2 through 5.14 match.

### Chapter 6

Polygonal Jordan, the continuous argument, no retraction and Brouwer, the crossing lemma, arcs do not separate, and Maehara’s proof of the Jordan curve theorem. Recomputed: \(n(\gamma_1,0)=2\), \(n(\gamma_2,0)=-3\), \(n(\gamma_1,5)=0\); the triangle point \((2,1)\) is odd and \((2,-1)\) is even; the barycentric weights \(1/4\), \(5/12\), \(1/3\) recover \((2,1)\). Index numbers 6.1 through 6.10 match, with the three polygon lemmas counted before the continuous argument.

### Chapter 7

Carathéodory, extension, Lebesgue measure, Stieltjes, the quantile, Vitali, independent digits, and absolute normality. The removed length in the fat Cantor set is \(1/2\). The binary digits of \(1/5\) are \(0.00110011\ldots_2\). The fourth-moment constant \(3/(\varepsilon^4 n^2)\) was checked. Solovay and Banach–Tarski are quoted. Index numbers 7.4 through 7.19 match.

### Chapter 8

Monotone convergence, Fatou, dominated convergence, the Riemann integral of a continuous function, Lebesgue’s criterion, uniform integrability, and differentiation under the integral sign. The Dirichlet integral equals \(\pi/2\) as an improper integral. The layer-cake identity was checked. The integral of \((1-x/n)^n e^{x/2}\) on \([0,n]\) is about \(1.511\) at \(n=10\) and about \(1.926\) at \(n=100\). Index numbers 8.4 through 8.16 match.

### Chapter 9

Product measure, Tonelli, Fubini, the absolute value of a determinant, change of variables, polar coordinates, the ball, and the Gaussian density. The ball volumes in dimensions \(1,2,3,4\) are \(2\), \(\pi\), \(4\pi/3\), \(\pi^2/2\). Also \(\lambda_{100}(B^{100})=\pi^{50}/50!\approx 2.37\times 10^{-40}\), against the text’s \(2.4\times 10^{-40}\); the cube \(2^{100}\approx 1.27\times 10^{30}\); the fraction is about \(1.9\times 10^{-70}\); \(0.9^{100}\approx 2.7\times 10^{-5}\). The Basel integral gives \(\zeta(2)=\pi^2/6\). Beta, Gamma, and the simplex volume \(1/n!\) are exercises. Index numbers 9.4 through 9.12 match.

### Chapter 10

Young, Hölder, Minkowski, Riesz–Fischer, Jensen, density of \(C_c\) and of \(C_c^\infty\), and approximate identities. Hardy’s constant \(p/(p-1)\) is sharp. On \([0,1]\), \(\lVert x\rVert_{100}\approx 0.955\). The heat-kernel identity \(G_s*G_t=G_{s+t}\) was checked. Index numbers 10.1 through 10.10 match.

### Chapter 11

Hahn, Jordan, Radon–Nikodym, Lebesgue decomposition, the maximal inequality with constant \(3^d\), Lebesgue points, differentiation of measures, the fundamental theorem for an absolutely continuous function, conditional expectation, and the tower property. The maximal function of \(\mathbf 1_{[-1,1]}\) is \(1/(\lvert x\rvert+1)\) for \(\lvert x\rvert\ge 1\). The likelihood ratio has entropy \(m^2/2\). The die averages \(3/2\), \(7/2\), \(11/2\), and the coarse average \(5/2\). Index numbers 11.2 through 11.17 match.

### Chapter 12

Ulam, Riesz representation on a compact metric space, portmanteau, Prokhorov for a compact metric space and for \(\R^d\), Kolmogorov’s extension for consistent laws on \(\R^n\), and \(\dim_H C=\log 2/\log 3\), with \(\tfrac12\le\mathcal H^s(C)\le 1\). The equality \(\mathcal H^s(C)=1\), the two facts from Falconer, the Polish form of Prokhorov, and the Moran–Hutchinson theorem are quoted and unused. The carpet has dimension \(\log 8/\log 3\), and the set of numbers with no decimal digit \(7\) has dimension \(\log 9/\log 10\approx 0.954\). Index numbers 12.1 through 12.10 match.

### Chapter 13

Every problem was read, including the hints and the solutions. Borel–Cantelli gives the convergent half of Khinchin. The divergent half uses the Borel–Bernstein comparison for continued-fraction digits, the bound \(q_n\le e^{5n}\) for almost every \(x\), and monotonicity of \(q^2\psi(q)\). The constant \(c\) in that bound is V7-010. Jarník–Besicovitch gives \(\dim_H W(\tau)=2/\tau\). The bounds \(\log 2/(2\log\varphi)=0.7202\ldots\) and \(\log 2/(2\log(1+\sqrt 2))=0.3932\ldots\) were recomputed, as were \(H(1/3)/\log 2=\log_2 3-2/3=0.9183\ldots\), the gap \(2/\sqrt 3-1=0.1547\ldots\), and \(\lvert\hat\mu(1)\rvert=0.37143\ldots\). A high-precision check of the continued fraction of \(e\) finds exactly the nine solutions listed, the last being \(1084483/398959\); the next convergent fails the inequality. The one-sentence gap in the Bernstein set is V7-011. Euler’s expansion of \(e\), Lévy’s constant, Khinchin’s constant, Good’s matching lower bound \(\dim_H D=1/2\), and Jarník’s theorem \(\dim_H\mathrm{Bad}=1\) are quoted and unused. The map at the end of the chapter sends each problem to chapters already proved.

## Not checked

- A TeX run, so unresolved references were not compiled. The 80 index targets were counted in source order and match.
- Portrait files against `photos/CREDITS.md`.
- TikZ coordinate files against their captions, beyond the mathematical claims in the captions that were checked with the prose.
- The equality \(\mathcal H^s(C)=1\), quoted from Hausdorff (1918).
- The value \(0.5312805062772051\ldots\), quoted from Jenkinson and Pollicott.
- The historical fine print against the primary papers, beyond the citations printed in the chapters. The attributions that the text marks as quotations were left as quotations.
