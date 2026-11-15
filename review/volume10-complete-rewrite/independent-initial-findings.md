# Independent initial reading: Volume 10

Reviewer: the `independent_review` agent, separate from all manuscript writers.
Baseline main: `59014a9aad3454ad60786c6549c81fcac88df9df`.
This is an initial source reading, not certification of the rewritten final book.
No builds, rendered-page inspections, CI or publication checks are claimed here.

## Scope

Read root instructions, the writing style and mathematician-writer instructions,
interior design, the actual `main.tex`, all eleven baseline chapters including
exercises, hints and solutions, and front/back matter. Printed order is Categories;
Tensors and the Cost of Multiplying Matrices; Tensors and Exactness; Noetherian
Rings; Localisation; Dedekind Domains; Homological Algebra; Group Cohomology;
Semisimple Algebras; The Symmetric Group; Compact Groups. There are no appendices.
Some source passages were read through inherited parent context and the remainder
through direct source reads. Findings were sent to the owning writer before edits.

## Findings to fix and recheck

1. Chapter 1, matrix category: matrices do act on coordinate vector spaces. The
   claim that a morphism is not a map between anything is misleading.
2. Chapter 1, size conventions: natural-transformation families range over all
   objects, so saying every argument uses finitely many Hom-sets is inaccurate.
   Explain local smallness and the set-sized Yoneda parametrisation.
3. Chapter 1, Cayley example: distinguish right translations as natural maps from
   the faithful left action; evaluation at the identity proves faithfulness.
4. Chapter 1, nonnaturality wording: a suitable scalar with square different from
   one obstructs natural duality. Identity scalars themselves satisfy the equation.
5. Chapter 2, rectangular Kronecker proof: the product of two rectangular diagonal
   matrices under Kronecker need not be diagonal in ordinary row/column ordering.
   Independent row/column permutations put it in diagonal form; conclusions hold.
6. Chapter 2, rank-limit discussion: specify real/complex Euclidean topology.
7. Chapter 2, exponent theorem: require integer block size k at least two.
8. Chapter 2, entropy equality: equality at log(min(m,n)) requires full Schmidt
   rank min(m,n), as well as equal nonzero coefficients.
9. Chapter 2, no-approximation exercise: first rank-one term has norm
   (1+epsilon^2)^(3/2)/abs(epsilon), not exactly 1/epsilon; both diverge at that rate.
10. Chapter 2, Waring exercise: specify real or complex field (or a suitable
    characteristic restriction); the symmetric tensor/polynomial identification
    used in the solution fails in characteristics two and three.
11. Chapter 2, grid Laplacian solution: give the rectangular condition number
    requested before its square-grid asymptotic.
12. Chapter 2, Strassen threshold: justify the all-later-powers claim, beyond
    evaluating the two sizes 512 and 1024.
13. Chapter 3, composite-kernel exercise: the displayed snake sequence and verbal
    identification disagree about the connecting-map location. The claimed exact
    sequence is valid; a direct map-by-map exactness proof repairs the solution.
14. Chapter 3, Hom cyclic calculation: require positive m,n. For n=0,m positive,
    Hom(Z/m,Z)=0 rather than Z/m, so the unspecified boundary is false.
15. Chapter 3, bilinear prose: zero bilinear maps can be jointly linear. Say that
    bilinear maps generally are not jointly linear; specify the two-by-two
    determinant in the list of bilinear examples.
16. Chapter 4, invariant example: the discriminant scales by determinant squared
    under general linear substitutions. Use determinant-one changes or say
    relative invariant.
17. Chapter 4, lexicographic elimination: a general Groebner basis need not contain
    a nonzero univariate last polynomial. The ideal (XY) is a counterexample.
    State the elimination property and its actual hypotheses for solving.
18. Chapter 4, Groebner definition/algorithm: leading monomials require nonzero
    inputs, and the algorithm starts with a finite list. Handle the zero ideal.
19. Chapter 5, Noether normalisation: explicitly require a nonzero K-algebra,
    since the zero algebra is otherwise allowed by the ring conventions and
    cannot contain a copy of K[z_1,...,z_d].
20. Chapter 5, geometric normalisation: surjectivity on K-rational points needs
    algebraically closed K. Over R the algebra R[x,y]/(x^2+y^2+1) is finite over
    R[x], but has no real points. Spectral surjectivity holds over arbitrary K.
21. Chapter 6, Z[sqrt(-5)] example: it currently uses trace and integral-closure
    statements printed later in the chapter. Supply their needed local arguments
    before the example, or prove Dedekind properties directly.
22. Chapter 6, cubic arithmetic: the Dedekind property is used before the proof
    deferred to the later exercise. Supply the squarefree-cubic trace/norm proof
    locally before using ideal factorisation.
23. Chapter 7, higher Ext: equivalence of longer Yoneda extensions uses zigzags,
    not the preceding middle-term isomorphism definition. Label the result quoted.
24. Chapter 7, de Rham comparison: linear-algebra duality is not the de Rham
    comparison theorem. Distinguish the algebraic duality from the later quoted
    differential-form/topological comparison.
