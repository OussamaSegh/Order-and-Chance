# Series review, October 2026

This review scores the tree at commit `0419e16`. The current series is Volumes
0–14 plus Crossroads. Volume 14 is *Order and Chance: Where Number Meets
Randomness*. The workshop is Part V of that volume. Crossroads is the only
problem book. The titles scored below as a fifteenth volume and as two further
problem books are not in the catalog.



Review of *Order and Chance* at commit `0419e16`, covering Volumes 2–13, Volume 15, and problem books P1–P3. Volumes 0 and 1 are excluded: other work is rewriting them. The new Volume 14, *Order and Chance: Where Number Meets Randomness*, is not reviewed as a book. A draft under the old title *Random Arithmetic* is on disk at `volume14-random/` (thirteen chapters, preface still the sentence “Preface to come”); the capstone plan treats that draft as a quarry. This review edits no book source.

The audit read the flagship proofs, the statements of the named theorems, and a sample of solutions (the first and the last in each chapter, the short write-ups, and the solutions attached to any suspicious argument). It is a mathematician’s reading, not a line-by-line certification of every exercise in a corpus of this size. Findings below are ones that can be defended from the text. Each is marked **error** (the written argument asserts something false), **gap** (a correct theorem whose written proof misses a step), or **slip** (a wrong pointer, a mismatched name, or a sentence that overclaims).

Scores are readiness for publication as a mathematical book, from 1 to 10. They judge the manuscript against its own preface, not against the cover or the print pipeline.

| Book | Score |
| --- | ---: |
| 2 Structures | 8 |
| 3 Chance | 8 |
| 4 The Art of Calculation | 8 |
| 5 Where It All Meets | 7 |
| 6 Spaces | 8 |
| 7 Analysis in Depth | 7 |
| 8 Shapes | 7 |
| 9 Higher Structures | 8 |
| 10 Chance II | 8 |
| 11 Random Motion | 8 |
| 12 Arithmetic | 8 |
| 13 Primes in Depth | 8 |
| 15 The Research Workshop | 7 |
| P1 Crossroads | 8 |
| P2 Machinery | 2 |
| P3 Frontiers | 2 |

## Volume 2 — Structures

*The Language of Symmetry.* Twelve chapters (groups through characters and the finite subgroups of \(\mathrm{SO}(3)\)) and thirteen linear-algebra appendices. About 250 exercises, each with a hint and a write-up; the labels match.

### Mathematical correctness

**Gap.** `volume2-structures/chapters/ch10-galois.tex:170`, proof that the Galois group of \(X^5-4X+2\) is \(S_5\).

