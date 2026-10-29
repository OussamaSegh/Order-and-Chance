# Book 14 — The Primes

*Their Hidden Rhythm.* The on-disk subtitle is "The Hidden Rhythm of Primes".

**Element.** The rhythm in the courses. The bricks were laid in Book 2. The span was thrown in Book 6. This floor asks how regular the courses are up close, and where the method stops hearing them.

**Source.** `tome14-primes`. Fourteen chapters, about 211 pages. The October review scored it 8, and called its register the most careful in the series. The bound \(600\) is now labelled as depending on a rational witness and Engelsma's tuple, neither printed. The preface no longer calls its list of quotations short.

## Promise

Book 6 ended with the prime number theorem, an error term, and the first sieves. The primes looked regular from far away and mysterious from close up. This book proves the answers that are known: primes in short intervals from a zero-density estimate, Siegel's theorem, the parity problem, Bombieri–Vinogradov, the circle method through the Hardy–Ramanujan asymptotic and Vinogradov's three primes, Maynard's bounded gaps, Halász's theorem, Roth's theorem by Fourier analysis, the \(U^2\) theory around Green–Tao, and Montgomery's pair correlation on a limited range. Green–Tao itself is quoted. A positive proportion of zeros on the critical line is quoted. Three primes, Siegel–Walfisz, and Bombieri–Vinogradov share one ineffective constant, from Siegel's theorem, and the preface says so.

The cliffhanger is the dictionary. The courses can be heard. Which statistics are the coin model, and which remember the small primes, is Book 15's question, asked there as the meeting of structure and randomness.

## Prerequisites

Book 6, entire, and the cut named in that book's preface. Book 5's tauberian and residue tools. Book 8's finite Fourier analysis, Meshulam as a numbered theorem. Book 11's ergodic proof of Roth, cited and not absorbed. Book 13's Chebotarev and the discriminant of \(\mathbb Q(\sqrt 2)\) from Chapter 1 or its figure, not from Theorem 2.15 unless that theorem is the ramification criterion and the citation says the criterion.

## How the subtitle is delivered

The parts keep their catalog names. *Their Hidden Rhythm* is what they hear.

Zeros and Sieves is the rhythm of zeros, short intervals, sieves, and exponential sums over primes. Bombieri–Vinogradov, the Riemann hypothesis on average, is the climax of that part. Additive Problems and Bounded Gaps is the rhythm of additive structure and of gaps. Partitions and Waring leave, because they are not primes. Three primes stays, so the part name remains true: an additive problem, then the bounded-gap theorems. No rename is proposed. Structure in the Primes is Halász, the additive lemmas Roth needs, Roth, the \(W\)-trick, and the critical line.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | Zeros and Sieves | 1–5 |
| II | Additive Problems and Bounded Gaps | 7–9, after Waring leaves Chapter 7. Chapter 6 moves. |
| III | Structure in the Primes | 10–14 |

**Moves.**

| Chapter | File | Where it goes |
| --- | --- | --- |
| 6 Partitions | `ch06-partitions.tex` | Book 5, *From Formula to Insight*. The Hardy–Ramanujan formula is the insight of the partition generating function. The proof moves with it. Book 14 cites the circle method's shape and does not keep a chapter about \(p(n)\). |
| Waring's problem, inside Chapter 7 | `ch07-waring.tex` | Book 5, beside that formula. Three primes stays here. The chapter is retitled around the primes. |

Additive combinatorics in Chapter 11 stays, because the next two chapters use it on the primes. The opening sentence says so. A section that never mentions a prime becomes an exercise of Roth's chapter, not its own subject. The sine kernel this book cites now lives in Book 8. The citation changes. The theorem does not.

---

### Part I. Zeros, Sieves and Averages

#### Chapter 1. Zeros and Primes in Short Intervals

**Status.** KEEP — `tome14-primes/chapters/ch01-zeros.tex` (425 lines). Huxley, Baker–Harman–Pintz, and Guth–Maynard stay labelled "quoted, not proved".

**Hook.** Is there always a prime between \(x\) and \(x+\sqrt x\)? The Riemann hypothesis would only just fail to say so. A weaker zero-density theorem already finds primes in shorter intervals than the classical zero-free region, and longer than \(\sqrt x\).

**Synopsis.** From zeros to primes in short intervals, mean values of Dirichlet polynomials, zeta as a Dirichlet polynomial, mollifiers, and Carlson's density theorem. The theorem is primes in every interval of length \(x^\theta\) for \(\theta>3/4\), or the exponent the file achieves. Book 15 cites this and does not reprove Carlson.

