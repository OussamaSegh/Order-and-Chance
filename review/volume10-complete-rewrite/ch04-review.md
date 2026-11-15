# Chapter 4: separate mathematical and editorial source review

Reviewer: `/root/rewrite_ch09_ch10`, a different agent from this chapter's writer.
The complete final chapter was read, including every proof, unboxed example,
short formula introducer, exercise, hint, solution, historical paragraph, ending
and bibliography. Every original statement was compared with its full baseline
block in `starting-statement-content.json`, starting main
`59014a9aad3454ad60786c6549c81fcac88df9df`.

**Source review passed after repairs.** Reviewed final chapter SHA256:
`dcdaebe0b363f0cf73b1ae0d2d4da81454de3fa7cdc6fd6a4e06063bbebf8229`.
This is a separate source-level mathematical/editorial review, not a rendered-page,
PDF, EPUB or publication certificate. Parent owns those checks.

## Findings and recheck

1. The new prose definition of a reduced Gröbner basis excluded only the
   non-leading monomials from divisibility by another generator's leading
   monomial. Under that wording, {1,X} would qualify for the unit ideal,
   contradicting the subsequent assertion that its reduced basis is {1}.
   Parent's fixing commit `ee5c8ac6` changes the definition to exclude **every**
   monomial of one generator from divisibility by another leading monomial.
   Re-read the exact repaired sentence and verified it rules out {1,X} while
   allowing {1}. No numbered statement or numbering changes.
2. The two-colour counterexample at characteristic 2 correctly disproved the
   characteristic restriction, but its final sentence called this the 'field
   hypothesis'. The same commit changes that wording to 'characteristic
   assumption'. Rechecked the final characteristic-2 triangle assignment and
   the preceding characteristic-not-2 odd-cycle certificate.

Both findings are closed. The writer's earlier corrections (discriminant
transformation hypothesis, finite fields, elimination overclaim, zero leading
monomials and characteristic-independent evaluation) were also checked below.

## Every original numbered statement

Baseline printed numbers and labels are retained in the same order. No original
valid mathematical conclusion was silently weakened.

