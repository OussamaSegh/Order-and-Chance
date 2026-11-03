# Volume 2 — Step 5 mathematics, worked examples and hypotheses review

**Date:** 3 November 2026
**PR:** #97, editorial/volume2-continuity-foundations-20261103
**Status:** Step 5 **source-level editorial mathematics review completed**, subject to exact-head CI.
**Not a release sign-off:** This review does not replace the line-by-line 144-exercise/hint/solution review of Step 6, rendered production/KDP proof of Steps 8–9, or an external mathematical referee.

## Scope, method and inventory

Read the eleven chapters in the approved printed sequence, with the statements and actual proof text for all named theorem/lemma/proposition/corollary results, then inspected the 99 embedded worked examples and their numeric assertions and the descriptive mathematical figure captions. In the pre-exercise manuscript the source inventory is:

| Printed chapter | Source | Named result statements | Worked example blocks | Proof environments |
| --- | --- | ---: | ---: | ---: |
| 1 — Divisibility | ch01-divisibility.tex | 6 | 5 | 6 |
| 2 — Primes | ch02-primes.tex | 5 | 6 | 5 |
| 3 — Congruences | ch03-congruences.tex | 8 | 6 | 8 |
| 4 — Arithmetic functions | ch04-arithmetic-functions.tex | 4 | 9 | 4 |
| 5 — Primitive roots | ch05-primitive-roots.tex | 6 | 11 | 6 |
| 6 — Quadratic reciprocity | ch06-quadratic-reciprocity.tex | 6 | 9 | 6 |
| 7 — Sums of squares | ch07-sums-of-squares.tex | 5 | 6 | 5 |
| 8 — Diophantine methods | ch09-diophantine.tex | 5 | 15 | 5 |
| 9 — Continued fractions and Pell | ch08-continued-fractions.tex | 7 | 12 | 7 |
| 10 — Quadratic integer rings | ch10-gaussian-eisenstein.tex | 9 | 8 | 9 |
| 11 — Characters and sieve | ch14-characters.tex | 11 | 12 | 11 |
| **Total** |  | **72** | **99** | **72** |

A proof may appear after the statement and an intervening lemma (quadratic reciprocity), and may have an optional title. Regression scanning now includes the titled proof environments as well.

The review distinguished **logical proof validity** (whether the arguments use earlier established tools and handle their hypotheses), **finite certificates** (recalculating examples independently) and **production rendering** (which remains the job of Steps 8–9). Computer spot-checks are not a replacement for theorems; they help catch counterexamples to stated boundaries and incorrect numerical constants.

## Theorem and proof audit by chapter

