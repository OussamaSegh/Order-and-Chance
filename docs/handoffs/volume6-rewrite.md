# Handoff: Volume 6 rewrite

Volume 6, *Crossroads*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-06.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** The work is on branch `claude/project-thread-5mayg8`, one pull request for the whole volume, as Volume 5 landed on its own pull request. The master plan and the blueprints stay on PR #157 (branch `claude/project-thread-khh5pi`), which remains open and is not merged. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-06.md`.

## What "rewrite" means here

The blueprint freezes the structure and the numbering of Volume 6: twelve chapters, three parts, no new topic. So each chapter gets one pass, with the same list as Volume 5 (`docs/handoffs/volume5-rewrite.md`):

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, shows an example before the general statement, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number that is not proved on the page is recomputed by a script in `review/volume6-rewrite/`, one script per chapter (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's one "Sources" section.
5. **References.** Hand-typed numbers inside the volume became `\ref`. Chapters have labels: `ch:mertens`, `ch:averages`, `ch:characters`, `ch:dirichlet`, `ch:pnt`, `ch:zeros`, `ch:explicit`, `ch:sieves`, `ch:erdoskac`, `ch:random`, `ch:sums`, `ch:modular`.
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No solution uses a later chapter. A forward part moves to the end of the later chapter's exercise list.
8. **Build.** The volume builds with no undefined reference.

Gate B (independent verification) is not this pass.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| — | Citations of Volumes 1–5, labels, internal `\ref` | all chapters | **Done** |
| 1 | Mertens's Theorems | `ch01-mertens.tex` | **Done** |
| 2 | Arithmetic Functions on Average | `ch02-averages.tex` | **Done** |
| 3 | Dirichlet Characters and L-Functions | `ch03-characters.tex` | **Done** |
| 4 | Dirichlet's Theorem | `ch04-dirichlet.tex` | **Done** |
| 5 | The Prime Number Theorem | `ch05-pnt.tex` | **Done** |
| 6 | Zeros of the zeta function | `ch06-zeros.tex` | Not started |
| 7 | The explicit formula | `ch07-explicit.tex` | Not started |
| 8 | Sieves | `ch08-sieves.tex` | Not started |
| 9 | Erdős–Kac | `ch09-erdoskac.tex` | Not started |
| 10 | Random models of the primes | `ch10-random.tex` | Not started |
| 11 | Exponential and character sums | `ch11-sums.tex` | New exercise received from Chapter 3; pass not started |
| 12 | Modular forms, closing problems | `ch12-modular.tex` | Not started |
| — | Preface, blurb, final checks | `preface.tex`, `blurb.tex` | Not started |

## Done so far

**Citations (all chapters).** Volume 6 cited Volume 5 in its old chapter order. Every "Volume 5, Theorem c.n" was shifted to the new order (old 6–13 are 4–11, zeta is 10, asymptotics 11, Hardy–Ramanujan 12, AGM 13) and each was checked against Volume 5's printed statement list. Citations of Volume 2 used an obsolete order (arithmetic functions 6, primitive roots 4, reciprocity 5) and now follow the printed one (4, 5, 6). Volume 1's inequalities are Chapter 10. Inside the volume, 150 hand-typed statement numbers and 80 "Chapter N" became `\ref`. Tools: `review/volume6-rewrite/statements.py` (prints every numbered statement of a volume in printed order), `internal_numbers.py`, `list_citations.py`. `baseline-numbering.txt` holds the numbering before the rewrite.

**Chapter 1.** Worked example at N = 10 before Theorem 1.3. The first proof of `lem:mplush` now rests on Volume 5, Proposition 10.6 (the expansion of zeta at 1). Closing section. Sources for the Euler epigraph and for the Poisson–Dirichlet remark. Check: `check_ch01_mertens.py`.

**Chapter 2.** The constant term of P₃ is stated in closed form and quoted from Titchmarsh. `pb:fracmean` (c) computes its two integrals on the page and no longer cites `pb:fracint` of Chapter 12. Solutions no longer say "one finds numerically": each value is stated and checked. Closing section. Sources for the epigraph, the divisor-problem history and the closing problems. Check: `check_ch02_averages.py`.

**Chapter 3.** The journey `pb:primroot` (Exercise 3.8) used Pólya–Vinogradov, which is Chapter 11. It keeps its number and now stops at the character formula for primitive roots (with a count and a worked case modulo 7). The bound for the least primitive root is the new last exercise of Chapter 11, `pb:leastprimroot`. The class-number remark is labelled as quoted, with the right address (Volume 13, Chapters 2 and 11). Closing section. Check: `check_ch03_characters.py`.

**Chapter 4.** The caption of the figure for q = 3 gave the values at x = 10⁶ as limits. The limits are −1.188 and −0.511, the gap is 0.677; the caption now gives both. Closing section. Check: `check_ch04_dirichlet.py`.

**Chapter 5.** `pb:sidon` (d) used Singer sets from Chapter 12. It now uses Ruzsa's sets modulo p(p−1), proved in the solution. `pb:nsq1sqfree` is self-contained (it cited a Chapter 12 problem and a wrong address for Hensel's lemma). Closing section. Duplicate source removed, sources for the closing problems added. Check: `check_ch05_pnt.py` (about a minute: it sieves to 10⁸).

## Rules kept from Volume 5

- **Numbering inside a chapter is preserved.** Other volumes cite Volume 6 by hand-typed numbers. New exercises go at the END of the exercise list, their hints and solutions at the end of those sections.
- Citations of Volumes 1–4 are by chapter and topic, or by a statement number checked against the printed list.

## For the threads of other volumes

- **Volume 5.** Volume 6 uses Γ′(1) = −γ from Volume 5, Exercise 5.7, which is only an exercise there.
- **Any volume citing Volume 6, Exercise 3.8** for the least primitive root: the bound is now the last exercise of Chapter 11 (`pb:leastprimroot`). No such citation was found in the repository on 2026-11-11.

## Not re-fetched

Bibliographic details added in this pass (journal, volume, pages) were written from memory in a container without the papers at hand: Chapter 2 (Weber 1893, Walfisz 1963, Voronoï 1903, Hardy 1916, Cramér 1922, Sierpiński 1906, Schoenberg 1928, Erdős 1939, Franel and Landau 1924, Kalmár 1931, Hille 1936, Chor–Lemke–Mador 2000), Chapter 5 (Erdős–Turán 1941, Ruzsa 1993, Lindström 1969, Balogh–Füredi–Roy 2023, Estermann 1931, Granville 1998, Brandt–Damgård 1993). An independent reviewer should check them against the papers.
