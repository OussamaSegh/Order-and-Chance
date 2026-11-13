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
| 1 | Quadratic Fields and Their Integers | `ch11-algebraic.tex` | done: three exercises, closing section, Dirichlet source |
| 2 | Ideals, Prime Splitting and Class Groups in Quadratic Fields | `ch12-ideals-quadratic.tex` | done: second-proof heading (D-22), closing section |
| 3 | Number Fields and Their Integers | `ch01-number-fields.tex` | done |
| 4 | Ideals and the Splitting of Primes | `ch02-ideals.tex` | done: `thm:ufi` from Volume 10 (D-22), numbering kept, see `d22-equivalence.md` |
| 5 | The Geometry of Numbers | `ch03-geometry.tex` | done: Minkowski portrait moved here, Viazovska corrected |
| 6 | Units | `ch04-units.tex` | done: Siegel beauty box corrected, determinant 0.5255 |
| 7 | Cyclotomic Fields and Fermat (+ `polyfermat.tex` as last section) | `ch05-cyclotomic.tex` | done: `polyfermat.tex` folded in as last section (D-24), heuristic labelled, two exercises appended |
| 8 | The p-adic Numbers | `ch12-padic.tex` | done: construction cited from Volume 7, broken examples replaced |
| 9 | Local Fields | `ch06-local.tex` | done |
| 10 | Quadratic Forms and the Local–Global Principle | `ch07-hasse.tex` | done: self-citations now `\ref` |
| 11 | Zeta Functions and Densities | `ch08-zeta.tex` | done: epigraph signs fixed, Chebotarev headed "in Dirichlet density", natural density quoted |
| 12 | Adèles, Idèles and Tate's Thesis | `ch09-tate.tex` | done: Haar measure and Fourier inversion cited from Volume 8 (D-23), see `d23-equivalence.md`; Hecke's functional equation a sketch |
| 13 | Class Field Theory | `ch10-cft.tex` | done: `thm:xnyy`, `cor:principalsplit` headed "assuming the Hilbert class field" |
| 14 | Algebraic Curves | `ch11-curves.tex` | done: `prop:goppa` (14.23, the last statement) became Exercise 14.8 |
| 15 | Elliptic Curves | `ch12-elliptic.tex` | done: Mordell headed "both halves proved here for every curve"; Mazur quoted; heights and Selmer named, not developed |
| 16 | Curves over Finite Fields | `ch13-finite.tex` | done: Weil for every curve and Sato–Tate quoted; prime count of the Sato–Tate figure corrected (78 496 odd primes) |
| 17 | Modular Forms and L-functions | `ch14-modular.tex` | done: Theorem 17.1(a) cites Volume 6 Theorem 12.2(b), part (b) proved; Eichler–Shimura, modularity, Fermat, CM quoted; Shimura source |
| — | Preface, blurb, `kdp.md` | | done: Volume 12 link paragraph, four parts, the admitted and quoted list matches D-25 |

## Tools

`review/volume13-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `qb.sh` is a quick two-pass interior build that lists undefined references.

## How to build

`./build.sh --pdf-only volume13-arithmetic`, or `review/volume13-rewrite/qb.sh` for a quick check. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. Before the pull request, also run `python3 tools/listing.py volume13-arithmetic /tmp/x.md` (CI fails on a `kdp.md` keyword over 50 characters).

## What changed (summary)

- Every chapter: an epigraph that asks the chapter's question, a closing section "What we proved, and what comes next", a hostile proof read, and a check script (`check_ch01_quadratic.py` … `check_ch17_modular.py`, all passing).
- D-22: Chapter 4 factorises ideals by Volume 10 (`d22-equivalence.md`); Chapter 2 keeps its proof as a second proof.
- D-23: Chapter 12 cites Volume 8 Chapter 13 for Haar measure, self-duality and inversion on Q_p (`d23-equivalence.md`: same measure, conjugate character).
- D-24: `polyfermat.tex` is the last section of Chapter 7; the file is deleted.
- D-25 headings: Artin reciprocity, existence, Hilbert class field admitted; results that rest on them say "assuming"; Chebotarev in Dirichlet density; Hecke's functional equation for zeta_K a sketch; Mazur, Weil for every curve, Sato–Tate, Eichler–Shimura, modularity, Fermat's second case quoted; canonical heights and Selmer named; three cubes heuristic labelled; Mordell proved for every curve.
- Errors corrected along the way: the Chapter 11 epigraph series, the Chapter 8 "square everywhere locally" example, the Chapter 9 Q_p vs Q_q solution, Chapter 14's claim that Mordell needs 2-torsion, the x^2+14y^2 range (2·10^4), the regular-prime count (181 of 302 below 2000), the Sato–Tate prime count.

## Numbering changes for Volumes 14–15

Compared with `baseline-numbering.txt`. Every numbered statement of Chapters 1–17 keeps its number, with three exceptions, none cited elsewhere:

- Chapter 4: number 4.3 is now `lem:okdedekind` (O_K is Dedekind, from Volume 10) instead of `lem:containsprod`; 4.4 `lem:missing` now states P P^{-1} = O.
- Chapter 7: new Theorem 7.14 (Mason), Corollary 7.15, Propositions 7.16–7.18 (the old Chapter 18), new Exercises 7.8, 7.9. Old Chapter 18 no longer exists.
- Chapter 14: Proposition 14.23 (Goppa codes) removed; it is Exercise 14.8. Chapter 1: new Exercises 1.6–1.8.

`resolve_citations.py` on all of Volumes 14 and 15 resolves every Volume 13 citation to the intended statement. Owed to Volume 15: `ra-polynomials.tex` quotes Chebotarev (Theorem 11.23) as "density"; Volume 13 proves it in Dirichlet density, so that reminder should say so.

`tools/cross_volume_citations.py` reports no mismatch after merging `main` (PR #226 fixed the one Volume 14 citation of Volume 5).

Full build: 359 pages, no undefined references; `tools/listing.py` passes; tool tests 639 OK.
