# Volume 13 fix, second review — 22 November 2026

Independent reading of PR #266. The fixes were written by another agent. The head under review was `e6c61316cc57cd077a517342e5a866db0831d006`. This reading found four gaps in the new proofs. They are repaired in `665391b3ff46bd6fe18e70d58a571e46e88921f3`. This log is the following commit on `cursor/fix-volume13-review`.

The issue list is `docs/review/series-sequential-review/volume13.md` on `cursor/series-sequential-review` at `2691145e6a366f1ed2cbc6968802ad899f7069de`. The state-after-Volume-K comments on PR #253 were read through the Volume 12 comment (`7075783113`). `origin/main` for this reading is `f2b5a67cfab8b39d4afa18ce4165ac8f229808f5`.

## Verdicts

**Correctness.** All eight issues are fixed, and none was declined. No numbered statement was shortened. The four findings below were holes in the new arguments for V13-002, V13-003 and V13-007. The repairs stay inside `volume13-arithmetic/` and do not change a numbered statement.

**V13-001.** The preface and `kdp.md` no longer say “journey”. Both keep the map: number fields, the \(p\)-adic numbers, curves, and the modular forms that tie them together. A search of `volume13-arithmetic/` finds no remaining “journey”.

**V13-002.** Volume 5, Corollary 9.17 is `cor:fta`: every non-constant complex polynomial has a root in \(\C\). Volume 3, Lemma 8.12 is `lem:extend1`: an isomorphism of the base field extends uniquely along a root of an irreducible polynomial. Volume 3, Theorem 8.9 remains Kronecker’s abstract root and is no longer cited for the embedding. On `e6c61316` the new sentence applied those two results to “a primitive element”. Volume 3, Theorem 8.20, the primitive-element theorem cited in the reminder two paragraphs earlier, produces one generator only for an extension that is already a subfield of \(\C\). That is the conclusion the sentence is justifying. SR-001 replaces it by a finite basis. Volume 3, Corollary 8.7 says each basis element is algebraic. Corollary 9.17 and Lemma 8.12 adjoin the first element, and the same two steps, applied to the minimal polynomial over the subfield already reached, adjoin each later element.

**V13-003.** The unnumbered proposition `prop:purecubic` is the standard pure-cubic rule for squarefree \(m\ne 0,\pm 1\): the index of \(\Z[\theta]\) is \(3\) exactly when \(m\equiv\pm 1\pmod 9\), with basis \(1,\theta,(1+s\theta+\theta^2)/3\), and is \(1\) otherwise. That is the squarefree case of the statement quoted from Marcus, *Number Fields*, end of Chapter 2, Exercise 41, and from Marcus, pp. 35–36, as cited by Aygin–Nguyen, arXiv:2009.02442. The sign \(s=\pm 1\) is the residue of \(m\). The algebra of the proof does not use \(m>0\).

The index formula is Proposition `prop:index`: \(\operatorname{disc}(1,\theta,\theta^2)=[\mathcal O_K:\Z[\theta]]^2 d_K\). Proposition `prop:disc`(c) with \(n=3\) gives \(\operatorname{disc}(1,\theta,\theta^2)=(-1)^3 N(3\theta^2)=-27m^2\), since \(N(\theta)=m\) and \(N(3)=27\). So the square of the index divides \(27m^2\). A prime divisor of the index divides \(3m\).

If a prime \(q\) divides \(m\), then \(X^3-m\) is \(q\)-Eisenstein, because \(m\) is squarefree. Proposition `prop:eisenstein` says \(q\) does not divide the index. In particular, if \(3\) divides \(m\), the index is \(1\), and such an \(m\) is \(3\) or \(6\) modulo \(9\).

