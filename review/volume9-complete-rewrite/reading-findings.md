# Complete source read and mathematical findings

The 11 chapters and 11 appendices were read in the order in `main.tex`, together
with the preface, selective index, jacket copy, KDP copy and generated cover note.
The read used source chunks, revisiting portions whose tool output was truncated.
This is a list of findings to resolve, **not a certificate that they are fixed**.
A later, separate review must compare every numbered statement with starting main.
Original figure captions and bibliography records are protected even where nearby
prose needs qualification. Source drawings are not to be changed.

## Chapter findings and repair plan

1. **Manifolds.** Handle a zero-dimensional target before selecting a unit vector
   in the mean-value proof. Explain dimension-zero and empty-manifold cases of
   Sard, null sets, partitions and Whitney. The quoted strong Whitney theorem
   needs positive dimension. Avoid using the later mini-Sard exercise to establish
   that the crossing curve is not a submanifold. State positive matrix size for SL.
2. **Flows.** Picard's displayed time needs a convention when the bound or Lipschitz
   constant vanishes. The variational equation has continuous time-dependent
   coefficients: prove its integral-equation existence locally, rather than
   invoking an autonomous C1 theorem it does not meet. Choose the time before a
   finite escape endpoint inside the actual interval. Exponential separation alone
   is not chaos; a pendulum's upright equilibrium has exponential linearisation.
   Treat the zero-sphere separately in hairy-ball reasoning. Complete the negative
   half-line in the logarithmic ODE exercise. The noncommuting loop in that exercise
   moves along, rather than leaves, the line x=0.
3. **Forms.** Define negative-degree forms as zero for the homotopy convention.
   Stokes needs n>=1; Brouwer's n=0 case is separate. H0 is the space of functions
   on connected components; its dimension equals the component count as stated
   only for finitely many components. Explain partitions in boundary charts before
   using them. Original second figure occurs in a solution: additions go after it.
4. **Curvature.** A whole cylinder does not unroll bijectively to a plane strip;
   the statement is local or requires a cut. Explicitly exclude boundary in the
   closed-surface Gauss--Bonnet statement. The pseudosphere-to-half-plane formula
   uses a local angular coordinate, not a globally defined angle. Include both
   signs and translation constants for its profile. Supply the local hyperbolic
   polar calculation in the exercise rather than using Chapter 9 in advance.
   Distinguish smooth surface classification quoted in the Euler comparison.
5. **Coverings.** Mark early group computations as previews where van Kampen is
   still needed. Fix the claim that all four sides of the van Kampen homotopy are
   fixed at the basepoint. Explain reparametrising concatenations into equal time
   pieces. Keep the general infinite graph extension clearly separated from the
   locally finite proof. Check trivial groups, covers and zero-rank free groups.
6. **Homology.** Explain augmentation and the empty-space reduced convention.
   Choose subdivision depths geometrically before cancellation, so face depths
   are monotone. Separate the zero-sphere and zero-dimensional invariance-of-domain
   cases. Distances to empty sets in Lusternik's exercise need a substitute positive
   coordinate. Handle empty or singleton point sets in discrete pancakes.
   In the transfer argument only the indicated connecting and transfer maps are
   isomorphisms; the quotient map is not one.
7. **Lie groups.** The full-turn clause of the spin theorem needs |u|=1.
   Commuting-rotation claims need the identity exception; zero angular velocity
   has no distinguished positive period. O(n) has two components for n>=1, not n=0.
   Rewrite the closed subgroup chart argument with a neighbourhood containing no
   nonzero transverse exponential. Use a local elementary 2x2 polar formula in
   place of unexplained functional calculus in the SL2 exercise.
