# Book 9 — Shapes

*The Geometry of Connection.*

**Element.** The joints. How rooms connect, and what curvature can be read from inside a room.

**Source.** `tome9-shapes`. Ten main chapters and twelve geometry appendices. About 343 pages. The October review scored it 7. Andreief's identity now divides by \(n!\) in `ch08-haar.tex`. The letter \(\Delta\) is still asked to be both a modular function and a Vandermonde product in that chapter; the notation sheet gives \(V\) and \(\delta\).

## Promise

A sphere, a torus, and the set of rotations are shapes. Calculus on them, curvature read from inside, the fundamental group, homology, Lie groups, Haar measure on the unitary group, and the hyperbolic plane. Weyl's integration formula is the joint into Book 12: a random unitary matrix has a law for its eigenvalues. The geometry appendices are the pictorial elementary track, from Euclid to convex bodies. They are not a second Book 9.

## Prerequisites

Book 7: topology, measure, Fubini, change of variables. Book 8: the inverse-function theorem if this book does not prove it, and the complex analysis of Chapter 9. Book 3: groups and quaternions. The book proves the inverse and implicit function theorems itself if that is what `ch01-manifolds.tex` does; Book 7's change of variables is cited, not rebuilt.

## How the subtitle is delivered

The title is Shapes. The subtitle says which geometry: connection. A chapter stays if it shows how pieces join, how a space is tied to its loops or its holes, or how a shape in this book connects to a later floor. A gallery of Euclidean tricks does not.

| Connection | Chapters |
| --- | --- |
| The infinitesimal connection | 1–2 and 4: charts, flows that fail to commute, curvature read from inside, Gauss–Bonnet |
| Forms joining the classical theorems | 3: Stokes as one statement |
| Spaces joined to their covers and holes | 5–6: the fundamental group, coverings, homology |
| The series joined to its shapes | 7–10: the double cover of the rotation group, Weyl's eigenvalue law, the modular surface and continued fractions, Crofton's measure on lines |
| Shapes that connect | Appendices B–G and I–L, once each opening says what is being connected. Appendix H keeps the picture of a cubic and sends the group law to Book 13. |

**Move or fold.** Appendix A, Euclid revisited (`geometry-ch01-euclid.tex`), is triangle centres, Napoleon, and Morley. That is a shape, and it is not a connection. FOLD each theorem that truly joins lines (Ceva, the Euler line) into exercises of Appendix B, Transformations. The rest does not move to another book: no other title wants it. It leaves the edition's main text. The Riemann mapping theorem arrives from Book 8, as a conformal connection, beside the hyperbolic and Möbius material.

## Parts

The catalog names stay. Manifolds and Surfaces is the opening geometry. Forms and Homology joins Stokes, curvature, coverings, and homology: that is the connection of a shape to its holes. Groups and Geometry joins the double cover, Weyl's formula, the modular surface, integral geometry, the Riemann mapping theorem from Book 8, and the appendices that still connect one shape to another. No part is renamed.

| Part | Name | Chapters |
| --- | --- | --- |
| I | Manifolds and Surfaces | 1–2 |
| II | Forms and Homology | 3–6 |
| III | Groups and Geometry | 7–10, the Riemann mapping theorem, and Appendices B–L. Appendix A folds as described above. |

---

### Part I. Curves and Surfaces

#### Chapter 1. Smooth Manifolds

**Status.** KEEP — `tome9-shapes/chapters/ch01-manifolds.tex` (854 lines).

**Hook.** A sphere is round, and a small piece of it looks flat. A manifold is a space in which every small piece looks like a piece of \(\mathbb R^n\).

**Synopsis.** Calculus in \(\mathbb R^n\), submanifolds, abstract manifolds, tangent spaces, the regular-value theorem, Sard in equal dimensions, and the easy Whitney embedding. The inverse-function theorem is the first joint: it is how charts fit. Book 7 cited change of variables and left this theorem to be proved where it is used.

**Proved.** The inverse and implicit function theorems. The regular-value theorem. Sard in equal dimensions. Every compact manifold embeds in some \(\mathbb R^N\), in the easy form.

