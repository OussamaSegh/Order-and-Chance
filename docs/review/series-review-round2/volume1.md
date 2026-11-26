# Volume 1 — First Principles

**Score: 8/10.**

The book does the job the preface announces. A reader with secondary-school algebra can follow induction from well-ordering, unique factorisation with the exponent test for the gcd and the lcm, inclusion–exclusion, the five theorems on a closed interval, a proof that \(\pi/2\) is the least positive zero of cosine, the spectral theorem for a real symmetric matrix, Stirling’s constant from the Wallis integrals, and Chebyshev’s weak law. The prose is a person teaching: short sentences, a number next to the claim, and none of the banned filler. Round 1’s thirteen unfinished justifications are now arguments. The score stays at 8 because a dozen local steps are still one sentence short, and the secret-sharing example still finishes in the language of chance before probability is defined. No main theorem was found false.

**Counts.** 0 critical, 0 major, 14 minor. Fourteen issues, `V1-R2-001` through `V1-R2-014`.

**Round-1 follow-up.** 90 resolved, 1 partial, 0 open, 0 regressed. The partial item is `V1-010`.

**How this was read.** Book order in `volume1-first-principles/main.tex`: preface and jacket; Chapter 0 Language; 1 Sums; 2 Counting; 3 Sequences; 4 Orders; 5 Complex numbers; 6 Polynomials; 7 Linear algebra; 8 Calculus; 9 Inequalities; 10 Probability; field guide, image credits, index, About the Cover. Every chapter file was read, including exercises, hints, and solutions. Every former major, the partial item, and every new issue below was re-opened in the source. Displayed constants named under “Recomputed here” were recomputed in Python in this review. A scan of `\ref` and `\ocindexpage` against `\label` in this volume found 419 labels, 1066 references, and no missing target. The banned-word pass was a search of the volume’s `.tex` and `.md` files. Historical memoirs, the PDF build, and portrait files were not reopened.

**Style, once.** The banned openers and intensifiers (`delve`, `it is important to note`, `in this section we will`, `in conclusion`, `robust`, `comprehensive`, `seamless`, `leverage`, `tapestry`, `unlock`, `pivotal`, `underscore`, `realm`) do not occur. No notebook is mentioned. Reader-facing copy does not call the book a revision. The recurring habit is a true one-line reason left unwritten. Those instances are the rows below.

## Issues

