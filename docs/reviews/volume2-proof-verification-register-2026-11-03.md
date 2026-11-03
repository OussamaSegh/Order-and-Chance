# Volume 2 — named mathematical result verification register

**Initial audit snapshot:** 3 November 2026, branch `editorial/volume2-independent-proof-and-reader-rewrite-20261103`, source head `b88f49510f821cec3e74b37a1f539ee16f004f7f` (before creating this register). Printed order matters: sources `ch09-diophantine` and `ch08-continued-fractions` are printed Chapters 8 and 9.

This list enumerates **all 72 named theorem/proposition/lemma/corollary environments** found directly in the eleven current chapter sources, per chapter **6/5/8/4/6/6/5/5/7/9/11**. It is **not** an enumeration of every proof obligation: informal assertions, examples, exercises, figure claims, identities in prose and unnamed arguments must receive separate audits. For unlabeled results use the synthetic `file:type:ordinal` key until a permanent LaTeX label is provided. Source line numbers may move.

**Two-pass gate:** First pass reconstructs the exact claim and proof from earlier permitted tools, with all quantifiers/edge cases. Second pass independently checks the chain using a different argument or an adversarial symbol-by-symbol reconstruction and finite tests when meaningful. Store assumptions, first-use dependencies, actual calculation, deficiencies, exact commit and separate checker evidence in the main ledger before marking VERIFIED_TWICE. If a named theorem changes, reopen every theorem and exercise that depends on it.

