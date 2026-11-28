# Volume 7, round 1 review

Reviewed `af3f9afbaee7b76237f8b9ad085420fda82d328f` (`origin/main` at review time). Sources: `volume7-spaces/`. Intent: `docs/plan/book-07.md`. No book file was edited.

**Score: 8/10.**

The constructions this volume owns are in place: the reals, Banach's fixed-point theorem, compactness and Stone–Weierstrass (Theorem 4.19), Baire, Carathéodory and Lebesgue measure, the convergence theorems, Tonelli and Fubini (Theorems 9.5 and 9.6), change of variables (Theorem 9.8), \(L^p\), Hahn and Radon–Nikodym, conditional expectation and the tower, Riesz, Prokhorov, Kolmogorov, and the Jordan argument. The convergent half of Khinchin really does give \(\lambda(E_q)\le 8q\psi(q)\). One numbered statement is false as written, the mean-value corollary without continuity, and a run of local sentences in proofs and solutions are false or do not close. That is short of a broken flagship theorem, and it is more than a handful of slips.

Jordan is a real chapter, so the printed numbers sit one chapter later than the plan's "Theorem 8.6 / 8.8 / 10.4 / 11.3". The book and its index use the printed numbers. Do not renumber.

## Issues

V7-R1-001 | major | `volume7-spaces/chapters/ch04-compact.tex:178` | Part (d) of the mean value theorem says that \(f'\ge 0\) on the interior of an interval \(I\) makes \(f\) non-decreasing, that \(f'=0\) makes \(f\) constant, and that \(|f'|\le M\) makes \(f\) Lipschitz. Continuity of \(f\) on \(I\) is not assumed. On \([0,1]\), the function with \(f(0)=1\) and \(f=0\) on \((0,1]\) has derivative \(0\) on the interior and is neither non-decreasing, nor constant, nor Lipschitz. The proof applies part (c) on every \([x,y]\subset I\), and part (c) needs continuity on that segment. | State that \(f\) is continuous on \(I\) and differentiable on the interior.

V7-R1-002 | minor | `volume7-spaces/chapters/ch01-sets.tex:354` | The proof that \(\mathbb Q\) is countable injects \(\mathbb Q\) into \(\mathbb Z\times\mathbb Z\) and then says a subset of a countable set is countable. \(\mathbb Z\times\mathbb Z\) has not been shown countable. The injection of \(\mathbb Z\) into \(\mathbb N\times\mathbb N\) does finish the argument for \(\mathbb Z\). | Compose with an injection \(\mathbb Z\to\mathbb N\) and the pairing already proved for \(\mathbb N\times\mathbb N\).

V7-R1-003 | minor | `volume7-spaces/chapters/ch01-sets.tex:641` | A bijection between the segment and the square "cannot be continuous", with the proof deferred to Exercise `ex:notR2`. That exercise shows there is no homeomorphism. A continuous bijection is a homeomorphism only after the compact-to-Hausdorff fact in Chapter 4. | Cite the exercise for "not homeomorphic", and the later proposition for "no continuous bijection".

V7-R1-004 | minor | `volume7-spaces/chapters/ch01-sets.tex:648` | A finite-dimensional vector space over \(\mathbb Q\) is described as a finite union of copies of \(\mathbb Q^d\). It is one copy of \(\mathbb Q^d\). | Say it is in bijection with \(\mathbb Q^d\), which is countable by the pairing.

V7-R1-005 | minor | `volume7-spaces/chapters/ch02-metric.tex:169` | Banach's second bound uses \(x_{n-1}\). At \(n=0\) that term is not defined. For \(n\ge 1\) the bound is the first estimate restarted one step earlier. | Restrict the second inequality to \(n\ge 1\).

V7-R1-006 | minor | `volume7-spaces/chapters/ch02-metric.tex:185` | The cosine Newton map is said to double the number of correct digits at each step, citing Exercise `ex:newton`. That exercise is \(N(x)=\frac12(x+a/x)\) for square roots. It does not treat \(x-(x-\cos x)/(1+\sin x)\). | Point the cosine sentence at a simple root, and leave the exercise as the square-root case.

V7-R1-007 | minor | `volume7-spaces/chapters/ch02-metric.tex:442` | The solution says the a priori bound gives \(|T^n(2)-x|_5\le 5^{-n-1}\). Here \(k=\frac15\) and \(d(2,T(2))=\frac15\), so Theorem `thm:banach` gives \(\frac{k^n}{1-k}d(2,T(2))=\frac54\cdot 5^{-n-1}\), which is larger than \(5^{-n-1}\). The contraction \(|T(y)-x|_5\le\frac15|y-x|_5\) with \(|2-x|_5\le\frac15\) does give \(5^{-n-1}\). The digits \(2,1,2\) and \(57^2+1=3250=26\cdot 125\) are right. | Name the contraction from the first step, not the a priori bound.

V7-R1-008 | minor | `volume7-spaces/chapters/ch03-topology.tex:304` | "The values of sine fill \([-1,1]\) on every interval of length \(2\pi\)." On \((\pi/2,\pi/2+2\pi)\) the value \(1\) is missed. The next sentences prove the fact actually used, on the closed intervals \([2\pi n+\pi/2,\,2\pi n+3\pi/2]\). | Delete the sentence, or replace it with those closed intervals.

V7-R1-009 | minor | `volume7-spaces/chapters/ch03-topology.tex:580` | "An interval \(I\) that is a continuous image of \(S^1\) has at least two points." A constant map is a continuous image of the circle. The exercise is about homeomorphisms, and a homeomorphic image cannot be a singleton. | Replace "continuous image" with "homeomorphic image".

V7-R1-010 | minor | `volume7-spaces/chapters/ch05-baire.tex:182` | The proof says the complement of the meagre set is exactly the set of nowhere differentiable functions. Membership in \(E_n\) only bounds right difference quotients; it does not force a derivative. The complement is a comeagre set of nowhere differentiable functions, which is what Theorem `thm:banachmaz` needs, and it is smaller than the whole set. Takagi's function is nowhere differentiable by Theorem `thm:takagi`, and it lies in \(E_n\) for every \(n\ge 7\): at \(x=\frac13\), each term of slope \((-1)^n\) contributes that sign to the quotient while \(2^nh<\frac16\), the alternating sum through that range has absolute value at most \(1\), and the tail is at most \(6\), so the quotient is at most \(7\). | End with: the complement is a comeagre, hence dense, set of nowhere differentiable functions.

V7-R1-011 | minor | `volume7-spaces/chapters/ch07-integral.tex:171` | A Riemann sum trapped between \(L(f,P)\) and \(U(f,P)\) does not by itself tend to the integral as the mesh tends to \(0\). Darboux integrability produces some partitions with \(U-L\) small. The passage from those partitions to every partition of small mesh is not written. The claim is true for a bounded function on a segment. | Add the standard mesh estimate, or point at it.

V7-R1-012 | minor | `volume7-spaces/chapters/ch07-integral.tex:475` | For \(f_n=\mathbf 1_{[n,n+1]}\), "each \(x\) belongs to at most one of these intervals". The integer \(n+1\) lies in both \([n,n+1]\) and \([n+1,n+2]\). The limit is still \(0\), since each \(x\) lies in at most two of them, and the integral is still \(1\). | Say at most two, or use \([n,n+1)\).

V7-R1-013 | minor | `volume7-spaces/chapters/ch07-integral.tex:487` | For \(f=\mathbf 1_{]0,\infty[}\), "on any segment, \(f\) has one discontinuity". On \([1,2]\) the function is identically \(1\). On \([0,1]\), the segment the counterexample uses, there is one discontinuity, at \(0\). | Restrict the sentence to \([0,1]\).

V7-R1-014 | minor | `volume7-spaces/chapters/ch07-integral.tex:638` | Theorem `thm:riemanncont` is cited as identifying the Riemann integral of a continuous function with the Lebesgue integral. That theorem gives Riemann integrability and the four rules. It does not mention Lebesgue measure. The value \(2\ln 2-1\) is right: the antiderivative of \(2/(2-x)-1\) is \(-2\ln(2-x)-x\). | Cite Lebesgue's criterion for the identification.

V7-R1-015 | minor | `volume7-spaces/chapters/ch09-lp.tex:113` | Off the null set \(N\), a Cauchy sequence in \(L^\infty\) is uniformly Cauchy, and the proof says the limit is a bounded function. An essentially bounded representative can be unbounded on a null set that never enters \(N\). Take every \(f_n\) equal to the function that is \(n\) at the integer \(n\) and \(0\) elsewhere. Then all differences are \(0\), so \(N=\varnothing\), and the pointwise limit is unbounded. The norm bound two sentences later is unaffected. | Excise \(\{|f_n|>\|f_n\|_\infty\}\) into \(N\), or say the limit is essentially bounded.

V7-R1-016 | minor | `volume7-spaces/chapters/ch10-radon.tex:476` | One \(\varepsilon>0\) and \(\mathbb P(|\sum_{k\le n}Y_k|\ge n\varepsilon)\le 3/(\varepsilon^4 n^2)\) give, by Borel–Cantelli, only \(\limsup_n|\frac1n\sum_{k\le n}B_k-p|\le\varepsilon\) almost surely. The null set depends on \(\varepsilon\). The fourth-moment count \(n+3n(n-1)=3n^2-2n\le 3n^2\) is right. The strong law itself is true after a countable intersection. | Intersect the null sets for \(\varepsilon=1/m\), as in the proof of Theorem `thm:borelnormal`.

V7-R1-017 | minor | `volume7-spaces/chapters/ch11-metricmeasures.tex:76` | If the finite subcover never uses an index \(i\), then \(W_i=\varnothing\). The distance from the empty set is not a positive real, and the Urysohn formula on line 81 is then undefined. The lemma is true. | If \(W_i=\varnothing\), set \(g_i=0\).

V7-R1-018 | minor | `volume7-spaces/chapters/ch11-metricmeasures.tex:774` | Tightness is "for every \(\varepsilon>0\) there is an \(M\)". The write-up assumes one pair \((M,\varepsilon)\) and concludes \(\lim_{t\to-\infty}F(t)=0\) and \(\lim_{t\to+\infty}F(t)=1\). One pair gives only the bounds \(\varepsilon\) and \(1-\varepsilon\). The escape example \(F_n=\mathbf 1_{[n,\infty)}\) is right. | Write the quantifier: for every \(\varepsilon>0\), tightness supplies an \(M\).

V7-R1-019 | minor | `volume7-spaces/chapters/index.tex:76` | The index entry "Tychonoff, 1930" points at Theorem 4.11. That theorem is headed "Tychonoff, 1935", and the chapter text says 1930 is the product of segments while 1935 is the general product. The number 4.11 matches the environment count. | Change the index name to "Tychonoff, 1935".

Counts: 0 critical, 1 major, 18 minor.

## Citations checked, and not issues

Volume 1 sets the chapter counter to \(-1\) before the language chapter, so that chapter is Chapter 0. Theorem, proposition, lemma, corollary, definition, and example share one counter. Opened and matched:

- Volume 1, Proposition 6.9 is Gauss's lemma (polynomials is Chapter 6; the ninth environment). Part (b) is the factorisation form used for rational roots.
- Volume 1, Theorem 9.4 is Cauchy–Schwarz, Theorem 9.5 is Young, and Theorem 9.6 is Hölder (inequalities is Chapter 9).
- Volume 2, Chapter 9 is continued fractions. Proposition 9.1 is the convergent recurrence, Theorem 9.2 is the signed error, Lemma 9.4 is best approximation, Theorem 9.5 is Legendre's \(\frac1{2q^2}\) test, and Theorem 9.6 is "eventually periodic if and only if quadratic". Exercise 2.8 is Furstenberg's arithmetic-progression topology. Exercise 9.7 is the Liouville exercise.
- Volume 3, Chapter 6 is the rings chapter; the field of fractions is constructed there.
- Volume 4, Chapter 5 is the continuous chapter, and Exercise 5.7 is \(X=\sum 2B_k 3^{-k}\). Chapter 6 is the chapter that contains the Gaussian vectors.
- Volume 5, Chapter 3 is the series chapter (\(\zeta(2)\)), Chapter 4 the integral chapter, Chapter 5 the Gamma chapter (the ball volume \(V_n=\pi^{n/2}/\Gamma(n/2+1)\), with \(V_1=2\), \(V_3=\frac43\pi\), \(V_4=\pi^2/2\)). Theorem 6.13 is Weyl's criterion.
- Volume 6, Theorem 5.5 is the prime number theorem (`ch05-pnt.tex` is Chapter 5, and that theorem is the fifth environment).
- Volume 11, Chapter 9 is the martingale chapter.

The plan's "Theorem 8.6" and "Theorem 8.8" are the positions of Fubini and change of variables inside `ch08-products.tex`. Printed, with Jordan as Chapter 6, they are Theorems 9.6 and 9.8. The index in this volume says so, and Volume 5 cites Tonelli as Volume 7, Theorem 9.5. Not an error.

Conditional expectation is Theorem `thm:condexp` and the tower is Theorem `thm:tower`, both in the Radon–Nikodym chapter. The plan's request to promote the exercise is already done.

## Recomputed and left as correct

- \(\sin 1\le 1-\frac16+\frac1{120}=\frac{101}{120}\). Numerically \(\sin 1\approx 0.84147<0.84167\). The fixed point of cosine on \([0,1]\) is \(0.739085\ldots\).
- Newton for \(\sqrt 2\) from \(2\): the stated majorants \(0.586\), \(0.122\), \(0.0053\), \(1.0\cdot 10^{-5}\), \(3.6\cdot 10^{-11}\), \(4.6\cdot 10^{-22}\) hold, and the true fifth error is \(8.99\cdot 10^{-25}\).
- Unit-ball volumes \(2\), \(\pi\), \(\frac43\pi\), \(\frac{\pi^2}2\). Carpet dimension \(\log 8/\log 3\approx 1.8928\).
- Khinchin's convergent cover: for \(x\in[0,1]\) and \(q\psi(q)<1\), the integers \(p\) with \(|qx-p|<1\) satisfy \(-1\le p\le q+1\), so \(q+3\) intervals of length \(2\psi(q)\). For \(q\ge 1\), \(2(q+3)\le 8q\).
- The series evaluation \(\int_0^1 x/(2-x)\,dx=2\ln 2-1\).
- Inside `volume7-spaces/`, 399 labels, every `\ref` resolves, and no label is repeated. This was a source check, not a TeX run.

## Not checked

`./build.sh` was not run. No Actions log was opened. TikZ geometry was not checked, except where a caption states a number listed above. Historical publication data were not re-opened, apart from the 1930/1935 split as this book states it. The change-of-variables proof, the Jordan chain, and Tychonoff's maximality argument were not re-derived line by line; the numbered statements and the solutions that produced the issues above were read in the source. Chapter-level pointers to Volumes 8 and 12 were not opened.

## Exact next step

From `af3f9afbaee7b76237f8b9ad085420fda82d328f`, open one PR that fixes only V7-R1-001, by adding continuity of \(f\) on the interval \(I\) to part (d) of the mean value theorem in `volume7-spaces/chapters/ch04-compact.tex`. A different reviewer then writes `docs/review/volume7-r1-001-review.md` on that fix branch. Do not merge until CI is green on the reviewed head, and do not touch the Volume 6 branches.