Paths are relative to `volume1-first-principles/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V1-R2-001 | `chapters/ch03-polynomials.tex:257` (sharing a secret) | prerequisite | minor | “With the equally likely coefficient pairs, it occurs with chance \(1/p^2\) for every fixed \(s\). The two shares therefore have the same distribution for every choice of the secret.” | The bijection of the \(p^2\) pairs is written, and the next sentence defers the general model to Chapter 10. “Equally likely”, “chance”, and “distribution” are still the finished conclusion. Counting postpones those words. End on the bijection, as `ex:secret` already does. This is the remainder of `V1-010`. |
| V1-R2-002 | `chapters/ch01-sums.tex:396` | math | minor | “the leading terms of \(P(X+1)\) and \(P(X)\) agree, so they cancel in the difference. Hence \(\deg\Delta P<d\).” | The binomial theorem, already proved, gives \((X+1)^d=X^d+dX^{d-1}+\cdots\). That line is the reason the degree-\(d\) terms match. Newton’s formula does not need the sentence, but the sentence is offered as the reason. |
| V1-R2-003 | `chapters/ch02-counting.tex:622` (`ex:surj`) | math | minor | “for \(k=n\) a surjection between sets of the same size is a bijection, so the sum is \(n!\).” | `prop:counts` shows that an injection from an \(n\)-set to itself is a bijection, because the product uses every element. The dual used here is the other sentence: a collision would make the image smaller than the codomain. The count \(3^5-3\cdot2^5+3=150\) is right. |
| V1-R2-004 | `chapters/ch02-counting.tex:622` (`ex:surj`) | math | minor | “applying \(\Delta\) once more and using Pascal’s rule gives \(\Delta^n f(x)=\sum_{j=0}^n(-1)^j\binom{n}{j}f(x+n-j)\).” | The displayed formula is the right forward difference. The inductive step is not written. The surjection count does not need it. |
| V1-R2-005 | `chapters/ch02-counting.tex:596` (`ex:phi`) | math | minor | “distinct primes all divide \(x\) iff their product does” | For two or more primes this is the valuation test after unique factorisation, or Euclid’s lemma repeated. Neither is cited. The product formula matches the usual count of \(\varphi(n)\) for \(n<200\). |
| V1-R2-006 | `chapters/ch01-sums.tex:970` (`ex:sumsq`) | reference | minor | “The sequences chapter only shows that the sum stays bounded.” | That chapter also contains `ex:eulerbasel`, which proves \(\zeta(2)=(\ln 2)^2+2\sum_{n\ge1}1/(n^2 2^n)\) and evaluates twenty terms as \(1.644934\). The identification with \(\pi^2/6\) is still the polynomials exercise. The word “only” is false. |
| V1-R2-007 | `chapters/ch05-sequences-series.tex:313` (`fig:cobweb`) | prerequisite | minor | “On \((0,\pi)\) the graph of sine lies below the diagonal, so the first vertical segment runs down.” | The first step is the numerical fact \(\sin 1.5<1.5\), which the same caption records (\(\sin 1.5=0.99749\ldots\)). The comparison \(\sin t\le t\) for \(t\ge 0\) is proved later, at line 599, and the strict inequality on \((0,\pi/2]\) is `prop:sincmp`. The caption’s interval \((0,\pi)\) is wider than that statement. |
| V1-R2-008 | `figures/ch05-uniform.tex:11`; caption `ch05-sequences-series.tex:534` | figure | minor | The node \(\frac12\) is placed at \(x=0.55\), while the marked input and the ochre arrow end at \(x=0.50\). | The caption says the inputs are \(\frac13\) and \(\frac12\), differing by \(\frac16\). The drawn points do that. The axis label \(\frac12\) does not sit under its point. Move the node to \(x=0.50\). |
| V1-R2-009 | `chapters/ch05-sequences-series.tex:1390` (`ex:sinn`) | exercise | minor | “the partial sums of \(\cos 2n\) are bounded (multiply by \(2\sin 1\) and telescope, as for the sines).” | The sine bound is written earlier in the chapter. The product \(2\sin 1\cdot\cos(2n)=\sin(2n+1)-\sin(2n-1)\) is not. The constant is the right one. |
| V1-R2-010 | `chapters/ch05-sequences-series.tex:611` | math | minor | “The same theorem forbids a negative value on \([0,\alpha)\), because cosine is positive at \(0\). Thus \(\cos t>0\) on \([0,\alpha)\).” | A zero on \((0,\alpha)\) would be a smaller positive zero, contradicting the definition of \(\alpha\). That clause is not written. The rest of the least-period argument was read and holds, including the evaluation \(\cos(8/5)\le -13/1875<0\). |
| V1-R2-011 | `chapters/ch02-complex-roots.tex:247` (`prop:expform`) | reference | minor | “The mean value theorem, Theorem~\ref{thm:mvt}, says that sine is strictly increasing on \([0,\pi/2]\).” | Clause (c) of `thm:mvt` says that a nonnegative derivative makes the function non-decreasing. It does not state the strict case. `prop:sincmp` already proves the strict increase. The cosine difference two lines later is written; the sine difference is not. |
| V1-R2-012 | `chapters/ch07-linear-algebra.tex:786` (`ex:fibmat`) | math | minor | “\(\chi_M=X^2-X-1\) has roots \(\varphi\neq\psi\), so \(M\) is diagonalisable (Theorem~\ref{thm:diag}).” | `thm:diag` needs a split square-free polynomial that annihilates \(M\). Distinct roots give that after Cayley–Hamilton, or by the eigenvector paragraph at line 330. The solution names neither. Cayley–Hamilton is already proved. |
| V1-R2-013 | `chapters/ch06-integrals-taylor.tex:759` (`ex:xnlnx`) | math | minor | “As \(\varepsilon\to 0\), \(\varepsilon^{n+1}\ln\varepsilon\to 0\).” | The antiderivative is right, and the limit is true. The chapter has \(\ln x/x\to 0\) as \(x\to\infty\). The translation \(x=1/\varepsilon\), and the extra factor \(\varepsilon^n\) when \(n\ge 1\), is the missing line. The sibling `ex:xnex` writes that argument. |
| V1-R2-014 | `chapters/field-guide.tex:265` | math | minor | “The three consecutive integers \(n-1,n,n+1\) contain exactly one multiple of \(3\). … Since \(8\) and \(3\) are coprime, their product divides \(n^2-1\) exactly when both do.” | The factor-of-\(8\) half is complete. The “exactly one” claim is the division algorithm: the remainder of \(n\) on division by \(3\) is \(0\), \(1\), or \(2\). The coprime-product step is one use of Euclid’s lemma: if \(3\) divides \(8\cdot(m/8)\) and \(3\) does not divide \(8\), then \(3\) divides \(m/8\). Both criteria were checked for \(-30\le n\le 40\). At \(n=3\), \(n^2-1=8\). |

## Round-1 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V1-001 | resolved | `chapters/ch01-sums.tex:661` “If some \(m\) with \(1\le m\le n\) had \(v_2(m)\ge s+1\), then \(2^{s+1}\) would divide \(m\), hence \(m\ge 2^{s+1}>n\). … \(v_2(L)=s\).” Exponents add and \(d\mid n\) iff \(v_p(d)\le v_p(n) |
| V1-002 | resolved | `chapters/ch02-counting.tex:241` “Chapter~\ref{ch:probability} asks for the expected number of cycles of a random permutation. That count uses expectation, which this chapter does not have yet.” `ex:cycles` (`ch09-probab |
| V1-003 | resolved | `orders.tex:287` “The count \(2k-1\) says the list is complete: nothing that meets \(A\) was left out.” The \(2k-1\) arcs are \(A\) and \(k-1\) explicit disjoint pairs, and that count is the classification. |
| V1-004 | resolved | `ch05-sequences-series.tex:277` \(u_{2n}-u_n=\frac1{n+1}+\cdots+\frac1{2n}\ge n\cdot\frac1{2n}=\frac12\). The square-root and logarithm witnesses are gone. |
| V1-005 | resolved | `ch05-sequences-series.tex:1315` “the mean value theorem on the exponential, from \(0\) to \(u\), supplies a point \(c\) … \(e^u-1=u\,e^c\). Apply it again, from \(0\) to \(c\).” Then \(\lvert e^u-1-u\rvert\le e\,u^2\),  |
| V1-006 | resolved | `ch05-sequences-series.tex:1424` “Hence \(\ln s=4\ln(s^{1/4})\le 4s^{1/4}\), and \(0<(\ln s)/s\le 4s^{-3/4}\).” The right side tends to \(0\), so the constant value of \(F\) is \(\zeta(2)\). |
| V1-007 | resolved | `ch05-sequences-series.tex:355` “Those three numbers are the slopes of \(y=x^2\) … The vertical axis is drawn at \(0.52\) of the mathematical height.” BrickRed, Goldenrod, and ForestGreen are rust, coral, and ochre in `c |
| V1-008 | resolved | `ch02-complex-roots.tex:245` “The zero argument before Proposition~\ref{prop:sincmp} gives \(\sin0=\sin\pi=0\), \(\sin(\pi/2)=1\), \(\cos0=1\), \(\cos(\pi/2)=0\), \(\cos\pi=-1\), and the two leastness sentences.” That ar |
| V1-009 | resolved | `ch03-polynomials.tex:112` “The formal derivative, defined above, satisfies \((A^m)'=mA^{m-1}A'\) in \(\mathbb K[X]\). … The same arithmetic holds for \(a\in\C\), because no step used a real limit.” The product rule and  |
| V1-010 | partial | `ch03-polynomials.tex:257` “With the equally likely coefficient pairs, it occurs with chance \(1/p^2\) for every fixed \(s\). The two shares therefore have the same distribution for every choice of the secret.” The bijec |
| V1-011 | resolved | `ch07-linear-algebra.tex:478–484` writes \(c^{\mathsf T}H_nc=\int_0^1\bigl(\sum c_ix^{i-1}\bigr)^2\,\mathrm dx\), invokes the sequences paragraph that a continuous nonnegative function of integral zero vanishes, and conc |
| V1-012 | resolved | `ch07-linear-algebra.tex:961` “The Gram section showed \(c^{\mathsf T}H_nc>0\) for every \(c\ne0\), so every eigenvalue of the real symmetric matrix \(H_n\) is positive. … \(\lambda_i\ge\lambda_{\min}>0\) for every \(i\) |
| V1-013 | resolved | `chapters/ch04-inequalities.tex:618` / “Termwise equivalence is not yet a statement about partial sums.” The next lines prove the comparison. Fix \(\eta\in(0,1)\), take \(\varepsilon\in(0,\eta/3)\), and split the sum at  |
| V1-014 | resolved | `chapters/preface.tex:41` “Chapter~\ref{ch:sequences} defines the limit and the derivative. The integral enters there as signed area, with the four rules in the paragraph on the integral below. A later volume builds that |
| V1-015 | resolved | The interval \([1,2]\) for \(x^2-2\) is gone. `chapters/ch00-language.tex:488` “For \(y>0\) the function \(t\mapsto t^2\) runs from \(0\) to \((y+1)^2>y\) on \([0,y+1]\).” |
| V1-016 | resolved | `chapters/ch00-language.tex:171` “For a collection \(E\) and a predicate \(P\), the word set still having the ordinary sense named in the opening reminder.” The reminder at `:51` allows ordinary use until the definition. |
| V1-017 | resolved | `chapters/ch00-language.tex:98` “Assuming the negation of the conclusion and reaching a statement together with its negation is a proof by contradiction. The next section separates that shape from the contrapositive.” |
| V1-018 | resolved | `chapters/ch00-language.tex:139` “If \(x>0\), then \(x\cdot x\) is a product of positive numbers, so \(x^2>0\). If \(x<0\), … so \(x^2>0\). If \(x=0\), then \(x^2=0\). In every case \(x^2\ge 0\).” The negation solution a |
| V1-019 | resolved | `chapters/ch00-language.tex:602` “Inclusions compose. If \(A\subseteq B\) and \(B\subseteq C\), then every element of \(A\) belongs to \(B\) and therefore to \(C\), so \(A\subseteq C\).” |
| V1-020 | resolved | `chapters/ch00-language.tex:606` defines a greatest element before the example. The example at `:610` comes after that sentence. |
| V1-021 | resolved | `chapters/ch00-language.tex:538` “If \(x\in f^{-1}(B)\), then \(f(x)\in B\), so \(x=g(f(x))\) lies in \(g(B)\). If \(x\in g(B)\), then \(x=g(y)\) for some \(y\in B\), so \(f(x)=y\in B\).” |
| V1-022 | resolved | `chapters/ch00-language.tex:418` “An ordered pair uses the same parentheses. When both readings are possible, the text says which.” |
| V1-023 | resolved | `chapters/ch00-language.tex:91` “Whether the implication holds for every real \(x\) is Exercise~\ref{ex:lang-implications}(c).” The universal claim is no longer given as a worked fact before the exercise. |
| V1-024 | resolved | `chapters/ch00-language.tex:890` “If \(x\ne 2\), the hypothesis is false, so the implication is true. If \(x=2\), then \(x^2=4\) by substitution.” |
| V1-025 | resolved | `chapters/ch00-language.tex:902` “From the definition of absolute value, \(\lvert t\rvert^2=t^2\): if \(t\ge 0\) then \(\lvert t\rvert=t\), and if \(t<0\) then \(\lvert t\rvert=-t\) and \((-t)^2=t^2\).” The midpoint solu |
| V1-026 | resolved | `chapters/ch00-language.tex:1061` “It is the only maximal element. If \(m\) is maximal, then \(m\preceq g\) because \(g\) is greatest. The alternative \(m\prec g\) would put something strictly above \(m\), so \(m=g\).” |
| V1-027 | resolved | `chapters/ch00-language.tex:859` “Equality of outputs inherits reflexivity, symmetry and transitivity from equality of elements of \(F\).” |
| V1-028 | resolved | `blurb.tex:7` “One workshop matches the powers of two five times, then gives 31. … The probability chapter works a medical test … the expected counts are 99 true positives and 495 false positives.” That matches `ex:five- |
| V1-029 | resolved | `kdp.md:13` “The cube identity, the hat check, and the intermediate value theorem are here so you can see why a formula holds.” |
| V1-030 | resolved | `chapters/preface.tex:62` “This volume defines a prime and proves that every integer greater than \(1\) factors into primes in exactly one way, up to order. Exercise~\ref{ex:fermat} proves \(a^p\equiv a\pmod p\). Volume~ |
| V1-031 | resolved | `chapters/ch01-sums.tex:379` “The coefficient comparison is the second proof already written. … Exercise~\ref{ex:squares} is the case \(m=n\) and \(r=n\).” |
| V1-032 | resolved | `chapters/ch01-sums.tex:228` “For any integers \(a\) and \(b\), say that \(a\) divides \(b\), … when \(b=ac\) for some integer \(c\).” Restated at `:595` with “no restriction on the sign of \(a\).” |
| V1-033 | resolved | `chapters/ch01-sums.tex:228` “A single prime counts as a product of one prime.” Used at `:231`: “a prime would be a product of one prime.” |
| V1-034 | resolved | `chapters/ch01-sums.tex:650` “The positive divisors of \(q\) are \(1\) and \(q\). Since \(p>1\), one has \(p=q\). … a nonempty product of primes is at least \(2\), and cannot equal \(1\).” |
| V1-035 | resolved | `chapters/ch01-sums.tex:560` “The first term is odd. … Each later term differs from this first term by \(2t\) … and \(2t\) is even, so each later term is odd as well.” |
| V1-036 | resolved | `chapters/ch01-sums.tex:164` “the same cancellation … applies, with a different range. … The proposition sums \(v_{k+1}-v_k\) from \(k=0\) to \(n-1\). Here the sum runs from \(k=1\) to \(n\).” The value \(1-1/(n+1)\) is  |
| V1-037 | resolved | `chapters/ch01-sums.tex:632`–`:634` “Since \(a\) divides both \(M\) and \(L\), it divides \(r=M-qL\).” Then transitivity is written, and the repeated lcm is shown to divide every common multiple of the list. |
| V1-038 | resolved | `chapters/ch01-sums.tex:630` “Every integer not divisible by \(p\) therefore has a multiplicative inverse modulo \(p\).” The word “residue” is gone. The inverse is Bézout. |
| V1-039 | resolved | `chapters/ch01-sums.tex:1056` “\((\Delta P)(m)=P(m+1)-P(m)\) is a difference of integers whenever \(P\) takes integer values at the integers, and the same holds at each later difference.” The unwritten binomial expansion |
| V1-040 | resolved | `chapters/ch01-sums.tex:704` “Volume~5 reads an exact coefficient off the binomial series of a rational generating function.” That is the coefficient \(\alpha^n\sum_j c_{m-j}\binom{n+j-1}{j-1}\) in `volume5-calculation/c |
| V1-041 | resolved | `chapters/ch02-counting.tex:410` “\(\binom60+\binom51+\binom42+\binom33=1+5+6+1=13\)”. The stray opening bar is gone. The sum is 13, and \(F_7=13\). |
| V1-042 | resolved | `chapters/ch02-counting.tex:146` “Proposition~\ref{prop:binom} expands \((x+y)^r=\sum_k\binom rk x^k y^{r-k}\), so the sum here is \(\bigl((-1)+1\bigr)^r=(1-1)^r=0\).” |
| V1-043 | resolved | `chapters/ch02-counting.tex:73` “For \(k=n\) the injection count is the product \(n(n-1)\cdots 1=n!\). Every such injection uses every element of \(E\), so it is surjective, and therefore a bijection.” |
| V1-044 | resolved | `orders.tex:24` “The list \(3,2,1,6,5,4,9,8,7,10\) has the increasing subsequence \(3,6,9,10\), and no four consecutive terms are monotone. That subsequence is the case \(n=3\).” |
| V1-045 | resolved | `orders.tex:324` “Volume 7, Chapter 1, states the axiom of choice and proves Zorn’s lemma. It does not define dependent choice.” |
| V1-046 | resolved | The announcing sentence is gone. `orders.tex:314` “Euclid’s algorithm stops because the remainder is a natural number, and a natural number cannot fall forever.” |
| V1-047 | resolved | The `make` sentence is gone. `orders.tex:86` “It is the order of a list of tasks: choose a minimal task, do it, and repeat on what remains.” |
| V1-048 | resolved | `ch05-sequences-series.tex:308` “That preservation is what the next section calls continuity. Newton’s argument above did not need the word.” |
| V1-049 | resolved | `ch05-sequences-series.tex:194` “The same words will be used for functions once a limit \(x\to a\) has been defined, later in this chapter. Until then they are statements about sequences.” |
| V1-050 | resolved | `ch05-sequences-series.tex:470` “The closed form \(\frac{1+\sqrt5}2\) waits until the next example has produced positive square roots.” Rolle’s interval \([0,\sqrt3]\) is named at line 549, after the root example at line |
| V1-051 | resolved | `ch05-sequences-series.tex:640` “the mean value theorem gives \(\cos y-\cos x=-\sin c\cdot(y-x)\) … so \(\cos y<\cos x\). Cosine is strictly decreasing from \(\cos 0=1\) to \(\cos\frac\pi2=0\).” |
| V1-052 | resolved | `ch05-sequences-series.tex:485` “a general real polynomial of odd degree is a nonzero constant times a monic one: divide by the leading coefficient.” |
| V1-053 | resolved | `ch05-sequences-series.tex:661` “Set \(\int_a^a f=0\). … For \(a<b\), define \(\int_b^a f=-\int_a^b f\).” The sign is derived from the constant rule and additivity. |
| V1-054 | resolved | `ch05-sequences-series.tex:659` “On each refined piece, … heights differ by at most \(\varepsilon\). The total change is at most \(\varepsilon(b-a)\). … The two original sums therefore differ by at most \(2\varepsilon(b- |
| V1-055 | resolved | `ch05-sequences-series.tex:268` “Past the corresponding \(N\), every term is within \(1\) of \(u_N\), so the tail is bounded. To bound the terms before \(N\), take the largest of \(0\) and their absolute values.” |
| V1-056 | resolved | `ch05-sequences-series.tex:270` the estimate is a single pair of bars: absolute value of \(u_p-\ell\) is at most \(\varepsilon\). The doubled bar is not in the source. |
| V1-057 | resolved | `ch05-sequences-series.tex:313` “the first vertical segment runs down from \((1.5,1.5)\) to \((1.5,\sin 1.5)\).” The plate uses \(0.9975\), and \(\sin 1.5=0.99749\ldots\). |
| V1-058 | resolved | `ch05-sequences-series.tex:313` “The four rust labels are those block sums, about \(0.50\), \(0.58\), \(0.63\) and \(0.66\). The horizontal rust edges sit at the shortest bar of each block, which equals the sum only for  |
| V1-059 | resolved | `ch05-sequences-series.tex:1244` “Proposition `prop:posseries`(c) assumes the interval \([1,\infty)\), and both functions blow up at \(t=1\), so the comparison has to start at \(2\).” |
| V1-060 | resolved | `ch05-sequences-series.tex:1418` “For any \(x\in(0,1)\), that theorem on the segment joining \(x\) to \(1/2\) gives \(F(x)=F(1/2)\).” |
| V1-061 | resolved | `ch05-sequences-series.tex:1383` “If \(\alpha\le 0\), then \(n^{-\alpha}\) does not tend to \(0\). … The series diverges.” |
| V1-062 | resolved | `ch05-sequences-series.tex:448` “restrict \(f(x)=x^2-2\) to the rationals in \([0,2]\).” Line 463 names the failing step: adjacent sequences over \(\mathbb Q\). |
| V1-063 | resolved | `ch02-complex-roots.tex:235–239` sets \(n=-m\), writes \((e^{i\theta})^n=(e^{-i\theta})^m\), and applies the nonnegative case at angle \(-\theta\), with \(\cos(-t)=\cos t\) and \(\sin(-t)=-\sin t\) from the addition form |
| V1-064 | resolved | `ch02-complex-roots.tex:52–67` expands \((z_1z_2)z_3\) into the eight real products, then says the other grouping “produces the same eight real products, because multiplication of real numbers is commutative and associat |
| V1-065 | resolved | `ch02-complex-roots.tex:651` “Volume~3 proves that a regular \(p\)-gon for an odd prime \(p\) is constructible with ruler and compass exactly when \(p-1\) is a power of \(2\).” The degree \(p-1\) is the local theorem. Th |
| V1-066 | resolved | `figures/ch02-bombelli.tex:17` “one cube root: \((2+i)^3=2+11i\)”. The caption at `ch02-complex-roots.tex:176` states the four powers and the angle, not a unique cube-root symbol. |
| V1-067 | resolved | `ch02-complex-roots.tex:838` integrates \(\cos(k\theta)\) and \(\sin(k\theta)\) by `prop:early-ftc` and says “A complex integral is not defined in this volume.” |
| V1-068 | resolved | `figures/ch03-threepoints.tex:6` places the third node at \((3.6,1.33)\). The drawn formula \(0.15(x-0.6)(x-2.2)+0.7\) equals \(1.33\) there. |
| V1-069 | resolved | `ch03-polynomials.tex:294` defines \(\sinh t\) and says “The hyperbolic sine is the square root in that check.” The proof takes \(\sqrt{x^2-1}=\sinh t\) for \(t\ge0\). |
| V1-070 | resolved | `ch03-polynomials.tex:739` writes the two bounds \(\pi^2 m(2m-1)/\bigl(3(2m+1)^2\bigr)\) and \(\pi^2\cdot 2m(m+1)/\bigl(3(2m+1)^2\bigr)\), both tending to \(\pi^2/6\), and says the old leading piece “is that same constan |
| V1-071 | resolved | `ch03-polynomials.tex:442` factors \(P'=3\bigl(X-1/\sqrt3\bigr)\bigl(X+1/\sqrt3\bigr)\), gives the sign chart on \((-\infty,0]\), and compares \(\bigl(2/(3\sqrt3)\bigr)^2=4/27<1\). |
| V1-072 | resolved | `ch03-polynomials.tex:451` inducts: the two-factor rule adds one logarithmic derivative, so a product’s logarithmic derivative is the sum. |
| V1-073 | resolved | `ch03-polynomials.tex:151` “cut off at \(3.5\)” and “at the corner \(-1.6-1.6i\) one has \(\lvert z\rvert^2=5.12\)”. That square is \(2\cdot1.6^2\). The plate stores the cutoff; the caption states the true square. |
| V1-074 | resolved | `ch07-linear-algebra.tex:403` “Theorem~\ref{thm:dalembert} supplies a root \(\lambda\in\C\).” |
| V1-075 | resolved | `ch07-linear-algebra.tex:330` and `:337`: \(n\) eigenvectors for distinct eigenvalues are independent by the Lagrange action on eigenvectors, “so \(M\) is diagonalisable without Cayley–Hamilton.” `thm:diag` is no longer  |
| V1-076 | resolved | `ch07-linear-algebra.tex:272` “The monic divisor and the leading coefficient therefore fix the constant: \(P=V(x_1,\dots,x_{n-1})\prod_{i<n}(X-x_i)\).” |
| V1-077 | resolved | `ch07-linear-algebra.tex:340` substitutes \(u_n=\alpha+\beta n\) into the recurrence, matches \(\alpha=u_0\) and \(\beta=u_1-u_0\), and computes \(\ker(M-I)\) as the line through \((1,1)\). |
| V1-078 | resolved | `ch07-linear-algebra.tex:154` computes the shear on the spot: \((a)(d+tc)-(b+ta)c=ad-bc\). The forward citation of `thm:det` is gone. |
| V1-079 | resolved | `chapters/ch06-integrals-taylor.tex:68` and `:326` / “Until that proposition the picture is a quarter disk; the number \(\pi/4\) is not a standing evaluation of its area.” Proposition `prop:wallis` then computes \(W_2=\f |
| V1-080 | resolved | `chapters/ch06-integrals-taylor.tex:287` / “Theorem~\ref{thm:lhopital} proves only the \(\frac00\) case. Exercise~\ref{ex:lhopital} gives the other form a proof, and that exercise has not been done yet.” The limit \(\ln  |
| V1-081 | resolved | `chapters/ch06-integrals-taylor.tex:522` / “The derivatives of \(\ln(1+t)\) are \((1+t)^{-1}\), \(-(1+t)^{-2}\), \(2(1+t)^{-3}\), \(-6(1+t)^{-4}\) and \(24(1+t)^{-5}\).” Taylor’s inequality at order \(4\) gives a remaind |
| V1-082 | resolved | `chapters/ch06-integrals-taylor.tex:505` / “Convexity, and the claim that a tangent lies below the graph, are the next chapter. The error bounds in Proposition~\ref{prop:quadrature} do not use them.” In `main.tex` the in |
| V1-083 | resolved | `chapters/ch06-integrals-taylor.tex:860` / “To see \(\varepsilon^{m+1}(\ln\varepsilon)^n\to0\), set \(t=-\ln\varepsilon\)” and reduce to \((\ln t)/t\to0\) by \(\ln t\le4t^{1/4}\). The exponential of an exponent that tend |
| V1-084 | resolved | `chapters/ch06-integrals-taylor.tex:890` / “The second equality uses additivity of oriented integrals, so it holds for any finite cutoffs.” The error after replacing \(f\) by the constant \(f(0)\) or \(f(\infty)\) is bou |
| V1-085 | resolved | `chapters/ch06-integrals-taylor.tex:123` / “Volume~7 builds the integral as Lebesgue measure. Heine's theorem, already proved, is what makes a continuous function on a segment Riemann integrable; it is one step of that d |
| V1-086 | resolved | `chapters/ch06-integrals-taylor.tex:101` / “A continuous strictly increasing graph with \(f(0)=0\).” The caption then states the inverse-integral identity under those hypotheses. |
| V1-087 | resolved | `chapters/ch04-inequalities.tex:305` and `:651` / “The sequences chapter showed that a continuous nonnegative function with integral zero vanishes everywhere.” That argument is now written in `chapters/ch05-sequences-ser |
| V1-088 | resolved | `chapters/ch04-inequalities.tex:559` / “If every coordinate is nonzero, the \(p\)-norm is \(n^{1/p}M_p(\lvert a_1\rvert,\dots,\lvert a_n\rvert)\), and \(n^{1/p}\to1\).” A zero coordinate is dropped; the maximum of the ab |
| V1-089 | resolved | `chapters/ch09-probability.tex:219` / “The terms \(1/k!\) are non-increasing and tend to \(0\). The first two equal \(1\), and the sequence is strictly decreasing from \(k=1\) on. Proposition~\ref{prop:signedseries} asks |
| V1-090 | resolved | `chapters/ch09-probability.tex:764` / “The bar comparison in Proposition~\ref{prop:posseries}(c), started at \(19\) rather than at \(1\), gives \(\sum_{k\ge20}1/k^2\le\int_{19}^\infty x^{-2}\,dx=1/19\).” That is the ineq |
| V1-091 | resolved | `chapters/ch09-probability.tex:791` / “A million independent, identically distributed continuous observations are not a model built in this chapter. … That identification is not a theorem here.” The Chebyshev bound is pr |

