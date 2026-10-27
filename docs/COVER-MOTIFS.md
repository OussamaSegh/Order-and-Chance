# Mathematical cover illustrations

All 28 illustrations use the approved black/gold vector style. Each cover has one
main plate and one smaller supporting construction tied to its own mathematics.
The table identifies the main subject and manuscript evidence; the generator
records exact parameters and seeds. Finite simulations illustrate mathematics;
they are not proofs of open conjectures.

| Volume | New illustration | Manuscript evidence |
|---|---|---|
| 0: Mathematical Maturity | Gaussian wireframe surface | ch06-integrals-taylor.tex; ch08-counting-probability.tex |
| 1: The Integers | Lattice circle and 3–4–5 triangle | ch07-sums-of-squares.tex |
| 2: Structures | Truncated icosahedron, rotations and A5 | ch11-characters.tex; ch12-quaternions.tex |
| 3: Chance | Binomial board and Gaussian approximation | ch02-discrete.tex; ch06-clt.tex |
| 4: The Art of Calculation | Fourier partial sums and Gibbs overshoot | ch06-fourier.tex |
| 5: Where It All Meets | Critical-line zeta curve | ch06-zeros.tex |
| 6: Spaces | Sierpinski carpet and Cantor construction | ch11-metricmeasures.tex |
| 7: Analysis in Depth | Image of an orthogonal grid under sin(z) | ch09-complex.tex |
| 8: Shapes | Farey tessellation of the hyperbolic disk | ch09-hyperbolic.tex |
| 9: Higher Structures | Young diagram and Plancherel limit shape | ch09-symmetric.tex |
| 10: Chance II | GEM(1) proportional stick-breaking bands | ch12-permutations.tex |
| 11: Random Motion | Hermitian Brownian eigenvalue trajectories | ch10-semicircle.tex |
| 12: Arithmetic | Ford circles over reduced rationals | ch14-modular.tex; ch12-elliptic.tex |
| 13: Primes in Depth | Prime residues, twins and constellations | Prime distribution and progressions |
| 14: Random Arithmetic | Steinhaus multiplicative partial-sum walks | ch05-randommult.tex |
| 15: The Research Workshop | Branching random walk and critical barrier | ch06-chaos.tex |
| P1: Crossroads | Gaussian primes in a bounded integer lattice | Gaussian integers and number theory |
| P2: Machinery | Golden-ratio rotation and equidistribution | ch01-almost.tex; ch02-hilbert.tex |
| P3: Frontiers | Exact scaled binomial masses and Gaussian limit | ch01-pieces.tex |

Generate both plate files with `python3 tools/cover_plates.py`. The machine-readable
manifest is [cover-art-manifest.json](cover-art-manifest.json).

Geometry checks include the exact 3–4–5 identity, sorted Hermitian eigenvalues,
the two-step conjugate-gradient solution, exact binomial masses and rational Ford
circle radii. Steinhaus samples now use one uniform angle for both sine and cosine;
this fixes the old nonuniform angle construction. Lozenge tilings are finite
Glauber-dynamics samples; no claim of exact stationarity is made.
