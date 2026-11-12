# Second review of PR #199

**Verdict: REQUEST CHANGES**

**Head reviewed:** `299895f839487dd0c6e9392a292c6e9c5c08e1c8` on `cursor/volume3-apply-scored-read-c1a4`.

**Pull request:** https://github.com/OussamaSegh/Order-and-Chance/pull/199

**Source log:** PR #173, `docs/review/volume3-independent-scored-read-2026-11-11.md`, rows V3-1 through V3-48, at `8d9ef257a7380bc1c620c1c13186469cb27c4b33`. That pull request is still open. The log is not on `main`.

This review was written without pushing to that branch and without merging it. The diff was read at the head above, in a detached worktree at `/tmp/review199/tree`. The repairs of the forty-eight rows are real, with one exception: the derivative sentence in the circulant solution names the wrong proposition. A few smaller defects sit beside that sentence. No numbered theorem, proposition, lemma, corollary, or exercise moved.

## What was run

All of the following were run on the tree at `299895f8`, except where a command is named as reading `main` for a comparison.

- `python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1177, "pending": 19}` and exited 0.
- From `tools/`, `python3 -m unittest test_cross_volume_citations.py -v` ran 12 tests and exited 0. That includes `test_resolved_volumes_have_no_mismatch` and `test_volume3_pointers_name_the_stated_fact`. Volume 3 is no longer in `OPEN_CITED_VOLUMES`.
- The walker in `tools/cross_volume_citations.py` finds 109 citations of Volume 3 in Volumes 9, 10, 13, 14, and 15. Every cited theorem, proposition, lemma, corollary, exercise, and chapter number exists and has that kind. The subject mismatches below are outside that check: the number exists, and the nearby words are not in the walker's subject list.
- The same walker, run on this head and on `main` at `1ac3cb11`, returns the same 375 numbered statements in the same order. No label changes its kind or its number. The new exchange argument is `\begin{lemmax}`, and `common/interior-boxes.tex` defines `lemmax` with `\newtheorem*`, so it takes no number.
- `./build.sh --pdf-only volume3-symmetry` exited 0. `build/volume3-symmetry/main.log` has no line containing `Overfull` and no line containing `undefined`. The same log has 39 lines containing `Underfull`. `tools/check_book_layout.py`, as reported by the build, checked 408 whole boxes, maximum height 432.6 pt, and reported no overflow and no unresolved references.
- `pdfinfo` on `build/volume3-symmetry/main.pdf`: 523 pages, 504 × 720 pt, PDF 1.5.
- `pdfinfo` on `dist/Volume 3 - Symmetry.pdf`: 524 pages, 504 × 720 pt, PDF 1.5. The extra page is the front cover.
- `pdfinfo` on `dist/kdp/Volume 3 - Symmetry - Print.pdf`: 523 pages, 513 × 738 pt, PDF 1.3, encrypted no, empty title, author, subject, keywords, creator, and producer. Every page rectangle is 513 × 738 pt. The build log's own line is `KDP interior checked: 523 pages, PDF 1.3`.
- The 11 November release recorded in the source log had a 517-page print interior. This head's print interior is 523 pages. The pull request does not invent a page count. The measurement above is the one the KDP section left to the build.
- The index in `volume3-symmetry/chapters/index.tex` has 96 `\ocindexpage` entries. Every label is a `\newlabel` in `main.aux`, and the number printed beside the label agrees with the aux. For each entry, the interior PDF page whose label is that folio contains the number, or the name when the entry is unnumbered. The index itself is folios 509–512. About the Cover is folio 513. Spot checks of the statement pages: Proposition 1.2 on folio 3, Proposition 1.4 on folio 6, Lemma 6.16 and Theorem 6.18 on folios 160 and 161, Theorem 8.20 on folio 222, Exercise 10.1 on folio 281, Lemma 12.3 on folio 356, Theorem C.12 on folio 477.
- Figure 5.1 is on folio 128. The order-6 box reads \(D_3\cong\mathfrak S_3\) and sits clear of the \(2p\) column. The render is `build/volume3-symmetry/main.pdf`, page label 128.
- The chapter and appendix probes `review/volume3-internal/check_chapter1.py` through `check_chapter12.py`, `check_appendix_a.py` through `check_appendix_d.py`, `check_global_chapter1.py`, `check_global_copy.py`, and `check_global_ledgers.py` exited 0. Appendix B, Chapter 4, and Chapter 12 import `mpmath`, which was installed for this run. `check_output_links.py`, `check_reader_behavior.py`, and `check_reader_browser.py` were not run: the first requires a site and an EPUB, and the other two import Playwright. This build was `--pdf-only`.
- Volumes 9, 10, 13, 14, and 15 were not rebuilt. Their page movement from the longer citation sentences is unchecked.

