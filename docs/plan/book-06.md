# Book 6 — Crossroads

*Arithmetic Meets Analysis.* The on-disk subtitle is "Where Numbers Meet Infinity".

**Element.** The great span. The first arch that asks the primes to be both a law and a game of chance. The arch holds in bulk. A crack is marked.

**On disk.** Volume 5, `tome5-meets`. Twelve chapters. About 176 pages in the 7×10 table. The October review scored it 7, and the two errors it named are repaired: the names \(\liminf\) and \(\limsup\) in `ch01-mertens.tex`, and the Brun–Titchmarsh paragraph in `ch08-sieves.tex`. Maier's theorem is a remark in `ch10-random.tex`.

## Promise

The primes thin out irregularly, twins keep appearing, and no formula produces the next prime. In bulk they obey laws. This book proves the laws that close the first part of the series: Dirichlet's theorem, the prime number theorem, the explicit formula, the classical zero-free region, Selberg's sieve, and Erdős–Kac. Cramér's model is described, and Maier's theorem is stated as a fact whose proof is Book 15. A modular form appears at the end, long enough to show that the masonry has a further storey.

This is the turn of the story. The preface should say the series question in the form the span can touch: the explicit formula writes the primes as waves, one per zero, and Erdős–Kac writes \(\omega(n)\) as a Gaussian. Both are theorems. They are not yet a dictionary.

## Prerequisites

Book 2: characters, Möbius inversion, the Legendre sieve, Chebyshev's bounds. Book 3: orthogonality of characters. Book 4: means, variances, characteristic functions, Borel–Cantelli. Book 5: \(\zeta(2k)\), Stirling, Weyl, the Gauss-sum sign, residues, the Euler product, the functional equation. Fubini–Tonelli remains an admitted, labelled fact.

Throughout, \(\log\) is the natural logarithm and \(p\) is a prime. \(\mathrm{Li}(x)=\int_2^x\mathrm dt/\log t\).

## How the subtitle is delivered

The subtitle is one meeting: arithmetic meets analysis. A chapter stays only if both are on the page.

| Chapter | The arithmetic | The analysis |
| --- | --- | --- |
| 1–2 Mertens and averages | Primes and divisor functions | Partial summation and the hyperbola |
| 3–4 Characters and Dirichlet | Residue classes | \(L(1,\chi)\ne 0\) |
| 5 The prime number theorem | \(\pi(x)\) | A zero-free line and a tauberian theorem |
| 6–7 Zeros and the explicit formula | \(\psi(x)\) | Contours, Hadamard products, waves |
| 8 Sieves | Survivors of small primes | A quadratic form and an \(L^2\) bound |
| 9 Erdős–Kac | \(\omega(n)\) | The bell curve |
| 10 Random models | The primes | Borel–Cantelli, from Book 4, fed by the analytic count |
| 11 Exponential sums | Primes and characters | Weyl and van der Corput |
| 12 A taste of modular forms | \(\tau(n)\) and Eisenstein series | Complex analysis on the upper half-plane |

Chapter 12 stays a meeting, not a second Book 13. The valence formula, Hecke's general theory, and modularity stay in Book 13. What stays here is the exhibit: \(E_4^2=E_8\) and \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\). No chapter fails the subtitle.

The cut with Book 14, already in the preface, stays: this book ends at the classical explicit formula, Selberg's sieve, Erdős–Kac, and the shape of Cramér's model. Bombieri–Vinogradov, the circle method, and a positive proportion of zeros on the critical line are Book 14.

---

### Part I. Counting Primes

#### Chapter 1. Mertens's Theorems

**Status.** KEEP — `tome5-meets/chapters/ch01-mertens.tex` (356 lines). The liminf and limsup are now named correctly.

**Hook.** Euler, on the primes: mathematicians have tried in vain to find some order in them, and we have reason to believe it is a mystery the mind will never penetrate. The chapter then proves three theorems about their averages.