**Proved.** Carlson's zero-density estimate. The short-interval prime theorem that follows from it.

**Examples.** The end of Carlson's exponent with a mollifier of length \(T\), the exercise the review checked. One numerical interval.

**Figures.** Two.

#### Chapter 2. Siegel's Theorem

**Status.** KEEP — `chapters/ch02-siegel.tex` (428 lines). The constant is ineffective, and the chapter says so. Book 15's Maier argument may use Siegel–Walfisz and must keep the constant ineffective.

**Hook.** A real character might have a zero very close to 1. Nobody has found one. Siegel showed that if it exists it is extremely close, at the price of a constant nobody can compute.

**Synopsis.** The zero-free region and the exceptional zero, Siegel's theorem, Siegel–Walfisz, and class numbers. \(L(1,\chi)\gg_\varepsilon q^{-\varepsilon}\), ineffectively, is the only proved constraint on how small \(h(-d)\) can be. Book 13 computed class numbers. This chapter bounds them. Book 15 will say the bound does not yield Cohen–Lenstra.

**Proved.** Siegel's theorem. Siegel–Walfisz. The class-number lower bound of the strength the file gives.

**Examples.** A real character and its \(L(1,\chi)\), computed, against the ineffective bound, so the reader sees that the theorem does not help the computation.

**Figures.** None in the inventory. A figure is optional. Do not add one for decoration.

#### Chapter 3. Sieves and the Parity Problem

**Status.** KEEP — `chapters/ch03-sieves.tex` (561 lines). The parity obstruction for twins is "believed, not proved". Chen is quoted. Buchstab's function is drawn, and the fundamental lemma is proved for large \(u\). The fixed-range Buchstab theorem is Book 15's. This chapter must not be cited as if it contained that theorem.

**Hook.** A sieve counts what survives when the multiples of small primes are struck out. It can count almost-primes. It cannot, by itself, tell the primes from the almost-primes.

**Synopsis.** The fundamental lemma, the parity problem for the Liouville weight, and Artin's conjecture under the generalised Riemann hypothesis. The parity barrier is a theorem about a weight the sieve does not see. For twins it is a belief. Book 15 repeats the logical shape and not the combinatorial details, and it keeps the same care.

**Proved.** The fundamental lemma for large \(u\). The parity obstruction for the primes, in the form "a sieve that does not see the Liouville function cannot tell the primes from the almost-primes".

**Examples.** A small sieve that stops at the parity wall. One numerical fundamental-lemma count.

**Figures.** Two. Buchstab's function is one of them, drawn, not proved in the fixed-range form.

#### Chapter 4. The Large Sieve and Bombieri–Vinogradov

**Status.** KEEP — `chapters/ch04-largesieve.tex` (437 lines). The level is \(\sqrt x\,(\log x)^{-A}\), and the constant cannot be computed. That sentence stays. This is the climax of Part I: the Riemann hypothesis on average.

**Hook.** One modulus at a time, the Riemann hypothesis is out of reach. On average over the moduli up to \(\sqrt x\), it is a theorem.

**Synopsis.** The large sieve for characters, Vaughan's identity, bilinear forms, Bombieri–Vinogradov, the Barban–Davenport–Halberstam variance, and Linnik's theorem on the least quadratic non-residue. Book 6 proved the large sieve and stopped. This chapter spends it. Book 15 does not reprove it. Gallagher's weighted theorem in Book 15 is a different input, for one modulus, and Book 15's wrapper already says Bombieri–Vinogradov does not replace it.

**Proved.** Bombieri–Vinogradov for \(\theta<\tfrac12\), ineffective via Siegel. Vaughan's identity.

**Examples.** A level of distribution written as \(\sqrt x/(\log x)^A\). One bilinear form estimated by Vaughan.

**Figures.** Two.

### Part II. The Circle Method

#### Chapter 5. Exponential Sums over Primes

**Status.** KEEP — `chapters/ch05-expsums.tex` (390 lines). Book 6 owns Weyl and van der Corput for smooth phases. This chapter owns sums over primes. The Vinogradov mean value theorem and Weil's Kloosterman bound stay quoted.

**Hook.** Multiply the primes by an irrational and keep the fractional parts. They fill the unit interval. Vinogradov proved it.

