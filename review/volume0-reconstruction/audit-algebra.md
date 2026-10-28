# Algebra audit — original Volume 0, 28 October 2026

Scope: complete source reading of `ch02-complex-roots.tex` (683 lines),
`ch03-polynomials.tex` (910 lines), and `ch07-linear-algebra.tex` (791 lines),
including 49 exercise statements, their 49 hints and 49 solutions, workshops,
challenge notes and source lists. Line references below refer to commit
`3259d462860e13150fc6cb15ecb0e3109f95b5ed`, before reconstruction.

This is a mathematical/editorial review, not formal verification. Historical
references were inspected for whether sources are actually supplied; the cited
books and primary documents have not all been independently retrieved.

## Actual coverage and preservation inventory

| Original unit | Existing coverage | Proposed home |
| --- | --- | --- |
| Complex opening and from-scratch arithmetic, lines 1–98 | Cardano/Bombelli motivation; pair arithmetic; inverses; conjugation/modulus; triangle inequality including equality; algebraic square roots; meaningful powers figure | Chapter 4, retain |
| Exponential form, 99–156 | Absolutely convergent exponential series; explicitly admitted real trigonometric properties; polar representation and uniqueness; half-angle argument; trigonometric addition formulas | Chapter 4; earlier sequences chapter supplies series |
| Roots/filter, 157–230 | Exact enumeration and order; orthogonality; Fourier-basis interpretation; residue-class coefficient extraction with proof | Chapter 4, retain |
| Geometry/cyclotomy, 231–320 | Similarities; equilateral criterion with proof; cyclotomic factorisation; integrality via monic division; prime powers | Chapter 4; polynomial toolkit is a named forward dependency |
| Workshop and problems, 321–683 | Robot discovery workshop; 15 exercises with complete strategy/write-up solutions; Gauss sums, circulants, Napoleon, finite Basel identity; 3 outlook challenges; source list | Chapter 4, retain all labels; mark circulant/integral problems as return bridges |
| Polynomials, 1–199 | Euler/Basel and Chebyshev motivation; formal polynomial versus function; Horner/formal derivative; Euclidean division; roots/multiplicities; full compactness-based fundamental theorem of algebra; Viète | Chapter 5, retain; earlier completeness removes major forward dependency |
| Interpolation/Chebyshev, 200–282 | Lagrange proof, examples and finite-field secret sharing; recurrence, closed form and minimax motivation | Chapter 5, retain |
| Integer/symmetric/root location, 283–494 | Rational roots; polynomial Gauss lemma; Eisenstein; reduction mod p; Newton identities; fundamental theorem of symmetric polynomials; Descartes; Gauss–Lucas | Chapter 5, retain: these are already present, not missing additions |
| Polynomial workshop/problems, 495–910 | Sensitivity/model-selection workshop; 18 exercises with hints/strategy/write-up; Basel, discriminant, log-concavity and Mason–Stothers; three challenges | Chapter 5, retain; clearly label calculus-dependent return problems |
| Linear opening/spaces, 1–73 | Chessboard/Cassini; historical determinant motivation; spaces, span, independence, bases; complete exchange/dimension proof; compressed map/matrix reminder | Chapter 6; expand definitions and examples before computations |
| Determinant/reduction, 74–228 | Permutation sign proof; determinant uniqueness/product/invertibility; Laplace; rank-nullity; Vandermonde; characteristic polynomial; annihilator criterion; real symmetric spectral theorem; recurrence applications | Chapter 6; move rank-nullity and inner products earlier |
| Volumes/adjugate, 230–369 | Gram–Schmidt/projection with proof; Gram determinant; adjugate/Cramer; full Cayley–Hamilton proof, with invalid-proof warning | Chapter 6, preserve proofs, remove avoidable forward prerequisites |
| Linear workshop/problems, 371–791 | Exact least squares and uniqueness; conditioning counterexamples; 16 exercises/hints/strategy/write-up; PageRank contraction, Cauchy determinant/Hilbert; advanced challenges | Chapter 6, retain; polynomial integral Gram exercise returns after calculus |

All 20 associated figure sources were located. Dense sampled-coordinate plots
were inspected by structure/data summaries; the small geometric figures were
read in full. No PDF page-by-page visual review was done by this audit.

## Findings requiring implementation

1. **Essential addition / accessibility:** linear lines 39–45 define a vector
   space by “the usual rules.” The stated readership cannot supply the axioms.
   State additive group/scalar compatibility/distributive/unit rules; give a
   worked subspace and a non-example. This is a real gap, unlike spectral theory,
   least squares and Cayley–Hamilton, which already have substantial proofs.
2. **Essential structural improvement:** lines 66–68 compress maps, kernels,
   images, injectivity, matrices, composition and change of basis into one
   reminder without proofs. Establish these in separate short paragraphs with
   a worked example. Move rank-nullity (136–143) immediately after maps, before
   determinant invertibility (103–105) uses independence/invertibility.
3. **Essential structural improvement:** spectral theorem (206–213) uses inner
   products, orthogonality, orthonormal bases and a symmetric restriction before
   their introduction (232 onward) and before Gram–Schmidt (241–270), which the
   text itself acknowledges it used. Introduce/prove inner products,
   Gram–Schmidt and projection before spectral theorem. Explain that a real
   eigenvector follows by taking a nonzero real or imaginary part of the complex
   eigenvector. Define orthogonal matrix and the direct-sum notation.
4. **Essential addition:** positive definite/semidefinite and quadratic form are
   used (e.g. 366, 434–440, 629–638) but never defined as vocabulary. A short
   definition plus eigenvalue criterion follows immediately from spectral theorem.
   “Nilpotent” in exercise 7.2 (419) also needs the definition `A^m=0` for some
   positive integer m. Define trace as the sum of diagonal entries before use.