**Synopsis.** Chebyshev's functions, Mertens's theorems, the divergence of \(\sum 1/p\), and the Mertens product. The opening corollary is that if \(\theta(x)/x\) has a limit, the limit is 1. The prime number theorem is not this corollary. A sentence says so.

**Proved.** \(\sum_{p\le x}(\log p)/p=\log x+O(1)\). The Mertens product. \(\sum_{p\le x}1/p=\log\log x+M+O(1/\log x)\), at the precision the file gives. The Chebyshev liminf and limsup bounds.

**Examples.** The product up to \(\sqrt{10^6}\) set against \(1/\log n\), with the discrepancy tied to the failure of independence past \(\sqrt n\). One partial sum of \(1/p\).

**Figures.** Two.

#### Chapter 2. Arithmetic Functions on Average

**Status.** KEEP — `chapters/ch02-averages.tex` (448 lines).

**Hook.** Kronecker: God made the integers; all else is the work of man.

**Synopsis.** Mean values, error terms, the hyperbola method, and Dirichlet's divisor problem. The average of \(d(n)\) is the theorem Book 15's exercises will quote. The hyperbola method is partial summation made geometric.

**Proved.** The Dirichlet divisor estimate with the error term the chapter achieves. The mean of \(\varphi(n)\), \(\sigma(n)\), or \(\mu(n)\), whichever theorems are numbered. Partial summation.

**Examples.** A numerical divisor sum against \(x\log x\). One hyperbola splitting drawn for a small \(x\).

**Figures.** Two.

#### Chapter 3. Dirichlet Characters and \(L\)-Functions

**Status.** KEEP — `chapters/ch03-characters.tex` (459 lines). Book 2 defined characters. This chapter builds \(L(s,\chi)\).

**Hook.** Jacobi, on Dirichlet's use of Fourier series in number theory.

**Synopsis.** Characters, primitive characters, Gauss sums, \(L\)-functions, the non-vanishing of \(L(1,\chi)\), and the class-number formula for the value \(L(1,\chi)\) in the cases the chapter proves. Book 13's class-number formula cites this value, including the odd-character formula. The numbering has to stay stable, or Book 13's citation has to be updated in the same pass.

**Proved.** Orthogonality, if it is reproved, or the citation to Book 2. Non-vanishing of \(L(1,\chi)\) for \(\chi\) non-principal, including Landau's argument for a real character. The evaluation of \(L(1,\chi)\) the file contains. Gauss sums.

**Examples.** \(L(s,\chi_4)\) and its value at 1. One Gauss sum computed two ways.

**Figures.** Two.

#### Chapter 4. Dirichlet's Theorem

**Status.** KEEP — `chapters/ch04-dirichlet.tex` (300 lines). A three-star exercise is a small EXPAND. The theorem itself is the first great lock in the masonry: an arithmetic progression that can contain primes contains infinitely many.

**Hook.** Dirichlet: an unbounded arithmetic progression whose first term and difference are coprime contains infinitely many primes.

**Synopsis.** The proof from \(L(1,\chi)\ne 0\), the consequences, and the sense in which the primes are equally distributed among the admissible classes. Equal distribution here is an infinitude in each class, or a Dirichlet density. Natural density in the form of the prime number theorem for progressions waits until Chapter 5, and only for fixed modulus.

**Proved.** Dirichlet's theorem.

**Examples.** The progression \(4n+3\), or \(5n+2\), with the characters written. One progression a congruence forbids.

**Figures.** Two.

#### Chapter 5. The Prime Number Theorem

**Status.** KEEP — `chapters/ch05-pnt.tex` (522 lines). Newman's proof in Zagier's form is the climax of Part I. The text already separates "no zero on \(\mathrm{Re}\,s=1\)" from the tauberian machine. Keep that separation: it is the span's two members, an arithmetic zero-free line and an analytic machine.

**Hook.** Gauss, recognising that the frequency of primes is on average inversely proportional to the logarithm.