> It has exactly three real roots: \(f(-2)=-22\), \(f(0)=2\), \(f(1)=-1\), \(f(2)=26\) give three sign changes, and by Rolle’s theorem \(f\) has at most one more real root than \(f'=5X^4-4\), which has two.

The intermediate-value theorem gives at least three distinct real roots, and Rolle caps the number of distinct real roots by three. The next sentence treats complex conjugation as a transposition of the other two roots. That requires the three real roots to be simple and to account for only three of the five roots counted with multiplicity. A multiple root would have to be a root of \(f'\), and \(f''=20X^3\) shares no root with \(f'\), so any multiple root has multiplicity two. A double root together with three distinct sign-changing roots cannot fit in degree 5 without a further real root, which Rolle forbids. The polynomial does have three simple real roots (evaluate \(f\) at \(\pm(4/5)^{1/4}\)). The theorem is the right one. The written paragraph does not yet force the transposition.

**Gap.** `ch10-galois.tex:117–128`. After Gauss–Wantzel, a regular \(n\)-gon is constructible if and only if \(\varphi(n)\) is a power of 2, if and only if \(n=2^kp_1\cdots p_s\) with distinct Fermat primes. The degree argument is in place, including the identification \([\mathbb Q(\zeta_n):\mathbb Q]=\varphi(n)\) via the exercise `ex:phin`. The arithmetic equivalence “\(\varphi(n)\) is a power of 2 if and only if \(n\) has that shape” is not proved.

**Gap, structural.** Chapter 10 uses \(|\mathrm{Gal}(L/K)|\le[L:K]\) from the primitive element theorem, which is only Exercise `ex:primitive` in Chapter 8. The solution there is a complete proof for subfields of \(\mathbb C\), which is the book’s running convention. A numbered theorem should not depend on an exercise for a step it uses in the Galois correspondence.

The arguments that were recomputed and found correct include Lagrange, orbit–stabiliser, Burnside and Pólya, both Sylow theorems, the groups of order \(pq\), \(8\) and \(12\), simplicity of \(A_n\) for \(n\ge 5\), the structure theorem for finitely generated modules over a PID and the Jordan form deduced from it, the fundamental theorem of Galois theory in the book’s convention, Maschke, Schur, row and column orthogonality, the character tables of \(S_4\) and \(A_5\), the count of monic irreducibles over \(\mathbb F_q\), and the double cover \(S^3\to\mathrm{SO}(3)\). The friendship theorem (`linear-ch08-graphs.tex:106`) does contain the sentence that a rational square root of an integer is an integer; that parenthetical is brief, and it is not a false step. No `TODO` or “proof omitted” marker appears.

### Writing quality

The voice is concrete, then formal, and it stays that way. `ch01-groups.tex:13` (“These two facts, and nothing else, are what a group records”) and `ch05-sylow.tex:14` (“Lagrange’s theorem forbids… It promises nothing”) are the register the series should keep. \(D_n\) is the symmetry group of the regular \(n\)-gon, of order \(2n\), throughout, and composition in \(S_n\) is “first the right factor”. Euler’s \(\varphi\) is used at `ch01-groups.tex:187` as a Volume 1 object, with no local sentence of the form “\(\varphi(n)\) is the number of units modulo \(n\)”. `ch04-symmetric.tex:218` packs the quintic, random transpositions, and the classification of finite simple groups into one sentence.

### Depth

Against Dummit–Foote, and against Axler together with Horn–Johnson for the appendices, the spine of a first serious course is here: actions, Sylow, solvable groups, PIDs, finitely generated modules, rational and Jordan form, splitting fields, finite fields, the Galois correspondence, solvability by radicals, and complex characters through \(A_5\), plus the finite subgroups of \(\mathrm{SO}(3)\). The twelve linear-algebra appendices go past a first course (Cauchy–Binet, the spectral theorem, SVD, Perron–Frobenius, Huang’s signed adjacency bound, Strassen, Hilbert’s inequality).

Absent, and mostly named rather than skipped in silence: free groups and presentations, Artin–Wedderburn, inseparable extensions and an abstract algebraic closure (the Galois chapter restricts to subfields of \(\mathbb C\), and says so), Dedekind domains (sent to Volume 12), and a Galois closure in the abstract. Later volumes are named when a proof stops: Frobenius elements in Volume 12, the Diaconis–Shahshahani cutoff in Volume 9, Dirichlet’s theorem in Volume 5.

### Exercises and solutions

253 exercises and 253 solutions, labels and order matched: 88 single-star, 136 double-star, 29 triple-star. The write-ups that were compared with their statements are complete arguments. Samples that check: Wilson’s theorem as the unique element of order 2, the five groups of order 12, \(X^4+1\) irreducible over \(\mathbb Q\) and reducible modulo every prime, \(\lambda(360)=12\), and the \(A_5\) character norms. No solution was found arguing a different claim from its exercise.

### Coherence

From Volumes 0–1 the book takes cyclic groups, \(\varphi\), Euler’s theorem, Eisenstein, the binomial theorem modulo \(p\), primitive roots, and the real spectral theorem. It sends forward the characters of \(S_n\) (Volume 3 for the walk, Volume 9 for the cutoff), Dirichlet characters (Volume 5), Jordan form (Markov chains in Volume 3), and Frobenius (Volume 12). Appendix letters match `main.tex`. The strain is the primitive element theorem, above.

### Readiness: 8

The path from Lagrange to the fundamental theorem and the character table is proved at a level a specialist can read without rewriting it. The book’s own summit, \(X^5-4X+2\), is the place where a short justification is missing.

1. At `ch10-galois.tex:170`, prove that the three real roots are simple before calling conjugation a transposition.
2. Make the primitive element theorem a numbered result in Chapter 8, before Chapter 10 cites it.
3. Prove that \(\varphi(n)\) is a power of 2 precisely for \(n=2^kp_1\cdots p_s\) with distinct Fermat primes, or stop the polygon paragraph at “\(\varphi(n)\) is a power of 2”.
4. At the first use of \(\varphi\), one sentence recalling the definition from Volume 1.
5. Have a second reader walk the six rectangles in the 15-puzzle proof (`ch04-symmetric.tex:151–159`). The steps that were recomputed are consistent, and this is the longest unchecked coordinate chase in the book.

## Volume 3 — Chance

*The Logic of Uncertainty.* Twelve chapters, from counting and paradoxes through Brownian motion and the probabilistic method, plus appendices on orders and on extremal graph theory and Ramsey theory.

### Mathematical correctness

No false theorem turned up in the arguments that were recomputed: Bertrand’s three chord models \(\frac13,\frac12,\frac14\); Buffon \(\frac{2\ell}{\pi d}\) for \(\ell\le d\); the ballot theorem \(\frac{a-b}{a+b}\); Lindeberg’s swapping argument for the test functions of the chapter; Stirling’s constant from the Poisson(\(n\)) central limit theorem; optional stopping with the three standard sufficient conditions and the counter-example of the first hit of \(+1\); Lévy’s midpoint construction; the Black–Scholes limits \(d_\pm\) on the numerical example \(S_0=K=100\), \(r=0.05\), \(\sigma=0.2\), \(T=1\); Pólya’s theorem; Katona’s proof of the Erdős–Ko–Rado theorem; Dilworth in the Perles form; and the small Ramsey numbers, including the Clebsch colouring and \(R_3(3)=17\).

**Slip.** `volume3-chance/chapters/extremal.tex:185–186`.

> Volume 3, Proposition 12.1 proved the recursion… Theorem L.2 there proved \(R(k,k)>2^{k/2}\).

Proposition 12.1 is the first numbered result of Chapter 12. The Erdős bound is the next theorem of that chapter. There is no Appendix L in this volume. The result itself is proved, as `thm:erdosramsey`.

**Gap, exposition.** `ch06-clt.tex:262–271`. The limsup in the Lindeberg proof is compressed: the terms \(\|f''\|L_n(\varepsilon)\) and \(\max_k\sigma_{n,k}\le\sqrt{\varepsilon^2+L_n(\varepsilon)}\) are left for the reader to reconstruct. The limit claimed is the right one.

**Slip.** `ch06-clt.tex:142`. Glivenko–Cantelli is proved for continuous distribution functions, and a sentence says the result holds without continuity “with a little more care”. That case is not proved.

The book is explicit about what it does not prove. Lebesgue measure on \(\mathbb R^d\), infinite products, and Fubini–Tonelli are labelled “Admitted (proved in Volume 6)” at `ch05-continuous.tex:107`. The strong law under only a first moment is postponed in one sentence at `ch06-clt.tex:123`. The uniqueness of the giant component is a remark; the exercise proves only a component of linear size.

### Writing quality

`ch01-counting.tex:1–6` states Monty Hall as a host’s rule, and the later calculation shows that a different rule gives \(\frac12\). `ch05-continuous.tex:9` quotes Hermite on continuous functions without derivatives and then says what Lebesgue changed. “With high probability” is defined at `ch12-method.tex:117` before the theorems that use it. The Lindeberg limsup is the one place where the prose is tighter than the estimate.

### Depth

Against Feller’s first volume, Grimmett–Stirzaker, and Durrett, a first course that is willing to use measure theory is here: axioms, conditioning, generating functions and branching processes, Chernoff and Hoeffding, entropy and the asymptotic equipartition property, the integral through dominated convergence, the central limit theorem by Lindeberg, random walks through Pólya, finite and countable Markov chains with Doeblin coupling, Poisson processes and M/M/1, conditional expectation as an \(L^2\) projection extended by truncation, optional stopping, \(L^2\) and almost-sure martingale convergence, Azuma, Brownian motion through quadratic variation and the reflection principle, and Black–Scholes as a binomial limit. The probabilistic method covers the first and second moments, the symmetric local lemma, and the subcritical random graph. The appendices add Dilworth, Sperner, the Erdős–Ko–Rado theorem, Turán, Ramsey, Schur, van der Waerden, and the sunflower lemma.

Named and postponed: the strong law from a first moment and Lévy’s continuity theorem (Volume 10), Berry–Esseen and Donsker (Volume 10), Itô calculus (Volume 11), the full supercritical random graph. Continuous-time chains stop at M/M/1.

### Exercises and solutions

118 exercises and 118 solutions: 47 single-star, 59 double-star, 12 triple-star. Short solutions that were checked match their statements, including the giant-component exercise, which does not pretend to prove the constant \(\rho\).

### Coherence

The volume takes Stirling, the Gaussian integral, and finite-sum inequalities from Volume 0, and characters of \(S_n\) from Volume 2. The sharp cutoff for random transpositions is deferred to Volume 9, with the citation. It builds the integral itself and labels the two facts that need Volume 6. Notation is Kolmogorov’s triple. The broken “Theorem L.2” is the cross-reference that does not land.

### Readiness: 8

Dynkin, monotone and dominated convergence, conditional expectation, Lindeberg, and Lévy’s construction are real proofs, and the deferred analytic facts are named.

1. In `extremal.tex:186`, replace “Theorem L.2” by the Erdős theorem of Chapter 12.
2. Expand the limsup in `ch06-clt.tex:262–271` so that both error terms are on the page.
3. Delete the sentence that Glivenko–Cantelli holds at a jump “with a little more care”, or prove that case.
4. In the preface, say that the strong law is proved for bounded variables and under a fourth-moment bound, and that the first-moment theorem is in Volume 10.
5. Keep the giant-component remark as a remark. The exercise gives a component of size at least \(c(\varepsilon)n\).

## Volume 4 — The Art of Calculation

*From Formula to Insight.* Twelve chapters: finite calculus, generating functions, series and products, integration, Gamma and Beta, Fourier series, the discrete Fourier transform, the Fourier transform, complex analysis for computation, the zeta function, asymptotics, and the arithmetic–geometric mean.

### Mathematical correctness

**Error in the written evaluation; the identity is the classical one.** `volume4-calculation/chapters/ch10-zeta.tex:186–188`, Theorem (Riemann, 1859).

The display splits the integral over \((0,1]\) as
\[
J=\int_1^\infty\omega(u)\,u^{(1-s)/2-1}\,\mathrm du+\frac12\int_1^\infty\bigl(u^{-(s+1)/2}-u^{-s/2-1}\bigr)\,\mathrm du.
\]
The text then says: “The last integral is \(\frac2{s-1}-\frac2s\). Adding the part over \([1,\infty[\) gives the formula.”

The integral without the factor \(\frac12\) is \(\frac2{s-1}-\frac2s\). With the factor already written, it is \(\frac1{s-1}-\frac1s=-\frac1s-\frac1{1-s}\), which is what the theorem claims. The sentence evaluates the wrong multiple and then asserts the classical formula. The rest of the contour substitution, the asymmetric form \(\zeta(1-s)=2(2\pi)^{-s}\cos(\pi s/2)\Gamma(s)\zeta(s)\), and the values \(\zeta(-1)=-\frac1{12}\), \(\zeta(-3)=\frac1{120}\) check.

**Slip.** `ch10-zeta.tex:263–266`. For a general smooth cutoff, the constant term of \(\sum n\,e^{-n/N}\) is said to be independent of the cutoff and equal to \(\zeta(-1)\). Only the exponential cutoff is proved.

Checked and in order: real Stirling from log-convexity, the Stirling series with the sign of the remainder, Euler–Maclaurin and the expansion of \(H_n\), Niven’s proof that \(\pi^2\) is irrational, the residue \(\int_{-\infty}^\infty(1+x^4)^{-1}\,\mathrm dx=\pi/\sqrt2\), and the Brent–Salamin formula. Solutions that were recomputed (the lemniscate evaluation \(\Gamma(1/4)^2/(4\sqrt{2\pi})\), the Motzkin transfer, Gauss multiplication) agree with the exercises.

### Writing quality

Numerical checks sit next to the theorems. `ch11-asymptotics.tex:281–284` says plainly how the alternating remainder was used to compute \(\log\Gamma\). `ch05-gamma.tex:248–251` explains why Artin’s proof of the Beta integral is used: it avoids the Fubini–Tonelli change of variables deferred to Volume 6. `ch10-zeta.tex:188` is the bad pattern, a correct display followed by a sentence that does not evaluate it. `ch01-finite.tex:618–631` lists Bernoulli’s *Ars Conjectandi* twice.

### Depth

The aim is a working analyst’s toolkit for Volume 5, and against that aim the book is strong. Against Whittaker–Watson, Andrews–Askey–Roy, de Bruijn, or Stein–Shakarchi it is a selection. Present and proved: finite calculus, ordinary and exponential generating functions, the pentagonal-number theorem, the cotangent and sine products, \(\zeta(2k)\), Gamma through Bohr–Mollerup, reflection, duplication, and real Stirling, Fourier series through Fejér and Weyl’s criterion, the FFT, Poisson summation and the sign of the quadratic Gauss sum, a complex-analysis core through Rouché, Dirichlet series and the Euler product, Riemann’s functional equation, Laplace’s method and a Flajolet–Odlyzko transfer, the AGM and Brent–Salamin.

Missing, and relevant later: steepest descent and Watson’s lemma (the circle method in Volume 13 needs saddle-point language; Volume 13 builds its own major and minor arcs), a Mellin transform used as a tool rather than one Gaussian integral, Hankel’s contour for \(\Gamma\), the Weierstrass \(\wp\)-function, Phragmén–Lindelöf (that is Volume 7), and Picard. The preface’s bargain is kept on Fubini–Tonelli. The constant-term claim for a general cutoff is the exception.

### Exercises and solutions

Seventy-two exercises, labels matched to hints and solutions. Chapters 4, 7, and 11 have no three-star problem. The partition exercise states the Hardy–Ramanujan asymptotic in the solution without proving it. The solutions that were read are full write-ups.

### Coherence

Volume 5’s hard-coded theorem numbers were counted against this book’s counter and match: \(\zeta(2k)\) is 3.7, real Stirling is 5.8, reflection and duplication are 5.13–5.14, Weyl is 6.13, the Gauss-sum sign is 8.14, the residue theorem is 9.26, the Euler product is 10.3, the functional equation is 10.8. Inside this volume \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) and \(\theta(t)\) is a Jacobi theta. Chapter 12 reuses \(\Lambda(k)\) for Legendre’s relation. Volume 5 reassigns \(\Lambda\), \(\theta\), \(\psi\), and \(\omega\). Volume 5 warns the reader once, in the \(\xi\) section; the warning belongs at the boundary.

### Readiness: 8

The theorems a later volume quotes are the right ones. The functional-equation write-up does not, as printed, produce its own constant term.

1. At `ch10-zeta.tex:188`, replace the sentence by \(\frac12\bigl(\frac2{s-1}-\frac2s\bigr)=\frac1{s-1}-\frac1s\).
2. Prove, or delete, the claim that every smooth cutoff of \(\sum n\) has finite part \(-\frac1{12}\).
3. Add one complex saddle-point argument in Chapter 11 before Volume 13 uses the circle method. Volume 13 can stand without it; the reference would be cleaner.
4. Put a three-star exercise in Chapters 4, 7, and 11. Chapter 11’s should be an error term, not another Laplace example.
5. At the first use of \(\Lambda(s)\) and \(\theta(t)\), say that Volume 5 uses those letters for von Mangoldt’s function and Chebyshev’s \(\theta\).

## Volume 5 — Where It All Meets

*Where Numbers Meet Infinity.* Twelve chapters: Mertens, averages, characters, Dirichlet’s theorem, the prime number theorem, zeros, the explicit formula, sieves, Erdős–Kac, random models, exponential sums, and a taste of modular forms.

### Mathematical correctness

**Error in the proof; the statement is correct.** `volume5-meets/chapters/ch01-mertens.tex:131–132`, Corollary (Chebyshev, 1852).

The corollary states
\[
\liminf_{x\to\infty}\frac{\theta(x)}{x}\le 1\le\limsup_{x\to\infty}\frac{\theta(x)}{x}.
\]
The proof shows that \(\theta(t)\ge(1+\varepsilon)t\) for all large \(t\) contradicts \(\sum_{p\le x}(\log p)/p=\log x+O(1)\). That forbids \(\liminf>1\), so it yields \(\liminf\le 1\). The text says “So the \(\limsup\) is at least \(1\)”. The opposite bound \(\theta(t)\le(1-\varepsilon)t\) forbids \(\limsup<1\) and is described as giving the \(\liminf\). The two names are swapped. The comparison with \(\pi(x)\) in the next sentence is right.

**Error in the prose after a correct theorem.** `ch08-sieves.tex:149–151`.

The short-interval Brun–Titchmarsh inequality
\[
\pi(x+N)-\pi(x)\le\frac{2N}{\log N}\Bigl(1+O\Bigl(\frac{\log\log N}{\log N}\Bigr)\Bigr)
\]
is proved, and the Selberg-sieve argument checks. The following paragraph says that no interval contains “more than twice” the prime-number-theorem count \(N/\log x\), “when \(x\) is a power of \(N\)”, and that “improving the \(2\) to \(2-\varepsilon\) would rule out Siegel zeros (Chapter 3)”. If \(x=N^k\), the ratio of \(2N/\log N\) to \(N/\log x\) is \(2k\), not \(2\). The obstruction that ties the constant \(2\) to Siegel zeros is the arithmetic-progression inequality \(\pi(x;q,a)\le 2x/(\varphi(q)\log(x/q))\), which Chapter 3 does not prove; Chapter 3 only introduces the name. The parity problem does block sieve upper bounds of shape \(2-\varepsilon\) in both settings. A short-interval improvement of the constant is not a disproof of Siegel zeros.

**Slip, against the preface’s own rule.** `ch10-random.tex:269–276` displays Maier’s theorem as a pair of inequalities and sketches the mechanism. It is not a theorem environment and it is not proved. The preface says that results quoted only for their interest appear as remarks. The inequalities are displayed as facts. Granville’s refinement is in the same register.

**Slip.** `ch10-random.tex:275` says the oscillating factor “is given by Buchstab’s function, met in sieve theory.” Chapter 8 does not define Buchstab’s function. Volume 13, Chapter 3, draws it and proves the fundamental lemma for large \(u\), which is a different statement. The theorem \(\Phi(x,z)=\omega(u)x/\log z+O(x/\log^2 z)\) for \(u\) in a fixed range is proved in the Volume 14 draft, `volume14-random/chapters/ch11-gaps.tex`, and nowhere in Volumes 0–13.

**Slip.** `ch06-zeros.tex:388`. A positive proportion of zeros, “more than \(41\%\)”, is said to lie on the critical line. That sentence records a moving numerical bound. It is not a derivation, and Volume 13 correctly marks a positive proportion as quoted.

Flagship proofs that check: Dirichlet’s theorem from \(L(1,\chi)\ne 0\); the Landau argument for a real character; Newman’s proof of the prime-number theorem in Zagier’s form, including \(g(0)=-1-\gamma\) and the passage \(\psi\sim x\), then \(\theta\sim x\), then \(\pi(x)\sim x/\log x\); the classical zero-free region \(1-\beta_0\ge 1/(14A'\log|t|)\); the explicit formula for \(\psi_0(x)\) and von Koch’s equivalence; the bias identity for \(\theta(x;4,3)-\theta(x;4,1)\); Erdős–Kac with the Kubilius truncation; the multiplication-table theorem \(D(N)=o(N^2)\); Siegel’s contour for the Dedekind \(\eta\)-function; \(E_4^2=E_8\); and \(\tau(n)\equiv\sigma_{11}(n)\pmod{691}\). The numerical caption at \(10^8\) (\(\pi(10^8)=5761455\), \(\mathrm{Li}(x)-\pi(x)=753\) with \(\mathrm{Li}(x)=\int_2^x\mathrm dt/\log t\)) matches that normalisation.

The functional equation of a primitive \(L(s,\chi)\) is not proved here. The bias section uses \(\psi(x,\chi_{-4})\) and points at Davenport for that step. Volume 12 later proves Tate’s thesis for \(\mathbb Q\), including primitive Dirichlet \(L\)-functions, so the series does contain the missing equation, two volumes later.

### Writing quality

`ch01-mertens.tex:131` narrates a correct dichotomy backwards. `ch01-mertens.tex:229–235` is the other extreme: the product up to \(\sqrt{10^6}\) is set against \(1/\log n\), and the \(12\%\) is tied to the failure of independence past \(\sqrt n\). `ch05-pnt.tex:169–171` separates “no zero on \(\mathrm{Re}\,s=1\)” from the Tauberian machine. `ch12-modular.tex:270` pins \(\sigma_7(2)=129=9+120\). `ch08-sieves.tex:149–151` packs short intervals, arithmetic progressions, and Siegel zeros into one word, “twice”.

### Depth

Against Apostol this is a deeper book: it proves the prime-number theorem and continues through zeros, the explicit formula, sieves, and Erdős–Kac. Against Davenport it covers the same spine and adds the probabilistic half. Absent, relative to Montgomery–Vaughan and Tenenbaum, and in several cases owned honestly by Volume 13: the approximate functional equation (quoted in Volume 13, Chapter 14, not proved), a convexity bound better than the \(O(|t|^{1/2})\) of Exercise 6.6, Vinogradov–Korobov, Vaughan’s identity, Bombieri–Vinogradov, Siegel’s theorem, sieve lower bounds, Halász’s theorem, and a proof of Maier’s theorem. The large sieve is proved and used for a square-sieve application. It is not pushed to Bombieri–Vinogradov.

### Exercises and solutions

Eighty-three exercises, labels matched. Chapters 1–4 and 12 have no three-star problem. From Chapter 5 each chapter has one three-star problem and a separate two-star “signature” exercise; several signature problems (the \(n\)th prime, the bias, the multiplication table) are better than the three-star problems beside them. Recomputed solutions — Meissel–Mertens, the largest prime factor (proportion tending to \(\log 2\)), \(\sigma_7\), the congruence modulo \(691\) — agree with the statements.

### Coherence

Inputs match the prefaces of Volumes 1–4: \(\Lambda*\mathbf 1=\log\), orthogonality of characters, moments and characteristic functions, and the analytic theorems whose numbers were checked above. \(\mathrm{Li}(x)\) starts at 2. Collisions that are declared: \(\psi_\Gamma=\Gamma'/\Gamma\) because \(\psi\) is taken; \(\Lambda(s)\) “only here” in Chapter 6; \(q=e^{2\pi i\tau}\) in Chapter 12 after eleven chapters in which \(q\) is a modulus. Volume 12’s use of the class-number formula matches Theorem 3.10, including the odd-character formula. Volume 11’s pair correlation should cite Volume 13, Theorem 14.15, which it does; it should not cite this volume for a proof of Montgomery’s theorem.

### Readiness: 7

The prime-number theorem, Dirichlet’s theorem, the explicit formula, and Erdős–Kac are in a state a reader can trust. The first corollary of the first chapter names the wrong limit, and the sieve chapter states a false implication.

1. At `ch01-mertens.tex:131–132`, exchange the names: \(\theta(t)\ge(1+\varepsilon)t\) yields \(\liminf\le 1\), and \(\theta(t)\le(1-\varepsilon)t\) yields \(\limsup\ge 1\).
2. Rewrite `ch08-sieves.tex:149–151`. State the short-interval bound as \(2N/\log N\). Put the constant \(2\) and Siegel zeros on the arithmetic-progression inequality.
3. Mark the explicit formula for \(\psi(x,\chi_{-4})\) as a quotation, or point forward to Volume 12’s Tate thesis for the functional equation of \(L(s,\chi)\).
4. Move Maier’s display in `ch10-random.tex:269–272` into a remark, until the capstone proves it.
5. Keep the cut with Volume 13 explicit in the preface: this book ends at the classical explicit formula, Selberg’s sieve, Erdős–Kac, and the shape of Cramér’s model.

## Volume 6 — Spaces

*A Landscape of Limits.* Eleven chapters: sets and choice, metric spaces, topology, compactness, Baire, measures, the Lebesgue integral, products and change of variables, \(L^p\), Radon–Nikodym, and measures on metric spaces.

### Mathematical correctness

**Gap.** `volume6-spaces/chapters/ch06-measures.tex:194–196`, in the characterisation of Lebesgue measure by translation invariance.

> A general box \(]a,b]\) is the increasing union of boxes \(]a^n,b^n]\) with dyadic corners, \(a^n\) decreasing to \(a\) and \(b^n\) increasing to \(b\) (strictly above \(a\), below \(b\)), so \(\mu\) and \(\lambda_d\) agree on it by continuity from below.

Existence of \(\lambda_d\), and uniqueness among Borel measures that reproduce box volumes, are already finished by the premeasure argument. This paragraph is the extra claim that a translation-invariant Borel measure with \(\mu(]0,1]^d)=1\) equals \(\lambda_d\). With the corners strictly inside, the union is \(]a,b[\), not \(]a,b]\). Continuity from below gives the open box. The face \(]a,b]\setminus\,]a,b[\) is not shown to be null for a general invariant \(\mu\). For \(d=1\) the face is a point; for \(d\ge 2\) it is a union of faces. The claim is true, by sandwiching a general box between dyadic-corner boxes whose volumes differ by an arbitrary \(\varepsilon\). The written sentence does not do that.

