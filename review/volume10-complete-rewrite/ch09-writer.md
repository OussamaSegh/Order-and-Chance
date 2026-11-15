# Chapter 9 writer record

Scope: the complete printed chapter, including six original exercises, all hints,
all six idea/writeup solutions, history, transitions and ending. The rewrite was
read in full against starting main `59014a9aad3454ad60786c6549c81fcac88df9df`.
This is the writer's audit, not independent certification. No build was run by
this writing agent; parent owns production and the separate review.

Preservation: original statement/exercise order and all original labels retained;
the complete original Wedderburn figure block and figure source are unchanged.
All numbered sections retain their order. Quotations from Burnside and the
bibliographic records remain literal. No additional numbered formal statements.

Added figures (after the original figure):
- `v10-new-ch09-induction`: coset coordinates split into constants and the
  sum-zero plane for induction from S2 to S3; the mean projection is explicit.
- `v10-new-ch09-affine`: all twenty affine maps of F5, with unique fixed points
  computed as b/(1-a) and the five-element translation kernel distinguished.

Added Exercises 9.7–9.10: central idempotents in C[S3]; normal abelian induction
and the affine F7 character; real versus complex C3 algebras; A4 classes,
characters and integral central scalars. Each has stars, a hint, and a full
idea/writeup solution. They use only this chapter and earlier material.

Mathematical corrections and prerequisite repairs (fixing commit: to be assigned
by parent when committing this chapter):

1. `thm:burnsidepq` permitted p=q, while its proof treated a Sylow q-subgroup
   as having index p^a. If p=q its index is 1 instead. The statement remains
   valid for equal primes and now explicitly permits a,b>=0. The proof first
   handles equal primes and vanishing exponents as prime-power groups, then
   assumes distinct primes and positive exponents. No theorem is weakened.
2. `ex:doublecosets` lacked |G/H|>=2 in the equivalence with double transitivity.
   On a singleton, the usual distinct-pair condition is vacuous but the
   permutation module has no nontrivial irreducible summand. The pair-orbit
   equivalence is now stated for at least two points; the double-coset identity
   still holds without restriction.
3. Maschke's citation in the prose claimed every C[G]-module was semisimple,
   beyond the finite-dimensional proof of Volume 3. We only use and now claim
   the finite-dimensional version (all representations in this chapter).
   The original ring theorem, including its general division-ring assertion,
   retains its full hypotheses and conclusion.
4. `cor:mackeyirr` proof asserted <W,W>>=1 without handling W=0. The zero case
   is now disposed of before the norm argument; the criterion is unchanged.
5. Frobenius-kernel proof now handles H=1 explicitly and distinguishes
   chi(g)=chi(1), which forces the identity matrix, from equality only in
   absolute value, which forces merely a scalar. The original conclusion is
   unchanged.
6. `ex:centrefaithful` no longer needs to use a prior exercise as an unnamed
   theorem: a local proof of degree-divides-order follows directly from
   character orthogonality and Lemma 9.11. Tensor powers and the growing
   denominator argument are written out, with faithful and arbitrary parts
   separated.

Prerequisites actually inspected: Volume 3 `ch11-characters.tex`, Maschke,
Schur, orthogonality, class-count theorem, column orthogonality and the complete
solution of Exercise 11.8; `ch10-galois.tex` for cyclotomic/Galois fixed fields.
The algebraic-integrality arguments use the earlier current Chapter 5 labels
`cor:integralclosure`, `prop:integralcrit`; rational integrality is supplied
locally. Real division-algebra classification and Thompson's nilpotency theorem
are explicitly quoted and used in no proof.

Boundary audit includes zero ring/empty products in Wedderburn, zero inducing
module, trivial group, trivial Frobenius complement, q=2 affine group, n=2
Klein-four dihedral group, and a,b=0/equal primes for Burnside.

Source-only verification by writing agent: original figure block is an exact
substring; every baseline original label remains; ten exercise and three figure
environments occur (6+4 and 1+2). Parent must verify compiled numbers, layout,
EPUB and separate mathematical/editorial review. Numerical checks are illustrations,
not proof substitutes.
