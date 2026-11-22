# Volume 9 fix, second review — 22 November 2026

Independent reading of PR #262 at `1056a80ab75c1b654000b77eb73166340072fef4`. The fixes were written by another agent. This reading found no further defect, so no chapter file changes. The log is the later commit on `cursor/fix-volume9-review`.

The issue list is `docs/review/series-sequential-review/volume9.md` on `cursor/series-sequential-review` at `2691145e`, including the spot-check. The state-after-Volume-K comments on PR #253 were read through Volume 8.

## Verdicts

**Correctness.** The reviewed head stands. V9-002, V9-003 and V9-004 are fixed in the places the issues named. V9-001 is rightly left unchanged. Nothing extra was rewritten.

**Dropped or weakened proofs.** No numbered statement was shortened, and no statement was weakened. The Brouwer argument keeps the ray, the smooth retraction, and the appeal to the no-retraction theorem. The defining-function solution keeps the level description. The invariance note keeps the local-homology route and adds the openness route.

**V9-001.** The decline is right. On this head, and on `origin/main` at `a94d01c3` (the commit the spot-check names), line 200 of `volume9-shapes/chapters/ch01-manifolds.tex` is

```
\nabla f=(4x(x^2+y^2-1),\ 4y(x^2+y^2+1)).
```

The bytes begin with `\nabla`. A numbered listing prints the same line as `200|\nabla`. The review quote `\|\nabla` is that gutter. The spot-check’s confirmation of V9-001 repeats the same quote.

The function in the example is \(f(x,y)=(x^2+y^2)^2-2(x^2-y^2)\). It equals \(|z-1|^2|z+1|^2-1\). SymPy’s derivative is exactly the displayed pair: \(4x(x^2+y^2-1)\) and \(4y(x^2+y^2+1)\). The real solutions of \(\nabla f=0\) are \((-1,0)\), \((0,0)\) and \((1,0)\), with values \(-1\), \(0\) and \(-1\). The Hessian determinant is \(-16\) at the origin and \(64\) at \((\pm1,0)\), with \(f_{xx}=8>0\) at the latter two, so the origin is a saddle and the other two are minima. That is the order of values in the example, and it is the classification in the caption. The caption and the figure file are absent from the diff.

On a level \(f=c\) the product of the distances to \(\pm1\) is \(\sqrt{1+c}\) for \(c\ge-1\). In polar form the quadratic in \(u=x^2+y^2\) has product of roots \(-c\). For \(c>0\) exactly one root is positive at every angle. For \(-1<c<0\) the positive root occupies two angular intervals. At \(c=-1\) the completed square leaves only \((\pm1,0)\). Below \(-1\) there is no positive \(u\).

**V9-002.** Stone–Weierstrass, Volume 7, Theorem 4.19, is `thm:sw`. Corollary 4.20 is the polynomial case: the coordinate polynomials form an algebra to which Theorem 4.19 applies. The proof names Theorem 4.19, as the hairy-ball and torus arguments in this volume do, and it says to approximate the coordinates closely enough for the Euclidean bound. Density supplies a polynomial with \(\|P-f\|_\infty<m/4\).

Let \(\delta=m/4\). Since \(|f|\le1\) on the closed unit ball,
\[
|P|\le|f|+|P-f|<1+\delta,
\]
so \(|g|=|P|/(1+\delta)<1\). The identity
\[
g-f=(P-f)-\frac{\delta}{1+\delta}P
\]
is exact. Each summand then has norm strictly less than \(\delta\), and
\[
|g-f|\le|P-f|+\frac{\delta}{1+\delta}|P|<\frac m2.
\]
Hence \(|g(x)-x|\ge|f(x)-x|-|g-f|>m/2>0\). The smooth map \(g\) sends the ball into the open ball and has no fixed point.