**Synopsis.** Rational approximations, Vinogradov's estimate for exponential sums over primes, the mean value theorem as a quotation, and Kloosterman and Salié sums. These sums are the beams of the circle method. A saddle-point remark may cite Book 5 if the complex saddle was added there. The chapter stands without it.

**Proved.** Vinogradov's bound for \(\sum_{p\le x}e^{2\pi i\alpha p}\), of the strength the file proves.

**Examples.** A geometric sum over primes in a short arc. One Kloosterman sum modulo a small prime.

**Figures.** Two.

#### Chapter 6. The Circle Method I: Partitions

**Status.** MOVE — `chapters/ch06-partitions.tex` (251 lines), to Book 5. Partitions are not the hidden rhythm of the primes. Rademacher's exact formula stays quoted. The Hardy–Ramanujan proof moves with the chapter. Book 5 introduced the generating function and did not prove the asymptotic. It will.

**Hook.** Four has five partitions. Two hundred has nearly four trillion. There is a formula.

**Synopsis.** The generating function, the Dedekind eta function from Book 6's taste, the major and minor arcs, and the Hardy–Ramanujan asymptotic with an error \(O(n^{-1/4})\) or the error the file proves. The circle is the method's picture: most of the integral is a small arc near a rational of small denominator.

**Proved.** The Hardy–Ramanujan asymptotic for \(p(n)\), with the error term the chapter achieves.

**Examples.** \(p(200)\) against the formula. One major arc, written.

**Figures.** Two.

#### Chapter 7. The Circle Method II: Three Primes and Waring's Problem

**Status.** SPLIT — `chapters/ch07-waring.tex` (396 lines). Three primes stays. It is the rhythm. Waring's problem moves to Book 5 with the partition asymptotic. Every large odd number is a sum of three primes, proved, ineffective. Helfgott's theorem, every odd number greater than 5, is stated. Waring for \(s\ge 2^k+1\) is proved. Positivity of the singular series is quoted where the file quotes it. The ineffective constant is the same Siegel constant as in Chapters 2 and 4, and one sentence says so.

**Hook.** Goldbach's letter to Euler, 7 June 1742. Every large odd number is three primes. Vinogradov proved it.

**Synopsis.** The singular series, Vinogradov's three-prime theorem, Weyl's inequality and Hua's lemma as used here, and Waring's problem. Three primes is the climax of the circle method on this floor. Schnirelmann's theorem, that the primes are an additive basis of finite order, lives in the workshop appendix this plan cuts. A remark in Book 15's sieve chapter may point at it. It is not reproved here.

**Proved.** Vinogradov's three-prime theorem, for all sufficiently large odd numbers, with an ineffective threshold. Waring's problem for \(s\ge 2^k+1\).

**Examples.** A small odd number as three primes. The singular series of a named equation, computed.

**Figures.** Two.

### Part III. Gaps and Bounded Gaps

#### Chapter 8. Small Gaps between Primes

**Status.** KEEP — `chapters/ch08-gpy.tex` (389 lines). The GPY theorem is conditional on a level of distribution past \(\tfrac12\). Zhang is quoted. The conditional heading stays.

**Hook.** On average, consecutive primes near \(x\) differ by about \(\log x\). How close can they come, infinitely often? In 2005 nobody could prove a gap smaller than the average.

**Synopsis.** Admissible tuples, sieve weights, sums of multiplicative functions, the two asymptotic formulas, the GPY weights, and Zhang's theorem as a quotation. The method is a weighted sieve that detects at least two primes in a tuple if the level of distribution is good enough. Bombieri–Vinogradov is just short of the level GPY needs. That sentence is the joint into Maynard's chapter.

**Proved.** The GPY criterion, as a conditional theorem. The asymptotic formulas for the weights, under the level the chapter assumes.

**Examples.** An admissible tuple of small diameter. One weight, written for \(k=2\) or the smallest case the file computes.

**Figures.** Two.

#### Chapter 9. Bounded Gaps between Primes

**Status.** KEEP — `chapters/ch09-maynard.tex` (295 lines). The sieve deduction is a theorem. The bound \(p_{n+1}-p_n\le 600\) rests on \(M_{105}>4.002\) and Engelsma's tuple, and the file now says the witness is not printed. Polymath's \(246\) is quoted. Leave the honesty. Printing the witness would be an expansion, not a repair of a false proof. The case \(k=5\) is an explicit rational and can be checked.

**Hook.** In May 2013 the record for a bounded gap was seventy million. By November it was six hundred, and the new proof did not need Zhang's equidistribution theorem.

