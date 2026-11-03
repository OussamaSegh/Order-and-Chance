# Volume 2 — Step 6: complete exercise, hint and solution ledger

**Review date:** 3 November 2026. **PR:** #97 (draft), branch `editorial/volume2-continuity-foundations-20261103`.
**Source gate:** reviewed at manuscript level. This ledger is a keyed inventory and audit record, not a formal proof-checker or KDP approval.

## Review scope and acceptance standard

The review followed the **actual printed order** of the eleven chapters, not their legacy source filenames. For each of the **144** exercises, the prompt, hint and formal solution were read together against the results already established for the specified reading route. For every key, its exercise/hint/solution match and order were checked. The existing `\\idea` discovery note and `\\writeup` full argument were retained. Longer `pb:` problems additionally have prerequisite `\\tools` and future-context `\\leads` markers; shorter `ex:` keys were not falsely required to have those extra sections. No exercise, hint, solution key or mathematical topic was removed.

Mathematical review concentrated on: boundary assumptions; nonnegative versus positive solutions; finite versus infinite counts; irreducible and coprime factors; exact-congruence and valuation conditions; sign and normalization in reciprocity and character sums; justification of conditional convergence; and the claimed completeness of Diophantine and Vieta descents. Separate finite calculations tested representative cases of the long results, including exact strong-liar counts and four-square local densities. **Finite arithmetic certificates support, but do not prove, general claims.**

**Independent source key invariant:** 16 + 11 + 21 + 13 + 15 + 17 + 8 + 8 + 8 + 8 + 19 = **144** exercises; exactly one hint and one solution per key, in the same order. All 144 solution bodies have `\\idea` and `\\writeup`; no duplicate keys.

**Post-review grading:** **37** one-star, **80** two-star, **20** three-star, **7** Journey. All grading changes are additive classification corrections: the 144 exercises and key text remain.

## Mathematical fixes and decisions