**Examples.** \(S^n\) as a regular level set. One manifold atlas that is not a single graph.

**Figures.** Two.

#### Chapter 2. Vector Fields and Flows

**Status.** KEEP — `chapters/ch02-flows.tex` (569 lines).

**Hook.** A vector field is an arrow at every point. Follow the arrows and the whole space moves. Two flows, run one after the other, need not commute.

**Synopsis.** Ordinary differential equations in \(\mathbb R^n\), flows on manifolds, the Lie bracket, Frobenius, and the hairy-ball theorem. Non-commuting flows are curvature's infinitesimal shadow, though the curvature tensor itself is not this book's load.

**Proved.** Existence and uniqueness for Lipschitz vector fields on \(\mathbb R^n\). The Lie bracket as the commutator of flows. Frobenius. The hairy-ball theorem.

**Examples.** A rotation field on \(\mathbb R^2\) and its flow. The hairy ball on \(S^2\).

**Figures.** Two.

#### Chapter 4. Curvature

**Status.** KEEP — `chapters/ch04-curvature.tex` (475 lines). REVISE the title clash with Appendix L, also called Curvature. This chapter is intrinsic surface geometry. The appendix is curves and polyhedral defect. Rename the appendix **Curvature of curves and polyhedra**.

**Hook.** An ant on a surface cannot see the surface bend in space. It can measure lengths, angles, and the circumference of a small circle.

**Synopsis.** Riemannian metrics, the connection form, surfaces in space, Gauss's Theorema Egregium, Gauss–Bonnet, and the Laplacian of a surface. Gauss–Bonnet is the climax of the geometric half: a local curvature integrates to a global invariant. Chern's proof for surfaces, if that is the proof in the file, stays. There is no curvature tensor and no Hopf–Rinow.

**Proved.** Theorema Egregium for surfaces. Gauss–Bonnet.

**Examples.** The sphere, total curvature \(4\pi\). A torus, total curvature 0. One polyhedral picture may wait for the appendix so the two proofs are not confused.

**Figures.** Two.

### Part II. Forms and Homology

#### Chapter 3. Differential Forms and Stokes' Theorem

**Status.** REVISE — `chapters/ch03-forms.tex` (506 lines). de Rham cohomology is defined. The general de Rham theorem is not a numbered theorem of this book; the proof on the page is the punctured plane. The sentence a reader would quote must say that. Later chapters do not use the general statement.

**Hook.** Green, Gauss, and Stokes look like three theorems. They are one line.

**Synopsis.** Alternating forms, the exterior derivative, orientation, integration, Stokes, and de Rham cohomology. The half-space \(x_1\le 0\) with the outward normal is the local computation. Brouwer's fixed-point theorem in every dimension is the application. The classical theorems are absorbed into the definitions, and the text may say so.

**Proved.** Stokes' theorem. The Poincaré lemma in the star-shaped case the chapter treats. Brouwer's no-retraction theorem. de Rham's theorem for the punctured plane, labelled as that case.

**Examples.** The fundamental theorem of calculus as Stokes in dimension 1. The area of a plane region as a line integral.

**Figures.** Two.

#### Chapter 5. The Fundamental Group and Coverings

**Status.** KEEP — `chapters/ch05-coverings.tex` (599 lines).

**Hook.** Walk around a circle and you are home, having gone around once. Go around twice and you have not repeated the first walk.

**Synopsis.** Loops, the fundamental group, covering spaces, the circle, deck transformations and a Galois correspondence for coverings, Seifert–van Kampen, and Nielsen–Schreier. The correspondence is named as a cousin of Book 3's Galois correspondence, not as the same theorem. Free groups appear here. Book 3 sent them forward.

**Proved.** \(\pi_1(S^1)=\mathbb Z\). The lifting criterion. Seifert–van Kampen. Nielsen–Schreier: a subgroup of a free group is free.

**Examples.** The figure-eight and its free group. One covering of the circle.

**Figures.** Two.

#### Chapter 6. Homology

