# Second review of PR #197

**Verdict: REQUEST CHANGES**

**Head reviewed:** `e3e25b4b5d3484d78a0c46802f35abfc19d89d8b` on `cursor/volume2-apply-scored-read`.

**Pull request:** https://github.com/OussamaSegh/Order-and-Chance/pull/197

**Source log:** PR #174, `docs/review/volume2-independent-scored-read-2026-11-11.md`, rows V2-01 through V2-23, scored at `8645c9e11eae13e30c59052d2199db5c17b0d383`.

This review was written without pushing to that branch and without merging it. The diff was read at the head above, in a detached worktree at `/tmp/review197/tree`. The mathematical repairs inside Volume 2 hold. The claim that every later citation now names the printed statement does not.

## What was run

All of the following were run on the tree at `e3e25b4b`, except the page-count builds, which were `./build.sh --pdf-only` in that same worktree.

- `python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1178}` and exited 0.
- From `tools/`, `python3 -m unittest test_cross_volume_citations.py test_volume2_dependency_review.py test_volume2_exercise_keys.py test_volume2_manuscript.py -v` ran 45 tests and exited 0. That includes `test_swapped_volume2_chapter_is_rejected`, `test_volume2_numbers_match_the_printed_statements`, and `test_resolved_volumes_have_no_mismatch`.
- `python3 tools/cross_volume_citations.py` exited 1 and printed `198 citation mismatches`. None of those lines contains `Volume 2`. The open cited volumes in the unit test are `{3, 5, 7, 8, 10, 12}`. Volume 2 is closed for that existence-and-kind check. The subject checker did not flag a Volume 2 line either. The two wrong citations below survive both checks: the number exists and has the right kind, and the nearby words are not in the short subject list.
- `./build.sh --pdf-only volume2-integers` exited 0. `build/volume2-integers/main.log` has no line containing `Overfull` and no line containing `undefined`. The same log has 27 lines containing `Underfull`. `tools/check_book_layout.py`, as reported by the build, checked 391 whole boxes, maximum height 371.3 pt, and reported no overflow and no unresolved references.
- `pdfinfo` on `build/volume2-integers/main.pdf`: 337 pages, 504 × 720 pt.
- `pdfinfo` on `dist/kdp/Volume 2 - The Integers - Print.pdf`: 337 pages, 513 × 738 pt, PDF 1.3, encrypted no, empty title, author, subject, keywords, creator, and producer. Every page rectangle is 513 × 738 pt. The build log's own line is `KDP interior checked: 337 pages, PDF 1.3`.
- The index in `volume2-integers/chapters/index.tex` has 77 `\ocindexpage` entries. Every label is a `\newlabel` in `main.aux`. For each of the 72 entries that print a theorem, proposition, lemma, corollary, exercise, definition, or chapter number, that number agrees with the aux label and the PDF page whose label is that folio contains the number. The five unnumbered entries were read on the folio the aux records: the valuation on folio 6, Legendre's formula on folio 7, φ on folio 51, μ on folio 86, and `|x|_p` on folio 319.
- `./build.sh --pdf-only volume3-symmetry` exited 0. Interior and print PDFs are 517 pages. The interior log has no `Overfull` and no `undefined` (39 underfull lines). Layout: 408 whole boxes, maximum 432.6 pt, no overflow and no unresolved references. Print page size 513 × 738 pt, PDF 1.3, encrypted no.
- `./build.sh --pdf-only volume6-crossroads` exited 0. Interior and print PDFs are 275 pages. The interior log has no `Overfull` and no `undefined` (40 underfull lines). Layout: 272 whole boxes, maximum 479.1 pt, no overflow and no unresolved references. Print page size 513 × 738 pt, PDF 1.3, encrypted no.
- Volumes 5, 7, 8, 9, 10, 11, 13, and 15 were not rebuilt here. Their page counts in the pull request are unchecked.
- `ζ(3)/(4ζ(2))`, with `ζ(2)=π²/6` and the partial sum for `ζ(3)` through 500,000 plus the integral tail, is `0.182690742`. The printed `0.18269…` matches. The Jacobi symbol `(43/91)` is `+1`, and `(3/5)=-1`. Euler's four-square formula, evaluated on `(1,2,3,4)` and `(5,-1,2,0)`, gives `900` on both sides.

## Printed chapter numbers