If \(3\) does not divide \(m\), then \(v_3(27m^2)=3\), so the power of \(3\) in the index is \(0\) or \(1\). The translate \((X+m)^3-m=X^3+3mX^2+3m^2X+(m^3-m)\) is the minimal polynomial of \(\theta-m\), and \(\Z[\theta-m]=\Z[\theta]\). On `e6c61316` the proof asserted that \(9\) divides the constant term if and only if \(m\equiv\pm 1\pmod 9\), without the residues. SR-002 writes them. The residues not divisible by \(3\) are \(1,2,4,5,7,8\), and their squares modulo \(9\) are \(1,4,7,7,4,1\). So \(m^2\equiv 1\pmod 9\) exactly for \(m\equiv\pm 1\), and then \(9\) divides \(m^2-1\). For the other four residues, \(m^2-1\equiv 3\) or \(6\pmod 9\), so the translate is \(3\)-Eisenstein and the index is \(1\). Irreducibility of \(X^3-m\) is Volume 1, Theorem 6.10, not Proposition `prop:eisenstein`. That proposition assumes the polynomial is already minimal and concludes only that the prime does not divide the index. The repair cites Theorem 6.10 at the place the degree is deduced.

When \(m=9t+s\) with \(s=\pm 1\), the difference of cubes gives \((\theta-s)(1+s\theta+\theta^2)=9t\). Clearing the denominator produces the monic equation \(\beta^3-\beta^2-3st\beta-3t^2=0\). For \(m=10\) this is the equation already in Example `exa:cuberoot10`. An exact reduction in \(\Z[\theta]/(\theta^3-m)\), for every squarefree \(m\) from \(-80\) to \(80\) with \(m\equiv\pm 1\pmod 9\), gave the zero remainder: \(24\) values, no failures. Then \(3\beta\in\Z[\theta]\) and \(\beta\notin\Z[\theta]\), so the index is exactly \(3\).

On `e6c61316` the index \([M:\Z[\theta]]\) was read off a change-of-basis matrix of determinant \(1/3\). That matrix is not integral, and Volume 3, Corollary 7.8 applies to an integer matrix. SR-003 writes the basis \(1,\theta,\theta^2\) in the basis \(1,\theta,\beta\) of \(M\). The matrix is triangular with diagonal \(1,1,3\) and determinant \(3\), so \([M:\Z[\theta]]=3\). Both quotients over \(\Z[\theta]\) have order \(3\), and \(M\subseteq\mathcal O_K\), so \(M=\mathcal O_K\) and \(d_K=-3m^2\).

The sentence after the proof is now the right reading of a repeated factor. A repeated root of \(m_\theta\) modulo \(p\) means \(p\) divides \(\operatorname{disc}(m_\theta)\). The index formula splits that into \(p\) dividing the index, or \(p\) dividing \(d_K\). Theorem `thm:ramdisc` in Chapter 4 says the second alternative is ramification. Theorem `thm:kd` assumes \(p\) does not divide the index, and a repeated factor is then an exponent \(e_i\ge 2\). The chapter summary says the same two sentences. The repeated root is not, by itself, a test for the index.

**V13-004.** Volume 3, Proposition 6.5 is `prop:quotring`, the construction of the quotient ring. Proposition 6.8 is `prop:primemax`: an ideal \(I\ne R\) is prime if and only if \(R/I\) is a domain, and maximal if and only if \(R/I\) is a field. Proposition 6.3 is `prop:finitedomain`: a finite integral domain is a field. The reminder now says that.

**V13-005.** Volume 3, Theorem 3.11 is `thm:cauchy`: a prime dividing the order of a finite group is the order of some element. The proof of `prop:eisenstein` uses it for that step and for nothing else.

**V13-006.** The only change in the caption of `fig:lattice` is the phrase “circled in ochre”. The `\caption` command, the label, and the rest of the sentence are the same. `figures/ch11-lattice.tex` is not in the diff. The fill of \(P\) is `MidnightBlue`, which `common/figure-palette.tex` defines as `#151516` and names charcoal. The circles of \((2)\) are `ForestGreen!70!black`. The same file defines `ForestGreen` as `#B08D57` and names it ochre. The caption uses those two names.