**Synopsis.** The logarithmic derivative of zeta, the zero-free line \(\mathrm{Re}\,s=1\), Newman's theorem, and the passages \(\psi\sim x\), \(\theta\sim x\), \(\pi(x)\sim x/\log x\). The mean of the Möbius function. The prime number theorem in arithmetic progressions for a fixed modulus, if the chapter proves it.

**Proved.** No zeros on \(\mathrm{Re}\,s=1\). Newman's tauberian theorem in the form used. The prime number theorem. \(\sum_{n\le x}\mu(n)=o(x)\).

**Examples.** \(\pi(10^8)=5761455\), and \(\mathrm{Li}(x)-\pi(x)=753\) with the integral from 2. The numerical caption stays, because it fixes the normalisation of \(\mathrm{Li}\).

**Figures.** Two.

### Part II. Zeros and Explicit Formulas

#### Chapter 6. The Zeros of Zeta

**Status.** KEEP — `chapters/ch06-zeros.tex` (532 lines). REVISE the sentence that more than \(41\%\) of the zeros lie on the critical line. A moving numerical bound is not a theorem. Book 14 marks a positive proportion as quoted. This chapter should too, or delete the percentage. The completed zeta, if it is called \(\Lambda(s)\) "only here", gets the notation warning in the first line of the section.

**Hook.** Riemann: one finds about this many real roots, and it is very probable that all roots are real. He means the \(\xi\) function.

**Synopsis.** Complex Stirling, the \(\xi\) function, a contour count of zeros, Hadamard's product, the Riemann–von Mangoldt formula, and a classical zero-free region. The zero-free region \(1-\beta\ge c/\log(|t|+2)\) is the theorem. The Riemann hypothesis is stated and not proved.