External checks used for the new sources and for the derivative sentence: Dummit and Foote, 3rd ed., Section 4.3 is conjugation and the class equation, and Proposition 11 of that section is the cycle-type criterion; Section 4.6 is the simplicity of \(A_n\). Paley, *Journal of Mathematics and Physics* 12 (1933), 311–320, is the orthogonal-matrix paper. Hadamard, *Bulletin des Sciences Mathématiques* 17 (1893), 240–246, is the determinant note. Paley's *Proceedings of the London Mathematical Society* (2) 34 (1932) is two consecutive articles, (I) on 241–264 and (II) on 265–279. Volume 1's preface names \(\sin'=\cos\) and \(\cos'=-\sin\) as standing facts, and Proposition `prop:sincmp` uses those facts to prove \(\sin h<h<\tan h\).

## Numbering

`volume3-symmetry/main.tex` is unchanged in chapter order. The walker still gives Lemma 6.16 as Gauss's content formula, Proposition 6.17 as the primitive-polynomial criterion and the divisibility descent, Theorem 6.18 as "\(R\) a UFD implies \(R[X]\) a UFD", Exercise 10.1 as the cyclotomic exercise `ex:phin`, Exercise 10.8 as Cardano, Proposition 10.9 as the cyclotomic injection (an isomorphism when \(n\) is prime), Theorem 8.19 as the quartic non-constructibility proposition, Theorem 8.20 as the primitive element theorem, Theorem C.11 as the combinatorial nullstellensatz, Theorem C.12 as Cauchy–Davenport, and Lemma 12.3 as Euler's axis lemma. Corollary 7.7 remains the classification of finitely generated abelian groups, and Theorem 7.6 remains the structure theorem for finitely generated modules over a PID.

The exchange lemma, label `lem:anyfield`, sits in Chapter 1 after the field axioms and before the examples. It is unnumbered. Chapters 7 and 8 cite it for rank and for the tower law. Nothing later in the numbered sequence shifts.

## Issue log

