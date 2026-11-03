# Volume 2 — independent per-exercise verification register

**Edition:** manuscript on draft PR #103, initial register created 3 November 2026. **Branch:** `editorial/volume2-independent-proof-and-reader-rewrite-20261103`. **Source snapshot:** branch head `654f869d8ec3e8b98fff5df5b1e7bb1d904212f3` before this file is added.

This register is generated **from the actual 11 chapter sources in printed order**, not copied from an older proof ledger. It lists all 144 keyed exercises; the ordered exercise, hint and solution keys match independently in every chapter at this snapshot. The total is **144**, distributed by chapter **15/11/21/10/16/19/8/8/8/8/20**. Grade distribution: \star: 37; \star\star: 80; \star\star\star: 20; Journey: 7. The manuscript sources, not these static rows, define problem text and source position.

**Meaning of columns:** Pass A = an independent solution without trusting the printed answer; Pass B = genuinely separate symbolic/adversarial reconstruction; earlier-tool check = every needed result proved before this exercise (including hint and full solution). Enter a checker, exact proof link, commit and boundary evidence before changing a status to `VERIFIED_TWICE`. Fifty-two exercises now have two recorded mathematical checks (all fifteen Chapter 1 keys, all eleven Chapter 2 keys, twelve Chapter 3 keys, Morley, the gcd/Fibonacci journeys, the redesigned factorial sum, Ramanujan Journey and the redesigned large-prime-factor exercise, the relocated sums-of-squares problem, the self-contained cyclotomic-factor-degree problem, the cubic Jacobi-sum exercise, the two-kth-powers (Waring) exercise, Jacobi's four-square journey and its local-density follow-up, and the relocated Eisenstein trigonometric and Euler--Jacobi exercises). The Ramanujan problem's second pass separately checked the formal substitutions, cancellation, signs and coefficient extraction; finite computations support but do not prove the general statements. Independent external review and final-head CI remain open. Use `IN_PROGRESS`, `BLOCKED`, `CORRECTED_NEEDS_RECHECK`, `UNREVIEWED`, `VERIFIED_TWICE` only.

| Printed chapter | Key | Grade | Pass A | Pass B | Earlier-tool check | Status | Finding / source |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `ex:bez` | ★ | Euclid/back-substitution | Mod-5 congruence + enumeration | PASS | VERIFIED_TWICE | Reader-level proof in ledger |
| 1 | `ex:gcdn` | ★ | Integer-combination bound | Alternative resultant identity + 10,001 checks | PASS | VERIFIED_TWICE | n=0 and 5 residue classes |
| 1 | `ex:zeros` | ★ | Count powers dividing factorial | Telescope exact-valuation classes + recompute | PASS | VERIFIED_TWICE | v2=994, v5=249 |
| 1 | `ex:sqrt` | ★★ | Prime-valuation parity for square roots and reduced-fraction monic root divisibility | Separate cleared-denominator/prime-divisor contradiction and Bézout–Gauss route; bounded rational probes | PASS | VERIFIED_TWICE | DEP-013: n=0, negative integer roots, q>1 and degree-one endpoints checked; no later tools |
| 1 | `ex:mersgcd` | ★★ | Subtractive Euclidean algorithm on exponents, with exact 2-power remainder identity | Independent exponent Bézout with inverse of 2 modulo odd common divisor; 14,400 gcd pairs | PASS | VERIFIED_TWICE | DEP-013: a=b, a=1, gcd=1 and exponent-zero endpoint; proof only requires earlier Chapter 1 facts |
| 1 | `ex:lame5` | ★★ | Fibonacci–golden-ratio growth | Five-step Fibonacci growth + finite sweep | PASS | VERIFIED_TWICE | 28,680 Euclid pairs |
| 1 | `ex:frob` | ★★ | Canonical 0≤x<b solution and obstruction at ab−a−b | Independent minimum of by over residue classes modulo a; 1,799 coprime pairs including unit denomination | PASS | VERIFIED_TWICE | DEP-013: exact largest missing integer −1 if a=1 or b=1; source clarified, all greater integers covered |
| 1 | `ex:supercat` | ★★★ | Fractional-part floor inequality followed by Legendre valuations of the factorial ratio | Independent floor-carry argument and signed central coefficient via Fourier extraction + Wallis/integration by parts; 1,764 factorial/central-coefficient cases | PASS | VERIFIED_TWICE | DEP-014: m=0, n=0, negative real inputs, m=n=1, coefficient sign and leading factors audited |
| 1 | `ex:n2n` | ★★★ | Smallest prime factor, binomial Fermat proof and prior Mersenne-gcd lemma | Independent finite-residue permutation Fermat proof plus exponent Bézout; 9,999 integers probed | PASS | VERIFIED_TWICE | DEP-014: n even excluded, p odd, gcd(n,p−1)=1, inverse of 2 justified by earlier Bézout |
| 1 | `ex:t1-divisibility-lattice` | ★★ | Bézout's integer-combination subgroup and Gauss' coprime cancellation for intersection | Independent prime-valuation meet/join proof plus 109² exact Bézout witnesses and lattice membership checks | PASS | VERIFIED_TWICE | DEP-014: zero intersection, positive a,b, gcd/lcm and 12/18 union counterexample checked |
| 1 | `ex:t1-binomial-carry` | ★★ | Legendre's floor valuation; two low-digit remainders identify the carry across p^j | Independent digit-sum identity v_p(n!)=(n−s_p(n))/(p−1), digit-column carry recurrence and 21,125 cases | PASS (math; final CI pending) | VERIFIED_TWICE | DEP-015: p=2/3/5/7/11, m,n=0, base-3 carry chain, and first-use base-p notation taught locally |
| 1 | `ex:t1-euclid1071` | ★ | Euclidean remainder chain 147,21,0 and back-substitution u=−3,v=7 | Independent Bezout certificate 7×462−3×1071=21 plus common 21 factor and gcd(51,22)=1 | PASS (math; final CI pending) | VERIFIED_TWICE | DEP-015: fixed prior exact-answer spoiler by changing earlier worked examples to 899,372; 201 solution-family trials for each pair |
| 1 | `pb:valuation` | ★★ | Exact multiple counts, finite tail sums, inclusion–exclusion for fixed prime powers, O(1) level error | Independent periodic reduced-residue count by elementary coprime modulus bijection; weighted tail formula; 27 exact three-prime event counts | PASS (math; final CI pending) | VERIFIED_TWICE | DEP-015: p fixed; k=0, N=1, rare 2-adic outliers, finite/infinite interchange avoided; actual Volume 1 probability proof sites found |
| 1 | `pb:parity` | ★★ | Prime-factor cancellation, independent geometric valuations of a,b and limit-tail truncation from earlier pb:valuation | Independent exact finite pair-residue counts modulo p^K, coprime modulus bijection and error bound, plus 2-prime joint checks | PASS (math; final CI pending) | VERIFIED_TWICE | DEP-016: (a) 1/(p+1), (b) three 1/3 parity outcomes, (c) arbitrary fixed prime family; 12/18 example, unit/finite truncations checked |
| 1 | `pb:orchard` | ★★ | Minkowski rectangle folded into one unit square by area pigeonhole; strict and area-equality cases; ray-strip/tree intersection and rational-slope escaping line | Independent finite-grid mod-1 pigeonhole for rotated rectangles and elementary quadratic distance-to-ray with sharp tangency; 135 rectangle, 2,112 blocking rays and 49 sharp escape radii | PASS (math; current-head CI and rendered figure pending) | VERIFIED_TWICE | DEP-018: area=4 CLOSED, open counterexample, r=1/R equality, u>0, R>=2, strict r<1/sqrt(R²+1), no collinear tree; figure R=11 gives 224/376, slope wording and unproved density repaired |
| 2 | `ex:mod4` | ★ | Complete Euclid 4∏p−1 contradiction, prime-factor residue parity incl empty list | Independent 2∏p+1 construction and modular exclusion; 18 exact finite prime-list probes | PASS (math; latest CI pending) | VERIFIED_TWICE | DEP-022: q≡3 mod4, every listed p fails by remainder −1 or 1, all tools before Chapter 3; illustrated 923=13×71 |
| 2 | `ex:mersenne` | ★ | Composite n factors 2^n−1; odd exponent factor in 2^n+1 yields a proper divisor | Independent modular exponent-divisibility via least factor and n=2^k·odd-part; 110 exponents | PASS (math; latest CI pending) | VERIFIED_TWICE | DEP-022: n=1 endpoints, necessary not sufficient: 2047 and 4294967297 composites factored in source |
| 2 | `ex:germain` | ★ | Sophie Germain square completion (n²−2n+2)(n²+2n+2) | Independent modular proof n²≡2n−2 mod d entails n⁴≡−4 mod d; 999 exact n probes | PASS (math; latest CI pending) | VERIFIED_TWICE | DEP-022: n>1 is essential; n=1 gives prime 5, both factors proper for n≥2 |
| 2 | `ex:fermatnum` | ★★ | Difference-of-squares induction proves product Fn−2, hence pairwise gcd 1 and new primes | Independent finite polynomial telescope at base 2 and direct modular Fn≡2 mod Fm for n>m; 13 products and 78 gcd pairs | PASS (math; latest CI pending) | VERIFIED_TWICE | DEP-022: n=0 empty product=1 clarified; all Fermat numbers odd>1; no primality of individual Fn assumed |
| 2 | `ex:gaps` | ★★ | Factorial run M+j for j=2…n+1 proves length n composite for every n≥1; compares length scales with Bertrand | Independent Bézout-derived residue construction for pairwise distinct primes ensures arbitrary runs; exact finite cases n≤40 | Optional Bertrand theorem proven earlier in printed Chapter 2; finite gcd/proper-divisor check | VERIFIED_TWICE | DEP-023: 4! gives 26,27,28; two scales n vs factorial(n+1), no contradiction with prime between x and 2x |
| 2 | `ex:factorial` | ★★ | Bertrand after floor(n/2) gives prime n/2<p≤n; Legendre v_p(n!)=1 | Separate integer-multiple count p occurs exactly once; kth-power exponent divisibility by FTA; n 2…500 | Earlier Chapter 2 thm:bertrand, earlier Chapter 1 Legendre/FTA; p²>n verified | VERIFIED_TWICE | DEP-023: n=2 floor case; 5! has isolated p=3; prime appears exactly once for all n≥2 |
| 2 | `ex:erdosdiv` | ★★★ | Finite union bound, unique squarefree-square n=ab² smooth decomposition and N=2^(2k+2) contradiction | Independent exponent-vector smooth-count O((ln N)^k)=o(N) contradiction plus direct subset/parity count for specified part (b) | Earlier Chapter 1 FTA/prime valuations and Volume 1 finite probability/sums; no later analytic prime theorem | VERIFIED_TWICE | DEP-023: n=1 included, empty a-subset, infinitely many p>N contribute zero to finite union, strict <N/2 |
| 2 | `ex:furstenberg` | ★★★ | Prove topology axioms, infinite progression, clopen classes, finite-union contradiction using ±1 and 0 | Independent arithmetic basis via x+lcm(b,c)Z and residue-class complement; contradiction against finite open via alternative base argument | Topology axioms explicitly defined inside question; Euclid/FTA from Chapter 1; no prior topology needed | VERIFIED_TWICE | DEP-023: b=1 complement empty, progression infinite, 0 is divisible by every prime, ±1 excluded |
| 2 | `ex:t1-factorial-new-prime` | ★ | If p≤n divides n!+1 it divides n! and consecutive integers, contradiction | Independent modular n!≡0 => n!+1≡1 mod every p≤n; 5!+1=121=11² | Earlier Chapter 1 factorials, prime factors and gcd; n≥2 | VERIFIED_TWICE | DEP-023: all prime factors >n, not entire number prime; exact n=5 counterexample and n≤150 probes |
| 2 | `ex:t1-euclid-sequence` | ★★ | Recursive E_j−1 divisible by any earlier E_i; hence gcd(E_i,E_j)=1 and fresh prime factors | Inductively gcd(P_r,P_r+1)=1 with P_r=∏E_i, proving E_{r+1} coprime to whole prior product; finite E1…E8 | Earlier Chapter 1 FTA, Euclid and divisibility; no later result | VERIFIED_TWICE | DEP-023: E5=1807=13×139 composite; correct E2=3 E3=7 E4=43, pairwise coprime suffices |
| 2 | `ex:t1-prod11` | ★ | List primes 2,3,5,7,11, multiply to 2310; ln2310≈7.745<11ln4≈15.249 | Independent grouping 2×3×5×7×11 and sum of five individual natural logarithms, compare 2310<4^11=4194304 | Earlier Chapter 2 thm:cheb and Volume 1 ln product rule; optional after Chebyshev | VERIFIED_TWICE | DEP-023: numeric computation is demonstration, not a universal proof; 4^11 and all rounded logs cross-checked |
| 3 | `ex:last2` | ★ | Direct 7⁴≡1 mod100 and 2026≡2 mod4, yielding49 | Independent CRT: 7^2026≡1 mod4, ≡−1 mod25, unique residue49 | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: n≥0 exponent, modulus100 via Euclid; exact pow checks |
| 3 | `ex:sunzi` | ★ | Progression 8+15t, solve t≡1 mod7 gives23 mod105 | Independent combine identical remainders mod3,7 as x≡2 mod21, then solve mod5 | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: full family 23+105k; moduli pairwise coprime |
| 3 | `ex:digits` | ★ | Decimal polynomial 10≡1 mod9 and −1 mod11, sign reversal for negative | Independent divisibility factor 10^i−1 by9 and 10^i−(−1)^i by11; negative via additive inverses | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: n=0, −12 examples; exact signed digit tests |
| 3 | `ex:sqrt1` | ★★ | For odd p, p cannot divide both x−1 and x+1, hence ±1 modp^k; CRT 2^r | Independent valuation v_p product and all sign-vector CRT reconstruction; n1 empty product checked | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: all odd moduli≤301 enumerated; n=1 yields one root |
| 3 | `ex:wilsonconv` | ★★ | Composite ab with distinct a,b or square a² using a,2a; n=4 exception | Independent Legendre prime-power valuation of (n−1)! for all composite n>4; Wilson primes | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: n2, n3, exceptional n4; factorial residues n≤300 |
| 3 | `ex:hensel` | ★★ | Both starting roots2,3 mod5 uniquely lifted to7,18 mod25 then57,68 mod125 | Independent base-five digit expansion solves quadratic congruences directly, checks both branches complete | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: 57²+1=26×125, 68²+1=37×125 |
| 3 | `ex:tower` | ★★ | Euler exponent reduction mod40, 3^27≡27 mod40 then power period20 gives87 | Independent CRT modulo4 and25, exponent3^27 mod20≡7, root x≡3 mod4 and12 mod25 | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: exact modular power checks, full tower handled |
| 3 | `ex:korselt` | ★★ | For each p|squarefree n, nonunit case zero, unit Fermat n−1 multiple p−1, CRT | Independent polynomial factor X^n−X=(X^p−X)Σ X^{j(p−1)} mod each prime, product of primes | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: 561=3×11×17, 560 divisible2,10,16; all 561 residues checked |
| 3 | `ex:lucas` | ★★★ | Freshman dream (1+X)^{p^j}=1+X^{p^j}, coefficient digit extraction | Independent one-digit recursion n=pq+r,k=ps+t via (1+X^p)^q(1+X)^r, induct on digits | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: n,k≥0 added; k>n convention; 2≤p≤13, all n≤150 and k≤n+4 checked |
| 3 | `ex:t1-toy-rsa` | ★★ | CRT mod5,11 Fermat for units and zero for nonunits gives m^81≡m mod55 | Independent finite-field polynomial X^81−X multiple of X^5−X and X^11−X; exhaustive55 residues | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: cipher12→23→12; Euler alone does not apply to nonunits |
| 3 | `ex:t1-two-power-roots` | ★★★ | Track exact 2-adic valuations of (x−1)(x+1), force ±1 mod2^(k−1), four lifts | Independent x=1+2t gives 2^(k−2)|t(t+1); consecutive factors coprime and each parent has two lifts | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: k1 one, k2 two, k≥3 four distinct; tested k≤13 |
| 3 | `ex:t1-sunzi23` | ★ | Reassigned genuinely distinct CRT puzzle mod4,9,11: x=21+36s, s≡9 mod11 gives345 | Independent Bézout CRT idempotents 297,352,144 yield 345 mod396, uniqueness | PASS (math; current-head CI pending) | VERIFIED_TWICE | DEP-026: previous duplicate Sunzi23 question replaced; stable legacy label retained for crossrefs; new answer345, not23 |
| 3 | `pb:primepoly` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `pb:fpfunctions` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `pb:aks` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `pb:wolsten` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `pb:jacobsthal` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `pb:morley` | ★★ | Binomial/harmonic reconstruction | Adversarial modulus audit + primes ≤997 | PASS | VERIFIED_TWICE | DEP-003, no Chapter 11 input |
| 3 | `pb:glaisher` | ★★★ | Fermat/Wilson quotient product proof | Adversarial modulus check + 24 primes ≤97 | PASS | VERIFIED_TWICE | Replaced old Bernoulli question; documented in main ledger |
| 3 | `pb:ramanujan5` | Journey | Coefficientwise Jacobi/Euler derivation | Adversarial second symbolic audit + 1,207 independent coefficients | PASS | VERIFIED_TWICE | No Volume 5 dependency; details in main ledger |
| 3 | `pb:kloosterman` | ★★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:360` | ★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:muid` | ★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:sigmaodd` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:coprimesum` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:even` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:oddperfect` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:primitive` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:coprimeprob` | ★★★ | — | — | — | UNREVIEWED | — |
| 4 | `ex:t1-mu12` | ★ | — | — | — | UNREVIEWED | — |
| 4 | `pb:nsq1` | ★★★ | Chebyshev/factorial prime-sum proof | Independent prime-power root, endpoint and asymptotic audit | PASS | VERIFIED_TWICE | Replaced P(x)>x by P(x)>x^(1−δ) for fixed δ>0; see main ledger |
| 5 | `ex:findroots` | ★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:period` | ★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:fermatfactor` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:powersum` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:kth` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:gausswilson` | ★★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:cyclotomic` | ★★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:t1-units16` | ★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:t1-square-cosets` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `ex:t1-gen7` | ★ | — | — | — | UNREVIEWED | — |
| 5 | `pb:smith` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `pb:lambert` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `pb:ramsum` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `pb:phipm1` | ★★ | — | — | — | UNREVIEWED | — |
| 5 | `pb:gcdmean` | Journey | Four-part Möbius/harmonic proof | Abel alternate mean + weighted endpoint + numeric tests | PASS | VERIFIED_TWICE | DEP-002, W(M) uniform for M≥1 |
| 5 | `pb:fibcoprime` | Journey | Fibonacci gcd/Binet solution | Exact bounded-log factor + independent counts | PASS | VERIFIED_TWICE | DEP-001, follows pb:gcdmean |
| 6 | `ex:minus3` | ★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:onemod4` | ★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:minus2` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:mersfactor` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:consecutive` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:pepin` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:gausssum` | ★★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:t1-residue-chance` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `ex:t1-res11` | ★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:primsum` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:phimodp` | ★★ | Quotient field from polynomial Bézout; multiplicative product and degree bound | Independent Frobenius-orbit polynomial proof; 275 finite-field factor pairs, 70 prime-power congruences, 40 trial-factor and 44 index checks | PASS | VERIFIED_TWICE | DEP-008: no Volume 3 extension theorem; n≥2, p∤n; p=2 and m=1 cases checked |
| 6 | `pb:fermatnum` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:carmichael` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:pratt` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:rabin` | Journey | — | — | — | UNREVIEWED | — |
| 6 | `pb:squaresmodpk` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:eisensine` | Journey | De Moivre polynomial, distinct sin-squared roots, signed half-residue Gauss lemma, symmetric double product | Independent odd-index Chebyshev recurrence, Legendre/negative-q sine probes and full reciprocity sign audit | PASS | VERIFIED_TWICE | DEP-012: q=1/negative q and p≠q checked; Volume 1 trigonometry + earlier Chapter 6 only; peer review pending |
| 6 | `pb:euler` | ★★ | Kernel of Jacobi-weighted power map; squareful primitive-root obstruction and squarefree CRT nonresidue witness | Independent local-modulus contradiction and coset-cardinality proof; exact enumeration of Euler liar subgroups for odd composites ≤401 | PASS | VERIFIED_TWICE | DEP-012: lifts of primitive roots from p² to p^e now explicitly taught; no Volume 3 Lagrange theorem; peer review pending |
| 6 | `pb:sumsquares` | ★★ | Hyperbola change of variables; recurrence N(n+2) from N(n) | Independently reconstructed earlier Gauss-sum route; 2,608 exact residue/count checks plus direct tuple checks | PASS | VERIFIED_TWICE | DEP-007: no Volume 4 definition or future Gauss sum; new elementary proof, prime p odd, n≥1, c=0 included |
| 7 | `ex:three` | ★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:2026` | ★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:primitive2` | ★★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:x2y2` | ★★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:x3y2` | ★★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:eureka` | ★★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:zagier` | ★★★ | — | — | — | UNREVIEWED | — |
| 7 | `ex:t1-which20` | ★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:areaper` | ★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:x2y23z2` | ★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:catalan23` | ★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:mordell5` | ★★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:eisentri` | ★★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:markovcoprime` | ★★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:imo88` | ★★★ | — | — | — | UNREVIEWED | — |
| 8 | `ex:t1-triple` | ★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:cf415` | ★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:cfunique` | ★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:calendar` | ★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:n21` | ★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:sqtri` | ★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:golden` | ★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:liouville` | ★★★ | — | — | — | UNREVIEWED | — |
| 9 | `ex:t1-pell3` | ★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:gaussfactor` | ★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:zsqrt5` | ★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:gaussgcd` | ★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:euler1000009` | ★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:x3y21` | ★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:xxyy` | ★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:y2x3m2` | ★★★ | — | — | — | UNREVIEWED | — |
| 10 | `ex:t1-split13` | ★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-char5` | ★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-chi8check` | ★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-sieve30` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-phi-ratio` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-mu-floor` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-squarefree` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-char-series` | ★★★ | — | — | — | UNREVIEWED | — |
| 11 | `ex:t1-group3` | ★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:pseudo` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:pocklington` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:fermatquot` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:mullin` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:artin` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:fermatcubic` | ★★★ | Full four-part character/Jacobi/Gauss/norm proof, cubic congruence by three-cycle, norm uniqueness by Chapter 10 UFD | Independent discrete-log and (omega-1)^2=-3omega congruence, reconstructed Gauss/Jacobi sums, 22-prime brute solution and unique-norm checks | PASS | VERIFIED_TWICE | DEP-009: no Volume 13; p>=7, p=7/13 examples, units and conjugation checked; external peer review pending |
| 11 | `pb:euclidgame` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:pascalthree` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:powerful` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:jacobi` | Journey | Formal triple-product, double-series parity split, logarithmic derivatives, divisor extraction and lattice proof | Independent symbolic coefficientwise product audit, annulus-volume squeeze, 156-term exact identities and 10^7 divisor-sum check | PASS | VERIFIED_TWICE | DEP-011: four-ball volume proved locally; every part (a)-(f), hints and non-Volume-5 prerequisite checked; external review pending |
| 11 | `pb:densities` | Journey | Odd-prime primitive lifting, nonprimitive recursion, exact 2-adic pairing, base-eight vector counts, Euler-product reconciliation | Independent cyclic convolution of four-square residues at prime powers, symbolic valuation-case audit and global divisor-count agreement for n≤300 | PASS | VERIFIED_TWICE | DEP-011: two-adic unit vector and mod8 coefficient table explained locally; p=2,3,5 finite regressions; external review pending |
| 11 | `pb:waring` | ★★★ | Multiplicative-character root count, Jacobi pair classification and positive-bound inequality | Independent additive-Fourier/Gauss derivation; 3,658 (p,k,c) Jacobi-vs-direct checks and independent Fourier tests | PASS | VERIFIED_TWICE | DEP-010: e(t) defined at first use; zero, k=2 and gcd(k,p−1) cases checked; external review pending |

## Update discipline

- Preserve the exact stable key. If a problem is redesigned or deleted, record the old and new mathematical obligation and justification in the main review ledger and PR comment.
- Review the prompt, hint, idea, full derivation, notation, exceptional cases, chapter-order references and final display. A numerical sample cannot certify a general identity.
- Keep all review claims tied to an exact source commit. Changing an exercise, prerequisite theorem or its hint reopens its affected verification status.
- The original manuscript tests check matching keys and numeric cases, but **do not establish mathematical correctness**. A row changes status only after the main ledger records both mathematical checks; four Chapter 1 rows now meet that standard, while the remaining rows do not.
- See `docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md` for gates P06/P07; `docs/reviews/volume2-independent-verification-ledger-2026-11-03.md` for current blockers and next exact task.