**Synopsis.** The variational problem, many primes in bounded intervals, and the six-hundred bound with its certificate labelled. Maynard's theorem in the form "\(M_k>4m\) and level \(\theta<\tfrac12\) give \(m+1\) primes" is the theorem Book 15 is allowed to cite. The number 600 is cited only with the sentence that the certificate is not in the book, or not at all.

**Proved.** The reduction to \(M_k\). The case \(k=5\), with the rational \(1417255/708216\). The bounded-gap theorem for an admissible tuple once \(M_k\) is large enough.

**Examples.** The 5-tuple \(\{0,2,6,8,12\}\). The figure of \(M_k\) against the upper bound, captioned so the plotted values are not mistaken for a proof of \(M_{105}>4.002\).

**Figures.** Two.

### Part IV. Structure in the Primes

#### Chapter 10. Multiplicative Functions

**Status.** KEEP — `chapters/ch10-halasz.tex` (383 lines). Halász, Delange, Wirsing, and the mean of \(\mu\) are proved. Matomäki–Radziwiłł is quoted. Book 15's random-multiplicative chapter uses Halász and does not reprove it.

**Hook.** A multiplicative function is decided by its values at the primes. When is its average decided as well?

**Synopsis.** Pretentious distance, Halász's theorem, Delange and Wirsing, and the mean of the Möbius function by this route, beside Book 6's deduction from the prime number theorem. Pretentiousness is the language Book 15 will use to explain, without proving, the Lemke Oliver–Soundararajan bias.

**Proved.** Halász's theorem. The Delange–Wirsing theorem in the form stated. \(\sum_{n\le x}\mu(n)=o(x)\) by this method, if the chapter includes it, labelled as a second proof of Book 6's theorem.

**Examples.** A pretentious distance from \(\mu\) to a real character, numerical and small. One multiplicative function whose mean is a product.

**Figures.** Two.

#### Chapter 11. Additive Combinatorics

**Status.** KEEP — `chapters/ch11-additive.tex` (407 lines). Plünnecke–Ruzsa, Balog–Szemerédi–Gowers, Elekes, and Freiman's theorem in \(\mathbb F_2^n\) are proved. Freiman's theorem in \(\mathbb Z\) is quoted.

**Hook.** Add a set to itself. If almost nothing new appears, the set was an arithmetic progression, or a subspace, or a large piece of one.

**Synopsis.** Small doubling, Ruzsa's inequalities, Plünnecke, Freiman in \(\mathbb F_2^n\), Balog–Szemerédi–Gowers, and sum-product. Structure means the set correlates with a subgroup or a progression. Randomness, in the next chapters, means a norm is small. The dichotomy is named here in examples and proved for length-three progressions in Chapter 12.

**Proved.** Plünnecke–Ruzsa. Balog–Szemerédi–Gowers. Freiman's theorem in \(\mathbb F_2^n\). Elekes's sum-product bound.

**Examples.** An arithmetic progression, doubling 2. A random set, doubling about the square of its size. One subspace of \(\mathbb F_2^n\).

**Figures.** Two.

#### Chapter 12. Roth's Theorem

**Status.** REVISE — `chapters/ch12-roth.tex` (263 lines). The density-increment proof is complete, with the bound \(500N/\log\log N\) or the bound the file proves. Book 11 proves the same theorem by ergodic theory. The two introductions name each other. Szemerédi and Kelley–Meka stay quoted. Behrend's construction stays, as the matching lower bound of a different shape.

**Hook.** How many integers below \(N\) can you choose with no three in arithmetic progression? Fewer than a vanishing proportion.

**Synopsis.** Fourier analysis on \(\mathbb Z/N\mathbb Z\), the density increment, and the theorem. A set either correlates with a character, and the density increments on a progression, or it is uniform, and the count of progressions matches the random model. That sentence is the \(U^2\) case of the dichotomy Book 15 will retell. This chapter owns the proof. Book 15 does not give a third one.

**Proved.** Roth's theorem. The \(U^2\) inverse theorem in the form "large Fourier coefficient". The density increment.

**Examples.** A long progression, which has three-term progressions. Behrend's construction, described, with the exponent the chapter states.

**Figures.** Two.

#### Chapter 13. Gowers Norms and the Green–Tao Theorem

