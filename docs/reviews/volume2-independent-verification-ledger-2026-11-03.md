# Volume 2 independent verification ledger — NEW, strict standard

**Date:** 2026-11-03. **Branch:** editorial/volume2-independent-proof-and-reader-rewrite-20261103. **Starting main SHA:** e3b60ca365c601e681c36632a5cd1a2b1d8e5aea. **Plan:** docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md.

## Honest current status

**IN PROGRESS; NOT COMPLETE; NOT APPROVED FOR MERGE OR KDP PUBLICATION.** This is a fresh independent review after merged PRs #89, #97 and #102. Those PRs' audits are useful clues, not proof that the stricter new requirements pass. Five named Chapter 1 results are now documented as VERIFIED_TWICE in the proof table below; no exercise solution has yet completed the full two-pass acceptance protocol. No final build or page-by-page inspection has been executed for this PR.

### Source discovery completed (inventory, not proof verification)

- Read canonical house voice: docs/WRITING-STYLE.md; role brief: docs/agents/mathematician-writer.md; current editorial author instructions: AGENTS.md (opening section).
- Read Volume 2 main.tex, preface, legacy continuity plan and prior exercise and prerequisite ledgers.
- Printed chapters: ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch09, ch08, ch10, ch14. Legacy stems ch09 and ch08 must **not** be confused with printed chapter numbers.
- Independently fetched each of 11 current chapter files via GitHub and counted 144 exercise environments, 144 hint environments, 144 solution environments, and 144 writeup tags. *Starting baseline* per printed chapter: **16, 11, 21, 13, 15, 17, 8, 8, 8, 8, 19**; *current branch* after moving one prerequisite-dependent exercise: **15, 11, 21, 13, 16, 17, 8, 8, 8, 8, 19**.
- Current style contract says one-star core exercises should be navigable with Volume 1 + earlier Volume 2. The new commission strengthens this to **every** full exercise solution, including optional advanced work.
- No local clone is available from this execution environment: github.com DNS is not reachable from the local container. GitHub repository reads/writes work through the connected GitHub tools. Thus **no claim of local tests or LaTeX compilation** is made. CI must prove executable gates on the exact branch head.

### Difference from previous PR #97 (important)

PR #97 explicitly accepted the following optional challenges as using other books/undeveloped tools. Under the new requirement they are **BLOCKED until redesigned, relocated or locally taught**; merely writing “return after Volume N” is insufficient:
- ch03: Glaisher/Bernoulli, Ramanujan partitions; potentially Kloosterman/Gauss-sum prerequisites.
- ch04: Eisenstein sine reciprocity, nonlocal prime-distribution estimates, total variation in finite-field square sums.
- ch05: any remaining mean gcd/LCM asymptotic tool not proved locally.
- ch06: finite-field extension and two kth-powers/character-sum methods.
- ch11: cubic Gauss/Jacobi sums, four-square theta-series, four-square local densities and algebraic/p-adic methods.
- Other advanced/return exercises in the previous ledger need individual checking too; these are **risk pointers, not yet defects proven by this review**.

## Phase and chapter matrix

| Gate | State | Actual evidence and remaining obligation |
| --- | --- | --- |
| P00 Exact baseline inventory and executable tests | IN_PROGRESS | GitHub source count and original main SHA captured. All source IDs, Volume 1 actual contents, runnable test results still pending. |
| P01 Volume 1 prerequisite crosscheck | IN_PROGRESS | Confirmed well ordering, strong induction, Fibonacci gcd/Binet and Basel proof sites; rest pending. |
| P02 Continuous story architecture | UNREVIEWED | Current four-part TOC is a baseline, not fixed. |
| P03 First-use dependency graph | IN_PROGRESS | Repaired forward dependency pb:fibcoprime and later analytic dependency pb:gcdmean; rest pending. |
| P04 All theorem/proof second checks | IN_PROGRESS | Five Chapter 1 named results VERIFIED_TWICE with explicit evidence; all others pending. |
| P05 Every worked example and figure | UNREVIEWED | No example certified under this new standard. |
| P06 All exercises independent reconstruction | IN_PROGRESS | Reworked pb:gcdmean and relocated pb:fibcoprime; 0 first-pass certified on full protocol. |
| P07 All exercises independent adversarial second pass | IN_PROGRESS | Finite arithmetic cross-checks for repaired cases; 0 VERIFIED_TWICE. |
| P08 11 chapter rewrites + field guide/preface | IN_PROGRESS | Targeted C01/C03/C05 proof and prerequisite repairs; full chapter rereads missing. |
| P09 Interior illustration mathematical and format proof | UNREVIEWED | No new figures inspected. |
| P10 Full-book voice/transition pass | UNREVIEWED | Existing edited preface is baseline. |
| P11 Tests and exact-head CI | IN_PROGRESS | Early run failed stale pre-move counts; tests updated; exact-latest-head result pending. |
| P12 Every actual PDF/EPUB/site page | UNREVIEWED | No current-branch artifacts inspected. |
| P13 Final editorial sign-off (not KDP approval) | UNREVIEWED | Independent review and author KDP proof later. |

