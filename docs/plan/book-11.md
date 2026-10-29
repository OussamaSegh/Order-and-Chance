# Book 11 — Randomness

*Martingales, Limits and Ergodicity.* The on-disk subtitle is "The Structure of Randomness".

**Element.** Settlement. The building under a long load: what remains when the bell curve is not the whole story, and when the variables are one deterministic system watched for a long time.

**On disk.** Volume 10, `tome10-chance2`. Twelve chapters plus `chapters/ch13-harder.tex`, the former Frontiers chapter "Sums of Random Pieces". About 192 pages before that chapter. The October review scored the twelve chapters 8. The preface now names three exceptions, not one: Selberg–Delange, the triangular-array converse, and non-symmetric stable laws.

## Promise

Book 4 proved the first two answers of probability, the law of large numbers and the central limit theorem. This floor asks the questions those answers raise. How good is the bell curve, and what replaces it when there is no variance? How unlikely is a rare event, on the exponential scale? Why is a function of many independent variables almost constant? What does the whole path look like from far away? What can be said when the variables are not independent, but one system observed over time? The last two chapters are the joint into the primes: the same Poisson–Dirichlet law for cycles of a permutation and for prime factors of an integer. The arithmetic half quotes Selberg–Delange, which is proved in Book 15.

## Prerequisites

Book 4. Book 7, including Prokhorov and, once it is promoted, the tower property of conditional expectation. Book 8's compact operators, for the weakly mixing lemma. Book 6's Erdős–Kac theorem, quoted. No stochastic calculus; that is Book 12.

## How the subtitle is delivered

The subtitle names three subjects, in this order: martingales, limits, and ergodicity. The contents page uses those words. The manuscript currently hides martingales in Chapter 9 and ergodicity in Chapter 10. The edition puts them in the part the subtitle names. Reading order may still take the limit theorems before the martingale convergence that uses them; the contents page does not.

| Subtitle word | Chapters |
| --- | --- |
| Martingales | Chapter 9, the whole of it: uniform integrability, de Finetti, Kakutani, Ville. Book 4 built the first martingales. This part is where the subtitle's word is proved at full strength. |
| Limits | Chapters 1–8, 11–13, and the shuffle cutoff moved from Book 10. Zero–one laws, the strong law, Donsker, Berry–Esseen, stable laws, Stein, large deviations, concentration, mod-\(\varphi\) convergence, and the Poisson–Dirichlet law are limits. |
| Ergodicity | Chapter 10. Birkhoff, the Gauss map, and Furstenberg's proof of Roth. |

No chapter that stays fails the subtitle. The arithmetic in Chapters 11 and 12 is a limit law. Selberg–Delange remains quoted from Book 15.

---

The chapter notes follow the manuscript's file order. On the contents page the parts are Martingales, Limits, and Ergodicity, in that order.

### Part I. Laws and Invariance

#### Chapter 1. Independence and Zero–One Laws

**Status.** KEEP — `tome10-chance2/chapters/ch01-zero-one.tex` (553 lines).

**Hook.** The harmonic series diverges, and the alternating harmonic series converges. Choose every sign by a fair coin. With probability one the random series converges.

**Synopsis.** Independent \(\sigma\)-algebras, Kolmogorov's zero–one law, exchangeable events, random series, random signs, and the random harmonic series. A tail event has probability 0 or 1. That is the sense in which an infinite sequence of loads settles into a yes or a no, with nothing in between.

**Proved.** Kolmogorov's zero–one law. The three-series theorem's companions that this chapter owns, if the three-series theorem itself is Chapter 2's. Convergence of random series under the hypotheses stated.

**Examples.** The random harmonic series, almost surely convergent, with a picture of a few paths. One tail event that is not a function of any finite set of coordinates.

**Figures.** Two.

#### Chapter 2. Laws of Large Numbers

**Status.** KEEP — `chapters/ch02-lln.tex` (439 lines).

**Hook.** A casino pays \(2^k\) if the first head arrives on toss \(k\). The expected win is infinite. The strong law still has something to say, and the something is not the expectation.

**Synopsis.** Truncation and the weak law, Etemadi's strong law, Kolmogorov's three-series theorem, and renewal. The strong law from a first moment, which Book 4 postponed, is proved here. Book 4's preface, after its revision, points at this chapter.

**Proved.** Etemadi's strong law. The three-series theorem. The weak law under truncation.

**Examples.** The St. Petersburg game, whose expectation is infinite and whose typical fortune grows much more slowly. One renewal count.

**Figures.** Two.

