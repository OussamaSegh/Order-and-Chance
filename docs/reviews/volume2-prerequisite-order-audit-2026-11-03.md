# Volume 2 — Step 4 prerequisite and printed-order ledger

**Date:** 3 November 2026
**PR:** #97, editorial/volume2-continuity-foundations-20261103
**Status:** Step 4 source-order/prerequisite gate complete, subject to exact-head CI.
**Not a substitute for:** Step 5 independent proof/example review, Step 6 individual review of the 144 exercise solutions, or Step 8--9 rendered/KDP sign-off.

## Reader contract and audit method

The chapter sequence comes from volume2-integers/main.tex, not from the old numerical chapter filenames. Volume 1 is the only assumed earlier volume. The first reading may skip every section marked optional without losing a proof in the core itinerary. A forward reference is legitimate only as an explicitly signalled preview or a labelled optional challenge, never as an unstated proof hypothesis.

All eleven chapter sources were inspected in printed order. A separate source scan indexed 266 unique labels and classified references by chapter and by whether they occur in an explanatory passage, theorem proof, or exercise/hint/required solution. The scan confirmed zero references to later manuscript labels in the main chapter proofs and zero references to later chapters in **41 one-star exercise statements, hints or required solution bodies**. Solution outlooks introduced by the \leads marker were correctly treated as previews rather than prerequisites. This does not assert that every one-star proof is mathematically correct; that belongs to Steps 5 and 6.

### First-use and proof-location ledger

