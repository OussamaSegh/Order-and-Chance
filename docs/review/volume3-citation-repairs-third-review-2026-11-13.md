# Third review of the Volume 3 citation repairs

**Verdict: APPROVE** at `e4c2e75c3738aa0298f99e1e5a2254b904555216`.

**Pull request:** https://github.com/OussamaSegh/Order-and-Chance/pull/235

**Branch reviewed:** `cursor/volume3-apply-scored-read`. This review does not edit that branch.

This is a separate reading from the second review in pull request #236. The head under review is the commit the fixer pushed after that review asked for a change at `939f6eacb7d344af8f67115b64b709ff4763c3b5`. Pull request #235 was squash-merged to `main` as `1e85f6ff8e3fc683d0861b641155e671336e91b1` while this reading was in progress. The verdict below is for the exact SHA `e4c2e75c`, not for the squash commit. The seven repaired files and `volume3-symmetry` match `main` at that squash.

## Proposition 6.17

On `main`, and on this SHA (the Volume 3 tree is the same object `b5db677f6b20428ebd95d02dcc90a71d2de2d953`), `volume3-symmetry/chapters/ch06-rings.tex` states:

```tex
\begin{proposition}\label{prop:gaussirr}
Let $R$ be a UFD with fraction field $K$, and $f\in R[X]$ primitive of degree $\ge1$. Then $f$ is irreducible in $R[X]$ iff it is irreducible in $K[X]$. If $f$ divides $g\in R[X]$ in $K[X]$, it divides $g$ in $R[X]$.
\end{proposition}
```

The shared counter in `common/interior-boxes.tex` numbers theorem, proposition, lemma, corollary, definition, and example together. The walker in `tools/cross_volume_citations.py` assigns this environment Proposition 6.17. It sits between Lemma 6.16 (`lem:gauss`, the content formula) and Theorem 6.18 (`thm:gaussufd`, a UFD coefficient ring gives a UFD polynomial ring). The index records those two neighbours as Lemma 6.16 and Theorem 6.18. The same walk gives 375 numbered statements in Volume 3.

The proposition has two sentences. The second is the divisibility descent. The reminder in Volume 13 quotes that sentence, with the indeterminate renamed from \(X\) to \(y\).

The reminder at `e4c2e75c`, in `volume13-arithmetic/chapters/ch11-curves.tex`, reads:

> Let \(R\) be a UFD with fraction field \(K\), and let \(f\in R[y]\) be primitive of degree at least 1. If \(f\) divides \(g\in R[y]\) in \(K[y]\), then \(f\) already divides \(g\) in \(R[y]\) (Volume 3, Proposition 6.17). If two polynomials in \(R[y]\) have a common factor of positive degree in \(K[y]\), scale that factor to a primitive polynomial of degree at least 1 in \(R[y]\). By the proposition, that polynomial divides both in \(R[y]\).

Every hypothesis of the descent is present: \(R\) is a UFD, \(K\) is its fraction field, \(f\) lies in \(R[y]\) and is primitive of degree at least 1, \(g\) lies in \(R[y]\), and the given division is the division in \(K[y]\). The conclusion is division in \(R[y]\).

The dividend has to lie in \(R[y]\). In the counterexample that the previous review named, \(X\) divides \(\frac12 X\) in \(\mathbb Q[y]\), and the quotient \(\frac12\) is not in \(\mathbb Z[y]\). The new sentence does not claim that case: \(\frac12 X\) is not an element of \(\mathbb Z[y]\).

The next sentence is the use on two curves. Volume 3, in the paragraph before Lemma 6.16, writes every nonzero polynomial of \(K[X]\) as \(\lambda f_0\) with \(\lambda\in K^\times\) and \(f_0\in R[X]\) primitive: clear a common denominator, then divide by the content. Multiplication by an element of \(K^\times\) preserves degree, so a common factor of positive degree scales to a primitive polynomial of degree at least 1. That primitive polynomial divides each curve in \(K[y]\), because it differs from the original factor by a unit of \(K\). Proposition 6.17, applied once to each curve, puts both quotients in \(R[y]\).

