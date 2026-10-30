# Series structure

The series is fifteen volumes, numbered 1 through 15, in six parts. There is no separate problem book. Under the name Order and Chance, the series subtitle is *The Hidden Architecture of Mathematics*. The source of the titles, subtitles and part grouping is `common/series-catalog.json`. `tools/series_metadata.py` writes `common/volume-subtitles.json`, `common/volume-subtitles.tex` and `common/series.tex` from it.

## Series parts

| Part | Volumes |
| --- | --- |
| I. Foundations | 1 First Principles; 2 The Integers; 3 Symmetry; 4 Chance |
| II. Bridges | 5 Calculation; 6 Crossroads |
| III. Analysis and Geometry | 7 Spaces; 8 Analysis; 9 Shapes; 10 Abstraction |
| IV. Randomness | 11 Randomness; 12 Random Motion |
| V. Number | 13 Arithmetic; 14 The Primes |
| VI. Synthesis | 15 Order and Chance |

## Old number to new number

Chapter text that says “Volume 4” still means the old number. Use this table when those citations are revised. Do not treat the old number as the number printed on the title page.

| Old number and title | New number and title | Directory |
| --- | --- | --- |
| 0 Mathematical Maturity | 1 First Principles | `volume1-first-principles` |
| 1 The Integers | 2 The Integers | `volume2-integers` |
| 2 Structures | 3 Symmetry | `volume3-symmetry` |
| 3 Chance | 4 Chance | `volume4-chance` |
| 4 The Art of Calculation | 5 Calculation | `volume5-calculation` |
| 5 Where It All Meets | 6 Crossroads | `volume6-crossroads` |
| 6 Spaces | 7 Spaces | `volume7-spaces` |
| 7 Analysis in Depth | 8 Analysis | `volume8-analysis` |
| 8 Shapes | 9 Shapes | `volume9-shapes` |
| 9 Higher Structures | 10 Abstraction | `volume10-abstraction` |
| 10 Chance II | 11 Randomness | `volume11-randomness` |
| 11 Random Motion | 12 Random Motion | `volume12-random-motion` |
| 12 Arithmetic | 13 Arithmetic | `volume13-arithmetic` |
| 13 Primes in Depth | 14 The Primes | `volume14-primes` |
| 14 Order and Chance | 15 Order and Chance | `volume15-order-and-chance` |
| Problem book Crossroads | exercises in Volumes 1–6 | removed |

Notebook folders follow the new numbers: `python/volume1` through `python/volume15`.

## Parts inside each volume

A few part names were adjusted so the part matches the chapters that actually sit there.

