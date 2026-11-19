# Volume 5 — Calculation

**Score: not yet assigned.** Chapters 2 and 4–13, the blurb, `kdp.md`, the index beyond the lines named below, the sources, and About the Cover are still being read. The score, the severity counts, and the ledger section will be filled when that reading is finished. Chapters 1 and 3 were read line by line, including every exercise, hint, and solution.

**Counts so far.** 0 critical, 0 major, 4 minor. Issues `V5-001` through `V5-004`. No prerequisite issue in Chapters 1 or 3.

**How this was read.** Book order in `volume5-calculation/main.tex`. Chapter 1 is `chapters/ch01-finite.tex`. The shared counter (theorem, proposition, lemma, corollary, definition, example; starred environments do not count) was counted in source order. Those numbers match the index lines for the fundamental theorem (1.2), falling powers (1.4), summation by parts (1.5), Abel summation (1.7), Dirichlet’s test (1.8), the sine sum (1.9), the Stirling recurrences (1.11), the change of basis (1.12), Bernoulli numbers (1.14), Faulhaber (1.15), and Newton (1.16).

## Issues

Paths are relative to `volume5-calculation/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V5-001 | `chapters/ch01-finite.tex:181` (after `prop:sinsum`) | math | minor | “The convergence is not absolute. The terms \(\frac{\lvert\sin kx\rvert}{k}\) do not form a convergent series.” | The proposition has just shown that \(\sum\sin(kx)/k\) converges for every real \(x\). At \(x\in\pi\Z\) every term is \(0\), so the convergence is absolute. Elsewhere the terms do not form a convergent series, but the page does not prove it: the cosine sums are bounded by the same method as the sine sums, and \(\sum\sin^2(kx)/k\) then diverges with the harmonic series. Name the exception, and write that comparison. The closed form \((\pi-x)/2\) on \((0,2\pi)\) is proved later, in Example `ex:sawtooth`. |
| V5-002 | `chapters/ch01-finite.tex:345` (remark after Faulhaber) | math | minor | “Since \(\zeta(2k)\to 1\), one has \(\lvert B_{2k}\rvert\sim\frac{2(2k)!}{(2\pi)^{2k}}\), which outgrows every exponential. The series \(\frac{t}{e^t-1}\) therefore has radius \(2\pi\).” | The asymptotic is the right one, and the radius of that exponential series is \(2\pi\). Outgrowing every exponential is not the step that produces the radius: \(n!\) outgrows every exponential, and \(\sum t^n/n!\) has infinite radius. The general term is \(B_{2k}t^{2k}/(2k)!\sim 2(t/(2\pi))^{2k}\). Chapter 3, lines 203–214, writes the same growth with the factor \(\zeta(2k)\) kept, and the remark there points the radius at the poles. |
| V5-003 | `chapters/ch03-series.tex:87` (`thm:sineproduct`) | math | minor | “Proposition~\ref{prop:products} says the product \(P(x)=\pi x\prod_{n\ge1}\bigl(1-\frac{x^2}{n^2}\bigr)\) converges for every \(x\).” | The proposition needs \(a_n>-1\). For \(\lvert x\rvert>1\) the early factors \(1-x^2/n^2\) are \(\le -1\), so the logarithm in the proof does not apply to them. On \((-1,1)\) every factor is positive and the proposition does apply, and the relation \(P_N(x+1)=P_N(x)(x+N+1)/(x-N)\) then extends the limit. Say that the proposition is used for the tail \(n>\lvert x\rvert\), or only on \((-1,1)\), before the extension. |
| V5-004 | `chapters/ch03-series.tex:310` (`ex:rw03c`); the write-up is line 451 | exercise | minor | The exercise asks for \(0<\pi^2/6-5/4<1/2\). The solution concludes \(\le 1/2\). | For \(n\ge 3\) and \(x\in[n-1,n)\), \(x^{-2}>n^{-2}\), so each integral comparison is strict and the tail is strictly less than \(1/2\). The decimal \(0.3949\ldots\) also lies under \(1/2\), but the sentence that the exercise asked for is the strict one. |

## Verified correct

### Chapter 1

The difference operator, the half-open sum, and the fundamental theorem. Falling powers, including the negative case \(\Delta x^{\underline{-r}}=-r\,x^{\underline{-r-1}}\), the hockey-stick identity, and \(\sum_{k=0}^{n-1}1/((k+1)(k+2))=1-1/(n+1)\). The product rule and summation by parts. Abel summation and Dirichlet’s test, including the bound \(Mb_1\). The sine sum, checked algebraically from the cosine difference and numerically at three pairs \((n,x)\). Stirling numbers of both kinds: the counts \(\stirlingii42=7\) and \(\stirlingi42=11\), the recurrences, and both displayed triangles through \(n=6\). The row sums of the first-kind triangle at \(n=6\) are \(720=6!\), and the second-kind row sums to the Bell number \(203\). The change-of-basis theorem, including the map count and the induction for rising powers. Power sums through the falling basis: \(\sum_{k<n}k^2=(n-1)n(2n-1)/6\) and the cube identity used in the text.

Bernoulli numbers from \(t/(e^t-1)\), with \(B_1=-1/2\). The recurrence produces \(B_2=1/6\), \(B_4=-1/30\), \(B_6=1/42\), \(B_8=-1/30\), \(B_{10}=5/66\), \(B_{12}=-691/2730\), and \(B_n=0\) for odd \(n\ge 3\). The evenness argument in the formal series was read and holds. Faulhaber’s formula. For \(p=5\),
\[
\sum_{k<n}k^5=\frac{n^6}6-\frac{n^5}2+\frac{5n^4}{12}-\frac{n^2}{12},
\]
and the value at \(n=1000\) is \(166\,167\,083\,333\,250\,000\). The identity with \(T=n(n-1)/2\) was expanded and equals \(T^2(4T-1)/3\); at \(n=4\) both sides are \(276\). The sum of the first thousand tenth powers, evaluated at \(n=1001\), is \(91\,409\,924\,241\,424\,243\,424\,241\,924\,242\,500\), which is the number in the opening paragraph. Newton’s formula, the explicit Stirling number of the second kind, and the difference table of \(x^3+x+1\): the left edge \(1,2,6,6\) rebuilds the polynomial, and the forward diagonal \(6\), \(18+6=24\), \(38+24=62\), \(69+62=131\) is \(f(5)\).

All eleven exercises were read with their hints and solutions. In particular \(\sum_{k=0}^n k^22^k=(n^2-2n+3)2^{n+1}-6\), checked at \(n=2\); the partial-fraction sum \(1/4\); \(\sum_{k<n}kH_k=n(n-1)(H_n-1/2)/2\), checked at \(n=3\); the surjection count and the two inclusion–exclusion corollaries; the engine polynomial; the power sum modulo a prime, using a primitive root, which is Volume 2, Chapter 5, for every prime; von Staudt–Clausen, including both numerical checks \(B_2+1/2+1/3=1\) and \(B_{12}+1/2+1/3+1/5+1/7+1/13=1\), and the \(p=2\) sign; \(\sum_{k<n}k^{\underline 3}=n^{\underline 4}/4\); the cube sum; \(B_4=-1/30\) and \(\sum_{k<3}k^4=17\); and \(\sum_{k<n}kc^k=((n-1)c^{n+1}-nc^n+c)/(c-1)^2\), checked at \(c=3\), \(n=3\).

Inclusion–exclusion is Volume 1, Chapter 2, Theorem `thm:incexc`. Two polynomials that agree at infinitely many points are equal by Volume 1, Chapter 6: the language chapter is numbered 0, and `prop:rootsfactor` is the polynomials chapter. The alternating series test is Volume 1, Proposition `prop:signedseries`, in the sequences chapter. The expected number of cycles is Volume 4, Chapter 2: \(\mathbb E[C_n]=H_n\), and \(\frac1{n!}\sum_k k\stirlingi nk\) is that expectation once the Stirling number has been defined. Fermat’s little theorem, used in the solution of `ex:powersmodp`, is Volume 2, Theorem 3.3. \(K[X]\) is not needed in this chapter.

The four plates match their captions. The staircase bars are \(k^2\) on \([k,k+1)\) for \(k<8\), summing to \(140\), against \(\int_0^8 x^2\,dx=512/3\), labelled \(170.7\). The falling-power bars differ by exactly \(k\). The square table has left edge \(0,1,2\) and constant second difference \(2\). The cubic table matches the numbers in the caption. `figures/ch01-rudin.tex` is not an input of this chapter.

The bridge names the generating function, which is the next chapter. No notebook is mentioned. The prose does not call the book a revision. The banned openers and intensifiers do not appear.

### Chapter 3

Infinite products under \(\sum\lvert a_n\rvert<\infty\), apart from the citation in V5-003. The telescoping product equals \(1/2\), and the partial product at \(N=4\) is \(5/8\). Herglotz’s proof of the cotangent expansion: oddness, period 1, the duplication identity for both functions, the Taylor expansion \(\pi\cot\pi x-1/x\to 0\), and the maximum principle from the averaging relation. The sine product on \((-1,1)\) by integrating the cotangent, and the extension \(P(x+1)=-P(x)\). Wallis’s product at \(x=1/2\), and Viète’s product from the double-angle formula. The areas of the inscribed \(4\)-, \(8\)- and \(16\)-gons in the unit circle are \(2\), \(2\sqrt2\), and \(4\sqrt{2-\sqrt2}\approx 3.061\). The plates use a circle of radius \(1.1\) as a scale drawing; the printed areas are the unit-circle areas.

Euler’s formula for \(\zeta(2k)\). The coefficient comparison gives
\[
\zeta(2k)=\frac{(-1)^{k+1}B_{2k}(2\pi)^{2k}}{2(2k)!},
\]
and the four values are \(\pi^2/6\), \(\pi^4/90\), \(\pi^6/945\), \(\pi^8/9450\). The bound \(0<\zeta(2k)-1\le 3\cdot 4^{-k}\) was checked. Niven’s proof that \(\pi^2\) is irrational, including \(F''+\pi^2 F=\pi^2 a^n f\) and the integral equal to the integer \(F(0)+F(1)\).

The Basel count in the opening is the one Chapter 9 later calls the sixth proof: Volume 1, Exercise 6.7, is `ex:basel` in the polynomials chapter and does prove \(\sum 1/k^2=\pi^2/6\); this chapter’s coefficient theorem is one proof and Exercise `ex:ritelli` is the other; Chapter 6, Exercise `ex:x2`, gives two more; Corollary `cor:baselres` is the sixth. Ritelli admits Tonelli, and it says so. Volume 7’s index lists Tonelli as Theorem 9.5, label `thm:tonelli`. The sentence on \(\zeta(5)\) matches the Archive of Formal Proofs entry of 26 October 2026: the only oracle named there is `holds`, from 72 numeric inequalities. The book says the argument is not a theorem of this volume.

All eleven exercises were read with their hints and solutions. Leibniz’s series and the bound \(1/(2n+1)\). The cotangent sum at \(a=1/2\) equals \(2\), by the closed form and by the telescope. \(\zeta(6)\) and \(\zeta(8)\) again, \(\sum(2n+1)^{-4}=\pi^4/96\), and the alternating Basel sum \(\pi^2/12\). Ritelli’s integral equals \(\pi^2/2\), the folded integral equals \(\pi^2/8\), and the odd subsum gives \(\zeta(2)\). The irrationality of \(e\), and the proof that \(e\) is not quadratic. The continued fraction of a reduced quadratic irrational is purely periodic, using Volume 2, Theorem `thm:periodic`, which is in the continued-fraction chapter, numbered 9. The example \(\sqrt{14}=[3;\overline{1,2,1,6}]\) matches the algorithm. The coprime sum equals \(5/2\), and \(c_n=2^{\omega(n)}\). The three short exercises on the product, the odd and even Basel sums, and Viète’s first two factors. The strict tail bound is V5-004. The partial products were recomputed: eight sine factors at \(x=1/2\) give \(1.0298\ldots\), two Viète factors give \(0.653\), and four give \(0.638\). The Basel partial sum through \(N=12\) is about \(0.080\) under \(\pi^2/6\), and the plotted ordinates match that scale. The index numbers 3.2 and 3.4 through 3.8 match the counter.

The bridge names integrals, which are the next chapter.

## Not checked

- Chapter 2, and Chapters 4 through 13, including `chapters/bbp-borwein.tex` (input from Chapter 4), every later exercise, the preface’s full list of admitted external theorems, the blurb, `kdp.md`, the index beyond the Chapter 1 and Chapter 3 lines named above, the sources list, and About the Cover.
- A LaTeX build, so printed page numbers were not seen.
- The 1687 portrait attribution, beyond the agreement of the caption with `photos/CREDITS.md`.
- Whether Chapter 6’s proof of the sawtooth identity is complete. The statement that Chapter 1 points to is in Example `ex:sawtooth`.
