# Book 13 — Arithmetic

*From Equations to Hidden Worlds.*

**Element.** The concealed storeys. When unique factorisation fails, the rooms that were already inside the integers.

**Source.** `volume13-arithmetic` (this directory name becomes valid once step 2 in [PROGRESS.md](PROGRESS.md) merges). Fourteen chapters, about 248 pages. The October review scored it 8. The three-squares test now requires \(n=4^am\) with \(4\nmid m\), in `ch07-hasse.tex`. The preface already narrows "every result is proved" to exclude the remarks: Mazur, modularity, Sato–Tate, Weil for a general curve, and the second case of regular Fermat. The functional equation of \(\zeta_K\) for a general field is a sketch. Artin reciprocity and the existence theorem are admitted in their headings.

## Promise

In \(\mathbb Z[\sqrt{-5}]\) the number 6 factors in two ways. Book 2 repaired that one ring. This floor opens the wing: number fields, the geometry of numbers, units, cyclotomic fields and the first case of Fermat for regular primes, local fields, the Hasse–Minkowski theorem, zeta functions of number fields, Tate's thesis for \(\mathbb Q\), class field theory with Kronecker–Weber proved and Artin reciprocity admitted, algebraic curves, elliptic curves through Mordell–Weil, curves over finite fields through Hasse's bound, and modular forms. Tate's thesis is the third construction of the functional equation, from Poisson summation on the adèles. The statistical questions, whether a class group is random and whether the average rank is \(\tfrac12\), are handed to Book 15 unproved.

## Prerequisites

Book 2's quadratic examples, as examples, not as the general theorems. Book 3's Galois theory and Dedekind's language. Abstraction's axioms for Dedekind domains; this book proves the number-field case itself and does not quote the unfinished cubic class-group sentence. Book 8's Haar measure and adèles. Book 6's large sieve, Theorem 8.8, and the value of \(L(1,\chi)\). Book 9's picture of a cubic, not its unfinished group law.

## How the subtitle is delivered

The subtitle is a motion: from equations to hidden worlds. Every chapter starts with an equation and opens a room that was not visible in \(\mathbb Z\).

| Chapter | Equation | Hidden world |
| --- | --- | --- |
| 1–2 | A polynomial | The integers of a field, and the ideals that factor uniquely |
| 3–4 | A convex body, Pell's equation | The class group and the unit lattice |
| 5 | \(x^n+y^n=z^n\) | Cyclotomic fields |
| 6–7 | A quadratic form | The \(p\)-adic fields, and the local-global principle |
| 8–10 | A zeta function, an \(L\)-function | Densities, the adèles, and class field theory |
| 11–14 | A cubic, a modular form | Curves, ranks, and the form that counts their points |

The four catalog parts are that motion. Number Fields opens the polynomial. Local and Global opens the places. Adèles and Tate's Thesis opens the functional equation a third time. Elliptic Curves and Modular Forms opens the curve and the form that counts its points. No part is renamed.

**Receives.** Book 2's chapters on quadratic fields, ideals, and the \(p\)-adic numbers. Book 8's construction of the adèles, beyond the Haar measure Book 8 keeps. No chapter of this book fails the subtitle. Artin reciprocity stays admitted inside class field theory. It is part of the hidden world, and the heading says it is not proved.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Number Fields | 1–5 |
| II | Local and Global | 6–8 |
| III | Adèles and Tate's Thesis | 9–10 |
| IV | Elliptic Curves and Modular Forms | 11–14 |

---

### Part I. Number Fields

#### Chapter 1. Number Fields and Their Integers

**Status.** KEEP — `volume13-arithmetic/chapters/ch01-number-fields.tex` (793 lines). The discriminant of \(\mathbb Q(\sqrt 2)\) is a figure in this chapter, not Theorem 2.15. Book 14's citation, if it still says Theorem 2.15 for the value 8, points here.

**Hook.** Is \(\mathbb Z[\sqrt 2]\) the full ring of integers of \(\mathbb Q(\sqrt 2)\)? Is \(\mathbb Z[\sqrt{10}]\) the full ring of \(\mathbb Q(\sqrt{10})\)? One answer is yes and the other is no.

**Synopsis.** Embeddings, algebraic integers, norm, trace, discriminant, integral bases, and Stickelberger's theorem. Book 2 computed \(\mathcal O_K\) for quadratic fields. This chapter is the general construction. The quadratic case returns as the first example, named as a return.

**Proved.** The ring of integers is a free \(\mathbb Z\)-module of rank \(n\). The discriminant of a basis, and the relation between bases. Stickelberger's congruence, if the file proves it.

