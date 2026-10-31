# Volume and chapter map

Internal editorial map for Edition 1. Reader-facing books use the new numbers only.
The renumber commit `68aff65` gave the volumes their present numbers and left chapter-body citations on the old ones.
A citation that a later commit changed is already on the new number. Every other citation was translated with this table.

## Old number to title-page number

| Old citation | Title now | Directory now |
| --- | --- | --- |
| 0 | 1 First Principles | `volume1-first-principles` |
| 1 | 2 The Integers | `volume2-integers` |
| 2 | 3 Symmetry | `volume3-symmetry` |
| 3 | 4 Chance | `volume4-chance` |
| 4 | 5 Calculation | `volume5-calculation` |
| 5 | 6 Crossroads | `volume6-crossroads` |
| 6 | 7 Spaces | `volume7-spaces` |
| 7 | 8 Analysis | `volume8-analysis` |
| 8 | 9 Shapes | `volume9-shapes` |
| 9 | 10 Abstraction | `volume10-abstraction` |
| 10 | 11 Randomness | `volume11-randomness` |
| 11 | 12 Random Motion | `volume12-random-motion` |
| 12 | 13 Arithmetic | `volume13-arithmetic` |
| 13 | 14 The Primes | `volume14-primes` |
| 14 | 15 Order and Chance | `volume15-order-and-chance` |

Old Volume 0's numbered citations (Proposition 3.7, Exercise 1.6, and the rest) use the original eight-chapter edition, not the chapter numbers printed after the foundations book was reordered. `review/volume0-reconstruction/NUMBERING-CONCORDANCE.md` sends each of those numbers to a label, and the label's place in the present Volume 1 is the number printed now. The language chapter is chapter 0.

## Where each old chapter sits now