1. **`ex:imo88` (printed Chapter 8):** The prior proof claimed a negative Vieta root makes a quadratic positive without controlling the constant `−k`. It did not establish the root needed for descent. Fixed by (f(t)=t^2-kbt+b^2-k), with (f(-1)>0), (f(b)<0) for nonsquare integer (k\ge2). The second integer root lies in ((-1,b)), so it is positive unless (k=b^2), excluded. Thus (1\le a'<b\le a) and the descent is valid.
2. **`pb:gcdmean` (printed Chapter 5):** The formula for (\mathbb E[\gcd(a,b)]) formerly relied on an unproved average-order theorem apparently deferred to Volume 6. A direct Möbius inversion and finite partial-summation derivation now proves (A(t)=\sum_{d\le t}\varphi(d)/d=t/\zeta(2)+O(\log(2t))) and (\sum_{d\le N}\varphi(d)/d^2=(\log N)/\zeta(2)+O(1)). Volume 6 remains an outlook, not an unearned prerequisite.
3. **Difficulty calibration:** Regraded `pb:valuation`, `pb:parity` (multi-part asymptotic probability), `pb:fermatnum` (prime-factor order refinement and explicit 641 factor) and `pb:artin` (safe-prime primitive roots) from ★ to ★★. Their source labels, hints and solutions did not change.
4. **Advanced journeys retained as optional:** `pb:fibcoprime`, `pb:ramanujan5`, `pb:eisensine`, `pb:gcdmean`, `pb:rabin`, `pb:jacobi`, `pb:densities`. Their statements explicitly direct readers to prerequisite theorems and later-volume chapters where needed.
5. **Other later-route challenges kept:** Glaisher (Bernoulli theory, Volume 5), finite-field extensions (Volume 3), Kloosterman moments, Gauss/Jacobi sums, analytic prime-factor estimates (Volume 6), four-square theta products (Volume 5), and p-adic/local-density extensions (Volume 13). Every later-chapter or later-volume reference was screened against the exercise introduction for a clear return/optional disclosure. No silently mandatory later-volume theorem remains in the first-route exercise ledger.

## Independent regression and computational evidence

The new `tools/test_volume2_exercise_keys.py` retains chapter-level counts and the complete **37 / 80 / 20 / 7** grading distribution. It also checks independently:

- IMO 1988 integer-square conclusion for all (1\le b\le a<160), backed by the repaired symbolic proof.
- Gcd moment (\sum_{a,b\le N}\gcd(a,b)=\sum_{d\le N}\varphi(d)\lfloor N/d\rfloor^2) at (N=10,30,60), backed by the new averaging proof.
- Modular and Diophantine examples: roots of (y^2=x^3-2) and (y^2=x^3-5) over a bounded interval, and the **nine** Markov triples up to maximum 200.
- Quadratic symbols of 2, Fermat factor 641, (n\nmid2^n-1) for bounded n and all four roots of 1 modulo powers of 2.
- Waring two (k)-th-power exceptions ((k=3,4,8), primes below 800), including the largest exceptional prime 761 for (k=8). Independent enumeration up to primes below 4096 confirmed the claimed finite list for (k=8).
- Complete strong-liar enumeration for odd composite (n<400) against **Monier's exact formula**, with sole (\varphi(n)/4) exception (n=9); the sharp case (n=15) has two liars among eight units.
- Pseudoprime 341, Proth certificate (3329) using base 3, Pell's equation for (d=61), Euler's (1{,}000{,}009) factorisation, the powerful-number representation for (n\le1000), and the primitive 4-square count at modulus 8.

The existing `tools/test_volume2_arithmetic_sanity.py` and manuscript tests also cover Hensel lifts, reciprocal-Fermat quotient edge cases, finite-field reciprocity, two- and four-square representations, and referenced advanced-section boundaries. Source-level invariants are also covered by `tools/test_volume2_manuscript.py`.

## All 144 keyed exercises, in printed chapter order

The “extension/return” tag describes **reader routing**, not a lack of a hint or solution; all entries have both. The topic is the individually checked problem's mathematical focus.

| Chapter | Exercise key | Grading | Mathematical check focus | Reader route |
| ---: | --- | --- | --- | --- |
| 1 | `ex:bez` | ★ | Bézout integer equation | In-volume |
| 1 | `ex:gcdn` | ★ | Adjacent quadratic gcd | In-volume |
| 1 | `ex:zeros` | ★ | Legendre factorial valuation / trailing zeroes | In-volume |
| 1 | `ex:sqrt` | ★★ | Rational algebraic integers | In-volume |
| 1 | `ex:mersgcd` | ★★ | Gcd of Mersenne expressions | In-volume |
| 1 | `ex:lame5` | ★★ | Lamé decimal-digit bound | In-volume |
| 1 | `ex:frob` | ★★ | Two-coin Frobenius number | In-volume |
| 1 | `ex:supercat` | ★★★ | Super-Catalan integrality | In-volume |
| 1 | `ex:n2n` | ★★★ | The n∤(2ⁿ−1) congruence | In-volume |
| 1 | `ex:t1-divisibility-lattice` | ★★ | Ideal sum/intersection | In-volume |
| 1 | `ex:t1-binomial-carry` | ★★ | Base-p carries in binomial valuations | In-volume |
| 1 | `ex:t1-euclid1071` | ★ | Euclid (1071,462) | In-volume |
| 1 | `pb:valuation` | ★★ | Random p-valuations / independence | In-volume |
| 1 | `pb:parity` | ★★ | Reduced random fraction parities | In-volume |
| 1 | `pb:fibcoprime` | Journey | Random Fibonacci gcds | Extension/return |
| 1 | `pb:orchard` | ★★ | Pólya orchard / Minkowski rectangle | In-volume |
| 2 | `ex:mod4` | ★ | Euclid primes 3 mod4 | In-volume |
| 2 | `ex:mersenne` | ★ | Mersenne/Fermat exponents | In-volume |
| 2 | `ex:germain` | ★ | Sophie Germain factorization | In-volume |
| 2 | `ex:fermatnum` | ★★ | Pairwise-coprime Fermat numbers | In-volume |
| 2 | `ex:gaps` | ★★ | Composite runs / Bertrand | Extension/return |
| 2 | `ex:factorial` | ★★ | No factorial perfect powers | Extension/return |
| 2 | `ex:erdosdiv` | ★★★ | Erdős reciprocal-prime proof | Extension/return |
| 2 | `ex:furstenberg` | ★★★ | Furstenberg's topology argument | Extension/return |
| 2 | `ex:t1-factorial-new-prime` | ★ | Prime factors of n!+1 | In-volume |
| 2 | `ex:t1-euclid-sequence` | ★★ | Euclid–Mullin-type number sequence | In-volume |
| 2 | `ex:t1-prod11` | ★ | Chebyshev numeric bound at 11 | Extension/return |
| 3 | `ex:last2` | ★ | Final digits of 7²⁰²⁶ | In-volume |
| 3 | `ex:sunzi` | ★ | Sunzi CRT | In-volume |
| 3 | `ex:digits` | ★ | Decimal divisibility rules | In-volume |
| 3 | `ex:sqrt1` | ★★ | Square roots of 1 mod odd prime powers | In-volume |
| 3 | `ex:wilsonconv` | ★★ | Converse to Wilson | In-volume |
| 3 | `ex:hensel` | ★★ | Hensel lifts mod125 | Extension/return |
| 3 | `ex:tower` | ★★ | Power-tower final digits | In-volume |
| 3 | `ex:korselt` | ★★ | Korselt direction / 561 | In-volume |
| 3 | `ex:lucas` | ★★★ | Lucas digitwise binomials | In-volume |
| 3 | `ex:t1-toy-rsa` | ★★ | Toy RSA correctness incl nonunits | Extension/return |
| 3 | `ex:t1-two-power-roots` | ★★★ | Four roots of 1 mod 2^k | In-volume |
| 3 | `ex:t1-sunzi23` | ★ | Smallest Sunzi CRT solution | In-volume |
| 3 | `pb:primepoly` | ★★ | Schur prime-divisor argument | In-volume |
| 3 | `pb:fpfunctions` | ★★ | Polynomial maps F_p→F_p | In-volume |
| 3 | `pb:aks` | ★★ | Polynomial primality criterion | In-volume |
| 3 | `pb:wolsten` | ★★ | Wolstenholme congruences | In-volume |
| 3 | `pb:jacobsthal` | ★★ | Jacobsthal binomial congruence | In-volume |
| 3 | `pb:morley` | ★★ | Morley congruence | Extension/return |
| 3 | `pb:glaisher` | ★★★ | Glaisher Bernoulli congruence | Extension/return |
| 3 | `pb:ramanujan5` | Journey | Ramanujan partition mod5 | Extension/return |
| 3 | `pb:kloosterman` | ★★★ | Kloosterman second/fourth moment | In-volume |
| 4 | `ex:360` | ★ | τ, σ, φ at 360 | In-volume |
| 4 | `ex:muid` | ★ | Möbius-divisor sums | In-volume |
| 4 | `ex:sigmaodd` | ★★ | Parity of σ(n) | In-volume |
| 4 | `ex:coprimesum` | ★★ | Sum of units | In-volume |
| 4 | `ex:even` | ★★ | Ending digits of even perfect numbers | In-volume |
| 4 | `ex:oddperfect` | ★★ | Prime factors of odd perfect number | In-volume |
| 4 | `ex:primitive` | ★★ | Primitive word count | In-volume |
| 4 | `ex:coprimeprob` | ★★★ | Coprime-pair density | Extension/return |
| 4 | `ex:t1-mu12` | ★ | μ∗1 at sample values | In-volume |
| 4 | `pb:eisensine` | Journey | Eisenstein trigonometric reciprocity | Extension/return |
| 4 | `pb:euler` | ★★ | Euler–Jacobi liar subgroup | Extension/return |
| 4 | `pb:nsq1` | ★★★ | Large prime factors of n²+1 product | Extension/return |
| 4 | `pb:sumsquares` | ★★ | Finite-field sums of squares / TV | Extension/return |
| 5 | `ex:findroots` | ★ | Primitive roots mod7,11,13 | In-volume |
| 5 | `ex:period` | ★ | Period of decimal 1/p | In-volume |
| 5 | `ex:fermatfactor` | ★★ | Fermat-number factor orders | In-volume |
| 5 | `ex:powersum` | ★★ | Finite-field power sum | In-volume |
| 5 | `ex:kth` | ★★ | k-th roots count mod p | In-volume |
| 5 | `ex:gausswilson` | ★★★ | Gauss generalised Wilson product | In-volume |
| 5 | `ex:cyclotomic` | ★★★ | Cyclotomic primes 1 mod n | In-volume |
| 5 | `ex:t1-units16` | ★ | Unit group mod16 | In-volume |
| 5 | `ex:t1-square-cosets` | ★★ | Square cosets mod2^k | In-volume |
| 5 | `ex:t1-gen7` | ★ | Primitive root 3 mod7 | In-volume |
| 5 | `pb:smith` | ★★ | Smith gcd-matrix determinant | In-volume |
| 5 | `pb:lambert` | ★★ | Lambert series/convolution | In-volume |
| 5 | `pb:ramsum` | ★★ | Ramanujan sums | In-volume |
| 5 | `pb:phipm1` | ★★ | Cyclotomic evaluation at ±1 | In-volume |
| 5 | `pb:gcdmean` | Journey | Mean gcd/LCM asymptotics | Extension/return |
| 6 | `ex:minus3` | ★ | Quadratic symbol of −3 | In-volume |
| 6 | `ex:onemod4` | ★ | Primes 1 mod4 via n²+1 | In-volume |
| 6 | `ex:minus2` | ★★ | Quadratic symbol of −2 | In-volume |
| 6 | `ex:mersfactor` | ★★ | Factors of selected Mersenne numbers | In-volume |
| 6 | `ex:consecutive` | ★★ | Consecutive quadratic residues | In-volume |
| 6 | `ex:pepin` | ★★ | Pépin Fermat primality test | In-volume |
| 6 | `ex:gausssum` | ★★★ | Gauss-sum reciprocity proof | Extension/return |
| 6 | `ex:t1-residue-chance` | ★★ | Legendre signs and chance | In-volume |
| 6 | `ex:t1-res11` | ★ | Residues mod11 / symbols mod13,17 | In-volume |
| 6 | `pb:primsum` | ★★ | Primitive-root sums/products | In-volume |
| 6 | `pb:phimodp` | ★★ | Cyclotomic splitting mod p | Extension/return |
| 6 | `pb:fermatnum` | ★★ | Fermat factors and 641 | In-volume |
| 6 | `pb:carmichael` | ★★ | Carmichael structure / Chernick | In-volume |
| 6 | `pb:pratt` | ★★ | Pratt certificates | In-volume |
| 6 | `pb:rabin` | Journey | Monier/Miller–Rabin liar counts | Extension/return |
| 6 | `pb:waring` | ★★★ | Two k-th powers / Waring | Extension/return |
| 6 | `pb:squaresmodpk` | ★★ | Squares mod prime powers | Extension/return |
| 7 | `ex:three` | ★ | Three-square residue obstruction | In-volume |
| 7 | `ex:2026` | ★ | Two-square tests near 2026 | In-volume |
| 7 | `ex:primitive2` | ★★ | Primitive sums of two squares | In-volume |
| 7 | `ex:x2y2` | ★★ | Prime x²+2y² | In-volume |
| 7 | `ex:x3y2` | ★★ | Prime x²+3y² | In-volume |
| 7 | `ex:eureka` | ★★ | Three triangular numbers | Extension/return |
| 7 | `ex:zagier` | ★★★ | Zagier involution proof | In-volume |
| 7 | `ex:t1-which20` | ★ | Which small numbers are two squares | In-volume |
| 8 | `ex:areaper` | ★ | Area=perimeter right triangles | In-volume |
| 8 | `ex:x2y23z2` | ★ | No rational point on x²+y²=3 | In-volume |
| 8 | `ex:catalan23` | ★ | Equation 2^x−3^y=1 | In-volume |
| 8 | `ex:mordell5` | ★★ | Mordell x³−5 | Extension/return |
| 8 | `ex:eisentri` | ★★ | Rational 120° triangles | Extension/return |
| 8 | `ex:markovcoprime` | ★★ | Coprimality of Markov triples | Extension/return |
| 8 | `ex:imo88` | ★★★ | IMO 1988 Vieta descent | Extension/return |
| 8 | `ex:t1-triple` | ★ | Primitive Pythagorean triples | In-volume |
| 9 | `ex:cf415` | ★ | CF of 415/93 and Bézout | In-volume |
| 9 | `ex:cfunique` | ★★ | Irrational CF existence/uniqueness | In-volume |
| 9 | `ex:calendar` | ★★ | Leap-calendar rational models | In-volume |
| 9 | `ex:n21` | ★★ | CF of √(n²+1) / Pell | In-volume |
| 9 | `ex:sqtri` | ★★ | Square triangular numbers | In-volume |
| 9 | `ex:golden` | ★★ | Golden ratio approximation constant | In-volume |
| 9 | `ex:liouville` | ★★★ | Liouville transcendence | In-volume |
| 9 | `ex:t1-pell3` | ★★ | Pell solution for √3 | In-volume |
| 10 | `ex:gaussfactor` | ★ | Gaussian factorisations / gcd | In-volume |
| 10 | `ex:zsqrt5` | ★ | Non-UFD Z[√−5] | In-volume |
| 10 | `ex:gaussgcd` | ★★ | Gaussian Cornacchia gcd | In-volume |
| 10 | `ex:euler1000009` | ★★ | Euler 1,000,009 factorisation | In-volume |
| 10 | `ex:x3y21` | ★★ | Equation x³=y²+1 | In-volume |
| 10 | `ex:xxyy` | ★★ | Eisenstein x²+xy+y² representation | In-volume |
| 10 | `ex:y2x3m2` | ★★★ | Equation y²=x³−2 | In-volume |
| 10 | `ex:t1-split13` | ★ | Gaussian/Eisenstein norm of 13 | In-volume |
| 11 | `ex:t1-char5` | ★ | Character table mod5 | In-volume |
| 11 | `ex:t1-chi8check` | ★ | Character χ8 and (2/p) | In-volume |
| 11 | `ex:t1-sieve30` | ★★ | Legendre sieve at x30,x50 | In-volume |
| 11 | `ex:t1-phi-ratio` | ★★ | Totient Möbius ratio | In-volume |
| 11 | `ex:t1-mu-floor` | ★★ | Möbius floor-sum identity | In-volume |
| 11 | `ex:t1-squarefree` | ★★ | Squarefree sieve identity | In-volume |
| 11 | `ex:t1-char-series` | ★★★ | Summation-by-parts character series | Extension/return |
| 11 | `ex:t1-group3` | ★ | Three grouped χ4 terms | Extension/return |
| 11 | `pb:pseudo` | ★★ | Pseudoprime constructions | In-volume |
| 11 | `pb:pocklington` | ★★ | Pocklington/Proth criterion | In-volume |
| 11 | `pb:fermatquot` | ★★ | Fermat quotient/Lerch | In-volume |
| 11 | `pb:mullin` | ★★ | Mullin prime sequences | In-volume |
| 11 | `pb:artin` | ★★ | Artin safe-prime primitive roots | In-volume |
| 11 | `pb:fermatcubic` | ★★★ | Cubic Gauss/Jacobi sums | Extension/return |
| 11 | `pb:euclidgame` | ★★ | Euclid's subtraction game | In-volume |
| 11 | `pb:pascalthree` | ★★ | Pascal triangle mod3 | In-volume |
| 11 | `pb:powerful` | ★★ | Powerful numbers | Extension/return |
| 11 | `pb:jacobi` | Journey | Jacobi four-square theta proof | Extension/return |
| 11 | `pb:densities` | Journey | Four-square local densities | Extension/return |

## Scope boundary and outstanding release gates

This internal manuscript review and the keyed matrix constitute the **Step 6 source-level editorial acceptance record**; they are **not** formal proofs for every key, external mathematical refereeing, or evidence that the page proofs were inspected. The full mathematical statements and arguments remain in the TeX sources, not reproduced here. CI against the exact latest commit must pass before treating the build as verified. Step 7's adjacent-chapter transitions/listing, Step 8's reading/print PDF and EPUB inspection and matching page-count-derived print wrap, and Step 9 KDP proof and physical checks remain independent gates. PR #97 remains **draft and unmerged**.
