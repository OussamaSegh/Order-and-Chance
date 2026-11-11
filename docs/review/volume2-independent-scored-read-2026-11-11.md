# Volume 2 independent scored read

**Book.** *Order and Chance*, Volume 2: *The Integers: Primes, Patterns and Proofs*.
**Commit reviewed.** `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f` (11 November 2026), which is `8b8a5be3` as named in the brief.
**Artefacts.** GitHub release `books` (published 2026-11-11): reading PDF `Volume.2.-.The.Integers.pdf` (334 pages, 504 × 720 pt) and print PDF `Volume.2.-.The.Integers.-.Print.pdf` (333 pages, 513 × 738 pt), plus the EPUB.
**Reader.** A motivated reader who has Volume 1 and no university course in algebra or number theory.
**Referee.** Independent of the author. Existing files under `review/`, `docs/review/`, `docs/handoffs/` and `docs/plan/` whose names concern Volume 2, and earlier Volume 2 pull-request discussions, were not opened before this scorecard and issue log were written. The comparison section is added only after this record is committed.

Printed chapter numbers follow `volume2-integers/main.tex`, not the filenames. Theorems, propositions, lemmas, corollaries, definitions and numbered examples share one counter per chapter. The reading-PDF contents and the rendered theorem numbers agree with that order:

| Printed chapter | Title | Source file |
|---|---|---|
| 1 | Divisibility and the Euclidean Algorithm | `ch01-divisibility.tex` |
| 2 | Primes | `ch02-primes.tex` |
| 3 | Congruences | `ch03-congruences.tex` |
| 4 | Arithmetic Functions | `ch04-arithmetic-functions.tex` |
| 5 | Primitive Roots and the Multiplicative Group | `ch05-primitive-roots.tex` |
| 6 | Quadratic Residues and Reciprocity | `ch06-quadratic-reciprocity.tex` |
| 7 | Sums of Squares | `ch07-sums-of-squares.tex` |
| 8 | Diophantine Equations | `ch09-diophantine.tex` |
| 9 | Continued Fractions and Pell's Equation | `ch08-continued-fractions.tex` |
| 10 | Gaussian and Eisenstein Integers | `ch10-gaussian-eisenstein.tex` |
| 11 | Characters, Euler Products and the Sieve | `ch14-characters.tex` |

There is no printed Chapter 12, 13 or 14. Reading-PDF page \(N\) in the main matter carries folio \(N-13\) (Chapter 1 opens on PDF page 15, folio 2; About the Cover is PDF page 334, folio 321).

## How the scores were reached

Main-text proofs in all eleven chapters, the preface, the blurb, the field guide and About the Cover were read from the source. Every solution in Chapter 1 was read line by line. Selected solutions in Chapters 2 and 7 were read line by line and are named below. Numerical claims were recomputed in Python and are listed under Verified correct. A numerical check is not treated as a proof. Classical comparisons used the standard statements of the theorems (two squares, reciprocity, Pell, Fermat for exponents 3 and 4, the Euclid–Euler theorem on even perfect numbers) and, for the circle problem, M. N. Huxley, *Exponential sums and lattice points III*, Proc. London Math. Soc. (3) 87 (2003), 591–609, whose abstract gives the exponent \(131/208\), together with the historical table on MathWorld’s “Gauss’s circle problem” page (consulted 11 November 2026), which records later exponents and agrees that \(131/208\) is not the current record. Volume 1 was opened for the group definition, Euler’s constant, the Basel problem, and the irrationality exercises for \(e\) and \(\pi\).

Layout scores rest on a sample of rendered reading pages (cover, Chapter 1 opener, the reciprocity and Markov figures, About the Cover), a full-page geometry scan of both PDFs, and a structural check of the EPUB. They are not a page-by-page proofread of all 334 pages.

## 1. Chapter and appendix scores

Dimensions: (a) correctness, (b) rigor, (c) prerequisite discipline, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) layout. A dash means the section has no exercises or no figures of its own. Ten is reserved for work with no defect of that kind.

| Chapter | a | b | c | d | e | f | g | h | i | j |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 Divisibility | 9 | 8 | 8 | 9 | 8 | 8 | 9 | 8 | 5 | 8 |
| 2 Primes | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 7 | 8 |
| 3 Congruences | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 6 | 8 |
| 4 Arithmetic functions | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 6 | 8 |
| 5 Primitive roots | 8 | 8 | 8 | 7 | 8 | 6 | 7 | 8 | 7 | 8 |
| 6 Reciprocity | 9 | 8 | 8 | 7 | 8 | 6 | 9 | 8 | 5 | 8 |
| 7 Sums of squares | 9 | 8 | 8 | 8 | 9 | 8 | 9 | 8 | 7 | 8 |
| 8 Diophantine equations | 8 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 7 | 8 |
| 9 Continued fractions | 8 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | 7 | 8 |
| 10 Gaussian and Eisenstein | 8 | 7 | 8 | 6 | 7 | 6 | 8 | 7 | 7 | 8 |
| 11 Characters and the sieve | 8 | 8 | 8 | 7 | 7 | 6 | 8 | 8 | 7 | 8 |
| Field guide | 9 | 8 | 8 | 8 | 8 | — | — | 8 | 7 | 8 |

### Chapter 1

