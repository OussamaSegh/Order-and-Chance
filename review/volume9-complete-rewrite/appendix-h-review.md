# Appendix H — rewrite and checking record

Status: full draft rewrite; combined PDF-only build passed; rendered figures inspected. Separate final
independent review and EPUB validation remain outstanding. This is a later
checking pass by the writer, not an independent certificate.

## Coverage

Rewrote the opening, every definition and numbered statement, every proof,
all twelve original exercises, hints and idea/writeup solutions, remarks and
closing guidance. The original epigraph, four figure blocks and bibliographic
records are literal. Section order, original labels and formal-environment
counts are unchanged. Two added figures follow the last original figure;
four exercises follow all original exercises.

## Corrections and prerequisite repairs

- Dimension-zero lattices have covolume one and no nonzero vector; no shortest
  length is asserted there. The strict-volume hypotheses are vacuous in that
  dimension. Empty/lower-dimensional convex sets cannot satisfy the positive
  volume threshold. The text gives a local measurability argument for bounded
  convex sets before using their volume.
- The index/covolume argument needed in D_n and E8 is now supplied locally before
  use, including basis existence from the earlier subgroup theorem, rather than
  relying only on a later exercise solution.
- The circle-counting solution no longer uses a negative inner radius for
  1<=r<sqrt(2). It handles that range separately and retains the full original
  bound and limiting conclusion.
- The projected-basis step in Hermite's solution proves real independence,
  which is needed for a lattice, not merely integer independence. The quotient
  torsion-free argument uses the established intersection with the shortest line.
- The Fibonacci explanation no longer claims every rounded step advances exactly
  two indices. The exact vector operations are displayed.
- The even-dimensional shifted D_n exercise explicitly retains n>=3 from D_n's
  definition. Its n=4 and n=6 density ratios are given exactly, and the improvement
  statement covers every even n in scope.
- Optimality among unrestricted packings, the dimension-24 theorem and the
  dimension restriction on positive-definite even unimodular lattices are clearly
  quoted results. Constructing E8 is not presented as a proof of optimality.

## Mathematical checks

Blichfeldt uses finitely many measurable cell pieces and a genuine nonzero
lattice difference. Minkowski takes a midpoint of 2x and -2y. The Fermat proof
checks the congruence, nonzero norm and strict bound <2p. Reduced-basis existence
uses a primitive shortest vector and Bezout extension. The shortest-vector
estimate in a reduced basis uses a positive INTEGER quadratic expression.
Both equality conditions in the determinant bound are retained. General discs
have radius at most the touching radius; equality in the density bound requires
that largest radius as well as the hexagonal lattice.

The D_n roots and covolume are checked before E8. The half-integer coset is a
group because 2h lies in D8. Evenness in both cosets gives integrality by
polarisation. All 112 integer roots and 128 parity-constrained half-integer
roots are counted; no smaller norm is possible. The extension of four-square
representations from primes invokes the earlier quaternion norm identity,
confirmed in Volume 3's quaternion chapter and Exercise `ex:euler4`.
The direct prime proof does not need that extension. Gauss reduction's stopping
rule avoids the half-integer tie cycle. Kissing uses pairwise nonoverlap of
interiors and cyclic angular gaps. Hermite's lift is nonzero because its
projection is nonzero; all determinant exponents and the final power are checked.

## Added material

- `v9-app-h-folding`: two different pieces in adjacent cells; translating the
  rust one by (-1,0) gives a positive overlap. The caption does not falsely
  identify the entire pieces as exact translates of one another.
- `v9-app-h-basis-reduction`: u=(1,0), v=(2.4,1), v'=(0.4,1), determinant one
  before and after, with the reduced inequalities checked explicitly.

Four two-star exercises have unique labels, hints and full idea/writeup solutions:

- `geometry:ex:v9-closed-minkowski`: threshold case by compactness and a repeated
  nonzero lattice point; the open-cube counterexample isolates the failed step.
- `geometry:ex:v9-dual-lattice`: exact dual basis, reciprocal covolume, bidual,
  and self-duality of E8, with finiteness of the relevant index justified.
- `geometry:ex:v9-complex-lattice`: integer multiplication matrix, covolume,
  index, shortest length and packing density; a scale change cannot improve it.
- `geometry:ex:v9-reduction-domain`: both basis operations, preservation of
  orientation, modular-region inequalities, determinant formula and all sharp
  equality cases. It uses the earlier reduced-basis theorem, not a later premise.

No numerical illustration is used as proof. Full build exit, preservation and
rendered inspection are pending; they will be recorded when actually completed.

## Actual intermediate validation

The four-unit plus front/back matter PDF-only build exited 0 at **403 print
pages**, with 581 whole boxes checked (maximum 318.2 pt), no overflow or
unresolved references, and passing font, reading-PDF, print and cover checks.
The preservation checker passed all 544 original printed labels/captions and
57 original figure files. Both added H figures were inspected on rendered
manuscript PDF page 349; the cell overlap, arrows, vector directions, equal-area
parallelograms, labels and captions were legible and consistent. The rendered
text includes the dimension-zero clarification. `check_appendices.py` exited 0;
its numerical examples are illustrations, not proof verification.
`git diff --check` passed. EPUB and exact-final-head CI remain unverified.

## Later draft-check repair

The new non-strict compact Minkowski exercise explicitly assumes n>=1 and now
asks for the dimension-zero exception as well. For n=0, C=Lambda={0} meets the
threshold but contains no nonzero vector; dilation cannot make its volume strict.
The solution gives this counterexample. This fixes a boundary omission in the
new exercise, not a false statement on starting main. Original strict Minkowski
and Blichfeldt statements remain valid and vacuous in dimension zero.