**V13-007.** For \(\Q(\sqrt[3]7)\), \(7\not\equiv\pm 1\pmod 9\), so `prop:purecubic` gives \(\mathcal O_K=\Z[\theta]\) and \(d_K=-27\cdot 49=-1323\). The Minkowski bound is
\[
M_K=\frac4\pi\cdot\frac6{27}\sqrt{1323}=\frac{56\sqrt3}{3\pi}.
\]
The inscribed regular hexagon gives \(2\pi>6\), and \((7/4)^2=49/16>3\), so \(\sqrt3<7/4\). Hence \(M_K<98/9<11\). Numerically \(M_K=10.291\ldots\). Every class contains an ideal of norm at most \(M_K\), so the class group is generated by the prime ideals of norm at most \(10\).

Kummer–Dedekind, which applies because the index is \(1\), was recomputed directly:

- Modulo \(2\), \(X^3-1=(X-1)(X^2+X+1)\) and the quadratic has no root. So \(2\mathcal O=PQ\) with norms \(2\) and \(4\).
- Modulo \(3\), \(X^3-7\equiv(X-1)^3\). So \(3\mathcal O=R^3\) with norm \(3\).
- Modulo \(5\), the only root is \(3\), and \(X^2+3X+4\) has discriminant \(-7\equiv 3\), not a square modulo \(5\). So \(5\mathcal O=ST\) with norms \(5\) and \(25\).
- Modulo \(7\), \(X^3\equiv 0\) and \((\theta)^3=(7)\).

The prime ideals of norm at most \(10\) are \(P\), \(Q\), \(R\), \(S\) and \((\theta)\). No prime ideal has norm \(8\), \(9\) or \(10\).

On `e6c61316` the norm \(a^3+7b^3+49c^3-21abc\) was introduced as “the same shape” as the formula for \(\sqrt[3]2\). SR-004 writes the multiplication matrix, the Chapter 3 matrix with \(2\) replaced by \(7\), and the expansion
\[
a(a^2-7bc)-7c(ab-7c^2)+7b(b^2-ac)=a^3+7b^3+49c^3-21abc.
\]
The determinant identity was checked for seven values of \(m\), including \(7\), and for coefficients in a box of side about \(6\): no failures. Every term but \(a^3\) is divisible by \(7\). The cubes modulo \(7\) are \(0,1,-1\), as Example `exa:cubesplit` records, and none of \(\pm 2,\pm 3,\pm 4,\pm 5\) is congruent to one of those. A search with \(|a|\le 12\), \(|b|\le 8\), \(|c|\le 6\) found no element of those norms. So \(P\), \(R\) and \(S\) are not principal.

The principal ideals were recomputed from the same polynomial: \(N(1+\theta)=8\), \(N(1-\theta)=-6\), \(N(2+\theta)=15\), \(N(\theta)=7\). Then \((1+\theta)=P^3\), because the other candidate \(PQ=(2)\) would make \((1+\theta)/2\) a unit of trace \(3/2\). The class of \(P\) therefore has order \(3\). From \(N(1-\theta)=-6\) one gets \((1-\theta)=PR\), and from \(N(2+\theta)=15\) one gets \((2+\theta)=RS\). With \(PQ=(2)\) and \((\theta)\) principal, every generator is trivial or equal to \([P]\) or \([P]^2\). Hence \(h_K=3\).

The other class numbers are marked as computations, and the arguments that are proved are not. For \(p\le 19\) and for \(p=23\), the text says a class-group computation gives \(h_p=1\) and \(h_p=3\), and that neither value is proved in this book. The values \(h_{37}=h^-=37\) and \(h_{37}^+=1\), and the table of \(h^-\) through \(p=41\), are labelled computations. The factorisation \(7709321041217=37\cdot 683\cdot 305065927\), which is what the chapter uses to show \(37\mid h_{37}\), is unchanged and is not folded into that label.