**Status.** REVISE — `chapters/ch06-homology.tex` (536 lines). The Borsuk–Ulam transfer at the lines the review named should deduce \(H_k(\mathbb{RP}^n;\mathbb Z/2)\cong\mathbb Z/2\) from the exact sequence as printed. The exact sequence already contains a correct proof. The sentence does not. The classification of surfaces stays a remark.

**Hook.** Count the vertices of a cube, subtract the edges, add the faces: \(8-12+6=2\). The same count for a tetrahedron, an icosahedron, or a soccer ball.

**Synopsis.** Chain complexes, simplicial and singular homology, Mayer–Vietoris, excision, spheres and degree, invariance of domain, and Borsuk–Ulam. Invariance of domain is the theorem that an open set of \(\mathbb R^n\) is not an open set of \(\mathbb R^m\). Homology \(H_n\) is the series' notation. de Rham cohomology keeps the subscript \(\mathrm{dR}\). Group cohomology waits for Abstraction.

**Proved.** Homotopy invariance. Mayer–Vietoris. Excision. \(H_n(S^n)=\mathbb Z\). Invariance of domain. Borsuk–Ulam, after the exact-sequence sentence is rewritten.

**Examples.** The cube's Euler characteristic. \(\mathbb{RP}^2\), whose homology Book 10's universal-coefficient discussion quotes as an exercise. Keep that exercise's label stable, or update the citation.

**Figures.** Two.

### Part III. Groups and Geometry

#### Chapter 7. Matrix Lie Groups

**Status.** KEEP — `chapters/ch07-liegroups.tex` (361 lines).

**Hook.** Rotations, unitary matrices, and matrices of determinant one are groups and manifolds, and the two structures lock.

**Synopsis.** Matrix groups and their Lie algebras, the adjoint representation, \(\mathrm{SU}(2)\to\mathrm{SO}(3)\), and \(\mathrm{SL}_2(\mathbb R)\) with the maximal torus of \(U(n)\). The plate trick of Book 3 is now a homomorphism of Lie groups. A full turn is not the identity on the double cover, and the chapter can point back in one sentence.

**Proved.** The closed-subgroup theorem for matrix groups, if the file proves it. The double cover. The Lie algebra of \(U(n)\), \(\mathrm{SU}(n)\), and \(\mathrm{SO}(n)\).

**Examples.** A rotation as a unit quaternion, now inside \(\mathrm{SU}(2)\). One one-parameter subgroup.

**Figures.** One.

#### Chapter 8. Haar Measure and Weyl Integration

**Status.** REVISE — `chapters/ch08-haar.tex` (516 lines). Andreief's last sentence now divides by \(n!\). Rename the two \(\Delta\)s. The modular function of Haar measure is \(\delta\). The Vandermonde product is \(V\), or it is written as a product. This chapter is the plant of the sine kernel: Dyson's pair correlation for finite \(n\).

**Hook.** What does it mean to choose a unitary matrix at random? There is one fair way.

**Synopsis.** Invariant volume forms, sampling a random unitary matrix, Weyl's integration formula, and eigenvalue correlations. The joint law of the eigenvalues is \(\frac1{n!}|V|^2\) times Haar measure on the torus. Book 12 quotes this as the finite-\(n\) circular ensemble and passes to the sine kernel. The citation number, Theorem 8.15 if that is the one Book 12 uses, stays stable.

**Proved.** Existence of Haar measure on a compact matrix group, by the volume form, citing Book 8's Haar theorem where the argument is the same. Weyl's integration formula. Andreief's identity.

**Examples.** \(U(2)\), eigenvalues computed by hand. One pair correlation at finite \(n\).

**Figures.** One.

#### Chapter 9. The Hyperbolic Plane and the Modular Group

**Status.** KEEP — `chapters/ch09-hyperbolic.tex` (371 lines). This is the return of Book 2's continued fractions.

**Hook.** The hyperbolic plane is the most symmetric surface of negative curvature. Its symmetries are the matrices of determinant one.