#### Chapter 3. Weak Convergence and Donsker's Theorem

**Status.** REVISE — `chapters/ch03-donsker.tex` (590 lines). The introduction must point at the Kolmogorov–Smirnov remark, so that "made Doob's heuristic a proof" cannot be read as a theorem about the empirical process. Donsker here is Skorokhod embedding plus a modulus comparison, for random walks in \(C[0,1]\). The empirical-process version is not proved.

**Hook.** Any random walk with mean 0 and variance 1, seen from far away, time shrunk by \(n\) and space by \(\sqrt n\), becomes the same curve.

**Synopsis.** Lévy's continuity theorem, random continuous functions, the strong Markov property, Skorokhod's embedding, Donsker's theorem, and the law of the iterated logarithm. This is the climax of the first part. Book 4 built one Brownian motion. This chapter says every finite-variance walk is that motion, in distribution, in \(C[0,1]\). Prokhorov from Book 7 is the tightness. Book 12 starts from the process this theorem names.

**Proved.** Lévy's continuity theorem, without the unproved converse of Bochner. Donsker's theorem under finite variance and mean zero. The Hartman–Wintner law of the iterated logarithm, if it is this chapter's.

**Examples.** A simple random walk and a walk with a different step law, drawn at a large \(n\), against the same Brownian scaling. One statement of what the chapter does not prove: the Kolmogorov–Smirnov theorem.

**Figures.** Two.

#### Chapter 4. The Central Limit Theorem, Sharpened

**Status.** KEEP — `chapters/ch04-clt.tex` (593 lines).

**Hook.** Book 4 proved that sums of small independent pieces look Gaussian. Is the hypothesis the right one, and how fast is the approximation?

**Synopsis.** The Lindeberg–Feller converse, Berry–Esseen with the book's constant \(3.1\), several dimensions and Pearson's test, the local limit theorem, and recurrence by Fourier analysis, including Chung–Fuchs. Berry–Esseen is what Book 15's workshop cites when it reads a Rademacher sum. The constant stays on the page.

**Proved.** Lindeberg–Feller, both directions. Berry–Esseen. The local limit theorem. Chung–Fuchs, including transience in dimension \(\ge 3\) with no moment assumption.

**Examples.** A Berry–Esseen numerical bound next to a binomial. One local-limit histogram.

**Figures.** Two.

#### Chapter 13. Sums of Random Pieces

**Status.** REVISE — `chapters/ch13-harder.tex` (about 1200 lines). Retitle from "Harder problems". The file is the finished Frontiers chapter, local limit theorems, signed sums, Bernoulli convolutions, and real roots of random polynomials. It belongs with Part I, after Chapter 4, because its tools are Chapters 2–4 and 6. The unpublished second Frontiers chapter, on rare events, is not restored: its discrepancy and blow-up solutions did not prove the stated bounds.

**Hook.** Add many small random pieces and a bell curve appears. How soon? Point by point, or only on intervals? What if the pieces depend on each other?

**Synopsis.** Problems, each with a hint and a complete solution, on the limit theorems of this part. Lindeberg's swap of one variable at a time is the opening. A problem may use Stein's method and must then say Chapter 6 is allowed. Nothing in the chapter is a second proof of Donsker.

**Proved.** The solutions prove the problems. The chapter does not add an unproved limit theorem in the voice of the main text.

**Examples.** A signed sum. One Bernoulli convolution. The expected number of real roots of a random polynomial, at the precision the problem asks.

**Figures.** Three.

### Part II. Beyond the Gaussian

#### Chapter 5. Infinitely Divisible and Stable Laws

**Status.** REVISE — `chapters/ch05-stable.tex` (521 lines). The preface already says the triangular-array converse is referred to Gnedenko–Kolmogorov, and that non-symmetric stable laws are quoted from Feller. Repeat that sentence after the Feller formula in the chapter, not only in the preface. The symmetric theory, and the one-sided law of index \(\tfrac12\), are proved. Skewness is not used later.

**Hook.** Which laws can be the limit of a sum of many small independent pieces? The Gaussian. The Poisson, when the pieces are rare. And others, with heavy tails.

**Synopsis.** Infinite divisibility, the Lévy–Khintchine formula with uniqueness, limits of infinitesimal arrays in the direction the chapter proves, symmetric stable laws, and the one-sided stable law of index \(\tfrac12\). The Gaussian is no longer the only shape a settled sum can have. Book 12's Lévy–Itô decomposition is the pathwise form of the same idea.

**Proved.** Lévy–Khintchine with uniqueness. The symmetric stable domains of attraction the chapter claims. The one-sided law of index \(\tfrac12\).