**Examples.** \(\mathbb Q(\sqrt 2)\) and \(\mathbb Q(\sqrt{10})\). One integral basis computed from a polynomial.

**Figures.** Two.

#### Chapter 2. Ideals and the Splitting of Primes

**Status.** KEEP — `chapters/ch02-ideals.tex` (878 lines).

**Hook.** In \(\mathbb Z[\zeta_7]\), the prime 7 becomes a sixth power, 29 breaks into six prime ideals, and 2 into two.

**Synopsis.** Unique factorisation of ideals in \(\mathcal O_K\), the norm of an ideal, Kummer–Dedekind, ramification and the discriminant, and decomposition, inertia, and Frobenius in a Galois extension. Abstraction axiomatised Dedekind domains. This chapter proves that \(\mathcal O_K\) is one. The splitting law is the concealed storey's floor plan: a polynomial modulo \(p\) shows how \(p\) breaks.

**Proved.** Unique factorisation of nonzero ideals. Kummer–Dedekind. \(p\) ramifies if and only if \(p\) divides the discriminant. The Frobenius element, and Dedekind's theorem on factoring the Galois group from a polynomial.

**Examples.** The three primes in the hook. \(\mathbb Q(\sqrt 2)\), discriminant 8, as a figure of this chapter or of Chapter 1, not as Theorem 2.15.

**Figures.** Two.

#### Chapter 3. The Geometry of Numbers

**Status.** KEEP — `chapters/ch03-geometry.tex` (548 lines). Minkowski's theorem returns from Book 9's lattice appendix. The citation says so. This chapter owns the embedding of \(\mathcal O_K\) and the finiteness of the class group.

**Hook.** A convex body in the plane, symmetric about the origin, of area greater than 4, contains a nonzero lattice point.

**Synopsis.** Lattices, Minkowski's theorem, the Minkowski embedding, the finiteness of the class group, and the Minkowski bound. The class group Book 2 computed for one quadratic field is finite for every number field. That is the theorem.

**Proved.** Minkowski's convex-body theorem. Finiteness of the class group. The Minkowski bound of the strength the file gives.

**Examples.** A class number computed from the bound, \(\mathbb Q(\sqrt{-5})\) again, and one field whose bound is larger than 1 so the computation is real.

**Figures.** Two.

#### Chapter 4. Units

**Status.** KEEP — `chapters/ch04-units.tex` (424 lines). Dirichlet's unit theorem is proved here, and again from Fujisaki in Chapter 9. The second proof is a return, and Chapter 9 should say so.

**Hook.** The smallest positive solution of \(x^2-61y^2=1\) has ten digits. Why must there be one at all?

**Synopsis.** Roots of unity, the logarithmic embedding, Dirichlet's unit theorem, the regulator, and the search for fundamental units. Book 2 proved Pell's equation. This chapter is the general unit theorem: the unit group has rank \(r_1+r_2-1\).

**Proved.** Dirichlet's unit theorem. The structure \(\mathcal O_K^\times\cong\mu\times\mathbb Z^{r_1+r_2-1}\).

**Examples.** A real quadratic unit, from Book 2's continued fraction, recognised as the fundamental unit. One regulator.

**Figures.** One.

#### Chapter 5. Cyclotomic Fields and Fermat

**Status.** KEEP — `chapters/ch05-cyclotomic.tex` (634 lines). The first case of Fermat for regular primes is proved. The second case stays a remark.

**Hook.** Fermat's sentence in the margin: no \(n\)th power is a sum of two \(n\)th powers for \(n>2\). The chapter proves a piece of it, and says which piece.

**Synopsis.** Cyclotomic fields, the prime above \(p\), the ring of integers, Gauss sums and a return of quadratic reciprocity, Kummer's lemma on units, and the first case for regular primes. Regularity is a condition on the class group. The class group, a concealed room, is now carrying Fermat's sentence.

**Proved.** \([\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n)\), matching Book 3. The ring of integers of \(\mathbb Q(\zeta_p)\). The first case of Fermat's last theorem for a regular prime.

**Examples.** The class number of \(\mathbb Q(\zeta_p)\) for a small irregular or regular prime, whichever the chapter computes. One Kummer descent step, written out.

**Figures.** Two.

### Part II. Local and Global

#### Chapter 6. Local Fields

**Status.** KEEP — `chapters/ch06-local.tex` (592 lines). Book 2 built \(\mathbb Q_p\). Book 8 gave it Haar measure. This chapter classifies the finite extensions.

