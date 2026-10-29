# Book 1 — First Principles

*Proof, Problem Solving and Mathematical Thinking.*

**Element.** The survey. Before any course of masonry can be read, the lines on the drawing have to mean one thing.

**On disk.** Volume 0, `tome0-mathematical-maturity`. Ten chapters in `main.tex`, numbered from 0, plus a field guide and image credits. `docs/DESIGN.md` records a 295-page 7×10 print interior after the October reconstruction. The README's "8 chapters" is stale.

## Promise

The reader learns to say what a mathematical sentence promises, to turn a pattern into a proof, and to tell a finite check from a law. Order appears as the identity \(1^3+\cdots+n^3=(1+\cdots+n)^2\). Chance appears as the hat check. They are asked to meet one standard. The series question is planted in one paragraph of the preface and taken up by the field guide: the primes are the masonry on which that standard will be tested, and this book does not yet contain them.

## Prerequisites

Secondary-school algebra. No prior course in proof, calculus, linear algebra, or probability. The preface's foundational contract stays: classical logic, the ordered fields, well-ordering of \(\mathbb N\), completeness of \(\mathbb R\), and the elementary functions \(\exp\), \(\ln\), \(\sin\), \(\cos\) with their addition laws. The short derivative toolkit is in the sequences chapter; the full rules are in the calculus chapter.

## How the subtitle is delivered

The subtitle is three promises: proof, problem solving, and mathematical thinking. The contents page uses those three names. Chapter order still follows the dependencies.

| Subtitle word | Where it is visible |
| --- | --- |
| Proof | Part I. What a sentence promises, induction, and counting arguments that are proofs. |
| Mathematical thinking | Part II. Limits, complex numbers, polynomials, linear algebra, calculus, inequalities, and first probability, each rebuilt as a way of thinking rather than a list of formulas. |
| Problem solving | The workshop section of every chapter, named in the contents under Part III, and the field guide. The workshops stay inside their chapters so the tool and the problem are not torn apart. |

No teaching chapter fails the title. Image credits stay back matter. They are not a chapter.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Proof | 0–2 |
| II | Mathematical Thinking | 3–9 |
| III | Problem Solving | The workshop in every chapter, and the field guide |

---

The chapter notes follow the manuscript's file order. The contents page uses the three part names in the table above.

### Part I. The Language of Proof

#### Chapter 0. The Language of Mathematics

**Status.** KEEP — `tome0-mathematical-maturity/chapters/ch00-language.tex` (1138 lines). REVISE the closing page so the series question is one sentence: a proof is how a pattern becomes a member of the building, and the primes are where that will be hard.

**Hook.** "The equation \(x^2=1\) has a solution. It has a unique solution. Every real number solves it." Three sentences, one equation, three different promises.

**Synopsis.** Definitions, connectives, quantifiers, sets, functions, relations, and order, then a workshop on whether an image preserves an intersection. The reader learns who chooses what in a quantifier, and that an equivalence relation is a partition. This is the legend on the survey. Nothing later is allowed to use a word this chapter has not fixed, except the foundational contract in the preface.

**Proved.** The inverse criterion. Equivalence relations are partitions.

**Examples.** The three readings of \(x^2=1\). A proof that a direct image need not preserve an intersection, and the extra hypothesis that repairs it.

**Figures.** Two figures. The quantifier diagrams and the image-of-intersection picture are the ones to keep.

### Part II. Counting and Sums

#### Chapter 1. Sums, Binomials and Induction

**Status.** KEEP — `chapters/ch01-sums.tex` (748 lines).

**Hook.** Is it a coincidence that \(1^3+\cdots+n^3=(1+\cdots+n)^2\)? Ten values agree. Agreement is not a structural fact.

**Synopsis.** Sums, three flavours of induction, telescoping, binomial coefficients, and the binomial basis of polynomials. The workshop treats a pattern as a suspect. This is the first course of the masonry: a finite identity, proved for every \(n\), with the induction principle derived from well-ordering rather than assumed as a mood.

**Proved.** Newton's forward-difference formula. The binomial theorem in the form the later floors quote. The closed form for the sum of cubes, by more than one route, so the reader sees that one fact can have several members.

**Examples.** The sum of cubes. A false pattern that fails at a named \(n\), so the workshop is not only a sermon.

**Figures.** Seven. The binomial triangle and the telescoping picture.

#### Chapter 2. Counting and Discrete Reasoning

**Status.** KEEP — `chapters/ch02-counting.tex` (439 lines).

**Hook.** How many ways can every guest receive the wrong hat? The difficulty is to count overlapping restrictions once.

**Synopsis.** Counting from scratch, lattice paths, and a first generating function. Inclusion–exclusion is the load-bearing tool. The derangement count plants the deck of cards: Book 4 will shuffle it, Abstraction will prove the cutoff, Book 15 will keep the Bayer–Diaconis profile. The chapter does not say that. The field guide may.

