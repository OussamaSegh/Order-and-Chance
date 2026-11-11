# Volume 3 independent scored read

**Book.** *Order and Chance*, Volume 3: *Symmetry*. Subtitle: *Groups, Rings and Fields*.
**Author.** SEGHAIER Oussama. First edition, 2026. Paperback ISBN 9798167514683.
**Source.** `main` at `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f` (equal to `origin/main` on 11 November 2026).
**Artifacts.** GitHub release `books` (published 2026-11-11): reading PDF `Volume.3.-.Symmetry.pdf` (518 pages, PDF 1.5, page labels Cover, i–x, 1–507), print PDF `Volume.3.-.Symmetry.-.Print.pdf` (517 pages, 513×738 pt, PDF 1.3, metadata stripped), EPUB `Volume.3.-.Symmetry.epub` (24 MB compressed).
**Reader.** A motivated reader who has Volumes 1 and 2. The series contract treats Volume 1 as high-school mathematics with proofs, and Volume 2 as depending only on Volume 1. This volume is a full algebra course on that base.
**Calibration.** 10 is reserved for work with no defect I could find at the level of Artin, *Algebra*, Dummit–Foote, or Spivak’s care with hypotheses. A numerical check is recorded separately from a proof check.

This report was written before any file under `review/`, `docs/review/`, `docs/handoffs/`, or `docs/plan/` whose path mentions Volume 3 was opened, and before any earlier Volume 3 pull-request discussion was read. The comparison with those documents is a later commit.

Printed folios below are the reading PDF’s page labels. Reading PDF page \(N\) is print PDF page \(N-1\). Arabic folio \(n\) is reading page \(n+11\).

## How the scores were reached

Every exercise, hint and solution label in the sixteen chapter files was matched by a script: 163 exercises, 163 hints, 163 solutions, same order in each file. Theorem numbers below were taken from the reading PDF, not from a hand count.

Line-by-line reading, with recomputation where a number appears, covered: the preface, blurb, About the Cover, and afterword; all of Chapter 1, including every solution; the quotient and isomorphism theorems in Chapter 2; Burnside’s lemma, the six-bead count, and Pólya’s statement in Chapter 3; the fifteen-puzzle theorem and the simplicity proof for \(A_5\) in Chapter 4; the three Sylow theorems and the subgroup-of-order-\(p^k\) corollary in Chapter 5; Gauss’s lemma, the primitive-polynomial proposition, and the polynomial UFD theorem in Chapter 6; the Smith normal form statement in Chapter 7; the irreducible-polynomial count in Chapter 9; the fundamental theorem, the cyclotomic injection, and the proof that the Galois group of \(X^5-4X+2\) is \(S_5\) in Chapter 10; Maschke, Schur, and the character tables of \(S_3\), \(S_4\) and \(A_5\) in Chapter 11; Euler’s axis lemma, the Hurwitz four-square solution, and the Egyptian-fraction check \(4/13=1/4+1/18+1/468\) in Chapter 12; Wielandt’s exponent bound and the PageRank example in Appendix A; the cap-set theorem and the constant \(2.7552\) in Appendix C; the Paley congruences in Appendix D.

Proofs not read line by line are listed under **Not reviewed**. They were not treated as certified.

## 1. Chapter and appendix scores

Rows are chapters. Columns are (a) correctness, (b) rigor, (c) prerequisites, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography. Scores for (b) and (f) fall where the proofs or solutions were only sampled.

|  | a | b | c | d | e | f | g | h | i | j |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 Groups as Symmetries | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 2 Morphisms and Quotients | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 3 Actions and Counting | 8 | 8 | 8 | 8 | 9 | 7 | 8 | 8 | 8 | 8 |
| 4 The Symmetric Group | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 5 Sylow | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 6 Rings and Ideals | 8 | 8 | 7 | 7 | 7 | 7 | 7 | 8 | 8 | 8 |
| 7 Modules over a PID | 8 | 7 | 7 | 7 | 7 | 6 | 7 | 7 | 8 | 8 |
| 8 Field Extensions | 7 | 7 | 7 | 7 | 7 | 6 | 7 | 7 | 8 | 8 |
| 9 Finite Fields | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 8 | 8 | 8 |
| 10 Galois Theory | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| 11 Representations | 8 | 8 | 7 | 8 | 8 | 7 | 9 | 8 | 8 | 8 |
| 12 Quaternions | 8 | 7 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 |
| A Positive Matrices | 8 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | 8 | 8 |
| B Symmetry Diagonalises | 7 | 6 | 6 | 7 | 7 | 6 | 7 | 7 | 7 | 8 |
| C The Linear Algebra Method | 8 | 8 | 7 | 7 | 8 | 7 | 8 | 7 | 8 | 8 |
| D Hadamard matrices | 8 | 7 | 7 | 7 | 7 | 6 | 7 | 7 | 8 | 8 |

