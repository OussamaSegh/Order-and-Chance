# Volume 8 — Analysis

**Score: 8/10.**

Hahn–Banach, the Baire theorems, weak compactness, the projection theorem, the compact spectral theorem, the matrix spectral theorem and the singular-value decomposition, Cheeger’s inequality, the expander Chernoff bound, Wiener’s lemma, Sturm–Liouville, Plancherel, the Sobolev embedding on the line, quadratic reciprocity again, Haar measure and the self-duality of \(\Q_p\), Dixon’s theorem, Hadamard factorisation, Wiener–Ikehara, and the second proof of the prime number theorem are proved. The constants that were recomputed match the page. The score is 8 because the slips are local: two theorem numbers point at a neighbouring result, one complex estimate is a phase short, one figure’s tails are coarser than the drawn picture, and the listing says every theorem is proved. No numbered statement was found false.

**Counts.** 0 critical, 0 major, 11 minor. Eleven issues, `V8-001` through `V8-011`. None is a prerequisite issue.

**How this was read.** Book order in `volume8-analysis/main.tex`: preface, Banach and Hilbert (Chapters 1–2), Spectral Theory (3–9), Fourier and Tauberian Methods (10–16), then Appendices A–F and About the Cover. The blurb and `kdp.md` were read with the preface. Every chapter file was read, including every exercise, hint, and solution. There are 300 exercises. The shared theorem counter was counted in source order. Exercises use a separate counter and restart each chapter. After `\appendix` the chapter letters are A–F.

**Style, once.** The house voice holds. No notebook is mentioned, and the reader-facing copy does not call the book a revision. “Moreover” occurs inside arguments (`chapters/ch01-banach.tex:98`, `:223`, `chapters/ch04-spectral.tex:92`, `chapters/linear-ch04-inner.tex:84`), not as a section opener. The exercise grade `[Journey]` is printed in place of the stars, twice, and it is V8-008. Two sentences send the reader to Problem Book I, and that is V8-007.

## Issues

