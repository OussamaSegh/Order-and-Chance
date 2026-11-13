# Handoff: Volume 15 rewrite

Volume 15, *Order and Chance: The Meeting of Structure and Randomness*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-15.md`. Read this file first. It is updated after every chapter.

**Branch and pull request.** Branch `claude/project-thread-wa0mzy`, one pull request for the whole volume, as Volumes 5–14 each landed on their own pull request. The master plan and the blueprints are on PR #157 (branch `claude/project-thread-khh5pi`), which stays open. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-15.md`. The copy of `book-15.md` on `main` is an older specification (it still lists the workshop chapters to move); the blueprint on PR #157 (decisions D-29, D-30, D-31) wins.

## What "rewrite" means here

The blueprint keeps the fourteen printed chapters (D-29), writes the three stubs (Chapters 8, 12, 14; D-30), fills out Chapter 6, adds the glossary of Chapter 1, makes the hypotheses of Gallagher's and Maier's theorems explicit, confirms that `thm:sd` does not rest on Volume 11, and removes the unreached files. The work on each chapter is the list used for Volumes 5–14:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. The epigraph asks the chapter's question; the chapter ends with "What we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner.
3. **Numbers.** Every printed number not proved on the page is recomputed by a script in `review/volume15-rewrite/` (`check_chNN_*.py`, helper `common.py`).
4. **History.** Every date, quotation and attribution has a source in the chapter's one "Sources and further reading" section.
5. **References.** Citations of other volumes checked against their printed order today (`resolve_citations.py`, `reminder_citations.py`; Volume 1 counted from Chapter 0; Volume 5 after its renumbering; Volume 8 as sixteen chapters plus Appendices A–F; Volume 11 with shuffling as Chapter 13; Volume 14 with Waring as Chapter 6).
6. **Plan items** of the blueprint for that chapter. D-31: a theorem is proved when the series can prove it, otherwise stated with a source and a heading that says "quoted", "conjecture" or "conditional".
7. **R1.** Nothing after this volume: no forward premise is possible, but no proof may rest on a quoted theorem without saying so in its heading.
8. **Build.** The volume builds with no undefined reference.

Gate B of the master plan (independent verification records) is not this pass.

## Owed to this volume by earlier rewrites

- Volume 14: cite Montgomery 14.15, Halász's Plancherel lemma 10.4, `thm:maynard` 9.5, `cor:threeprimes` 7.5. The bounded-gap bound proved in the series is 4580 (Volume 14, Theorem 9.8); 600 and 246 are quoted records. Usable as proved: Siegel–Walfisz 2.12, fundamental lemma 3.4, Bombieri–Vinogradov 4.7 (ineffective), Halász 10.7, Maynard's sieve 9.3–9.6, the U^2 inverse theorem 13.3, Montgomery 14.15 (RH, α < 1). Not as proved: Zhang, Green–Tao, higher inverse theorems, Kelley–Meka, a positive proportion on the line.
- Volume 13: `ra-polynomials.tex` must say Chebotarev in Dirichlet density (Volume 13, Theorem 11.23).
- Volume 12: `moments-zeta.tex` cites "Volume 6, the zero-counting formula" and "Volume 8" for Plancherel; check against printed order. Sine kernel, trace limits and Keating–Snaith point to Volume 12, not Volume 8.
- Volume 11: Selberg–Delange is admitted there and proved here (Chapter 3, `thm:sd`); confirm no circle.
- Volume 5 renumbering table: `docs/plan/volume-citation-map.md`. Volume 1: cite via `statements.py`.

## Unreached files

Removed in the first commit after the written check `review/volume15-rewrite/unreached-removal-check.md` (28 chapter files, 35 figures, two test assertions). `reached.py --unreached` prints nothing.

## Numbering

`review/volume15-rewrite/baseline-numbering.txt` is the printed order before the rewrite. No other volume cites Volume 15 by number except Volume 11 (`thm:sd` by name and chapter) and Volume 6 (Maier by chapter). New statements go at the end of a chapter's list where possible.

## Chapter progress