| Printed chapter | Label / stable review key | Heading | First proof check | Second proof check | State | Evidence |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `thm:div` | Euclidean division | Recorded in ledger | Recorded in ledger | VERIFIED_TWICE | 2 proof routes in main verification ledger |
| 1 | `prop:subgroups` | proposition | Recorded in ledger | Recorded in ledger | VERIFIED_TWICE | 2 proof routes in main verification ledger |
| 1 | `thm:bezout` | B\'ezout | Recorded in ledger | Recorded in ledger | VERIFIED_TWICE | 2 proof routes in main verification ledger |
| 1 | `thm:gauss` | Gauss' lemma | Recorded in ledger | Recorded in ledger | VERIFIED_TWICE | 2 proof routes in main verification ledger |
| 1 | `thm:fta` | fundamental theorem of arithmetic | Recorded in ledger | Recorded in ledger | VERIFIED_TWICE | Prime case and induction made explicit at b0273852 |
| 1 | `thm:lame` | Lam\'e | Recurrence induction logged | Independent Fibonacci-minimality audit + finite sweep | VERIFIED_TWICE | Proof ledger, 28,680 division pairs |
| 2 | `thm:euclid-primes` | Euclid | Prime-product contradiction logged | Independent factorial-plus-one construction | VERIFIED_TWICE | Empty-list edge corrected, commit 514541c6 |
| 2 | `thm:euler` | Euler | Euler product and harmonic inequality logged | Power-series log-tail audit + numeric check | VERIFIED_TWICE | Proof ledger; numeric range 2–15000 |
| 2 | `lem:binom` | central binomial lemma (three parts) | Pascal-row and Legendre valuation reconstruction, all low-n hypotheses | Independent induction for B_n, odd central recurrence and base-p carry proof; 7,197 exact (n,p) checks | VERIFIED_TWICE | DEP-019: n≥1, n≥5 restriction is essential (n=2,p=2 counterexample), p^a≤2n precisely stated; no later prerequisites |
| 2 | `thm:cheb` | Chebyshev-type bounds | Prime-product odd-index induction with exact integer-to-real floor step; prime factors of central binomial and asymptotic log inequalities | Independent even/odd half-interval prime-product induction and factorial-ratio/carry estimate; 1,200 primorial and 5,000 π checks | VERIFIED_TWICE | DEP-020: all real x≥1, all n≥1 including π(2)=1 equality; explicit x≥16 lower constant; actual Volume 1 ln/MVT sites |
| 2 | `thm:bertrand` | Bertrand's postulate; Chebyshev–Erdős elementary bounds | Entire 11-prime covering chain for 1≤n≤630 and central-binomial contradiction n≥631; exact h(512), derivative signs | Separate primality/case verification and independent monotone h(n)/n route, complete prime-factor ledger; finite prime/growth regressions | VERIFIED_TWICE | DEP-021: n=1 upper equality, n=630/631 transition, h(n)>0 uniformly for real n≥512, not merely sampled; actual Volume 1 MVT site |
| 3 | `prop:ringZn` | proposition | Quotient residue operations well-defined by integer divisibility, ring laws and n Euclidean classes | Independent canonical remainder quotient/operation coherence, exact associativity and 0=1 zero-ring endpoint | VERIFIED_TWICE | DEP-024: n≥1; full ring axioms, residue arithmetic and n=1 singleton; 50 moduli with representative cross-checks |
| 3 | `prop:units` | proposition | Bézout inverse iff gcd(a,n)=1, p prime field criterion, φ(n) units | Independent finite multiplication-permutation injection via Gauss plus nonunit gcd obstruction; 80 exhaustive moduli | VERIFIED_TWICE | DEP-024: defined φ(n) before use, special Z/1Z zero ring not field, φ(1)=1; actual finite permutation witnesses |
| 3 | `thm:eulerthm` | Euler, Fermat | Product-of-all-units permutation and cancellation, φ(p)=p−1 | Independent cyclic subgroup orbit partition proves order divides φ(n); checked n≤400 | VERIFIED_TWICE | DEP-024: explicit n≥1 modulus hypothesis, n=1 congruence trivial, p=2 Fermat edge; no unproved Lagrange import |
| 3 | `thm:wilson` | Wilson | Pairs inverse classes in F_p; only self-inverses ±1, p=2 checked | Independent polynomial X^(p−1)−1=∏(X−a) by Euler+Volume1 polynomial roots, compare constant; 31 polynomial probes | VERIFIED_TWICE | DEP-024: uses earlier Volume 1 prop:rootsfactor; p=2 sign coincidence and exact factorial tests |
| 3 | `thm:crt` | Chinese remainder theorem | — | — | UNREVIEWED | — |
| 3 | `prop:lincong` | linear congruences | — | — | UNREVIEWED | — |
| 3 | `prop:phisum` | Gauss | — | — | UNREVIEWED | — |
| 3 | `thm:hensel` | Hensel's lemma | — | — | UNREVIEWED | — |
| 4 | `prop:conv` | proposition | — | — | UNREVIEWED | — |
| 4 | `thm:mobius` | M\"obius inversion | — | — | UNREVIEWED | — |
| 4 | `thm:perfect` | Euclid--Euler | — | — | UNREVIEWED | — |
| 4 | `thm:hyperbola` | Dirichlet | — | — | UNREVIEWED | — |
| 5 | `prop:order` | proposition | — | — | UNREVIEWED | — |
| 5 | `thm:cyclic` | Gauss | — | — | UNREVIEWED | — |
| 5 | `lem:lift` | lemma | — | — | UNREVIEWED | — |
| 5 | `thm:cyclicn` | theorem | — | — | UNREVIEWED | — |
| 5 | `thm:twopower` | theorem | — | — | UNREVIEWED | — |
| 5 | `cor:mod8squares` | corollary | — | — | UNREVIEWED | — |
| 6 | `thm:eulercrit` | Euler's criterion | — | — | UNREVIEWED | — |
| 6 | `thm:gausslemma` | Gauss' lemma | — | — | UNREVIEWED | — |
| 6 | `cor:two` | corollary | — | — | UNREVIEWED | — |
| 6 | `thm:qr` | quadratic reciprocity; Gauss, 1796 | — | — | UNREVIEWED | — |
| 6 | `lem:eisenstein` | Eisenstein | — | — | UNREVIEWED | — |
| 6 | `prop:jacobi` | proposition | — | — | UNREVIEWED | — |
| 7 | `lem:thue` | Thue | — | — | UNREVIEWED | — |
| 7 | `thm:twosq` | Fermat, 1640; Euler, 1749 | — | — | UNREVIEWED | — |
| 7 | `thm:twosqn` | theorem | — | — | UNREVIEWED | — |
| 7 | `thm:foursq` | Lagrange, 1770 | — | — | UNREVIEWED | — |
| 7 | `thm:circle` | Gauss | — | — | UNREVIEWED | — |
| 8 | `thm:pyth` | theorem | — | — | UNREVIEWED | — |
| 8 | `thm:fermat4` | Fermat | — | — | UNREVIEWED | — |
| 8 | `prop:chord` | proposition | — | — | UNREVIEWED | — |
| 8 | `thm:mordell7` | a Mordell equation | — | — | UNREVIEWED | — |
| 8 | `thm:markov` | Markov, 1879 | — | — | UNREVIEWED | — |
| 9 | `prop:cfconv` | proposition | — | — | UNREVIEWED | — |
| 9 | `thm:cfapprox` | theorem | — | — | UNREVIEWED | — |
| 9 | `lem:cfexistence` | An infinite expansion determines its number | — | — | UNREVIEWED | — |
| 9 | `lem:best` | best approximation | — | — | UNREVIEWED | — |
| 9 | `thm:legendre` | Legendre | — | — | UNREVIEWED | — |
| 9 | `thm:periodic` | Euler, Lagrange | — | — | UNREVIEWED | — |
| 9 | `thm:pell` | Lagrange, 1768 | — | — | UNREVIEWED | — |
| 10 | `prop:quadunits` | proposition | — | — | UNREVIEWED | — |
| 10 | `prop:eucl` | Euclidean division | — | — | UNREVIEWED | — |
| 10 | `thm:ufd` | theorem | — | — | UNREVIEWED | — |
| 10 | `thm:six` | theorem | — | — | UNREVIEWED | — |
| 10 | `thm:gaussprimes` | theorem | — | — | UNREVIEWED | — |
| 10 | `thm:r2` | Jacobi | — | — | UNREVIEWED | — |
| 10 | `thm:eisprimes` | theorem | — | — | UNREVIEWED | — |
| 10 | `lem:cube` | lemma | — | — | UNREVIEWED | — |
| 10 | `thm:flt3` | Euler; Gauss | — | — | UNREVIEWED | — |
| 11 | `prop:t1-charsum` | proposition | — | — | UNREVIEWED | — |
| 11 | `prop:t1-unitproduct` | proposition | — | — | UNREVIEWED | — |
| 11 | `thm:t1-charcount` | theorem | — | — | UNREVIEWED | — |
| 11 | `thm:t1-ortho` | orthogonality | — | — | UNREVIEWED | — |
| 11 | `lem:t1-pseries` | lemma | — | — | UNREVIEWED | — |
| 11 | `lem:t1-dseries` | lemma | — | — | UNREVIEWED | — |
| 11 | `thm:t1-eulerprod` | Euler product | — | — | UNREVIEWED | — |
| 11 | `cor:t1-mu-zeta` | corollary | — | — | UNREVIEWED | — |
| 11 | `thm:t1-sieve` | Legendre | — | — | UNREVIEWED | — |
| 11 | `prop:t1-chi4series` | proposition | — | — | UNREVIEWED | — |
| 11 | `prop:t1-charbound` | proposition | — | — | UNREVIEWED | — |

## Complementary records

- The eight `VERIFIED_TWICE` rows are documented in full under the two named proof-audit checkpoints in `docs/reviews/volume2-independent-verification-ledger-2026-11-03.md`. All other named results remain UNREVIEWED under the new standard.
- `docs/reviews/volume2-exercise-verification-register-2026-11-03.md` indexes all 144 problem and solution keys, not these 72 results.
- The plan `docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md` requires **all** unnamed proof passages, equations and examples as well. This register is an accountability tool, **not** a mathematics certificate.
