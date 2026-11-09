# Volume 4 — Phase 2 sole-validator continuation, 9 November 2026

## Scope and baseline

- Author decision: **ChatGPT GPT-6 is the only mathematical validator**. No external mathematical referee signature is required. A validation by the agent that edited the source must be described as *sole-validator/self-review*, not independent external review.
- Exact starting `main`: `ac9032796a8eae1836617f301f89f936fbc2429c` (PR #120). Exact pre-change Chapter 11 TeX blob: `7cbc0f7a749af5fbf16ee17455ff1bd9fe7ff291`.
- Printed Chapter 11 is `volume4-chance/chapters/ch10-martingales.tex`. No changes to published Volumes 1–3 or the 14-chapter/four-part/Appendix B architecture.

## V4-P2-010 — anticipative random time mislabeled (P2 precision)

Location: `def:stopping`. The definition previously said to *declare the stopping time* to be N if X_N > 0 and 0 otherwise, immediately explaining that this is **not** a stopping time. The phrase introduces a contradiction in the teaching of stopping times.

Proof of the distinction: in the two-outcome fair one-step walk, X_0=0, X_1∈{−1,+1} equiprobably; put tau=1 if X_1>0 and tau=0 otherwise. Then `{tau≤0}={X_1=−1}`, an event of probability 1/2 not belonging to the initial sigma algebra `{∅,Ω}`. Thus this bounded random time **violates** the stopping-time criterion at time 0. The source now explicitly calls it a *random time*, assumes N≥1, and spells out the one-step counterexample.

Regression: `test_volume4_pattern_waiting.py::test_anticipating_clock_fails_time_zero_measurability` computes the event and checks the source's amended wording. **Disposition: SOURCE-CORRECTED; sole validator checked the counterexample.**

## Targeted VERIFIED claim — ABRACADABRA exact expected waiting time

Location: `thm:monkey`, Chapter 11, baseline TeX blob `7cbc0f7a749af5fbf16ee17455ff1bd9fe7ff291`. The theorem states that independent uniform 26-letter draws take mean `26^11+26^4+26 = 3,670,344,487,444,778` to first ABRACADABRA.

Two methods were checked:

1. **Source proof reading:** At each time a new gambler brings one unit of wealth; the total wealth minus number of entrants is a finite-information martingale. Bounded stopping at tau∧N preserves expectation. Before the first completion, at most eleven active gamblers can survive, each with wealth at most 26^11; the same bound holds at the first completion. The difference between stopped and terminal wealth expectations is at most `11·26^11 P(tau>N)→0`. Disjoint eleven-letter blocks ensure `tau<∞` a.s. and justify passage to the expected stopping time. At first completion, the surviving prefixes are the full word, ABRA and A, of lengths 11, 4 and 1, respectively. Their fixed wealths add as claimed.
2. **Independent mathematical computation:** A finite-state automaton stores the length `i∈{0,…,m−1}` of the longest observed suffix equal to the word prefix; reading a letter moves to `j`, and full length `m` is absorbing. For each state set `E_i=1+q^{−1}∑_{c∈alphabet} E_{next(i,c)}`, with `E_m=0`. Solve the exact `(I−Q)E=1` system by rational Gaussian elimination. No casino wealth, optional stopping, or prefix/suffix expectation formula is used. With m=11, q=26 the exact answer is 3,670,344,487,444,778. With the binary alphabet, HT has mean 4 and HH has mean 6; the method additionally verifies HTH=10, HHH=14, HTT=8 and all one/two-letter binary patterns.

Regression: `tools/test_volume4_pattern_waiting.py`, exact `fractions.Fraction` arithmetic, with no floating-point approximations. **Disposition: SOLE-VALIDATOR VERIFIED for this named theorem only**, on the baseline blob. If the theorem proof changes, its validation must be revisited. This is not an assertion that the other Chapter 11 proofs have been validated.

## Existing corrections and technical gates

Previous V4-P2-001…009 source corrections are integrated in PRs #117, #118 and #120. PR #120 exact head `3a66b66432b87bb672e993c8f44b9803515ecc75` passed both Build books 42535668300 (553 tests run, 32 skipped, site success, publication skipped) and native QA 42535668191 (285-page print, 268 layout boxes with no overflow/reference failures, both print preflights pass, 41 figure plates, 10,543 formula occurrences). This branch must pass its **own** exact-head unit/full-build/native QA checks before merging.

## Remaining acceptance work

Not yet reviewed means exactly that. The named Chapter 11 theorem's verification does not close the whole chapter. Finish the 14 printed chapters, Appendix B and each of 107 exercise statements/hints/solutions; scrutinize all 41 figure semantics and output readability; check prerequisite/downstream references. Preserve published Volumes 1–3 and require the author's final publication release approval. **Do not wait for a second mathematical referee**: the author has explicitly assigned sole validation to ChatGPT GPT-6.