**Gap.** `ch06-measures.tex:148–149`. Outer-measure subadditivity chooses an \(\varepsilon\)-cover for every \(n\), including the case \(\mu^*(A_n)=\infty\), where no such cover exists. The inequality is then immediate; the case should be separated.

**Gap.** `ch11-metricmeasures.tex:171–172`. Finite additivity of the cylinder set function in Kolmogorov’s extension is asserted. The tightness argument after that line is complete.

Checked and in order: Carathéodory and the extension theorem; monotone convergence, Fatou, dominated convergence; Tonelli and Fubini, including the diagonal counter-example when \(\sigma\)-finiteness drops; the change of variables, including the inverse-diffeomorphism step; Hahn, Radon–Nikodym, Lebesgue decomposition; the maximal inequality and Lebesgue differentiation; Riesz representation for positive functionals on compact metric spaces; portmanteau; Ulam; Kolmogorov on \(\mathbb R^{\mathbb N}\). Hausdorff measure is used as an outer measure, and the text refers the Borel property, and the normalisation \(\mathcal H^d=c_d\lambda_d\), to Falconer (`ch11-metricmeasures.tex:201–203`).

No solution error turned up in the first and last solutions of each chapter.

### Writing quality

`ch07-integral.tex:76–77` announces monotone convergence as the engine of Fatou and dominated convergence, and ties the escape of mass for \(n\mathbf 1_{]0,1/n[}\) to one missing hypothesis. `ch10-radon.tex:8–14` uses the cricket maximal function as the inequality that differentiates integrals. `ch06-measures.tex:194–196` calls the union “the box”; the slip is linguistic and mathematical at once. “Word for word” at `ch11-metricmeasures.tex:199` describes Hausdorff outer measure as identical to Carathéodory’s extension; the construction is analogous.

### Depth

Against Munkres, the topology that analysis uses is proved: bases, products, quotients, connectedness, compactness, Heine–Borel, sequential compactness in metric spaces, Tychonoff by Zorn, Arzelà–Ascoli, Stone–Weierstrass, Baire, and a metric Urysohn lemma. Tietze is an exercise with a full solution. Absent, and not needed later: Urysohn metrization, paracompactness, nets as a systematic language.

Against Folland or Rudin, the core is present at a comparable standard through Radon–Nikodym, differentiation, and Riesz–Markov on compact metric spaces. Thinner: no complex measures; Prokhorov’s converse on a general Polish space is stated and not proved; conditional expectation is Exercise 10.2, with a complete solution for the defining property and without the tower property written out. Product measures and change of variables, the two tools Volume 8 cites, are theorems.

### Exercises and solutions

Every exercise has a hint and a solution split into an idea and a write-up. The non-Borel set pulled back from a Vitali set, the Dirichlet integral, and the Gaussian cosine transform match their claims.

### Coherence

Numbering used later is stable: Fubini is Theorem 8.6, change of variables Theorem 8.8, Stone–Weierstrass Theorem 4.19, Radon–Nikodym Theorem 10.4, Riesz Theorem 11.3, Prokhorov Theorem 11.7, Kolmogorov Theorem 11.8. Volume 8 cites change of variables from here and proves the inverse-function theorem itself. Volume 10 builds Lévy’s continuity theorem on Prokhorov. Volume 11’s Girsanov theorem uses the Radon–Nikodym derivative constructed here. The tower property, which Volumes 10 and 11 use, is the piece still living in an exercise.

### Readiness: 8

The book can carry Volumes 8–13 in measure, integration, weak convergence, and point-set topology. The translation-invariant paragraph should be repaired before the characterisation is quoted.

1. Close the face estimate in `ch06-measures.tex:193–196`.
2. Move conditional expectation, including the tower property, from Exercise 10.2 to a numbered theorem.
3. Prove that a metric outer measure is a Borel measure, and record \(\mathcal H^1=\lambda_1\) on \(\mathbb R\), or keep the Falconer citation and stop any later appeal to \(\mathcal H^d\) as a measure.
4. Add one line of finite additivity for the cylinder set function (`ch11-metricmeasures.tex:171–172`).
5. Separate the case \(\mu^*(A_n)=\infty\) in `ch06-measures.tex:148–149`.

## Volume 7 — Analysis in Depth

*Limits, Measures and Transformations.* Ten chapters: Banach and Hilbert spaces, operators, the spectral theorem, the Fourier transform, distributions and Sobolev spaces, finite abelian Fourier analysis, Haar measure and the \(p\)-adics, complex analysis, and Tauberian theorems.

### Mathematical correctness

**Error in the proof; the lemma is true.** `volume7-analysis/chapters/ch10-tauberian.tex:270–273`, Lemma (local inverse), used for Wiener’s lemma.

The book’s convention is \(\hat g(\xi)=\int g(x)e^{-2\pi ix\xi}\,\mathrm dx\). The reduction
\[
f_1(x)=\frac{f(x)e^{-2\pi i\xi_0 x}}{\hat f(\xi_0)},\qquad \hat f_1(\xi)=\frac{\hat f(\xi+\xi_0)}{\hat f(\xi_0)}
\]
matches that convention. The same exponential on the inverse does not: if \(h(x)=h_1(x)e^{-2\pi i\xi_0 x}/\hat f(\xi_0)\), then \(\hat h(\xi)=\hat h_1(\xi+\xi_0)/\hat f(\xi_0)\). The text claims
\[
\hat h(\xi)\hat f(\xi)=\hat h_1(\xi-\xi_0)\hat f_1(\xi-\xi_0).
\]
The right-hand side is \(\hat h_1(\xi-\xi_0)\hat f(\xi)/\hat f(\xi_0)\). The two sides differ by the sign of the shift. If \(h_1\) inverts \(\hat f_1\) on \([-\delta,\delta]\), this \(h\) does not invert \(\hat f\) on \([\xi_0-\delta,\xi_0+\delta]\). The opposite modulation \(e^{+2\pi i\xi_0 x}\) makes the identity true. The construction under the reduction \(\hat f(0)=1\), and the partition of unity that glues local inverses, were checked separately. Ikehara’s theorem does not use this lemma; its Fejér-kernel proof (the Laplace-transform identity, the bound on \(\psi\), de-smoothing by monotonicity) is in order, and so is the passage to \(\psi(x)\sim x\) from the zero-free line imported from Volume 5.

**Slip, public text.** `volume7-analysis/blurb.tex:5–6` says the book proves “the spectral theorem for compact, bounded and unbounded operators” and that “Every theorem is proved in full.” Chapter 4 proves the compact self-adjoint theorem and the continuous functional calculus for bounded self-adjoint operators, then sends the projection-valued measure and the unbounded case to Reed–Simon (`ch04-spectral.tex:381–384`).

**Slip.** `preface.tex:19` lists “Perron’s formula”. That name does not occur again. What is proved is Mellin inversion and one rectangular shift.

Checked and in order: analytic and geometric Hahn–Banach; uniform boundedness; the open mapping theorem; the closed graph theorem; \(L^p\) duality for real scalars; Riesz–Markov for real \(C(K)\); Banach–Alaoglu; the compact self-adjoint spectral theorem and Courant–Fischer; Fourier inversion when \(\hat f\in L^1\), Plancherel, the Hermite basis; Tauber’s \(o(1/n)\) theorem; Karamata; Wiener–Ikehara; Dixon’s homology form of Cauchy’s theorem; the residue theorem. The spot-checked solutions (the divisor sum by Karamata, quicksort \(C_n\sim 2n\log n\), the cap-set bound, majority Fourier coefficients) match.

**Slip, exposition.** `ch01-banach.tex:229`. Complex \(L^p\) duality is one sentence (“apply the real case to the real and imaginary parts”). The real proof is complete; the complex bookkeeping is the reconstruction already written for Hahn–Banach, and it is not repeated. `ch04-spectral.tex:230–231` says “word for word” of a decreasing-eigenvalue form of Courant–Fischer, while the Sturm–Liouville form used there is the increasing min-max. Exercise 5.3 on Bochner’s theorem proves that Fourier transforms of finite positive measures are positive definite, then names the converse. The solution’s last sentence cites the converse. A reader can mistake the exercise for a proof of it.

### Writing quality

`ch09-complex.tex:222–224` summarises Dixon’s argument in three lines that match the proof. `ch10-tauberian.tex:270–273` puts the false “because” in one clause that carries the whole reduction. The blurb and `ch04-spectral.tex:381–384` disagree about what has been proved, in public.

### Depth

Against Brezis or Conway: Hahn–Banach, the three Baire theorems, the duals of \(L^p\), \(c_0\) and \(C(K)\), weak compactness, compact and Fredholm theory, the compact spectral theorem, the continuous functional calculus, Lax–Milgram, and \(H^1\) on an interval with Rellich. Missing: the spectral theorem for a general bounded or unbounded self-adjoint operator, locally convex spaces, the Krein–Milman theorem, and the Bochner integral.

