# Volume 9 review index — final manuscript and local validation

PR: https://github.com/OussamaSegh/Order-and-Chance/pull/243.
Starting main: `9cd86c15bd386d59e7a1c6f96fb0ea5ed808c26b`, 385 print pages.
All 22 units have complete rewrites and author-directed final review. Each adds two figures and four
exercises with fresh labels, difficulty, hints and full idea/writeup solutions:
**44 figures and 88 exercises** altogether. Two unnumbered, credited public-domain
photographs have been added. Original figure sources, complete figure blocks,
printed labels and numbered structure remain protected by the baseline audits.

The final mathematical and editorial review was performed by Codex at the
author's explicit direction, “You review and merge.” No independent second
reader is claimed. [The mathematical review](final-mathematical-review.md),
[editorial review](final-editorial-review.md) and [statement records](final-statement-review.json)
cover the complete source and every original numbered statement. R01–R20 are
tracked in postrewrite-review-findings.md. The unit reports below retain their
historical build checkpoints; final validation supersedes their pending statuses.

| Printed unit | Rewrite and principal mathematical repairs | Fixing commit | Detailed writer record |
| --- | --- | --- | --- |
| 1. Smooth manifolds | Rebuild local calculus and global constructions; include empty/zero-dimensional cases, nonempty regular fibres, connected analytic identity hypothesis and n≥1 strong Whitney/SL assumptions. | `4c3168bf`, `fb4502e3` | [Chapter 1](ch01-review.md) |
| 2. Vector fields and flows | Complete Picard/variational regularity and finite escape, Frobenius endpoint ranks, bracket signs and projective/quaternion examples. | `195cd412` | [Chapter 2](ch02-review.md) |
| 3. Forms and Stokes | Complete boundary orientation and zero-dimensional Stokes; H0 is a product over components, with full constructive torus calculations. | `3929915f`, `612854ac`, `2c0fccc8` | [Chapter 3](ch03-review.md) |
| 4. Curvature | Remove prerequisite circularity in Morse/Euler and local distance arguments; make quoted genus construction and sphere-chart reflection explicit. | `5d5391e7`, `30cbe592` | [Chapter 4](ch04-review.md) |
| 5. Coverings and fundamental groups | Repair the van Kampen boundary word, normalizer arguments and arbitrary-rank graph proof; retain covering hypotheses and require nonempty domains for exact root counts. | `7f656353`, `612854ac`, `30cbe592`, `2c0fccc8` | [Chapter 5](ch05-review.md) |
| 6. Homology | Supply subdivision/comparison/transfer details and empty augmentation conventions; handle projective top degree, null measures and connected Euler comparison. | `57f9e4ee`, `30cbe592`, `2c0fccc8` | [Chapter 6](ch06-review.md) |
| 7. Matrix Lie groups | Complete closed-subgroup charts, the spin lift and all exponential cases; repair unit-axis/identity and O0 exceptions and supply local polar coordinates. | `aad3d3d9` | [Chapter 7](ch07-review.md) |
| 8. Haar and Weyl integration | Prove measurable sampling, absolute Weyl Jacobian and correlation limits; isolate n=1 atoms/counts and signed domination. | `66ca56fd` | [Chapter 8](ch08-review.md) |
| 9. Hyperbolic geometry | Complete isometry/trace/equality and Farey coding proofs; distinguish horocycle normals, orbifold points, conjugate axes and complete reduced-form lists. | `8a19ff17` | [Chapter 9](ch09-review.md) |
| 10. Riemann mapping | Complete square-root/existence/extremal proof with empty Montel cases; separate quoted square-image construction and prove all normalization/equality examples. | `71d47c17` | [Chapter 10](ch10-review.md) |
| 11. Integral geometry | Replace infinite Haar pushforward with quotient factor; prove joint Borel counts, local isoperimetry and full C1 spherical incidence. Repair the affected Volume 15 citation to Example 8.5. | `5c094ef0` | [Chapter 11](ch11-review.md) |
| A. Transformations | Repair Fagnano's arbitrary-candidate argument and verify attainment; give lattice/frieze closure, billiard parity, signed Ceva and correct Routh vectors. | `d667a1c5` | [Appendix A](appa-review.md) |
| B. Inversion | Treat coincident Ptolemy points, forward Steiner chains, generalized-circle swap lines, the equilateral Feuerbach case and finite-sphere hexlet qualification. | `1dc39af8` | [Appendix B](appb-review.md) |
| C. Projective geometry | Keep all field/characteristic hypotheses; prove homogeneous infinity cross-ratios and semilinear steps; distinguish quoted division-ring results and explicit complex counterexamples. | `3c883119` | [Appendix C](appc-review.md) |
| D. Conics | Complete five-point/normal-form and empty-real cases, harmonic secant scope and smooth Poncelet invariant measure; prove Fuss and directed chord conditions. | `1f778501` | [Appendix D](appd-review.md) |
| E. Quadrics | Include zero-sized Gram and rank cases, nondegenerate quotient arguments and Witt cancellation; preserve Segre over every field. | `8418357e`, `66ca56fd` | [Appendix E](appendix-e-review.md) |
| F. Plane curves | Prove finiteness before projection, define proved multiplicities relative to O rather than claiming unproved intrinsic independence, repair characteristic-two conics and nonzero polars, and verify all nine intersections. | `62fa7135` | [Appendix F](appf-review.md) |
| G. Cubics | Correct geometric versus rational neutral claims and affine Hesse incidence; retain the nine-distinct association scope, prove elementary doubling infinitude and check all finite recursions. | `42e0f8fa`, `835800ac`, `2c0fccc8`, `21ca4d5a` | [Appendix G](appg-review.md) |
| H. Lattices | Repair n=0 and non-strict Minkowski boundary cases, measurable convex sets, reduction tie stopping, circle-count range and complete E8/root arguments. | `c363b76e`, `66ca56fd` | [Appendix H](appendix-h-review.md) |
| I. Non-Euclidean geometry | Make spherical/ideal hypotheses and Klein incidence explicit; supply local cosine-law error control instead of an unproved shortest-path step. | `71d47c17`, `1017fbd8` | [Appendix I](appendix-i-review.md) |
| J. Convex bodies | Correct the small-family disk-cover hypothesis; prove the full compact nonconvex Brunn–Minkowski bound, degenerate perimeters and fixed-epsilon Steiner limits. | `f393a975`, `fb4502e3` | [Appendix J](appendix-j-review.md) |
| K. Curvature | Handle periodic derivatives and non-strict/infinite four-vertex extrema, rank-zero Gauss-map area, prior planar separation, Fresnel tails and arbitrarily small flattening obstruction. | `ceef8ece`, `835800ac`, `2c0fccc8` | [Appendix K](appendix-k-review.md) |

