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
- Chapter 11 gained **Corollary `cor:unifomega`** (uniform integers, from the admitted Selberg–Delange formula), placed after `thm:omegamod` at the end of the list, so no existing number moved.
- New chapter labels `ch:ergodic` (Chapter 10) and `ch:shuffling` (Chapter 13). The table is also in `docs/plan/volume-citation-map.md`, section "Volume 11 after the master plan".
- No printed citation in Volumes 12–15 used either chapter by number except `volume15-order-and-chance/chapters/ch03-shuffling.tex`, a file not reached from Volume 15's `main.tex`; its numbers were updated anyway.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Independence and Zero–One Laws | `ch01-zero-one.tex` | Done |
| 2 | Laws of Large Numbers | `ch02-lln.tex` | Done |
| 3 | Weak Convergence and Donsker's Theorem | `ch03-donsker.tex` | Done |
| 4 | The Central Limit Theorem, Sharpened | `ch04-clt.tex` | Done |
| 5 | Infinitely Divisible and Stable Laws | `ch05-stable.tex` | Done |
| 6 | Stein's Method | `ch06-stein.tex` | Done |
| 7 | Large Deviations | `ch07-ldp.tex` | Done |
| 8 | Concentration of Measure | `ch08-concentration.tex` | Done |
| 9 | Martingales II: Closing the Circle | `ch09-martingales.tex` | Done |
| 10 | Ergodic Theory | `ch10-ergodic.tex` | Done |
| 11 | Mod-φ Convergence | `ch11-modphi.tex` | Done |
| 12 | Random Permutations and the Poisson–Dirichlet Law | `ch12-permutations.tex` | Done |
| 13 | Shuffling Cards | `shuffling.tex`, `riffle-cutoff.tex` | Moved (was 14); done |
| 14 | Sums of Random Pieces (problems) | `ch13-harder.tex` | Moved (was 13); done |
| — | Preface, blurb, `kdp.md`, citations of Volume 11 in other volumes | | Done |

## What changed, chapter by chapter

Every chapter now opens on a question (epigraph and first section) and ends with a closing section "What we proved, and what comes next" that leads into the next chapter. Every chapter has a number check in `review/volume11-rewrite/check_chNN_*.py`; all pass.

- **Ch 1.** Epigraph question; the martingale theorem on refining partitions cited as Volume 4, Theorem 11.12, and the series consequence proved directly; Lévy's equivalence (in distribution) stated as not proved.
- **Ch 2.** Volume 4 maximal inequality cited for finite partitions (Theorem 11.4) and the general-filtration step justified; the infinite-mean converse corrected ($\limsup|S_n|/n=\infty$); St Petersburg figure description matched to the figure.
- **Ch 3.** Donsker's theorem for the empirical process (Doob's heuristic) marked as not proved here, with the reason (the empirical process jumps); the two-sided Kolmogorov law computed exactly by counting lattice paths.
- **Ch 4.** Smoothing inequality cited from Volume 7, Theorem 8.17; Weldon's dice table recomputed (1216, 1255); one estimate corrected from 20 to about 18.
- **Ch 5.** The triangular-array converse and the non-symmetric stable laws named as the two quoted results (with Selberg–Delange, the three exceptions of the preface).
- **Ch 6.** Chen's thesis dated 1971; near-birthday and poll numbers checked.
- **Ch 7.** $\nu^*$ table entry 0.348 corrected to 0.347; Chernoff information checked.
- **Ch 8.** Azuma restricted to finitely valued coordinates (McDiarmid for the general case); Johnson–Lindenstrauss gain "thousandfold" corrected to "more than eight hundredfold".
- **Ch 9.** Ville's inequality given a direct supermartingale-sum proof; the Kakutani example fixed ($\varepsilon_n=\frac12n^{-1/2}$, since $\varepsilon_1=1$ was invalid); Armitage, McPherson and Rowe (1969) sourced for the peeking numbers; stale Volume 5 Section 7.4 corrected to 5.4.
- **Ch 10.** Mean ergodic theorem cited from Volume 8, Theorem 2.10; adjoint via Riesz–Fréchet, conditional expectation as a projection via Volume 7, Theorem 11.16; Szemerédi marked as quoted; Volume 14's Roth chapter named without a chapter number (it will move when Volume 14 wires in Waring).
- **Ch 11.** Selberg–Delange declared admitted (proved in Volume 15, Chapter 3); new Corollary `cor:unifomega`; Delange 1959 sourced.
- **Ch 12.** Duplicated sentence removed; Dickman, Golomb–Dickman and smooth-number proportions checked.
- **Ch 13 (was 14).** Closing section added; the $n=52$ bound, riffle distances and constants checked.
- **Ch 14 (was 13).** Retitled "Sums of Random Pieces"; self-citations "Volume 11" made internal; the upper bound lemma cited as Lemma 13.4; Volume 7 Corollary 11.6; the Erdős golden-ratio problem now needs only the rational root test (Volume 13 named as background, not a premise); "about three real roots" corrected to "about three and a half" ($\mathbb EN_{100}=3.56$); the map's "Volumes used" column renumbered to title-page numbers; new section "Continued fractions and the Gauss map" with the two Volume 7 problems (Problems 14.23 and 14.24, figure, hints, solutions, sources). `from-volume7-problems.tex` deleted. Two citations found by `tools/cross_volume_citations.py` fixed in Problem 14.11's solution (Erdős–Taylor): Prokhorov is Volume 7, Theorem 12.7, and the identity theorem is Volume 5, Theorem 9.18.
- **Front matter.** The preface says a reader may begin after Volume 8, Volume 10 is needed only for Chapter 13, and describes Chapters 13 and 14; blurb and `kdp.md` likewise.
- **Other volumes.** `volume15-order-and-chance/chapters/ch03-shuffling.tex` now cites the shuffling chapter as 13.x.

## Tools

`review/volume11-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py`, `list_citations.py` as for Volume 10.

## How to build

`./build.sh --pdf-only volume11-randomness`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.

## Left for other volumes

- `tools/cross_volume_citations.py` reports one mismatch outside this volume: `volume14-primes/chapters/ch14-critical.tex` cites "Volume 5, Corollary 10.10", which is a theorem. The Volume 14 rewrite fixes it.
- Volume 14's Roth chapter is cited by name only from Chapters 10 and 12, so it can move when Volume 14 wires in Waring.