Against Stein–Shakarchi or Katznelson: \(L^1\) theory, inversion, Plancherel, Riesz–Thorin, Poisson summation, finite abelian Fourier analysis through quadratic reciprocity and the cap-set bound, tempered distributions, and a fundamental solution of \(\Delta\) in \(\mathbb R^3\). The converse half of Paley–Wiener is an exercise that does the easy half. Carleson’s theorem is named and not claimed. Sobolev space in dimension \(d>1\) stops at the remark that the embedding threshold is \(s>d/2\).

Against Ahlfors, this is a second course. Winding numbers, the Jordan curve theorem, Dixon, Phragmén–Lindelöf, Hadamard factorisation, Montel, the Riemann mapping theorem, and Mellin inversion are proved. Carathéodory’s boundary theorem is not. For Volumes 12 and 13 the contour tool that is actually here is Mellin inversion, the residue theorem, and Ikehara.

Volume 11’s Itô integral is an \(L^2\) limit, so the missing Bochner integral does not block it. Volume 12’s adelic Fourier analysis uses the explicit Haar measure and the \(\mathbb Q_p\) duality of Chapter 8. General Haar existence on a compact metrizable abelian group is proved; the abstract existence theorem is marked unused.

### Exercises and solutions

Every exercise has a hint and a reasoned solution. The three-star write-ups carry the argument. The Bochner solution does not prove existence of the representing measure, and its last sentence says so.

### Coherence

Citations of Volume 6 match the theorems checked. The zero-free line is taken from Volume 5 and not re-proved. The preface’s chapter map is faithful except for Perron’s formula. Lévy’s continuity theorem is proved in Volume 10 and does not depend on the Bochner exercise; that separation should stay.

### Readiness: 7

Hahn–Banach, the Baire theorems, compact spectral theory, Plancherel, global Cauchy, and Ikehara are in a state later volumes can quote. The Wiener reduction is not, until the sign is corrected, and the blurb currently claims a spectral theorem the chapter postpones.

1. Replace \(e^{-2\pi i\xi_0 x}\) by \(e^{+2\pi i\xi_0 x}\) in the return map of `ch10-tauberian.tex:270–273`, and write the two transform identities.
2. Change the blurb so the spectral theorem is the compact self-adjoint theorem plus the continuous functional calculus. Delete “Perron’s formula” from the preface, or add the formula next to Mellin inversion.
3. Either write the projection-valued theorem, which the remark at `ch04-spectral.tex:381–384` says is the functional calculus plus Riesz–Markov, or keep the reference and make the blurb agree.
4. Write the complex \(L^p\) dual at `ch01-banach.tex:229` with the real-part reconstruction used for Hahn–Banach.
5. State in the text of Exercise 5.3 that the converse half of Bochner’s theorem is not proved.

## Volume 8 — Shapes

*The Geometry of Connection.* Ten main chapters (manifolds through integral geometry) and twelve geometry appendices, from Euclid through curvature of curves.

### Mathematical correctness

**Gap.** `volume8-shapes/chapters/geometry-ch08-cubics.tex:75–108`. Associativity \((P+Q)+R=P+(Q+R)\) is proved when the nine points are distinct, from Cayley–Bacharach. The text says the remaining cases are handled in Volume 12, that a numerical calculation checks associativity, and that “from now on we use that \((E(K),+)\) is an abelian group.” Theorem `geometry:thm:nineflexes` then treats the flexes as the subgroup \(E[3]\cong(\mathbb Z/3)^2\). That step needs the group law for every triple. Volume 12, Chapter 12, does prove the group law from Riemann–Roch. Until a reader has that chapter, the flex theorem is ahead of its proof. The Weierstrass addition formulas a few lines later are explicit enough to support an algebraic verification; it is not given.

**Gap.** `ch08-haar.tex:281–290`, Andreief’s identity. The lemma has \(1/n!\) on the left. The proof expands the determinants, sums over permutations, and ends with “the \(n!\) choices of \(\pi\) give \(n!\det M\).” That is the integral without the \(1/n!\). The last sentence never divides. Heine’s identity, which calls the lemma, is nevertheless the correct Toeplitz determinant.

**Gap.** `ch06-homology.tex:381–383`, the top of the Borsuk–Ulam transfer.

> If \(H_n(\mathbb{RP}^n)\) were \(0\) the middle term would be both the kernel of \(q_*\) and the image of \(\tau_*=0\); so \(\tau_*\) is an isomorphism.

If the group vanished, exactness would make \(q_*\) injective from \(\mathbb Z/2\) into \(0\). The middle term would not equal that kernel. The exact sequence printed just above does contain a correct proof (\(\tau_*\) is injective and \(H_{n-1}\) is already \(\mathbb Z/2\)). The sentence as written does not give it.

Stokes (half-space \(x_1\le 0\), outward normal first), the homotopy formula, Mayer–Vietoris, excision, invariance of domain, the Haar modular factor, and the Jacobian in Weyl’s integration formula check. So do Bézout’s count, the \(E_8\) minimal vectors \(112+128=240\), the Hermite constant in the plane, Brunn–Minkowski, and the discriminant \(4a^3+27b^2\). The de Rham theorem is stated at `ch03-forms.tex:355` and proved for the punctured plane. The classification of surfaces is used as a remark at `ch06-homology.tex:305`.

### Writing quality

The geometry appendices are the same voice as the main chapters, more elementary and more pictorial. `ch03-forms.tex:234` describes the Stokes proof as the fundamental theorem of calculus, with the classical theorems absorbed into the definitions. `geometry-ch09-lattices.tex:81` gives Fermat’s two-squares theorem in four lines after Minkowski, with the lattice drawn for \(p=13\). Two chapters are titled Curvature (`ch04-curvature.tex` and `geometry-ch12-curvature.tex`): the appendix is curves and polyhedral defect, the main chapter is intrinsic surface geometry. A reader can think the appendix is repeating Chapter 4.

### Depth

Against Lee’s *Smooth Manifolds*: inverse and implicit function theorems, Sard in equal dimensions, the easy Whitney embedding, flows, Frobenius, forms, Stokes, the Poincaré lemma. No Poincaré duality, no curvature tensor, no Hopf–Rinow. Gauss–Bonnet for surfaces is complete (Chern’s proof).

Against Hatcher: \(\pi_1\), coverings, Seifert–van Kampen, Nielsen–Schreier, singular homology through invariance of domain and Borsuk–Ulam. Missing: cohomology and cup products, cellular homology, higher homotopy groups, a proof of the classification of surfaces.

Against Hall: the closed-subgroup theorem, \(\mathrm{SU}(2)\to\mathrm{SO}(3)\), the maximal torus of \(U(n)\). Chapter 8 then goes past Hall, through Dyson’s pair correlation for the finite unitary group. The twelve geometry appendices sit at a strong Coxeter level, and the cubic appendix reaches Bézout and singular points without local intersection rings. The multiplicity \(I_P\) is said to depend a priori on an auxiliary point (`geometry-ch07-curves.tex:150`).

### Exercises and solutions

Every chapter and appendix ends with starred exercises, a hint, and a solution. Recalculated: the sphere area \(\omega_n=\pi^{n/2}/\Gamma(n/2+1)\), the Möbius orientation sign \((-1)^{n+1}\), Bachet’s tangent arithmetic, the \(E_8\) inner products, and the football’s twelve pentagons. The solution of the six-points exercise uses the unfinished group law. The Hermite solution invokes “two standard facts (Cassels, Chapter I)” for the determinant of a projected lattice. That is not a complete solution.

### Coherence

Volume 6, Theorems 8.8 and 8.6, are change of variables and Fubini, as cited. Volume 7’s Haar measure on \(\mathrm{GL}_n\) matches the modular function used here. Inside Chapter 8 the letter \(\Delta\) is the modular function at `ch08-haar.tex:69` and, twenty lines into the Weyl section, the Vandermonde product at line 159. Volume 12 proves the group law on its own and does not quote the unfinished argument. Volume 9’s picture of \(\mathrm{Cl}(A)\) for a cubic does.

### Readiness: 7

The analytic and topological core could be published. The cubic group, the unproved de Rham theorem, and one sentence of Borsuk–Ulam keep it from an 8.

1. Prove associativity on a smooth cubic in every characteristic not 2 or 3, degenerate cases included, or point the flex theorem at Volume 12, Chapter 12, and do not use the group before that citation.
2. Mark the de Rham sentence at `ch03-forms.tex:355` as a statement with one proved case, or prove it for compact manifolds. Later chapters do not use the general statement.
3. Rewrite `ch06-homology.tex:381–383` so that \(H_k(\mathbb{RP}^n;\mathbb Z/2)\cong\mathbb Z/2\) is deduced from exactness in print.
4. End the Andreief proof with the division by \(n!\).
5. Rename one of the two \(\Delta\)s in the Haar chapter, and replace the Cassels citation in the Hermite solution by the two projection lemmas.

## Volume 9 — Higher Structures

*Categories, Rings and Homology.* Eleven chapters: categories, tensors, Noetherian rings, localisation and dimension, Dedekind domains, homological algebra, group cohomology, semisimple algebras, the symmetric group, card shuffling, and compact groups.

### Mathematical correctness

No false theorem in the arguments read in full: Hilbert’s basis theorem, Zariski’s lemma, the weak and strong Nullstellensatz, Noether normalisation and \(\dim K[x_1,\ldots,x_n]=n\), the equivalence of the four Dedekind axioms including uniqueness of prime factorisation, Wedderburn, the hook-length formula, the transposition character and the cutoff for \(n\ge 10^4\), Hilbert 90, the Ext classification of extensions, and Weyl’s character formula for \(U(n)\) (dimensions \(8\) and \(10\) for the two sample weights).

Maschke is not reproved. The appeal at `ch08-semisimple.tex:31` to “Volume 2, Theorem 11.3” lands on the averaging proof that every finite-dimensional \(\mathbb C[G]\)-module is a sum of irreducibles. Schur, orthogonality, \(\sum d_i^2=|G|\), and Dedekind’s independence lemma match Volume 2’s counters.

**Slip.** `ch10-shuffling.tex:32`.

> For \(G\) abelian … this is the Fourier analysis of Volume 2, Theorem 11.14, up to a complex conjugation.

Volume 2 puts \(1/|G|\) into the transform and inverts without it. This chapter does the opposite, and it also replaces \(\chi\) by \(\overline\chi\). Conjugation is half the difference. Line 44 cites Theorem 11.8 for the multiplicity of an irreducible in the regular representation; that multiplicity is Corollary 11.9. The one-line computation written there is correct.

**Gap.** `ch05-dedekind.tex:328`.

> One can show that \(P\mapsto[\mathfrak m_P]\) is an isomorphism from the group of points \(E(\mathbb C)\) onto \(\mathrm{Cl}(A)\).

The ideal factorisations that precede it are proved. The isomorphism is not. It also inherits Volume 8’s unfinished group law. Volume 12 does not depend on this sentence; it proves the number-field case of unique ideal factorisation on its own.

Schur–Weyl duality is stated at `ch11-compact.tex:186–189` and not proved. The character formula does not need it.

### Writing quality

`ch03-noetherian.tex:15` attributes Gordan’s “theology” to Constance Reid. `ch09-symmetric.tex:262` makes the hook walk the whole proof of the identity \((h_{a\beta}-1)+(h_{\alpha b}-1)=h_{ab}-1\). `ch10-shuffling.tex:1` announces the cutoff \(\frac12 n\log n\) and then proves a weaker explicit bound, and says so at line 202. `ch03-noetherian.tex:221` is one honest sentence on schemes. The title of the volume still suggests a start that the sentence does not make.

### Depth

Against Atiyah–Macdonald this is Chapters 1–3, 5–7, and 9, plus Gröbner bases and the Nullstellensatz. Proved: Noetherian modules, Hilbert basis, localisation, Nakayama, integral dependence, going up, Nullstellensatz, Noether normalisation, dimension, Dedekind domains, \(\sum e_if_i=n\). Absent: primary decomposition and associated primes, going down, Artinian rings, completions, and Hilbert–Samuel polynomials. \(\mathrm{Spec}\) is defined and is not a locally ringed space.

Against Weibel: projective and injective resolutions, the horseshoe lemma, a long exact sequence, the classification of \(\mathrm{Ext}^1\), and universal coefficients for finitely generated free complexes over a PID. No spectral sequences and no derived categories. The universal-coefficient theorem is not stated for singular chains, which are not finitely generated; that restriction is correct. Group cohomology is inhomogeneous cochains, Hilbert 90, and Schur–Zassenhaus. There is no Lyndon–Hochschild–Serre sequence.

Against Fulton–Harris: Wedderburn, Frobenius reciprocity, Mackey, Burnside’s \(p^aq^b\) theorem, Specht modules, the hook-length formula, and the Weyl character formula for \(U(n)\). Chapter 10, the random-transposition cutoff, is not in those books. The eigenvalue \(1-2/n\) on the standard representation is the right one.

### Exercises and solutions