| Volume | Part | Chapters |
| --- | --- | --- |
| 1 First Principles | The Language of Proof | Language |
| 1 | Counting and Sums | Sums, counting |
| 1 | Algebra, Limits and Functions | Sequences, complex numbers, polynomials, linear algebra, integrals. The requested name was “Limits and Functions”; algebra is in this block. |
| 1 | Chance and Inequality | Inequalities, probability |
| 2 The Integers | Divisibility | Divisibility |
| 2 | The Primes | Primes |
| 2 | Congruences | Congruences, primitive roots, quadratic reciprocity, arithmetic functions |
| 2 | Equations and Characters | Sums of squares, continued fractions, Diophantine equations, the Gaussian and Eisenstein integers, one section on the failure of unique factorisation, and the characters chapter. |
| 3 Symmetry | Groups | Groups through Sylow |
| 3 | Rings and Polynomials | Rings, modules, extensions |
| 3 | Fields and Galois Theory | Finite fields, Galois theory, characters, quaternions, then the linear-algebra and combinatorics appendices |
| 4 Chance | Discrete Probability | Counting, discrete laws, generating functions, inequalities |
| 4 | Limit Theorems | Continuous distributions, the central limit theorem |
| 4 | Random Structures | Walks through the probabilistic method, then the combinatorics appendices. Martingales and Brownian motion stay here because they follow the walks. |
| 5 Calculation | Series and Products | Finite differences, generating functions, series, the Hardy–Ramanujan formula, and Waring's problem for large s |
| 5 | Integrals and Transforms | Integrals through complex analysis. The requested name was “Integrals and Asymptotics”; Fourier sits in this block, and the asymptotic chapter follows zeta. |
| 5 | The Zeta Function | Zeta, asymptotics, the arithmetic-geometric mean |
| 6 Crossroads | Counting Primes | Mertens through the prime-number theorem |
| 6 | Zeros and Explicit Formulas | Zeros, explicit formulae |
| 6 | Sieves and Randomness | Sieves through modular forms. The modular-forms chapter closes the part. |
| 7 Spaces | Metric and Topological Spaces | Sets through the Baire category theorem, then the Jordan curve theorem. |
| 7 | Measure and Integration | Measures through L^p |
| 7 | Measures on Spaces | Radon measures, metric measure spaces, harder problems |
| 8 Analysis | Banach and Hilbert Spaces | Banach spaces, Hilbert spaces |
| 8 | Spectral Theory | Operators, the spectral theorem |
| 8 | Fourier and Tauberian Methods | Fourier through Tauberian theorems and the harder problems. Haar measure and complex analysis sit in this part. |
| 9 Shapes | Manifolds and Surfaces | Manifolds, flows. The requested name was “Curves and Surfaces”; the book opens with manifolds. |
| 9 | Forms and Homology | Forms, curvature, coverings, homology |
| 9 | Groups and Geometry | Lie groups through the hyperbolic plane, the Riemann mapping theorem and integral geometry, then the geometry appendices. Ceva and the Euler line are exercises on transformations. The curvature appendix is the curvature of curves and polyhedra. |
| 10 Abstraction | Categories | Categories, tensors |
| 10 | Commutative Algebra | Noetherian rings through homological algebra |
| 10 | Representations | Group cohomology through compact groups. The Fourier analysis of the symmetric group stays here. The transposition cutoff is in Volume 11. |
| 11 Randomness | Invariance Principles | Zero–one law through the central limit theorem |
| 11 | Stable Laws | Stable laws, Stein’s method, large deviations, concentration. The requested phrase “Stable Laws and Ergodic Theory” is split because the martingale chapter lies between them. |
| 11 | Martingales and Ergodic Theory | Martingales through sums of random pieces, then the transposition cutoff. |
| 12 Random Motion | Brownian Motion | The Gaussian measure, paths |
| 12 | Stochastic Calculus | Martingales through Lévy processes, then the branching random walk and the largest values of a characteristic polynomial. |
| 12 | Networks | Walks on graphs, resistance, and the matrix-tree theorem, then the Laplacian appendix. Expanders, the semicircle and the sine kernel are in Volume 8. |
| 13 Arithmetic | Number Fields | Number fields through cyclotomic fields |
| 13 | Local and Global | Local fields, the Hasse principle, zeta functions of number fields |
| 13 | Adeles and Tate's Thesis | Tate’s thesis and class field theory |
| 13 | Elliptic Curves and Modular Forms | Curves through modular forms |
| 14 The Primes | Zeros and Sieves | Zeros through exponential sums. The requested name was “Sieves”; the book opens with zeros. |
| 14 | Additive Problems and Bounded Gaps | Three primes and bounded gaps. The part name stays Additive Problems and Bounded Gaps. Partitions and Waring's problem are in Volume 5. |
| 14 | Structure in the Primes | Halász through the critical line |
| 15 Order and Chance | The Question | Order in the integers, models of the primes, independent prime divisors |
| 15 | Arithmetic Statistics | Multiplicative functions through ranks of elliptic curves |
| 15 | Spectra | Random matrices, moments, value distribution |
| 15 | Structure versus Randomness | Pseudorandomness, Chebyshev’s bias |
| 15 | The Research Workshop | A reading method practised on Maier or Selberg, and two projects |

## Where the Crossroads problems went

Each problem kept its label, hint, solution and figures, and was appended to an existing exercise list. The volume is the one in 0–5, under the old numbering, whose tools the solution uses most often. Problems that refer to each other stay in the same volume. The new volume number is the old one plus 1.

# Crossroads placement

## Volume 1, First Principles (volume1-first-principles), formerly Volume 0: 22 problems