**Hook.** \(\mathbb Q_2\) has seven quadratic extensions. \(\mathbb Q_5\) has three.

**Synopsis.** Absolute values, Hensel's factorisation, ramification index and residue degree, unramified and totally ramified extensions, Krasner's lemma, and the completions of a number field. Every finite extension of \(\mathbb Q_p\) is generated by a root of a polynomial the chapter can describe. The numbers \(e\) and \(f\) return from Chapter 2, now locally.

**Proved.** Existence and uniqueness of the extension of the absolute value. \(ef=n\). The classification of unramified extensions. Krasner's lemma. Finiteness of the number of extensions of a given degree.

**Examples.** The seven quadratic extensions of \(\mathbb Q_2\). One unramified extension, a root of unity.

**Figures.** Two.

#### Chapter 7. Quadratic Forms and the Local–Global Principle

**Status.** KEEP — `chapters/ch07-hasse.tex` (598 lines). The three-squares proof was the review's false conclusion about the integer 28. The source now writes \(n=4^am\) with \(4\nmid m\) before the 2-adic test. A second reading of that paragraph is the only work. Hasse–Minkowski and the Davenport–Cassels lemma checked out. The preface's sentence that the chapter settles sums of three squares is true of the repaired proof.

**Hook.** Does \(2x^2+7y^2=3z^2\) have a nontrivial rational solution? It has real solutions and \(p\)-adic solutions at 3 and at 5. It fails at 2.

**Synopsis.** Quadratic forms, the Hilbert symbol, the product formula, forms over \(\mathbb Q_p\), the Hasse–Minkowski theorem, Legendre's theorem, and three squares. A quadratic equation is solvable over \(\mathbb Q\) exactly when it is solvable over \(\mathbb R\) and over every \(\mathbb Q_p\). Three squares is the application: \(n\) is a sum of three integer squares if and only if it is not of the form \(4^a(8b+7)\). Book 2 admitted this theorem. This chapter owns it.

**Proved.** The Hilbert product formula. Hasse–Minkowski for quadratic forms. The three-squares theorem, with \(m\) odd in the 2-adic test.

**Examples.** The form in the hook, failing at 2. The integer 28, which is \(4\cdot 7\) and is not a sum of three squares, computed both ways so the repaired test is visible. The integer 7 itself.

**Figures.** One.

#### Chapter 8. Zeta Functions and Densities

**Status.** KEEP — `chapters/ch08-zeta.tex` (940 lines). Chebotarev is proved in Dirichlet density. Natural density is explicitly not claimed. That sentence stays.

**Hook.** \(\mathbb Q(\sqrt{-23})\) has class number 3. A series with signs from the squares modulo 23 sums to \(3\pi/\sqrt{23}\), or the multiple the chapter actually displays.

**Synopsis.** The Dedekind zeta function, lattice points in cones, counting ideals, the analytic class-number formula, abelian fields and Dirichlet \(L\)-functions, the class number of \(\mathbb Q(\zeta_p)\), and Chebotarev in Dirichlet density. The class-number formula ties \(h_K\) to a special value. Book 15's Cohen–Lenstra heuristic will say the formula does not determine the proportion of discriminants with \(3\mid h(-d)\). This chapter does not pretend it does.

**Proved.** The class-number formula. Analytic continuation of \(\zeta_K\) to \(\mathrm{Re}\,s>1-1/n\), of the strength the file proves. Chebotarev in Dirichlet density. The class-number formula's special case for an imaginary quadratic field, matching Book 6's Theorem on \(L(1,\chi)\).

**Examples.** \(h(-23)=3\), from the series. One Frobenius density, a splitting type whose density is the size of a conjugacy class.

**Figures.** Two.

### Part III. Adèles and Tate's Thesis

#### Chapter 9. Adèles, Idèles and Tate's Thesis

**Status.** REVISE — `chapters/ch09-tate.tex` (873 lines). Tate's thesis for \(\mathbb Q\), including primitive Dirichlet \(L\)-functions, is proved. The functional equation of \(\zeta_K\) for a general number field is a sketch: Haar measure on each completion, the character \(\psi\circ\mathrm{Tr}\), and Poisson summation on the adèles are not written. Call that paragraph a sketch in its heading. The preface's "Tate derives the functional equation" is true for Riemann's zeta and for Dirichlet \(L\)-functions. Fujisaki's compactness, and the second proof of the unit theorem, name Chapter 4.

**Hook.** Riemann proved the functional equation with Poisson summation. Tate proved it with Poisson summation too, on a larger group.

