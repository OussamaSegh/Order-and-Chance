# Chapter 9 — rewrite and checking record

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: full draft rewrite. Intermediate PDF-only build exited 0 at 419 print pages; no overflow or unresolved references. Original labels, captions, section numbers, figure sources and cover artwork pass preservation. Both new figures have been inspected in rendered pages. Twenty citation tests and the cross-volume checker (5,019 statements) pass.
A later checking pass by the writer is not an independent certificate; the
separate final manuscript review remains outstanding.

## Coverage and preservation

All introductory and explanatory prose, definitions, sixteen formal statements (including the definition),
proofs, historical discussion, transitions, chapter ending, six original
exercises, hints, idea/writeup solutions and reading guidance are rewritten.
The three original figure blocks and all bibliography records remain literal.
Original section titles, labels and formal-statement order are retained.
Two diagrams follow the last original figure. Four new exercises follow the six
original exercises, each with a unique label, difficulty, hint and full solution.
Poincaré's literal quotation is preserved.

## Explicit corrections and prerequisite repairs

- PSL2(R) is the orientation-preserving isometry group, not the full group.
  The original full classification, including reflection, is retained.
- The angle-sum corollary had both area<pi and an ideal triangle of area pi.
  It now gives area<=pi, with equality exactly for three ideal vertices.
- The perpendicular-bisector argument called the bisector nonvertical when
  nonhorizontal was needed. A solved centre equation replaces that inference.
- The distance proof handles coincident endpoints and distinguishes the unique
  geometric minimizing arc from its many monotone parametrizations.
- A local generator/equation argument establishes preservation of h-lines before
  using it in the distance proof; later inversion material is not a prerequisite.
- Hyperbolic circles explicitly require nonnegative radii, include radius zero,
  and distinctness of their Euclidean equations is justified before subtraction.
  The isometry theorem retains its stronger conclusion for maps not assumed onto.
- The carried unit vector for the right-N flow is normal, not tangent, to the
  horocycle. Both flows, their conventions and the factor -2 in k_theta are clear.
- Elliptic fixed points give cone points in the modular orbifold, rather than
  ordinary smooth surface points. The free left group action is distinguished.
- An axis projected under a nonprimitive matrix can traverse a geodesic several
  times; its translation length is not automatically the primitive period.
- A closed arithmetic axis requires the two conjugate quadratic endpoints, not
  one quadratic endpoint paired with an arbitrary other endpoint.
- Reduced forms are fully listed BEFORE boundary identifications: three triples
  for D=-20, four for D=-23, giving two and three equivalence classes.
- The quartic area calculation does not prove the existence of its tiling or its
  automorphism action. These are identified as quoted geometric facts.
- Coding/ergodic extensions are quoted with suitable return sections and boundary
  exceptions, not claimed proved by the elementary cutting argument.

## Additions checked in the draft

- Flow diagram: upward geodesic motion versus horizontal horocycle motion and
  upward carried normal, using the actual a_t and n_s conventions.
- Axis diagram: ell=log2, z=1+i, image 2+2i, circle centre 3 and radius sqrt5;
  graph cosh d=5/4+(x/y)^2/4. Axis displacement is exactly log2.
- Axis distance exercise: unique foot i|z|, rho=arsinh(|x|/y); equality and large
  rho checked without introducing later perpendicular-projection theorems.
- Ford disks: inverse-height equation, integer determinant separation, Farey
  tangency at h=1, and cusp truncation including h=1.
- Centralizers: determinant-one representatives, possible PSL sign excluded by
  nonzero trace, positive diagonal and antidiagonal forms, endpoint distinction.
- Direction measure: triangular Jacobian, adjoint determinants on E,H,F for N,A,K,
  normalized finite quotient volume; zero/full direction arcs handled. This is
  a probability calculation, not an ergodicity proof.

## Intermediate six-unit checkpoint and CI dependency repair

The full build on 66ca56fd5574659147614271c2ea2d2d7d8bd7ae exited 0 at
413 print pages. Its EPUB is 29,554,897 bytes, 67 plates at 1800 pixels,
and all 18,245 local links/media references resolve. Twenty citation tests pass,
and cross-volume citations match 5,015 numbered statements. Logs are stored here.
This predates the Chapter 9 rewrite and is not its build result.

CI run 43619208600 failed the Volume 3 inventory freshness check because the
approved canonical cover-note rewrite changed the hash of common/cover-notes.json.
Regeneration was compared structurally: ONLY that supporting-source hash changed;
all Volume 3 manuscript items, prose, figures and references were identical.
The inventory and conceptual-snapshot hashes are refreshed without assigning any new review statuses. A recorded hash-only reconciliation follows the existing Volume 6–8 practice.
Inventory --check and the strict Volume 3 registers then exit 0. This repairs the
cross-volume build dependency rather than bypassing the check.
