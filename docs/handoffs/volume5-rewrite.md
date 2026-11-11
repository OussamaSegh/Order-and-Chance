# Handoff: Volume 5 rewrite

Volume 5, *Calculation: From Formula to Insight*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-05.md`. This file is updated with every chapter. Read it first.

**Branch and pull request.** The author chose to keep the whole rewrite in PR #157, on branch `claude/project-thread-khh5pi`, together with the master plan. Do not merge without the author's word.

## What "rewrite" means here

The blueprint keeps the mathematics of Chapters 1–11 and 13 and asks for new mathematics in Chapter 12 only. So each chapter gets one pass with a fixed list:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. A friend who loves mathematics, explaining the step. Opens with a question, shows an example before the general statement, names the stages of long proofs, ends with "what we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner. Skipped steps written out. Hypotheses matched against the statements cited.
3. **Numbers.** Every printed number that is not proved on the page is recomputed by a script in `review/volume5-rewrite/`, one script per chapter.
4. **History.** Every date, quotation and attribution has a source in the chapter's one "Sources" section.
5. **References.** Hand-typed numbers inside the volume ("Chapter~7", "Theorem~12.3") become `\ref` to labels. Chapters have labels `ch:…` (table in `docs/plan/volume-citation-map.md`).
6. **Plan items** for that chapter (list below).
7. **Exercises.** Three levels, at least one proof and one computation, each with hint and solution (`\idea`, then `\writeup`).
8. **Build.** The volume builds, `tools/check_book_layout.py` and `tools/check_edition_copy.py` pass.

Gate B of the master plan (independent verification) is not this pass. The writer cannot verify their own chapter. Statuses in a future theorem ledger stay NOT REVIEWED until an independent reviewer files records.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| — | Structure (D-10, D-11) | `main.tex` | **Done** |
| 1 | Finite Calculus | `ch01-finite.tex` | Not started |
| 2 | Generating Functions as a Computing Tool | `ch02-generating.tex` | Not started |
| 3 | Classic Series and Infinite Products | `ch03-series.tex` | Not started |
| 4 | Integration Techniques | `ch04-integrals.tex`, `bbp-borwein.tex` | Not started |
| 5 | The Gamma and Beta Functions | `ch05-gamma.tex` | Not started |
| 6 | Fourier Series | `ch06-fourier.tex` | Not started |
| 7 | The Discrete Fourier Transform and the FFT | `ch07-fft.tex` | Not started |
| 8 | The Fourier Transform and Poisson Summation | `ch08-transform.tex` | Not started |
| 9 | Complex Analysis for Computing | `ch09-complex.tex` | Not started |
| 10 | The Zeta Function | `ch10-zeta.tex` | Not started |
| 11 | Asymptotics | `ch11-asymptotics.tex` | Not started |
| 12 | The Hardy–Ramanujan Formula | `hardy-ramanujan.tex` | **Done** (rewritten, new proof of the η transformation) |
| 13 | The Arithmetic–Geometric Mean | `ch12-agm.tex` | Not started |
| — | Preface, blurb, final checks | `preface.tex`, `blurb.tex` | Preface chapter list updated; final pass not started |

## Done so far

**Structure.** `main.tex` equals the blueprint's table: three parts, thirteen chapters. `waring.tex` and its figure moved to `volume14-primes/` (figure renamed `waring-fivesquares.tex`). Volume 14's `main.tex` does not input it yet, so **Waring's problem is in no printed volume until Volume 14 is rewritten**. The thread that owns Volume 14 wires it in as Chapter 6. Figures `ch06-ratio`, `ch06-circle` renamed `hr-ratio`, `hr-circle`. `docs/SERIES-STRUCTURE.md` and the citation map carry the new numbering.

**Chapter 12.** New: Lemma `lem:pdisc` (the partition product as a holomorphic function on the disc, which the old chapter assumed), Theorem `thm:eta` (η(−1/τ)=√(−iτ)·η(τ), proved from `thm:pentagonal`, `thm:poisson`, `thm:gaussianft`, `prop:ftbasic`, `thm:identity`), a table of p(n) against the formula, a closing section, one computation exercise (`ex:etacheck`). The citation of Volume 6 as a premise is gone. The reference to a "Problem Book" is gone. The remaining mentions of later volumes are previews (Volume 14 for the circle method and Kloosterman sums, Volume 6 for modular forms). Checks: `python3 review/volume5-rewrite/check_ch12_hardy_ramanujan.py` (η transformation at three points to 30 digits, every constant of the proof, the Rademacher partial sums, the table, the congruences, the exercises). The four mathematical risks of the blueprint: (1) branch of the square root, convergence and the passage to the half-plane are written out in the proof of `thm:eta`; (2) the chapter uses nothing from the Waring chapter; (3) the minor arc is y ≤ |x| ≤ 1/2, the whole rest of the circle; (4) is a Chapter 8 item.

## Plan items still open, by chapter

- **Ch. 4, 7, 9.** One new exercise of the hardest level each.
- **Ch. 8.** Jacobi's theta becomes ϑ, with a sentence fixing the letter at first use. State the class of functions of the inversion theorem (`thm:ftinversion`) and check it is the class Chapter 12 and Volume 6 use (risk 4). "Chapter~12 follows him" is a stale number.
- **Ch. 9.** One sentence saying which complex analysis this chapter owns and which Volume 8, Chapter 14 owns. The line about the homology form of Cauchy's theorem says "proved in Volume 8": check against Volume 7, Chapter 6 (Jordan) and Volume 8.
- **Ch. 10.** Completed zeta is ξ, not Λ (master plan 4.5). A sentence fixing the letter. The unproved claim about smooth cutoffs of Σn: prove it or remove it. Numerical zeros of ζ: stated as computations with a source.
- **Ch. 13.** Legendre's modulus function must not use Λ. The closing problems each state the chapters they use; their hand-typed numbers ("Theorem~12.3", "Exercise~7.7", "Volume~5") are in the old numbering. Problems citing Volume 13, Exercise 8.5 or Volume 6 as tools break rule R1 (a solution is a proof): rework or move.
- **Ch. 3, 5.** Tonelli is "Admitted here, proved in Volume 7, Theorem 9.5" at each use; Chapter 5 line on Fubini–Tonelli and change of variables needs the same wording or a proof on rectangles.
- **All.** About 460 hand-typed internal references to convert to `\ref`.
- **Other volumes.** Citations of Volume 5 by chapter number in Volumes 6–15 are now off (table in the citation map). This thread does not edit other volumes.
- **Ledgers.** `docs/plan/ledgers/` does not exist yet (Phase 0 of the master plan). The per-chapter check scripts are the trace for numerical claims until it does.

## How to build

`xelatex` three passes in `volume5-calculation/` as `build.sh` does, or `./build.sh --pdf-only volume5-calculation`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`.