| Printed chapter / file | Status | Target focus |
| --- | --- | --- |
| 1 / ch01-divisibility.tex | IN_PROGRESS | Euclid, FTA, valuations, quantitative exercises |
| 2 / ch02-primes.tex | UNREVIEWED | infinitude, Euler, sieve, Bertrand |
| 3 / ch03-congruences.tex | IN_PROGRESS | residue classes, CRT, prime powers, advanced congruences |
| 4 / ch04-arithmetic-functions.tex | UNREVIEWED | Möbius, convolution, perfect numbers, analytic extras |
| 5 / ch05-primitive-roots.tex | IN_PROGRESS | group orders, cyclicity, lifts, mean gcd |
| 6 / ch06-quadratic-reciprocity.tex | UNREVIEWED | Gauss lemma, signs, reciprocity, advanced tasks |
| 7 / ch07-sums-of-squares.tex | UNREVIEWED | two/four-square proofs, descent |
| 8 / ch09-diophantine.tex | UNREVIEWED | equation domains, Mordell, Vieta/descent |
| 9 / ch08-continued-fractions.tex | UNREVIEWED | approximation quantifiers, periodicity and Pell |
| 10 / ch10-gaussian-eisenstein.tex | UNREVIEWED | Euclidean norms, UFD, Eisenstein cubic proof |
| 11 / ch14-characters.tex | UNREVIEWED | character definitions, series and sieve, deeper exercises |
| Field guide/preface/blurb/KDP description | UNREVIEWED | consistency with final book, no uncovered math |

## Finding log

| ID | Severity | Location | Finding | Evidence / resolution | State |
| --- | --- | --- | --- | --- | --- |
| RISK-001 | critical contract | Optional challenges throughout book | Prior audit accepts outside-volume tools in some solutions, unlike new reader contract | Prior exercise ledger, “Other later-route challenges kept”; examine actual proofs before declaring individual defects | BLOCKED |
| RISK-002 | high | All 11 chapters | Prior source-level reviews did not independently prove every step under current double-verification rule | Historical PR #97 descriptions | UNREVIEWED |
| RISK-003 | medium | Print/EPUB | Preexisting production QA is tied to old commits, not this branch | Previous final acceptance record | UNREVIEWED |
| DEP-001 | confirmed | C01→C05 pb:fibcoprime | A required result was taught four chapters after first use | Moved exercise/hint/solution to after pb:gcdmean in C05 | CORRECTED_NEEDS_RECHECK |
| DEP-002 | confirmed | C05 pb:gcdmean | Prompt borrowed Chapter 11 ζ-differentiation and part (a) cited an unproved asymptotic | Defined ζ locally; proved coprime estimate; changed part (c) to equivalent convergent series and justified truncation | CORRECTED_NEEDS_RECHECK |
| DEP-003 | confirmed | C03 pb:morley | Essential Chapter 11 Fermat-quotient identity cited in Chapter 3 exercise solution | Replaced by a local derivation from binomial theorem and Fermat's congruence; test updated | CORRECTED_NEEDS_RECHECK |

## Implementation checkpoint — first teaching-order repair (3 November 2026)