## Recomputed here

These values were recomputed in Python for this review. Each matches the text.

- \(1^3+\cdots+10^3=3025=55^2\). For \(2\le n\le 39\), if \(2^s\le n<2^{s+1}\), then \(v_2(\operatorname{lcm}(1,\ldots,n))=s\).
- Six bisection steps on an interval of length \(1.2\) leave length \(1.2/64=0.01875\). The cosine upper bound at \(8/5\) equals \(-13/1875\).
- At \(n=10\), \(10!/(\sqrt{10}\,(10/e)^{10})=2.527597\) and \(\sqrt{2\pi}\,(1+1/120)=2.527517\).
- Birthday: the probability that \(23\) dates are distinct is \(0.492703\), so a shared birthday has probability \(0.507297\).
- Medical test: \(P(+)=0.0594\) and \(0.0099/0.0594=1/6\).
- \(\varphi^{10}\) begins \(122.991869\), and \(\varphi^{10}+\psi^{10}=123\).
- Derangement counts through \(n=7\): \(1,0,1,2,9,44,265,1854\).
- Twenty terms of Euler’s fast series for \(\zeta(2)\) total \(1.644934\). The comparison tail \(1/(21^2\cdot 2^{20})\) equals \(2.16\times 10^{-9}\).
- The orbit of \(27\) under the cover rule takes \(111\) steps and peaks at \(9232\). Every integer from \(2\) to \(8000\) reaches \(1\).
- Divisibility of \(n^2-1\) by \(24\) holds exactly for odd \(n\) not divisible by \(3\), on \(-30\le n\le 40\).

