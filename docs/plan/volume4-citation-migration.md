# Volume 4 citation migration (fourteen-chapter contract)

Owner approval of 6 November 2026 replaces the twelve-chapter numbering. Other
volumes were not edited. Each row is a live citation in `volume5`–`volume15`
(or a shared note). Historical review JSON is not a live citation and is omitted.

Printed numbers below were counted from the numbered environments
`theorem`, `proposition`, `lemma`, `corollary`, `definition` in the new
`main.tex` order, and from exercise order. `examplex` and `definitionx` are
unnumbered and were not counted.

## Chapter map

| Old draft chapter (12) | New chapter |
| --- | --- |
| 1 Counting and Paradoxes | 1 From Games to Probability Spaces (Bertrand and Buffon moved to 5) |
| 2 Discrete Random Variables | 2 Random Variables and Their Laws |
| 3 Generating Functions | 3 Generating Functions and Random Families |
| 4 Inequalities, Large Numbers and Entropy | 4 Concentration (entropy removed) |
| 5 Continuous Probability | 5 Continuous Chance (Bertrand, Buffon inserted; no new numbered theorem before the old list except the two moved theorems, which sit after Box–Muller and before the exercises) |
| 6 Convergence and the CLT | 6 Why the Bell Curve Appears |
| 7 Random Walks | 8 Random Walks |
| 8 Markov Chains | 9 Markov Chains and Mixing |
| 9 Poisson Processes | 10 The Poisson Clock |
| 10 Martingales | 11 Martingales and Fair Games |
| 11 Brownian Motion | 12 Brownian Motion |
| 12 The Probabilistic Method | 13 The Probabilistic Method, and 14 Random Graphs |
| Appendix B Extremal | Appendix B Extremal (counter still set to 1) |

## Numbers that stay honest

- Exercise 6.1 is still Slutsky (`ex:slutsky`), first exercise of Chapter 6.
- Theorem 6.10 is still Lindeberg. No numbered environment was inserted before it.
- Theorem 4.5 is still Weierstrass via Bernstein.
- Exercise 13.4 is the crossing lemma (`ex:crossing`), fourth exercise of Chapter 13. The live citation says Exercise 12.4.
- Appendix letter remains B.

## Numbers that moved, and the live lines that still use the old ones

These files were not changed. The new number is what a later edit of that line would have to say.

