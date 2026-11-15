# Separate review: Chapter 8, Group Cohomology

Reviewer: the agent who wrote Chapters 3 and 4, reviewing a different agent's chapter. Source mathematical/editorial review only; no human second reader, rendered inspection or production validation is claimed.

Reviewed SHA-256: `52cd813c90823a28d21b869ad0e3ae3ebbcd069ba154be088ad476255183ccac` for `volume10-abstraction/chapters/ch07-groupcoh.tex`. Compared every one of the eleven original formal statements and six original exercises with `starting-statement-content.json` at main `59014a9aad3454ad60786c6549c81fcac88df9df`; read the complete final prose, all proofs, all ten hints/solutions, both new figure sources, the protected figure/caption and bibliography.

**Result:** no unresolved mathematical or editorial finding in the reviewed sources. The writer's explicit repairs of scope, degree-one cyclic cases, base assumptions and relative Brauer terminology are correct. Parent owns exact typeset numbering, overflow, rendered figure and EPUB checks.

## Every original formal statement

| Label | Comparison with baseline and mathematical judgement |
| --- | --- |
| `def:cochains` | Same cochain groups, all three low-degree coboundary formulas and quotient definitions retained. The text limits the defined Hn to degrees zero through two, exactly the available coboundaries, and explicitly checks d² on degrees zero and one. Group actions are defined first. |
| `lem:normalised` | Original normalisation conclusion retained for every action. Cocycle identity gives f(1,k)=a and f(g,1)=g·a; the constant cochain has db(g,h)=g·a, so subtraction normalises both edges. |
| `prop:complements` | Same graphs of crossed homomorphisms and A-conjugacy iff coboundary. Projection is bijective for each complement, graph inverse follows from the cocycle equation, and conjugation computes f−da with correct sign. |
| `thm:hilbert90` | Full finite Galois statement, multiplicative and additive vanishing, retained. Independence of distinct automorphisms makes the weighted sum nonzero; reindexing gives f(sigma)=b/sigma(b), which is the principal cocycle of b^{-1}. Additive trace-one construction avoids division by |G| and therefore covers positive characteristic dividing the group order. |
| `cor:hilbert90` | Norm-one and trace-zero conclusions retained. Partial products/sums define the cyclic cocycles, including wraparound. Degree-one extension is checked separately, repairing the original proof's empty generator range rather than weakening its assertion. |
| `ex:pythagoras` | Same rational-circle parametrisation and denominator clearing retained. beta≠0, both endpoints, slopes and (3/5,4/5) example checked. Actual earlier reference is Volume 2 Theorem 8.1. |
| `thm:h2ext` | Full fixed-action classification and split zero class retained. Associativity gives the correct cocycle, change of section gives f+db, normalised crossed product has identity and explicitly verified inverses, and equivalences fix both ends. Both constructions are inverse; zero iff homomorphic section. |
| `thm:h2cyclic` | Isomorphism with A^G/N(A), not just set bijection, and every carry representative retained. Trivial group handled separately; for n≥2 extraction t^n, action invariance, norm change of lift, standard section and addition of f_a prove all assertions. |
| `ex:carry` | All b classes, standard carry cyclic extension, zero class direct product, generator order, cyclic iff unit and phi(b) count retained. New b≥2 convention is appropriate for a numeral base. Converse uses the exponent and abelianness, so it does not infer noncyclicity solely from the order of one element. |
| `prop:killed` | Full order-m annihilation in degrees one/two, any action/coefficient group, and finite coprime vanishing retained. Sums give mf=d(−b) and mf=dc with correct signs; Bézout kills each class. Trivial group and trivial coefficient group included. |
| `thm:sz` | Retains finite E, abelian normal A, coprime orders, existence and conjugacy of complements. H² supplies splitting, H¹ and the earlier graph proposition supply A-conjugacy, a stronger specification of the original conclusion. General nonabelian case remains explicitly quoted. |

## Every exercise, hint and solution

All original six labels/stars/number positions remain; four additions follow them, each with a unique label, rating, useful hint and full idea/writeup solution.

