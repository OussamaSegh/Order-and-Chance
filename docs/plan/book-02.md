# Book 2 — The Integers

*Primes, Patterns and Proofs.*

**Element.** The masonry. The bricks look irregular. The courses lock.

**Source.** `tome2-integers`. Fourteen chapters in `main.tex`, in this order: divisibility, primes, congruences, primitive roots, quadratic reciprocity, arithmetic functions, sums of squares, continued fractions, Diophantine equations, Gaussian and Eisenstein integers, quadratic fields, ideals, \(p\)-adic numbers, characters. The October reconstruction measured 189 print pages through the field guide; `ch14-characters.tex` (520 lines) is in the book now, so the live source is longer. `chapters/preface.tex` already describes the fourteen-chapter route.

## Promise

The reader meets the primes as objects a child can define and nobody can list, and then watches them obey laws: Euclid, Chebyshev, Bertrand, reciprocity. The same floor shows the first concealed room. In \(\mathbb Z[\sqrt{-5}]\) the equation \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\) breaks unique factorisation, and ideals restore it for that ring. Characters and Legendre's sieve are the door into Book 6. Dirichlet's theorem is not proved here.

## Prerequisites

Book 1 entire: proof, induction, binomial coefficients, complex numbers, Eisenstein, the spectral theorem for symmetric matrices, integral comparison, and finite probability for the bridge exercises. No abstract algebra course. Groups, rings, and ideals are explained at the size this book uses them. Book 3 will make them a theory.

## How the subtitle is delivered

The parts keep their catalog names. *Primes, Patterns and Proofs* is what they do.

Divisibility and The Primes are the primes: Euclid, Chebyshev, and Bertrand, proved. Congruences is the modular pattern and its proofs, through primitive roots, reciprocity proved twice, and arithmetic functions. Equations, Ideals and Characters runs from sums of squares through the characters chapter. Those chapters deliver the patterns: which integers are sums of squares, which rationals come from continued fractions, which equations die by descent, and the characters that close the book. The proofs are the standard of every part.

Three chapters now filed in that last block do not deliver this subtitle. Quadratic fields, the class group, and the \(p\)-adic field move to Book 13. Book 2 keeps Pell's equation, the Gaussian and Eisenstein integers, and one section on \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). Hensel's lemma for a congruence stays in Congruences.

## Proposed part-name change

**Equations, Ideals and Characters** becomes **Equations and Characters**. After the move, "Ideals" would name a chapter that is no longer in the part.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Divisibility | 1 |
| II | The Primes | 2 |
| III | Congruences | 3–6 |
| IV | Equations, Ideals and Characters | 7–10 and 14. Chapters 11–13 move. See the proposed rename above. |

---

The chapter notes follow the manuscript's file order, including the three chapters that move. The part names are the table above.

### Part I. Divisibility

#### Chapter 1. Divisibility and the Euclidean Algorithm

**Status.** KEEP — `tome2-integers/chapters/ch01-divisibility.tex` (418 lines).

**Hook.** Euclid's algorithm is still in daily use. Its worst case is a pair of consecutive Fibonacci numbers.

**Synopsis.** Division, the ideals of \(\mathbb Z\) as a first look rather than a theory, and the Euclidean algorithm with its Fibonacci bound. Bézout's identity is the tool every later congruence stands on. The word "ideal" is used here only for subgroups of \(\mathbb Z\), with a sentence that Book 3 and Chapter 12 of this book will mean something larger.

**Proved.** The division algorithm. Bézout. Euclid's lemma. The Fibonacci bound on the number of steps.

**Examples.** One Euclidean algorithm run to the end, with the Bézout coefficients kept. The worst-case pair.

**Figures.** Three.

### Part II. The Primes

#### Chapter 2. Primes

**Status.** KEEP — `chapters/ch02-primes.tex` (423 lines). This is the character's entrance. REVISE the last paragraph so the series question is explicit: infinitude is a law, the list still looks like rubble, and the rest of the series is about which impression is right at which scale.

**Hook.** There is always a prime between \(n\) and \(2n\). Chebyshev proved a stronger estimate in 1852. The proof here is Erdős's, and it uses binomial coefficients.