**Synopsis.** The adèles and idèles of \(\mathbb Q\), Haar measure, characters, Fourier analysis, and Tate's thesis. This is the third time the series builds the functional equation: Book 5 from the theta function, Book 6 as a tool, Book 8's Ikehara as a consequence of a zero-free line, and now Tate as a theorem about Fourier analysis on the adèles. The chapter's introduction counts those constructions so the reader sees one beam, three times.

**Proved.** The functional equation of \(\zeta(s)\) and of \(L(s,\chi)\) for primitive Dirichlet characters, by Tate's method over \(\mathbb Q\). Compactness of the idèle-class group modulo the connected component, or the form Fujisaki's lemma takes in the file. Dirichlet's unit theorem recovered from that compactness, labelled as a second proof.

**Examples.** The local factor at a prime, computed. The completed \(L\)-function of \(\chi_4\), matching Book 6's value at 1.

**Figures.** One.

#### Chapter 10. Class Field Theory

**Status.** KEEP — `chapters/ch10-cft.tex` (707 lines). Artin reciprocity and the existence theorem are admitted in the headings. Kronecker–Weber is proved. That split is the right one, and the preface matches it.

**Hook.** A prime \(p\equiv 1\pmod 3\) can be written \(x^2+27y^2\) exactly when 2 is a cube modulo \(p\). No congruence on \(p\) says this. What kind of law is it?

**Synopsis.** Kronecker–Weber, the statements of Artin reciprocity and the existence theorem, cubic reciprocity and \(x^2+27y^2\), and one page on Langlands. The concealed storey has a law that is not a congruence. The law is stated. The proof that every abelian extension of \(\mathbb Q\) lies in a cyclotomic field is the theorem this book owns. The Hilbert class field is described under the admitted existence theorem, and the heading says "admitted".

**Proved.** Kronecker–Weber. The consequences of the admitted reciprocity law that the chapter derives, including the \(x^2+27y^2\) criterion if it is derived from the admitted statement and not smuggled in as a proof of reciprocity.

**Examples.** The Hilbert class field of \(\mathbb Q(\sqrt{-5})\) and of \(\mathbb Q(\sqrt{-23})\), the exercises the review checked. One prime written as \(x^2+27y^2\), and one that is not.

**Figures.** Two.

### Part IV. Elliptic Curves and Modular Forms

#### Chapter 11. Algebraic Curves

**Status.** KEEP — `chapters/ch11-curves.tex` (752 lines). Book 9's appendix gave Bézout as a picture. This chapter proves it with intersection numbers. The appendix is the drawing; this is the proof.

**Hook.** A line meets a parabola twice, a circle meets a circle twice, a cubic meets a cubic nine times. Except when they do not, until one counts points at infinity and multiplicities.

**Synopsis.** Plane curves, intersection numbers, Bézout, Max Noether's theorem, divisors, Riemann–Roch for smooth plane curves, and codes from curves. Riemann–Roch is the theorem the elliptic group law will use. Genus is a number the reader can compute for a smooth plane curve.

**Proved.** Bézout. Riemann–Roch for smooth plane curves. The genus formula for a smooth plane curve of degree \(d\).

**Examples.** A smooth cubic, genus 1. One Riemann–Roch space, computed.

**Figures.** Two.

#### Chapter 12. Elliptic Curves

**Status.** KEEP — `chapters/ch12-elliptic.tex` (602 lines). The group law is proved here, from Riemann–Roch. Book 9's appendix does not carry it. The canonical height is named and not proved as a quadratic form. The \(n\)-Selmer group is not constructed. The Tate–Shafarevich group is named as the gap between a Selmer bound and the rank. A full 2-descent is given for \(y^2=x^3-x\) and \(y^2=x^3-4x\). Mordell–Weil is proved for \(E(\mathbb Q)\) and stated over a general number field.

**Hook.** The right triangle of sides 3, 4, 5 has area 6. So does a triangle with sides in the hundreds. Where did that come from?

**Synopsis.** The group law, torsion, Nagell–Lutz, Mordell's theorem, and congruent numbers. The rank is finite. The chapter does not determine it. Book 15 will build a 2-Selmer group for one family in this language and will state the average-rank conjectures. It will not reprove Mordell.

**Proved.** The chord-and-tangent group law on a smooth cubic, including the degenerate cases. Nagell–Lutz. Mordell–Weil for \(E(\mathbb Q)\). The 2-descent for the two curves named above.

