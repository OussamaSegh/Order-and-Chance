# Volume 13 — Arithmetic

**Score: 8/10.**

The quadratic rings, the ideal factorisation, Minkowski’s bound, Dirichlet’s units, Kummer’s first case, the three-squares theorem, the class-number formula, Tate’s thesis for \(\Q\), Kronecker–Weber over \(\Q\), Gauss’s theorem on \(x^2+27y^2\), Bézout and Riemann–Roch, Nagell–Lutz and Mordell, Hasse’s bound for \(y^2=f(x)\), and Hecke’s functional equation were checked step by step. The recomputed numbers match the page, including \(e^{\pi\sqrt{163}}\), the coefficient \(21493760\) of \(j\), the sums \(-7\), \(-69\) and \(-235\) for the class numbers \(1\), \(3\) and \(5\), the Chebotarev deviation \(0.00280\), the Hasse ratio \(0.977\) at \(p=2671\), and the level-\(11\) table through \(p=31\). The score is 8 because one sentence about the index is false. No numbered theorem was found false.

**Counts.** 0 critical, 1 major, 7 minor. No prerequisite issue.

**How this was read.** Book order in `volume13-arithmetic/main.tex`: preface, Quadratic Fields and Their Integers, Ideals in quadratic fields, Number Fields and Their Integers, Ideals and the Splitting of Primes, The Geometry of Numbers, Units, Cyclotomic Fields and Fermat, The \(p\)-adic Numbers, Local Fields, Quadratic Forms and the Local–Global Principle, Zeta Functions and Densities, Adèles and Tate’s Thesis, Class Field Theory, Algebraic Curves, Elliptic Curves, Curves over Finite Fields, Modular Forms and \(L\)-functions, then About the Cover. The blurb and `kdp.md` were read with the preface. Every exercise was read, including its hint and its solution. There are 206 exercises. The shared counter numbers theorems, propositions, lemmas, corollaries, definitions, and examples inside each chapter. Exercises use a separate counter.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. Proofs are dense, in the same register as Volumes 10 and 11. The word “journey” is the one banned filler that recurs; it is V13-001. Artin reciprocity, the existence theorem, and the Hilbert class field are labelled admitted. Mazur, Eichler–Shimura, modularity, Weil’s theorem for a general curve, Sato–Tate, Chebotarev in natural density, the converse of Kummer’s criterion, and the functional equation of \(\zeta_K\) for a general field are marked as quoted or sketched. The class-number-one list is attributed to Heegner, Baker and Stark and is not proved here.

## Issues