`volume2-integers/main.tex` inputs the chapters in this order. The printed numbers follow. There is no printed Chapter 12, 13, or 14.

| Printed | File | Title |
|---|---|---|
| 1 | `ch01-divisibility.tex` | Divisibility and the Euclidean Algorithm |
| 2 | `ch02-primes.tex` | Primes |
| 3 | `ch03-congruences.tex` | Congruences |
| 4 | `ch04-arithmetic-functions.tex` | Arithmetic Functions |
| 5 | `ch05-primitive-roots.tex` | Primitive Roots and the Multiplicative Group |
| 6 | `ch06-quadratic-reciprocity.tex` | Quadratic Residues and Reciprocity |
| 7 | `ch07-sums-of-squares.tex` | Sums of Squares |
| 8 | `ch09-diophantine.tex` | Diophantine Equations |
| 9 | `ch08-continued-fractions.tex` | Continued Fractions and Pell's Equation |
| 10 | `ch10-gaussian-eisenstein.tex` | Gaussian and Eisenstein Integers |
| 11 | `ch14-characters.tex` | Characters, Euler Products and the Sieve |

The citation-map change is right against that order. In `docs/plan/volume-citation-map.md` the Now column sends old chapter 4 (primitive roots, file `ch05`) to Volume 2, Chapter 5; old chapter 5 (reciprocity, file `ch06`) to Chapter 6; old chapter 6 (arithmetic functions, file `ch04`) to Chapter 4; old chapter 8 (continued fractions, file `ch08`) to Chapter 9; and old chapter 9 (Diophantine equations, file `ch09`) to Chapter 8. The prose paragraph states the same printed order. The Old ch. column was left as the historical number. That is what the table header says it is.

## Volume 2 rows

`python3` numbering of the head, walking `main.tex` in input order, still gives Euclid's lemma as Theorem 1.5, the fundamental theorem as Theorem 1.6, Bertrand as Theorem 2.5, Euler–Fermat as Theorem 3.3, the Chinese remainder theorem as Theorem 3.5, the totient sum as Proposition 3.7, Hensel as Theorem 3.8, Dirichlet convolution as Proposition 4.3, Möbius inversion as Theorem 4.4 (`μ*1=ε`), the hyperbola theorem as Theorem 4.6, the order as Proposition 5.2, cyclicity of `(Z/pZ)×` as Theorem 5.3, cyclicity for `n=p^k` and `n=2p^k` (`p` odd, `k≥1`) as Theorem 5.5, the Legendre symbol as Definition 6.1, Euler's criterion as Theorem 6.2, Gauss's lemma on the symbol as Theorem 6.3, the law for 2 as Corollary 6.4, reciprocity as Theorem 6.5, the two-square criterion as Theorem 7.3, four squares as Theorem 7.4, primitive triples as Theorem 8.1, Fermat's fourth-power equation as Theorem 8.2, the convergent formula and the determinant `p_n q_{n-1}-p_{n-1}q_n=(-1)^{n-1}` as Proposition 9.1, the error bound as Theorem 9.2, the existence of the value of an infinite expansion as Lemma 9.3, best approximation as Lemma 9.4, Legendre's test as Theorem 9.5, periodicity as Theorem 9.6, Pell as Theorem 9.8, Gaussian primes as Theorem 10.5, Jacobi as Theorem 10.6, Eisenstein primes as Theorem 10.7, and the cube theorem as Theorem 10.9. Exercise 1.3 is still Legendre's count, Exercise 1.4 is the monic rational-root statement, Exercise 1.9 is the factorial argument used in Lucas's solution, Exercise 1.11 is Kummer's carry count, Exercise 1.15 is the orchard, Exercise 2.9 is the prime factor of `n!+1`, Exercise 4.2 is `2^{ω(n)}=∑|μ(d)|` (equal to `∑μ²(d)`), Exercise 4.7 is primitive words, Exercise 4.8 is the coprime probability, Exercise 5.4 is the power sum, Exercise 5.7 is primes `≡1 (mod n)`, Exercise 6.7 is `g²=p*`, Exercise 7.1 is the three-square obstruction, Exercise 9.7 is Liouville's number, Exercise 10.2 is the failure in `Z[√-5]`, and Exercise 10.5 is `x³=y²+1`.

Legendre's formula is an unnumbered `propositionx`. It does not move any later number. Lemma 2.3 now cites that main-text formula. The forward pointer to Exercise 1.3 is recorded as `practice` in `docs/reviews/volume2-forward-reference-review-2026-11-04.json`, with the reason that the proof of Lemma 2.3 uses the main text.

