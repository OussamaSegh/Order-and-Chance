# Volume 4 — mathematical, reader, figure, and independent-review issue log

Scope: draft PR #111, branch `cursor/volume4-rewrite-ee7f`. This is an editorial working log, **not** a certificate that a chapter is accepted. Source line numbers refer to the snapshot where an issue was discovered; use the stable file, section, theorem or exercise label after edits.

## Review rule

A writer's mathematical reconstruction, critical rereading, numerical check, or compiler pass is **not** an independent second review. Every chapter needs a separate identified reviewer who examined the **exact pushed commit**. Record that reviewer's identity, date, commit, report, issue disposition, and rechecks here. At this checkpoint **none of Chapters 1–14 has a verified independent reviewer or approval**. No review is attributed to a nonexistent person or model.

## Per-chapter independent-review register

| Chapter | Authoring / writer inspection | Independent second reviewer | Unresolved gate |
| --- | --- | --- | --- |
| 1 From Games to Probability Spaces | Prior mathematical pass at `b267c681`; defect C1-01 found during Ch. 2 prerequisite check and repaired | PENDING — none assigned or reported | Recheck C1-01, diagrams, reader/voice, independent review |
| 2 Random Variables and Their Laws | All main proof statements and eight exercises/hints/solutions inspected on 6 Nov 2026; corrections C2-01–C2-07 pushed | PENDING — none assigned or reported | Post-fix critical pass, full reader/voice, native figure/PDF check, independent review |
| 3 Generating Functions and Random Families | Full source/exercise inspection; author fixes `7bb94ec9`, `87699c36`, illustration `3e63117f` | PENDING | Post-fix proof/figure pass; reader/voice, native build and independent review |
| 4 Concentration and the Laws of Large Numbers | Full source/exercise inspection and author corrections `9cb2451d` | PENDING | Post-fix critical pass; reader/voice, native build and independent review |
| 5 Continuous Chance | Draft plus `3ab3ad32` angle repair | PENDING | Mathematical and reader passes |
| 6 Why the Bell Curve Appears | Draft only | PENDING | Mathematical and reader passes |
| 7 Entropy, Codes and Typical Sequences | Draft plus `62f02af4` environment repair | PENDING | Mathematical and reader passes |
| 8 Random Walks | Draft plus `966843f6` last-visit repair | PENDING | Mathematical and reader passes |
| 9 Markov Chains and Mixing | Draft only | PENDING | Mathematical and reader passes |
| 10 The Poisson Clock | Draft only | PENDING | Mathematical and reader passes |
| 11 Martingales and Fair Games | Draft only | PENDING | Mathematical and reader passes |
| 12 Brownian Motion | Draft only | PENDING | Mathematical and reader passes |
| 13 The Probabilistic Method | Draft only | PENDING | Mathematical and reader passes |
| 14 Random Graphs and the Search for Structure | Draft plus `d07a4e33` component-count repair | PENDING | Mathematical and reader passes |

Appendix B, preface, blurb, back matter, photographs, and the full-book reader/build/voice checks remain separate open gates.

## Findings and fixes, discovered 6 November 2026

| ID | Location / precise anchor | Severity | Finding | Resolution / pushed commit | Recheck |
| --- | --- | --- | --- | --- | --- |
| **C1-01** | `volume4-chance/chapters/ch01-counting.tex`, `ex:run`, original lines 80–84 | **Major proof gap** | Showing the set with *no occurrence at all* has outer content zero proves at least one run, not infinitely many runs. | For each block-start `J`, rule out any future run using `(7/8)^M`, then take the countable union over `J`. Commit `95c84ad27ebaa87de46706fba2421eda7420781e`. | Writer checked the corrected quantifier argument against Proposition `prop:subadd`; independent verification PENDING. Earlier Chapter 1 self-signoff must not substitute for this recheck. |
| **C2-01** | `ch02-discrete.tex`, `ex:rare`, original line 63 | **Mathematical numerical error** | Upper Taylor bound was written as `0.0202 + 0.0004/(2·0.98²)`, double-counting the quadratic term. | Changed to `0.02 + 0.0004/(2·0.98²)`. Commit `01c85fbb6a5087700dad384bdf19dedea44e9af3`. | Direct arithmetic recomputed; independent PENDING. |
| **C2-02** | `ch02-discrete.tex`, `ex:rare`, original line 71 | **False example assertion** | Claimed two enclosing values both round to 0.1326 to four decimals. In fact the bounds are approximately 0.1325454 and 0.1326555, while the exact value is 0.13261956. | States actual enclosing bounds and exact direct evaluation, without claiming unwarranted four-digit precision. Same `01c85fbb` commit. | Python recomputed `0.98**100`, `exp(-2.02083)`, `exp(-2.02)`; independent PENDING. |
| **C2-03** | `ch02-discrete.tex`, `ex:birthdaywait` solution, original line 313 | **Major proof gap** | Bound `Σ_{j=1}^{m-1}j² ≤ (m-1)³/3` is false (e.g. `m=2`: `1>1/3`). | Use `Σ_{j=1}^{m-1}j² ≤ ∫₀^m x²dx=m³/3`, preserving uniform `O_A(N^{-1/2})` error. Commit `01c85fbb`. | Exact finite sums compared and the `m ≤ A√N` tail-scale inequalities rederived; independent PENDING. |
| **C2-04** | `ch02-discrete.tex`, `ex:reservoir` and solution | **Missing input hypothesis** | Uniform on the set of values fails if values repeat, although uniform **input position** is true. | Exercise and solution now distinguish stored input positions from equal item values. Commit `01c85fbb`. | Induction checked; independent PENDING. |
| **C2-05** | `ch02-discrete.tex`, `ex:quicksort` solution | **Unstated sampling hypothesis** | Stated recursive sublists were independent without explaining fresh random pivot choices; the recurrence needs only expected values. | Specifies fresh uniform pivots and no reliance on mutual independence for linearity. Commit `01c85fbb`. | Recurrence telescoped and small `n` checked; independent PENDING. |
| **C2-06** | `volume4-chance/figures/ch02-cycles.tex` | **Misleading mathematical figure** | Straight line from `(1,1)` to `(8.7,0.12)` labelled `E[X_k]=1/k` is not the reciprocal curve. | Replaced by native TikZ `y=1/x` over `k=1..8`, aligned to the expectation bars. Commit `0ba6e24dc5a2f2972a9923c1a93af378836e14bb`. | Formula/coordinates checked; native PDF visual check PENDING. |
| **C2-07** | `ch02-discrete.tex`, after countable-laws setup and hint `ex:twopoisson` | **Prerequisite / pedagogy gap** | Infinite independent coupon trials with `r` outcomes were assumed but only binary-digit products had been constructed; Poisson-addition hint invoked a limiting argument without identifying compatible binomial models. | Base-`r` cylinder argument constructs independent uniform trials; hint now proves convolution directly. Commit `fe2136ce4c4a0fd8ba1e50545820d11ca6015016`. | Cylinder probabilities and convolution algebra checked; independent PENDING. |