**Commits:** a16b2ede0ddd15e9345f3cd6f4ac86a45008ea97, 7f3250d3ece056cf4acc685aaebb19054ed51ea5, 7b0f61c52c172f1563ee8c8fcceffd19aac3fab9, 6f17782d16f014d362d8f926bb35615e68339bbb, 6e05e7790b2487faeb719c961b8b7173d6f3afbe. **Do not mark P03/P06/P07 complete.**

**Confirmed issue DEP-001 (corrected, needs source/CI and independent recheck):** printed Chapter 1's `pb:fibcoprime` depended in its prompt and final solution on `pb:gcdmean` in Chapter 5. The reader had not yet been taught that gcd distribution. Moved exercise, matching hint and complete solution to **immediately after** `pb:gcdmean` in Chapter 5. Did not change the exercise ID, mathematical answer or grade; moved all three synchronized blocks. The **current** distribution is **15, 11, 21, 13, 16, 17, 8, 8, 8, 8, 19** (144 total), replacing the *baseline* 16/11/21/13/15/17/8/8/8/8/19. Updated canonical `docs/SERIES-STRUCTURE.md` and source tests; earlier #97 records intentionally retain old historical counts.

**Confirmed issue DEP-002 (corrected, needs source/CI and independent recheck):** the original Chapter 5 `pb:gcdmean` prompt asked to use analytic Dirichlet-series and differentiation material from the later character chapter. Its part (c) wrote an answer as `-ζ'(2)/ζ(2)` without having taught differentiation of ζ. The new prompt defines ζ(s) explicitly for s>1, derives convergence by integral comparison, and points at Volume 1's actual Basel proof. Part (c) now asks for the accessible equivalent convergent series `(6/π²) ∑_{g≥1} (log g)/g²`. Its solution uses a **finite truncation and uniform tail bound**, with no differentiated series. Part (a) now derives the needed coprime-pair asymptotic using Chapter 4's Möbius identity and the absolutely convergent reciprocal-square series, instead of importing an unproved probability estimate.

**Actual Volume 1 proof-site checks (completed for these two tools only):**
- `volume1-first-principles/chapters/ch01-sums.tex`, exercise `ex:fibgcd`, full solution `\begin{solution}{ex:fibgcd}`: induction and Euclidean argument establish `gcd(F_m,F_n)=F_gcd(m,n)`. Binet's formula is present in the same chapter. This is a *solution* in Volume 1 rather than a standalone core theorem; Volume 2 now cites the problem in a location where readers can consult it.
- `volume1-first-principles/chapters/ch03-polynomials.tex`, exercise `ex:basel`, full solution: the finite polynomial/cotangent squeeze derives `∑_{n≥1}1/n²=π²/6`. The new Chapter 5 paragraph explicitly identifies that proof as the source of ζ(2).
- These checks establish **where** the imported arguments live; they are not a fresh independent audit of the entirety of those Volume 1 proofs.

**Independent finite arithmetic cross-check:** for N=5,10,30,60 the direct count of coprime ordered pairs equals the independent Möbius count `Σ_{d≤N} μ(d)⌊N/d⌋²`: respectively **19, 63, 555, 2203**. Direct Fibonacci-gcd computations for indices 1 to 23 and the corresponding gcd(F_a,F_b)=1 criterion have been encoded in `tools/test_volume2_exercise_keys.py`. The same test guards the moved order, retained keys and the removal of the later derivative prerequisite. **These finite checks do not prove the limits or certify the entire exercise.**

**Current chapter status:** printed Chapter 1 = IN_PROGRESS (one forward-usage defect corrected), printed Chapter 5 = IN_PROGRESS (one exercise repaired and supporting proof expanded), all others UNREVIEWED. Exercises `pb:gcdmean` and `pb:fibcoprime` = CORRECTED_NEEDS_RECHECK, **not VERIFIED_TWICE**. P03, P06, P07, P08 = IN_PROGRESS. The CI and rendered-proof gates remain unchecked.

**Next exact tasks:** (1) run/inspect current-head tests and CI and fix any regressions; (2) finish P01 toolkit proof-site ledger; (3) independently re-derive gcd asymptotic with all error terms and the Fibonacci exercise without looking at the newly edited proof; (4) inspect Chapter 3 `pb:glaisher` and `pb:ramanujan5` as concrete later-volume dependencies, redesign rather than merely label as optional; (5) continue all proofs and exercises by actual printed order.