The non-strict reading that the issue described does fail. With \(m=1\), \(\delta=1/4\), \(|f|=1\) and \(P=(1+\delta)f\), one has \(|P-f|=\delta\), \(|g|=1\), \(|g-f|=0\), and the loose sum \(\delta+(\delta/(1+\delta))|P|\) equals \(1/2\). A strict error \(6/25\) in the same direction gives \(g=124/125\) and \(|g|^2=15376/15625<1\). If \(|f|\le1\) and the error \(e\) satisfies \(0\le e<\delta\), the triangle bound is at most \(e+\delta(1+e)/(1+\delta)\), which is strictly less than \(m/2\) precisely because \(e<\delta\). Samples with \(m\in\{1/10,1,7/3,2,4\}\), \(|f|\in\{0,1/2,1\}\), and errors \(0\), \(\delta/2\) and \(0.99\delta\) all met both strict bounds. At \(m=1\), \((m/2)/(1+m/4)=2/5<1/2\).

On the boundary, \(|g|<1\) forces \(\langle x,g(x)\rangle\le|g(x)|<1\), so \(\langle x,u\rangle>0\). The radicand is then \(\langle x,u\rangle^2>0\), and the displayed nonnegative root is \(0\). A boundary sample with \(g=(1/5,1/10)\) gives that root exactly. An interior sample lands on the sphere: the squared norm of the exit point simplifies to \(1\). The formula is unchanged. Theorem 3.15, `thm:noretraction`, is still the contradiction, and its statement is unchanged.

**V9-003.** For \(g=x^4+y^4-1\) and \(G=g^2\), \(DG=2g\,Dg\). The critical set is the curve \(M=g^{-1}(0)\) together with the origin. The values are \(0\) and \(1\). Negative levels are empty. For \(0<c<1\) the equations \(x^4+y^4=1\pm\sqrt c\) are two positive scalings of \(M\). At \(c=1\) the level is the curve \(x^4+y^4=2\) and the origin. For \(c>1\) only the outer curve remains. The new sentence says that \(DG\) is the zero map, hence not surjective, at every point of \(G^{-1}(0)\). That is the definition of a critical value in this chapter: a value is regular when the differential is surjective at every point of the fibre, including an empty fibre.

The second derivative is \(\partial^2G/\partial x^2=32x^6+24gx^2\). At \((1,0)\) it equals \(32\). At \((0,1)\), which also lies on \(M\), the pure \(y\) derivative equals \(32\). On \(M\) the Hessian is \(32\) times the outer product of \((x^3,y^3)\) with itself, and \(Dg=(4x^3,4y^3)\) does not vanish on \(M\), so the Hessian is not the zero matrix at any point of the fibre. The solution no longer says that every derivative vanishes. The tangent, the local graph, and the slope \(0\) at \((1,0)\) are unchanged.

**V9-004.** Volume 7, Chapter 3, after the argument that \(\R\) and \(\R^2\) are not homeomorphic, says that the same question for \(\R^2\) and \(\R^3\) is not settled by deleting a point, that both complements stay path-connected, and that the tools are in Volume 9. It does not say that a continuous injection of an open set is an open map.

Corollary 6.13, `cor:brouwerH`, separates dimensions by local homology. Its proof identifies \(H_k(U,U\setminus\{x\})\) with the local group of \(\R^m\), which is \(\Z\) in degree \(m\). Theorem 6.18 is proved later, from the Jordan–Brouwer separation in the preceding proposition, and that proof does not cite the dimension clause.

The new note takes the second route. If \(h:\R^3\to\R^2\) were a homeomorphism onto \(\R^2\), the inclusion \(i(x,y)=(x,y,0)\) would make \(i\circ h:\R^3\to\R^3\) a continuous injection of an open set. Theorem 6.18 makes the image open in \(\R^3\). The image is the plane. A nonempty open set in \(\R^3\) contains a ball, and every open ball meets the complement of the plane. The note is that composition and that contradiction.

**Concept order.** The new appeals are to tools already in hand: uniform density from Volume 7, Theorem 4.19; the definition of a regular value in this chapter; Corollary 6.13 and Theorem 6.18, both proved before the note.

