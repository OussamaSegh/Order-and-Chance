# Book 3 — Symmetry

*Groups, Rings and Fields.* The on-disk subtitle is "The Language of Symmetry".

**Element.** The symmetries of the plan. What one may do to the building without changing it, and which openings cannot be cut with the tools one has.

**Source.** `tome3-symmetry`. Twelve main chapters and thirteen linear-algebra appendices in `main.tex`. About 372 pages in the 7×10 table. The October review scored it 8. The primitive-element theorem and the three simple real roots of \(X^5-4X+2\) are now in the source.

## Promise

Symmetry is what a transformation preserves. The floor climbs to two summits the preface already names: there is no formula in radicals for the roots of \(X^5-4X+2\), because the Galois group is \(S_5\); and the character table of a finite group is a small square of numbers that holds the representation theory. The linear-algebra appendices are the specialist's drawings of a member Book 1 already set in place. They are not a second book hidden in the back.

## Prerequisites

Book 1, especially polynomials, complex numbers, and the spectral theorem for symmetric matrices. Book 2's cyclic groups, \(\varphi\), Euler's theorem, Eisenstein, the binomial theorem modulo \(p\), and primitive roots. \(\varphi(n)\) is recalled in one sentence at its first use. No topology and no measure.

## How the subtitle is delivered

The parts keep their catalog names. *Groups, Rings and Fields* is what they contain.

Groups is the symmetries of a set, through Sylow. Rings and Polynomials is the symmetries of addition and multiplication, through extensions. Fields and Galois Theory is the subtitle's third word, and it is also where the catalog places the character table and the quaternions: the character table is the group's shadow, reached after Galois, and the quaternions are the division ring that realises rotations. Both deliver the title, Symmetry, from inside that part. The linear-algebra appendices that count by symmetry stay at the end of it. The ones that are spectra, operators, or a reprint of Book 1's linear algebra do not, and they move.

No part is renamed. Characters and quaternions were already in Fields and Galois Theory in the catalog.

**Moves.** Book 1 already teaches the first course. What later books cite as spectra and operators belongs in Book 8.

| Appendix | File | Verdict |
| --- | --- | --- |
| C Eigenvalues, E Spectral theorem, F Singular values, H Graphs through eigenvalues, K Matrix inequalities, L Linear dynamics | `linear-ch03`, `linear-ch05`, `linear-ch06`, `linear-ch08`, `linear-ch11`, `linear-ch12` | MOVE to Book 8, Spectra and Operators. |
| J Tensors and the cost of multiplying matrices | `linear-ch10-tensors.tex` | MOVE to Book 10, Algebra, as multilinear algebra. |
| A, B, D Duality, determinants, inner products | `linear-ch01`, `linear-ch02`, `linear-ch04` | MOVE the specialist theorems Book 8 or Book 9 quotes. Do not reprint Book 1's Chapter 6. |
| G Positive matrices, I Symmetry diagonalises, M The linear algebra method | `linear-ch07`, `linear-ch09`, `combinatorial.tex` | KEEP, inside Groups. A circulant, a Perron root of a symmetry, and the linear algebra method are symmetry counting. |

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Groups | 1–5 |
| II | Rings and Polynomials | 6–8 |
| III | Fields and Galois Theory | 9–12, and the appendices that stay |

---

The chapter notes follow the manuscript's file order. The part names are the table above. Appendices marked MOVE leave Fields and Galois Theory.

### Part I. Groups

#### Chapter 1. Groups as Symmetries

**Status.** KEEP — `tome3-symmetry/chapters/ch01-groups.tex` (344 lines). The voice of this opening ("these two facts, and nothing else, are what a group records") is the voice the series should keep.

**Hook.** A cube can be put back in its box in 24 ways, and four cards can be shuffled in 24 ways. They are the same 24.

**Synopsis.** The axioms, subgroups, order of an element, Lagrange, and cyclic groups. \(D_n\) is the symmetry group of the regular \(n\)-gon, of order \(2n\), and every later book keeps that convention. Composition in \(S_n\) is "first the right factor", stated once.

**Proved.** Lagrange's theorem. The classification of cyclic groups. Euler's theorem recovered from Lagrange when the group is \((\mathbb Z/n\mathbb Z)^\times\).

**Examples.** The 24 rotational symmetries of the cube, matched with \(S_4\). One non-abelian group of small order written as a multiplication table only long enough to see it.

