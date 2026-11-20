# Volume 9 — Shapes

**Score: 9/10.**

The inverse-function theorem, equal-dimensional Sard, Stokes, Gauss–Bonnet, the spin double cover, Weyl’s integration formula, Dyson’s pair correlation, the hyperbolic distance and cutting sequence, the Riemann mapping theorem, and Crofton’s formula are proved. The constants that were recomputed match the page. The score is 9 because the two slips are local: a stray bar in one gradient display, and a non-strict estimate in the polynomial approximation used for Brouwer’s theorem. No numbered statement was found false.

**Counts.** 0 critical, 0 major, 2 minor. Two issues, `V9-001` and `V9-002`. None is a prerequisite issue.

**How this was read.** Book order in `volume9-shapes/main.tex`: preface, Manifolds and Surfaces (Chapters 1–2), Forms and Homology (3–6), Groups and Geometry (7–11), then Appendices A–K, the index, and About the Cover. The blurb and `kdp.md` were read with the preface. Every chapter file was read, including every exercise, hint, and solution. There are 288 exercises. The shared theorem counter was counted in source order. Exercises use a separate counter and restart each chapter. After `\appendix` the chapter letters are A–K. Integral geometry is Chapter 11; the file is `ch10-integral.tex`.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. Quoted results are marked, including the full cubic group law, Adams’s vector-field count, the general de Rham theorem, Viazovska’s optimality theorem, and Montgomery’s restricted pair correlation. “We will” occurs as a concrete promise inside an argument, not as a section opener.

## Issues

