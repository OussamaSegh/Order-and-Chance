# Chapter 2 separate source review

A reviewer who did not write Chapter 2 read the entire replacement in a separate
phase: every sentence, all 14 original numbered formal statements against their
immutable baseline text, all proofs and calculations, the 12 original plus four
new exercises, their hints and complete idea/writeup solutions, and all four
figure sources/blocks. This is a **source-only** mathematical and editorial
review. Parent owns builds, rendered pages, media and final publication checks.

The 26 original formal/exercise comparisons, their baseline printed numbers and
exact block hashes, and all four new exercise judgments are in
`ch02-statements.json`.

## Review findings resolved

The first replacement of `linear:ex:waring` unnecessarily restricted the field to
R or C. Separate review found the displayed tensor identity is valid over every
field of characteristic different from two, including characteristic three.
The polynomial identity itself holds in every field. Parent corrected the task,
hint and solution in commit `ee5c8ac6`: compare tensor entries directly; the three-
distinct patterns have signed coefficient four and repeated-index patterns zero.
This retains characteristic three without relying on injectivity of the cubic-
polynomial correspondence, which fails there. Characteristic two is explicitly
excluded only from division by four in this particular tensor decomposition.
The final clarification distinguishing characteristics two and three was re-read.
No unresolved source finding remains for this chapter.

## Baseline statement/content review

- Kronecker rules retain every trace/determinant/rank/eigenvalue conclusion.
  Schur triangularisation handles defective matrices. The corrected rectangular
  SVD proof uses distinct row/column pairs and independent permutations; the
  product need not already be lexicographically diagonal.
- Column vectorisation gives B-transpose tensor A, without conjugation, and
  Sylvester's iff condition is proved for every right-hand side. Empty matrices
  and zero tensors are handled without inventing eigenvalues or positive rank.
- The slice test works over every field with invertible first slice. Both its
  directions and the explicit real-rank-three/complex-rank-two example were
  checked by reconstructing both slices.
- The W rank-three proof remains valid in every characteristic. Convergence and
  border rank now specify R/C with ordinary entry topology; the rank obstruction
  is a proof, not a numerical observation. A rank-two flattening gives the lower
  border-rank obstruction, so no missing rank-one limit case remains.
- Tensor/algorithm equivalence has correct third-index reversal for trace(ABC)
  and both directions preserve bilinear length. Strassen's four output equations
  were expanded without commuting input factors. Its formulas remain valid for
  noncommutative blocks and in characteristic two.
- The exponent theorem retains r>k² and explicitly supplies integer k>=2, making
  log_k meaningful. Its geometric recurrence and zero-padding argument prove the
  stated bound, including sizes not powers of k. Later exponent records and
  optimality bounds remain quoted, not premises.
- The Schmidt proof uses conjugation of the second singular-vector family, so
  coefficient matrices correspond to ab-transpose rather than ab-adjoint. All
  original rank, positivity, orthonormality and norm conclusions are preserved.
- Entropy's previously incomplete equality case is repaired: the number of
  nonzero coefficients must equal the smaller ambient dimension, and then all
  squared coefficients must be equal. The local log inequality proves both bound
  and exact equality. A Bell vector embedded in dimension at least three shows
  why equal nonzero coefficients alone do not suffice.

## Exercise completeness

Every original star rating and task remains, subject to explicit corrections
listed below, with an effective hint and complete idea/writeup solution. Each
exercise has its individual judgment in the JSON.

- The no-approximation exercise originally claimed both pure summands have norm
  1/epsilon. The first norm is actually (1+epsilon²)^(3/2)/epsilon for positive
  epsilon, and the second is 1/epsilon; the corrected solution proves these and
  the bounded sum norm²=3+3epsilon²+epsilon⁴.
- Full Strassen cost crossover is proved for all powers of two, using a monotone
  normalized difference and exact signs; two numerical sizes alone are not used
  to establish the persistent threshold 1024.
- The Schmidt exercise now gives actual normalized vectors, with the negative
  eigenvalue sign absorbed into the second factor, as the original task asks.
- The grid solution gives the requested exact rectangular spectral condition
  number, with square asymptotic and 1×1 case, not only a square-grid estimate.
- The border-rank solution supplies a two-stage sequence approximating arbitrary
  first slices, so no density-to-sequence step is left implicit.

The four new exercises have substantive proofs: overlapping-spectrum Sylvester
compatibility and eigenspace obstruction; a real open-set obstruction to border
rank two; the three real quadratic-algebra cases; and entropy equality/purity in
larger dimensions. All are solvable from earlier material and this chapter.
Their hints, stars and solutions were read separately. No new solution depends on
a later exercise. The Sylvester shear is already proved directly earlier, so its
reference to the original exercise does not introduce a missing premise.

## Prerequisites actually checked

Read Volume 8's actual `main.tex`, confirming that its chapters and appendices are
all earlier in the series. Read the cited statements/proofs for Schur C.2
(`linear-ch03-eigen.tex`), SVD 4.1 and Eckart–Young 4.5
(`linear-ch06-svd.tex`), path Exercise 3.3 and solution
(`linear-ch05-spectral.tex`), hypercube Exercise 5.1 and solution
(`linear-ch08-graphs.tex`), and Lyapunov F.5
(`linear-ch12-dynamics.tex`). The current statement walker confirms those printed
numbers. Actual path and cube solutions provide the eigenvectors/multiplicities
used here. No Volume 11–15 result is a premise. Complex norm/topology facts come
from earlier analysis; finite-field tensor computations remain algebraic.

## Figures and prose

Original W and omega blocks are byte-for-byte preserved and their sources keep
baseline hashes. New figures occur after both original figures, preserving the
original figure sequence. Vectorisation labels stack x11,x21,x12,x22,x13,x23,
matching the definition and caption. Recursion has seven child blocks at n/2,
7^s scalar products, and the correct 18·7^j(n/2^(j+1))² addition cost. Shared palette,
line weights and labels are used; actual rendered sizing is parent's gate.

All exposition was read, including short formula lead-ins, the limit discussion,
field assumptions, equality clauses, practical operation-count caveats and the
chapter bridge. Strassen's literal opening quotation and bibliography are intact.
The new prose explains the steps with concrete arrays and calculations. No
remaining source-level editorial blocker was found.

## Commands actually run

With the repository Python environment activated,
`python3 review/volume10-rewrite/check_ch02_kronecker.py` exited 0. Its illustration
checks cover the displayed Strassen identities, rank decompositions, operation
counts, Schmidt numbers, entropy and grid spectrum. A separate exact 27-entry
calculation of the Waring tensor identity in characteristics 3, 5 and 7 returned
true in every case. These checks support the direct coefficient proof, not replace
it. The source walk checks every original label/figure hash/block and original
formal-environment sequence, and records 4 figures, 16 exercises, 16 hints and
16 solutions. No PDF/full build was run by this reviewer.