The chapter reading recomputed the other displayed constants named in the round-1 “Verified correct” sections (inclusion–exclusion up to \(100\), Catalan numbers through \(C_6\), Hilbert determinants, PageRank fractions, Carleman ratios, Wallis and Simpson samples). No mismatch with the printed value was reported, and the samples re-opened here agree.

## Verified correct

### Preface, jacket, About the Cover

The standing list now says that the two cosine comparisons are theorems of the sequences chapter, not extra assumptions (`preface.tex:31` and `:42`). The integral is signed area plus four rules, with the construction deferred. The blurb’s four cube proofs, the medical-test counts, and the named theorems are in this volume. About the Cover matches `common/cover-notes.json`, and the Collatz claims were recomputed as above. The handoff names Volume 2, *The Integers: Primes, Patterns and Proofs*.

### Chapters 0–2

The sign proof of \(x^2\ge 0\), transitivity of inclusion, the two inclusions for \(f^{-1}\), and the valuation form of the lcm were read. Unique factorisation now cancels a prime by the positive-divisor sentence, and \(v_p(ab)=v_p(a)+v_p(b)\) is written. The harmonic solution cites that test. Inclusion–exclusion up to \(100\) is \(74\). The derangement list through \(n=7\) matches.

### Chapters 3–4

The harmonic Cauchy witness \(u_{2n}-u_n\ge 1/2\) replaces the old square-root and logarithm witnesses. The two mean-value steps for the Stirling exercise give \(|e^u-1-u|\le e\,u^2\). The Basel exercise names the constant from \(\ln s\le 4s^{1/4}\). The cosine least-period argument was read line by line: the bound \(\cos(8/5)<0\), the sign chart of sine on \((0,4\alpha]\), and the identification \(4\alpha=2\pi\). The one missing clause is `V1-R2-010`. The Erdős–Ko–Rado list was read: the \(2k-1\) arcs are \(A\) and \(k-1\) disjoint pairs, separated because one arc of each pair contains \(n\) and the forward arc does not, and the count says the list is complete.