(a) The division theorem, Bézout, Euclid’s lemma, unique factorisation, Lamé’s bound and all fifteen solutions were checked; the recomputed values (gcd examples, \(v_5(1000!)=249\), the orchard count) agree. (b) Existence and uniqueness of the remainder are separated, and the induction for unique factorisation names Gauss’s lemma at the cancellation step (`ch01-divisibility.tex:117–148`). The orchard solution is a correct planar Minkowski argument, written more briefly than the surrounding chapter. (c) The subgroup test is taken from Volume 1’s complex-numbers chapter, which is printed Chapter 5 and really does define a group and prove the subtraction test for \((\Z,+)\). Probability exercises use Volume 1’s expectation and tail sum. (d) The opening staircase \(252,198\) is the right first page for this reader (folio 2). (e) Examples precede the general algorithm, and the three-part exit check separates invariant, termination and certificate. Pólya’s orchard, at two stars, is a sharp jump. (f) Every exercise has a hint and a solution; the solutions teach the method, and the numerical ones were recomputed. (g) The visible-point caption, \(224\) of \(376\) points in the disc of radius \(11\), matches a direct count (`ch01-divisibility.tex:426–430`). (h) The voice is concrete and addressed to the reader. (i) Theorem 1.5 is Euclid’s lemma and is named “Gauss’ lemma” (`ch01-divisibility.tex:106`); Chapter 6 then gives that name to a different theorem. (j) The sampled opener is clean and inside the margins.

### Chapter 2