**Synopsis.** Euclid's infinitude, Chebyshev's bounds, and Bertrand's postulate. The prime number theorem is named as a destination, not proved. The October errata already corrected the small-\(n\) step in Bertrand's argument. Chebyshev's \(\theta\) appears; the letter is flagged because Book 5 uses \(\theta\) for a Jacobi theta and Book 6 takes \(\theta\) back.

**Proved.** Infinitely many primes. Chebyshev's upper and lower bounds of the strength the chapter states. Bertrand's postulate.

**Examples.** Euclid's proof written so the constructed number is computed for a small start. One binomial-coefficient estimate in Erdős's proof, with the inequality on the page.

**Figures.** Three.

### Part III. Congruences

#### Chapter 3. Congruences

**Status.** KEEP — `chapters/ch03-congruences.tex` (422 lines).

**Hook.** The last two digits of a power tower of \(3\)s, a number with more than \(3\cdot 10^{12}\) digits. Arithmetic modulo \(100\) answers in a few lines.

**Synopsis.** The ring \(\mathbb Z/n\mathbb Z\), the Chinese remainder theorem, and Hensel's lemma in its first form, lifting a simple root modulo a prime. Wilson's theorem and Fermat's little theorem sit here. Euler's theorem waits for the next chapter if the manuscript puts \(\varphi\) with the units; either way \(\varphi\) is defined before it is used, in a sentence a later book can quote.

**Proved.** The Chinese remainder theorem. Fermat and Wilson. Lifting a simple root modulo \(p\) to modulo \(p^k\).

**Examples.** The power tower of \(3\)s. A simultaneous system solved by the Chinese remainder theorem, with the moduli not prime.

**Figures.** Three.

#### Chapter 4. Primitive Roots and the Multiplicative Group

**Status.** KEEP — `chapters/ch05-primitive-roots.tex` (482 lines).

**Hook.** The decimal of \(1/7\) repeats every \(6\) digits, and \(1/17\) every \(16\). Why do some primes give the longest period \(p-1\)?

**Synopsis.** Orders, the theorem that \((\mathbb Z/p\mathbb Z)^\times\) is cyclic, the moduli for which \((\mathbb Z/n\mathbb Z)^\times\) is cyclic, discrete logarithms, and the structure of the units modulo a power of \(2\). This is the first time a residue ring is a group in the sense Book 3 will define. The chapter should use the word and point forward, not develop Sylow theory.

**Proved.** Existence of a primitive root modulo an odd prime. The classification of \(n\) for which \((\mathbb Z/n\mathbb Z)^\times\) is cyclic. The structure modulo \(2^k\).

**Examples.** A primitive root modulo a small prime, used to compute a power. One modulus where the group is not cyclic, with the invariant factors exhibited.

**Figures.** Three.

#### Chapter 5. Quadratic Residues and Reciprocity

**Status.** KEEP — `chapters/ch06-quadratic-reciprocity.tex` (537 lines). This is the climax of the floor.

**Hook.** Is \(219\) a square modulo the prime \(383\)? A search might square \(191\) residues. Reciprocity answers in four lines. Gauss called it the golden theorem.

**Synopsis.** Euler's criterion, Gauss's lemma, the law of quadratic reciprocity, and the Jacobi symbol. Two proofs, as the preface promises, exposing two structures: one elementary, one through roots of unity and a cyclotomic. The second proof is why Book 1's complex numbers are load-bearing. The Jacobi symbol is the computational form, and the chapter says it is not a character until the next definition, in Chapter 14, makes characters.

**Proved.** Euler's criterion. Gauss's lemma. The law of quadratic reciprocity, including the supplementary laws. The Jacobi symbol's multiplicativity.

**Examples.** The residue of \(219\) modulo \(383\), in the four lines the hook promises. One supplementary law used on a real example where the odd prime alone would have lied.

**Figures.** Three.

### Part IV. Patterns

#### Chapter 6. Arithmetic Functions

**Status.** KEEP — `chapters/ch04-arithmetic-functions.tex` (500 lines).