**Examples.** \(y^2=x^3-x\), its torsion and its rank by the descent. One congruent number.

**Figures.** Two.

#### Chapter 13. Curves over Finite Fields

**Status.** KEEP — `chapters/ch13-finite.tex` (662 lines). Hasse's bound is proved for \(y^m=f(x)\) by Stepanov–Bombieri. Weil's theorem for a general curve is stated. The preface says so.

**Hook.** How many solutions has \(x^3+y^3=1\) modulo \(p\)? About \(p\), give or take \(2\sqrt p\).

**Synopsis.** Frobenius, the zeta function of a curve, counting with characters, Bombieri's upper bound, and the Riemann hypothesis for the curves the method reaches. This is a Riemann hypothesis the series proves, for a special class of curves. The Riemann hypothesis for \(\zeta(s)\) remains open. The two share a name and not a proof, and the chapter says so.

**Proved.** The zeta function of the curves treated. Hasse's bound for \(y^m=f(x)\).

**Examples.** \(x^3+y^3=1\) modulo a small prime, counted and compared with \(p\pm 2\sqrt p\).

**Figures.** Two.

#### Chapter 14. Modular Forms and \(L\)-functions

**Status.** REVISE — `chapters/ch14-modular.tex` (586 lines). Book 6 tasted \(E_4^2=E_8\) and \(\tau(n)\) modulo 691. This chapter owns the valence formula, Hecke operators, and Hecke's proof that the \(L\)-function of a cusp form has a functional equation. Modularity is stated. In the beauty paragraph, do not attribute \(|c_p|\le 2\sqrt p\) for \(\eta(\tau)^2\eta(11\tau)^2\) to the curve Riemann hypothesis unless Eichler–Shimura is marked as quoted. The identification \(c_p=a_p\) is a numerical check plus a remark.

**Hook.** Count the points of \(y^2+y=x^3-x^2\) modulo \(p\). Expand \(q\prod(1-q^n)^2(1-q^{11n})^2\). The same numbers come out. Why?

**Synopsis.** The fundamental domain, the valence formula, Hecke operators, \(L\)-functions, and one elliptic curve matched with one modular form. The functional equation of \(\eta^2\eta(11\tau)^2\) is proved. The reason the coefficients count points is modularity, stated and not proved. That statement is the cliffhanger of the concealed storeys: the rooms exist, the count matches as far as the series can see, and the identification is a theorem the series does not prove.

**Proved.** The valence formula. Hecke's functional equation for the \(L\)-function of a modular form of the type the chapter treats. The dimension of a space of cusp forms, if the file computes one. Multiplicativity of \(\tau(n)\) from the Hecke operators, if that is included; otherwise it stays in Book 6 and this chapter cites it.

**Examples.** The curve of conductor 11 and the product for \(\eta(\tau)^2\eta(11\tau)^2\), coefficients compared for small \(p\), the comparison labelled as a check. \(j=q^{-1}+744+196884q+\cdots\), the expansion the exercises already compute.

**Figures.** Two.

## Owns, defers, hands forward

**Owns.** Unique ideal factorisation in \(\mathcal O_K\). The Minkowski bound and finiteness of the class group. Dirichlet's unit theorem. Kronecker–Weber. Hasse–Minkowski and three squares. The class-number formula. Chebotarev in Dirichlet density. Tate's thesis for \(\mathbb Q\) and primitive Dirichlet \(L\)-functions. Riemann–Roch for smooth plane curves. The group law, Nagell–Lutz, and Mordell–Weil over \(\mathbb Q\). Hasse's bound for \(y^m=f(x)\). The functional equation of a modular \(L\)-function of the type proved here. The first case of Fermat for regular primes.

**Defers.** Artin reciprocity and the existence theorem, admitted. The functional equation of \(\zeta_K\) for a general field, a sketch. Modularity, Sato–Tate, Mazur's torsion theorem, Weil for a general curve, the second case of Fermat. Genus theory of the 2-rank. The canonical height as a quadratic form. The general \(n\)-Selmer group. Class-group moments and average ranks (Book 15, stated).

**Hands forward.** The concealed storeys, furnished. Book 14 uses the class group, Siegel's input, and the discriminant. Book 15 uses one 2-descent, the class-number formula, and the admitted shape of modularity, and it does not pretend to prove the averages.

## Pages and effort

Baseline 248 pages. Target 250–270. Effort: light to moderate. A second reading of the repaired three-squares test, the sketch heading on the general functional equation, the Eichler–Shimura sentence, and the discriminant pointer in Book 14 if it is still wrong.
