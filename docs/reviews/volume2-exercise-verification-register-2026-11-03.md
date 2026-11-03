# Volume 2 — independent per-exercise verification register

**Edition:** manuscript on draft PR #103, initial register created 3 November 2026. **Branch:** `editorial/volume2-independent-proof-and-reader-rewrite-20261103`. **Source snapshot:** branch head `654f869d8ec3e8b98fff5df5b1e7bb1d904212f3` before this file is added.

This register is generated **from the actual 11 chapter sources in printed order**, not copied from an older proof ledger. It lists all 144 keyed exercises; the ordered exercise, hint and solution keys match independently in every chapter at this snapshot. The total is **144**, distributed by chapter **15/11/21/13/16/17/8/8/8/8/19**. Grade distribution: \star: 37; \star\star: 80; \star\star\star: 20; Journey: 7. The manuscript sources, not these static rows, define problem text and source position.

**Meaning of columns:** Pass A = an independent solution without trusting the printed answer; Pass B = genuinely separate symbolic/adversarial reconstruction; earlier-tool check = every needed result proved before this exercise (including hint and full solution). Enter a checker, exact proof link, commit and boundary evidence before changing a status to `VERIFIED_TWICE`. Nine exercises now have two recorded mathematical checks (four Chapter 1 keys, Morley, the gcd/Fibonacci journeys, the redesigned factorial sum and the Ramanujan Journey). Its second pass separately checked the formal substitutions, cancellation, signs and coefficient extraction; finite computations support but do not prove the general statements. Independent external review and final-head CI remain open. Use `IN_PROGRESS`, `BLOCKED`, `CORRECTED_NEEDS_RECHECK`, `UNREVIEWED`, `VERIFIED_TWICE` only.

| Printed chapter | Key | Grade | Pass A | Pass B | Earlier-tool check | Status | Finding / source |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `ex:bez` | ★ | Euclid/back-substitution | Mod-5 congruence + enumeration | PASS | VERIFIED_TWICE | Reader-level proof in ledger |
| 1 | `ex:gcdn` | ★ | Integer-combination bound | Alternative resultant identity + 10,001 checks | PASS | VERIFIED_TWICE | n=0 and 5 residue classes |
| 1 | `ex:zeros` | ★ | Count powers dividing factorial | Telescope exact-valuation classes + recompute | PASS | VERIFIED_TWICE | v2=994, v5=249 |
| 1 | `ex:sqrt` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:mersgcd` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:lame5` | ★★ | Fibonacci–golden-ratio growth | Five-step Fibonacci growth + finite sweep | PASS | VERIFIED_TWICE | 28,680 Euclid pairs |
| 1 | `ex:frob` | ★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:supercat` | ★★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:n2n` | ★★★ | — | — | — | UNREVIEWED | — |
| 1 | `ex:t1-divisibility-lattice` | ★★ | — | — | — | UNREVIEWED | — |
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
| 4 | `pb:eisensine` | Journey | — | — | — | UNREVIEWED | — |
| 4 | `pb:euler` | ★★ | — | — | — | UNREVIEWED | — |
| 4 | `pb:nsq1` | ★★★ | — | — | — | UNREVIEWED | — |
| 4 | `pb:sumsquares` | ★★ | — | — | — | UNREVIEWED | — |
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
| 6 | `pb:phimodp` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:fermatnum` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:carmichael` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:pratt` | ★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:rabin` | Journey | — | — | — | UNREVIEWED | — |
| 6 | `pb:waring` | ★★★ | — | — | — | UNREVIEWED | — |
| 6 | `pb:squaresmodpk` | ★★ | — | — | — | UNREVIEWED | — |
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
| 11 | `pb:fermatcubic` | ★★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:euclidgame` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:pascalthree` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:powerful` | ★★ | — | — | — | UNREVIEWED | — |
| 11 | `pb:jacobi` | Journey | — | — | — | UNREVIEWED | — |
| 11 | `pb:densities` | Journey | — | — | — | UNREVIEWED | — |

## Update discipline

- Preserve the exact stable key. If a problem is redesigned or deleted, record the old and new mathematical obligation and justification in the main review ledger and PR comment.
- Review the prompt, hint, idea, full derivation, notation, exceptional cases, chapter-order references and final display. A numerical sample cannot certify a general identity.
- Keep all review claims tied to an exact source commit. Changing an exercise, prerequisite theorem or its hint reopens its affected verification status.
- The original manuscript tests check matching keys and numeric cases, but **do not establish mathematical correctness**. A row changes status only after the main ledger records both mathematical checks; four Chapter 1 rows now meet that standard, while the remaining rows do not.
- See `docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md` for gates P06/P07; `docs/reviews/volume2-independent-verification-ledger-2026-11-03.md` for current blockers and next exact task.
