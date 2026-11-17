# Frozen original Volume 12 manuscript

**Immutable original commit:** `a685eb79a5551d0ee8a7b05074b3d01fc7677530` on `main`, the verified merge of Volume 11 PR #247.

This is the source *before* any Volume 12 complete-rewrite changes. Use `git show a685eb79a5551d0ee8a7b05074b3d01fc7677530:<path>` as the authoritative byte-for-byte original.

Original scope: `volume12-random-motion/main.tex`, 11 `chapters/ch*.tex` files, `chapters/spectral.tex`, `chapters/brw-halfmoment.tex`, preface, blurb, KDP metadata and all `volume12-random-motion/figures/**` at the baseline SHA. Do not edit published Volumes 1–11. The source of PR #222 is already included in this baseline.

**Numbering contract.** Every pre-existing formal-statement label and position, theorem/definition/example counter, original exercise and solution/hint must survive. All new exercises go after original exercise blocks and before existing hints and solutions, so downstream citations continue to resolve to their original numbers.

**Authoritative curriculum:** `claude/project-thread-khh5pi:docs/plan/book-12.md` from PR #157 (the main branch copy is historical and superseded).

Important stable labels: `thm:logclt`, `thm:sinekernel`, `prop:cuelogcorr`, `thm:gmc`, `spectral:thm:dirmatrixtree`, `spectral:thm:best`; Keating–Snaith Theorem 10.10, matrix-tree A.4. The previous numbering inventory is `review/volume12-rewrite/baseline-numbering.txt`.

The `check_preservation.py --final` audit reads frozen objects directly from the immutable SHA and also enforces two new mathematical figures and four new fully solved exercises per printed unit. **Structural preservation is not proof verification.**