| ID | Ruling |
|---|---|
| V3-1 | Fixed. Volumes 13 and 15 cite Exercise 10.1 for \(\Phi_n\in\mathbb Z[X]\), the degree \(\varphi(n)\), and \(\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^*\). The solution of Exercise 10.1 boxes both the degree and the isomorphism. Proposition 10.9 is named only for the injection and the prime case. Exercise 10.8 remains Cardano. Volume 10's use of Proposition 10.9, in the Burnside lemma of `ch08-semisimple.tex`, is the sentence that \(\mathbb Q(\zeta_m)/\mathbb Q\) is Galois, which is what that proposition says for every \(n\). |
| V3-2 | Fixed. Theorem 6.18 states that a UFD coefficient ring gives a UFD polynomial ring, and names \(K[X_1,\ldots,X_n]\). Proposition 6.17 states the descent for a primitive polynomial. Volumes 10 and 13 cite those numbers for those facts. Lemma 6.16 remains the content formula. |
| V3-3 | Fixed. Cauchy–Davenport is Theorem C.12 in Volume 14 and in the three-cubes solution of Volume 15. Theorem C.11 remains the combinatorial nullstellensatz. |
| V3-4 | Fixed for the three pointers the log named. Lemma 12.3 is cited for the axis-angle statement. The exponential of \(L(u)\) is stated in Volume 9 from the eigenvalues \(0,\pm i|u|\). The spectral theorem is Volume 1, Theorem 7.9, and the squared volume is Volume 1, Theorem 7.10 (the Gram determinant). The primitive element theorem is Theorem 8.20; Theorem 8.19 is the quartic obstruction. A different Volume 9 pointer, to Chapter 3 for the matrix exponential, is F-5 below. |
| V3-5 | The index exists, and its 96 page numbers match the built interior. The opener and the running head are F-2 and F-3. |
| V3-6 | Fixed. The Rokicki–Kociemba–Davidson–Dethridge item is gone from Chapter 1 and remains in Chapter 4, beside the cube. |
| V3-7 | Fixed. Appendix D has a sources list: Sylvester 1867, Hadamard 1893 (pages 240–246), Paley 1932 and 1933, and arXiv:2610.27175. The 1932 range 241–279 is the union of parts (I) and (II). |
| V3-8 | Fixed. The case \(a=0\) is \(\binom{m}{1}=m\), and both sides of the congruence are \(m\). |
| V3-9 | Fixed. The converse cites Frobenius, Theorem A.6, for a nonnegative eigenvector of an irreducible nonnegative matrix. |
| V3-10 | Fixed. Strict positivity of a nonzero nonnegative eigenvector is taken from the same theorem: such a vector is a positive multiple of the positive Perron vector. |
| V3-11 | Fixed. The icosahedral case cites the Chapter 1 classification and applies it to every Sylow subgroup through \(a\). The classification is Exercise `ex:order4`, whose solution is in the book: both groups of order 4 are abelian. |
| V3-12 | Fixed. A pure unit perpendicular to the axis conjugates \(\cos(\theta/2)+u\sin(\theta/2)\) to \(\cos(\theta/2)-u\sin(\theta/2)\), using \(vu=-uv\) and \(v^{-1}=-v\), both already in Proposition `prop:quat`. That quaternion is rotation by \(-\theta\). |
| V3-13 | Fixed. The six extra involutions are named as half-turns about equatorial axes inside \(SO(3)\), and the word reflection is kept for the planar model. |
| V3-14 | Fixed. \(1=1^2+0^2+0^2+0^2\) is written before the product sentence, and 1 is called the empty product. |
| V3-15 | Fixed. The three coordinates are written, and their squares are identified with \(\sum_{i<j}(u_iv_j-u_jv_i)^2\), which expands to the Lagrange identity. |
| V3-16 | Fixed. The supplementary law is cited as Volume 2, Corollary 6.4. |
| V3-17 | Fixed. Theorem 11.14 and its proof use the identity \(e\). |
| V3-18 | Not fixed. Ruled as F-1. |
| V3-19 | The template, the three sample rows, the table, and the six leftover orders are written, and the homomorphism into \(\mathfrak S_4\) names its kernel and the bound 24 on the image. \(\mathfrak S_4\) is already shown solvable, by the chain \(\{e\}\trianglelefteq V\trianglelefteq A_4\trianglelefteq\mathfrak S_4\), before this induction, so the appeal is not circular. The one missing clause is F-7. The Chapter 5 probe reports the 27 table orders and the six exceptions. |
| V3-20 | Fixed. \(n_2=5\) and \(n_2=15\) are split. The products \(6\cdot4\), \(10\cdot2\), \(15\cdot2\), and \(15\cdot3\) are displayed. A 3-cycle \(\tau\) satisfies \((\tau^2)^2=\tau\). A nontrivial homomorphism from a simple group is injective, and that sentence is used for the embeddings. |
| V3-21 | Fixed. The citation is Sections 4.3 and 4.6. Section 4.3 contains Proposition 11, the cycle-type criterion, and Section 4.6 is the simplicity proof. |
| V3-22 | Fixed. Exercises on \(p^2\) and order 8 are named in Chapters 3 and 2. Order 12 stays below. |
| V3-23 | Fixed. The order-6 box reads \(D_3\cong\mathfrak S_3\), in the same script size, and the rendered folio 128 does not collide with the \(2p\) label. |
| V3-24 | Fixed. A move from cell \(c\) into the blank \(b\) is the position \((b\,c)\sigma\), and the sign is the sign of that transposition. |
| V3-25 | Fixed. On an \(F\)-turn the primary facet of each of \(UF,FR,DF,FL\) alternates, in both orientations, and a counterclockwise turn is the inverse of that toggle. |
| V3-26 | Fixed. The Rubik solution uses \(\varepsilon\). |
| V3-27 | The unnumbered exchange lemma proves bases, equal dimension, and the subspace theorem by Steinitz exchange, dividing only by a nonzero coefficient. Chapters 7 and 8 cite it. The sentence that introduces dimension over \(R/(p)\) is F-4. |
| V3-28 | Fixed. After the field operations, the centre is the intersection of two perpendicular bisectors from Step 1, and \((w-c)/(v-c)=e^{\pm 2i\pi/n}\). The heptagon, the nonagon, and the prime \(p\)-gon use that converse. |
| V3-29 | Fixed. The case \(a=0\) says \(b\) is a rational root of \(2X^2-3\), and the candidates \(\pm1,\pm3,\pm1/2,\pm3/2\) are the ones Volume 1's rational-root proposition allows. None satisfies the equation. |
| V3-30 | Fixed. Wantzel says a constructible number is algebraic. If \(\sqrt\pi\) were algebraic then so would \(\pi\). Lindemann stays. |
| V3-31 | Fixed. Agreement on \(\sqrt[3]{2}\) and on \(\omega\) is the injection into \(\mathfrak S_3\), and both sets have six elements. |
| V3-32 | Fixed. The two sentences are the ones the log asked for. |
| V3-33 | Fixed. \(X\cdot(nX^{n-1})-n(X^n-1)=n\), so a common divisor divides the nonzero constant \(n\), and the gcd is 1. |
| V3-34 | Fixed. The state at time 1 modulo 11 is \((1,1)\), and the proper divisors 1, 2, and 5 are all named. |
| V3-35 | Fixed. \(r_1^2+r_2^2+r_3^2=(\sum r_i)^2-2p\) is written, the quadratic formula is expanded, and dividing by 27 uses \(\frac12\sqrt A=\sqrt{A/4}\). Both end formulas match. |
| V3-36 | Fixed. A term of degree \(k<d\) meets degrees \(d-k\) through \(d+k\), so only the leading term meets the constant term, with coefficient 1. |
| V3-37 | Fixed. A Euclidean isometry is defined by distances, and \(|g(x)|=|x|\) and \(|g(x)-g(y)|=|x-y|\) are written before the polarization identity. |
| V3-38 | Fixed. Left cancellation expands \((a^{-1}a)b=b\). |
| V3-39 | Fixed. \(sr^k=r^{-k}s\) is proved by induction and then multiplied. |
| V3-40 | Fixed. An element that commutes with both generators is shown to commute with every word, by appending one generator at a time. |
| V3-41 | Fixed. The exercise names \(F_0=0\), \(F_1=1\), and the recurrence. |
| V3-42 | Fixed. The hint separates the fresh block of increments from the symmetry \(X_t^{-1}\). |
| V3-43 | Fixed. \(HN=\{hn:h\in H,\,n\in N\}\). |
| V3-44 | Fixed. Conjugation is named as an automorphism, so it sends a word to the word in the conjugates. |
| V3-45 | Fixed. The additive rule is \(k+(-1)^\varepsilon k'\). |
| V3-46 | Fixed. The class equation uses \(C_G(x)\), the same symbol as the solution. |
| V3-47 | Fixed. If the centre had order \(p\), the quotient would be cyclic and the displayed multiplication would make the group abelian. |
| V3-48 | Fixed. Independence uses the extended basis: a relation in \(U\) is a linear dependence of that basis, so every coefficient of a \(v_i\) vanishes. |

No numbered statement was rewritten. Proof hashes in `review/volume3-internal/proofs.json` change only for the dihedral proof, whose text gained the distance hypothesis, and the other changed `related` ids are the same proof bytes with a shifted proof index after that insertion. Exercise claim fields are unchanged.

## Findings

### F-1. The circulant solution attributes the derivative to the comparison proposition

**Severity:** minor.

**Location:** `volume3-symmetry/chapters/ch11-characters.tex:1187`.

**What is wrong.** The sentence says that the proposition comparing sine and tangent with the identity proves \(\sin'=\cos\) and \(\cos'=-\sin\). In Volume 1 that proposition is `prop:sincmp`. Its proof opens from the standing fact \(\sin'=\cos\) and deduces \(0<\sin x<x<\tan x\). The preface, and the sequences chapter once the word derivative has a meaning, name \(\sin'=\cos\) and \(\cos'=-\sin\) as facts the book does not prove. The second half of the Volume 3 sentence is right: the inequality is a consequence of the derivative. The first half points the reader at the proposition that uses the derivative.

**Fix.** Quote the preface's standing facts, or the sequences chapter's restatement of them. Leave the comparison proposition as the source of \(\sin h<h<\tan h\) only.

### F-2. The index opener talks about the two PDFs

**Severity:** minor.

**Location:** `volume3-symmetry/chapters/index.tex:4` and `:106`.

**What is wrong.** The opener says "The numbers are the printed ones. In the reading and print PDFs, a page number follows the statement." A reader of the book does not need that production sentence. The later line "The exercises below are the ones a later volume cites by number" is an editorial note about the series, not a direction to a statement.

**Fix.** Open with one sentence: each name points at the statement, exercise, or definition it names. The page number can stay, since `\ocindexpage` prints it. Drop the sentence about later volumes, or replace it with a plain heading for those three exercises.

### F-3. Odd index pages keep the previous running head

**Severity:** minor.

**Location:** `volume3-symmetry/chapters/index.tex:1`, visible on interior folio 511.

**What is wrong.** `\chapter*` does not call `\chaptermark`. Appendix D's numberless section "Sources and further reading" sets `\rightmark` through the numberless-section format in `common/interior-style.tex`. Folio 511, a recto of the index, is headed SOURCES AND FURTHER READING. Even pages correctly show the volume name.

**Fix.** After `\chapter*{Index}`, set both marks to Index.

### F-4. The dimension sentence over \(R/(p)\) precedes the vector-space structure

**Severity:** minor.

**Location:** `volume3-symmetry/chapters/ch07-modules.tex:374`.

**What is wrong.** "Its dimension is the one from the exchange lemma of Chapter 1" stands before the scalar multiplication is defined, and it does not say which number the dimension is. The next sentences define the scalar multiplication and then say the dimension is an invariant. The lemma does make dimension well-defined over every field. The sentence as placed does not yet have a vector space to measure.

**Fix.** After the vector-space laws, say that the exchange lemma of Chapter 1 makes the dimension well-defined over the field \(R/(p)\).

### F-5. Volume 9 still sends the matrix exponential to Chapter 3

**Severity:** minor.

**Location:** `volume9-shapes/chapters/ch02-flows.tex:504`.

**What is wrong.** The solution of the linear-fields exercise says the flow is \(e^{tA}x\) "by uniqueness" and adds "(Volume 3, Chapter 3, for the exponential)." Volume 3, Chapter 3 is group actions, orbits, and Burnside's lemma. A search of `volume3-symmetry` finds no matrix exponential \(e^{tA}\). The real exponential appears as a group homomorphism in Chapter 2, and the series for the natural exponential is built in the circulant solution of Chapter 11. The parenthetical does not name either of those, and neither is the linear flow.

**Fix.** Drop the chapter pointer, or point at the place that actually defines this exponential. The derivative check already written in the sentence can stand on its own.

### F-6. Two accepted register rows describe text that is not on the page

**Severity:** minor.

**Location:** `review/volume3-internal/exposition.json`, ids `1.prose.e5c1e3ea7ca081bb.1` and `main.prose.dae952bccbf9d233.1`.

**What is wrong.** `registers.py` exits 0, and the counts 1177 and 19 match the pull request. Fifteen new exposition rows were then marked `accepted-internal` by hand. Two of those claims do not match the source the hash certifies. The reflection row's claim still quotes \((sr^k)^2=sr^ksr^k=r^{-k}r^k=e\), which is the sentence V3-39 replaced; the page now has the induction. The `main.tex` row's claim lists the inputs through the afterword and About the Cover and omits `\input{chapters/index}`, which is in the file. The script checks the hash and that the review fields are non-empty. It does not check that the claim is the text on the page.

**Fix.** Rewrite those two claims to the text that is there, including the induction and the index input, or return the rows to `pending`.

### F-7. The homomorphism into \(\mathfrak S_4\) is called nontrivial without the reason

**Severity:** minor.

**Location:** `volume3-symmetry/chapters/ch05-sylow.tex:586`.

**What is wrong.** For orders 12, 24, and 36 with \(n_3=4\), the text says the conjugation action is nontrivial, and therefore the kernel is proper. Sylow II, already proved, says the four subgroups are conjugate, so some element moves one of them. If the action were trivial, each Sylow subgroup would be normal, hence unique. The previous draft said the action was transitive. That word was dropped, and nothing replaced the reason.

**Fix.** One clause: the four Sylow subgroups are conjugate, so the action is nontrivial.

## Pull-request table and KDP section

The table's forty-eight rows name the right files and the right mathematical change. V3-18's status "fixed" does not hold, for F-1. The other forty-seven statuses hold, with F-4 and F-7 as remaining sentences inside V3-27 and V3-19.

The KDP section is right that Volumes 9, 10, 13, 14, and 15 are not renumbered, that a reflow can still move a later page, that Volume 3's page count changes, that KDP upload stays with the author, and that the order-6 label is the text \(D_3\cong\mathfrak S_3\) at the existing script size. The phrase "they rename a theorem or an exercise" is short of the Volume 9 paragraph, which replaces the false appeal to Volume 3 with two sentences about \(e^{L(u)}\), and short of the extra Proposition 10.9 sentences in Volume 13. Those sentences do not renumber anything. This build measures the Volume 3 print interior at 523 pages, six more than the 517-page print interior in the source log. The reading PDF is 524 pages. No caption font, figure palette, or diagram metric was changed. The figure on folio 128 was looked at.

## Unresolved doubts

The exchange lemma says that the family obtained by adding vectors outside the current span "stays independent," without the one-line check that a vector outside the span of an independent set keeps the set independent. The rest of the Steinitz argument is written, and the subspace theorem follows from the size bound. I do not treat that compression as a false step.

The exponential of \(L(u)\) in Volume 9 is one sentence from the eigenvalues \(0,\pm i|u|\). It is no longer attributed to Volume 3. A displayed \(2\times2\) exponential is not there. Surjectivity onto \(SO(3)\) still follows, because both orientations occur as \(u\) runs through \(\mathbb R^3\).

Paley's 1932 item is printed as one article on pages 241–279. The London Mathematical Society issued it as (I) 241–264 and (II) 265–279. The range is the union, and part II is the Walsh–Kaczmarz half the annotation describes.

The Cohen–Lenstra reminder cites Theorem 7.6 for the partition form of a finite abelian \(p\)-group. Theorem 7.6 states invariant factors. For a \(p\)-group those factors are the prime powers in the partition, and Corollary 7.7 writes the prime-power form. I do not require a renumbering.
