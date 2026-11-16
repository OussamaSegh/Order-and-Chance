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

## Chapter 5 first implementation (not accepted)

Reworked infinite-divisibility/stability motivation. Corrected gamma shape factor in the Lévy measure and compensated drift convention for gamma, compound Poisson and positive stable examples. Handled zero-mass finite measures in the representation and triangular-array limits, boundary atoms, independence in the domain-of-attraction statement, and discrete infinite waiting time versus a weak limit. Added two figures and four fully solved exercises on convolution roots, drift, stable scales and closure. Full review/build remain open.

## Chapter 6 first implementation (not accepted)

Reworked Stein motivation and supplied a direct characteristic-function proof of the Gaussian characterization. Corrected the falling-factorial recursion, zero Wasserstein case, positive Poisson intensity, hypergeometric nondegeneracy and fourth-moment assumptions; justified the exact closest integer head-run length using two adjacent approximations and monotonicity. Added two figures and four solved exercises. Full review/build remain open.

## Chapter 7 first implementation (not accepted)

Reworked large-deviation motivation; distinguished global exponential-moment hypothesis from the exponential example and quoted Bahadur–Rao hypotheses; removed an unsupported importance-sampling guarantee; handled empty conditioning/compact sets, corrected the shrinking-deviation hint and clarified asymptotic testing sample size. Added two figures and four solved exercises on tilting, types, Gaussian tails and rate curvature. Full review/build remain open.

## Chapters 8–14 first implementation (not accepted)

- **8, concentration:** refined variance/entropy and bounded-difference assumptions, repaired zero constants and convex-distance/certificate boundary cases, added cube-distance and bounded-difference illustrations and four solved exercises.
- **9, martingales:** strengthened optional-stopping and maximal-event justifications, repaired the Kakutani example and the treatment of zero probabilities and sequential testing; added two figures and four solved exercises.
- **10, ergodic theory:** corrected finite-cycle/nonergodic illustrations, recurrence and continued-fraction qualifications, added two figures and four solved exercises.
- **11, mod-phi:** distinguished convergence domains and residue evaluation, clarified Dirichlet versus uniform integer models and admitted Selberg–Delange, added two figures and four solved exercises.
- **12, permutations:** repaired finite-cycle counting and limiting Poisson–Dirichlet qualifications, added two figures and four solved exercises.
- **13, shuffling:** corrected cutoff integer-time and spectral estimates, clarified random-transposition and riffle hypotheses, added two figures and four solved exercises. The separate riffle-cutoff input remains in Chapter 13.
- **14, problems:** repaired the dependence range for peaks and block CLT normalization, prime-size condition for three-term progressions, Bernoulli-convolution evidence and the misuse of a limiting Kolmogorov distribution as a finite-sample tail. Added two figures and four solved problems; extended the problem map.

## Current workstream status

- All 14 printed chapters have a substantive first implementation. The 182 original formal blocks, 110 exercises/problems and 30 figure environments remain in their original order, with 28 new figures and 56 new exercises/problems, each with a hint and solution. Source comparison of all 15 chapter files against the immutable baseline passed: labels, formal blocks, original exercise order, figure blocks and section/subsection/equation counts. Original figure files were not modified. This does not certify the proofs.
- The separate PR #246 citation corrections passed production CI and merged into main at 75eb4e3f3f7eb84a90b7222224c2270d5bc17fd6; PR #248 integrated that main into this rewrite branch. No changes to Volumes 1–3, 10 or 13 remain in the rewrite diff against main.
- Preface rewritten: precise Donsker hypotheses, infinitesimal-array/stability scope, proved versus quoted results and prerequisites. Cover artwork preserved. New figure tick-label/plot-domain polish applied.
- New deterministic arithmetic/enumeration checks: `node review/volume11-complete-rewrite/check_new_examples.mjs` executed successfully for all 14 chapter groups. These supplement, not replace, the original numerical review scripts or proof review.
- Added a branch-scoped exact-head CI audit `.github/workflows/volume11-rewrite-audit.yml` running the immutable preservation check and new regressions. The normal production workflow is unchanged. Its result and the full build must be checked on the final head.
- Open acceptance gates: full sentence-level and hostile proof/editorial review, original numerical regressions and citation verification, exact-head TeX/EPUB/print CI, rendered page/figure inspection and production acceptance. No independent reviewer has certified the rewrite. PR #247 remains draft until these gates are complete.