Six exercises a chapter, with hints and full solutions. Recalculated: the real Nullstellensatz counter-example \((X^2+Y^2)\), the Gröbner basis of \((X^2-Y,X^3-X)\) with zero set \(\{(0,0),(1,1),(-1,1)\}\), and the proof that \((x,y)\) is not principal on \(y^2=x^3-x\) by degrees of norms.

### Coherence

Volume 2’s numbering agrees with Chapters 8–10 except the Fourier normalisation and the regular-representation label. Volume 8, Exercise 6.1, is the homology of \(\mathbb{RP}^2\) that the universal-coefficient discussion quotes. Euler characteristic and characters both use \(\chi\), in different volumes. Volume 12, Chapter 2, points here for the abstract Dedekind axioms and proves the number-field case itself.

### Readiness: 8

The theorems that carry the book are proved, and the citations into Volume 2 land on the right statements, with the two exceptions above.

1. Prove the map \(E(\mathbb C)\to\mathrm{Cl}(A)\), or delete the word “isomorphism” at `ch05-dedekind.tex:328`.
2. Add primary decomposition and associated primes before Dedekind domains.
3. State the inflation-restriction sequence in degrees 1 and 2, even if the spectral sequence itself stays a remark.
4. Correct `ch10-shuffling.tex:32` and `:44`: the Fourier transform differs from Volume 2 by the factor \(|G|\) and by conjugation, and the multiplicity is Corollary 11.9.
5. Move the Schur–Weyl isomorphism at `ch11-compact.tex:189` into a remark, next to the sentence that already says it is not proved.

## Volume 10 — Chance II

*The Structure of Randomness.* Twelve chapters: zero–one laws, laws of large numbers, Donsker, the central limit theorem, stable laws, Stein’s method, large deviations, concentration, martingales, ergodic theory, mod-\(\varphi\) convergence, and random permutations.

### Mathematical correctness

**Slip, preface.** `preface.tex:30–31`: “Every result is proved, with one exception: the Selberg–Delange theorem.” Two further results are stated and not proved. In `ch05-stable.tex:209–212` the triangular-array converse (infinitesimal row sums have infinitely divisible limits, with the Lévy triple recovered) is sent to Gnedenko–Kolmogorov. At lines 296–299, non-symmetric stable laws are written down and attributed to Feller. The symmetric theory that is claimed is proved.

Donsker’s theorem (`ch03-donsker.tex:249–273`) is Skorokhod’s embedding plus a modulus comparison, under finite variance and mean zero. The Kolmogorov–Smirnov remark correctly says the empirical-process version is not proved. Lindeberg–Feller’s converse, Berry–Esseen with the book’s constant \(3.1\) (the bracket is about \(3.04\)), the local limit theorem, and Chung–Fuchs, including transience in dimension \(\ge 3\) with no moment assumption, are complete.

Cramér’s theorem (`ch07-ldp.tex:91–125`) assumes \(\Lambda(\theta)<\infty\) for every real \(\theta\), a stronger hypothesis than the classical neighbourhood of \(0\). Under that hypothesis the proof is complete. Bahadur–Rao is explicitly not proved. Sanov is only for a finite alphabet.

Roth’s theorem for three-term progressions is proved in full by Furstenberg’s correspondence principle (`ch10-ergodic.tex:288–428`), including the compact/weakly mixing split. Szemerédi’s theorem for longer progressions is stated as not proved. Volume 13, Chapter 12, proves the same length-three theorem by Fourier analysis. The two proofs do not cite each other.

No solution error turned up in the first and last solutions of Chapters 1–7 and 10–12. Chapters 8 and 9 were sampled more lightly.

### Writing quality

`ch07-ldp.tex:136–139` makes the point of large deviations with four numbers: a gamma tail, the Cramér bound, Bahadur–Rao, and a Gaussian tail. `ch10-ergodic.tex:434–437` asks where the argument used the ratio \(1:2\). `ch11-modphi.tex:210–221` displays Selberg–Delange and then paraphrases it as a mod-Poisson theorem; a reader can miss that the paraphrase is not proved in this volume. Nothing at the end of Chapter 12 points to Volume 5’s Erdős–Kac chapter or Volume 13’s Roth chapter.

### Depth

Against Durrett, Kallenberg, Dembo–Zeitouni, Ledoux, and Einsiedler–Ward, this is a strong one-volume graduate course. Present at reference level: Etemadi’s strong law, the three-series theorem, Lévy’s continuity theorem, Donsker in \(C[0,1]\), the Hartman–Wintner law, Lindeberg–Feller, Berry–Esseen, Lévy–Khintchine with uniqueness, symmetric stable domains, Stein and Chen–Stein, Cramér on \(\mathbb R\) under a global moment generating function, Sanov on a finite alphabet, McDiarmid, Gaussian concentration, Talagrand’s convex distance, de Finetti, Kakutani, Birkhoff, the Gauss map, and Furstenberg for three-term progressions.

Missing, and mostly said: tightness in \(D[0,1]\) and Donsker for the empirical distribution function; a martingale central limit theorem; non-symmetric stable laws; Cramér in \(\mathbb R^d\) and Cramér with the moment generating function finite only near \(0\); Schilder's theorem; Sanov for general spaces; multiple recurrence past \(k=3\).

### Exercises and solutions

The series pattern holds. The hardest exercises (Talagrand certificates, the Gauss-map exponent, Dickman) track the chapter.

### Coherence

The preface assumes Volumes 3, 6, and 7, and the reminders match. Brownian motion and the direct half of Lindeberg come from Volume 3; Prokhorov from Volume 6; compact operators from Volume 7, used for the weakly mixing lemma. Erdős–Kac is quoted from Volume 5 (`ch11-modphi.tex:8–9`). The mod-Poisson residue for a uniform integer is assigned to Volume 14. The existing draft `volume14-random/chapters/ch02-selbergdelange.tex` does contain that theorem; Volumes 0–13 do not.

### Readiness: 8

The probabilistic core can be taught as written. The preface’s completeness claim is larger than the stable-law chapter, and the last two chapters depend on Volumes 5 and 14 for their number-theoretic punchline.

1. Rewrite the preface sentence so that it also names the symmetric-only stable theory and the unproved array converse.
2. After the Feller formula in `ch05-stable.tex`, say that skewness is not proved and is not used later.
3. Cross-refer Volume 5’s Erdős–Kac theorem at the start of Chapter 11, and Volume 13’s Fourier proof at Roth.
4. At `ch11-modphi.tex:214–218`, label the uniform-integer statement as a corollary of the quoted Selberg–Delange formula.
5. Point from the Donsker introduction (`ch03-donsker.tex:17–19`) to the Kolmogorov–Smirnov remark, so “made Doob’s heuristic a proof” cannot be read as a result of this chapter.

## Volume 11 — Random Motion

*The Geometry of Random Paths.* Twelve chapters, from Gaussian processes through log-correlated fields, plus appendices on spectral graph theory and on zeta and random matrices.

### Mathematical correctness

The Itô integral (`ch04-ito.tex:111–129`), localisation, Itô’s formula, and Lévy’s characterisation are complete. Girsanov (`ch05-analysis.tex:90–111`) is proved for bounded drift. Novikov’s condition is stated and cited to Revuz–Yor (lines 113–117). Cameron–Martin for deterministic shifts in \(L^2\) is proved by approximation. Black–Scholes in Chapter 6 uses a constant drift, which is covered.

**Slip.** `ch06-sde.tex:430–434`. The theorem that precedes the remark is a complete proof that Hermitian Brownian motion started with distinct eigenvalues never collides and that the eigenvalues solve the \(\beta=2\) Dyson system. The remark then says that, started from \(H_0=0\), the eigenvalues separate at once and that \(\lambda(1)\) has the GUE joint density, “which Chapter 10 studies.” Chapter 10 studies the GOE semicircle, Marchenko–Pastur, and a Wigner spike. It does not derive \(\prod_{i<j}|\lambda_i-\lambda_j|^2\exp(-\sum\lambda_i^2/2)\), and the theorem excludes a multiple initial eigenvalue.

**Slip.** `ch10-semicircle.tex:298–304`. The outlier theorem for a spiked Wigner matrix \(W+\theta vv^\top\) is a complete secular-equation proof, and \(G(\theta+1/\theta)=1/\theta\) checks. The following remark states the Baik–Ben Arous–Péché transition for sample covariance and says “the proof is the one above, with the Marchenko–Pastur law in place of the semicircle.” The Stieltjes-transform idea is the same. The \(XX^\top\) secular equation is not written.

The almost-sure Wigner semicircle, Marchenko–Pastur for \(\gamma\in(0,1)\), and the Tracy–Widom remark (with the tails \(e^{-|s|^3/12}\) and \(e^{-(2/3)s^{3/2}}\), and with the longest increasing subsequence correctly limited to the concentration proved in Volume 10) are in the right register. Montgomery’s theorem is stated as “proved in Volume 13” (`ch11-cue.tex:384–389`). The cross-reference is right: Volume 13, Chapter 14, the fifteenth numbered statement, and Volume 13 calls the Volume 11 statement Theorem 11.13, which matches. The pair-correlation conjecture is labelled a conjecture. The matrix side that is claimed is proved: the sine-kernel limit from Volume 8’s Weyl formula, the gap series, the characteristic-polynomial factorisation, Keating–Snaith’s integer moments (including \(42/9!=1/8640\)), and the central limit theorem for \(\log|\det|\).

The tightness of \(\max\log|Z_n|-(\log n-\frac34\log\log n)\) is an admitted theorem (`ch12-logcorrelated.tex:235–237`). Appendix B proves the mean square of \(\zeta(\sigma+it)\) for fixed \(\sigma>1/2\) and quotes Hardy–Littlewood and Ingham on the critical line. Lévy–Itô, part (b) (`ch07-levy.tex:239–243`), reduces the identification of the jump measure to a one-paragraph claim that jumps of a càdlàg path are a measurable function of the values at rational times. That measurability is true and not written out. Ramanujan graphs are described in remarks; what is proved is Sunada’s eigenvalue form of the graph-theoretic Riemann hypothesis and the prime-number theorem for a non-bipartite Ramanujan graph.

### Writing quality

`ch04-ito.tex:4–19` puts Itô’s left endpoint, and Doeblin’s envelope, to work before any definition. `ch10-semicircle.tex:247–252` gives Tracy–Widom its tails and does not box it as a theorem. `ch11-cue.tex:348` has a stray capital in “Direct numerical experimentation”. `moments.tex:1–19` retells the tea of Chapter 11 and reprints a weaker semicircle law.

### Depth

Against Mörters–Peres or Karatzas–Shreve, the continuous stochastic calculus is a full first book: Kolmogorov–Chentsov, Lévy’s modulus, the zero set, quadratic variation, Itô, Tanaka and local time, Feynman–Kac, Girsanov for bounded drift, the Dirichlet problem, recurrence by dimension, strong existence for Lipschitz coefficients, and the Lévy–Itô decomposition. General predictable integrands, local time of semimartingales, and the full excursion measure are not here. There are no stochastic partial differential equations.

Against Anderson–Guionnet–Zeitouni: the global semicircle, Marchenko–Pastur, a Wigner spike, the sine kernel, gap probabilities as a Fredholm series, and Dyson Brownian motion for \(\beta=2\) from a simple spectrum. Tracy–Widom, bulk universality, and the identity \(p(s)=\mathrm d^2E(0;s)/\mathrm ds^2\) (cited to Mehta) are not proved.

### Exercises and solutions

Spot checks match: the three Riemann-sum conventions for \(\int B\,\mathrm dB\), the branching-random-walk maximum \(c_*=\sqrt{2\log 2}\), and the Abel limit of \(-\log|1-re^{ix}|\).

### Coherence

`main.tex` reads Chapters 1–12, then the spectral appendix, then the zeta appendix. Chapter 10’s reminder uses the appendix’s moment method and Theorem B.3 before that appendix has appeared. Chapters 8 and 9 rest on Appendix A (Cheeger is Theorem A.9, the mixing lemma is Lemma A.10, Alon–Boppana is Theorem A.11; those numbers match). The appendix proofs do not depend on Chapters 8–10, so there is no circle. The basic semicircle argument is easier than the chapter that quotes it and is printed after the unitary-matrix chapter as well.

Dependencies that are real: Volume 3 for Brownian motion, Volume 6 for Prokhorov, Volume 7 for Plancherel, Volume 8 for the finite-\(n\) circular ensemble (Theorem 8.15), Volume 10 for Gaussian concentration and Stein’s lemma. Volume 5’s zero-counting is used as a dictionary, not reproved.

### Readiness: 8

The stochastic-calculus half and the global random-matrix theorems can be taught as written. Two remarks state proofs the book does not contain, and the semicircle is used before its elementary proof is printed.

