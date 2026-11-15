# Chapter 1 separate source review

A different agent from the Chapter 1 writer read the complete final chapter in a
separate review phase: every short formula introduction and longer paragraph,
all 23 original numbered formal statements against their immutable original text,
every proof and worked example, and all six original plus four new exercises,
hints and complete idea/writeup solutions. This is a **source-only** review; no
rendered interior page, photograph, EPUB or build was reviewed by this agent.
Parent owns those final artifact checks.

Per-statement and per-exercise judgments, baseline printed numbers and exact
reviewed source/block hashes are in `ch01-statements.json`.

## Mathematical findings and repairs

- The replacement correctly repairs the original matrix-category description:
  dimensions are objects, but the matrices do act on coordinate vector spaces.
- The size discussion correctly distinguishes a locally small category from a
  small category, and does not pretend natural-transformation families have only
  finitely many components. Yoneda supplies the required set parametrisation.
- Both variances in Yoneda's embedding consequence, both inverse equations and
  the naturality-in-target step for uniqueness of adjoints were checked directly.
  The theorem has the same conclusion as the baseline; it does not claim arbitrary
  natural isomorphisms between adjoints are unique without adjunction compatibility.
- The scalar obstruction to natural self-duality preserves |K|>3 and every
  nonzero finite dimension; the zero space and F2-plane exception are explicit.
- Separate review identified a complex-field qualification needed in the prose
  after `thm:notnatural`: a Hermitian inner product identifies a space with its
  ordinary linear dual conjugate-linearly. Parent repaired the prose in commit
  `ee5c8ac6`, distinguishing nondegenerate bilinear forms, real inner products
  and complex Hermitian products. The exact repaired sentence was re-read.
- Parent restored the literal nickname quotation ``general abstract nonsense'';
  the source reviewed includes that restoration. The original bibliography and
  complete original figure block remain literal.

## Prerequisite audit

Actual earlier sources read: Volume 8 `main.tex` gives Appendix A before Volume 10;
`linear-ch01-duality.tex` defines duals, proves evaluation isomorphism A.8 and
supplies the infinite-dimensional obstruction. Volume 9 `ch05-coverings.tex`
constructs and proves free products and free groups, including the empty-generator
case; its statement walker confirms Proposition 5.17. Volume 9 homology computes
H1 of the circle and proves the no-retraction/fixed-point route. Volume 3
`ch02-quotients.tex` provides derived-subgroup Exercise 2.4. The chapter's own
abelianisation proof also supplies the needed universal property locally.

No proof depends on a later chapter, appendix or exercise. The left-adjoint
coproduct comment is a forward exercise pointer, and its solution proves the
opposite-category argument. The new power-set exercise checks arbitrary families
and empty families directly; it does not leave arbitrary preservation inferred
only from the preceding binary-product theorem. Monads are explicitly a preview.

## Exercises and figures

All six original exercises retain their mathematical tasks and stars. Each hint
points to an available method, and every requested component is solved. The new
four exercises cover ordered adjunctions, natural abelian-group operations,
inverse-image adjoints and pullbacks. Their boundary checks include negative
integers, d=1, empty fibres, empty families, zero elements, and the difference
between abstract isomorphism and maps preserving a universal construction.
`ch01-statements.json` contains an individual judgment for every exercise.

Both new figure sources were read against their captions. The divisor-of-12
Hasse arrows all point from divisor to multiple; gcd(4,6)=2 and lcm(4,6)=12 occupy
the correct universal positions. The Yoneda square has Hom(A,A)→Hom(A,B), F(A)→F(B),
and alpha components in the correct directions, with the identity and its image.
They follow the original figure. The palette and label sizes follow the shared
figure conventions; actual rendered legibility remains parent's check.

## Actual checks

The source preservation walk found all original labels, the exact original figure
block, unchanged original figure-file hashes, and the same sequence of original
formal environment kinds. Counts are 3 figures, 10 exercises, 10 hints, 10 solutions.
Original printed numbers are recorded for all 29 original formal/exercise blocks.
The existing `check_ch01_categories.py` was run with the activated repository
Python environment and exited 0. It checks finite-field scalar obstructions and
F2-plane calculations; it supports, rather than substitutes for, the proof reading.

No book build was run by this reviewer. Final source hash and review disposition
are recorded in the JSON; any parent repair requires a hash recheck before this
source review is treated as final. Both reported Chapter 1 findings are repaired;
no unresolved source-level mathematical or editorial blocker remains.