**Figures.** One.

#### Chapter 2. Morphisms and Quotients

**Status.** KEEP — `chapters/ch02-quotients.tex` (304 lines).

**Hook.** Arithmetic modulo \(n\) forgets everything about an integer except its remainder, and the operations survive. The sign of a permutation is the same kind of forgetting.

**Synopsis.** Homomorphisms, normal subgroups, quotients, and products. The first isomorphism theorem is the method. Quotients are how a symmetry can be coarse-grained without the operations falling apart.

**Proved.** The first isomorphism theorem. The correspondence theorem at the level the exercises need. The sign homomorphism.

**Examples.** \(\mathbb Z/n\mathbb Z\) as a quotient. \(S_n/A_n\).

**Figures.** One.

#### Chapter 3. Group Actions and Counting

**Status.** KEEP — `chapters/ch03-actions.tex` (286 lines).

**Hook.** How many necklaces of 6 beads in 3 colours, if rotation does not make a new necklace? Not \(3^6/6\).

**Synopsis.** Actions, orbits, stabilisers, Burnside's lemma, and conjugacy. Counting orbits is inclusion of symmetry into a count, the same impulse as Book 1's inclusion–exclusion, now with a group. The \(p\)-group class equation prepares Sylow.

**Proved.** Orbit–stabiliser. Burnside. The class equation.

**Examples.** The necklace count, finished. A conjugacy class of \(S_4\) listed.

**Figures.** One.

#### Chapter 4. The Symmetric Group

**Status.** KEEP — `chapters/ch04-symmetric.tex` (360 lines). REVISE only if a second reader, walking the fifteen-puzzle rectangles, finds a coordinate the October review left unchecked. The mathematics that was recomputed there was consistent.

**Hook.** Swap tiles 14 and 15 of the fifteen-puzzle and try to slide them home. In 1880, thousands of people tried.

**Synopsis.** Cycles, conjugacy in \(S_n\), generators, the fifteen-puzzle, and simplicity of \(A_n\) for \(n\ge 5\). The fifteen-puzzle is the first theorem whose obstruction is a sign: the building has a parity the eye does not see. Simplicity of \(A_5\) is the member the quintic will load.

**Proved.** Conjugacy classes in \(S_n\) are cycle types. The alternating group is generated by 3-cycles. \(A_n\) is simple for \(n\ge 5\). The fifteen-puzzle's reachable positions are the even permutations.

**Examples.** A position of the fifteen-puzzle proved unreachable. A 3-cycle written as a product of an even number of transpositions, and the sign computation beside it.

**Figures.** One.

#### Chapter 5. Sylow Theorems and Finite Groups

**Status.** KEEP — `chapters/ch05-sylow.tex` (324 lines). The line "Lagrange forbids; it promises nothing" stays.

**Hook.** Is there a simple group of order 30?

**Synopsis.** The three Sylow theorems, the groups of order \(pq\), \(8\), and \(12\), and solvable groups. Solvability is defined here because Galois theory will use it. The classification of finite simple groups is at most a sentence, and it is not a theorem of this book.

**Proved.** Both Sylow theorems the book states (existence, and conjugacy together with the congruence for the number of subgroups). The lists of groups of orders \(pq\), \(8\), and \(12\).

**Examples.** Order 30, in full. One Sylow count that is not 1, so the subgroups are not normal.

**Figures.** One.

### Part II. Rings and Polynomials

#### Chapter 6. Rings and Ideals

**Status.** KEEP — `chapters/ch06-rings.tex` (352 lines). The hook repeats Book 2's equation on purpose. One sentence says the equation was the crack in the masonry, and this chapter is the language of the repair.

**Hook.** In \(\mathbb Z[\sqrt{-5}]\), \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\). Unique factorisation, which held in \(\mathbb Z\), has failed.

**Synopsis.** Rings, ideals, quotients, prime and maximal ideals, factorisation in domains, and polynomials over a UFD. Gauss's lemma and the fact that a UFD's polynomial ring is a UFD. Book 2's quadratic ideals are an example, not the definition.

**Proved.** The isomorphism theorems for rings. Prime and maximal ideals in the form the Nullstellensatz will want. Gauss's lemma. \(\mathbb Z[x]\) is a UFD.

