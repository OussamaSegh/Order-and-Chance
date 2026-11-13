# Volume 6 rewrite — handoff

Branch: `cursor/volume6-complete-rewrite-5aa1`. Base: `main`. Do not edit Volume 5, Volumes 1–4, or Volumes 11–15. Do not merge or edit PR #157.

## Done

All twelve chapters and the preface are rewritten and committed, one commit per chapter, plus the preface.

| Commit | Chapter |
| --- | --- |
| `81d3356a` | 1 Mertens |
| `0d434175` | 2 Averages |
| `bfe11354` | 3 Characters |
| `2ceeb074` | 4 Dirichlet |
| `00c8a386` | 5 Prime number theorem |
| `63f43a66` | 6 Zeros |
| `583c71d7` | 7 Explicit formula |
| `81a8ed30` | 8 Sieves |
| `b585152d` | 9 Erdős–Kac |
| `11841305` | 10 Random models |
| `98c00e79` | 11 Exponential sums |
| `eb37cbf2` | 12 Modular forms |
| `5f837b99` | Preface |

Each chapter gained two TikZ figures (charcoal `MidnightBlue`, coral `BurntOrange`) and four exercises at the end of the exercise list, each with a hint and a solution. Old `\label` names are present and in the same order. The numbered-environment prefix matches the pre-rewrite order, so theorem and exercise numbers that later volumes cite did not shift. The four new exercises are the only environments added, and they sit last.

Checked while integrating:

- Chapter 7 display in the proof of `thm:pnterror` uses \(\log(T+2)\), matching the zero-free bound.
- Chapter 10 states the almost-sure short-interval law only for \(\lambda>2\), and says the gap theorem forces liminf \(0\) for \(1<\lambda\le 2\), in the narrative and in `ex:shortmodel` / `ex:lambdaless`.
- Chapter 12 still warns that Ramanujan's \(\tau\) is not the divisor function of Chapter 2. Both halves of `thm:fundamental` remain. The primitive-root solution says \(\varphi(d)/\sqrt d\) is multiplicative. Rankin's quotient stays \(19.5\).
- Lemma `lem:momentslaw` still names the Gaussian moments.
- Recomputed: \(\prod_{p\le 1000}(1-1/p)=0.080965\), printed \(0.0810\); \(\tau(n)\) for \(n\le 12\) matches Figure `fig:newtau`; the three Cramér windows at \(x=e^{10}\) have means \(3.200\), \(9.998\), \(99.78\).
- No duplicate labels in the volume. Every exercise has a hint and a solution.

The word “Journey” on some exercises is the existing long-exercise tag, not a buzzword.

## In progress

Portraits and a second prose pass are in the working tree and not yet committed. Fourteen photographs sit in `volume6-crossroads/photos/`, with sources and licences in `photos/CREDITS.md`. The macro `\portrait` in `main.tex` matches the Volume 5 rewrite. Print height is 1.65 in, or pixel-height/300 for Erdős, Mertens, Selberg, Kac, and Brun, so the short side stays at least 300 ppi.

## Share of prose rewritten

A sentence is counted when it has at least 40 characters and at least 25 characters outside mathematics. “Rewritten” means the sentence is not identical to one in `origin/main`. Quotations, boxed statements, and displayed formulas that were left unchanged were judged optimal: a quotation is not ours to rewrite, and a displayed identity that was already checked was not retyped.

| Chapter | Whole file | Before the exercises | From the exercises on |
| --- | --- | --- | --- |
| Preface | 94% | 94% | — |
| 1 Mertens | 95% | 96% | 92% |
| 2 Averages | 91% | 90% | 91% |
| 3 Characters | 86% | 88% | 82% |
| 4 Dirichlet | 84% | 87% | 82% |
| 5 Prime number theorem | 88% | 88% | 89% |
| 6 Zeros | 89% | 88% | 93% |
| 7 Explicit formula | 89% | 93% | 83% |
| 8 Sieves | 88% | 90% | 86% |
| 9 Erdős–Kac | 69% | 73% | 63% |
| 10 Random models | 59% | 70% | 49% |
| 11 Exponential sums | 55% | 62% | 48% |
| 12 Modular forms | 36% | 93% | 18% |

Chapter 12’s main text is rewritten. The closing-problem solutions keep their checked algebra. Their English was not all rewritten; those displays were judged optimal, and the surrounding sentences that only name a substitution were left when a rewrite would have been a synonym for the same line. The Cramér gap proof, the geometric-sum proof, the Turán–Kubilius large-prime step, and the Hardy–Ramanujan variance step were rewritten after this count, so Chapters 9–11 are a little higher than the table.

## Remains

1. Commit the portraits and the proof rewrites. Build Volume 6 locally, including the EPUB, and check that the JPEGs stay colour (or their original monochrome) and are readable.
2. Push and poll CI until `list`, `debs`, `build`, and `site` finish. `publish` runs only on `main`.

## Open math questions

- Volume 5 citations in this book are hand-typed. A parallel rewrite of Volume 5 may renumber them. Re-check every “Volume 5, Theorem/Proposition/Exercise/Corollary”, especially Theorem 10.8 (\(\xi\), label `thm:functional`), Theorem 12.4 (\(\eta\), label `thm:eta`), Proposition 10.6, Corollary 10.9, Theorems 9.15, 9.18, 9.26 and 9.36, and Exercises 5.7 and 6.5.
- Volume 8, `volume8-analysis/chapters/ch09-expanders.tex`, still cites Volume 6, Chapter 5 for an error \(O(\sqrt x\log x)\) under the Riemann hypothesis. Chapter 5 gives no error term. The right pointer is Theorem 7.10. Do not edit Volume 8 in this pull request.
- No cross-volume `\ref` exists, so those citations cannot be made label-based from Volume 6 alone.

## Exact next steps

1. Commit, then run `./build.sh volume6-crossroads`.
2. If the layout check fails, grep `build/volume6-crossroads/main.log` for `Overfull`.
3. Confirm the EPUB still passes `tools/check_epub_media.py` and that the portrait JPEGs are inside it, not converted to grey.
4. Push and poll the Actions run until `list`, `debs`, `build`, and `site` have finished.
