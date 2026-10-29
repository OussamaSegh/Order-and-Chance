# Book 15 — Order and Chance

*The Meeting of Structure and Randomness.*

**Element.** The section through the building. The series subtitle is the hidden architecture. This floor is where the section is drawn, and the drawing's title is the meeting: structure on one side, randomness on the other, and the members that only look like one of them.

**Source.** `tome15-order-and-chance`. The catalog subtitle is *The Meeting of Structure and Randomness*. Parts I–IV are wrappers around `chapters/ra-*.tex`, five of them only a page long. Part V is the old workshop, twelve chapters, and appendices A–L are the conjecture tours. `chapters/preface.tex` still describes that longer book.

## Promise

The series question, asked in a form the previous floors have made precise. Can pure order and pure chance be told apart, and why do the primes look random yet obey laws? The answer is the meeting. A deterministic set can match the mean and the variance of a random model and still fail a short-interval test. That failure is Maier's theorem, proved here. A function built from the primes, \(\log|\zeta(\tfrac12+it)|\), is nevertheless Gaussian at a random height. That is Selberg's theorem, proved here. Between those two theorems the book files the other meetings: Kubilius, a random multiplicative function, a sieve read as an expectation, a class group and a Selmer group modelled by a random group, and the form factor shared by a zero and an eigenvalue. Conjectures stay in headings that say so. The book does not reprove the prime number theorem, Bombieri–Vinogradov, the sine kernel, Erdős–Kac, or Roth.

## Prerequisites

The floors that now hold the theorems this book cites. In particular: Book 6 for the prime number theorem, the explicit formula, Erdős–Kac, and the shape of Cramér's model; Book 8 for the sine kernel, the semicircle, and Mellin inversion, after the moves in `book-08.md` and `book-12.md`; Book 11 for Berry–Esseen, the Gauss map, and the ergodic proof of Roth; Book 13 for the class group, one 2-descent, and the functional equation of a primitive Dirichlet \(L\)-function; Book 14 for Siegel–Walfisz, Bombieri–Vinogradov, Halász, Maynard's sieve, the \(U^2\) inverse theorem, and Montgomery for \(\alpha\le 1-\varepsilon\).

## How the subtitle is delivered

The parts keep their catalog names. *The Meeting of Structure and Randomness* is what they do.

The Question asks what "random-like" will mean, sets Cramér's model against the primes, and proves Maier's theorem: matching a mean and a variance is not the same as being the model. Arithmetic Statistics is the meeting one statistic at a time: a random multiplicative function, short intervals, a sieve read as an expectation, a class group, and a rank. Spectra is the meeting of a zero and an eigenvalue: the form factor, the moments, and Selberg's theorem that \(\log|\zeta|\) is Gaussian at a random height. Structure versus Randomness is the dictionary, Roth's dichotomy told once, and Chebyshev's bias, where the structure wins. The Research Workshop is the same meeting practised as a skill: how to read a paper about it, and two projects that stop on the line between a theorem and a guess. The twelve-chapter tour and the appendices that are not this meeting leave the part. The part name stays. No rename is proposed.

The climax is two theorems this book owns: Maier's, in The Question, and Selberg's, in Spectra.

## Parts

| Part | Name | Chapters |
| --- | --- | --- |
| I | The Question | 1–3 |
| II | Arithmetic Statistics | 4–8 |
| III | Spectra | 9–11 |
| IV | Structure versus Randomness | 12–13 |
| V | The Research Workshop | 14, and the reading method kept from the old workshop |

---

### Part I. The Question

#### Chapter 1. Order and chance in the integers

**Status.** EXPAND — `tome15-order-and-chance/chapters/ch01-integers.tex` includes only `ra-anatomy.tex` (382 lines). The anatomy is the right quarry for friable integers and Dickman. The chapter still needs the glossary: which statistic is a theorem, which is a model, and which later chapter owns it. Normal order of \(\omega(n)\) is cited to Book 6, not reproved.

