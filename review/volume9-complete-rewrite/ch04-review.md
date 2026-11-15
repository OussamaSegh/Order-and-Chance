# Chapter 4 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite. Intermediate PDF-only build exited 0 at 445 print pages, with no overflow or unresolved references. Both diagrams were inspected on manuscript pages 89–90.
Separate final review remains outstanding; this is writer checking.

All original formal statements, prose, examples, proofs, exercises, hints,
solutions and ending are rewritten; two original figure blocks and all
bibliographic records remain literal. Four substantial exercises and two diagrams
are drafted. Original formal environment order and source labels match main. All 544 original printed labels/captions, 213 section numbers, 57 original figure sources and two cover-art files pass preservation. The existing chapter numerical illustrations exit 0; cross-volume citations match 5,035 statements. These checks do not certify the proofs.

Corrections/prerequisite repairs to record in the fixing commit:

- Gauss--Bonnet, its index-based Euler definition and consequences explicitly
  exclude boundary. A flat disk shows why the farthest-point exercise also
  needs no boundary. General boundary versions have additional terms.
- The Morse height-function EXISTENCE PROOF is taught BEFORE the Euler definition
  and Gauss--Bonnet corollary first use it. It needs only earlier embedding,
  equal-dimensional Sard, Fubini and inverse-function arguments. The later
  numbered Morse theorem records the already established construction; formal
  statement and section numbering stay unchanged. This repairs the original
  logical forward use even though it was noncircular.
- Gauss lemma is proved locally from the structure equations' torsion-free
  identity and radial variations, instead of remaining an admitted later tool.
- The half-plane exponential-map solution supplies the full local Cayley/polar
  calculation and radial geodesic verification without using Chapter 9.
- The cylinder unrolls isometrically only locally or after a cut, not by a global
  bijection of the whole cylinder with a plane strip.
- Connection-form coordinate orientation and local angle branches are explicit;
  the scalar curvature remains orientation independent. Shape-operator signs
  are fixed consistently, rather than mixing dN and -dN eigenvalues.
- The pseudosphere gives ALL profiles z0 plus/minus the integral, proves the unit
  tractrix tangent, and identifies the angular cover/translation quotient.
  There is no globally real angular map from the actual circular surface to H.
- The z^n index exercise requires integer n>=1 for an isolated zero; n=0 has no
  zero there. Girard uses standard convex minor-arc triangles, and the geodesic
  exercise treats coincident endpoints and geometric-arc equality up to pauses.
- Green's identity proves nonnegative REAL eigenvalues also for complex-valued
  eigenfunctions. The zero eigenspace and r2(0)=1 are explicit.
- Existence of a generic height's finite critical set uses both CLOSEDNESS and
  isolation in a compact surface, not isolation alone.
- Smooth surface classification by genus, higher Poincare--Hopf, general Weyl law,
  spherical harmonics and Milnor's example are identified as quoted extensions
  or later comparisons, not prerequisites of the local proofs.

New material: conformal-chart curvature/spherical circle length; global conformal
change and torus obstruction; normalized rectangular-torus modes with first
multiplicity and cell-count leading term; degenerate gradient index -2 splitting
into two ordinary saddles for either sign of a perturbation. Diagrams show
stereographic circle lengths and Fourier lattice multiplicities.

The full ten-unit checkpoint on 5c094ef0a19842eb098059a65b5ed190214d60e6 exited 0 at 441 print pages. Its EPUB is 30,384,213 bytes, 75 figure plates at 1800 pixels, with media checks passing and all 18,350 local links/media references resolved. Artifact hashes and logs are stored here. This full build predates Chapter 4's rewrite.