## Chapter 2 writer-check evidence (not independent review)

- Read the full chapter, including the Poisson limit, fixed-point Poisson approximation, cycle expectation, coupon collector, eight exercise statements, eight hints, and eight solutions.
- Checked formulas: `E[X_k]=1/k`, `E[C_n]=H_n`, `E[T]=nH_n`, `Var(F_n)=1`, Quicksort `E[Q_n]=2(n+1)H_n-4n`, Poisson falling factorial moments, reservoir-sampling induction, long-cycle disjointness, hundred-prisoner probability `0.3118278206898...`, and Poisson convolution.
- Reconstructed the birthday expectation as the sum of no-collision tail probabilities and compared it with a Riemann integral on scale `√N`. Original `(m-1)^3/3` error has been fixed; final source should be reread after all edits.
- Checked all nine `k=0..8` binomial-vs-Poisson figure entries numerically against the displayed formulas. Replaced the false straight-line expectation plot. Native PDF visual verification **not performed**.
- Cross-referenced earlier Volume 1 finite probability, convergence, Stirling, the Gaussian integral, and the Chapter 1 digit construction. Added the base-`r` trial bridge. Later-volume citation migration still open in `docs/plan/volume4-citation-migration.md`.
- Bibliography checks against external sources: BnF confirms Poisson (Paris: Bachelier, 1837); Wiley confirms Feller vol. I (3rd ed., 1968); MathNet / journal references confirm Goncharov 1942 `35:267–269` and 1944 `8:3–48`. These checks are not a comprehensive independent historical review.
- Remaining: repeat a post-fix writer second pass; exact pushed SHA second reviewer with identification/report; voice/reader checks; native PDF and downstream reference checks. **No checkmark for acceptance.**


## Chapter 3 findings (writer inspection; independent reviewer PENDING)

| ID | Location | Severity | Finding | Resolution | Recheck |
| --- | --- | --- | --- | --- | --- |
| **C3-01** | `ch03-generating.tex`, `prop:randomsum` and proof | **Major prerequisite** | An infinite Cartesian product of countable sets need not be countable; the draft described such a product as though it were a Volume 1 countable probability model. | Conditional finite-list sampling after drawing `N`, with disjoint union of finite products and nonnegative sums. Commit `7bb94ec95a0fa94b3d53c7ed9d40c5f9d0b0869e`. | Algebra reconstructed; a distinct reviewer has not verified the exact corrected commit. |
| **C3-02** | `thm:extinction`, increasing extinction events | **Major proof gap** | Finite additivity alone cannot justify passage to the probability of an increasing countable union. | Express extinction as the disjoint union of *first*-extinction-at-`j` events; nonnegative series give `η=lim η_n`. Commit `7bb94ec9`. | Writer checked series telescoping; independent PENDING. |
| **C3-03** | `prop:pgfmean` and pgf differentiation | **Proof exposition** | Infinite-sum differentiation and limit interchange lacked an explicit finite-partial-sum squeeze suitable for infinite means. | Uniform derivative domination on `[0,r]`, finite-partial-sum upper/lower argument, and nonnegative-series quotient for supercritical extinction. Commit `7bb94ec9`. | Writer check only. |
| **C3-04** | `ex:poissongw` solution | **Missing limiting step** | Claim `ρ(c)→0` near `c=1` lacked a stated justification before the asymptotic expansion. | Compactness/subsequence and uniqueness at `c=1`, with uniform Taylor remainder. Commit `7bb94ec9`. | Writer check only. |
| **C3-05** | `ch03-generating.tex`, Catalan generating function | **Convergence justification** | Series product used before the convergence interval was justified. | Bound `C_n≤binom(2n,n)≤4^n`, hence absolute convergence for `|x|<1/4`. Commit `87699c3633d928a3e30f668912deda2445aed091`. | Writer check only. |
| **C3-06** | `figures/ch03-familytree.tex`, Galton–Watson exposition | **Missing pedagogical figure** | Branching recursion had no source diagram. | Added a possible generation-0–2 tree, explicitly labelled as a possible outcome rather than a frequency. Figure commit `3e63117ff7db8587c950c2e317fd714f54e01254`; integrated via `87699c36`. | Native TeX and PDF layout/render check PENDING. |

