# Appendix J — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: complete draft rewrite; intermediate PDF-only build exited 0 at 425 print pages. Layout checks report no overflow or unresolved references. Both added figures were inspected on manuscript pages 395–396. Separate final
review remains outstanding. This is writer checking, not independent review.

## Coverage

Rewrote the opening, every explanation and transition, two lemmas, four theorems,
two corollaries, all proofs, all twelve original exercises, hints, full
idea/writeup solutions, ending and reading guidance. The literal epigraph,
three original figure blocks and bibliography records are preserved.
Original statement order, labels and section numbering remain. Two new diagrams
follow the last original figure; four new exercises follow all original exercises.

## Explicit corrections and prerequisite repairs

- The enclosing-unit-disk exercise was false for a two-point set because its
  every-three condition was vacuous. Every subset of AT MOST three must fit.
  The solution gives the original counterexample of two points more than 2 apart.
  All valid cases with at least three points are retained.
- Width requires nonempty compact convex sets. Perimeter of a segment is twice
  its length, and perimeter of a point is zero. These conventions are used in
  Cauchy, Barbier, perimeter addition and Steiner, including collapsed limits.
- Brunn--Minkowski and surface-content roots explicitly require n>=1. The theorem
  still covers ALL nonempty compact sets, including nonconvex and zero-volume
  sets. No positive-volume or convexity hypothesis was silently added.
- The cutting induction explains why each side has fewer A boxes, how equal
  volume fractions are chosen, and why discarded zero-volume cut pieces are
  unnecessary for its LOWER bound on the sum's volume.
- Steiner's extension is no longer an unexplained polygon approximation. A
  scaling proof gives boundary measure zero; nested convex dense unions contain
  the interior by a surrounding-triangle argument. Taking volume limits at fixed
  epsilon proves the full identity before taking the difference quotient.
- Helly on the line treats open/half-open/unbounded intervals and a shared
  endpoint explicitly. Radon handles repeated indices, and n=0 Helly and the
  n=0 sharpness example (one empty set) are included.
- Buffon's curve count uses traversal multiplicity for retraced arcs. Expected
  count is distinguished from hit probability, including the needle-length-1
  boundary event. Vertex and coincident-line exceptions have measure zero.
- A circle's crossing expectation is computed directly in its solution rather
  than inferred from an unproved polygon-to-curve passage.
- The broad surface-content theorem proves balls attain equality, not an
  unproved uniqueness theorem. The constant-width area exercise claims the disk
  is a maximizer and explicitly avoids asserting unproved uniqueness.
- Slice concavity remains valid for noncompact convex sets with finite-area
  slices: inner regularity from Volume 7 extends the compact-set inequality.
  A lower endpoint chord bound for arbitrary compact sets is distinguished from
  actual concavity, with an explicit new counterexample.

## Additions

- Helly diagram: the three convex edges of one triangle meet pairwise but not
  all together. Each labelled pair intersection is the opposite vertex.
- Parallel-body diagram: four rectangles total L*epsilon, four quarter-disks total
  pi*epsilon^2. No original diagram/caption is changed.
- Long needle: exact angular probability for all ell>=0, agreement at ell=1,
  expected count distinction and missing-probability asymptotic 1/(pi*ell).
- Parallel-set stability: width and perimeter bounds and a two-sided area bound,
  covering approximations collapsing to a segment or point.
- Smooth constant-width example: h=1+eta*cos(3 theta), 0<|eta|<1/8, positive radius
  rho=1-8 eta*cos(3 theta), unique supporting point, local proof of support-line
  existence, perimeter 2pi and area pi-4pi*eta^2. Green is available in Chapter 3.
- Nonconvex obstruction: A=[0,1] union [3,4]; weighted self-sums have measures
  2,4,3,4,2 at weights 0,1/3,1/2,2/3,1. Concavity fails while BM's lower bound 2
  remains valid.

## Actual checks so far

Original formal-statement environment order and source labels match starting
main. The existing check_appendices.py numerical illustrations exit 0; these do
not certify proofs. All 544 original labels/captions, 213 section numbers, 57 figure sources and two cover-art sources pass preservation.
