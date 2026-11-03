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
| 1 | `thm:lame` | Lam\'e | — | — | UNREVIEWED | — |
| 2 | `ch02-primes:theorem:1` | Euclid | — | — | UNREVIEWED | Unlabeled theorem; source line 37 |
| 2 | `thm:euler` | Euler | — | — | UNREVIEWED | — |
| 2 | `lem:binom` | lemma | — | — | UNREVIEWED | — |
| 2 | `thm:cheb` | Chebyshev-type bounds | — | — | UNREVIEWED | — |
| 2 | `thm:bertrand` | Bertrand's postulate; Chebyshev's proof, and Erd\H{o}s's elementary proof (1932) | — | — | UNREVIEWED | — |
| 3 | `prop:ringZn` | proposition | — | — | UNREVIEWED | — |
| 3 | `prop:units` | proposition | — | — | UNREVIEWED | — |
| 3 | `thm:eulerthm` | Euler, Fermat | — | — | UNREVIEWED | — |
| 3 | `thm:wilson` | Wilson | — | — | UNREVIEWED | — |
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

- The five `VERIFIED_TWICE` rows are documented in full under "Proof audit — five individual Chapter 1 results" in `docs/reviews/volume2-independent-verification-ledger-2026-11-03.md`. All other named results are genuinely UNREVIEWED under the new standard.
- `docs/reviews/volume2-exercise-verification-register-2026-11-03.md` indexes all 144 problem and solution keys, not these 72 results.
- The plan `docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md` requires **all** unnamed proof passages, equations and examples as well. This register is an accountability tool, **not** a mathematics certificate.
