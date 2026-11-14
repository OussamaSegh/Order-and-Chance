# Appendix I — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite; final-volume independent review is outstanding.
The checks below are a later pass by the writer, not an independent certificate.

All prose, both formal statements and their proofs, all twelve original exercises,
hints and idea/writeup solutions were rewritten. The epigraph, both original
figure blocks and all bibliographic records remain literal. Original section
numbers and labels are retained. Hyperbolic formulas still rely on the earlier
proofs in Chapter 9; this appendix does not pretend to prove them again.

## Corrections and prerequisite repairs

- Defined the intended nondegenerate convex spherical triangle, with minor sides
  and interior angles in (0,pi). The original vague 'three arcs' definition also
  allowed complementary or self-overlapping regions to which its formula did not
  apply with the same angle interpretation.
- Proved lune area by integrating the spherical area element, then checked the
  six-lune multiplicity count. Both sides are 4 times the relevant angle/area sum.
- Marked triangle-group reflection tilings and Hurwitz's theorem as quoted facts,
  rather than implications of the area computation. Explained the doubled region
  for the orientation-preserving subgroup in the factor 84.
- Removed the assertion that a numerical construction proves existence of every
  permissible hyperbolic angle triple. The exercise asks only for the necessary
  inequality and the minimum among triangles already assumed to exist.
- Made the horocycle limit pointwise for fixed x. The original 'independently of x'
  could imply a false uniform estimate over the entire horizontal line.
- Introduced the Klein coordinate change locally before the new polygon figure.
  Its radial monotonicity gives a bijection; the orthogonal-circle equation gives
  a straight-line equation. The caption says explicitly that angles are distorted.

## Proof and solution checks

The spherical cosine proof divides only by positive sin(a) and sin(b).
Small-triangle errors use c<=a+b before controlling c^4. All radius parameters
exclude the undefined/degenerate endpoints in assertions about nonempty circles.
The inverse-isometry proof uses real translations and positive dilations.
The hyperbolic cosine computation keeps the two opposite side lengths in the
correct positions. Ideal-triangle normalisation includes negative determinants
and hence orientation reversal. The angle-of-parallelism solution checks the
actual rays towards F and the ideal endpoint, not just unoriented tangent lines.
The reciprocal-sum bound separates q=3 from q>=4 and includes p=q=2 impossibility.
The horocycle solution computes the distance before expanding, and treats x=0.

## New material

Two explanatory figures, both following the last original figure:

- `v9-app-i-polar-circles`: exact radii tanh(r/2), labelled r values, dashed
  excluded boundary; the image is a plot in the conformal disc.
- `v9-app-i-triangle-area`: a Klein-disc fan with three nonoverlapping triangles;
  its straight lines are h-lines, and its Euclidean angles are not used.

Four exercises follow the original twelve; each has a fresh label, two-star
rating, useful hint and full idea/writeup solution:

- `geometry:ex:v9-caps-and-balls`: polar areas, quartic expansions and strict
  spherical/Euclidean/hyperbolic comparison. The inequality is integrated over
  a positive interval, so equality does not occur for r>0.
- `geometry:ex:v9-offset-circle`: completes the Euclidean square, verifies its
  lowest height remains positive, and computes the vertical diameter's distance.
- `geometry:ex:v9-hyperbolic-polygons`: fan proof, necessary n>=5 for right angles,
  hexagon area pi and ideal polygon area. The exercise does not claim sufficiency
  from the angle inequality alone.
- `geometry:ex:v9-rigid-equilateral`: exact angle/length relation, strict
  monotonicity, both limiting areas and the obstruction to nontrivial uniform
  distance rescaling. The map sends geodesic segments to geodesic segments by
  preservation of distance-triangle equality, before angles are compared.

Existing `check_appendices.py` and `check_ch10_riemannmap.py` both exited 0 after
these drafts. They check numerical/algebraic illustrations, not full proofs.
The combined PDF build, preservation check and rendered inspections are pending.
No full EPUB or exact-final-head CI result is claimed here.

## Combined PDF-only build and rendered inspection

The Chapter 10 + Appendix I + portrait PDF-only build exited 0 at **393 print
pages**. It checked 573 whole boxes (maximum 318.2 pt), reported no overflow or
unresolved references, and passed font, reading-PDF, print-interior and cover
checks. The preservation checker again passed all 544 original printed labels,
all original captions and 57 original figure files. A contact sheet of manuscript
PDF pages 189, 194, 195, 354 and 355 was rendered and inspected: the Riemann portrait
and all four new diagrams were visible, labels and captions legible, with no
visible collision. The source photograph was also inspected at native resolution.
The earlier scripts are illustrative algebra/numerical checks, not proof tests.
This intermediate result predates the Appendix E rewrite and is not final-volume
or exact-final-head verification. Full EPUB checks and final independent review
remain outstanding.