The six dot products in the four-square expansion are zero, and each row has squared length `∑b_j²`. The displayed identity is the orthogonal assembly of those rows. The statement is every non-negative integer, and the proof writes the zero tuple and `1²+0²+0²+0²` before the descent. Gauss's lemma remains the name of Theorem 6.3 only. The remaining uses of that name in Volume 2 are the Legendre-symbol lemma. The Hensel arrows run from modulo 5 down to modulo 125. The two-square cells are `ocTeal!30` and `ocCoralDeep!12`. The lattice arrow runs from height 5 to `4√2`. The cube step uses Lemma 10.8: a cube prime to `λ` is `±1` modulo `λ⁴`, so a sum of two such cubes is `0` or `±2`; `±2` is not divisible by `λ` because `3` does not divide `N(2)=4`.

Eight exposition ids in `review/volume3-internal/exposition.json` were removed and eight new ids appeared, one pair on each edited passage. For each pair the status is still `accepted-internal`, and the review fields (`reconstruction_A`, `adversarial_check_B`, `boundary_probes`, `defects_and_corrections`, and the rest of that record aside from `id`, `sha256`, `line`, and `claim`) match. Concept, proof, exercise, dependency, and forward-reference statuses have no changed status value.

## Rulings the pull request asked for

**Binary quadratic forms.** `volume6-crossroads/chapters/ch12-modular.tex` Exercise 12.42 (`pb:euler41`) asks the reader to prove that a reduced positive definite form satisfies `a≤√|D|/3`. Volume 2 does not contain that reduction. The tools line now cites the Legendre symbol through Volume 2, Theorem 6.5 and Corollary 6.4. Corollary 6.4 is the law for 2, `(2/p)=(-1)^{(p²-1)/8}`. The pull-request summary calls that pair "Theorems 6.5 and 6.4". The manuscript says Corollary 6.4. The manuscript is the right repair.

**Lemma 8.3.** In `volume7-spaces/chapters/ch12-harder.tex` the sentence uses two facts: the exact error `|x-p_n/q_n|=1/(q_n(x_{n+1}q_n+q_{n-1}))`, which is Theorem 9.2, and `|qx-p|≥|q_n x-p_n|` whenever `1≤q<q_{n+1}`, which is Lemma 9.4 word for word. Lemma 9.3 is the existence lemma, "an infinite expansion determines its number." Under filename numbering that existence lemma would have been Lemma 8.3 of the continued-fraction file. The inequality the old sentence displayed is the best-approximation lemma, so the retargeting from 8.3 to 9.4 is right. The claim that the old "Lemma 8.3" was not the existence lemma is true of the fact the sentence uses.

**No Chapter 13.** Volume 2's printed chapters stop at 11. The field guide defines `|x|_p=p^{-v_p(x)}` on the rationals and names the symbols `Z_p` and `Q_p`. It does not construct compatible residue sequences. Dropping the old "Volume 2, Chapter 13" pointer is right. The replacement sentence overstates the field guide; that is CITE-04 below.

## Issue log

