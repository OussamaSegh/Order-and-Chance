# Handoff: Volume 12 rewrite

Volume 12, *Random Motion*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-12.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-c9wcni`, one pull request for the whole volume, as Volumes 5–11 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-12.md`. The copy of `book-12.md` on `main` is an older specification that sends the random-matrix chapters to Volume 8; the blueprint on PR #157 (decision D-16: they come back to Volume 12) wins.

## What "rewrite" means here

The blueprint preserves Chapters 1–8 and the appendix, keeps the two random-matrix chapters that the Volume 8 rewrite already moved back (now Chapters 9 and 10), and ends Part III with the log-correlated chapter (Chapter 11). The structure in `main.tex` already matched the blueprint when this pass started. The work on each chapter is the list used for Volumes 5–11:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. The epigraph asks the chapter's question; the chapter ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume12-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources and further reading".
5. **References.** Citations of other volumes checked against their printed order today (`resolve_citations.py`; Volume 1 counted from Chapter 0; Volume 5 after its renumbering; Volume 7 Chapters 2, 6, 13; Volume 8 as sixteen chapters plus Appendices A–F; Volume 11 with shuffling as Chapter 13).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses Volumes 13–15 as a premise. Montgomery's theorem (Volume 14) is stated for comparison only.
8. **Build.** The volume builds with no undefined reference.

Numbering inside every chapter is preserved: new statements go at the end of a list, because Volumes 8, 14 and 15 cite Volume 12 by hand-typed numbers (Keating–Snaith Theorem 10.10, `thm:logclt` 10.11, `prop:cuelogcorr` 11.3, `thm:gmc` 11.4, matrix-tree A.4). `review/volume12-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

Gate B of the master plan (independent verification records) is not this pass.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Gaussian Processes and the Birth of Brownian Motion | `ch01-gaussian.tex` | Done |
| 2 | The Fine Structure of a Brownian Path | `ch02-paths.tex` | Done |
| 3 | Continuous Martingales | `ch03-martingales.tex` | Done |
| 4 | The Itô Integral | `ch04-ito.tex` | Done |
| 5 | Brownian Motion and Analysis | `ch05-analysis.tex` | Done |
| 6 | Stochastic Differential Equations | `ch06-sde.tex` | Done |
| 7 | Markov Processes and Lévy Processes | `ch07-levy.tex` | Done |
| 8 | Random Walks on Networks and Groups | `ch08-networks.tex` | Done |
| 9 | Random Matrices I: The Semicircle | `ch09-semicircle.tex` | To do |
| 10 | Random Matrices II: Unitary Matrices and the Zeros of Zeta | `ch10-cue.tex` | To do |
| 11 | Log-Correlated Fields and the Largest Values | `ch12-logcorrelated.tex` (to be renamed `ch11-`), `brw-halfmoment.tex` | To do |
| A | Spectral Graph Theory | `spectral.tex` | To do |
| — | `moments.tex` (not printed): written check, then removal | | To do |
| — | Preface, blurb, `kdp.md` | | To do |

## Tools

`review/volume12-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py`, `list_citations.py` as for Volumes 10 and 11.

## How to build

`./build.sh --pdf-only volume12-random-motion`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`. Before the pull request, also run `python3 tools/listing.py volume12-random-motion /tmp/x.md` (CI fails on a `kdp.md` keyword over 50 characters).