| Printed chapter | First-use concept or tool | Definition/proof available to reader; prerequisite boundary |
| --- | --- | --- |
| 1 — Divisibility | Euclidean division, subgroup of the integers, gcd/Bézout, Gauss' divisibility lemma | Theorem thm:div, Proposition prop:subgroups, Theorems thm:bezout and thm:gauss prove these here. The elementary group/subgroup test comes from Volume 1's complex-roots chapter and is repeated locally. Well ordering comes from Volume 1's sums/induction chapter. |
| 1 | Prime factorisation, valuations, gcd/lcm and Euclidean algorithm | Theorem thm:fta proves existence and uniqueness using only earlier local results and strong induction. Valuations and their product/min-max rules immediately follow. Euclidean algorithm and Lamé's bound (thm:lame) follow; Fibonacci identities are in Volume 1. |
| 2 — Primes | Euclid's prime infinitude and Euler's reciprocal-prime divergence | Both proved in the opening section; Euler's product comparison uses the Chapter 1 FTA and Volume 1's series/integral tools. Quantitative estimates (lem:binom, thm:cheb) and Bertrand (thm:bertrand) are expressly optional; neither is a premise for Chapter 3. |
| 3 — Congruences | Residue classes, rings/fields, units, modular inverses and totient | Ring and field are defined immediately before prop:ringZn. Proposition prop:units uses Chapter 1 Bézout; it defines unit counting as φ(n), also met in Volume 1 counting. Euler/Fermat thm:eulerthm follows by permuting units, with Wilson thm:wilson proved next. Neither needs Chapter 5's multiplicative-order theorem. |
| 3 | Chinese remainder theorem and divisor-sum counting | Theorem thm:crt uses Bézout and local residue-ring arithmetic; prop:lincong gives the gcd criterion. Gauss' divisor identity prop:phisum is established by reducing fractions, before Chapter 4 uses it. Optional Hensel thm:hensel defines the formal derivative and proves its own simple-root lift rather than presuming Volume 13. |
| 4 — Arithmetic Functions | Arithmetic functions, multiplicativity, τ/σ/φ/μ | Arithmetic functions and multiplicativity are defined in the opening section. τ/σ derive from Chapter 1 FTA; φ/units from Chapter 3; μ is defined here by squarefreeness. No Dirichlet-series theory is needed. |
| 4 | Dirichlet convolution and Möbius inversion | Convolution is defined just before prop:conv; finite associativity and multiplicativity are proved. Theorem thm:mobius proves μ * 1 = ε and the inversion rule. The Euclid--Euler perfect-number result thm:perfect follows from divisor sums. Optional analytic average orders thm:hyperbola reuses Volume 1 harmonic estimates but is not required for Chapter 5. |
| 5 — Primitive Roots | Multiplicative order, cyclic groups and primitive roots | Order is defined at the start of the Orders section and prop:order proves the divisor-of-exponent property using the Chapter 1 subgroup result and Chapter 3 Euler theorem. Cyclic-group vocabulary appears in Volume 1. The prime-field generator theorem thm:cyclic is proved via the polynomial root bound from Volume 1 plus Chapter 3 prop:phisum; cyclicity is not assumed. |
| 5 | Primitive roots modulo prime powers and units modulo powers of 2 | Lemma lem:lift, theorem thm:cyclicn and theorem thm:twopower use the earlier order, CRT, valuations and binomial expansion. All needed group structure for later characters is thus proved in Volume 2, not borrowed from Volume 3. Discrete logs are defined only after primitive roots are proved. |
| 6 — Reciprocity | Legendre symbol, Euler criterion, Gauss' lemma, quadratic reciprocity and Jacobi symbol | Legendre symbol is defined in the first section; thm:eulercrit uses Chapter 5 prime-field cyclicity. thm:gausslemma and thm:qr give the reciprocity law, with lem:eisenstein as a supporting sign formula. The Jacobi symbol is defined after reciprocity and prop:jacobi proves the composite-denominator rules. Gauss-sum alternatives requiring more theory are explicitly optional. |
| 7 — Sums of Squares | Thue's lemma, two-square prime and integer criteria, four squares | lem:thue proves its lattice-box step using Volume 1 pigeonhole; thm:twosq invokes the already proved -1 residue criterion from Chapter 6. thm:twosqn uses Chapter 1 factorisation and the Volume 1 Brahmagupta identity; thm:foursq proves four-square existence. The optional circle-counting theorem thm:circle is not needed in the Diophantine chapter. |
| 8 — Diophantine Equations (source ch09) | Local obstructions, Pythagorean triples, infinite descent | Congruences and valuations are already proved; thm:pyth gives the primitive Pythagorean parametrisation, and thm:fermat4 proves the fourth-power descent from it. The least-counterexample principle is proved in Volume 1. Rational conics (prop:chord), the Mordell example (thm:mordell7), Markov (thm:markov) and Vieta jumping are separate optional explorations and are not premises for continued fractions. |
| 9 — Continued Fractions (source ch08) | Convergents, approximation, best approximation, periodicity | prop:cfconv sets up convergents via Chapter 1 Euclidean division. thm:cfapprox, lem:cfexistence, lem:best, thm:legendre and thm:periodic develop the real approximation route locally; Volume 1 provides elementary real sequences and pigeonhole arguments. |
| 9 | Pell solutions and quadratic norm | The norm N(x+y√d)=x²-dy² is defined and shown multiplicative immediately before thm:pell. That theorem proves a nontrivial norm-one solution and the power classification in this chapter. It does not rely on Chapter 10's quadratic integer rings or Volume 13's unit theorem. |
| 10 — Gaussian and Eisenstein Integers | Ring, integral domain, units, associates, irreducibles, prime elements, norms | The terms are defined in the opening section. Norms are given and multiplied using Volume 1 complex conjugation. prop:quadunits proves the norm-one unit criterion; prop:eucl establishes smaller-norm division in all three specified quadratic rings, including Z[√-2]. |
| 10 | Ring gcd/Bézout, UFD, Gaussian/Eisenstein primes and representation count | thm:ufd proves the Euclidean-domain implications here rather than citing Volume 3; thm:six shows their failure in Z[√-5]. thm:gaussprimes and thm:r2 classify Gaussian primes and two-square representations. χ4 is explicitly defined by residues here before Chapter 11 names it a character. thm:eisprimes, lem:cube and thm:flt3 cover the Eisenstein/cubic route. |
| 11 — Characters and Sieve | Homomorphism, Dirichlet character, orthogonality | The character definition is def:t1-character and the group-homomorphism rule is explained at first use. prop:t1-charsum, prop:t1-unitproduct, thm:t1-charcount and thm:t1-ortho prove existence, count and two orthogonality formulas using the group structures proved in Chapter 5 and roots of unity from Volume 1. No Volume 3 representation theory is assumed. |
| 11 | Convergence, Dirichlet series, Euler products, finite sieve | lem:t1-pseries proves convergence for real s>1; lem:t1-dseries proves absolute-convergence regrouping; thm:t1-eulerprod proves the product and non-vanishing for s>1. thm:t1-sieve is a finite inclusion--exclusion/Möbius identity using Chapter 4. The χ4 series and character-sum bound (prop:t1-chi4series and prop:t1-charbound) form an optional preview; the Dirichlet theorem itself belongs to Volume 6. |

### Forward-reference classifications

**Harmless first-reading previews.** The only cross-chapter forward-label targets in the pre-exercise exposition (including after the source-order fixes) are:

| Printed chapter | Forward target(s) | Why not a premise |
| --- | --- | --- |
| 1 | ch:congruences, ch:continued, ch:gaussian | Explicit later uses of Bézout, Euclid's algorithm and Euclidean rings; no result imported |
| 2 | ch:characters | Prime race and Volume 6 destination; no character theorem used |
| 3 | ch:orders, ch:characters | Terminology and a preview of orders/sieve; the first example defines the return exponent without the later group theorem |
| 4 | ch:orders, ch:characters | Chapter 5 order-count handoff and Chapter 11 sieve preview |
| 5 | ch:characters | Character-count handoff after cyclicity is proved |
| 6 | none | Reciprocity's actual proofs cite earlier tools |
| 7 | ch:gaussian | Later representation-count formula and UFD context explicitly stated not to be used here |
| 8 | ch:gaussian and ex:y2x3m2 | Eisenstein/cubic discussion and a labelled advanced later-chapter exercise; all after the optional-route marker |
| 9 | none | Continued fractions/Pell self-contained |
| 10 | ch:characters | χ4 is defined here; the term Dirichlet character is a preview of the next chapter |
| 11 | none | Final volume chapter |

