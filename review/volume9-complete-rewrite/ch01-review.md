# Chapter 1 writer check — smooth manifolds

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

## Full coverage and preservation

Introductions, teaching prose, all definitions, original numbered statements and proofs, examples, seven old exercises with hints and idea/writeup solutions, ending and reading guidance are rewritten. All original formal environments and labels keep their order. Both original figure blocks and accurate bibliography records are literal; historical quotations are preserved. Two added diagrams follow the old arm figure; four new exercises follow the original seven, with fresh labels, ratings, hints and complete solutions. This writer check is not the separate final review.

## Mathematics and prerequisite repairs

- R0, empty sets and empty determinants are explicit. The mean-value proof handles zero output difference before selecting a unit vector, covering a zero-dimensional target. Partial derivatives and inverse/implicit statements retain all regularity hypotheses and handle zero-sized blocks.
- The inverse proof keeps its contraction, injectivity, inverse Lipschitz estimate, differentiability and full regularity induction. The implicit product neighbourhood ensures that its graph actually remains in the chosen second neighbourhood. Four-description proof retains the homeomorphic-image restriction excluding remote parametrized branches and uses the empty-minor conventions at ranks zero/full.
- Sphere and orthogonal examples include dimensions zero; the empty manifold's dimension is assigned rather than claimed intrinsically determined. Nonempty smooth dimension follows from tangent spaces; purely topological invariance is not assumed here. Cassini levels include empty and isolated cases and justify component counts by polar roots.
- A local target-submanifold smoothness fact is supplied before matrix/sphere solutions use it. Projective quotient charts, Hausdorffness, countable basis and compactness are proved. The analytic vanishing comparison now requires a connected domain and a nonempty open zero region.
- Partitions treat the empty manifold and permit repeating a finite basis in the exhaustion. Compact layers, support containment, local finiteness and positivity of the normalizing sum are explicit. Tangent derivations use bump extensions, Hadamard and the empty coordinate basis; the rectangular parametrization derivative is inverted only on its image, not as a nonexistent full matrix inverse.
- The regular-value theorem keeps its NONEMPTY fibre hypothesis so that m>=n follows and no negative-dimensional fibre is asserted. The empty fibre remains a regular-value case by definition. Compact injective-immersion embedding uses the Hausdorff target.
- Null-set/Sard proofs separate dimension zero: counting measure has only the empty null set and the empty determinant is one, giving no critical points. Lipschitz bounds can be chosen at least one, avoiding degenerate covering cubes. The positive-dimensional proof retains its full pancake estimate. Density on zero-dimensional targets follows because every value is regular.
- The general Morse--Sard result remains explicitly QUOTED with its regularity threshold. The compact Whitney construction is fully proved, including finite zero-manifolds and the empty manifold; its cutoff coordinates are explained rather than merely written down.
- CORRECTION OF MISSING HYPOTHESIS: the QUOTED strong Whitney embedding into R^(2n) is stated for n>=1. A two-point zero-manifold cannot embed in the one-point R0, so the old unrestricted formulation was false. The R^(2n+1) statement remains quoted for compact and noncompact manifolds; the compact projection sketch is not represented as a proof of the noncompact case.
- CORRECTION OF MISSING HYPOTHESIS: the SL_n and SU(n) exercise assumes n>=1; their n²-1 formula is false for n=0. O0/U0 conventions do not silently give negative dimensions.
- The crossing-curve solution proves nonopenness by the missing points (epsilon,0), removing its dependence on the later mini-Sard exercise. Injectivity checks all reflection cases. Stereo charts include S0's empty overlap, and the lower-dimensional null-image solution includes a point source. The RP2 embedding separates projector recovery from its derivative proof, so the square-root reconstruction is never differentiated at its singular value.

## New teaching material

Figures show the Schur-complement chart for fixed-rank matrices and the exact square image under (x,y)->(x,y²), with equal panel scales. Exercises develop a smooth zero set with a singular squared defining function; rank-r matrices and rank-at-most-r singularities; transverse intersections with tangent and empty sphere-plane cases; and a proper smooth exhaustion plus compact cutoff/extension. Every proof uses material already available on the printed route.

The existing Riemann portrait is moved from Chapter 10 to the first substantive Riemann discussion in Chapter 1. Its file, presentation macro and adjacent credit remain unchanged; photos/CREDITS.md now records the new location. There are still two distinct added photographs, not three.

## Actual validation

The sixteen-unit PDF-only build exits 0 at 477 print pages, with no overflow or unresolved references. Fonts, bleed, print interior and cover checks pass. Preservation checks all 544 old printed labels/captions, 213 numbered part/chapter/sections, 57 old figure files and two cover-art sources. Both new diagrams were inspected on PDF page 34, and the relocated portrait/credit on page 14. The original numerical script exits 0 (illustrations, not a proof certificate), cross-volume citations match 5,094 statements, and git diff --check passes.

Before applying this chapter, the clean fixed source 57f9e4ee had a successful full fifteen-unit build: 471 print pages, EPUB 30,607,901 bytes, 85 plates at 1800 pixels and passing media checks. All 17,666 local links resolve. Actual EPUB samples of both homology diagrams, the matrix exercise, hints, formulas and solutions were inspected in Chromium. Artifact hashes and audit are recorded separately. This does not substitute for the final full build and separate review of all 22 units.
