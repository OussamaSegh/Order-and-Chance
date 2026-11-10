# Volume 4 successor review (Volumes 1–3)

**Date:** 10 November 2026.
**Reviewer:** the author's designated reviewer for this pass. Not an independent referee.
**Baseline:** `main` at `b5543de6f7484176471206f7558462cc24b245b2` (`docs(v4): record why drafts 113 and 114 are superseded`).
**Book:** Volume 4, *Chance — The Logic of Uncertainty*, as published on the rolling release tag `books`. Volumes 1–3 are the published predecessors. This file is a review and a list of proposals. It does not change any chapter, figure, or build file.

## Executive summary

Volume 4 is a genuine successor to Volumes 1–3, and it is the right predecessor for Volume 5. The preface's contract matches the citations in the proofs: high-school mathematics and Volume 1. No proof I opened cites a numbered theorem of Volume 2 or Volume 3. The promises Volume 1 makes about this book are kept in substance: one sample space for an infinite sequence of tosses, the Poisson limit for fixed points, a strong law under a fourth-moment hypothesis, the central limit theorem, the definition of covariance, and entropy as the uncertainty of a distribution. The last chapter names Volume 5, *Calculation: From Formula to Insight*, and hands it the generating function from Chapter 3.

I do not certify that every line is correct. I found no critical error: no theorem whose conclusion I could refute, and no numerical claim I recomputed that came out wrong. What I did find are gaps in write-ups that the book, by its own rules, is not allowed to leave open. The rules are the ones the preface states. A later volume is not a premise, and an interchange of sums, expectations, or limits has to be an argument already on the page.

Five places in Volume 4 need a repair. The product formula for moments of unbounded independent copies is used in the fourth-moment strong law and again in Lindeberg's proof, without a product theorem that covers unbounded quantiles. The \(L^2\) martingale theorem passes from a summable series of mean-square increments to the expectation of the infinite sum. The strong-Markov restart names bounded convergence and does not write it; the reflection principle then uses that restart in one sentence. Superposition restarts the surviving exponential clock at a random time, which is more than the fixed-time memorylessness proved earlier. The Bayer–Diaconis box can be read as the probability of the event "\(r\) rising sequences"; the formula, the proof, and the distance display are the probability of each such arrangement. In each case the mathematics aimed at is the standard theorem. The printed step does not yet earn it.

Three cross-volume pointers are wrong as navigation, not as mathematics. Two sentences in the published Volume 3 send the reader to Chapter 8 for Markov-chain coupling and for matrix powers of chains. Those arguments are in Chapter 9. Volume 12 calls nowhere-differentiability Theorem 12.10. It is Theorem 12.9. Proposition 12.10 is a different result.

**Verdict:** keep the book as the published successor, and repair the five write-ups inside the existing theorems. Do not renumber anything. Downstream volumes cite these numbers; a mechanical check of 454 numbered "Volume 4, …" citations found no missing number except the 12.10/12.9 mismatch.

| Severity | Count | Where |
| --- | ---: | --- |
| Critical | 0 | — |
| Major | 8 | five in Volume 4 (M1–M5); two in Volume 3 (R1–R2); one in Volume 12 (R3) |
| Minor | 14 | m1–m14, all either in Volume 4 or in a pointer at Volume 4 |

## How this review was done

Printed numbers below come from the source counters, not from a typeset PDF. I did not build the book. Theorem, proposition, lemma, corollary, definition, and example share one counter per chapter. Exercises have their own. `\chapter*` on the preface does not take a number. After `\appendix` and `\setcounter{chapter}{1}`, the extremal file is Appendix B. There is no Appendix A, and the file says so. `gilmer.tex` is not `\input` by `main.tex`.

Volume 1's printed chapters, from `volume1-first-principles/main.tex` with the counter set to \(-1\) before the language chapter, are: 0 language, 1 sums, 2 counting, 3 sequences and limits, 4 orders, 5 complex numbers, 6 polynomials, 7 linear algebra, 8 calculus and Taylor, 9 inequalities, 10 probability.

Every issue in the log was re-opened in the source for this report. A parallel reading of the chapters, exercises, and solutions supplied the first pass and the list of statements that survived it. Where that reading named a small gap and I did not re-open the lines, the item is in "Not logged", not in the table. I do not treat that parallel reading as a second signature on every exercise solution.

Numerical checks in this report were recomputed in Python for this pass. A numerical match is not a proof. Sources used for history and for the shape of a classical statement are named where a claim depends on them. I did not open Feller, Bayer–Diaconis 1992, or Galton's 1889 book.

## Issue log