(a) Euclid, Euler’s reciprocal bound, the Chebyshev product and Erdős’s form of Bertrand were re-derived; the chain of test primes through \(631\) is prime, and \(h(512)=\frac{34}{3}\ln 2>0\) with \(h'>0\) on \([512,\infty)\). (b) Finite products are not silently replaced by infinite ones, and the small range of Bertrand is a finite check rather than an appeal to the asymptotic (`ch02-primes.tex:250–265`). (c) Binomial coefficients, integrals and series are Volume 1 tools, and the quantitative half is marked optional (`ch02-primes.tex:121–131`). Furstenberg’s proof defines the topology it uses and is labelled optional. (d) The distinction between a new prime factor and a prime value of \(N\) is made with \(30031=59\cdot509\). The Bertrand write-up is dense for a first reading, which is why the optional banner matters. (e) The sieve, the mod-\(4\) tracks and the binomial contest each earn their picture. (f) The solutions read for Exercises 2.1–2.3 are correct, including \(4\cdot3\cdot7\cdot11-1=923=13\cdot71\) and Sophie Germain’s factorisation. The remaining solutions were sampled rather than re-proved. (g) The prime-count caption at \(10^5\) matches \(\pi(10^5)=9592\): the ratios are \(1.104\) and \(0.996\). (h) Same plain voice as Chapter 1. (i) Notation is stable, apart from the inherited name of Euclid’s lemma where a solution uses it. (j) Sampled pages sit inside the text block.

### Chapter 3

(a) Hensel’s lemma, as stated for a simple root, follows from the polynomial expansion, and the lift \(2\mapsto7\pmod{25}\), then \(57\) and \(68\pmod{125}\), was recomputed (`ch03-congruences.tex:270–291`). (b) The hypothesis \(f'(a)\not\equiv0\pmod p\) is shown to be necessary by the two singular examples \(X^2\) and \(X^2-5\). (c) Euler, Wilson and the Chinese remainder theorem are proved here before use; the chapter does not borrow Bertrand. (d) The clock-and-lift exposition is clear. Several later exercises (Wolstenholme, Morley, Kloosterman) are not clear at two stars without a much longer apprenticeship. (e) The first-reading banner correctly says later chapters need the Chinese remainder theorem and Euler, not Hensel. (f) Score limited because the long optional solutions were not line-checked. The exercise *statements* that were read are well posed, and Lucas’s theorem is correctly pointed at \((1+X)^p\). (g) The Hensel tree matches the arithmetic. (h) Voice holds. (i) Solutions again call Euclid’s lemma “Gauss’s lemma” (`ch03-congruences.tex:663`), so the ambiguous name is already in use before Chapter 6. (j) No overflow found on the sampled pages.

### Chapter 4

(a) The Euclid–Euler theorem and Dirichlet’s hyperbola formula were checked. The identity \(\sum_{n\le x}\tau(n)=x\ln x+(2\gamma-1)x+O(\sqrt x)\) follows from the stated harmonic bounds, and those bounds are exactly what Volume 1 proves for \(\gamma\). The case \(x=10\) gives \(27\), as claimed. (b) The error \(O(\sqrt x)\) is defined before it is interpreted, and the text refuses to turn an average into a pointwise bound (`ch04-arithmetic-functions.tex:458–464`). (c) The citation is by chapter name (“Sequences and Series”), and that chapter does contain the inequality. The Basel evaluation used in Exercise 4.8 is in Volume 1’s polynomials chapter, as the exercise says. (d) Multiplicative functions are motivated by formulas before the Dirichlet ring. (e) Perfect numbers are reached through \(6\), \(28\) and \(496\). (f) Not every solution was re-proved. Exercise 4.7 is the count of primitive words, \(\sum_{d\mid n}\mu(d)q^{n/d}\); later volumes cite “Exercise 4.7” for a different theorem (issue V2-01). (g) The hyperbola figure’s job matches the double count. (h) Voice holds. (i) The same borrowed name of Euclid’s lemma appears in the perfect-number proof (`ch04-arithmetic-functions.tex:302`). (j) Sampled pages are clean.

### Chapter 5

(a) The structure of \((\Z/2^k\Z)^\times\) and the square test modulo \(2^k\) were checked, including \(v_2(5^{2^m}-1)=m+2\) and the order of \(5\) modulo \(32\). The mod-\(5\) character table printed in Chapter 11, which depends on this chapter’s primitive root \(2\), was recomputed. (b) The lifting-the-exponent step keeps the odd unit \(t\) visible, so the valuation increases by exactly one. (c) Orders divide \(\varphi(m)\) only after Euler’s theorem, and cyclicity of \((\Z/p\Z)^\times\) is Theorem 5.3, not a forward reference. (d) The discrete-logarithm examples modulo \(13\) are easy to follow; the existence proof that a prime modulus has a primitive root is necessarily more abstract. (e) A generator is exhibited before the classification of all \(n\). Artin’s constant is correctly described as about \(37.4\%\) and not universal (`ch05-primitive-roots.tex:459`). (f) Exercise 5.7 proves infinitely many primes \(\equiv1\pmod n\) by cyclotomic polynomials. It is not the Gauss-sum evaluation later volumes attach to that number. Solutions beyond the statements were not all re-checked. (g) The order diagrams were not numerically audited one vertex at a time. (h) Voice holds. (i) Local notation for orders is consistent with the field guide. (j) Sampled pages are clean.

### Chapter 6

(a) Euler’s criterion, Gauss’s lemma, the law for \(2\), quadratic reciprocity and the Jacobi symbol were checked on the printed examples: \(\bigl(\frac{3}{11}\bigr)\), \(\bigl(\frac{2}{11}\bigr)\), \(\bigl(\frac{3}{13}\bigr)\), \(\bigl(\frac{219}{383}\bigr)\) with root \(169\), and the Jacobi values \(\bigl(\frac{1001}{9907}\bigr)=-1\), \(\bigl(\frac{43}{91}\bigr)=1\), \(\bigl(\frac{2}{15}\bigr)=1\). (b) Eisenstein’s lemma records that \(a\) must be odd, and the text immediately shows that \(a=2\), \(p=3\) makes the floor sum lie (`ch06-quadratic-reciprocity.tex:290–295`). The rectangle count \(T(11,7)+T(7,11)=8+7=15\) matches the figure. (c) Nothing here is used before the two-square chapter, which cites it openly. The Gauss-sum proof is an optional exercise and names the Volume 1 input. (d) The law itself is one sentence; the proof is a lattice count a strong reader can follow, and a first reader will feel the density. (e) A sign table is demanded before the proof, and the false comfort of a Jacobi symbol equal to \(1\) is shown rather than only warned about. (f) Exercise 6.7 really is the Gauss sum with \(g^2=p^*\). The long optional solutions were not line-checked, so the exercise score stays at the level of the statements. (g) Figure 6.3’s eight points below the diagonal and seven above it agree with the floors. (h) Voice holds, including the sentence that tells the reader to try \(a=2\) before dropping a hypothesis. (i) This chapter’s own Theorem 6.3 is the classical Gauss lemma, while Theorem 1.5 still carries the same name. A reader who meets “Gauss’s lemma” in a solution cannot tell which result is meant without the context. (j) The figure and the following proof sit on facing material and are readable; the sum in Lemma 6.6 is tight but not broken.

### Chapter 7

(a) Fermat’s two-square theorem, the general criterion (Theorem 7.3), Lagrange’s four-square argument and Gauss’s circle estimate were checked. The list of sums of two squares through \(20\), the factorisations from \(2021\) to \(2030\), and \(N(2)=13\), \(N(6)=113\), \(N(10)=317\) all match. (b) Thue’s lemma supplies the strict inequalities \(0<x^2+y^2<2p\). The four-square descent keeps the multiplier odd before it uses residues of size at most \((m-1)/2\), so the new multiplier is strictly smaller. The Euler identity is not expanded in the text. (c) The square root of \(-1\) is quoted from Chapter 6, and Jacobi’s formula is labelled as a preview proved only in Chapter 10. (d) \(2026=1^2+45^2\) against \(2027\equiv3\pmod4\) is the right opening. (e) Obstruction and classification are separated in a workshop, and the circle problem is marked optional. (f) The solutions of Exercises 7.1–7.5 and the triangular-number exercise were re-read; \(1013=22^2+23^2\) and the identity producing \(1^2+45^2\) are correct, and the three-square obstruction modulo \(8\) is complete. Zagier’s involution was not expanded term by term. (g) The sixteen representations of \(65\) agree with \(r_2(65)=16\). (h) Voice holds. (i) The two-square and four-square statements are worded so the reader can see which one allows zero. The epigraph says every non-negative integer is a sum of four squares, while Theorem 7.4 says every positive integer. (j) Sampled pages are clean.

### Chapter 8

(a) The Pythagorean parametrisation, Fermat’s descent for \(x^4+y^4=z^2\), the chord method and the Mordell equation \(y^2=x^3+7\) were checked. The inradius \(r=n(m-n)\) recovers \(1\) for \((3,4,5)\) and \(2\) for \((5,12,13)\). The Markov tree drawn in the figure satisfies \(a^2+b^2+c^2=3abc\). (b) Descent is stated as three obligations (integers, the same equation, a strictly smaller positive measure) and the Fermat proof meets them: the new hypotenuse \(w\) satisfies \(w<z\). Pairwise coprimality of \(m,a,b\) is compressed into one sentence. (c) The chapter uses unique factorisation and the two-square obstruction already proved, and it tells the reader that continued fractions do not depend on the optional conic and Markov material (`ch09-diophantine.tex:294–302`). (d) The positive-integer domain is discussed before any clever factorisation. The Fermat proof is still a hard page. (e) Congruences, then parametrisation, then descent, is the right order, and each is shown failing to do the others’ job. (f) The optional exercises were not line-checked. (g) Figure 8.3’s slopes \(t=\tfrac12\) and \(t=\tfrac23\) give \((3/5,4/5)\) and \((5/13,12/13)\), and the Markov children of \((1,5,13)\) and \((2,5,29)\) are the ones drawn. (h) Voice holds. (i) Notation for primitive triples is fixed before the theorem and kept. (j) The combined chord-and-tree figure is crowded but the labels that were checked are the right points.

### Chapter 9

(a) The convergent recurrence, the determinant identity, the approximation theorem, Legendre’s test, Lagrange’s periodicity theorem and the existence of a Pell solution were checked on \(\sqrt2\), \(\sqrt3\), \(\sqrt7\), \(415/93\) and \(-43/19\). The fundamental solution of \(x^2-61y^2=1\) is the pair printed, and \(8^2-7\cdot3^2=1\). (b) The proof that an infinite continued fraction defines a unique irrational keeps even and odd convergents monotone and the tail strictly above its first partial quotient. The Pell argument uses infinitely many approximations, a finite set of norms, and a pigeonhole, and it separates existence from the generation of all solutions. (c) Dirichlet’s approximation theorem is proved here from the convergents; it is not quoted from a later volume. The irrationality of \(e\) and of \(\pi\) is correctly placed in Volume 1’s calculus chapter, which is printed Chapter 8 and contains those two exercises. (d) The passage from Euclid’s algorithm on \(43/19\) to \(\sqrt2\) is clear. Lagrange’s proof that a quadratic irrational has a periodic expansion is a difficult page for this reader, though the bookkeeping is present. (e) \(3/2\) and \(17/12\) are solved as Pell equations before the general theorem, and the text separates \(|x-p/q|\) from \(|qx-p|\) with the explicit pair \(311/99\) and \(22/7\). (f) Exercise solutions in this chapter were not line-checked. (g) The quality caption’s limits \(1/\sqrt5\) and \(1/(2\sqrt2)\) are the right limits for the convergents of \(\varphi\) and of \(\sqrt2\). (h) Voice holds. (i) The subscript of a convergent starts at \(0\), and the field guide says so. (j) Sampled pages are clean.

### Chapter 10

(a) Failure of unique factorisation in \(\Z[\sqrt{-5}]\), the list of Gaussian primes, Jacobi’s formula and the splitting law in \(\Z[\omega]\) agree with the classical statements, and the norm checks \(N(2-\omega)=7\), \(N(2+\omega)=3\), \(N(1-\omega)=3\) are right. (b) The Fermat proof for exponent \(3\) is the standard descent and the unit check modulo \(\lambda^2\) is complete, but it is compressed to the point that a first reader cannot reconstruct the valuation count without copying the page. The four-square identity’s style of “one checks” reappears as unique factorisation “by the same chain”. Score 7 because the argument is present and correct, yet several implications are one sentence long. (c) The two-square theorem is cited as Theorem 7.2, which is the right printed number, and the text does not use the ideal theory it postpones to Volume 13. (d) This is the least readable chapter for the intended reader. The Gaussian prime list is clear; the cube descent is not, despite the three-job summary that follows it. (e) \(6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})\) is shown before the definition of a non-unique factorisation, which is the right order. (f) Exercise statements were read; their solutions were not re-proved. Euler’s \(1000009=293\cdot3413\), with the two printed representations, is correct. (g) The norm-\(\le225\) prime plot was not counted element by element. The Eisenstein lattice figure matches \(N(1-\omega)=3\). (h) The voice is still plain, but the cube proof sounds like a lecture compressed into one page. (i) Units, norms and associates are distinguished, and the text says an irreducible need not be prime. (j) Sampled pages are clean.