| Printed chapter | Proof chains reviewed | Particular boundaries verified |
| --- | --- | --- |
| 1 | Euclidean division and uniqueness; classification of subgroups of Z; Bézout; Gauss' divisibility lemma; fundamental theorem of arithmetic; Lamé/Fibonacci lower bounds | Euclidean remainder non-negative even for negative dividend; Bézout uses non-both-zero gcd input; valuation formulas apply to nonzero integers; the last Euclidean division is counted correctly |
| 2 | Euclid infinitude; Euler reciprocal-prime comparison via geometric products; central binomial coefficient valuation bounds; Chebyshev products/count estimates; Bertrand's binomial-contradiction proof | Prime powers p^e dividing a binomial have p^e≤2n; medium-prime cancellation uses n≥5; small n≤630 case and monotonicity for n≥512 are separately justified; asymptotic estimates are not substituted for the finite check |
| 3 | Well-defined residue ring; unit iff gcd=1; Euler/Fermat via unit permutation; Wilson; CRT; linear congruences; totient divisor-sum count; simple-root Hensel lemma | Invertibility and cancellation are restricted to units; CRT needs coprime moduli or the stated compatibility criterion; lifting needs nonzero derivative mod p; explicit positive-modulus hypotheses added to linear congruence and totient identities |
| 4 | Multiplicativity and finite Dirichlet convolution; Möbius inversion; Euclid–Euler even-perfect classification; Dirichlet's hyperbola count | Convolution is not pointwise multiplication; factorisation is used only for coprime factors; even-perfect converse checks every extra divisor; asymptotic divisor count is now explicitly for real x→∞, x≥1 |
| 5 | Multiplicative order; existence and count of primitive roots mod primes; lifting a root to odd prime powers; classification of cyclic unit groups; structure mod 2^k and odd-square test | Euler's theorem supplies the order; Gauss' φ divisor identity supplies the generator count; prime versus composite field root bound is distinguished; odd p is required for lifting; cyclicity exceptions n=1,2,4 are handled |
| 6 | Euler's criterion and Legendre symbol; Gauss' lemma; 2/p supplementary law; Eisenstein floor lemma and lattice count for quadratic reciprocity; Jacobi symbol | The multiplicative Legendre claim is for odd prime p; exactly (p−1)/2 **nonzero** squares is now explicit; Eisenstein floor formula requires odd numerator; the rectangle line contains no eligible lattice points; the Jacobi value +1 is not a root certificate |
| 7 | Thue pigeonhole lemma; two-square prime/integer criteria; Euler four-square identity and the least-multiple descent; circle-counting bound | The four-square descent checks m odd and strict 0<r<m; primes q≡3 mod 4 have even exponent in representable numbers; circle counting includes all boundary lattice points, also in the small R∈[1,√2) range |
| 8 | Primitive Pythagorean parametrisation; Fermat fourth-power infinite descent; rational conic chord parametrisation; Mordell y²=x³+7 obstruction; Markov/Vieta involution and strict descent | Positive/primitivity/parity conditions tracked; in Fermat descent n=2u²v² is **twice** a square; singular/tangent conic cases are not treated as automatically giving two intersections; Markov descent changes a largest coordinate, while a different move can grow |
| 9 | Convergent recurrence/determinant; alternating approximation bounds; existence/uniqueness of irrational infinite CF; best approximations; Legendre criterion; periodic iff quadratic; Pell existence and power classification | Convergent denominators and sign alternation; absolute error versus |qx−p| distinction; periodic quadratic has bounded integer complete-quotient coefficients; Pell solution includes integer signs and inverse powers; the quadratic norm is locally defined |
| 10 | Norm-one units and the three Euclidean quadratic integer rings; Bézout and unique factorisation in Euclidean domains; non-UFD example; Gaussian primes and Jacobi r₂(n); Eisenstein primes; cube congruence; exponent-three Fermat descent | The norms N(a+bi), N(a+bω) and N(a+b√−2) are distinct; closest-coordinate rounding gives strict smaller norm; Gaussian factors q≡3 mod 4 remain irreducible; 3 ramifies at 1−ω; the cubic proof descends in v_(1−ω) |
| 11 | Character definitions and zero extension; unit-group product/count; two orthogonality formulas; absolute convergence of p-series/Dirichlet convolutions; nonzero Euler product for s>1; Möbius-zeta identity; exact finite Legendre sieve; conditional χ4 boundary-series arguments | A finite character sum is not an infinite Euler product; the p-series tail bound starts at floor X; logarithmic Euler expansion is uniform for s≥1 but is asserted only where products converge absolutely; the sieve requires z≥√x; bounded Abel-weighted **difference** does not imply convergence of an unweighted signed prime series |

## Mathematical corrections committed during Step 5