The \(2\times 2\) minor for \(\theta=2\cos(2\pi/7)\) and \(1+\theta\) was recomputed from the three real embeddings. Deleting any one column gives absolute value \(0.52545468\ldots\), which rounds to the printed \(0.5255\). The Euclidean area of the parallelogram in the plane \(x_1+x_2+x_3=0\) is \(\sqrt3\) times that minor, \(0.910114\ldots\), which rounds to the printed \(0.910\). The exercise proves that the minor is non-zero, so the two units are independent, and it says that the minor is the regulator of the subgroup they generate with \(-1\). That the subgroup is the full unit group is marked as a computation, both in the solution and in the caption. The figure file is not in the diff.

**V13-008.** The sentence after Minkowski’s discriminant bound keeps the sphere as a local analogy and no longer points at Chapter 13. Chapter 13, `ch10-cft.tex`, does not mention the sphere or a covering map. It still uses \(|d_K|>1\).

**Concept order.** The new appeals are to tools already proved. Eisenstein’s irreducibility criterion is Volume 1, Theorem 6.10. The basis and the algebraicity of a finite extension are Volume 3, Corollary 8.7 and Lemma 8.12, with the fundamental theorem of algebra as Volume 5, Corollary 9.17. The index of an integer matrix is Volume 3, Corollary 7.8, already used in the proof of the index formula. Cauchy’s theorem, the quotient ring, and the prime and maximal tests are the Volume 3 numbers in V13-004 and V13-005. The class-number argument uses the pure-cubic proposition from Chapter 3, Kummer–Dedekind and the ramification theorem from Chapter 4, and Minkowski’s bound from earlier in Chapter 5.

**Labels and numbering.** Against `origin/main`, the TeX files under `volume13-arithmetic/` have the same labels, plus the new unnumbered label `prop:purecubic`. There are \(538\) labels, \(537\) of them on main, with no removals and no change of multiplicity. The numbered-environment counts are unchanged: \(206\) exercises, \(82\) theorems, \(70\) propositions, \(56\) lemmas, \(28\) corollaries, \(28\) definitions, and \(13\) examples. The one new environment is `propositionx`, which does not step the shared counter. `python3 tools/cross_volume_citations.py` matched \(5446\) numbered statements, the same total as on main.

**Voice.** The repaired sentences name the basis element, the six squares modulo \(9\), the integer matrix, or the norm determinant. They stay in the same register as the surrounding proofs.

**Downstream impacts.** None. No numbered statement changes its number. Nothing outside this volume cites `prop:purecubic`. Volumes 14 and 15 cite Volume 13, Theorems 4.18, 4.20, 11.9, 11.10, 11.23, 15.7, 15.10 and 15.15, Corollaries 7.5, 12.21 and 16.14, Exercise 11.1, and Propositions 15.13 and 15.14. Those labels do not appear in the diff. The files that contain them and were otherwise edited are `ch02-ideals.tex`, `ch05-cyclotomic.tex` and `ch08-zeta.tex`; the hunks are the ideal reminder, the regular-prime paragraph, and the \(h^-\) table. Corollary 12.21 and the Chapter 15 and Chapter 16 statements sit in files that are not in the diff. The Volume 10 citation in `ch12-ideals-quadratic.tex` at line 137 is unchanged: Theorem 6.6 is `thm:dedekind`, unique factorisation in a Dedekind domain, and Theorem 6.13 is `thm:intclosure`, the integral closure in a finite separable extension is Dedekind. The only edit in that file is the lattice caption.

