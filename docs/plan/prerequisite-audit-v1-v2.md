# Volumes 1–2: prerequisite audit and editorial contract

**Audit date:** 2 November 2026  
**Audience:** readers beginning with high-school mathematics  
**Reading order:** as specified by each volume's current \`main.tex\`, not alphabetical filenames  
**Canonical voice:** \`docs/WRITING-STYLE.md\` and \`docs/agents/mathematician-writer.md\`

## The contract

1. The *foundations route* through Volume 1 requires high-school algebra, elementary geometry and the familiar functions of secondary-school mathematics, plus only the explicit starting assumptions in its preface. Proofs, sets, induction, sequences, complex numbers, polynomials, linear algebra, calculus and probability must be taught in the book, not presupposed as earlier courses.
2. The *foundations route* through Volume 2 assumes Volume 1 and nothing from Volume 3 or later. If the argument needs a new structure, define it with a worked example before using it. A reference to a future volume is a preview, not a proof.
3. A **marked optional bridge** may point ahead, but its statement must say what has not yet been taught. Such bridges cannot support a theorem used later on the main route. A reader should be able to complete the two-volume reading path while skipping all marked bridges.

This is a *prerequisite* audit, not an independent certificate that every mathematical claim in the manuscripts has received a new proof-by-proof verification. Typesetting and CI validation must be recorded separately.

## Chapter-by-chapter coverage

| Volume | Chapters read in book order | Prerequisite trajectory |
| --- | --- | --- |
| 1 | Language of Mathematics; Sums, Binomials and Induction; Counting and Discrete Reasoning | Logic and sets → induction and divisibility → finite counting |
| 1 | Sequences, Series and Limits; Orders; Complex Numbers and Roots of Unity | Completeness and convergence → order relations → complex arithmetic, an elementary definition of group and subgroup, roots of unity |
| 1 | Polynomials; Linear Algebra; Differential and Integral Calculus | Polynomials and roots → matrices and linear maps → proofs of calculus rules and Stirling's constant |
| 1 | Inequalities, Convexity and Estimates; First Probability | Inequality methods and estimates → elementary finite probability |
| 2 | Divisibility and the Euclidean Algorithm; Primes | Integer arithmetic and the additive subgroup test from Volume 1 → prime number theorems proved in the chapter |
| 2 | Congruences; Primitive Roots and the Multiplicative Group | Residue classes, commutative rings, fields and units → orders, generators and cosets |
| 2 | Quadratic Residues and Reciprocity; Arithmetic Functions | Multiplicative structure and earlier congruences → Legendre symbols, reciprocity and divisor sums |
| 2 | Sums of Squares; Continued Fractions and Pell's Equation; Diophantine Equations | Earlier integer results, Volume 1 complex arithmetic and elementary analysis |
| 2 | Gaussian and Eisenstein Integers; Characters, Euler Products and the Sieve | Complex arithmetic and integer factorisation → multiplicative functions, homomorphisms and finite character theory |

## Concrete defects identified and corrected

- **Volume 1, Roots of Unity:** the words *group* and *subgroup* previously appeared without a definition. A new introductory passage motivates operations using a square, states the group axioms, checks $(\Z,+)$ and its even subgroup, proves the subtraction test and defines cyclic groups and element order. The root-of-unity theorem now follows that passage.
- **Volume 2, Divisibility:** its first subgroup theorem now recalls and illustrates the Volume 1 definition. The chapter initially used *ideal* before a reader had met a ring; the proof is now expressed through integer combinations, and the general ideal terminology is only previewed.
- **Volume 2, Primitive Roots:** cosets and index were used without teaching them. The passage now defines cosets, proves disjointness/equality and equal size, and computes all four cosets of the square subgroup modulo 16 before returning to the general modulus $2^k$. The advanced solution involving an $\mathbb F_2$-vector space also explains the vector-space operations.
- **Volume 2, Characters:** the term *group homomorphism* is now defined and checked with the units modulo 4 before its use in Dirichlet characters.
- **Volume 1, optional polynomial bridges:** a small toolkit explains finite fields, multivariable polynomials, total/partial degree, bipartite graphs and perfect matchings. Nullstellensatz and Newton's inequalities are explicitly marked as return-after-later-chapters problems. The Erdős–Heilbronn problem includes the meaning of arithmetic modulo a prime.
- **Volume 2, optional reciprocity challenges:** the cyclotomic-factorisation problem explicitly warns that finite-field extensions are taught in Volume 3. A Gauss-sum challenge now states its extra ring and irreducibility prerequisites. Neither supplies a premise for the reciprocity theorem in the regular chapter.
- **Prefaces and canonical style:** now state the distinction between high-school prerequisites, tools built in the main progression and optional forward-looking challenges.

## Assumptions intentionally retained

Volume 1's preface expressly takes ordinary arithmetic and real-number completeness as starting points, along with standard identities for elementary functions and four basic properties of integration of continuous functions. These are **declared starting assumptions**, not unannounced use of undergraduate theorems. The author can make the book more foundational by constructing $\R$, $\exp$ and the integral in later work, but doing so is not necessary to keep the declared high-school entrance level.

Stirling's formula appears in Volume 1's sequences chapter with an explicit explanation that identifying its constant requires Wallis's integrals in the later calculus chapter. It is a visible deferred proof, not an assumed external result. The later chapter finishes the calculation.

The advanced bridge exercises and outlook remarks have a different purpose from the first-reading path. Some deliberately point to later parts of this series. This is acceptable only because they are identified as optional and not relied upon in the main line of argument.

## Review and future edit checklist

For every changed chapter, including its exercises, hints and solutions:

- Check its position in \`main.tex\`.
- Find the first use of each non-high-school mathematical noun and operation. Define, motivate and test it before first *required* use.
- Check every proof dependency against either an earlier chapter/section or a proof already supplied locally; do not use a theorem from a future volume as an unseen premise.
- Audit exercises individually. If an advanced exercise needs unbuilt tools, either supply a self-contained toolkit, move the exercise to the book that develops them, or label it as a clearly optional advanced bridge with named dependencies.
- Read changed text in the canonical friendly step-by-step voice; verify hypotheses and algebra line by line.
- Run the TeX build and manuscript tests before merging, and record failures instead of treating a source edit as proof of a successful published artifact.

**Audit status:** the explicitly identified progression gaps above are repaired in this PR. The complete proof-by-proof mathematical verification of every chapter, exercise and solution and a fresh successful PDF/EPUB build are separate acceptance checks; they should not be claimed from an editorial dependency scan alone.
