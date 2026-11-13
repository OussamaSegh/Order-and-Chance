# Volume 9 independent scored read

**Book.** *Order and Chance*, Volume 9, *Shapes: The Geometry of Connection*. Source directory `volume9-shapes` on `main` at `49001ed9` (13 November 2026). The Volume 9 files are unchanged since the rewrite commit `b9728797`.

**Artifacts.** The GitHub release `books` (published 13 November 2026, 11:15 UTC) contains `Volume.9.-.Shapes.pdf` (378 pages, 7 × 10 in, created 02:20 UTC) and `Volume.9.-.Shapes.-.Print.pdf` (377 pages, 7.125 × 10.25 in). Both postdate the rewrite. The EPUB is 26 MB. This read uses those files and the source. No book file was edited.

**Reader.** A reader who has Volumes 1–8 and is still meeting each new definition in plain English. Scores are against a careful textbook at that level (Spivak, Guillemin–Pollack, Lee, Hatcher for the topology, Hall for the matrix groups), not against a research monograph. A 10 would be flawless.

**Method.** Proofs named in “Verified correct” were read line by line and, where they contain a number, recomputed. Numbered back-references were checked against the statement counters in Volumes 1–8 and 13 (theorem, proposition, lemma, corollary, definition and example share one counter per chapter). Later volumes were searched for `Volume~9`. Classical constants were compared with Meckes’ notes on the classical compact groups (Weyl’s formula), with Adams’ count as recorded in the Wikipedia summary of *Vector fields on spheres* and the MathOverflow statement of the same formula, and with Cauchy’s surface-area formula as in MathWorld and Zachary’s note arXiv:1109.0595. Anything not in “Verified correct” is listed under “Not reviewed”. A numerical check is not a proof.

## Scorecard

Dimensions: (a) correctness, (b) rigor, (c) prerequisites, (d) clarity, (e) pedagogy, (f) exercises, (g) figures, (h) voice, (i) notation, (j) typography as rendered. Integers 0–10.

| Unit | a | b | c | d | e | f | g | h | i | j |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 Smooth Manifolds | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 2 Vector Fields and Flows | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 3 Forms and Stokes | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 4 Curvature | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 8 | 8 |
| 5 Fundamental group and coverings | 8 | 7 | 8 | 7 | 7 | 7 | 8 | 8 | 8 | 8 |
| 6 Homology | 9 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 8 | 8 |
| 7 Matrix Lie groups | 8 | 8 | 9 | 7 | 7 | 7 | 8 | 8 | 8 | 8 |
| 8 Haar measure and Weyl | 9 | 9 | 8 | 7 | 8 | 9 | 8 | 9 | 8 | 8 |
| 9 Hyperbolic plane and modular group | 8 | 8 | 5 | 8 | 8 | 7 | 8 | 9 | 8 | 8 |
| 10 Riemann mapping | 8 | 7 | 8 | 8 | 7 | 6 | 8 | 8 | 8 | 8 |
| 11 Integral geometry | 9 | 8 | 9 | 8 | 9 | 9 | 8 | 9 | 8 | 8 |
| A Transformations | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| B Inversion | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| C Projective geometry | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 8 |
| D Conics | 7 | 7 | 8 | 8 | 7 | 7 | 8 | 8 | 8 | 8 |
| E Quadratic forms and quadrics | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| F Plane curves | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| G Cubic curves | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| H Lattices and sphere packings | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| I Non-Euclidean geometry | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| J Convex bodies | 8 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |
| K Curvature of curves and polyhedra | 8 | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 |

### Why those chapter scores

**Chapter 1.** Correctness 9 and rigor 8: the inverse-function proof (Theorem 1.7) reduces to the identity derivative, gets a strict contraction on the closed ball of radius \(2r\), and puts the fixed point in the open ball; the \(C^k\) induction stops cleanly at \(k=1\). Prerequisites 8: Banach is Volume 7, Theorem 2.12, and that label is the Banach fixed-point theorem. Clarity, pedagogy and voice 8: the Riemann lecture, the robot arm and the figure-eight that is not a submanifold come before the definitions. Exercises 8: seven exercises, each with a hint and a solution; the cube-root and exponential examples were checked. Figures 8: two plates. Typography 8 on the sampled opener. Sard is only the equal-dimension case, and the text says so.

**Chapter 2.** Correctness 9: Milnor’s hairy-ball argument (Theorem 2.16) is the standard one, and the parity is right (\(n\) even means \(N=n+1\) odd, so \((1+t^2)^{N/2}\) is not a polynomial). The Adams count \(2^b+8a-1\) matches the classical formula for the number of fields on \(S^{n-1}\). The contact bracket \([\partial_y,\partial_x+y\partial_z]=\partial_z\) is correct. Rigor 8 because the Picard theorem was not re-read line by line. Prerequisites 8: Stone–Weierstrass is Volume 7, Theorem 4.19, and equidistribution of \(n\alpha\) is Volume 5, Corollary 6.14. The other scores are 8: the parking and falling-cat pictures earn their place, and every exercise has a hint and a solution.

**Chapter 3.** Correctness and rigor 8: the general de Rham theorem is stated as an identification that this book does not prove (the punctured plane is the numbered theorem). That is the right sentence. Stokes’ sign convention in the half-space was not re-derived here, so the score stays short of 9. Prerequisites 8: Brouwer for the disc is Volume 7, Theorem 6.7, which is that theorem. Clarity, pedagogy, exercises, figures, voice, notation and typography 8. The opening (Thomson’s letter, the Smith’s Prize paper, Cartan) is concrete.

