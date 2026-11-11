# Handoff: Volume 5 rewrite

Volume 5, *Calculation: From Formula to Insight*, is being rewritten to `docs/plan/MASTER-PLAN-V5-V15.md` and `docs/plan/book-05.md`. This file is updated with every chapter. Read it first.

**Branch and pull request.** The author chose to keep the whole rewrite in PR #157, on branch `claude/project-thread-khh5pi`, together with the master plan. Do not merge without the author's word.

## What "rewrite" means here

The blueprint keeps the mathematics of Chapters 1–11 and 13 and asks for new mathematics in Chapter 12 only. So each chapter gets one pass with a fixed list:

1. **Voice.** `docs/WRITING-STYLE.md`, Sound human. A friend who loves mathematics, explaining the step. Opens with a question, shows an example before the general statement, names the stages of long proofs, ends with "what we proved, and what comes next".
2. **Proof read.** Every proof re-read as a hostile examiner. Skipped steps written out. Hypotheses matched against the statements cited.
3. **Numbers.** Every printed number that is not proved on the page is recomputed by a script in `review/volume5-rewrite/`, one script per chapter.
4. **History.** Every date, quotation and attribution has a source in the chapter's one "Sources" section.
5. **References.** Hand-typed numbers inside the volume ("Chapter~7", "Theorem~12.3") become `\ref` to labels. Chapters have labels `ch:…` (table in `docs/plan/volume-citation-map.md`).
6. **Plan items** for that chapter (list below).
7. **Exercises.** Three levels, at least one proof and one computation, each with hint and solution (`\idea`, then `\writeup`).
8. **Build.** The volume builds, `tools/check_book_layout.py` and `tools/check_edition_copy.py` pass.

Gate B of the master plan (independent verification) is not this pass. The writer cannot verify their own chapter. Statuses in a future theorem ledger stay NOT REVIEWED until an independent reviewer files records.

## Chapter progress

| Ch. | Title | File | State |
| --- | --- | --- | --- |
| — | Structure (D-10, D-11) | `main.tex` | **Done** |
| 1 | Finite Calculus | `ch01-finite.tex` | **Done** |
| 2 | Generating Functions as a Computing Tool | `ch02-generating.tex` | **Done** |
| 3 | Classic Series and Infinite Products | `ch03-series.tex` | **Done** |
| 4 | Integration Techniques | `ch04-integrals.tex`, `bbp-borwein.tex` | **Done** |
| 5 | The Gamma and Beta Functions | `ch05-gamma.tex` | **Done** |
| 6 | Fourier Series | `ch06-fourier.tex` | **Done** |
| 7 | The Discrete Fourier Transform and the FFT | `ch07-fft.tex` | **Done** |
| 8 | The Fourier Transform and Poisson Summation | `ch08-transform.tex` | Not started |
| 9 | Complex Analysis for Computing | `ch09-complex.tex` | Not started |
| 10 | The Zeta Function | `ch10-zeta.tex` | Not started |
| 11 | Asymptotics | `ch11-asymptotics.tex` | Not started |
| 12 | The Hardy–Ramanujan Formula | `hardy-ramanujan.tex` | **Done** (rewritten, new proof of the η transformation) |
| 13 | The Arithmetic–Geometric Mean | `ch12-agm.tex` | Not started |
| — | Preface, blurb, final checks | `preface.tex`, `blurb.tex` | Preface chapter list updated; final pass not started |

## Done so far

**Structure.** `main.tex` equals the blueprint's table: three parts, thirteen chapters. `waring.tex` and its figure moved to `volume14-primes/` (figure renamed `waring-fivesquares.tex`). Volume 14's `main.tex` does not input it yet, so **Waring's problem is in no printed volume until Volume 14 is rewritten**. The thread that owns Volume 14 wires it in as Chapter 6. Figures `ch06-ratio`, `ch06-circle` renamed `hr-ratio`, `hr-circle`. `docs/SERIES-STRUCTURE.md` and the citation map carry the new numbering.

**Chapter 12.** New: Lemma `lem:pdisc` (the partition product as a holomorphic function on the disc, which the old chapter assumed), Theorem `thm:eta` (η(−1/τ)=√(−iτ)·η(τ), proved from `thm:pentagonal`, `thm:poisson`, `thm:gaussianft`, `prop:ftbasic`, `thm:identity`), a table of p(n) against the formula, a closing section, one computation exercise (`ex:etacheck`). The citation of Volume 6 as a premise is gone. The reference to a "Problem Book" is gone. The remaining mentions of later volumes are previews (Volume 14 for the circle method and Kloosterman sums, Volume 6 for modular forms). Checks: `python3 review/volume5-rewrite/check_ch12_hardy_ramanujan.py` (η transformation at three points to 30 digits, every constant of the proof, the Rademacher partial sums, the table, the congruences, the exercises). The four mathematical risks of the blueprint: (1) branch of the square root, convergence and the passage to the half-plane are written out in the proof of `thm:eta`; (2) the chapter uses nothing from the Waring chapter; (3) the minor arc is y ≤ |x| ≤ 1/2, the whole rest of the circle; (4) is a Chapter 8 item.