**Status.** KEEP — `chapters/ch13-gowers.tex` (281 lines). The title says "quoted" for Green–Tao, and the text separates the \(W\)-trick, which is proved, from the relative Szemerédi theorem, which is not. The inverse theorem for \(U^{s+1}\), the linear forms condition, and the relative Szemerédi theorem stay quoted. Every cross-reference in Book 15 keeps the word "quoted".

**Hook.** Fourier analysis sees progressions of length three. For length four it is blind. A new norm is needed. With it, the primes contain arbitrarily long arithmetic progressions, a theorem this book quotes.

**Synopsis.** The Gowers norms, the generalised von Neumann theorem, and the \(W\)-trick. The primes are biased modulo small primes. After the \(W\)-trick removes that bias, a transference argument would finish the proof, and the transference is quoted. The singular series for prime progressions, if it is computed here, is a theorem and can be cited. The capstone does not contain a proof of Green–Tao.

**Proved.** The \(U^2\) inverse theorem, the generalised von Neumann inequality, and the \(W\)-trick. The Gowers norms' basic properties.

**Examples.** The \(U^2\) norm as an \(\ell^4\) norm of the Fourier transform, the exercise the review checked. A quadratic phase with \(U^3\)-norm 1. The \(W\)-trick modulo 6, on a short interval of primes.

**Figures.** Two.

#### Chapter 14. The Critical Line

**Status.** KEEP — `chapters/ch14-critical.tex` (516 lines). The approximate functional equation is a quoted theorem of Hardy and Littlewood. Book 15's moments chapter either proves it or marks every use of it. Montgomery's pair correlation is proved under the Riemann hypothesis for \(0\le\alpha\le 1-\varepsilon\). The form factor for \(\alpha\ge 1\) is Montgomery's conjecture. A positive proportion of zeros on the critical line is quoted. Book 12's Theorem 11.13 points here, at the fifteenth numbered statement, and the numbers match. Do not renumber this chapter without updating that citation.

**Hook.** Riemann guessed that all the zeros lie on one line. Nobody has proved it. Infinitely many do lie on it, and, if he was right, their spacings match a random matrix on a limited range.

**Synopsis.** Hardy's theorem, the mean square on the critical line, and Montgomery's pair correlation. The mean square \(\frac1T\int_0^T|\zeta(\tfrac12+it)|^2\,\mathrm dt\sim\log(T/2\pi)\) is a theorem. The fourth moment is Ingham's, quoted. This is not a central limit theorem for \(\log|\zeta|\). Book 15 proves that different theorem and says the difference in one sentence.

**Proved.** Infinitely many zeros on the critical line. The mean square on the critical line. Montgomery's theorem for \(0\le\alpha\le 1-\varepsilon\), under the Riemann hypothesis.

**Examples.** A numerical mean square against \(\log(T/2\pi)\). One pair correlation at a height the book can compute, labelled as a computation.

**Figures.** Three.

## Owns, defers, hands forward

**Owns.** Carlson's zero density and primes in intervals of length \(x^\theta\), \(\theta>3/4\). Siegel, Siegel–Walfisz, and the shared ineffective constant. The fundamental lemma and the parity obstruction for the Liouville weight. Bombieri–Vinogradov. Vinogradov's exponential sums over primes. The Hardy–Ramanujan asymptotic. Three primes. Waring for \(s\ge 2^k+1\). The GPY criterion as a conditional theorem. Maynard's sieve deduction, with \(600\) labelled. Halász. Roth by Fourier analysis. The \(W\)-trick, the Gowers norms, and the \(U^2\) inverse theorem. Hardy's theorem, the critical-line mean square, and Montgomery for \(\alpha\le 1-\varepsilon\).

**Defers.** Buchstab's fixed-range theorem and Maier's theorem (Book 15). Green–Tao, the higher inverse theorems, and the relative Szemerédi theorem, quoted. Chen, Zhang, a positive proportion of critical zeros, the Vinogradov mean value theorem, Rademacher, Helfgott, Matomäki–Radziwiłł, quoted. The approximate functional equation, quoted. The form factor for \(\alpha\ge 1\).

**Hands forward.** The rhythm, heard as far as the method reaches. Book 15's subtitle is the meeting of structure and randomness. This book has both on the page, in Roth's dichotomy and in Montgomery's theorem, and it does not yet say they are one dictionary.

## Pages and effort

Baseline 211 pages. Target 210–230. Effort: light. The book is in the form a later volume can cite. The work is the Roth cross-reference, the discriminant pointer if it is still wrong, and the discipline of the word "quoted".
