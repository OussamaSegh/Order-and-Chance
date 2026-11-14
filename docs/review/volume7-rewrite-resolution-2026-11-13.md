# Volume 7 rewrite: second-review resolutions, 13 November 2026

Source of truth: [the full independent review on PR #241](https://github.com/OussamaSegh/Order-and-Chance/blob/cursor/volume7-second-review-9e0e/docs/review/volume7-rewrite-second-review-2026-11-13.md), read in full. The continuation started from `9b1114a32ce36f367bd1af3a672a5b911bdc8880`, the latest remote head of PR #237. All 23 requested repairs were already present there. This pass checked their statements, proofs, hints and drawings, then corrected the additional slips listed below.

## Finding-to-commit map

A second commit in a row records a follow-up found during this continuation. Every commit is on PR #237; no review branch was merged.

| Finding | Repair commit(s) | Verified result |
| --- | --- | --- |
| V7-1 | `129f777d` | The exponential spike satisfies `f_m(x) > m/e >= 1/(2ex)`. |
| V7-2 | `129f777d`, `fd967597` | Both endpoints are included; the decreasing case applies the increasing case to `-y`. |
| V7-3 | `129f777d`, `9b1114a3` | Both almost-surely quantifiers remain. `X_0 = X 1_{X>=0}` is introduced before monotone convergence, with the original `X` visible in the integral identities. |
| V7-4 | `129f777d` | The counting-measure solution cites `thm:continuum`. |
| V7-5 | `6f03a1ed` | Dominated convergence explicitly assumes the limit is measurable. |
| V7-6 | `6f03a1ed` | The cut plate uses `4/3`, `1.4`, and `1.41`, three distinct rationals. |
| V7-7 | `6f03a1ed` | The dashed segment ends strictly inside the open-ball boundary. |
| V7-8 | `6f03a1ed` | The 1924 paper gets a finite decomposition; Robinson (1947) gets five versus four pieces. |
| V7-9 | `6f03a1ed` | The square-root proof compares `h(2s+1) < h(2s+2) < x-s^2`. |
| V7-10 | `9b1114a3` | Uniform limits are continuous by the neighbourhood estimate, without assuming a metric. |
| V7-11 | `9b1114a3` | The complete space in the Baire corollary is nonempty. |
| V7-12 | `9b1114a3` | The uncountable interval contains two points. |
| V7-13 | `9b1114a3` | Interval covers are enlarged before compactness; infinite endpoints and `c=b` are treated. |
| V7-14 | `9b1114a3`, `56aea886` | Every component has an endpoint in `J`; the empty case is separate. The mean-value identity includes its interval-length factor. |
| V7-15 | `9b1114a3` | Both real-coordinate comparisons precede the rectangle containment. |
| V7-16 | `9b1114a3` | The exit time may equal `1`; both cases reach the boundary or contradict openness. |
| V7-17 | `9b1114a3`, `56aea886` | The coral arrow makes a full turn. The charcoal arrow also points counterclockwise, agreeing with winding number `1`. |
| V7-18 | `9b1114a3` | The typewriter indicator has squared L2 norm `2^{-k}` and L2 norm `2^{-k/2}`. |
| V7-19 | `9b1114a3` | Positivity everywhere makes the union of the level sets equal to `E`, of measure `1`. |
| V7-20 | `9b1114a3` | Jensen is first applied to bounded truncations; monotone convergence establishes integrability before the untruncated application. |
| V7-21 | `9b1114a3` | The caption describes a continuous piecewise-linear trapezoid that still has corners. |
| V7-22 | `9b1114a3` | Measurability for the trivial sigma-algebra means constant everywhere. |
| V7-23 | `9b1114a3` | Both Baire solutions and the hint use the open intervals spanned by cylinder closures; the digit conditions follow after excluding the rationals. |

## Numbered-statement audit against main

The comparison used `origin/main` at `3092c046`. All 308 original numbered environments have the same kind, printed number and label in the same order. This includes definitions, examples and exercises, and the polygon subfile input by the Jordan chapter. All 323 original labels survive; 76 labels are added and none is duplicated. The 52 added exercises are the last four exercises in each of the thirteen chapters. The figure-file diff against main contains additions only.

Every original numbered statement was compared in full, including its hypotheses, quantifiers and conclusion. The additional restriction `a,b,c>1` in `ex:youngconv` narrowed the three-function Hölder exercise. Commit `fd967597` restores `1 <= a,b,c <= infinity` and proves the endpoint cases by essential-supremum bounds and the earlier two-function Hölder inequality. The Basel exercise again requires justification of every exchange of limits, including sum-integral exchanges.

The comparison also makes these corrections to false or underspecified statements explicit, rather than describing them as prose alone:

- Dominated convergence requires a measurable limit on a space that need not be complete (V7-5).
- The Baire corollary needs a nonempty complete space and an interval containing two points (V7-11 and V7-12).
- `ex:hamel` uses nonempty open intervals for unboundedness, and `ex:monotone2` uses nondegenerate intervals for failure of monotonicity. A singleton cannot satisfy either conclusion.
- The local-extremum clause of `thm:mvt` says that the extremum is at an interior point. The layer-cake moment identity explicitly uses `p>0`. The mass-distribution lemma explicitly quantifies its finite constant and positive scale. Log-convexity is stated where the logarithm is finite.

No other dropped hypothesis or quantifier was found. No printed number moved, so no cross-volume renumbering was needed.

The same reading caught three proof/hint slips repaired by `fd967597`: the missing factor `||f||_p` in the last Hardy bound, the variable in the scaled-function norm used to motivate that proof, and the reversed sign of the nonnegative Young gap in the Hölder-equality hint. It also corrected the Baire chapter's uncountability citation to `thm:continuum`. These use tools already taught.

The cylinder arguments were rechecked directly: every relatively open interval contains the closure of a sufficiently small cylinder; prolonging its digit word forces the requested inequality or last digit. Removing the countably many rationals makes membership in the spanning interval equivalent to membership in its irrational cylinder. The measure argument for repeated digit `1` uses the earlier conditional lower bound `1/4`, and the large-digit argument uses Borel–Bernstein with the divergent harmonic series. No ergodic theorem is used.

Only the winding plate added by this rewrite was edited during this continuation. No pre-existing figure file was edited. Across all second-review repairs, the other edited plates are `ch01-rw-cut` and `ch02-rw-open`, also additions in this rewrite.

## Validation

Local `./build.sh --pdf-only volume7-spaces` exited 0 after the manuscript repairs. The print interior has **409 pages**, each 513 by 738 pt. The reading PDF has **410 pages**, including its front cover. The final TeX log has no overfull box and no undefined reference. The layout check reports 394 whole boxes, maximum height 288.5 pt, no overflow and no unresolved reference. Interior and paperback-cover preflight passed. The corrected winding arrows were inspected in the rendered PDF.

`python3 -m unittest discover -s tools -p '*citation*.py'` ran 18 tests and passed. `python3 tools/cross_volume_citations.py` exited 0 and checked 4,903 numbered statements. `python3 review/volume3-internal/registers.py` exited 0 with `{"accepted-internal": 1177, "pending": 19}`. `git diff --check` passed.

Exact-final-head CI run IDs and conclusions belong in the PR description and the author-facing handoff message once those runs finish. No extra commit will be pushed just to record a run. PR #237 remains unmerged; Volume 8 has not been started in this continuation.
