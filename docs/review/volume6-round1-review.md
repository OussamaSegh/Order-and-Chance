# Volume 6, round 1 (review only)

Score: **8/10**.

Base: `1ccf4e181833cf50bb569e31f0e986124ed579b0` on `main`. Sources: `volume6-crossroads/` (twelve chapters, preface, exercises with hints and solutions). Intent: `docs/plan/book-06.md`. No book source was edited.

The numbered theorems of the volume hold up. The score stops at 8 because five statements a reader would trust are false: four Volume 1 citations in the closing solutions point at a different theorem, and one solution names the wrong factor of \(\xi\) at the trivial zeros. Six further slips are local. Nothing found breaks a main theorem.

## What was checked

Read against the source, not against an earlier review: the preface; the proofs of Abel summation, Chebyshev's bounds, and Mertens's three theorems; Dirichlet's \(L(1,\chi)\) formulae and the check \(L(1,\chi_{-4})=\pi/4\); the zero-free argument, including the arithmetic that produces \(1/(14A'\log|t|)\); the residues in the explicit formula and the claim that the horizontal error is absorbed for \(x\ge 2\); Selberg's weight at \(d=2\) for level \(y=10\), which is \(-21/22\); Brun's passage from \(16x/\log^2 y\) to \(O(x/\log^2 x)\); the Erdős–Kac truncation \(z=x^{1/\beta}\); the coefficient comparison for \(E_4^2=E_8\) and the congruences \(65520\equiv -125\), \(432000\equiv 125\pmod{691}\).

A script walked every `Volume N, Theorem/Proposition/Lemma/Corollary/Definition/Exercise a.b` citation in Volume 6 (163 distinct targets) against the numbered environments in the current volumes, in `main.tex` order, with lemmas and propositions on the shared counter. Internal `\ref` targets: none missing, no duplicate labels. Exercises: 188, each with one hint and one solution.

Recomputed, and in agreement with the text: \(\prod_{p\le 1000}(1-1/p)=0.0810\) against \(e^{-\gamma}/\log 1000=0.0813\); the product at \(100\) is \(0.1203\) against \(0.1219\); \(R(10^3)=-1.298\), \(R(10^5)=-1.329\), \(R(10^7)=-1.3324\); \(\sigma_7(2)=129=9+120\).

Citations that were opened and match: Volume 2, Theorems 2.2 (Euler's reciprocal sum), 2.4 (the product bound and the lower bound for \(\pi\)), 2.5 (Bertrand), and 7.5 (the circle problem, which does give \(N(R)\sim\pi R^2\)). Volume 4, Proposition 6.7 states that a standard normal has transform \(e^{-t^2/2}\). Volume 5, Exercise 5.7 is \(\Gamma'(1)=-\gamma\), and Exercise 6.5 is Benford's law for the powers of 2. Volume 13, Chapter 12 is Tate's thesis, which contains the functional equation of \(L(s,\chi)\) that Chapter 7 admits. Volume 13, Chapter 11 contains the analytic class-number formula named in the remark of Chapter 3. Dirichlet's finite formula is Volume 6, Theorem 3.10, which is the number Volume 13 cites. The preface is right that Volume 6 is the last volume of Part II.

The plan's later heading "Part IV" is the plan's own outline. The parts table in that same note, and `main.tex`, put Chapters 11 and 12 in Part III. The book already says the closing problems are a separate list. That placement was not scored as a defect.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled, and no GitHub Actions run was inspected. A parser of `\label` and `\ref` is not a substitute for a TeX run: it does not see multiply defined counters inside conditionals, and it does not see overfull boxes.

TikZ geometry was not redrawn. Only the numerical claims that were recomputed above were checked against captions.

Not every line of every solution was recalculated. The closing problems (Singer through Romanoff) were sampled through their citations and through the arithmetic that the issue list names. Historical page numbers were not checked. Proofs that the text marks as quoted or admitted (class-number formula, Bombieri–Vinogradov, the functional equation of \(L(s,\chi)\) inside one remark, Tonelli in one Chapter 12 solution) were not re-proved.

## Issues

V6-R1-001 | major | volume6-crossroads/chapters/ch12-modular.tex:1499 | The tools line cites Volume 1, Theorem 9.4 as Cauchy–Schwarz. In the current Volume 1 that item is the Wallis product, and it is a proposition. Cauchy–Schwarz is Theorem 10.4. | Cite Volume 1, Theorem 10.4. Do not renumber Volume 1.

V6-R1-002 | major | volume6-crossroads/chapters/ch12-modular.tex:1691 | The tools line cites Volume 1, Theorem 9.3 as AM–GM. Theorem 9.3 is l'Hôpital's rule. AM–GM is Theorem 10.3. | Cite Volume 1, Theorem 10.3.

