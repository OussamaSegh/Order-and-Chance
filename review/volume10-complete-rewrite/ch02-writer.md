# Chapter 2 writer record

The complete chapter has been replaced by a handwritten rewrite: all exposition,
numbered statements, every proof, worked calculation, twelve original exercises,
twelve hints and twelve idea/writeup solutions, and the closing reading bridge.
Strassen's literal opening quotation, bibliographic records and both complete
original figure blocks are unchanged. The section count and all original labels
are preserved. This is a writer's mathematical/editorial pass, not a claim of
independent second-reader certification.

## Additions

Exactly two mathematical figures follow the last original figure: column
vectorisation for a 2×3 matrix, and the seven-branch Strassen recursion with the
addition cost at each level. Four appended exercises have stars, hints and full
idea/writeup solutions: compatibility and eigenspace obstruction for Sylvester
with overlapping spectra; real versus complex border rank near the rotation
tensor; the three real quadratic algebras u²=t; and entropy equality versus
ambient dimension, including purity. No new numbered formal statements were added.

## Corrections and completed arguments

- **T01 (false exercise claim).** `linear:ex:noapprox` originally asked that both
  pure summands of W_epsilon have norm 1/epsilon. The first has norm
  (1+epsilon²)^(3/2)/|epsilon|, and the second 1/|epsilon|. The revised exercise
  states these exact values for positive real epsilon; the solution derives them
  and the bounded sum norm²=3+3epsilon²+epsilon⁴.
- **T02 (equality case).** Entropy was said to attain log2(min(m,n)) “when all the
  sigma_s are equal”. Equal nonzero coefficients with rank below min(m,n) do
  not suffice. The full-rank condition is now explicit and a local logarithm
  proof gives both the bound and its exact equality condition. A rank-two Bell
  vector embedded in dimensions at least three is the counterexample to the
  original unqualified sentence.
- **T03 (rectangular proof).** The Kronecker SVD proof called Sigma1 tensor Sigma2
  a rectangular diagonal matrix. Under standard lexicographic ordering this can
  fail for differently shaped rectangles. Distinct occupied row/column pairs
  permit independent row and column permutations to a rectangular diagonal.
  The original rank and singular-value conclusions are retained in full.
- **T04 (topology/field).** The algebraic W-rank calculation still covers every
  field; all convergence, norm and border-rank claims now explicitly use R or C
  with the ordinary entry topology. The original arbitrary-field convention did
  not by itself supply a topology for these claims.
- **T05 (missing base hypothesis).** The exponent theorem explicitly assumes
  integer k>=2. The original expression log_k(r) is undefined at k=1; no valid
  case is removed. The proof covers padding, block coefficient centrality and
  the r>k² geometric-sum condition.
- **T06 (characteristic).** The Waring exercise's interpretation from cubic
  polynomials to symmetric tensors implicitly used division and injectivity of
  the cubic coefficient correspondence. It is now stated over R or C, and the
  solution explains the characteristic-two/three obstruction to that argument.
  The signed polynomial identity is retained. No claim of this polynomial
  correspondence in characteristic three is made.
- **T07 (incomplete original solution).** The rectangular grid exercise now
  receives its full requested condition number, not only the square asymptotic:
  (4+2cos(pi/(m+1))+2cos(pi/(n+1))) /
  (4-2cos(pi/(m+1))-2cos(pi/(n+1))). The 1×1 boundary case is checked.
- **T08 (threshold proof).** The original solution compared only n=512 and1024
  and inferred the permanent crossover. The new solution proves monotonicity of
  q_s=2(8/7)^s+5(4/7)^s-7 for s>=3, with exact signs at s=1,2,9,10. Thus every
  earlier positive power is worse and every power from1024 onward is better.
- The complex-rank-two formula now calls a-ib a coordinate linear form when
  coefficients themselves are complex; it is not necessarily conjugation.
- The Schmidt exercise now supplies normalised eigenvectors and the sign in
  the negative-eigenvalue factor, completing the requested decomposition.
- Strassen's theorem proof checks all four output entries locally rather than
  leaving one to a later exercise. Border rank of W is shown at least two using
  a closed flattening-rank condition. Zero tensors and empty matrices are checked.

Fixing commit: to be entered by the parent after integration.

## Prerequisites and actual checks

Read the entire original chapter, actual Volume 10 printed order, current Volume 8
main.tex and the earlier Schur triangularisation, SVD and double-dual theorem
texts. All new proofs and solutions use only earlier linear algebra and the
material already taught before this chapter's exercise list. Advanced record
bounds, NP-hardness and Roth's stronger theorem are clearly quoted, not premises.
The earlier graph/path eigenvalues are named with their existing references.

Executed Python source comparison, exit0: all original labels retained;
numbered section order identical; original nonexercise formal-environment order
identical; both original figure blocks literal; figures2→4; exercises12→16.
Executed exact integer arithmetic for operation-count differences, exit0:
D1=-13, D2=-135, D9=-12729073, D10=175399785.
No build was run by this writer; the parent controls the build process.

## Integrated fixing commits

b03ed741 (initial rewrite), ee5c8ac6 (preserve characteristic-three Waring identity). These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.

Final Waring scope: the polynomial identity holds over every field. The explicit
four-pure-tensor formula is proved by ordered entries in characteristic other
than 2, including 3; the first draft's R/C-only restriction was removed in ee5c8ac6.
