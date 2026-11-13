# Volume 6 rewrite plan

Volume 6 is *Crossroads: Arithmetic Meets Analysis* (`volume6-crossroads`). This pass rewrites every chapter in the voice of Volumes 1–4. The curriculum stays the one in `docs/plan/book-06.md` and `docs/SERIES-STRUCTURE.md`: twelve chapters, three parts, no new topic and no deleted theorem.

Branch: `cursor/volume6-complete-rewrite-5aa1`. One pull request, one commit per chapter. PR #157 is not merged and not edited. Volume 5 is not edited.

## Voice, from Volumes 1–4 and the style sheet

The reader is a serious beginner who has finished Volumes 1–5. The voice is a friend with a pencil, not a lecture and not a chatbot (`docs/WRITING-STYLE.md`, Sound human).

- Open on a picture or a small number, then the question. The epigraph stays a real quotation.
- One concrete case before the general statement. Name the object and the job in one plain sentence. Do not announce the outline.
- Short sentences. “You” when the reader should check a case. “We” when the argument is shared.
- Proofs keep every algebraic step. Connective sentences say why the step is there.
- A chapter ends by naming what was proved, by label, and the one question the next chapter answers.
- No “in this section we will”, no “it is important to note”, no “in conclusion”, no hollow intensifiers.
- First-edition copy: the book is not described as a revision. No notebooks.
- Humour only when it teaches. History only when the fact is checked, and the source sits in that chapter’s Sources list.

## Structure that does not move

| Part | Chapters |
| --- | --- |
| Counting Primes | 1 Mertens, 2 averages, 3 characters, 4 Dirichlet, 5 prime number theorem |
| Zeros and Explicit Formulas | 6 zeros, 7 explicit formula |
| Sieves and Randomness | 8 sieves, 9 Erdős–Kac, 10 random models, 11 exponential sums, 12 modular forms |

Numbered environments stay in their present order, so theorem numbers that Volumes 7–15 cite do not shift. New exercises go at the end of the exercise list, with hints and solutions after the existing ones. Existing `\label` names stay. Displayed formulas keep their constants, hypotheses, indices and signs. `\log` is natural, \(p\) is prime, \(\mathrm{Li}(x)=\int_2^x dt/\log t\).

The letter \(\tau\) is the divisor function in Chapter 2 and Ramanujan’s function in Chapter 12. Chapter 12 says so on the first page. The completed zeta is \(\xi\) (Volume 5, Theorem 10.8): \(\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac12+\frac12 s(s-1)I(s)\), entire, \(\xi(1-s)=\xi(s)\). Jacobi’s theta is \(\vartheta\). The Riemann–Siegel phase is \(\alpha\). Volume 5’s Fourier inversion (Chapter 8) needs a continuous integrable function whose transform is integrable. A jump is not in that class. Volume 6 does not use that theorem as a premise; if a remark mentions Poisson summation, it names the class. Chapter 12 cites the transformation of \(\eta\) as Volume 5, Theorem 12.4 (label `thm:eta` in `hardy-ramanujan.tex`). A parallel rewrite of Volume 5 may renumber that theorem. The citation is listed for a re-check when that pull request lands.

## What each chapter gains

Two new TikZ figures, in the series palette (charcoal `MidnightBlue`, coral `BurntOrange`), with a caption that states the takeaway. Four new exercises at the end, graded, each with a hint and a solution that teaches. One worked numerical check before the main theorem, recomputed rather than copied. One historical aside with a source. The known defects below are fixed in the same pass.

## Defects this pass still has to catch

Several items in `docs/review/volume6-independent-scored-read-2026-11-13-reread.md` are already repaired on `main` (the \(\tau\) warning, the Piltz quotation, the cotangent comparison, the \(\lambda>2\) restriction in the Chapter 10 narrative, the jacket’s conditional \(99.59\%\), the index entries for the fundamental domain and the congruence, the Volume 14 handoff, Rankin’s quotient \(19.5\), and the Gaussian-moment clause in Lemma 9.6). The rewrite must not undo them.

Still to check while rewriting:

- Chapter 7, proof of the error term: the displayed exponential must use \(\log(T+2)\), matching the sentence above it.
- Chapter 7: the passage from the \(\theta\)-race to the \(\pi\)-race, and the solution of the bias exercise, must not claim more than the identity proves.
- Chapter 10: the solution of the short-interval exercise must say the almost-sure asymptotic is proved for \(\lambda>2\) and is false for \(1<\lambda\le 2\).
- Chapter 12: the solution that uses \(\varphi(d)\ge\sqrt{d/2}\) must say the ratio is multiplicative, not only check prime powers.
- Chapter 1: the comparison of Mertens’s product with \(1/\log n\) waits for Chapter 5, and the discrepancy is about \(12.3\%\).

## Continuity this pass does not edit

Volumes 1–4 and 11–15 stay untouched, and so does Volume 5. Later volumes cite Volume 6 by hand-typed numbers (Theorem 1.3, 1.5, 4.1, 5.5, 6.9, 7.5, 7.8, 7.10, 7.11, 8.2, 8.4, 8.5, 9.1, 9.7, 10.1, 10.7, 11.11, 12.2, equation (8.1), and others). Those numbers are frozen. Volume 8’s expander chapter still cites Chapter 5 for an error term that Chapter 5 does not prove; the right pointer is Theorem 7.10. That sentence is listed here and is not edited.

Volume 5 citations inside Volume 6 are hand-typed (there is no cross-volume `\ref`). After the parallel Volume 5 rewrite, re-check every “Volume 5, Theorem/Proposition/Exercise/Corollary” in this book against the new chapter order, especially Theorem 10.8 (\(\xi\)), Theorem 12.4 (\(\eta\)), Proposition 10.6, Corollary 10.9, Theorems 9.15, 9.18, 9.26 and 9.36, and Exercises 5.7 and 6.5.