## Implementation checkpoint — Chapter 3 Morley proof made self-contained

**Committed:** `8f714eb063508f32aae77e940e27ea3b8a6ca70a` (chapter); `fe1aae657c1255eef3a89f167b7f5058f559f751` (regression).

**Confirmed issue DEP-003, status CORRECTED_NEEDS_RECHECK.** `pb:morley` was previously printed in Chapter 3 yet required the *solution* of Chapter 11 `pb:fermatquot(b)` for an alternating harmonic congruence. The modified exercise, hint, idea and writeup now use only Chapter 1 binomial coefficients and Chapter 3 Fermat's congruence. For odd prime p, the proof uses

`binom(p,j) ≡ (p/j)(-1)^(j-1) (mod p²)`, for 1 ≤ j < p,

hence `2^p - 2 ≡ p Σ_{j=1}^{p-1}(-1)^(j-1)/j (mod p²)`. With `2^(p-1)=1+pt`, the alternating sum equals `2t (mod p)`. Pairing terms of the full harmonic sum shows `H_(p-1)/2 ≡ -2t (mod p)`. The product expansion of the required binomial coefficient and `(1+pt)² ≡ 1+2pt (mod p²)` finish the proof. Every division is by an integer prime to p. Unlike the earlier proof, there is **no forward reference** to Chapter 11. The regression test formerly enforcing that wrong pedagogy was replaced by a test that prohibits the dependency and checks all odd primes p=3,5,7,11,13,17,19,23,29,31. Their complete numerical congruences were independently checked and agreed.

**CI evidence and limit:** The early `7f3250d3ece056cf4acc685aaebb19054ed51ea5` workflow failed only because the old hard-coded per-chapter count test still expected 16/15; its log reports 155 tests, 3 failures about stale counts, 27 skips. The source tests were updated in `7b0f61c52c172f1563ee8c8fcceffd19aac3fab9`. More recent intermediate workflows were cancelled when new commits arrived. A run for head `fe1aae657c1255eef3a89f167b7f5058f559f751` was in progress when inspected. **No latest-head CI success is asserted**.

**State:** printed Chapter 3 IN_PROGRESS; problem `pb:morley` CORRECTED_NEEDS_RECHECK. A complete second symbolic audit, every other Chapter 3 exercise and final rendered outputs remain pending.

## Proof audit — five individual Chapter 1 results, two documented checks

**Source under review:** `volume2-integers/chapters/ch01-divisibility.tex`. **Imported tool checked against actual Volume 1:** well ordering and strong induction are developed in `volume1-first-principles/chapters/ch01-sums.tex`, Section "Induction, in three flavours" (including its proof of their equivalence). The earlier Volume 1 integer-divisibility workshop also proves Bézout and prime cancellation, but the first-route Volume 2 chapter supplies its own proofs independently.