**Chapter 1.** The group axioms, Lagrange, cyclic groups, and the classification of groups of order 4 are proved with the usual edge cases (empty word, \(k=0\), modulus 1). The dihedral relation \(srs=r^{-1}\) and the cube count \(9+8+6+1=24\) match the multiplication table on folio 8. All thirteen solutions were read. Ruzsa’s injection, the Fibonacci entry point via \(\gcd(F_a,F_b)=F_{\gcd(a,b)}\) (Volume 1, Exercise on Fibonacci gcd), and the symmetric-walk identity \(p_{2t}(e)=\sum_g p_t(g)^2\) are correct as written. The random-matrix counts over \(\mathbb F_p\) sum to \(p^4\) for \(p=2,3,5,7,11\). The field is defined in the middle of the first chapter and the cube argument uses orthogonal matrices; that is a steep opening, which keeps clarity and pedagogy at 8 rather than 9. The sources list a paper on the diameter of the Rubik’s cube group that the chapter never uses.

**Chapter 2.** The quotient product is shown independent of representatives, and the converse (a well-defined product forces normality) is included. Index 2 is handled by comparing the two left cosets with the two right cosets. The first isomorphism theorem includes the finite count \(|G|=|\ker|\,|\operatorname{im}|\), and the \(GL_0\) exception is stated. Exercises were label-matched, not recomputed, so (f) stays at 7. The lattice figure was not redrawn.

**Chapter 3.** Burnside’s double count is correct, and the six-bead average \((64+2+4+8+4+2)/6=14\) matches the cycle index of the rotation group. The caption check \(2\cdot 1+1\cdot 2+2\cdot 3+9\cdot 6=64\) is arithmeticly right. Pólya’s weighted form is the standard cycle index. Pedagogy is the strongest in the book: the failed division \(64/6\) is the reason for the average. Later solutions in the chapter were not recomputed.

**Chapter 4.** \(A_4\) has no subgroup of order 6, by a 3-cycle count. The fifteen-puzzle invariant \(\varepsilon(\sigma)\delta(\sigma)\) is the standard one: each move is a transposition and changes the colour of the blank. The base \(2\times 2\) loop on cells 11, 12, 15 was simulated; the tile cycle is \(15\to 12\to 11\to 15\), as written, and it generates \(A_3\). The class-size proof that \(A_5\) is simple was recomputed: the identity-containing class unions have orders \(1,13,16,21,25,28,33,36,40,45,48,60\), and only 1 and 60 divide 60. The sign of a 5-cycle is \((-1)^4\). The figure of the puzzle was not inspected cell by cell.

**Chapter 5.** Sylow I is Wielandt’s subset argument. The binomial congruence \(\binom{p^a m}{p^a}\equiv m\pmod p\) is proved in characteristic \(p\), and the check \(\binom{6}{2}=15\equiv 3\pmod 2\) is right. Sylow II–III, including \(n_p\equiv 1\pmod p\), follow the usual normaliser argument. The case \(a=0\) of the freshman’s-dream induction is not written out; it is the trivial subgroup and is not used when \(p\) divides \(|G|\). Solutions were not recomputed.

**Chapter 6.** Gauss’s content lemma, the descent of divisibility from \(K[X]\) to \(R[X]\), and “\(R\) a UFD implies \(R[X]\) a UFD” are in the right logical order. The example \(\mathbb Z[(1+\sqrt{-19})/2]\), with minimal polynomial \(X^2-X+5\), really has no root modulo 2 or 3, so the Euclidean-function argument is not vacuous. The zero ring is allowed and excluded from the domains. Prerequisite load is real: the reader is handed fraction fields and contents immediately after ideals. Later volumes cite these three results under the wrong numbers (issue V3-2).

**Chapter 7.** The Smith theorem states the divisibility chain, the minor gcds, the empty-matrix conventions, and that the determinant formula used is the one from Volume 1. The structure theorem for finitely generated modules is Theorem 7.6 and the classification of finitely generated abelian groups is Corollary 7.7, which is what the later volumes that cite those numbers need. The proof of uniqueness of the invariant factors was not reread, so rigor stays at 7. Solutions were not recomputed.

**Chapter 8.** The tower law, splitting fields, and ruler-and-compass are the right bridge, and Rolle’s theorem for the quintic is available as Volume 1, Theorem on Rolle and the mean value theorem. The degree arguments and the impossibility proofs were not reread line by line, so correctness and rigor are capped at 7. This is the chapter whose proofs are least covered by the present read.

