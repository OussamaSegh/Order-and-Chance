# Volume 7 rewrite — handoff

Branch: `cursor/volume7-complete-rewrite-8161`. Base: `main` at `87b07362` (Volume 6 rewrite, PR #234). Do not edit Volumes 1–6 or Volumes 11–15. Do not merge or edit PR #157. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-07.md`. The blueprint keeps thirteen chapters and the existing statement numbers. Where it disagrees with the older `docs/plan/book-07.md` on `main`, the blueprint wins. The sentence-level rewrite does not renumber.

## What “rewritten” means

A sentence counts when it has at least 40 characters and at least 25 characters outside mathematics. It is rewritten when it is not identical to the sentence in `origin/main`. Target: at least 90% in every chapter, in the main text and again from the exercises onward (hints and solutions included). Quotations inside quotation marks may stay. A displayed formula that was already checked may stay. The English around it may not.

## Style

`docs/WRITING-STYLE.md`, Sound human, and the openings of Volumes 5 and 6 after their rewrites. Short sentences. A small case before the general claim. “You” when the reader should check a case. No “delve”, “robust”, “landscape”, “tapestry”, “journey”, “it is important to note”, “in this section we will”, “in conclusion”. The volume already has that voice. This pass still rewrites the sentences. It does not replace the voice with a generic textbook.

## Numbering lock

Do not insert a theorem, proposition, lemma, corollary, or exercise except four new exercises at the **end** of each chapter’s exercise list. Keep every `\label`. Keep the order of numbered environments. Later volumes cite Volume 7 by hand-typed numbers (Banach is Theorem 2.12, Jordan is Theorem 6.10, Carathéodory extension is Theorem 7.10, Fubini is Theorem 9.6, conditional expectation is Theorem 11.16, the tower property is cited elsewhere as Theorem 11.17, Riesz representation is Theorem 12.3). A new statement in the middle would shift those numbers. New exercises use fresh labels `ex:v7cNNa` through `ex:v7cNNd`.

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

## Figures

Each chapter gains at least two new TikZ figures, files `volume7-spaces/figures/chNN-rw-*.tex`, colours `MidnightBlue` and `BurntOrange`, included by `\fig{...}` inside `\begin{figure}[ht]`. Captions state the takeaway. Do not overwrite an existing figure file. Do not set a pixel width.

## Exercises

Four new exercises per chapter, after the last existing exercise, each with a hint and a solution (`\idea` then `\writeup`). Solvable from this chapter and earlier. Stars as in the series.

## Done

- Branch created.
- Portrait macro, eighteen photographs, `photos/CREDITS.md`.
- About the Cover rewritten (112 words, inside the 80–150 check). Only the Volume 7 string in `common/cover-notes.json` changed, plus the generated `about-the-cover.tex`, the Volume 7 paragraph in `docs/COVER-NOTES.md`, and the two hashes in `tools/assets/series/manifest.json`. Motifs and lettering were not regenerated.
- `blurb.tex` rewritten (194 words, the same length as before). `kdp.md` rewritten. ISBN left blank. Riesz representation is claimed only for positive functionals. Prokhorov is claimed only for tight laws on Euclidean space. Hausdorff measure as a Borel measure is marked quoted.

## Done

- Setup commit `9bfef5e5`: portraits, credits, blurb, listing, About the Cover.
- Preface and index introduction: `8ffe7fb2`.
- Chapter 1, `ch01-sets.tex`, commit `b1e0447f`. Labels preserved in order. New figures `ch01-rw-cut`, `ch01-rw-cauchy`. New exercises `ex:v7c01a`–`ex:v7c01d`. Measured rewrite share against `origin/main`: 99% before the exercises, 96% from the exercises on, 98% whole file (sentences of at least 40 characters with at least 25 outside math).

## In progress

Chapter 2, `ch02-metric.tex`. No other chapter file has been rewritten yet.

## Remains

Chapters 2–13, then the independent review, the local PDF and EPUB build, marking the PR ready, and CI.

## Remains

1. Rewrite every chapter, including proofs, exercises, hints, solutions, and the sources section’s English. Commit after each chapter.
2. Add the portraits, two figures, and four exercises in each chapter as above.
3. Rewrite `chapters/preface.tex` (the debts table stays; the prose changes). The index is a list of statement names. Rewrite its one introductory sentence only. Do not change index numbers.
4. Independent review. Write `docs/review/volume7-rewrite-findings-<date>.md`.
5. Measure the rewrite share against `origin/main` and put the table in this file.
6. `./build.sh volume7-spaces`. Zero undefined references. Layout checks pass. EPUB plates full width and in colour. Portraits at least 300 ppi.
7. Push and poll CI until `list`, `debs`, `build`, and `site` pass. `publish` is skipped on a pull request.

## Open math questions

- Chapter 12 quotes, and must keep quoting: that Hausdorff measure is a Borel measure, the general Prokhorov theorem on Polish spaces, and Moran–Hutchinson. The proved Prokhorov theorem is the Euclidean form.
- Chapter 13 must not use the ergodic theorem or Lévy’s constant as a premise. The existing elementary bound for Khinchin stays.
- Fréchet’s file is marked public domain on Commons, with no photographer and no date. It is included with that note. Drop it if a later check rejects the claim.
- Volume 8 still cites Volume 6, Chapter 5, for an error term that chapter does not give (recorded in the Volume 6 handoff). Not this pull request.
- Later volumes cite Volume 7 by hand-typed numbers. This pass must not shift them. Do not edit those volumes. List any citation that is already wrong, and leave it.

## Exact next steps

1. Rewrite `volume7-spaces/chapters/ch01-sets.tex` in place. Preserve labels and order. Add `\portrait{dedekind}` and `\portrait{cantor}` with the captions in `photos/CREDITS.md`. Add two figures `figures/ch01-rw-*.tex` and four exercises `ex:v7c01a`–`ex:v7c01d` at the end of the exercise list, with hints and solutions.
2. Commit that chapter. Update this file: chapter 1 done, chapter 2 next.
3. Repeat for chapters 2–13 and the preface, one commit each.
4. Do not start the build until the sentence rewrite of every chapter is committed.
