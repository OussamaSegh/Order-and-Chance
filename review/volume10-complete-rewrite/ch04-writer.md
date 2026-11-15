# Chapter 4 writer record

Owned source: `volume10-abstraction/chapters/ch03-noetherian.tex` (printed Chapter 4).
Baseline main: `59014a9aad3454ad60786c6549c81fcac88df9df`.

All explanatory prose, all 20 original formal statements, complete proofs, examples, original exercise instructions, hints, idea/writeup solutions and closing bridge have been rewritten in a complete writer pass. The original varieties figure block is inserted byte-for-byte from the captured source; original bibliography records and Gordan's literal quotation are preserved. All original statement environments, labels and order, original six exercise positions, and numbered section order are unchanged. Parent owns fixing-commit hashes and actual production receipts; this writer record is not an independent review or a build pass.

## Explicit corrections and clarifications

- **C04-1: invariant hypothesis.** Original historical example said the discriminant `b²−4ac` of a binary quadratic form does not change under a linear change of variables. A change `x -> 2x, y -> y` over the reals multiplies the discriminant by 4. The text now specifies determinant-one changes for invariance, and gives determinant-squared scaling for general invertible changes. The original historical point remains; the missing transformation hypothesis is repaired.
- **C04-2: finite-field irreducibility.** Original prose identified the two axes as the irreducible components of `V(XY)` over an unspecified field `K`. For finite `K` the line Zariski topology is discrete; an axis has several closed points and is not irreducible. The rewrite specifies `K` infinite for the two-axis assertion, proves the vanishing-ideal identification there, and explicitly describes the finite-field exception. The numbered components proposition was already valid and keeps its full hypotheses and conclusions.
- **C04-3: overclaim about elimination.** Original prose asserted that a lexicographic Gröbner basis is triangular, that its last elements involve only the last variable, and that the system can be solved one variable at a time. This fails for positive-dimensional ideals such as `(XY)`, whose intersection with `K[Y]` is zero. The rewrite proves the actual elimination statement `G ∩ K[X_n]` is a Gröbner basis of `I ∩ K[X_n]`, with an empty basis allowed, then explains why a non-zero elimination equation is not guaranteed. The original three-point exercise still supplies the finite solving example. No numbered theorem is weakened.
- **C04-4: undefined leading-monomial boundary cases.** Original division proposition applied `LM(f)` to `f=0`. It now states the bound for `f≠0` and explicitly gives the zero decomposition for `f=0`. The Gröbner-basis definition now excludes zero generators and specifies the empty basis for the zero ideal; Buchberger's algorithm starts with a finite non-zero list, discards zero inputs, and handles the zero ideal. Original non-zero assertions, conclusions and labels are retained. Finite input is required for the finite list of pairs and is already available from Hilbert's basis theorem.
- **C04-5: characteristic-independent evaluation proof.** The weak Nullstellensatz's old parenthetical “Taylor expansion” is replaced by successive polynomial substitutions and the difference-of-powers identity. This gives the actual ideal-generation argument over every characteristic, without differentiability or factorial division assumptions.

## Proof and prerequisite coverage

The full writer proof pass checked Hilbert basis over coefficient rings with zero divisors; empty lists and zero modules in the Noetherian equivalences; subspace Noetherianity; the empty-set exclusion in irreducibility/primality; Artin–Tate's extra constant module generator; the difference between field generation and algebra generation in Zariski's lemma; all proper-ideal/maximal-ideal steps; `f=0` and `n=0` in Nullstellensatz; finite monomial supports, well-order termination, cancellation normalisation and minimisation in Buchberger's criterion. The real nodal-cubic claim in the preserved caption is supported by a new direct irreducibility/vanishing-ideal explanation, using both real branches for infinitely many positive `X`.

Read actual earlier material: Volume 3 Chapter 6's quotient, CRT and polynomial-UFD results; Volume 3 Chapter 7's module correspondence and PID structure theorem; the finite-field group material in Chapter 9; the topology references in Volume 7 are only definitions of cofinite/product/subspace topology, whose needed properties are also explained locally. All numbered internal dependencies precede their use. No later exercise is used as a premise: the staircase description explicitly says the displayed list's Gröbner-basis computation is still to be proved in its exercise, while the illustration only identifies its leading monomials.

## Additions

Exactly two new mathematical figure sources and blocks, both after the original varieties figure:

1. `v10-new-ch04-multiplicity.tex`: the different quotients by `(X)` and `(X²)` over the same zero set.
2. `v10-new-ch04-staircase.tex`: standard monomials `1,X,Y` for leading ideal `(X²,XY,Y²)`.

Exactly four new graded exercises after the original six, each with hint and complete idea/writeup solution:

- `ex:v10new-ch04-finitefield`: all polynomial functions on a finite affine space, unique reduced representatives, vanishing ideal, radicality and discrete topology, including `n=0`.
- `ex:v10new-ch04-elimination`: hyperbola projection, zero elimination ideal, dense nonclosed image.
- `ex:v10new-ch04-squarezero`: a three-dimensional square-zero quotient, units and radical.
- `ex:v10new-ch04-twocolours`: a two-colour polynomial model, explicit odd-cycle certificate, characteristic-2 counterexample.

The requested unnumbered Hilbert portrait macro is placed after the first substantive Hilbert discussion. Parent supplied and owns identification, public-domain evidence, original image file, credits and resolution validation. No separate historical-image verification is claimed by this writer.

## Checks actually run

A source inventory compared all original formal-environment counts, all original labels, and the entire ordered numbered-section list against the initial source: counts and order match, and no label is missing. The original figure block was copied verbatim. An intermediate parent build identified an unsupported arrow style in the separate Chapter 3 new lifting diagram; it has been replaced by a normal arrow labelled “inclusion”. I have not run a build or claimed rendered inspection. Separate final mathematical/editorial review and production checks remain parent tasks.

## Integrated fixing commits

b03ed741 (mathematical rewrite), ee5c8ac6 (reduced-basis precision). These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
