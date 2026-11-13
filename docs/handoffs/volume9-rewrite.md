# Handoff: Volume 9 rewrite

Volume 9, *Shapes*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-09.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-k4hv7k`, one pull request for the whole volume, as Volumes 5–8 each landed on their own pull request. The master plan and the blueprints stay on PR #157 (branch `claude/project-thread-khh5pi`), which remains open and is not merged. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-09.md`. Where it differs from the copy on `main`, the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps the structure of Volume 9 ("Structure: unchanged"; "Preserve. All chapters and appendices, in their order"): eleven chapters in three parts and eleven appendices A–K. `main.tex` already matches the blueprint's table, so no chapter moves and no chapter number changes. The work is one pass per chapter with the list used for Volumes 5–8:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number or formula that is not proved on the page is recomputed by a script in `review/volume9-rewrite/`, one per chapter (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources" section.
5. **References.** Citations of other volumes checked against their printed order today (Volume 5 after its renumbering, `docs/plan/volume-citation-map.md`; Volume 7 after Chapters 2, 6, 13 changed; Volume 8 after its restructure into sixteen chapters and Appendices A–F; Volume 6 `thm:fundamental` after D-20).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses a later chapter or a later volume (10–15) as a premise.
8. **Build.** The volume builds with no undefined reference.

Numbering inside each chapter is preserved: new statements and exercises go at the end of a list, because Volumes 10–15 cite Volume 9 by hand-typed numbers. `review/volume9-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

Gate B of the master plan (independent verification) is not this pass.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Smooth Manifolds | `ch01-manifolds.tex` | Done |
| 2 | Vector Fields and Flows | `ch02-flows.tex` | Done |
| 3 | Differential Forms and Stokes' Theorem | `ch03-forms.tex` | To do |
| 4 | Curvature | `ch04-curvature.tex` | To do |
| 5 | The Fundamental Group and Coverings | `ch05-coverings.tex` | To do |
| 6 | Homology | `ch06-homology.tex` | To do |
| 7 | Matrix Lie Groups | `ch07-liegroups.tex` | To do |
| 8 | Haar Measure and Weyl Integration | `ch08-haar.tex` | To do |
| 9 | The Hyperbolic Plane and the Modular Group | `ch09-hyperbolic.tex` | To do |
| 10 | The Riemann Mapping Theorem | `riemann-mapping.tex` | To do |
| 11 | Integral Geometry | `ch10-integral.tex` | To do |
| A–K | Appendices | `geometry-ch02` … `geometry-ch12` | To do |
| — | Preface, blurb, `kdp.md`, citations of Volume 9 in other volumes | | To do |

## What changed, chapter by chapter

- **1.** Opening question; closing section. The null-set lemma cited Carathéodory's extension theorem (Volume 7, Theorem 7.10) for a cover by cubes: now outer regularity (Volume 7, Proposition 7.12) and the dyadic cubes of its proof. Check: `check_ch01_manifolds.py`.
- **2.** Opening question; closing section. Equidistribution of $k\alpha$ now cites Volume 5, Corollary 6.14 (it cited Volume 6, Chapter 11). The escape lemma no longer restarts at a negative time when $\beta<\tau/2$. Check: `check_ch02_flows.py`.

## Tools

`review/volume9-rewrite/statements.py <volume dir>` prints every numbered statement in printed order. `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py` lists hand-typed numbers inside the volume. `list_citations.py` lists every citation of another volume.

## How to build

`./build.sh --pdf-only volume9-shapes`, or `xelatex` in `volume9-shapes/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