| Ch. | Title | Files | State |
| --- | --- | --- | --- |
| 1 | Order and Chance in the Integers | `ch01-integers.tex`, `ra-anatomy.tex` | done: question epigraph, opening count of squarefree windows (too regular for coins), glossary kept, stale section numbers replaced by labels, the use of Chapter 3's `cor:bigomegasd` declared (no circle), closing section; captions corrected (Rankin factor 2.7–21; arcsine gap; Ford curve 4e14); `check_ch01_integers.py` |
| 2 | Models of the Primes | `ch02-cramer.tex`, `ra-largemoduli.tex`, `ra-gaps.tex` | done: question epigraph; new Section "Cramér's coins" (`lem:chernoffcoins`, `prop:cramershort`: the model predicts the share for λ>2 a.s., and fluctuates by a factor 2 for λ<2); `thm:gallagher` restated unconditionally with the exceptional term (D-29: its only zero input is `lem:onezero`, proved from Volume 14 Theorems 2.3–2.4), so Maier is unconditional; `lem:localL` now has its own proof (it pointed forward to Chapter 13's `thm:explicitchi`); section epigraphs removed; Maier's λ>2 framing fixed; one Sources section (added Pan 1957, Chowla 1934, Cramér 1920, Cramér 1936), solutions in order; closing; `check_ch02_models.py` (Buchstab sign changes, Maier figure recomputed, least-prime figure) |
| 3 | Independent Prime Divisors | `ch03-divisors.tex`, `ra-additive.tex`, `ra-selbergdelange.tex`, `ra-erdoskac.tex` | done: question epigraph and opening (2 and 3 as coins); section epigraphs removed; **no circle with Volume 11** (`sd-circle-check.md`; said in the text); Erdős–Kac corollary proof rewritten cleanly (y = x^{1/log L}, Lindeberg V4 6.10); Slutsky exercise no longer a premise (inline argument, V7 12.4); false promise of a Sathe–Selberg section replaced by Exercise `ex:landaupik` + quoted source; one Sources section, solutions in order; closing; `check_ch03_divisors.py` (about 8 minutes) |
| 4 | Random Multiplicative Functions | `ch04-multiplicative.tex`, `ra-randommult.tex`, `ra-polynomials.tex` | done: question epigraph and opening (μ is the sample with every coin −1); section epigraphs removed; hard-coded Section 5.x numbers replaced by labels (`sec:wintner`, `sec:fourth`, `sec:betterthan`); **new Section `sec:chowla`** with Proposition `prop:modelchowla` (Chowla k=2 and Sarnak hold almost surely for the Rademacher model, full proof by second moment along squares) and Chowla's and Sarnak's conjectures stated under a 'conjecture' heading, M(x)=o(x) cited to V6 Ex 5.3, Matomäki–Radziwiłł, Tao, Tao–Teräväinen, Green–Tao, BSZ quoted; new Exercise `ex:shifttwo`; Chebotarev reminder now says Dirichlet density (V13 Thm 11.23), natural density quoted, figure called an observation; `(Section~4.4)` fixed to `sec:table`; Monte Carlo numbers recomputed (V/x mean 0.65 vs exact 0.64 at 10^5, median 0.33, fourth moments 2.1 and 5.2; P≈0.4 in ex:pz; first moment drop about 20%); two Sources sections merged into one at the end; closing section. Checks: `check_ch04_multiplicative.py` (about 3 min). |
| 5 | Primes in Short Intervals | `ch05-short.tex` | done: question epigraph; Hardy–Littlewood 1923 (Partitio Numerorum III) named; closing section after the solutions (the old final paragraph of 'What stays open' moved there); every printed number recomputed: table of the pair average, V(10^8,H) for H=100, 1000 and the window ]0.9e8,1e8], V6 Fig 10.2 (mean 1.013, variance 0.79); fixes: 70 755 (not 70 750), 0.737 (not 0.736), 0.785λ = 0.79 at λ=1.01, figure agreement 'within 1% up to H=3000' (0.92% at H=30). Checks: `check_ch05_short.py` (about 6 min, 4 GB). |
| 6 | Sieves as Probability | `ch06-sieves.tex` | done, filled out: question epigraph; Brun 1919 and Selberg's 4-page Trondheim note; **new** Theorem `thm:brunpure` (Brun's pure sieve with explicit truncation, full proof from Bonferroni) and Corollary `cor:brunpure` (coins honest below x^{1/(10 log log x)}, relative error (log x)^{-2}); **new** Proposition `prop:sievefail` (ratio → e^γ ω(u) at z=x^{1/u}, from Ch 2's Buchstab theorem) with a table; Selberg corollary renamed R(x,D) (Ch 2's Φ means no prime factor < z); **new** Schnirelmann section: Def `def:schnirelmann`, Lemmas `lem:schnirelmann`, `lem:schnirelmannhalf`, Theorem `thm:schnirelmannbasis` (all proved), Goldbach sieve bound r(N) quoted (Nathanson GTM 164 Ch 7), Proposition `prop:goldbachdensity` proved from it; four new exercises; closing section. Checks: `check_ch06_sieves.py`. |
| 7 | Random Groups in Arithmetic | `ch07-classgroups.tex`, `ra-cohenlenstra.tex`, `ra-symmoments.tex` | to do |
| 8 | Ranks of Elliptic Curves | `ch08-ranks.tex` | to do (write) |
| 9 | Random Matrices and the Zeros of Zeta | `ch09-gue.tex`, `moments-zeta.tex` | to do |
| 10 | Moments of L-Functions | `ch10-moments.tex`, `ra-moments.tex` | to do |
| 11 | Value Distribution | `ch11-values.tex`, `ra-bohrjessen.tex`, `ra-selberg.tex` | to do |
| 12 | Pseudorandomness | `ch12-pseudorandom.tex` | to do (write) |
| 13 | When Order Wins | `ch13-bias.tex`, `ra-bias.tex` | to do |
| 14 | The Meeting | `ch14-meeting.tex` | to do (write, D-30) |
| — | Preface, blurb, `kdp.md` | | to do |

## Tools

`review/volume15-rewrite/reached.py` lists the reached files (`--unreached`, `--figures`). `statements.py <volume dir>` prints every numbered statement in printed order. `resolve_citations.py <files>` prints each numbered citation of another volume beside the statement that number has today; `reminder_citations.py` does the same inside reminder boxes. `qb.sh` is a quick two-pass interior build that lists undefined references.

## How to build

`./build.sh --pdf-only volume15-order-and-chance`, or `review/volume15-rewrite/qb.sh`. The container has no TeX by default: install the packages listed in `.github/workflows/build.yml`. The checks need `pip install mpmath numpy scipy sympy`. Before the pull request, also run `python3 tools/listing.py volume15-order-and-chance /tmp/x.md`.
