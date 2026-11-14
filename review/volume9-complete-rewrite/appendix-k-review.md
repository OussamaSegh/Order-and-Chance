# Appendix K — rewrite and checking record

Status: full draft rewrite; intermediate PDF-only build exited 0 at 433 print pages, with no overflow or unresolved references. Both figures were inspected on manuscript pages 415–416. The normal-arrow label touched the circle and was moved inside; this small relocation awaits the next PDF build. Separate final
review is outstanding. This is writer checking, not an independent certificate.

## Coverage and preservation

Rewrote the opening, every definition and explanation, seven formal statements
(including the definition), every proof, all eleven original exercises, hints,
full idea/writeup solutions, ending and reading guidance. The literal epigraph,
two original figure blocks and bibliography records remain unchanged. The formal
environment order and all original labels match main. Two diagrams follow the
last original figure, and four new exercises follow the original eleven.

## Explicit mathematical corrections and prerequisite repairs

- A tangent angle is constructed without circularly assuming theta'=kappa:
  T'=kappa*JT follows from the unit-vector identity, and rotating T by the
  integral angle produces a constant vector.
- Closed Ck curves explicitly have matching derivatives through order k. The
  total-turning and integration-by-parts arguments use this periodicity.
  Signed total curvature is distinguished from the integral of its absolute value.
- The four-vertex proof covers non-strict extrema, constant-curvature arcs and
  infinitely many extrema. A plateau supplies infinitely many extrema of both
  kinds. Without plateaux, two maxima give a minimum on each joining arc and
  conversely. If the conclusion fails there must therefore be exactly one of
  each kind. Monotonicity on their two arcs and a strictly positive affine-line
  integral contradict closure. No unsupported finite alternation shortcut remains.
- Gauss maps are defined on oriented patches, rather than assuming that every
  surface has a global unit normal. Convex boundaries have a global outward one.
- The Gauss-map determinant formula is retained. The area assertion specifies
  shrinking tangent-coordinate disks. Nonzero curvature uses a locally invertible
  map; zero curvature uses the rank-deficient Taylor image in an O(r)-by-o(r)
  rectangle, not a one-to-one change of variables at a critical point.
- General compact smooth Gauss--Bonnet explicitly excludes boundary; its boundary
  turning term is mentioned. Only the strictly positive convex case is proved here.
- Euler's projection uses a straight-edged Schlegel drawing, rather than applying
  polygonal separation without explaining curved projected edges. The exact earlier
  prerequisite is Volume 7, Theorem 6.1, disclosed in the opening and proof.
- Convergence of polyhedral defects to smooth curvature is not asserted as a proved
  consequence of the finite defect sum; it is identified as requiring further work.
- The clothoid solution replaces the invalid cosine-half-period alternating-series
  claim by integration by parts with tail bound 2/R. The exact original limit
  (sqrt(pi)/2,sqrt(pi)/2) is retained and justified by a damped Gaussian integral,
  the earlier holomorphic identity theorem and a uniform tail bound. The use of
  Volume 5 for the exact value is explicit; convergence itself uses calculus only.
- The no-map solution proves a nonzero small-a discrepancy -a^4/32+O(a^6), so it
  holds for every sufficiently small positive a. A decimal example is not used
  to infer a universal interval assertion. Existence of the small equilateral
  spherical triangle is also shown with a longitude formula.
- The football hint no longer claims equal angular defects from combinatorial
  data. The proof works without regular faces or equal defects.
- Five Platonic types are separated from construction of their regular realizations;
  incidence counts restrict p,q and do not by themselves construct a solid.

## New material checked in the draft

- Offset circle diagram: left normal inward, radius R-a for 0<=a<R, collapse at
  a=R. The example is regular only before collapse.
- Pyramid development: beta=pi/6,n=6, unit slant length, alpha=2*asin(1/4), six
  congruent triangular faces, missing angle 2pi-6alpha. Axial section uses the
  same beta, base radius sin(beta) and height cos(beta).
- Offset exercise: positive speed factor 1-a*kappa, changed arc length, signed
  curvature, singular factor, outward length via explicitly quoted turning theorem.
- Closure obstruction: positive periodic kappa=1+eta*cos(s) with total turning
  2pi but displacement -pi*eta+O(eta^2), nonzero for all sufficiently small eta!=0.
- Cone limit: exact n-gon apex angle, limiting apex defect 2pi(1-sin beta), base
  total 2pi(1+sin beta), and each base defect tending to zero with positive total.
- Noncompact quadratic graphs: K=ab/(1+a^2*x^2+b^2*y^2)^2; total curvature
  2pi*sign(ab) for ab!=0, zero otherwise. The normal image is an open hemisphere,
  semicircle or point. No compact Gauss--Bonnet claim is used outside its scope.

## Validation

Original statement-environment order and source labels match main. All 544 old labels/captions, 213 section numbers, 57 figure files and two cover-art files pass preservation. The existing appendix numerical examples exit 0; these illustrate computations and are not proof verification.