**Synopsis.** The isometry group, points and directions, the modular group, and the Farey tessellation with cutting sequences. A geodesic on the modular surface records a continued fraction. Book 11's Gauss map is the ergodic form of the same walk. The chapter may say so in one sentence.

**Proved.** The classification of isometries, or the form the file proves. The fundamental domain of \(\mathrm{SL}_2(\mathbb Z)\). The cutting-sequence description of a geodesic.

**Examples.** The modular fundamental domain, drawn. The continued fraction of a quadratic, read as a closed geodesic.

**Figures.** Two.

#### Chapter 10. Integral Geometry

**Status.** KEEP — `chapters/ch10-integral.tex` (322 lines). Buffon's needle from Book 4 returns as Crofton's formula.

**Hook.** How many lines meet a curve? The question needs a measure on the set of lines, and symmetry allows one.

**Synopsis.** The kinematic measure of lines, Crofton's formula, convex sets, and moving curves. Book 4's needle is the case of a segment. The appendix on convex bodies proves Brunn–Minkowski and may share the needle; this chapter owns the invariant measure.

**Proved.** Uniqueness of the rigid-motion-invariant measure on lines, up to a constant. Crofton's formula.

**Examples.** Buffon's needle recovered. The length of a convex curve from its support function, if the chapter does that.

**Figures.** One.

### Appendices A–L

The appendices are the elementary, pictorial track. KEEP them. They do not replace the main chapters. Two title repairs are noted below.

#### Appendix A. Euclid Revisited

**Status.** KEEP — `chapters/geometry-ch01-euclid.tex` (576 lines).

**Hook.** Euclid to Ptolemy: there is no royal road.

**Synopsis.** The plane as the complex numbers, the classical centres, Ceva, Napoleon, and Morley. Complex numbers from Book 1 do Euclidean geometry.

**Proved.** Ceva. Morley, if the file's proof is complete.

**Examples.** The Euler line of a named triangle. One Morley triangle.

**Figures.** Three.

#### Appendix B. Transformations

**Status.** KEEP — `chapters/geometry-ch02-transformations.tex` (618 lines).

**Hook.** Klein's Erlangen programme, in his own sentence: a manifold and a group of transformations.

**Synopsis.** Isometries, Klein's programme, finite symmetry groups of the plane, friezes, the crystallographic restriction, and the shortest closed billiard path. Book 3's finite subgroups of \(\mathrm{SO}(3)\) are the spatial cousins. This appendix owns the plane.

**Proved.** The crystallographic restriction. Classification of friezes, if the file finishes it.

**Examples.** A frieze of each type, or one of each that the chapter draws. The Fagnano billiard, the acute triangle's orthic triangle.

**Figures.** Three.

#### Appendix C. Inversion

**Status.** KEEP — `chapters/geometry-ch03-inversion.tex` (644 lines).

**Hook.** Soddy's kiss: the bend is the inverse of the distance from the centre.

**Synopsis.** Inversion, Ptolemy, Steiner's porism, the Pappus chain, Descartes' circle theorem, Apollonian gaskets, Möbius transformations, and Feuerbach. Inversion is the geometric face of the Möbius group Book 9's modular chapter uses.

**Proved.** Ptolemy via inversion, or the file's proof. Descartes' circle theorem. Feuerbach.

**Examples.** Four mutually tangent circles and their bends. The nine-point circle and the incircle.

**Figures.** Three.

#### Appendix D. Projective Geometry

**Status.** KEEP — `chapters/geometry-ch04-projective.tex` (696 lines).

**Hook.** Cayley: metrical geometry is a part of descriptive geometry, and descriptive geometry is all geometry.

**Synopsis.** The projective plane, projective transformations, Desargues, Pappus, the cross-ratio, the fundamental theorem, and finite projective planes. The cross-ratio is the invariant. Book 13's plane curves will count intersections in the projective plane.

**Proved.** Desargues. Pappus. The fundamental theorem of projective geometry in the form the appendix states.

**Examples.** A perspectivity. The Fano plane.

**Figures.** Four.

#### Appendix E. Conics

