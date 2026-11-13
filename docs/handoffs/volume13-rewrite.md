# Handoff: Volume 13 rewrite

Volume 13, *Arithmetic*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-13.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-gcbsmf`, one pull request for the whole volume, as Volumes 5–12 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-13.md`. The copy of `book-13.md` on `main` is an older fourteen-chapter specification; the blueprint on PR #157 (seventeen chapters, decisions D-22 to D-25) wins.

## What "rewrite" means here

The blueprint keeps Chapters 1–17 in their order and numbers, folds the short Chapter 18 (`polyfermat.tex`) into Chapter 7 as its last section (D-24), consolidates Chapter 4 on Volume 10 (D-22) and Chapter 12 on Volume 8 (D-23), and fixes the headings of what is admitted (D-25). The work on each chapter is the list used for Volumes 5–12:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. The epigraph asks the chapter's question; the chapter ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume13-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources and further reading".
5. **References.** Citations of other volumes checked against their printed order today (`resolve_citations.py`; Volume 1 counted from Chapter 0; Volume 5 after its renumbering; Volume 7 Chapters 2, 6, 13; Volume 8 as sixteen chapters plus Appendices A–F; Volume 11 with shuffling as Chapter 13).
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses Volumes 14–15 as a premise.
8. **Build.** The volume builds with no undefined reference.

Numbering inside Chapters 1–17 is preserved: new statements go at the end of a chapter's list, because Volumes 3–15 cite Volume 13 by hand-typed numbers (for example Volume 14 cites Theorem 4.18, Corollary 7.5, Theorems 11.9 and 11.23; Volume 15 cites Theorem 4.20, Corollary 12.21, Propositions 15.14 and 17.11, Theorems 15.2, 15.15, 17.3, 17.9, Corollary 16.14). `review/volume13-rewrite/baseline-numbering.txt` is the printed order before the rewrite.

Gate B of the master plan (independent verification records) is not this pass.

## Owed to this volume by earlier rewrites

- Volume 9: Chapter 15 owns associativity of the cubic group law; Chapter 14 owns Bézout with the intrinsic intersection multiplicity (Volume 9 Appendices F and G no longer cover them).
- Volume 10: cite Volume 10, Theorems 6.6 (`thm:dedekind`), 6.13 (`thm:intclosure`), 6.14 (`thm:fundid`) for factorisation of ideals; number fields have characteristic 0, so separability holds. The proof of $efg=n$ stays in Chapter 4.
- Volume 8: Haar measure, self-duality and Fourier inversion on $\mathbb Q_p$ are Volume 8, Chapter 13 (D-23). The squares exercise already moved into `ch12-padic.tex`.
- Volume 6: the fundamental domain is Volume 6, Theorem 12.2 (both halves). Chapter 12's `cor:dirichletFE` discharges Volume 6's admitted functional equation.
- Volume 11: shuffling is Chapter 13, problems Chapter 14. Volume 12: numbering unchanged.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Quadratic Fields and Their Integers | `ch11-algebraic.tex` | |
| 2 | Ideals, Prime Splitting and Class Groups in Quadratic Fields | `ch12-ideals-quadratic.tex` | |
| 3 | Number Fields and Their Integers | `ch01-number-fields.tex` | |
| 4 | Ideals and the Splitting of Primes | `ch02-ideals.tex` | |
| 5 | The Geometry of Numbers | `ch03-geometry.tex` | |
| 6 | Units | `ch04-units.tex` | |
| 7 | Cyclotomic Fields and Fermat (+ `polyfermat.tex` as last section) | `ch05-cyclotomic.tex` | |
| 8 | The p-adic Numbers | `ch12-padic.tex` | |
| 9 | Local Fields | `ch06-local.tex` | |
| 10 | Quadratic Forms and the Local–Global Principle | `ch07-hasse.tex` | |
| 11 | Zeta Functions and Densities | `ch08-zeta.tex` | |
| 12 | Adèles, Idèles and Tate's Thesis | `ch09-tate.tex` | |
| 13 | Class Field Theory | `ch10-cft.tex` | |
| 14 | Algebraic Curves | `ch11-curves.tex` | |
| 15 | Elliptic Curves | `ch12-elliptic.tex` | |
| 16 | Curves over Finite Fields | `ch13-finite.tex` | |
| 17 | Modular Forms and L-functions | `ch14-modular.tex` | |
| — | Preface, blurb, `kdp.md` | | |

## Tools

`review/volume13-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `qb.sh` is a quick two-pass interior build that lists undefined references.

## How to build

`./build.sh --pdf-only volume13-arithmetic`, or `review/volume13-rewrite/qb.sh` for a quick check. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. Before the pull request, also run `python3 tools/listing.py volume13-arithmetic /tmp/x.md` (CI fails on a `kdp.md` keyword over 50 characters).

## What changed (summary)

(filled in chapter by chapter)

## Numbering changes for Volumes 14–15

(filled in at the end)