1. **Chapter 7, lattice-disc example:** The example claimed N(2)=9, omitting (±2,0) and (0,±2). Now N(2)=1+4+4+4=**13**. Independently enumerated N(6)=113 and N(10)=317 and locked all three counts in finite arithmetic regression.
2. **Chapter 11, Möbius series:** The ten-term example assigned μ(6)=−1 and μ(7)=0, but the values are **μ(6)=+1** and **μ(7)=−1**. The corrected partial sum is approximately **0.6162585034**, tending toward 6/π²≈0.607927. Regression checks the ten μ values and the sum independently.
3. **Chapter 10, Eisenstein factorisation:** The example assigned N(2+ω)=7, silently using a plus-sign norm; actually N(2+ω)=3, while **N(2−ω)=7**. Correct factorisation: **7=(2−ω)(2−ω²)**. Regression computes norms and multiplication for a finite grid of Eisenstein integers.
4. **Chapter 8, modular obstruction:** An example claimed every odd x was excluded from y²=x²+x+1 modulo 4, and all even x survived. Both claims are false. The exact sequence for x≡0,1,2,3 mod 4 is **1,3,3,1**; only classes 1 and 2 are excluded. Explicit solutions (0,1) and (−1,1) demonstrate that the equation is solvable. Regression checks the residue table.
5. **Chapter 8, Fermat descent:** Two explanatory worked examples incorrectly described both m and n as squares or gave incorrect intermediate square equations. The proof itself has m=w² and n=2ab with a=u²,b=v², so **n=2u²v²**. The examples now follow the actual two-stage Pythagorean parametrisation and strict w<z inequality.
6. **Chapter 8, Vieta jump:** An example said a jump from (5,2,1) gives a larger partner without specifying that it must replace the **smallest** coordinate. Replacing 1 yields 29, hence (5,2,29); replacing the largest coordinate is the **descending** move used in the theorem. Regression verifies the sample Markov triples.
7. **Chapter 8, reader-facing context:** Removed hard-coded “Theorem 9.1/9.2” (this is now printed Chapter 8) and replaced with stable theorem references. Corrected the inaccurate identification of rational conic parametrisation with the Hasse principle. The descent caption now describes both parameter steps instead of falsely implying the first set of parameters already solves the original fourth-power equation.
8. **Chapter 11, analytic boundary:** A passage inferred convergence of the signed sum ∑_p χ4(p)/p from bounded Abel-weighted expressions. That inference does not follow. The replacement proves the valid conditional implication needed: the two non-negative residue-class sums have divergent sum and bounded Abel-weighted difference, hence each diverges; no convergence of an unweighted signed series is claimed.
9. **Other hypotheses and captions:** Bézout's statement explicitly excludes simultaneous zero inputs; the linear-congruence and totient-sum statements explicitly require positive modulus; the divisor hyperbola theorem specifies x→∞; Euler's criterion counts the nonzero square classes. Fixed the 19/6 approximation to π to about 0.0251, corrected half-open square geometry, and described the Eisenstein basis without incorrectly identifying a triangle as a parallelogram.
10. **Historical precision:** Bertrand's heading now credits Chebyshev's first proof and Erdős's 1932 elementary proof without choosing one contested year for Chebyshev. Independent historical accounts variously cite 1850 and 1852; the proof author, not that exact year, is important mathematically. The Pell d=61 solution matches the MacTutor Pell history, and the Gauss-circle exponent 517/824 is cited as a dated Bourgain–Watt 2017 benchmark, never as a verified current record.

## Independent numerical and structural evidence

The suite tools/test_volume2_arithmetic_sanity.py already independently checks: Fermat quotient odd-prime boundary, Hensel lifts mod 125, the r₂(n) divisor formula and two-square criterion for n≤150, quadratic reciprocity on odd primes up to 79, fourth-moment Kloosterman cases at 3,5,7,11, Schur nonzero-value hypotheses, primitive Pythagorean triples, small four-square representations and primitive-root counts. Step 5 added tests of:

- radius-2, radius-6 and radius-10 integer discs;
- Eisenstein norm multiplicativity and the splitting of 7;
- the exact ten Möbius coefficients and finite s=2 sum;
- the mod-4 Diophantine obstruction and Vieta examples.

The manuscript regressions additionally check that named proof environments, including optional proof titles, are included in the printed-order future-dependency scan. Direct source verification at the final content state found **72 named result environments and 72 corresponding proof environments**, **99 worked example blocks**, **144 exercises + 144 hints + 144 solutions**, **266 distinct source-local labels**, **no missing local \ref/\eqref/\autoref targets**, and **no imbalanced checked LaTeX environments**.

### Historical reference spot checks

- Chebyshev and Erdős on Bertrand: David Galvin, “Erdős’s proof of Bertrand’s postulate,” https://academicweb.nd.edu/~dgalvin1/pdf/bertrand.pdf ; MathWorld, https://mathworld.wolfram.com/BertrandsPostulate.html .
- Bhāskara II and the Pell equation for 61: MacTutor, https://mathshistory.st-andrews.ac.uk/HistTopics/Pell/ .
- The circle problem exponent is mentioned only as the explicitly dated 2017 Bourgain–Watt result; it is not represented as the current state of research.

## Acceptance and remaining blockers

**Step 5 editorial mathematics gate:** Completed at source level. No known incorrect claim in the first-route theorems or the 99 reviewed worked-example blocks is being carried as an accepted exception. This statement means the manuscript has undergone an internal mathematical/editorial pass, **not** that every claim has been machine-proved or externally refereed.

**Still open:** latest exact-head automated build/test success; Step 6 individual review of the **144** exercise problems, hints and solutions (which may expose additional mathematical errors); Step 7 transition and metadata polish; Step 8 actual rendered reading/print PDF and EPUB visual checks, correct page-count-dependent cover; Step 9 KDP Previewer and physical print proof. None of these can be waived on the strength of this source audit. PR #97 must remain draft and unmerged.
