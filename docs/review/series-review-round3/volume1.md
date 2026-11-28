# Volume 1 — First Principles

**Score: 8/10.**

The book does the job the preface announces. A reader with secondary-school algebra can follow induction from well-ordering, unique factorisation, inclusion–exclusion, the five theorems on a closed interval, the least positive zero of cosine, the spectral theorem, Stirling’s constant, and Chebyshev’s weak law. The fourteen local gaps from round 2 are now written out. What remains is the same kind of gap in other sentences: a supremum taken without naming the extreme-value theorem, a sign of the mean-value clause left implicit, a name used before its definition. No main theorem checked here was false.

**Counts.** 0 critical, 0 major, 19 minor. Nineteen issues, `V1-R3-001` through `V1-R3-019`.

**Round-2 follow-up.** 14 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume1-first-principles/main.tex`: preface and jacket; Chapter 0 Language; 1 Sums; 2 Counting; 3 Sequences; 4 Orders; 5 Complex numbers; 6 Polynomials; 7 Linear algebra; 8 Calculus; 9 Inequalities; 10 Probability; field guide, image credits, index. Every chapter file was read, including exercises, hints, and solutions. Every round-2 issue and every new row below was re-opened at the cited line on main at `68261d60`. The constants under “Recomputed here” were recomputed in Python, separately from the proofs. A search of this volume’s `.tex` and `.md` files found none of the banned fillers, and no notebook. No full LaTeX build of Volume 1 was run for this note. The uniform-continuity figure was read as source.

**Style, once.** The prose is a person teaching. The blurb’s cube sum, the five-agreement workshop, and the medical-test counts match the chapters. Reader-facing copy does not call the book a revision.

## Issues

Paths are relative to `volume1-first-principles/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V1-R3-001 | `chapters/ch01-sums.tex:231` | math | minor | “So \(n=ab\) with integers \(a,b\) satisfying \(1<a<n\) and \(1<b<n\).” | Not being prime means a positive divisor other than \(1\) and \(n\). A positive divisor of \(n\ge 2\) lies between \(1\) and \(n\), so both factors then lie in \(\{2,\ldots,n-1\}\). Unique factorisation cites this paragraph for existence. |
| V1-R3-002 | `chapters/ch01-sums.tex:560` | math | minor | “The product \(k(k-1)\) is even, so \(k^2-k=2m\).” | Chapter 0 has split the integers into even and odd. If \(k\) is even the product is even; if \(k\) is odd then \(k-1\) is even. The later terms of the block are then odd, as the text says. |
| V1-R3-003 | `chapters/ch01-sums.tex:693`; also `:1070` | math | minor | “Alternatively, among three consecutive integers \(n\), \(n+1\) and \(n+2\), one is divisible by \(3\).” | The binomial coefficient already shows the sum is an integer. The alternative is the division algorithm: the remainder of \(n\) on division by \(3\) is \(0\), \(1\), or \(2\). The same sentence is missing at line 1070, where the binomial identity \(\binom{X+1}{3}=(X^3-X)/6\) is already a complete proof that the polynomial is integer-valued. |
| V1-R3-004 | `chapters/ch02-counting.tex:596` (`ex:phi`) | math | minor | “Thus \(\lvert A_I\rvert=n/\prod_{i\in I}p_i\).” | The valuation test just written shows that the product \(P_I\) divides \(x\). It does not show that \(P_I\) divides \(n\), which is what makes the count of multiples exact. Each exponent in the factorisation of \(n\) is at least \(1\), so the same test applies to \(n\). The product formula for \(\varphi(n)\) was checked for \(n<200\). |
| V1-R3-005 | `chapters/ch02-counting.tex:677` (`ex:catalan`) | math | minor | “Between these two steps lies a good path translated to start at \((1,0)\) and end at \((k+1,k)\), which stays strictly below the diagonal, i.e. a good path of length \(k\).” | Parts (a) and (b) were read and hold, and \(C_4=14\) matches. The return step is asserted to be north, and the shift \((x,y)\mapsto(x-1,y)\) is not written. |
| V1-R3-006 | `chapters/ch01-sums.tex:937` (`ex:fibgcd`) | math | minor | “Any common divisor of \(F_{n-1}F_{m-n}\) and \(F_n\) is therefore coprime to \(F_{n-1}\).” | Part (b) gives \(\gcd(F_{n-1},F_n)=1\). A common divisor of the product and of \(F_n\) divides \(F_n\), and that is why it is coprime to \(F_{n-1}\). The identity was checked for \(0\le m,n\le 14\). |
| V1-R3-007 | `chapters/ch03-polynomials.tex:183` (`thm:dalembert`) | math | minor | “with \(M=\sup_{0\le t\le 1}\lvert u^{k+1}S(tu)\rvert\). Choose \(0<t<1\) with \(Mt<\lvert P(z_0)\rvert\).” | The strict decrease needs a finite \(M\). On the segment, \(t\mapsto\lvert u^{k+1}S(tu)\rvert\) is continuous, so the extreme-value theorem bounds it. The rest of the minimum argument was read and holds. |
| V1-R3-008 | `chapters/ch02-complex-roots.tex:247` | math | minor | “On \([0,\pi]\) we already know \(\sin\ge 0\), so \(\cos'=-\sin\le 0\) and cosine is non-increasing there.” | The mean-value clause that was proved turns a nonnegative derivative into a non-decreasing function. Apply it to \(-\cos\). Two lines later the strict decrease on \([0,\pi]\) is computed directly, and that computation is complete. The non-increasing sentence is used before it, to rule out \(\cos=+1\). |
| V1-R3-009 | `chapters/ch05-sequences-series.tex:611` | math | minor | “a positive value would stay positive on a neighbourhood, and a negative value would force an earlier zero” | The negative alternative is a complete contradiction. The positive one does not say that a neighbourhood with no zero makes \(\alpha+\delta\) a greater lower bound. |
| V1-R3-010 | `chapters/ch05-sequences-series.tex:736` | math | minor | “If \(\alpha>0\), apply the integral test to \(t^{-\alpha}\).” | The test needs a non-increasing integrand. For \(\alpha>0\) the derivative \(-\alpha t^{-\alpha-1}\) is negative. That sentence is not written. |
| V1-R3-011 | `chapters/ch03-polynomials.tex:470` | prerequisite | minor | “Choose each of two integers independently, with equal chances for the values \(1,\ldots,N\).” | Polynomials come before probability. The secret-sharing example now stops at the bijection. This beauty note still finishes in the language of chance. The proportion of coprime pairs is a count. |
| V1-R3-012 | `figures/ch05-bisection.tex:23`; input at `chapters/ch05-sequences-series.tex:474` | prerequisite | minor | The axis tick is \(\sqrt{3}\). | A general positive root is constructed in the example that begins at line 483, after this figure environment. The Rolle sentence at line 549 names \([0,\sqrt{3}]\) after that example. No LaTeX build was run, so this is the source order, not a claim about where the float sits on the page. |
| V1-R3-013 | `chapters/ch05-sequences-series.tex:1343` (`ex:nested`) | exercise | minor | “\(u_{n+1}=\sqrt{2+2\cos\frac{\pi}{2^{n+1}}}=\sqrt{4\cos^2\frac{\pi}{2^{n+2}}}\).” | The half-angle line \(2+2\cos x=4\cos^2(x/2)\) is the addition formula, already standing, and it is not written. The cosine is correctly taken positive. |
| V1-R3-014 | `chapters/ch05-sequences-series.tex:1384` (`ex:condensation`) | exercise | minor | “which is eventually non-increasing for every fixed real \(\beta\)” | Condensation needs a monotone sequence. For \(\beta\le 0\) the logarithm in the denominator does not increase, and the claim is still true for large \(n\). The derivative of the logarithm of the denominator is positive for large \(x\). |
| V1-R3-015 | `chapters/ch07-linear-algebra.tex:905` | prerequisite | minor | “the second factor is the Lucas number \(L_n\).” | The identity \(F_{2n}=F_n(F_{n+1}+F_{n-1})\) is proved. The name \(L_n\) is defined in the field guide at line 189, which comes later. |
| V1-R3-016 | `chapters/ch07-linear-algebra.tex:550` | prerequisite | minor | “its interesting eigenvector is still a probability.” | Probability is Chapter 10. The covariance sentence at line 435 is marked as a preview. This one is not. The exercise defines a nonnegative column summing to \(1\), and the proof uses only that. |
| V1-R3-017 | `chapters/ch06-integrals-taylor.tex:876` | math | minor | “Taylor’s theorem gives \(e^t\ge t^2/2\) for \(t>0\).” | The inequality is true. The integral remainder, or the series with positive terms already proved, is the reason. The absolute form of the order-2 bound does not by itself give it for every \(t>0\). |
| V1-R3-018 | `chapters/ch06-integrals-taylor.tex:863` | math | minor | “as \(A\to\infty\), \(A^ne^{-A}\to 0\), so \(I_n=nI_{n-1}\).” | The limit is true. The Gamma argument and `ex:xnex` write how a power loses to the exponential. This factorial step does not point at either. |
| V1-R3-019 | `chapters/ch06-integrals-taylor.tex:909` | math | minor | “It follows from the integral above by the substitution \(x=u/\sqrt{2}\).” | The product of the odd numbers equals \((2n)!/(2^n n!)\), and that is the even moment of the standard normal density. The three constant factors in the substitution are not written. |

## Round-2 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V1-R2-001 | resolved | `ch03-polynomials.tex:257` “That count is what the two shares determine. Chapter 10 is where a count of this kind becomes a probability, and this example does not take that step.” No “equally likely”, “chance”, or “distribution”. |
| V1-R2-002 | resolved | `ch01-sums.tex:396` The binomial theorem expands \((X+1)^d\), the coefficient of \(X^{d-1}\) is \(ad\neq 0\), and \(\deg\Delta P=d-1\). |
| V1-R2-003 | resolved | `ch02-counting.tex:622` “If two domain elements shared an image, the image would have at most \(n-1\) elements.” |
| V1-R2-004 | resolved | `ch02-counting.tex:626–632` The inductive step for the forward difference is expanded, reindexed, and closed with Pascal’s rule. |
| V1-R2-005 | resolved | `ch02-counting.tex:596` The valuation test is cited for distinct primes and their product. The exact count of multiples is `V1-R3-004`, not a return of the missing test. |
| V1-R2-006 | resolved | `ch01-sums.tex:970` The sequences chapter bounds the partial sums, and `ex:eulerbasel` writes the fast series without identifying it with \(\pi^2/6\). The word “only” is gone. |
| V1-R2-007 | resolved | `ch05-sequences-series.tex:313` “The value \(\sin 1.5\) is about \(0.99749\), which is less than \(1.5\).” Recomputed: \(\sin 1.5=0.99749498\ldots\). |
| V1-R2-008 | resolved | `figures/ch05-uniform.tex:11` The label \(\frac12\) is at \(x=0.50\), on the marked point. |
| V1-R2-009 | resolved | `ch05-sequences-series.tex:1391–1396` \(\sin(2n+1)-\sin(2n-1)=2\cos(2n)\sin 1\), and the partial sums telescope. |
| V1-R2-010 | resolved | `ch05-sequences-series.tex:611` A negative value on \((0,\alpha)\) would put a zero strictly below \(\alpha\). The positive alternative at \(\alpha\) itself is `V1-R3-009`. |
| V1-R2-011 | resolved | `ch02-complex-roots.tex:247` The mean-value theorem gives \(\sin y-\sin x=\cos c\cdot(y-x)\) with the cosine factor positive. |
| V1-R2-012 | resolved | `ch07-linear-algebra.tex:786` Cayley–Hamilton gives \(\chi_M(M)=0\), the roots differ by \(\sqrt5\), and `thm:diag` applies. |
| V1-R2-013 | resolved | `ch06-integrals-taylor.tex:759–763` The substitution \(x=1/\varepsilon\) reduces the limit to \((\ln x)/x\to 0\), with the extra factor \(x^{-n}\) when \(n\ge 1\). |
| V1-R2-014 | resolved | `field-guide.tex:264–267` The three remainders on division by \(3\) are written, and Euclid’s lemma is applied to \(3\mid 8t\). |

## Recomputed here

These values were recomputed in Python for this review. Each matches the text.

- \(1^3+\cdots+10^3=3025=55^2\). For \(2\le n\le 39\), if \(2^s\le n<2^{s+1}\), then \(v_2(\operatorname{lcm}(1,\ldots,n))=s\).
- \(\cos(8/5)=-0.02919\ldots\le -13/1875=-0.006933\ldots\). \(\sin 1.5=0.99749498\ldots\).
- At \(n=10\), \(10!/(\sqrt{10}\,(10/e)^{10})=2.527597\) and \(\sqrt{2\pi}\,(1+1/120)=2.527517\).
- Birthday: the probability that \(23\) dates are distinct is \(0.492703\), so a shared birthday has probability \(0.507297\).
- Medical test: \(P(+)=0.0594\) and \(0.0099/0.0594=1/6\).
- \(\varphi^{10}=122.991869\ldots\), and \(\varphi^{10}+\psi^{10}=123\).
- Derangement counts through \(n=7\): \(1,0,1,2,9,44,265,1854\).
- Twenty terms of Euler’s fast series for \(\zeta(2)\) total \(1.644934\). The comparison tail \(1/(21^2\cdot 2^{20})\) equals \(2.16\times 10^{-9}\).
- The orbit of \(27\) under the cover rule takes \(111\) steps and peaks at \(9232\). Every integer from \(2\) to \(8000\) reaches \(1\).
- Divisibility of \(n^2-1\) by \(24\) holds exactly for odd \(n\) not divisible by \(3\), on \(-30\le n\le 40\).
- \(|\mathrm{GL}_2(\mathbb F_p)|\) matches a direct count for \(p=2,3,5\): \(6\), \(48\), \(480\).

## Verified correct

The secret-sharing example now ends on the bijection of coefficient pairs. The forward-difference degree drop names the binomial expansion. The surjection onto a set of the same size is a bijection because a collision shrinks the image. The cosine zero on \((0,\alpha)\) contradicts the infimum, and the strict increase of sine is a mean-value difference with a positive cosine. Binet’s diagonalisation cites Cayley–Hamilton. The improper logarithm limit is \((\ln x)/x\) after \(x=1/\varepsilon\). The field-guide divisibility by \(24\) writes the remainders and Euclid’s lemma. The blurb’s \(3025\), \(31\) against \(32\), and the counts \(99\) and \(495\) match.

## Not checked

- A LaTeX build, so printed page numbers, overfull boxes, and the printed position of the bisection float were not seen.
- EPUB rendering and the Kindle alt text.
- Portrait files and licence lines. `photos/CREDITS.md` was not re-hashed.
- Primary pages of the memoirs named in the source lists.
