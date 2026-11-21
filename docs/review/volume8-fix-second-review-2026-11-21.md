# Volume 8 fix, second review — 21 November 2026

Independent reading of PR #261 at `b7aa95d7c463d7571c957af2f7c05385dcffaee3`. The fixes were written by another agent. This reading found no further defect, so no chapter file changes. The log is the later commit on `cursor/fix-volume8-review`.

## Verdicts

**Correctness.** The reviewed head stands. Each of V8-001 through V8-011 is settled in the place the issue named. V8-002 is rightly left unchanged. Nothing extra was rewritten.

**Dropped or weakened proofs.** No numbered statement was shortened, and no statement was weakened. The Moore–Aronszajn argument gains the phase that makes Cauchy–Schwarz bound the modulus. The square-root solution keeps the binomial for a nonzero eigenvalue. The Ramanujan and zeta-mean arguments keep their estimates after the problem-book sentences are removed.

**V8-001.** In `thm:alaoglu`, each value sequence \((\varphi_n(x_k))_n\) is bounded in \(\mathbb R\) or \(\mathbb R^2\), because \(|\varphi_n(x_k)|\le M\|x_k\|\). Volume 7, Theorem 4.8 is `thm:compactmetric`. The paragraph after its proof identifies that theorem, in \(\mathbb R^n\), with Bolzano–Weierstrass: a bounded sequence has a convergent subsequence, since the closure of its range is closed and bounded, hence compact, hence sequentially compact. \(\mathbb R\) and \(\mathbb R^2\) are the real and complex cases. Volume 7, Exercise 4.5 is `ex:hilbertcube`. Its solution writes the diagonal extraction: nested infinite index sets, one coordinate at a time, then the diagonal subsequence. The estimate \(|\psi_n(x)-\psi_m(x)|\le 2M\varepsilon+|\psi_n(x_k)-\psi_m(x_k)|\) is unchanged, and the pointwise limit is still linear and norm-bounded. Theorem 4.15 remains Arzelà–Ascoli and is no longer cited for this step.

**V8-002.** The decline is right. On main, Volume 7, Proposition 10.6 is `prop:simpledense`: simple functions are dense in \(L^p\). Theorem 10.7 is `thm:ccdense`: for \(1\le p<\infty\), the step functions are dense in \(L^p(\mathbb R^d)\), and so are the functions in \(C_c(\mathbb R^d)\). The sentence at `ch01-banach.tex:259` asks for a step-function approximation of an \(L^1\) weight, which is the first claim of Theorem 10.7, at \(p=1\). The reflexive-exercise solution cites Proposition 10.6 and Theorem 10.7 together because it needs a countable dense set of rational step functions. The estimate \(|\int f_n(g-h)|\le\|g-h\|_1\) uses the step functions the sentence names.

**V8-003.** The kernel form is linear in the first argument and conjugate-linear in the second, as in the displayed sum \(\sum_{i,j}a_i\overline{b_j}K(y_j,x_i)\) and as fixed at the start of the chapter. The hypothesis \(K(x,y)=\overline{K(y,x)}\) gives \(\langle g,f\rangle=\overline{\langle f,g\rangle}\). If \(\langle f,g\rangle\ne 0\), the scalar \(\omega=\langle f,g\rangle/|\langle f,g\rangle|\) has modulus one, and conjugate linearity gives \(\langle f,\omega g\rangle=|\langle f,g\rangle|\). For real \(t\),
\[
\langle f+t\omega g,f+t\omega g\rangle=\langle f,f\rangle+2t|\langle f,g\rangle|+t^2\langle g,g\rangle\ge 0.
\]
If \(\langle g,g\rangle=0\), the coefficient of \(t\) vanishes, so \(\langle f,g\rangle=0\). If \(\langle g,g\rangle>0\), a quadratic \(At^2+Bt+C\) with \(A>0\) that stays nonnegative has nonpositive discriminant, and \(|\langle f,g\rangle|^2\le\langle f,f\rangle\langle g,g\rangle\). Then \(|f(x)|=|\langle f,K_x\rangle|\le\langle f,f\rangle^{1/2}K(x,x)^{1/2}\), since \(\langle K_x,K_x\rangle=K(x,x)\). Zero squared norm forces \(f=0\). The Gaussian check after the theorem uses complex coefficients, and the inequality now covers them. The completion appeal is still Volume 7, Theorem 2.9.