Chapter 3 writer inspected the chapter's three numbered main results, all eight exercise statements, hints and solutions, Catalan identities, extinction cases including `p_1=1`, Poisson thinning, finite/infinite progeny and first passage. No independent second review, post-fix critical pass or production build is claimed. An external university probability course confirms the standard extinction fixed-point statement; this is supporting literature, not a second-review signoff.

## Chapter 4 findings (writer inspection; independent reviewer PENDING)

| ID | Location | Severity | Finding | Resolution | Recheck |
| --- | --- | --- | --- | --- | --- |
| **C4-01** | `lem:hoeffding` / `thm:hoeffding` | **Endpoint proof gap** | Chord proof divided by `b-a` when `a=b`; Hoeffding's denominator vanishes when every summand is constant. | Separate both degenerate cases explicitly; use `D>0` for exponential optimisation. Commit `9cb2451d334c849856903efdc140e39bf914ced6`. | Writer recomputed inequality; independent PENDING. |
| **C4-02** | `thm:bc` part (b) | **Major proof gap** | Zero probability of *no future event after a fixed N* does not alone establish infinitely many occurrences. | Write `{only finitely many}=⋃_N ⋂_{n≥N} A_n^c` and use outer-content countable subadditivity. Commit `9cb2451d`. | Writer checked quantifiers; independent PENDING. |
| **C4-03** | `ex:bcfinite` hint/solution | **Major false construction** | Draft claimed an infinite product of countable spaces is countable, and offered geometric waiting-time thresholds giving exactly `1/n` without justification. | Construct exact independent `1/n` and `1/n²` cylinder events by successive equal partitions of intervals with varying radices `n` and `n²`. Commit `9cb2451d`. | Product cylinder lengths `1/n!` and `1/(n!)²` checked; independent PENDING. |
| **C4-04** | `thm:sllnbound` and following paragraph | **Overclaimed prerequisites** | A fixed finite block of *binary* digits cannot simulate all finite-alphabet probability laws exactly, such as probability `1/3`; the old text claimed that it could. | Scope to finite cylinder partitions of arbitrary fixed/mixed base and rational finite-alphabet laws, with general bounded laws explicitly deferred. Commit `9cb2451d`. | Prerequisite reasoning checked; independent PENDING. |
| **C4-05** | Figure `ch04-chernoff` caption | **Incorrect mathematical label** | Plot values are the **one-sided** Hoeffding bound `exp(-2nε²)`; a two-sided bound would include factor 2. | Caption explicitly calls the event one-sided and describes Chebyshev's two-sided upper bound as a valid looser one-sided estimate. Commit `9cb2451d`. | Raw plot values inspected; PDF visual PENDING. |
| **C4-06** | `thm:weierstrass` proof and `ex:runs` | **Proof clarity** | Weierstrass proof stopped at `2ε` rather than translating back to an arbitrary tolerance; runs proof implicitly needs `0<ε<1`. | Explicit tolerance `η/2` and exercise domain. Commit `9cb2451d`. | Writer check only. |

Chapter 4 writer inspected five main numbered environments, six exercises, hints and solutions, logarithmic tail numerics, the bounded-variable assumptions, the one-sided bounds and the associated TikZ figure source. Checks confirm `P(Bin(1000,1/2)≥600)≈1.364232078×10^-10`, `e^-20≈2.061153622×10^-9` and the entropy-optimised bound `≈1.799938120×10^-9`. **No native PDF, independent review or full post-fix source reread completed.**

## Project-wide blockers

1. No distinct independent mathematical reviewer has yet examined an exact pushed chapter commit. Every independent-review gate stays PENDING.
2. This chat runtime has GitHub connector access for branch reads/writes but no git network transport (DNS lookup of github.com failed) and no mounted full repository. Native `./build.sh volume4-chance` and PDF visual checks were **not run here**; prior 135-page one-pass XeLaTeX remains provisional evidence only.
3. No edits to Volumes 1–3 or Volumes 5–15. Downstream references remain listed as unresolved migrations, not silently repaired.
4. The 400–500-page planning target has not been measured on a completed native book; do not infer a page count from any draft.
