# Batch H — Quadratic fields, ideals and class groups

## Changes implemented
Split old Chapter 11 into 11 Quadratic Fields and Their Integers and 12 Ideals, Prime Splitting and Class Groups; p-adics is consequently 13. Reworked the integrality proof with a complete monic-divisor/primitive-polynomial argument. Added embedding/unit examples, two exercise triples, precise quotient-ring construction, ideal sum/intersection rules, ideal CRT, a proved norm-as-index proposition and a concrete binary-form bridge. Corrected the inert-2 norm in its solution.

## Mathematical improvements
The rational scalar in the original proof is not assumed integral: the revised proof derives it from leading coefficients and primitive contents. Rechecked quadratic integer parity, norm +/-1 units, finiteness below a real unit bound, two-generator lattice independence, conjugate ideals, multiplicative norms, cancellation, containment/division, maximal ideal primality, induction and uniqueness of ideal factorization. The norm/index proof uses ideal factorization already established, so it creates no circular dependency. Splitting of odd primes and the separate four cases at 2 remain fully proved.

The class-number-two proof retains its exact 9/16 approximation bound. Binary forms are restricted to the explicit discriminant -20 calculation and its proved class interpretation; no general form-class correspondence is assumed. The new d=13 unit/Pell exercise distinguishes the maximal order from its smaller integer-coordinate subring.

## Pedagogical improvements
Element integrality and units now form a prerequisite stage before ideals. Ideal multiplication is explained as sums of products, and concrete residue switches connect it with ordinary CRT. The direction of containment and the difference between element norm and ideal norm are retained and reinforced.

## Content preservation
All original eight advanced exercises survive: ringint/goldenunit move with their triples to 11, while the other six remain with ideals in 12. The sqrt10 exercise deliberately stays in 12 because its class-number conclusion would be premature in 11. All old numbered results, the entire original ideal-factorization proof, historical opening, illustrations and bibliography survive. Total exercises: 100 (97 original, three new).

## Verification
Full production PDF build passes all gates, 185 interior pages and 173 whole boxes. PDFs/logs in `/workspace/volume1-checkpoints/H/`; inventory/diff checks pass. Independent lattice computations verify the original ideal products and representative conjugate-norm identities, including inert index 4. Exact symbolic calculation verifies epsilon_13^3=18+5 sqrt(13), epsilon_13^6=649+180 sqrt(13) and norm 1. The new norm/index argument received a separate statement-to-proof dependency review, including k=0 and nonprincipal ideals.

## Remaining issues
Final second-pass review and exercise ledger remain; p-adic fraction/completeness explanations are next. The page target is an editorial guide, not a quota; expansion remains focused on actual gaps.

## Next work
Batch I: explicitly construct Qp and prove its completeness and Zp's covering compactness.
