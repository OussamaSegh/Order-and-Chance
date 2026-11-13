# Volume 15 — Order and Chance

*The Meeting of Structure and Randomness.*

**Status of this file.** Blueprint of Volume 15 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification and the review notes of 2026-11-03. The volume is the fourteen chapters reached from `main.tex` (decision D-29). No proof named here has been verified.

**Series part.** VI. Synthesis. **Directory.** `volume15-order-and-chance`.

## Central question

The question of the series: can pure order and pure chance be told apart, and why do the primes look random yet obey laws? This volume answers as far as mathematics can. For each statistic the series has studied, it sets the theorem beside the random model and says which of three things the agreement is: a theorem, a model that is known to fail somewhere, or a conjecture.

## Prerequisites

Every earlier volume, through these theorems in particular.

| From | What is used |
| --- | --- |
| Volume 4, 11 | Central and local limit theorems, Berry–Esseen, the method of moments, martingales, mod-\(\varphi\) convergence, the Poisson–Dirichlet law |
| Volume 5, 8 | Residues, Mellin inversion, Hadamard factorisation, Fourier inversion |
| Volume 6 | The prime number theorem with error, the zero-free region, the explicit formula, Selberg's sieve, Erdős–Kac, Cramér's model |
| Volume 7 | Weak convergence, Kolmogorov extension |
| Volume 12 | The sine kernel, trace limits, Keating–Snaith's moments, the log-correlated maximum |
| Volume 13 | Class groups, the class number formula, 2-descent, the functional equation of \(L(s,\chi)\), point counts |
| Volume 14 | Siegel–Walfisz, Bombieri–Vinogradov, the fundamental lemma, Halász, Maynard's sieve, the \(U^2\) inverse theorem, Carlson's zero-density estimate, Montgomery's theorem |

**Rule for this volume.** Every citation of an earlier volume names a label, and the cited theorem's status is carried with it. A proof here that rests on a hypothesis (a zero-free region wider than the proved one, the Riemann hypothesis, linear independence of zeros, Hardy–Littlewood, Elliott–Halberstam) names the hypothesis in the theorem's heading. A proof here never rests on a theorem that an earlier volume only quotes, unless the heading says so.

## Structure

Unchanged. Three chapters are stubs today and are written under this plan.

| Ch. | Title | Files | Action |
| --- | --- | --- | --- |
| | **Part I. The Question** | | |
| 1 | Order and Chance in the Integers | `ch01-integers.tex`, `ra-anatomy.tex` | Keep; add the glossary |
| 2 | Models of the Primes | `ch02-cramer.tex`, `ra-largemoduli.tex`, `ra-gaps.tex` | Keep; hypotheses made explicit |
| 3 | Independent Prime Divisors | `ch03-divisors.tex`, `ra-additive.tex`, `ra-selbergdelange.tex`, `ra-erdoskac.tex` | Keep |
| | **Part II. Arithmetic Statistics** | | |
| 4 | Random Multiplicative Functions | `ch04-multiplicative.tex`, `ra-randommult.tex`, `ra-polynomials.tex` | Keep |
| 5 | Primes in Short Intervals | `ch05-short.tex` | Keep |
| 6 | Sieves as Probability | `ch06-sieves.tex` | Keep; short, to be filled out |
| 7 | Random Groups in Arithmetic | `ch07-classgroups.tex`, `ra-cohenlenstra.tex`, `ra-symmoments.tex` | Keep |
| 8 | Ranks of Elliptic Curves | `ch08-ranks.tex` | Write (about 50 lines today) |
| | **Part III. Spectra** | | |
| 9 | Random Matrices and the Zeros of Zeta | `ch09-gue.tex`, `moments-zeta.tex` | Keep; citations retargeted to Volume 12 |
| 10 | Moments of \(L\)-Functions | `ch10-moments.tex`, `ra-moments.tex` | Keep |
| 11 | Value Distribution | `ch11-values.tex`, `ra-bohrjessen.tex`, `ra-selberg.tex` | Keep |
| | **Part IV. Structure versus Randomness** | | |
| 12 | Pseudorandomness | `ch12-pseudorandom.tex` | Write (about 50 lines today) |
| 13 | When Order Wins | `ch13-bias.tex`, `ra-bias.tex` | Keep |
| | **Part V. The Research Workshop** | | |
| 14 | The Meeting | `ch14-meeting.tex` | Write (about 45 lines today) (D-30) |

