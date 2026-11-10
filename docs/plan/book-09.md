# Volume 9 — Shapes

*The Geometry of Connection.*

**Status of this file.** Blueprint of Volume 9 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. No proof named here has been verified.

**Series part.** III. Analysis and Geometry. **Directory.** `volume9-shapes`.

## Central question

How do spaces join, and what can be measured from inside one? Charts join into a manifold, loops and holes describe how it is connected, and a group that is also a manifold carries one fair measure.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 7 | Topology, compactness, measure, Fubini, change of variables |
| Volume 8 | Haar measure and its uniqueness on compact groups; the complex analysis of Chapter 14 (for the Riemann mapping theorem); linear algebra of the appendices |
| Volume 3 | Groups, quotients, quaternions |
| Volume 5 | Cauchy's formula and residues (for the Riemann mapping theorem and winding numbers) |
| Volume 6 | The fundamental domain of \(SL_2(\mathbb Z)\), Chapter 12 (after decision D-20) |
| Volume 2 | Continued fractions |

No statement of Volumes 10–15 is used as a premise. Today Chapter 9 takes one fact about the fundamental domain from Volume 13; that fact moves to Volume 6.

## Structure

Unchanged.

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Manifolds and Surfaces** | | |
| 1 | Smooth Manifolds | `ch01-manifolds.tex` | Keep |
| 2 | Vector Fields and Flows | `ch02-flows.tex` | Keep |
| | **Part II. Forms and Homology** | | |
| 3 | Differential Forms and Stokes' Theorem | `ch03-forms.tex` | Keep |
| 4 | Curvature | `ch04-curvature.tex` | Keep; two statements need a proof or a heading |
| 5 | The Fundamental Group and Coverings | `ch05-coverings.tex` | Keep |
| 6 | Homology | `ch06-homology.tex` | Keep |
| | **Part III. Groups and Geometry** | | |
| 7 | Matrix Lie Groups | `ch07-liegroups.tex` | Keep |
| 8 | Haar Measure and Weyl Integration | `ch08-haar.tex` | Keep |
| 9 | The Hyperbolic Plane and the Modular Group | `ch09-hyperbolic.tex` | Keep; one citation changes |
| 10 | The Riemann Mapping Theorem | `riemann-mapping.tex` | Keep |
| 11 | Integral Geometry | `ch10-integral.tex` | Keep |
| | **Appendices** | | |
| A | Transformations | `geometry-ch02-transformations.tex` | Keep |
| B | Inversion | `geometry-ch03-inversion.tex` | Keep |
| C | Projective Geometry | `geometry-ch04-projective.tex` | Keep |
| D | Conics | `geometry-ch05-conics.tex` | Keep |
| E | Quadratic Forms and Quadrics | `geometry-ch06-quadrics.tex` | Keep |
| F | Plane Curves | `geometry-ch07-curves.tex` | Keep; heading says what is proved |
| G | Cubic Curves | `geometry-ch08-cubics.tex` | Keep; heading says what is proved |
| H | Lattices and Sphere Packings | `geometry-ch09-lattices.tex` | Keep |
| I | Non-Euclidean Geometry | `geometry-ch10-noneuclid.tex` | Keep |
| J | Convex Bodies | `geometry-ch11-convex.tex` | Keep |
| K | Curvature of Curves and Polyhedra | `geometry-ch12-curvature.tex` | Keep |

The appendices are the elementary, pictorial track. Each opens by saying what is being connected and what it assumes. They may be cited as premises under rule R1; today only the lattice appendix (Minkowski) is cited by a later volume, and Volume 13 proves Minkowski's theorem itself.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Inverse and implicit function theorems; Sard in equal dimensions | | 1 |
| Picard–Lindelöf; Frobenius; the hairy ball theorem | | 2 |
| Stokes; Brouwer's fixed point theorem; the Poincaré lemma | | 3 |
| Theorema Egregium; Gauss–Bonnet | | 4 |
| Classification of coverings; Seifert–van Kampen | | 5 |
| Mayer–Vietoris; excision; invariance of domain; Borsuk–Ulam | | 6 |
| Closed subgroups of matrix groups are Lie groups; the spin double cover | | 7 |
| Haar measure on a matrix Lie group and its uniqueness; Weyl's integration formula; Andreief and Heine's identities; correlation functions of a random unitary matrix; the pair correlation at finite \(n\) | `thm:weyl`, `lem:andreief`, `thm:heine`, `thm:correlations`, `cor:dyson` | 8 |
| Isometries of the hyperbolic plane; the Farey tessellation; Series's coding of geodesics by continued fractions | | 9 |
| Montel; the Riemann mapping theorem | | 10 |
| Crofton's formula; Cauchy's surface area formula | | 11 |