**Examples.** The two factorisations of 6, now in the language of principal ideals that do not exist. A maximal ideal that is not principal, if the chapter has one it can afford; otherwise the prime ideal \((2,1+\sqrt{-5})\) is the example.

**Figures.** One.

#### Chapter 7. Modules over a Principal Ideal Domain

**Status.** KEEP — `chapters/ch07-modules.tex` (323 lines).

**Hook.** How many abelian groups of order 360 are there? And why does every square matrix satisfy its own characteristic polynomial? One theorem answers both.

**Synopsis.** Modules, Smith normal form, the structure theorem for finitely generated modules over a PID, and linear algebra over \(K[X]\). Finite abelian groups and rational canonical form are the two faces. Jordan form is deduced here and cited by Book 4's Markov chains.

**Proved.** The structure theorem. Smith normal form over a Euclidean domain. Cayley–Hamilton as a corollary, matching Book 1's theorem rather than replacing it. Jordan form where the characteristic polynomial splits.

**Examples.** The abelian groups of order 360. One matrix brought to Jordan form, with the minimal polynomial.

**Figures.** One.

### Part III. Fields and Galois Theory

#### Chapter 8. Field Extensions

**Status.** KEEP — `chapters/ch08-extensions.tex` (417 lines). The primitive element theorem is now numbered (`thm:primitiveelement`). Chapter 10 may cite it.

**Hook.** A ruler and compass bisect any angle. Can they trisect \(60^\circ\)? Can they double the cube?

**Synopsis.** Degree, the tower law, algebraic elements, splitting fields, and the classical impossibilities. Constructibility is a degree obstruction. The chapter works inside \(\mathbb C\), and it says so. An abstract algebraic closure is not this book's load.

**Proved.** The tower law. The degree of a simple algebraic extension. The primitive element theorem for subfields of \(\mathbb C\). The impossibilities: duplication of the cube, trisection of \(60^\circ\), and squaring the circle if transcendence of \(\pi\) is quoted with a date rather than proved.

**Examples.** \([\mathbb Q(\sqrt 2,\sqrt 3):\mathbb Q]=4\), with a basis. One constructible length and one that is not.

**Figures.** One.

#### Chapter 9. Finite Fields

**Status.** KEEP — `chapters/ch09-finite-fields.tex` (323 lines).

**Hook.** A damaged QR code can lose almost a third of its squares and still be read. The repair is a finite field.

**Synopsis.** Characteristic, Frobenius, the cyclic multiplicative group, existence and uniqueness of \(\mathbb F_q\), subfields, the count of monic irreducibles, and Reed–Solomon codes. Frobenius is the same map Book 13 will use on primes. One sentence says so.

**Proved.** Existence and uniqueness of the field with \(q\) elements. The multiplicative group is cyclic. The number of monic irreducibles of degree \(n\) over \(\mathbb F_q\).

**Examples.** \(\mathbb F_8\) or \(\mathbb F_9\) built by hand. One Reed–Solomon decoding on a tiny alphabet.

**Figures.** One.

#### Chapter 10. Galois Theory

**Status.** KEEP — `chapters/ch10-galois.tex` (362 lines). The three simple real roots are now written out, and the primitive element theorem is a theorem. REVISE the regular-polygon paragraph so that "\(\varphi(n)\) is a power of 2 if and only if \(n=2^kp_1\cdots p_s\) with distinct Fermat primes" is either proved or stopped at the degree. The October review's gap on that arithmetic equivalence was not the one checked as closed.

**Hook.** Formulas for degrees 2, 3, and 4 exist. Why was there never a formula for the quintic?

**Synopsis.** The Galois group, Galois extensions, the fundamental theorem in the book's convention (subfields of \(\mathbb C\)), cyclotomic fields and constructible polygons, and solvability by radicals. The climax of the floor is the identification \(\mathrm{Gal}(X^5-4X+2)\cong S_5\).

**Proved.** \(|\mathrm{Gal}(L/K)|=[L:K]\) for a Galois extension in the book's setting. The fundamental theorem. \(\mathbb Q(\zeta_n)/\mathbb Q\) has degree \(\varphi(n)\) and abelian Galois group. Solvability by radicals implies a solvable Galois group. The quintic computation.

**Examples.** The quadratic formula read as a group of order 2. \(X^5-4X+2\), with the transposition and the 5-cycle both on the page. One cyclotomic extension whose Galois group is computed, \((\mathbb Z/n\mathbb Z)^\times\).