| Number and label | Concrete mathematical comparison and verification |
| --- | --- |
| Proposition 4.1 `prop:noetherian` | All three ideal conditions, nonempty-family quantifier and module counterparts retained. Union-of-chain ideal and finite-generator stage valid; no-maximal sequence contradicts ACC; finitely generated subideal maximality forces equality. Zero/empty generation handled. |
| Proposition 4.2 `prop:noethmodules` | Both directions of exact-sequence equivalence and both finitely generated/submodule consequences retained. Stabilising intersection and quotient-image chains together force each step of the middle chain to stabilise. Induction begins at R^0. |
| Theorem 4.3 `thm:hilbertbasis` | General Noetherian coefficient rings, repeated finite variables, K and Z, and finitely generated algebras all retained. Degree-d leading-coefficient ideals include zero, so scalar annihilation over zero-divisor rings is valid. Finite degrees through stabilisation N give generators; cancelling leading terms gives degree induction. n=0 included. |
| Corollary 4.4 `cor:finitesystem` | Arbitrary equation set and a finite **subset of that set**, not merely a finite set of ideal generators, retained. Collecting finitely many original equations from generator expressions proves the stronger subsystem claim. Empty system handled. |
| Proposition 4.5 `prop:zariski` | Both extreme sets, finite union/product ideal, arbitrary intersection/sum ideal and V(I(Y))=Y retained. Converse union argument uses a field to prevent a nonzero product vanishing. Closed-set recovery does not require algebraic closure. |
| Definition 4.6 `def:irreducible` | Nonempty requirement, two equivalent topological conditions and descending-closed-chain Noetherian definition retained. |
| Proposition 4.7 `prop:components` | Ambient and every subspace Noetherianity, closed-set irreducibility iff prime vanishing ideal, and finite unique irredundant components retained. Closure-of-subspace-chain argument valid; empty set has improper vanishing ideal and is not irreducible. Minimal counterexample splits; mutual containments prove uniqueness, not just existence. |
| Lemma 4.8 `lem:artintate` | All three-ring inclusions, A Noetherian, finite A-algebra and finite B-module assumptions retained. Finite coefficient ring B0 handles products of module generators; including constant 1 makes C finite over B0. B is a B0-submodule of finite C, hence finite; adding its module generators gives finite A-algebra generators. |
| Theorem 4.9 `thm:zariskilemma` | Field L finitely generated as K-algebra implies finite extension, unchanged. Maximal algebraically independent subset of a finite generator list yields finite extension of its rational-function field. Artin–Tate would make that field a finite K-algebra, contradicted by an irreducible denominator not dividing q. Euclid-type infinitude of irreducibles works also over finite K and r≥1. |
| Theorem 4.10 `thm:weaknull` | Algebraic closure, every proper ideal, nonempty zeros, and complete maximal-ideal description retained. Evaluation kernel proved by difference of powers in every characteristic. Field quotient is finite by Zariski lemma and hence K; Noetherian maximal-element argument places arbitrary proper ideal inside such a maximal ideal. n=0 handled. |
| Theorem 4.11 `thm:nullstellensatz` | Every ideal J and full equality I(V(J))=rad(J) retained. Field has no nonzero nilpotents for one inclusion. For nonzero f, auxiliary 1−Yf ideal has no zero; weak Nullstellensatz gives polynomial identity; substitution in the fraction field and multiplying by positive f-power clears denominators. f=0 handled separately. |
| Corollary 4.12 `cor:dictionary` | Inverse inclusion-reversing radical/closed bijections and prime/irreducible, maximal/point correspondences retained. Both inverse identities proved using earlier results with matching hypotheses. |
| Definition 4.13 `def:monomialorder` | Total order, 1 least, multiplication compatibility and LM/LC/LT for **nonzero** polynomials retained. Lex and graded reverse lex examples agree with conventions. |
| Lemma 4.14 `lem:dickson` | Finite subset of original monomial generating set and resulting well-order property retained. Monomial membership test is proved before use; divisibility makes a finite least generator least in arbitrary nonempty M. No circular use of Gröbner termination. |
| Proposition 4.15 `prop:division` | Nonzero divisor list, remainder nondivisibility, representation and leading-product bounds retained. Bound only invokes LM(f) for f≠0; f=0 given zero decomposition. Maintained identity, leading cancellation/move-to-remainder and well-order termination all checked. |
| Definition 4.16 `def:groebner` | Finite set inside a nonzero ideal and equality of full leading-monomial ideals retained. Zero generators excluded explicitly; empty list convention extends to zero ideal without changing nonzero claims. |
| Proposition 4.17 `prop:groebnerprops` | Existence, generation, unique remainder under choices, and membership iff zero remainder all retained. Difference of two reduced remainders still has only standard monomials; a nonzero difference in I would contradict its leading ideal. |
| Lemma 4.18 `lem:cancel` | Equal top monomials, cancellation including p=0, and K-linear combination of lower S-polynomial multiples retained. LC normalization and telescoping partial sums correct. Repeated generators give zero differences; empty/one-summand cases explicitly zero. |
| Theorem 4.19 `thm:buchberger` | Both directions of pair remainder criterion retained, with empty zero-ideal extension. Minimal maximal-leading-monomial representation exists by established well-order. All top cancellations rewritten via the lemma; division bounds on each zero-reducing S-polynomial strictly lower every replacement. Contradicts minimality. |
| Corollary 4.20 `cor:buchalg` | Adding nonzero remainders preserves generated ideal and strictly grows leading ideal. ACC forces finitely many additions; no unresolved pair then gives criterion. Finite/nonzero input and empty zero ideal now explicit, preserving original valid finite algorithm. |

## Every original and added exercise/hint/solution

All ten exercises have unique labels, stars, one useful semantic hint and one
complete idea/writeup solution. All solutions were checked independently.

| Exercise | Concrete verification |
| --- | --- |
| 4.1 `ex:nonnoeth` | In subring K[X,XY,...], nonconstant coefficients add an X factor. Thus XY^(k+1) cannot lie in ideal (XY,...,XY^k); the explicit strictly ascending chain proves non-Noetherianity. |
| 4.2 `ex:radicals` | Two diagonal lines for X²−Y²; three axes for pairwise coordinate products. Quotient domains establish irreducibility. V(X²Y,XY²)=V(XY), and radical (XY) verified by a power and containments. |
| 4.3 `ex:notproduct` | Infinite field essential: cofinite product basic opens meet diagonal, so diagonal is dense but not product closed. It is polynomial closed in plane; coordinate projections prove comparison of the two topologies before strictness. |
| 4.4 `ex:realnull` | Sum of real squares makes one equation, including empty list. X²+1 refutes weak version; J=(X²+Y²) has real zero only origin but X is not radical-member, as complex substitution (1,i) refutes any power identity. |
| 4.5 `ex:colouring` | Vertex cube roots distinct in C; edge polynomial zero precisely for different roots, equal value gives 3x²≠0. Weak Nullstellensatz gives proper-ideal equivalence. Empty graph case checked. |
| 4.6 `ex:groebnerhand` | All S-polynomial cancellations checked by expansion. Result {X²−Y,XY−X,Y²−Y} has LMs X²,XY,Y². Zeros (0,0),(1,1),(−1,1). Standard basis 1,X,Y and evaluation coordinates (a,a+b+c,a−b+c) give quotient C³, proving radicality rather than inferring it just from the points. |
| 4.7 `ex:v10new-ch04-finitefield` | Monic reductions leave degrees<q individually. Root-bound induction proves reduced vanishing polynomial zero. Lagrange products interpolate every function; quotient product of fields proves radicality and arbitrary subsets closed. n=0 unique empty tuple and zero ideal handled. |
| 4.8 `ex:v10new-ch04-elimination` | Principal LM multiplication proves singleton GB of (XY−1). No pure-Y nonzero ideal element; projection precisely K\{0}. For infinite K, this is proper, infinite, dense and nonclosed. Does not incorrectly identify projection with zero set of elimination ideal. |
| 4.9 `ex:v10new-ch04-squarezero` | Radical (X,Y), point zero set over any field, basis 1,X,Y. Positive-degree ideal square zero; inverse a^-1−a^-2u valid for a≠0, nilpotent cannot be unit for a=0. |
| 4.10 `ex:v10new-ch04-twocolours` | Distinct roots ±1 require char≠2; common zero iff proper colouring and weak Nullstellensatz supplies ideal version. Odd-cycle alternating edge sum 2X0, then X0*(sum/2)−(X0²−1)=1 is explicit certificate. All-ones triangle in char2 shows failure. Terminology finding repaired. |

