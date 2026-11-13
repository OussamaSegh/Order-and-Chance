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

Nothing. Pull request #234 is open. Actions run [43467337453](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43467337453) finished successfully: `list`, `debs`, `build (volume6-crossroads)`, and `site` passed. `publish` is skipped on a pull request; it runs only on `main`. Do not merge.

Head after the citation fix: `5023acf0`. This handoff commit does not change the book. If it starts another Actions run, that run is docs-only.

## Remains

None for this rewrite. A later pass should re-check the hand-typed Volume 5 citations after the parallel Volume 5 pull request lands, and should point Volume 8's expander chapter at Theorem 7.10. Neither file is edited here.

## Open math questions

- Volume 5 citations in this book are hand-typed. A parallel rewrite of Volume 5 may renumber them. Re-check every “Volume 5, Theorem/Proposition/Exercise/Corollary”, especially Theorem 10.8 (\(\xi\), label `thm:functional`), Theorem 12.4 (\(\eta\), label `thm:eta`), Proposition 10.6, Corollary 10.9, Theorems 9.15, 9.18, 9.26 and 9.36, and Exercises 5.7 and 6.5.
- Volume 8, `volume8-analysis/chapters/ch09-expanders.tex`, still cites Volume 6, Chapter 5 for an error \(O(\sqrt x\log x)\) under the Riemann hypothesis. Chapter 5 gives no error term. The right pointer is Theorem 7.10. Do not edit Volume 8 in this pull request.
- No cross-volume `\ref` exists, so those citations cannot be made label-based from Volume 6 alone.

## Exact next steps

1. From this branch, run `./build.sh volume6-crossroads`.
2. If `check_book_layout.py` fails, grep `build/volume6-crossroads/main.log` for `Overfull`.
3. Confirm `dist/` has the reading PDF, the print PDF, and the EPUB, and that `tools/check_epub_media.py` passed (the build script runs it).
4. Record the review, commit, push.
5. Open the PR with `ManagePullRequest`, `base_branch` `main`, title `Volume 6: complete rewrite`.
6. Poll the GitHub Actions run until every job is finished.
