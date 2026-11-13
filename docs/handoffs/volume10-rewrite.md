# Handoff: Volume 10 rewrite

Volume 10, *Abstraction*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-10.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-8g87ej`, one pull request for the whole volume, as Volumes 5–9 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-10.md`. Where it differs from the copy on `main` (which still describes an older plan with the shuffle chapter here), the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps the structure ("Structure: unchanged"; "Preserve. All eleven chapters in their order"): eleven chapters in three parts, already matching `main.tex`. The shuffling chapter has already left for Volume 11. No chapter moves and no chapter number changes. The work is one pass per chapter with the list used for Volumes 5–9:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume10-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources" section.
5. **References.** Citations of other volumes checked against their printed order today (Volume 1 with the fixed `statements.py`; Volume 5 after its renumbering; Volume 7 Chapters 2, 6, 13; Volume 8 as sixteen chapters plus Appendices A–F).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses Volumes 11–15 as a premise.
8. **Build.** The volume builds with no undefined reference.

Numbering inside each chapter is preserved: new statements go at the end of a list, because Volumes 11–15 cite Volume 10 by hand-typed numbers. `review/volume10-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Categories | `ch01-categories.tex` | Done |
| 2 | Tensors and the Cost of Multiplying Matrices | `linear-ch10-tensors.tex` | Done |
| 3 | Tensors and Exactness | `ch02-tensors.tex` | Done |
| 4 | Noetherian Rings and Hilbert's Theorems | `ch03-noetherian.tex` | |
| 5 | Localisation and Dimension | `ch04-localisation.tex` | |
| 6 | Dedekind Domains | `ch05-dedekind.tex` | |
| 7 | Homological Algebra | `ch06-homological.tex` | |
| 8 | Group Cohomology | `ch07-groupcoh.tex` | |
| 9 | Semisimple Algebras and Induction | `ch08-semisimple.tex` | |
| 10 | The Symmetric Group | `ch09-symmetric.tex` | |
| 11 | Compact Groups | `ch11-compact.tex` | |
| — | Preface, blurb, `kdp.md`, citations of Volume 10 in other volumes | | |

## What changed, chapter by chapter

- **1.** Closing section. Sources for Mac Lane's summary of the logic of categories and his slogan on adjoints. Check: `check_ch01_categories.py`.
- **2.** Opening question, and a first paragraph that says how the chapter relates to Chapter 3 (blueprint). Strassen's epigraph marks its omission with an ellipsis. Every "proved in Volume 8" now has its number: Theorem C.2 (Schur), Exercise 3.3 (path), Exercise 5.1 (hypercube), Theorem F.5 (Lyapunov), Theorems 4.1 and 4.5 (SVD, Eckart–Young); "Volume 8 returns to [fast Poisson solvers]" was false and is gone. The records remark and the figure caption say the bounds on $\omega$ are quoted, with dates (blueprint). $\sigma_2\approx0.521$ (the text said 0.520). Closing section. Check: `check_ch02_kronecker.py` (Strassen's identity over non-commuting symbols, the rank decompositions, the operation counts, the Schmidt example).
- **3.** Opening question; the first paragraph says how it relates to Chapter 2 (blueprint). The film anecdote now says only what the sources say (Gross was the consultant and coached Clayburgh); the unsourced "just for show" and the removed credit are gone. "Chapter 6" for homological algebra is Chapter 7. The tensor product of vector spaces was attributed to "Volume 3, Chapter 10" (Galois theory, no tensors): now Chapter 2. The beauty box no longer retells Strassen with a hand-typed "Theorem 2.12". Closing section. Check: `check_ch03_exactness.py`.

## Owed to later volumes

(Filled in as chapters are done.)

## Tools

`review/volume10-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py`, `list_citations.py` as for Volume 9.

## How to build

`./build.sh --pdf-only volume10-abstraction`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
