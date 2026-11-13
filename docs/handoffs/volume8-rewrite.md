# Volume 8 rewrite — handoff

Branch: `cursor/volume8-complete-rewrite-3faf`. Base: `main` at `e9711ffe`. The folder is `volume8-analysis`. Do not edit any other volume. Do not merge, and do not edit, PR #157. Read the blueprint with `git show origin/claude/project-thread-khh5pi:docs/plan/book-08.md`. The structural pass (sixteen chapters, six appendices, random-matrix chapters in Volume 12) is already on `main`. Where the blueprint disagrees with the older `docs/plan/book-08.md` on `main`, the blueprint wins. This pass does not renumber.

## What “rewritten” means

A sentence counts when it has at least 40 characters and at least 25 characters outside mathematics. It is rewritten when it is not identical to the sentence in `origin/main`. Target: at least 90% in every chapter, in the main text and again from the exercises onward (hints and solutions included). Quotations inside quotation marks may stay. A displayed formula that was already checked may stay. The English around it may not.

## Style

`docs/WRITING-STYLE.md`, Sound human. Short sentences. A small case before the general claim. “You” when the reader should check a case. No “delve”, “robust”, “landscape”, “tapestry”, “journey”, “it is important to note”, “in this section we will”, “in conclusion”. The volume already has that voice. This pass still rewrites the sentences. It does not replace the voice with a generic textbook.

## Numbering lock

Do not insert a theorem, proposition, lemma, corollary, definition, or example except nothing: no new numbered statement in the middle. Four new exercises go at the **end** of each chapter’s exercise list. Keep every `\label`. Keep the order of numbered environments. Later volumes cite Volume 8 by hand-typed numbers. A new statement in the middle would shift those numbers. New exercises use fresh labels `ex:v8c01a` through `ex:v8c16d` for the sixteen chapters and `ex:v8cAa` through `ex:v8cFd` for the appendices.

No proof or solution may use a later chapter or a later volume as a premise. A forward pointer is a preview. Proofs use only what Volumes 1–8 have already taught, in the printed order of `main.tex`. Numerical checks are not proofs. Do not weaken a theorem.

Do not change fonts, sizes, or the text inside an existing diagram. New figures are new files. Do not regenerate cover motifs or lettering. The paperback ISBN stays blank.

## Portraits

`\portrait` is defined in `volume8-analysis/main.tex`, the same macro Volumes 5 and 7 use. Credits live in `volume8-analysis/photos/CREDITS.md`. Place a portrait at the first real mention. Caption pattern repeats the credit. Short photographs are capped so the print height keeps the short side at about 300 ppi.

## Figures

Each chapter includes two new TikZ figures, colours `MidnightBlue` and `BurntOrange` (and `BrickRed` where a third ink helps), by `\fig{...}` inside `\begin{figure}[ht]`. Captions state the takeaway. No existing figure file is overwritten. No pixel width is set. New files are named `chNN-rw-*.tex` or `appX-rw-*.tex`.

## Exercises

Four new exercises per chapter, after the last existing exercise, each with a hint and a solution (`\idea` then `\writeup`). Solvable from this chapter and earlier volumes. Stars as in the series.

## Scope of files

- `volume8-analysis/`
- `docs/handoffs/volume8-rewrite.md`
- the Volume 8 sentence in `common/cover-notes.json`, and the hashes `tools/series_cover.py --check` needs (`volume8-analysis/about-the-cover.tex`, `docs/COVER-NOTES.md`, `tools/assets/series/manifest.json`)
- if the cover-note hash moves, the Volume 3 inventory and conceptual snapshot get a hash-only refresh, because `inventory.py --check` and `registers.py` compare those hashes

## Chapter map

| Ch. | Title | File | Label |
| --- | --- | --- | --- |
| 1 | Banach Spaces | `ch01-banach.tex` | `ch:banach` |
| 2 | Hilbert Spaces | `ch02-hilbert.tex` | `ch:hilbert` |
| 3 | The Spectral Theorem and Its Relatives | `linear-ch05-spectral.tex` | `linear:ch:spectral` |
| 4 | Singular Values | `linear-ch06-svd.tex` | `linear:ch:svd` |
| 5 | Graphs through Their Eigenvalues | `linear-ch08-graphs.tex` | `linear:ch:graphs` |
| 6 | Cuts, Mixing and Expansion | `spectral-expansion.tex` | `ch:cheeger` |
| 7 | Expanders and Ramanujan Graphs | `ch09-expanders.tex` | `ch:expanders` |
| 8 | Operators, Spectra and Banach Algebras | `ch03-operators.tex` | `ch:operators` |
| 9 | The Spectral Theorem for Compact Operators | `ch04-spectral.tex` | `ch:spectral` |
| 10 | The Fourier Transform | `ch05-fourier.tex` | `ch:fourier` |
| 11 | Distributions and Sobolev Spaces | `ch06-distributions.tex` | `ch:distributions` |
| 12 | Fourier Analysis on Finite Abelian Groups | `ch07-finite.tex` | `ch:finite` |
| 13 | Haar Measure, Duality and the p-adic Numbers | `ch08-haar.tex` | `ch:haar` |
| 14 | Cauchy's Theorem, Growth and Mellin Inversion | `ch09-complex.tex` | `ch:complex` |
| 15 | Tauberian Theorems | `ch10-tauberian.tex` | `ch:tauberian` |
| 16 | The Values of Zeta | `ch11-harder.tex` | `ch:harder` |
| A | Spaces, Quotients and Duality | `linear-ch01-duality.tex` | `linear:ch:duality` |
| B | Determinants as Volume | `linear-ch02-volume.tex` | `linear:ch:volume` |
| C | Eigenvalues and Invariant Subspaces | `linear-ch03-eigen.tex` | `linear:ch:eigen` |
| D | Inner Products and Projections | `linear-ch04-inner.tex` | `linear:ch:inner` |
| E | Inequalities between Matrices | `linear-ch11-inequalities.tex` | `linear:ch:inequalities` |
| F | Linear Dynamics | `linear-ch12-dynamics.tex` | `linear:ch:dynamics` |

## Progress

| Ch. | State |
| --- | --- |
| — | Draft pull request opened: https://github.com/OussamaSegh/Order-and-Chance/pull/242 |
| — | Preface, blurb, `kdp.md`, About the Cover, portrait macro and credits | Done |
| 1–16, A–F | Sentence rewrite, two figures, four exercises | In progress |

Portraits on disk, not yet placed in the chapters: Banach, Hilbert, Cayley, Kirchhoff, Fredholm, Fourier, Poisson, Gauss, Haar, Hadamard, Cauchy, Tauber, Riemann, Jordan, Frobenius, Schwarz, Lyapunov. Credits are in `volume8-analysis/photos/CREDITS.md`. Place each at the first real mention. Do not invent a caption.

The Volume 8 cover note changed `common/cover-notes.json`. `tools/series_cover.py --check` passes. The Volume 3 inventory and conceptual snapshot were restamped for that one hash. No Volume 3 anchor or status changed.

## Build

Not yet. When the manuscript is in, `./build.sh --pdf-only volume8-analysis` and the EPUB. No overfull boxes, no undefined references. Page count must stay between 300 and 600.

## Remains

Every chapter, the preface, the blurb, `kdp.md`, the About the Cover note, portraits, two new figures per chapter, four new exercises per chapter. Then the local build, then CI.

The independent review is a separate agent. This file does not contain that review.