Preface, back-cover blurb, KDP listing and approved-scope About the Cover were
rewritten in `331fa2c3`; `c724c7f4` restores the required cover-generator credit.
The cover explanation corrects the finite-group uniformisation claim. Approved
artwork and typography are preserved. `612854ac` keeps the unassigned paperback
ISBN blank and repairs two EPUB accent arguments. Photo evidence and attribution
are in ../../volume9-shapes/photos/CREDITS.md. Native print resolutions were
measured at 597.59 and about 1626.08 ppi.

Final book sources are `fb4502e3acda521b598c5bc3cd5e46e2f0e028d0`.
Both required commands exit 0 at 511 print pages. The EPUB is 31,586,815 bytes;
all 16,454 local links/media references/fragments resolve, with 99 full-width
plates. Source/numbering/figure preservation, 20 citation tests, cross-volume
citations, the register and all 12 numerical illustration scripts pass.
All added figures, photo placements, covers and representative actual EPUB
content were inspected. See [the final validation](final-validation.md).

R20 in `fb4502e3` supplies local arguments at the Cassini crossing and before
identifying outer surface content with perimeter. R15–R18 are fixed in
`2c0fccc8`; R13/R14 in `835800ac`; R19 clarifies the new Hesse caption in
`21ca4d5a`. Intentionally stopped intermediate full builds are labelled STOPPED,
with exit 143, and are never counted as successful exports.

Exact final-head CI, normal merge and exact-merge publication receipts are
recorded in the delivery section of PR #243. No Amazon KDP upload.