**Not in the volume.** The files in `chapters/` that `main.tex` does not reach (the former workshop chapters and tours). Nothing they contain is needed elsewhere: the riffle-shuffle cutoff is printed in Volume 11, Chapter 13; Mason–Stothers in Volume 13, Chapter 7; the BBP formula in Volume 5, Chapter 4. They are removed from the directory after a written check per file.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Friable integers and Dickman's function; Rankin's trick; Erdős's multiplication table theorem | | 1 |
| The smoothed explicit formula; a log-free zero-density estimate; Gallagher's prime number theorem for large moduli; Buchstab's asymptotic; **Maier's theorem**; the Erdős–Rankin lower bound for large gaps | `thm:logfree`, `thm:gallagher`, `thm:buchstab`, `thm:maier`, `thm:erdosrankin` | 2 |
| Turán–Kubilius; the Kubilius model; Erdős–Wintner; Selberg–Delange; Landau's count of sums of two squares; Erdős–Kac as a corollary (second proof) | `thm:sd` | 3 |
| Wintner's theorem for a random multiplicative function; statistics of polynomials over finite fields | | 4 |
| The pair average to second order; Gallagher's Poisson law under Hardy–Littlewood | | 5 |
| Selberg's weights as a projection; the sieve bound read as an expectation | | 6 |
| Moments of cokernels of random matrices; Friedman–Washington; the moments determine the Cohen–Lenstra law | | 7 |
| The linear algebra of a random maximal isotropic intersection, as the model for a Selmer group | new | 8 |
| The form factor of the unitary ensemble beside Montgomery's theorem; the mean square of \(\zeta\) to the right of the line | `thm:formfactor` | 9 |
| The second moment of \(\zeta\) on the line; lower bounds for higher moments | | 10 |
| Bohr–Jessen's limiting distribution; **Selberg's central limit theorem** for \(\log\lvert\zeta(\tfrac12+it)\rvert\) | `thm:selberg`, `thm:twisted` | 11 |
| The dichotomy for three-term progressions told once: correlation with a character, or small \(U^2\) norm, in the language of Volumes 11 and 14 together | new | 12 |
| The limiting logarithmic distribution of the prime race, under the generalised Riemann hypothesis and linear independence | | 13 |

## Stated without proof

Decision D-31: proved when the series can prove it from its own volumes, otherwise stated with a source, never sketched as if proved.

| Statement | Heading must say |
| --- | --- |
| Cramér's conjecture on gaps; Granville's correction | Conjecture |
| Linnik's theorem with the exceptional zero; Deuring–Heilbronn | Quoted |
| Chowla's and Sarnak's conjectures | Conjecture |
| Harper's theorems on random multiplicative functions | Quoted |
| Montgomery–Soundararajan beyond the second moment | Quoted, conditional |
| The Cohen–Lenstra heuristics for class groups; their 2-part | Heuristic. The measure is a theorem; its match with class groups is not |
| Davenport–Heilbronn; Bhargava's averages; Bhargava–Shankar | Quoted |
| Goldfeld's conjecture; Poonen–Rains | Conjecture, heuristic |
| The fourth moment of \(\zeta\) | Quoted from Ingham unless proved here |
| Keating–Snaith's conjecture for moments of \(\zeta\) | Conjecture |
| Fyodorov–Hiary–Keating; the theorems towards it | Conjecture; quoted |
| Montgomery's conjecture for \(\alpha\ge1\); the identification of zeros with a spectrum | Conjecture |
| Green–Tao; nilsequences | Quoted. The series has no nilsequences and the chapter does not use them |
| Lemke Oliver–Soundararajan | Quoted |

## Climax

Two theorems, one on each side.

**Maier's theorem (Chapter 2).** The primes match Cramér's coin model in mean and in variance, and still fail it: in intervals of length \((\log x)^\lambda\) the number of primes is, infinitely often, larger and smaller than the model predicts by a constant factor. Order shows through.

**Selberg's central limit theorem (Chapter 11).** At a random height, \(\log\lvert\zeta(\tfrac12+it)\rvert\) divided by \(\sqrt{\tfrac12\log\log T}\) is Gaussian. A function built from the primes behaves exactly as chance would.

## The ending

Chapter 14, "The Meeting", is the synthesis the series has promised since its first volume. It has three sections.

1. **The ledger.** One table of every statistic the series has studied: the number of prime factors, primes in long and in short intervals, primes in progressions, gaps, values of \(\mu\), class groups, ranks, pairs of zeros, moments and values of \(\zeta\), three-term progressions, the prime race. For each: the random model; whether the agreement is a theorem, and where it is proved; where the model is known to fail; what remains conjecture. The table agrees line by line with the theorem-status ledger of the repository.
2. **The answer.** Two pages. Order and chance cannot be told apart by any one statistic in bulk, and that is a collection of theorems. They can be told apart at fine scales, and Maier's theorem is the proof. Why the zeros of \(\zeta\) follow the statistics of a random unitary matrix is not known. The book says so in those words.
3. **Reading a paper, and two projects.** As now: how to read a research paper in this area, and two projects that use only tools the series has proved, each stopping on the line between a theorem and a guess.

