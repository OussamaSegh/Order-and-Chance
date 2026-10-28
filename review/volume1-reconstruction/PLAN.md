# Evidence-based revision plan

Baseline: a65d685, actual available Volume 0 is its completed ten-chapter revision. Inventory files give source locations, semantic labels, dependencies, full-unit hashes and migration destinations. A hash match establishes preservation, never mathematical correctness.

## Architecture decision
Use thirteen chapters: 1 Divisibility; 2 Primes; 3 Congruences; 4 Orders and primitive roots (old 5); 5 Reciprocity (old 6); 6 Arithmetic functions (old 4); 7 Sums of squares; 8 Continued fractions/Pell; 9 Diophantine methods; 10 Gaussian/Eisenstein; 11 Quadratic fields and their integers; 12 Ideals, prime splitting and class groups; 13 p-adic numbers (old 12).

Move the totient divisor-sum identity, with its counting proof, from arithmetic functions to Chapter 3, where totients are already defined. Its inversion consequence stays in arithmetic functions. This removes the only essential dependency preventing the preferred early order. Split old Chapter 11 at the introduction of ideals: integer rings and units are needed before ideals, and the two kinds of factorization deserve separate learning stages. Retain the norm/conjugate-ideal approach to Dedekind factorization, not a replacement with an assumed graduate theorem.

## Classification and batch scope

| Batch | Classification and justified work |
|---|---|
| B | Missing prerequisite: elementary self-contained Fermat route for exercise n2n. Boundary conventions for gcd, signed inputs, coin problem. Distinguish trial primality testing from factorization and input digit cost. |
| C | Structural correction: move roots to 4, reciprocity to 5, functions to 6; move totient identity to 3. Define ring maps. Prove field-root bound locally. Audit existing Euler/CRT/lifting proofs and solutions. |
| D | Pedagogical precision: both reciprocity proofs, remove brittle Volume 0 numbers, identify Legendre symbol as a first character without general character theory; retain existing rigorous coprime density exercise, quantify its error. |
| E | Proof dependencies: establish continued-fraction uniqueness before its use in periodicity; make foundational exercise rating reflect its depth. Preserve four-square proof and both approximation metrics. Qualify time-sensitive circle-bound claims by their dated references. |
| F | Essential expansion: congruence and valuation obstructions with worked successes and failures, method-selection workshop using actual equations; preserve parametrization/descent/Vieta proofs. |
| G | Missing algebra language and proof precision: integral domains and prime elements; exceptional lambda factors, units and descent audited. Preserve three Euclidean rings and all original exercises. |
| H | Highest priority: split fields/ideals, fully justify monic-divisor argument, concrete ideal products and quotient arithmetic, ideal factorization/class number review, norm-4 inert correction. Short binary-form bridge only with explicit proved identity and clear limits. |
| I | Missing prerequisites: construct Qp from fractions, establish extension of valuation, density/completeness, compactness with metric definition; retain Newton/Ostrowski proofs and actual precision examples. |
| J | Integration: 6–10 bridge exercises counting existing strong examples; selected new problems with both discovery and write-up. Update preface, routes, prerequisites, field guide and publishing instructions. |
| K | Separate second-pass review of all 81 original numbered results and all 97 original solutions, plus additions; exact arithmetic/symbolic calculations and mathematical figure data checks. Correct findings before completion. |
| L | Complete PDF/EPUB/HTML build; source preservation and navigation checks; EPUBCheck and browser review; representative pages of all thirteen chapters; deliver actual artifacts and reproducible reports. |

Unnecessary additions: general Galois theory, a full character theory, general Dedekind-domain machinery, binary-form reduction/composition theory, measure-theoretic random integers, arbitrary-length elementary exercise drills. None is required to repair the actual manuscript.

## Foundational contract
Use the standard integer/real/complex systems; induction and well-ordering; finite counting; elementary polynomial division, gcd/Bézout and Gauss/Eisenstein arguments; real completeness, convergence, absolute rearrangement, logarithm and elementary calculus; finite vector-space/determinant language. Volume 0 supplies these by concept. Reprove small algebra facts when new coefficient rings make their scope important. The Basel value is an explicitly identified Volume 0 result, not a new assumption. Introduce all groups/rings/ideals/quotient and fraction constructions used here. Advanced outlooks (PNT, three-square converse, full unit theorem, Hasse–Minkowski, Selmer, class-field theory) remain identified and referenced rather than claimed proved.