**Figures.** One.

### Part IV. Representations and Rotations

#### Chapter 11. Representations and Characters

**Status.** KEEP — `chapters/ch11-characters.tex` (400 lines). This is the second summit. The Fourier convention is the series convention: \(1/|G|\) in the analysis. Abstraction's shuffle chapter now states the difference; this chapter should state the convention in one line at the abelian section so the joint is made from both sides.

**Hook.** \(24=1^2+1^2+2^2+3^2+3^2\) and \(60=1^2+3^2+3^2+4^2+5^2\). Why is the order of a group a sum of squares?

**Synopsis.** Representations, characters, orthogonality, the tables of \(S_4\) and \(A_5\), and Fourier analysis on finite abelian groups. Dirichlet characters are recovered as the abelian case, with a pointer to Book 2 and ahead to Book 6. The deck's random transpositions are mentioned; the cutoff is Abstraction.

**Proved.** Maschke. Schur's lemma. Row and column orthogonality. \(\sum d_i^2=|G|\). The character tables of \(S_4\) and \(A_5\).

**Examples.** The table of \(S_4\), computed, not only displayed. One abelian Fourier inversion, a residue character.

**Figures.** One.

#### Chapter 12. A Glimpse Beyond: Quaternions and Rotations

**Status.** KEEP — `chapters/ch12-quaternions.tex` (304 lines). The cliffhanger is the plate trick: a full turn is not the identity on the double cover. Book 9 proves \(\mathrm{SU}(2)\to\mathrm{SO}(3)\) as a Lie-group homomorphism. This chapter is the picture.

**Hook.** Turn a plate one full turn, keeping it flat, and your arm is twisted. Turn again, and the twist is gone.

**Synopsis.** Quaternions, unit quaternions and rotations, the finite subgroups of \(\mathrm{SO}(3)\), and the four-square identity read off the norm. The finite list (cyclic, dihedral, \(A_4\), \(S_4\), \(A_5\)) is the theorem. The plate trick is the pointer.

**Proved.** The normed division algebra structure. The double cover \(S^3\to\mathrm{SO}(3)\), at the level of unit quaternions. The classification of finite subgroups of \(\mathrm{SO}(3)\).

**Examples.** A rotation written as conjugation by a quaternion. The binary tetrahedral group, or whichever finite subgroup the file draws.

**Figures.** Two.

### Appendices A–M

These are KEEP as the specialist linear algebra. Book 1 owns the first course. A one-line preface to Appendix A says that. They are not renumbered into the main story. Each is a drawing of a member the later floors quote.

#### Appendix A. Spaces, Quotients and Duality

**Status.** KEEP — `chapters/linear-ch01-duality.tex` (721 lines).

**Hook.** Grassmann, on the labour of a formal science. The appendix then does the labour: bases, quotients, duals, annihilators, transpose.

**Synopsis.** The coordinate-free linear algebra Book 1 used in examples and this book needs as a language. Dimension counting is the method.

**Proved.** Dimension formulas for quotients, sums, and annihilators. The dual of a dual in finite dimension.

**Examples.** A quotient basis exhibited. One annihilator computation.

**Figures.** Two.

#### Appendix B. Determinants as Volume

**Status.** KEEP — `chapters/linear-ch02-volume.tex` (762 lines).

**Hook.** Alice and the March Hare, on saying what one means. A determinant is a signed volume, and the appendix says so.

**Synopsis.** Exterior powers, minors, Dodgson condensation, and the Lindström–Gessel–Viennot lemma for nonintersecting paths. Volume is the geometric meaning Book 1 stated and this appendix organises.

**Proved.** The exterior-algebra characterisation of the determinant. Cauchy–Binet, if it is the theorem the file contains. The path lemma.

**Examples.** A \(2\times 2\) volume. One nonintersecting-path count.

**Figures.** Three.

#### Appendix C. Eigenvalues and Invariant Subspaces

**Status.** KEEP — `chapters/linear-ch03-eigen.tex` (619 lines).

**Hook.** Cayley, declining to write the general case. The appendix writes it.

**Synopsis.** Invariant subspaces, triangularisation, Cayley–Hamilton again from this point of view, generalised eigenspaces, nilpotent operators and Young diagrams, commuting families, and functions of a matrix. Young diagrams here are linear algebra; Abstraction's Specht modules are the return.