**Hook.** Two integers chosen "at random" are coprime with probability \(6/\pi^2\). The proof is one inversion. Zeta is not built yet; the Euler product of \(\zeta(2)\) is allowed as the Basel sum from Book 1's horizon, or the identity is stated with the product written out and the evaluation of \(\sum 1/n^2\) cited to Book 5 if this book does not prove it.

**Synopsis.** Multiplicative functions, Dirichlet convolution, Möbius inversion, perfect numbers, and average orders. The probability \(6/\pi^2\) is zeta's shadow: the function is not named as an analytic object. Möbius inversion is the tool Legendre's sieve, in Chapter 14, will use. The preface's bridge exercises on random divisibility live naturally beside this chapter.

**Proved.** Möbius inversion. The Euler product for the proportion of coprime pairs, at the level of formal products or absolutely convergent series the chapter actually justifies. The average order of \(d(n)\) or of \(\sigma\), whichever the file proves.

**Examples.** \(\varphi\), \(\mu\), and \(d\) on a factored integer. One convolution inverted by hand.

**Figures.** Three.

#### Chapter 7. Sums of Squares

**Status.** KEEP — `chapters/ch07-sums-of-squares.tex` (354 lines). The three-square theorem stays admitted, with the triangular-number exercise labelled as such. Book 13 proves three squares. The preface already says this.

**Hook.** \(2026=1^2+45^2\), \(2027\) is not a sum of two squares, and every non-negative integer is a sum of four.

**Synopsis.** The two-square theorem, Lagrange's four-square theorem, and the lattice-point discrepancy of a disc as a first geometry-of-numbers picture. Fermat's theorem on sums of two squares is the pattern. The Gaussian integers in Chapter 10 will give it a second proof; this chapter's proof should remain the elementary one, so the return is visible.

**Proved.** An integer is a sum of two squares if and only if every prime \(3\pmod 4\) has even exponent. Lagrange's four-square theorem. A lattice-point error of the strength the chapter states.

**Examples.** \(2026\) and \(2027\). The identity that multiplies sums of four squares, used in the descent.

**Figures.** Three.

#### Chapter 8. Continued Fractions and Pell's Equation

**Status.** KEEP — `chapters/ch08-continued-fractions.tex` (468 lines). Hurwitz's theorem stays a stated idea with a pointer, as the October errata decided. Book 9 returns to continued fractions as cutting sequences. Book 11 returns to them as the Gauss map.

**Hook.** \(\sqrt 2=1+1/(2+1/(2+\cdots))\), and the calendar's leap years come from the expansion of \(0.24219\).

**Synopsis.** Finite continued fractions, the expansion of a real number, best approximations, periodic expansions, and Pell's equation. Existence of a non-trivial solution of \(x^2-dy^2=1\) is proved. The fundamental unit of a real quadratic field in Chapter 11 cites it. The calendar computation's error term was corrected in the errata and should stay corrected.

**Proved.** Best approximations. Periodicity for quadratic irrationals. Existence of a positive solution of Pell's equation. The continued fraction of a rational is the Euclidean algorithm.

**Examples.** \(\sqrt 2\), and one Pell equation whose fundamental solution is large enough to be surprising and small enough to compute, or \(d=61\) stated with its solution checked rather than derived digit by digit if the chapter already does that.

**Figures.** Four.

#### Chapter 9. Diophantine Equations

**Status.** KEEP — `chapters/ch09-diophantine.tex` (517 lines). The chord method's hypothesis (no linear factor) is the repaired form.

**Hook.** \(3^2+4^2=5^2\), but \(x^4+y^4=z^4\) has no solution, and neither does \(y^2=x^3+7\).

**Synopsis.** Obstructions before constructions, Pythagorean triples, infinite descent, the chord method for conics, factoring with a sum of squares, and Vieta jumping. Descent is the method Book 13's Fermat chapter will use in cyclotomic fields. This chapter owns the elementary descents. It does not own Fermat's last theorem.

**Proved.** The classification of primitive Pythagorean triples. Fermat's theorem that \(x^4+y^4=z^4\) has no positive solution. The chord method under the hypothesis that makes it true. At least one Vieta-jumping argument written in full.

