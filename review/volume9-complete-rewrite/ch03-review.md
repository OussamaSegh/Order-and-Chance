# Chapter 3 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite; intermediate PDF-only build exited 0 at 451 print pages, with no overflow or unresolved references. Both added diagrams were inspected on manuscript page 77. Separate final
review is outstanding; this is writer checking, not an independent certificate.

## Coverage and preservation

Rewrote all opening/explanatory prose, definitions, formal statements and proofs,
examples, six original exercises, hints, complete idea/writeup solutions, ending
and reading guidance. Both original figure blocks, their captions and all
bibliographic records remain literal. Formal-statement environment order and all
original source labels match main. The two added diagrams follow the original
shoelace figure INSIDE the solutions, preserving all original figure numbers.
Four new exercises follow all six original exercises.

## Explicit corrections and prerequisite repairs

- Negative-degree forms are zero, so exact degree-zero forms and K on degree zero
  are defined. Empty wedge/determinant, k>n, n=0, empty spaces and zero forms are
  treated. Stokes has a trivial n=0 extension with its only (-1)-form zero.
- H0 is the PRODUCT of copies of R indexed by connected components. Its dimension
  equals the component count as stated only when that count is finite; the
  original unconditional dimension assertion was false for infinite components.
- A boundary-chart orientation issue in dimension one is repaired explicitly.
  Restricting every chart to H^-={x1<=0} cannot give an all-positive atlas at both
  ends of an oriented interval. The definition now allows H^- or H^+ (equivalent
  smooth structures by reflection). For n>=2, reflect x1 and x2 together to
  normalize positive charts to H^- before the determinant boundary proof. For
  n=1, an H^+ starting chart has boundary sign minus and an H^- ending chart plus.
  Signed zero-manifold integration is defined separately, not by an impossible
  reflection of a zero-dimensional coordinate.
- Relative boundary bumps are restrictions of ambient Euclidean bumps; local
  finiteness/normalization gives the partition needed by Stokes up to boundary.
  Boundary localization is not silently borrowed from the boundaryless proof.
- Sphere sigma explicitly has n>=1. The n=1 signed S0 integral is 2. Brouwer's
  n=0 ball is a fixed singleton, handled without an undefined S^-1 formula.
- The no-retraction proof distinguishes the derivative ON the sphere (zero by
  degree) from the nonzero ambient derivative of sigma. The ray-root argument
  retains polynomial approximation, strict radicand positivity and smoothness
  on an ambient neighborhood, rather than only continuity on the ball.
- Exterior-derivative uniqueness explains locality via bumps and extension of
  local coordinate expressions; product signs and pullback compatibility remain.
- Shoelace at polygon corners is justified by rounding in disjoint small disks,
  with O(delta^2) area and O(delta) boundary-integral error. No unexplained
  triangulation or direct smooth-boundary application at corners is needed.
- Torus coordinates have period 1 (not 2pi). The original exercises' independence
  tests and area obstruction are retained. A new exercise proves BOTH full H1
  and H2 computations using explicit periodic primitives, so their dimensions
  are no longer a silent appeal to later topology.
- The Mobius-band nonorientation claim gets its own strip/core sign argument.
  Odd-dimensional projective-space orientability is proved by gluing local
  inverse quotient charts using antipodal invariance; descent is explained.
- Sphere/ball formulas retain all original values, maximum dimension 5 and n=10
  cube fraction. A two-step recurrence and explicit finite rational pi bound
  justify the maximum. The high-dimensional statement is distance from the
  centre, not an unsupported claim that typical points lie next to vertices.
- General de Rham and the RP3/SO3 comparison are explicitly quoted or previews;
  no later homology or Lie-group result enters the proofs.

## Additions

- Pullback-area diagram: M=[[2,1],[0,1]] takes the unit square to vertices
  (0,0),(2,0),(3,1),(1,1), area 2; wedge pullback has the same factor.
- Vector-potential diagram: F=(0,0,1), A=(-y/2,x/2,0), counterclockwise tangent
  arrows with magnitude r/2, circulation pi*R^2 matches upward flux.
- Compact-potential exercise: compactly supported closed 1-forms on the punctured
  plane are ordinary exact, but dchi gives no compactly supported primitive;
  a nonconstant radial cutoff of dtheta fails to stay closed.
- Torus-period exercise: full H1 and H2, explicit periodic functions A(y),B(x,y),
  integer-matrix pullback M^T and det M, a two-to-one example and singular map.
- Source-flux exercise: r^-n*sigma is closed away from zero, sphere flux constant,
  punctured-region Stokes distinguishes source inside/outside. n=2 angle and n=3
  inverse-square fields; singular-boundary case is excluded.
- Radial-potential exercise: full homotopy contraction formula with t^(k-1),
  scalar and vector potentials, all-time smoothing convention, constant-field
  curl and circulation check. All prerequisites are earlier in the printed order.

## Actual checks so far

The existing check_ch03_forms.py numerical illustrations exit 0; these are not
proof certificates. cross_volume_citations.py matches 5,039 numbered statements.
All 544 original printed labels/captions, 213 section numbers, 57 original figure files and two cover-art files pass preservation.