**Examples.** A Cauchy law as a symmetric stable law of index 1. The hitting-time law of Brownian motion, index \(\tfrac12\), which Book 12 will meet as a first-passage time.

**Figures.** Two.

#### Chapter 6. Stein's Method

**Status.** KEEP — `chapters/ch06-stein.tex` (556 lines).

**Hook.** Characteristic functions prove limit theorems and hide the error. Stein measures the error with one identity.

**Synopsis.** Gaussian integration by parts, the Stein equation, Wasserstein distance, exchangeable pairs, and Chen–Stein for Poisson approximation. Birthdays, hashes, and triangles are the examples. The method is how a later sentence can say "the distance to the bell curve is at most this", with the constant visible.

**Proved.** The Stein equation for the normal law and the bounds the chapter derives. Chen–Stein for dependency graphs of the type stated.

**Examples.** A birthday collision. The number of triangles in a random graph, Poisson approximation with an explicit error.

**Figures.** Two.

#### Chapter 7. Large Deviations

**Status.** KEEP — `chapters/ch07-ldp.tex` (504 lines). Cramér's theorem assumes a finite moment generating function on the whole line, stronger than a neighbourhood of 0. The hypothesis stays in the heading. Bahadur–Rao is not proved. Sanov is for a finite alphabet.

**Hook.** The central limit theorem describes the usual fluctuations. An insurer cares about the unusual ones.

**Synopsis.** Cramér's theorem, Sanov on a finite alphabet, the shape of a rare event, the best test, and Varadhan's lemma on a toy magnet. Four numbers in the text, a gamma tail, the Cramér bound, Bahadur–Rao, and a Gaussian tail, are the point of the subject. Leave them.

**Proved.** Cramér's theorem on \(\mathbb R\) under a global moment generating function. Sanov's theorem for a finite alphabet.

**Examples.** A coin's large-deviation rate. One Sanov rate for a die.

**Figures.** Two.

#### Chapter 8. Concentration of Measure

**Status.** KEEP — `chapters/ch08-concentration.tex` (456 lines).

**Hook.** A function of many independent variables, none of them too influential, is nearly constant.

**Synopsis.** Efron–Stein, McDiarmid, Gaussian concentration, the Johnson–Lindenstrauss lemma, and Talagrand's convex distance. The longest increasing subsequence and the chromatic number of a random graph are the applications, at the concentration the chapter proves. Tracy–Widom is not this chapter. Book 12 says so again.

**Proved.** McDiarmid's inequality. Gaussian concentration. Johnson–Lindenstrauss. Talagrand's convex distance in the form stated.

**Examples.** A Lipschitz function of independent bits, with McDiarmid's width. One projection of a high-dimensional point set.

**Figures.** Two.

### Part III. Martingales and Ergodic Theory

#### Chapter 9. Martingales II: Closing the Circle

**Status.** KEEP — `chapters/ch09-martingales.tex` (587 lines).

**Hook.** A fair game can converge to zero while its average stays at one. Uniform integrability is the missing beam.

**Synopsis.** Uniformly integrable martingales, backward martingales, de Finetti's theorem, Kakutani's dichotomy for product measures, and Ville's inequality. Book 4 proved \(L^2\) and almost-sure convergence. This chapter closes the circle: convergence in \(L^1\) is uniform integrability. The tower property, once Book 7 numbers it, is used here and should be cited there.

**Proved.** The \(L^1\) convergence theorem for uniformly integrable martingales. De Finetti for exchangeable binary sequences, or the form the file proves. Kakutani's dichotomy.

**Examples.** A martingale that converges almost surely and not in \(L^1\). One exchangeable sequence and its directing measure.

**Figures.** Two.

#### Chapter 10. Ergodic Theory

**Status.** REVISE — `chapters/ch10-ergodic.tex` (563 lines). The proof of Roth's theorem for three-term progressions is complete, by Furstenberg's correspondence principle, including the compact and weakly mixing split. Szemerédi's theorem for longer progressions is stated as not proved. Book 14, Chapter 12, proves the same length-three theorem by Fourier analysis. Neither proof cites the other. Each introduction names the other. That is the whole revision.

**Hook.** Follow one point for a long time, or look at all points at one instant. The ergodic theorem says the averages agree.

**Synopsis.** Measure-preserving systems, the ergodic theorems, the digits of a random number, the Gauss map, and recurrence. Birkhoff's theorem computes the statistics of the continued fraction of almost every real, the return of Book 2's continued fractions and of Book 7's problem chapter. Furstenberg's proof of Roth is the climax. The ratio \(1:2\) in the argument is a pause the text already asks the reader to find. Keep the question.