| ID | Location | Problem | Required fix |
|---|---|---|---|
| CITE-01 | `volume13-arithmetic/chapters/ch12-ideals-quadratic.tex:400` | Cites Volume 2, Theorem 1.4 for "the Bézout property in a Euclidean domain" that makes all ideals principal in `Z[i]`, `Z[ω]`, and `Z[√-2]`. Theorem 1.4 states Bézout for ordinary integers: `au+bv=gcd(a,b)`. The Euclidean-domain statement, including part (a) labelled Bézout, is Theorem 10.3. | Cite Theorem 10.3. |
| CITE-02 | `volume15-order-and-chance/chapters/ch09-lean.tex:87` | Says the proof of Theorem 2.1 is that a prime factor of `n!+1` cannot be at most `n`. Theorem 2.1 proves infinitude from `N=p_1\cdots p_k+1`. The factorial argument is Exercise 2.9. | Cite Exercise 2.9 for the factorial sentence, or rewrite the sentence to the product in the proof of Theorem 2.1. |
| CITE-03 | `volume6-crossroads/chapters/ch05-pnt.tex:585` | Attributes the count of lattice points in the disc of radius `√x`, asymptotically `πx`, to Volume 2, Chapter 10. Chapter 10 identifies Gaussian integers with those lattice points and proves Jacobi's formula. The asymptotic `N(R)∼πR²` is Theorem 7.5. The sentence also allows a direct count. | Cite Theorem 7.5 for the asymptotic, or leave the count as the area of the disc and drop the chapter number. |
| CITE-04 | `volume7-spaces/chapters/ch02-metric.tex:187` | Says the field guide of Volume 2 names the closed unit ball `Z_p={x:\|x\|_p≤1}` of the completion. The field guide defines the absolute value on `Q` and names the symbols `Z_p` and `Q_p`. It does not identify `Z_p` with that ball. | Say the field guide names the absolute value and the symbol `Z_p`. The ball and the compatible sequences are constructed in this chapter. |
| CITE-05 | `volume13-arithmetic/chapters/ch12-elliptic.tex:11` | Cites Theorem 8.2 for "no right triangle with rational sides has a square area." Theorem 8.2 states that `x⁴+y⁴=z²` has no positive integer solution, and in particular that `x⁴+y⁴=z⁴` has none. The rational-triangle claim is not in that theorem. The later reminder in the same chapter, which cites Theorem 8.2 for the equation and Theorem 8.1 for integer-sided right triangles, matches the statements. | Keep Theorem 8.2 on the equation. State the square-area claim only with the reduction that produces it, or leave the citation on the equation alone. |
| IDX-01 | `volume2-integers/chapters/index.tex:4` and `:77` | The opener says "The numbers are the printed ones. In the reading and print PDFs, a page number follows the statement." A reader of the book does not need that production sentence. The symbol line then sends `a\|b`, `gcd`, and `lcm` to Theorem 1.4, folio 5, and says symbols are listed where the book defines them. `a\|b` is defined on folio 3, `gcd` on folio 4, and the lcm formula is in the valuation paragraph on folio 6. | Open with one sentence: each name points at the statement, and a page number follows it. Point each symbol at the paragraph that defines it. |

## Rows that hold

V2-02 through V2-23, read against the edited source and the numbering above, do what the pull request says. Theorem, proposition, and exercise numbers are unchanged. Euclid's lemma keeps the label `thm:gauss` and the number 1.5. The new proofs use only the preceding definitions in this volume, or Volume 1's linear algebra for the dot product that the four-square rows have already expanded. The optional three-star banners on Exercises 1.15, 3.16, and 3.18 match the book's "optional exploration" pattern, and the main route does not call those arguments as premises. The new mathematical sentences are plain. The index opener is the voice failure, IDX-01.

V2-01 is not finished. The filename swap is gone from the citations that the scored read listed, and the checker now rejects that swap when the subject phrase sits next to the number. CITE-01 through CITE-05 are Volume 2 pointers whose nearby claim is still a different statement from the item they name. CITE-01 and CITE-02 were introduced by adding a theorem number to a sentence that had only said "Volume 2."

## Recheck at `2aef4b5f`

**Verdict: APPROVE**

**Head:** `2aef4b5f405284b2eff15a218e1af56dd8a5b9fe` on `cursor/volume2-apply-scored-read`. One commit after `e3e25b4b`: "Point the remaining Volume 2 citations at the fact they name."

This recheck did not push to that branch and did not merge it. The diff from `e3e25b4b` was read in the same detached worktree. `origin/main` is still `c734fe3a`, the parent of the review commit, so this branch did not need a merge from `main`.

GitHub runs [43188775406](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43188775406) (Build books) and [43188775171](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43188775171) (Volume 4 native production QA) both completed with conclusion `success` at this SHA.

### What was run on `2aef4b5f`