8. **Haar.** The first-column density requires n>=2; at n=1 the squared modulus is
   the point mass at 1. Dyson's dominated-convergence bound must be an absolute
   value bound for signed h. Repulsion suppresses close eigenvalues, not all close
   pairs. Distinguish symmetric matrix ensembles from Haar orthogonal matrices.
   Hilbert--Polya alone does not establish pair correlation. State which general
   compact-group Weyl facts are quoted. QR phase conventions do not all necessarily
   fail Haar invariance. Treat counting measure in dimension zero.
9. **Hyperbolic.** PSL2 is the orientation-preserving isometry group. The angle-sum
   corollary's area<pi conflicts with its ideal-triangle clause: area<=pi, equality
   exactly for three ideal vertices. In the h-line proof the perpendicular bisector
   is nonhorizontal, not nonvertical. Treat coincident distance endpoints and
   uniqueness as a geometric arc up to reparametrisation. Right-N horocycles have
   the pointed vector as normal, not tangent. Explain the orbifold exception at
   modular elliptic points. List all reduced forms before identifying classes.
   Two arbitrary quadratic irrational endpoints need not bound a closed axis;
   a conjugate pair is required for that assertion.
10. **Riemann mapping.** The opening omits 'without zeros' in its root hypothesis
    and contains the sentence 'A square is a map'. The square integral is an
    example quoted from Schwarz--Christoffel, not a proved intermediate result.
    The numbered statements and the extremal proof are valid. Explain every
    composition's domain and why the square-root step strictly increases scale.
    Preserve the original figure and all three exercises.
11. **Integral geometry.** Pushing motion Haar measure directly to unoriented lines
    gives infinite mass because the stabiliser is noncompact. Use quotient
    integration and the direct locally finite measure, not that pushforward.
    Give a local planar isoperimetric proof before exercises that otherwise invoke
    Appendix J. Complete the spherical Crofton solution with the incidence
    parametrisation and C1 change-of-variables argument. Establish joint
    measurability of intersection counts, and specify multiplicity for retraced
    paths. An integral over infinite Haar measure is not a probability average.
    Avoid using the later convex separation theorem in the shadow argument.

## Appendix findings and repair plan

A. **Transformations.** Treat the trivial rotation subgroup in the finite isometry
   classification. Prove the shortest-vector lattice spanning step locally rather
   than citing a later exercise. Fagnano's lower bound holds for all D, but its
   reflected segment need not stay in the sides for arbitrary D; verify equality
   at the orthic triangle separately. Vertex-hitting billiards are excluded.
   The identity translation is not the square of a genuine glide reflection.
   Correct Routh's edge vectors to (-3/7,2/7),(-2/7,-1/7). Midpoints of chords
   perpendicular to u lie on the diameter parallel to u in the ellipse argument.
B. **Inversion.** Ptolemy's equality clause needs coincident-point cases.
   Handle already concentric circles and nested-radius ordering. Steiner and
   Pappus chains must advance rather than backtrack. A zero Descartes curvature
   represents a line; do not describe it as a finite circle with centre.
   Equilateral Feuerbach has coincident incircle and nine-point circle rather
   than a unique tangency point. Require distinct arguments for cross ratios.
   Exclude the identity before classifying nonidentity Mobius maps. State
   nondegeneracy and forward progression for the Soddy hexlet exercise.
C. **Projective.** Quote the general division-ring Pappus characterisation rather
   than claiming the commutative determinant proof works verbatim. The six-value
   cross-ratio exercise needs characteristic-2 and characteristic-3 exceptions.
   'Plane of order' counting requires finiteness. Give explicit complex Hesse
   coordinates in the ordinary counterexample exercise, not a forward dependency
   on Appendix G's flex theorem.
D. **Conics.** In Poncelet, establish smooth dependence and the interior chord
   intersection before deriving orientation from alternating endpoints. State
   f>0 in the parabolic reflection example. Keep the general algebraic porism a
   clearly quoted extension. Remove unsupported historical dismissal of early
   conic applications.