**V8-004.** Schur–Horn remains the proved identification of diagonals with majorisation. The beauty note marks Rado’s convex-hull identification with the phrase “quoted here”, the mark used for Eberlein–Šmulian, Malgrange–Ehrenpreis, and the other quotations in this volume. A search of `volume8-analysis/` finds Rado only in that sentence.

**V8-005.** The caption change is the three numerals. Against `origin/main`, the unified diff of `linear-ch06-svd.tex` replaces `0.30`, `0.16` and `0.07` by `0.28`, `0.12` and `0.05`, and the surrounding caption text is the same. `figures/linear-ch06-lowrank.tex` is absent from the diff. The storage count \(8\cdot 65=520\) and the comparison \(1024\) are unchanged: a singular triple on a \(32\times 32\) matrix is \(32+32+1=65\) numbers, and \(8\cdot 65=520\), while \(32\cdot 32=1024\).

**V8-006.** `kdp.md` now says that the theorems on the main path are proved and that the quotations are marked. The generated listing repeats that sentence. The blurb was outside the issue and is unchanged.

**V8-007.** Both pointers to Problem Book I are gone: the sentence in `pb:ramanujan`, and the sentence in the solution of `pb:zetamellin`. The Ramanujan solution still derives \(c_q(n)=\sum_{d\mid(q,n)}\mu(q/d)d\) and the orthogonality \(\varphi(q)\mathbf 1_{q=r}\), and it still records that the argument includes \(q=1\). The zeta-mean solution still reaches \(I_N\to\log(2\pi)-\gamma\) from Stirling (Volume 6, Theorem 6.1(c)) and \(H_N-\log N\to\gamma\). A search of `volume8-analysis/` finds neither “Problem Book” nor “Journey”.

**V8-008.** `pb:mvt` and `pb:vandelune` are graded `$\star\star\star$`. The exercise box prints its optional argument after the number, which is how the other grades in the chapter are set. The exercise counter is separate from the grade, and the exercise count is unchanged.

**V8-009.** The exercise asks for \(n\ge 2\). If \(B^2=J_n\), then \(B^{2n}=J_n^n=0\). The block sends \(e_1\) to zero and \(e_j\) to \(e_{j-1}\), so \(\dim\ker J_n=1\). Thus \(\dim\ker B\le\dim\ker B^2=1\). The two kernels have dimension \(1\). The solution then shows that \(\ker B=\ker B^2\) forces every later kernel to equal \(\ker B\): if \(\ker B^k=\ker B\) and \(B^{k+1}v=0\), then \(Bv\in\ker B\), so \(v\in\ker B^2=\ker B\). Nilpotence makes \(\ker B^{2n}\) the whole space, of dimension \(n\). The common dimension is \(1\), and \(n\ge 2\). The binomial square root for \(\lambda\ne 0\) is still the next paragraph.

