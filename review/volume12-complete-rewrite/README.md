# Volume 12 — complete-rewrite implementation and verification

**Baseline:** `a685eb79a5551d0ee8a7b05074b3d01fc7677530` (already includes PR #222 and merged Volume 11 PR #247). **Reference:** PR #157's newer `book-12.md`; Volume 11 final acceptance in `review/volume11-complete-rewrite/ACCEPTANCE.md`.

The implementation adds two mathematical TikZ figures and four graded, hinted, fully solved exercises to each of the 11 chapters and Appendix A: 24 illustrations, 48 exercises, 48 hints and 48 complete solutions. Original labelled statements, old exercise/hint/solution lists, chapter order, and historical figure assets are preserved by a frozen-baseline CI check. The teaching additions cover Brownian covariance and bridges, modulus and reflection, time-changing martingales, Itô integrals, heat/Girsanov, OU/Dyson, Lévy processes, resistive networks, the semicircle/outlier threshold, sine-kernel/CUE moments, log-correlations/chaos, and matrix-tree/BEST.

## Verification and acceptance gates

1. Source inventory: `python3 review/volume12-complete-rewrite/check_preservation.py --final` compares original source to immutable Git objects and checks new exercise/hint/solution pairings.
2. Arithmetic: `python3 review/volume12-complete-rewrite/check_new_examples.py`, all `review/volume12-rewrite/check_ch*.py` and `check_appA*.py` checks, and the project-wide unit suite. One independent deterministic computation per printed unit is included; statistical simulations are not proof checking.
3. Printed citation audit: numbered references to/from Volume 12 across the fifteen-volume structure; preserve Chapter 10 and Appendix A references exactly.
4. Mathematics: review every statement/proof and classify independently rederived arguments versus author-side checks, quoted/admitted results, and zeta-zero conjectures. Track any conjectural or external signoff status without overstatement.
5. Production: full GitHub `Build books` workflow, inspect actual reading PDF, KDP bleed/cover/interior, EPUB images/math/links/navigation/accessibility, online reader and metadata. Record checksums for the actual generated outputs and show visual rendered-page review.
6. Acceptance: do not merge on the strength of a passing structural/numerical audit alone; merge only after mathematical author-side acceptance, final production build, and physical artifact inspection have passed.

The author-side review is distinct from **unavailable independent third-party mathematical certification**. The audit workflow is intentionally branch-scoped so it cannot alter already accepted volumes.

**Status:** Implementation committed; production and mathematical acceptance pending evidence. No automatic approval is implied by this working record.
