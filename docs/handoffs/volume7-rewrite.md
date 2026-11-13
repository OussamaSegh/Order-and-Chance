# Volume 7 rewrite — handoff

Branch: `cursor/volume7-complete-rewrite-8161`. Base: `main` at `87b07362` (Volume 6 rewrite, PR #234). `origin/main` has since moved by the Volume 3 review commits `1e85f6ff` and `68c03cb0`; those commits do not touch Volume 7. Do not edit Volumes 1–6 or Volumes 11–15. Do not merge or edit PR #157. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-07.md`. The blueprint keeps thirteen chapters and the existing statement numbers. Where it disagrees with the older `docs/plan/book-07.md` on `main`, the blueprint wins. The sentence-level rewrite does not renumber.

## What “rewritten” means

A sentence counts when it has at least 40 characters and at least 25 characters outside mathematics. It is rewritten when it is not identical to the sentence in `origin/main` (the Volume 7 files are unchanged between `87b07362` and current `origin/main`). Target: at least 90% in every chapter, in the main text and again from the exercises onward (hints and solutions included). Quotations inside quotation marks may stay. A displayed formula that was already checked may stay. The English around it may not.

## Style

`docs/WRITING-STYLE.md`, Sound human, and the openings of Volumes 5 and 6 after their rewrites. Short sentences. A small case before the general claim. “You” when the reader should check a case. No “delve”, “robust”, “landscape”, “tapestry”, “journey”, “it is important to note”, “in this section we will”, “in conclusion”. The volume already has that voice. This pass still rewrites the sentences. It does not replace the voice with a generic textbook.

## Numbering lock

Do not insert a theorem, proposition, lemma, corollary, or exercise except four new exercises at the **end** of each chapter’s exercise list. Keep every `\label`. Keep the order of numbered environments. Later volumes cite Volume 7 by hand-typed numbers (Banach is Theorem 2.12, Jordan is Theorem 6.10, Carathéodory extension is Theorem 7.10, Fubini is Theorem 9.6, conditional expectation is Theorem 11.16, the tower property is cited elsewhere as Theorem 11.17, Riesz representation is Theorem 12.3). A new statement in the middle would shift those numbers. New exercises use fresh labels `ex:v7cNNa` through `ex:v7cNNd`.

Counted from the shared theorem counter (definitions and examples included), those seven labels are still 2.12, 6.10, 7.10, 9.6, 11.16, 11.17 and 12.3. No numbered environment was inserted except the four exercises at the end of each list. No label is duplicated. Every exercise has a hint and a solution.

No proof or solution may use a later chapter or a later volume as a premise. A forward pointer is a preview.

## Portraits

`volume7-spaces/photos/CREDITS.md` lists eighteen files, the source URL, the licence, and the print cap. `\portrait` is defined in `volume7-spaces/main.tex`, the same macro Volumes 5 and 6 use. Place them at the first real mention:

| Chapter | File | Portraits |
| --- | --- | --- |
| 1 | `ch01-sets.tex` | `dedekind`, `cantor` |
| 2 | `ch02-metric.tex` | `frechet` |
| 3 | `ch03-topology.tex` | `hausdorff`, `urysohn` |
| 4 | `ch04-compact.tex` | none (Weierstrass is in Chapter 5) |
| 5 | `ch05-baire.tex` | `baire`, `weierstrass` |
| 6 | `jordan.tex` | `jordan` |
| 7 | `ch06-measures.tex` | `lebesgue`, `borel`, `vitali`, `caratheodory` |
| 8 | `ch07-integral.tex` | `fatou`, `levi` |
| 9 | `ch08-products.tex` | `fubini`, `tonelli` |
| 10 | `ch09-lp.tex` | none (no Riesz portrait with a clear licence) |
| 11 | `ch10-radon.tex` | `radon` |
| 12 | `ch11-metricmeasures.tex` | `kolmogorov` |
| 13 | `ch12-harder.tex` | none (no Khinchin portrait with a clear licence) |

Caption pattern, credits exactly as in `photos/CREDITS.md`. Example:

```
\portrait{dedekind}{Richard Dedekind (1831--1916). Photograph, about 1870. Public domain, via Wikimedia Commons.}
```

Banach, Nikodym, Khinchin and Riesz were not included. The Commons files were a monument, a tomb, or a portrait whose public-domain claim had no source.

Short photographs are capped in `main.tex` so the print height keeps the short side at about 300 ppi. The KDP image check rejects a placement below 299.5 ppi.

## Figures

Each chapter includes at least two new TikZ figures, colours `MidnightBlue` and `BurntOrange`, by `\fig{...}` inside `\begin{figure}[ht]`. Captions state the takeaway. No existing figure file was overwritten. No pixel width was set.

| Chapter | Included figures |
| --- | --- |
| 1 | `ch01-rw-cut`, `ch01-rw-reals` |
| 2 | `ch02-rw-open`, `ch02-rw-ultra` |
| 3 | `ch03-rw-openclosed`, `ch03-rw-ends` |
| 4 | `ch04-rw-subcover`, `ch04-rw-escape` |
| 5 | `ch05-rw-fatcantor`, `ch05-rw-lines` |
| 6 | `jordan-rw-winding`, `jordan-rw-vertex` (the vertex plate is in `jordan-polygon.tex`) |
| 7 | `ch07-rw-intervals`, `ch07-rw-cantor` |
| 8 | `ch08-rw-slices`, `ch08-rw-nodom` |
| 9 | `ch09-rw-slices`, `ch09-rw-det` |
| 10 | `ch10-rw-split`, `ch10-rw-conv` |
| 11 | `ch11-rw-hahn`, `ch11-rw-vitali` |
| 12 | `ch12-rw-slide`, `ch12-rw-tight` |
| 13 | `ch13-rw-approximants`, `ch13-rw-borel` |

Three earlier plates, `ch01-rw-cauchy`, `ch03-rw-cut` and `ch03-rw-product`, remain in `figures/` and are not included. The build compiles every file in that directory. Do not delete them in passing.

## Exercises

Four new exercises per chapter, after the last existing exercise, each with a hint and a solution (`\idea` then `\writeup`). Solvable from this chapter and earlier. Stars as in the series. Labels `ex:v7c01a`–`ex:v7c13d`.

## Done

| Commit | What |
| --- | --- |
| `9bfef5e5` | Portraits, credits, blurb, listing, About the Cover |
| `8ffe7fb2` | Preface. The debts table stayed. The index introductory sentence was rewritten; the index entries were not |
| `b1e0447f`, `3e6f392a` | Chapter 1 |
| `7d86c23c` | Chapter 2 |
| `2be5e1f2`, `a144e00f` | Chapter 3 |
| `304904d8` | Chapter 4 |
| `ff654555` | Chapter 5 |
| `c81b3aa1` | Chapter 6, Jordan |
| `53a03872` | Chapter 7, measures |
| `c30155bf` | Chapter 8, the integral |
| `5500a88d` | Chapter 9, products |
| `777fb90d` | Chapter 10, \(L^p\) |
| `80bf00c0` | Chapter 11, differentiation and Radon–Nikodym |
| `46f0f8f6` | Chapter 12, measures on metric spaces |
| `2c8286b5` | Chapter 13, the problem chapter |
| `d66b19de` | Cleared a duplicated figure label |

Checked while continuing from `d66b19de`:

- The shared counter still prints Banach 2.12, Jordan 6.10, Carathéodory extension 7.10, Tonelli 9.5, Fubini 9.6, conditional expectation 11.16, the tower property 11.17, Riesz 12.3, Prokhorov 12.7.
- Volume 5, Theorem 6.13, cited for Weyl’s criterion, is `thm:weyl`.
- Recomputed: the four convergents of \(\sqrt2-1\) are \(1/2\), \(2/5\), \(5/12\), \(12/29\), and the two windows in `ch13-rw-approximants` place them where the caption says. The golden-ratio histogram for \(1\le n\le 4000\) puts 1997 samples in each end bin of width \(0.05\). Newton’s bounds for \(\sqrt2\) from \(x_0=2\), rounded up at each step, are the printed ones, and the true error at step 5 is \(8.99\times 10^{-25}\). The Dottie number begins \(0.7390851332\), and \(\sin\) of it is about \(0.674\). The Calkin–Wilf index of \(13/5\) is 43. The 5-adic check \(57^2+1=3250=26\cdot 125\) holds. The unit ball in dimension 4 has volume \(\pi^2/2\), matching the new exercise.
- Four sentences in the new solutions were repaired after that reading. The positive square root now spells why the shift \(2s+2\) beats the factor \(2s+1\). The truncated metric states the two cases of the triangle inequality. The \(\varepsilon\)-net of \((0,1]\) uses the point \(1\) when \(\varepsilon\ge 1\). The sliding intervals \([n,n+1]\) meet an integer in two sets, not one, and the limit superior is still empty.
- Two sentences that later-volume tests pin by their wording were put back after the first CI list job failed. Chapter 2 again says that the closed unit ball, and its identification with the compatible residue sequences, are built in this chapter. Chapter 9 again says that Volume 4 proved its rectangular identities without importing general Tonelli or Fubini.
- The Volume 7 cover note changes the hash in `review/volume3-internal/inventory.json` and the Volume 3 concept snapshot. That refresh is hash-only. No Volume 3 anchor or classification changed. `main` was merged so the list job sees the current citation tests.

## Share of prose rewritten

Measured against `87b07362`. A sentence is counted when it has at least 40 characters and at least 25 characters outside mathematics. “Rewritten” means the sentence is not identical to one in that file.

| Chapter | Whole file | Before the exercises | From the exercises on |
| --- | --- | --- | --- |
| Preface | 96% | 96% | — |
| 1 Sets | 99% | 100% | 97% |
| 2 Metric spaces | 97% | 98% | 94% |
| 3 Topology | 99% | 100% | 98% |
| 4 Compactness | 99% | 100% | 97% |
| 5 Baire | 99% | 100% | 97% |
| 6 Jordan | 99% | 100% | 98% |
| 7 Measures | 99% | 100% | 98% |
| 8 Integral | 100% | 100% | 99% |
| 9 Products | 98% | 98% | 98% |
| 10 \(L^p\) | 99% | 100% | 98% |
| 11 Radon–Nikodym | 96% | 97% | 94% |
| 12 Metric measures | 98% | 99% | 97% |
| 13 Almost every number | 97% | 100% | 97% |

The index is a list of statement names. Its one introductory sentence was rewritten. The entries were left, so the file as a whole is not a 90% rewrite, and it was not meant to be. Chapter 13’s prose before the problems is short because the chapter is a problem chapter; those sentences are rewritten. `jordan-polygon.tex` is rewritten with the Jordan chapter.

The four repairs above are later than this count. They change a few sentences and do not pull any chapter under 90%.

## Build

Local `./build.sh volume7-spaces` finished with exit 0.

- Print interior: **407 pages**, 513 × 738 pt (7.125 × 10.25 in). Spine 0.9576 in. Two pages flattened at 600 ppi. KDP interior and cover checks passed.
- Reading PDF: 408 pages, cover plus the same body.
- Layout: 394 whole boxes, maximum height 288.5 pt, no overflow, no unresolved references.
- `main.log`: no overfull boxes, no undefined references.
- EPUB: 25 MB. 58 plates at 1800 px, full width, colour. Inline mathematics carries an em baseline. The three unincluded plates are not in the EPUB.

## In progress

Push, mark PR #237 ready, and wait for CI (`list`, `debs`, `build`, `site`).

## Remains

CI on the final head. `publish` is skipped on a pull request.

The independent review is a separate agent. This file does not contain that review.

## Open math questions

- Chapter 12 quotes, and must keep quoting: that Hausdorff measure is a Borel measure, the general Prokhorov theorem on Polish spaces, and Moran–Hutchinson. The proved Prokhorov theorem is the Euclidean form.
- Chapter 13 must not use the ergodic theorem or Lévy’s constant as a premise. The existing elementary bound for Khinchin stays. Both constants are named as previews.
- Fréchet’s file is marked public domain on Commons, with no photographer and no date. It is included with that note. Drop it if a later check rejects the claim.
- Volume 8 still cites Volume 6, Chapter 5, for an error term that chapter does not give (recorded in the Volume 6 handoff). Not this pull request.
- Later volumes cite Volume 7 by hand-typed numbers. This pass did not shift them. Those volumes were not edited.

## Repairs after the second review

The second review, `docs/review/volume7-rewrite-second-review-2026-11-13.md` on PR #241, asked for four repairs at `a17a4d18`. They are in the following commit.

- Exercise `ex:v7c08c` now bounds \(f_m(x)=me^{-mx}\) by \(m/e\ge 1/(2ex)\), using \(mx<1\).
- Lemma `lem:monoivt` again says every value between \(f(a)\) and \(f(b)\), endpoints included. The proof takes the endpoints first, then the open interval, and reduces a decreasing map to \(-f\).
- Theorem `thm:condexp` again says that \(X\ge 0\) almost surely forces \(\mathbb E[X\mid\mathcal G]\ge 0\) almost surely. The proof passes to \(\max(X,0)\).
- The solution of `ex:v7c11b` cites `thm:continuum` for the uncountability of \(\R\).
- Theorem `thm:dct6` now assumes that the pointwise limit \(f\) is measurable. Without that hypothesis the claim is false on Borel measure: the indicator of a non-Borel subset of a Borel null set is a dominated almost-everywhere limit of the zero sequence and is not integrable, because the integral is not defined. The proof builds a measurable \(\varphi\) that agrees with the limit off one null set, then uses the hypothesis to pass from \(\varphi\) to \(f\). Vitali's theorem is unchanged: convergence in measure is defined only for a measurable limit.
- The cut plate labels \(\frac43\), not both \(\frac75\) and \(1.4\). The open-ball radius ends inside the circle. Banach and Tarski in 1924 are credited with a finite decomposition; five pieces, and the failure of four, are Robinson's 1947 result. The square-root step in `thm:uniqueR` now uses \(h(2s+1)<h(2s+2)<x-s^2\).

A comparison of every numbered statement with `origin/main` found no other dropped hypothesis or quantifier. Replacements such as “for all” by “for every”, and “unique” by “exactly one”, keep the claim.

## Exact next steps

1. Push `cursor/volume7-complete-rewrite-8161`.
2. Mark PR #237 ready and poll the Actions run until `list`, `debs`, `build`, and `site` have finished.
3. Report the head SHA and the run IDs on the pull request. Do not push again just to record them.
