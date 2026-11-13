# Volume 5 rewrite, second pass

*Calculation: From Formula to Insight.* Branch `cursor/volume5-complete-rewrite-a791`. This note is the contract for the sentence-by-sentence rewrite. It does not change Volumes 1–4, Volume 6, or Volumes 11–15.

The manuscript on `main` already follows the master plan on `claude/project-thread-khh5pi` (PR #157, read only, not merged and not edited). Thirteen chapters, three parts. Hardy–Ramanujan is Chapter 12, with `thm:eta` proved here. Waring is not in this volume. The BBP series stays inside Chapter 4. The independent re-read of 13 November 2026 scored the book 8, and the in-volume slips V5-4 through V5-20 are already repaired on `main`. This pass rewrites the prose, adds figures, exercises and portraits, and must not undo those repairs or move a numbered statement.

## Voice, taken from Volumes 1–4

The reader is a serious beginner with a pencil. The writer is a friend who loves the subject. Volumes 1–4 do this in a fixed shape.

- A chapter opens with a centred italic of two lines: a question, or one surprising number. The first paragraphs then give a dated fact and a count you can check, and name the job of the chapter. They do not announce an outline.
- A `think` box asks for a guess. The next page answers it with a calculation.
- A definition is followed by one check with a small integer. A long proof is cut into italic stages. After a formula, one sentence says what it buys.
- “You” means the reader should compute. “We” means the argument is shared. Sentences are short. One idea each, when a step is being taught.
- A historical aside is one paragraph: who, which year, which paper or book, and why it matters here. No invented quotation, no biography.
- The close of a chapter says what was proved and the one question the next chapter answers.
- Exercises are graded ★, ★★, ★★★. Each has a hint and a solution. The solution begins with `\idea` (“How to find it”) and then `\writeup`.
- The order-and-chance thread is a sentence, not a slogan. A closed form is order. An error term, a sign we did not expect, or a sum that behaves like a random model is the other half. Plant it; do not lecture it.
- Words that do not teach are out: “in this section we will”, “it is important to note”, “delve”, “robust”, “comprehensive”, “landscape”, “journey”, “pivotal”, “tapestry”, “unlock”.

A sentence stays only when it is already the shortest correct way to say a formula, a hypothesis, or a definition. Everything else is rewritten.

## What must not move

Later volumes cite Volume 5 by printed numbers. `docs/plan/volume-citation-map.md` and the ownership table in `MASTER-PLAN-V5-V15.md` (decision D-10, D-11, section 4.3) fix the homes:

| Result | Home |
| --- | --- |
| Pentagonal-number theorem | Chapter 2, used by Chapter 12 |
| Poisson summation and the sign of the Gauss sum | Chapter 8 |
| Functional equation of \(\zeta\), label `thm:functional`, completed function \(\xi\) | Chapter 10 |
| Transformation of \(\eta\), label `thm:eta` | Chapter 12 |
| Hardy–Ramanujan asymptotic | Chapter 12 |
| Waring | Volume 14, not this book |

Rules for the source:

- Do not add, remove, or reorder a numbered `theorem`, `proposition`, `lemma`, `corollary`, `definition`, or `example`. An example shares the statement counter. A new illustration of a statement uses `examplex` or ordinary prose.
- Do not rename a `\label`. Do not retarget a `\ref`.
- New exercises go at the end of the exercise list, with hint and solution at the end of those sections, before Sources. Old exercise numbers stay.
- Do not change a formula inside a numbered statement unless the formula is false. The repairs already on `main` stay: the \(\zeta(5)\) sentence is a 2026 preprint plus an Archive of Formal Proofs entry whose only oracle is interval approximation; independence is Volume 4, Chapter 2; \(e(t)=e^{2\pi it}\) is defined at its first use; \(\rho_0\approx 0.73025\); the \(H_{10}\) partial sum is \(2.928968253927\ldots\); the Newman sum below \(4^k\) is \(\frac23 N^{\log 3/\log 4}\); the log-convex integral is passed to the limit on compact pieces because both sides are non-negative.
- Jacobi’s theta is \(\vartheta\). The completed zeta is \(\xi\). \(\Lambda\) is not used for either. Legendre’s auxiliary function in the AGM chapter is \(W\).
- Citations of Volumes 1–4 stay by chapter and topic. Do not re-prove a result those volumes own. Volume 1: language is Chapter 0, sums 1, counting 2, sequences 3, orders 4, complex numbers 5, polynomials 6, linear algebra 7, calculus 8, inequalities 9, probability 10. Volume 2: divisibility 1, primes 2, congruences 3, arithmetic functions 4, primitive roots 5, quadratic reciprocity 6, sums of squares 7, Diophantine 8, continued fractions 9. Volume 4: counting 1, random variables 2, generating functions 3, concentration 4, continuous laws 5, the central limit theorem 6, walks 8.
- Forward references are previews, or a result labelled admitted. The admitted list in the preface stays: Tonelli (Volume 7, Theorem 9.5) in two exercises; the volume of a convex body (Volume 7, Theorem 7.11) in one exercise of Chapter 6; Fulton–Harris, Proposition 3.12, quoted in one exercise of Chapter 5; Mertens’s third theorem and a comparison with the prime-number theorem, both in the closing problems of Chapter 13. No theorem depends on them.
- Reader-facing text does not call the book a revision, and does not mention notebooks.
- Do not edit `kdp.md`’s ISBN. It is blank. Do not edit `common/cover-notes.json` or `about-the-cover.tex` (the cover generator owns them). Do not edit another volume. A continuity mistake found elsewhere is recorded in `docs/review/`, not patched.

## What this pass adds

Each chapter gains at least two new TikZ figures and at least four new exercises, except Chapters 2 and 13, which already carry the long problem lists and gain three exercises aimed at that chapter’s own method. Figures use the palette names `MidnightBlue` (charcoal), `BrickRed` (rust) and `BurntOrange` (coral). A figure file is only a `tikzpicture`, included by `\fig{name}`, and the caption states the takeaway. New figure files are named `chNN-rewrite-*.tex`.

Portraits, with credits in `volume5-calculation/photos/CREDITS.md`, are placed once each, beside the paragraph that needs the person:

| Chapter | Command stem | Why it is there |
| --- | --- | --- |
| 1 | `jbernoulli` | The 1713 boast about the tenth powers |
| 3 | `wallis`, then `euler` | The product, then \(\pi^2/6\) |
| 6 | `fourier` | The series on the circle |
| 8 | `poisson` | Poisson summation |
| 9 | `cauchy` | Cauchy’s theorem |
| 10 | `riemann` | The 1859 paper |
| 11 | `abel`, then `maclaurin` | Divergent series, then the Euler–Maclaurin formula |
| 12 | `ramanujan` | The partition asymptotic |
| 13 | `gauss`, then `jacobi` | The diary entry, then the elliptic integral |

The command is `\portrait{stem}{caption}`. Captions name the person, the dates, the artist or the photograph, and “Public domain.” Abel and Cauchy are the short files; the height cap is already in `main.tex`.

Chapters 9 and 12 are the ones the re-read found hard to follow. Their proofs keep every estimate and gain stage names and one numerical check that was only implied.

## Chapter jobs

The subtitle is a motion from a formula to what the formula means. Each chapter keeps that motion.

1. Finite calculus. \(1^5+\cdots+n^5\) by antidifferences, not by a memorised polynomial. Falling powers, summation by parts, Stirling numbers, Bernoulli numbers, Newton’s series.
2. Generating functions. A recurrence becomes a rational function. The pentagonal theorem is proved here and spent in Chapter 12.
3. Series and products. The sine product, \(\zeta(2k)\), Niven’s proof that \(\pi^2\) is irrational.
4. Integrals. Differentiation under the sign, with the justification on the page. Frullani, Dirichlet’s integral, the BBP series.
5. Gamma and Beta. Bohr–Mollerup picks the interpolation. The ball’s volume tends to zero.
6. Fourier series. Fejér, Parseval, Gibbs, Weyl’s criterion, the isoperimetric inequality.
7. The DFT and the FFT. Inversion, convolution, the operation count, a transform modulo a prime.
8. The Fourier transform. The Gaussian is its own transform. Poisson summation fixes the sign of the Gauss sum. The class of the inversion theorem stays written down, because Chapter 12 uses it.
9. Complex analysis for computing. Star-shaped Cauchy, residues, Rouché. Homology, Phragmén–Lindelöf and the Riemann mapping theorem stay in Volume 8, Chapter 14, and the chapter keeps saying so.
10. Zeta. Euler product, continuation, `thm:functional`, the trivial zeros, \(\zeta(-1)=-\frac1{12}\). The hypothesis is stated and not proved.
11. Asymptotics. Euler–Maclaurin with a remainder, Stirling’s series with the sign of the remainder, Laplace’s method, one complex saddle.
12. Hardy–Ramanujan. `thm:eta` on the half-plane, with the branch of \(\sqrt{-i\tau}\) the principal root of positive real part. The error proved is \(O(n^{-1/4})\), and the text keeps saying where the factor was lost. Rademacher’s series stays quoted.
13. The arithmetic–geometric mean. Digits double because of an elliptic integral. The closing problems of the volume stay, labelled as such.

The last page of Chapter 13 still opens the door to Volume 6, *Crossroads*, and the primes in bulk. It does not spoil the prime-number theorem.