## Stated without proof

| Statement | Heading must say |
| --- | --- |
| de Rham's theorem in general | Not proved. The punctured plane is proved |
| Classification of compact surfaces | Quoted |
| The two statements of Chapter 4 that have no proof on the page | Proved, or headed as quoted, after inspection |
| Bézout's theorem with full multiplicities (Appendix F) | Proved in Volume 13, Chapter 14. The appendix proves the cases it states |
| Associativity of the chord-and-tangent law for all triples (Appendix G) | Proved in Volume 13, Chapter 15. The appendix proves the case of nine distinct points |
| The sine-kernel limit | Preview of Volume 12 |
| Ergodicity of the geodesic flow | Quoted |

## Climax

Gauss–Bonnet in Part II: curvature, measured from inside, adds up to a number that counts holes. Weyl's integration formula in Part III: the eigenvalues of a random unitary matrix repel, with an exact density. That formula is the door Volume 12 walks through.

## Motivation and history

Gauss's survey of Hanover and the Theorema Egregium, Riemann's Habilitation lecture, Poincaré's Analysis Situs, Brouwer, Lie and Klein, Weyl's 1925 papers, Buffon and Crofton. The appendices carry Klein's Erlangen programme, Soddy, Cayley, Newton's cubics, Kepler's packing, Bolyai, Dido.

## Examples and exercises

The sphere, the torus and the rotation group recur in every chapter of Parts I–III: as manifolds, with their flows, forms, curvature, coverings and homology, and finally as groups. Appendices carry 11–16 exercises each, mostly constructions and computations.

## Figures and experiments

This is the most illustrated volume. Every figure is built from source in the repository. One experiment is printed: eigenvalue angles of sampled unitary matrices against independent uniform points; its script and seed are in the ledger.

## Changes from the current manuscript

**Preserve.** All chapters and appendices, in their order.

**Rewrite.** Chapter 9: the citation of "Volume 13, Theorem 17.1" becomes a citation of Volume 6, `thm:fundamental`. Chapter 8: the letter \(\Delta\) is used for two things; the modular function becomes \(\delta\) and the Vandermonde product \(V\). Appendix G: the text must not treat the points of a cubic as a group for all triples before Volume 13.

**Label.** The headings in the table above. The intersection multiplicity in Appendix F: either its independence of the auxiliary choice is proved, or the choice is part of the definition.

**Remove.** Hand-typed citations of "Volume 13, Chapter 5" and similar stale numbers. In Appendix H, a solution that cites "two standard facts" without proof: prove them or drop the claim.

**Missing.** One sentence in Chapter 6 deducing the homology of real projective space from the exact sequence actually printed.

## Links

**From Volume 8.** Haar measure on abelian groups becomes Haar measure on Lie groups.
**To Volume 10.** Homology, used as an example by homological algebra; the unitary group, for Weyl's character formula.
**To Volume 11.** The modular surface, for the Gauss map.
**To Volume 12.** Weyl's integration formula and the finite-\(n\) correlation functions, the premises of the sine kernel.
**To Volume 13.** Pictures of curves; the modular group.

## Size

About 11,180 source lines: about 5,270 in the eleven chapters and about 5,900 in the appendices. **Estimate, not measured:** 310–340 printed pages.

## Mathematical risks

1. Chapter 4: twelve statements, ten proofs.
2. Stokes on a manifold with boundary: orientation conventions.
3. Excision and the subdivision argument.
4. Chapter 8: the Jacobian in Weyl's formula and the constant in Andreief's identity, repaired once.
5. Appendix G's use of the group law.
6. The Riemann mapping theorem depends on Volume 8, Chapter 14 after the reorder there.

## Acceptance requirements

- No premise from Volumes 10–15.
- Verification records for: Stokes, Gauss–Bonnet, Seifert–van Kampen, excision, `thm:weyl`, `thm:heine`, `thm:correlations`, `cor:dyson`, the Riemann mapping theorem, Crofton.
- Every statement of the "without proof" table carries its heading.
- Volume 12's citations of Chapter 8 resolve by label.
- The ten editorial standards of the master plan, section 6.5.