- `ch01-sums.tex` (4): pb:millin, pb:erdosheil, pb:sauer, pb:bilinear
- `ch06-integrals-taylor.tex` (3): pb:lightsout, pb:hyperplanes, pb:kakeya
- `ch05-sequences-series.tex` (3): pb:schwartz, pb:nullstellensatz, pb:newton
- `ch09-probability.tex` (8): pb:cauchydav, pb:distances, pb:incidences, pb:szemereditrotter, pb:sumproduct, pb:treebound, pb:parking, pb:sinesecond
- `ch03-polynomials.tex` (2): pb:benford, pb:bellasym
- `ch04-inequalities.tex` (1): pb:stanley
- `ch07-linear-algebra.tex` (1): pb:tanroots

## Volume 2, The Integers (volume2-integers), formerly Volume 1: 41 problems

- `ch03-congruences.tex` (9): pb:primepoly, pb:fpfunctions, pb:aks, pb:wolsten, pb:jacobsthal, pb:morley, pb:glaisher, pb:ramanujan5, pb:kloosterman
- `ch05-primitive-roots.tex` (5): pb:smith, pb:lambert, pb:ramsum, pb:phipm1, pb:gcdmean
- `ch06-quadratic-reciprocity.tex` (8): pb:primsum, pb:phimodp, pb:fermatnum, pb:carmichael, pb:pratt, pb:rabin, pb:waring, pb:squaresmodpk
- `ch04-arithmetic-functions.tex` (4): pb:eisensine, pb:euler, pb:nsq1, pb:sumsquares
- `ch14-characters.tex` (11): pb:pseudo, pb:pocklington, pb:fermatquot, pb:mullin, pb:artin, pb:fermatcubic, pb:euclidgame, pb:pascalthree, pb:powerful, pb:jacobi, pb:densities
- `ch01-divisibility.tex` (4): pb:valuation, pb:parity, pb:fibcoprime, pb:orchard

## Volume 3, Symmetry (volume3-symmetry), formerly Volume 2: 31 problems

- `ch09-finite-fields.tex` (5): pb:fibmodp, pb:pascal2, pb:lucaslehmer, pb:moore, pb:mseq
- `ch12-quaternions.tex` (8): pb:sylvester, pb:jensen, pb:mersennediv, pb:dice, pb:ksubsets, pb:egz, pb:abelian, pb:dodecaturns
- `ch01-groups.tex` (4): pb:matrices2, pb:fibdivides, pb:ruzsa, pb:returnbound
- `ch11-characters.tex` (3): pb:glnz, pb:commutators, pb:frobschur
- `ch03-actions.tex` (6): pb:sieving, pb:patterns, pb:landau, pb:nilpotent, pb:flags, pb:touchard
- `ch07-modules.tex` (1): pb:kronecker
- `ch10-galois.tex` (2): pb:rattan, pb:ramacube
- `ch04-symmetric.tex` (2): pb:discphi, pb:conjugate

## Volume 4, Chance (volume4-chance), formerly Volume 3: 68 problems

- `ch03-generating.tex` (3): pb:sicherman, pb:loaded, pb:subsetsum
- `ch01-counting.tex` (4): pb:whichroot, pb:nouniform, pb:bollobas, pb:granularity
- `ch08-markov.tex` (6): pb:carries, pb:dicemod, pb:hypercubemix, pb:antipode, pb:holte, pb:gilbreath
- `ch05-continuous.tex` (5): pb:laplace, pb:passone, pb:irwinhall, pb:borwein, pb:stick
- `ch12-method.tex` (33): pb:vanish, pb:samecycle, pb:denes, pb:conics, pb:hashing, pb:triangleseigen, pb:walks, pb:littlewoodofford, pb:cubeiso, pb:erdosselfridge, pb:shearer, pb:sincpower, pb:cantor, pb:majoritystable, pb:period, pb:rollingdie, pb:gapdiam, pb:treewalk, pb:commute, pb:foster, pb:rayleigh, pb:aldousbroder, pb:terras, pb:everett, pb:coprimewalk, pb:range, pb:cyclecover, pb:threegamblers, pb:moran, pb:bernoullilaplace, pb:binompowers, pb:saw, pb:inspection
- `ch07-walks.tex` (1): pb:rootwalk
- `ch02-discrete.tex` (8): pb:leastqnr, pb:glfix, pb:foata, pb:paley, pb:goodman, pb:influence, pb:arrow, pb:lcs
- `ch04-inequalities.tex` (5): pb:capset, pb:kac, pb:bonami, pb:kacring, pb:nbonacci
- `ch09-poisson.tex` (2): pb:spacings, pb:dixie
- `ch06-clt.tex` (1): pb:sincsum