| ID | Reader-facing statement and first-pass reconstruction | Second independent verification and boundary test | Status |
| --- | --- | --- | --- |
| `thm:div` | For any a∈Z,b>0, choose least nonnegative a−bq by well ordering; if it were ≥b subtract b; uniqueness from b(q−q')=r'−r and `|r−r'|<b`. All steps checked, including construction q=−|a| for a<0 and b=1. | Independent floor construction q=⌊a/b⌋, r=a−bq gives 0≤r<b. If q differed by a nonzero integer, the remainders would differ by at least b, contradicting both bounds. Exhaustively tested 5,025 pairs −100≤a≤100, 1≤b≤25 with Python integer quotient/remainder. | **VERIFIED_TWICE** |
| `prop:subgroups` | For additive subgroup H≤Z, if H={0}, generator d=0. Otherwise closure under negatives produces a positive h; take least positive d∈H; closure produces dZ⊆H; division by d sends each a∈H to remainder r∈H smaller than d, hence r=0; uniqueness from least positive element. | Independently re-deriving with q=⌊a/d⌋ verifies a−qd∈H even for negative a. An adversarial case audit checked H={0}, H=Z, proper H=kZ, necessity of nonempty/closure assumptions, and uniqueness of nonnegative d; none relies on a later group theorem. | **VERIFIED_TWICE** |
| `thm:bezout` | With a,b not both zero, aZ+bZ is an additive subgroup. Its positive generator d is itself one of the combinations au+bv, and d divides both a and b; every common divisor divides au+bv=d. Thus d=gcd(a,b). Similarly au+bv=1 iff d=1. | Independent constructive check via the extended Euclidean algorithm: each remainder remains an integer combination of original inputs, all common divisors are preserved, last positive remainder = gcd. Edge cases a=0,b≠0; b=0,a≠0; negative inputs and units checked. Algorithm proof appears later but is **not** imported into the earlier manuscript theorem. | **VERIFIED_TWICE** |
| `thm:gauss` | From gcd(a,b)=1 pick au+bv=1; multiply by c. If a|bc, then both acu and bcv are multiples of a; hence a|c. For p prime with p|bc, either p|b or gcd(p,b)=1 and the first claim applies. | Re-derived as invertible multiplication in residue classes modulo |a| for |a|>1 (inverse u from Bézout), with trivial cases |a|=1. Also checked the special a=0,b=±1 case directly: 0|bc implies c=0. Contradiction check with a=6,b=2,c=3 shows coprimality cannot be dropped. No FTA used as a prerequisite. | **VERIFIED_TWICE** |
| `thm:fta` | Existence by strong induction n≥2: prime case, else n=uv with 2≤u,v<n. Uniqueness by matching one prime factor using iterated Gauss lemma, cancelling and invoking strong induction. A missing explicit prime n base case in the former text was fixed in commit `b02738523cfc5fb3de6eaf1b61f3c7cea444af9e`. Revised proof separates prime and composite n: for composite n, after cancellation the remaining m=n/p satisfies 2≤m<n. | Second adversarial minimal-counterexample argument: if n were the least number with two different prime multisets, n could not be prime; common p exists by Gauss, and cancelling yields a smaller integer m≥2 with two different multisets, contradicting minimality. Checked n=2,3,4,6, prime n with singleton list, repeated primes and n=1 excluded by the theorem. Recomputed sample decompositions for 2,3,4,8,17,360,997; examples cannot prove uniqueness. | **VERIFIED_TWICE** |

These are **five individual source claims**, not a sign-off on the rest of Chapter 1. Each has a mathematical proof and an adversarial second check; finite tests only support the edge handling. Any later changes to these premises must reopen dependent rows.

## Structured verification entries

**Result/proof entry template:** ID; file:line or exact label; statement/hypotheses; use-site/prerequisites; reconstructed proof; independent second test/proof/reference; edge cases; fixes + commit; status. Add *one row per actual theorem/proof*, including unnamed arguments.

**Exercise entry template:** key, stars, printed chapter; precise problem and edge conditions; independent solution without trusting \writeup; separate adversarial second derivation; hint/idea/writeup alignment; tools introduced before exercise; possible source change + commit; status. The 144 keys are already listed in docs/reviews/volume2-exercise-solution-audit-2026-11-03.md, but that ledger cannot be used to pre-fill VERIFIED_TWICE.

**Example/figure entry template:** stable key, formula/data, independently recalculated result, printed page and visual check when produced, status.

## Checkpoint protocol (mandatory on each active work session)

1. Read PR title/body, comments, this ledger, and full plan; inspect branch head and open CI; compare with main.
2. Pick one specific result/proof or exercise that is UNREVIEWED/BLOCKED. Keep source text plus your independent argument; cite exact local previous proof rather than saying “well known”.
3. Record the finding and write a focused code+test+ledger commit. Never mark a row VERIFIED_TWICE on a single explanation or finite sample.
4. Update PR description/comment with **what changed**, exact SHA and checked tests, **what is not checked**, and the **next exact task**.
5. At session end include the next location and proof question. Leave draft, do not merge or publish before P13.

**Next exact task:** inspect current CI at latest head, complete Volume 1 toolkit and independent second checks on pb:gcdmean/pb:fibcoprime/pb:morley, then redesign Chapter 3 pb:glaisher and pb:ramanujan5 rather than using Volume 5. Continue first-use/proof ledgers for all remaining claims. See latest checkpoint and PR comments. 
