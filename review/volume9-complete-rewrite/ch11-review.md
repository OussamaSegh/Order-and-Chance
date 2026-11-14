# Chapter 11 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite; intermediate PDF-only build exited 0 at 441 print pages, with no overflow or unresolved references. Both diagrams were inspected on manuscript pages 219–220; the relocated K normal-arrow label was also inspected and is clear. The separate
final review remains outstanding. This record describes writer checking.

## Coverage and preservation

Rewrote all opening and explanatory prose, nine formal statements and proofs,
all six original exercises, hints and complete idea/writeup solutions, ending
and reading guidance. The original figure block and bibliographic records are
literal; Bertrand's quoted words are preserved. Formal environment order and
all original labels match starting main. Two diagrams follow the original figure;
four substantial exercises follow the six original exercises.

## Explicit corrections and prerequisite repairs

- The locally finite invariant line measure is NOT the direct pushforward of
  motion Haar measure. Along-line translations stabilize the line and have
  infinite measure. The coordinates (theta,p,s) explicitly factor Haar volume
  into line measure dtheta*dp and stabilizer measure ds, explaining the quotient.
- There is no uniform probability on ALL lines or motions. Each probability
  calculation specifies a finite hitting or translation window and normalization.
  Poincare's 4*L1*L2 is an integral, not an unnormalized probability average.
- The line-measure uniqueness proof explains the approximate uniform-offset
  shifts, compact-support bound, atom-free interval measure, product structure,
  sigma-finite uniqueness and the factor two for orientations, including c=0.
- Joint measurability of crossing counts in (theta,p) is proved by dyadic-cell
  images as countable unions of compact images. Separate measurability alone
  is not substituted for the hypothesis needed by Tonelli.
- Counting uses parameter/traversal multiplicity, including retraced arcs,
  critical values and zero-speed points. Null joining and coincident-line
  events are distinguished. The straight short-needle probability is not
  asserted for every bent curve of the same length.
- The isoperimetric bound and its disk equality case are proved locally using
  Green, Cauchy--Schwarz and the EARLIER periodic Wirtinger inequality. Periodic
  convolution explains extension to the arc-length boundary. No exercise uses
  Appendix J before it is printed, including two-line probability and Laplace's
  grid offset count. Later appendix references are reading guidance only.
- The shadow proof establishes that an interior projected point lifts to an
  interior body point by a convex combination and a ball, without invoking
  the later convex separation theorem. The twice-covered-face count is explicit.
- The rectifiable kinematic extension and Hadwiger theorem are quoted, with
  valuation/convex-union, continuity and empty-set conventions. Polygon pictures
  converging are not asserted to prove convergence of all intersection counts.
- The sphere shadow check is direct and is not passed off as a proof of the
  extension from polytopes to arbitrary convex bodies.
- Spherical Crofton now has a full C1 incidence map F(t,phi) built from a local
  C1 frame perpendicular to c, not a differentiable unit-tangent frame that may
  fail at C1 regularity or zero speed. Its Jacobian |F dot c'| is derived. A
  multiplicity area formula follows from equal-dimensional C1 Sard, inverse
  charts and Borel preimage counts; seams are null. The result includes constant
  curves and does not rely on a thin-band approximation as a proof.

## New material

- Rectangle-window illustration: horizontal and vertical normals allow offset
  ranges a and b; conditional angle density is proportional to width.
- Spherical-incidence illustration: meridian section of pole band |u dot n|<=sin a
  and uniform height interval; a=pi/6 gives band probability 1/2.
- Window law exercise: angle density w/L, conditionally uniform offsets,
  nonuniform square angle law, constant width rather than circularity. Reuleaux
  construction is supplied locally, so the new exercise has no forward premise.
- Moving circles/disks: direct annulus and disk translation integrals, null
  tangencies/coincident circles, rotation factor 2pi and finite-window probability.
- Affine Crofton: inverse-transpose normal, offset and angular Jacobians give
  1/(|det T|*|T^-T u|^3), including orientation-reversing T. Rotation/dilation
  checks and ellipse perimeter integral fix normalization.
- Spherical cap: boundary hit probability sin(a), mean boundary count 2sin(a),
  cap hit probability sin(a) for a<=pi/2 and one for larger caps. Endpoint limits
  explain why the planar exactly-two-crossings rule fails for large caps.

## Cross-volume citation repair

The earlier review deferred V9-04: Volume 15 ra-polynomials cited Theorem 8.8 for
SU(2)'s eigenangle law. Theorem 8.8 is the U(n) Weyl formula; the actual local
SU(2) calculation is Example 8.5. The sentence now cites that example directly.
No printed number changes. This is a semantic citation correction in the same PR.

## Actual validation so far

Original formal environment order/source labels match main. The existing
check_ch11_integral.py numerical illustrations exit 0 (not proof verification).
Twenty citation tests pass; cross_volume_citations.py matches 5,031 statements.
Preservation checks pass for all 544 old printed labels/captions, 213 section numbers, 57 original figure sources and both cover-art sources.

Representative EPUB content from the six-unit checkpoint on 66ca56fd was opened
in Chromium using a temporary local HTTP server and the extracted actual EPUB.
The Haar opening, formulas, two Haar diagrams, Riemann portrait/credit and Cayley
proof, and Shukhov photograph/credit were inspected. Images and math displayed
without visible overflow in these samples. This is not final EPUB acceptance.
