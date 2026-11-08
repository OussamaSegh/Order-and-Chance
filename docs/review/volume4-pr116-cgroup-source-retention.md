# PR #116 — protected Volume 3 conceptual-source seam review

**Date:** 8 November 2026  
**Purpose:** Explain, verify and retain a previously accepted *internal* Volume 3 conceptual ledger after a narrow Volume 4 correction. The protected guard must still compute the full source fingerprint and reject any unreviewed drift. **This note is source-side internal evidence, not independent human mathematical refereeing, book approval, or permission to weaken the guard.**

## Why the guard failed

[PR #116](https://github.com/OussamaSegh/Order-and-Chance/pull/116) changes `volume4-chance/chapters/ch08-markov.tex`, one of the **90 exact paths** in `review/volume3-internal/concepts.json`'s `reviewed_snapshot`. The initial `main` source matches its registered SHA-256 exactly; the PR head does not. As designed, `review/volume3-internal/check_global_ledgers.py` reports `Whole-volume conceptual source/figure drift: C-GROUP` before allowing the full publishing build.

At the audited source head `6c288e8a848deab07cd6f7a0c58dd07c7fd26a20`, the exact source fingerprint data are:

| Check | Value |
| --- | --- |
| Tracked sources in previous review fingerprint | 90 |
| Source paths changed by this PR that belong to that review fingerprint | **1**, `volume4-chance/chapters/ch08-markov.tex` |
| Prior Markov source SHA-256 | `9758b812a3bff0f8d8a0ba9da540e3ca34b7abd9c8361a7abd469a3bea5ac274` |
| Corrected Markov source SHA-256 | `02b8a27b1cf8ba8341c078820737b26f606cf8e55badda7afce2020093c16b2d` |
| Prior whole-review fingerprint | `53041fccdb247c15c3009c27f95fad78aa949aac2d938360b86ae331a4c6dbf2` |
| Corrected whole-review fingerprint | `89915e3a8d86d5d43f276e3d8a222a071daa81d3e62963d1233be4e52b7ee38f` |

The single-file source hashes were computed from UTF-8 GitHub file bytes, and the whole-review hashes from the source list using the guard's canonical sorted-key compact JSON convention. The previous snapshot's own fingerprint was recomputed and matched the stored value before the corrected fingerprint was calculated.

The **89 other tracked paths are untouched by this PR relative to `main`**, as determined by its complete diff (not 89 individual proof rereads). No Volume 1–3 manuscript path, common template, figure input or external reference source is modified by PR #116.

## Targeted source-content audit

A direct old-versus-new `ch08-markov.tex` line comparison found **exactly two changed physical lines, with no changed line count**:

1. **Line 299:** The three-decimal 52-card riffle table originally said `d_k=1` for `k≤4`. The revision explicitly says the calculated values **round to 1.000**, while the exact total-variation distances are strictly below 1. The identity permutation has positive probability after any positive number of ordinary riffle shuffles, and the uniform law also assigns positive mass to it, so the two distributions overlap. An exact Eulerian-number computation in `tools/test_volume4_math_audit.py` independently checks all ten printed rounded values.
2. **Line 304:** The caption previously stated that distance “stays at 1.” The revised caption correctly says the first four **plotted** values round to 1, and explains that the curve comes from a finite formula, not sampled data.

No theorem statement, proof, hypothesis, exercise, hint, solution, label, inclusion order, definition of stochastic matrices, Markov mixing proof, sample-space law, figure source or downstream Volume 3 proof changed.

## Conceptual dependencies re-read for this retention

- Volume 3 `chapters/preface.tex` lines 12 and 45: a shuffle is a permutation, and Volume 4 introduces random transformations. These claims are untouched by the later decimal precision of a 52-card *random* riffle chain.
- Volume 3 `chapters/afterword.tex` lines 4–42: a two-state random walk and its convergence to uniform illustrate random motion; the Chapter 9 riffle round-off does not change the two-state transition matrix or its argument.
- Volume 3 `chapters/linear-ch07-perron.tex` (Markov/PageRank and the shuffled-permutation model): its existence, stationarity and primitive-stochastic-matrix conclusions do not use the numerical riffle table. The correction does not alter the proof hypotheses or any mathematical claim used in that V3 chapter.
- Volume 3 `chapters/ch04-symmetric.tex`: deterministic perfect shuffles and random transpositions are different models from the Gilbert–Shannon–Reeds riffle model; no finite shuffle law or exact numerical proof was changed.
- One **separate inherited editorial issue**: Volume 3 `linear-ch07-perron.tex` line 784 says “Volume 4, Chapter 8 returns to convergence by coupling.” In the approved fourteen-chapter Volume 4, Markov chains are **printed Chapter 9**. This is a *published* Volume 3 cross-reference issue, **not introduced by PR #116**. It is recorded for a later author-approved correction; Volume 3 source must remain unchanged here.

**Scope decision:** The mathematical group-concept definitions, examples, proofs, original anchors and later-use chains retained by the previous V3 internal review are unaffected by these two numeric/caption wording corrections. The previous internal acceptance may therefore be retained against the new tracked source fingerprint **after this targeted change review**, without re-awarding a new review status.

The original 120 internal conceptual rows, their classifications, first-use anchors and historical review evidence remain unchanged, except for updating the common fingerprint to the corrected source revision. This is an exact-source freshness migration for a **nonpremise** numerical/caption fix, not a claim to have redone V3's entire conceptual review or to have independently refereed the correction.

## Validation and constraints

The PR's native V4 workflow previously passed at an earlier source revision, while the protected full build failed on the obsolete conceptual fingerprint. On this proposed review-retention change, **both full and V4 native workflows must rerun on the exact new PR head**. The protected check must compute the new fingerprint from actual source files rather than being disabled or skipped. If it detects any other drift, leave the gate red and investigate it; do not patch the expected fingerprint without a new source comparison.

No published Volume 3 mathematical text was changed. No production release signoff, independent math-review signoff, Kindle inspection or KDP approval is recorded by this note.