1. Move the moment-method half of Appendix B to the front of Chapter 10, and leave the zeta narrative in Chapter 11.
2. Delete or qualify `ch06-sde.tex:432–434`. State the entrance from a multiple eigenvalue as not proved.
3. In `ch10-semicircle.tex:302–303`, replace “the proof is the one above” by the statement that the sample-covariance spike is not derived here.
4. Add one sentence to the Tracy–Widom remark and to `ch11-cue.tex:186–189`: neither the limit law nor \(p(s)=\mathrm d^2E(0;s)/\mathrm ds^2\) is proved in this book.
5. Write the rational-time measurability step in Lévy–Itô (b), or mark part (b) as using it.

## Volume 12 — Arithmetic

*From Equations to Hidden Worlds.* Fourteen chapters, from number fields through modular forms.

### Mathematical correctness

**Error in the proof; the statement is the classical theorem.** `volume12-arithmetic/chapters/ch07-hasse.tex:417–423`, three squares.

> Let \(n=4^am\) with \(m\not\equiv 7\pmod 8\) (and \(4\nmid m\) or not, it does not matter). … \(-n=4^a(-m)\) is a square in \(\mathbb Q_2\) iff \(-m\equiv 1\pmod 8\), i.e. iff \(m\equiv 7\pmod 8\).

The local criterion is right when \(m\) is odd: \(4^a\) is a square in \(\mathbb Q_2^\times\), and an odd unit is a square if and only if it is \(1\) modulo \(8\). If \(4\) divides \(m\), the test is false. For \(n=28=4^0\cdot 28\), one has \(28\not\equiv 7\pmod 8\), so the written test says that \(-28\) is not a square in \(\mathbb Q_2\). Then “it suffices that the discriminant is not a square” is applied, and the proof concludes that \(\langle 1,1,1,-28\rangle\) is isotropic over every \(\mathbb Q_v\), hence that \(28\) is a sum of three rational squares. It is not: \(28=4\cdot 7\) and \(7\equiv 7\pmod 8\). In fact \(-28=4\cdot(-7)\) and \(-7\equiv 1\pmod 8\), so \(-28\) is a square in \(\mathbb Q_2\). The same chapter’s solution of Exercise 7.1 treats \(28\), \(7\), and \(7/4\) as one square class and gets the right answer. Hasse–Minkowski itself, and the Davenport–Cassels lemma, check. The repair is to require \(m\) odd before the 2-adic test.

**Gap.** `ch09-tate.tex:655–665`. Hecke’s functional equation for a general number field is said to follow “word for word” from the rational case. Haar measure on each completion, the additive character \(\psi\circ\mathrm{Tr}\), and Poisson summation on the adèles are not written. Tate’s thesis for \(\mathbb Q\), including primitive Dirichlet \(L\)-functions, is proved.

**Slip.** `ch14-modular.tex:427–430`. The beauty paragraph says the Riemann hypothesis for curves bounds the coefficients of \(\eta(\tau)^2\eta(11\tau)^2\) by \(|c_p|\le 2\sqrt p\). Hasse’s bound is proved for \(y^2=f(x)\). The identification \(c_p=a_p\) is a numerical check for \(p<10^5\) plus Eichler–Shimura, which is only a remark.

**Slip.** `preface.tex:31`: “Every result is proved, apart from the two admitted theorems.” Artin reciprocity and the existence theorem are marked admitted in their headings, which is the right standard. Mazur’s torsion theorem, modularity, Sato–Tate, Weil’s theorem for a general curve, and the second case of regular Fermat sit in remarks and are not proved. The three-squares sentence in the preface (“settles which integers are sums of three squares”) describes a proof that, as printed, does not.

| Theorem | Where | Status |
| --- | --- | --- |
| Unique factorisation of ideals in \(\mathcal O_K\) | ch. 2 | Proved |
| Minkowski, finiteness of the class group | ch. 3 | Proved |
| Dirichlet’s unit theorem | ch. 4; again from Fujisaki in ch. 9 | Proved |
| Kronecker–Weber | ch. 10 | Proved |
| Hasse–Minkowski | ch. 7 | Proved |
| Three squares | ch. 7 | Statement classical; the 2-adic test fails if \(4\mid m\) |
| Class-number formula; \(\zeta_K\) on \(\mathrm{Re}\,s>1-1/n\) | ch. 8 | Proved |
| Functional equation of \(\zeta_K\) | ch. 9 | Proved for \(\mathbb Q\); sketch for a general field |
| Chebotarev | ch. 8 | Proved in Dirichlet density; natural density explicitly not |
| Tate’s thesis | ch. 9 | Proved for \(\mathbb Q\) and primitive Dirichlet \(L\)-functions |
| Artin reciprocity, existence, the Hilbert class field | ch. 10 | Stated, marked admitted |
| Riemann–Roch for smooth plane curves | ch. 11 | Proved |
| Group law, Nagell–Lutz | ch. 12 | Proved |
| Mordell–Weil | ch. 12 | Proved for \(E(\mathbb Q)\); over a general number field, stated |
| Hasse’s bound | ch. 13 | Proved for \(y^m=f(x)\); Weil for a general curve, stated |
| Modularity | ch. 14 | Stated. The functional equation of \(\eta^2\eta(11\tau)^2\) is proved |
| First case of Fermat for regular primes | ch. 5 | Proved |

### Writing quality

`ch10-cft.tex:299–308` labels Artin reciprocity “admitted, not proved in this series” in the theorem heading. `ch08-zeta.tex:747–751` separates natural density from the Dirichlet-density theorem in one sentence. `ch12-elliptic.tex:361–364` names the Tate–Shafarevich group as the gap in the descent, and does not sell the descent as an algorithm. `ch07-hasse.tex:418`, “and \(4\nmid m\) or not, it does not matter”, is the sentence that breaks the three-squares proof.

### Depth

Against Marcus, Chapters 6–14 are beyond the Minkowski bound. Against Neukirch and Cassels–Fröhlich, the algebraic core through units, ramification, and local fields is complete, and Tate’s thesis for \(\mathbb Q\) is written out. Missing: the functional equation of \(\zeta_K\) as a theorem, idèlic class field theory as a proof, and the cohomology proof of Artin reciprocity. Against Silverman’s *Arithmetic of Elliptic Curves*: the group law, Nagell–Lutz, reduction, and Mordell over \(\mathbb Q\) are here, with a full 2-descent for \(y^2=x^3-x\) and \(y^2=x^3-4x\). The canonical height is named and not proved as a quadratic form. Siegel’s theorem on integral points, isogenies, and the general Selmer group are absent. The \(n\)-Selmer group is not constructed; the Tate–Shafarevich group is named. Genus theory of the 2-rank of the class group is not developed. The Hasse bound is proved by the Stepanov–Bombieri method for \(y^m=f(x)\), which is more elementary than Weil and narrower than Weil.

### Exercises and solutions

Spot checks that came out right: class numbers of \(\mathbb Q(\sqrt{-p})\) and \(\mathbb Q(\sqrt 2)\); the regulator of a real quadratic field; \(\mathbb Q_p\not\cong\mathbb Q_q\); the Hilbert class field of \(\mathbb Q(\sqrt{-5})\) and of \(\mathbb Q(\sqrt{-23})\); \(j=q^{-1}+744+196884q+\cdots\); the \(E_8\) theta series equal to \(E_4\).

### Coherence

Notation matches earlier volumes: \(\mathcal O_K\), \(N(I)\), \((r_1,r_2)\), decomposition group, Frobenius, the Hilbert symbol. Volume 5’s large sieve is Theorem 8.8. Volume 9 is the home of the abstract Dedekind axioms; this book stays with \(\mathcal O_K\). Volume 13, `ch03-sieves.tex:358`, cites “\(\mathbb Q(\sqrt 2)\), of discriminant \(8\) (Volume 12, Theorem 2.15)”. Theorem 2.15 is the ramification criterion “\(p\) ramifies if and only if \(p\mid d_K\)”. The value \(d_{\mathbb Q(\sqrt 2)}=8\) is a figure in Chapter 1.

### Readiness: 8

The algebraic theorems a capstone would cite are proved, and the two gaps in class field theory are labelled in the chapter. The three-squares slip is the one place a written proof reaches a false conclusion about a concrete integer.

1. In the proof of three squares, require \(m\) odd, and only then test \(-m\equiv 1\pmod 8\).
2. Call the general-field sentence at `ch09-tate.tex:655–665` a sketch, or write the missing Haar and Poisson steps. The preface’s “Tate derives the functional equation” is true for Riemann’s zeta and for Dirichlet \(L\)-functions.
3. In the Chapter 14 beauty paragraph, do not attribute \(|c_p|\le 2\sqrt p\) to the curve Riemann hypothesis unless Eichler–Shimura is marked as quoted.
4. Narrow the preface so that remarks (Mazur, modularity, Sato–Tate, general Weil, the second case of Fermat) are outside the sentence “every result is proved”.
5. Point the discriminant \(8\) at Chapter 1. Leave Theorem 2.15 as the ramification criterion, and correct the citation in Volume 13, Chapter 3.

## Volume 13 — Primes in Depth

*The Hidden Rhythm of Primes.* Fourteen chapters, from zero density through the critical line.

### Mathematical correctness

No false theorem statement turned up in the proofs read line by line: Vaughan’s identity and the passage to Bombieri–Vinogradov, Siegel’s ineffective argument, the Hardy–Ramanujan major and minor arcs, Vinogradov’s three-prime asymptotic, the Goldston–Pintz–Yıldırım ratio, Maynard’s reduction to \(M_k\), Roth’s density increment, the generalised von Neumann inequality, and Hardy’s theorem on zeros. Ineffective constants are named as ineffective.

Green–Tao is titled “quoted”. The \(W\)-trick, the Gowers norms, the generalised von Neumann theorem, and the \(U^2\) inverse theorem are proved. The inverse theorem for \(U^{s+1}\), the linear forms condition, and the relative Szemerédi theorem are not.

**Slip, a certificate that is not on the page.** `ch09-maynard.tex:165`. “A numerical calculation carries out both computations; they reproduce Maynard’s value.” The bound of \(600\) rests on \(M_{105}>4.002\) and Engelsma’s admissible tuple. The vector is not printed. The case \(k=5\) is given as explicit rationals and can be checked. The sieve theorem does not need the certificate; the numerical bound does.

The approximate functional equation is Theorem (Hardy and Littlewood, 1921; quoted) at `ch14-critical.tex:232`. It is not proved. Montgomery’s pair correlation is proved under the Riemann hypothesis for \(0\le\alpha\le 1-\varepsilon\). The form factor for \(\alpha\ge 1\) is stated as Montgomery’s conjecture.

| Theorem | Where | Status |
| --- | --- | --- |
| Carlson’s zero density; primes in intervals of length \(x^\theta\), \(\theta>3/4\) | ch. 1 | Proved. Huxley, Baker–Harman–Pintz, Guth–Maynard quoted |
| Siegel and Siegel–Walfisz | ch. 2 | Proved, ineffective |
| Parity for the Liouville weight | ch. 3 | Proved. For twins, “believed, not proved” |
| Chen | ch. 3 | Quoted |
| Bombieri–Vinogradov, level \(\theta<1/2\) | ch. 4 | Proved, ineffective via Siegel |
| Exponential sums over primes | ch. 5 | Proved. The Vinogradov mean value theorem and Weil’s Kloosterman bound quoted |
| Hardy–Ramanujan asymptotic for \(p(n)\) | ch. 6 | Proved, with an \(O(n^{-1/4})\) factor. Rademacher quoted |
| Every large odd number is three primes | ch. 7 | Proved, ineffective. Helfgott stated |
| Waring for \(s\ge 2^k+1\) | ch. 7 | Proved. Positivity of the singular series quoted |
| GPY, conditional on a level of distribution past \(1/2\) | ch. 8 | Proved as a conditional theorem. Zhang quoted |
| Maynard’s bounded gaps | ch. 9 | Sieve deduction proved. The explicit \(600\) rests on an unprinted computation. Polymath’s \(246\) quoted |
| Halász, Delange, Wirsing, the mean of \(\mu\) | ch. 10 | Proved. Matomäki–Radziwiłł quoted |
| Plünnecke–Ruzsa, Balog–Szemerédi–Gowers, Elekes; Freiman in \(\mathbb F_2^n\) | ch. 11 | Proved. Freiman in \(\mathbb Z\) quoted |
| Roth, with \(500N/\log\log N\) | ch. 12 | Proved. Szemerédi and Kelley–Meka quoted |
| Green–Tao | ch. 13 | Quoted. The \(W\)-trick and \(U^2\) theory proved |
| Infinitely many zeros on the critical line; the mean square on the critical line | ch. 14 | Proved |
| Montgomery, \(0\le\alpha\le 1-\varepsilon\), under RH | ch. 14 | Proved |
| A positive proportion of zeros on the critical line | ch. 14 | Quoted |

### Writing quality

`ch13-gowers.tex:126–128` separates the \(W\)-trick, which is proved, from the relative Szemerédi theorem, which is quoted. `ch04-largesieve.tex:168–174` states the level \(\sqrt x\,(\log x)^{-A-6}\) and says the constant cannot be computed. `ch03-sieves.tex:305` distinguishes the parity obstruction for twins from the theorem for the primes. `ch01-zeros.tex:294` lists Huxley, Baker–Harman–Pintz, and Guth–Maynard and labels them “quoted, not proved”. This is the most careful register in the series.