**Proved.** The zero-counting formula. Hadamard factorisation at the level the chapter reaches. The classical zero-free region of the strength \(1-\beta_0\ge 1/(14A'\log|t|)\), or whatever constant the repaired file proves. The review checked that constant's argument.

**Examples.** A zero count up to a small height, against the formula. One zero-free rectangle.

**Figures.** One.

#### Chapter 7. The Explicit Formula and the Riemann Hypothesis

**Status.** REVISE — `chapters/ch07-explicit.tex` (512 lines). The explicit formula for \(\psi_0(x)\) is a theorem of this book. The formula for \(\psi(x,\chi_{-4})\) uses the functional equation of \(L(s,\chi)\), which Book 13 proves for primitive Dirichlet \(L\)-functions. Until a reader has Book 13, that step is a quotation, labelled, or the bias identity is stated with the functional equation as a hypothesis this book does not discharge. Von Koch's equivalence stays.

**Hook.** Hilbert, waking after a thousand years and asking whether the Riemann hypothesis has been proved.

**Synopsis.** Perron's formula, the explicit formula, the error term in the prime number theorem, the Riemann hypothesis as a statement about \(\psi(x)-x\), and Chebyshev's bias. The explicit formula is the span made visible: the primes are a smooth main term plus a wave for each zero. Chebyshev's bias is the first place a random model is not just incomplete but skewed. Book 15 returns to it and either proves the logarithmic-density integral or cites this chapter.

**Proved.** The explicit formula for \(\psi_0(x)\). Von Koch's equivalence. The classical error term that follows from the zero-free region. The bias identity in the form that remains after the functional equation of \(L(s,\chi_{-4})\) is labelled.

**Examples.** The race \(\pi(x;4,3)-\pi(x;4,1)\), with the first crossing near \(26861\) if the chapter discusses it. One truncated explicit formula against \(\psi(x)-x\).

**Figures.** One.

### Part III. Sieves and Randomness

#### Chapter 8. Sieves

**Status.** KEEP — `chapters/ch08-sieves.tex` (463 lines). The Brun–Titchmarsh paragraph now says the short-interval ratio is \(2k\), and that the constant 2 which bears on Siegel zeros is the arithmetic-progression inequality. Book 14 owns that inequality's consequences and the parity problem.

**Hook.** Eratosthenes' sieve is two thousand years old, and for most of that time it was the only algorithm that counted primes.

**Synopsis.** Why Legendre's sieve, from Book 2, fails when the level is too high. Selberg's sieve. The large sieve, used for a square-sieve application and not pushed to Bombieri–Vinogradov. Brun's upper bound for twins. Buchstab's function is not defined here. Book 6's Chapter 10 must not say it was met in sieve theory. Book 15 proves Buchstab.

**Proved.** Selberg's upper-bound sieve. Brun's theorem that the twin sum converges, or the upper bound of the strength the file gives. The large sieve inequality. The short-interval Brun–Titchmarsh inequality in the repaired form.

**Examples.** A Selberg sieve for twins at a small level, with the weights written. One numerical upper bound next to the true count.

**Figures.** One.

#### Chapter 9. The Erdős–Kac Theorem

**Status.** KEEP — `chapters/ch09-erdoskac.tex` (338 lines). This is the Gaussian's return, and it is the first complete proof. Book 15's Kubilius model re-derives it as a corollary and compares the two proofs. It does not replace this one.

**Hook.** Kac: primes play a game of chance.

**Synopsis.** Turán's second-moment bound, the model of small prime factors as independent coins, the passage from moments or characteristic functions to the bell curve, and the theorem. A typical integer near \(x\) has about \(\log\log x\) distinct prime factors, with Gaussian fluctuations of size \(\sqrt{\log\log x}\).

**Proved.** Erdős–Kac, with the Kubilius truncation the file uses. Turán's variance bound.

**Examples.** \(\omega(n)\) against \(\log\log n\) up to a named bound, if a figure exists; otherwise the theorem's statement with one numerical \(n\). The proportion of integers with \(\omega(n)\) in a named range.

**Figures.** One.

#### Chapter 10. Random Models of the Primes

**Status.** KEEP — `chapters/ch10-random.tex` (469 lines). Maier is a remark, headed as quoted. REVISE the phrase that the oscillating factor "is given by Buchstab's function, met in sieve theory", if it is still there. Point to Book 15, where Buchstab is proved. Gallagher's average of the singular series, if it is a theorem of this chapter, stays a theorem. The Poisson law stays conditional.

**Hook.** The primes look as if something were throwing dice, and the dice are not quite fair.

**Synopsis.** Cramér's coins with \(P(n\text{ is prime})=1/\log n\). The almost-sure gap bound the model gives. What the model cannot see: the singular series. A first form of the twin constant on average. Maier's theorem as a remark: for every \(\lambda>1\), the short-interval count is sometimes too large and sometimes too small. This remark is the crack in the span. Book 15 fills it.

**Proved.** The Borel–Cantelli consequences of the model that use only Book 4: the prime number theorem with probability 1 inside the model, and the gap bound \(O((\log x)^{2+\varepsilon})\) almost surely. Gallagher's average, if the file proves it.

**Stated.** Maier. Granville's refinement. The Hardy–Littlewood conjectures, as conjectures.

**Examples.** A sample of the model up to a small limit, compared with the primes. The twin constant as a numerical product.

**Figures.** Two. The Poisson histogram near \(10^9\), if it is this chapter's, should be drawn so Book 15 can return to it and mark the variance defect.

### Part IV. Exponential Sums and a First Modular Form

#### Chapter 11. Exponential Sums

**Status.** KEEP — `chapters/ch11-sums.tex` (430 lines). Book 14 owns exponential sums over primes, Vaughan's identity, and the Vinogradov mean value theorem. This chapter owns Weyl differencing and van der Corput for smooth phases.

**Hook.** Poincaré: mathematics gives the same name to different things. An exponential sum is the name.

**Synopsis.** Geometric sums, Weyl differencing, square-root cancellation as a standard rather than a theorem for every sum, van der Corput, and character sums. The Polya–Vinogradov inequality, if proved, is the character-sum theorem.

**Proved.** Weyl's inequality in the form stated. Van der Corput's estimate. The geometric-sum bound.

**Examples.** A quadratic Weyl sum. One geometric sum that is small because the phase is not integral.

**Figures.** One.

#### Chapter 12. A Taste of Modular Forms

**Status.** KEEP — `chapters/ch12-modular.tex` (484 lines), as a taste and a cliffhanger. REVISE the preface sentence of the chapter so it does not claim the theory Book 13 proves. The proofs that are here stay here: they are the reader's first sight of a modular form. REVISE the letter \(q\): after eleven chapters as a modulus, \(q=e^{2\pi i\tau}\) needs a sentence.

**Hook.** The old joke that modular forms are the fifth arithmetic operation. The chapter then computes.

**Synopsis.** The modular group, Eisenstein series, Dedekind's \(\eta\), a dimension count, and Hecke operators at the level of the Ramanujan discriminant. \(E_4^2=E_8\) and \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\) are the theorems worth keeping on this floor. Siegel's contour for \(\eta\) is part of the argument. Book 13 rebuilds the analytic theory and does not cite this chapter as the home of Hecke's functional equation.

**Proved.** \(E_4^2=E_8\). The congruence for \(\tau(n)\) modulo 691. The transformation law of \(\eta\) or of \(\Delta\), whichever the file finishes.

**Examples.** \(\sigma_7(2)=129=9+120\), the numerical check the review pinned. One coefficient of \(\Delta\).

**Figures.** Two.

## Crossroads problems that belong here

| Source | Home |
| --- | --- |
| `tomeP1-crossroads/chapters/ch14-meets.tex` | The sixteen Journeys. Jacobi and the four-square theorem sit with Book 2's sums of squares if the proof is elementary, and here if it uses modular forms or theta functions. "The zeros hear the primes" and "The primes hear the zeros" belong with Chapter 7. "The coin and the sign of \(\pi(x)-\mathrm{li}(x)\)" belongs with the bias section. Ramanujan's differential equations belong with Chapter 12. Dedekind sums and the Gauss-sum sign belong with Chapter 11 or Book 5. |
| `tomeP1-crossroads/chapters/ch13-average.tex` | End of Part I. The Lemke Oliver–Soundararajan count, \(17.7\%\) after a prime ending in 1, is stated here as a phenomenon and proved nowhere. Book 15 states the theorem and does not sketch a false proof. The figure moves with a precise citation. |
| `tomeP1-crossroads/chapters/ch13-average.tex`, the one-star problem whose part (d) asks for a zero-free error | Re-levelled. Part (d) is not a one-star exercise. It can live as a three-star problem on Chapter 5. |

## Owns, defers, hands forward

**Owns.** Mertens. Averages of arithmetic functions. Non-vanishing of \(L(1,\chi)\). Dirichlet's theorem. The prime number theorem by Newman. The classical zero-free region, the zero count, the explicit formula for \(\psi_0\), von Koch. Selberg, Brun, the large sieve. Erdős–Kac. The shape of Cramér's model. Weyl and van der Corput. \(E_4^2=E_8\) and \(\tau(n)\) modulo 691.

**Defers.** Bombieri–Vinogradov, Siegel's theorem, Vaughan's identity, the circle method, Halász, Maynard, a positive proportion of critical zeros, Montgomery's pair correlation (Book 14). Buchstab, Maier, Selberg–Delange, the Kubilius model as a named probability space (Book 15). The functional equation of a primitive \(L(s,\chi)\), as a proof (Book 13). The modularity theorem.

**Hands forward.** The span. Book 8 quotes the zero-free line and does not reprove it. Book 14 starts where this book stops. Book 15 fills the crack the Maier remark marked, and compares its Erdős–Kac proof with this one.

## Pages and effort

Baseline 176 pages. Target 190–220 once Part IV is named and the Crossroads Journeys that belong here are attached. Effort: moderate. The false steps are repaired. The remaining work is the \(41\%\) sentence, the Buchstab pointer, the labelling of \(\psi(x,\chi)\), the letter \(q\), and the preface's statement of the series question.