## Motivation and history

Cramér's 1936 model, Maier's 1985 surprise, Kubilius, Erdős and Kac at Princeton, Wintner, Cohen and Lenstra's tables, Selberg's 1946 paper, Bohr and Jessen, Montgomery and Dyson, Keating and Snaith, Chebyshev's 1853 letter on the prime race, Rubinstein and Sarnak. Each sourced.

## Examples and exercises

Each chapter of Parts I–IV has a computed comparison of an arithmetic statistic with its model, and exercises (five to fourteen) at three levels. Chapters 8, 9, 10, 12 and 13 need exercises of their own: today they have none or inherit them from an included file.

## Figures and experiments

This volume prints more data than any other: counts of primes in short intervals against the Poisson and Maier predictions; histograms of \(\omega(n)\); partial sums of a random multiplicative function; class group statistics; spacings of zeros; values of \(\log\lvert\zeta\rvert\); the prime race modulo 4. Every figure and every printed number has a script, a seed and a data source in the numerical-claims ledger, and every caption says "theorem", "model" or "observation".

## Changes from the current manuscript

**Preserve.** The fourteen chapters and their included files.

**Write.** Chapters 8, 12 and 14 to the standard of the others. Chapter 1's glossary of what "random-like" means. Chapter 6 filled out.

**Rewrite.** Chapter 2: `thm:gallagher` is headed "under the zero-free region of Volume 14" while assuming a lemma of this chapter; the hypothesis is stated once, exactly, and traced to a proved theorem (Volume 6's zero-free region, Volume 14's Landau–Page) or kept as a named hypothesis. Maier's theorem then carries whatever it inherits. Chapter 9, 10 and anywhere else: citations of the sine kernel, the trace limits and Keating–Snaith point to Volume 12, not Volume 8. Chapter 3: the citation of Volume 11, Chapter 11 inside the proof of Selberg–Delange is confirmed to be a comparison, and reworded so that it cannot be read as a premise.

**Remove.** The duplicated "Sources and further reading" sections in Chapters 2, 3, 4 and 11: one per chapter. The unreached files. Any mention of nilsequences as a tool.

**Missing.** Exercises where noted. The ending.

## Links

**From Volume 14.** Its last theorem is this volume's Chapter 9.
**From Volume 12.** The chance side of Part III.
**From Volume 6.** The Maier remark and Cramér's model, answered. Erdős–Kac, proved a second time and compared.
**Back to Volume 11.** `thm:sd` discharges the admitted Selberg–Delange formula.
**Forward.** Nothing. Chapter 14 closes the series.

## Size

About 5,430 source lines today. The three written chapters, the glossary and the exercises add perhaps 1,500. **Estimate, not measured:** 200–250 printed pages. The earlier target of 280–340 pages assumed the workshop chapters and is withdrawn.

## Mathematical risks

1. **Maier's theorem's hypotheses.** The climax must be unconditional or say what it assumes. This is checked before any other work on the volume.
2. **The circle with Volume 11** through Selberg–Delange.
3. **Selberg's theorem.** The proof must use only zero-density input that Volume 14 or this volume proves. Every use of a density estimate is listed in the verification record.
4. **The log-free zero-density estimate**, a hard theorem proved in an included file with no exercises around it.
5. **Overclaiming in the new chapters.** Ranks and pseudorandomness are areas where almost everything is conjecture. Decision D-31 governs.
6. **The prime race.** The theorem is conditional on two hypotheses; the percentages quoted for how often one side leads are computations from the literature, not theorems of the book.
7. **The ledger of Chapter 14** must not promote a model to a theorem.

## Acceptance requirements

- Structure equals the table above. No file in `chapters/` is unreached.
- Every theorem heading names its hypotheses. No proof rests on a quoted theorem without saying so.
- Verification records for every label in the flagship table: `thm:gallagher`, `thm:maier`, `thm:sd`, `thm:selberg` first.
- A written confirmation that the proof of `thm:sd` does not use Volume 11, Chapter 11's corollary.
- Chapter 14's ledger equals the repository's status ledger for the statements it lists.
- Every figure and printed number in the numerical-claims ledger.
- One "Sources" section per chapter.
- The ten editorial standards of the master plan, section 6.5.