**Chapter 4.** Correctness 9: Gauss–Bonnet–Chern (Theorem 4.11) tracks orientations, the index is the winding number, and the torus spectrum \(4\pi^2(k_1^2+k_2^2)\) with multiplicity \(r_2(n)\) is the right computation for \(-\Delta\) on \(\mathbb R^2/\mathbb Z^2\). Weyl’s law \(N(\lambda)\sim\lambda/(4\pi)\) for area 1 is the area of the disc of radius \(\sqrt\lambda/(2\pi)\). The sphere \(K=1/R^2\) and the unproved spherical harmonics are labelled as such. Rigor 8: the Theorema Egregium frame argument was read as a sketch of the cancellation, not recomputed from the structure equations. Prerequisites 8. Voice 9: the ant, the cylinder that unrolls, and Kac’s question are the series’ voice. Other scores 8.

**Chapter 5.** Correctness 8 and rigor 7: the free product and the rank formula \(1+k(n-1)\) for a subgroup of index \(k\) in \(F_n\) are stated correctly, including the special case “index \(k\) in \(F_2\) needs \(k+1\) generators”. The Seifert–van Kampen and Nielsen–Schreier proofs were not read line by line, so rigor stays at 7. Clarity and pedagogy 7: the subject is right for this point in the series, and it is still a sharp climb. Exercises 7. The Galois analogy is pointed at Volume 3, Chapter 10, which is the Galois chapter. Figures, voice, notation, typography 8.

**Chapter 6.** Correctness 9: the transfer sequence for \(H_k(\mathbb{RP}^n;\mathbb Z/2)\) (Theorem 6.20) does what it claims. From \(H_0=\mathbb Z/2\) the connecting maps are isomorphisms up to degree \(n-1\); the top degree cannot be 0, because \(\mathbb Z/2\) would then have to inject into 0. The non-surjective map has degree 0 by the sentence already proved at the definition of degree. The exercise solution \(H_1(\mathbb{RP}^2)=\mathbb Z/2\), \(H_2=0\), and \(H_2(\mathbb{RP}^2;\mathbb Z/2)=\mathbb Z/2\) matches that computation. Rigor 8: excision and the comparison of simplicial and singular homology were not re-read. Clarity and pedagogy 7: this is the hardest chapter for the intended reader, and the book does not pretend otherwise. Exercises 8, including a stable label for the projective plane that Volume 10 quotes correctly. Other scores 8.

**Chapter 7.** Correctness 8 and rigor 8 on the part that was read: Theorem 7.9 says every unitary matrix is conjugate to a diagonal matrix, the Weyl group is \(S_n\), and the proof uses the spectral theorem for normal matrices, which is Volume 8, Theorem 3.2, and that theorem is exactly \(A=UDU^*\). Prerequisites 9 for the citations that were checked. Clarity and pedagogy 7: the closed-subgroup theorem and the spin cover are the right material and they are dense. Exercises 7. The double-cover story is the one the preface promises. Other scores 8. The matrices of the spin cover were not multiplied out again.

**Chapter 8.** Correctness 9 and rigor 9 for Weyl’s formula (Theorem 8.8): the Jacobian contributes \(\prod_{j<k}|t_k-t_j|^2\), the \(n!\) sheets produce the factorial, and \(\int_T|V|^2\,d\theta=(2\pi)^n n!\) fixes the constant \(1/(n!(2\pi)^n)\). That is the formula in Meckes and in Bourgade’s notes. Andréief’s identity has the factor \(1/n!\) on the side the classical statement requires, and the expansion gives it. Dyson’s substitution \(x=2\pi u/n\) produces \(1-(\sin\pi u/(\pi u))^2\), and the small-\(u\) expansion is \((\pi^2/3)u^2\). The \(SU(2)\) density \((2/\pi)\sin^2\alpha\) and the mean rotation angle \(\pi/2+2/\pi\approx 126.5^\circ\) were recomputed from the solution of Exercise 8.3. Prerequisites 8: the Vandermonde determinant is Volume 1, Proposition 7.4, and that is `prop:vdm`. Volume 1 sets the chapter counter to \(-1\) before its first chapter, so linear algebra is Chapter 7, not Chapter 8. Clarity 7 because the Jacobian paragraph is a single long computation. Pedagogy 8: Montgomery and Dyson, then the formula, then a picture of 24 eigenvalues. Exercises 9: the six solutions that were recomputed (trace moments \(\min(k,n)\), the gap probability, the \(n=2\) repulsion density \(1-\cos(\theta_1-\theta_2)\), the \(SU(2)\) law) are right. Voice 9. Notation 8: the modular function is \(\delta\) and the Vandermonde product is \(V\), so the two \(\Delta\)s are gone. Figures and typography 8.

**Chapter 9.** Correctness 8: the area \(\pi/3\) of the modular triangle is the angle defect \(\pi-\pi/3-\pi/3-0\), and the cone angles \(\pi\) and \(2\pi/3\) are the standard ones. The trace classification (Theorem 9.6) has the right fixed-point trichotomy and \(2\cosh(\ell/2)=|\operatorname{tr} g|\). Volume 6, Proposition 12.1 and Theorem 12.2, are the generators and the fundamental domain, and the text uses them for what they say. Prerequisites 5: the distance, the shortest-path property and the area formula are Theorem I.8 and its neighbours, proved only in Appendix I, which is printed after this chapter, and Chapter 9 uses them as premises (printed pp. 158–159 and p. 163). The reminder box names the debt; it does not discharge it. Clarity, pedagogy and voice 8–9: the omnibus at Coutances is a real story and it earns the matrices. Exercises 7. The parenthetical on the angle at \(\rho\) swaps horizontal and vertical; the angle it then uses, \(\pi/3\), is the right one. See the issue log.

