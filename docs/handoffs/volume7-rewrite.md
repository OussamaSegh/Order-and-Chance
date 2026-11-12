# Handoff: Volume 7 rewrite

Volume 7, *Spaces: Topology, Measure and Limits*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-07.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** The work is on branch `claude/project-thread-ehtc3u`, one pull request for the whole volume, as Volumes 5 and 6 each landed on their own pull request. The master plan and the blueprints stay on PR #157 (branch `claude/project-thread-khh5pi`), which remains open and is not merged. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-07.md`. The copy of `docs/plan/book-07.md` on `main` is the older specification; where the two differ, the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps the structure of Volume 7 (thirteen chapters, three parts) and its numbering. Chapters 1–12 are "Keep", Chapter 2 gains one corollary, Chapter 13 is split (decision D-15). So each chapter gets one pass, with the same list as Volumes 5 and 6 (`docs/handoffs/volume5-rewrite.md`):

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, shows an example before the general statement, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number that is not proved on the page is recomputed by a script in `review/volume7-rewrite/`, one script per chapter (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's one "Sources" section.
5. **References.** Hand-typed numbers inside the volume become `\ref`. Chapters get labels (table below).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses a later chapter or a later volume as a premise. A forward part moves to the end of the later chapter's exercise list, or to the later volume.
8. **Build.** The volume builds with no undefined reference.

Gate B of the master plan (independent verification) is not this pass.

## Chapter progress

| Ch. | Title | File | Label | State |
| --- | --- | --- | --- | --- |
| 1 | Sets, Choice and the Real Numbers | `ch01-sets.tex` | `ch:sets` | Not started |
| 2 | Metric Spaces and Completeness | `ch02-metric.tex` | `ch:metric` | Not started |
| 3 | Topological Spaces | `ch03-topology.tex` | `ch:topology` | Not started |
| 4 | Compactness | `ch04-compact.tex` | `ch:compact` | Not started |
| 5 | Baire's Theorem | `ch05-baire.tex` | `ch:baire` | Not started |
| 6 | The Jordan Curve Theorem | `jordan.tex`, `jordan-polygon.tex` | `ch:jordan` | Not started |
| 7 | Measures | `ch06-measures.tex` | `ch:measures` | Not started |
| 8 | The Lebesgue Integral | `ch07-integral.tex` | `ch:integral` | Not started |
| 9 | Product Measures and Change of Variables | `ch08-products.tex` | `ch:products` | Not started |
| 10 | $L^p$ Spaces | `ch09-lp.tex` | `ch:lp` | Not started |
| 11 | Differentiation and Radon–Nikodym | `ch10-radon.tex` | `ch:radon` | Not started |
| 12 | Measures on Metric Spaces | `ch11-metricmeasures.tex` | `ch:metricmeasures` | Not started |
| 13 | Almost Every Number (problems) | `ch12-harder.tex` | `ch:harder` | Not started |
| — | Preface (debts table), blurb, final checks | `preface.tex`, `blurb.tex`, `kdp.md` | | Not started |

File names keep their old numbers (the Jordan chapter was inserted as Chapter 6), so the file number is one less than the chapter number from `ch06-measures.tex` on.

## Tools

`review/volume7-rewrite/statements.py volume7-spaces` prints every numbered statement in printed order. `baseline-numbering.txt` is that list before the rewrite. `internal_numbers.py` finds hand-typed statement numbers. `list_citations.py` lists every citation of another volume.

## Rules kept from Volumes 5 and 6

- **Numbering inside a chapter is preserved.** Other volumes cite Volume 7 by hand-typed numbers. New statements and exercises go where they shift nothing that is cited, by default at the END of a list.
- Citations of Volumes 1–4 are by chapter and topic, checked against the printed order listed in `docs/handoffs/volume5-rewrite.md`. Citations of Volume 5 follow its new chapter order (`docs/plan/volume-citation-map.md`).

## How to build

`./build.sh --pdf-only volume7-spaces`, or `xelatex` in `volume7-spaces/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`.
