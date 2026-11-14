# Chapter 2 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite; intermediate PDF-only build running. The separate
final review is outstanding. This is writer checking, not independent review.

## Coverage and preservation

Rewrote all prose, definitions, numbered statements and proofs, examples, seven
original exercises, hints, complete idea/writeup solutions, ending and reading
guidance. The two original figure blocks/captions and bibliography records remain
literal. Original formal environment order and source labels match main. Two
added figures follow both original figures, after the Frobenius/contact example;
four added exercises follow all seven originals.

## Explicit corrections and prerequisite repairs

- Picard's radius is positive. Zero bounds in b/M or 1/(2L) mean infinity; if M=0
  the equilibrium solution is constructed for all real times separately. Banach
  contraction is not applied to an undefined infinite closed time interval.
  The original quantitative interval and uniqueness conclusion are retained.
- The unlabelled compact-set Lipschitz proof is moved BEFORE Picard uniqueness
  uses it. Both compact and convex-ball versions are proved with their actual
  hypotheses; no segment through a nonconvex compact tube is assumed contained.
- Variational coefficients DF(phi(t,x)) are only continuous when F is C1.
  Their linear integral equation is solved directly by contraction on short
  continuous-matrix-function intervals, then concatenated with a uniform bound.
  The autonomous C1 theorem is no longer applied to a time coefficient lacking
  the required derivative. Differentiability, joint derivative continuity and
  higher regularity are proved separately with uniform remainder estimates.
- The remainder segment lies in a ball about a REFERENCE trajectory point,
  which is inside the tube; uniform continuity is used on an actual compact set.
- Finite escape implies eventually leaving EACH compact set, by uniform local
  time at any late return. Completeness chooses t1 in the ACTUAL maximal interval,
  rather than assuming beta-epsilon/2 belongs to it. Empty support, empty manifold
  and zero-dimensional fields are treated directly.
- Flow composition includes s in J(p) and s+t in J(p), with shifted maximal
  domain. The existence of phi(t+s,p) alone does not define phi(s,p).
- Exponential error amplification alone is not chaos. x'=x is a direct simple
  example, and the upright pendulum linearizes to delta''=delta, so the original
  blanket claim of only linear growth for a pendulum was false.
- Integer times for irrational torus flow fill only a vertical circle; adding
  a fixed fractional time proves full density. The nonembedded immersion is
  explained by local closedness, not a later Sard argument.
- Bracket small-loop order/sign and transported-back Lie derivative are fully
  retained. Frobenius handles k=0,k=n,n=0 and changes a spanning basis before
  requiring it to commute. Variable-rank spans remain outside the theorem.
- The contact example's covector is defined before the later differential-form
  notation. Its missing bracket direction rules out any tangent surface. Full
  bracket spanning is asserted for this particular R3 model, not inferred from
  mere nonintegrability in every dimension. Real-car clearance/steering and cat
  reachability are not silently claimed proved by an ideal unicycle calculation.
- Hairy ball treats S0 separately because its tangent spaces are zero. Milnor's
  connected-sphere open/closed argument then has n>=2. Adams is quoted; the full
  frame list S1,S3,S7 is for positive-dimensional spheres, with S0's empty frame
  explicitly included as the trivial case.
- The logarithmic ODE solution covers both positive AND negative starts and rules
  out finite-time arrival/departure at zero, not only positive splicing. Osgood
  is mentioned only as a broader sufficient criterion, not a blanket unproved
  necessary-and-sufficient assertion.
- The projective x'=x^2 flow uses homogeneous coordinates for all times, including
  zero; division by t is only used for t!=0. The common stationary point and
  identity-time fixed points are distinguished.
- The noncommuting loop's final point moves ALONG the x=0 line; only intermediate
  steps leave it. The original contradictory wording is corrected.
- Matrix exponential convergence/differentiation is supplied locally by its
  power series. The bracket BA-AB sign and complete second-order expansion stay.
- Parking invariants are globally constant because the configuration space is
  connected. Quaternion right-multiplication fields are computed without calling
  them right-invariant; their mutual bracket 2*xk is proved directly using V3.

## Additions

- Escape plot: x0=1/-1 branches on their actual maximal intervals, stationary
  zero and vertical finite endpoint markers at t=1/-1.
- Flow coordinates: X=partialx,Y=y partialx+partialy, u=x-y^2/2,v=y; fixed-u
  curves become parabolas and fixed-v curves horizontal lines.
- Nonlinear decay: exact -x^3 flow, maximal backward escape, initial derivative
  and variational equation, polynomial attraction without uniform exponential
  contraction at the zero equilibrium.
- Volume Jacobian: determinant expansion, inverse flow, exp(int divF) for both
  time directions, volume equivalence including empty determinant, and planar
  (H_y,-H_x) conservation/area with an explicit clockwise quadratic example.
- Simultaneous coordinates: commuting coefficient criterion and exact integral
  chart; e^x partialy shows an integrable plane distribution may have a
  noncommuting chosen basis that cannot both be coordinate fields.
- Torus averages: continuous invariants, uniform Fourier-mode time averages and
  Stone--Weierstrass; rational invariants from Bezout integer coordinates. No
  later ergodic theorem is used as a premise.

## Actual checks so far

The existing check_ch02_flows.py numerical illustrations exit 0, not a proof
certificate. cross_volume_citations.py matches 5,043 numbered statements.
The thirteen-unit PDF-only build exits 0 at 455 print pages, with no overfull boxes or undefined references. All original labels, printed section numbers, figure files and cover-art sources pass preservation. Both added diagrams were inspected on PDF page 51. Inspection prompted a clarification of the NEW escape caption: its dashed lines mark the excluded endpoints of the respective solution intervals, rather than excluding those times for every initial value. That wording-only repair awaits the next build. These writer checks are not the separate final mathematical/editorial review.