**Status.** KEEP — `chapters/geometry-ch05-conics.tex` (586 lines).

**Hook.** Galileo's book of nature, written in triangles, circles, and other figures.

**Synopsis.** Conics as quadratic forms, parametrisation, the three affine types, Pascal, poles and polars, and Poncelet's porism. A rational parametrisation of the circle is the same chord method as Book 2's conics, now geometric.

**Proved.** The classification of real affine conics. Pascal's theorem. Poncelet for triangles, or the case the file proves.

**Examples.** A circle parametrised by stereographic projection. One Poncelet triangle.

**Figures.** Four.

#### Appendix F. Quadratic Forms and Quadrics

**Status.** KEEP — `chapters/geometry-ch06-quadrics.tex` (508 lines).

**Hook.** Sylvester, on reducing a quadratic form by an orthogonal substitution.

**Synopsis.** Symmetric bilinear forms, Sylvester's law of inertia, quadric surfaces, ruled quadrics, Witt's theorem, and quadrics over finite fields. Inertia is the continuous shadow of the Hasse invariant Book 13 will use. A sentence may say so.

**Proved.** Sylvester's law. Witt's cancellation or extension theorem, at the strength the file proves.

**Examples.** A hyperboloid of one sheet, ruled. One form over \(\mathbb F_p\).

**Figures.** Three.

#### Appendix G. Plane Curves

**Status.** KEEP — `chapters/geometry-ch07-curves.tex` (505 lines). The multiplicity \(I_P\) is said to depend a priori on an auxiliary point. REVISE that sentence so the independence is either proved or the dependence is part of the definition the reader is allowed to use. Bézout's count itself checked out in the review.

**Hook.** Euler to Cramer: nine points are worth but eight.

**Synopsis.** The resultant, plane curves, Bézout, singular points, and Cayley–Bacharach. Bézout is the theorem Book 13's curve chapter will prove again with more algebra. This appendix is the pictorial count. Book 13 should cite it as the picture, not as the proof it relies on.

**Proved.** Bézout's theorem at the level the appendix reaches. Cayley–Bacharach for the cubic case the file proves.

**Examples.** A line and a conic. Two conics meeting in four points.

**Figures.** Three.

#### Appendix H. Cubic Curves

**Status.** REVISE — `chapters/geometry-ch08-cubics.tex` (471 lines). Associativity of the chord-and-tangent law is proved when the nine points are distinct, from Cayley–Bacharach. The text must not use \((E(K),+)\) as a group for every triple before Book 13, Chapter 12, which proves the group law from Riemann–Roch. The flex theorem that needs \(E[3]\cong(\mathbb Z/3)^2\) points at that chapter. The Weierstrass addition formulas may stay as formulas. A six-points exercise that uses the unfinished group law points at Book 13 as well.

**Hook.** Newton: every cubic is the shadow of one of five parabolas.

**Synopsis.** Chords and tangents, the Weierstrass form, the nine flexes, and cubics over finite fields. The picture of the group law is this appendix's gift. The proof that it is a group is Book 13's. Abstraction's sentence about \(\mathrm{Cl}(A)\) for a cubic already refuses the word "isomorphism"; this appendix should not rebuild that claim.

**Proved.** The Weierstrass form over a field of characteristic not 2 or 3. The distinct-points case of associativity, labelled as that case. Bézout's count of flexes, if it does not require the group.

**Examples.** \(y^2=x^3-x\), the tangent at a named point. One addition of two rational points by the formulas, checked by arithmetic, not by the general theorem.

**Figures.** Four.

#### Appendix I. Lattices and Sphere Packings

**Status.** REVISE — `chapters/geometry-ch09-lattices.tex` (467 lines). Fermat's two-square theorem in four lines after Minkowski is a return of Book 2, and it should say so. The Hermite-constant solution must not cite "two standard facts (Cassels)" for the determinant of a projected lattice. Write the two projection lemmas, or drop the exercise's claim.

**Hook.** Kepler, on the greengrocer's packing of pellets.