**Examples.** A Pythagorean triple generated from a pair. One equation killed by a congruence, before any descent is attempted.

**Figures.** Three.

### Part V. First enlargements

These four chapters are the first time the masonry opens. A page at the head of Chapter 10 says what Book 13 will generalise, so the duplication is a return and not an accident.

#### Chapter 10. Gaussian and Eisenstein Integers

**Status.** KEEP — `chapters/ch10-gaussian-eisenstein.tex` (495 lines).

**Hook.** In \(\mathbb Z[i]\), \(5=(2+i)(2-i)\), \(3\) stays prime, and \(2=-i(1+i)^2\). That sentence is the two-square theorem again.

**Synopsis.** Three rings and their norms, unique factorisation, Gaussian primes, and the Eisenstein integers with Fermat's last theorem for cubes. The second proof of the two-square theorem is the point: the elementary theorem of Chapter 7 returns as a splitting law. Unique factorisation still holds here. The next chapters are what happens when it does not.

**Proved.** \(\mathbb Z[i]\) and \(\mathbb Z[\omega]\) are Euclidean, hence UFDs. The classification of Gaussian primes. Fermat's last theorem for exponent \(3\), by Eisenstein descent, if the file's proof is the one the preface claims; otherwise the chapter keeps the descent it actually finishes and does not advertise the other.

**Examples.** The factorisation of a small integer in \(\mathbb Z[i]\). One cube descent written with the norm.

**Figures.** Three.

#### Chapter 11. Quadratic Fields and Their Integers

**Status.** MOVE — `chapters/ch11-algebraic.tex` (358 lines), to Book 13, Chapter 1. The description of \(\mathcal O_K\), the embeddings, and the units beyond Pell's equation are hidden worlds, not a pattern in \(\mathbb Z\). Pell stays in Chapter 8.

**Hook.** The golden ratio is a root of a monic integer polynomial and has a denominator \(2\). Which fractions deserve to be called integers?

**Synopsis.** The ring of integers of a quadratic field, units, and the two embeddings. The norm matrix uses Book 1's determinant. This is a single room, fully furnished, not the wing.

**Proved.** The description of \(\mathcal O_K\) for \(K=\mathbb Q(\sqrt d)\). The relation between units and Pell's equation. The norm and trace identities the exercises use.

**Examples.** \(\mathbb Q(\sqrt 5)\) and \(\mathbb Q(\sqrt{-5})\), side by side, so the next chapter's failure has somewhere to stand.

**Figures.** Two.

#### Chapter 12. Ideals, Prime Splitting and Class Groups

**Status.** MOVE — `chapters/ch12-ideals.tex` (641 lines), to Book 13, Chapters 2–3. A full class group does not deliver *Primes, Patterns and Proofs*. Book 2 keeps the display \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\) as one section after the Gaussian integers, and points to Book 13 for the repair.

**Hook.** In \(\mathbb Z[\sqrt{-5}]\), \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). None of the four factors further. Kummer's answer was to invent the missing factors.

**Synopsis.** Ideal numbers, unique factorisation of ideals in the quadratic case the chapter proves, splitting of a rational prime, ideal arithmetic, the class group of a quadratic order or field as the chapter defines it, and a short bridge to binary quadratic forms. Finiteness of the class group in general is Book 13's Minkowski argument. If this chapter proves finiteness only for imaginary quadratic fields by a reduced-form argument, that is the right scope, and the heading should say so.

**Proved.** Unique factorisation of ideals in the rings the chapter treats. The splitting law for odd primes not dividing the conductor, in the quadratic case. The class group as a group, and at least one class number computed by hand (\(h(-5)=2\), or whichever example the file finishes).

**Examples.** The two factorisations of \(6\). A prime that splits, a prime that stays inert, a prime that ramifies, in one field.

**Figures.** Four.

#### Chapter 13. The \(p\)-adic Numbers

**Status.** MOVE — `chapters/ch12-padic.tex` (663 lines), to Book 13, Chapter 6. Ostrowski's theorem and the field \(\mathbb Q_p\) are a hidden world. They do not deliver the subtitle. The congruence form of Hensel's lemma stays in Chapter 3.