| ID | Location | Category | Severity | Evidence | Proposed fix |
| --- | --- | --- | --- | --- | --- |
| M1 | `volume4-chance/chapters/ch06-clt.tex:105`–`108`, Theorem 6.4 `thm:slln4`; same gap at `:418`, Theorem 6.10 `thm:lindeberg` | gap | major | The fourth-moment expansion says that a term with a unique index has expectation zero, and that \(\mathbb E[Z_i^2 Z_j^2]=\sigma^4\), so \(\mathbb E[T_n^4]=n\mu_4+3n(n-1)\sigma^4\). The \(Z_i\) are quantile transforms and may be unbounded. Volume 1's product formula for independent variables is the finite or countable sum in the probability chapter. Chapter 5's Fubini (`prop:fubini`) is for a continuous integrand on a compact rectangle, and the text refuses to swap improper integrals on the strength of two iterated tails. The constant \(C\) in the Borel–Cantelli bound is this expansion. Lindeberg then says the linear terms have expectation 0 and the quadratic terms match because \(X_{n,k}\) and the Gaussian copy "are independent of \(A_{n,k}\)". That is the same product, now with a bounded smooth function of the other coordinates and a summand that is assumed only to have a finite variance. The pattern count \(3n(n-1)\) is the right one. The factorisation is not a theorem yet. | Before Theorem 6.4, prove an unnumbered product lemma: for functions of two independent uniform blocks, truncate to a large compact square, apply `prop:fubini` to continuous approximations, and pass to the limit with the fourth-moment (or second-moment) tail. Use it in both proofs. Do not insert a numbered theorem. Theorems 6.4 and 6.10 are cited downstream. |
| M2 | `volume4-chance/chapters/ch10-martingales.tex:275`–`286`, Theorem 11.12 `thm:L2conv` | gap | major | After \(\sum_j\mathbb E\|X_{n_{j+1}}-X_{n_j}\|\le\sum_j 2^{-2j}\), the proof says the series of absolute increments "has finite expectation, so it converges almost surely", then \(\|X_\infty-X_{n_j}\|\le\sum_{k\ge j}\|\Delta_k\|\), then the expectation of the right-hand side is at most the numerical tail, and a weighted Cauchy–Schwarz gives \(\mathbb E[(X_\infty-X_{n_j})^2]\to 0\). Finite additivity gives the expectation of a partial sum. The expectation of the infinite sum, and the comparison for the square, are monotone convergence for an unbounded limit of interval-simple functions. The book has not proved that. On the null set the proof sets \(X_\infty=0\), so the pointwise bound can fail there, and the square is not bounded. Theorem 11.13 quotes the square-mean limit to reach convergence in probability for Pólya's urn. The urn conclusion is the standard one. This step is the one that is not written. | Keep the almost-sure Cauchy argument, which is an outer-content argument and is in good shape. Bound \(\sum\|\Delta_k\|<\infty\) by Markov on the partial sums and countable subadditivity. Copy the truncation comparison already used in Theorem 11.14, and let the truncation rise with the \(L^2\) tail \(r_{n_j}\). Do not renumber. Volume 15 cites Theorem 11.12 as the finite-partition \(L^2\) theorem and correctly contrasts it with the general filtration in Volume 11. |
| M3 | `volume4-chance/chapters/ch11-brownian.tex:275`–`277`, Proposition 12.11 `prop:restart`; used at `:294`, Theorem 12.12 `thm:reflection` | gap | major | The identity at a dyadic time \(\tau_n\) is a finite sum of fixed-time independences, and that part is complete. The passage to \(\tau\) says the products are bounded, "so passing to expectations is justified by bounded convergence", and names a compact-box approximation with Gaussian tails. Proposition 12.10 writes that approximation out. Proposition 12.11 does not. Theorem 12.12 then says the future after the first hit "is a fresh Brownian motion, by restarting the dyadic construction", without citing Proposition 12.11, and equates the two sides of the reflection in one sentence. The displayed formula \(P(M_t\ge a)=2(1-\Phi(a/\sqrt t))\) is the classical one. The symmetry of the post-hit increment is the step that is only named. Exercise 12.3 and Volume 12's citations of Theorem 12.12 depend on it. | Write the \(\varepsilon\) argument in Proposition 12.11 the way Proposition 12.10 does, for a bounded continuous function of finitely many stopped coordinates. In Theorem 12.12, cite Proposition 12.11 and record that, on \(\{\tau_a\le t\}\), the increment \(B_t-a\) is symmetric. Do not renumber. |
| M4 | `volume4-chance/chapters/ch08-markov.tex:277`–`281`, Theorem 9.9 `thm:bayerdiaconis`; the correct use is at `:296` | math error | major | The box says an \(a\)-shuffle "produces an arrangement with \(r\) rising sequences with probability" \(Q_a=a^{-n}\binom{a+n-r}{n}\). Read as the probability of one fixed arrangement, this is the classical Bayer–Diaconis formula, and the proof counts words for a given \(\sigma\). Read as the probability of the event "the arrangement has \(r\) rising sequences", it is false. For \(n=3\), \(a=2\), \(r=2\), \(Q_2=1/8\), while four of the six permutations have two rising sequences, so the event has probability \(1/2\). The distance \(d_k\) multiplies by \(A(n,r)\) and is the per-permutation reading. The decimals in the text match a direct recomputation (below). The box is the sentence a later volume will quote. | Replace the opening sentence with: each arrangement with \(r\) rising sequences has probability \(Q_a\). Leave the formula and the number 9.9 unchanged. Volume 15 cites Theorem 9.9 for the formula \(Q_a\). |
| M5 | `volume4-chance/chapters/ch09-poisson.tex:115`, Theorem 10.8 `thm:superpose` | gap | major | The first merged gap is the minimum of two independent exponentials. Its survival \(e^{-(\lambda+\mu)t}\) is a product and is proved. The later gaps need the surviving clock's residual, after a random ring time, to be a fresh exponential of its own rate, independent of who rang and of that time. Proposition 10.1 is memorylessness at a fixed time \(s\). The race, which is the right computation, is Proposition 10.11 and comes later. The second paragraph of the proof, reading the colouring lemma backwards, identifies one merged count with a sum of Poissons. It does not by itself show that the gap construction in Definition 10.3 has been met. | Inside this proof, compute the joint law of the ring time, the identity of the winner, and the survivor's residual, by iterating the exponential densities. Do not move Proposition 10.11 in front of Theorem 10.8: that would renumber 10.8 through 10.11. No downstream sentence cites those four numbers; the constraint is still to leave them alone, because later drafts may. |
| R1 | `volume3-symmetry/chapters/ch07-modules.tex:920` | reference | major | "Volume 4, Chapter 8, applies matrix powers to finite Markov chains." Chapter 8 is the walk chapter (`ch07-walks.tex`): reflection, ruin, Pólya, arcsine, electrical networks. Finite transition matrices, stationary laws, and convergence of \(P^k\) are Chapter 9 (`ch08-markov.tex`), Theorems 9.2 and 9.4. The sentence is a forward pointer, not a premise of Volume 3. | In a later correction to Volume 3, change Chapter 8 to Chapter 9. Do not renumber Volume 4 to make the old sentence true. |
| R2 | `volume3-symmetry/chapters/linear-ch07-perron.tex:784` | reference | major | "Volume 4, Chapter 8 returns to convergence by coupling: it compares two chains directly." Coupling, total variation, and convergence to the stationary law are Lemma 9.3 and Theorem 9.4. Chapter 8 does not run that argument. Again a forward pointer, not a premise. | Same correction: Chapter 9. |
| R3 | `volume12-random-motion/chapters/ch01-gaussian.tex:42` | reference | major | The reminder says Brownian motion "is nowhere differentiable (Volume 4, Theorem 12.10)". Nowhere-differentiability is Theorem 12.9, `thm:pwz`, in `ch11-brownian.tex:215`. Theorem 12.10 is not a theorem. The tenth numbered result in Chapter 12 is Proposition 12.10, `prop:bmmart`, the finite-observation martingale identity. | In Volume 12, cite Theorem 12.9. Do not insert a dummy result in Volume 4 to make 12.10 the differentiability theorem. |
| m1 | `volume4-chance/chapters/ch07-walks.tex:241`, Theorem 8.5 `thm:polya` | gap | minor | The balls of radius \(\sqrt 2\) about the origin and about a corner of \([-\pi,\pi]^d\) are separated by appealing to \(\pi>3\), hence \(\pi\sqrt 3>3\sqrt 3\) and \(27>8\). Volume 1, Proposition `prop:sincmp` in the sequences chapter, gives \(0<\sin x<x\) on \((0,\pi/2]\) and \(\sin(\pi/2)=1\), so \(\pi>2\). Then \(\pi\sqrt 3>2\sqrt 3\) and \((2\sqrt 3)^2=12>8=(2\sqrt 2)^2\). The balls are disjoint. The number \(\pi>3\) is not proved or cited. | Replace \(\pi>3\) by the proved bound \(\pi>2\), and compare with \(2\sqrt 3\). |
| m2 | `volume4-chance/chapters/ch07-walks.tex:110`, Proposition 8.3 `prop:duration` | gap | minor | From \(\mathbb E[g(S_{\tau_n})+\tau_n]=g(k)\) and \(\mathbb E[g(S_{\tau_n})]\to 0\) one gets \(\mathbb E[\tau_n]\to g(k)\). The proof writes \(\mathbb E[\tau]=g(k)\). For a nonnegative integer-valued time, \(\mathbb E[\tau]=\lim_n\mathbb E[\min(\tau,n)]\) is the tail sum Volume 1 already uses for a geometric wait. It is not cited here. The same omission is the natural reading of the exit-time solution later in the chapter. The closed forms match the one-step system, including the text's check at \(p=2/3\), \(N=3\). | Cite the tail sum, and write \(\mathbb E[\tau_n]\to g(k)\). |
| m3 | `volume4-chance/chapters/ch05-continuous.tex:509`, solution of Exercise 5.7 `ex:cantor` | math error | minor | "Either way only one sequence of bits, or two, realises \(x\)." Endpoints of the Cantor set have two ternary expansions, but the second expansion uses a digit \(1\). The series \(X=\sum 2B_k 3^{-k}\) only produces digits \(0\) and \(2\), and a base-3 expansion in that digit set is unique. So each \(x\) has at most one bit-string preimage. \(P(X=x)=0\) still follows from one cylinder of length \(2^{-N}\). | Say each \(x\in C\) has exactly one expansion in the digits \(\{0,2\}\), hence exactly one bit string. |
| m4 | `volume4-chance/chapters/ch04-inequalities.tex:181`, Theorem 4.4 `thm:bc` (b) | gap | minor | "The complements of a finite subcollection obey the same product." Volume 1, Chapter 10, defines mutual independence by the product formula for the events, not for their complements. For events that are finite unions of intervals, finite additivity gives \(P(A^c\cap B)=P(B)-P(A\cap B)\), and induction extends it. That induction is not on the page. The bound \(1-x\le e^{-x}\) is then applied correctly. | Add the induction before the exponential bound. |
| m5 | `volume4-chance/chapters/ch06-clt.tex:267`, Theorem 6.8 `thm:inversion` | reference | minor | "The Gaussian integral \(I(0)=\sqrt{2\pi}\) is the one from Volume 1." Volume 1, Chapter 8, Proposition `prop:gaussianintegral`, states \(\int_0^\infty e^{-x^2}\,\mathrm dx=\sqrt\pi/2\). The full-line integral \(\int_{-\infty}^{\infty}e^{-t^2/2}\,\mathrm dt=\sqrt{2\pi}\) is that result after \(t=\sqrt 2\, x\). Chapter 5 already records the scaled integral for the normal density. The constant in the next line is the right one: \(\sqrt{2\pi}/(2\pi)=1/\sqrt{2\pi}\). | Cite Chapter 5's scaled integral, or write the substitution. |
| m6 | `volume4-chance/chapters/ch06-clt.tex:570`, Theorem 6.14 `thm:gaussvec` (b) | math error | minor | "Any covariance satisfies \(t^{\mathsf T}\Sigma t=\mathbb E[(t\cdot X)^2]\ge 0\)." For a centred vector this is the variance. For a general vector the quadratic form is \(\mathrm{Var}(t\cdot X)=\mathbb E[(t\cdot(X-\mathbb EX))^2]\). A constant \(1\) has covariance \(0\) and \(\mathbb E[(tX)^2]=t^2\). Part (a) builds centred vectors, and part (b) is stated for a centred Gaussian vector, so the theorem box is right. The word "any" is not. | Write the identity for a centred vector. |
| m7 | `volume4-chance/chapters/ch10-martingales.tex:180` | prerequisite | minor | "Conditional Jensen on each atom" produces the submartingales \(\|X_k\|\) and \(X_k^2\). On a finite partition the conditional law on an atom, given the next partition, is a finite convex combination of the child values. That is Volume 1's Jensen, from the inequalities chapter, applied to those weights. The name is used without a pointer. The inequality is the right one for \(\|x\|\) and \(x^2\). Volume 1's beauty note also says that in Volume 4, Jensen reads \(f(\mathbb E[X])\le\mathbb E[f(X)]\). The expectation form is never stated. | One sentence: on each atom this is Volume 1's Jensen for a finite convex combination. That also keeps the forward pointer. |
| m8 | Volume 1, `volume1-first-principles/chapters/ch04-inequalities.tex:516`; absent from Volume 4 | gap | minor | Volume 1 says Volume 4 defines \(\operatorname{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]\), "and the same sign computation shows the covariance is nonnegative when \(X\) and \(Y\) are increasing functions of one variable." Volume 4, Chapter 2, lines 61–64, defines covariance exactly that way. The sign computation for increasing functions of one variable is not in Volume 4. I searched the volume for it. | After the definition in Chapter 2, add the short argument: if \(f\) and \(g\) are increasing and \(X\) is real, then \((f(x)-f(y))(g(x)-g(y))\ge 0\), and the expectation of that product is twice the covariance. Unnumbered. About half a page of source. No downstream number moves. |
| m9 | `volume4-chance/blurb.tex:1` against `volume4-chance/chapters/preface.tex:26` | style | minor | The preface says the prerequisites for the proofs are high-school mathematics and Volume 1, and that no proof cites a theorem from Volume 2 or Volume 3. The blurb says every step used in a proof is proved in this volume or in Volumes 1–3. The blurb is not false, because Volume 1 is among them. It still groups Volumes 2 and 3 as possible sources of a proof step, which is the claim the preface withdrew. | In the blurb, name Volume 1. Jacket copy is reader-facing; this is a one-line change, not a new mathematical claim. |
| m10 | `volume4-chance/chapters/ch01-counting.tex:104`; `volume4-chance/chapters/ch08-markov.tex:245` | reference | minor | Both cite "Volume 1, Chapter 9" for \(1-x\le e^{-x}\) or \(1-1/n\le e^{-1/n}\). Chapter 9 is the inequalities chapter. Its convexity proposition says a function with positive second derivative lies strictly above its tangents. The sentence \(1-x\le e^{-x}\), as the tangent to \(e^{-x}\) at \(0\), is written in Volume 1, Chapter 10 (`ch09-probability.tex:55`), and it cites that proposition. The inequality is true, and the uses of it are correct. | Cite Chapter 10, where the inequality is written, or add the one-line tangent in the Chapter 9 sentence being cited. |
| m11 | `volume4-chance/chapters/ch02-discrete.tex:89`, Theorem 2.1 `thm:poissonlimit` | reference | minor | "Volume 1, Chapter 3, says this tends to \(\ln'(1)=1\)." Chapter 3 defines the derivative as a difference quotient and treats \(\ln'(x)=1/x\) as known. The derivation from the inverse-function rule is in Chapter 8, the calculus chapter. The limit \(\ln(1-x)/x\to -1\) is the right one once the derivative is known. | Cite Chapter 8 for the value of the derivative. |
| m12 | `volume4-chance/chapters/ch09-poisson.tex:42`, before Theorem 10.4 `thm:uniform` | gap | minor | The paragraph cites Theorem 10.4 for \(\sum_n P(N(t)=n)=1\) before that theorem is stated, and says Theorem 6.4 applies to the exponential gaps because \(E=-\ln(1-U)/\lambda\). Theorem 6.4 asks for copies "in the sense of" the inverse-distribution proposition. That proposition's proved case is a distribution function that is continuous and strictly increasing, with limits \(0\) and \(1\) at \(\pm\infty\). The exponential law is flat on \((-\infty,0]\). The fourth moment \(24/\lambda^4\) does follow from the integration by parts in the same paragraph (\(m_k=k!/\lambda^k\)). The paragraph itself says the finiteness of \(N(t)\) does not use the strong law. | Move the finiteness sentence to after the proof of Theorem 10.4. Delete the claim that Theorem 6.4 applies, unless the inverse-distribution proposition is extended to this quantile first. |
| m13 | `volume4-chance/chapters/ch10-martingales.tex:346`–`348`, Theorem 11.14 `thm:asconv` | math error | minor | "At every point of \([0,1)\), \(Z_n-\varepsilon-M\mathbf 1_{O_N}\le Z\le Z_n+\varepsilon+M\mathbf 1_{O_N}\)." On the set where \(X_n\) diverges, the proof sets \(X_\infty=0\), so \(Z=\min(\|X_\infty\|,M)=0\). For \(\sum\varepsilon_n/n\) with every sign positive, the partial sums diverge, but the truncated \(Z_n=\min(\|X_n\|,M)\) is eventually the constant \(M\), so the point lies outside \(O_N\) for large \(N\). Then \(M-\varepsilon\le 0\) fails when \(\varepsilon<M\). A single binary point has outer content zero, and the length-based integral of a bounded function does not see it. The sentence "at every point", which the next line uses to trap the integral of \(Z\), is false. | Claim the sandwich off the exceptional set. Integrate the comparisons, which are constant on interval pieces. |
| m14 | `volume12-random-motion/chapters/ch01-gaussian.tex:39`–`41` | reference | minor | The reminder attributes to Theorem 6.14 the definition "every linear form is Gaussian", the characteristic function \(e^{i\langle u,m\rangle-u^{\mathsf T}\Sigma u/2}\) with a mean, and the claim that \(AX+b\) is Gaussian. Theorem 6.14(a) is the centred law of \(X=AZ\), with characteristic function \(\exp(-\tfrac12 t^{\mathsf T}\Sigma t)\). Part (b) is the centred positive-semidefinite characterisation. The centred facts Volume 12 uses at line 85, positive-semidefiniteness, do match part (b), up to the slip in m6. The mean term is not in the theorem. | Add one sentence to Theorem 6.14(a): if \(b\) is a constant vector then \(AZ+b\) has characteristic function \(\exp(it\cdot b-\tfrac12 t^{\mathsf T}\Sigma t)\). That does not change the number 6.14. Then point the Volume 12 reminder at that sentence. |

## Continuity with Volumes 1–3

### What Volume 1 asks Volume 4 to do

| Promise in Volume 1 | Where Volume 4 delivers it |
| --- | --- |
| One probability space for an infinite sequence of trials (`ch09-probability.tex:24`, `:463`) | Chapter 1, Definition 1.1 and Propositions 1.2–1.4: binary digits of a uniform point of \([0,1)\), outer content, countable subadditivity |
| Fixed-point counts converge in law to Poisson (`ch09-probability.tex:236`, `:460`) | Proposition 2.3 `prop:fixedpoisson` |
| A strong law under a fourth-moment hypothesis, and the central limit theorem (`ch09-probability.tex:409`, `:477`) | Theorem 6.4 and Corollary 6.11. The fourth-moment write-up is M1. The classical CLT statement is the right one. |
| The normal approximation behind the newspaper poll of about \(1070\) people (`ch09-probability.tex:796`) | The approximation is Corollary 6.11. Volume 4 does not recompute the figure \(1070\). It does not have to: Volume 1 presents that figure as a reading of the approximation, not as a theorem. |
| \(\operatorname{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]\), and the sign for increasing functions of one variable | The definition is Chapter 2, lines 61–64. The sign argument is m8. |
| Jensen in the form \(f(\mathbb E[X])\le\mathbb E[f(X)]\), and Cauchy–Schwarz for a covariance | Cauchy–Schwarz is used, with a citation of Volume 1, Chapter 9, in the probabilistic-method chapter. The expectation form of Jensen is m7. |
| Entropy of a probability distribution: the uniform law is the most unpredictable (`ch04-inequalities.tex:771`) | Proposition 7.1 `prop:gibbs` |
| Absolute convergence when an expectation is an infinite sum (`ch05-sequences-series.tex:1094`) | Chapter 2 separates nonnegative and absolutely summable expectations. I did not re-audit every series interchange in Volume 1. |
| The Gaussian integral becomes the law of a sum of many small independent pieces (`ch06-integrals-taylor.tex:606`, `:697`) | The normal density is Chapter 5; the sum is Corollary 6.11. The constant \(\sqrt{2\pi}\) is Stirling's constant from Volume 1, used in the local theorem. |
| Even moments of \(e^{-x^2}/\sqrt\pi\) "which Volume 4 needs" (`ch06-integrals-taylor.tex:683`) | Volume 4 needs the Gaussian integral and the fourth moment \(3\sigma^4\). It derives the fourth moment by two integrations by parts from \(\phi'(x)=-x\phi(x)\), in the Lindeberg proof. It does not cite the general even-moment formula. The pointer is a little wider than the use. Not logged as an error. |

Volume 2 does not mention Volume 4. That matches the preface: no proof needs a theorem from the integers book. Primes are not a step. The last chapter says the primes are not among the shapes this book has used, and leaves them to later volumes. That is the right handoff.

Volume 3's preface, afterword, and the leads in the group and character chapters point at Volume 4 for a random change of viewpoint, for mixing, and for the random-transposition transition near \(\tfrac12 n\log n\). The transition is discussed in Chapter 9 (Proposition 9.11 gives the untouched-card lower bound) and is not proved as a cutoff theorem. Volume 3 says the cutoff is discussed in Volume 4 and proved in Volume 11. That division is accurate. The two wrong chapter numbers are R1 and R2.

### Tools taken from Volume 1, and where they actually are

These are the citations I opened on both sides. "Gives" means the cited chapter contains a proved form strong enough for the step, or a one-line corollary of a proposition in that chapter.

| Tool as used in Volume 4 | Printed Volume 1 home | Match |
| --- | --- | --- |
| Finite probability, conditional probability, Bayes, pairwise against mutual independence, linearity, indicators | Chapter 10, probability | Yes. Chapter 1 cites it and does not re-prove it. |
| Chebyshev, and the weak law for pairwise i.i.d. variables with a finite variance | Chapter 10 | Yes. Chapter 4 cites them and then proves Hoeffding, Kolmogorov, Borel–Cantelli, and a bounded strong law. |
| Poisson masses, mean, and variance; \(\mathbb E[F_n]=1\); the derangement error \(\le 1/(n+1)!\) | Chapter 10, with the series for \(e^{-1}\) | Yes. The Poisson *limit* of the binomial is Theorem 2.1, new here. |
| Derangement formula \(D_r/r!=\sum_{j=0}^r(-1)^j/j!\) | Chapter 2, counting | Yes. |
| Geometric tail sum \(\mathbb E[G]=\sum_{j\ge 0}P(G>j)\) | Chapter 10 | Yes. Used for the coupon collector. |
| Integral test for \(H_n\), derivative as a difference quotient, ratio test, \(q^n\to 0\), Bolzano–Weierstrass in \(\mathbb R\) | Chapter 3 | The integral test and Bolzano–Weierstrass are used correctly in the coupon collector and in Pólya's Fourier bound. The value \(\ln'(1)=1\) is m11. |
| Taylor with integral remainder, Taylor–Lagrange, \(\ln(1+u)\le u\) for \(u\ge 0\), the series for \(e\), \(\int_0^\infty e^{-x^2}\,\mathrm dx=\sqrt\pi/2\), Stirling \(n!\sim\sqrt{2\pi n}(n/e)^n\) | Chapter 8 | Yes, at the strength the local theorem, Hoeffding's lemma, the local lemma, and the Gaussian tail use. The full-line normal integral is m5. |
| Convexity and the tangent test; Cauchy–Schwarz for finite sums | Chapter 9 | Cauchy–Schwarz is cited correctly in Chapter 13. The exponential inequality is m10. |
| Spectral theorem for a real symmetric matrix, Gram–Schmidt, nonnegative eigenvalues for a positive-semidefinite matrix | Chapter 7 | Yes. Theorem 6.14 says so at the first use. The covariance identity in the proof is m6. |

I did not find a notion used in a proof before it is taught in Volume 1 or earlier in Volume 4, except the places logged as M1–M5, where the missing piece is an interchange, a restart, or a sentence that can be read two ways. Characteristic functions, outer content, the inverse distribution function, and conditional expectation on a finite partition are built before they are used. Lévy's continuity theorem, Tonelli's theorem for general nonnegative integrands, and the Itô integral are named as belonging to Volumes 11, 7, and 12, and the proofs I opened do not call them as lemmas. That restraint is real, and it is why M1–M3 matter: they are the places the restraint slips.

### Repeated material

Chapter 1 recalls the finite rules and cites Volume 1 instead of proving them again. The three-event inclusion–exclusion is one illustration of linearity, not a second development of the counting formula. Chapter 2 recalls the Poisson masses and then proves the limit, which Volume 1 did not prove. Generating functions in Chapter 3 are the probability form; Volume 5 is where the analytic remainder belongs, and the last chapter says that. I would not cut these recalls. A reader who finished Volume 1 a volume ago needs the sentence that names \(\Omega\) before the fraction.

### What later volumes require, and what a repair must not break

I extracted every citation of the form "Volume 4" followed by Theorem, Proposition, Lemma, Corollary, Definition, or Exercise and a number, in Volumes 1–3 and 5–15. There were 454 such matches. Against the source counters, the only failures were R3 (Theorem 12.10, which is Proposition 12.10, and the sentence wants Theorem 12.9) and m14 (the mean in the characteristic function). In particular, the numbers that later books actually lean on are the ones in the manuscript:

| Cited as | What it is |
| --- | --- |
| Theorem 2.1 | Poisson limit of binomial laws |
| Theorem 4.2 | Hoeffding |
| Theorem 4.4 | Borel–Cantelli |
| Theorem 4.6 | Weierstrass via Bernstein |
| Theorem 5.12 | Buffon's needle |
| Theorem 6.8 | Fourier inversion |
| Theorem 6.10 | Lindeberg |
| Theorem 6.14 | Gaussian vectors, centred case |
| Exercise 6.1 | Slutsky |
| Theorem 8.1 | walk reflection |
| Theorem 8.6 | discrete arcsine (last visit) |
| Theorem 8.8 | arcsine limit |
| Theorem 9.6 | strong stationary time, \(d(t)\le P(\tau>t)\) |
| Lemma 9.7 | total variation does not increase |
| Definition 9.8, Theorem 9.9, Propositions 9.10 and 9.11 | \(a\)-shuffle, \(Q_a\), riffle composition, untouched cards |
| Exercise 9.6, Exercise 9.8 | top-to-random; rising-sequence mean \((n+1)/2\) and variance \((n+1)/12\) |
| Lemma 10.5 | Poisson colouring |
| Definition 11.1, Theorems 11.4, 11.5, 11.9, 11.10, 11.12, 11.13 | conditional expectation, optional stopping, Doob, Azuma, \(L^2\) convergence, Pólya's urn |
| Definition 12.1, Theorems 12.4 and 12.12, Exercise 12.3 | Brownian motion, Lévy construction, reflection, zero set |
| Exercise 13.4 | crossing lemma, constant \(64\) |
| Theorem B.7 | van der Waerden |

Volume 5's return-probability example really does use the integral written in Chapter 8: \(u_n=(2\pi)^{-d}\int_{[-\pi,\pi]^d}\phi(\theta)^n\,\mathrm d\theta\). That pointer is right. Volume 14 and Volume 15 quote the cubic crossing bound with the hypothesis \(m\ge 4n\) and the constant \(64\), which is Exercise 13.4 and Proposition 13.6. Volume 14 quotes Theorem B.7 for arbitrarily long monochromatic arithmetic progressions. Those statements match.

There is no Theorem 2.11, 4.7, 10.21, or 12.10. The repairs that removed the old phantom numbers are still in force on this baseline. A new numbered theorem inserted in the middle of a chapter would break this table. Every proposal below is written so that it does not.

## Pedagogy

The order is the right one for a reader who has Volumes 1–3. Outcomes and outer content come before random variables. The binomial-to-Poisson limit comes before the process. Inequalities come before the strong law. Densities, a rectangle Fubini, and Box–Muller come before Gaussian vectors and the central limit theorem. Walks come before Markov chains, Markov chains before the Poisson process, and martingales before Brownian motion. The probabilistic method comes after expectation is a tool, and random graphs come last, with the subcritical regime proved and the supercritical regime only begun. Appendix B is counting, and it does not use a later volume. That is what the opening sentence of the appendix says, and the proofs I read stay inside it.

The part titles match the work. Entropy sits in "The Laws of Uncertainty" because it is a concentration statement about surprise, and Chapter 7 says so in its first page, pointing back at Chapter 4. The jump from the bell curve to codes is a change of question, not a missing lemma. The bridge at the end of Chapter 14 is a real handoff: generating functions, remainders, and Volume 5 by name and subtitle.

Examples usually come before the general statement. Two coins before the definition of a uniform model. A deck of 52 before the cycle mean. \(n=100\), \(p=0.02\) before the general Poisson remainder. A three-state chain before the convergence theorem. ABRACADABRA after the bounded-stopping argument, with the overlap HT against HH as the small case. The two-step binomial contract is priced as an expectation and as a hedge, and the text says it is not a continuous call price. That is good teaching.

The steep places are the ones the major gaps sit in. A reader who has been trained, by this series, not to swap a limit and an integral without a named theorem will stop at Theorem 6.4, Theorem 11.12, and Proposition 12.11, and will be right to stop. Smoothing those proofs is the pedagogical repair. Adding a chapter on measure theory would betray the preface.

Exercise ladders exist in every chapter, with stars, hints, and solutions. A mechanical check found a hint and a solution for every `\label{ex:…}` attached to an exercise, including Appendix B. I did not re-derive every solution. The balance is reasonable through Chapter 10. Chapters 11 and 12 are the thinnest: martingales has one one-star and four two-star exercises and no three-star; Brownian motion has five one-star and two two-star exercises and no three-star. The proofs are much longer than the exercises. That is a real imbalance. It is not a mathematical error.

One promise to the reader is heavier than a high-school course, and it should stay that way. Volume 1 already contains Stirling, the Gaussian integral, and the spectral theorem. Volume 4 is allowed to use them. It is not allowed to pretend that Lindeberg's swap or the strong-Markov limit is a routine citation.

## Writing and voice

The voice is the series voice. The preface opens on three tails and the question of an infinite string, not on a programme of instruction. Chapter openings name a small experiment: birthdays, a rare success, a message of heads and tails, a walk, a deck. I found none of the stock phrases the style sheet bans ("delve", "it is important to note", "in this section we will", "robust", "comprehensive", and the rest of that list) in the volume's tex. Sentences in the early chapters are short. The Fourier bound in Pólya's theorem and the inversion argument in Chapter 6 are dense, in the same way Volume 1 is dense when it proves Stirling. That is the house style at a climax, not a second voice.

Notation agrees with Volume 1: \(\mathbb E\), \(\operatorname{Var}\), \(\operatorname{Cov}\) defined as in the promise, \(\varphi\) for a characteristic function, \(\Phi\) for the standard normal distribution function. Logarithms in the entropy chapter are base \(2\), and the text says so when a natural logarithm is the tool underneath. I did not find a silent change of base in a numbered theorem.

Figure captions I read state a takeaway and say when a drawing is a mechanism rather than a sample (the riffle distances, Pólya's urn, the inspection paradox, the preface tails). The approved caption style is a production rule. Nothing in this review asks for a change to it. I did not compare captions to rendered plates.

The blurb is the one voice mismatch, and it is m9. The About the Cover note matches the style sheet's test: it says what the picture is, one historical fact, and why it faces the bell-curve chapter. The dates agree with the UCL Galton Collection record LDUGC-063 (quincunx made in 1873 by Tisley and Spiller to Galton's design) and with the standard account that he showed the device at the Royal Institution on 27 February 1874, and described it in *Natural Inheritance* (1889). I did not open the 1889 book. I am not logging the note as an error.

`gilmer.tex` is a drafted section on union-closed families. It is not in the book. Its entropy is the natural-log form of Proposition 7.1, and the constant \((1-\ln 2)/2\) is computed in the file. Volume 15 has its own copy. No later volume cites a Volume 4 Gilmer theorem. Leaving the file out of `main.tex` breaks nothing. I would not add it here.

## Content proposals

Ranked. Page counts are source-page estimates from the length of the surrounding proofs. I did not typeset them. None of these proposals adds a numbered theorem in the middle of a chapter.

### 1. Close M1, M2, M3, and M5 inside the existing proofs

**Motivation.** These are the steps a careful reader cannot grant, and they sit under theorems that Volumes 11, 12, and 15 cite.

**Location.** Theorem 6.4 and the independence sentence in Theorem 6.10; Theorem 11.12; Proposition 12.11 and the first paragraph of Theorem 12.12; the restart sentence in Theorem 10.8.

**Sketch.** As in the proposed-fix column. The product lemma stays unnumbered. The \(L^2\) repair copies Theorem 11.14's truncation. The strong-Markov repair copies Proposition 12.10's compact-box estimate. Superposition computes the residual in place.

**Size.** About four to six pages of source, spread over four proofs.

**Risk.** Low, if no number changes and the displayed statements stay. The risk is a "repair" that quietly assumes Tonelli. The repair has to be written in outer content, finite sums, and the continuous Fubini already in Chapter 5.

### 2. Correct the Bayer–Diaconis sentence (M4)

**Motivation.** The formula is right and the box can be read as a different, false theorem. The distance numbers are the ones readers will check.

**Location.** Theorem 9.9, first sentence.

**Sketch.** "Each arrangement with \(r\) rising sequences has probability \(Q_a\)."

**Size.** One sentence.

**Risk.** None for downstream citations. Volume 15 already treats \(Q_a\) as the probability attached to a given rising-sequence count in the sum for total variation.

### 3. Keep Volume 1's covariance promise (m8), and name Jensen (m7)

**Motivation.** Volume 1 tells the reader this argument is here. It is half a page, and it is the natural companion of the definition already in Chapter 2. The Jensen sentence keeps a second promise and justifies the submartingale step.

**Location.** Chapter 2, after line 64. Chapter 11, the sentence at line 180.

**Sketch.** The sign computation in m8. For Jensen, a pointer to Volume 1's finite form, applied on one atom.

**Size.** Under a page.

**Risk.** None. Unnumbered. Do not restate the whole of Volume 1's inequality chapter.

### 4. Correct the three wrong pointers (R1, R2, R3, and the mean in m14)

**Motivation.** A reader of Volume 3 who turns to Chapter 8 for coupling finds random walks. A reader of Volume 12 who turns to Theorem 12.10 finds a martingale identity, or rather a proposition, and not the differentiability theorem.

**Location.** The three files named in R1, R2, and R3. Optionally one sentence inside Theorem 6.14(a) so that the mean in m14 becomes true.

**Sketch.** Chapter 8 becomes Chapter 9 in the two Volume 3 sentences. Theorem 12.10 becomes Theorem 12.9 in Volume 12. The Gaussian sentence is the translation \(AZ+b\).

**Size.** Four sentences.

**Risk.** These edits are in other volumes. They are not part of a Volume 4 mathematical change, and they must not be bundled with a renumbering. Volumes 1–3 are published. The Volume 3 edits are errata to forward pointers, not changes to a proof. I would still make them: a wrong chapter number is a wrong chapter number.

### 5. Small repairs m1–m6, m12, m13

**Motivation.** Each is a false or incomplete sentence whose correction does not move a number. m1 is the one most likely to be copied into a later Fourier bound.

**Location.** As in the log.

**Sketch.** As in the log.

**Size.** Under two pages in total.

**Risk.** Low.

### 6. Do not do

- Do not add `gilmer.tex` to the book. Volume 15 already treats union-closed families. Inserting the section would duplicate it and would need a home that does not shift Chapter 7's numbers if it were placed inside entropy.
- Do not relabel Appendix B as Appendix A. Theorem B.7 is cited from Volume 14.
- Do not promote the supercritical giant component from Exercise 14.2 to a full theorem unless you want that theorem for its own sake. Exercise 14.2 proves a uniform lower bound on the probability that one vertex's component is linear, by comparison with a Galton–Watson process, and it does not claim that a giant component exists with probability tending to 1. Nothing cites a Theorem 14.3, so a new theorem at the end of Chapter 14 would not shift an existing number. It would be several hard pages, and the book is honest about stopping short. I would leave it for a later decision, not for a correctness repair.
- Do not add Berry–Esseen, Lévy's continuity theorem, or the Itô integral. The text assigns them to Volumes 11 and 12, and those volumes cite Volume 4 for the theorems they actually contain.

### 7. Optional exercises, only if the thin ladder in Chapters 11 and 12 bothers you

**Motivation.** The hardest proofs have the shortest exercise lists.

**Location.** New exercises after 11.5 and after 12.7. Existing exercises 11.1–11.5 and 12.1–12.7 stay put. Volume 12 cites Exercise 12.3; it does not cite an Exercise 12.8.

**Sketch.** One two-star on the quadratic variation of a dyadic skeleton at a fixed \(t\), asking only for the mean \(t\) and the variance bound already in Theorem 12.7. One two-star on optional stopping for the walk stopped at a deterministic time \(N\), with the barrier example already in the text as the case that fails.

**Size.** About two pages, including solutions.

**Risk.** Low, because the new numbers are at the end. Still optional. The correctness repairs come first.

## Verified correct

### Recomputed in this pass

These are numerical checks, not proofs.

- Ballot count at \((a,b)=(5,3)\): \((a-b)/(a+b)=1/4\), and \(\binom{7}{4}-\binom{7}{5}=14\), agreeing with \((a-b)/n\binom{8}{5}\).
- \(22/365=0.06027\ldots<0.0603\). \(365\ln 2=252.9987\ldots\). The birthday comparison in the solution of Exercise 1.1 uses a sharper decimal than Volume 1's recorded bounds, but those bounds already give \(365\ln 2<253\). Not logged, because the inequality the solution needs is true from the bound Volume 1 prints.
- \(H_{52}=\sum_{k=1}^{52}1/k=4.538\ldots\), with \(\ln 53=3.970\ldots\) and \(1+\ln 52=4.951\ldots\), as Chapter 2 states.
- \((0.98)^{100}=0.13262\ldots\) and \(e^{-2}=0.13534\ldots\). The text's stricter bounds around \(e^{-2.02}\) were part of the chapter reading; I recomputed only these two anchors.
- ABRACADABRA: \(26^{11}+26^4+26=3670344487444778\), Theorem 11.11.
- Exponential moments: the recurrence \(m_k=(k/\lambda)m_{k-1}\) with \(m_0=1\) gives \(m_4=24/\lambda^4\), as the paragraph before Theorem 10.4 says.
- Riffle-shuffle total variation for \(n=52\), from the Eulerian numbers of descents (so \(r\) rising sequences means \(r-1\) descents) and the displayed formula. Half the \(\ell^1\) distance, to five decimals, and the book's three-decimal rounding:

| Shuffles \(k\) | Distance | Book's three decimals |
| ---: | ---: | --- |
| 1 | \(1\) to ten decimals | \(1.000\) (rounded; the text says \(d_k<1\)) |
| 2 | \(1\) to ten decimals | \(1.000\) |
| 3 | \(1\) to ten decimals | \(1.000\) |
| 4 | \(0.999999533\) | \(1.000\), and the text says the first four are rounded |
| 5 | \(0.92373\) | \(0.924\) |
| 6 | \(0.61355\) | \(0.614\) |
| 7 | \(0.33406\) | \(0.334\) |
| 8 | \(0.16716\) | \(0.167\) |
| 9 | \(0.08542\) | \(0.085\) |
| 10 | \(0.04295\) | \(0.043\) |

For one, two, and three shuffles the floating-point value was \(1\) to ten decimals, which is enough to confirm the book's three-decimal rounding and not enough to exhibit the exact deficit below \(1\). The text already says those four leading values are rounded and that \(d_k<1\). The separation \(\pi\sqrt 3>2\sqrt 2\) used in the proposed fix of m1 holds: \(2\sqrt 3\approx 3.464\) and \(2\sqrt 2\approx 2.828\).

### Statements I re-read and am willing to call intact

The boxes, not every line of every proof. Where a proof has a logged gap, the gap is the log entry. M4 is the exception: the box itself can be read as the wrong event. The other boxes state the classical conclusion.

- Chapter 1: uniform digits, outer content, subadditivity, the ballot theorem's reflection count as used again in Chapter 8, the distinction between the three-label list and the four coin outcomes.
- Chapter 2: Poisson limit for \(np_n\to\lambda\) and for \(np_n\to 0\); cycle indicators \(\mathbb E[X_k]=1/k\); coupon collector \(\mathbb E[T]=nH_n\); covariance definition.
- Chapter 3: extinction threshold, including the case \(m=1\) with \(P(X=1)<1\), and the probability-generating-function mean and variance for the binomial and Poisson laws.
- Chapter 4: Hoeffding's exponent \(-2t^2/\sum(b_i-a_i)^2\); Borel–Cantelli (a) by outer content; the bounded strong law along squares; Bernstein's proof of Weierstrass on a compact interval. The complement step in (b) is m4.
- Chapter 5: normal density from Volume 1's half-line Gaussian integral after \(u=x/\sqrt 2\); Gaussian tail \(e^{-x^2/2}/x\); Buffon for \(0<\ell\le d\), value \(2\ell/(\pi d)\); Bertrand's three probabilities \(1/3\), \(1/2\), \(1/4\); Box–Muller factor \(r\), with the Rayleigh factor cancelling to \(\phi(x)\phi(y)\). I did not re-expand the polar Jacobian from scratch in this pass; the displayed integral and the cancellation were checked against the proof's algebra.
- Chapter 6: inversion constant \(1/(2\pi)\) and the sign \(e^{-itx}\); Lindeberg's condition as a truncated second-moment condition, with the fair-sign counterexample when it fails; local limit at the centre, \(\binom{2m}{m}\sim 4^m/\sqrt{\pi m}\), from Volume 1's Stirling formula; Corollary 6.11 as the i.i.d. finite-variance case. Slutsky is Exercise 6.1, and Volume 15 cites that exercise for the right statement.
- Chapter 7: Gibbs, Kraft, Shannon's code bounds \(H\le L<H+1\), Huffman. Zero-probability symbols are omitted rather than sent to \(\log(1/0)\).
- Chapter 8: reflection \(P(M_n\ge a)=P(S_n\ge a)+P(S_n>a)\) for a positive integer \(a\); gambler's ruin; Pólya for \(d=1,2\) by the local theorem and for \(d\ge 3\) by the Fourier integral, apart from m1; discrete arcsine \(P(L_{2n}=2k)=u_{2k}u_{2n-2k}\); the limit with constant \(2/\pi\).
- Chapter 9: stationary law on a finite irreducible chain; coupling bound on total variation; top-to-random stationary time with mean \(nH_n\); the \(a\)-shuffle definition; composition of riffles; untouched-card lower bound \(1-6e^{1-2c}\). The Bayer–Diaconis formula is correct per arrangement (M4).
- Chapter 10: Poisson counts and order statistics; colouring lemma; thinning; M/M/1 geometric stationary law when \(\rho<1\), mean \(\rho/(1-\rho)\). Superposition's restart is M5. The marginal Poisson probabilities in the colouring lemma are the right ones.
- Chapter 11: optional stopping under a deterministic bound \(\tau\le N\); the first-hit of \(+1\) as a case where \(\tau<\infty\) almost surely and \(\mathbb E[S_\tau]\ne\mathbb E[S_0]\); Doob's inequality in the stated direction; Azuma's exponent \(-t^2/(2\sum c_k^2)\); Pólya's urn \(P(R_n=k)=1/(n+1)\) and the beta-free identification of the uniform law once convergence in probability is granted. The \(L^2\) passage is M2.
- Chapter 12: dyadic Lévy construction's increment variances; quadratic variation along the dyadic partition plus one stub, at each fixed \(t\), with the text refusing the claim for every sequence of partitions; the dyadic Taylor expansion not presented as Itô's formula; reflection's density and infinite mean once symmetry is granted. The grant is M3.
- Chapter 13: Erdős's bound \(R(k,k)>2^{k/2}\); the symmetric local lemma under \(ep(d+1)\le 1\); the crossing constants \(m-3n\) and \(m^3/(64n^2)\). The algebra \(1/16-3/64=1/64\) checks.
- Chapter 14: the subcritical bound does not claim a giant component for \(c>1\); the triangle threshold distinguishes \(np\to 0\) and \(np\to\infty\). Exercise 14.2's Galton–Watson comparison is a lower bound for one vertex, not a full giant-component theorem.
- Appendix B: Turán's conclusion \(T(n,r)\); Ramsey \(R(3,3)=6\) via the 5-cycle; Erdős–Ko–Rado bound \(\binom{n-1}{k-1}\); \(W(3,2)=9\); van der Waerden's finite theorem and the passage to the infinite form by the pigeonhole principle. I re-read the statements and the focus step, not every colouring case in the length-three argument.

### Cross-volume navigation that is right

Volume 5's integral formula for returns, Volume 6's use of the Poisson limit as Theorem 2.1 on the current baseline, Volume 11's use of Theorem 11.13 for Pólya's uniform limit, Volume 14's crossing lemma and van der Waerden citations, and Volume 15's use of Exercises 6.1 and 9.8, Theorem 9.6, and Theorem 11.12 in the senses recorded above. The 454-count is the net: those matches, minus R3.

## Not reviewed

- The PDF, EPUB, and HTML reader were not built and not opened. Printed folios, line breaks, and caption colour were not inspected. Numbers in this report are source counters.
- TikZ coordinates were not measured against captions. The riffle ordinates were not re-read from `figures/ch08-riffle.tex` in this pass; the distances above were recomputed from the formula in the chapter.
- Bibliographic pages were not opened in the journals (Bernoulli, Chebyshev, Hoeffding, Borel, Cantelli, Bernstein, Bayer–Diaconis, Pólya 1921, Lévy, Doob, Galton 1889). The Galton dates were checked against the UCL collection record and secondary accounts, as noted above.
- I did not re-derive every exercise solution. The pairing of hints and solutions is mechanical and complete. The mathematical check of solutions is the chapter reading, plus the solutions I opened while confirming M4, m2, m3, and the cycle CLT's appeal to Slutsky.
- Internal proofs of Volume 1 were not re-audited past the statements cited here. If Volume 1's proof of \(\ln'(x)=1/x\) or of Stirling were wrong, this review would not have caught it.
- Volumes 5–15 were not read as books. They were read at the Volume 4 citations the extractor found, and at the sentences needed to judge R1–R3 and m14.

