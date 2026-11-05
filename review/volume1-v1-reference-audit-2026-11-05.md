# Volume 1 review and V2–V15 reference audit

Date: 5 November 2026.
Branch: `cursor/volume1-high-school-path-f51c`.
Base at the time of the audit: `origin/main` `975672206d3123274289652962f104a170af2a8e` (merge of PR #104, the redone Volume 3). That commit is also the merge-base of this branch with `main`.
This file is an editorial report. It is not part of any volume.

The Volume 1 this branch delivers is the teaching manuscript from PR #106, merged with current `main`. Volume 1 chapter files were not changed on `main` between the previous base and `97567220`. The redone Volume 3 arrived entirely from that merge.

## What “checked” means

A reference was checked when the sentence was read against the current Volume 1, in `main.tex` order, and the cited fact was compared with the statement that actually sits at that number. A label existing was not enough.

Numbered statements in Volume 1 share one counter per chapter (theorem, proposition, lemma, corollary, definition, example). Unnumbered `theoremx` / `propositionx` / `definitionx` / `examplex` do not move the counter. Exercises have their own counter. The language chapter is Chapter 0.

The insert that matters for later books is Proposition 3.11, the sequence for \(e\), in the sequences chapter. It sits after the mean value theorem (Theorem 3.10) and before the sine comparison. Every numbered statement in Chapter 3 after the mean value theorem is one higher than in the text this pull request started from. The shape of Stirling is now Proposition 3.18. Euler’s constant is Proposition 3.17. The full formula \(n!\sim\sqrt{2\pi n}\,(n/e)^n\) is Theorem 8.6. Exercise 3.7 only sharpens the shape and leaves the constant unknown.

## Search

In every `*.tex` file of Volumes 2 through 15:

- `Volume~1` not followed by another digit (so Volume 10–15 are not counted as Volume 1), and the plain strings `Volume 1` and `First Principles`
- `Theorem`, `Proposition`, `Lemma`, `Corollary`, `Exercise`, `Definition` with a number `N.M`, kept only when `Volume~1` is the volume that number belongs to
- `Volume~1, Chapter~N` with the subject in the same sentence
- unnumbered clauses (“Volume 1 proved…”, “Volume 1 admitted…”, tools lines, reminders)
- `Volume~0` (none in Volumes 2–15)
- no `\externaldocument` / `xr` cross-references anywhere in the repository

Maintained maps read: `docs/plan/volume-citation-map.md`, `docs/SERIES-STRUCTURE.md`.

## Per-volume inventory

“Hits” counts occurrences of `Volume~1` / `Volume 1` / `First Principles` in that volume’s tex. “Changed” counts files whose text was edited in this audit.

| Volume | Hits | Files with a hit | Changed files | Result |
| --- | ---: | ---: | ---: | --- |
| 2 The Integers | 67 | 12 | 3 | Basel tools now name Exercise 6.7. Group recall names Chapter 5. Irrationality of \(e\) and \(\pi\) names Chapter 8, not the filename “Integrals and Taylor”. |
| 3 Symmetry | 52 | 15 | 1 | Product, quotient and chain rules were cited as Chapter 5. They are Chapter 3. The other Volume 1 sentences in this volume were read and left. |
| 4 Chance | 90 | 13 | 6 | Stirling uses that need \(\sqrt{2\pi}\) now cite Theorem 8.6. Log-tangent is Proposition 9.1(b) applied to \(-\ln\). Cauchy–Schwarz is Theorem 9.4. \(\Phi_p\) is Exercise 6.5. Limsup is no longer claimed as a Volume 1 definition. |
| 5 Calculation | 66 | 12 | 6 | \(\gamma\) is Proposition 3.17. Full Stirling is Theorem 8.6. Exponential form is Proposition 5.1. Sine product is the unnumbered example in Chapter 5. The \(O(1/n)\) harmonic bound and term-by-term differentiation are stated at the strength Volume 1 actually has. |
| 6 Crossroads | 10 | 3 | 1 | Dominated convergence for series is no longer attributed to Volume 1. Comparison \(\sum k^{-2}<\infty\) stays Chapter 3. |
| 7 Spaces | 29 | 8 | 2 | Intermediate value, extreme value, and the mean value theorem are described as proved in Volume 1, not admitted. The integral is still described as admitted, which matches the preface. |
| 8 Analysis | 9 | 7 | 0 | Read. Determinant uniqueness is Theorem 7.3. No change. |
| 9 Shapes | 0 | 0 | 0 | Searched. No Volume 1 mention. |
| 10 Abstraction | 1 | 1 | 1 | Theorem 6.12 is ordinary symmetric polynomials. The Laurent form is now the one-line reduction by a power of \(e_n\). |
| 11 Randomness | 2 | 2 | 0 | Theorem 3.10 is still Rolle and the mean value theorem. Theorem 4.5 is still Erdős–Szekeres. No change. |
| 12 Random motion | 1 | 1 | 0 | Theorem 7.9 is the spectral theorem. No change. |
| 13 Arithmetic | 3 | 3 | 0 | Proposition 6.8 is rational roots. The root-bound sentence matches the polynomials chapter. No change. |
| 14 Primes | 0 | 0 | 0 | Searched. No Volume 1 mention. |
| 15 Order and Chance | 7 | 4 | 1 | Central binomial with \(\sqrt{2/(\pi n)}\) cites Theorem 8.6, and says the unspecified-constant shape is Proposition 3.18. LYM, Erdős–Szekeres, and Exercise 4.1 were already right. |

Maps: `docs/SERIES-STRUCTURE.md` now lists Orders in the Algebra part of Volume 1. `docs/plan/volume-citation-map.md` no longer says the central-binomial form of Stirling is Exercise 3.7.

## Corrections, with the fact that was wrong

Chapter 3 numbers below are the numbers in the Volume 1 this branch would print.

1. Several books cited “Theorems 3.17 and 8.5” for \(n!\sim\sqrt{2\pi n}\,(n/e)^n\). Proposition 3.17 is Euler’s constant. Theorem 8.5 is the Gaussian integral. The formula with the constant is Theorem 8.6. The shape with an unknown \(C>0\) is Proposition 3.18. Files: `volume4-chance/chapters/ch06-clt.tex`, `volume4-chance/chapters/ch07-walks.tex`, `volume5-calculation/chapters/ch05-gamma.tex`, and the same pair in `volume4-chance/chapters/ch03-generating.tex`, `volume4-chance/chapters/ch12-method.tex`, `volume5-calculation/chapters/ch12-agm.tex`, `volume15-order-and-chance/chapters/ch02-reading.tex`. Exercise 3.7 does not supply \(\sqrt{\pi}\). The Littlewood–Offord tools line in `ch12-method.tex` was pointing at that exercise for \(\binom{2k}{k}2^{-2k}\sim 1/\sqrt{\pi k}\).

2. Euler’s constant was still “Proposition 3.16” in `volume5-calculation/chapters/ch05-gamma.tex` and `ch10-zeta.tex`. It is Proposition 3.17. The boxed statement is \(H_n=\ln n+\gamma+o(1)\). The proof also gives \(0\le H_n-\ln n-\gamma\le\ln(1+1/n)\). `volume5-calculation/chapters/ch02-generating.tex` was using the stronger \(O(1/n)\) form and citing only “Chapter 3”. It now says which half is boxed and which half is in the proof.

3. `volume5-calculation/chapters/ch09-complex.tex` called the exponential form Proposition 2.1. Chapter 2 is counting. The identity \(e^{x+iy}=e^x(\cos y+i\sin y)\) is Proposition 5.1.

4. `volume5-calculation/chapters/ch05-gamma.tex` called \(\prod_{k=1}^{m-1}\sin(k\pi/m)=m/2^{m-1}\) Exercise 5.5. Exercise 5.5 is a different roots-of-unity product. The sine product is the unnumbered example “the product of sines” in Chapter 5.

5. `volume4-chance/chapters/ch04-inequalities.tex` cited “Proposition 4.1(b)” for \(\ln y\le y-1\). Chapter 4 is orders. The tangent inequality is Proposition 9.1(b) in the inequalities chapter, applied to \(-\ln\).

6. `volume4-chance/chapters/ch02-discrete.tex` sent Stirling to Chapter 3 and Cauchy–Schwarz to Chapter 1. Stirling’s constant is Theorem 8.6. Cauchy–Schwarz is Theorem 9.4.

7. `volume4-chance/chapters/ch12-method.tex` said \(\Phi_p\) is irreducible in “Chapter 6”. The proof is the solution of Exercise 6.5, not a main-text theorem.

8. The same file’s self-avoiding-walk tools line said Volume 1, Chapter 3, defines lim sup and lim inf. Volume 1 defines limits of sequences and does not use those words. The solution now names the tail supremum and the tail infimum in the argument, and the tools line says Volume 1 does not define them.

9. `volume6-crossroads/chapters/ch12-modular.tex` attributed “dominated convergence for series” to Volume 1. Proposition 3.16 is nonnegative double sums and rearrangement of absolutely convergent series. The comparison \(\sum k^{-2}<\infty\) is Volume 1. Passing a limit under the sum is not.

10. `volume7-spaces/chapters/ch03-topology.tex` and `ch04-compact.tex` said Volume 1 “admitted” the intermediate value theorem, the extreme value theorem, and the mean value theorem. Volume 1 proves them: Theorems 3.7, 3.8 and 3.10.

11. `volume10-abstraction/chapters/ch11-compact.tex` said a symmetric Laurent polynomial is a polynomial in \(e_1,\ldots,e_n\) and \(e_n^{-1}\) by Theorem 6.12. Theorem 6.12 is the fundamental theorem for ordinary symmetric polynomials. The Laurent case is \(e_n^{-k}\) times such a polynomial. The sentence now says that.

12. `volume5-calculation/chapters/ch10-zeta.tex` tools line said Volume 1, Chapter 3, gives uniform convergence and term-by-term differentiation. Volume 1 never uses those phrases, and one sentence in the sequences chapter says no infinite sum was integrated term by term. The tools line now cites the comparison \(\sum k^{-2}<\infty\) and says the differentiation step is not a theorem of Volume 1.

13. `volume3-symmetry/chapters/ch11-characters.tex` said the product, quotient and chain rules were proved in Chapter 5. Chapter 5 is complex numbers. The rules are Proposition 3.6 in the sequences chapter.

14. `volume2-integers/chapters/ch05-primitive-roots.tex` said “the Basel sum” without a place to find \(\pi^2/6\). It is Exercise 6.7. The same chapter’s earlier sentence that names the Basel exercise was already accurate.

15. `volume2-integers/chapters/ch01-divisibility.tex` recalled groups from a chapter title alone. It now says Chapter 5. `ch08-continued-fractions.tex` sent the irrationality of \(e\) and \(\pi\) to a chapter called “Integrals and Taylor”, which is the filename. The printed title is Differential and Integral Calculus, Chapter 8, Exercise on \(e\) and Niven’s exercise on \(\pi\).

16. `volume4-chance/chapters/ch12-method.tex` tools line for the clique game said only “Volume 1, Chapter 10”. That chapter has expectation of indicators and the union bound. It does not define conditional expectation. The tools line now says so.

## Left on purpose

- Volume 7 still says the integral of a continuous function on a segment is what Volume 1 admitted. That matches the preface and the sequences chapter: the area and four rules are used, Heine’s theorem is named as the reason Riemann sums settle, and Volume 7 is where the integral is built. Volume 1 does not prove existence as a theorem.
- Volume 7 still says Volume 1 admitted the basic properties of \(\exp\), \(\ln\), \(\cos\), \(\sin\) and \(\pi\). The preface still takes those as named facts. The derivative formulas for them are admitted after the word “derivative” is defined.
- `volume4-chance/chapters/extremal.tex` says Volume 1 records the convex-polygon theorem, and then points at a local exercise. Theorem 4.5 is the monotone-subsequence form. Exercise 4.1 is Klein’s five-point polygon. The local exercise label is Volume 4’s own. The sentence is readable; it was not rewritten.
- Numbered citations whose number survived the Chapter 3 shift and whose statement is the fact in the sentence were left. Samples that were re-read and kept: Exercise 1.7 (Fibonacci gcd), Proposition 2.3 (derangements), Proposition 3.4 (convergence criteria, including Bolzano–Weierstrass), Theorem 4.5, Theorem 4.6 (LYM), Exercise 4.1, Theorem 6.4 (d’Alembert–Gauss), Proposition 6.8, Theorem 7.3, Theorem 7.9, Exercise 8.4, Exercise 8.6 (Riemann–Lebesgue for \(C^1\)), Exercise 8.7, Theorem 9.2 (Jensen), Theorem 9.3 (AM–GM), Theorem 9.4.

## Unresolved, not renumbered away

These are real gaps. The sentences now say so instead of pointing at a theorem Volume 1 does not have.

- Lim sup and lim inf are not defined in Volume 1.
- Dominated convergence for a sequence of series is not proved in Volume 1.
- Term-by-term differentiation of a series of functions is not proved in Volume 1.
- Conditional expectation is not defined in Volume 1.
- Theorem 6.12 does not by itself state the Laurent case.
- The constant \(\sqrt{2\pi}\) in Stirling is not Exercise 3.7 and not Proposition 3.18.

## Review of the current Volume 1

This is not a complete reading of every solution. Chapters and passages actually read for this report:

- `volume1-first-principles/main.tex` (full: part and chapter order)
- `chapters/preface.tex` (through the “for the record” remark)
- `chapters/ch05-sequences-series.tex`: the differentiation proposition and its proof opening, the integral-as-area paragraph (Riemann sums, triangle \(1/2\), four rectangles \(5/8\)), Euler’s constant and its proof, the Stirling-shape proposition’s exercise, the sentence that refuses term-by-term integration
- `chapters/orders.tex`: opening through the first think-box
- `chapters/ch03-polynomials.tex`: the root bound and the “agree at enough points” paragraph, enough to check Theorem 6.12’s scope and Exercise 6.5
- `chapters/ch02-complex-roots.tex`: the place \((\Z,+)\) is called a group, and the exponential-form proposition’s neighbourhood (for Proposition 5.1 and the sine product)
- `chapters/ch06-integrals-taylor.tex`: Stirling’s theorem (Theorem 8.6), the \(e\)-irrational exercise, Niven’s exercise
- `chapters/ch04-inequalities.tex`: Jensen, AM–GM, Cauchy–Schwarz, the tangent form of Proposition 9.1(b)

Not read end to end: language, sums, counting, the rest of sequences, the rest of orders, the rest of complex numbers, the rest of polynomials, linear algebra, the rest of calculus, probability, the field guide, and the solution blocks except where a later volume’s citation forced a look.

### Findings

**The three old blockers are still fixed.** The preface says the derivative and the integral are taught in the sequences chapter, and it sets \(e=\exp(1)\approx 2.718\). The differentiation rules are a proposition with a proof, not a reminder. The integral is introduced as area, with a Riemann sum, before it is used. \((1+1/k)^k\to e\) is Proposition 3.11, after the mean value theorem.

**Medium. The preface’s contents list skips Orders.** `preface.tex` around the “Along the way” paragraph names induction, counting, limits, complex numbers, polynomials, linear algebra, calculus, inequalities and probability. It does not name Orders. In `main.tex` Orders is Chapter 4, between sequences and complex numbers: posets, Dilworth, LYM, the Erdős–Ko–Rado theorem. The chapter opening itself is a story and a ten-number example, and it says the chapter uses no limit. A reader who trusted the preface list will still meet that chapter with no warning. Remedy: one sentence in that preface paragraph, naming Orders and repeating the chapter’s own instruction that it can be read after counting. This audit did not edit the preface. Moving the chapter would renumber every later citation that this pass just checked.

**Low. The integral is still a working rule, not a constructed object.** The sequences chapter says the sums settle because of Heine, then takes four rules as known and sends the construction to Volume 7. The preface says the same thing. That is consistent. It is not the existence proof.

**Deferred items from the teaching pass, rechecked rather than assumed.** Orders was not moved. The circulant exercise is still an explicit skip. Summation by parts is still marked as a second reading. Solution prose outside the rewritten solutions was not reread.

## Review of the redone Volume 3

Read:

- `volume3-symmetry/main.tex` (full). Parts: Groups (chapters 1–5), Rings and Polynomials (6–8), Fields and Galois Theory (9–12), then appendices Perron, symmetry, combinatorial, Paley, afterword. ISBN in the source is 9798167514683. Subtitle: Groups, Rings and Fields.
- `chapters/preface.tex` (full)
- `chapters/ch01-groups.tex` opening through the group definition
- `chapters/ch04-symmetric.tex` the cyclotomic reminder before the discriminant exercise
- `chapters/ch11-characters.tex` the passage that rebuilds the sine derivative and the exponential series
- every `Volume~1` line in the volume, against the chapter it names

Not read: the bodies of chapters 2, 3, 5–10, 12, and the four appendices, except the Volume 1 sentences inside them.

### Findings

**The preface’s dependency is accurate.** It says Volume 1 gave polynomials, complex numbers and matrices, and Volume 2 taught residues, primitive roots and Dirichlet characters. The character modulo 4 is called a homomorphism in Volume 2, Chapter 14, with the definition written there. Volume 3 is not inventing that word.

**Fixed in this audit, and it was a real stumble.** In `ch11-characters.tex` the product, quotient and chain rules were “Volume 1, Chapter 5”. A reader who turned back would be in complex numbers. The rules are Chapter 3.

**Medium, not fixed, because this was a review.** The same section then rebuilds \(\sin'=\cos\) from areas of triangles and sectors, and rebuilds \(E(x)=\sum x^k/k!\) from the ratio test. The steps are written out, so the reader is not asked to know a later volume. The stumble is the place: this is a characters chapter in a book of groups, rings and fields, and the digression is not announced as a return to Volume 1’s calculus. Remedy: two sentences at the start of that digression, saying the derivatives are about to be rebuilt and that the chain rule is already Proposition 3.6. Do not delete the argument.

**The cyclotomic reminder is honest.** It says the exercise on Eisenstein’s criterion in Volume 1’s polynomial chapter proves \(\Phi_p\) irreducible, after the shift \(X\mapsto X+1\). That is Exercise 6.5, whose proof is in the solution. The reminder does not pretend there is a main-text theorem.

**No Volume 1 chapter number in this volume was found pointing at the wrong subject**, after the chain-rule correction. Determinants, the sign, the spectral theorem, Lagrange interpolation, Gauss’s lemma, roots of unity, Bolzano–Weierstrass, Cauchy sequences, and the Fibonacci identities sit in the chapters the sentences name. That check was sentence-by-sentence for the Volume 1 clauses, not a reading of the proofs around them.

## Validation

- `git diff --check` on the citation edits: clean.
- `tools/check_edition_copy.py` on Volumes 1–3, 4–7, 10 and 15: clean.
- There is no repository script that checks cross-volume citation numbers. The table above is the check.
- XeLaTeX, two passes, `PRINTINNER=0.9in`, then `tools/check_book_layout.py`:
  - Volume 1, after the merge with current `main` (preamble included): 421 whole boxes, maximum height 507.4 pt, no overflow, no unresolved references. Volume 1 text was not edited in the citation commit.
  - Volumes 2, 3, 4, 5, 6, 7, 10 and 15, the volumes whose text changed or whose Volume 3 text is new: each compiled with exit code 0, and the layout check passed. Box counts: V2 389 (max 371.3 pt), V3 409 (432.6), V4 439 (315.2), V5 389 (383.4), V6 272 (479.1), V7 330 (262.0), V10 272 (384.6), V15 279 (401.4).
- Not run: EPUB, KDP print export, cover checks, and XeLaTeX for Volumes 8, 9, 11, 12, 13 and 14. Those six had no text change. Volumes 9 and 14 have no Volume 1 mention. The layout check on a single first pass fails with unresolved references; that is the aux, and the second pass cleared it. A successful compile is not a proof that every citation is the right theorem. The semantic audit is the table and the correction list.

`origin/main` was fetched again immediately before this report and was still `975672206d3123274289652962f104a170af2a8e`.