**Hook.** In the \(2\)-adic world, \(1+2+4+8+\cdots=-1\), and \(-7\) has a square root.

**Synopsis.** The \(p\)-adic absolute value, the \(p\)-adic integers, Hensel's lemma as Newton's method, Ostrowski's theorem, and a first local-global sentence. Ostrowski is the structural fact: the absolute values of \(\mathbb Q\) are the real one and the \(p\)-adic ones, up to equivalence. The Hasse–Minkowski theorem is named and not proved.

**Proved.** Completeness of \(\mathbb Q_p\). Hensel's lemma for a simple root. Ostrowski's theorem. A square-root computation in \(\mathbb Z_2\) or \(\mathbb Z_7\) of the kind the hook states.

**Examples.** The series for \(-1\). One Hensel lift from a small residue to a named precision.

**Figures.** Four.

### Part VI. Characters and Sieves

#### Chapter 14. Characters, Euler Products and the Sieve

**Status.** KEEP — `chapters/ch14-characters.tex` (520 lines). This is the cliffhanger. REVISE only the last page: Dirichlet's theorem is the first theorem of Book 6's counting, and the sieve here is Legendre's, which Book 6 will show fails for the prime number theorem and then repair.

**Hook.** Euler factored the harmonic series into a product over primes. The same idea, with a sign that remembers a residue class, is the door to Dirichlet's theorem.

**Synopsis.** Dirichlet characters as homomorphisms of \((\mathbb Z/m\mathbb Z)^\times\), orthogonality, Euler products, and Legendre's formula for the sifted count. The Legendre symbol is recovered as a character. One series sits at the boundary of convergence, so the reader feels why Book 5 and Book 6 have to be analytic. The chapter uses the structure of the unit group from Chapter 4 and the convolution algebra from Chapter 6.

**Proved.** Orthogonality of Dirichlet characters. The Euler product for \(L(s,\chi)\) in the region of absolute convergence. Legendre's exact sieve identity, and the estimate that shows why truncating it is not yet a prime-number theorem.

**Examples.** The three characters the reader already knows: the principal character, \(\chi_4\), and the Legendre symbol. One sifted count computed both ways for a small \(x\) and a small \(z\).

**Figures.** Three.

### Back matter

**An arithmetic field guide.** KEEP — `chapters/field-guide.tex` (112 lines). It collects notation and proof strategies. REVISE the notation paragraphs to match the series sheet in `SERIES-CONTENT-PLAN.md` at the letters this book introduces: \(\varphi\), \(\left(\frac{\cdot}{p}\right)\), \(\mu\), and the first \(\theta\).

## The old problem book

Book 6 is Crossroads, the analytic volume. The old P1 problem book is removed by the renumbering branch, which appends its problems to Books 1–6. This plan does not place them again. A problem that cites a chapter moved here follows that chapter.

## Owns, defers, hands forward

**Owns.** Euclid, Chebyshev, Bertrand. Congruences, primitive roots, quadratic reciprocity. Arithmetic functions and Möbius inversion. Two squares and four squares. Continued fractions and Pell. Elementary descent. \(\mathbb Z[i]\), \(\mathbb Z[\omega]\), quadratic integers, quadratic ideals and one class group, \(\mathbb Q_p\), Ostrowski. Dirichlet characters and Legendre's sieve.

**Defers.** The prime number theorem, Dirichlet's theorem, the functional equation, three squares, the general unit theorem, the general class-number formula, Hasse–Minkowski, Haar measure on \(\mathbb Q_p\).

**Hands forward.** A reader who can compute a reciprocity symbol, factor an ideal in \(\mathbb Z[\sqrt{-5}]\), expand a quadratic irrational, and write a character sum. Book 3 takes the word "group". Book 6 takes the characters and the sieve.

## Pages and effort

Baseline about 190 pages through the field guide, plus the characters chapter. Target 230–270. Effort: moderate, and almost all of it is framing. The proofs stay. The added pages are the part openings, the page at the head of Chapter 10, and a handful of Crossroads problems.