**Chapter 9.** Theorem 9.10 is the standard count \(\sum_{d\mid n} d N_q(d)=q^n\) and \(N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}\). The error \(|N_q(n)-q^n/n|<2q^{n/2}/n\) was rechecked: the tail is at most the geometric sum up to \(\lfloor n/2\rfloor\), which is strictly less than \(\frac{q}{q-1}q^{n/2}\le 2q^{n/2}\). The quadratic count \((q^2-q)/2\) matches, and the three listed irreducibles over \(\mathbb F_3\) have no root. Reed–Solomon was not reread.

**Chapter 10.** The fundamental theorem’s three parts match the form later volumes use. For \(X^5-4X+2\), Eisenstein at 2 applies (the constant term is 2, not divisible by 4), the sign changes give roots in \((-2,0)\), \((0,1)\) and \((1,2)\), and \(f'\) has two real zeros, so Rolle forbids a fourth real root. A common root of \(f\) and \(f'\) would be \(5/8\), and \((5/8)^4\neq 4/5\). The 5-cycle-and-transposition generation of \(S_5\) is written with the relabeling, and one root in a radical extension is correctly shown to drag in the whole splitting field. Exercise 10.1, not Exercise 10.8, is the cyclotomic isomorphism. The Galois lattice for \(X^4-2\) is described as \(D_4\) of order 8, consistent with the book’s \(D_n\) of order \(2n\).

**Chapter 11.** Maschke’s average and the characteristic-\(p\) counter-example \(T(a,b)=(a+b,b)\) are correct. Schur’s lemma records that an eigenvalue is used, so the scalar conclusion needs \(\mathbb C\). The printed tables match the classical ones: \(S_4\) classes \(1,6,3,8,6\); \(A_5\) classes \(1,15,20,12,12\); the golden ratio is defined in the caption as \((1+\sqrt 5)/2\); the five \(A_5\) degrees square-sum to 60. Theorem 11.14’s third formula is the stated orthogonality \(\frac1{|A|}\sum_\chi\chi(a)=0\) for \(a\neq 0\). Exercise 11.8(c) really is “the degree divides \(|G|\)”. Hermitian form is linear in the first slot, and the text says so.

**Chapter 12.** Euler’s lemma proves an axis by \(\det(A-I)=-\det(A-I)\) in dimension 3. It does not mention \(\mathfrak{so}(3)\) or the matrix exponential; Volume 9 cites it as if it did (issue V3-4). The Hurwitz proof that every positive integer is a sum of four squares was read: the ideal argument, the exclusion of norms \(1\) and \(p^2\), and the passage from odd half-integers to \(\mathcal H\) by a unit of norm 1 are the standard ones, and \(1+x^2+y^2\equiv 0\pmod p\) is in Volume 2, Chapter 7. The identity \(4/13=1/4+1/18+1/468\) was recomputed. The classification of finite subgroups of \(SO(3)\) was not reread past the vertex counts.

**Appendix A.** Wielandt’s bound \(A^{(n-1)^2+1}>0\) is the classical \(n^2-2n+2\), and the exponent arithmetic \(n+s(n-2)\le (n-1)^2+1\) checks. The historical note matches Holladay–Varga, *Proc. Amer. Math. Soc.* 9 (1958), and Schneider’s publication of the diary proof, *Linear Algebra Appl.* 353 (2002). The eight-page PageRank vector at \(\alpha=0.85\) was recomputed from the drawn digraph: \(A=0.3295\), \(B=0.1689\), \(C=0.3511\), and the smaller nodes fall in \((0.018,0.041)\), matching the caption to three decimals. A later pass read the exercises. Two solutions name Perron’s theorem where the hypothesis is only irreducibility, so Frobenius is the theorem that applies (issues V3-9 and V3-10). The conclusions of those solutions are still right. The Leslie solution’s “block lower triangular” is the correct shape: if \(f_m\) is the last positive fertility, the upper-right block is zero and \(s_m\) sits in the lower-left block.

**Appendix B.** The stated circulant eigenvalues and the Paley eigenvalues \(\frac{p-1}{2}\) and \(\frac{-1\pm\sqrt p}{2}\) for \(p\equiv 1\pmod 4\) are the classical ones. The proofs, the Krawtchouk identities, and the Delsarte linear program were not read line by line. Rigor is 6 for that reason: this is not a certificate that every inequality in the appendix is complete. The About the Cover graph is the Paley graph of order 13, and its parameters \((13,6,2,3)\) are right: the quadratic residues modulo 13 are \(1,3,4,9,10,12\).

