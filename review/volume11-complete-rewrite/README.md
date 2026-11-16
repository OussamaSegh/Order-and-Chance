# Volume 11 complete rewrite — working record

Baseline: b005c4a0a33409f443594f3bb1efe3e955e95468. Prior master-plan rewrite: PR #221; authoritative historical blueprint: PR #157 branch `claude/project-thread-khh5pi`, `docs/plan/book-11.md`. Read `docs/handoffs/volume11-rewrite.md` and `docs/WRITING-STYLE.md`.

Scope: 14 printed chapters, with Shuffling Cards at 13 and Sums of Random Pieces at 14; preserve all existing numbered statements, exercises and figure blocks. The deeper rewrite follows the Volume 10 precedent: two added mathematical figures and four solved graded exercises per printed chapter (28/56 total). Chapter 14 uses its existing problem convention. Do not touch published Volumes 1–3 or Volume 10. PR #246 is a separate downstream citation fix; integrate main normally after it lands.

## Chapter 1 first implementation (not accepted)

- Reworked introduction, distinction between tail and permutation-invariant events, transitions and prerequisites; moved the general strong law and iterated-logarithm references to explicitly marked previews.
- Fixed Rademacher moment lemma: its positive probability bound needs strictly positive variance. The zero vector is a counterexample to the original unconditional bound. Expanded the fourth-moment derivation and restricted the later exercise application.
- Completed exponential-moment equality proof using a uniform second-moment bound, clarified Levy convergence Cauchy criterion and limit identification, and replaced an unnecessary complex random-sign argument for power series radii by Cauchy–Hadamard.
- Added two mathematical figures (block swap and dyadic sum) after original figures; four graded exercises with hints and full solutions after original lists. The original label sequence and complete original figure blocks were checked unchanged; exercise/hint/solution counts increased by four each. Original artwork files untouched.
- This is a substantive first pass, not a complete sentence-level rewrite or independent review. See the current workstream status below; this entry records Chapter 1's implementation only.

No local TeX build or separate AI/human review has been performed in this session. Do not mark the chapter or volume accepted on structural checks alone.

## Chapter 2 first implementation (not accepted)

Reworked motivation and truncation explanation; clarified typical St Petersburg scale versus expected payoff and n≥2; corrected the zero-variance domain of Kolmogorov's lower maximal inequality and its application in the three-series theorem; made countable intersection explicit in Etemadi's proof; established finite renewal counts and handled infinite means explicitly; gave the renewal-reward statement its hypotheses. Added two figures and four graded solved exercises. The original label order, complete figure blocks and original exercise lists were preserved. Full proof/editorial review and build remain open.

## Chapter 3 first implementation (not accepted)

Reworked the invariance-principle motivation to distinguish weak convergence from pathwise convergence and to require continuity of path functionals. Repaired the stopping-time and independence justification in the repeated Skorokhod embedding, the degenerate zero-variance case, the Donsker time-window restriction, the maximum's vertex at time zero, the arcsine law's endpoint identification, and the countable-event argument for the LIL. Required positive cell probabilities in Pearson's statistic and positive modulus constants. Added two illustrations and four solved exercises (asymmetric exit, discontinuous occupation functional, Poisson limit and Gaussian path integral). Original labels and figure blocks preserved. Full review and build remain open.

## Chapter 4 first implementation (not accepted)

Reworked the introduction to separate uniform distribution-function accuracy, lattice-point accuracy and recurrence. Fixed the Feller-counterexample exercise for negative exponents, the nonintegral exponent in the density local-limit exercise, and positivity of Pearson cell probabilities; corrected the recurrence scope and used grouped-cell maximum likelihood for Weldon's dice (recomputed p=0.3376911823, chi-square=8.1800560, fixed-p chi-square=35.4942986). Added two figures and four complete solved exercises on rare arrays, Bernoulli Berry--Esseen factors, span-two LLT and radial integrability. Original labels and figures preserved. Full review and build remain open.

## Current workstream status

- Chapters 1–4: first implementation committed; complete sentence-level and independent proof/editorial reviews remain open.
- Chapters 5–14: not yet rewritten in this workstream.
- Added 8 mathematical figures and 16 graded exercises with hints and full solutions, toward targets of 28 and 56.
- `check_preservation.py` records the immutable baseline and enforces structural preservation and final per-chapter addition counts. Individual edited sources have been checked for preserved original label order and figure blocks, and four additional exercises/hints/solutions per chapter. The whole-repository audit has not yet run against a local checkout.
- The grouped-cell dice calculation in Chapter 4 was independently recomputed numerically. Remaining numerical tests, full TeX builds, EPUB/print checks, visual inspection, front/back matter and final exact-head CI are open.
- PR #247 remains a draft. PR #246 is independent and must pass CI before merging; incorporate it from main before final review.
