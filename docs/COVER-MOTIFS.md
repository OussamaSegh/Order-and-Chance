# Mathematical meaning of every cover illustration

The author's requirement (27 October 2026): **the illustration must be meaningful
to the content of its book**. Use the attached visual reference's paper, type and
border, but derive each plate from the mathematics. Do not copy its generic circles
onto every volume. All diagrams are computed TikZ vectors; `tools/cover_motifs.py`
contains the constructions and `<volume>/cover-motif.tex` the generated result.

| Volume | Illustration and mathematical connection |
|---|---|
| 0 Back in Shape | Chords joining j to 2j modulo 200: roots of unity, modular arithmetic and complex geometry from the refresher. |
| 1 The Integers | Sacks spiral: plot each prime p at radius sqrt(p), angle 2π sqrt(p). A genuine picture of the primes, central to Chapter 2. |
| 2 Structures | Truncated icosahedron / Cayley graph of A5, connecting symmetry, groups and actions. |
| 3 Chance | A Galton board: coin-flip paths and the binomial distribution approaching a Gaussian. |
| 4 The Art of Calculation | Fourier partial sums of a square wave, showing Gibbs overshoot; Fourier series and summation methods. |
| 5 Where It All Meets | The complex curve ζ(1/2+it), illustrating the connection between analysis, zeta zeros and prime distribution. |
| 6 Spaces | Sierpiński carpet: a set of Hausdorff dimension log(8)/log(3), connecting topology and metric measures. |
| 7 Analysis in Depth | Image of a rectangular grid under sin(z), yielding confocal ellipses/hyperbolas: conformal mapping and complex analysis. |
| 8 Shapes | Farey tessellation of the hyperbolic disc: geodesics, modular group and continued fractions. |
| 9 Structures II | A Plancherel-distributed Young diagram and its limit shape: symmetric-group representations. |
| 10 Chance II | GEM(1) stick-breaking samples: the Poisson–Dirichlet laws studied with permutation cycles. |
| 11 Random Motion | Dyson Brownian eigenvalue trajectories: stochastic motion and random-matrix repulsion. |
| 12 Arithmetic | Ford circles with exact radii 1/(2q²) over reduced rationals p/q: modular geometry behind the modular-forms chapter. |
| 13 Primes in Depth | Prime residue constellations: arithmetic progressions and the distribution of primes. |
| 14 Random Arithmetic | Partial-sum walks of Steinhaus random multiplicative functions: probabilistic models of arithmetic functions. |
| 15 The Research Workshop | Binary branching random walk and its barrier: the guided reading on multiplicative chaos and random multiplicative functions. |
| C1 Discrete Structures | Boolean lattice of subsets of a five-element set, with symmetric chains: orders and combinatorics. |
| C2 Algorithms | Batcher bitonic sorting network on 16 wires: comparison networks and algorithm design. |
| C3 Computation and Complexity | Three-state binary divisibility-by-3 automaton: finite-state computation from Chapter 1. |
| C4 Information, Codes and Secrets | Binary entropy h(p) and binary symmetric channel capacity 1-h(p), from Chapters 1 and 3. |
| C5 Data, Optimisation and Learning | Level sets of a positive quadratic, steepest-descent iterates and the exact two-step conjugate-gradient solution, from Chapter 2. |
| S1 Linear Algebra in Depth | Random lozenge tiling, connected to nonintersecting paths and determinants, an application highlighted in the preface. |
| S2 Geometry | Integral Apollonian gasket: mutually tangent circles and their integer curvatures. |
| S3 A Book of Conjectures | Collatz orbit tree: finite computed orbits illustrating the open iteration problem. |
| S4 The Companion | Chord diagram of actual cross-volume citations: the map of the series itself. |
| P1 Crossroads | Gaussian primes a+bi in a bounded disc: number theory, complex geometry and algebra crossing subjects. |
| P2 Machinery | First 89 iterates of an irrational rotation by (√5−1)/2: equidistribution and Kronecker's theorem in Chapters 1–2. |
| P3 Frontiers | Standardized binomial probability masses for n=8,32,128 with the Gaussian reference: local limit theorems for sums of random pieces in Chapter 1. |

C4, C5, P2 and P3 were revised during this design session to tie their plates to
material already included in their manuscripts, rather than later planned topics.
The conjugate-gradient generator checks that the two-dimensional iterate reaches
the minimizer within floating-point error. Binomial heights are exact probabilities
divided by lattice spacing; the normal curve is explicitly an approximation.
Finite experiments, Collatz trees and zeta plots are illustrations, not proofs of
open conjectures. Preserve their parameters and meaning when changing presentation.