## Whole-prose and prerequisite review

The reader gets a small system before the Noetherian statement, actual parity of
leading coefficients in the zero-divisor basis proof, examples of empty/nonempty
zero sets, radical/nonradical quotients, a correct nonunique-division example,
and an honest elimination conclusion. Short introductions name the objects and
jobs. Formula clauses were read as well as long paragraphs. No theorem proof
silently borrows a later exercise or later unit. The displayed staircase candidate
is explicitly left for computation in its exercise; no theorem uses its unproved
GB status. Its caption previews the quotient basis with the exercise named.

Writer corrections checked: discriminant invariant only under determinant-one
changes, with determinant-squared scaling generally; two-axis irreducibility
requires infinite K, finite fields explicitly separate; lexicographic elimination
need not give a nonzero last-variable equation; leading monomials are used only
for nonzero polynomials. The preserved real nodal-cubic caption is now supported
by a direct fraction-field nonsquare/Gauss argument and real vanishing-ideal proof
using both branches for infinitely many positive X. Thus irreducibility is not
inferred from the picture.

Actually inspected earlier sources: Volume 3 ring quotient/CRT Theorem 6.9,
polynomial UFD Theorem 6.18, module subobject correspondence and PID context in
Chapter 7, field extensions in Chapter 8 and finite fields in Chapter 9; Volume 7
Chapter 3 supplies cofinite/product/subspace topology. Required topological
properties are also explained locally. Current Chapter 3 exact sequences precede
the first module extension proposition. No proof uses Volumes 11–15.

## Figures and photograph

Read both new figure sources and captions completely. Multiplicity picture
correctly distinguishes K[X]/(X) from K[X]/(X²), with the same one-point zero set.
Staircase picture has standard monomials 1,X,Y and all marked excluded monomials
divisible by X²,XY or Y²; axes are exponent axes with the correct orientation.
Both use the approved palette, appear after the original varieties block, and
are referred to in explanatory prose. Source comparison confirms the complete
original figure block and all original figure-file hashes are unchanged. Counts
are exactly 6+4 exercises and 1+2 numbered mathematical figures. The portrait
macro has no caption/counter increment, so it does not insert a figure number.

I separately opened [the Commons Hilbert file page](https://commons.wikimedia.org/wiki/File:Hilbert.jpg)
on 15 November 2026. It identifies David Hilbert and an anonymous Göttingen faculty
postcard published for students in 1912, with Reid's biography as its evidence.
It displays PD-1923 for US pre-1931 publication and PD-anon-70-EU for anonymous
publication without a timely authorship claim. The adjacent chapter credit
identifies subject, date, postcard/source and public domain; photos/CREDITS.md
contains full URLs and the licensing evidence.

A separate live download of the Commons original matched the repository image
byte-for-byte (Python urllib/Pillow check exit 0): 437×592 pixels, SHA256
`e0510813434980c4f93329694b0816770d388aacb27f0d83b88588cbc119a930`.
The source portrait macro caps height at 1.65 in with aspect ratio retained,
giving at least 592/1.65 = 358.79 effective ppi. This source calculation does
not replace parent's measurement of the actual rendered image placement.

## Actual reviewer commands and limits

Python source comparison exited 0: original blocks, original labels, figure-file
hashes and section order checked against immutable records. Citation resolver
command recorded in ch03-review.md exited 0 and located the expected earlier
statements. SHA256 was recomputed after fixing commit ee5c8ac6; repaired passages
were reread. No local build or numerical experiment was run by this reviewer.
Rendered figures/photo, layout, final built numbering, EPUB and publication must
pass the parent's separate verification.