**Proved.** Inclusion–exclusion. The derangement probability's exact formula, with the limit \(1/e\) deferred until the sequences chapter has a limit.

**Examples.** Derangements. A lattice-path count that removes a restriction by changing the objects.

**Figures.** Four.

### Chapters 3–7, in file order

#### Chapter 3. Sequences, Series and Limits

**Status.** KEEP — `chapters/ch05-sequences-series.tex` (1012 lines). The filename says `ch05`; the book numbers it as Chapter 3. Leave the file name. REVISE nothing mathematical.

**Hook.** \(1-\frac12+\frac13-\frac14+\cdots=\log 2\). Rearrange the same terms and the sum changes. Infinite sums are not finite sums with dots.

**Synopsis.** Limits from completeness, sequences, continuity and a short derivative toolkit, series, and summation by parts. The workshop is a limit with an explicit rate. This is where the survey learns to pass to infinity without pretending the infinite object was finite. Stirling's first form appears here and is completed in the calculus chapter.

**Proved.** Cesàro means. Intermediate values, extreme values, Heine's uniform continuity, Rolle, and the mean value theorem, from completeness, as the preface promises. Dirichlet's test. A first Stirling approximation.

**Examples.** The alternating harmonic series and a rearrangement. A limit whose error is exhibited, not merely said to be small.

**Figures.** Seven.

#### Chapter 4. Complex Numbers and Roots of Unity

**Status.** KEEP — `chapters/ch02-complex-roots.tex` (712 lines).

**Hook.** Why is \((\sqrt2+i\sqrt2)^2\) a real multiple of \(i\), and why do certain integers factor on the unit circle? Both answers live there.

**Synopsis.** Complex numbers from scratch, the exponential form, roots of unity, the filter, a little geometry, and cyclotomic polynomials. The roots-of-unity filter is the first symmetry in the building: a sum over all characters kills every term but one. Book 2's second proof of reciprocity and Book 6's Dirichlet characters stand on this chapter.

**Proved.** The roots-of-unity filter. De Moivre. The cyclotomic polynomials' integrality and irreducibility over \(\mathbb Q\) at the level this book claims; the Galois group is Book 3's.

**Examples.** A filter extracting every third binomial coefficient. One cyclotomic factorisation written in full.

**Figures.** Eight.

#### Chapter 5. Polynomials

**Status.** KEEP — `chapters/ch03-polynomials.tex` (943 lines).

**Hook.** Among monic polynomials of degree \(n\), which stays closest to zero on \([-1,1]\)? And how can the roots of one polynomial compute a power sum?

**Synopsis.** Division, roots, multiplicities, Lagrange interpolation, Chebyshev polynomials, integer polynomials, symmetric functions, and Descartes' rule. The fundamental theorem of algebra is proved in the book's real-and-complex setting. Eisenstein's criterion is the tool Book 2 and Book 3 quote. Interpolation is the workshop's warning: a polynomial that fits \(n\) points is not a prophecy.

**Proved.** d'Alembert–Gauss. Lagrange interpolation. Eisenstein. The fundamental theorem on symmetric polynomials. Descartes' rule of signs. Gauss–Lucas.

**Examples.** The monic polynomial of smallest maximum norm on \([-1,1]\), identified as a Chebyshev polynomial. An interpolation that fits and then fails off the nodes.

**Figures.** Eight.

#### Chapter 6. Linear Algebra

**Status.** KEEP — `chapters/ch07-linear-algebra.tex` (868 lines). This is the first-course spectral theorem. Book 3's appendices own Cauchy–Binet, SVD, Perron–Frobenius, and the combinatorial method. The two do not silently reprove each other: one sentence at the end of this chapter names the appendices as the specialist floor.

**Hook.** Why is \(F_{n+1}F_{n-1}-F_n^2\) always \(\pm 1\)? Why is the Hilbert determinant positive and tiny? Matrices answer questions that do not mention matrices.

**Synopsis.** Vector spaces, determinants, reduction, inner products, the spectral theorem for real symmetric matrices, determinants as volumes, the adjugate, and Cayley–Hamilton. The workshop is least squares with the geometry left in. Book 2's norm matrices and Book 3's modules over a PID both need this chapter, at different depths.

**Proved.** The determinant characterisation used later. Diagonalisability criteria. Gram–Schmidt and orthogonal projection. The spectral theorem. The Gram determinant. Cayley–Hamilton.

**Examples.** The Cassini identity for Fibonacci numbers, read off a matrix. Least squares on a small inconsistent system.

**Figures.** Seven.

#### Chapter 7. Differential and Integral Calculus

**Status.** KEEP — `chapters/ch06-integrals-taylor.tex` (798 lines).

