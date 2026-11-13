# Handoff: Volume 14 rewrite

Volume 14, *The Primes*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-14.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-7s9t0g`, one pull request for the whole volume, as Volumes 5–13 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-14.md`. The copy of `book-14.md` on `main` is an older specification that sends Waring to Volume 5; the blueprint on PR #157 (decision D-11: Waring is Volume 14, Chapter 6) wins.

## What "rewrite" means here

The blueprint preserves Chapters 1–5, 7–8 and 10–14, receives `waring.tex` from Volume 5 as Chapter 6 (D-11), restructures one theorem of Chapter 9 (D-27), and fixes the list of quoted results (D-28). The work on each chapter is the list used for Volumes 5–13:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. The epigraph asks the chapter's question; the chapter ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume14-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's "Sources and further reading".
5. **References.** Citations of other volumes checked against their printed order today (`resolve_citations.py` for "Volume N, Theorem X"; `reminder_citations.py` for the bare numbers inside reminder boxes; Volume 1 counted from Chapter 0; Volume 5 after its renumbering; Volume 7 Chapters 2, 6, 13; Volume 8 as sixteen chapters plus Appendices A–F; Volume 11 with shuffling as Chapter 13). Internal chapter numbers become `Chapter~\ref{ch:...}`, because Waring shifts every chapter after Chapter 5.
6. **Plan items** of the blueprint for that chapter.
7. **R1.** No proof or solution uses Volume 15 as a premise.
8. **Build.** The volume builds with no undefined reference.

Gate B of the master plan (independent verification records) is not this pass.

## Owed to this volume by earlier rewrites