| Live citation | File:line | New number |
| --- | --- | --- |
| Theorem 4.11, Borel–Cantelli | `volume15-order-and-chance/chapters/ra-randommult.tex:15` | Theorem 4.3 (`thm:bc`). The label 4.11 was already the pre-rewrite book, not the twelve-chapter draft. |
| Chapter 4, Borel–Cantelli (no number) | `volume15-order-and-chance/chapters/ra-additive.tex:19` | Still Chapter 4. |
| Chapter 4, Chebyshev | `volume15-order-and-chance/chapters/ch01-research.tex:28` | Chebyshev is recalled, not restated as a numbered theorem. The inequality used is Volume 1. |
| Theorem 6.8, inversion | `volume15-order-and-chance/chapters/ra-bohrjessen.tex:20` and `:162` | No inversion theorem is numbered 6.8. Characteristic-function inversion is not a theorem of this manuscript. Repair needs a statement in Volume 4 or a different citation. Not invented here. |
| Theorem 6.10, Lindeberg | `volume15-order-and-chance/chapters/ch03-shuffling.tex:165` and `:396` | Still Theorem 6.10. |
| Theorem 6.15, Gaussian vectors | `volume12-random-motion/chapters/ch01-gaussian.tex:39` and `:85`; `volume12-random-motion/chapters/ch03-martingales.tex:556`; `volume8-analysis/chapters/ch11-harder.tex:1139` | Theorem 6.14 (`thm:gaussvec`). |
| Exercise 6.1, Slutsky | `volume15-order-and-chance/chapters/ra-selberg.tex:26`; `ra-additive.tex:170`; `volume8-analysis/chapters/ch11-cue.tex:32` | Still Exercise 6.1. |
| Theorem 7.7, arcsine | `volume15-order-and-chance/chapters/ra-anatomy.tex:174` and `:238` | There is no arcsine theorem in the manuscript. The walk chapter proves reflection, ruin, and Pólya. The continuous arcsine law is not claimed. |
| Theorem 7.9, gambler's ruin | `volume12-random-motion/chapters/ch03-martingales.tex:451` and `:538` | Theorem 8.2 (`thm:ruin`). |
| Theorem 7.12, returns | `volume12-random-motion/chapters/ch08-networks.tex:24` | Pólya is Theorem 8.4 (`thm:polya`). The visit criterion is Proposition `prop:visits` in the same chapter; its printed number is the third numbered environment of Chapter 8, so Proposition 8.3. |
| Chapter 7, walks / cone | `volume12-random-motion/chapters/ch05-analysis.tex:25` and `:268` | Chapter 8. |
| Exercise 7.8, electrical networks | `volume12-random-motion/chapters/ch08-networks.tex:12` | Exercise 8.8 (`ex:electric`), eighth exercise of the walk chapter. |
| Exercise 8.6, top-to-random | `volume15-order-and-chance/chapters/ch03-shuffling.tex:300` and `:384`; `ch12-projects.tex:28` | Exercise 9.6 (`ex:toptorandom`). |
| Exercise 8.8, rising-sequence variance | `volume15-order-and-chance/chapters/ch03-shuffling.tex:167` | Exercise 9.8 (`ex:risingmean`). Variance `(n+1)/12` is unchanged. |
| Lemma 8.10, Definition 8.22, Theorem 8.23, Proposition 8.24 | `volume15-order-and-chance/chapters/ch03-shuffling.tex:234`, `:395`, `:396`, `:397` | The Markov chapter has two numbered theorems. Those four labels are the pre-rewrite shuffle chapter. They are not in this manuscript. Bayer–Diaconis profile analysis was deliberately not copied. |
| Chapter 8, total variation | `volume15-order-and-chance/chapters/ch03-shuffling.tex:396` | Chapter 9, and only for the coupling proof that is actually written. |
| Lemma 9.5, colouring | `volume12-random-motion/chapters/ch07-levy.tex:25` | Lemma 10.5 (`lem:colouring`). |
| Chapter 9, Poisson processes | `volume12-random-motion/chapters/ch07-levy.tex:25` | Chapter 10. |
| Chapter 10, martingale $L^2$ | `volume15-order-and-chance/chapters/ch11-values.tex:115` | Chapter 11. The $L^2$ sentence in that line is Doob's theorem, now Theorem 11.4 (`thm:doob`), not a numbered 10.15. |
| Theorem 10.15, Doob maximal | `volume12-random-motion/chapters/ch03-martingales.tex:30` and `:129`; `ch04-ito.tex:322` | Theorem 11.4. |
| Theorem 10.18, $L^2$ convergence | `volume12-random-motion/chapters/ch03-martingales.tex:31` and `:166` | Theorem 11.4 states $L^2$ convergence for a martingale bounded in $L^2$. Confirm the exact sentence before changing the citation; the old 10.18 is not a separate environment. |
| Theorem 10.24, Azuma | `volume12-random-motion/chapters/ch04-ito.tex:259` | Theorem 11.5 (`thm:azuma`). |
| Theorem 11.4, existence of Brownian motion | `volume12-random-motion/chapters/ch01-gaussian.tex:42` | Theorem 12.4 (`thm:levy`). |
| Proposition 11.5 and 11.7 | `volume12-random-motion/chapters/ch02-paths.tex:32` | Scaling is the fifth numbered environment of Chapter 12, so Proposition 12.5 if the label is `prop:scaling`. The second citation must be re-read against the chapter before a number is assigned. |
| Theorem 11.8, quadratic variation | `volume12-random-motion/chapters/ch03-martingales.tex:34` and `:302` | Theorem 12.7 (`thm:qv`). |
| Theorem 11.12, reflection | `volume12-random-motion/chapters/ch01-gaussian.tex:42`; `ch02-paths.tex:32`, `:162`, `:359`; `ch03-martingales.tex:414` | Theorem 12.12 (`thm:reflection`). |
| Exercise 11.3, zero set | `volume12-random-motion/chapters/ch02-paths.tex:170`, `:183`, `:378` | Exercise 12.3 (`ex:zeros`). The solution uses the integral of Chapter 5, not Tonelli. The Volume 12 sentence that says "by Tonelli" overstates the tool. |
| Chapter 11, Brownian motion and Itô | `volume8-analysis/chapters/ch04-spectral.tex:197`, `:328`, `:392`, `:467`; `volume12-random-motion/chapters/ch04-ito.tex:21` and `:211` | Chapter 12. The Itô formula in Volume 4 is a dyadic expansion, marked as such, and is not the general integral. |
| Exercise 12.4, crossing lemma | `volume14-primes/chapters/ch11-additive.tex:15`; `volume15-order-and-chance/chapters/conjectures-ch08-geometric.tex:101` | Exercise 13.4. |
| Theorem B.15, van der Waerden | `volume14-primes/chapters/ch12-roth.tex:15` | Appendix B has five numbered theorems (Turán, Ramsey, Schur, sunflower, EKR). Van der Waerden is not among them. |
| Buffon, Chapter 1 | `volume9-shapes/chapters/ch10-integral.tex:124` | Chapter 5 (`thm:buffon`). |
| Chapter 6, Gaussian law | `volume8-analysis/chapters/ch02-hilbert.tex:276` | Still Chapter 6. |
| Theorem 4.5, Weierstrass | `volume8-analysis/chapters/ch10-semicircle.tex:103` | Still Theorem 4.5. |

## What was not done

No file under `volume5`–`volume15` was edited. Compatibility is not green.
The minimal repairs are the rows above whose "New number" differs from the
printed citation, plus the four rows marked as absent (inversion 6.8, arcsine
7.7, shuffle labels 8.10/8.22/8.23/8.24, van der Waerden B.15). Those four
need an owner decision: add a proved statement, or retarget the later book.