**Hook.** Wallis's product for \(\pi\), and \(\int_0^\infty e^{-x^2}\,\mathrm dx=\sqrt\pi/2\). Both come out of one family of integrals, which also completes Stirling.

**Synopsis.** The rules of differentiation, with proofs, now that the mean value theorem exists. Antiderivatives, Wallis integrals, l'Hôpital, a first Gamma integral, numerical integration, and the next term of Stirling. The Gaussian integral is planted as a number. Book 4 will explain it as the law of a sum. Book 5 will build the Gamma function properly and will not pretend this chapter did.

**Proved.** Taylor's theorem with a remainder the reader can bound. l'Hôpital. Stirling's constant, completed. The Wallis product.

**Examples.** A Taylor polynomial whose remainder is smaller than a named tolerance. One numerical integral compared with its error bound.

**Figures.** Six.

### Part IV. Chance and Inequality

#### Chapter 8. Inequalities, Convexity and Estimates

**Status.** KEEP — `chapters/ch04-inequalities.tex` (712 lines).

**Hook.** The number \(e\) appears in an inequality about averages of an arbitrary positive sequence. Why there, and why is the constant best possible?

**Synopsis.** Inequalities from scratch, Jensen, Cauchy–Schwarz, Hölder, means and norms. A bridge records that convexity selects the factorial interpolation, which is why Book 5's Bohr–Mollerup theorem will look inevitable. The workshop asks the reader to measure the slack, not only to name the inequality. Carleman's inequality may stay a remark if the constant \(e\) is only numerical; the October errata already says so.

**Proved.** Jensen. AM–GM. Cauchy–Schwarz. Power means. Minkowski's inequality.

**Examples.** A Cauchy–Schwarz estimate with the equality case exhibited. The convexity argument that picks the Gamma interpolation, one page, pointing forward.

**Figures.** Six.

#### Chapter 9. First Probability

**Status.** KEEP — `chapters/ch09-probability.tex` (876 lines). REVISE the last page. The hat check tends to \(1/e\). The sum of cubes was a structural identity. The reader can now say what each sentence proved. The next floor asks the same question of the primes, and this book does not answer it.

**Hook.** \(n\) guests collect their hats at random. The probability that nobody gets their own hat tends to \(1/e\), whether one is told \(n=10\) or \(n=10^6\).

**Synopsis.** Finite probability, variance, a controlled step past finite sample spaces, and a first weak law. This is the load of uncertainty in its smallest form: Chebyshev's inequality, not Lindeberg's theorem. Book 4 owns the central limit theorem. The chapter must not gesture at it as if it had been proved.

**Proved.** Markov and Chebyshev. The weak law of large numbers for independent random variables with a uniform variance bound, in the finite or elementary setting the chapter actually builds.

**Examples.** The hat check, with the exact derangement count from Chapter 2 and the limit from Chapter 3. A coin-toss average inside Chebyshev's band.

**Figures.** Five.

### Back matter

**A field guide to the next problem.** KEEP — `chapters/field-guide.tex` (106 lines). REVISE so it names the series question and the next floor, in the voice of a method (what to try when a problem looks unfamiliar), not as a table of contents of later books.

**Image credits.** KEEP — `chapters/image-credits.tex`.

## Crossroads problems that belong here

From `tomeP1-crossroads`. Journeys and a short set only.

| Source | What moves | Home |
| --- | --- | --- |
| `chapters/ch02-roots.tex` | Problems that use only the roots-of-unity filter and cyclotomic factorisations | End of Part III, after Chapter 4 |
| `chapters/ch08-inequalities.tex` | The Journey "Shearer's lemma and the Loomis–Whitney inequality", if its tools are Book 1's inequalities and counting; otherwise it waits for Book 4's entropy | End of Part IV |
| `chapters/ch01-two-tomes.tex` | The problems whose tools are only this book | Scattered as extra exercises, not a new chapter |

The Journey "Eisenstein's trigonometric proof of quadratic reciprocity" is Book 2's, not this book's. It uses the roots of unity and then leaves.

## Owns, defers, hands forward

**Owns.** The language of proof. Induction and the binomial theorem. Inclusion–exclusion and derangements. Completeness and the elementary calculus that follows from it. Complex numbers and the roots-of-unity filter. Polynomials through Eisenstein and the fundamental theorem of algebra. The first-course spectral theorem. Finite probability and Chebyshev's weak law.

**Defers.** The primes, as a theory. The central limit theorem. Lebesgue measure. Group theory. The Gamma function as Bohr–Mollerup. Zeta.

**Hands forward.** A reader who can test a proof, sum a series, factor a cyclotomic, diagonalise a symmetric matrix, and estimate a variance. The field guide points at Book 2.

## Pages and effort

Baseline 295 print pages. Target 310–340 after a short Crossroads set. Effort: light. The reconstruction is the chapter list. The rework is the preface paragraph, the last page of Chapter 9, the field guide, and the part title.