E. **Quadrics.** The binary-root discussion must include a=0: a projective root
   may be at infinity. Gram determinant volume is zero when k>n; one cannot
   choose a containing k-dimensional subspace of R^n then. The zero quadratic
   equation defines the whole projective plane and must be included if 'all'
   projective quadratic loci are requested, or explicitly specify nonzero forms.
   Verify rank-3 cone and split-plane degeneracy reasoning over the algebraic
   closure in the skew-lines exercise. Preserve the characteristic assumption.
F. **Plane curves.** Supply a noncircular justification that an irreducible curve
   has infinitely many points and finitely many singular points before choosing
   further smooth points in the singular bound. Prove the singular conic fact in
   arbitrary characteristic by moving the singular point and inspecting
   coefficients; the matrix gradient 2Ax proof fails in characteristic 2.
   State distinctness of points where independence is asserted. The polar
   solution must rule out a zero polar for the actual nonzero Q, not merely
   'a suitable Q'. Remove numerical claims as proof of generic tangent counts.
   Keep the auxiliary-point multiplicity limitation explicit.
G. **Cubics.** Distinguish operations on K-rational points from geometric points
   over an algebraic closure. The no-neutral-element assertion cannot hold on
   every finite E(K); its proof varies geometric points. Specify characteristic
   different from 2 where y=0 is identified with affine 2-torsion. Full group
   associativity remains quoted from Volume 13, not silently assumed. Replace
   the 'finite plane of order 3' wording for the nine-point configuration by
   'affine plane'. Give an exact substitution for the Bachet check. Check small
   characteristics and the finite-field point tables.
H. **Lattices.** Shortest nonzero vectors require n>=1. Explain real independence
   of the projected basis in Hermite's solution, not just integer independence.
   In circle counting use max(0,r-sqrt(2)) for the inner radius; finish the stated
   bound separately where that radius vanishes. Keep Viazovska's optimality quoted.
I. **Non-Euclidean.** Specify a nondegenerate convex spherical triangle with minor
   sides and angles, rather than an arbitrary choice of three great-circle arcs.
   The claimed converse existence of hyperbolic angle triples is not proved by
   a numerical construction: remove that unsupported proof aside or prove it.
   Horocycle asymptotics are for each fixed x, not uniform independently of x.
   Keep Chapter 9 as the earlier source of all hyperbolic results.
J. **Convex.** The enclosing-unit-disk exercise is false for a two-point set under
   its vacuous 'any three' hypothesis. Require every subset of at most three to
   fit, preserving all valid >=3 cases. Define the perimeter convention for a
   segment (twice its length) and a point (zero); exclude the empty body where
   width is undefined. State n>=1 for roots 1/n. Make polygon-to-body passage in
   Steiner's formula rigorous, and distinguish the proved inequality from the
   unproved uniqueness of all equality cases. Treat open interval endpoints in
   the one-dimensional Helly solution explicitly.
K. **Curvature.** Closed curves must have periodic derivatives before using total
   turning and integrating by parts. Repair the four-vertex proof's finite versus
   infinite non-strict extremum cases; plateaux need an explicit argument.
   Give a local tangent-angle construction without presupposing the desired
   derivative identity. The Gauss-map small-area interpretation needs local
   invertibility when K!=0 and an o(area) statement when K=0. General compact
   Gauss--Bonnet excludes boundary. The clothoid convergence proof should use
   integration by parts, since the stated cosine half-period alternation is not
   valid on [k*pi,(k+1)*pi]. Prove a nonzero small-a discrepancy in the no-map
   exercise using its expansion, rather than claiming a numerical example proves
   all a in (0,pi/2). Euler's polygon separation premise needs an earlier source
   or a local proof under the appendix's advertised prerequisites.

## Review status

Chapter 10 is being rewritten first. No entry above is considered fixed until
its manuscript change, mathematical recheck and fixing commit are recorded.
No full-volume acceptance gate has been passed for the rewritten manuscript.
