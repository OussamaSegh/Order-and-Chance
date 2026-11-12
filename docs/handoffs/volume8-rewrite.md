# Handoff: Volume 8 rewrite

Volume 8, *Analysis: Operators, Spectra and Transforms*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-08.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-hngezv`, one pull request for the whole volume, as Volumes 5, 6 and 7 each landed on their own pull request. The master plan and the blueprints stay on PR #157 (branch `claude/project-thread-khh5pi`), which remains open and is not merged. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-08.md`. The copy of `docs/plan/book-08.md` on `main` is the older ten-chapter specification; where the two differ, the blueprint on PR #157 wins.

## What "rewrite" means here

The blueprint keeps every chapter that stays ("Preserve. Every chapter that stays, as written") and asks for structure: decisions D-16 (the two random-matrix chapters go to Volume 12), D-17 (Haar measure on $\mathbb Q_p$ stays, built on Volume 7), D-18 (a main path of sixteen chapters and six appendices), D-19 (length accepted). So the work is the restructure, then one pass per chapter with the list used for Volumes 5, 6 and 7:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. Opens with a question, ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number that is not proved on the page is recomputed by a script in `review/volume8-rewrite/`, one per chapter (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources" section.
5. **References.** Hand-typed numbers inside the volume become `\ref`. Every chapter has a label (table below). The hand-typed numbers were written against three different orders (the ten-chapter book, the twenty-four-chapter book, and Volume 3's old appendices), so each one was resolved by reading, not by a table.
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses a later chapter or a later volume as a premise. The appendices are premises (D-18).
8. **Build.** The volume builds with no undefined reference.

Gate B of the master plan (independent verification) is not this pass.

## Structure (done)

`main.tex` equals the blueprint's table. Chapter numbers changed for every chapter after Chapter 2:

| Now | Title | File | Label | Before |
| --- | --- | --- | --- | --- |
| 1 | Banach Spaces | `ch01-banach.tex` | `ch:banach` | 1 |
| 2 | Hilbert Spaces | `ch02-hilbert.tex` | `ch:hilbert` | 2 |
| 3 | The Spectral Theorem and Its Relatives | `linear-ch05-spectral.tex` | `linear:ch:spectral` | 7 |
| 4 | Singular Values | `linear-ch06-svd.tex` | `linear:ch:svd` | 8 |
| 5 | Graphs through Their Eigenvalues | `linear-ch08-graphs.tex` | `linear:ch:graphs` | 9 |
| 6 | Cuts, Mixing and Expansion | `spectral-expansion.tex` | `ch:cheeger` | 10 |
| 7 | Expanders and Ramanujan Graphs | `ch09-expanders.tex` | `ch:expanders` | 11 |
| 8 | Operators, Spectra and Banach Algebras | `ch03-operators.tex` | `ch:operators` | 16 |
| 9 | The Spectral Theorem for Compact Operators | `ch04-spectral.tex` | `ch:spectral` | 17 |
| 10 | The Fourier Transform | `ch05-fourier.tex` | `ch:fourier` | 18 |
| 11 | Distributions and Sobolev Spaces | `ch06-distributions.tex` | `ch:distributions` | 19 |
| 12 | Fourier Analysis on Finite Abelian Groups | `ch07-finite.tex` | `ch:finite` | 20 |
| 13 | Haar Measure, Duality and the $p$-adic Numbers | `ch08-haar.tex` | `ch:haar` | 21 |
| 14 | Cauchy's Theorem, Growth and Mellin Inversion | `ch09-complex.tex` | `ch:complex` | 22 |
| 15 | Tauberian Theorems | `ch10-tauberian.tex` | `ch:tauberian` | 23 |
| 16 | The Values of Zeta (problems) | `ch11-harder.tex` | `ch:harder` | 24 |
| A | Spaces, Quotients and Duality | `linear-ch01-duality.tex` | `linear:ch:duality` | 3 |
| B | Determinants as Volume | `linear-ch02-volume.tex` | `linear:ch:volume` | 4 |
| C | Eigenvalues and Invariant Subspaces | `linear-ch03-eigen.tex` | `linear:ch:eigen` | 5 |
| D | Inner Products and Projections | `linear-ch04-inner.tex` | `linear:ch:inner` | 6 |
| E | Inequalities between Matrices | `linear-ch11-inequalities.tex` | `linear:ch:inequalities` | 14 |
| F | Linear Dynamics | `linear-ch12-dynamics.tex` | `linear:ch:dynamics` | 15 |

Numbering inside each chapter is preserved (new statements and exercises go at the end of a list), so a citation "Volume 8, Theorem 17.6" becomes "Volume 8, Theorem 9.6": only the chapter number moves. `review/volume8-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

**Moved to Volume 12 (D-16).** "Random Matrices I: The Semicircle" and "Random Matrices II: Unitary Matrices and the Zeros of Zeta" are now `volume12-random-motion/chapters/ch09-semicircle.tex` and `ch10-cue.tex`, with the figure `moments-ch05-semicircle.tex`. They ARE wired into Volume 12's `main.tex`, after the networks chapter, so they stay in print: Volume 12, Chapters 10 and 11. The third part of Volume 12 is "Networks and Random Matrices" in `main.tex` and in `common/series-catalog.json`. **Owed by the Volume 12 rewrite:** the blueprint's final order (networks 8, semicircle 9, unitary 10, log-correlated 11). It was not applied here because moving the log-correlated chapter renumbers Volume 12's Chapters 8 and 9, which Volume 15 cites by number; that is Volume 12's own pass.

## Chapter progress

| Ch. | Title | State |
| --- | --- | --- |
| — | Structure (D-16, D-18) | Done |
| 1 | Banach Spaces | Done |
| 2 | Hilbert Spaces | Done |
| 3 | The Spectral Theorem and Its Relatives | Done |
| 4 | Singular Values | Done |
| 5 | Graphs through Their Eigenvalues | Done |
| 6 | Cuts, Mixing and Expansion | Done |
| 7 | Expanders and Ramanujan Graphs | Done |
| 8 | Operators, Spectra and Banach Algebras | Done |
| 9 | The Spectral Theorem for Compact Operators | Done |
| 10 | The Fourier Transform | Not started |
| 11 | Distributions and Sobolev Spaces | Not started |
| 12 | Fourier Analysis on Finite Abelian Groups | Not started |
| 13 | Haar Measure, Duality and the $p$-adic Numbers | Not started |
| 14 | Cauchy's Theorem, Growth and Mellin Inversion | Not started |
| 15 | Tauberian Theorems | Not started |
| 16 | The Values of Zeta (problems) | Not started |
| A–F | Appendices | Not started |
| — | Preface, blurb, `kdp.md`, citations of Volume 8 in other volumes | Not started |

## What changed, chapter by chapter

- **1.** The complex case of the $L^p$ dual is written out in four steps (blueprint item, risk 4). The old paragraph tested the norm with $|g|^{q-1}\operatorname{sgn}g$ without the conjugate and did not treat $p=1$. Lebesgue constants are printed (1.436, 2.223, 3.139, 4.070) in place of "a direct computation gives them". Closing section. Citations of Volumes 5 and 7 checked: Volume 5's Fourier series are its Chapter 6. Sources added for Kolmogorov 1926, Riesz 1910, Steinhaus 1919, Wright 1973, Garnir 1974.
- **2.** The Radon–Nikodym section is headed "A second proof" and says so (blueprint). Closing section. Citations of Volume 5 moved to its new chapters (6, 5, 9); the Gaussian kernel cites Volume 5, Theorem 8.3.
- **3.** A reminder of what the chapter assumes (Appendices C and D). Closing section.
- **4.** The photograph keeps 24 singular triples (24 cost 48,024 numbers, a 25th would exceed 50,000); caption fractions checked against the figure. Closing section.
- **5.** Volume 3 Perron theory cited precisely (Appendix A: Theorems A.1, A.6, Exercise A.2). History corrected: Aschbacher 1971 excluded rank three, not vertex-transitivity (Higman; Mačaj–Širáň 2010 added); Graham–Pollak has had a counting proof since Vishwanathan 2013; the unsupported "no proof of the friendship theorem without counting" removed. Closing section.
- **6.** The Laplacian is now defined before it is used; Fiedler named; the hypercube's h = 1 follows from the theorem itself. LPS needs d − 1 ≡ 1 mod 4. A Sources section added (there was none). Opening question, closing section.
- **7.** R1: the reminder no longer imports Kesten's theorem from Volume 12 (the chapter proves its own Kesten 1959 statement, and the text compares it with Volume 12's `thm:kesten`, blueprint item 7); the Catalan moments of the semicircle are now proved in the solution instead of cited from the moved chapter. LPS girth corrected (about (4/3) log_p N in the bipartite case). Hoeffding cited as Volume 4, Theorem 4.2. Closing section. **Note for Volume 12:** the text says Volume 12, Chapter 9 (networks, `thm:kesten`) and Chapter 10 (semicircle), the current printed order; if the Volume 12 rewrite applies the blueprint order (networks 8, semicircle 9), these two numbers in `ch09-expanders.tex` must move with it.
- **8.** All hand-typed internal numbers became `\ref`. Liouville and Laurent cited as Volume 5, Theorems 9.16 and 9.22; Fubini for series as Volume 7, Theorem 9.6. Wiener–Lévy marked as not developed. Opening question, closing section.
- **9.** All hand-typed internal numbers became `\ref` (they were in the ten-chapter order: 3.x = Chapter 8, 1.x, 2.x). The full spectral theorem stays a remark, and the closing section says it was not proved (blueprint). Opening question, closing section.

## Tools

`review/volume8-rewrite/statements.py volume8-analysis` prints every numbered statement in printed order. `resolve_citations.py <chapter file>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py` lists hand-typed numbers inside the volume against the old order. `list_citations.py` lists every citation of another volume.

## How to build

`./build.sh --pdf-only volume8-analysis`, or `xelatex` in `volume8-analysis/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