| Old vol. | Old ch. | Title then | File then | Now |
| --- | --- | --- | --- | --- |
| 0 | 0 | The Language of Mathematics | `chapters/ch00-language.tex` | Volume 1, Chapter 0 |
| 0 | 1 | Sums, Binomials and Induction | `chapters/ch01-sums.tex` | Volume 1, Chapter 1 |
| 0 | 2 | Counting and Discrete Reasoning | `chapters/ch02-counting.tex` | Volume 1, Chapter 2 |
| 0 | 3 | Sequences, Series and Limits | `chapters/ch05-sequences-series.tex` | Volume 1, Chapter 3 |
| 0 | 4 | Complex Numbers and Roots of Unity | `chapters/ch02-complex-roots.tex` | Volume 1, Chapter 5 |
| 0 | 5 | Polynomials | `chapters/ch03-polynomials.tex` | Volume 1, Chapter 6 |
| 0 | 6 | Linear Algebra | `chapters/ch07-linear-algebra.tex` | Volume 1, Chapter 7 |
| 0 | 7 | Differential and Integral Calculus | `chapters/ch06-integrals-taylor.tex` | Volume 1, Chapter 8 |
| 0 | 8 | Inequalities, Convexity and Estimates | `chapters/ch04-inequalities.tex` | Volume 1, Chapter 9 |
| 0 | 9 | First Probability | `chapters/ch09-probability.tex` | Volume 1, Chapter 10 |
| 1 | 1 | Divisibility and the Euclidean Algorithm | `chapters/ch01-divisibility.tex` | Volume 2, Chapter 1 |
| 1 | 2 | Primes | `chapters/ch02-primes.tex` | Volume 2, Chapter 2 |
| 1 | 3 | Congruences | `chapters/ch03-congruences.tex` | Volume 2, Chapter 3 |
| 1 | 4 | Primitive Roots and the Multiplicative Group | `chapters/ch05-primitive-roots.tex` | Volume 2, Chapter 4 |
| 1 | 5 | Quadratic Residues and Reciprocity | `chapters/ch06-quadratic-reciprocity.tex` | Volume 2, Chapter 5 |
| 1 | 6 | Arithmetic Functions | `chapters/ch04-arithmetic-functions.tex` | Volume 2, Chapter 6 |
| 1 | 7 | Sums of Squares | `chapters/ch07-sums-of-squares.tex` | Volume 2, Chapter 7 |
| 1 | 8 | Continued Fractions and Pell's Equation | `chapters/ch08-continued-fractions.tex` | Volume 2, Chapter 8 |
| 1 | 9 | Diophantine Equations | `chapters/ch09-diophantine.tex` | Volume 2, Chapter 9 |
| 1 | 10 | Gaussian and Eisenstein Integers | `chapters/ch10-gaussian-eisenstein.tex` | Volume 2, Chapter 10 |
| 1 | 11 | Quadratic Fields and Their Integers | `chapters/ch11-algebraic.tex` | Volume 13, Chapter 1 |
| 1 | 12 | Ideals, Prime Splitting and Class Groups | `chapters/ch12-ideals.tex` | Volume 13, Chapter 2 |
| 1 | 13 | The \texorpdfstring{$p$}{p}-adic Numbers | `chapters/ch12-padic.tex` | Volume 13, Chapter 8 |
| 1 | 14 | Characters, Euler Products and the Sieve | `chapters/ch14-characters.tex` | Volume 2, Chapter 11 |
| 2 | 1 | Groups as Symmetries | `chapters/ch01-groups.tex` | Volume 3, Chapter 1 |
| 2 | 2 | Morphisms and Quotients | `chapters/ch02-quotients.tex` | Volume 3, Chapter 2 |
| 2 | 3 | Group Actions and Counting | `chapters/ch03-actions.tex` | Volume 3, Chapter 3 |
| 2 | 4 | The Symmetric Group | `chapters/ch04-symmetric.tex` | Volume 3, Chapter 4 |
| 2 | 5 | Sylow Theorems and Finite Groups | `chapters/ch05-sylow.tex` | Volume 3, Chapter 5 |
| 2 | 6 | Rings and Ideals | `chapters/ch06-rings.tex` | Volume 3, Chapter 6 |
| 2 | 7 | Modules over a Principal Ideal Domain | `chapters/ch07-modules.tex` | Volume 3, Chapter 7 |
| 2 | 8 | Field Extensions | `chapters/ch08-extensions.tex` | Volume 3, Chapter 8 |
| 2 | 9 | Finite Fields | `chapters/ch09-finite-fields.tex` | Volume 3, Chapter 9 |
| 2 | 10 | Galois Theory | `chapters/ch10-galois.tex` | Volume 3, Chapter 10 |
| 2 | 11 | Representations and Characters | `chapters/ch11-characters.tex` | Volume 3, Chapter 11 |
| 2 | 12 | A Glimpse Beyond: Quaternions and Rotations | `chapters/ch12-quaternions.tex` | Volume 3, Chapter 12 |
| 2 | A | Spaces, Quotients and Duality | `chapters/linear-ch01-duality.tex` | Volume 8, Chapter 3 |
| 2 | B | Determinants as Volume | `chapters/linear-ch02-volume.tex` | Volume 8, Chapter 4 |
| 2 | C | Eigenvalues and Invariant Subspaces | `chapters/linear-ch03-eigen.tex` | Volume 8, Chapter 5 |
| 2 | D | Inner Products and Projections | `chapters/linear-ch04-inner.tex` | Volume 8, Chapter 6 |
| 2 | E | The Spectral Theorem and Its Relatives | `chapters/linear-ch05-spectral.tex` | Volume 8, Chapter 7 |
| 2 | F | Singular Values | `chapters/linear-ch06-svd.tex` | Volume 8, Chapter 8 |
| 2 | G | Positive Matrices | `chapters/linear-ch07-perron.tex` | Volume 3, Chapter A |
| 2 | H | Graphs through Their Eigenvalues | `chapters/linear-ch08-graphs.tex` | Volume 8, Chapter 9 |
| 2 | I | Symmetry Diagonalises | `chapters/linear-ch09-symmetry.tex` | Volume 3, Chapter B |
| 2 | J | Tensors and the Cost of Multiplying Matrices | `chapters/linear-ch10-tensors.tex` | Volume 10, Chapter 2 |
| 2 | K | Inequalities between Matrices | `chapters/linear-ch11-inequalities.tex` | Volume 8, Chapter 14 |
| 2 | L | Linear Dynamics | `chapters/linear-ch12-dynamics.tex` | Volume 8, Chapter 15 |
| 2 | M | The Linear Algebra Method | `chapters/combinatorial.tex` | Volume 3, Chapter C |
| 3 | 1 | Counting and Paradoxes | `chapters/ch01-counting.tex` | Volume 4, Chapter 1 |
| 3 | 2 | Discrete Random Variables | `chapters/ch02-discrete.tex` | Volume 4, Chapter 2 |
| 3 | 3 | Generating Functions | `chapters/ch03-generating.tex` | Volume 4, Chapter 3 |
| 3 | 4 | Inequalities, Large Numbers and Entropy | `chapters/ch04-inequalities.tex` | Volume 4, Chapter 4 |
| 3 | 5 | Continuous Probability Done Properly | `chapters/ch05-continuous.tex` | Volume 4, Chapter 5 |
| 3 | 6 | Convergence and the Central Limit Theorem | `chapters/ch06-clt.tex` | Volume 4, Chapter 6 |
| 3 | 7 | Random Walks | `chapters/ch07-walks.tex` | Volume 4, Chapter 7 |
| 3 | 8 | Markov Chains | `chapters/ch08-markov.tex` | Volume 4, Chapter 8 |
| 3 | 9 | Poisson Processes | `chapters/ch09-poisson.tex` | Volume 4, Chapter 9 |
| 3 | 10 | Conditional Expectation and Martingales | `chapters/ch10-martingales.tex` | Volume 4, Chapter 10 |
| 3 | 11 | Brownian Motion | `chapters/ch11-brownian.tex` | Volume 4, Chapter 11 |
| 3 | 12 | The Probabilistic Method | `chapters/ch12-method.tex` | Volume 4, Chapter 12 |
| 3 | A | Orders | `chapters/orders.tex` | Volume 1, Chapter 4 |
| 3 | B | Extremal Problems and Ramsey Theory | `chapters/extremal.tex` | Volume 4, Chapter B |
| 4 | 1 | Finite Calculus | `chapters/ch01-finite.tex` | Volume 5, Chapter 1 |
| 4 | 2 | Generating Functions as a Computing Tool | `chapters/ch02-generating.tex` | Volume 5, Chapter 2 |
| 4 | 3 | Classic Series and Infinite Products | `chapters/ch03-series.tex` | Volume 5, Chapter 3 |
| 4 | 4 | Integration Techniques | `chapters/ch04-integrals.tex` | Volume 5, Chapter 6 |
| 4 | 5 | The Gamma and Beta Functions | `chapters/ch05-gamma.tex` | Volume 5, Chapter 7 |
| 4 | 6 | Fourier Series | `chapters/ch06-fourier.tex` | Volume 5, Chapter 8 |
| 4 | 7 | The Discrete Fourier Transform and the FFT | `chapters/ch07-fft.tex` | Volume 5, Chapter 9 |
| 4 | 8 | The Fourier Transform and Poisson Summation | `chapters/ch08-transform.tex` | Volume 5, Chapter 10 |
| 4 | 9 | Complex Analysis for Computing | `chapters/ch09-complex.tex` | Volume 5, Chapter 11 |
| 4 | 10 | The Zeta Function | `chapters/ch10-zeta.tex` | Volume 5, Chapter 12 |
| 4 | 11 | Asymptotics | `chapters/ch11-asymptotics.tex` | Volume 5, Chapter 13 |
| 4 | 12 | The Arithmetic--Geometric Mean | `chapters/ch12-agm.tex` | Volume 5, Chapter 14 |
| 5 | 1 | Mertens's Theorems | `chapters/ch01-mertens.tex` | Volume 6, Chapter 1 |
| 5 | 2 | Arithmetic Functions on Average | `chapters/ch02-averages.tex` | Volume 6, Chapter 2 |
| 5 | 3 | Dirichlet Characters and \texorpdfstring{$L$}{L}-Functions | `chapters/ch03-characters.tex` | Volume 6, Chapter 3 |
| 5 | 4 | Dirichlet's Theorem | `chapters/ch04-dirichlet.tex` | Volume 6, Chapter 4 |
| 5 | 5 | The Prime Number Theorem | `chapters/ch05-pnt.tex` | Volume 6, Chapter 5 |
| 5 | 6 | The Zeros of \texorpdfstring{$\zeta$}{zeta} | `chapters/ch06-zeros.tex` | Volume 6, Chapter 6 |
| 5 | 7 | The Explicit Formula and the Riemann Hypothesis | `chapters/ch07-explicit.tex` | Volume 6, Chapter 7 |
| 5 | 8 | Sieves | `chapters/ch08-sieves.tex` | Volume 6, Chapter 8 |
| 5 | 9 | The Erd\H{o}s--Kac Theorem | `chapters/ch09-erdoskac.tex` | Volume 6, Chapter 9 |
| 5 | 10 | Random Models of the Primes | `chapters/ch10-random.tex` | Volume 6, Chapter 10 |
| 5 | 11 | Exponential Sums | `chapters/ch11-sums.tex` | Volume 6, Chapter 11 |
| 5 | 12 | A Taste of Modular Forms | `chapters/ch12-modular.tex` | Volume 6, Chapter 12 |
| 6 | 1 | Sets, Choice and the Real Numbers | `chapters/ch01-sets.tex` | Volume 7, Chapter 1 |
| 6 | 2 | Metric Spaces and Completeness | `chapters/ch02-metric.tex` | Volume 7, Chapter 2 |
| 6 | 3 | Topological Spaces | `chapters/ch03-topology.tex` | Volume 7, Chapter 3 |
| 6 | 4 | Compactness | `chapters/ch04-compact.tex` | Volume 7, Chapter 4 |
| 6 | 5 | Baire's Theorem | `chapters/ch05-baire.tex` | Volume 7, Chapter 5 |
| 6 | 6 | Measures | `chapters/ch06-measures.tex` | Volume 7, Chapter 7 |
| 6 | 7 | The Lebesgue Integral | `chapters/ch07-integral.tex` | Volume 7, Chapter 8 |
| 6 | 8 | Product Measures and Change of Variables | `chapters/ch08-products.tex` | Volume 7, Chapter 9 |
| 6 | 9 | \texorpdfstring{$L^p$}{Lp} Spaces | `chapters/ch09-lp.tex` | Volume 7, Chapter 10 |
| 6 | 10 | Differentiation and Radon--Nikodym | `chapters/ch10-radon.tex` | Volume 7, Chapter 11 |
| 6 | 11 | Measures on Metric Spaces | `chapters/ch11-metricmeasures.tex` | Volume 7, Chapter 12 |
| 6 | 12 | Harder problems | `chapters/ch12-harder.tex` | Volume 7, Chapter 13 |
| 7 | 1 | Banach Spaces | `chapters/ch01-banach.tex` | Volume 8, Chapter 1 |
| 7 | 2 | Hilbert Spaces | `chapters/ch02-hilbert.tex` | Volume 8, Chapter 2 |
| 7 | 3 | Operators, Spectra and Banach Algebras | `chapters/ch03-operators.tex` | Volume 8, Chapter 16 |
| 7 | 4 | The Spectral Theorem | `chapters/ch04-spectral.tex` | Volume 8, Chapter 17 |
| 7 | 5 | The Fourier Transform | `chapters/ch05-fourier.tex` | Volume 8, Chapter 18 |
| 7 | 6 | Distributions and Sobolev Spaces | `chapters/ch06-distributions.tex` | Volume 8, Chapter 19 |
| 7 | 7 | Fourier Analysis on Finite Abelian Groups | `chapters/ch07-finite.tex` | Volume 8, Chapter 20 |
| 7 | 8 | Haar Measure, Duality and the \texorpdfstring{$p$}{p}-adic Numbers | `chapters/ch08-haar.tex` | Volume 8, Chapter 21 |
| 7 | 9 | Curves, Growth and Conformal Maps | `chapters/ch09-complex.tex` | split or dropped from the edition (see the note list) |
| 7 | 10 | Tauberian Theorems | `chapters/ch10-tauberian.tex` | Volume 8, Chapter 23 |
| 7 | 11 | Harder problems | `chapters/ch11-harder.tex` | Volume 8, Chapter 24 |
| 8 | 1 | Smooth Manifolds | `chapters/ch01-manifolds.tex` | Volume 9, Chapter 1 |
| 8 | 2 | Vector Fields and Flows | `chapters/ch02-flows.tex` | Volume 9, Chapter 2 |
| 8 | 3 | Differential Forms and Stokes' Theorem | `chapters/ch03-forms.tex` | Volume 9, Chapter 3 |
| 8 | 4 | Curvature | `chapters/ch04-curvature.tex` | Volume 9, Chapter 4 |
| 8 | 5 | The Fundamental Group and Coverings | `chapters/ch05-coverings.tex` | Volume 9, Chapter 5 |
| 8 | 6 | Homology | `chapters/ch06-homology.tex` | Volume 9, Chapter 6 |
| 8 | 7 | Matrix Lie Groups | `chapters/ch07-liegroups.tex` | Volume 9, Chapter 7 |
| 8 | 8 | Haar Measure and Weyl Integration | `chapters/ch08-haar.tex` | Volume 9, Chapter 8 |
| 8 | 9 | The Hyperbolic Plane and the Modular Group | `chapters/ch09-hyperbolic.tex` | Volume 9, Chapter 9 |
| 8 | 10 | Integral Geometry | `chapters/ch10-integral.tex` | Volume 9, Chapter 11 |
| 8 | A | Euclid Revisited | `chapters/geometry-ch01-euclid.tex` | Volume 9, Chapter B |
| 8 | B | Transformations | `chapters/geometry-ch02-transformations.tex` | Volume 9, Chapter A |
| 8 | C | Inversion | `chapters/geometry-ch03-inversion.tex` | Volume 9, Chapter B |
| 8 | D | Projective geometry | `chapters/geometry-ch04-projective.tex` | Volume 9, Chapter C |
| 8 | E | Conics | `chapters/geometry-ch05-conics.tex` | Volume 9, Chapter D |
| 8 | F | Quadratic forms and quadrics | `chapters/geometry-ch06-quadrics.tex` | Volume 9, Chapter E |
| 8 | G | Plane curves | `chapters/geometry-ch07-curves.tex` | Volume 9, Chapter F |
| 8 | H | Cubic curves | `chapters/geometry-ch08-cubics.tex` | Volume 9, Chapter G |
| 8 | I | Lattices and sphere packings | `chapters/geometry-ch09-lattices.tex` | Volume 9, Chapter H |
| 8 | J | Non-Euclidean geometry | `chapters/geometry-ch10-noneuclid.tex` | Volume 9, Chapter I |
| 8 | K | Convex bodies | `chapters/geometry-ch11-convex.tex` | Volume 9, Chapter J |
| 8 | L | Curvature | `chapters/geometry-ch12-curvature.tex` | Volume 9, Chapter K |
| 9 | 1 | Categories | `chapters/ch01-categories.tex` | Volume 10, Chapter 1 |
| 9 | 2 | Tensors and Exactness | `chapters/ch02-tensors.tex` | Volume 10, Chapter 3 |
| 9 | 3 | Noetherian Rings and Hilbert's Theorems | `chapters/ch03-noetherian.tex` | Volume 10, Chapter 4 |
| 9 | 4 | Localisation and Dimension | `chapters/ch04-localisation.tex` | Volume 10, Chapter 5 |
| 9 | 5 | Dedekind Domains | `chapters/ch05-dedekind.tex` | Volume 10, Chapter 6 |
| 9 | 6 | Homological Algebra | `chapters/ch06-homological.tex` | Volume 10, Chapter 7 |
| 9 | 7 | Group Cohomology | `chapters/ch07-groupcoh.tex` | Volume 10, Chapter 8 |
| 9 | 8 | Semisimple Algebras and Induction | `chapters/ch08-semisimple.tex` | Volume 10, Chapter 9 |
| 9 | 9 | The Symmetric Group | `chapters/ch09-symmetric.tex` | Volume 10, Chapter 10 |
| 9 | 10 | Shuffling Cards | `chapters/ch10-shuffling.tex` | Volume 11, Chapter 14 |
| 9 | 11 | Compact Groups | `chapters/ch11-compact.tex` | Volume 10, Chapter 11 |
| 10 | 1 | Independence and Zero--One Laws | `chapters/ch01-zero-one.tex` | Volume 11, Chapter 1 |
| 10 | 2 | Laws of Large Numbers | `chapters/ch02-lln.tex` | Volume 11, Chapter 2 |
| 10 | 3 | Weak Convergence and Donsker's Theorem | `chapters/ch03-donsker.tex` | Volume 11, Chapter 3 |
| 10 | 4 | The Central Limit Theorem, Sharpened | `chapters/ch04-clt.tex` | Volume 11, Chapter 4 |
| 10 | 5 | Infinitely Divisible and Stable Laws | `chapters/ch05-stable.tex` | Volume 11, Chapter 5 |
| 10 | 6 | Stein's Method | `chapters/ch06-stein.tex` | Volume 11, Chapter 6 |
| 10 | 7 | Large Deviations | `chapters/ch07-ldp.tex` | Volume 11, Chapter 7 |
| 10 | 8 | Concentration of Measure | `chapters/ch08-concentration.tex` | Volume 11, Chapter 8 |
| 10 | 9 | Martingales II: Closing the Circle | `chapters/ch09-martingales.tex` | Volume 11, Chapter 9 |
| 10 | 10 | Ergodic Theory | `chapters/ch10-ergodic.tex` | Volume 11, Chapter 10 |
| 10 | 11 | Mod-\texorpdfstring{$\varphi$}{phi} Convergence | `chapters/ch11-modphi.tex` | Volume 11, Chapter 11 |
| 10 | 12 | Random Permutations and the Poisson--Dirichlet Law | `chapters/ch12-permutations.tex` | Volume 11, Chapter 12 |
| 10 | 13 | Harder problems | `chapters/ch13-harder.tex` | Volume 11, Chapter 13 |
| 11 | 1 | Gaussian Processes and the Birth of Brownian Motion | `chapters/ch01-gaussian.tex` | Volume 12, Chapter 1 |
| 11 | 2 | The Fine Structure of a Brownian Path | `chapters/ch02-paths.tex` | Volume 12, Chapter 2 |
| 11 | 3 | Continuous Martingales | `chapters/ch03-martingales.tex` | Volume 12, Chapter 3 |
| 11 | 4 | The It\^o Integral | `chapters/ch04-ito.tex` | Volume 12, Chapter 4 |
| 11 | 5 | Brownian Motion and Analysis | `chapters/ch05-analysis.tex` | Volume 12, Chapter 5 |
| 11 | 6 | Stochastic Differential Equations | `chapters/ch06-sde.tex` | Volume 12, Chapter 6 |
| 11 | 7 | Markov Processes and L\'evy Processes | `chapters/ch07-levy.tex` | Volume 12, Chapter 7 |
| 11 | 8 | Random Walks on Networks and Groups | `chapters/ch08-networks.tex` | Volume 12, Chapter 9 |
| 11 | 9 | Expanders and Ramanujan Graphs | `chapters/ch09-expanders.tex` | Volume 8, Chapter 11 |
| 11 | 10 | Random Matrices I: The Semicircle | `chapters/ch10-semicircle.tex` | Volume 8, Chapter 12 |
| 11 | 11 | Random Matrices II: Unitary Matrices and the Zeros of Zeta | `chapters/ch11-cue.tex` | Volume 8, Chapter 13 |
| 11 | 12 | Log-Correlated Fields and the Largest Values | `chapters/ch12-logcorrelated.tex` | Volume 12, Chapter 8 |
| 11 | A | Spectral Graph Theory | `chapters/spectral.tex` | Volume 12, Appendix A |
| 11 | B | Zeta and Random Matrices | `chapters/moments.tex` | Volume 15, Chapter 9 |
| 12 | 1 | Number Fields and Their Integers | `chapters/ch01-number-fields.tex` | Volume 13, Chapter 3 |
| 12 | 2 | Ideals and the Splitting of Primes | `chapters/ch02-ideals.tex` | Volume 13, Chapter 4 |
| 12 | 3 | The Geometry of Numbers | `chapters/ch03-geometry.tex` | Volume 13, Chapter 5 |
| 12 | 4 | Units | `chapters/ch04-units.tex` | Volume 13, Chapter 6 |
| 12 | 5 | Cyclotomic Fields and Fermat | `chapters/ch05-cyclotomic.tex` | Volume 13, Chapter 7 |
| 12 | 6 | Local Fields | `chapters/ch06-local.tex` | Volume 13, Chapter 9 |
| 12 | 7 | Quadratic Forms and the Local--Global Principle | `chapters/ch07-hasse.tex` | Volume 13, Chapter 10 |
| 12 | 8 | Zeta Functions and Densities | `chapters/ch08-zeta.tex` | Volume 13, Chapter 11 |
| 12 | 9 | Ad\`eles, Id\`eles and Tate's Thesis | `chapters/ch09-tate.tex` | Volume 13, Chapter 12 |
| 12 | 10 | Class Field Theory | `chapters/ch10-cft.tex` | Volume 13, Chapter 13 |
| 12 | 11 | Algebraic Curves | `chapters/ch11-curves.tex` | Volume 13, Chapter 14 |
| 12 | 12 | Elliptic Curves | `chapters/ch12-elliptic.tex` | Volume 13, Chapter 15 |
| 12 | 13 | Curves over Finite Fields | `chapters/ch13-finite.tex` | Volume 13, Chapter 16 |
| 12 | 14 | Modular Forms and $L$-functions | `chapters/ch14-modular.tex` | Volume 13, Chapter 17 |
| 13 | 1 | Zeros and Primes in Short Intervals | `chapters/ch01-zeros.tex` | Volume 14, Chapter 1 |
| 13 | 2 | Siegel's Theorem | `chapters/ch02-siegel.tex` | Volume 14, Chapter 2 |
| 13 | 3 | Sieves and the Parity Problem | `chapters/ch03-sieves.tex` | Volume 14, Chapter 3 |
| 13 | 4 | The Large Sieve and Bombieri--Vinogradov | `chapters/ch04-largesieve.tex` | Volume 14, Chapter 4 |
| 13 | 5 | Exponential Sums over Primes | `chapters/ch05-expsums.tex` | Volume 14, Chapter 5 |
| 13 | 6 | The Circle Method I: Partitions | `chapters/ch06-partitions.tex` | Volume 5, Chapter 4 |
| 13 | 7 | The Circle Method II: Three Primes and Waring's Problem | `chapters/ch07-waring.tex` | split or dropped from the edition (see the note list) |
| 13 | 8 | Small Gaps between Primes | `chapters/ch08-gpy.tex` | Volume 14, Chapter 7 |
| 13 | 9 | Bounded Gaps between Primes | `chapters/ch09-maynard.tex` | Volume 14, Chapter 8 |
| 13 | 10 | Multiplicative Functions | `chapters/ch10-halasz.tex` | Volume 14, Chapter 9 |
| 13 | 11 | Additive Combinatorics | `chapters/ch11-additive.tex` | Volume 14, Chapter 10 |
| 13 | 12 | Roth's Theorem | `chapters/ch12-roth.tex` | Volume 14, Chapter 11 |
| 13 | 13 | Gowers Norms and the Green--Tao Theorem | `chapters/ch13-gowers.tex` | Volume 14, Chapter 12 |
| 13 | 14 | The Critical Line | `chapters/ch14-critical.tex` | Volume 14, Chapter 13 |
| 14 | 1 | Order and chance in the integers | `chapters/ch01-integers.tex` | Volume 15, Chapter 1 |
| 14 | 2 | Models of the primes | `chapters/ch02-cramer.tex` | Volume 15, Chapter 2 |
| 14 | 3 | Independent prime divisors | `chapters/ch03-divisors.tex` | Volume 15, Chapter 3 |
| 14 | 4 | Random multiplicative functions | `chapters/ch04-multiplicative.tex` | Volume 15, Chapter 4 |
| 14 | 5 | Primes in short intervals | `chapters/ch05-short.tex` | Volume 15, Chapter 5 |
| 14 | 6 | Sieves as probability | `chapters/ch06-sieves.tex` | Volume 15, Chapter 6 |
| 14 | 7 | Random groups in arithmetic | `chapters/ch07-classgroups.tex` | Volume 15, Chapter 7 |
| 14 | 8 | Ranks of elliptic curves | `chapters/ch08-ranks.tex` | Volume 15, Chapter 8 |
| 14 | 9 | Random matrices and the zeros of zeta | `chapters/ch09-gue.tex` | Volume 15, Chapter 9 |
| 14 | 10 | Moments of \texorpdfstring{$L$}{L}-functions | `chapters/ch10-moments.tex` | Volume 15, Chapter 10 |
| 14 | 11 | Value distribution | `chapters/ch11-values.tex` | Volume 15, Chapter 11 |
| 14 | 12 | Pseudorandomness | `chapters/ch12-pseudorandom.tex` | Volume 15, Chapter 12 |
| 14 | 13 | When order wins | `chapters/ch13-bias.tex` | Volume 15, Chapter 13 |
| 14 | 14 | How Research Works | `chapters/ch01-research.tex` | split or dropped from the edition (see the note list) |
| 14 | 15 | How to Read a Paper | `chapters/ch02-reading.tex` | split or dropped from the edition (see the note list) |
| 14 | 16 | Reading a Classic: Shuffling Cards | `chapters/ch03-shuffling.tex` | Volume 11, Chapter 14 |
| 14 | 17 | Guided Reading: Selberg's Theorem at Many Points | `chapters/ch04-selberg.tex` | Volume 12, Chapter 8 |
| 14 | 18 | Guided Reading: Random Groups | `chapters/ch05-sandpiles.tex` | Volume 15, Chapter 7 |
| 14 | 19 | Guided Reading: Better Than Square Root | `chapters/ch06-chaos.tex` | Volume 12, Chapter 8 |
| 14 | 20 | From Data to Conjecture | `chapters/ch07-experiments.tex` | split or dropped from the edition (see the note list) |
| 14 | 21 | Heuristics That Predict | `chapters/ch08-heuristics.tex` | Volume 13, Chapter 18 |
| 14 | 22 | Proofs a Computer Can Check | `chapters/ch09-lean.tex` | split or dropped from the edition (see the note list) |
| 14 | 23 | Writing It Down | `chapters/ch10-writing.tex` | Volume 7, Chapter 6 |
| 14 | 24 | Problems to Work On | `chapters/ch11-problems.tex` | split or dropped from the edition (see the note list) |
| 14 | 25 | Five Projects | `chapters/ch12-projects.tex` | Volume 15, Chapter 14 |
| 14 | A | How Conjectures Are Born and Die | `chapters/conjectures-ch01-born.tex` | Volume 5, Chapter 6 |
| 14 | B | Twin Primes and Prime Gaps | `chapters/conjectures-ch02-twins.tex` | split or dropped from the edition (see the note list) |
| 14 | C | Goldbach | `chapters/conjectures-ch03-goldbach.tex` | split or dropped from the edition (see the note list) |
| 14 | D | The Riemann Hypothesis | `chapters/conjectures-ch04-riemann.tex` | split or dropped from the edition (see the note list) |
| 14 | E | Random Matrices and the Zeta Function | `chapters/conjectures-ch05-zetarmt.tex` | split or dropped from the edition (see the note list) |
| 14 | F | Collatz | `chapters/conjectures-ch06-collatz.tex` | split or dropped from the edition (see the note list) |
| 14 | G | Hadamard Matrices | `chapters/conjectures-ch07-hadamard.tex` | Volume 3, Chapter 13 |
| 14 | H | Points, Distances and Families of Sets | `chapters/conjectures-ch08-geometric.tex` | Volume 4, Chapter 4 |
| 14 | I | The abc Conjecture | `chapters/conjectures-ch09-abc.tex` | Volume 13, Chapter 18 |
| 14 | J | Birch and Swinnerton-Dyer | `chapters/conjectures-ch10-bsd.tex` | split or dropped from the edition (see the note list) |
| 14 | K | Randomness in the Integers | `chapters/conjectures-ch11-random.tex` | split or dropped from the edition (see the note list) |
| 14 | L | Open Doors in Algebra | `chapters/conjectures-ch12-algebra.tex` | split or dropped from the edition (see the note list) |

## Chapters that moved

These are the moves in pull requests 30–39. A citation of the old chapter follows the file, or the theorem's label when the file was split.

| From | Chapter | To |
| --- | --- | --- |
| 2 The Integers (old 1) | Quadratic fields; ideals and class groups; the p-adic field | 13 Arithmetic |
| 3 Symmetry (old 2) | Spectral theorem, SVD, graph spectra, matrix inequalities, linear dynamics | 8 Analysis |
| 3 Symmetry (old 2) | Tensors | 10 Abstraction |
| 4 Chance (old 3) | Orders (appendix) | 1 First Principles, Chapter 4 |
| 8 Analysis (old 7) | Jordan curve theorem | 7 Spaces |
| 8 Analysis (old 7) | Riemann mapping theorem | 9 Shapes |
| 10 Abstraction (old 9) | Shuffle cutoff | 11 Randomness |
| 12 Random Motion (old 11) | Expanders, semicircle, sine kernel | 8 Analysis |
| 14 The Primes (old 13) | Partitions (circle method) | 5 Calculation |
| 14 The Primes (old 13) | Waring's problem (split from three primes) | 5 Calculation |
| 14 The Primes (old 13) | Three primes (split from Waring) | 14 The Primes |

Gaussian and Eisenstein integers stayed in Volume 2. Perron–Frobenius and the symmetry that diagonalises stayed in Volume 3. Haar measure stayed in Volume 8. Dyson Brownian motion stayed in Volume 12. Three primes stayed in Volume 14.

## Volume 0, original chapter to Volume 1 now

| Original chapter | Lands now |
| --- | --- |
| 1 | Volume 1, Chapter 1 |
| 2 | Volume 1, Chapter 5 |
| 3 | Volume 1, Chapter 6 |
| 4 | Volume 1, Chapter 9 |
| 5 | Volume 1, Chapter 3 |
| 6 | Volume 1, Chapter 8 |
| 7 | Volume 1, Chapter 7 |
| 8 | Volume 1, Chapter 10 |

## Citations read by hand

The pass left these because one phrase named two homes, or the appendix letter was not a chapter of that book. Each one was then read against the sentence.

| Place | Decision |
| --- | --- |
| `volume2-integers` reciprocity tools | Cyclic units and reciprocity stay in Volume 2, Chapters 4 and 5. The \(p\)-adic squares are Volume 13, Chapter 8. |
| `volume2-integers` characters tools | \(\mathbb Z[\omega]\) stays in Volume 2, Chapter 10. The quadratic integers are Volume 13, Chapter 1. |
| `volume4-chance` `ch12-method.tex` | Adjacency eigenvalues are Volume 8, Chapter 9. Ramanujan graphs are Volume 8, Chapter 11. The matrix-tree theorem is Volume 12, Appendix A. Stirling's formula is Volume 1, Exercise 3.7. Jensen's inequality is Volume 1, Theorem 9.2. The Collatz appendix is not in the printed series; the sentence keeps the open question and drops the pointer. |
| `volume8-analysis` `linear-ch08-graphs.tex` | Cheeger is Chapter 10 of that book, expanders and Ramanujan graphs are Chapter 11, and the matrix-tree theorem is Volume 12, Appendix A. |
| `volume8-analysis` `linear-ch11-inequalities.tex` | The order-\(668\) account is not a printed chapter. Volume 3, Chapter 13, builds the known Hadamard matrices. |
| `volume9-shapes` forms, curvature, coverings | The continuous argument is Volume 7, Lemma 6.1, in the Jordan chapter. |
| `volume9-shapes` `ch01-manifolds.tex` and the unused algebra conjectures file | The complex logarithm is Volume 8, Chapter 22. |
| `volume9-shapes` `ch10-integral.tex` | Buffon–Barbier is Volume 9, Appendix J, and Cauchy's formula for the perimeter is Theorem J.5 of that appendix. |
| `volume9-shapes` `ch09-hyperbolic.tex` | The half-plane model is Volume 9, Appendix I, not the integral-geometry chapter that now carries the old number 10. |
| `volume12-random-motion` `moments.tex` | The twin-prime appendix is not printed. The problem is taken up in Volume 6 and again in Volume 14. |

Three further sentences were inconsistent inside a paragraph that a later edit had only partly renumbered. Conditional expectation in the Volume 11 martingale reminder is Volume 4, and the tower property is Volume 7, Theorem 11.17. The adjacency spectra in the Volume 12 spectral chapter are Volume 8, Chapter 9. Fourier analysis in the Volume 13 Tate reminder is Volume 5, Chapter 10, and Carathéodory's extension theorem is Volume 7, Theorem 7.10.

Volume 4 has a single appendix, the extremal chapter, so Ramsey citations of the old Appendix B are Appendix A. Mordell's theorem is Volume 13, Chapter 15. A later pass checked every `Volume~N` followed by a chapter, theorem, proposition, lemma, corollary, exercise or appendix number. The number was kept only when that item exists in the named volume and its label or title is the statement the sentence describes. Parenthetical locators and the later numbers in a list had often kept the pre-insertion number after the volume was updated; those now point at the current home of the same label. Volume 12 has no Chapter 10: the matrix-tree theorem is Appendix A.

No citation was left on an old volume number. `Volume~0` does not remain in Volumes 2–15.

