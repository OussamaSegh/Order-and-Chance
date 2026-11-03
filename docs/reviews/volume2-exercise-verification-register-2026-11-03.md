# Volume 2 — independent per-exercise verification register

**Edition:** manuscript on draft PR #103, initial register created 3 November 2026. **Branch:** `editorial/volume2-independent-proof-and-reader-rewrite-20261103`. **Source snapshot:** branch head `654f869d8ec3e8b98fff5df5b1e7bb1d904212f3` before this file is added.

This register is generated **from the actual 11 chapter sources in printed order**, not copied from an older proof ledger. It lists all 144 keyed exercises; the ordered exercise, hint and solution keys match independently in every chapter at this snapshot. The total is **144**, distributed by chapter **15/11/21/10/16/19/8/8/8/8/20**. Grade distribution: \star: 37; \star\star: 80; \star\star\star: 20; Journey: 7. The manuscript sources, not these static rows, define problem text and source position.

**Meaning of columns:** Pass A = an independent solution without trusting the printed answer; Pass B = genuinely separate symbolic/adversarial reconstruction; earlier-tool check = every needed result proved before this exercise (including hint and full solution). Enter a checker, exact proof link, commit and boundary evidence before changing a status to `VERIFIED_TWICE`. Twenty-four exercises now have two recorded mathematical checks (ten Chapter 1 keys, Morley, the gcd/Fibonacci journeys, the redesigned factorial sum, Ramanujan Journey and the redesigned large-prime-factor exercise, the relocated sums-of-squares problem, the self-contained cyclotomic-factor-degree problem, the cubic Jacobi-sum exercise, the two-kth-powers (Waring) exercise, Jacobi's four-square journey and its local-density follow-up, and the relocated Eisenstein trigonometric and Euler--Jacobi exercises). The Ramanujan problem's second pass separately checked the formal substitutions, cancellation, signs and coefficient extraction; finite computations support but do not prove the general statements. Independent external review and final-head CI remain open. Use `IN_PROGRESS`, `BLOCKED`, `CORRECTED_NEEDS_RECHECK`, `UNREVIEWED`, `VERIFIED_TWICE` only.

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
| 1 | `ex:t1-binomial-carry` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:t1-euclid1071` | ★ | — | — | — | UNREVIEWED | — |
| 1 | `pb:valuation` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `pb:parity` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `pb:orchard` | ★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:mod4` | ★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:mersenne` | ★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:germain` | ★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:fermatnum` | ★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:gaps` | ★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:factorial` | ★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:erdosdiv` | ★★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:furstenberg` | ★★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:t1-factorial-new-prime` | ★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:t1-euclid-sequence` | ★★ | — | — | — | UNREVIEWED | — |
| 2 | `ex:t1-prod11` | ★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:last2` | ★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:sunzi` | ★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:digits` | ★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:sqrt1` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:wilsonconv` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:hensel` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:tower` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:korselt` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:lucas` | ★★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:t1-toy-rsa` | ★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:t1-two-power-roots` | ★★★ | — | — | — | UNREVIEWED | — |
| 3 | `ex:t1-sunzi23` | ★ | — | — | — | UNREVIEWED | — |
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