5. **Essential addition:** polynomial gcd/coprimality/Bézout do not appear as a
   proved toolkit, though Mason (628–641, 861–873) and later Volume 1 use them.
   Add the Euclidean algorithm, monic gcd, Bézout and coprime cancellation in a
   compact section after polynomial division. Define irreducible explicitly
   before the fundamental theorem of algebra; field/ring terminology needs a
   concrete operational explanation rather than assumed abstract algebra.
6. **Domain clarification:** complex exercise `ex:sumdist` (396–399) should say
   n≥2 (or n≥3 under the polygon convention). At n=1 the displayed identity is
   false for arbitrary z. `ex:circulant` part (c), 376–385, needs n≥2 for the
   proposed first row `(1,1,0,...)` to exist. Chebyshev root formula (248–255)
   should explicitly attach n≥1 to the formula containing division by n.
7. **Essential explanatory correction:** linear solution `ex:tracerank`, 666,
   says the finite-dimensional trace obstruction is “why quantum mechanics needs
   infinitely many dimensions.” This overstates what was proved; finite spin
   systems exist. Say the canonical relation `DX-XD=I` has no finite-dimensional
   real/complex representation. Preserve the actual polynomial-operator example.
8. **Proof-contract correction:** Hilbert solution 763 invokes the unproved bound
   λ_max(H_n)<π. It is unnecessary. Since the (1,1) entry is 1, Rayleigh gives
   λ_max≥1; λ_min≤(det H_n)^(1/n), and the proved determinant bound establishes
   an unbounded condition number. This supplies an elementary rigorous explanation.
9. **Precision:** polynomial prose 393 says Viète makes symmetric functions
   “polynomials in the coefficients.” For a nonmonic P they are ratios involving
   its leading coefficient. Say coefficients of the monic normalisation. The
   preceding displayed Viète theorem is already correct.
10. **Proof completion / pedagogy:** minimax uniqueness challenge note 885–887
    leaves a delicate multiplicity count to the reader. A short alternative uses
    the leading coefficient in Lagrange interpolation at the n+1 alternating
    extrema: all summands have the same sign, their sum is zero, hence all vanish.
11. **Missing hypotheses:** `ex:logconcave`, 621, should explicitly assume n≥1
    and a_n≠0. Otherwise the zero/constant polynomial case makes “P' has only real
    roots” ambiguous or false under the definition of a root of the zero polynomial.
12. **Historical precision:** linear challenge note 770 calls Hadamard order 428
    “resolved in 2005”; the prior repository errata already distinguishes its
    June 2004 construction from the 2005 publication. Correct to 2004 and retain
    the 2005 bibliography. The October 2026 frontier claim and arXiv source require
    fresh source confirmation; this audit has not confirmed them.

## Dependencies and justified choices

Preferred order 3→4→5→6 works well for completeness, Cauchy products and the
fundamental theorem of algebra. There remains an honest small cycle: complex
roots/cyclotomic integrality use polynomial root factorisation and monic division
from Chapter 5; Chapter 5 needs complex roots for its fundamental theorem. Solve
this conservatively with an explicitly named elementary polynomial toolkit or
clearly signposted proofs in Chapter 5, rather than moving all polynomials earlier.

Calculus-dependent return problems already exist and should not be deleted:
`ex:lin` (complex, integral of sin^4), `ex:cotsum` (can use formal polynomial
product rules, so no analytic differentiation is needed), `ex:chebprod(c)`
(improper weighted integral/change of variables), `ex:logconcave(b)` (Rolle),
`ex:hilbert` (polynomial integrals and strict positivity), and minimax/Descartes
(intermediate values). The contract can explicitly admit the elementary real
mean-value and intermediate-value facts; otherwise mark the relevant problems
for return after Chapter 7. Do not claim they require no calculus.

Existing bridge problems are excellent: mod-3 binomial filter, finite Basel,
interpolation of 2^k via finite differences, matrix recurrences, Hilbert Gram,
PageRank convergence, and Mason’s arithmetic analogy. Avoid duplicating them to
inflate the bridge count. A short explicit interpolation/difference extraction
problem and an operator recurrence problem would be useful additions.

## Cross-volume numeric citations — preserve a compatibility record

Read-only search found, among others:

- Volume 1 ch12 line 257 → original Proposition 3.2 (polynomial root bound).
- Volume 1 ch11 line 42 → original Propositions 3.7 and 3.8(b).
- Volume 1 ch06 lines 282/361 → original Exercise 3.5 (cyclotomic irreducibility);
  line 283 → Exercise 2.8 (Gauss sum), line 355 → Proposition 2.4 (orthogonality).
- Volume 2 linear-ch02 line 55 and ch02-quotients line 27 → Theorem 7.2.
- Volume 3 ch08 line 339 and ch06 line 407 → Theorem 7.7 (spectral theorem).
- Volume 4 ch09 lines 99/310 → Proposition 2.1 and Theorem 3.3.
- Volume 4 ch07 lines 254/333 → Exercises 2.8/2.7.

Later books also contain many chapter-level citations. No later volume was edited.
A concordance from original numeric locations and stable labels to new locations
is necessary. Preserving labels alone does not fix hardcoded citations elsewhere.

## Checks and limitations

Complete proof/exercise source reading was performed, with attention to zero
roots, multiplicity, covariance prerequisites and field restrictions. No new
universal claim is inferred from sampled computations. The existing reproducible
fact-check program was started separately; completion must be recorded from its
actual result. No compilation, formal proof verification, full historical source
retrieval or page-by-page visual proofread is asserted by this report.