**V8-010.** Volume 6, Theorem 3.6 is `thm:lbasic`. For a nonprincipal character it gives holomorphy of \(L(s,\chi)\) on \(\operatorname{Re}s>0\), and part (a) gives \(L(s,\chi)\ne 0\) for \(\operatorname{Re}s>1\). Theorem 5.2 is `thm:line`: \(L(1+it,\chi)\ne 0\) except at the principal pole \((\chi_0,0)\). For a nonprincipal character that includes \(s=1\). The closed half-plane \(\operatorname{Re}s\ge 1\) sits inside the open half-plane of holomorphy, and \(L\) has no zero there, so \(-L'/L\) is continuous on that closed half-plane. That is the boundary hypothesis of `thm:ikehara`. The principal-character formula is unchanged.

**V8-011.** Proposition `prop:cauchylaw` gives \(\hat p_a(\xi)=e^{-2\pi a|\xi|}\), so \(\hat p_s\hat p_t=\hat p_{s+t}\). Proposition `prop:ftl1`(c), earlier in the chapter, turns convolution into multiplication. The two probability densities therefore have the same Fourier transform. Theorem `thm:measuniq`, proved in the preceding section, identifies the laws. Volume 7, Exercise 10.2 is `ex:approxid`. It states \(P_s*P_t=P_{s+t}\) and says Volume 8 proves that identity. The backward pointer is gone. Corollary `cor:cauchymean` still multiplies characteristic functions and appeals to uniqueness.

**Concept order.** The new appeals are to tools already in hand: Bolzano–Weierstrass in Volume 7, Theorem 4.8; the diagonal extraction written in the solution of Volume 7, Exercise 4.5; holomorphy and the half-plane zero-free region in Volume 6, Theorem 3.6; nonvanishing on the line in Volume 6, Theorem 5.2. The Cauchy semigroup is proved from the transform rules of this chapter.

**Labels and numbering.** Against `b7aa95d7`, which is the reviewed head, the TeX files under `volume8-analysis/` have the same `\label` names: 729 labels, no duplicate, and the same multiset as `origin/main`. There is no new numbered statement. The counts of `theorem`, `proposition`, `lemma`, `corollary`, `definition`, `example` and `exercise` environments are 145, 45, 30, 38, 18, 17 and 300.

**Recomputed numbers.** A Python session on this review read `figures/linear-ch06-lowrank.tex`. The original panel is the block labelled “original”, with \(x\) from 114 to 145. Each cell `black!N` was entered as the ink \(N\). The \(32\times 32\) grid has 984 drawn cells. The 40 undrawn positions are white paper and were entered as 0. Relative scale does not change a ratio of Frobenius norms. Singular values came from `numpy.linalg.svd`. The relative tail is \(\bigl(\sum_{i>k}\sigma_i^2/\sum_i\sigma_i^2\bigr)^{1/2}\).

```
rank 1: 0.2766238856   two decimals 0.28   three decimals 0.277
rank 3: 0.1214309991   two decimals 0.12   three decimals 0.121
rank 8: 0.0467035857   two decimals 0.05   three decimals 0.047
```

The Eckart–Young reconstruction from the same singular vectors reproduces these three tails. The caption’s \(0.28\), \(0.12\) and \(0.05\) are those two-decimal values. Also \(32+32+1=65\), \(8\cdot 65=520\) and \(32\cdot 32=1024\).

**Voice.** The new sentences name the object and the step. The banned fillers do not appear in the changed paragraphs. The Cauchy–Schwarz expansion and the kernel induction sit in the manner of the proofs around them. The listing sentence is the same plain register as the description it closes.

**Downstream impacts.** No numbered statement in Volume 8 changes its number. `python3 tools/cross_volume_citations.py` matched 5446 numbered statements. The caption numerals are local to this volume. Later volumes cite statements whose text this branch does not change:

- Volume 9, `riemann-mapping.tex`, cites Corollary 14.3 and Proposition 14.4.
- Volume 9, `ch07-liegroups.tex:584`, cites Theorem 4.3.
- Volume 10, `linear-ch10-tensors.tex`, cites Theorems 4.1, 4.5, C.2 and F.5. `ch01-categories.tex:144` cites Theorem A.8. `ch11-compact.tex` cites Theorem 13.11.
- Volume 11, `ch13-harder.tex`, cites Theorem 10.2.
- Volume 14, `waring.tex` and `ch11-additive.tex`, cites Theorems 10.2, 12.16 and 12.17. `ch10-halasz.tex` cites Theorem 10.4.
- Volume 15, `moments-zeta.tex:122`, cites Theorem 10.4.

Those numbers are still `linear:thm:svd`, `linear:thm:polar`, `linear:thm:eckartyoung`, `thm:ftinv`, `thm:plancherel`, `thm:meshulam`, `thm:blr`, `thm:duals`, `cor:hsc`, `prop:hsccriterion`, `linear:thm:bidual`, `linear:thm:schur` and `linear:thm:lyapunov`. The files that contain Theorems 4.1, 4.3, 4.5, 10.2 and 10.4, and Theorem C.2, were touched only in a caption, a semigroup sentence, or the square-root solution.

Volume 7’s Theorem 2.10, Corollary 2.11 and Theorem 1.21 are still cited, and those statements are unchanged. Theorem 1.21 is `thm:basis`, a Hamel basis from the axiom of choice. Theorem 2.10 is `thm:Qp`. Corollary 2.11 is `cor:Zpcompact`.

- `volume8-analysis/chapters/ch08-haar.tex:217`
- `volume8-analysis/chapters/ch01-banach.tex:309`

Volume 8 does not cite the items Volumes 1–6 left for later books: the unnumbered cosine proposition before `prop:sincmp`, Volume 2’s `prop:legendre`, Volume 3’s `prop:cyclodegree` and `prop:solids`, Volume 4’s `lem:tree` and `lem:sector`, Volume 5’s `cor:cotagain`, or the removed secondary constant in Volume 6’s `ex:twoomega`.

## Findings

None. There is no SR-001.

| ID | Verdict |
| --- | --- |
| V8-001 | Fixed. Theorem 4.8 supplies the bounded subsequence in \(\mathbb R\) or \(\mathbb R^2\). Exercise 4.5 is the diagonal extraction. |
| V8-002 | Declined, correctly. Theorem 10.7 states that step functions are dense in \(L^p(\mathbb R^d)\) for \(1\le p<\infty\). Proposition 10.6 is simple functions. |
| V8-003 | Fixed. A unimodular phase makes the cross term real and nonnegative, and the quadratic bounds the modulus. |
| V8-004 | Fixed. Rado’s identification is marked “quoted here” and is not used as a proved step. |
| V8-005 | Fixed. The drawn original panel has tails \(0.2766238856\), \(0.1214309991\) and \(0.0467035857\), printed as \(0.28\), \(0.12\) and \(0.05\). Only those numerals changed. |
| V8-006 | Fixed. The listing says the theorems on the main path are proved and that the quotations are marked. |
| V8-007 | Fixed. Both problem-book pointers are gone, and the arguments remain. |
| V8-008 | Fixed. `pb:mvt` and `pb:vandelune` are graded \(\star\star\star\). |
| V8-009 | Fixed. The two kernels have dimension \(1\), and nilpotence requires dimension \(n\ge 2\). |
| V8-010 | Fixed. Holomorphy on \(\operatorname{Re}s>0\) and nonvanishing for \(\operatorname{Re}s>1\) are Theorem 3.6. The line \(\operatorname{Re}s=1\), including \(s=1\), is Theorem 5.2. |
| V8-011 | Fixed. The semigroup identity is proved from the product of transforms, convolution, and uniqueness. |

## What this review did not check

- A page-by-page visual reading of the PDF. `./build.sh volume8-analysis` produced the reading PDF, the print PDF, the EPUB and the HTML reader. The layout check, printed during the run, reported 659 whole boxes, maximum height 391.2 pt, no overflow and no unresolved reference. The log has no undefined reference and no overfull box. The print interior is 491 pages, and the page size is 513 by 738 pt. The reading PDF is the cover plus that interior, 492 pages at 7 by 10 in. After the script exited, `tools/check_epub_media.py` and the cover-template check on the EPUB and the reader both exited 0. EPUB figures are full width, and the math images carry an em baseline. The EPUB is 31 MB.
- Kindle rendering of the EPUB, beyond those build checks.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V8-001 through V8-011.
- The items the Volume 8 review left unchecked: portrait files, TikZ coordinates beyond the low-rank panel, the Kesten–McKay histogram, the pseudospectra of the \(64\times 64\) Jordan block, the Fiedler drawing, the Hadamard constructions announced in August 2026, the long decimal \(\sigma_0\), and the historical fine print.
- Acceptance of the print file by KDP.
