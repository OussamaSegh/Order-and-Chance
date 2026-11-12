# Volume 7, independent scored read

**Book.** *Order and Chance*, Volume 7, *Spaces: Topology, Measure and Limits*.
**Commit reviewed.** `604f29ea416307ef8e0e1b0ac9f99723f533157a` on `main` (the merge of the rewrite, PR #204). No later commit was pulled. A concurrent revision of Volumes 5 and 6 was left out of this reading, as instructed.
**Build reviewed.** The GitHub release `books` points at that commit. Its Volume 7 reading PDF (268 pages, 7 × 10 in), print PDF (267 pages, 7.125 × 10.25 in) and EPUB were the files inspected. They were built by the successful Actions run [43259350073](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43259350073).
**Reader assumed.** A motivated reader who has the calculus of Volume 1 and, for the last chapter, the continued fractions of Volume 2. The bar used below is a careful textbook at that level (Tao, *Analysis I*; Spivak; the early chapters of Folland for the measure-theoretic part), not a research monograph.
**Plan used, and only for structure.** `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-07.md` as they stand on PR #157. No other Volume 7 review, plan, or handoff was opened before the scores and the issue log below were committed.

A 10 is reserved for work with no gap I could find. A numerical check is recorded as a numerical check. It is not a proof.

## Scorecard

### Chapters and the Jordan chapter

Columns are (a) correctness, (b) rigor, (c) prerequisites, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography of the rendered page.

| Chapter | Title | (a) | (b) | (c) | (d) | (e) | (f) | (g) | (h) | (i) | (j) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Sets, Choice and the Real Numbers | 8 | 7 | 8 | 8 | 9 | 8 | 8 | 8 | 8 | 8 |
| 2 | Metric Spaces and Completeness | 9 | 8 | 8 | 9 | 9 | 8 | 8 | 9 | 8 | 8 |
| 3 | Topological Spaces | 8 | 7 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 4 | Compactness | 8 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 5 | Baire's Theorem | 8 | 8 | 8 | 8 | 9 | 7 | 8 | 8 | 8 | 8 |
| 6 | The Jordan Curve Theorem | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 7 | Measures | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 8 | The Lebesgue Integral | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 9 | Product Measures and Change of Variables | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 10 | \(L^p\) Spaces | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 11 | Differentiation and Radon–Nikodym | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 12 | Measures on Metric Spaces | 8 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 13 | Almost every number | 8 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |

**(a)–(b), Chapter 1.** The constructions of \(\mathbb N\), \(\mathbb Z\), \(\mathbb Q\) and \(\mathbb R\), Cantor's theorem, Schröder–Bernstein and the equivalence of choice, Zorn and well-ordering are right, and the Peano and recursion proofs are written out. Inside the uniqueness of \(\mathbb R\) (`ch01-sets.tex:287–289`, Theorem 1.11) the existence of square roots is a one-sentence sketch: “a small rational \(h\)” is not produced. That is the step a reader can get wrong.

**(c), Chapter 1.** The field of fractions is pointed at Volume 3, Chapter 6, which does construct \(\operatorname{Frac} R\) (`volume3-symmetry/chapters/ch06-rings.tex:732`), and the text says the rational case is the same kind of identity, not a citation of a theorem. The injection \(\mathbb N\times\mathbb N\to\mathbb N\), \((m,n)\mapsto 2^m 3^n\), is justified by “unique factorisation” (`ch01-sets.tex:325`) before this volume has proved it.

**(d)–(j), Chapter 1.** The opening (Dedekind, 24 November 1858, sourced in the chapter) and the exercises are the right shape: a computation (Calkin–Wilf, recomputed below), a proof, and a hard recounting. The solutions I recomputed agree with the statements. Figures for the tree, the diagonal and Schröder–Bernstein match their captions.

**(a)–(b), Chapter 2.** Completion, \(\mathbb Q_p\), compactness of \(\mathbb Z_p\), Banach's theorem and Theorem 2.16(a)–(e) on \(\exp\), \(\cos\), \(\sin\) and \(\pi\) were checked line by line. The \(p\)-adic digit expansion and the clopen balls are correct, including \(|x-a|_p\le p^{-n}\) if and only if \(|x-a|_p<p^{-n+1}\). Part (f), the length of the arc \(t\mapsto e^{it}\), defines length as an integral (`ch02-metric.tex:374–375`) before Theorem 8.10 builds that integral. The dependence is the one Volume 1 admitted; it is not marked at the point of use.

**(c)–(j), Chapter 2.** The cosine example uses the mean value theorem from Volume 1 and says so, before Chapter 4 proves it again. Ostrowski is quoted in the prose and not used. The Dottie number, \(\sin 1<0.85\), the Hensel digits \(2,1,2\) in \(\mathbb Z_5\), and \(\phi(1/3)=11/12\) were recomputed and agree. Voice and examples (the calculator, the Sierpiński game, \(\mathbb Z_2\) as the Cantor set) are the best in the book.

**(a)–(f), Chapter 3.** The statements of connectedness, the intermediate-value corollary, Urysohn and Tietze for metric spaces are the standard ones, and the chapter does not use a later volume as a premise. I did not recompute every solution; the exercise score is the score of a sample, not of a complete check. See “Not reviewed”.

**(a)–(b), Chapter 4.** Heine–Borel, the extreme-value corollary, Tychonoff for an arbitrary product (via Zorn, with the use of choice named), Stone–Weierstrass and the polynomial approximation of \(|t|\) are correct. In Arzelà–Ascoli (`ch04-compact.tex:355–361`, Theorem 4.15) the parenthetical builds a \(2\varepsilon\)-net of the value vectors and the next sentence claims an \(\varepsilon\)-net. The \(3\varepsilon\) that follows should be \(4\varepsilon\). Total boundedness still follows, so the theorem stands; the write-up does not.

**(a)–(b), Chapter 5.** Baire's theorem for complete metric spaces and for locally compact Hausdorff spaces, the squeeze lemma, and the proof that the Takagi function is nowhere differentiable were checked and are correct. The difference quotients on dyadic intervals of length \(2^{-k}\) jump by \(\pm 1\) and so cannot converge. Weierstrass's cosine series is not proved. The classical sufficient condition \(ab>1+\tfrac{3\pi}{2}\) with \(b\) odd is stated accurately (Encyclopedia of Mathematics, “Non-differentiable function”; Hardy, *Trans. Amer. Math. Soc.* 17 (1916)), and Hardy's weaker condition \(ab\ge 1\) is attributed but not marked *quoted*. The drawn example \(a=\tfrac12\), \(b=3\) has \(ab=\tfrac32\), which meets Hardy's condition and not Weierstrass's.

**(a)–(b), Chapter 6.** The polygonal parity argument, including a ray through a vertex, and Maehara's proof of the Jordan theorem were read line by line. The lens estimate \(|\operatorname{Im} z|\le\sqrt 3<2\), the crossing lemma, and the four steps that produce exactly two components are correct. The general proof does not depend on the polygons; the chapter says so. The continuous argument uses “the principal logarithm” on the right half-plane (`jordan.tex:36–38`) without a definition. Theorem 2.16 supplies the pieces, but they are not assembled.

**(a)–(b), Chapters 7 and 8.** Dynkin's theorem, uniqueness of measures, the outer measure (including the case \(\mu^*(A_n)=\infty\)), Carathéodory extension, Lebesgue measure and its scaling, Vitali, the fourth-moment bound for normal numbers, and the statement of monotone and dominated convergence are correct. The fourth-moment count \(n+3n(n-1)\) is the right number of surviving tuples, and the bound \(\le 3/(\varepsilon^4 n^2)\) follows. I did not recheck every \(\varepsilon\) in the mode-of-convergence exercises.

**(a)–(b), Chapter 9.** Tonelli, Fubini, the determinant formula for linear maps (shears included), the change-of-variables inequality and its reverse via \(\varphi^{-1}\), polar coordinates, the ball volume and the Gaussian density were checked. The ball formula \(\pi^{d/2}/\Gamma(d/2+1)\) is the standard one (it gives \(2\), \(\pi\), \(\tfrac43\pi\), \(\pi^2/2\) in dimensions \(1\) to \(4\), as the text says). The sentence that every open set is a union of maximal closed dyadic cubes is loose for an unbounded open set; the proof only uses it inside the bounded sets \(U_n\). Sigma-finiteness is stated and the diagonal counterexample is the right one.

**(a)–(b), Chapters 10 and 11.** Hölder's inequality is the usual one; I checked the convolution proposition (Theorem number 10.9) and the approximate-identity argument, not every constant in the exercises. Radon–Nikodym for \(\sigma\)-finite measures, Lebesgue decomposition, the maximal inequality with the factor \(3^d\), differentiation of monotone functions, the fundamental theorem for absolutely continuous functions, conditional expectation and the tower property were checked. The Hahn-decomposition step \((\nu_0-\varepsilon\mu)(P)\ge(\nu_0-\varepsilon\mu)(E)\) is legitimate because the negative set contributes a non-positive number. The conditional-expectation proof really does only use Radon–Nikodym on the sub-sigma-algebra.

**(a)–(b), Chapter 12.** Ulam, the Riesz representation estimate (the constants in `ch11-metricmeasures.tex:70–74` do close), Prokhorov on a compact metric space and on \(\mathbb R^d\), and Kolmogorov's extension were checked. The compactness argument that turns finite additivity into countable additivity is present and correct: if cylinders decrease to empty and stay heavier than \(\delta\), tight compact subsets produce a point in the intersection. Hausdorff dimension of the Cantor set is proved as an outer measure, with \(\tfrac12\le\mathcal H^s(C)\le 1\) for \(s=\log 2/\log 3\), and the facts that \(\mathcal H^s\) is a Borel measure and that \(\mathcal H^d=c_d\lambda_d\) are in a remark headed *quoted, not proved here* and are not used later. The portmanteau theorem (Theorem 12.4, `ch11-metricmeasures.tex:109`) calls the layer-cake formula, and the only proof of that formula is the solution of Exercise 8.4 (`ch07-integral.tex:328` and `:428`). The solution is correct. A flagship proof should not live in an exercise.

**(a)–(c), Chapter 13.** Khinchin's theorem, both halves, is proved from the Borel–Bernstein distortion estimate and Borel–Cantelli, not from the ergodic theorem. The constant \(c=2\sum_{k\ge 1}(k\sqrt{k+1})^{-1}=4.3680\ldots\) was recomputed (\(4.36802\)), and \((2c)^2<77<e^5\) holds. Volume 2 is cited by the numbers it actually has: Proposition 9.1 is the convergent recurrence, Theorem 9.2 the error formula, Lemma 9.4 the best-approximation lemma, Theorem 9.5 Legendre, Theorem 9.6 periodicity of quadratic irrationals (continued fractions are the ninth chapter of Volume 2). Volume 5, Theorem 6.13 is Weyl's criterion. Volume 6, Theorem 5.5 is the prime number theorem. No solution I read uses Volume 11 as a premise. Lévy's constant, Khinchin's constant, Bowen's formula and Good's sharp dimension are marked quoted. Euler's continued fraction for \(e\) is marked quoted and is used, as the problem says.

The census of solutions of \(|e-p/q|<1/(q^2\log q)\) is wrong by one. The eight reduced fractions listed at `ch12-harder.tex:572` do satisfy the inequality, and the next convergent \(13580623/4996032\) does not. The unreduced pair \((p,q)=(6,2)\) also satisfies it: \(|e-3|\approx 0.2817<1/(4\log 2)\approx 0.3607\). Legendre's test does not remove it, because the error is larger than \(1/(2q^2)\). There are nine solutions in integers \(q\ge 2\), eight of them in lowest terms.

**(f), throughout.** Every chapter has a warm-up, a middle exercise and a hard one, except that two problems in Chapter 13 are marked *Journey* rather than with stars (`ch12-harder.tex:96` and `:138`). Solutions I recomputed (Calkin–Wilf, Newton for \(\sqrt 2\), Hensel in \(\mathbb Z_5\), \(\mathbb Z_2\) onto the Cantor set, Khinchin, Borel–Bernstein, the \(e\) bounds, the Jarník–Besicovitch dimension) are right apart from the census just named. The exercise column is a 7 wherever I did not recompute the whole set.

**(g)–(j).** Captions I checked (Calkin–Wilf, maximal function of \(1_{[-1,1]}\), which really is \(1/(|x|+1)\) off \([-1,1]\), Cantor covers with \(\sum(\operatorname{diam})^s=1\), the carpet \(\log 8/\log 3\)) match the mathematics. Plates in the EPUB are PNG and 1800 pixels wide. Rendered chapter pages (a part opener, the Hausdorff-distance definition, the opening of Chapter 12) follow the series page. The preface table does not; it is scored with the front matter, not against a chapter.

### Whole book

| Item | Score |
| --- | ---: |
| Structure and arc | 9 |
| Continuity with Volumes 1–6 | 8 |
| Preparation for Volumes 8–15 | 7 |
| Delivery of the title and subtitle | 9 |
| Front matter, back matter, index, bibliography | 6 |
| Print PDF | 7 |
| EPUB | 8 |

**Structure.** Three parts and thirteen chapters, as the blueprint on PR #157 requires. The arc is the one the preface announces: the real line, then distance, then length, then a limit of measures. Fubini is the debt the earlier volumes named. The last chapter returns to continued fractions. \(\mathbb Z_p\) is proved compact (Corollary 2.11), and \(\mathbb Q_p\) is built here, with its arithmetic deferred to Volume 13 in so many words.

**Continuity.** The preface table lists the admissions I could find in Volumes 4, 5 and 6, and the theorem numbers it prints are the right ones: Tonelli is Theorem 9.5, the integral of a continuous function is Theorem 8.10, Jordan is Theorem 6.10, Lebesgue measure is Theorem 7.11. Volume 5, Chapter 3, line 314, and Chapter 4, line 555, admit Tonelli and name Theorem 9.5. Volume 5, Chapter 5, says it does not have Fubini–Tonelli or the change of variables. Volume 5, Chapter 6, Exercise on Siegel's proof, admits volumes of convex bodies. Volume 6, Chapter 12, admits Tonelli in one solution. Volume 4, Chapter 5, proves the continuous rectangle case and says the general theorem is Volume 7's. I did not re-read every solution in Volumes 5 and 6 to see whether any further admission was left off the table.

**Preparation.** Of the numbered citations of Volume 7 in Volumes 8–15, almost all point at the statement they describe. Theorem 2.10 is \(\mathbb Q_p\), Theorem 4.19 is Stone–Weierstrass, Theorem 9.5 is Tonelli, Theorem 9.8 is the change of variables, Theorem 11.4 is Radon–Nikodym, Theorem 11.17 is the tower property, Theorem 12.7 is Prokhorov in the form actually proved (compact metric spaces and \(\mathbb R^d\)), Theorem 12.8 is Kolmogorov. Volume 14 does not cite Volume 7. Three citations do not resolve. They are V7-03, V7-04 and V7-05 below. That is why this score is not a 9.

**Title.** *Spaces: Topology, Measure and Limits* is what the book is. The subtitle of the series is not argued here; the preface's last paragraph says what this floor contributes, and it is accurate.

**Front and back matter.** The blurb matches the contents, including the honest sentence that a few results are quoted. Each chapter has a “Sources and further reading” section, and the historical claims I checked (Dedekind's date, the Weierstrass condition, the ball formula) are sourced or standard. There is no index. Only the Jordan chapter puts its sources into the table of contents (`jordan.tex:283`). The debts table, which is the page a reader will trust, is badly set (V7-01).

**Print PDF.** Every page is 513 × 738 pt, which is the 7.125 × 10.25 in bleed page the series requires. The reading PDF is 504 × 720 pt. The print file has 267 pages (the reading file's extra page is the cover). I did not repeat the series' bleed-pixel comparison. The debts table is in the print file as well as the reading file.

**EPUB.** 18 MB, under the 50 MB cap. Thirty-two plates, each a PNG of width 1800. The stylesheet sets `figure img, img.oc-plate { width: 100%; max-width: 100%; height: auto; }`, and inline mathematics carries an em width and a `vertical-align` in em. I did not open it on a Kindle.

### Overall

**8.**

The constructions a reader will be examined on — the reals, \(\mathbb Q_p\), Baire, Jordan, Lebesgue measure, Tonelli and Fubini, the change of variables, Radon–Nikodym, conditional expectation, Prokhorov on \(\mathbb R^d\), Kolmogorov, and Khinchin — are proved, and the proofs I checked are the right proofs. Quoted results are marked, and the ergodic theorem is not smuggled into the last chapter. I would recommend the book to a strong reader who wants one path from sets to a limit of measures.

I would not call the press file finished. The preface ledger is mis-set, one flagship argument is an exercise solution, three later volumes still point at the wrong line, and there is no index.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V7-01 | `chapters/preface.tex:31–43`; reading PDF p. vi (sheet 7); same table in the print PDF | Typography | major | The third column is justified in a narrow `p` column. “Theorems 1.10 and 1.11” breaks so that `1.10` sits on the right margin, level with the next row (“the functions exp, cos, sin”), and “and 1.11” wraps under it. The same stretch hits “Theorems 9.6, 9.8 and 9.4” and “Theorem 7.11 and Chapter 9”. The numbers are the right numbers; a reader cannot see which row they belong to. | Set the third column ragged-right, or stack each reference on its own line. |
| V7-02 | `chapters/ch11-metricmeasures.tex:109` (Theorem 12.4, portmanteau); the formula is Exercise 8.4, `chapters/ch07-integral.tex:328` and solution at `:428` | Rigor | major | The step \((e)\Rightarrow(a)\) of the portmanteau theorem cites the layer-cake formula and says it is proved in the solution of an exercise. That solution is complete and correct. It is the only proof, and a later flagship uses it. The master plan's exercise rule (section 6.5 on PR #157) forbids exactly this. | Promote the layer-cake formula to a lemma in Chapter 8 and cite the lemma. |
| V7-03 | Citing line: `volume8-analysis/chapters/ch08-haar.tex:67`. Target that the sentence needs: Theorem 7.5, `chapters/ch06-measures.tex:80`. What “Theorem 6.5” actually is: the definition of the winding number, `chapters/jordan.tex:42` | Downstream citation | major | Haar uniqueness ends with “compact sets form a \(\pi\)-system; they generate the Borel sets… Theorem 6.5 of Volume 7 concludes.” Uniqueness of measures that agree on a \(\pi\)-system is Theorem 7.5. Item 6.5 is the definition of \(n(\gamma,a)\). The number is the measures chapter's old number, from when that chapter was still Chapter 6. | Cite Theorem 7.5. |
| V7-04 | Citing line: `volume8-analysis/chapters/ch05-fourier.tex:210`. The density of simple functions is Proposition 10.6, `chapters/ch09-lp.tex:131` | Downstream citation | major | The Hausdorff–Young argument says simple functions approximate in \(L^1\) and in \(L^p\) “by Proposition 9.6 of Volume 7”. Proposition 9.6 is Fubini. Two lines earlier the same chapter cites Proposition 10.6 for the same fact, correctly. | Cite Proposition 10.6. |
| V7-05 | Citing line: `volume9-shapes/chapters/ch03-forms.tex:347`. The winding number is Definition 6.5, `chapters/jordan.tex:42–44`, which follows Lemma 6.4 (`jordan.tex:31`) | Downstream citation | major | “The winding number of Volume 7 (the definition after Lemma 6.1)”. There is no Lemma 6.1. Item 6.1 is the polygonal Jordan theorem (`jordan-polygon.tex:7`). The continuous argument is Lemma 6.4; the definition is the next item, 6.5. The same chapter's citation of Lemma 6.4 itself is right. | Say “Definition 6.5, after Lemma 6.4”. |
| V7-06 | `volume7-spaces/main.tex` (no index is input); reading PDF outline ends at “About the Cover” | Front matter | major | The reading PDF has no index. Volume 2, in the same series, has one. A 267-page book whose later volumes cite it by theorem number is hard to use without one. | Generate an index from the theorem captions and the names already in the sources sections. |
| V7-07 | `chapters/ch01-sets.tex:287–289`, inside Theorem 1.11 | Rigor | minor | “Every \(x\ge 0\) is a square: \(s=\sup\{q:q^2<x\}\) satisfies \(s^2=x\) (if \(s^2<x\), then \((s+h)^2<x\) for a small rational \(h>0\)…).” The \(h\) is not chosen. The rest of the uniqueness proof is complete. | Write \(h=\min\bigl(1,(x-s^2)/(2s+2)\bigr)\) or the usual estimate. |
| V7-08 | `chapters/ch02-metric.tex:374–375`, Theorem 2.16(f) | Prerequisites | minor | Arc length is defined as \(\int_a^b|\gamma'|\) and evaluated, before Theorem 8.10. Parts (a)–(e), which pay the Volume 1 debt on \(\exp\) and \(\pi\), do not use it. The preface lists the integral as a debt discharged by Theorem 8.10; this sentence does not say that. | Mark the integral as the one Volume 1 admitted, discharged by Theorem 8.10, or postpone (f) until Chapter 8. |
| V7-09 | `chapters/ch12-harder.tex:570–572`, Problem 13.5(c); reading PDF folio 227 | Correctness | minor | The eight reduced fractions are solutions, and the next convergent is not (recomputed). So is \((p,q)=(6,2)\): \(\lvert e-3\rvert\approx 0.2817 < 1/(4\log 2)\approx 0.3607\). The text says a check of the convergents and of \(q<8\) “gives the eight solutions” and then lists only the reduced ones. | Either count nine integer solutions, or say “eight in lowest terms” and note that \(6/2\) repeats the value \(3\). |
| V7-10 | `chapters/ch04-compact.tex:355–361`, Theorem 4.15 | Rigor | minor | The parenthetical produces a \(2\varepsilon\)-net (“\(2\varepsilon\)-balls”). The next sentence claims \(\lVert v(f)-v(f_l)\rVert_\infty<\varepsilon\), and the display concludes \(<3\varepsilon\). With the net actually constructed the bound is \(<4\varepsilon\). Relative compactness is unaffected. | Choose the net at scale \(\varepsilon\), or write \(4\varepsilon\). |
| V7-11 | `chapters/jordan.tex:36–38`, Lemma 6.4 | Rigor | minor | The lift is built from \(\operatorname{Im}\operatorname{Log}\) on the right half-plane. Theorem 2.16 gives \(\exp\), \(\ln\) on \((0,\infty)\), and the argument of a point of the circle. It does not define \(\operatorname{Log}\) on \(\{\operatorname{Re}>0\}\). | Add two lines: for \(\operatorname{Re} w>0\) there is a unique \(t\in(-\pi/2,\pi/2)\) with \(w=\lvert w\rvert e^{it}\), and set \(\operatorname{Log} w=\ln\lvert w\rvert+it\). |
| V7-12 | `chapters/ch01-sets.tex:325`, Proposition 1.13(b) | Prerequisites | minor | \((m,n)\mapsto 2^m 3^n\) is called injective “by unique factorisation”. That fact is Volume 2's, and this chapter's stated premise is Volume 1. The injection has a short proof from the recursion theorem already proved. | Prove it, or cite Volume 2, Theorem 1.6, and accept Volume 2 as a premise of this one paragraph. |
| V7-13 | `chapters/ch06-measures.tex:199–202`, after Theorem 7.11 | Prerequisites | minor | A coordinate hyperplane is shown null by a cover. “Any hyperplane is a rotation of this one; Chapter 9 shows that rotations preserve \(\lambda_d\).” Faces of boxes, which are all this paragraph needs for the open/closed distinction, are coordinate. The forward reference is for the general case only. | Prove the coordinate case, and postpone tilted hyperplanes to the sentence in Chapter 9 that already has the determinant. |
| V7-14 | `chapters/ch05-baire.tex:131–140` and Figure `figures/ch05-weierstrass.tex` | Quoted results | minor | The text states Weierstrass's condition \(ab>1+3\pi/2\), then says Hardy showed \(ab\ge 1\) suffices, then draws \(a=1/2\), \(b=3\) (\(ab=3/2\)). The figure is not an instance of the inequality just stated, and Hardy's theorem is not marked *quoted*. Takagi's function, which is proved, is the theorem of the section. | Mark Hardy's statement *quoted*, and say that the drawing meets Hardy's condition rather than Weierstrass's. |
| V7-15 | `chapters/jordan.tex:282–283`; every other chapter's sources section is starred and not in the contents | Front matter | minor | `\addcontentsline` appears only for the Jordan sources. The other twelve source lists are invisible in the table of contents and in the PDF outline. | Add the same line to each, or to none. |
| V7-16 | `chapters/ch12-harder.tex:96`, `:138` | Notation | minor | The preface promises three grades, star, two stars, three stars. Problems 13.4 and 13.8 are marked *Journey*. | Use three stars, or add *Journey* to the preface's scale. |
| V7-17 | `chapters/ch08-products.tex:305–306` | Numerical | minor | \(0.9^{100}=2.656\times 10^{-5}\), printed as \(\approx 3\times 10^{-5}\). The companion values \(\pi^{50}/50!\approx 2.37\times 10^{-40}\) (printed \(2.4\times 10^{-40}\)) and \(2^{100}\approx 1.27\times 10^{30}\) (printed \(1.3\times 10^{30}\)) are fair one-figure approximations. The fraction \(2\times 10^{-70}\) matches \(2.37\times 10^{-40}/1.27\times 10^{30}\) at one figure. | Print \(2.7\times 10^{-5}\), or say “about \(10^{-5}\)”. |
| V7-18 | `volume9-shapes/chapters/ch01-manifolds.tex:539`, citing Theorem 7.11 | Downstream citation | minor | The sentence uses “a null set may be covered by cubes of total volume \(<\varepsilon\)”. That is the definition of outer measure in Theorem 7.10, together with \(\lambda=\lambda^*\). Theorem 7.11 is the measure of boxes, translation, and scaling. The fact is true and nearby; the number is one off in spirit. | Cite Theorem 7.10, or the sentence after Theorem 7.11 that discusses null covers. |

Severity counts: **critical 0, major 6, minor 12.**

## Verified correct

These were checked as proofs, not as numerical illustrations. “Checked” means the hypotheses are the ones used, and each step follows.

- **Peano, recursion, and the semiring structure of \(\mathbb N\)** (Theorems 1.2, 1.3, Proposition 1.4). The transitive-set argument for injectivity of the successor is complete.
- **The field \(\mathbb R\)** (Theorem 1.10): inverses, order, Archimedes, density, completeness of Cauchy sequences, least upper bounds by bisection. The identification of a positive element is independent of the representative.
- **Cantor, Schröder–Bernstein, and \(|\mathbb R|=|\mathcal P(\mathbb N)|\)** (Theorems 1.14–1.16). The injection by ternary series differs by at least \(3^{-n-1}\); the geometric sum was recomputed and equals that bound.
- **Zorn, and the equivalence with choice and well-ordering** (Theorems 1.19, 1.20). The comparison of \(g\)-sets is the standard one and is written out.
- **Completion** (Theorem 2.9), Kuratowski's embedding, with the note that it cannot be used to build \(\mathbb R\).
- **\(\mathbb Q_p\) and the compactness of \(\mathbb Z_p\)** (Theorem 2.10, Corollary 2.11). Digits, compatible residue sequences, clopen balls, sequential compactness, local compactness, and the unbounded sequence \(p^{-n}\).
- **Banach's fixed-point theorem** (Theorem 2.12), including both error bounds.
- **Theorem 2.16(a)–(e)**: the Cauchy product, \(\exp(z+w)\), \(|e^{it}|=1\), the first positive zero of cosine (the alternating bound \(\cos 2\le -1/3\) is true; \(\cos 2\approx -0.416\)), and the argument that \(e^{it}\ne 1\) on \((0,2\pi)\). This last is Rudin's argument, as the sources say, and the arithmetic \(1/4-6/4+1/4=-1\) is right.
- **Hutchinson's theorem** (Theorem 2.20): the Hausdorff metric makes the set map a contraction. The displayed formula for \(d_H\) has no stray bar; the rendered page 35 of the chapter (reading PDF sheet 48) shows the formula as written.
- **Baire** (Theorem 5.2) in both forms, and the dependence on countable dependent choice, which the text names.
- **Takagi** (Theorem 5.6). Slopes of the early terms are \(\pm 1\) on the dyadic interval, later terms vanish at the endpoints, and the difference quotients do not converge.
- **Tychonoff for a general product** (Theorem 4.11), including the two uses of choice. The finite-intersection property passes to the projected closures.
- **Stone–Weierstrass** (Theorem 4.19) and the bound \(0\le |t|-p_n(t)\le 2/(en)\).
- **Polygonal Jordan** (Theorem 6.1), including the parity at a vertex, and **Maehara's proof of the Jordan theorem** (Theorem 6.10). The rectangle, the lens, and the three appeals to the crossing lemma were checked. The proof does not use the polygonal case.
- **Dynkin, uniqueness, outer measure with the infinite term, Carathéodory extension, Lebesgue measure** (Theorems 7.4, 7.5, 7.7, 7.10, 7.11). Scaling \(t^d\) and the characterisation by the unit cube are included.
- **Vitali** (Theorem 7.15). The translates by \(\mathbb Q\cap[-1,1]\) sit in \([-1,2]\), and \(\mu([-1,2])\le 3\mu([0,1])\).
- **Borel normality** (Theorem 7.19), including the fourth-moment count.
- **Tonelli and Fubini** (Theorems 9.5, 9.6), with sigma-finiteness, and the diagonal counterexample when it is dropped.
- **Linear images and the change of variables** (Theorems 9.7, 9.8). The shear has slices of length 1. The passage from cubes to functions, and the reverse inequality through \(\varphi^{-1}\), close.
- **Polar coordinates, the ball, the Gaussian density** (Theorems 9.10–9.12). \(\int_{\mathbb R}e^{-x^2}\,dx=\sqrt\pi\) is the computation the text gives, and it is right. The Jacobian of \(z\mapsto Az+m\) produces the displayed Gaussian density.
- **Radon–Nikodym, Lebesgue decomposition, conditional expectation, the tower property** (Theorems 11.4, 11.5, 11.16, 11.17).
- **Lebesgue differentiation and the fundamental theorem for absolutely continuous functions** (Theorems 11.9, 11.14), including the comparison of \([x,x+h]\) with \(B(x,2h)\) in dimension one.
- **Riesz representation on a compact metric space** (Theorem 12.3). The \(\varepsilon\)-budget in the displayed estimate was expanded and matches the text.
- **Prokhorov** in the form stated (Theorem 12.7): every sequence on a compact metric space, and every tight sequence on \(\mathbb R^d\). The general Polish equivalence is marked quoted and unused. The portmanteau inequality used for the closed set \(\varphi(K)\) goes the right way: \(\nu(\varphi(K))\ge\limsup\nu_n(\varphi(K))\).
- **Kolmogorov** (Theorem 12.8). Finite additivity is written down. Countable additivity is the compact-cylinder argument. The diagonal extraction produces a point of every \(K_j\).
- **Cantor dimension** (Theorem 12.11). For \(3^{-k-1}\le\operatorname{diam} U<3^{-k}\), a closed \(U\) meets at most one interval of stage \(k\), and \(\mu_c(U)\le 2(\operatorname{diam} U)^s\). Hence \(\mathcal H^s(C)\ge 1/2\), and the stage-\(n\) cover gives \(\mathcal H^s(C)\le 1\).
- **Khinchin** (Problem 13.4), both halves, from distortion (Problem 13.3) and Borel–Cantelli. The comparison \(\sum_{Q_{n-1}<q\le Q_n}q\psi(q)<6f(Q_{n-1})\) uses \(\ln 150<6\) and \(Q_n/Q_{n-1}<150\). Both numerical claims hold.
- **The debts table's references**, as numbers: 1.10 and 1.11, 2.16, 8.10, 9.5, 9.5 and 9.6, 9.6 with 9.8 and 9.4, 7.11 with Chapter 9, 6.10. Each is the theorem the row describes. The defect is the typesetting (V7-01), not the assignment.
- **Numbered back-references into Volumes 2, 5 and 6** that this volume uses as premises of the last chapter: Volume 2, Proposition 9.1, Theorem 9.2, Lemma 9.4, Theorems 9.5 and 9.6; Volume 5, Theorem 6.13; Volume 6, Theorem 5.5. The counters in those chapters were enumerated. The labels match.

### Numerical checks (not proofs)

| Claim | Location | Result |
| --- | --- | --- |
| Dottie number \(0.7390851332\ldots\) | `ch02-metric.tex:294` | Iteration of cosine from \(0.5\) gives \(0.739085133215\). |
| \(\sin 1<0.85\) | `ch02-metric.tex:294` | \(\sin 1\approx 0.84147\). |
| \(\cos 2\le -1/3\) | `ch02-metric.tex:363` | The alternating bound is valid on \([0,2]\); \(\cos 2\approx -0.416\). |
| Hensel digits of a square root of \(-1\) in \(\mathbb Z_5\) start \(2,1,2\) | solution of Exercise 2.7, `ch02-metric.tex:627–628` | \(T(2)\equiv 7\pmod{25}\), \(T(7)\equiv 57\pmod{125}\), \(57=2+1\cdot 5+2\cdot 25\), and \(57^2+1=26\cdot 125\). |
| \(\phi(1/3)=11/12\) | solution of Exercise 2.9, `ch02-metric.tex:664` | The digit sum is \(2/3+1/4\). |
| Calkin–Wilf \(q_1,\ldots,q_{10}\) | solution of Exercise 1.10, `ch01-sets.tex:691–694` | \(1,1/2,2,1/3,3/2,2/3,3,1/4,4/3,3/5\). |
| \(q_{43}=13/5\) | same solution, `:700` | The path \(L,R,L,R,R\) from the root has index \(43\). |
| \(c=4.3680\ldots<4.4\), \((2c)^2<77<e^5\) | `ch12-harder.tex:527–530` | \(c=4.368019\), \((2c)^2=76.22\), \(e^5\approx 148.41\). |
| Ball volumes \(2,\pi,4\pi/3,\pi^2/2\) | `ch08-products.tex:297` | The Gamma formula returns these four values. |
| \(\lambda_{100}(B^{100})=\pi^{50}/50!\approx 2.4\times 10^{-40}\) | `ch08-products.tex:305` | \(2.368\times 10^{-40}\). |
| \(\log 2/\log 3\approx 0.631\), \(\log 8/\log 3\approx 1.893\) | Theorem 12.11; carpet caption | \(0.6309\) and \(1.8928\). |
| Lévy's constant \(\pi^2/(12\log 2)=1.1866\ldots\), quoted | `ch12-harder.tex:550` | \(1.18657\). The text marks it quoted. |
| Eight listed approximations to \(e\) | `ch12-harder.tex:572` | Each satisfies the strict inequality; see V7-09 for the missing ninth. |
| Maximal function of \(1_{[-1,1]}\) | caption of `figures/ch10-maximal.tex`, discussed at `ch10-radon.tex:148` | For \(x>1\) the supremum of the averages is \(1/(x+1)\), attained at radius \(x+1\). |

### Conformance to the blueprint on PR #157

The blueprint was used as a list of contents, not as a review.

The printed book has the thirteen chapters the blueprint names, in that order, with Jordan as Chapter 6 and the file `ch06-measures.tex` printed as Chapter 7. Corollary 2.11 is the compactness of \(\mathbb Z_p\), and local compactness of \(\mathbb Q_p\), which decisions D-14 and D-17 asked for. The preface has the debts table. The last chapter does not take the Gauss map, Birkhoff, or Lévy's theorem as premises; it says the ergodic proofs live in Volume 11. Hausdorff measure is quoted (Remark 12.9, `ch11-metricmeasures.tex:201`) and is not then used as a measure built in the book. The infinite term in the subadditivity of outer measure is written (`ch06-measures.tex:150`). Finite additivity of the cylinder set function is written before Kolmogorov (`ch11-metricmeasures.tex:172`).

Two differences, neither of them a false theorem. The blueprint's size estimate was 200–230 pages and was marked “not measured”; the print PDF has 267 pages. The blueprint's sentence about the cover still says the Sierpiński carpet. The book that was printed has the Cantor staircase on the cover, and the preface, the opening of Chapter 12, and “About the Cover” all say so. The carpet is a figure and an exercise, with dimension \(\log 8/\log 3\).

## Not reviewed

- Every exercise solution in Chapters 3, 4, 5, 7, 8, 10 and 11, and the solutions in Chapter 13 after Jarník–Besicovitch (equidistribution, the Koksma argument, category versus measure, the Bernstein set). The solutions that were read are named above.
- The second half of a few long exercises whose statements I read and whose write-ups I did not: Picard–Lindelöf was read; several \(L^p\) exercises were not.
- A line-by-line reading of the Arzelà–Ascoli proof beyond the net argument, of Tietze's proof, and of the modes-of-convergence section in Chapter 8.
- Whether every historical date in the sources sections is accurate. The ones I checked are named.
- Every TikZ figure against its caption. The plates' pixel widths were checked; four rendered pages were looked at (the debts table, a part opener, the Hausdorff-distance definition, the opening of Chapter 12).
- The EPUB on a Kindle. The stylesheet and the image sizes were checked from the file.
- A bleed-pixel comparison of the print PDF. The media box is the required 513 × 738 pt on every page.
- The internal development of the integral and the mean value theorem inside Volume 1. This volume treats them as admitted and replaces them by Theorems 8.10, 4.5 and 4.10.
- Whether every solution in Volumes 5 and 6 that admits a Volume 7 theorem is listed in the preface. The admissions I found by searching those volumes are listed.
- The proofs in Volumes 8–15 that cite Volume 7, beyond the sentence that names the citation. The check was: the number exists, the environment type matches, and the sentence's claim is the statement of that item.
- Volume 14, which does not mention Volume 7.
- Anything in `docs/review/`, `docs/handoffs/`, or other Volume 7 plan files. Those were not opened before this scorecard and this issue log were committed.
