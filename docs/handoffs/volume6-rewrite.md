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
| 6 | Zeros of the zeta function | `ch06-zeros.tex` | **Done** |
| 7 | The explicit formula | `ch07-explicit.tex` | **Done** |
| 8 | Sieves | `ch08-sieves.tex` | **Done** |
| 9 | Erdős–Kac | `ch09-erdoskac.tex` | **Done** |
| 10 | Random models of the primes | `ch10-random.tex` | **Done** |
| 11 | Exponential and character sums | `ch11-sums.tex` | **Done** |
| 12 | Modular forms, closing problems | `ch12-modular.tex` | In progress |
| — | Preface, blurb, final checks | `preface.tex`, `blurb.tex` | Not started |

## Done so far

**Citations (all chapters).** Volume 6 cited Volume 5 in its old chapter order. Every "Volume 5, Theorem c.n" was shifted to the new order (old 6–13 are 4–11, zeta is 10, asymptotics 11, Hardy–Ramanujan 12, AGM 13) and each was checked against Volume 5's printed statement list. Citations of Volume 2 used an obsolete order (arithmetic functions 6, primitive roots 4, reciprocity 5) and now follow the printed one (4, 5, 6). Volume 1's inequalities are Chapter 10. Inside the volume, 150 hand-typed statement numbers and 80 "Chapter N" became `\ref`. Tools: `review/volume6-rewrite/statements.py` (prints every numbered statement of a volume in printed order), `internal_numbers.py`, `list_citations.py`. `baseline-numbering.txt` holds the numbering before the rewrite.

**Chapter 1.** Worked example at N = 10 before Theorem 1.3. The first proof of `lem:mplush` now rests on Volume 5, Proposition 10.6 (the expansion of zeta at 1). Closing section. Sources for the Euler epigraph and for the Poisson–Dirichlet remark. Check: `check_ch01_mertens.py`.

**Chapter 2.** The constant term of P₃ is stated in closed form and quoted from Titchmarsh. `pb:fracmean` (c) computes its two integrals on the page and no longer cites `pb:fracint` of Chapter 12. Solutions no longer say "one finds numerically": each value is stated and checked. Closing section. Sources for the epigraph, the divisor-problem history and the closing problems. Check: `check_ch02_averages.py`.

**Chapter 3.** The journey `pb:primroot` (Exercise 3.8) used Pólya–Vinogradov, which is Chapter 11. It keeps its number and now stops at the character formula for primitive roots (with a count and a worked case modulo 7). The bound for the least primitive root is the new last exercise of Chapter 11, `pb:leastprimroot`. The class-number remark is labelled as quoted, with the right address (Volume 13, Chapters 2 and 11). Closing section. Check: `check_ch03_characters.py`.

**Chapter 4.** The caption of the figure for q = 3 gave the values at x = 10⁶ as limits. The limits are −1.188 and −0.511, the gap is 0.677; the caption now gives both. Closing section. Check: `check_ch04_dirichlet.py`.

**Chapter 5.** `pb:sidon` (d) used Singer sets from Chapter 12. It now uses Ruzsa's sets modulo p(p−1), proved in the solution. `pb:nsq1sqfree` is self-contained (it cited a Chapter 12 problem and a wrong address for Hensel's lemma). Closing section. Duplicate source removed, sources for the closing problems added. Check: `check_ch05_pnt.py` (about a minute: it sieves to 10⁸).

**Chapter 6.** ξ is taken from Volume 5, Theorem 10.8. New proof of the bound Γ(x) ≤ 1/x on [¼, 1]. The Riemann–Siegel phase is α (as in Volume 5), never ϑ, which is Jacobi's theta. The records for zeros on the line (Levinson, Conrey, Pratt et al.) are quoted with sources. Z(1) = 1 and Z′(1) = γ via Volume 5, Proposition 10.6. A gap value printed 0.524 (a truncation) is now 0.525. Check: `check_ch06_zeros.py`.

