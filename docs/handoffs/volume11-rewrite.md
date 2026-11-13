# Handoff: Volume 11 rewrite

Volume 11, *Randomness*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-11.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-pro7lo`, one pull request for the whole volume, as Volumes 5–10 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-11.md`. Where it differs from the copy on `main` (an older specification that puts the problem chapter in Part I), the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps every chapter ("Preserve. All fourteen chapters") and makes one structural change (D-26): **Shuffling Cards becomes Chapter 13 and the problem chapter "Sums of Random Pieces" becomes Chapter 14**, the last chapter, which also receives the two problems moved from Volume 7 (D-15: Minkowski's question mark, the Cantor orbit under multiplication by 3). The work on each chapter is the list used for Volumes 5–10:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume11-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources" section.
5. **References.** Citations of other volumes checked against their printed order today (Volume 1 with the fixed `statements.py`; Volume 5 after its renumbering; Volume 7 Chapters 2, 6, 13; Volume 8 as sixteen chapters plus Appendices A–F).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses Volumes 12–15 as a premise. The one admitted forward statement is the Selberg–Delange formula (Chapter 11), labelled.
8. **Build.** The volume builds with no undefined reference.

Numbering inside Chapters 1–12 is preserved: new statements go at the end of a list, because Volumes 12–15 cite Volume 11 by hand-typed numbers. `review/volume11-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

## Numbering changes (for Volumes 12–15)

- Old Chapter 14 (Shuffling Cards) is now **Chapter 13**: every `14.x` statement or exercise of the shuffling chapter is now `13.x` (Theorem 13.8 = `thm:ds`, Corollary 13.9 = `cor:cutoff`, Theorem 13.10 = `thm:bd`, Corollary 13.14 = `cor:riffle`, Lemma 13.4 = `lem:upperbound`). Its exercises are now called "Exercise" (they were printed as "Problem" because the problem chapter's name switch came first).
- Old Chapter 13 (problems) is now **Chapter 14**: `pb:*` problems `13.x` are now `14.x`, followed by the two problems from Volume 7.
- No printed citation in Volumes 12–15 used either chapter by number except `volume15-order-and-chance/chapters/ch03-shuffling.tex`, a file not reached from Volume 15's `main.tex`; its numbers were updated anyway.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Independence and Zero–One Laws | `ch01-zero-one.tex` | To do |
| 2 | Laws of Large Numbers | `ch02-lln.tex` | To do |
| 3 | Weak Convergence and Donsker's Theorem | `ch03-donsker.tex` | To do |
| 4 | The Central Limit Theorem, Sharpened | `ch04-clt.tex` | To do |
| 5 | Infinitely Divisible and Stable Laws | `ch05-stable.tex` | To do |
| 6 | Stein's Method | `ch06-stein.tex` | To do |
| 7 | Large Deviations | `ch07-ldp.tex` | To do |
| 8 | Concentration of Measure | `ch08-concentration.tex` | To do |
| 9 | Martingales II: Closing the Circle | `ch09-martingales.tex` | To do |
| 10 | Ergodic Theory | `ch10-ergodic.tex` | To do |
| 11 | Mod-φ Convergence | `ch11-modphi.tex` | To do |
| 12 | Random Permutations and the Poisson–Dirichlet Law | `ch12-permutations.tex` | To do |
| 13 | Shuffling Cards | `shuffling.tex`, `riffle-cutoff.tex` | Moved (was 14); to do |
| 14 | Sums of Random Pieces (problems) | `ch13-harder.tex` | Moved (was 13); to do |
| — | Preface, blurb, `kdp.md`, citations of Volume 11 in other volumes | | To do |

## What changed, chapter by chapter

(Filled in as each chapter is done.)

## Tools

`review/volume11-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py`, `list_citations.py` as for Volume 10.

## How to build

`./build.sh --pdf-only volume11-randomness`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