- Volume 5: wire `waring.tex` as Chapter 6 (done in the first commit). Volume 5 chapters renumbered (old 6–13 are 4–11, Hardy–Ramanujan 12, AGM 13); table in `docs/plan/volume-citation-map.md`.
- Volume 7: numbering changed in Chapters 2, 6, 13 (`docs/handoffs/volume7-rewrite.md`). Volume 8: sixteen chapters plus Appendices A–F. Volume 9: cite Volume 1 via `statements.py`. Volume 10: shuffling moved to Volume 11 (Chapter 13; problems Chapter 14).
- Volume 11: `volume14-primes/chapters/ch14-critical.tex` cited "Volume 5, Corollary 10.10" (fixed by PR #226). Volume 11 cites Volume 14's Roth chapter by name only.
- Volume 12: cites Montgomery as Volume 14, Theorem 13.15 (`thm:montgomerypc`), which becomes 14.15 once Waring is Chapter 6.
- Volume 13: no Volume 13 number cited here moved (Theorems 4.18, 11.9, 11.10, 11.23, Corollary 7.5 unchanged).

## Numbering

Inserting Waring as Chapter 6 shifts every later chapter by one: Three Primes 6 → 7, GPY 7 → 8, Maynard 8 → 9, Halász 9 → 10, Additive Combinatorics 10 → 11, Roth 11 → 12, Gowers 12 → 13, Critical Line 13 → 14. `review/volume14-rewrite/baseline-numbering.txt` is the printed order before the rewrite (without Waring). Inside Chapters 1–5, 7–8 and 10–14 the statement numbers are preserved: new statements go at the end of a chapter's list. Chapter 9 is restructured (D-27); its new numbering is recorded below.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| 1 | Zeros and Primes in Short Intervals | `ch01-zeros.tex` | done: closing section; checks `check_ch01_zeros.py` |
| 2 | Siegel's Theorem | `ch02-siegel.tex` | done: question epigraph, closing; `check_ch02_siegel.py` |
| 3 | Sieves and the Parity Problem | `ch03-sieves.tex` | done: epigraph, closing; `check_ch03_sieves.py` (caption: ratio at u=2 is 0.954, not 0.9545) |
| 4 | The Large Sieve and Bombieri–Vinogradov | `ch04-largesieve.tex` | done: epigraph, closing, BV constant said ineffective; `check_ch04_largesieve.py` (caption: 0.26x at x=10^7, not 0.31x) |
| 5 | Exponential Sums over Primes | `ch05-expsums.tex` | done: epigraph, closing; `check_ch05_expsums.py` (caption: peak 0.168 at 1/7) |
| 6 | Waring's Problem | `waring.tex` | done: rewritten; singular series proved positive (`thm:singpos`), so `cor:gk` G(k) ≤ max(4k, 2^k+1) is proved; `check_ch06_waring.py` |
| 7 | Three Primes | `three-primes.tex` | done: epigraph, first sentence points to Chapter 6, closing; `check_ch07_threeprimes.py` (caption: singular series 1.47 to 2.3) |
| 8 | Small Gaps between Primes | `ch08-gpy.tex` | done: epigraph line, closing; `check_ch08_gpy.py` |
| 9 | Bounded Gaps between Primes | `ch09-maynard.tex` | done (D-27): `lem:productF`, `prop:mk582`, `thm:explicitgap` (gap ≤ 4580 proved), `thm:mfive`, remark "Records, quoted"; `check_ch09_maynard.py` |
| 10 | Multiplicative Functions | `ch10-halasz.tex` | done: closing; `check_ch10_halasz.py` |
| 11 | Additive Combinatorics | `ch11-additive.tex` | done: epigraph, closing; `check_ch11_additive.py` (caption: Elekes lines through at least 4 points) |
| 12 | Roth's Theorem | `ch12-roth.tex` | done: closing, sentence naming Volume 11 Theorem 10.15; `check_ch12_roth.py` (about 5 minutes) |
| 13 | Gowers Norms and the Green–Tao Theorem | `ch13-gowers.tex` | done: epigraph, closing; `check_ch13_gowers.py` (caption ratios 0.991, 0.988, 0.978; about 3 minutes) |
| 14 | The Critical Line | `ch14-critical.tex` | done: epigraph, closing, sentence naming Volume 12 Theorem 10.4 (sine kernel); `check_ch14_critical.py` |
| — | Preface, blurb, `kdp.md` | | done: new part structure, Waring, bound 4580, quoted list |
| — | Citations of Volume 14 in other volumes | | done: Volume 12 cites 14.15; Volume 15 cites 10.4, 9.5, 7.5 (`external_citations.py`) |

## Numbering after the rewrite

Chapters 1–5, 7–8 and 10–14 keep their statement numbers (Chapters 7–14 shifted by one chapter). Chapter 6 is new (Waring, 6.1–6.12, Exercises 6.1–6.5). Chapter 9 is restructured: 9.1 `lem:ltwo`, 9.2 `lem:dirichletint`, 9.3 `prop:mklower`, 9.4 `lem:productF`, 9.5 `thm:maynard`, 9.6 `cor:mprimes`, 9.7 `prop:mk582`, 9.8 `thm:explicitgap`, 9.9 `lem:symint`, 9.10 `thm:mfive`; Exercises 9.1 `ex:pigeon`, 9.2 `ex:mk581`, 9.3 `ex:mtwo`, 9.4 `ex:progs`, 9.5 `ex:gooddiff`, 9.6 `ex:upper`. `thm:six` and `thm:246` are gone.

## Owed to Volume 15

- Cite Volume 14 by today's numbers: Montgomery 14.15, Halász's Plancherel lemma 10.4, `thm:maynard` 9.5, `cor:threeprimes` 7.5 (fixed in `ch06-*.tex`; check any new text).
- The bounded-gap bound proved in this series is 4580 (`thm:explicitgap`, Theorem 9.8); 600 and 246 are quoted records. `conjectures-ch02-twins.tex` uses 246 as a quoted record; keep it marked so.
- Statements Volume 15 may use as proved: Siegel–Walfisz 2.12, the fundamental lemma 3.4, Bombieri–Vinogradov 4.7 (ineffective constant), Halász 10.7, Maynard's sieve 9.3–9.6, the U^2 inverse theorem 13.3, Montgomery 14.15 (under RH, α < 1). Not as proved: Zhang, Green–Tao, the higher inverse theorem, Kelley–Meka, a positive proportion on the line.
- From Volume 13: `ra-polynomials.tex` should say Chebotarev in Dirichlet density.

## Tools

`review/volume14-rewrite/statements.py <volume dir>` prints every numbered statement in printed order (Volume 1 counted from Chapter 0). `resolve_citations.py <chapter files>` prints each numbered citation of another volume beside the statement that number has today. `reminder_citations.py <chapter files>` does the same for the bare numbers inside reminder boxes. `qb.sh` is a quick two-pass interior build that lists undefined references.

## How to build

`./build.sh --pdf-only volume14-primes`, or `review/volume14-rewrite/qb.sh` for a quick check. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy`. Before the pull request, also run `python3 tools/listing.py volume14-primes /tmp/x.md` (CI fails on a `kdp.md` keyword over 50 characters).