## Volume 5, Calculation (volume5-calculation), formerly Volume 4: 82 problems

- `ch03-series.tex` (2): pb:coprime52, pb:levy
- `ch12-agm.tex` (36): pb:cyclewalk, pb:detsquare, pb:hadamard, pb:rank, pb:derangements, pb:noroots, pb:gaussmeasure, pb:digitsclt, pb:kolberg, pb:kummer, pb:pascalfour, pb:centralp, pb:sternfib, pb:thuemorse, pb:hermite, pb:centralsum, pb:lehmer, pb:catalanmoments, pb:apcount, pb:dftspectrum, pb:erdosturan, pb:circlewalk, pb:fejer, pb:bernstein, pb:bernsteinabs, pb:fantaussky, pb:involasym, pb:distinctcycles, pb:ramanujan, pb:mappings, pb:xplusinv, pb:hyperfactorial, pb:banach, pb:primezeta, pb:dickmanint, pb:polymertens
- `ch01-finite.tex` (2): pb:fixmoments, pb:necklacering
- `ch06-fourier.tex` (3): pb:flat, pb:rudin, pb:siegel
- `ch04-integrals.tex` (3): pb:bricks, pb:golomb, pb:sondow
- `ch02-generating.tex` (19): pb:prouhet, pb:phipq, pb:commuting, pb:roots, pb:squares, pb:randpoly, pb:parts123, pb:selfconj, pb:glaisherthm, pb:eulerlog, pb:catalanodd, pb:stern, pb:binarypart, pb:arcsin, pb:quotientlaw, pb:zigzag, pb:poissonise, pb:diehit, pb:flory
- `ch07-fft.tex` (6): pb:midpoint, pb:napoleon, pb:pdn, pb:cdg, pb:newman, pb:bent
- `ch05-gamma.tex` (4): pb:nair, pb:ncycles, pb:dalzell, pb:sophomore
- `ch11-asymptotics.tex` (3): pb:unlabelled, pb:oddcycles, pb:powersum
- `ch09-complex.tex` (2): pb:rankdist, pb:dedekind
- `ch10-zeta.tex` (2): pb:gausskuzmin, pb:sqrtsum

## Volume 6, Crossroads (volume6-crossroads), formerly Volume 5: 56 problems

- `ch05-pnt.tex` (4): pb:gaussprimes, pb:findprime, pb:sidon, pb:nsq1sqfree
- `ch01-mertens.tex` (1): pb:poissoncycles
- `ch12-modular.tex` (39): pb:singer, pb:consecsqfree, pb:pairwise, pb:twosqfree, pb:dsquared, pb:energy, pb:kleitman, pb:chebyshevsum, pb:primitive, pb:divisorbound, pb:logtwo, pb:doubleint, pb:beukerstwo, pb:beukersthree, pb:fracint, pb:primefrac, pb:leastpf, pb:largestpf, pb:factorialdiv, pb:centralbinom, pb:superprimes, pb:ramprimes, pb:pminusone, pb:titchmarsh, pb:menon, pb:omegapoly, pb:rankin, pb:renyi, pb:twosquares, pb:ramanujanE2, pb:landauzeros, pb:hearzeros, pb:cramersign, pb:selberg, pb:schur, pb:euler41, pb:hecke, pb:shifted, pb:romanoff
- `ch02-averages.tex` (6): pb:phiovern, pb:visible, pb:farey, pb:orderedfact, pb:fracmean, pb:radical
- `ch08-sieves.tex` (2): pb:bonferroni, pb:buchstab
- `ch10-random.tex` (2): pb:hawkins, pb:digitpairs
- `ch03-characters.tex` (1): pb:primroot
- `ch11-sums.tex` (1): pb:erdosnp