| Label | Review judgement |
| --- | --- |
| `ex:h1sign` | Sign action gives H0=0,H1=Z/2,H2=0; trivial action gives Z,0,Z/2. The nonzero extension and reflection interpretation agree with the formulas. |
| `ex:carry10` | All ten parameters classified. Exponents 100,20,50,10 and prime-primary decomposition give exactly the listed groups; four unit parameters produce distinct cyclic extension classes. |
| `ex:quaternion` | All sixteen cocycle entries checked against quaternion multiplication. Normalised coboundary diagonal must be +1, contradicting −1. Any order-four subgroup contains −1, so there is no complement, giving the second proof. |
| `ex:cyclich1` | Partial norm sums give precisely ker N; principal values give (sigma−1)A, including n=1. The “converse” is now explicitly the cyclic Galois converse, repairing the old ambiguous implication towards the general finite-Galois theorem. |
| `ex:artinschreier` | Trace(−1)=0 gives sigma(alpha)=alpha+1 with correct sign. The p conjugates are distinct; tower degree p gives L=K(alpha), and binomial characteristic-p identity gives the fixed constant. Includes p=2. |
| `ex:order20` | Unique Sylow five-subgroup and Schur–Zassenhaus give the semidirect decomposition. Three C4 actions up to automorphism and two V4 actions exhaust the list. Sylow-two type, abelianness and centre distinguish the five groups. The inversion action with C4 complement is the dicyclic order-20 group; centre calculation correct. |
| `ex:v10new-ch08-inversion` | Inversion on C4 gives H0=H1=H2=C2. Carry parameters t²=1 or u² yield D8 and Q8. All outside squares and the counts five/one involutions check. |
| `ex:v10new-ch08-affine` | T²+T+I=0, no integer invariants, and image(T−I)={coordinate sum 0 mod3} give 0,C3,0. Fixed point (2/3,1/3), affine order three and no integer fixed point checked. The cohomology obstruction uses the correct sign, whose image is unchanged under negation. |
| `ex:v10new-ch08-quadratic90` | b=1+x works when nonzero; x=1 and x=−1 are separately treated, including their coincidence in characteristic two. c−sigma(c) handles x=−1≠1. Finite-field quotient/kernel argument gives q+1 without assuming norm surjectivity or cyclicity. |
| `ex:v10new-ch08-averaging` | Inverse of multiplication by m commutes with the action and d by uniqueness. Applying it to the proved averaged identities supplies explicit primitives; arbitrary infinite coefficient groups/vector spaces are permitted. |

## Actual prerequisite checks and editorial coverage

Read actual Volume 3 Chapter 10 `lem:dedekind` and proof (printed Lemma 10.15): independence is over the field in every characteristic, precisely what the weighted-sum and trace-one arguments require. Read the earlier fixed-field theorem in that chapter. The Sylow and finite-abelian-group results in Volume 3 are available before this volume. The quoted Ext interpretation involves a possibly noncommutative group ring, and the text correctly says the general module version is outside the commutative-ring proof of Chapter 7 and is not used. No result from Volumes 11–15 or a later exercise is a hidden premise.

All prose, including short equation introductions, was read. Technical words (action, crossed homomorphism, complement, normalised, equivalence of extension, norm) are defined before reliance. The opening carry story states fixed action and fixed end identifications rather than promising classification of all groups of order 100. Nonabelian H¹ is distinguished as a pointed set, H² is correctly the relative Brauer group, and all advanced descent/Brauer/Feit–Thompson material is quoted. The close poses the concrete next representation-theory question.

## Preservation and figure checks actually performed

Source inventory: every original label present and unique, original formal environment order retained, 10 exercises/hints/solutions, three figure blocks total. The complete original `fig:rationalcircle` block matches the immutable captured block; original `figures/ch07-circle.tex` SHA-256 matches baseline. Numbered section source order retained.

Read both new figure sources and mathematical captions. Base-four table has c(x,y)=floor((x+y)/4) for all sixteen pairs, with rust cells precisely x+y≥4. The displayed triple (3,2,1) gives 1+0 versus 0+1 carries, both one. Reflection mirrors at x/2 move by one under translation by one, so the parameter changes by two and its parity is invariant; arrow orientations and the two mirror types are correct. Both use the approved palette. No photograph occurs here. These source checks do not replace actual rendered figure inspection or final printed-number verification.