**Appendix C.** Oddtown, the combinatorial nullstellensatz, and Cauchy–Davenport are stated in that order. Cauchy–Davenport is **Theorem C.12**, not C.11. The cap-set argument is Tao’s slice-rank form of Ellenberg–Gijswijt. The constant was checked in integers: with \(x=59/100\),
\[
19381^3\cdot 625 < 1722^3\cdot 256\cdot 3481,
\]
so \((1+x+x^2)/x^{2/3}<1722/625=2.7552\). The critical point of \((1+x+x^2)^3/x^2\) is \((\sqrt{33}-1)/8\), and the minimal base is about \(2.755105\). The \(\mathbb F_3^2\) count of 12 lines is \((9\cdot 8)/(3\cdot 2)\).

**Appendix D.** Paley I (order \(q+1\) for \(q\equiv 3\pmod 4\)) and Paley II (order \(2(q+1)\) for \(q\equiv 1\pmod 4\)) are the right constructions, and both orders are divisible by 4. The Hadamard footnote matches arXiv:2610.27175 (Egan, Kotsireas, London, Ó Catháin, 19 October 2026): the twelve orders below 2000 that were open, including 668, and the claim that those verifications cover every positive multiple of 4 below 2000. The proofs of the two constructions were sampled, not reread from the first character sum.

## 2. Whole-book scores

| Item | Score |
|---|---:|
| Structure and arc | 8 |
| Continuity with Volumes 1 and 2 | 8 |
| Preparation for later volumes | 6 |
| Delivery of the title and subtitle | 9 |
| Front matter, back matter, index, bibliography | 6 |
| Print PDF | 8 |
| EPUB | 8 |
| **Overall** | **8** |

**Structure.** Three parts (Groups; Rings and Polynomials; Fields and Galois Theory), then characters and quaternions, then four appendices the preface places on the main route: A after Chapter 7, B after Chapter 11, C and D after Chapter 9. The printed appendix letters match that preface. The afterword computes the walk on \(\mathbb Z/2\mathbb Z\) and names Volume 4, *Chance: The Logic of Uncertainty*. The appendices are long enough to feel like a second book, which is why the arc is 8 and not 9.

**Continuity.** Back-references that were opened do say what is claimed: Volume 1 has Rolle, the intermediate-value theorem, and \(\gcd(F_m,F_n)=F_{\gcd(m,n)}\); Volume 2, Chapter 7 contains \(x^2+y^2+1\equiv 0\pmod p\); Euler’s theorem is recovered as Lagrange in the unit group. The field language in Chapter 1 assumes the determinant theory of Volume 1 can be read over any field. The text argues that the permutation formula uses only ring operations. That argument was not matched sentence by sentence against Volume 1.

**Preparation for later volumes.** The results later volumes need are in the book: Smith form (Theorem 7.4), the structure theorem (Theorem 7.6), Corollary 7.7, finite fields (Theorems 9.4 and 9.6), the irreducible count (Theorem 9.10), the fundamental theorem (Theorem 10.6), Fourier analysis (Theorem 11.14 and Section 11.4), and Cauchy–Davenport. Several of the pointers, however, name the wrong number. A reader who follows them lands on a different theorem. That is a failure of preparation even though the mathematics is present. Score 6.

**Title and subtitle.** *Symmetry* is carried by the cube, the dihedral groups, necklaces, the fifteen-puzzle, Galois actions, characters, and rotations. *Groups, Rings and Fields* is what the three parts are. The quintic \(X^5-4X+2\) and the identity \(24=1^2+1^2+2^2+3^2+3^2\) are proved, not only advertised. The blurb names those objects and does not use the banned intensifiers.

**Front and back matter.** The preface is a real map: it names the quintic, the character identity, and which appendix depends on which chapter. There is no index in a book of 507 folios. Bibliography is a “Sources and further reading” list at the end of each main chapter and of Appendices A–C. Appendix D has a footnote instead of a list. The lists that were checked against publication data (Artin and Dummit–Foote as general algebra sources, Wielandt 1950, Holladay–Varga 1958, Schneider 2002, Ellenberg–Gijswijt, the 2026 Hadamard report) are real. One Chapter 1 item does not belong to the chapter.

**Print PDF.** Every page is \(513\times 738\) pt. Text lies inside the trim (recto trim \([0,504]\times[9,729]\), verso trim \([9,513]\times[9,729]\) in PDF points, \(y\) downward): a scan of all 517 pages found no word outside that trim. The part opener (print page 11) is charcoal to the media edge, including the four corners. Fonts embedded are EB Garamond, Garamond-Math, Fira Sans, Cormorant Garamond, and DejaVu Sans Mono. Bookmarks and document metadata are absent, as the KDP export requires. The spine in the metadata uses the even round-up of 517, which is 518, times \(0.002347\). Sampled pages (front matter, Chapter 1, the \(D_4\) table, a part page) show the design-5e boxes, running heads, and a readable figure. Not every folio was looked at as a picture.