Lemma `lem:finite` uses that step with \(R=k[x]\) and \(K=k(x)\). A field is a UFD, and Theorem 6.18 then makes \(k[x]\) a UFD. A primitive polynomial of positive degree is a non-unit of \(k[x,y]\). So a common factor of positive degree in \(K[y]\) would be a common factor in \(k[x,y]\), which the lemma has assumed away. The appeal in the proof is the same scaling, cited as Proposition 6.17.

## The seven rows

The walker supplied the numbers below. Each row is the corresponding line of the citation table in pull request #235.

| ID | Location | What the book now says | Statement it points at | Verdict |
|---|---|---|---|---|
| V3-2 | `volume13-arithmetic/chapters/ch11-curves.tex` | Primitive \(f\in R[y]\) of degree at least 1 divides \(g\in R[y]\) in \(R[y]\) when it divides \(g\) in \(K[y]\). A positive-degree common factor scales to such a polynomial, and that polynomial divides both curves in \(R[y]\). | Proposition 6.17, label `prop:gaussirr`, second sentence. Theorem 6.18 is the UFD sentence beside it. | Correct |
| V3-4 | `volume6-crossroads/chapters/ch12-modular.tex` | The tools line cites Vandermonde determinants as Volume 1, Proposition 7.4, and eigenvalues and traces as Volume 1, Chapter 7. | Proposition 7.4, label `prop:vdm`, is \(\det(x_i^{j-1})=\prod_{i<j}(x_j-x_i)\). Chapter 7 defines the trace and states that, over \(\mathbb C\), the trace and the determinant are the sum and the product of the eigenvalues. The Gauss-sum solution uses both: \(F\) is a Vandermonde matrix, and the multiplicities are read from \(\operatorname{tr} F\), \(\operatorname{tr} F^2\), and \(\det F\). | Correct |
| V3-4 | `volume8-analysis/chapters/linear-ch01-duality.tex` | The characters \(e^{ikx}\) for \(\lvert k\rvert\le N\) are orthonormal, hence independent, by Volume 5, Chapter 6. | Volume 5, Chapter 6 (`ch06-fourier.tex`) sets \(\langle f,g\rangle=\frac1{2\pi}\int_{-\pi}^{\pi} f\overline g\) and states that \(e_n(t)=e^{int}\) are orthonormal. Orthonormal functions are linearly independent, which is the dimension count in the solution. Volume 4, Chapter 6 is “Why the Bell Curve Appears” and does not contain this basis. | Correct |
| V3-4 | `volume9-shapes/chapters/geometry-ch06-quadrics.tex` | The signature check for \(xy+yz+zx\) cites the spectral theorem, Volume 1, Theorem 7.9. | Theorem 7.9, label `thm:spectral`, says a real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors. The same chapter of Volume 9, a few pages earlier, records the consequence used here: in that basis the form is \(\sum\lambda_i x_i^2\), so the signature counts positive and negative eigenvalues. The matrix of \(xy+yz+zx\) is \(\frac12(J-I)\). The eigenvalues of the \(3\times 3\) all-ones matrix are \(3,0,0\), so those of \(\frac12(J-I)\) are \(1,-\frac12,-\frac12\). That is signature \((1,2)\), the signature the solution already reached by completing the square. | Correct |
| V3-4 | `volume5-calculation/chapters/ch04-integrals.tex` | The tools line names the count \(n!/z_\lambda\) and places it in Volume 3, Chapter 4. | That count is part (c) of Proposition 4.4, label `prop:conjSn`: a class of cycle type \(\lambda\) has \(n!/z_\lambda\) elements, with \(z_\lambda=\prod_i i^{m_i}m_i!\). The Golomb solution uses \(\frac{n!}{\prod j^{c_j}c_j!}\), which is the same count. Volume 3, Chapter 4 does not call the count Cauchy's formula. The tools line names the count. The writeup still says "By Cauchy's formula"; that name is the one Volume 11 later prints on the same formula, and the exercise prompt in this chapter already uses it. The pointer at the end of the solution is the Volume 3 count. | Correct |
| V3-1 | `volume15-order-and-chance/chapters/ra-symmoments.tex` | A finite abelian \(p\)-group is \(\mathbb Z/p^{\lambda_1}\oplus\cdots\oplus\mathbb Z/p^{\lambda_r}\) by Volume 3, Corollary 7.7, and \(p^kG=0\) forces \(1\le\lambda_i\le k\). | Corollary 7.7, label `cor:abelian`, includes the elementary-divisor form \(\mathbb Z^s\oplus\bigoplus_j\mathbb Z/p_j^{a_j}\mathbb Z\). A finite \(p\)-group has free rank \(0\) and one prime. The upper bound on the exponents is the relation \(p^kG=0\), read off that decomposition. | Correct |
| V3-1 | `volume13-arithmetic/chapters/ch12-elliptic.tex` | After the height descent shows that a finite set generates \(E(\mathbb Q)\), Volume 3, Corollary 7.7 supplies the decomposition. | The same corollary: every finitely generated abelian group is \(\mathbb Z^s\) times a finite abelian group, with \(s\) unique. Mordell's theorem states \(E(\mathbb Q)\cong E(\mathbb Q)_{\mathrm{tors}}\times\mathbb Z^r\). Finite generation is proved in the paragraph; the corollary is what splits off the free part. | Correct |