### Chapter 11

(a) The count of characters, orthogonality, the sieve identity and the bound on \(\sum\chi_4(n)/n\) were checked. \(\Phi(30,5)=8\), \(\Phi(100,10)=22\) and \(\pi(100)=25\) are right, and the partial sum of \(\mu(n)/n^2\) through \(n=10\) is \(0.6163\). The mod-\(5\) table matches \(i^{jk}\). (b) The sieve is an exact finite identity. The discussion at \(s=1\) states what is proved (the grouped series lies in \(\bigl(\tfrac23,1\bigr)\), which contains the true value \(\pi/4\) but is not claimed to equal it) and what is not (non-vanishing of \(L(1,\chi)\), and convergence of \(\sum_p\chi_4(p)/p\)). That restraint is the right standard. (c) Characters are built from the unit groups of Chapters 3 and 5. The indicator formula is not used to prove a theorem that this chapter has postponed. (d) The finite theory is readable. The Abel-mean argument at the boundary is honestly labelled optional and is still hard. (e) \(\chi_4\) is met as Jacobi’s sign before it is axiomatised. (f) Twenty exercises, many of them optional and some far above two stars; their solutions were not line-checked. (g) The sieve picture for \(1\) through \(30\) leaves the eight survivors the formula counts. The mod-\(4\) race at \(100\) is \(13\) against \(11\), as the caption says. (h) Voice holds, and the text declines a conclusion it has not earned. (i) \(\chi_4\), \(L(s,\chi)\) and \(\Phi(x,z)\) match the field guide. (j) Sampled pages are clean.

### Field guide

(a) The worked inverse of \(35\) modulo \(12\), the failure for \(18\), and the glossary agree with the chapters. \(\gcd(0,0)=0\) matches the subgroup \(0\Z\). (b) The five questions at the end are checks a proof can fail, not a substitute for one. (c) The \(p\)-adic notation is marked as a later-volume preview and is not used as a premise. (d) A reader who has finished the book can use the tool list. (e) The \(n^2+1\) investigation shows a failed guess turning into Euler’s criterion, and it stops before claiming infinitely many prime values. (h) The closing invitation to Volume 3 names groups, rings and homomorphisms on three examples the reader has. (i) The glossary repeats the careful distinction between the Legendre and Jacobi symbols. (j) The closing pages are sparse and readable. There is no exercise section and no figure of its own.