### Noted by the chapter reading, and not re-opened here

These are not findings of this report. I am recording them so the coverage is auditable. A later pass can promote any of them by opening the line.

- Hoeffding's proof speaks of a finite sum while the theorem allows a countable model (`ch04-inequalities.tex:71`).
- Inversion compares an indicator with a test-function expectation without a written grid bound (`ch06-clt.tex` around the uniqueness argument).
- The binomial-series solution differentiates at negative \(x\) by a domination stated for nonnegative terms (`ch03-generating.tex` around Exercise 3.7).
- The birthday-wait solution's Riemann-sum limit is in the right order and is not written with liminf and limsup (`ch02-discrete.tex` around Exercise 2.7).
- The escape-time solution cites the arcsine theorem for an asymptotic that the local theorem supplies (`ch07-walks.tex` around Exercise 8.6).
- Memorylessness omits the two lines \(G(1)=G(1/q)^q\) and \(G(p/q)=G(1/q)^p\) (`ch09-poisson.tex` around Proposition 10.1).
- Le Cam's coupling bound is stated in Chapter 9 for a finite set (`ch09-poisson.tex` around Theorem 10.12).
- The Lévy construction cites Borel–Cantelli for a Gaussian midpoint tail without the outer-content comparison written later for the scaling maxima (`ch11-brownian.tex` around Theorem 12.4).
- The Poisson-half exercise cites Chapter 2 for the sum of \(n\) independent Poisson random variables; Chapter 2 treats two (`ch06-clt.tex` around Exercise 6.5).