25. Chapter 8, opening H2 classification: fix the trivial action and equivalence
    relation; H2(C10,C10) does not classify extensions with all possible actions.
26. Chapter 8, cyclic order-one case: t=(0,sigma) is identity when n=1, and the
    proof assertion t^n=(a,1) is false for arbitrary a. The theorem remains true
    because N=id and H2=0; handle n=1 separately.
27. Chapter 8, Brauer terminology: H2(G,L*) is the relative Brauer group Br(L/K),
    the kernel of Br(K) to Br(L), not generally all of Br(K).
28. Chapter 8, cyclic H1 converse: it recovers the cyclic case of Hilbert 90, not
    the theorem for an arbitrary finite Galois group.
29. Chapter 9, Burnside proof: handle p=q as a p-group before treating Sylow q
    subgroups as having order q^b. State nonnegative integer exponents.
30. Chapter 9, double transitivity exercise: exclude the singleton coset action
    in the trivial-plus-one-irreducible characterisation.
31. Chapter 9, Maschke scope: the earlier cited averaging proof concerns finite
    dimensional representations. Restrict the explanatory claim accordingly or
    prove its arbitrary-module extension rather than assume it.
32. Chapter 10, modular aside: the nonzero simple Specht quotient criterion is
    known (p-regular partitions), not an open problem. General decomposition
    numbers are difficult; quote the distinction accurately.
33. Chapter 10, cover description: the current cover is the snake lemma, not a
    Plancherel diagram. Repair the obsolete prose without touching artwork.
34. Chapter 10, small cases: (n-1,1) requires n at least two; define the empty
    partition/tableau convention f^empty=1 for recursions and Chapter 11 a=0.
35. Chapter 11, finite trace law: the trace of a fixed-size Haar unitary matrix
    is not exactly Gaussian. Its absolute value is at most n. The Gaussian law
    is a limit; the variance is exactly one.
36. Chapter 11, exercise dimensions: require n at least two for weight
    (1,0,...,0,-1); distinguish exterior powers with k>n (zero) from irreducibles.
37. Chapter 11, SU2 exercise: specify integer m at least zero and the continuous
    endpoint values of the sine quotient at alpha=0,pi.
38. Chapter 11, general Peter-Weyl extension: the supplied elementary proof uses
    a faithful defining matrix representation. The extension to all compact
    groups is a quoted stronger theorem, not the same supplied proof.
39. Chapter 11, Schur orthogonality: choose one representative of each
    isomorphism class, or discuss equivalent representations in compatible bases.
40. Chapter 11, spherical harmonics aside: the sphere is a homogeneous quotient
    of SO3; density on the group is not literally the same statement. Explain
    quotient averaging or remove the unsupported identification.
41. Jacket copy: increasing run and increasing subsequence are different;
    the theorem concerns subsequences. The promise that every theorem is proved
    is inconsistent with explicitly quoted advanced results.

## Core arguments checked in this initial phase

The local Yoneda and adjunction arguments; the slice-test rank proof and
Strassen identities; the snake lemma, tensor-Hom proof of right exactness and
Baer criterion; Hilbert basis including zero divisors, Artin-Tate, Zariski lemma,
weak/strong Nullstellensatz and Buchberger cancellation; localisation,
lying-over/going-up, primary decomposition; Dedekind equivalences, trace
integral-closure proof and fundamental identity; comparison/horseshoe,
Tor/Ext long exact sequences, Ext classification and finite free UCT;
Hilbert 90, cocycle extensions and abelian Schur-Zassenhaus; Wedderburn,
induction/Mackey, Burnside norm argument, Frobenius kernel; Specht
irreducibility/completeness, standard polytabloid independence, insertion,
Schensted invariant and hook walk; matrix-group Peter-Weyl, alternants,
Weyl character formula, power traces, Pieri and trace moment calculation.
The findings above qualify this list; listing an argument does not certify
unread future changes.

Actually inspected earlier prerequisite sources include Volume 7 Theorem 4.19
(complex Stone-Weierstrass), Volume 8 Theorem 13.11 (circle characters) and
Volume 6 Lemma 9.6 (full Gaussian moments-to-law argument). Their printed numbers
were checked with the existing statement walker, and their actual proofs read.
The final review must add a complete frozen-source comparison, all new exercises
and figures, photos/source evidence, full cross-reference/prerequisite audit and
production evidence supplied by the parent. No final acceptance is recorded.

Additional prerequisite read: Volume 3 Theorem 8.20 (primitive element) is stated
for subfields of C and its proof chooses c in Q. Chapter 6 must give the short
adaptation over an arbitrary infinite base field K with separable roots in a
splitting field, rather than invoke the earlier statement for positive
characteristic. The finite forbidden-coefficients argument does adapt, preserving
the full finite-separable integral-closure theorem. The owning writer was notified.
Volume 3 Lemma 10.15 (Dedekind independence) was also read and is genuinely valid
for automorphisms of an arbitrary field; no extra characteristic restriction is
needed for Chapter 8 Hilbert 90. Volume 3 Maschke's actual proof was read and does
use finite-dimensional termination, confirming finding 31's scope distinction.