Paths are relative to `volume8-analysis/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V8-001 | `chapters/ch01-banach.tex:277` (`thm:alaoglu`) | reference | minor | “A diagonal extraction (Volume 7, Theorem 4.15)”. | Theorem 4.15 is Arzelà–Ascoli. The diagonal extraction is the argument inside that proof, and it is written out in Volume 7, Exercise `ex:hilbertcube`. Point at the exercise, or say that the proof of Theorem 4.15 extracts the subsequence. |
| V8-002 | `chapters/ch01-banach.tex:259` | reference | minor | “Approximate an arbitrary \(g\in L^1\) by a step function \(h\) (Volume 7, Theorem 10.7)”. | Theorem 10.7 is density of \(C_c\). Simple functions are Proposition 10.6. The same chapter’s solution of the reflexive exercise cites both. The estimate works with either approximation. |
| V8-003 | `chapters/ch02-hilbert.tex:237` (`thm:aronszajn`) | math | minor | “Cauchy–Schwarz follows, even before positive definiteness, by expanding \(\langle f+tg,f+tg\rangle\ge 0\) and minimising over \(t\).” | Real \(t\) bounds the real part. The kernel is Hermitian, and the Gaussian example uses complex coefficients. Replace \(g\) by a phase times \(g\), then minimise. |
| V8-004 | `chapters/linear-ch05-spectral.tex:201` | math | minor | “Rado’s theorem identifies it with the convex hull of the permuted spectrum.” | The identification is asserted, not proved, not marked quoted, and not used again. Schur–Horn is the theorem that was proved. Mark Rado quoted. |
| V8-005 | `chapters/linear-ch06-svd.tex:161` (`linear:fig:lowrank`) | figure | minor | “The relative errors in Frobenius norm … are about \(0.30\), \(0.16\) and \(0.07\).” | On the drawn original panel the singular-value tails are \(0.277\), \(0.121\) and \(0.047\). The rank-8 storage count \(8\cdot 65=520\) is right. Print \(0.28\), \(0.12\) and \(0.05\). |
| V8-006 | `kdp.md:13` | reference | minor | “Every theorem is proved.” | The blurb names the spectral theorem that is proved. The chapters mark Carleson, the unbounded spectral theorem, Littlewood’s \(O(1/n)\) converse, Landau’s unweighted two-squares theorem, the Pontryagin–van Kampen theorem in general, and several others as quoted. Say that the theorems of the main path are proved, and that the quotations are marked. |
| V8-007 | `chapters/ch11-harder.tex:175` (`pb:ramanujan`); also the solution of `pb:zetamellin` at `:645` | style | minor | “they are also the subject of Problem Book I, Problem 2.3.” The zeta-mean solution adds “Problem Book I, Problem 9.12”. | The solution of `pb:ramanujan` already says the argument needs no result from that book. Delete both pointers. |
| V8-008 | `chapters/ch11-harder.tex:96` (`pb:mvt`); also `:222` (`pb:vandelune`) | style | minor | The optional argument is `[Journey]`, which the exercise box prints in place of the stars. | The other grades in the chapter are \(\star\), \(\star\star\), and \(\star\star\star\). The preface does not say what Journey means. Give both \(\star\star\star\). |
| V8-009 | `chapters/linear-ch03-eigen.tex:359` (solution of `linear:ex:sqrt`) | exercise | minor | “The first kernel has dimension one below \(n\), a contradiction.” | The preceding sentence has \(\dim\ker B^2=1\). The common kernel dimension is \(1\), and \(1<n\). The words “one below \(n\)” read as \(n-1\). |
| V8-010 | `chapters/ch10-tauberian.tex:326` (`cor:pntapikehara`) | reference | minor | “\(L(s,\chi)\) is holomorphic on \(\operatorname{Re}s>0\) and nonzero on \(\operatorname{Re}s\ge 1\), including one, by Volume 6, Theorem 5.2.” | Theorem 5.2 is the nonvanishing on the line \(\operatorname{Re}s=1\). Holomorphy on \(\operatorname{Re}s>0\), and nonvanishing for \(\operatorname{Re}s>1\), are Volume 6, Theorem 3.6. |
| V8-011 | `chapters/ch05-fourier.tex:232` | reference | minor | “the identity from Volume 7, Exercise 10.2” for \(p_s*p_t=p_{s+t}\). | Exercise 10.2 states the identity and says Volume 8 proves it. The sentence before the citation is that proof. Drop the backward pointer. |

## Verified correct

### Preface, blurb, listing, cover

The preface’s map matches the sixteen chapters and the six appendices. It assumes Volume 7, Volume 5’s Fourier series and complex analysis, Volume 3’s groups, and Volume 1’s linear algebra. Adèles are deferred to Volume 13. The blurb names the spectral theorem that is proved: matrices, and compact self-adjoint operators. The listing’s sentence “Every theorem is proved” is V8-006. About the Cover is the partial sums of the square wave, with the Gibbs overshoot, Wilbraham 1848 and Gibbs 1899. The square wave’s Fourier series is the one drawn.

### Chapter 1

Normed spaces, Riesz’s lemma, the non-compactness of the unit ball, Hahn–Banach in both forms, uniform boundedness, a continuous function with a divergent Fourier series, the open mapping and closed graph theorems, the dual of \(L^p\), Riesz–Markov, reflexivity, and Banach–Alaoglu. The Lebesgue constants, recomputed from the Dirichlet kernel, are \(L_1=1.436\), \(L_{10}=2.223\), \(L_{100}=3.139\), \(L_{1000}=4.070\), and \((4/\pi^2)\log 10=0.933\). The two citations in the weak-star and Alaoglu arguments are V8-001 and V8-002. The oscillation figure is \(\operatorname{sgn}\sin(nx)\) at \(n=2\) and \(n=12\).

### Chapter 2

The nearest point in a closed convex set, orthogonal decomposition, Riesz–Fréchet, orthonormal bases, the trigonometric system in \(L^2\), Legendre polynomials through the Rodrigues formula’s consequences that are proved here, Kronecker–Weyl, von Neumann’s mean ergodic theorem, the second proof of Radon–Nikodym, and Moore–Aronszajn. The complex Cauchy–Schwarz step is V8-003. The Gaussian kernel’s positivity is the Fourier representation from Volume 5, Theorem 8.3. The Legendre plate matches \(P_1\) through \(P_5\).

### Chapter 3

The spectral theorem for normal matrices, Courant–Fischer, Cauchy interlacing, Weyl’s inequalities, Birkhoff’s theorem on doubly stochastic matrices, Schur–Horn, and Hoffman–Wielandt. The Rayleigh quotient of the displayed \(2\times 2\) matrix has maximum \(3\) at \(\pi/6\) and minimum \(1\) at \(2\pi/3\). Rado’s sentence is V8-004. Horn’s conjecture and Mirsky’s dominance theorem are quoted.

### Chapter 4

The singular-value decomposition, the polar decomposition, Ky Fan norms, Eckart–Young, the pseudoinverse, principal components, the condition number, and orthogonal Procrustes. The matrix \(\begin{pmatrix}3&0\\4&5\end{pmatrix}\) has singular values \(3\sqrt 5\) and \(\sqrt 5\). The low-rank caption is V8-005. A singular triple of a \(1000\times 1000\) matrix costs \(2001\) numbers, and twenty-four cost \(48024\).

### Chapter 5

Friendship, the eigenvalues of a strongly regular graph, the Hoffman–Singleton bound, Hoffman’s ratio bound, the Erdős–Ko–Rado theorem for pairs, Graham–Pollak, Huang’s signed adjacency theorem, and Schwenk’s theorem on the spectral determination of trees. The Petersen graph has spectrum \(3,1^5,(-2)^4\). Huang’s neighbour lists on the \(8\)-cycle plus the edge \(1100\) in the \(4\)-cube were checked. The factor \(2\) in the sensitivity bound is the Nisan–Szegedy estimate the text cites. The matrix-tree theorem is deferred to Volume 12, Appendix A, where it is proved.

### Chapter 6

The Rayleigh quotient for the Laplacian, Cheeger’s inequality, the expander mixing lemma, and the Alon–Boppana bound in Nilli’s form. The cycle ratio \(h/\sqrt{2d\mu_2}\) tends to \(1/\pi\). The level-set figure with heights \(9,4,1,0\) matches the exercise.

### Chapter 7

Mixing and hitting, the expander Chernoff bound with constant \(20\), the non-backtracking polynomials, Kesten’s measure, McKay’s theorem, Serre’s gap, the Ihara determinant, Bass’s formula, the Riemann hypothesis for graphs, and the prime-number theorem for graphs. The tree moments \(a_4=d(2d-1)\) and \(a_6=d(5d^2-6d+2)\) give \(15\) and \(87\) at \(d=3\). The graph prime-number bound \(6nq^{k/2}/k\) was checked. Friedman, the LPS construction, and the Huang–McKenzie–Yau proportion are quoted.

### Chapter 8

The adjoint, compact operators, Hilbert–Schmidt kernels, the Fredholm alternative, the Neumann series, the spectrum, Gelfand–Mazur, the spectral radius formula, and Wiener’s lemma. The curve \(1+0.6e^{it}+0.3e^{-3it}\) has modulus between \(0.100\) and \(1.900\). Schauder’s theorem cites Volume 7, Theorem 4.15, and that citation is Arzelà–Ascoli.

### Chapter 9

The spectral theorem for a compact self-adjoint operator, the min-max principle, Weyl’s perturbation bound, the Sturm–Liouville oscillation theorem, Weyl’s law on an interval, Hilbert–Schmidt operators, Mercer, and the continuous functional calculus. For \(q=60x\) the first four eigenvalues are about \(36.17\), \(70.42\), \(119.52\) and \(188.34\), inside the caption’s one-decimal values, and each sits above \(\pi^2 n^2\). The Brownian covariance puts mass \(8/\pi^2\) on the first mode. The Basel identity \(\int_0^1\int_0^1\min(s,t)\,ds\,dt=1/90\) was checked. The unbounded spectral theorem, Ambartsumian, Borg, and Gordon–Webb–Wolpert are quoted. Dini’s theorem is Volume 7, Exercise 4.1, as the Mercer argument says.

### Chapter 10

The \(L^1\) transform, inversion, the Schwartz class, Plancherel, the Hermite basis, the three-lines lemma, Riesz–Thorin, Hausdorff–Young, uniqueness of measures, the Cauchy law, Shannon sampling in the Hilbert-space form, and Poisson summation for a lattice. The Gaussian \(e^{-4\pi x^2}\) transforms to \(\tfrac12 e^{-\pi\xi^2/4}\). The backward pointer for the Cauchy semigroup is V8-011. Shannon’s theorem in Volume 5 is Theorem 8.15. Bochner’s converse and Beckner’s sharp constant are quoted.

### Chapter 11

Distributions, distributional derivatives, the structure of a distribution supported at a point, smoothing, tempered distributions and their transforms, Newton’s potential, the Sobolev scale, the embedding \(H^1(\R)\hookrightarrow L^\infty\), Rellich, Lax–Milgram, and Céa’s lemma. The two-material flux constant is \(5/12\), and the Galerkin error on the hat basis is \(1/48\). The identity \(\lVert f\rVert_{H^1(\R)}^2=\lVert f\rVert_2^2+(4\pi^2)^{-1}\lVert f'\rVert_2^2\) was checked. The Newtonian integral of the fundamental solution against a radial test equals \(1\). Malgrange–Ehrenpreis in general is quoted.

### Chapter 12

Duality for finite abelian groups, annihilators, convolution, Poisson summation, the splitting lemma, the fast transform, Donoho–Stark, Chebotarev’s lemma, Tao’s uncertainty principle, the Gauss-sum proof of quadratic reciprocity, Meshulam’s cap-set bound, and the Blum–Luby–Rubinfeld test. The number of nonempty square minors of the \(5\times 5\) Fourier matrix is \(\binom{10}{5}-1=251\). The cap-set comparison at \(t=3/5\) differs by the positive integer \(1574950625\). Volume 3’s citations match: Corollary 7.7 is the structure of finitely generated abelian groups, Theorem 11.14 is abelian Fourier analysis, Proposition 10.9 is the cyclotomic Galois group, and Example B.15 is the length-\(7\) code of \(8\) words.

### Chapter 13

Left Haar measure, uniqueness on a second-countable locally compact group, the Markov–Kakutani fixed-point theorem, amenability of abelian groups, Banach’s finitely additive measure on \(\Z\), the free-group paradox, Hausdorff’s paradoxical decomposition of the sphere, the duals of \(\R\), \(\Z\), the circle and \(\Q_p\), and the Fourier transform on \(\Q_p\). The Jacobian of left multiplication on \(GL_n\) is \((\det A)^n\). The rotation through \(\arccos(1/3)\) matches the matrices in the Hausdorff argument. The ball \(B_n\) in the free group on two generators has size \(2\cdot 3^n-1\). The modular function of the affine group is \(\Delta(a)=a_0^{-1}\). Compactness of \(\Z_p\) is Volume 7, Corollary 2.11. The general Pontryagin–van Kampen theorem is quoted.

### Chapter 14

The homology form of Cauchy’s theorem, the residue theorem, the argument principle in that form, Phragmén–Lindelöf, the convexity bound for \(\zeta\), Hadamard factorisation, Mellin inversion, and the maximum of geometric levels. The oscillation bound in `thm:maxgeom` was certified by the rational comparison printed in the proof: the Taylor sum through order \(69\) exceeds the displayed threshold, and the loose majorant is about \(1.590\times 10^{-6}\), under \(1.6\times 10^{-6}\). Riemann mapping is deferred to Volume 9. Rouché is Volume 5, Theorem 9.38. The change of variables used for the Bergman area is Volume 7, Theorem 9.8. Bourgain’s \(13/84\) is quoted.

### Chapter 15

Abel’s theorem, the passage from Cesàro to Abel, Tauber’s theorem, the Hardy–Littlewood–Karamata theorem, Wiener’s theorem on translates, the Tauberian form, Wiener–Ikehara, the prime number theorem, the theorem for progressions, and the weighted count of sums of two squares. The local-inverse modulation has the frequency shift in the direction the uniqueness step needs. The Ikehara smoothing uses \(k_1\ge 4/\pi^2\) on an interval of length \(1/2\). The constant \(K\) begins \(0.76422365\), and \(\Gamma(3/2)=\sqrt\pi/2\) turns \(K\sqrt\pi\) into \(2K\). The citation of holomorphy in the progression corollary is V8-010. Volume 6, Theorem 5.5, is the prime number theorem, including the passage from \(\psi\) to \(\pi\). Volume 6, Example 3.11, is \(L(1,\chi_{-4})=\pi/4\). Littlewood’s \(O(1/n)\) converse, Landau’s unweighted theorem, and Delange’s extension are quoted.

### Chapter 16

Every problem was read, including the hints and the solutions. There is no numbered theorem. Selberg’s Gram bound, Welch’s bound with equality for the Mercedes-Benz frame and the icosahedron, Gerzon’s \(n(n+1)/2\), Halász, Ingham’s cosine weight, the Fejér majorant, the Christoffel–Darboux kernel for Legendre polynomials, the Bergman space and the area theorem, the Fock space, the Sobolev kernel on an interval, the Dirichlet-series Hilbert space, Franel’s integral, Ramanujan’s expansion with mean \(\tfrac52\zeta(3)\), the weighted zeta mean \(\log(2\pi)-\gamma\), one direction of Nyman–Beurling, Bohr’s value set, relative density of returns, van de Lune’s threshold, Khinchin recurrence, arbitrarily slow ergodic averages, Wiener’s theorem on atoms, and Gebelein’s inequality. Recomputed: the icosahedral coherence is \(1/5\); Ingham’s telescoping sum equals \(1/2\); the mean-value constant \((2\pi+4)/(\pi-1)\) is below \(5\); \(\zeta(2)^2\zeta(3)/\zeta(4)=\tfrac52\zeta(3)\approx 3.00514\); \(\log(2\pi)-\gamma\approx 1.26066\); the Cantor coefficient is \(0.37144\); the four planar lines at angles \(\pi/4\) have Gram row sum \(1+\sqrt 2\) and frame bound \(2\). The grades `[Journey]` are V8-008. The Problem Book pointers are V8-007. Pólya–Vinogradov is Volume 6, Theorem 11.11. The Cantor coefficient is Volume 7, Problem 13.16. Volume 14, Lemma 1.3, is the mean-value bound with error \(8M(1+\log M)\), cited as a comparison. The map at the end of the chapter sends each problem to chapters already proved.

### Appendix A

Steinitz exchange, dimension, quotients, the first isomorphism theorem, the dual basis, the double dual, Lagrange interpolation, the trace pairing, annihilators, the transpose, the finite-dimensional Fredholm alternative, Oddtown, and unisolvent points. On the \(5\times 5\) Lights Out board, \(P_6\) is the printed matrix and its kernel over \(\mathbb F_2\) has dimension \(2\). The \(3\times 3\) and \(6\times 6\) boards are invertible, and the \(4\times 4\) kernel has dimension \(4\). Simpson’s weights are \(1/6\), \(2/3\), \(1/6\), and the cubic moment is \(1/4\). The cubic \(1+2X+3X^2+4X^3\) reduces to \(1+9X\).

### Appendix B

Exterior powers, Cauchy–Binet, Jacobi’s complementary minors, the adjugate identity, Desnanot–Jacobi, Dodgson condensation, the Lindström–Gessel–Viennot lemma, and the lozenge determinant. The side-two hexagon has determinant \(20\). MacMahon’s product at side three is \(980\). Condensation of the printed \(4\times 4\) matrix ends at \(-20\), which is its determinant. The shoelace of \((0,0),(4,0),(5,3),(2,5),(-1,2)\) is \(20\). The alternating-sign counts \(1,2,7,42,429,7436\) are the quoted enumeration. The general MacMahon product is quoted, and the cases \(c=1,2\) are proved.

### Appendix C

Independence of eigenvectors, triangularisation, Cayley–Hamilton, the kernel lemma, generalised eigenspaces, the Dunford decomposition, the Jordan form, commuting families, and the matrix exponential. The nilpotent diagram with kernel dimensions \(4,7,8,9\) has block sizes \(4,2,2,1\). The perturbation \(10^{-6}\) of \(J_{12}\) has spectral radius \(10^{-1/2}\approx 0.316\). The off-diagonal entry \(10k(9/10)^{k-1}\) equals \(38.742\) at \(k=9\) and at \(k=10\). The square-root solution’s last sentence is V8-009. Partitions of \(6\) with parts at most \(3\) number seven.

### Appendix D

Cauchy–Schwarz, Gram–Schmidt, \(QR\), orthogonal projection, least squares, Gauss–Markov, Gram determinants, Cauchy’s determinant, the Hilbert matrix, the three-term recurrence, the zeros of an orthogonal polynomial, Gauss quadrature, finite-dimensional Riesz representation, the adjoint, unitary maps, and Cholesky. The line through \((0,0),(1,1),(2,1)\) is \(y=1/6+x/2\), with squared error \(1/6\). The distances from \(t\) and \(t^2\) to lower degrees on \([0,1]\) are \(1/(2\sqrt 3)\) and \(1/(6\sqrt 5)\). The reciprocal Hilbert determinants through size four are \(1\), \(12\), \(2160\), \(6048000\). The three-node Legendre rule has nodes \(\pm\sqrt{3/5},0\) and weights \(5/9,8/9,5/9\), and the error on \(t^6\) is \(8/175\). Weighted least squares with weights \(1,2,1\) gives residuals \(-1/4,1/4,-1/4\) and weighted squared error \(1/4\).

### Appendix E

The Loewner order, Löwner–Heinz for the square root, Schur complements, Sylvester’s identity, Hadamard, Fischer, Minkowski’s determinant inequality, concavity of \(\log\det\), the Schur product theorem, Gershgorin, and Hilbert’s inequality with constant \(\pi\). For the printed pair, \(\det(A-B)=9/200\) and \(\det(A^2-B^2)=-25219/40000\). The row-sum comparison uses the convexity of \(1/((m+1+x)\sqrt{x+1/2})\) and evaluates to \(\pi\). The Hadamard existence claim below \(2000\) is a citation of a 2026 report. Loewner’s characterisation of operator-monotone functions is quoted.

### Appendix F

An adapted norm, convergence of powers, Gelfand’s formula, exponential stability, Lyapunov’s equation, Chebyshev acceleration, the heavy ball, Kalman’s rank condition, and Maxwell’s cubic. At \(\kappa=100\) the three rates are \(99/101\), \(9/11\) and \(2(9/11)^k\). The energy matrix in the figure satisfies \(A^{\mathsf T}P+PA=-I\). The least-energy cart costs \(12/T^3\). Maxwell’s identity \(ab-c=p(b+r^2)\) was checked. The cubic \(s^3+2s^2+s+k\) is stable for \(0<k<2\), and at \(k=2\) it is \((s+2)(s^2+1)\). Nesterov’s theorem beyond quadratics, and the general Routh–Hurwitz criterion, are quoted.

## Not checked

- A TeX run, so unresolved references were not compiled. The numbered statements above were counted from the source environments.
- Portrait files against `photos/CREDITS.md`.
- TikZ coordinate files against their captions, beyond the mathematical claims that were recomputed. The Kesten–McKay histogram, the pseudospectra of the \(64\times 64\) Jordan block, and the Fiedler drawing were not regenerated.
- The Hadamard constructions announced in August 2026 and the report arXiv:2610.27175.
- The long decimal \(\sigma_0=1.192347337186193\ldots\), which the solution marks as a reported approximation.
- De Bruijn–Wilf’s asymptotic \(\pi-\lambda_{\max}(H_N)\sim\pi^5/(2\log^2 N)\), quoted.
- The historical fine print against the primary papers, beyond the citations printed in the chapters. The attributions that the text marks as quotations were left as quotations.