- `./build.sh --pdf-only volume2-integers` exited 0. `build/volume2-integers/main.log` has no `Overfull` and no `undefined` (27 underfull lines). Layout: 391 whole boxes, maximum 371.3 pt, no overflow and no unresolved references.
- `pdfinfo` on `build/volume2-integers/main.pdf`: 337 pages, 504 × 720 pt.
- `pdfinfo` on `dist/kdp/Volume 2 - The Integers - Print.pdf`: 337 pages, 513 × 738 pt, PDF 1.3, encrypted no, empty title, author, creator, and producer. Every page rectangle is 513 × 738 pt. The build log says `KDP interior checked: 337 pages`.
- The index has 80 `\ocindexpage{...}` entries. Every label is in `main.aux`. Each of the 72 numbered entries has the printed number on the PDF page whose label is that folio. The eight unnumbered entries land on the folio that holds the words: Legendre's formula on folio 7, `a|b` on folio 3 ("We write"), `gcd` on folio 4 ("greatest common divisor"), `lcm` and `v_p` on folio 6, φ on folio 51, μ on folio 86, `|x|_p` on folio 319. Exercise 2.9 is on folio 41, and that page prints "every prime divisor of n! + 1 exceeds n".
- From `tools/`, `python3 -m unittest test_cross_volume_citations.CrossVolumeCitations.test_volume2_pointers_name_the_stated_fact test_cross_volume_citations.CrossVolumeCitations.test_volume2_numbers_match_the_printed_statements -v` ran 2 tests and exited 0.
- `python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1178}` and exited 0. The concepts file changes only snapshot hashes. No review status changes.

### The six fixes

| ID | Ruling |
|---|---|
| CITE-01 | Fixed. The sentence now cites Theorem 10.3 for the Bézout property in a Euclidean domain. Theorem 10.3(a) is that property for the three rings, and for a domain with Euclidean division. |
| CITE-02 | Fixed. The Lean sentence cites Exercise 2.9. That exercise says every prime divisor of `n!+1` exceeds `n`. The formalisation uses `minFac (n ! + 1)`. Theorem 2.1 is no longer named there. |
| CITE-03 | Fixed. The disc of radius `√x` is cited as Theorem 7.5. That theorem is `N(R)∼πR²` for `x²+y²≤R²`, so the count at radius `√x` is `∼πx`. |
| CITE-04 | Fixed. The field guide is now said to name the symbol `Z_p` and the absolute value `|x|_p`. The next sentence says the closed unit ball and the compatible sequences are built in Volume 7. |
| CITE-05 | Fixed. Ruled below. |
| IDX-01 | Fixed. The opener is "Each name points at the statement, exercise or definition it names." The page number is still printed by `\ocindexpage`. `a\|b` points at the sentence that defines it, `gcd` at the definition as the positive generator of `aZ+bZ`, and `lcm` at the valuation formula. Those are folios 3, 4, and 6. |

### CITE-05

The square-area claim is now supported, and it is not left as what Theorem 8.2 says.

The opening sentence cites Theorem 8.2 only for `x⁴+y⁴=z²` having no positive integer solution. That is the statement of the theorem. The square-area sentence then names two results in this chapter. Proposition `prop:congruent` states the two maps and proves they are inverse bijections between rational triples `a²+b²=c²`, `ab=2n`, and points of `y²=x³-n²x` with `y≠0`. The algebra in that proof checks: the forward map gives area `n` because `y²=x³-n²x`, and the reverse map recovers `a`, `b`, and `c`. Theorem `thm:onecongruent` proves that `E_1(Q)` is exactly the four torsion points, by a 2-descent that does not assume the triangle claim. The consequences paragraph then uses the proposition: `1` is not congruent, and a rational right triangle of area `s²` scales by `1/s` to one of area `1`. The sides stay rational when `s` is rational. That is the square-area statement, proved in the theorem the sentence names. The rank proof does not call that conclusion as a premise.

### The Volume 5 Gauss sum

`volume5-calculation/chapters/ch08-transform.tex` now says Exercise 6.7 gives `G(p)²=((−1)/p)p`. Exercise 6.7 defines `p^*=((−1)/p)p` and `g=∑(a/p)ζ^a`, asks for `g²=p*` in (a), and asks in (d) to show `g=∑_{x=0}^{p-1}ζ^{x²}` and to say what (a) then gives for that sum. Volume 5's `G(p)` is that sum. The identity is the exercise, not a theorem of the chapter text. The following "hence `±`" is the same sign left open in the exercise solution.

### Diff from `e3e25b4b`

The manuscript edits are the six repairs, the Exercise 6.7 citation, three definition labels in Chapter 1, and the new index line for Exercise 2.9. No theorem, proposition, or exercise number moves. The new citation test anchors Theorem 2.1, Exercise 2.9, Theorem 7.5, and Theorem 10.3 to the same labels as before. The Volume 3 concept records change only the snapshot hash of `ch01-divisibility.tex` and the volume snapshot. Nothing else in the citation sentences changed. The other Volume 2 pointers read at `e3e25b4b` are still the same sentences.
