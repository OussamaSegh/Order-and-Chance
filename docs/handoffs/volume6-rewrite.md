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

Main has been merged (`932bc285`, Volume 5 rewrite). Every Volume 6 citation of Volume 5 was checked against that book: 101 numbered citations, and every one matches the kind and the number. Nothing in Volume 6 was changed for this.

- Theorem 10.8 is `thm:functional`: \(\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac12+\frac12 s(s-1)I(s)\), entire, \(\xi(1-s)=\xi(s)\).
- Theorem 12.4 is `thm:eta`: \(\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)\).
- Theorem 8.6 is Fourier inversion. The class is a continuous integrable function whose transform is integrable. A jump is outside the class. Volume 6 says so in Chapter 9 and does not apply the theorem to a jump.
- Proposition 10.6, Corollary 10.9, Theorems 9.15, 9.18 and 9.26, Theorem 9.36, Exercises 5.7 and 6.5, and the Gauss-sum citations Theorem 8.14 and Proposition 7.13, are the statements Volume 6 uses.

Local `./build.sh volume6-crossroads` passed after the portraits: 381 print pages, no undefined reference, EPUB with 14 portrait JPEGs. Colour originals stayed RGB. Hadamard and Mertens are monochrome in the source files.

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

Push the merge and poll CI until `list`, `debs`, `build`, and `site` finish. `publish` runs only on `main`.

## Open math questions

- The Volume 5 citations were re-checked against `932bc285` and left as they stand. A later edit of Volume 5 would need the same check again.
- Volume 8, `volume8-analysis/chapters/ch09-expanders.tex`, still cites Volume 6, Chapter 5 for an error \(O(\sqrt x\log x)\) under the Riemann hypothesis. Chapter 5 gives no error term. The right pointer is Theorem 7.10. Do not edit Volume 8 in this pull request.

## Exact next steps

1. Push `cursor/volume6-complete-rewrite-5aa1`.
2. Poll the Actions run until `list`, `debs`, `build`, and `site` have finished.