**Proved.** Existence of an invariant flag over an algebraically closed field. The Jordan decomposition in the form Chapter 7 uses, if this appendix is the home of the details.

**Examples.** A nilpotent Jordan block and its diagram.

**Figures.** Two.

#### Appendix D. Inner Products and Projections

**Status.** KEEP — `chapters/linear-ch04-inner.tex` (915 lines).

**Hook.** Legendre, on least squares as the most general principle he can propose.

**Synopsis.** Cauchy–Schwarz, orthonormal bases, projections, least squares, Gram determinants, the Cauchy determinant and the Hilbert matrix, orthogonal polynomials, and Gauss quadrature. This is the enlargement of Book 1's Chapter 6.

**Proved.** Orthogonal projection. The Gram determinant. Gauss quadrature's exactness on the degree the chapter claims.

**Examples.** A least-squares line. One orthogonal polynomial computed by Gram–Schmidt.

**Figures.** Three.

#### Appendix E. The Spectral Theorem and Its Relatives

**Status.** KEEP — `chapters/linear-ch05-spectral.tex` (583 lines).

**Hook.** Hilbert, naming a purely mathematical theory "spectral analysis" before the physicists arrived.

**Synopsis.** The spectral theorem in the form this appendix owns, Rayleigh quotients, min-max, Weyl's inequalities, Schur–Horn, and eigenvalue perturbation. Book 8 owns the compact operators on Hilbert space. This appendix owns matrices.

**Proved.** The spectral theorem for Hermitian matrices, if it is not only cited back to Book 1. Courant–Fischer. Weyl's inequalities.

**Examples.** A \(2\times 2\) min-max. One perturbation bound with the numbers on the page.

**Figures.** Two.

#### Appendix F. Singular Values

**Status.** KEEP — `chapters/linear-ch06-svd.tex` (536 lines).

**Hook.** The singular value decomposition as the tool that does every job.

**Synopsis.** SVD, the polar decomposition, norms, Eckart–Young, the pseudo-inverse, principal components, conditioning, and Procrustes. Low-rank approximation is the structural fact: the best simpler model is a truncation of the spectrum.

**Proved.** Existence of the SVD. Eckart–Young.

**Examples.** A \(2\times 2\) SVD. One best rank-1 approximation.

**Figures.** Two.

#### Appendix G. Positive Matrices

**Status.** KEEP — `chapters/linear-ch07-perron.tex` (568 lines).

**Hook.** Fibonacci's rabbits. A positive matrix has a dominant eigenvalue, and the rabbits are the example.

**Synopsis.** Perron, Frobenius, Wielandt, and Markov chains with PageRank as an example. Book 4's Markov chapter cites the stochastic-matrix facts it needs; this appendix is the home of Perron–Frobenius.

**Proved.** Perron's theorem. The Frobenius form for irreducible non-negative matrices, at the strength the file proves.

**Examples.** A small positive matrix and its Perron root. One PageRank on a three-page graph.

**Figures.** Two.

#### Appendix H. Graphs through Their Eigenvalues

**Status.** KEEP — `chapters/linear-ch08-graphs.tex` (569 lines). The friendship theorem's parenthetical, that a rational square root of an integer is an integer, can stay: it is true and brief.

**Hook.** Huang's theorem on induced subgraphs of the hypercube.

**Synopsis.** Walks and adjacency matrices, the friendship theorem, strongly regular graphs, independence and colouring, Graham–Pollak, Huang, and the Petersen graph. Book 12's spectral graph theory is the analyst's return of this appendix.

**Proved.** The friendship theorem. Huang's signed-adjacency bound, if the file's proof is complete; the review found it so.

**Examples.** The Petersen graph's spectrum. One friendship-graph count.

**Figures.** Three.

#### Appendix I. Symmetry Diagonalises

**Status.** KEEP — `chapters/linear-ch09-symmetry.tex` (687 lines).

**Hook.** Weyl, on symmetry as a way of comprehending.

**Synopsis.** Circulants, characters of finite abelian groups, Cayley graphs, the Hamming cube and Krawtchouk polynomials, Delsarte's bound, and Dedekind's group determinant. Circulants are the first matrices symmetry diagonalises. Book 8's finite Fourier analysis is the same diagonalisation, written for an analyst.