Paths are relative to `volume13-arithmetic/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V13-001 | `chapters/preface.tex:4` and `kdp.md:3` | style | minor | “This book is a journey through that world.” | `docs/WRITING-STYLE.md` lists “journey” among the banned filler words. Replace it with the map the next sentences already give. The blurb does not use the word. |
| V13-002 | `chapters/ch01-number-fields.tex:50` | reference | minor | “every field of finite degree over \(\Q\) is isomorphic to such a \(K\) (Volume 3, Theorem 8.9 and the fundamental theorem of algebra).” | Theorem 8.9 is Kronecker’s construction of an abstract root. The embedding into \(\C\) is Volume 3, Lemma 8.12, together with the fundamental theorem of algebra. |
| V13-003 | `chapters/ch01-number-fields.tex:444–447` | math | major | “for a squarefree integer \(m\ne0,\pm1\), \(\mathcal O_{\Q(\sqrt[3]m)}=\Z[\sqrt[3]m]\) when \(m\not\equiv\pm1\pmod9\), and the index is \(3\) when \(m\equiv\pm1\pmod9\)… Chapter 4 explains why such repeated roots modulo \(p\) are exactly what makes \(p\) divide the index.” | The two examples \(m=2\) and \(m=10\) are proved. The general biconditional is not. A repeated root of \(m_\theta\) modulo \(p\) means \(p\) divides \(\operatorname{disc}(m_\theta)\), hence \(p\) divides the index or \(p\) ramifies. Chapter 4’s Kummer–Dedekind theorem assumes \(p\) does not divide the index and reads the ramification from the repeated factor. Prove the pure-cubic classification, or mark it unproved, and replace “exactly”. |
| V13-004 | `chapters/ch02-ideals.tex:33` | reference | minor | “Volume 3, Propositions 6.5 and 6.8” for “an ideal \(I\ne R\) is prime if and only if \(R/I\) is a domain” and the maximal-ideal form. | Proposition 6.5 is the construction of the quotient ring. Both characterisations are Proposition 6.8. Proposition 6.3, cited nearby for a finite domain, is the right number. |
| V13-005 | `chapters/ch01-number-fields.tex:402`, proof of `prop:eisenstein` | reference | minor | “The finite group \(\mathcal O_K/\Z[\theta]\) then has an element of order \(p\) (Cauchy’s theorem).” | The theorem used is Volume 3, Theorem 3.11. The step is correct. |
| V13-006 | `chapters/ch12-ideals-quadratic.tex:71`, caption of `fig:lattice`; drawing in `figures/ch11-lattice.tex:6` | figure | minor | “The ideal \(P\) (charcoal) contains every second point, the ideal \((2)=P^2\) (circled) every fourth.” | The TikZ fills \(P\) in MidnightBlue and circles \((2)\) in ForestGreen. The densities \(1/2\) and \(1/4\) are right. Name the colours that are drawn. |
| V13-007 | `chapters/ch03-geometry.tex:231`; `chapters/ch05-cyclotomic.tex:305`; `chapters/ch08-zeta.tex:482–486`; `chapters/ch04-units.tex:155` and the solution of `ex:cyclic7` at line 399 | math | minor | “For \(\Q(\sqrt[3]7)\), on the other hand, \(h_K=3\).” “For \(p\le19\), \(\Z[\zeta_p]\) is a principal ideal domain (\(h_p=1\)).” The table \(h^-=1,3,8,9,37,121\) “verifies every value against PARI.” The caption calls \(0.5255\) the regulator, and the solution says PARI shows that \(\theta\) and \(1+\theta\) generate the unit group. | Each value is a standard one. None is computed in the book, and the exercise on \(\Q(\cos(2\pi/7))\) asks only for independence. Mark the class numbers and the full unit rank as computations, or give the ideal arithmetic. The independence of \(\theta\) and \(1+\theta\) is proved. |
| V13-008 | `chapters/ch03-geometry.tex:254–255` | reference | minor | “just as the sphere has no connected unramified (covering) map onto it other than the identity (Chapter 13 takes up this analogy).” | Chapter 13 uses \(|d_K|>1\) to say that \(\Q\) has no unramified extension. It does not mention the sphere or covering spaces. Drop the forward pointer, or add the comparison where it is promised. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map is the seventeen chapters in `main.tex` order. The next two volumes are named for Siegel, the functional equation of \(L(s,\chi)\), Chebotarev, and the averages in Volume 15. About the Cover is the curve \(y^2=x^3-x+1\) with the chord-and-tangent law, and it names Abel, Jacobi and Mordell 1922. No notebook is promised. The jacket’s exceptions are the admitted class-field theorems and the quoted remarks.

### Chapter 1

The integral basis of a quadratic field, the units of the imaginary ones, and the real unit theorem in the Pell form were checked. The fundamental units \(1+\sqrt2\), \((3+\sqrt{13})/2\), \(2+\sqrt3\) and \(5+2\sqrt6\) have the norms stated, and \(35+6\sqrt{34}\) has norm \(+1\). All twelve exercises were read. Volume 1, Proposition 6.8 is the rational-root test, and Volume 2, Theorem 9.8 is Pell’s equation.

### Chapter 2

Hurwitz’s lemma, the second proof of unique ideal factorisation, the splitting law, and \(h(\Q(\sqrt{-5}))=2\) were checked. All eleven exercises were read. \(29=3^2+5\cdot2^2\). The value \(e^{\pi\sqrt{163}}=262537412640768743.99999999999925\ldots\) matches the remark. Volume 10, Theorems 6.6 and 6.13 are the citations used for the general Dedekind theory. The six factorisations of \(6\) are Volume 2, Theorem 10.4, and also Exercise 10.2.

### Chapter 3

Embeddings, the integrality criterion, the existence of an integral basis, Stickelberger’s congruence, and the index formula were checked. \(\Q(\sqrt[3]2)\) has discriminant \(-108\), and \(\Q(\sqrt[3]{10})\) has index \(3\) and discriminant \(-300\). The minimal polynomial of \(\sqrt2+\sqrt[3]2\) is \(X^6-6X^4-4X^3+12X^2-24X-4\). All sixteen exercises were read. The biquadratic basis \(1,\sqrt2,\sqrt3,(\sqrt2+\sqrt6)/2\) has discriminant \(2304\), and the index of \(\Z[\sqrt2+\sqrt3]\) is \(8\). V13-002, V13-003 and V13-005 are the slips.

### Chapter 4

Unique factorisation of ideals, \(\sum e_if_i=n\), Kummer–Dedekind, ramification at the discriminant, and Dedekind’s cycle theorem were checked. The roots of \(\Phi_7\) modulo \(29\) are \(7,16,20,23,24,25\), and \(2\) generates \(\mathbb F_{29}^\times\). \(\operatorname{disc}(X^5-X-1)=2869=19\cdot151\). Of the \(17982\) primes below \(2\cdot10^5\) that do not divide \(2869\), the cycle-type proportions deviate from the class sizes in \(S_5\) by at most \(0.00280\), printed as \(0.003\). All fifteen exercises were read. V13-004 is the slip in the reminder.

### Chapter 5

Blichfeldt, Minkowski, the covolume \(2^{-r_2}\sqrt{|d_K|}\), and Hermite’s finiteness were checked. The bounds are about \(2.85\), \(2.94\), \(4.90\), \(3.05\) and \(4.36\) for \(\Q(\sqrt{-5})\), \(\Q(\sqrt[3]2)\), \(\Q(\sqrt[3]{10})\), \(\Q(\sqrt{-23})\) and \(\Q(\sqrt{-47})\). All fourteen exercises were read. The four-squares volume comparison \(2\pi^2>16\) is right, and Lagrange’s theorem is already Volume 2, Theorem 7.4. V13-007 and V13-008 are the slips.

### Chapter 6

The log lattice, Dirichlet’s unit theorem, and the regulator identity were checked. For \(d=61\), \(\varepsilon=(39+5\sqrt{61})/2\) has norm \(-1\) and \(\varepsilon^6=1766319049+226153980\sqrt{61}\). The \(2\times2\) minor for \(\Q(\cos(2\pi/7))\) is about \(0.52545\). All eleven exercises were read. Siegel’s lower bound is deferred to Volume 14, which contains it. V13-007 is the PARI sentence in the solution.

### Chapter 7

The ring \(\Z[\zeta_p]\), the Gauss sum, reciprocity through Frobenius, Kummer’s lemma, and the first case for a regular prime were checked. The local density \(\sigma_\infty=2\Gamma(1/3)^2/(3\Gamma(2/3))\) is about \(3.533\). All thirteen exercises were read. The solution of the exercise on \(23\) proves that no element of \(\Q(\sqrt{-23})\) has norm \(47\); \(a^2+23b^2=188\) has no solution. The relative class numbers \(h_p=1\) for \(p\le19\) are V13-007. The count of \(181\) regular primes among the \(302\) odd primes below \(2000\) was not recomputed from Bernoulli numbers.

### Chapter 8

The ultrametric, the product formula, Hensel’s lemma, the squares in \(\Q_p\), and Ostrowski’s theorem were checked. \(1/3\) in \(\Z_2\) has digits \(1,1,0,1,0,\ldots\). The lifts of a square root of \(-1\) in \(\Z_5\) begin \(2,7,57,182\). All fourteen exercises were read. Volume 7, Theorem 2.10 is the construction of \(\Q_p\), and Corollary 2.11 is the compactness of \(\Z_p\). Volume 2, Theorem 3.8 is Hensel’s lemma in the form used here.

### Chapter 9

Ostrowski for number fields, the product formula, Hensel factorisation, \(ef=n\), Krasner’s lemma, and the finiteness of extensions of a given degree were checked. The Serre mass for the quadratic extensions of \(\Q_2\) is \(2\cdot\frac12+4\cdot\frac14=2\). All eleven exercises were read. A square root of \(2\) in \(\Z_7\) begins \(3+1\cdot7+2\cdot7^2+6\cdot7^3\), and \(2166^2\equiv2\pmod{2401}\).

### Chapter 10

The Hilbert-symbol formulas, the product formula, Hasse–Minkowski, and the three-squares theorem were checked, including the repair that a \(2\)-adic unit is a square if and only if it is \(1\) modulo \(8\). The rounding \(f(x-y)\le3/4<1\) lets Davenport–Cassels finish the argument, and \(28\equiv4\pmod8\) is the case the old argument mishandled. All eleven exercises were read. A positive integer is a sum of three integer squares exactly when it is not of the form \(4^a(8b+7)\).

### Chapter 11

The cone count, the residue \(\kappa=2^{r_1}(2\pi)^{r_2}hR/(w\sqrt{|d|})\), the formula for \(h^-\), Kummer’s criterion, and Chebotarev’s theorem in Dirichlet density were checked. \(\sum_{a=1}^{22}(a/23)a=-69\), so \(L(1,\chi)=3\pi/\sqrt{23}\) and \(h=3\). The numerator \(7709321041217=37\cdot683\cdot305065927\). All eleven exercises were read. \(L(1,\chi_8)=\log(1+\sqrt2)/\sqrt2\), and the class-number formula then gives \(h(\Q(\sqrt2))=1\). The natural-density form of Chebotarev is stated and not proved. V13-007 is the PARI table.

### Chapter 12

The decomposition \(\mathbb A_f=\Q+\hat\Z\), discreteness of \(\Q\), the self-dual Fourier transform on the Schwartz–Bruhat functions, adelic Poisson summation, Tate’s theorem for \(\Q\), and Fujisaki’s compactness were checked. The constant \(C_K=(2/\pi)^{r_2}\sqrt{|d_K|}\) matches Minkowski’s covolume. The duplication identity \(\Gamma_\R(s)\Gamma_\R(s+1)=\Gamma_\C(s)\) was recomputed. All eleven exercises were read. Volume 5, Theorem 9.15 is the parameter-integral theorem used for the continuation, Theorem 8.14 is the sign of the quadratic Gauss sum, and Theorem 10.8 is Riemann’s functional equation. Volume 8, Proposition 13.12 is Haar measure on \(\Q_p\). The functional equation of \(\zeta_K\) for a general field is a sketch.

### Chapter 13

Local Kronecker–Weber, the global theorem over \(\Q\), cubic reciprocity, and Gauss’s criterion for \(x^2+27y^2\) were checked. Artin reciprocity, the existence theorem, and the Hilbert class field are admitted and are not used except in the theorems that name that hypothesis. All eleven exercises were read. For \(f=X^3-X-1\), \(f(10)=989=23\cdot43\), and \(59=5^2+5\cdot2+6\cdot2^2\) splits completely. The three primes \(p\equiv1\pmod3\) that are \(x^2+27y^2\) are a set of density \(1/6\), as Chebotarev says.

### Chapter 14

Bézout’s dimension count \(\binom{d+2}2-\binom{d-m+2}2-\binom{d-n+2}2+\binom{d-m-n+2}2=mn\), Noether’s theorem, the residue theorem, and Riemann–Roch were checked. The genus of a smooth plane curve of degree \(n\) is \((n-1)(n-2)/2\). All twelve exercises were read. Two circles meet in four points, two of them the circular points at infinity. The Hermitian curve over \(\mathbb F_{16}\) has \(65\) points, which is the Weil maximum \(q+1+2g\sqrt q\).

### Chapter 15

The chord-and-tangent law, the nine-point proof of associativity, the filtration, Nagell–Lutz, reduction modulo a good prime, the weak Mordell–Weil theorem, and the height descent were checked. The identity \(4a^3+27b^2=(3x^2+4a)f'(x)^2-27(x^3+ax-b)f(x)\) holds. On the cover curve, the line through \((-1,1)\) and \((1,1)\) gives the sum \((0,-1)\), and the tangent gives \(2P=(3,-5)\). All eleven exercises were read. The point \((2,3)\) on \(y^2=x^3+1\) has order \(6\). Mazur’s list is quoted.

### Chapter 16

Rationality of the zeta function, the functional equation, Gauss’s count for \(X^3+Y^3=Z^3\), Bombieri’s auxiliary function, and the Riemann hypothesis for \(y^m=f(x)\) were checked. The dimension count in Bombieri’s proof reduces to \(q_0-(g+1)^2>0\). All eleven exercises were read. For \(y^2=x^3-x+1\) over \(\mathbb F_5\), \(N_1=8\) and \(N_2=32\). Among the \(667\) primes \(3\le p<5000\) with \(p\ne23\), the largest ratio \(|a_p|/(2\sqrt p)\) is \(0.977\), at \(p=2671\). Weil’s theorem for a general curve, and Sato–Tate, are quoted.

### Chapter 17

The fundamental domain, the valence formula, the bijection by \(j\), the Hecke algebra, and Hecke’s functional equation were checked. \(640320^3+744=262537412640768744\), and \(e^{\pi\sqrt{163}}\) lies within \(10^{-12}\) of that integer. \(\Delta=q-24q^2+252q^3-1472q^4+\cdots\), and \(j=q^{-1}+744+196884q+21493760q^2+\cdots\). All eleven exercises were read. The level-\(11\) form satisfies \(f(-1/(11\tau))=-11\tau^2f(\tau)\), and the printed table of \(a_p=c_p\) through \(p=31\) was recomputed. Eichler–Shimura and the modularity theorem are quoted. The comparison for every \(p<10^5\) was not rerun.

## Not checked

The book was not typeset. Figures were read from the TikZ sources and the captions. The value of \(B_{32}\) was not recomputed from the generating function; the printed factorisation of its numerator was checked. The census of \(181\) regular primes below \(2000\), the class number \(h(\Q(\sqrt[3]7))=3\), the relative class numbers through \(p=41\), and the claim \(a_p=c_p\) for every \(p<10^5\) were not recomputed. The quoted theorems named above were not proved again.