## Rows V3-1 through V3-48

`git rev-parse` of the tree `volume3-symmetry` is `b5db677f6b20428ebd95d02dcc90a71d2de2d953` at the pull-request base `b60c7d8ee462f80b58ef815bfd81a1f013d15841`, at `e4c2e75c`, and at `origin/main`. This pull request does not change Volume 3. The repairs from #199 and #202 are the text of that tree. The print page count of Volume 3 is unchanged because the sources are unchanged. Volume 3 was not rebuilt for this review.

The diff from `939f6eac` to `e4c2e75c` is two commits, `513768f2` and `e4c2e75c`, and one file. `git diff --name-status 939f6eac e4c2e75c` prints only `M volume13-arithmetic/chapters/ch11-curves.tex`. The hunk is the reminder quoted above. The Chinese-remainder sentence beside it is untouched.

## Prose of the changed sentences

The new reminder is three short statements: the hypotheses, the descent, and the scaling that the lemma needs. "Scale" is the operation Volume 3 has already described, multiplication by an element of \(K^\times\) that clears denominators and removes content. There is no stock opener, no hollow intensifier, and no sentence that only announces a topic. The other six repaired sentences are a citation, a tools line, or one clause naming the fact just used. They are plain.

## Checks

- `python3 -m unittest test_cross_volume_citations.py`, run from `tools/` on this SHA, ran 14 tests and exited 0. That includes `test_volume3_pointers_name_the_stated_fact`, which locks the seven new strings, and `test_volume1_chapter_glosses_match_the_printed_chapters`, which runs `volume3_misplaced_subject` over every volume. The checker flags a Volume 3 citation whose nearby words are "Vandermonde" or "eigenvalues and traces".
- The numbering script `number_volume` printed Proposition 6.17 for `prop:gaussirr`, Proposition 4.4 for `prop:conjSn`, Corollary 7.7 for `cor:abelian`, Volume 1 Proposition 7.4 for `prop:vdm`, and Volume 1 Theorem 7.9 for `thm:spectral`.
- GitHub lists 20 check runs on `e4c2e75c`. Nineteen concluded success, and `publish` was skipped. [Run 43489447614](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43489447614) (the book builds, `list`, `debs`, and `site`) succeeded. [Run 43489447516](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43489447516) (`volume4-native`) succeeded.

## Verdict

APPROVE `e4c2e75c3738aa0298f99e1e5a2254b904555216`.
