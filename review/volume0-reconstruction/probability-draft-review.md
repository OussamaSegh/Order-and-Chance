# Batch identifier

G — probability reconstruction draft, ready for integration and complete-book QA.

## Changes implemented

Prepared `ch09-probability.tex` in this draft directory from the discrete
reviewer's completed C split. No canonical manuscript or shared publishing files
were changed by this reviewer.

- Replaced the single overloaded vocabulary paragraph with three sequential
  subsections: outcomes/events/masses; information/independence; random variables,
  laws, expectation and variance. Added fair-dice/coin examples, a pause prompt,
  the equivalence between finite masses and finite axioms, and explicit product
  model normalisation and coordinate-independence proof.
- Defined mutual event independence separately from pairwise independence, with
  a concrete three-sign counterexample for random variables.
- Added covariance matrices, the proved positive-semidefinite identity, a
  two-variable covariance spectrum, and the distinction between orthogonal
  decorrelation and independence.
- Kept the central laws, Markov/Chebyshev, weak law and Bayesian workshop. Made
  distribution parameter/endpoint conventions explicit and identified the weak
  law's limit as convergence in probability across finite experiments.
- Added one controlled countable-mass section: nonnegative and absolutely
  convergent expectations, justified nonnegative regrouping, finite truncations
  and the tail-sum identity, geometric waiting, Poisson normalisation and moments.
- Replaced the coupon solution's assumed infinite sequence and unjustified sum
  of indicators by exact finite-word enumeration of phase lengths. Their joint
  mass factors into geometric masses, normalises to one, agrees with each finite
  truncated experiment, and gives nH_n by proved nonnegative linearity.
- Added two two-star bridge exercises, each with hint, discovery and write-up:
  sampling covariance/eigenvalues/fixed-sum invariant; finite arithmetic
  divisibility independence/inclusion–exclusion/error bounds.
- Added a finite arithmetic closing bridge toward Volumes 1 and 3.

## Mathematical improvements

The finite framework is explicit before countable examples occur. No probability
space supporting an infinite sequence is assumed or constructed. The countable
extension is limited to an elementary series model that existing waiting-time
examples actually need. Covariance is connected to Chapter 6's spectral theory
without confusing uncorrelated and independent variables.

Also repaired two additional issues in the original derangement paragraph:
the nearest-integer claim needs the error multiplied by n!, with n=1 checked
separately; the n=10 probabilities do not round to the same seven-decimal string,
although their difference is below 3e-8. Replaced that claim by the actual error
bound. The birthday half-probability comparison now points to a certified log(2)
bound instead of an imprecise decimal expansion of 253/365.

## Pedagogical improvements

Definitions now each address an identifiable example and limitation. Product
models establish independence rather than treating repetition as proof of it.
The covariance exercise starts from the invariant sum X_i=k, and the arithmetic
exercise exposes finite floor errors before any limiting language. Existing
workshop strategy and authorial voice remain.

## Content preservation

All 11 original probability exercise identifiers, hints and complete solutions
are retained, with domains/prerequisites repaired. The total is now 13 complete
triples. Existing probability figures, portraits, historical opening, Bayesian
workshop, all three challenge topics and full source list remain. The exact
derangement identity lives in Chapter 2; the analytical return and its figure
remain here. No original label was removed. Advanced birthday refinement is
retained but explicitly quoted as an outlook, rather than asserted proved by
its heuristic notes. No changes to other volumes.

## Verification

Executed `check_probability.py` in this directory: **3,349 exact finite and
source-structure checks passed**. Results are in `verification.json`.

Checks include every inclusion-indicator covariance entry for all subsets with
2<=n<=8 and every k; the associated zero and perpendicular eigenvalue identities;
finite arithmetic density errors for 1–4 primes and N=1,...,300, with mutual
independence at full periods; every completed coupon word of length at most 8
for n=1,...,4, comparing phase counts and finite-truncation probabilities; the
three-sign pairwise-independence example; all 13 matching exercise/hint/solution
triples and both solution headings; environment counts.

The new written arguments were reviewed for domain and zero cases: n=1 coupon,
p=1 geometric, p=0/1 binomial, lambda=0 Poisson, k=0/n sampling, zero event
probabilities, k>n Ramsey and fixed primes versus growing sieve dimension.
These checks support the proofs and do not certify universal correctness.

## Remaining issues

Complete-book compilation, style/layout/overflow checks, rendered-page review and
independent mathematical review belong to integration and were not run here.
Semantic labels expected: ch:sums, ch:counting, ch:sequences, ch:linear,
ch:calculus. The logarithm workshop must retain its proved upper bound below
0.693148. No fresh verification of historical primary documents, portrait
provenance or dynamic Ramsey records is claimed. The retained refinement's
bibliographic attribution is inherited and should be checked in the final
historical/source pass.

## Next work

Integrate after F, compile the complete book, inspect all new probability pages,
then run the full preservation and mathematical audit suites. Preserve the G
checkpoint before starting H integration.