Paths are relative to `volume9-shapes/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V9-001 | `chapters/ch01-manifolds.tex:200` (`ex:cassini`) | math | minor | The display begins `\|\nabla f=(4x(x^2+y^2-1),\ 4y(x^2+y^2+1)).` | The components are the gradient. Delete the bar. The critical points \((0,0),(\pm1,0)\) and the values \(0,-1,-1\) are right. |
| V9-002 | `chapters/ch03-forms.tex:244` (`thm:brouwern`) | math | minor | “Let \(g=P/(1+m/4)\). Then \(\lvert g\rvert<1\) … and \(\lvert g-f\rvert\le\lvert P-f\rvert+\frac{m/4}{1+m/4}\lvert P\rvert<m/2\).” | If the error is exactly \(m/4\) and points outward from a boundary value, the written bound reaches \(m/2\) and \(\lvert g\rvert\) can reach \(1\). Approximate strictly inside \(m/4\), or use \(\lvert g-f\rvert\le(m/2)/(1+m/4)\). The fixed-point contradiction then holds. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map matches the eleven chapters and the eleven appendices. It assumes Volume 7’s topology and integration, Volume 5’s complex analysis, Volume 8’s homological Cauchy theorem, Volume 3’s groups and quaternions, Volume 6’s modular domain, and Volume 2’s continued fractions. The cubic group law is deferred to Volume 13. The blurb and `kdp.md` name the same path, including the distinction between Dyson’s law and Montgomery’s theorem. About the Cover is the regular heptagon tiling of the Poincaré disc, three at a vertex, and the quotient is Klein’s quartic, a surface of genus 3. Chapter 9 and Exercise `ex:klein336` give the triangle of area \(\pi/42\) and the count 336.

### Chapter 1

Charts, the inverse and implicit function theorems, the four descriptions of a submanifold, tangent spaces, the regular-value theorem, equal-dimensional Sard, and the compact Whitney embedding. The Cassini gradient components are \(4x(x^2+y^2-1)\) and \(4y(x^2+y^2+1)\), and the stray bar is V9-001. The arm map is critical exactly when \(\sin\theta_2=0\), on the circles of radii \(\ell_1\pm\ell_2\). The rank-\(r\) chart has dimension \(r(m+n-r)\). Volume 7, Exercise 4.7, is Lebesgue’s space-filling curve. Volume 7, Theorems 2.12, 4.9 and 9.8, and Proposition 7.12, are the fixed-point theorem, Heine’s uniform continuity, the change of variables, and regularity.

### Chapter 2

Grönwall, Picard–Lindelöf, smooth dependence, the Lie bracket, Frobenius, and Milnor’s hairy-ball argument. For \(x'=x^2\) the flow is \(x_0/(1-tx_0)\) on \(tx_0<1\). The loop of \(\partial_x\) and \(x\partial_y\) displaces by exactly \(s^2\) in the vertical direction. The shell volume \((1+t^2)^{N/2}\) with \(N\) odd cannot be a polynomial square. Adams’s count \(\rho(n)-1\) is quoted with the standard formula. Volume 5, Corollary 6.14, is the irrational rotation. Volume 7, Theorem 4.19, is Stone–Weierstrass.

### Chapter 3

The exterior derivative, Stokes, the sphere form with \(\int_{S^{n-1}}\sigma=n\lambda(B^n)\), Brouwer in every dimension, the Poincaré lemma, and \(H^1(\R^2\setminus\{0\})=\R[\mathrm d\theta]\). The unit-ball volumes through dimension 5 are \(2,\pi,4\pi/3,\pi^2/2,8\pi^2/15\), and \(8\pi^2/15>\pi^3/6\) because \(\pi<16/5\). The partial sum of the Leibniz series through order 18 is about \(0.7985\), under \(4/5\). The fraction of the unit ball in the cube of side 2, at dimension 10, is about \(0.00249\). The written estimate in Brouwer’s approximation is V9-002. Volume 7, Theorems 6.7, 9.8 and 4.19, and Lemma 6.4 with Definition 6.5, are the disc theorem, the change of variables, Stone–Weierstrass, and the winding number.

### Chapter 4

The moving-frame connection, the Theorema Egregium in the form \(K=\det(\mathrm dN)\), Gauss–Bonnet, Morse indices, and the flat-torus spectrum \(4\pi^2(k_1^2+k_2^2)\). The sphere has \(K=1\) and integral \(4\pi\). The torus of revolution has integral zero. A conformal metric \(e^{2u}(dx^2+dy^2)\) has \(K=-e^{-2u}\Delta u\). The stereographic length \(4\pi r/(1+r^2)\) is largest at \(r=1\), with value \(2\pi\). The Brocken excess for area \(2900\,\mathrm{km}^2\) on a sphere of radius \(6371\,\mathrm{km}\) is about \(14.74\) arcseconds. Volume 7, Proposition 6.6, is the winding comparison, and Theorem 4.19 is Stone–Weierstrass.

### Chapter 5

The fundamental group, the circle, the classification of coverings, van Kampen, Nielsen–Schreier, and the surface presentation of genus \(g\). A subgroup of index \(k\) in \(F_n\) is free of rank \(1+k(n-1)\). The three index-two subgroups of \(F_2\) are the kernels of the three nonzero maps to \(\Z/2\), each free of rank 3. The commutator subgroup is the integer grid. The word \([[a,b],c]\) has ten letters and dies when any one letter is erased. Volume 7, Theorem 4.8, states the Lebesgue number in the compactness theorem. Volume 7, Theorem 1.19, is Zorn’s lemma.

### Chapter 6

Singular homology, Mayer–Vietoris, the homology of spheres, invariance of domain, Borsuk–Ulam, and the ham sandwich theorem. The antipodal map of \(S^n\) has degree \((-1)^{n+1}\). A nowhere-zero tangent field exists only for odd \(n\), among the spheres treated here. The boundary matrix with columns \((4,6,0)\) and \((6,12,0)\) has invariant factors \(2,6\), so \(H_1=\Z\oplus\Z/2\oplus\Z/6\). The Klein bottle has \(H_1=\Z\oplus\Z/2\) and \(H_2=0\). A football has twelve pentagons. Volume 3, Theorem 7.4, is the Smith form.

### Chapter 7

Closed subgroups, continuous homomorphisms, the spin cover \(SU(2)\to SO(3)\), and the maximal torus of \(U(n)\). For \(\lvert u\rvert=1\), \(e^{\theta X(u)}=\cos(\theta/2)I+2\sin(\theta/2)X(u)\), and a full turn lifts from \(I\) to \(-I\). Rodrigues’s formula has trace \(1+2\cos\theta\). The trace identity is \(\operatorname{tr}\pi(g)=(\operatorname{tr} g)^2-1\). The matrix \(\operatorname{diag}(-2,-1/2)\) is \(e^{\pi(E-F)}e^{(\log 2)H}\) and is not a single exponential. Volume 3, Lemma 12.3, is Euler’s rotation lemma. Volume 8, Theorem 3.2, is the spectral theorem for normal matrices, Theorem 4.3 is the polar decomposition, and Proposition C.13 is the matrix exponential.

### Chapter 8

Haar measure on a matrix group, the Gaussian QR sampler, Weyl’s formula, Heine’s identity, and Dyson’s limit \(1-(\sin(\pi u)/(\pi u))^2\). The pair intensity is \(n^2-\lvert K_n\rvert^2\). For \(U(2)\), the probability that the circular separation is less than \(\varepsilon\in(0,\pi)\) is \((\varepsilon-\sin\varepsilon)/\pi\), against \(\varepsilon/\pi\) for independent points; at \(\varepsilon=0.1\) the ratio is about \(600\). The second moment of \(\lvert\operatorname{tr} U^k\rvert\) is \(\min(k,n)\). A Haar element of \(SU(2)\) has angle density \(2\sin^2\alpha/\pi\) on \([0,\pi]\), and the spatial angle has density \((1-\cos\phi)/\pi\) and mean \(\pi/2+2/\pi\). The arc-count variance for \(U(2)\) is \(2p-2p^2-2(\sin(\pi p)/\pi)^2\). \(\mathbb E\det(I-zU)=1\), and \(\mathbb E\lvert e_j\rvert^2=1\). Volume 1, Proposition 7.4, is the Vandermonde determinant. Volume 8, Theorem 13.3, is uniqueness of Haar measure, and Exercise 13.1 is the affine group with densities \(a^{-2}\,\mathrm da\,\mathrm db\) and \(a^{-1}\,\mathrm da\,\mathrm db\).

### Chapter 9

The distance formula, ideal triangles of area \(\pi-\alpha-\beta-\gamma\), the disc model, the Iwasawa decomposition, and Series’s cutting sequence. The matrix \(\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)\) has trace 3 and translation length \(4\log\varphi\). The axis from \(1-\sqrt2\) to \(1+\sqrt2\) belongs to \(\bigl(\begin{smallmatrix}5&2\\2&1\end{smallmatrix}\bigr)\), of length \(4\log(1+\sqrt2)\), and the cutting sequence is \(LLRR\) repeated. The reduced forms of discriminants \(-20\) and \(-23\) give two and three classes. The modular fundamental domain has area \(\pi/3\), and the unit tangent quotient has volume \(2\pi^2/3\). Volume 6, Proposition 12.1 and Theorem 12.2, are the generators and the fundamental domain. Volume 2, Theorem 9.8, is Pell’s equation.

### Chapter 10

Montel’s theorem, Schwarz’s lemma, and the Riemann mapping theorem under the square-root hypothesis. Volume 8, Corollary 14.3, is the existence of holomorphic roots on a connected homologically simply connected domain. Volume 8, Proposition 14.4, puts the interior of a Jordan curve in that class. Volume 5, Corollary 9.12, is Cauchy’s estimate; Theorems 9.15, 9.18, 9.19 and 9.38 are Weierstrass’s convergence theorem, the identity theorem, the maximum principle, and Rouché. Volume 7, Theorem 6.10, is the Jordan curve theorem. The punctured disc has no holomorphic square root, because the winding would be \(1/2\).

### Chapter 11

The invariant line measure \(dp\,\mathrm d\theta\), Bertrand’s answer \(1/2\), Crofton’s formula \(\int n\,\mathrm d\ell=2L\), and Cauchy’s surface formula. Lines meeting the unit disc have measure \(2\pi\). The conditional mean number of crossings of a curve of length \(L\) inside a disc of radius \(R\) is \(2L/(2\pi R)\). Two curves of lengths \(2\pi r\) and \(2\pi s\) have kinematic measure \(16\pi^2 rs\). A latitude of colatitude \(a\) meets a random great circle with probability \(\sin a\), and the mean number of intersections is \(2\sin a\). Volume 4, Theorems 5.11 and 5.12, are Bertrand’s three models and Buffon’s needle. Volume 7, Theorem 7.5, is uniqueness for measures finite on an exhausting sequence from a \(\pi\)-system; the text uses it for locally finite measures on the line.

### Appendix A

Isometries are affine, three reflections suffice, the seven friezes, the crystallographic restriction, and Fagnano. A finite subgroup of \(SO(3)\) has order \(n\), \(2n\), \(12\), \(24\) or \(60\). The rotation group of the cube has order 24. Ceva’s product is one, including the parallel case. Routh’s triangle for the ratio \(1/2\) has area \(1/7\).

### Appendix B

Inversion, Ptolemy, Steiner’s porism, Descartes’s theorem, and Feuerbach. Curvatures \(1/2,1/3,1/10\) give the fourth curvatures \(29/15\) and \(-1/15\). The Apollonian root \((-1,2,2,3)\) stays nonzero modulo 4. Stereographic projection from the north pole is inversion in the sphere of radius \(\sqrt2\) centred there, restricted to the unit sphere.

### Appendix C

Duality, Desargues, Pappus, the cross-ratio, and the fundamental theorem. The Fano plane has \(168\) collineations. \(\lvert\mathrm{PGL}_3(\mathbb F_4)\rvert=60480\), and the full collineation group has order \(120960\). The Hamming code of the Fano plane is the \([7,4,3]\) code. The order-6 plane is excluded by the quoted Bruck–Ryser theorem.

### Appendix D

Five points determine a conic, Pascal, poles and polars, and Poncelet’s porism for two circles. The rational parametrization of the circle is \(((1-t^2)/(1+t^2),2t/(1+t^2))\). Volume 2, Theorem 8.1, is the primitive Pythagorean classification. The Pell conic \(y^2-2x^2=1\) has positive solutions \((2,3),(12,17),(70,99),\ldots\). Fuss’s condition for a bicentric kite is \(r^2/a^2+r^2/b^2=1\).

### Appendix E

Sylvester’s law, the classification of quadrics, the Segre quadric, and Witt cancellation. Volume 1, Theorem 7.9, is the spectral theorem for a real symmetric matrix, and Theorem 7.10 is the Gram identity \(\lvert\det A\rvert=\mathrm{vol}\).

### Appendix F

The resultant, Bézout’s count relative to one projection point, and Cayley–Bacharach for cubics. The intrinsic multiplicity is marked as Volume 13, Chapter 14. The lemniscate \((x^2+y^2)^2=z^2(x^2-y^2)\) is irreducible and has three singular points. The \(3\times3\) interpolation weights, multiplied by four, are the pattern \((1,-2,1)\otimes(1,-2,1)\).

### Appendix G

The chord law, associativity when nine points are distinct, the Weierstrass form, and nine flexes. The full group law is quoted from Volume 13, Chapter 15, and is not inferred from the nine-point case. Bachet’s point on \(y^2=x^3-2\) doubles to a non-integral point, and \(66234835^2=164323^3-2\cdot171^6\). The curve \(y^2=x^3+x+1\) over \(\mathbb F_5\) has nine points in one orbit. The Hesse pencil has twelve lines and \(\binom92=36\) pairs. Hasse’s bound is quoted from Volume 13, Chapter 16.

### Appendix H

Blichfeldt, Minkowski’s theorem, sums of two squares, Gauss reduction, and \(E_8\). The shortest vectors number \(112+128=240\), the covolume is 1, and the density is \(\pi^4/384\approx0.2537\). The open ball \(\lvert x\rvert^2<2p\) in \(\R^4\) has volume \(2\pi^2 p^2>16p^2\). Volume 3, Lemma 7.5, is freeness of submodules of \(R^n\), and Theorem 7.6 is the structure theorem over a PID. Viazovska’s theorem and the Leech lattice are quoted.

### Appendix I

Girard’s theorem and the spherical cosine law. A trirectangular triangle has area \(\pi/2\). The hyperbolic circle of radius \(r\) has length \(2\pi\sinh r\) and area \(4\pi\sinh^2(r/2)\). The distance from \(1+i\) to \(3+i\) is \(\log(3+2\sqrt2)\approx1.763\), against horizontal length 2. The smallest positive area of a \((p,q,r)\) triangle is \(\pi/42\), for \(\{2,3,7\}\).

### Appendix J

Helly, Buffon, Cauchy’s width formula, Barbier, Brunn–Minkowski, and the isoperimetric inequality. A Reuleaux triangle of width 1 has area \((\pi-\sqrt3)/2\approx0.7048\), against \(\pi/4\) for the disc. Lazzarini’s ratio \(355/113\) requires a multiple of \(213\) throws; \(T=3408\) and \(C=1808\) give it. A needle longer than the spacing has hit probability \((2/\pi)(\ell-\sqrt{\ell^2-1}+\arccos(1/\ell))\), and expected count \(2\ell/\pi\). The support function \(1+\eta\cos 3\theta\), with \(\lvert\eta\rvert<1/8\), has width 2, perimeter \(2\pi\), and area \(\pi-4\pi\eta^2\).

### Appendix K

The fundamental theorem for plane curves, the four-vertex theorem, Euler’s formula, and Descartes’s defect. The ellipse \(1.6\cos t,\sin t\) has radii of curvature \(0.625\) and \(2.56\). The clothoid with \(\kappa(s)=s\) tends to \((\sqrt\pi/2,\sqrt\pi/2)\). The five Platonic solids each have total defect \(4\pi\). A football has twelve pentagons. The graph \(z=(a x^2+b y^2)/2\) has total curvature \(2\pi\operatorname{sgn}(ab)\) when \(ab\ne0\). Volume 7, Theorem 6.1, is the polygonal Jordan theorem.

### Index

The index entries that were matched to labels point at the statements named above. Page numbers are produced by `\pageref` and were not compiled.

## Not checked

- A TeX run, so unresolved references were not compiled. The numbered statements above were counted from the source environments.
- Portrait files against `photos/CREDITS.md`.
- TikZ coordinate files against their captions, beyond the mathematical claims that were recomputed. The contact sheets, the Coxeter projection of the \(240\) roots, and the sampled \(U(24)\) eigenvalues were not regenerated.
- The universal-polynomial identity for the resultant, beyond the degree count and the specialisation \(c=1\) written in the solution.
- The historical fine print against the primary papers, beyond the citations printed in the chapters. The attributions that the text marks as quotations were left as quotations, including Perelman, Adams, the general de Rham theorem, the general Weyl formula, Viazovska, the Leech lattice, Mazur, and Bruck–Ryser.