The state-after comments name statements that moved in earlier volumes. The new Volume 13 citations were checked on this tree: Volume 5, Corollary 9.17 is the fundamental theorem of algebra; Volume 3, Lemma 8.12, Corollary 8.7, Corollary 7.8, Propositions 6.3, 6.5 and 6.8, and Theorem 3.11 are the statements named above; Volume 1, Theorem 6.10 is Eisenstein’s criterion. Volume 3, Theorem 8.20 remains the primitive-element theorem for subfields of \(\C\), and the reminder still says “inside \(\C\)”. Volume 5, Theorem 5.8, cited for Stirling, is `thm:stirlinggamma`. Volume 5, Theorem 8.9, cited for Poisson summation, is `thm:poisson`.

## Findings

**SR-001.** In the embedding paragraph of `ch01-number-fields.tex`, the text on `e6c61316` invoked a primitive element of an abstract finite extension. Volume 3, Theorem 8.20 supplies a primitive element only after the extension sits inside \(\C\). The paragraph now adjoins a finite basis one element at a time, by Volume 5, Corollary 9.17 and Volume 3, Lemma 8.12, using Volume 3, Corollary 8.7 for algebraicity.

**SR-002.** In the proof of `prop:purecubic`, the biconditional “\(9\) divides \(m^3-m\) if and only if \(m\equiv\pm 1\pmod 9\)” was asserted. The proof now lists the six squares modulo \(9\). The same proof cited Eisenstein for the degree \([K:\Q]=3\). That appeal is Volume 1, Theorem 6.10. Proposition `prop:eisenstein`, proved a page earlier, is the index test and assumes the polynomial is already minimal.

**SR-003.** The same proof deduced \([M:\Z[\theta]]=3\) from a change-of-basis matrix of determinant \(1/3\). Volume 3, Corollary 7.8 applies to an integer matrix. The coordinates of \(1,\theta,\theta^2\) in the basis of \(M\) are the columns of an integer matrix of determinant \(3\), and that determinant is the index.

**SR-004.** The class-number argument for \(\Q(\sqrt[3]7)\) used the norm \(a^3+7b^3+49c^3-21abc\) as “the same shape” as the formula for \(\sqrt[3]2\). The proof now displays the multiplication matrix and expands the determinant.

## Per-issue verdicts