### Depth

Against Davenport: the large sieve, Vaughan’s identity, and a complete Bombieri–Vinogradov theorem are past Davenport’s outline, and the three-prime theorem is proved. Against Montgomery–Vaughan: Siegel, Halász, the second moment on the critical line, and pair correlation under RH are proved; Vinogradov–Korobov and Huxley’s density estimate are not. Against Iwaniec–Kowalski the spectral theory is absent: no Kuznetsov formula, no subconvexity, no theorem on averages past \(\sqrt x\). Against Tao–Vu: Roth, Plünnecke, Balog–Szemerédi–Gowers, and Freiman in \(\mathbb F_2^n\) are proved; Szemerédi’s theorem and the higher inverse theorems are quoted.

### Exercises and solutions

Spot checks that came out right: the end of Carlson’s exponent with a mollifier of length \(T\); Hilbert’s inequality with constant \(\pi\); the \(U^2\) norm as an \(\ell^4\) norm of the Fourier transform; a quadratic phase with \(U^3\)-norm \(1\).

### Coherence

The book assumes Volume 5 and cites Volumes 4, 7, 10, and 12 by number. Meshulam is Volume 7, Theorem 7.16. Chebotarev is Volume 12, Theorem 8.23. The one bad pointer is the discriminant of \(\mathbb Q(\sqrt 2)\) as Theorem 2.15. Volume 11’s Theorem 11.13 is identified with Montgomery’s theorem in Chapter 14, and the numbers match. Notation for \(\psi(x,\chi)\), primitive characters, and the level of distribution is stable from the large sieve through Maynard.

### Readiness: 8

Bombieri–Vinogradov, Siegel, the circle method, Halász, and Roth are in a form a later volume can cite. Green–Tao is not overclaimed. The unreproduced certificate for the gap \(600\) is the main softness.

1. Print the rational witness for \(M_{105}>4.002\) and Engelsma’s tuple, or mark the bound \(600\) as depending on a computation that is not in the book.
2. Keep Green–Tao labelled quoted in every cross-reference. The proved pieces are the \(W\)-trick, the Gowers norms, and the generalised von Neumann theorem.
3. Repair the Volume 12 citation for the discriminant of \(\mathbb Q(\sqrt 2)\).
4. The preface’s “short list” of quoted theorems is long (Zhang, Weil, the Vinogradov mean value theorem, Chen, Szemerédi, Green–Tao, the inverse theorem, Rademacher, a positive proportion of zeros, Matomäki–Radziwiłł). The individual labels are accurate; the preface should not call the list short.
5. State, in one sentence a capstone can repeat, that three primes, Siegel–Walfisz, and Bombieri–Vinogradov share one ineffective constant.

## Volume 15 — The Research Workshop

*From Understanding to Discovery*, in `common/volume-subtitles.json`. The book title remains *The Research Workshop*. Twelve chapters and twelve appendices, about 9,700 lines. The preface describes twelve chapters and never mentions the appendices.

Chapters 1–10 and 12 prove things. Chapter 11 and Appendices A–D and F–L each prove one partial theorem and then explain why a famous conjecture remains open. Appendix E, `conjectures-ch05-zetarmt.tex`, is three lines: a pointer to Volume 11, Appendix B.

| Chapter or appendix | Lines | What it actually contains |
| --- | --- | --- |
| 1 How Research Works | 485 | Dissociated sets, the counting bound, Conway–Guy, a sharpened Erdős–Moser bound, and two elementary steps of a 2026 argument. The density theorem that finishes it is stated and not proved. The section title can be read as a complete proof. |
| 2 How to Read a Paper | 436 | Three passes on one note. Moser’s variance, Berry–Esseen for Rademacher sums with constant \(6.3\lambda\), and a shortcut that fails. |
| 3 Shuffling Cards | 419 | A reading map onto Volume 9, then a full proof of the Bayer–Diaconis limit profile. |
| 4 Selberg at Many Points | 298 | Takes a one-point approximation from the Volume 14 draft and proves a multipoint Gaussian limit for \(\log|\zeta|\). |
| 5 Random Groups | 278 | Cokernels of symmetric matrices and a corank chain. The matrix-tree theorem is quoted from Volume 11. |
| 6 Better Than Square Root | 277 | A reading map of Harper, then \(\mathbb E[W_n^{1/2}]\le Cn^{-1/4}\) with \(C<5.4\) for the critical branching random walk. |
| 7 From Data to Conjecture | 337 | The BBP formula, hexadecimal digits, and LLL with the factor \(2^{(n-1)/2}\). |
| 8 Heuristics That Predict | 304 | Three cubes: the mod-9 obstruction, local densities, Booker’s factorisation. Heath-Brown’s prediction is labelled a conjecture. |
| 9 Proofs a Computer Can Check | 350 | Curry–Howard for the implicational fragment, and that Peirce’s law is not provable. |
| 10 Writing It Down | 248 | The shape of a paper, then Jordan’s theorem for simple polygons. |
| 11 Problems to Work On | 278 | Seven open problems, each with a small theorem (Singmaster, lonely runner for two speeds, graceful caterpillars, Lehmer, Brocard, a weak Sendov bound). |
| 12 Five Projects | 193 | Project statements. The thinnest chapter. |
| A Conjectures born and die | 518 | Pólya, Landau’s oscillation theorem, and the Borwein sinc integrals, with an explicit first deficit. |
| B Twin primes and gaps | 471 | A Selberg upper bound, Erdős’s small gaps, Westzynthius’s large gaps, the parity barrier. |
| C Goldbach | 473 | Schnirelmann’s theorem that the primes are an additive basis of finite order. Ternary Goldbach is a paper to read. |
| D The Riemann Hypothesis | 442 | Gronwall, Robin’s criterion quoted, the easy half of Lagarias. |
| E Random matrices and zeta | 3 | A pointer. No mathematics. |
| F Collatz | 552 | Terras, the cycle equation, and a Farey bound of \(72\,057\,431\,991\) odd terms. |
| G Hadamard matrices | 500 | Hadamard’s bound, Sylvester, both Paley constructions, Williamson. |
| H Points and distances | 642 | The chromatic number of the plane, Szekély’s unit-distance bound, Erdős–Szekeres, Gilmer’s entropy argument. |
| I The \(abc\) conjecture | 490 | Mason–Stothers and Fermat for polynomials; a reduction of Erdős–Straus. |
| J Birch–Swinnerton-Dyer | 494 | Point counts by Jacobi sums; rank 0 and 1 quoted from Volume 12’s modularity package. |
| K Randomness in the integers | 533 | Chowla patterns, a case of the Erdős discrepancy problem, Artin’s conjecture on average, Cohen–Lenstra. |
| L Open doors in algebra | 612 | Inverse Galois for abelian groups and for \(S_n\), Smyth’s Mahler-measure bound, Ax–Grothendieck over finite fields. |

### Mathematical correctness

Constants that were recomputed and found right include the Erdős–Moser optimisation, Moser’s variance sum, the Berry–Esseen smoothing bound \(6.3\lambda\), the Bayer–Diaconis distance, the BBP partial fractions, the three-cubes integers, Gronwall’s limsup, the Borwein deficit, the Gilmer constant \((1-\ln 2)/2\), the Collatz Farey neighbours, and the symmetric-corank weights. No false theorem turned up in that sample.

**Gap.** `ch10-writing.tex:117–119`. After one cycle of the side graph is removed, “the other \(2n\) nodes form a second cycle” is true for this polygon graph and is not true of a general 2-regular graph. The forced walk around the other side is left implicit. The chapter itself sets a rewrite of a nearby sentence as an exercise.

**Gap.** `conjectures-ch09-abc.tex:110–112`. The leading terms of \(ab'\) and \(a'b\) have degree \(\deg a+\deg b-1\), not \(\deg a+\deg b\). The bound \(\deg W\le\deg a+\deg b-1\) that the proof uses is the correct one.

### Writing quality

`ch03-shuffling.tex:259–263` (“Seven is where the distance for 52 cards first falls below \(\frac12\) (\(0.334\)); after six it is still \(0.614\)”) is the workshop’s standard. `ch08-heuristics.tex:116–122` separates Heath-Brown’s conjecture from the theorems. The preface is silent on twelve appendices that are half the book.

### Depth, exercises, coherence

Against its preface, Chapters 1–10 deliver a workshop. Chapter 12 is a launch pad. The appendices are a second book of open-problem case studies. Main text: 75 exercises, 75 hints, 75 solutions. Appendices: 107 of each, and Appendix E has none. Citations that were checked resolve: Volume 3’s reflection formula, Volume 5’s sieve lemma \(\sum_{d\le y}\mu^2(d)/\varphi(d)\ge\log y\), Volume 9’s symmetric group. Chapter 4 cites the Volume 14 draft for Selberg’s one-point approximation. That approximation is not a theorem of Volumes 0–13.

### Readiness: 7

The proved workshop is in good shape. The book is too long for its preface, Appendix E is empty, and half the appendices repeat Volumes 5, 11, 12, and 13. The condensation into the capstone is in `CAPSTONE-PLAN.md`.

1. Write Appendix E, or stop counting it as an appendix.
2. Say in the preface that Appendices A–L are conjecture case studies and that E is a pointer.
3. Repair `ch10-writing.tex:117` and `conjectures-ch09-abc.tex:110`.
4. In Chapter 1, put “the density theorem is not proved here” in the statement a reader will quote, not only in the section body.
5. For the capstone, keep the method and cut the tours that Volumes 5, 11, 12, and 13 already own. The map is in the plan.

## Problem Book P1 — Crossroads

*Problems Across Mathematical Borders.* Fourteen chapters. The preface promises 300 problems, graded \(\star\) through Journey, with a hint, a “how to find it”, a complete write-up, and the volumes used. The count is exact: 300 exercises, 300 hints, 300 solutions. Chapters 1–12 have 22 problems each, Chapter 13 has 20, and Chapter 14 has 16, every one a Journey. Stars: 34 one-star, 169 two-star, 69 three-star, 28 Journey. Chapters 10, 11, and 14 have no one-star problem. The preface’s sentence that “a few \(\star\) problems open each chapter” does not hold for those three.

### Mathematical correctness

Eight solutions were recomputed, including Chapters 13 and 14.

- \(\sum_{p\le x}p\sim x^2/(2\log x)\), and the same sum against \(\mathrm{Li}(x^2)\). The substitution \(s=t^2\) is right. Part (d) of this one-star problem asks for the zero-free error \(O(x^2e^{-c\sqrt{\log x}})\). That is not an opening exercise (`ch13-average.tex:43`).
- \(\sum_{n\le x}P^+(n)\sim\frac{\pi^2}{12}x^2/\log x\). The constant is \(\frac12\zeta(2)\).
- The mean of \(\mathrm{rad}(n)/n\) is \(\prod_p(1-1/(p(p+1)))\).
- \(\omega\bigl(\binom{2n}{n}\bigr)\sim 2\log 2\cdot n/\log n\).
- Jacobi’s four-square theorem. The printed check \(\sum_{n\le 10^7}r_4(n)=493\,480\,252\,693\,888\) matches the claimed factor.
- Local densities for \(r_4(n)\). The end formula agrees with Jacobi. The count modulo 8 (`ch14-meets.tex:575–581`) asserts \(512\), \(768\), and \(256\) rather than deriving each residue class.
- Székely’s incidence bound, consistent with the unit-distance argument in Volume 15, with a slightly weaker constant.

No wrong solution turned up in this sample.

### Writing, depth, coherence

The Chapter 13 opening uses the Lemke Oliver–Soundararajan bias, with the figure \(17.7\%\) after a prime ending in 1, and says what the coin model will not explain. The promise of the preface is met: statements that do not name the tool, hints apart from solutions, and a map at the end of each chapter. The intended dependence is Volumes 0–5. Chapter 8 does not stay there. The spectral problems cite Volume 11, Appendix A, as a required tool (`ch08-inequalities.tex:541`, `:588`, `:609`), not as a remark in “where it leads”.

### Readiness: 8

This is a complete problem book of the kind the preface describes.

1. Re-level the large-prime-factor problem in `ch13-average.tex:43`. Part (d) is not one-star.
2. Re-prove the three spectral arguments in Chapter 8 from Volume 0, or change the preface so Volume 11 is an allowed tool.
3. Adjust the grading sentence in the preface, or add one-star openers, so that Chapters 10, 11, and 14 match it.
4. Expand the residue count modulo 8 in `ch14-meets.tex:575–581` until each of \(512\), \(768\), and \(256\) is derived.
5. Do one numerical pass on the remaining “one finds” claims in Chapters 10–12.

## Problem Book P2 — Machinery