## 2. Whole-book scores

| Item | Score |
|---|---:|
| Structure and arc | 9 |
| Continuity with Volume 1 | 8 |
| Preparation for later volumes | 4 |
| Delivery of the title and subtitle | 9 |
| Front matter, back matter, index and bibliography | 6 |
| Print PDF | 8 |
| EPUB | 8 |
| **Overall** | **8** |

**Structure and arc.** The four parts in the preface are the four parts of the book: divisibility and primes, then residue patterns, then equations, then characters. Each chapter ends by naming the next question, and the last page names Volume 3 rather than pretending Dirichlet’s theorem has been proved. Placing Diophantine equations before continued fractions matches the preface and is pedagogically sound. The filename order is the reverse of that choice, which is the root of issue V2-01, but the arc a reader meets is coherent.

**Continuity with Volume 1.** Volume 1’s field guide sends the reader here for division, Bézout and unique factorisation, and this book re-proves them instead of quoting them as black boxes. The group language used in Chapter 1 is the language of Volume 1, Chapter 5. The harmonic bounds, the Basel problem, and the irrationality of \(e\) and \(\pi\) are in the chapters the text names. The fit is real. It is not a 9 because Euclid’s lemma is renamed on its second appearance, and a reader fresh from Volume 1 will not have met that name for this fact.

**Preparation for later volumes.** The theorems later volumes need are in the book: the Chinese remainder theorem, Hensel, cyclicity, reciprocity, the two-square criterion, Pell, Gaussian and Eisenstein primes, Fermat for exponents 3 and 4, characters and the sieve. Internal cross-references use `\ref` and resolve. The hardcoded numbers in Volumes 3–15 often do not. Of the later volumes, ten contain numbered citations of Volume 2 (161 such citations). Many of those numbers belong to a different chapter order: primitive roots and reciprocity as Chapters 4 and 5 rather than 5 and 6, arithmetic functions as Chapter 6 rather than 4, and continued fractions and Diophantine equations swapped as Chapters 8 and 9. A reader who follows Volume 13’s “Theorem 9.2” lands on a continued-fraction bound, not on \(x^4+y^4=z^2\). That is a failure of the series handoff even though the mathematics is present. Details are issue V2-01. The prose handoff itself is accurate: Volume 6 is *Crossroads: Arithmetic Meets Analysis* and really does own the prime-number theorem, and Volume 13 really does own ideals and the \(p\)-adics.

**Title and subtitle.** *Primes, Patterns and Proofs* is what the book does. Primes are Chapters 2 and 11, patterns are reciprocity and characters, and the proofs are written out. The subtitle is not a decoration.

**Front matter, back matter, index and bibliography.** The preface is a genuine introduction: \(5=1^2+2^2\) against \(7\), four parts, 144 exercises (the count is right), and a first-reading route. The blurb names the same objects. About the Cover matches the two-square theorem and the rendered cover. The field guide is usable. There is no index and no single bibliography. Sources are chapter-end lists; the Chapter 1 list (Hardy–Wright, Ireland–Rosen, Knuth, Shoup, Ramírez Alfonsín, Euclid) is real and relevant. A 300-page book that the rest of the series cites by theorem number needs an index.

**Print PDF.** All 333 pages are \(513\times738\) pt, PDF 1.3, with empty document information, no outlines and no annotations. The part opener’s charcoal reaches the media-box corners, so the bleed is painted, not padded with white. Body text on the sampled pages sits inside the trim. This is not a KDP upload, and not every page was inspected by eye.

**EPUB.** The file is about 20 MB. Thirty-nine figure plates are PNG, each at least 1600 pixels wide, with `width: 100%` and `max-width: 100%`. Inline formulas carry an em width and an em `vertical-align`. There are no SVG plates. Fonts are embedded. It was not read on a Kindle Paperwhite.

## 3. Overall score

**8.** The mathematical spine is sound. Where a proof was read line by line, the hypotheses are the ones the argument uses, and where a number was recomputed, it agreed. The book is written in the series voice, it builds on Volume 1 by name and by chapter, and it stops at the analytic boundary instead of pretending to cross it.