**EPUB.** Compressed size 24 MB, under the 50 MB cap. Twenty-three non-formula PNGs, all at least 1600 pixels wide (the plates are about 1800). Figure images carry `width:100%; max-width:100%; height:auto`. Inline formulas are transparent PNGs with width and `vertical-align` in em. The stylesheet is the design-5e palette. The file was not read on a Kindle Paperwhite.

## 3. Overall

**Overall score: 8.**

**Verdict.** This is a careful algebra book. The theorems that were read are stated with their hypotheses, the edge cases that usually get dropped are often written in, and the solutions that were read teach the step rather than only certify it. The character tables, the cap-set constant, the PageRank vector, the \(A_5\) class arithmetic, and the quintic root count all survived recomputation. I would recommend the volume, as it stands, to a reader who has finished Volumes 1 and 2 and wants groups through Galois theory with full proofs.

I would not treat the later volumes’ numerical pointers into this book as safe. Exercise 10.8, Theorems 6.16–6.18, Theorem C.12, and the appeal to a spectral theorem in “Volume 3, Chapter 2” are the repairs that matter. An index is the other gap a 500-page book should not have. Those are not reasons to withhold the volume from a reader; they are reasons not to call the series cross-references finished.

## 4. Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
|---|---|---|---|---|---|
| V3-1 | `volume15-order-and-chance/chapters/conjectures-ch12-algebra.tex:59` and `:478`; `volume13-arithmetic/chapters/ch05-cyclotomic.tex:36`; `volume13-arithmetic/chapters/ch04-units.tex:291`; `volume13-arithmetic/chapters/ch02-ideals.tex:40`. Printed Exercise 10.8 is reading-PDF folio 292 | Prerequisite / citation | major | Those passages say Exercise 10.8 is \(\operatorname{Gal}(\mathbb Q(\zeta_n)/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^*\) and \([\mathbb Q(\zeta_m):\mathbb Q]=\varphi(m)\). Printed Exercise 10.8 is Cardano’s formula for \(X^3+pX+q\). The cyclotomic isomorphism is Exercise 10.1 (`ch10-galois.tex:419`, label `ex:phin`), including \(\Phi_n\in\mathbb Z[X]\) and the isomorphism. Proposition 10.9 (`ch10-galois.tex:360`) gives only an injection into \((\mathbb Z/n\mathbb Z)^*\), and an isomorphism when \(n\) is prime. | Point the later volumes at Exercise 10.1 for the general cyclotomic isomorphism, and at Proposition 10.9 only for the injection and the prime case. |
| V3-2 | `volume13-arithmetic/chapters/ch11-curves.tex:32–34`. Printed Lemma 6.16, Proposition 6.17, Theorem 6.18 are folio 169–170 | Prerequisite / citation | major | The reminder says \(k[x_1,\ldots,x_n]\) is a UFD by Theorem 6.17, and that a primitive polynomial dividing in \(K[y]\) divides in \(R[y]\) by Proposition 6.16. In the print, Lemma 6.16 is the content formula \(c(fg)=c(f)c(g)\). Proposition 6.17 is irreducibility over \(R\) versus \(K\) and the divisibility descent. Theorem 6.18 is “\(R\) a UFD implies \(R[X]\) a UFD”, which is the result that iterates to \(K[X_1,\ldots,X_n]\). | Cite Proposition 6.17 for the descent and Theorem 6.18 for the polynomial UFD. |
| V3-3 | `volume14-primes/chapters/ch11-additive.tex:16`. Printed Theorem C.12 is reading page 485 (folio 474) | Prerequisite / citation | major | The reminder states Cauchy–Davenport as Theorem C.11. Theorem C.11 is the combinatorial nullstellensatz. Cauchy–Davenport, \(|A+B|\ge\min(p,|A|+|B|-1)\), is Theorem C.12 (`combinatorial.tex`, label `combinatorial:thm:cd`). | Change the pointer to Theorem C.12. |
| V3-4 | `volume9-shapes/chapters/ch07-liegroups.tex:151`; `volume9-shapes/chapters/geometry-ch06-quadrics.tex:70` and `:425` | Prerequisite / citation | major | Lemma 12.3 (`ch12-quaternions.tex:208`) says every matrix in \(SO(3)\) is rotation by some angle about some axis. It does not mention \(\mathfrak{so}(3)\) or \(\exp\). A search of `volume3-symmetry` finds no skew-symmetric exponential and no \(\mathfrak{so}(3)\). Volume 9 says the exponential of \(L(u)\) is that rotation “as in Volume 3”, and that surjectivity of \(\exp\) is Euler’s lemma. Separately, “the spectral theorem of Volume 3” and “the square of the volume (Volume 3, Chapter 2)” do not match this book: Chapter 2 is quotients and the isomorphism theorems, and no spectral theorem for symmetric matrices is numbered in it. | Cite Lemma 12.3 only for the axis-angle statement. Move the exponential identification and the spectral theorem to the volume that proves them. Cite Chapter 2 only for quotients and the Chinese remainder theorem. |
| V3-5 | Whole book; contents end at “About the Cover”, reading page 518 | Back matter | major | There is no index. Folio count of the main matter is 507. Sources are split across chapter-end lists, so a name such as Wielandt or Gauss has no single place to look. | Add an index of names and of the notation \(D_n\), \(N_q(n)\), \(\varphi\), slice rank. |
| V3-6 | `ch01-groups.tex:1381` | Bibliography | minor | The sources list Rokicki, Kociemba, Davidson and Dethridge, *SIAM J. Discrete Math.* 27 (2013), on the diameter of the Rubik’s cube group. Chapter 1 does not discuss the cube puzzle or that diameter. The bibliographic facts I checked for that paper are the usual ones; the item is simply in the wrong chapter. | Move the item to a chapter that uses it, or delete it. |
| V3-7 | `paley.tex:17–24`; no `\section*{Sources}` | Bibliography | minor | Appendix D’s only source is the footnote to arXiv:2610.27175v1. Paley’s two papers and the Hadamard conjecture’s classical references are not listed. The footnote’s mathematical claim agrees with the arXiv abstract of 19 October 2026. | Give Appendix D the same sources list the other appendices have. |
| V3-8 | `ch05-sylow.tex:47–60` | Rigor | minor | Lemma 5.2 states the binomial congruence for \(a\ge 0\). The written induction starts from \((1+X)^p\equiv 1+X^p\) and raises the exponent, which covers \(a\ge 1\). The case \(a=0\) is \(\binom{m}{1}=m\), true and unused when one only wants a nontrivial Sylow subgroup. | Add the one-line case \(a=0\). |
| V3-9 | `linear-ch07-perron.tex:1066`, solution of the row-sum exercise; printed Theorem A.1 is Perron for \(A>0\), Theorem A.6 is Frobenius | Exercise | minor | The exercise is for irreducible \(A\ge 0\). The converse says that if every row sum equals \(c\), then Perron’s theorem gives \(c=\rho\) because \(\mathbf 1>0\). Theorem A.1 assumes every entry is positive. A cycle adjacency matrix is irreducible, has equal row sums, and has zeros. Frobenius (Theorem A.6) is what puts every nonnegative eigenvector on \(\rho\). The same chapter’s Markov paragraph cites Frobenius for this. The equality \(c=\rho\) is true. | Cite Frobenius in the converse. |
| V3-10 | `linear-ch07-perron.tex:1142`, solution of the monotone-radius exercise | Exercise | minor | Equality produces \(B|y|=\rho(B)|y|\) with \(B\) only assumed irreducible and nonnegative. The solution then says Perron’s theorem makes this eigenvector strictly positive. Strict positivity of a nonnegative eigenvector, under irreducibility alone, is Frobenius. The rest of the argument, that a positive weight on \(B-A\) forces \(A=B\), is correct once \(|y|>0\). | Name Frobenius there. |

No false theorem was found in the proofs that were read line by line. The major rows are wrong pointers from later volumes, plus the missing index. The two new minor rows are misnamed theorems inside solutions whose conclusions stand.

## 5. Verified correct

These were checked in the source and, where a number appears, recomputed. A numerical check is not a proof; the proofs named here were also read.

- Group axioms through Lagrange and cyclic groups (Theorems 1.10 and 1.13). Orders in \(D_n\): centre \(\{e\}\) for \(n\) odd and \(\{e,r^{n/2}\}\) for \(n\) even.
- Cube rotations: 24 signed permutation matrices of determinant 1, and the geometric split \(9+8+6\). The \(D_4\) table on folio 8 agrees with \(sr^k=r^{-k}s\).
- \(|GL_2(\mathbb F_p)|=(p^2-1)(p^2-p)\) and \(|SL_2(\mathbb F_p)|=p(p^2-1)\). The two matrices over \(\mathbb F_2\) in the solution do not commute.
- Wilson’s theorem from the pairing in an abelian group, including \(p=2\).
- Every finite subgroup of \(K^*\) is cyclic (the argument in the solution of Exercise 1.9, repeated as Theorem 9.4).
- Random \(2\times 2\) matrices over \(\mathbb F_p\): the four disjoint counts sum to \(p^4\). Limits \(1/2\) and \(1/2\).
- Fibonacci: every \(m\ge 1\) divides some \(F_n\) with \(n\ge 1\), and the set of such \(n\) is the multiples of the entry point, using \(\gcd(F_a,F_b)=F_{\gcd}\). The companion sequence \(J_{n+2}=J_{n+1}+2J_n\) is odd for \(n\ge 1\), and its state map is not bijective modulo 2.
- Ruzsa’s inequality and the covering lemma, including the empty-set cases written in the solution.
- Quotients, the first isomorphism theorem, and \(|A_n|=n!/2\).
- Burnside for 6 beads and 2 colours: 14 necklaces.
- No subgroup of order 6 in \(A_4\). The fifteen-puzzle invariant, the solved position, and the transposition of 14 and 15. The base rectangle cycle, by direct sliding.
- \(A_5\) class sizes \(1,15,20,12,12\) and the divisibility exclusion.
- Sylow I–III and “\(p^k\) divides \(|G|\) implies a subgroup of order \(p^k\)”, including the appeal to a nontrivial centre.
- No simple group of order 30, by the count \(24+20>30\).
- Gauss content, primitive descent, and \(R[X]\) a UFD when \(R\) is. The ring \(\mathbb Z[(1+\sqrt{-19})/2]\) is not Euclidean by the modulo 2 and 3 calculation.
- Smith normal form as stated (existence proof not fully reread). Corollary 7.7 is the classification of finitely generated abelian groups.
- Theorem 9.10, the quadratic count, and the three cubics over \(\mathbb F_3\).
- Galois correspondence as stated in Theorem 10.6. Galois group of \(X^5-4X+2\) is \(S_5\), so that polynomial is not solvable by radicals, and neither is a general quintic formula.
- Character tables of \(S_3\), \(S_4\) and \(A_5\) in `figures/ch11-tables.tex`, including class sizes. Theorem 11.14’s evaluation of \(\sum_\chi\chi(a)\).
- Euler axis lemma. Four-square theorem via the Hurwitz order. \(4/13=1/4+1/18+1/468\).
- Wielandt exponent \((n-1)^2+1\). PageRank numbers for the eight-page graph.
- Cap-set bound \(|A|\le 3M_n\) and \(M_n\le 2.7552^n\). Paley graph of order 13: degree 6, 39 edges, parameters \((13,6,2,3)\).
- About the Cover, the afterword’s two-state walk \(u_t=(1+(1-2p)^t)/2\), and its eigenvalues \(1\) and \(1-2p\).
- Print geometry, embedded fonts, part-page bleed, EPUB plate widths and the em baseline on inline mathematics.
- Exercise/hint/solution labels: 163, 163, 163, in the same order in every chapter file.

Sources actually consulted for the external claims: the reading and print PDFs; Volume 1 Chapters 1 and 5 and the preface (Fibonacci gcd, Rolle, intermediate values); Volume 2 Chapter 7 (the congruence \(x^2+y^2\equiv -1\pmod p\)); arXiv:2610.27175 (Hadamard orders below 2000); Holladay and Varga, *Proc. Amer. Math. Soc.* 9 (1958), 631–634, for the statement that Wielandt’s 1950 paper gave \(n^2-2n+2\) without proof; Schneider, *Linear Algebra Appl.* 353 (2002), for the diary proof. The character tables were compared with the standard tables of \(S_4\) and \(A_5\), recomputed from the cycle index rather than copied from a webpage.

## 6. Not reviewed

- Line-by-line reading of the proofs in Chapter 8 (tower law through constructibility), most of Chapter 7 after the Smith statement, the rational and Jordan forms, and the uniqueness of invariant factors.
- Appendix B beyond the statements of the circulant and Paley eigenvalue theorems: Krawtchouk polynomials, Delsarte’s bound, and the group-determinant factorisation.
- Existence proofs for Perron’s theorem and Frobenius’s theorem in Appendix A, other than the exponent arithmetic and the Markov corollary’s appeal to them.
- The two Paley constructions from the first character-sum estimate to the last matrix identity.
- Solutions other than those in Chapter 1, the four-square and Egyptian-fraction solutions in Chapter 12, and the class-size and Sylow arguments that sit in the main text. Label alignment was checked for all 163.
- Most figures as pictures. The \(D_4\) table, the cube axes, the character tables, the cap-set caption, the PageRank graph, and the About the Cover parameters were checked. The fifteen-puzzle drawing, the Galois lattice, and the icosahedron vertex list were not redrawn.
- Every one of the 249 lines in the repository that mention “Volume 3”. The numbered theorem, proposition, lemma, corollary, and exercise pointers found by a script were the ones opened. Unnumbered phrases (“as in Volume 3”, “the Vandermonde determinant of Volume 3”) were sampled, not exhausted.
- A Kindle Paperwhite rendering. EPUB structure and CSS were checked; device hyphenation and baseline alignment were not.
- Visual inspection of all 518 reading pages. All pages were measured for text outside the trim; about thirty were rendered and looked at.
- The comparison with existing Volume 3 reviews. That section is written after this scorecard is committed.

## 7. Comparison with existing reviews

Written after the scorecard above was committed. The documents opened were `review/volume3-rewrite/REVIEW.md` (2 November 2026, twelve editorial passes) and the internal series under `review/volume3-internal/`, chiefly `ASSIGNED-FINAL-REVIEW.md`, `PROGRESS.md`, `GLOBAL-CH10.md` and `GLOBAL-APPC.md`. No earlier pull-request thread was read.

### What those reviews already caught, and what is still fixed

The rewrite log’s corrections are present in the current manuscript, and the checks in this read agree with them.

- The odd-cycle walk in the solution of the character exercise uses \(\cos(\pi/n)\), attained at \(m=(n\pm1)/2\), not \(\cos(2\pi/n)\). For odd \(n\ge 3\), \(\pi/n<2\pi/n\le\pi/2\), so the cosine at the smaller angle is the larger one. The correction is right (`ch11-characters.tex` around the boxed transform of \(s^{*t}\)).
- The class equations of \(D_4\) and \(Q_8\) are \(8=1+1+2+2+2\) (`ch03-actions.tex`).
- The Galois memoir is dated 16 January 1831, with publication in 1846; the finite-field note stays in 1830 (`ch10-galois.tex` sources, `ch09-finite-fields.tex`).
- The cap-set base uses \(x=59/100\), not \(0.6\), and the rational comparison really is strict.
- Pohlig–Hellman is stated for a cyclic group of factored order (`ch05-sylow.tex`). The QR sentence counts codewords, not an arbitrary fraction of the printed square (`ch09-finite-fields.tex`).
- A search found no leftover `\end{solution>` typo. Exercise, hint and solution counts are 163 each.

The rewrite log is explicit that a finished proof ledger is not a mathematical certificate, and that cross-volume continuity was still open at the end of that file. The later internal review is more confident: it says every reference use inside Volume 3 was traced, and that merge required no unresolved mathematical finding. That audit follows pointers **out of** Volume 3 into Volumes 1 and 2, and it forbids using a later volume as a premise. It does not check pointers **into** Volume 3 from Volumes 4–15.

### What they missed

1. **Stale theorem and exercise numbers in later volumes.** This is the largest gap. `GLOBAL-CH10.md` knows that `ex:phin` is the cyclotomic isomorphism and that Cardano is a separate deferred exercise. It never notices that Volumes 13 and 15 still call that isomorphism Exercise 10.8, which is now Cardano. The same silence covers Theorem 6.17 versus 6.18, Proposition 6.16 versus 6.17, and Theorem C.11 versus C.12. `GLOBAL-APPC.md` checks the Cauchy–Davenport argument and does not record its printed number. Issues V3-1, V3-2 and V3-3 are absent from both reviews.

2. **Volume 9’s spectral theorem and “Chapter 2” as a volume formula.** Lemma 12.3 is discussed in the rewrite log as an axis-angle proof, which is what it is. Neither review flags Volume 9’s use of that lemma as surjectivity of \(\exp:\mathfrak{so}(3)\to SO(3)\), or the Gram-determinant sentence that sends the reader to Volume 3, Chapter 2. Issue V3-4.

3. **No index.** The internal review treats bibliographies as reviewed and the page count as closed. It does not say that a 507-folio book has no index. Issue V3-5.

4. **A verified paper left on the wrong chapter.** The rewrite log confirms Rokicki–Kociemba–Davidson–Dethridge and keeps it among the sources. The body of Chapter 1 no longer uses the cube-group diameter. The citation is accurate and misplaced. Issue V3-6.

5. **Appendix D’s missing source list.** Both reviews discuss the 2026 Hadamard report, which the footnote states correctly. They do not note that Appendix D, unlike A–C, has no “Sources and further reading” section. Issue V3-7.

The Sylow lemma’s unwritten case \(a=0\) (V3-8) is too small to call a miss; the internal registers are full of boundary notes of that kind. The two solution slips V3-9 and V3-10 were found by reading the appendix exercises after the first scorecard. They are misnamed theorems, not wrong conclusions, and they do not change the appendix score.

### What they mark as settled that is not

Nothing in the list of explicit mathematical corrections above is still broken. The claim that does not hold is the internal review’s closure of “reference uses” if that phrase is read as the series’ citations of this volume. Those citations still resolve to the wrong statement in the four places logged as V3-1 through V3-4. The rewrite file itself did not claim that audit was done. The assigned final review’s sentence that merge required “no unresolved identified mathematical/editorial finding” is about findings that review had already identified. It did not identify these.