**Proved.** Birkhoff's theorem. The Gauss-map ergodicity and the almost-everywhere continued-fraction statistics the chapter claims. Roth's theorem for three-term progressions.

**Examples.** The Gauss map on a named quadratic. One finite set with no three-term progression, of the Behrend shape if it is only a remark, or a small cyclic example.

**Figures.** Two.

### Part IV. Arithmetic Probability

#### Chapter 11. Mod-\(\varphi\) Convergence

**Status.** REVISE — `chapters/ch11-modphi.tex` (347 lines). Cross-refer Book 6's Erdős–Kac theorem at the start. At the display of Selberg–Delange, label the uniform-integer statement as a corollary of a formula quoted from Book 15, not as a theorem of this chapter. The paraphrase into a mod-Poisson theorem is not proved here. A reader must be able to see the label.

**Hook.** The central limit theorem is a magnifying glass that shows only the bell curve. Divide the characteristic function by the bell curve first, and a finer shape remains.

**Synopsis.** Mod-\(\varphi\) convergence, what mod-Poisson convergence gives, cycles of a random permutation, and prime factors of a random integer. The cycles are proved. The prime factors quote Selberg–Delange. Book 15, Chapter 3, is the home of that theorem, in `ra-selbergdelange.tex`, included from `ch03-divisors.tex`. Until that chapter is the citation, this chapter says "quoted".

**Proved.** The mod-Poisson convergence for the number of cycles, at the strength the file proves. The formal consequences of a quoted Selberg–Delange formula, labelled as formal.

**Examples.** The cycle count of a random permutation against a Poisson law. One numerical \(\omega(n)\) histogram, captioned as Book 6's theorem, not as a new proof.

**Figures.** Two.

#### Chapter 12. Random Permutations and the Poisson–Dirichlet Law

**Status.** KEEP — `chapters/ch12-permutations.tex` (475 lines). REVISE the last page so it points at Book 6's Erdős–Kac chapter and Book 14's Roth chapter, the two arithmetic returns a reader has now earned. Dickman's function is the joint to Book 15's anatomy of friable integers. The chapter proves the permutation form and cites the integer form.

**Hook.** Shuffle a million cards and look at the cycles. The small ones are independent Poisson variables. The big ones are a stick broken at random.

**Synopsis.** Small cycles, the broken stick, Dickman's function, correlation functions, and Billingsley's theorem. The Poisson–Dirichlet law describes both the cycle lengths and the sizes of the prime factors of a large integer. The second description is the cliffhanger. Its proof is not finished on this floor.

**Proved.** The Poisson law for small cycles. The Poisson–Dirichlet description of the large cycles. Billingsley's theorem in the form the file proves. The Dickman function as the limit for the longest cycle, or for the largest prime factor, whichever side is actually proved; the other side is cited.

**Examples.** A stick broken into Poisson–Dirichlet lengths, drawn. Dickman's \(\rho(u)\) on a short interval, the same function Book 15 will meet for friable integers.

**Figures.** Two.

## Owns, defers, hands forward

**Owns.** Kolmogorov's zero–one law, Etemadi's strong law, the three-series theorem, Lévy's continuity theorem, Donsker in \(C[0,1]\), Lindeberg–Feller, Berry–Esseen, Lévy–Khintchine with uniqueness, symmetric stable laws, Stein and Chen–Stein, Cramér on \(\mathbb R\) under a global moment generating function, Sanov on a finite alphabet, McDiarmid, Gaussian concentration, Talagrand, de Finetti, Kakutani, Birkhoff, the Gauss map, Furstenberg's Roth theorem, the cycle structure of a random permutation.

**Defers.** Selberg–Delange (Book 15). Tightness in \(D[0,1]\) and Donsker for the empirical distribution. A martingale central limit theorem. Non-symmetric stable laws. The Itô integral (Book 12). Multiple recurrence past length 3. The Fourier proof of Roth (Book 14), which is cited, not absorbed.

**Hands forward.** Settlement. Book 12 builds the calculus of the Brownian motion Donsker named. Book 15 proves the arithmetic theorem this book's last chapters quote, and it reads the ergodic proof of Roth beside the Fourier proof.

## Pages and effort

Baseline 192 pages plus the problem chapter. Target 210–240. Effort: light to moderate. The probabilistic core can be taught as written. The work is the labels, the two Roth citations, the Selberg–Delange label, the stable-law sentences, and the retitle.
