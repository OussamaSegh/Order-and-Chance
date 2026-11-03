# Volume 2 independent verification ledger — NEW, strict standard

**Date:** 2026-11-03. **Branch:** editorial/volume2-independent-proof-and-reader-rewrite-20261103. **Starting main SHA:** e3b60ca365c601e681c36632a5cd1a2b1d8e5aea. **Plan:** docs/plan/volume2-independent-verification-and-rewrite-2026-11-03.md.

## Honest current status

**IN PROGRESS; NOT COMPLETE; NOT APPROVED FOR MERGE OR KDP PUBLICATION.** This is a fresh independent review after merged PRs #89, #97 and #102. Those PRs' audits are useful clues, not proof that the stricter new requirements pass. Eight named results (six from printed Chapter 1, two from Chapter 2) and ten exercise solutions have two documented mathematical passes in the registers and checkpoint below. The remaining 64 named results, 134 exercises and all unnamed proof claims are not certified. An earlier print/EPUB build completed but the old spine QA rejected it; no passing final-head build or page-by-page visual proof has been recorded.

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
| P00 Exact baseline inventory and executable tests | IN_PROGRESS | 72 named results and 144 exercise keys independently indexed; Volume 1 crosswalk incomplete; current-head CI still pending. |
| P01 Volume 1 prerequisite crosscheck | IN_PROGRESS | Confirmed well ordering, strong induction, Fibonacci gcd/Binet and Basel proof sites; rest pending. |
| P02 Continuous story architecture | IN_PROGRESS | Chapter 2 redundant Euclid exposition condensed; whole-book story still pending. |
| P03 First-use dependency graph | IN_PROGRESS | Five concrete dependency repairs, including Glaisher and Ramanujan; later advanced challenges remain. |
| P04 All theorem/proof second checks | IN_PROGRESS | Eight named results VERIFIED_TWICE; all other result and unnamed proof chains pending. |
| P05 Every worked example and figure | IN_PROGRESS | Individually checked Euclid six-prime composite and 5!+1, plus arithmetic boundary probes; rest pending. |
| P06 All exercises independent reconstruction | IN_PROGRESS | Ten solutions have a complete author-level reconstruction; the other 134 remain. |
| P07 All exercises independent adversarial second pass | IN_PROGRESS | Ten solutions VERIFIED_TWICE, including redesigned Chapter 4 prime-factor proof; 134 remaining. |
| P08 11 chapter rewrites + field guide/preface | IN_PROGRESS | Targeted C01/C02/C03/C05 math and voice repairs; no chapter signed off. |
| P09 Interior illustration mathematical and format proof | UNREVIEWED | No new figures inspected. |
| P10 Full-book voice/transition pass | IN_PROGRESS | Local Chapter 2 duplicate-paragraph removal only; full read-aloud pending. |
| P11 Tests and exact-head CI | IN_PROGRESS | Main tests passed at earlier head but print-output QA had wrong rounding; fixed and added new regression tests. New exact-head CI pending. |
| P12 Every actual PDF/EPUB/site page | UNREVIEWED | No current-branch artifacts inspected. |
| P13 Final editorial sign-off (not KDP approval) | UNREVIEWED | Independent review and author KDP proof later. |

| Printed chapter / file | Status | Target focus |
| --- | --- | --- |
| 1 / ch01-divisibility.tex | IN_PROGRESS | Euclid, FTA, valuations, quantitative exercises |
| 2 / ch02-primes.tex | IN_PROGRESS | Euclid and Euler twice checked; estimates, Bertrand and all exercises still pending |
| 3 / ch03-congruences.tex | IN_PROGRESS | residue classes, CRT, prime powers, advanced congruences |
| 4 / ch04-arithmetic-functions.tex | IN_PROGRESS | Replaced pb:nsq1 requiring Volume 6; other advanced chapters and all named proofs still pending |
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
| DEP-001 | confirmed | C01→C05 pb:fibcoprime | A required result was taught four chapters after first use | Moved exercise/hint/solution to after pb:gcdmean in C05; proved Binet error explicitly | VERIFIED_TWICE |
| DEP-002 | confirmed | C05 pb:gcdmean | Prompt borrowed Chapter 11 ζ-differentiation and part (a) cited an unproved asymptotic | Local ζ, harmonic mean proof, uniform weighted endpoint and double check | VERIFIED_TWICE |
| DEP-003 | confirmed | C03 pb:morley | Essential Chapter 11 Fermat-quotient identity cited in Chapter 3 exercise solution | Local binomial/harmonic proof; adversarial algebra and independent prime checks | VERIFIED_TWICE |