**Chapter 1.** Worked first example, closing section, von Staudt part (a) now proved, citations of Volumes 1–2 corrected, sources merged. Two problems whose solutions need Chapter 2 (`pb:fixmoments`, `pb:necklacering`) moved to the end of Chapter 2. Check: `check_ch01_finite.py`.

**Chapter 2.** Opening example (paying 4 cents), closing section, all internal numbers turned into `\ref`, citations of Volumes 1–4 corrected. Solutions that leaned on later chapters are now self-contained or split: the die problem (`pb:diehit`) is solved with `thm:rational` instead of Cauchy's estimates; the arcsine series gets its end-point convergence from an elementary bound on the central binomial coefficient; the Catalan parity problem uses Legendre's formula (Volume 2, Chapter 1) instead of a Chapter 13 problem; the pole analysis of the zigzag numbers is a new exercise at the end of Chapter 9 (`pb:zigzagpole`); the large-n birthday asymptotic is a new exercise at the end of Chapter 11 (`pb:birthdaytriple`), with an elementary squeeze in place of dominated convergence. Check: `check_ch02_generating.py`.

**Chapter 3.** Closing section; the Bernoulli asymptotic now proves ζ(2k)→1 before using it; internal numbers turned into `\ref`; Volume 2 citations corrected (continued fractions are its Chapter 9); Tonelli in Ritelli's exercise is worded "Admitted here, proved in Volume 7, Theorem 9.5". The last exercise (`pb:levy`, growth of continued fraction denominators) used the Gauss–Kuzmin exercise of Chapter 10 as a premise, so it moved to the end of Chapter 10, with the attribution corrected to Khinchin 1935 and Lévy 1936. Check: `check_ch03_series.py`.

**Chapter 4.** The trick shown on one integral before the theory; closing section; labels; Volume 1 and 4 citations corrected. Proof repairs: the Borwein theorem no longer says "by dominated convergence" for a discontinuous limit (explicit two-step estimate instead); the tiling problem proves additivity of the double integral by a common grid; Sondow's part (b) has a real remainder estimate; Tonelli in Sondow's part (a) is worded as admitted (Volume 7, Theorem 9.5); Euler's constant is cited from Volume 1, not from the later asymptotics chapter. Plan item done: new three-star exercise `ex:fresnel` (Fresnel integrals by a parameter), appended last. Check: `check_ch04_integrals.py` (includes the hexadecimal digits of π at position 10^6 and the exact Borwein fraction).