I would recommend it to its intended reader as a book to learn from. I would not recommend the series citation apparatus as it stands. Later volumes send that reader to theorem numbers this printing does not use, and two different results are called Gauss’s lemma. Those are repairs, not a different book.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
|---|---|---|---|---|---|
| V2-01 | `volume2-integers/main.tex:37–54`, and the later-volume lines in the table below | Cross-volume citations | critical | Printed numbers follow `main.tex`: arithmetic functions is Chapter 4, primitive roots Chapter 5, reciprocity Chapter 6, Diophantine equations Chapter 8, continued fractions Chapter 9. Many later citations use the other assignment (primitive roots and reciprocity as 4 and 5, arithmetic functions as 6, continued fractions as 8, Diophantine equations as 9), which matches filenames `ch05`, `ch06`, `ch04`, `ch08`, `ch09` and not the printed book. | Keep this reading order; it is the order the preface teaches. Correct the hardcoded numbers in Volumes 3–15 to the printed numbers. Do not add an old-to-new concordance to reader-facing pages. Add a build check that a citation of the form “Volume 2, Theorem \(a.b\)” matches the statement at that printed number. |
| V2-02 | `ch01-divisibility.tex:106` (Theorem 1.5); `ch06-quadratic-reciprocity.tex:171` (Theorem 6.3); also `ch03-congruences.tex:663`, `ch04-arithmetic-functions.tex:302`, `ch05-primitive-roots.tex:82` | Terminology | major | Theorem 1.5 is Euclid’s lemma: if \(a\mid bc\) and \(\gcd(a,b)=1\), then \(a\mid c\). It is titled “Gauss’ lemma”. Theorem 6.3 is Gauss’s lemma on the Legendre symbol. Later solutions say “Gauss’s lemma” for the divisibility form. | Rename Theorem 1.5 to Euclid’s lemma, and say “Euclid’s lemma” wherever the divisibility form is used. Leave the name Gauss’s lemma for Theorem 6.3. |
| V2-03 | `volume2-integers/main.tex:56–60`; no `\printindex` or `\bibliography` in the volume | Back matter | major | The reading PDF contents run from the preface to About the Cover. There is no index and no consolidated bibliography. Sources exist at the end of chapters. Later volumes cite this book by theorem number. | Add an index of theorems, named lemmas and symbols. A single bibliography can gather the chapter lists; until then, keep the chapter lists, which are genuine. |
| V2-04 | `ch07-sums-of-squares.tex:164–168`, Theorem 7.4 | Rigor | minor | Euler’s four-square identity is the engine of Lagrange’s theorem and is introduced by “one checks by expansion”, with the four bilinear forms written out. The identity is true (it reproduces the printed descent for \(p=7\)), but it is not proved on the page. | Expand the identity once, or derive it from the quaternion norm and point to that derivation when Volume 3 is reached. Do not leave the first occurrence as an unchecked expansion. |
| V2-05 | `ch07-sums-of-squares.tex:4` and `:160–161` | Statement | minor | The chapter epigraph says every non-negative integer is a sum of four squares. Theorem 7.4 says every positive integer. The proof then treats \(0\) and \(1\) as extra cases. | State the theorem for non-negative integers, including the zero tuple, or drop zero from the epigraph. |
| V2-06 | `ch01-divisibility.tex:415–423`, Exercise 1.15 (two stars); `ch03-congruences.tex:408–421`, Exercises 3.16 and 3.18 | Pedagogy | minor | Exercise 1.15 asks for Minkowski’s theorem on a centred rectangle, proved in full in the solution. Wolstenholme’s theorem and Morley’s congruence are two-star exercises in Chapter 3. The mathematics of the orchard solution is right; the star does not describe the difficulty. | Mark these as optional three-star explorations, as the book already does for Bertrand’s quantitative route, or move the Minkowski argument into a clearly optional section. |
| V2-07 | `about-the-cover.tex` (the generated paragraph) | Caption | minor | “Eight dots lie on a prime one more than a multiple of four” is true as a count of representations with signs and order, for every prime \(p\equiv1\pmod4\) up to \(53\) (none of those primes is a square plus itself). Read quickly, it can sound like eight dots in the whole picture. The prime \(2\) is correctly given four dots. | Write “each prime one more than a multiple of four carries eight dots”. |

### V2-01. Citations that do not say what they claim

The right-hand column is the statement that actually carries that printed number.