| DEP-004 | confirmed | C03 pb:glaisher | Original problem imported Bernoulli denominator theory from Volume 5 | Replaced *mathematical problem* with Fermat/Wilson power-sum congruence, explicitly documented | VERIFIED_TWICE (replacement) |
| DEP-005 | confirmed | C03 pb:ramanujan5 | Original proof imported pentagonal theorem and complex analysis | All needed identities derived coefficientwise, then independently checked line by line | VERIFIED_TWICE |
| DEP-006 | confirmed | C04 pb:nsq1 | Original P(x)>x proof required quantitative primes in progressions from Volume 6 | Explicitly replaced by near-linear P(x)>x^(1−δ), fixed 0<δ<1, proved using Chapter 2 Chebyshev | VERIFIED_TWICE (new statement) |

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

## Session checkpoint — corrected build gate, two-pass proofs and exercises (3 November 2026)

**Exact branch:** editorial/volume2-independent-proof-and-reader-rewrite-20261103. **Main unchanged since initial PR:** e3b60ca365c601e681c36632a5cd1a2b1d8e5aea. **Files changed:** Chapter 2 proof/voice, Chapter 5 gcd/Fibonacci writeups, KDP output QA, focused tests, per-result and per-exercise registers. The PR stays **draft**.

### CI failure analysed and corrected, not yet certified green