| ID | Verdict |
| --- | --- |
| V13-001 | Fixed. “Journey” is gone from the preface and from `kdp.md`. Both sentences keep the map of the book. |
| V13-002 | Fixed, after SR-001. Volume 5, Corollary 9.17 and Volume 3, Lemma 8.12 embed a finite extension by adjoining a basis. Theorem 8.9 is not cited for this step. |
| V13-003 | Fixed, after SR-002 and SR-003. For squarefree \(m\ne 0,\pm 1\), the index is \(3\) exactly when \(m\equiv\pm 1\pmod 9\), with the basis in the statement, and the repeated-root sentence matches Theorems `thm:kd` and `thm:ramdisc`. |
| V13-004 | Fixed. Proposition 6.5 is the quotient ring. Both the prime test and the maximal test are Proposition 6.8. Proposition 6.3 is unchanged. |
| V13-005 | Fixed. The element of order \(p\) is Cauchy’s theorem, Volume 3, Theorem 3.11. |
| V13-006 | Fixed. Only the colour-name wording of the caption changed. Charcoal is the MidnightBlue fill `#151516`, and ochre is the ForestGreen circle. |
| V13-007 | Fixed, after SR-004. \(h(\Q(\sqrt[3]7))=3\) follows from the Minkowski bound and Kummer–Dedekind. The minor \(0.5255\) is the regulator of the subgroup generated by \(\theta\) and \(1+\theta\). The class numbers and the full unit group that are not proved here are marked as computations. |
| V13-008 | Fixed. The sphere stays a local analogy. The forward pointer to Chapter 13 is gone, and Chapter 13 does not mention the sphere. |

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume13.md` at `2691145e6a36`.
- The state-after-Volume-K comments on PR #253, through the Volume 12 comment (`7075783113`).
- `git diff origin/main...e6c61316`, and the same diff through `665391b3`, including the full proof of `prop:purecubic`, the class-number section, the repeated-root paragraph, Theorems `thm:kd` and `thm:ramdisc`, Propositions `prop:index`, `prop:disc` and `prop:eisenstein`, and the norm paragraph for \(\sqrt[3]2\).
- Statement numbers from `tools/cross_volume_citations.py` on this tree: Volume 5, Corollary 9.17 is `cor:fta`; Volume 3, Lemma 8.12 is `lem:extend1`; Corollary 8.7 is `cor:finitealg`; Corollary 7.8 is `cor:index`; Propositions 6.3, 6.5 and 6.8 are `prop:finitedomain`, `prop:quotring` and `prop:primemax`; Theorem 3.11 is `thm:cauchy`; Theorem 8.9 is `thm:kronecker`; Theorem 8.20 is `thm:primitiveelement`; Volume 1, Theorem 6.10 is `thm:eisenstein`; Volume 10, Theorems 6.6 and 6.13 are `thm:dedekind` and `thm:intclosure`. The statements were read beside the new sentences.
- The pure-cubic statement was compared with the form quoted from Marcus, *Number Fields*, Chapter 2, Exercise 41 (squarefree case: basis \(1,\alpha,\alpha^2\) when \(m\not\equiv\pm 1\pmod 9\), and \(1,\alpha,(\alpha^2\pm\alpha+1)/3\) when \(m\equiv\pm 1\pmod 9\)) and with the quotation of Marcus, pp. 35–36, in arXiv:2009.02442. Cohen’s book was not opened.
- Label multiset and environment counts against `origin/main`. The only new label is `prop:purecubic`. No caption command and no TikZ option is in the diff except the words “in ochre”. `figures/ch11-lattice.tex` is unchanged. `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- `git diff --check` on `origin/main`: clean.
- Python, as recorded under V13-003 and V13-007. The exact \(\beta\)-relation was checked for all \(24\) squarefree \(m\) from \(-80\) to \(80\) with \(m\equiv\pm 1\pmod 9\). The valuation \(v_3(m^3-m)\) was checked for every \(m\) from \(-200\) to \(200\) not divisible by \(3\): it is at least \(2\) exactly when \(m\equiv\pm 1\pmod 9\), and it equals \(1\) otherwise. No failures.
- `./build.sh volume13-arithmetic` on `665391b3` exited \(0\). The layout line is `Book layout checked: 601 whole boxes, maximum height 330.9pt; no overflow or unresolved references`. `build/volume13-arithmetic/main.log` has no line matching `undefined`, `Overfull`, or `Emergency stop`. `pdfinfo` on `dist/kdp/Volume 13 - Arithmetic - Print.pdf` reports \(387\) pages, page size \(513\times 738\) pts, PDF 1.3, not encrypted. The reading PDF is the cover plus that interior, \(388\) pages, at \(504\times 719.998\) pts. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that \(69\) plates were written at \(1800\) px. The EPUB is \(27\,617\,042\) bytes. The print metadata line reports \(387\) interior pages and spine \(0.9106\) in, which is the even rounding \(388\times 0.002347\).

## Print page count

387.

## Downstream impacts

None.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V13-001 through V13-008.
- The items the Volume 13 review left unchecked, other than \(h(\Q(\sqrt[3]7))\): the value of \(B_{32}\) from the generating function, the census of \(181\) regular primes below \(2000\), the relative class numbers through \(p=41\) as a fresh Bernoulli computation, and the claim \(a_p=c_p\) for every \(p<10^5\). The printed factorisation of the numerator of \(B_{32}\) was not recomputed again; the sequential review had already checked it, and this reading only checked that the sentence was not relabelled as a computation.
- A copy of Cohen, *A Course in Computational Algebraic Number Theory*, or of Marcus beyond the two published quotations named above.
- Acceptance of the print file by KDP.