**Synopsis.** Lattices, Minkowski's theorem, Gauss reduction in the plane, packings, and the \(E_8\) root lattice with its \(240\) minimal vectors. Minkowski's convex-body theorem is proved again in Book 13 for number fields. This appendix owns the geometric theorem and the packing pictures.

**Proved.** Minkowski's theorem. Gauss reduction. The count \(112+128=240\) of minimal vectors of \(E_8\), if the file derives it.

**Examples.** The hexagonal lattice. Sums of two squares via Minkowski, for \(p=13\).

**Figures.** Four.

#### Appendix J. Non-Euclidean Geometry

**Status.** KEEP — `chapters/geometry-ch10-noneuclid.tex` (479 lines). The main Chapter 9 is the modular surface. This appendix is spherical and hyperbolic geometry for itself.

**Hook.** Bolyai, writing to his father that he has created a world out of nothing.

**Synopsis.** Spherical geometry, the hyperbolic plane, the area of a triangle, and the Poincaré disk. Angle defect is curvature made elementary, before Chapter 4's intrinsic proof. The two accounts should point at each other.

**Proved.** The area of a hyperbolic triangle is its angle defect. The spherical excess formula.

**Examples.** A triangle with three right angles on a sphere. An ideal hyperbolic triangle, area \(\pi\).

**Figures.** Three.

#### Appendix K. Convex Bodies

**Status.** KEEP — `chapters/geometry-ch11-convex.tex` (419 lines).

**Hook.** Dido's hide: as much land as a bull's skin can enclose.

**Synopsis.** Convex sets, Helly, Buffon's needle again, curves of constant width, and Brunn–Minkowski. Brunn–Minkowski is the inequality. The needle here is a computation; Chapter 10 owns the invariant measure. A sentence prevents a third proof from looking like a new theorem.

**Proved.** Helly's theorem in the dimensions the appendix treats. Brunn–Minkowski. The existence of a curve of constant width that is not a circle, the Reuleaux triangle.

**Examples.** The Reuleaux triangle. One Helly configuration in the plane.

**Figures.** Three.

#### Appendix L. Curvature of Curves and Polyhedra

**Status.** REVISE — `chapters/geometry-ch12-curvature.tex` (382 lines). Rename from "Curvature". Descartes' theorem on polyhedral defect is the elementary Gauss–Bonnet. Chapter 4 is the intrinsic theorem. The appendix's first sentence says which is which.

**Hook.** Gauss: if a surface is developed on another, the curvature at each point is unchanged.

**Synopsis.** Plane curves, the four-vertex theorem, a second look at surface curvature for the reader of the appendix only, Gauss–Bonnet in its polyhedral form, and Descartes' theorem. A reader of the appendix who has not read Chapter 4 still gets a true theorem. A reader of both should not think the appendix repeats Chapter 4.

**Proved.** The four-vertex theorem, if the file's proof is complete. Descartes' theorem \( \sum \mathrm{defect}=4\pi\).

**Examples.** An ellipse and its four vertices. A cube's eight corners, each of defect \(\pi/2\).

**Figures.** Two.

## Owns, defers, hands forward

**Owns.** Manifolds, flows, Stokes, Gauss–Bonnet for surfaces, the fundamental group, singular homology through invariance of domain and Borsuk–Ulam, matrix Lie groups, Weyl's integration formula, the modular surface, Crofton, and the geometry appendices as pictures and elementary theorems.

**Defers.** The group law on a smooth cubic in every characteristic, for every triple (Book 13). de Rham's theorem in general. Poincaré duality, the curvature tensor, cohomology with cup products. The sine-kernel limit (Book 12).

**Hands forward.** Weyl's formula to Book 12. The modular surface to Book 11's Gauss map and Book 13's modular forms. The picture of an elliptic curve to Book 13, which proves the group law on its own.

## Pages and effort

Baseline 343 pages. Target 340–370. Effort: moderate. The analytic core stays. The work is the de Rham sentence, the Borsuk–Ulam sentence, the two \(\Delta\)s, the cubic group's citation, the Hermite solution, the multiplicity sentence, and one renamed appendix.
