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
| 4 | Noetherian Rings and Hilbert's Theorems | `ch03-noetherian.tex` | Done |
| 5 | Localisation and Dimension | `ch04-localisation.tex` | Done |
| 6 | Dedekind Domains | `ch05-dedekind.tex` | Done |
| 7 | Homological Algebra | `ch06-homological.tex` | Done |
| 8 | Group Cohomology | `ch07-groupcoh.tex` | Done |
| 9 | Semisimple Algebras and Induction | `ch08-semisimple.tex` | Done |
| 10 | The Symmetric Group | `ch09-symmetric.tex` | Done |
| 11 | Compact Groups | `ch11-compact.tex` | Done |
| — | Preface, blurb, `kdp.md`, citations of Volume 10 in other volumes | | Done |

## What changed, chapter by chapter

- **1.** Closing section. Sources for Mac Lane's summary of the logic of categories and his slogan on adjoints. Check: `check_ch01_categories.py`.
- **2.** Opening question, and a first paragraph that says how the chapter relates to Chapter 3 (blueprint). Strassen's epigraph marks its omission with an ellipsis. Every "proved in Volume 8" now has its number: Theorem C.2 (Schur), Exercise 3.3 (path), Exercise 5.1 (hypercube), Theorem F.5 (Lyapunov), Theorems 4.1 and 4.5 (SVD, Eckart–Young); "Volume 8 returns to [fast Poisson solvers]" was false and is gone. The records remark and the figure caption say the bounds on $\omega$ are quoted, with dates (blueprint). $\sigma_2\approx0.521$ (the text said 0.520). Closing section. Check: `check_ch02_kronecker.py` (Strassen's identity over non-commuting symbols, the rank decompositions, the operation counts, the Schmidt example).
- **3.** Opening question; the first paragraph says how it relates to Chapter 2 (blueprint). The film anecdote now says only what the sources say (Gross was the consultant and coached Clayburgh); the unsourced "just for show" and the removed credit are gone. "Chapter 6" for homological algebra is Chapter 7. The tensor product of vector spaces was attributed to "Volume 3, Chapter 10" (Galois theory, no tensors): now Chapter 2. The beauty box no longer retells Strassen with a hand-typed "Theorem 2.12". Closing section. Check: `check_ch03_exactness.py`.
- **4.** Opening question. Gordan's "theology" remark is hedged as the remark the story attributes to him, sourced to Reid's *Hilbert* and McLarty, "Theology and its discontents" (*Circles Disturbed*, 2012); the magazine source is gone. Closing section. Check: `check_ch04_noetherian.py` (Gröbner bases, 3-colouring ideals).
- **5.** Opening question. Proof of `lem:irredprimary` made explicit; Lasker–Noether proof wording fixed; "isolated" replaced by a sentence about embedded primes. Lasker as world chess champion 1894–1921, Lasker 1905 in the sources. The closing section says going down is not proved. Check: `check_ch05_localisation.py`.
- **6.** This chapter is now declared the series' home of unique factorisation of ideals (`thm:dvr`, `thm:dedekind`, `thm:intclosure`, `thm:fundid`), which Volume 13 applies. "$\mathcal O_K$ is Dedekind" is justified by `thm:intclosure` (characteristic 0, so separable). Example: proof that $\Z[\sqrt{-5}]$ is integrally closed (trace and norm, mod 4). Class group of order 2, $efg=n$ and the elliptic group law are marked as previews of Volume 13 (Chapters 4 and 15). Check: `check_ch06_dedekind.py`.
- **7.** Opening question. Hilbert's syzygy theorem labelled as quoted; the Zorn case and the symmetry of Tor marked as not proved; de Rham cites Volume 9, Chapter 3 (stated there); universal coefficients claimed only for algebraic complexes. Closing section points to spectral sequences and derived categories. Check: `check_ch07_homological.py` (Smith normal form homology).
- **8.** Opening question. $H^n=\operatorname{Ext}^n$ marked as stated and not needed, with a notation note (not Volume 9's $H_n$). Comparison of symmetric cocycles with Ext and the non-abelian Schur–Zassenhaus marked as not proved. Speiser 1919 in the sources. Inflation–restriction stays out: Volume 13 never uses it (blueprint condition). Check: `check_ch08_groupcoh.py`.
- **9.** Opening question, closing section (leads into Chapter 10 through the induced modules $M^\lambda$). All Volume 3 citations (11.3, 11.4, 11.8–11.11, 11.13, 11.14, 10.6, 10.9, 5.10, 3.10, Exercise 11.8) checked. Check: `check_ch09_semisimple.py` (class counts and degree sums for $\mathfrak S_3,\mathfrak S_4$, dihedral, Heisenberg, affine groups, $Q_8$; double cosets; integrality in $\mathfrak S_4$).
- **10.** Opening question, closing section (lists what is stated without proof: $S^{\lambda'}\cong S^\lambda\otimes\mathrm{sgn}$, the limit shape, Tracy–Widom). Check: `check_ch10_symmetric.py` (hook formula against brute-force tableaux to $n=9$, Robinson–Schensted bijection and Schensted's theorem to $n=7$, the transposition character against $p_2p_1^{n-2}$ in Schur functions, Catalan, two-row and Frobenius formulas, limit curve).
- **11.** Opening question, closing section (ends the volume). The Vandermonde determinant was cited to "Volume 3": now Volume 1, Proposition 7.4. Schur–Weyl duality was already a remark headed "not proved". Check: `check_ch11_compact.py` (Weyl dimension against hook-content, exercise dimensions, Theorem 11.9 exactly and by Monte Carlo on $U(2)$, $U(3)$, $\mathbb E|\det(I-U)|^2=n+1$, Keating–Snaith 42 and 24024).
- **Front and back matter.** The preface, `blurb.tex` and `kdp.md` still promised the shuffling theorem, which moved to Volume 11: now three representation chapters, the transposition character "which Volume 11 uses", and the trace moments instead. The preface's "next chapter" muddle for Chapters 2–3 fixed.
- **Numbering.** `statements.py` output identical to `baseline-numbering.txt` (no statement or exercise number changed).

## Owed to later volumes

- **Volume 11.** `volume11-randomness/chapters/ch13-harder.tex` (line ~813) cites "the upper bound lemma (Volume~10, Lemma~10.4)". Volume 10's Lemma 10.4 is the dominance lemma; the upper bound lemma is Volume 11's own `lem:upperbound` in the shuffling chapter. Cite it with `\ref`. Volume 11's other citations of Volume 10 (Wedderburn, the transposition character, Robinson–Schensted, conjugation keeps $f^\lambda$ and negates contents, $M^{(n-1,1)}\cong S^{(n)}\oplus S^{(n-1,1)}$, Exercise 10.4's multiplicity count) all point at statements that are there.
- **Volume 13.** Chapter 6 of Volume 10 is the home of ideal factorisation: Volume 13 should cite `thm:dedekind` (Theorem 6.6), `thm:intclosure` (Theorem 6.13) and `thm:fundid` (Theorem 6.14) rather than reprove them, and say that number fields have characteristic 0 (so the separability hypothesis holds). The proof of $efg=n$ stays in Volume 13, Chapter 4, which Volume 10 cites as such. Volume 13's `ch02-ideals.tex` line 80 already says "Volume 10 develops that abstract theory".
- **Volume 15.** `ch03-shuffling.tex` cites Volume 10, Theorem 10.15 for the transposition character: correct (unchanged).
- **Volume 12.** Does not cite Volume 10 by number; it may cite Chapter 11 (Theorem 11.9, Corollary 11.10) for trace moments.

## Tools

`review/volume10-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `internal_numbers.py`, `list_citations.py` as for Volume 9.

## How to build

`./build.sh --pdf-only volume10-abstraction`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy networkx`.
