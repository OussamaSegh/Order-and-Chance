# Second review of the Volume 3 citation repairs, 13 November 2026

**Verdict: REQUEST CHANGES**

**Head reviewed:** [`939f6eacb7d344af8f67115b64b709ff4763c3b5`](https://github.com/OussamaSegh/Order-and-Chance/commit/939f6eacb7d344af8f67115b64b709ff4763c3b5) on `cursor/volume3-apply-scored-read`, pull request [#235](https://github.com/OussamaSegh/Order-and-Chance/pull/235). One commit. Its parent is `b60c7d8ee462f80b58ef815bfd81a1f013d15841`. This review does not edit that branch, and it does not merge.

**CI.** [Run 43475710392](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43475710392) completed with conclusion success on that SHA. Eighteen jobs succeeded: `list`, `debs`, `site`, and the fifteen book builds. `publish` was skipped. The run has nineteen jobs.

**Current main.** After this branch was cut, `origin/main` moved to `932bc285207bed906aa5853efeebabb16cb06cf2` (the Volume 5 rewrite, #233). A merge of the reviewed head with that tip is clean. The Volume 5 tools line lands on the rewritten chapter, at the line that still said “Cauchy's formula.” Volume 3 and `common/` are the same trees on the reviewed head and on that main.

The statements below were read in the source. Printed numbers come from the shared counter in `tools/cross_volume_citations.py`, the same counter the books use: theorem, proposition, lemma, corollary, definition, and example, reset at each chapter. Volume 1 prints the language chapter as Chapter 0.

## The change this review asks for

**V3-2, the reminder in `volume13-arithmetic/chapters/ch11-curves.tex`.** The number is right, and the name “Gauss's lemma” is gone. The sentence that replaces it states a false claim.

Proposition 6.17 (`prop:gaussirr`, `ch06-rings.tex`) says: let \(R\) be a UFD with fraction field \(K\), and let \(f\in R[X]\) be primitive of degree at least 1. If \(f\) divides a polynomial \(g\in R[X]\) when the division is read in \(K[X]\), then \(f\) already divides \(g\) in \(R[X]\). Lemma 6.16 (`lem:gauss`) is the content formula \(c(fg)=c(f)c(g)\). Theorem 6.18 (`thm:gaussufd`) is the polynomial UFD, including \(K[X_1,\ldots,X_n]\).

The new reminder says a primitive polynomial of \(R[y]\) that divides another polynomial in \(K[y]\) already divides it in \(R[y]\). The polynomial being divided is placed in \(K[y]\). Take \(R=\mathbb Z\), \(f=X\), and \(g=\frac12 X\). Then \(f\) is primitive of degree 1, \(f\) divides \(g\) in \(\mathbb Q[y]\), and the quotient \(\frac12\) is not in \(\mathbb Z[y]\).

The use three paragraphs later is the proposition: a common factor in \(K[y]\) is scaled to a primitive polynomial of \(R[y]\), which would divide both curves in \(R[y]\). The reminder should say the same thing, including degree at least 1.

## Citation rows in the pull-request body

| ID | Location on the reviewed head | Verdict | What was opened |
| --- | --- | --- | --- |
| V3-2 | `volume13-arithmetic/chapters/ch11-curves.tex:32–33` | partial | Proposition 6.17 is the right statement, and the reminder no longer calls the descent Gauss's lemma. The new sentence puts the dividend in \(K[y]\). See the change above. Theorem 6.18 for \(k[x_1,\ldots,x_n]\) and Theorem 6.9 for the Chinese remainder theorem are the statements those numbers name; those two citations were already in the paragraph. |
| V3-4 | `volume6-crossroads/chapters/ch12-modular.tex:2403` | fixed | The Schur solution uses \(\det(x_i^{\,j-1})=\prod_{i<j}(x_j-x_i)\) and the trace of the Fourier matrix. Proposition 7.4 in Volume 1 is Vandermonde. Chapter 7 of Volume 1 is linear algebra: Proposition 7.5 introduces the trace and the eigenvalues, and Theorem 7.9 is the spectral theorem. Volume 3 has neither. |
| V3-4 | `volume8-analysis/chapters/linear-ch01-duality.tex:612` | fixed | Volume 5, Chapter 6, sets \(e_n(t)=e^{int}\) and proves \(\langle e_m,e_n\rangle\) is \(1\) or \(0\). Orthonormality gives independence, which is the dimension \(2N+1\) the unisolvence argument uses. The same sentence is in the rewritten Chapter 6 on current main. Volume 4, Chapter 6, is the bell curve. |
| V3-4 | `volume9-shapes/chapters/geometry-ch06-quadrics.tex:396` | fixed | Theorem 7.9 is the spectral theorem for a real symmetric matrix. The form \(xy+yz+zx\) has matrix \(\frac12(J-I)\). The eigenvalues of \(J\) are \(3,0,0\), so the eigenvalues of \(\frac12(J-I)\) are \(1,-\frac12,-\frac12\). One positive and two negative agrees with the signature \((1,2)\) already computed by completing the square. The clause “whose eigenvalues” sits after the name of \(J\); the numbers are the eigenvalues of \(\frac12(J-I)\). |
| V3-4 | `volume5-calculation/chapters/ch04-integrals.tex:542` | fixed | Proposition 4.4(c) says a class of cycle type \(\lambda\) has \(n!/z_\lambda\) elements, with \(z_\lambda=\prod_i i^{m_i}m_i!\). The Golomb solution uses that count. Volume 3, Chapter 4, does not call it Cauchy's formula. On current main the same tools line is the one the clean merge repairs. |
| V3-1 | `volume15-order-and-chance/chapters/ra-symmoments.tex:3` | fixed | Corollary 7.7 (`cor:abelian`) includes the prime-power form \(\mathbb Z^s\oplus\bigoplus\mathbb Z/p_j^{a_j}\mathbb Z\). For a finite abelian \(p\)-group the free rank is \(0\). The bounds \(1\le\lambda_i\le k\) are the omission of trivial summands together with \(p^kG=0\). |
| V3-1 | `volume13-arithmetic/chapters/ch12-elliptic.tex:357–358` | fixed | Mordell's theorem states \(E(\mathbb Q)\cong E(\mathbb Q)_{\mathrm{tors}}\times\mathbb Z^r\). The proof shows finite generation. Corollary 7.7 is the classification that supplies that decomposition. |

The other repaired Volume 3 pointers that this diff does not touch were re-read with the same counter. Exercise 10.1 is still the cyclotomic isomorphism in Volumes 13 and 15. Theorem C.12 is still Cauchy–Davenport in Volumes 14 and 15. Lemma 12.3 is still only the axis-angle statement, and the squared volume is still Volume 1, Theorem 7.10.

## Scored-read rows V3-1 through V3-48

These repairs were merged in #199 (`01eb4813`) and the three follow-up sentences in #202 (`2f570383`). The reviewed diff does not touch `volume3-symmetry`. The tree is identical to current main. Each row below was opened in that text. “Fixed” means the repair described in the final-status table of `docs/review/volume3-independent-scored-read-2026-11-11.md` is still the sentence on the page, and the sentence still says the thing that table names.

| ID | Verdict | Where the repair still sits |
| --- | --- | --- |
| V3-1 | fixed | Exercise 10.1 for the cyclotomic isomorphism and the degree, in `ch05-cyclotomic.tex`, `ch04-units.tex`, `ch02-ideals.tex`, and `conjectures-ch12-algebra.tex`. |
| V3-2 | fixed | Theorem 6.18 and Proposition 6.17 in Volume 13, and Theorem 6.18 in Volume 10. The partial row above is the new wording of the Volume 13 reminder. The numbers in this row remain Theorem 6.18 and Proposition 6.17. |
| V3-3 | fixed | Theorem C.12 in `volume14-primes/chapters/ch11-additive.tex` and in `volume15-order-and-chance/chapters/ch08-heuristics.tex`. |
| V3-4 | fixed | Lemma 12.3 for the axis and the angle. The spectral theorem and the Gram determinant are Volume 1, Theorems 7.9 and 7.10. |
| V3-5 | fixed | The index opener is “Each name points at the statement, exercise, or definition it names.” Ninety-six `\ocindexpage` entries, ninety-three distinct labels, every label defined in the volume, and every printed number beside a label equal to the shared counter. |
| V3-6 | fixed | The Rokicki–Kociemba–Davidson–Dethridge item is in the Chapter 4 sources. Chapter 1 has no such item. |
| V3-7 | fixed | Appendix D has a “Sources and further reading” section. |
| V3-8 | fixed | The case \(a=0\) is \(\binom{m}{1}=m\). |
| V3-9 | fixed | The row-sum converse cites Frobenius, Theorem A.6. |
| V3-10 | fixed | Strict positivity of a nonnegative eigenvector cites the same theorem. |
| V3-11 | fixed | Every group of order 4 is abelian, and that applies to every Sylow subgroup through the half-turn. |
| V3-12 | fixed | A pure unit perpendicular to the axis reverses the angle. The rotation \(c\) is named, with its angle and axis, before that formula. |
| V3-13 | fixed | The six extra involutions are half-turns inside \(SO(3)\). |
| V3-14 | fixed | \(1=1^2+0^2+0^2+0^2\) is written before the product. |
| V3-15 | fixed | The three coordinates of the cross product are written, and their squares are expanded. |
| V3-16 | fixed | The supplementary law is Volume 2, Corollary 6.4, which is \(\bigl(\frac{2}{p}\bigr)=(-1)^{(p^2-1)/8}\). |
| V3-17 | fixed | The indicator sum in Theorem 11.14 is \(1\) when \(a=e\). |
| V3-18 | fixed | Volume 1's preface takes \(\sin'=\cos\) and \(\cos'=-\sin\) as standing facts, and the comparison then gives \(\sin h<h<\tan h\). |
| V3-19 | fixed | The two-line Sylow template is written and used on three unlike rows. The four Sylow subgroups are conjugate, so the action is nontrivial. |
| V3-20 | fixed | The cases \(n_2=5\) and \(n_2=15\) are split. The products \(6\cdot4\) and \(10\cdot2\) are displayed. A 3-cycle satisfies \((\tau^2)^2=\tau\). A nontrivial homomorphism from a simple group is injective. The 3-cycles generate \(A_5\) by Proposition 4.5 (`prop:gens`). |
| V3-21 | fixed | Dummit and Foote are cited at Sections 4.3 and 4.6. |
| V3-22 | fixed | The exercises on \(p^2\) and order 8 are named in Chapters 3 and 2. |
| V3-23 | fixed | The order-6 box reads \(D_3\cong\mathfrak S_3\), in the figure and in the text. |
| V3-24 | fixed | A move into the blank is the position \((b\,c)\sigma\). |
| V3-25 | fixed | An \(F\)-turn alternates the primary facet on each of the four edges, in both orientations. |
| V3-26 | fixed | The Rubik solution uses \(\varepsilon\). |
| V3-27 | fixed | The exchange lemma of Chapter 1 is cited with no printed proposition number. #202 removed the reference that was printing as Proposition 1.2. |
| V3-28 | fixed | A constructed regular polygon produces \(e^{\pm 2\pi i/n}\). |
| V3-29 | fixed | \(2X^2-3\) has no rational root in lowest terms. |
| V3-30 | fixed | A constructible \(\sqrt\pi\) would make \(\pi\) algebraic. Lindemann stays quoted. |
| V3-31 | fixed | Agreement on the two generators is the injection into \(\mathfrak S_3\), and the two sets both have six elements. |
| V3-32 | fixed | Chapter 6 still has “in neither modulus” and “a non-zero class whose square is zero.” |
| V3-33 | fixed | \(X\cdot nX^{n-1}-n(X^n-1)=n\). |
| V3-34 | fixed | The state at time 1 modulo 11 is \((1,1)\). |
| V3-35 | fixed | The sum of squares and the division by 27 are written in the Cardano solution. |
| V3-36 | fixed | Only the leading term of \(P\) meets the constant term of \(Q\). |
| V3-37 | fixed | A Euclidean isometry is defined by distances, before the polarization identity. |
| V3-38 | fixed | Left cancellation expands \((a^{-1}a)b=b\). |
| V3-39 | fixed | \(sr^k=r^{-k}s\) is proved, and then \((sr^k)^2=e\). |
| V3-40 | fixed | An element that commutes with both generators is shown to commute with every word, by appending one generator at a time. |
| V3-41 | fixed | The exercise names \(F_0=0\), \(F_1=1\), and the recurrence. |
| V3-42 | fixed | The fresh block of increments is separated from the symmetry \(X_t^{-1}\). |
| V3-43 | fixed | \(HN=\{hn:h\in H,\,n\in N\}\). |
| V3-44 | fixed | Conjugation sends a word in the commutators to the word in the conjugates. |
| V3-45 | fixed | The additive rule is \(k+(-1)^\varepsilon k'\). |
| V3-46 | fixed | The class equation uses \(C_G(x)\). |
| V3-47 | fixed | A centre of order \(p\) makes a group of order \(p^2\) abelian, and the five lines are in the proof. |
| V3-48 | fixed | Independence of the quotient basis uses the extended basis. |

No theorem, proposition, lemma, corollary, or exercise number moves in the reviewed diff. The walker on this head returns the same Volume 3 numbers the index prints.

## Index and the Volume 3 print page count

The index file is byte-identical on the reviewed head and on `origin/main` (`f3ceedbc0496f3c784ea7549adada7835b6ce36a`). The check in the V3-5 row is the validity check: labels resolve, and the printed numbers match the counter.

`volume3-symmetry` and `common/` have an empty diff between the reviewed head and `origin/main`. Those are the sources that set the Volume 3 page breaks. The print page count on this head is the print page count on main. This diff does not typeset Volume 3, and this review did not typeset it either.

## The checker and the regression

`volume3_misplaced_subject` walks every `Volume~3` or `Volume3` mention. Within 80 characters before and 40 after, it rejects the phrases “Vandermonde” and “eigenvalues and traces”, and it rejects the tilde spelling of “Volume~3 or Volume~4”.

Probes on the reviewed source:

- “eigenvalues and traces (Volume~3)” is rejected.
- “eigenvalues and traces (Volume~1, Chapter~7)” is accepted.
- “Volume~3 or Volume~4, Chapter~6” is rejected.
- “Vandermonde determinants (Volume~1, Proposition~7.4)” is accepted.
- A Vandermonde more than 80 characters before `Volume~3` is accepted. One inside that window is rejected.
- `gloss_mismatches()` on the fifteen volumes is empty, so the new scan does not fire on the repaired books.

From `tools/`, `python3 -m unittest test_cross_volume_citations` ran 14 tests and exited 0, including `test_volume3_pointers_name_the_stated_fact` and the full gloss scan.

One branch of the new function does not run. The mention pattern is `Volume~?3`, which asks for a tilde or for no character at all between the word and the digit. The extra test for “Volume 3 or Volume 4” with spaces therefore never sees a match. The books type `Volume~3`, and that spelling is the one the repaired lines use. This does not affect the verdict.

## Scope, voice, and the sentences that were touched

The diff is nine files: the checker, its test, and the seven citation sites in the table. Nothing else moves.

The tools lines are citation lists. The Volume 8 parenthetical, “orthonormal, hence independent,” is the step the dimension needs. The Volume 9 lead-in names the spectral theorem and then the matrix. The elliptic and cokernel sentences name the classification and the corollary. None of them uses a stock opener, a hollow intensifier, or a transition that only announces a change of topic. The curves reminder is the sentence whose mathematics fails: \(K[y]\) is attached to the dividend.

## What clears the verdict

Rewrite the primitive-descent sentence in the Volume 13 reminder so that it matches Proposition 6.17: the primitive polynomial lies in \(R[y]\) and has degree at least 1, the polynomial it divides lies in \(R[y]\), and the given division is the one read in \(K[y]\). The citation number can stay Proposition 6.17.