**Labels and numbering.** Against `origin/main` at `a94d01c3`, the TeX files under `volume9-shapes/` have the same `\label` names: 676 labels, no duplicate, and the same multiset. The diff adds no environment. The counts of `exercise`, `theorem`, `proposition`, `lemma`, `definition`, `corollary` and `example` are 288, 116, 61, 43, 40, 25 and 17. Example 1.13 is `ex:cassini`. Theorem 3.15 is `thm:noretraction`. Theorem 3.16 is `thm:brouwern`. Corollary 6.13 is `cor:brouwerH`. Theorem 6.18 is `thm:invariancedomain`. No caption, `\fig`, TikZ picture, or label line is in the diff.

**Recomputed numbers.** A Python session on this review used SymPy for the polynomial identities and `Fraction` for the Brouwer bounds. The Cassini residual \(f-|z-1|^2|z+1|^2+1\) simplifies to \(0\). The gradient residual simplifies to \(0\). Central differences with step \(10^{-6}\), at fourteen points including \((3,-3)\), differ from the displayed formula by at most \(3.28\times10^{-8}\), the size of the \(h^2\) term where the third derivatives are large. \(\partial^2G/\partial x^2\) at \((1,0)\) is the integer \(32\). The Brouwer rearrangement has residual \(0\). The non-strict outward case gives \(|g|=1\) and loose sum \(1/2\). The strict case \(6/25\) gives \(124/125\) and \(15376/15625\). A boundary root was the integer \(0\), and an interior exit had squared norm \(1\).

**Voice.** The new sentences name the polynomial, the fibre, and the two spaces. The banned fillers do not appear in the changed paragraphs. The estimates sit in the manner of the inequalities around them.

**Downstream impacts.** None. No label, statement number, or cited claim changes. `python3 tools/cross_volume_citations.py` matched 5446 numbered statements. Later volumes do not cite Theorem 3.16 or Theorem 6.18. Volume 10’s disc retraction, at `volume10-abstraction/chapters/ch01-categories.tex`, is the continuous ray in the proof of Corollary 6.13. That proof was not edited. Volume 9 cites Volume 5, Theorem 6.17 only at `geometry-ch11-convex.tex`, for Hurwitz’s proof of the inequality. The sentence does not use the equality case. A search of `volume9-shapes/` finds neither “Problem Book” nor “notebook”.

## Findings

None. There is no SR-001.

| ID | Verdict |
| --- | --- |
| V9-001 | Declined, correctly. The display is the gradient. The quoted bar is the line-number gutter. The only real critical points are \((0,0)\) and \((\pm1,0)\), with values \(0\), \(-1\) and \(-1\). |
| V9-002 | Fixed. A strict polynomial error makes \(\|g\|<1\) and \(\|g-f\|<m/2\), and the boundary root is zero. |
| V9-003 | Fixed. \(DG\) vanishes on \(G^{-1}(0)\). The second derivative at \((1,0)\) is \(32\). |
| V9-004 | Fixed. The note derives the separation of \(\R^2\) and \(\R^3\) that Volume 7, Chapter 3 leaves open. |

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume9.md`, including the spot-check at `2691145e`.
- The state-after-Volume-K comments on PR #253, through Volume 8.
- `git diff origin/main...1056a80a` on the three chapter files, and the raw line 200 on both `origin/main` and this head.
- SymPy and exact rational arithmetic, as recorded above.
- Label and environment counts against `origin/main`.
- `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- `./build.sh volume9-shapes` exited 0. The layout check reported 649 whole boxes, maximum height 456.1 pt, no overflow and no unresolved reference. The log of `build/volume9-shapes/main.log` contains 0 occurrences of `undefined`, 0 of `Overfull`, and 0 of `Emergency stop`. `pdfinfo` on `dist/kdp/Volume 9 - Shapes - Print.pdf` reports 511 pages, page size 513 × 738 pt, PDF 1.3. The reading PDF is the cover plus that interior, 512 pages, at the 7 × 10 in trim. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that 99 plates were written at 1800 px. The EPUB is 30 MB.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V9-001 through V9-004, together with the Cassini level count, the no-retraction statement, and the local-homology proof of Corollary 6.13.
- The items the Volume 9 review left unchecked: portrait files, TikZ coordinate files beyond the Cassini mathematics, the contact sheets, the Coxeter projection, the sampled \(U(24)\) eigenvalues, the universal resultant identity, and the historical fine print.
- Acceptance of the print file by KDP.