| Later location | What it claims | What the printed number is |
|---|---|---|
| `volume15-order-and-chance/chapters/ra-anatomy.tex:23` and `:358`, Theorem 4.5 | \((\Z/p^e\Z)^\times\) is cyclic for odd \(p\) | Theorem 4.5 is the Euclid–Euler theorem on even perfect numbers. Cyclicity is Theorem 5.5. |
| `volume15-order-and-chance/chapters/conjectures-ch12-algebra.tex:54` and `:482`, Theorem 4.3 | \((\Z/p\Z)^\times\) is cyclic | Proposition 4.3 is Dirichlet convolution. Cyclicity is Theorem 5.3. |
| `volume15-order-and-chance/chapters/conjectures-ch11-random.tex:231`, Chapter 4 | primitive roots | Chapter 4 is arithmetic functions. Primitive roots are Chapter 5. |
| `volume15-order-and-chance/chapters/conjectures-ch11-random.tex:476`, Chapter 5 | \(\bigl(\frac{2}{p}\bigr)=1\) for \(p\equiv\pm1\pmod8\) | That supplementary law is Corollary 6.4. Chapter 5 is primitive roots. |
| `volume8-analysis/chapters/ch07-finite.tex:183` and `volume5-calculation/chapters/ch07-fft.tex:186`, Chapter 4 or Theorem 4.3 | a primitive root modulo \(p\) | Same mismatch as above. |
| `volume8-analysis/chapters/ch11-harder.tex:865`, Chapter 6 | multiplicative functions | Chapter 6 is quadratic reciprocity. Multiplicative functions are Chapter 4. |
| `volume5-calculation/chapters/ch10-zeta.tex:102` and `:406`, Theorem 6.4 | \(\mu*\mathbf1=\varepsilon\) | There is no Theorem 6.4 with that content. Corollary 6.4 is the law for \(2\). Möbius inversion is Theorem 4.4. |
| `volume5-calculation/chapters/ch01-finite.tex:685`, Chapter 6 | Möbius inversion | Same mismatch. |
| `volume9-shapes/chapters/ch09-hyperbolic.tex:235–236`, Theorem 8.6 | continued fractions of quadratic irrationals are eventually periodic | Theorem 8.6 is Markov’s theorem on \(x^2+y^2+z^2=3xyz\). Periodicity is Theorem 9.6. |
| `volume13-arithmetic/chapters/ch12-elliptic.tex:11` and `:32`, Theorem 9.2 | \(x^4+y^4=z^2\) has no positive solution, and no right triangle with rational sides has square area | Theorem 9.2 is the continued-fraction error bound. Fermat’s descent is Theorem 8.2. |
| `volume13-arithmetic/chapters/ch12-elliptic.tex:33`, Theorem 9.1 | integer-sided right triangles | Proposition 9.1 is the convergent recurrence. Pythagorean triples are Theorem 8.1. |
| `volume11-randomness/chapters/ch10-ergodic.tex:21`, `:188`, `:252`, Proposition 8.1 and Theorem 8.2 | continued-fraction convergents and complete quotients | Those numbers are the Pythagorean theorem and Fermat’s fourth-power theorem. The continued-fraction statements are Proposition 9.1 and Theorem 9.2. |
| `volume5-calculation/chapters/ch03-series.tex:306` and `:370`, Chapter 8 and Proposition 8.1 | the continued fraction of \(\sqrt d\), and the convergent formula | Chapter 8 is Diophantine equations. Continued fractions are Chapter 9. |
| `volume9-shapes/chapters/geometry-ch05-conics.tex:486` and `volume10-abstraction/chapters/ch07-groupcoh.tex:115`, Chapter 9 | Pythagorean triples | Chapter 9 is continued fractions. The triples are Chapter 8, Theorem 8.1. |
| `volume13-arithmetic/chapters/ch02-ideals.tex:589` and `:812`, Exercise 5.7 | the Gauss sum satisfies \(g^2=q^*\) | Exercise 5.7 is the cyclotomic proof of infinitely many primes \(\equiv1\pmod n\). The Gauss sum is Exercise 6.7. |
| `volume6-crossroads/chapters/ch04-dirichlet.tex:14`, Exercise 4.7 | infinitely many primes \(\equiv1\pmod k\) | Exercise 4.7 counts primitive words. The progression theorem is Exercise 5.7. |
| `volume13-arithmetic/chapters/ch06-local.tex:556`, Corollary 12.9 | a root of \(X^{p-1}-1\) in the \(p\)-adic integers | The book has no Chapter 12 and no Corollary 12.9. |
| `volume8-analysis/chapters/ch11-harder.tex:982`, Chapter 2 | unique factorisation | Unique factorisation is Theorem 1.6, in Chapter 1. Chapter 2 is the distribution of primes. |

Citations that were checked and do resolve: Theorem 7.3 is the two-square criterion, as Volumes 8 and 15 say; Theorem 3.5 is the Chinese remainder theorem and Theorem 3.8 is Hensel, as `ra-anatomy.tex:23` says for those two numbers; Theorem 10.6 is Jacobi’s formula; Theorems 10.7 and 10.9 are the Eisenstein primes and Fermat for cubes; Theorem 2.5 is Bertrand; Exercise 2.1 is infinitely many primes \(\equiv3\pmod4\); Exercise 7.1 is the three-square obstruction, which is the squares-modulo-\(8\) fact Volume 13 cites; Chapter 3 is \(\Z/n\Z\); Chapter 5 is primitive roots in the Volume 3 citations that say so; Chapter 6 is where \(-1\) is shown to be a square modulo \(p\) exactly for \(p\equiv1\pmod4\); Chapter 10 is the Gaussian and Eisenstein theory.

## Verified correct

These were checked in the source and, where a number appears, recomputed. The list is not a claim that nothing nearby could be improved.

**Chapter 1.** Euclidean division for negative dividends, including \(-17=5\cdot(-4)+3\). Bézout for \((240,46)\) giving \(-9\cdot240+47\cdot46=2\), and for \((899,372)\) giving \(5\cdot899-12\cdot372=31\). Unique factorisation, with \(1\) excluded from the primes for the reason the text gives. Lamé’s indexing: seven divisions on \((F_9,F_8)=(34,21)\), and the bound \(b\ge F_{n+1}\). The digit bound \(n\le5d\) from \(\varphi^5>10\). Legendre’s formula and \(v_5(1000!)=249\). The rational-root argument for monic polynomials. \(\gcd(2^a-1,2^b-1)=2^{\gcd(a,b)}-1\), checked on \((63,15)\). The Frobenius number \(ab-a-b\), including the case \(a=1\). The coin example \(3,5\) with largest gap \(7\). The super-Catalan integrality via non-negative valuations. \(n\nmid 2^n-1\) for \(n\ge2\), with Fermat’s little theorem proved from the binomial theorem rather than quoted from Chapter 3. Kummer’s carry count on \(\binom{10}{4}\) and \(\binom{16}{8}\). \(\gcd(1071,462)=21=(-3)\cdot1071+7\cdot462\). The geometric law for \(v_p\), the mean \(1/(p-1)\), and \(\mathbb E[2^{v_2(n)}]=\frac12\log_2 N+O(1)\). The reduced-denominator probability \(1/(p+1)\). The centred-rectangle form of Minkowski used in the orchard, including the strict inequality for the ray through \((R,1)\). The visible-lattice count \(224/376\).