V6-R1-003 | major | volume6-crossroads/chapters/ch12-modular.tex:2233 | The write-up says a continuous function on a closed interval attains its maximum by Volume 1, Theorem 3.8. Chapter 3 of Volume 1 has four numbered results (counts, inclusion–exclusion, derangements, paths). The extreme-value theorem is Theorem 4.8. The tools line at 2246 repeats 3.8. | Cite Volume 1, Theorem 4.8 in both places.

V6-R1-004 | major | volume6-crossroads/chapters/ch12-modular.tex:2410 | The tools line cites Volume 1, Proposition 7.4 for Vandermonde determinants. Item 7.4 is the d'Alembert–Gauss theorem. The Vandermonde determinant is Proposition 8.4. | Cite Volume 1, Proposition 8.4.

V6-R1-005 | major | volume6-crossroads/chapters/ch06-zeros.tex:759 | The solution of `ex:xi2` says that at the trivial zeros the pole of \(\Gamma(s/2)\) cancels a zero of the polynomial factor. That factor is \(\frac12 s(s-1)\), which is zero only at \(0\) and \(1\). The pole cancels a zero of \(\zeta\), and \(\xi\) stays non-zero because the polynomial factor does not vanish. The value \(\xi(2)=\pi/6\) in the same solution is right. | Name \(\zeta\), not the polynomial factor, as the function whose zero is cancelled.

V6-R1-006 | minor | volume6-crossroads/chapters/ch06-zeros.tex:183 | After the zeros of \(f\) are removed, the proof says \(g\) has no zeros on the closed disc, "hence none on a slightly smaller open disc \(D'\supset\{|z|\le R\}\)". A disc that contains the closed disc of radius \(R\) is larger, and the step from "no zeros on a compact set" to "no zeros on a neighborhood" uses that zeros are isolated. | Call \(D'\) slightly larger, and name isolation.

V6-R1-007 | minor | volume6-crossroads/chapters/ch06-zeros.tex:401 | "The integral is real, so \(2\pi N(T)=\operatorname{Im}\int\xi'/\xi\)." The argument principle gives \(\int\xi'/\xi=2\pi i\,N(T)\), which is purely imaginary. The identity used afterwards, \(\pi N(T)=\operatorname{Im}\int_L\xi'/\xi\), matches the theorem. | Say the count is real, so the integral is purely imaginary and its imaginary part is \(2\pi N(T)\).

V6-R1-008 | minor | volume6-crossroads/chapters/ch05-pnt.tex:588 | The solution assumes \(\pi(x)=\operatorname{Li}(x)+o(x/\log^2 x)\) and concludes \(\pi(x)\log x/x=1+1/\log x+O(1/\log^2 x)\). Multiplying the little-o error by \(\log x/x\) leaves \(o(1/\log x)\), which need not be \(O(1/\log^2 x)\). The expansion of \(\operatorname{Li}\) does give that stronger remainder once the error is \(O(x/\log^3 x)\), and Chapter 7 has a stronger error, but the displayed implication does not. | Write \(o(1/\log x)\) under the stated hypothesis, or invoke the Chapter 7 error before the big-O display.

V6-R1-009 | minor | volume6-crossroads/chapters/ch05-pnt.tex:196 | The caption says the shaded block has area independent of \(x\). Between the horizontal line \(\lambda cx\) and the line \(ct\) on \([x,\lambda x]\), the Euclidean area is \(\frac12 c(\lambda-1)^2 x^2\). The quantity that does not depend on \(x\) is \(\int_x^{\lambda x}(\lambda cx-ct)/t^2\,\mathrm dt\), which the lemma computes. | Change the caption wording so that the scale-free object is the integral. Leave the picture's typography alone.

V6-R1-010 | minor | volume6-crossroads/chapters/ch08-sieves.tex:655 | "As \(u\to 1\), the prediction \(e^{-\gamma}\) is smaller than \(\omega(u)=1/u\) by a factor that tends to infinity." On \((1,2]\), \(\omega(u)=1/u\to 1\), so the ratio tends to \(e^{\gamma}\approx 1.781\). The values \(\omega(2)=1/2\) and \(\omega(3)=(1+\log 2)/3\) in the same solution are right, and the integral evaluation \(\int_{1/u}^{1/2}\mathrm dt/(t(1-t))=\log(u-1)\) is right. | Say the ratio tends to \(e^{\gamma}\).

V6-R1-011 | minor | volume6-crossroads/chapters/ch10-random.tex:599 | For a gap divisible by 3 the two primes lie in the same class, so avoiding \(0\bmod 3\) costs \(2/3\). The sentence says independence of the two classes would cost \(1/3\). Independence costs \((2/3)^2=4/9\). The probability \(1/3\) is what distinct classes cost, and \((2/3)/(1/3)=2\) is the doubled weight the next sentence uses. | Say that distinct classes modulo 3 would cost \(1/3\).

## Counts

0 critical, 5 major, 6 minor.