**Chapter 10.** Correctness 8: the Cayley map (Lemma 10.1) is checked by \(|z-i|<|z+i|\) and by the imaginary part of the inverse. The Cauchy bound \(|f'|\le 4j M_j\) on a disc of radius \(1/(4j)\) inside a disc of radius \(1/(2j)\) is Corollary 9.12 of Volume 5, and that corollary is Cauchy’s estimate. Rigor 7: the extremal argument after Montel was not read line by line. Prerequisites 8: the Volume 5 and Volume 8 labels that were checked (identity theorem 9.18, maximum principle 9.19, Rouché 9.38, Arzelà–Ascoli as Volume 7, Theorem 4.15, homological simple connectivity as Volume 8, Corollary 14.3 and Proposition 14.4) are the theorems the sentences name. Pedagogy 7 and exercises 6: the chapter has a single exercise. The square-map figure is the right Schwarz–Christoffel picture. Other scores 8.

**Chapter 11.** Correctness 9: Crofton’s \(\int_0^\pi|\cos(\theta-\varphi)|\,d\theta=2\) gives \(\int n\,d\ell=2L\) (Theorem 11.4). Bertrand’s invariant answer is \(1/2\), because \(|p|<1/2\) is half of \([-1,1]\). Poincaré’s \(\int_0^{2\pi}|\sin|\,d\alpha=4\) gives \(4L_1L_2\). Cauchy’s mean shadow is \(A/4\) (Theorem 11.9), which is the classical formula. The unit cube’s mean shadow is \(3/2\), and the diagonal shadow has area \(\sqrt 3\). Buffon’s \(\frac{2L}{\pi d}\) matches Volume 4, Theorem 5.12, and Bertrand’s three models are Volume 4, Theorem 5.11. Laplace’s grid probability is the standard square case of the Buffon–Laplace formula. Rigor 8: the kinematic formula of Blaschke–Santaló–Chern is quoted and marked as quoted. Prerequisites 9. Pedagogy, exercises and voice 9: the needle, the noodle and the longimeter are one idea. Other scores 8.

**Appendix A.** Correctness and rigor 8 on the part that was read. The crystallographic restriction (Theorem A.8) is the trace argument, and \(2\cos\theta\in\mathbb Z\) in the plane and in space. The five lattice types then exclude \(C_4\) and \(C_6\) by producing the reflection in the line of a shortest vector. Wallpaper groups are quoted, with Fedorov’s 17 and the 230 space groups named as quoted. The frieze casework and Fagnano’s billiard were not re-read. Other scores 8. Ceva and the Euler line are exercises here, which is where the Euclidean centre theorems now live.

**Appendix B.** Correctness 9 for Descartes’ theorem (Theorem B.10): the Gram matrix \(2I-J\) is inverted by \(\frac12 I-\frac14 J\), and the curvatures \(1,\frac12,\frac13\) give \(\frac{11}6\pm 2\), so the enclosing circle has radius 6 and the inner circle has radius \(\frac6{23}\). Rigor 8: Feuerbach’s theorem was not re-read. Other scores 8. The appendix letters in the passages that were checked point at the right appendices.

**Appendix C.** Scores 7 for correctness, rigor, pedagogy and exercises, and 8 for the rest. Desargues, Pappus, the cross-ratio and the fundamental theorem were not read line by line. No false statement was noticed in the definitions that were sampled, and the appendix letters used by later appendices (Möbius maps of Appendix B, affine maps of Appendix A) point at the right chapters. The 7s mean “not certified”, not “found wrong”.

**Appendix D.** Same pattern as Appendix C. Pascal, poles and polars, and Poncelet were not read line by line. The cross-references to Appendices B, C, E, F and G that were checked name the right appendices. Scores 7 on correctness, rigor, pedagogy and exercises; 8 on the rest.

**Appendix E.** Correctness and rigor 8 on the calculations that were redone: the form \(xy+yz+zx\) has matrix \(\frac12(J-I)\), eigenvalues \(1,-\frac12,-\frac12\), signature \((1,2)\), and the isotropic vectors \((1,1,1)\) mod 3, \((1,2,0)\) mod 5 and \((1,2,3)\) mod 7 are isotropic. Prerequisites 8: Theorems 7.9 and 7.10 of Volume 1 are the spectral theorem and the Gram determinant. A counter that starts Volume 1 at Chapter 1 prints them as 8.9 and 8.10, because that volume’s first chapter is Chapter 0. Other scores 8.

**Appendix F.** Correctness and rigor 8: Bézout is proved with multiplicity relative to an auxiliary point \(O\), and the text says that this choice is part of the definition, that independence is not proved, and that the intrinsic count is Volume 13, Chapter 14. Volume 13’s fourteenth chapter is Algebraic Curves. The singular-point lemma (multiplicity at least 2) was read and the excluded tangent case is the one admissibility removes. Other scores 8. The sentence that locates Cayley–Bacharach “in Appendix G” is only a wording slip; the label sits in this appendix.

**Appendix G.** Correctness, rigor and prerequisites 8: associativity is a numbered theorem only for nine distinct points, and the text refuses to call \((E(K),+)\) a group for every triple until Volume 13, Chapter 15. That chapter is Elliptic Curves, and it is where Volume 13 proves the group law. The count of 12 lines on the nine flexes, \(\binom92/\binom32=12\), is arithmetic and is marked as depending on the group law, which is not used later in the appendix. Hasse’s bound is pointed at Volume 13, Chapter 16, which is Curves over Finite Fields. Other scores 8.

**Appendix H.** Correctness 9 and rigor 8: the Hermite induction was recomputed. From \(\frac34|b_1|^2\le|y|^2\) and the inductive bound one gets \(|b_1|^2\le(\frac43)^{(n-1)/2}(\det\Lambda)^{2/n}\), which is the claim. The projection step is written out; it does not cite Cassels for a missing lemma. The \(E_8\) centre density \(\pi^4/384\approx 0.2537\) is right, and \(\Delta\le\pi/\sqrt{12}\) for the hexagonal lattice is right. The ratio of densities for \(D_n\cup(D_n+h)\) is \(2\cdot(\min(2,n/4)/2)^{n/2}\), which is 2 for \(n=8\) and for \(n>8\), and less than 1 for \(n=4\) and \(n=6\). Volume 3, Lemma 7.5 and Theorem 7.6, are the freeness facts the solution uses. Other scores 8.

**Appendix I.** Correctness and rigor 8 for the area theorem (Theorem I.8): the ideal triangle integrates to \((\pi-\alpha)-\beta\), and a finite triangle is the difference of two ideal ones. That is the formula Chapter 9 quotes. The rest of the appendix (spherical excess, the disc model beyond the formula Chapter 9 copies) was sampled, not certified line by line. Exercises 7 for that reason. Other scores 8.

**Appendix J.** Correctness 8: Radon’s lemma, as printed, is the linear dependence of \((x_i,1)\) in \(\mathbb R^{n+1}\). Brunn–Minkowski and the isoperimetric argument were not re-read, so rigor and exercises are 7. The opening points at Volume 5, Theorem 6.17, for Hurwitz’s proof, and that theorem is the isoperimetric theorem in the Fourier chapter. Chapter 11 is correctly named as the chapter that extends Buffon and Cauchy. Other scores 8.

**Appendix K.** Correctness 8: the appendix says, in its first paragraph, that it is not a second proof of Chapter 4. The spherical median for side \(0.5\) was recomputed: \(\arccos(\cos 0.5/\cos 0.25)\approx 0.43767\), against \((\sqrt 3/2)\cdot 0.5\approx 0.43301\), which is what the solution prints. The four-vertex proof and Descartes’ polyhedral defect were not re-read, so rigor and exercises are 7. Other scores 8.

### Whole book

| Item | Score |
| --- | ---: |
| Structure and arc | 8 |
| Continuity with Volumes 1–8 | 8 |
| Preparation for later volumes | 8 |
| Delivery of the title and subtitle | 9 |
| Front and back matter, index and bibliography | 6 |
| Print PDF | 8 |
| EPUB | 8 |
| **Overall** | **8** |

**Structure and arc, 8.** Eleven chapters in three parts, then eleven appendices A–K. The arc the preface announces is the arc of the book: manifolds and flows, forms and curvature, the fundamental group and homology, then Lie groups, Weyl’s law, the modular surface, the Riemann map, and Crofton. The appendices are a second, pictorial track, and each one that was opened says what it connects. The Euclidean centre theorems are exercises in Appendix A rather than a separate gallery. Integral geometry is Chapter 11 because the Riemann mapping theorem is Chapter 10; the file is still named `ch10-integral.tex`, and the cross-references that were checked say Chapter 11. The book is 377 print pages, a little past the blueprint’s 340–370.

**Continuity, 8.** The numbered citations that were matched, with Volume 1’s `\setcounter{chapter}{-1}` taken into account, land on the theorem the sentence describes. Volume 1, Proposition 7.4 is the Vandermonde determinant, and Theorems 7.9 and 7.10 are the spectral theorem and the Gram determinant; a counter that ignores the setcounter prints those as 8.4, 8.9 and 8.10. Also checked: Volume 4, Theorems 5.11 and 5.12 (Bertrand and Buffon); Volume 5, Corollary 6.14, Corollary 9.12, Theorems 9.15, 9.18, 9.19 and 9.38; Volume 6, Proposition 12.1 and Theorem 12.2; Volume 7, Theorems 2.12, 4.9, 4.15, 4.19, 6.7, 6.10, 7.5, 9.6, 9.7 and 9.8, Proposition 7.12, Definition 6.5, Lemma 6.4, and Exercise 4.7 (Lebesgue’s space-filling curve); Volume 8, Proposition 13.2, Theorem 13.3, Corollary 14.3, Proposition 14.4 and Theorem 3.2; Volume 2, Theorem 8.1; Volume 3, Lemma 7.5 and Theorem 7.6. The score is not 9 because Chapter 9 takes the distance and the area formula from Appendix I, which a reader in order has not reached.

**Preparation for later volumes, 8.** Volumes 10 and 12 cite this book by theorem number, and the numbers resolve.

- Volume 12, `ch10-cue.tex`: Haar uniqueness is Theorem 8.3, Heine is Theorem 8.13, correlations are Theorem 8.15, Dyson is Corollary 8.16. Each of those labels is that statement, including the factor \(1/n!\) and the kernel \(K_n\).
- Volume 12, `ch05-analysis.tex`: the Riemann mapping theorem is Theorem 10.5, and that is `thm:riemannmap`.
- Volume 10, `ch11-compact.tex`: Theorem 7.9 is the maximal-torus theorem, Theorem 8.8 is Weyl, Theorem 8.3 is uniqueness, and Exercise 8.3 is the density \((2/\pi)\sin^2\alpha\).
- Volume 10, `ch06-homological.tex`: Lemma 6.2 is the zigzag lemma, and Exercise 6.1 is the projective-plane computation the universal-coefficient chapter quotes. The same chapter correctly says that Volume 9 states de Rham’s theorem for a compact manifold and does not prove it.
- Volume 10, `ch01-categories.tex`: Chapters 5 and 6 are the fundamental group and homology, and the free product is defined in Chapter 5.

Volume 15, `ra-polynomials.tex`, attributes the \(SU(2)\) density to Theorem 8.8. The density is Exercise 8.3, and the solution derives it from Haar measure on \(S^3\), not from the Weyl integral. The fact is in the book; the pointer is one label off. Volumes 11, 13 and 14 do not cite Volume 9. Volume 9’s forward pointers the other way are accurate: Volume 13, Chapters 14, 15 and 16 are Algebraic Curves, Elliptic Curves, and Curves over Finite Fields. Volume 11’s Gauss map is the ergodic form of the continued-fraction picture, and Volume 9 says so, but Volume 11 does not point back.

**Title and subtitle, 9.** *Shapes* is what the book is about. *The Geometry of Connection* is earned by charts that glue, Stokes as one theorem, the fundamental group and homology, the double cover, Weyl’s law as the joint into random matrices, geodesics that write continued fractions, and one measure on the set of lines. The appendices that stay are the ones that join a figure to a group, a circle to a matrix, or a curve to a count.

**Front and back matter, 6.** The preface lists the real prerequisites and the real deferred group law. About the Cover names the \(\{7,3\}\) tiling, Poincaré’s disc of 1882 and Klein’s quartic of 1878, and it says why the picture is on this volume. Every chapter ends with a sources section, and the citations that were opened (Riemann 1868, Whitney 1936, Hatcher, Conway–Sloane, the Kepler papers) are real. There is no index and no single bibliography. The back-cover blurb says “Every theorem is proved in full”. That sentence is false: de Rham’s theorem in general, the classification of surfaces, Hopf’s ergodicity of the geodesic flow, Hadwiger’s theorem, Adams’ theorem, the intrinsic form of Bézout, and associativity of the chord law for every triple are all explicitly not proved here. The copyright page prints “ISBN (paperback): to be assigned” (printed p. iv).

**Print PDF, 8.** The reading PDF is 7 × 10 in on every page. The print PDF is 7.125 × 10.25 in on every page, PDF 1.3, with empty document metadata. The three part openers (print pages 13, 59 and 135) are charcoal at the corners of the media box, so the full-page solid reaches the bleed. The sampled reading pages (part title, Chapter 3 opener, modular-group page, last exercise page, About the Cover) are the design-5e page: coral chapter label, charcoal text, no obvious collision. Not every page was inspected for an overfull line.

**EPUB, 8.** The package is 26 MB, under the 50 MB cap. It contains 55 plate PNGs, all at least 1600 pixels wide, each with `width:100%` in the `img`, and no plate SVG. Inline mathematics is a transparent PNG with width and `vertical-align` in em. Part openers, theorem boxes and the coral rule are in the stylesheet. It was not opened on a Kindle Paperwhite.

### Overall

**8.** The main theorems that carry the book, among those read line by line, are correct, and the places where a proof stops are labelled. The prose sounds like a person explaining a shape, with a date, a picture or a small number in the sentence. I would not send the jacket to press while it says every theorem is proved in full, and I would not leave Chapter 9 depending on a proof that appears only in Appendix I. I would recommend the mathematical text, after those two corrections, to a reader who has finished Volume 8.

The lowest chapter scores are Chapter 9 on prerequisites (5) and Chapter 10 on exercises (6). The lowest whole-book score is front and back matter (6). The lowest dimensions are that prerequisite gap, the thin exercise set in the Riemann mapping chapter, and rigor on the long proofs that were sampled rather than read line by line.

## Issue log

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V9-01 | `blurb.tex:11` | front matter | major | “Every theorem is proved in full” is the back-cover sentence. The book explicitly does not prove general de Rham, the classification of surfaces, Hopf’s ergodicity theorem, Hadwiger’s theorem, Adams’ theorem beyond the statement, intrinsic Bézout, or associativity of the chord-and-tangent law for every triple. | Replace the sentence with what is true: the numbered theorems are proved, and the named theorems that are only quoted are marked as quoted. |
| V9-02 | `ch09-hyperbolic.tex:17–31` and `:157`, reminder on printed pp. 158–159, area on printed p. 163 | prerequisite | major | Distance, unique shortest paths and the area formula are Theorem I.8 and the theorems beside it in Appendix I. Appendix I is printed after Chapter 9. The reminder box uses them as premises, and the area of the fundamental domain is deduced from Theorem I.8. | Prove the distance formula and the angle defect in Chapter 9, or move Appendix I before Chapter 9. A forward pointer is not enough while the formulas are premises. |
| V9-03 | `ch09-hyperbolic.tex:156–157`, printed p. 163 | correctness | minor | The radius to \(\rho=e^{2\pi i/3}\) makes the angle \(\pi/6\) with the vertical, and the tangent makes \(\pi/6\) with the horizontal. The text says the opposite. The interior angle it then uses is \(\pi/3\), which is the angle between that tangent and the vertical side, and the area \(\pi/3\) is right. | Swap “horizontal” and “vertical” in the parenthesis. |
| V9-04 | `volume15-order-and-chance/chapters/ra-polynomials.tex:55` | downstream citation | minor | The Sato–Tate density \((2/\pi)\sin^2\theta\) is attributed to Volume 9, Theorem 8.8. Theorem 8.8 is Weyl’s formula for \(U(n)\). The density is Exercise 8.3, derived from Haar measure on \(S^3\). | Cite Exercise 8.3, or one sentence that specialises Theorem 8.8 to \(SU(2)\). This is a Volume 15 pointer, not a false theorem in Volume 9. |
| V9-05 | `geometry-ch07-curves.tex:294` | notation | minor | “In Appendix G, Theorem `geometry:thm:cayleybacharach`” reads as if the theorem lived in Appendix G. The theorem is in Appendix F; Appendix G applies it. | Say “Theorem F.4, applied in Appendix G”. |
| V9-06 | `main.tex` has no index; the reading PDF has none | front matter | minor | A 377-page book with this many named theorems has chapter-end sources and no index. “Index” in the PDF is the Poincaré index, not a book index. | Add an index of theorems, or say in the preface that the sources sections are the bibliography and that there is no index. |
| V9-07 | `riemann-mapping.tex` | exercises | minor | The chapter has one exercise. The rest of the book gives every chapter a graded set. | Add two or three exercises: the Cayley map, a Schwarz-lemma consequence, and one simply-connected domain that is not a disc. |

No critical error was found in a proof that was read line by line. That is not a claim about the proofs listed under “Not reviewed”. Counts: 2 major, 5 minor, 0 critical.

## Verified correct

These were read line by line, or recomputed, as indicated.

**Analysis and topology.**

- Theorem 1.7, the inverse function theorem: reduction to \(Df(0)=I\), contraction constant \(1/2\) on \(\overline B(0,2r)\), surjectivity onto \(B(0,r)\) by Banach (Volume 7, Theorem 2.12), derivative of the inverse, and the \(C^k\) bootstrap.
- Theorem 2.16, the hairy ball theorem: the shell map \(f_t(x)=x+tv(x)\), the two volume computations, and the odd multiplicity of the root \(i\) when \(N\) is odd. The Adams count matches the classical formula.
- The contact distribution on \(\mathbb R^3\): \([Y_1,Y_2]=\partial_z\).
- Theorem 4.11 and Corollary 4.13: Gauss–Bonnet for a compact oriented surface, including the orientation of the small circles and the definition of \(\chi\) after Morse functions are shown to exist.
- Theorem 4.19: eigenvalues \(4\pi^2|k|^2\) of \(-\Delta\) on the square flat torus, orthonormal basis \(e^{2\pi i\langle k,x\rangle}\), and \(N(\lambda)\sim\lambda/(4\pi)\).
- Theorem 6.20: the transfer proof that \(H_k(\mathbb{RP}^n;\mathbb Z/2)=\mathbb Z/2\) for \(0\le k\le n\), and the deduction of Borsuk–Ulam. The degree of a non-surjective self-map of \(S^n\) is already zero at the definition of degree.
- The solution of Exercise 6.1 for \(\mathbb{RP}^2\) with coefficients \(\mathbb Z\) and \(\mathbb Z/2\).
- Theorem 7.9: every matrix of \(U(n)\) is conjugate to a diagonal matrix; the citation of Volume 8, Theorem 3.2, matches the spectral theorem for normal matrices.
- Theorem 8.1 through Corollary 8.16, including the constant in Theorem 8.8. The total mass of \(\frac1{n!}|V|^2\) against normalised Lebesgue measure on the torus is 1. Andréief’s \(1/n!\) is the classical factor (Meckes; Bourgade, *Conditional Haar measures*). Dyson’s limit and the expansion \((\pi^2/3)u^2\) were recomputed.
- Exercise 8.3 and its solution: if \(\operatorname{Re}a\) has density \((2/\pi)\sqrt{1-x^2}\) and \(x=\cos\alpha\), then \(\alpha\) has density \((2/\pi)\sin^2\alpha\). The rotation angle has density \((1-\cos\phi)/\pi\) and mean \(\pi/2+2/\pi\approx 126.48^\circ\).
- The solutions of the trace-moment, gap and \(n=2\) repulsion exercises in Chapter 8: \(\mathbb E|\operatorname{tr} U^k|^2=\min(k,n)\); the \(n=2\) gap probability \((1-\alpha/\pi)^2-\sin^2\alpha/\pi^2\); the density \(1-\cos(\theta_1-\theta_2)\).

**Geometry and integral geometry.**

- Lemma 10.1, the Cayley map, both directions.
- The Cauchy-estimate constant in the proof of Montel: radius \(1/(4j)\) gives the factor \(4j\).
- Theorem 11.1 through Theorem 11.9: uniqueness is used as printed; Crofton’s angular integral equals 2; Bertrand’s invariant probability is \(1/2\); Poincaré’s integral equals \(4ab\); Cauchy’s mean shadow is \(A/4\). The unit cube’s diagonal shadow has area \(\sqrt 3\). Laplace’s grid formula matches the classical square case \((4ld-l^2)/(\pi d^2)\).
- Theorem A.8 and the five lattice types: trace \(2\cos\theta\) or \(1+2\cos\theta\), and the exclusion of \(C_4\) and \(C_6\).
- Theorem B.10 and the coin radii \(6\) and \(6/23\). The inverse of \(2I-J\) was multiplied out.
- Theorem F.4’s definition of multiplicity relative to \(O\), and the singular-point lemma that follows it. The deferral to Volume 13, Chapter 14, matches that volume’s chapter order.
- Theorem G.4 and the surrounding refusal to treat \((E(K),+)\) as a group for every triple. The flex count \(\binom92/\binom32=12\) is arithmetic. Volume 13, Chapters 15 and 16, are the chapters the deferrals name.
- The Hermite solution in Appendix H, the \(E_8\) density \(\pi^4/384\approx 0.2537\), the hexagonal bound \(\pi/\sqrt{12}\), and the density ratio for the deep hole of \(D_n\).
- Theorem I.8 for an ideal triangle, by the integral \(\int dx/\sqrt{1-x^2}\), and the subtraction that gives a finite triangle.
- Radon’s lemma in Appendix J, including the sign split of the coefficients.
- The spherical-median number in the last solution of Appendix K.

**Citations that resolve.** The Volume 4, 5, 6, 7 and 8 numbers listed under “Continuity” were matched to the statement counter and, for the ones named there, to the statement. Volume 10 and Volume 12’s numbered citations of this book resolve, as listed under “Preparation”. Every exercise label in the volume has a hint and a solution (198 exercises). That checks existence, not the correctness of every solution.

**Rendering.** Reading PDF page size \(504\times 720\) pt. Print PDF page size \(513\times 738\) pt. Part openers are charcoal at the media-box corners. EPUB plates and inline mathematics satisfy the width and baseline rules that were checked in the package.

## Not reviewed

Line-by-line reading did not cover:

- the Picard–Lindelöf theorem and smooth dependence of the flow (Chapter 2), beyond the statement and the hairy-ball argument that uses the flow;
- the half-space computation of Stokes’ theorem (Chapter 3), beyond the book’s description of the orientation and the de Rham caveat;
- the structure equations in the proof of the Theorema Egregium (Chapter 4);
- the proofs of Seifert–van Kampen and Nielsen–Schreier (Chapter 5);
- excision, the small-chains theorem, and the inductive comparison of simplicial and singular homology (Chapter 6);
- the closed-subgroup theorem and the matrix of the spin cover (Chapter 7);
- the extremal construction in the Riemann mapping theorem after Montel, the Schwarz lemma and the Cayley map (Chapter 10);
- the case-by-case frieze classification, Fagnano’s theorem, Feuerbach’s theorem, Desargues, Pappus, the fundamental theorem of projective geometry, Pascal’s theorem, Poncelet’s porism, the full proof of Sylvester’s law, Witt cancellation, the four-vertex theorem, Brunn–Minkowski, and most exercise solutions in Appendices C, D, I, J and K;
- TikZ coordinates against the captions, except where a caption states a number that was recomputed (Crofton average, modular area, pair correlation, spherical median);
- a page-by-page search for overfull lines;
- the EPUB on a Kindle Paperwhite.

Volumes 11, 13 and 14 were searched for citations of Volume 9 and have none. Their proofs were not reviewed. The master-plan file on the open plan pull request was not re-read beyond the volume blueprint `docs/plan/book-09.md`, and that file was used only for structure and scope.

## Conformance to the volume blueprint

Read against `docs/plan/book-09.md` for structure and scope only.

The book keeps the three part names. It has the ten geometric subjects the blueprint lists, and it numbers the Riemann mapping theorem as Chapter 10, so integral geometry is Chapter 11. The blueprint’s “ten main chapters” counted the Riemann map beside them; the series structure note already lists it with the hyperbolic plane and integral geometry. Internal chapter numbers agree with that numbering.

Appendix A of the old Euclidean gallery is not in `main.tex`. Ceva and the Euler line are exercises in Transformations. The curvature appendix is titled “Curvature of Curves and Polyhedra” and its first paragraph separates it from Chapter 4. de Rham’s general theorem is marked unproved. The Borsuk–Ulam transfer computes the mod-2 homology of projective space. The modular function is \(\delta\) and the Vandermonde product is \(V\). The cubic group law is deferred to Volume 13, Chapter 15, for every triple. The Hermite solution contains the projection argument. Bézout’s multiplicity is defined relative to a point and says so.

The blueprint’s page target was 340–370. The print PDF has 377 pages.

## Sources consulted

- The Volume 9 source, the reading PDF, the print PDF and the EPUB in the release `books`.
- Statement counters and the cited theorems in Volumes 1, 2, 3, 4, 5, 6, 7, 8 and 13, and the Volume 9 citations in Volumes 10–15.
- E. Meckes, *Random Matrices from the Classical Compact Groups*, notes, Part V: the Weyl density \(1/(n!(2\pi)^n)\prod_{j<k}|e^{i\theta_j}-e^{i\theta_k}|^2\).
- P. Bourgade, *Conditional Haar measures on classical compact groups*, Ann. Probab. (2009), display (1.1), the same formula.
- F. Adams’ count, as stated in the Wikipedia article “Vector fields on spheres” and in the MathOverflow formulation \(k(n)=2^b+8a-1\) for \(n=2^{4a+b}(2s+1)\): the number of independent fields on \(S^{n-1}\).
- Cauchy’s surface-area formula: MathWorld, “Cauchy’s Surface Area Formula”, and S. Zachary, arXiv:1109.0595, the three-dimensional case “one fourth of the surface area”.
- `docs/plan/book-09.md`, for structure and scope.

## Comparison with the existing reviews

Written after the scorecard above was committed. The documents read for this section are `docs/review/SERIES-REVIEW-2026-10.md` (the October section “Volume 8 — Shapes”, the old number for this book), `docs/handoffs/volume9-rewrite.md`, and the Volume 3 second-reading note that records how Volume 9 cites Volume 1. The check scripts under `review/volume9-rewrite/` were used only to confirm that `statements.py` honours `\setcounter{chapter}{-1}`. Pull-request discussion was not opened.

**What those reviews found, and what is actually fixed.**

The October review’s five publication blockers are fixed in the book now on `main`, and the fixes survive a fresh reading.

- Andréief’s proof ends by dividing by \(n!\). Lemma 8.12 states the identity with that factor, and the expansion produces it. The October review stopped at “the \(n!\) choices of \(\pi\) give \(n!\det M\)” and reported that the last sentence never divides. That sentence now divides.
- The Borsuk–Ulam paragraph deduces \(H_k(\mathbb{RP}^n;\mathbb Z/2)=\mathbb Z/2\) from the exact sequence that is printed. The October sentence, which said the middle term would be both a kernel and an image of zero, is gone.
- The modular function is \(\delta\) and the Vandermonde product is \(V\). The two \(\Delta\)s in Chapter 8 are gone.
- Appendix G no longer says that \((E(K),+)\) may be used as a group from that point on. Associativity is numbered only for nine distinct points, and the flex identification with \(E[3]\) is marked as Volume 13, Chapter 15.
- The Hermite solution writes the projection and the determinant relation. It does not cite Cassels for those two facts.
- de Rham’s theorem for a general compact manifold is stated as not proved. Bézout’s multiplicity is defined relative to a chosen point. The curvature appendix has a different title from Chapter 4 and says it is not a second proof of Gauss–Bonnet.

The Volume 3 second reading says Volume 9’s spectral theorem and squared volume are Volume 1, Theorems 7.9 and 7.10. That is right. Volume 1’s first chapter is Chapter 0. A counter that starts at Chapter 1 prints the spectral theorem as 8.9 and the Gram theorem as 8.10, and then reports the citations as broken. The handoff already names that trap: “`statements.py` printed Volume 1 one chapter too high (it ignored `\setcounter{chapter}{-1}`)”. The first commit of this file repeated the trap and listed three major citation errors. Those three are withdrawn. Proposition 7.4 is the Vandermonde determinant, Theorem 7.9 is the spectral theorem, and Theorem 7.10 is the Gram determinant.

The handoff’s open debt, “Volume 10 still attributes the Vandermonde determinant to Volume 3”, is paid. `volume10-abstraction/chapters/ch11-compact.tex:109` cites Volume 1, Proposition 7.4.

**What they missed.**

- The back cover still says every theorem is proved in full (`blurb.tex:11`). The handoff marks the blurb “Done” and does not quote that sentence. The October review’s readiness note was about unproved theorems inside the book, not about the jacket repeating the opposite.
- Chapter 9 still uses Appendix I as a premise. The handoff replaced stale hand-typed numbers (“Proposition J.4”, “Theorem J.8”) with `\ref`s, which is the right repair of the numbers, and its own rule R1 says a later chapter is not available as a premise. The distance formula and Theorem I.8 are still premises of Chapter 9, on printed pages 158–159 and 163. The `\ref` makes the pointer accurate. It does not move the proof.
- At \(\rho\), the radius and the tangent have horizontal and vertical swapped (`ch09-hyperbolic.tex:156–157`). The angle \(\pi/3\) and the area \(\pi/3\) are right, so the slip does not reach the theorem. None of the reviews mention it.
- The Riemann mapping chapter has one exercise. The handoff’s check for that chapter recomputes the Cayley map, the strip, the slit plane and the square map. It does not note that the exercise list stops at one item.
- There is no index. The October review of this book did not ask for one. A 377-page volume whose later books cite it by theorem number is hard to search without one.
- Volume 15’s Sato–Tate sentence cites Theorem 8.8 for the density \((2/\pi)\sin^2\theta\). The handoff says that citation “still resolves”, which is true of the theorem number: Theorem 8.8 is Weyl’s formula. The density printed in Volume 15 is the conclusion of Exercise 8.3, and that solution does not use Theorem 8.8. The number exists. The sentence points at the wrong statement.

**What they claim is fixed, that is not.**

Nothing in the October list or the handoff’s chapter log was found still broken among the items checked above, except R1 as applied to Chapter 9 and Appendix I. The handoff records Chapter 9 as done after the `\ref` repair. The dependence on a later appendix is still in the book. That is the one item marked finished whose mathematical order is not finished. The three Volume 1 numbers the handoff defends are finished; the mistake was on this read’s first pass, not in the book.
- `docs/SERIES-STRUCTURE.md` and `common/series-catalog.json`, for the title, the subtitle and the part names.