**Chapter 5.** Proofs re-read and found sound (the chapter follows Artin: Bohr–Mollerup does the work, no double integral). Closing section added, which answers the opening question about (1/2)!. Internal numbers turned into `\ref`; Volume 1 citations corrected (Stirling's formula is its Chapter 9, the weighted AM–GM its Chapter 10, the product of sines its Chapter 6). The remark on the usual double-integral proof of the Beta formula now says plainly that this volume does not have Fubini–Tonelli or the change of variables, and does not use them. The ball volume keeps slicing as the definition of V_n. The sophomore's dream solution justifies term-by-term integration by uniform convergence (|x log x| ≤ 1/e) instead of an appeal to dominated convergence. Sources added for the exercises (Fulton–Harris, Nair, Dalzell, Lucas, Borwein–Bailey–Girgensohn). Check: `check_ch05_gamma.py` (includes a brute-force count of factorisations of an n-cycle for n ≤ 7).

**Chapter 6.** Opening experiment (the partial sums of Σ sin n / n on a calculator), closing section. Proofs re-read; one real repair: the paragraph "the Gibbs phenomenon is universal" subtracted a square wave, which has two jumps per period; it now subtracts the sawtooth (one jump), and proves that the sawtooth overshoots by the same proportion 0.0895. The stale line "Chapter 5 estimates the Weyl sums" (old Waring chapter) is now a preview of Volume 14. The Siegel exercise integrates over a convex set in R^n, which this volume has not defined: the exercise now says what is admitted (Volume 7 constructs the integral). Fejér was twenty, not nineteen, in 1900. Volume 1 and 4 citations corrected; self-citations "Volume 5, Chapter 8" removed. Sources added for the epigraph, Fejér, Carleson, Kahane–Katznelson, Rudin, flat Littlewood polynomials, Mauduit–Rivat, Siegel. Basel count checked: Chapter 3 announces six proofs (Volume 1, two in Chapter 3, two here, one in Chapter 9), and the labels "fourth and fifth" here and "sixth" in Chapter 9 agree. Check: `check_ch06_fourier.py`.

**Chapter 7.** Worked transform of (1,2,3,4) before the inversion theorem; closing section. Repairs: the aliasing proposition now assumes f continuous (it needs f equal to its series) and the sentence "a numerical calculation showed this error" (a leftover from the notebooks) is replaced by a proved bound π²C/n² when |c_m| ≤ C/m²; the number-theoretic transform says why n is invertible modulo p; the claim that all four eigenvalues of the normalised transform occur "once n ≥ 4" was false for n = 4 (eigenvalues 1, 1, −1, −i) and now says n ≥ 5. Stale citations of Volumes 1–3 corrected, self-citations "Volume 5, Chapter 9" replaced by labels. Plan item done: new three-star exercise `ex:uncertainty` (Donoho–Stark uncertainty principle on Z/n, with the sparse-recovery corollary), appended last. Sources added (Strang for the epigraph, Karatsuba–Ofman, Schönhage–Strassen, Chung–Diaconis–Graham, Newman, Rothaus, Donoho–Stark, Tao). Check: `check_ch07_fft.py` (every number of the modulo-17 example, the primes, operation counts of the FFT, and the exercises by brute force).

## Rules found on the way (keep them)

- **Numbering inside a chapter is preserved.** Volumes 6–15 cite Volume 5 by hand-typed numbers (for example "Volume 5, Theorem 2.12", "Volume 5, Exercise 2.3"). Their migration stays a pure chapter shift only if no numbered statement or exercise is inserted or removed in the middle of a chapter. New exercises go at the END of the exercise list (and their hints and solutions at the end of those sections). An exercise that needs a later chapter keeps its place and number, loses the forward part, and the forward part becomes a new exercise at the end of the later chapter.
- **Citations of Volumes 1–4 are by chapter and topic, not by statement number**, checked against the printed order: Volume 1: 1 Language, 2 Sums, 3 Counting, 4 Sequences and series, 5 Orders, 6 Complex numbers, 7 Polynomials, 8 Linear algebra, 9 Calculus, 10 Inequalities, 11 Probability. Volume 2: 1 Divisibility, 2 Primes, 3 Congruences, 4 Arithmetic functions (Möbius), 5 Primitive roots (cyclotomic polynomials), 6 Quadratic reciprocity, 7 Sums of squares, 8 Diophantine, 9 Continued fractions, 10 Gaussian and Eisenstein, 11 Characters. Volume 3: 1 Groups, 2 Quotients, 3 Actions, 4 Symmetric group, 5 Sylow, 6 Rings, 7 Modules, 8 Extensions, 9 Finite fields, 10 Galois, 11 Representations, 12 Quaternions, 13–16 linear algebra and combinatorics. Volume 4: 1 Counting, 2 Random variables, 3 Generating functions, 4 Concentration, 5 Continuous, 6 CLT, 7 Entropy, 8 Walks, 9 Markov, 10 Poisson, 11 Martingales, 12 Brownian, 13 Method, 14 Graphs, 15 Extremal. Many old citations in Volume 5 were written in file numbering and are off by one or more.
- Scratch build: three `xelatex` passes are not needed while editing; two give stable references.

## Plan items still open, by chapter

- **Ch. 9.** One new exercise of the hardest level (Chapter 4 has `ex:fresnel`, Chapter 7 has `ex:uncertainty`; Chapter 9 already received `pb:zigzagpole`, two stars, and still needs a three-star one).
- **Ch. 8.** Jacobi's theta becomes ϑ, with a sentence fixing the letter at first use. State the class of functions of the inversion theorem (`thm:ftinversion`) and check it is the class Chapter 12 and Volume 6 use (risk 4). "Chapter~12 follows him" is a stale number.
- **Ch. 9.** One sentence saying which complex analysis this chapter owns and which Volume 8, Chapter 14 owns. The line about the homology form of Cauchy's theorem says "proved in Volume 8": check against Volume 7, Chapter 6 (Jordan) and Volume 8.
- **Ch. 10.** Completed zeta is ξ, not Λ (master plan 4.5). A sentence fixing the letter. The unproved claim about smooth cutoffs of Σn: prove it or remove it. Numerical zeros of ζ: stated as computations with a source.
- **Ch. 13.** Legendre's modulus function must not use Λ. The closing problems each state the chapters they use; their hand-typed numbers ("Theorem~12.3", "Exercise~7.7", "Volume~5") are in the old numbering. Problems citing Volume 13, Exercise 8.5 or Volume 6 as tools break rule R1 (a solution is a proof): rework or move.
- **All.** About 460 hand-typed internal references to convert to `\ref`.
- **Other volumes.** Citations of Volume 5 by chapter number in Volumes 6–15 are now off (table in the citation map). This thread does not edit other volumes.
- **Ledgers.** `docs/plan/ledgers/` does not exist yet (Phase 0 of the master plan). The per-chapter check scripts are the trace for numerical claims until it does.

## How to build

`xelatex` three passes in `volume5-calculation/` as `build.sh` does, or `./build.sh --pdf-only volume5-calculation`. The cloud container has no TeX by default: install the packages listed in `.github/workflows/build.yml`.