## Bottom line for the author

Repair M1–M5 in Volume 4, without new numbers. Correct R1–R3 in the volumes that own those sentences. Add the half-page covariance argument Volume 1 already promised. Leave Gilmer out, leave Appendix B lettered B, and leave the giant-component theorem unproved until you want that theorem for itself. The book can stay the published successor while those repairs are made. I am not claiming that the list above is a proof that nothing else is wrong.

## Second pass after the repairs

This pass reads the repairs. Heads at the time of the reading:

| Pull request | Head | What it carries |
| --- | --- | --- |
| #152 | `789b09b512eb7d01b45dcb2f8617ed0a13b5562b` | M1, M2, M3, M5 |
| #155, stacked on #152 | `569b2a9580bc9bce29a59369e340193d498747ec` | M4, m1–m13, the Theorem 6.14 shift, and the Volume 3 seam-snapshot refresh |
| #153 | `94157806` | R1, R2 only |
| #154 | `2cf9d56e` | R3, m14 |

`python3 -m unittest discover -s tools -p 'test_volume4*.py'` passed, 94 tests, on the wording head. Source-identity pins were recomputed from the new blobs, and the label inventories in those tests were unchanged. A numerical check is not a proof. The two-point check and the exponential integral below only test algebra the proofs quote.

| ID | Location of the repair | What the second reading found | Residual doubt |
| --- | --- | --- | --- |
| M1 | `ch06-clt.tex`, unnumbered `prop:indepproduct`, used in Theorems 6.4 and 6.10 | Bounded monotone factors of at most four distinct blocks factor by dyadic steps and the independent-uniforms proposition. A finite-bit function against a monotone factor factors by the cylinder table. Clips remove the bound using \(\lvert Q-Q^{(M)}\rvert\le Q^2/M\) and the tail of a convergent improper integral. The strong law expands the centred clip \(Y=Q^{(M)}-\mathbb E[Q^{(M)}]\), whose mean is 0, so there is no \(n^4\) term. The deviation event is reduced to a finite-bit step of \(Y\) plus a mesh error whose fourth moment is made at most \(n^2\). Lindeberg replaces \(f'(A)\) by its average on the other blocks' first \(m\) digits and uses the same product. | The average is an integral of a bounded function of the remaining bits. The text points at the rectangle Fubini after clipping the coordinates of \(A\), and says the tails can be made small. It does not write a separate \(\varepsilon\) line for that tail. The constant \(C\) in \(\mathbb E[(\sum Y_i)^4]\le Cn^2\) is existential. For the fair sign \(Y=\pm 1\), \(\mathbb E[(Y_1+Y_2)^4]=8\), and \(n\mathbb E[Y^4]+3n(n-1)(\mathbb E[Y^2])^2\) is also 8. That checks the pattern. It is not a proof of the expansion. |
| M2 | `ch10-martingales.tex`, Theorem 11.12 | Almost-sure convergence is still the outer-content argument, and it still names the continuity-from-below theorem it refuses to use. The square limit is \(\mathbb E[\min(Y^2,M)]\le r_{n_j}\), then \(M\to\infty\). The \(L^1\) bound uses Volume 1's finite Cauchy–Schwarz on \(\min(\lvert Y_m\rvert,M)\). | The comparison of the bounded sequence with its limit is shorter than the write-up of Theorem 11.14. The exceptional set is covered by an extra length \(\varepsilon\). I did not re-sum every disjoint interval by hand. |
| M3 | `ch11-brownian.tex`, Proposition 12.11 and Theorem 12.12 | The limit from \(\tau_n\) to \(\tau\) uses a compact box and Gaussian tails. Reflection reads the symmetry at each fixed dyadic \(s\le t\), where \(B_t-B_s\) is independent of \(\{\tau_n=s\}\) and symmetric, then sends \(B_s\to a\). | The normal-tail scale is \(c=\sqrt{v}\) for a positive increment length. I did not rebuild the continuous approximation of the tail indicator line by line. The text says the indicator is squeezed between two continuous tests. |
| M5 | `ch09-poisson.tex`, Theorem 10.8 | \(\lambda e^{-(\lambda+\mu)t}\,\mathrm dt\) times \(e^{-\mu r}\) is the joint event that the \(\lambda\)-clock rings at \(t\) and the other residual exceeds \(r\). A Simpson rule on \([0,30]\) with \(3\cdot 10^5\) panels gave \(0.122620\) against \(\lambda/(\lambda+\mu)\,e^{-\mu r}=0.122626\) at \(\lambda=1\), \(\mu=2\), \(r=1/2\). The difference is quadrature. | The displayed line is the improper density. The bound \(e^{-\lambda A}+e^{-\mu A}\) for the corner of the square is written. |
| M4 | `ch08-markov.tex`, Theorem 9.9 | The box says each arrangement. For \(n=3\), \(a=2\), \(r=2\), \(Q_2=1/8\), and four permutations carry that mass, so the event has probability \(1/2\). | None on the wording. |
| m1 | `ch07-walks.tex`, Theorem 8.5 | \(\pi>2\), then \((2\sqrt3)^2=12>8\). | None. |
| m2 | `ch07-walks.tex`, Proposition 8.3 and Exercise 8.7 | The tail-sum identity is cited by chapter, not by a cross-book label. | A label in Volume 1 would not resolve in this book. |
| m3 | `ch05-continuous.tex`, Exercise 5.7 | One \(0\)-\(2\) expansion. | None. |
| m4 | `ch04-inequalities.tex`, Theorem 4.4(b) | Complement product by induction from finite additivity. | One paragraph, not a displayed induction. |
| m5 | `ch06-clt.tex`, Theorem 6.8 | Points at Chapter 5's substitution. | None. |
| m6 | `ch06-clt.tex`, Theorem 6.14(b) | The quadratic form is a centred variance. | None. |
| m7 | `ch10-martingales.tex`, before Theorem 11.9 | Jensen is Volume 1's finite convex combination, with no cross-book `\ref`. | The printed number of that theorem was not recomputed. The chapter is the inequalities chapter. |
| m8 | `ch02-discrete.tex`, after the covariance definition | The product of increments of two increasing functions is nonnegative. | The four-term expansion is the one in Volume 1 and is not rewritten in full. |
| m9 | `blurb.tex` | Names Volume 1. | Jacket copy, not an interior page. |
| m10 | `ch01-counting.tex`, `ch08-markov.tex` | Both cite Volume 1, Chapter 10, for \(1-x\le e^{-x}\). | None. |
| m11 | `ch02-discrete.tex`, Theorem 2.1 | Chapter 3 defines the derivative. Chapter 8 gives \(\ln'(1)=1\). | None. |
| m12 | `ch09-poisson.tex`, Theorem 10.4 | Theorem 6.4 is not applied. Finiteness is proved after the Poisson masses, and \(T_n\to\infty\) uses one intersection over the positive integers. | The old string \(t=1,2,3,\ldots\) was replaced. The test that pinned it was updated. |
| m13 | `ch10-martingales.tex`, Theorem 11.14 | The sandwich holds off a cover of the exceptional set. The gap gains \(M\varepsilon\), which tends to 0. | None beyond that \(\varepsilon\). |
| R1, R2 | two sentences in Volume 3 | Chapter 9. No other line in those files. | Volumes 1 and 2 are absent from the diff. |
| m14, R3 | `volume12-random-motion/chapters/ch01-gaussian.tex` | Theorem 12.9, and the reminder quotes centred \(AZ\), the translate \(AZ+b\), positive-semidefiniteness, and block independence. | Merge #155 before #154. |

Nothing in this pass needs an author decision. Gilmer stays out. Appendix B stays B. The giant-component statement stays an exercise.