Run [41667990866](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/41667990866), head \`d6b20f0ffa2ed8327f27eb51562a00b0c221b210\`, had a **successful list/unit gate** and a successful LaTeX/EPUB/print build. The print source produced **315 interior pages, 316 counted KDP pages, 0.7417-in spine, 14.9917-in wrap width, 10.25-in wrap height**. The build job then failed its cross-format script, not the TeX build: \`check_volume2_outputs.py\` compared the spine to the *three-decimal* \`round(316×0.002347,3)=0.742\`, while the canonical \`tools/print_layout.py\` generates *four decimals*, \`round(316×0.002347,4)=0.7417\`. Therefore the **checker was wrong; the generated cover was not resized by guesswork**.

Commits \`ee2f4026\` and \`e88a6d96\` repaired the checker and added explicit trim/bleed/spine geometry checks; \`1480db8c\` added focused odd/even page-count and incorrect-cover regression tests. \`tools/test_volume2_foundation_review.py\` adds finite mathematical probes. All new tests **still require an exact-head CI run**; old failed/cancelled workflows do not establish their outcome. The actual PDF, EPUB and physical paperback proof remain uninspected under P12/P13.

### Named result two-pass checks (new)

1. **\`thm:lame\` (Chapter 1) — VERIFIED_TWICE.** Pass A: the last nonzero remainder satisfies \`r_n≥1=F_2\`; the previous one is at least \`2=F_3\`. Backward use of \`r_{k-1}=q_kr_k+r_{k+1}\`, with \`q_k≥1\`, gives \`r_k≥F_{n+2-k}\`. Thus \`b≥F_{n+1}\`, \`a≥F_{n+2}\`; check separately the one-division case. Pass B: construct the *smallest possible* remainder sequence backward from 1,2 under the same recurrence. Its entries are consecutive Fibonacci numbers, with equality for consecutive Fibonacci inputs (final quotient 2). Independent exhaustive arithmetic over **28,680** pairs \`2≤a≤240\`, \`1≤b<a\` reported zero violations, including \`b=1\`. These computations are a boundary check, not the proof.
2. **\`thm:euclid-primes\` (Chapter 2) — VERIFIED_TWICE.** Pass A: finite list assumed *complete*, with \`k≥1\` because 2 is prime; a prime divisor of \`N=p_1···p_k+1>1\` cannot divide the product \`N−1\`. The empty-list oversight was closed in commit \`514541c6\`; theorem was given a stable label and repeated prose shortened in \`7fa1c2f4\`. Pass B: for each integer \`m≥2\`, any prime factor of \`m!+1\` must be **greater than m**, since all primes up to m divide m!; primes are unbounded. Checked \`2·3·5·7·11·13+1=59·509\` and \`5!+1=11²\`, which also demonstrate that the number constructed need not be prime.
3. **\`thm:euler\` (Chapter 2) — VERIFIED_TWICE.** Pass A: for real \`x≥2\`, unique factorisation gives \`H_floor(x)≤∏_{p≤x}(1−1/p)^{−1}\`; integral comparison gives \`H_floor(x)≥log x\`. The manuscript bounds each logarithmic error by \`1/[p(p−1)]\`, whose sum over all integers \`p≥2\` telescopes to 1, so \`∑_{p≤x}1/p≥log log x−1\`. Pass B: independently derive \`−log(1−1/p)−1/p=∑_{j≥2}1/(j p^j)≤1/[p(p−1)]\` from the Volume 1 logarithmic series, avoiding the manuscript's integral estimate for the logarithmic error. Numerically checked all integer \`2≤x≤15000\` (14,999 cutoffs), no violation; the smallest observed excess over the bound was about **1.26176**. Numerical checks do not establish divergence.

### Exercises with two substantive checks (new: 7 / 144)

- **\`ex:bez\` (Chapter 1) — VERIFIED_TWICE.** Pass A: Euclid yields \`7=2·91−5·35\`; cancelling the gcd and using Gauss gives all \`(x,y)=(2+5t,−5−13t)\`, \`t∈Z\`. Pass B: directly reduce \`13x+5y=1\` modulo 5; \`3x≡1\` forces \`x≡2\` and uniquely determines y. Exhaustive x from −200 to 200 found 80 integral pairs, every one in the family, plus substitution for t from −80 to 80. Hint, discovery and writeup use prior Chapter 1 tools only.
- **\`ex:gcdn\` (Chapter 1) — VERIFIED_TWICE.** Pass A: a common divisor of \`n²+1,(n+1)²+1\` divides \`2n+1\`, and \`4(n²+1)−(2n+1)(2n−1)=5\` forces it to divide 5. Pass B: set \`u=2n+1\` and compute \`4(n²+1)=u²−2u+5\`; use residues modulo 5 to show both inputs are divisible by 5 exactly for \`n≡2 mod5\`. Direct gcd enumeration for every \`0≤n≤10000\` found no exception. The boundary \`n=0\` gives gcd 1.
- **\`ex:zeros\` (Chapter 1) — VERIFIED_TWICE.** Pass A: count multiples of each \`p^k\` inside n!, giving Legendre's formula. Pass B: let \`c_k=⌊n/p^k⌋−⌊n/p^{k+1}⌋\` count the integers with exact valuation k; the finite telescoping sum \`∑k c_k=∑⌊n/p^k⌋\` checks the first argument. Direct evaluation gives \`v_2(1000!)=994\`, \`v_5(1000!)=249\`; a trailing zero consumes one of each, so exactly **249**.
- **\`ex:lame5\` (Chapter 1) — VERIFIED_TWICE.** Pass A: prove \`F_{k+1}≥φ^{k−1}\` by two-base-case induction; use \`φ⁵>10\` and \`b<10^d\` for d digits to deduce \`n≤5d\`. Pass B: *without golden-ratio estimates*, use \`F_{k+5}=8F_k+5F_{k−1}≥10F_k\` for k≥2 (since \`F_k≤2F_{k−1}\`). Iteration gives \`F_{5d+2}≥10^d\`; if n≥5d+1, Lamé contradicts \`b<10^d\`. Exhaustive 28,680 Euclidean input pairs independently satisfy the bound.
- **\`pb:morley\` (Chapter 3) — VERIFIED_TWICE.** Pass A: from \`binom(p,j)=(p/j)binom(p−1,j−1)\` get \`2^p−2≡p∑(-1)^{j−1}/j (mod p²)\`. Fermat's theorem writes \`2^{p−1}=1+pt\`, so this alternating harmonic sum is 2t mod p. Pairing j and p−j makes the full harmonic sum 0 mod p, hence \`H_{(p−1)/2}≡−2t\`. Expand the central binomial product to order p and compare with \`4^{p−1}=(1+pt)²\`. Pass B: independently reconstructed and checked every cancellation denominator \`j<p\`, sign, modulus and edge \`p=3\`; exact binomial arithmetic for **all odd primes 3≤p≤997** found no counterexample. No Chapter 11 reference remains in the question, hint or required solution.
- **\`pb:gcdmean\` (Chapter 5) — VERIFIED_TWICE.** Parts (a)–(d) checked against earlier tools: the coprime count \`C(M)=∑_{d≤M}μ(d)⌊M/d⌋²\` is \`M²/ζ(2)+O(Mlog(2M))\`; (b) has two separate general derivations of \`∑_{d≤N}φ(d)/d²=log N/ζ(2)+O(1)\`: original partial-summation derivation via \`A(t)=t/ζ(2)+O(log(2t))\`, and new, simpler finite Möbius regrouping \`∑_{h≤N}μ(h)H_{⌊N/h⌋}/h²\`, with the uniform bound \`H_{⌊N/h⌋}=log(N/h)+O(1)\`. Part (c) passes the limit by finite truncation and the uniform tail \`∑_{g>G}log g/g²\`, not by an unproved derivative of ζ. For (d), independently reconstructed the **weighted** sum \`W(M)=∑_{d≤M}μ(d)d²S(M/d)²\`, and its \`M⁴/(4ζ(2))+O(M³log(2M))\` error uniform to \`M=1\` (the old logarithm alone vanishes there). Rechecked the summed error \`O(N³log(2N))\` and the ζ(3) leading coefficient. Direct and weighted Möbius counts agree for \`M=1,2,3,5,10,25\`; direct gcd/lcm averages for \`N=30,100,300\` track the predicted limits. The latest correction is commit \`e7e1bc8c\`. No Chapter 11 differentiation or Volume 6 average order is imported.
- **\`pb:fibcoprime\` (Chapter 5) — VERIFIED_TWICE.** Pass A: the actual Volume 1 Fibonacci identity gives \`gcd(F_a,F_b)=F_g\`, \`g=gcd(a,b)\`; \`F_g=1\` precisely for g=1 or2, so the limiting probability is \`6/π²(1+1/4)=15/(2π²)\`. Part (b) follows by taking the expectation of \`log F_g=glog φ−log√5+O(1)\` and applying the preceding gcd mean. Pass B: explicitly factor Binet \`F_g=φ^g/√5 (1−(−φ^{−2})^g)\`; the correction factor lies in a fixed positive interval, so **its logarithm is uniformly bounded for every g≥1**. Direct index-gcd/Fibonacci checks for indices 1..23 and the empirical probabilities for N=30,100,300 are consistent. The exercise/hint/solution are printed **after** \`pb:gcdmean\` and use its already available results.

**Independent source regression:** \`tools/test_volume2_foundation_review.py\` guards first-chapter problem answers, prime counterexamples, numeric Euler inequality and Lamé bounds. \`tools/test_volume2_exercise_keys.py\` now guards the new elementary harmonic proof and the weighted M=1 endpoint. Both still require an exact-head CI test.

### Reopen rules and remaining risks

No chapter passes P08 yet: proof and exercise registers each list many more rows, and unnamed proofs/examples, references, illustrations, and publisher outputs are still unchecked. The latest corrections to \`pb:gcdmean\` reopen any exercise that uses it except \`pb:fibcoprime\`, which was rechecked above. The Bernoulli/Glaisher and partition/Ramanujan exercises in Chapter 3 still expressly borrow Volume 5 and remain **BLOCKED by the stricter contract**. Do not treat a later-volume label as a solution.

**Next exact task:** inspect exact-head CI for the new geometry and mathematical tests; triage \`pb:glaisher\`, \`pb:ramanujan5\` to self-contained, true Volume 2 alternatives; finish Volume 1 actual toolkit ledger; continue Chapter 1 remaining solution/proof audits and all Chapter 2 calculations before claiming any chapter signed off.

## Session checkpoint — advanced Chapter 3 repairs (3 November 2026)

### DEP-004 — Bernoulli exercise replaced, not silently certified

The former \`pb:glaisher\` asked for \((p-1)!\equiv pB_{p-1}-p\pmod{p^2}\), depending on Faulhaber's formula, Bernoulli denominators and von Staudt–Clausen from **Volume 5**, plus a later Chapter 11 Fermat-quotient congruence. Those results were not earned by a Chapter 3 reader. The replacement preserves the stable key, hint/solution and ★★★ grade but **changes the mathematical target** to the related, accessible congruence \(\sum_{a=1}^{p-1}a^{p-1}\equiv(p-1)!+p\pmod{p^2}\) for odd prime p. The original Bernoulli theorem is **not** claimed proved by Volume 2. The new problem explicitly introduces \(q_p(a)=(a^{p-1}-1)/p\) and \(W_p=((p-1)!+1)/p\), integers by Fermat/Wilson, and requires proving \(\sum q_p(a)\equiv W_p\pmod p\).

**Pass A:** write \(P=(p-1)!\). From \(\prod_{a=1}^{p-1}(1+pq_p(a))=P^{p-1}\), the left is congruent to \(1+p\sum q_p(a)\pmod{p^2}\). From \(P=-1+pW_p\) and even exponent p−1, the right is \(1-p(p-1)W_p\equiv1+pW_p\pmod{p^2}\). Cancellation of p changes the modulus to p; summing the exact equations \(a^{p-1}=1+pq_p(a)\) proves the required power-sum congruence. **Pass B:** explicitly checked invertibility, sign, p=3 boundary and the change of modulus; independently computed both quotient and power-sum congruences for **all 24 odd primes p≤97**, with no failures. The solution uses earlier Chapter 3 and Chapter 1 tools only. Source commit \`e4e65b69\`, test \`f87b0620\`. This new problem is **VERIFIED_TWICE**, subject to final exact-head CI and page proof.

### DEP-005 — Ramanujan problem retained, self-contained formal proof needs a second audit

The original \`pb:ramanujan5\` still asks for the full infinite congruence \(p(5n+4)\equiv0\pmod5\). Its previous proof relied on unintroduced holomorphic/Laurent expansions, analytic continuation, and Euler's pentagonal theorem. Replaced the question, hint and solution with a full *coefficientwise formal-power-series* route. A finite coefficient is defined by a finite convolution; each coefficient of an infinite product depends on only finitely many factors. This is taught at the exercise before any use.

The current source derives \`H(q,q²z)=H(q,z)/(qz)\` and \(c_m=q^{m^2}c_0\); evaluates at \(z=i\), \(z=-1,q\mapsto q^4\), uses a formal series with constant 1 to deduce \(c_0(q)E(q^2)=1\), and hence proves the Jacobi triple product. A specialization \(q=u^3,z=-u^{-1},x=u^2\) now **proves Euler's pentagonal identity inside the solution** rather than quoting it. A different specialization and cancellation of \(1-w^{-1}\) derives Jacobi's cubic identity by a finite geometric sum in w; no analytic limit is imported. Modulo 5, the identity \(8e(j,k)\equiv(2k+1)^2+2(j+4)^2\) forces every coefficient of \(x^{5m}\) in \(xE(x)^4\) to be divisible by 5. A direct combinatorial count proves \(1/E(x)=\sum p(n)x^n\), and \(E(x)^5\equiv E(x^5)\pmod5\) gives Ramanujan's congruence by residue-class extraction. Source commit \`f081b967\`, regression test \`e436e2f4\`.

**Independent finite checks:** 1,207 coefficients of the triple product through q-degree 70 agreed with the original finite products; all 51 values \(p(5n+4)\) for n=0,…,50 vanished mod5 in a separately implemented partition recurrence. The new test also checks Euler's and Jacobi's identities through degree 140. **Status remains CORRECTED_NEEDS_RECHECK:** these finite tests and the first symbolic derivation are not an independent second proof of the infinite identities. Revisit carefully the validity of formal substitution with temporary negative powers, factor cancellations, exponent signs and the final coefficient-class projection. No outside-volume theorem is now declared essential.

### CI and route status

Previous full build at head \`d6b20f0\` produced a **315-page interior**, with **316 KDP counted pages, 0.7417-inch spine and 14.9917-inch wrap width**, before a false 3-decimal spine validator failed. The QA now uses the canonical 4-decimal value; \`tools/test_volume2_output_geometry.py\` guards it. New maths regressions also cover first-chapter examples, Glaisher modular arithmetic and formal partition coefficients. **A passing current-head CI build is not yet evidenced**; do not infer one from earlier cancelled runs. No visual page-by-page proof or Kindle/KDP preview is certified.

**Next exact task:** check the newest GitHub Actions result on the PR head; independently reread the entire \`pb:ramanujan5\` formal proof; proceed with the remaining later-volume-dependent exercises (especially Chapter 4 and Chapter 6) and the Volume 1 prerequisite inventory. The release gates P00–P13 and complete 144-solution audit remain OPEN.

## Follow-up checkpoint — Ramanujan second proof pass complete

**DEP-005 is now VERIFIED_TWICE, superseding the earlier pending checkpoint.** Commits \`8d3be6e7\` and \`c09ac5d7\` clarify proof and regression arithmetic. Independent adversarial symbolic re-derivation checked each of the following, in addition to the original argument:

- The coefficient of \(z^m\) in \(H(q,z)\) first appears at q-degree at least \(m^2\), since the least exponents of \(|m|\) necessary factors sum to \(1+3+\cdots+(2|m|-1)=m^2\). Substitution \(z\mapsto q^2z\) shifts that degree to at least \((m+1)^2-1\ge-1\), so the reindexed formal Laurent series remains bounded below and coefficientwise comparison is legitimate. The uncancelled factors yield exactly \(1/(qz)\), and the recurrence works for both signs of m.
- At \(z=i\), the odd terms cancel in pairs; at \(z=-1,q\mapsto q^4\), the same theta series occurs. Its constant term is 1, so it is invertible. Checked the product split into exponent classes 2,4,6 mod 8, giving \(c_0(q)E(q^2)=c_0(q^4)E(q^8)\). The only formal power series with constant term 1 satisfying \(D(q)=D(q^4)\) is 1, by induction on degree. This proves the triple product without analytic continuation.
- For Euler's identity, \(q=u^3,z=-u^{-1},x=u^2\) turns the three product families into all factors \(1-x^r\) exactly once. The sum exponents \(j(3j-1)/2\) are nonnegative integers, even for negative j.
- For Jacobi's cubic identity, pair m=k with m=−k−1, cancel the common \(1-w^{-1}\) **in each finite Laurent-polynomial coefficient** and specialize \(w=1\). The quotient is \(w^{-k}(1+w+\cdots+w^{2k})\), whose value is \(2k+1\); no limit or undeveloped complex theorem appears.
- The mod-5 square identity \(8e(j,k)\equiv(2k+1)^2+2(j+4)^2\) was re-expanded. The residue sets for squares and twice-squares mod 5 intersect negatively only at zero, so every term at exponent divisible by 5 carries a coefficient divisible by 5. The partition generating function follows by choosing multiplicities of each part; \(E(x^5)\) is invertible coefficientwise mod 5 and does not mix exponent residue classes. The vanishing class is precisely \(p(5m+4)\).

**Independent finite corroboration:** 1,207 triple-product coefficient comparisons through q-degree 70; Euler pentagonal and Jacobi cubic expansions through degree 140; \(xE(x)^4\) coefficient checks at multiples of 5 through degree 140; and 51 separate partition counts for \(p(5m+4)\), m=0..50. All agreed. Finite evidence is not the proof; the symbolic derivation above is. These two passes were carried out in this work session; **independent external peer review, exact-head CI, full visual page inspection and publisher proof remain pending**.

**Current count:** 8/72 named results and 9/144 exercise solutions VERIFIED_TWICE; 64 named results and 135 exercises, plus unnamed arguments, remain. No chapter is signed off.

**Next:** check latest CI; inspect Chapter 4 and Chapter 6 advanced exercises for missing external theorems; complete Volume 1 prerequisite crosswalk and the rest of the theorem/exercise audits.

## Most recent checkpoint — elementary largest-prime-factor exercise (DEP-006)

**3 November 2026.** Replaced the mathematical target of `pb:nsq1` in Chapter 4, which formerly asserted `P(x)>x` and invoked the quantitative prime-number theorem in progressions from Volume 6. Under the user's prerequisite contract, that was not acceptable. **The new exercise explicitly states the weaker but still substantial result: for every fixed `0<δ<1`, the largest prime factor of `Q(x)=∏_{1≤n≤x}(n²+1)` exceeds `x^(1−δ)` for all sufficiently large x.** The original `P(x)>x` claim is **not** asserted proved. Source commit `84151c18`, finite regression `35c8c1a1`, exercise register `e7e5a475`.

**Independent symbolic Pass A:** Legendre's factorial valuation and the already-proved optional Chapter 2 Chebyshev count `π(m)=O(m/log m)` give `∑_{p≤y} log p/(p−1)=log y+O(1)` by comparing both sides with `log(m!)/m`. Two roots `a²≡b²≡−1 (mod p^k)` for odd p differ by a factor of `(a−b)(a+b)`; since p cannot divide both (it would divide `2a`), each root is ± the first. Thus at most two roots modulo `p^k`, and `v_p(Q(x))≤2x/(p−1)+O(log(x²+1)/log p)`. For p=2, every n²+1 has valuation at most 1. Assuming every prime factor ≤`y=x^(1−δ)`, summing logarithmic prime contributions gives `log Q(x)≤2(1−δ)x log x+O(x)` while `n²+1≥n²` gives `log Q(x)≥2x log x−O(x)`, impossible as x grows.

**Adversarial symbolic Pass B:** Rechecked the geometric tail and floor errors in Legendre's estimate and their sum against Chebyshev; all domains p odd and invertible roots in the mod-`p^k` argument; the p=2 parity case; the uniform `O(π(y)log x)=O(x^(1−δ))` error and the fixed-δ condition. Finite independent enumeration found at most two solutions of `z²≡−1` for odd prime powers ≤15000 and no violations of the replacement inequality for x=25..400 and δ=0.2,0.5,0.8. These finite tests support the symbolic proof but cannot prove the asymptotic. The replacement solution is marked **VERIFIED_TWICE** subject to exact-head CI and external mathematical review.

**Current totals:** 8/72 named results, 10/144 exercises VERIFIED_TWICE; **64 named results, 134 exercises, all unnamed arguments and full publishing/visual gates remain**. Chapter 4 remains IN_PROGRESS, not signed off. Next address `pb:sumsquares`: its statement borrows the total-variation definition from Volume 4 and its solution needs a Chapter 6 Gauss sum; define total variation here and move or re-prove the Gauss-sum prerequisite. Continue Volume 1 crosswalk and remaining exercises/proofs.

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

**Next exact task:** inspect exact-head CI for DEP-006; repair pb:sumsquares and subsequent advanced exercises' prerequisites; complete Volume 1 crosswalk, 64 remaining named proofs, 134 remaining exercises, unnamed arguments and visual/publisher gates. 