**Chapter 2.** Euclid’s proof, with \(2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509\). Euler’s inequality \(\sum_{p\le x}1/p\ge\ln\ln x-1\), and the printed partial sums at \(10\) and at \(100\). The binomial bounds in Lemma 2.3, including the empty range for \(n<5\). Chebyshev’s product \(\prod_{p\le x}p<4^x\), with \(2310<4^{11}\). Bertrand for \(n\ge1\), with the finite chain through \(631\) and the sign of \(h'\). \(\binom{20}{10}=184756=2^2\cdot11\cdot13\cdot17\cdot19\). Infinitely many primes \(\equiv3\pmod4\). Sophie Germain’s identity. The Fermat numbers’ product formula as stated, and \(2^{32}+1=641\cdot6700417\), \(2^{11}-1=23\cdot89\). The ratios of \(\pi(x)\) to \(x/\ln x\) and to \(\mathrm{Li}(x)\) at \(10^5\).

**Chapter 3.** Hensel’s lemma for a simple root, the lift of \(X^2+1\) through \(5\), \(25\) and \(125\), and the two singular examples. The last two digits of a pure power of \(3\) in the power tower are \(87\), as Exercise 3.7 asks (computed modulo \(4\) and \(25\)).

**Chapter 4.** Euclid–Euler, including \(\sigma(496)=992\). The hyperbola formula and the count \(27\) at \(x=10\). The description of Exercise 4.7 as a word count, not a Dirichlet theorem.

**Chapter 5.** The order of \(5\) modulo \(2^k\), the square criterion modulo \(8\), and \(7^2=49\equiv17\pmod{32}\). Artin’s constant left as a conditional prediction.

**Chapter 6.** The reciprocity examples listed under the chapter score, the Jacobi algorithm’s printed chain for \(1001/9907\), and the warning that \(\bigl(\frac{2}{15}\bigr)=1\) does not make \(2\) a square modulo \(15\). Eisenstein’s count \(T(11,7)=8\), \(T(7,11)=7\).

**Chapter 7.** Theorem 7.3 in the form later volumes quote. The representations of \(65\), \(85\), \(45\), \(1013\) and \(2026\). The classification of \(\{2021,\ldots,2030\}\): only \(2025\), \(2026\) and \(2029\) work. The three-square obstruction. The solutions of \(x^2+2y^2\) and \(x^2+3y^2\) for the primes named. \(N(R)\) at radii \(2\), \(6\) and \(10\). Huxley’s exponent \(131/208\), correctly described as a 2003 bound and not as the last word; the logarithm in Huxley’s theorem is absorbed into the \(\varepsilon\) the book writes.

**Chapter 8.** The primitive Pythagorean formula both ways, the inradius, Fermat’s descent for fourth powers, the chord formulas, \(y^2=x^3+7\) having no integer solution by the prime \(q\equiv3\pmod4\) in \(y^2+1\), and the Markov identities for the nodes drawn in Figure 8.3.

**Chapter 9.** Convergents of \(415/93\), \([1;2,2]\), \(\sqrt2\), \(\sqrt3\), \(\sqrt7\) and \(-43/19\). The determinant sign. Legendre’s sufficient condition. Pell solutions for \(d=2\), \(d=7\) and \(d=61\), the last being \(1766319049^2-61\cdot226153980^2=1\).

**Chapter 10.** The norm argument that \(2\), \(3\) and \(1\pm\sqrt{-5}\) are irreducible and not associates, and that \(2\) is not prime there. Jacobi’s formula at \(25\), \(65\) and \(325\) (\(r_2(325)=24\)). The Eisenstein norm computations above. The shape of the exponent-\(3\) descent, including which units satisfy \(\pm1\pm\eta\equiv0\pmod{\lambda^2}\).

**Chapter 11.** Character count \(\varphi(m)\), the mod-\(5\) table, orthogonality in the form stated, \(\Phi(30,5)=8\) with the eight survivors, \(\pi(100)=25\) from the sieve, the mod-\(4\) counts \(13\) and \(11\) up to \(100\), and the grouped series for \(\chi_4\) lying strictly between \(2/3\) and \(1\).

**Front and back.** One hundred forty-four exercises, each with a hint and a solution environment. The preface’s description of the four parts. The Volume 6 and Volume 13 handoffs, checked against those volumes’ titles and against Volume 6’s prime-number-theorem chapter. The cover colophon against Theorem 7.3 and the rendered cover.

**Production.** Reading PDF \(7\times10\) inches with bookmarks and the design fonts. Print PDF \(7.125\times10.25\) inches, PDF 1.3, no metadata, no annotations, no bookmarks, charcoal carried to the media edge on the part page. EPUB figure and formula rules as in the EPUB score.

## Not reviewed

- Exercise solutions in Chapters 3, 4, 5, 6, 8, 9, 10 and 11, except the individual solutions named above. In particular Wolstenholme, Morley, Kloosterman, the Gauss-sum proof of reciprocity, Zagier’s involution expanded term by term, and the optional exercises of Chapter 11 were not re-proved.
- Every TikZ coordinate. Captions were checked when they state a count or a coordinate that can be recomputed. The Gaussian-prime plot of norm at most \(225\) was not enumerated.
- A page-by-page visual proofread of the 334-page reading PDF and the 333-page print PDF. The geometry scan covered every page; the eye covered a sample.
- Kindle rendering. The EPUB was checked structurally, not on a Paperwhite.
- Portrait attributions beyond the credit lines and the public-domain claims printed with them.
- Every unnumbered mention of “Volume 2” in later books. The 161 citations that carry a chapter, theorem, lemma, proposition, corollary or exercise number were extracted; the rows in V2-01 are the ones whose claim was compared with the printed statement. Vague pointers were not all given a verdict.
- The ISBN \(9798167208650\) against an external registration record.
- Existing Volume 2 review documents. They are compared only in the next section, after this scorecard was committed.

## Comparison with existing reviews

Not written in this commit. The scores and the issue log above were fixed before any Volume 2 review file was opened. The comparison is added in the following commit.