**Hook.** Three deterministic sequences that look random: the square-free integers, the integers with a prime factor in a short range, and the primes. One of them will fail a short-interval test in the next chapter.

**Synopsis.** The chapter fixes the word "random-like" before any model is built. A set can match a mean and a variance and still be the wrong shape on a short interval. Dickman's function is derived for the continuous friable model. Book 11 already met Dickman through random permutations. The citation runs back. The series question is stated in the form the rest of the floor will answer.

**Proved.** The Dickman delay equation for the continuous model. The normal-order statement, quoted from Book 6 or re-proved in a page from the draft if that page is shorter than the citation.

**Examples.** \(\omega(n)\) and \(\Omega(n)\) for \(n\le 30\). \(\rho'(u)=-\rho(u-1)/u\) on \([0,1]\) and after.

**Figures.** \(\omega(n)\) against \(\log\log n\), with a band of width \(\sqrt{\log\log n}\). Dickman's \(\rho\) against the proportion of friable integers.

#### Chapter 2. Models of the primes

**Status.** REVISE — `ch02-cramer.tex` includes `ra-largemoduli.tex` (344 lines) and `ra-gaps.tex` (339 lines). The proofs of Buchstab, Maier, and the Erdős–Rankin lower bound are the ones to keep. The wrapper already says why Siegel–Walfisz and Bombieri–Vinogradov do not replace Gallagher's weighted theorem. The zero-free hypothesis belongs in the theorem heading, not only in the wrapper.

**Hook.** Let each integer \(n\ge 3\) be prime with probability \(1/\log n\), independently. The model proves a prime number theorem and a gap bound. Then Maier shows the primes have puddles and droughts the coins cannot see.

**Synopsis.** This is the first half of the climax. Structure (the small primes, through Buchstab's weights) meets a random model and the model loses, on intervals of length \((\log x)^\lambda\). Granville's factor \(2e^{-\gamma}\) and the Ford–Green–Konyagin–Maynard–Tao bound stay quoted. Maynard's bounded gaps are Book 14's theorem, named as the other end of the same scale.

**Proved.** The Borel–Cantelli gap bound inside the model. Buchstab's theorem for \(u\) in a fixed range. Maier's theorem. The Erdős–Rankin lower bound in the form the draft proves.

**Examples.** A sample of the coins against the primes. A numerical Buchstab function.

**Figures.** Maier's matrix: rows of residue classes modulo \(P(z)\), two of them on opposite sides of 1.

#### Chapter 3. Independent prime divisors

**Status.** REVISE — `ch03-divisors.tex` includes `ra-additive.tex`, `ra-selbergdelange.tex`, and `ra-erdoskac.tex`. Keep Turán–Kubilius, the Kubilius model, and Selberg–Delange. Those are not in Books 1–14. Shrink `ra-erdoskac.tex` (248 lines) to a comparison with Book 6's proof. One proof is enough to cite later. This chapter owns the model. Book 6 owns the first complete argument. Book 11's mod-\(\varphi\) chapter points here.

**Hook.** The prime factors of a typical integer behave like independent coins. The bell curve of Book 6 is what those coins add up to.

**Synopsis.** Turán–Kubilius is the \(L^2\) theorem. Kubilius is the probability space. Selberg–Delange is the mean-value theorem Book 11 quotes, proved from a Hankel contour and Book 8's Mellin inversion. Erdős–Kac is a corollary in two pages, then a comparison of what each proof makes visible.

**Proved.** Turán–Kubilius. The Kubilius comparison for strongly additive functions. Selberg–Delange in the form Book 11 quotes. Erdős–Kac as a corollary, not as a second foundation.

**Examples.** The Turán–Kubilius inequality for \(\Omega-\omega\). The mean of \(d(n)\) from Selberg–Delange, set beside Book 6's elementary mean.

**Figures.** The Kubilius space as a product of local factors at the small primes. The distribution of \((\omega(n)-\log\log n)/\sqrt{\log\log n}\) against the Gaussian.

### Part II. Arithmetic Statistics

#### Chapter 4. Random multiplicative functions

**Status.** REVISE — `ch04-multiplicative.tex` includes `ra-randommult.tex` (292 lines) and `ra-polynomials.tex` (253 lines). The Steinhaus and Rademacher models are the meeting: structure (a multiplicative function) against randomness (independent values at the primes). Möbius is the point one would like to prove behaves like the model. Chowla and Sarnak stay conjectures. Orthogonality of \(\mu\) against a periodic sequence is proved. Shrink the polynomial file to a section. A random polynomial's Galois group is a meeting, and it is not a second chapter.

**Hook.** Toss a coin for every prime and multiply. The Riemann hypothesis becomes true at once, almost surely. The Möbius function is one point of that model, and the series does not know whether the point is typical.

**Synopsis.** Moments of both random models. Möbius orthogonality for periodic sequences, from Book 6's characters. Halász, from Book 14, identifies the pretentious distance from \(\mu\) to a character. Nilsequences are not in the series. The chapter says so, and does not sketch a proof it does not have.

**Proved.** The moment calculations. Periodic orthogonality. The Halász consequences for \(\mu\).

**Examples.** The variance of a partial sum. Orthogonality against the indicator of a residue class.

**Figures.** A Steinhaus walk in the plane against a Rademacher sum on the line. The partial sums of \(\mu(n)\) up to \(10^6\), on the scale \(\sqrt x\).

#### Chapter 5. Primes in short intervals

**Status.** NEW — `ch05-short.tex` is 15 lines. The file names Hardy–Littlewood, Gallagher, and Montgomery–Soundararajan and proves nothing.

**Hook.** Book 6 put three statements in one story: an almost-everywhere short-interval theorem, a conditional Poisson law, and a variance that is smaller than the Poisson variance. They are not the same statement.

**Synopsis.** Zero density from Book 14 is cited, not reproved. The pair second moment under the Hardy–Littlewood conjecture is proved, including the constant in the variance. Gallagher's Poisson law stays conditional on the uniform conjecture. Maier's theorem, already proved in Chapter 2, is why the pointwise asymptotic fails for fixed \(\lambda\). The chapter points at it. It does not prove it twice.

**Proved.** The pair second moment under Hardy–Littlewood, with the secondary constant. The deduction of the Poisson law from the uniform conjecture, as a conditional theorem.

**Examples.** The mean \(\lambda\) recovered from the diagonal. The constant \(\gamma+\log 2\pi-1\), numerically.

**Figures.** Book 6's histogram, with the predicted variance marked. A schematic that separates \(h=x^{0.1}\) from \(h=(\log x)^2\).

#### Chapter 6. Sieves as probability

**Status.** NEW — `ch06-sieves.tex` is 11 lines.

**Hook.** Inclusion–exclusion is an expectation. The parity barrier is what happens when the expectation cannot see a sign.

**Synopsis.** Bonferroni, Selberg's weights read as an \(L^2\) projection, and the parity obstruction Book 14 proved for the Liouville weight, retold and not recomputed. For twins the barrier is believed, not proved. The sentence Book 14 uses is repeated, not softened. Brun, Bombieri–Vinogradov, and Maynard are a list of citations. Chen is stated.

**Proved.** Bonferroni in probabilistic language. The equivalence, in one setting, between a sieve weight and an \(L^2\) projection.

**Examples.** A small sieve of twins, the partial expectations oscillating. The Selberg upper bound of 2 as a variational fact.

**Figures.** The partial inclusion–exclusion for \(\pi(10^4)\), leaving the true count when the parity wall is hit.

#### Chapter 7. Random groups in arithmetic

**Status.** REVISE — `ch07-classgroups.tex` includes `ra-cohenlenstra.tex` (285 lines). MERGE the cokernel theorem from `ch05-sandpiles.tex` into this chapter, then that workshop chapter is not a second home for the same proof. The heuristic is labelled as a heuristic. Genus theory is not in the series. The 2-part is stated as a different measure, not as a theorem of Book 13.

**Hook.** A group with many symmetries is a group arithmetic seems shy to produce. Cohen and Lenstra made that sentence into a measure.

**Synopsis.** The measure proportional to \(1/|\mathrm{Aut}(G)|\) on finite abelian \(p\)-groups, its moments, and one cokernel theorem about matrices. The class group of an imaginary quadratic field is the heuristic. Book 13 proves the class group is finite and ties \(h(-d)\) to \(L(1,\chi)\). It does not prove a moment. Siegel's bound, from Book 14, is the only proved constraint, and it is ineffective.

**Proved.** Convergence of the measure. \(\mathbb E\#\mathrm{Sur}(G,A)=1\). The cokernel theorem imported from the workshop.

**Examples.** \(|\mathrm{Aut}(\mathbb Z/p\times\mathbb Z/p)|\). The moment for \(A=\mathbb Z/p\).

**Figures.** The 3-part of \(h(-d)\) for \(|d|\le 10^5\) against the prediction. A histogram of coranks over \(\mathbb F_3\).

#### Chapter 8. Ranks of elliptic curves

**Status.** NEW — `ch08-ranks.tex` is 15 lines. It names Goldfeld and Poonen–Rains and proves nothing.

**Hook.** Book 13 proves that \(E(\mathbb Q)\) is finitely generated. It does not say how large the rank is. A random model does, and the model is not a theorem.

**Synopsis.** The 2-descent Book 13 wrote for \(y^2=x^3-x\) is rewritten as a Selmer group, for that family only. The linear algebra of two random maximal isotropics is proved. Goldfeld, Birch–Swinnerton-Dyer, Bhargava–Shankar, and modularity stay stated. The orbit method is not attempted. This is a meeting: the structure is the Selmer group, the randomness is a count of subspaces, and the identification is a conjecture in a heading that says so.

**Proved.** The distribution of the intersection of two random maximal isotropics. The 2-Selmer group of the congruent-number curve, as a rewrite of Book 13's descent.

**Examples.** One further curve in the family, the rank found by the descent. The probability for \(n=2\).

**Figures.** Rank frequencies against \(\tfrac12\) and against the Poonen–Rains prediction, the prediction labelled as a model. The congruent-number curve and its 2-isogeny.

### Part III. Spectra

#### Chapter 9. Random matrices and the zeros of zeta

**Status.** NEW — `ch09-gue.tex` is 15 lines. After the moves, the sine kernel and the semicircle live in Book 8. Montgomery's theorem lives in Book 14. This chapter does not reprove either.

**Hook.** Book 8 has a theorem about eigenvalues. Book 14 has a theorem about zeros, on a limited range. They are the same formula. The chapter puts the formula on one page and says where each side stops being a theorem.

**Synopsis.** Cite Book 14 for \(F(\alpha)=|\alpha|\) when \(0\le\alpha\le 1-\varepsilon\), under the Riemann hypothesis. Cite Book 8 for the sine kernel. Prove the form-factor identity if Book 8 still cites it to Mehta. Odlyzko's histogram is a computation, and the chapter says what a histogram cannot prove. The conjecture for \(\alpha\ge 1\) stays a conjecture.

**Proved.** The form-factor identity for the sine kernel, or an explicit citation if Book 8 has gained the proof in the move. Nothing else.

**Examples.** \(\int_0^1 F(\alpha)\,\mathrm d\alpha\) under the theorem and under the conjecture. The range \(\alpha\le 1\) read as a restriction on which prime sums in the explicit formula are visible.

**Figures.** The sine kernel and the form factor on the same axes. A gap histogram computed from zeros the notebook can reach, labelled as a computation.

#### Chapter 10. Moments of \(L\)-functions

**Status.** REVISE — `ch10-moments.tex` includes `ra-moments.tex` (269 lines). The file is a start. The chapter's job is the dictionary between a random-matrix moment, now Book 8's theorem, and a number-theoretic prediction. The fourth moment of zeta is Ingham's, quoted in Book 14. No higher moment is known. The approximate functional equation is quoted in Book 14. Either prove it here, in an appendix of about twenty pages, or mark every line of the recipe that uses it.

**Hook.** The mean of \(|\zeta|^2\) was known in 1918. The mean of \(|\zeta|^4\) in 1926. For the sixth moment, what arrived was a conjecture, and half of the conjecture is a random matrix.

**Synopsis.** The proved mean square, cited from Book 14. The integer moments of \(|\det(I-U)|\), cited from Book 8, with the second moment computed by hand so the chapter is not only a citation. The CFKRS recipe for the second and fourth moments, checked against Ingham, and stated for the sixth. Families are one example, the symmetry type named and not derived from a monodromy group.

**Proved.** The second-moment comparison, arithmetic side cited. The formal fourth-moment expansion, marked where it uses a quoted formula.

**Examples.** The second moment of \(|\det(I-U)|\) for \(U(2)\). The diagonal contribution in the fourth-moment recipe.

**Figures.** The partial integral of \(|\zeta(\tfrac12+it)|^2\) against \(\log(T/2\pi)\), cited from Book 14. The Keating–Snaith coefficients for \(k=1,2,3,4\) against the proved or quoted arithmetic constants.

#### Chapter 11. Value distribution

**Status.** KEEP — `ch11-values.tex` includes `ra-bohrjessen.tex` (265 lines) and `ra-selberg.tex` (486 lines). These proofs are not in Books 1–14. They are the second half of the climax. REVISE only the join: every use of a zero-free region or of the Riemann hypothesis is named. A proof that quietly uses an unproved zero-density estimate is not acceptable. Book 14's proved density theorems are the legal input. The mean square of \(|\zeta|^2\) is a different theorem and gets one sentence that says so.

**Hook.** Off the critical line, \(\log\zeta(\sigma+it)\) wanders with a law one can compute. On the line the Euler product diverges and the zeros sit in the way, and at a random height the real part is still a bell curve.

**Synopsis.** Bohr–Jessen for fixed \(\sigma>\tfrac12\). The mean-square approximation of \(\log|\zeta(\tfrac12+it)|\) by a short prime sum. Selberg's central limit theorem, variance \(\tfrac12\log\log T\). The Fyodorov–Hiary–Keating conjecture is stated. The matrix maximum is the admitted theorem that moved with the branching random walk; this chapter does not claim the maximum of \(\log|\zeta|\).

**Proved.** Bohr–Jessen. The approximation lemma, with its hypotheses in the heading. Selberg's central limit theorem from that approximation.

**Examples.** The variance of \(\mathrm{Re}\,p^{-it}\). Bohr–Jessen for a partial Euler product, which is elementary probability. The covariance at two heights, which is the input a multipoint exercise needs.

**Figures.** The histogram of \(\log|\zeta(\tfrac12+it)|/\sqrt{\tfrac12\log\log T}\) against the Gaussian. The partial Euler products at \(\sigma=0.8\) and at \(\sigma=\tfrac12\).

### Part IV. Structure versus Randomness

#### Chapter 12. Pseudorandomness

**Status.** NEW — `ch12-pseudorandom.tex` is 15 lines, and the fifteen lines are too loose. They mention a nilsequence. The series does not have nilsequences. The chapter's dichotomy is the one Book 14 proved for length three: a set correlates with a character, or its \(U^2\) norm is small. Green–Tao stays quoted.

**Hook.** Book 11 proved Roth's theorem by ergodic theory. Book 14 proved it by a density increment. They are the same meeting, and neither introduction says so until those revisions. This chapter says it once.

**Synopsis.** No third proof of Roth. The \(W\)-trick in probabilistic language, the trick itself cited from Book 14. The count of three-term progressions in a set with small \(U^2\) norm, written in the language of Chapters 1 and 6, the inverse step cited. Green–Tao in a heading marked "quoted". The singular series for prime progressions is cited if Book 14 numbered it, and proved here only if it did not.

**Proved.** The \(U^2\) count, citing Book 14 for the inverse theorem. Nothing Book 14 has not already proved, except that organisation.

**Examples.** The \(U^2\) norm of an interval and of a random set. The \(W\)-trick modulo 6.

**Figures.** A Bohr set beside a random subset of the same density. The \(W\)-trick as a thinning by the small primes.

#### Chapter 13. When order wins

**Status.** REVISE — `ch13-bias.tex` includes `ra-bias.tex` (356 lines). Chebyshev's bias is the meeting in which the structure wins: the squares do not run, and one residue class leads. The logarithmic-density integral under the generalised Riemann hypothesis and linear independence is the piece to prove if Book 6 only cites it. Lemke Oliver–Soundararajan is stated. The \(17.7\%\) figure moves here from Crossroads, with a precise citation, and is not given a fake proof. Maier's theorem is a pointer to Chapter 2.

**Hook.** In the race between primes \(4n+3\) and primes \(4n+1\), one side leads almost all the time. A fair coin does not do that. The squares are the reason.

**Synopsis.** The reduction to \(\psi(x,\chi)\), cited from the repaired Book 6, which itself cites Book 13 for the functional equation. The torus integral, under hypotheses that stay in the heading. One section on Maier: the small primes are structure, in the sense of Chapter 12, and the model that forgets them loses. The consecutive-residue bias is stated.

**Proved.** The logarithmic-density computation, if it is not already a theorem of Book 6. Nothing about Lemke Oliver–Soundararajan except the statement and the singular-series exercise that shows why a computation is not yet the theorem.

**Examples.** The bias modulo 3. The torus integral for a single zero.

**Figures.** The race up to \(10^6\), the first crossing near \(26861\). The matrix of consecutive residues modulo 10, the diagonal light.

### Part V. The Research Workshop

#### Chapter 14. Two projects

**Status.** NEW, from `ch11-problems.tex` and `ch12-projects.tex`, which together are a tour of seven problems and five projects. Keep two. Both use tools this book has proved.

**Hook.** The edition ends with work, not with a survey.

**Synopsis.** One project is the short-interval Turán–Kubilius inequality: the second-moment step when the interval is a power of \(x\) is proved, and the short-interval form is open. The other is the consecutive-residue bias: which average of the singular series would imply the theorem, and which average the series has actually proved. A project whose first step is an admitted theorem is not in this chapter. Green–Tao, modularity, and Artin reciprocity are not first steps here.

**Proved.** The two first steps. The solutions stop at the open line, and the open line is named.

**Examples.** A short-interval sample of \(\omega(n)\). One residue matrix.

**Figures.** None required beyond the data the projects use.

## What leaves this book

These files are in `main.tex` today. They do not deliver the meeting of structure and randomness.

| File | Verdict |
| --- | --- |
| `ch01-research.tex`, `ch02-reading.tex` | CUT as chapters. The three-pass reading is one section of Chapter 14, practised on Maier's paper or on Selberg's, both proved in this book. The dissociated-set narrative does not serve a frozen subtitle. Its counting bound may be an exercise in Book 14 if it is not already there. |
| `ch03-shuffling.tex` | MOVE to Book 11, with the cutoff from Book 10. The Bayer–Diaconis profile is a limit. It is not this meeting. |
| `ch04-selberg.tex` | MERGE. The multipoint covariance becomes an exercise of Chapter 11. |
| `ch05-sandpiles.tex` | MERGE the cokernel proof into Chapter 7. Cut the tour around it. |
| `ch06-chaos.tex` | MOVE the proved half-moment of the critical branching random walk to Book 12, where the branching random walk stays. Cut the reading-map of Harper. |
| `ch07-experiments.tex` | MOVE the BBP series and LLL to Book 5, *From Formula to Insight*. |
| `ch08-heuristics.tex` | MOVE the proved three-cubes identities and local densities to Book 13. Heath-Brown's prediction stays a labelled conjecture there, one paragraph. |
| `ch09-lean.tex` | CUT. No frozen title is a book about proof assistants. The series does not gain a sixteenth subject. |
| `ch10-writing.tex` | MOVE the polygonal Jordan theorem to Book 7, beside the Jordan theorem that arrived from Book 8. Cut the essay, except the one defective sentence the exercise already asks the reader to repair, which travels with the proof. |
| `ch11-problems.tex` | CUT, except the two projects named in Chapter 14. |
| `conjectures-ch01-born.tex` | MOVE the Borwein integrals to Book 5. Pólya, Mertens, and \(\pi(x)-\mathrm{li}(x)\) are Book 6. |
| `conjectures-ch02-twins.tex`, `ch03-goldbach.tex`, `ch04-riemann.tex` | CUT. Books 6 and 14 own the theorems. A Schnirelmann remark may sit in Chapter 6. |
| `conjectures-ch05-zetarmt.tex` | CUT. It is a pointer. Chapter 9 replaces it. |
| `conjectures-ch06-collatz.tex` | CUT. No frozen subtitle asks for it. |
| `conjectures-ch07-hadamard.tex` | MOVE the proved Paley and Sylvester constructions to Book 3, Fields. Cut the tour of the open conjecture. |
| `conjectures-ch08-geometric.tex` | MOVE Gilmer's inequality to Book 4, where entropy already lives. The unit-distance bound folds into Book 9's integral geometry if the proof uses it, and otherwise leaves. |
| `conjectures-ch09-abc.tex` | MOVE Mason–Stothers, and Fermat for polynomials, to Book 13. The integer \(abc\) conjecture is one labelled paragraph there, not a chapter here. |
| `conjectures-ch10-bsd.tex`, `ch11-random.tex`, `ch12-algebra.tex` | CUT. Books 13 and 15, Chapters 4, 7, and 8, already say what is proved and what is not. |

## Owns, defers, hands forward

**Owns.** The meaning of "random-like". Buchstab, Maier, and the Erdős–Rankin bound. The Kubilius model and Selberg–Delange. The random multiplicative models and periodic Möbius orthogonality. Bohr–Jessen and Selberg's central limit theorem. The Cohen–Lenstra measure and one cokernel theorem. The linear algebra of a random isotropic intersection. The form-factor page. The second-moment calculation under Hardy–Littlewood. The logarithmic-density integral for Chebyshev's bias, if Book 6 has not proved it.

**Defers, by stating them.** Chowla, Sarnak for nilsequences, Gallagher's Poisson law as conditional, Montgomery–Soundararajan beyond the second moment, the parity barrier for twins, the Cohen–Lenstra heuristic and its 2-part, Goldfeld, Bhargava–Shankar, modularity, Green–Tao, Lemke Oliver–Soundararajan, GUE for \(\alpha>1\), moments of zeta past the second, Fyodorov–Hiary–Keating.

**Hands forward.** Nothing. This is the top floor. The two projects are the unfinished details on a section that can otherwise be read.

## Pages and effort

The wrapped proofs plus the uncondensed workshop are much longer than the edition. The old separate volumes were about 194 and 313 pages. Target 280–340 after the moves and the cuts. Effort: heavy. The heavy work is the five openings, the join of the Selberg proof, the shrinkage of the second Erdős–Kac write-up, and the discipline of moving a good chapter to the book whose title it actually serves.
