# Handoff: Volume 7 rewrite

Volume 7, *Spaces: Topology, Measure and Limits*, has been rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-07.md`. Read this file first. It was updated after every chapter; the state below is final for this pass.

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
| 1 | Sets, Choice and the Real Numbers | `ch01-sets.tex` | `ch:sets` | Done |
| 2 | Metric Spaces and Completeness | `ch02-metric.tex` | `ch:metric` | Done |
| 3 | Topological Spaces | `ch03-topology.tex` | `ch:topology` | Done |
| 4 | Compactness | `ch04-compact.tex` | `ch:compact` | Done |
| 5 | Baire's Theorem | `ch05-baire.tex` | `ch:baire` | Done |
| 6 | The Jordan Curve Theorem | `jordan.tex`, `jordan-polygon.tex` | `ch:jordan` | Done |
| 7 | Measures | `ch06-measures.tex` | `ch:measures` | Done |
| 8 | The Lebesgue Integral | `ch07-integral.tex` | `ch:integral` | Done |
| 9 | Product Measures and Change of Variables | `ch08-products.tex` | `ch:products` | Done |
| 10 | $L^p$ Spaces | `ch09-lp.tex` | `ch:lp` | Done |
| 11 | Differentiation and Radon–Nikodym | `ch10-radon.tex` | `ch:radon` | Done |
| 12 | Measures on Metric Spaces | `ch11-metricmeasures.tex` | `ch:metricmeasures` | Done |
| 13 | Almost Every Number (problems) | `ch12-harder.tex` | `ch:harder` | Done |
| — | Preface (debts table), blurb, final checks | `preface.tex`, `blurb.tex`, `kdp.md` | | Done |

## What changed, chapter by chapter

- **1.** Voice; new exercise `ex:cwcompute` at the end.
- **2.** New `cor:Zpcompact` after `thm:Qp` (the plan's addition, decisions D-14 and D-17); new exercise `ex:Z2cantor`. This shifts the statements after 2.10 by one: Banach is now Theorem 2.12, `thm:exp` 2.16, Hutchinson 2.20.
- **3.** New `prop:tietze` (Tietze for metric spaces) at the end of the statements; exercise `ex:tietze` replaced by `ex:tietzeR`.
- **4, 5.** Voice, sources, one new exercise in Chapter 5 (`ex:takagivalues`).
- **6.** Polygons first. Numbering changed: `thm:jordanpoly` 6.1, `lem:parity` 6.2, `lem:sides` 6.3, `lem:lift` 6.4, `prop:windingprops` 6.6, `thm:brouwer` 6.7, `lem:crossing` 6.8, `lem:arc` 6.9, `thm:jordan` 6.10. `lem:arc` now cites `prop:tietze`. Three new exercises.
- **7–12.** Wording about Volume 4 follows Volume 4 as printed (it no longer admits Kolmogorov's theorem or an axiom (A1)). New exercises `ex:dealing`, `ex:limits`, `ex:frullani`, `ex:tent`, `ex:maximalcompute`, `ex:coversums`. The solution of `ex:salem` proves the strong law for a biased coin by fourth moments; Chapters 12 and 13 use it. Statements quoted and not used are marked quoted (Hausdorff measure facts from Falconer, the general Prokhorov theorem, Moran–Hutchinson).
- **13.** See the next section.
- **Preface.** Rewritten, with the table of debts. `blurb.tex` and `kdp.md` no longer claim Dedekind cuts as a second construction, duality of $L^p$ or a Riesz representation theorem, none of which is in the book.

## Chapter 13 and decision D-15

No solution uses a later volume. What was done:

- **Khinchin's theorem** (`pb:khinchin`): Lévy's theorem is replaced by an elementary bound. $q_n\le\prod(a_i+1)$, the integral of $\prod(a_i+1)^{1/2}$ is at most $c^n$ with $c=2\sum 1/(k\sqrt{k+1})=4.3680\ldots$ by bounded distortion (`pb:borelbernstein`(a)), then Markov and Borel–Cantelli give $q_n\le e^{5n}$ for almost every $x$. The blocks are $Q_n=\lfloor e^{5n}\rfloor$ and the constant in (d) is 6.
- **Null sets** in `pb:badnull`(c), `pb:good`(a), `pb:etwo`(a) and `pb:typicalcf`(b) come from `pb:borelbernstein` and `pb:khinchin`(b), not from the ergodic theorem.
- `pb:eggleston`(b) uses the strong law from the solution of `ex:salem`. `pb:cantorfourier`(c) is now the elementary statement (no point of the Cantor set has an equidistributed orbit under multiplication by 3).
- **Moved to Volume 11**, file `volume11-randomness/chapters/from-volume7-problems.tex`, NOT wired into Volume 11's `main.tex`: Minkowski's question mark (whole problem, hint, solution, figure `volume11-randomness/figures/from-volume7-minkowski.tex`) and the old part (c) of the Cantor measure problem (the orbit is distributed according to the Cantor measure), as a new problem `pb:cantororbit`. The Volume 11 rewrite places them; the header of the file lists what to check.
- Quoted and not proved: Euler's continued fraction of $e$ (used in `pb:econt`, source Cohn 2006), Lévy's constant, Khinchin's constant (leads only).
- Problems after 13.5 are renumbered down by one.

## For the other volumes

- **Volume 9.** Fixed here because the numbers changed in this pass: Banach is Volume 7, Theorem 2.12 (`ch01-manifolds.tex`); the lifting lemma is Lemma 6.4 and the winding-number proposition is Proposition 6.6 (six citations in `ch03-forms.tex`, `ch04-curvature.tex`, `ch05-coverings.tex`).
- **Every later volume** cites Volume 7 by hand-typed numbers, some from before the Jordan chapter was inserted. Only Chapters 2, 6 and 13 changed numbering in this pass; `review/volume7-rewrite/baseline-numbering.txt` against `statements.py` gives the table. Each volume's rewrite checks its own citations of Volume 7.
- **Volume 11** owns the two moved problems (above), and Volume 7 now says, as previews, that Volume 11 proves Lévy's and Khinchin's constants and the ergodicity of the Gauss map.
- **Volume 6** (PR #195, not merged when this was written): Chapter 13 cites the prime number theorem as Volume 6, Theorem 5.5, Chapter 5. If the number changes, fix `pb:jarnik`(b).
- **Volumes 1–6** citations were checked against the printed books: Volume 2 continued fractions are Chapter 9 (Proposition 9.1, Theorem 9.2, Lemma 9.4, Theorems 9.5 and 9.6, Exercise 9.7); Volume 5 Weyl's criterion is Theorem 6.13.

## Not re-fetched

These bibliographic details were written from memory and not checked against the source in this pass: Miranda 1940 (Chapter 6); the pages of Lebesgue's 1926 Copenhagen lecture, *Matematisk Tidsskrift B* (1926) 54–74 (Chapter 8); Robinson 1947 and Littlewood 1944 (Chapter 7); Moran 1946 and Hutchinson 1981, and the chapter numbers of Falconer's *Fractal Geometry*, 3rd ed. (Chapter 12); Lévy 1936 and Khinchin 1935 as the years of the two constants (Chapter 13). Gate B should check them.

## Checks

`python3 review/volume7-rewrite/check_chNN_*.py`, thirteen scripts, all pass. The build has no undefined reference.


File names keep their old numbers (the Jordan chapter was inserted as Chapter 6), so the file number is one less than the chapter number from `ch06-measures.tex` on.

## Tools

`review/volume7-rewrite/statements.py volume7-spaces` prints every numbered statement in printed order. `baseline-numbering.txt` is that list before the rewrite. `internal_numbers.py` finds hand-typed statement numbers. `list_citations.py` lists every citation of another volume.

## Rules kept from Volumes 5 and 6

- **Numbering inside a chapter is preserved.** Other volumes cite Volume 7 by hand-typed numbers. New statements and exercises go where they shift nothing that is cited, by default at the END of a list.
- Citations of Volumes 1–4 are by chapter and topic, checked against the printed order listed in `docs/handoffs/volume5-rewrite.md`. Citations of Volume 5 follow its new chapter order (`docs/plan/volume-citation-map.md`).

## How to build

`./build.sh --pdf-only volume7-spaces`, or `xelatex` in `volume7-spaces/` as `build.sh` does. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`.