### Chapters 5–7

Formal differentiation gives the multiplicity count for \(a\in\C\). The Hilbert determinant is the integral of a square, and every eigenvalue is positive before the product bound. The spectral proof cites `thm:dalembert`. Distinct eigenvalues give \(n\) independent eigenvectors without Cayley–Hamilton. Horner’s value \(79\), the least-squares line \(a=7/6\), \(b=1/2\), and \(\det H_2=1/12\) match.

### Chapters 8–10 and the field guide

The Carleman comparison now splits the partial sums and proves \(\sum_{n\le N}1/(n!)^{1/n}\sim eH_N\). The quarter-disk area is \(W_2=\pi/4\), after the change of variables. The vanishing of a continuous nonnegative function with integral zero is proved in the sequences chapter and cited from there. Bertrand’s sentence in the field guide is the statement of Volume 2’s theorem: for every integer \(n\ge 1\) there is a prime \(p\) with \(n<p\le 2n\). Every index label exists.

## Not checked

- A LaTeX build, so printed page numbers, overfull boxes, and split frames were not seen.
- EPUB rendering and the Kindle alt text.
- Portrait files and licence lines. `photos/CREDITS.md` was not re-hashed.
- Primary pages of the memoirs named in the source lists.
- Every coordinate of the large `pgfplots` tables beyond the endpoints and the numbers recomputed above.
- The internal steps of Volume 7’s Lebesgue construction, beyond the sentence that Heine’s theorem is one step of it.