**Proved.** A circulant is diagonalised by the Fourier matrix. Delsarte's linear programming bound in the form the appendix states.

**Examples.** One circulant, diagonalised by hand.

**Figures.** Two.

#### Appendix J. Tensors and the Cost of Multiplying Matrices

**Status.** KEEP — `chapters/linear-ch10-tensors.tex` (599 lines).

**Hook.** Strassen's exponent, a matrix product in fewer than \(4.7\,n^{\log_2 7}\) operations.

**Synopsis.** Kronecker products, tensor rank, Strassen, the Schmidt decomposition, and the three-multiplication rule for complex products. The cost of a bilinear map is a rank. That is the whole idea.

**Proved.** Strassen's algorithm. The rank bound it implies.

**Examples.** The \(2\times 2\) Strassen identities, written out.

**Figures.** Two.

#### Appendix K. Inequalities between Matrices

**Status.** KEEP — `chapters/linear-ch11-inequalities.tex` (593 lines).

**Hook.** Hardy, on analysts hunting inequalities they cannot prove.

**Synopsis.** The Loewner order, Schur complements, determinant inequalities, the Schur product theorem, Gershgorin, and Hilbert's inequality. Hilbert's inequality is the one Book 14's large sieve is cousin to; a sentence may say so without proving the sieve.

**Proved.** Gershgorin. The Schur product theorem. Hilbert's inequality with the constant the appendix achieves.

**Examples.** A Gershgorin picture for a \(3\times 3\) matrix. Hilbert's inequality on a short vector.

**Figures.** Two.

#### Appendix L. Linear Dynamics

**Status.** KEEP — `chapters/linear-ch12-dynamics.tex` (550 lines).

**Hook.** Maxwell, on a governor: uniform motion plus a disturbance.

**Synopsis.** Powers of a matrix, Gelfand's formula, linear differential equations, Lyapunov, the speed of iteration, controllability, and Maxwell's cubic. Stability is a spectral condition. Book 8's Gelfand theory is the infinite-dimensional return of the spectral-radius formula.

**Proved.** Gelfand's formula for the spectral radius of a matrix. The stability criterion the chapter states for \(\dot x=Ax\).

**Examples.** A \(2\times 2\) saddle. Maxwell's cubic, checked.

**Figures.** Three.

#### Appendix M. The Linear Algebra Method

**Status.** KEEP — `chapters/combinatorial.tex` (564 lines).

**Hook.** Artin, on throwing the matrices out after they have done the work.

**Synopsis.** Oddtown and Eventown, Fisher's inequality, the polynomial method, the combinatorial Nullstellensatz, and the cap-set bound of the strength this appendix proves. The Crossroads Journey on the cap set belongs with this appendix if it uses only this method, and with Book 8's finite Fourier analysis if it uses the slice rank or the characters of \(\mathbb F_3^n\). The home is whichever proof the Journey actually writes. One home, not both.

**Proved.** Oddtown. The combinatorial Nullstellensatz. The cap-set bound the file contains.

**Examples.** Oddtown on a small ground set. One Nullstellensatz polynomial.

**Figures.** Two.

## The old problem book

Book 6 is Crossroads, the analytic volume. The old P1 problem book is removed by the renumbering branch, which appends its problems to Books 1–6. This plan does not place them again. A problem that cites a chapter moved here follows that chapter.

## Owns, defers, hands forward

**Owns.** Lagrange, actions, Sylow, \(A_n\) simple, PID modules, Jordan form, finite fields, the fundamental theorem of Galois theory in the book's convention, the quintic, character tables through \(A_5\), the finite subgroups of \(\mathrm{SO}(3)\), and the linear-algebra appendices.

**Defers.** Dedekind domains as a general theory (Abstraction, and the number-field case in Book 13). The shuffle cutoff (Abstraction). Dirichlet's theorem (Book 6). Artin–Wedderburn beyond what Chapter 11 and Abstraction together cover; Abstraction owns Wedderburn. An abstract algebraic closure.

**Hands forward.** Characters of finite groups, Dirichlet characters as the abelian case, Jordan form, Frobenius, and the plate trick.

## Pages and effort

Baseline 372 pages. Target 370–400. Effort: moderate. The flagship proofs stay. The work is the polygon arithmetic, the part title for representations, one sentence of Fourier convention, and the appendix preface.