**Chapter 7.** Reflection formula from Volume 5, Theorem 9.36(c), ζ(0) from Corollary 10.9(b). Von Koch's proof uses ½ + 2ε. Riemann's formula and the L-function waves are quoted (the functional equation of L is proved in Volume 13, Chapter 12). Edwards's chapters corrected. Check: `check_ch07_explicit.py` (several minutes, run in the background).

**Chapter 8.** Epigraph from Nicomachus (D'Ooge's translation). Volume 2 citations corrected (Chapter 4; squares modulo p are Volume 2, Chapter 6). Siegel zeros and Bombieri–Vinogradov quoted. Buchstab caption: crossings of e^{−γ} at 1.78, 2.48, 3.23, 4.00. Check: `check_ch08_sieves.py`.

**Chapter 9.** Gaussian moments proved inline. Smoothing step corrected to the set {εG > η}. Sathe–Selberg and Berry–Esseen quoted (Berry–Esseen is proved in Volume 11, Chapter 4). Multiplication-table bound written (1+ε)(L + log 2). Check: `check_ch09_erdoskac.py`.

**Chapter 10.** The unsourced Erdős epigraph replaced by Zagier's (1977). Kolmogorov's LIL, Montgomery–Soundararajan and Maier are quoted; Maier's theorem points to Volume 15, Chapter 2, and the remark now uses Buchstab's ω from Problem `pb:buchstab` of Chapter 8 instead of saying it is not defined. RH gap bound stated as O(√p log³p) to match Exercise `ex:shortprime`, with Cramér's √p log p as a quote. Self-citations "Volume 6, Chapter 10" replaced. Check: `check_ch10_random.py` (all printed data recomputed, including the Poisson figure by a segmented sieve near 10⁹).

**Chapter 11.** Vinogradov's non-residue theorem lost its year in the heading (the paper is 1927). The higher-degree remark and the remark on n(p) are quoted. In `pb:erdosnp` the mean is over the odd primes (the printed values are that mean), and two Chebyshev steps in the solution were wrong as written (y ≤ log M, θ(y) ≤ 1.01y) and are now correct. Self-citation replaced. Check: `check_ch11_sums.py` (n(p) for every prime below 10⁸, g(p) below 10⁶).

## Rules kept from Volume 5

- **Numbering inside a chapter is preserved.** Other volumes cite Volume 6 by hand-typed numbers. New exercises go at the END of the exercise list, their hints and solutions at the end of those sections.
- Citations of Volumes 1–4 are by chapter and topic, or by a statement number checked against the printed list.

## For the threads of other volumes

- **Volume 5.** Volume 6 uses Γ′(1) = −γ from Volume 5, Exercise 5.7, which is only an exercise there.
- **Any volume citing Volume 6, Exercise 3.8** for the least primitive root: the bound is now the last exercise of Chapter 11 (`pb:leastprimroot`). No such citation was found in the repository on 2026-11-11.

## Not re-fetched

Bibliographic details added in this pass (journal, volume, pages) were written from memory in a container without the papers at hand: Chapter 2 (Weber 1893, Walfisz 1963, Voronoï 1903, Hardy 1916, Cramér 1922, Sierpiński 1906, Schoenberg 1928, Erdős 1939, Franel and Landau 1924, Kalmár 1931, Hille 1936, Chor–Lemke–Mador 2000), Chapter 5 (Erdős–Turán 1941, Ruzsa 1993, Lindström 1969, Balogh–Füredi–Roy 2023, Estermann 1931, Granville 1998, Brandt–Damgård 1993). Chapters 10 and 11 added more in the same way (Zagier 1977, Westzynthius 1931, Baker–Harman–Pintz 2001, Selberg 1943, Hawkins 1958, Wunderlich 1974, Neudecker–Williams 1974, Heyde 1976, Lemke Oliver–Soundararajan 2016, Kolmogorov 1929, Littlewood 1914, Cramér 1920; Poincaré 1908, Bohl 1909, Sierpiński 1910, Weyl 1910, Pólya 1918, Vinogradov 1918, 1927, 1937, Ankeny 1952, Graham–Ringrose 1990, Miller 1976, Wooley 2016, Erdős 1961, Martin–Pollack 2013, Shoup 1992). An independent reviewer should check them against the papers.
