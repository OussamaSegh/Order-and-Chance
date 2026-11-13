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
| 3 | Differential Forms and Stokes' Theorem | `ch03-forms.tex` | Done |
| 4 | Curvature | `ch04-curvature.tex` | Done |
| 5 | The Fundamental Group and Coverings | `ch05-coverings.tex` | Done |
| 6 | Homology | `ch06-homology.tex` | Done |
| 7 | Matrix Lie Groups | `ch07-liegroups.tex` | Done |
| 8 | Haar Measure and Weyl Integration | `ch08-haar.tex` | Done |
| 9 | The Hyperbolic Plane and the Modular Group | `ch09-hyperbolic.tex` | Done |
| 10 | The Riemann Mapping Theorem | `riemann-mapping.tex` | Done |
| 11 | Integral Geometry | `ch10-integral.tex` | To do |
| A–K | Appendices | `geometry-ch02` … `geometry-ch12` | To do |
| — | Preface, blurb, `kdp.md`, citations of Volume 9 in other volumes | | To do |

## What changed, chapter by chapter

- **1.** Opening question; closing section. The null-set lemma cited Carathéodory's extension theorem (Volume 7, Theorem 7.10) for a cover by cubes: now outer regularity (Volume 7, Proposition 7.12) and the dyadic cubes of its proof. Check: `check_ch01_manifolds.py`.
- **2.** Opening question; closing section. Equidistribution of $k\alpha$ now cites Volume 5, Corollary 6.14 (it cited Volume 6, Chapter 11). The escape lemma no longer restarts at a negative time when $\beta<\tau/2$. Check: `check_ch02_flows.py`.
- **3.** Opening question; closing section. Brouwer for the disc is Volume 7, Theorem 6.7 (the text said Volume 8); the dog on a leash is Volume 7, Proposition 6.6; Fubini cited as Volume 7, Theorem 9.6. Check: `check_ch03_forms.py`.
- **4.** Blueprint item: the two statements without a proof on the page, Corollary `cor:gaussbonnet` and Corollary `cor:chimorse`, now have proofs (the first says why it does not use itself through Theorem `thm:morseexists`; the second classifies non-degenerate critical points of a surface). Gauss's field seasons are 1821–1825 (the text said 1818–1832). Hopf's paper is 1927. The pseudosphere's volume is $\pi/3$, half the unit hemisphere (the text said half the ball, attributed to Huygens without a source). Circle problem: Volume 6, Chapter 2. Opening question; closing section. Check: `check_ch04_curvature.py`.
- **5.** The winding number is Volume 7's, not Volume 8's; $F_2$ in Volume 8, Chapter 13 is the Banach–Tarski free group. Opening question; closing section. Check: `check_ch05_coverings.py`.
- **6.** Blueprint item: one paragraph after Borsuk–Ulam states the homology of real projective space mod 2, read off the transfer sequence actually printed. The remark on Radó and the classification of surfaces now says both are quoted (blueprint "Stated without proof"). Hopf 1927. Opening question; closing section (end of Part II). Check: `check_ch06_homology.py` (the 3×3 torus triangulation, its Betti numbers, the Klein bottle).
- **7.** Opening question; closing section. Citations of Volume 8 (Proposition C.13, Theorems 3.2, 4.3) and Volume 3 (Lemma 12.3) checked. Check: `check_ch07_liegroups.py`.
- **8.** Blueprint item: the modular function is now $\delta$ and the Vandermonde product $V$ (both were $\Delta$); the uniform variable in the solution of `ex:su2weyl` is now $R$. The Vandermonde determinant is Volume 1, Proposition 7.4 (the text said Volume 3; `statements.py` prints Volume 1 one chapter too high because Volume 1 starts at Chapter 0). Andréief's lemma is dated 1886, the year the Bordeaux volume appeared (Forrester 2019 added to the sources); Mehta–Gaudin 1960 added to the sources. Closing section. Check: `check_ch08_haar.py` (Haar sampling, Weyl's formula, trace moments, gap probability, Dyson's limit).
- **9.** Blueprint items: the tiling by $F$ now rests on Volume 6, Theorem 12.2(b) (it cited Volume 13, Theorem 17.1); the pointer to Volume 13, Chapter 5 is gone; Hopf's ergodicity theorem is stated as quoted, with what it says. The reminder and the area computations cited Appendix I by stale hand-typed numbers ("Proposition J.4", "Lemma 10.5", "Theorem J.8 of Volume 9"): now `\ref`s to Appendix I. Gauss's 1812 letter to Laplace added to the sources. Opening question; closing section. Check: `check_ch09_hyperbolic.py` (including cutting sequences computed by walking the Farey triangles).
- **10.** Every citation now has its number: Volume 5, Corollary 9.12, Theorems 9.15, 9.18, 9.19, 9.38; Volume 7, Theorems 4.15 and 6.10; Volume 8, Corollary 14.3 and Proposition 14.4 (Chapter 14 after Volume 8's reorder). Sources for Weierstrass 1870 and Koebe 1912 added. Opening question; closing section. Check: `check_ch10_riemannmap.py` (Cayley, strip, slit plane, the square map).
- **8 (later).** The remark after Dyson's formula now says that the sine-kernel limit for the Hermitian ensembles is not proved here and is a preview of Volume 12 (blueprint table "Stated without proof").

## Tools

`review/volume9-rewrite/statements.py <volume dir>` prints every numbered statement in printed order. `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py` lists hand-typed numbers inside the volume. `list_citations.py` lists every citation of another volume.

## How to build

`./build.sh --pdf-only volume9-shapes`, or `xelatex` in `volume9-shapes/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