*The Tools Behind the Proofs.* The preface promises 300 problems on Volumes 6–9. `main.tex` inputs two chapters: 22 problems on metric Diophantine approximation (`ch01-almost.tex`) and 22 on Hilbert space (`ch02-hilbert.tex`). That is 44 problems, \(44/300\). A third file, `drafts/ch03-operators.tex`, has 22 problems with hints and solutions and is not in the book. `HANDOFF.md` says Chapters 4–14 are not started. The README line “2 of 14 chapters” matches `main.tex`.

The two chapters that are in the book are written to the standard of P1. The convergence half of Khinchin (`ch01-almost.tex:419–441`) covers \(E_q\) by \(q+3\) intervals and gets measure at most \(8q\psi(q)\); Borel–Cantelli applies. Bounded partial quotients are equivalent to badly approximable numbers, with \(c=1/(K+2)\). The tools named in Chapter 1 are Volume 6, Volume 10’s Gauss map, and Volume 1’s continued fractions.

### Readiness: 2

The score is against the preface. Judged alone, the two written chapters are at the level of Book I.

1. Do not move `drafts/ch03-operators.tex` into the book until it has its figures, its notebook, and a rereading of the solutions.
2. Change the preface so that it describes two chapters, until Chapters 4–14 exist.
3. Leave the constant \(8q\psi(q)\) alone. It is crude and correct.
4. Write the Volume 6–8 chapters before the Volume 9 chapters.
5. Use the tools-and-map audit of Book I before any further chapter is called done.

## Problem Book P3 — Frontiers

*Problems Beyond Familiar Ground.* The preface promises 300 problems on Volumes 10–15. `main.tex` inputs one chapter, `ch01-pieces.tex`, with 22 problems: local limit theorems, signed sums, Bernoulli convolutions, and real roots of random polynomials. That is \(22/300\). A second file, `ch02-rare.tex`, has 22 problems and is not an input. `HANDOFF.md` calls it a first draft. The README line “1 of 14” matches the book.

Chapter 1’s opening, Lindeberg’s swap of one variable at a time, is finished prose. The draft of Chapter 2 is not safe to add.

**Error in a draft solution, not in the book `main.tex` builds.** `ch02-rare.tex:702–705`. The problem at line 156 asks for discrepancy at most \(\sqrt{2n\log(2n)}\). The union bound is
\[
n\cdot 2e^{-\log(2n)}=1.
\]
A bound of 1 does not prove existence. The strictness of Hoeffding’s inequality is asserted, not proved. The parenthetical repair changes the constant to \(\sqrt{2n\log(4n)}\), which is not what the problem asks for.

**Gap in the same draft.** `ch02-rare.tex:729–732`. The problem asks for Hamming distance strictly less than \(\sqrt{2ns}\). The solution stops at “up to rounding, which is the content.”

**Slip in the same draft.** Line 707 breaks off inside a formula (“So \(|H\chi|^2=\chi^THH^T\chi\cdots\) more simply”). Line 682 still has the placeholder “at a cost about \(p/\text{something}\) per step”. Line 285 grades an exercise `[Journey/$\star\star\star$]`, which is not a grade the preface defines. The figures `ch02-rem` and `ch02-markovrate` are named and unwritten.

### Readiness: 2

One chapter of a fourteen-chapter book is in the document, and it is a real chapter. The next file is not ready to join it.

1. Prove the discrepancy bound at the constant the problem states, or change the problem to the constant the union bound gives.
2. Prove the blow-up distance with an integer, including the ceiling.
3. Delete the broken sentence at line 707 and the placeholder at line 682.
4. Replace the grade at line 285 with one grade.
5. Only then add the two figures and `\input{chapters/ch02-rare}`. Chapters 3–14 are unstarted.

## Series-level findings

### Overlaps

The same theorem is often proved twice, on purpose, and the second copy does not say so.

- **Erdős–Kac** is proved in Volume 5, Chapter 9, quoted in Volume 10, Chapter 11, drafted again in `volume14-random`, Chapter 3, and touched by P1 and by Volume 15, Appendix K.
- **Roth’s theorem** is proved in Volume 10 by ergodic theory and in Volume 13, Chapter 12, by Fourier analysis. Neither proof cites the other.
- **Pair correlation** is proved for the finite unitary group in Volume 8, passed to the sine kernel in Volume 11, Chapter 11, told again in Volume 11, Appendix B, proved for the zeros under the Riemann hypothesis in Volume 13, Chapter 14, and reduced to a pointer in Volume 15, Appendix E.
- **Sieves** run from Volume 5 (Selberg, Brun, the large sieve) through Volume 13 (parity, Bombieri–Vinogradov, Goldston–Pintz–Yıldırım, Maynard) into Volume 15, Appendix B (elementary small and large gaps).
- **The zeta functional equation** is proved in Volume 4, used analytically in Volume 5, recovered from Ikehara in Volume 7 as a second proof of the prime-number theorem, and proved again for \(\mathbb Q\) by Tate’s thesis in Volume 12.
- **Dedekind domains** are axiomatised in Volume 9 and proved for rings of integers in Volume 12. That split is clean.
- **Card shuffling** is mentioned in Volume 3, proved as a cutoff in Volume 9, Chapter 10, and read as a paper in Volume 15, Chapter 3. The Bayer–Diaconis profile is the piece that is only in Volume 15.
- **Brownian motion** is constructed in Volume 3, embedded by Donsker in Volume 10, and given its stochastic calculus in Volume 11. The dependence is in the right order.
- **Chebyshev’s bias** is developed in Volume 5, Chapters 4 and 7, illustrated numerically in P1, Chapter 13, and drafted again in `volume14-random`, Chapter 9.

The duplication is a choice of method when both proofs are real (Roth, the prime-number theorem, Dedekind). It is a defect when the second text does not know the first exists, and when a remark in one volume is typeset as a theorem in the next.

### Gaps

These are absent from Volumes 0–13 as proofs, and at least one later chapter needs them or pretends to. The capstone plan marks each as prove, state, or cut.

- Buchstab’s theorem and Maier’s theorem (named in Volume 5, Chapter 10; Buchstab is drawn in Volume 13, Chapter 3, and both are proved only in the Volume 14 draft).
- The Selberg–Delange theorem (quoted in Volume 10, Chapter 11, and assigned to Volume 14).
- Selberg’s central limit theorem and the short Dirichlet-polynomial approximation of \(\log|\zeta(\tfrac12+it)|\) (used by Volume 15, Chapter 4, from the Volume 14 draft).
- The approximate functional equation (quoted in Volume 13, Chapter 14).
- The higher Gowers inverse theorem, the linear forms condition, and the relative Szemerédi theorem (quoted with Green–Tao).
- Artin reciprocity and the existence theorem (admitted in Volume 12).
- Modularity of elliptic curves, and root numbers of quadratic twists (stated in Volume 12).
- Genus theory of the 2-rank, and the \(n\)-Selmer group as a general construction.
- Primary decomposition (Volume 9).
- The unbounded spectral theorem and the converse of Bochner’s theorem (Volume 7).
- de Rham’s theorem beyond the punctured plane (Volume 8).
- The tower property of conditional expectation as a numbered theorem (Volume 6).

A positive proportion of zeros on the critical line, Chen’s theorem, Zhang’s theorem, Helfgott’s theorem, and the Vinogradov mean value theorem are quoted and labelled. They are not silent gaps.

The catalog disagrees with itself about the book this review does not score. `common/series.tex` and the README still title Volume 14 *Random Arithmetic* and keep Volume 15 as a separate book. `common/volume-subtitles.json` already gives Volume 14 the subtitle *Where Number Meets Randomness* and Volume 15 the subtitle *From Understanding to Discovery*. The restructuring that replaces Volume 14 and absorbs Volume 15 has reached the subtitle file and not the series page.

### Notation

The clashes that will confuse a reader who moves in order:

- **\(\Lambda\).** Completed zeta in Volume 4 and, “only here”, in Volume 5, Chapter 6. Von Mangoldt’s function from Volume 5 on. Legendre’s \(\Lambda(k)\) in Volume 4, Chapter 12.
- **\(\theta\).** Jacobi theta in Volume 4. Chebyshev’s function from Volume 5 on.
- **\(\omega\).** The theta remainder in Volume 4. The number of distinct prime factors from Volume 5 on. \(\Omega\) is reserved for the total number of prime factors, and Volume 5 keeps the two apart.
- **\(\psi\).** Digamma against Chebyshev. Volume 5 writes \(\psi_\Gamma\) and says why.
- **\(\Delta\).** Modular function and Vandermonde product, twenty lines apart, in Volume 8, Chapter 8.
- **Fourier normalisation.** Volume 2 puts \(1/|G|\) in the analysis. Volume 9, Chapter 10, puts it in the synthesis, and also conjugates. The comparison sentence at `ch10-shuffling.tex:32` records only the conjugation.
- **\(q\).** A modulus for eleven chapters of Volume 5, then the nome \(e^{2\pi i\tau}\). Standard, and still a trap. Volume 12 inherits both uses.
- **\(\mathrm{Li}(x)\).** \(\int_2^x\mathrm dt/\log t\) in Volume 5. Later volumes should not switch to a lower limit of \(0\) without a sentence.
- **\(\chi\).** A Dirichlet character, a group character, and, in Volume 13, Chapter 14, the factor \(\chi(s)\) in the functional equation.
- **\(D_n\).** Order \(2n\) in Volume 2, used consistently. Later volumes should not switch to the order-\(n\) convention.
- **Probability.** \(P\) is Kolmogorov’s measure in Volume 3. It is also a prime ideal and a polynomial. The distinction is by font more often than by a sentence.

Homology \(H_n\), de Rham cohomology \(H^k(M)\), and group cohomology \(H^n(G,M)\) are separated by the index. That convention should be kept in the capstone and not reinvented.

### Recommended order of work

Other agents own the rewrites of Volumes 0 and 1 and the restructuring of Volumes 14 and 15 and of P2 and P3. The order below is the one in which the mathematical defects found here should be cleared. None of it requires editing a book that those agents have open, except where a citation into Volume 12 or 13 is already wrong.

1. **Repair the four arguments that assert something false or evaluate the wrong expression.** Volume 12, three squares (`ch07-hasse.tex:417–423`). Volume 7, the sign in Wiener’s local inverse (`ch10-tauberian.tex:270–273`). Volume 4, the factor \(\frac12\) in the functional equation (`ch10-zeta.tex:188`). Volume 5, the names liminf and limsup (`ch01-mertens.tex:131–132`) and the Brun–Titchmarsh paragraph (`ch08-sieves.tex:149–151`). These are short, and later volumes cite the surrounding theorems.
2. **Repair the gaps that a citation already stands on.** The primitive element theorem in Volume 2, before the Galois correspondence uses it. The three simple real roots in the same chapter. The face of the box in Volume 6. The division by \(n!\) in Andreief’s identity. The word “isomorphism” at Volume 9, `ch05-dedekind.tex:328`. The discriminant pointer in Volume 13, Chapter 3.
3. **Make the prefaces and the blurb match the chapters.** Volume 7’s blurb (the unbounded spectral theorem, “every theorem is proved in full”). Volume 10’s “one exception”. Volume 12’s “every result is proved, apart from the two admitted theorems”. Volume 5’s Maier display, which should become a remark until it is proved. Volume 13’s preface should stop calling its list of quotations short. Volume 15’s preface should mention the appendices, and Appendix E should be written or removed.
4. **Leave P2 and P3 unpublished as 300-problem books** until the missing chapters exist. P3’s draft of Chapter 2 should not be added while the discrepancy and blow-up solutions fail to prove the stated bounds. P1 is ready, apart from the five fixes above.
5. **Write the capstone after steps 1 and 2**, mining `volume14-random` for Selberg–Delange, Bohr–Jessen, Selberg’s central limit theorem, and the Cohen–Lenstra moment calculations, and condensing Volume 15 as in the plan. Do not restart Erdős–Kac, Bombieri–Vinogradov, Montgomery’s theorem under the Riemann hypothesis, or the sine kernel.
6. **A notation pass** on \(\Lambda\), \(\theta\), \(\omega\), \(\Delta\), and the Fourier factor \(1/|G|\) can ride with the capstone. It should not block the local repairs.
7. **Re-check every capstone citation into Volumes 0 and 1** when those rewrites land. The citations this review relies on from Volume 2 onward were checked against the counters at `0419e16`.

The five repairs in step 1 are also the five most serious defects in the series as it stands. In order: the three-squares test, which concludes that 28 is a sum of three rational squares; the wrong modulation in the proof of Wiener’s lemma; the factor \(\frac12\) dropped from the polar terms of Riemann’s functional equation; the opening of Volume 5, which names liminf and limsup backwards and then, in the sieve chapter, ties a short-interval constant to Siegel zeros; and the completeness sentences — Volume 7’s blurb, Volume 10’s single exception, Volume 12’s preface — together with P2, P3, and Volume 15’s empty Appendix E, which present unfinished or quoted material as a finished book.