**Optional exercise/solution cross-references.** The remaining later-label uses after the Exercises headings were classified as follows:

- Chapter 1: pb:fibcoprime deliberately returns after the Chapter 5 pb:gcdmean density work; its instructions already name that dependency. The Chapter 1 probability exercise's required argument now uses elementary product-divisibility counting, not the later CRT.
- Chapter 3: pb:morley now explicitly says to return after Chapter 11 pb:fermatquot, which its hint and solution use. pb:glaisher discloses both Volume 5 Bernoulli theory and Chapter 11 Lerch's congruence. Other Chapter 3 forward character references are destination prose.
- Chapter 4: pb:eisensine, pb:euler and pb:sumsquares are explicitly optional returns after reciprocity/Gauss sums; pb:sumsquares identifies a Volume 4 total-variation input. The pb:euler subgroup half-size estimate is now proved by the two-disjoint-cosets argument, without needing Volume 3 Lagrange's theorem. Later pb:rabin mentions are outlooks. pb:nsq1 is labelled later-volume Volume 6.
- Chapter 6: pb:waring names Chapter 11 character/Jacobi-sum tools; pb:phimodp names Volume 3 finite-field extensions; optional pb:rabin uses the cyclic prime-power unit groups already proved in Chapter 5. The prime-power square-count problem pb:squaresmodpk now proves its integer local--global conclusion directly with odd valuations and a mod-4 obstruction, instead of asserting an unproved existence theorem for primes with a prescribed Legendre symbol.
- Chapters 2, 5, 7, 8 and 10: forward labels in closing editorial prose are previews; Chapter 5 pb:gcdmean and the other explicitly tagged journeys retain their named later prerequisites.
- Chapter 11: later-volume exercises on theta products, algebraic integers and distributional estimates remain labelled optional; Volume 6's Dirichlet theorem is not presumed in the main route.

**Resolution of real or potentially misleading dependencies.**
1. Chapter 1 pb:valuation: fixed the tools/discovery line to use the same elementary divisibility argument the actual proof provides; later CRT moved to outlook.
2. Chapter 3 example: replaced multiplicative-order theorem language with the checked small power and an explicit definition deferred to Chapter 5.
3. Chapter 3 pb:morley and pb:glaisher: named the exact Chapter 11 Fermat quotient input in their prompts and made the return route explicit.
4. Chapter 4 thm:perfect: moved a reference to a forthcoming exercise outside its proof, so no theorem proof cites a later problem.
5. Chapter 4 pb:euler: replaced an apparent reliance on Volume 3 Lagrange with a direct finite-subgroup counting argument.
6. Chapter 6 pb:rabin: relabelled Volume 3 cyclic group theory as outlook; Chapter 5's already-proved prime-power classification is the actual input.
7. Chapter 6 pb:squaresmodpk: removed the unproved nonresidue-prime existence claim. If a nonsquare integer has an odd prime valuation, its residue fails to be a square modulo the next prime power; if it is the negative of a positive square, modulo four times that square gives a contradiction. Thus no analytic prime distribution or p-adic result is assumed.

### Audit evidence and open gates

- **Proof-dependency check:** every referenced local label within a proof in the pre-exercise manuscript is already defined in the same chapter before the reference, or in an earlier printed chapter. Result: **zero future-label proof dependencies**.
- **One-star route check:** 41 one-star questions, matching hints and required full write-ups were scanned for later-label and later-volume prerequisites; outlook text after \leads is not part of the required method. Result: **zero unmarked later-label dependencies** and no same-chapter dependence on a later exercise.
- **Forward-prose review:** all pre-exercise cross-chapter references match the curated preview inventory in the table above; newly introduced targets must be classified before acceptance.
- **Structural invariants:** 11 chapter sources, 144 exercise/hint/solution IDs with matching order, 266 distinct source-local labels, no dangling local \ref/\eqref/\autoref references, and balanced checked LaTeX environments.
- **Regression coverage:** tools/test_volume2_manuscript.py now checks proof-reference ordering, all 41 one-star problem dependency boundaries, the curated forward-preview inventory, the Morley dependency warning and the earlier Step 2/3 guards.
- **Limitations:** source-level scans and targeted prerequisite inspection cannot guarantee every theorem or solution is correct. The end-to-end checking of all proofs, examples and 144 exercises (Steps 5 and 6), latest-head build and visual PDF/EPUB/print inspection (Step 8), and publisher-side KDP/physical proof (Step 9) remain explicitly open. Do not merge or tag on this evidence alone.
