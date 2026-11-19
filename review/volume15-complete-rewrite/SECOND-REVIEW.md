# Second review of PR #252

Independent review of the Volume 15 additions on `cursor/volume15-complete-rewrite`, against base `60ce094742a84e3da028ad2c9d31d535db656344`. The reviewer is not the author of the pull request.

Scope: the 56 new exercises with their hints and solutions, the 28 new TikZ figures, preservation of the original manuscript, and the audit workflow. Every numerical claim in the new solutions was recomputed in Python, separately from the proofs. The new prose was read against the series voice. Each of the 28 plates was rendered and read against its caption.

## Issues

| ID | Place | Severity | Evidence | Fix | Verdict |
| --- | --- | --- | --- | --- | --- |
| SR-01 | `figures/v15c04-phases.tex` `fig:v15c04-phases` | major | The caption and the paragraph above it say \(f(15)=f(3)f(5)\). On the circle the arguments add. The points were \(f(3)\) at \(150^\circ\), \(f(5)\) at \(250^\circ\), and \(f(15)\) at \(190^\circ\). Then \(150+250\equiv 40\pmod{360}\), which was the angle of \(f(2)\), and \(150+40=190\). The drawn point was \(f(2)f(3)\). | The labels of \(f(2)\) and \(f(5)\) are exchanged. The radii already drawn through \(40^\circ\), \(150^\circ\) and \(190^\circ\) are now \(f(5)\), \(f(3)\) and \(f(15)\). Positions, fonts and the caption are unchanged. Commit `ef75727f`. | Fixed. |
| SR-02 | `moments-zeta.tex:193` `fig:v15c09-tent` | major | Theorem `thm:formfactor` splits the two functions. \(\hat K(\alpha)=(1-\lvert\alpha\rvert)_+\) is the transform of the squared sinc. The form factor is the transform of \(\delta_0-K\), equal to \(\lvert\alpha\rvert\) on \(\lvert\alpha\rvert\le 1\) and to \(1\) outside. The lead-in called the drawn tent the form factor. At the sample points of Exercise `ex:v15-09-1` the two functions are \(1,1/2,0\) and \(0,1/2,1\). The caption and the exercises already described \(\hat K\). | The sentence now names the tent as \(\hat K\) and says what the form factor is. Commit `f2c30a41`. | Fixed. |
| SR-03 | `ch11-values.tex:89` `ex:v15-11-2` | major | \(P_T(\log\lvert\zeta(1/2+it)\rvert\le 0)\to 1/2\) follows from Theorem `thm:selberg` at \(a=0\). The next sentence said that the median of \(\lvert\zeta\rvert\) is \(1\). The same argument gives \(P_T(\lvert\zeta\rvert\le c)\to 1/2\) for every fixed \(c>0\), because \(\log c\) is negligible beside \(\sigma_T=\sqrt{\tfrac12\log\log T}\). A median \(m_T\) of \(\lvert\zeta\rvert\) is forced only to satisfy \(\log m_T=o(\sigma_T)\). The caption and the bell-curve label repeated the stronger claim. | The exercise, hint, solution, lead-in and caption now state the proportion on each side of \(1\), and the same limit for any fixed positive threshold. The figure label marks the centre \(a=0\). Commit `f2c30a41`. | Fixed. |
| SR-04 | `ch14-meeting.tex:151` `ex:v15-14-4` | major | The exercise fixes an arbitrary \(\theta>0\) and sets \(h=x^\theta\). The proof said that every \(n\in(x,x+h]\) satisfies \(n\le 2x\), hence \(\omega(n)-\omega_y(n)\le\log(2x)/\log y\to 2/\theta\). For \(\theta>1\) the right endpoint is \(x+x^\theta\). At \(\theta=4\) and \(x=100\), \(y=10^4\) and the prime \(10007\) lies in the interval and contributes a prime factor larger than \(y\). Volume 6, Theorem 1.5 is the right citation: it is the fifth numbered statement of Chapter 1, \(\sum_{p\le x}1/p=\log\log x+M+O(1/\log x)\). | The bound is now \(n\le 2x^{\max(1,\theta)}\), so the count of large prime factors tends to at most \(2\max(1,\theta)/\theta\) and remains \(O_\theta(1)\). The Chebyshev step is unchanged. Commit `f2c30a41`. | Fixed. |
| SR-05 | `ch11-values.tex:101` `ex:v15-11-4` | major | The identity is true, including the factor \(1/2\) and the whole line. The derivative of the integrand in \(a\) is \(a/(a^2+u^2)\), and its integral over \(\R\) is \(\pi\operatorname{sign}(a)\). The write-up determined the constant on each half-line by the single condition \(a=b\). That point lies on only one half-line, so the opposite-sign case was not reached. The case \(a=0\) was a limit with no integrable dominant. | The integrand depends only on \(a^2\) and \(b^2\). The write-up now proves the formula for \(a>0\), \(b>0\), passes to \(a=0\) by dominated convergence, and reaches \(b=0\) by monotone convergence. Commit `f2c30a41`. | Fixed. |
| SR-06 | `figures/v15c13-symmetry.tex` `fig:v15c13-symmetry` | major | The caption says the shaded mass to the left of \(0\) is \(1-\delta(4;3,1)\), about \(0.004\), and that half the mass lies to the right of \(1\). The curve that was drawn had height \(0.22\) at \(0\) against a peak of \(0.40\). For a law of variance \(V=0.1556\) the standard deviation is \(\sqrt V\approx 0.394\), and the density at \(0\) is about \(4\%\) of the density at the mean. The chapter's own race-density figure already says this tail is too small to see as a lobe. | The curve is now the Gaussian shape of variance \(0.1556\), centred at \(1\), with the same peak height \(0.40\). The shade to the left of \(0\) is the thin tail. Fonts and the caption are unchanged. Commit `ef75727f`. | Fixed. |
| SR-07 | `figures/v15c13-wave.tex` `fig:v15c13-wave` | major | TikZ evaluates \(\cos\) in degrees. The plotted curve was \(1+0.33\cos(70u)\), so the period was \(360/70\approx 5.14\). The function in the caption, \(1+2\cos(\gamma u)/\lvert\rho\rvert\) with \(\gamma=6.0209\), has period \(2\pi/\gamma\approx 1.043\). The amplitude \(0.33\) agrees with \(2/\lvert\rho\rvert=0.3310\), and both curves stay positive. | The plot is now \(1+0.331\cos(\gamma u)\) in radians, on the same domain. Commit `ef75727f`. | Fixed. |
| SR-08 | `figures/v15c07-auts.tex` `fig:v15c07-auts` | major | The bar heights \(6\) and \(48\) are the right orders, and \(48/6=8\). The second label was \(\lvert\mathrm{Aut}(\Z/3)^2\rvert=48\). \(\lvert\mathrm{Aut}(\Z/3)\rvert=\varphi(3)=2\), so that square has order \(4\). The count \(48\) is \(\lvert\mathrm{Aut}((\Z/3)^2)\rvert=\lvert GL_2(\mathbb F_3)\rvert\). The caption already named the elementary group. | The node is now \(\lvert\mathrm{Aut}((\Z/3)^2)\rvert=48\). Commit `ef75727f`. | Fixed. |
| SR-09 | `ra-bias.tex:317` `ex:v15-13-3` | major | \(P(X>1)=1/2\) follows from symmetry about \(1\) and the absence of an atom at \(1\). The next sentence said that the same symmetry forces \(P(X>0)>1/2\) because \((0,1)\) has positive mass. Symmetry and the lack of atoms do not give that mass. Theorem `thm:rubinsteinsarnak` states full support separately, and the proof of Corollary `cor:biasdensity` cites that clause. | The write-up now separates the two clauses and uses full support for \(P((0,1))>0\). Commit `f2c30a41`. | Fixed. |
| SR-10 | `ch04-multiplicative.tex:74` `ex:v15-04-1` | minor | The solution is right: if \(n=p^km\) with \(k\ge 1\), then \(\mathbb E f(p)^k=0\). The hint said that the average of \(f(p)\) factors out. For \(n=4\), \(f(4)=f(2)^2\), and \(f(2)\) is not independent of itself. The integral that vanishes is \(\frac1{2\pi}\int_0^{2\pi}e^{2i\theta}\,d\theta=0\). | The hint now says that the average of \(f(p)^k\) is \(0\). Commit `f2c30a41`. | Fixed. |
| SR-11 | `ch05-short.tex:485` `ex:v15-05-1` | minor | The partial product is \(\prod_{3\le p\le 29}(1-(p-1)^{-2})=0.66513839\ldots\), which is \(0.6651\) to four decimals. The tail against the twin-prime constant is \(0.992518\ldots\), which is \(0.9925\) to four decimals, not \(0.992\). | The sentence now says \(0.9925\). `check_new_examples.py` recomputes the ratio. Commit `f2c30a41`. | Fixed. |
| SR-12 | `figures/v15c05-series.tex` `fig:v15c05-series` | minor | \(\mathfrak S(2)=\mathfrak S(4)=2C_2\) and \(\mathfrak S(6)=4C_2\). The first two bars ended at \(1.320\) and the third at \(2.641\), so the drawn heights were not in the ratio \(1:1:2\). The vertical axis stopped at \(1.7\), below the bar it was scaling. | Both \(2C_2\) bars end at \(1.320\) and the \(\mathfrak S(6)\) bar at \(2.640\). The axis now passes \(3\). Fonts and labels are unchanged. Commit `ef75727f`. | Fixed. |
| SR-13 | `ch06-sieves.tex:308` `ex:v15-06-2` | minor | \(\tfrac12\cdot\tfrac23\cdot\tfrac45\cdot\tfrac67=8/35=0.228571428\ldots\). The printed \(0.2286\ldots\) puts a \(6\) in the fourth place. That digit appears only after rounding to four decimals. | The expansion is now \(0.22857\ldots\). Commit `f2c30a41`. | Fixed. |
| SR-14 | `ch07-classgroups.tex:38` `ex:v15-07-1` | minor | The six-factor product is \(0.56051045\ldots\), which is \(0.5605\) to four decimals. The displayed pieces \(0.5706\) and \(0.9822\) were already rounded, and \(0.5706\times 0.9822=0.56044\ldots\), which is \(0.5604\) to four decimals. A second line repeated the words "to four decimals." | The pieces are now \(416/729=0.570645\) and \(0.982241\), and the stray line is gone. Commit `f2c30a41`. | Fixed. |
| SR-15 | `ch08-ranks.tex:211` `ex:v15-08-4` | minor | The probabilities match the chain and Theorem `thm:altlaw`. Empty products equal \(1\), not \(p^{-1}\). At \(k=2\) the value \(p^{-1}\) is the prefactor \(p^{-\binom{2}{2}}\). At \(k=3\) the prefactor is \(p^{-\binom{3}{2}}=p^{-3}\). | The sentence now names those prefactors and says both products equal \(1\). Commit `f2c30a41`. | Fixed. |
| SR-16 | `ch12-pseudorandom.tex:217` `ex:v15-12-3` | minor | The display began with an unmatched extra bar, `\lvert\bigl\lvert`. The inequality that was meant is the one in the solution, and it is true: on \(A=\{0,1,2\}\subset\Z/5\Z\) the two sides are \(2/125=0.016\) and \(6\sqrt6/125=0.11757\ldots\). | The stray bar is deleted. Commit `f2c30a41`. | Fixed. |
| SR-17 | `ch12-pseudorandom.tex:213` `ex:v15-12-2` | minor | The count \(5\) is right: \((0,0)\), \((1,0)\), \((2,0)\), \((0,1)\) and \((2,4)\). The write-up said "no other pair works" and did not show it. | If \(d\ne 0\) the three terms are distinct, so they are \(\{0,1,2\}\) in order, and the only orders are \(0,1,2\) and \(2,1,0\). Commit `f2c30a41`. | Fixed. |
| SR-18 | `ra-bias.tex:321` `ex:v15-13-4` | minor | The one-term calculation is correct, and the coefficient \(2\) matches the series in Theorem `thm:rubinsteinsarnak`. The formula for \(J_0\) stands in the paragraph after Corollary `cor:biasdensity`, not before it. The passage from finite products to \(X\) was missing: the partial sums converge almost surely, and bounded convergence passes the characteristic functions to the limit. | The citation names the paragraph after the corollary, and the limit is written out. Commit `f2c30a41`, with the almost-sure citation tightened in `fc17c1a5`. | Fixed. |
| SR-19 | `ch11-values.tex:97` `ex:v15-11-3` | minor | Lemma `lem:kw` assumes distinct primes. Unique factorisation inside its proof is what gives the independence. The hint said that linear independence of \(\log 2\) and \(\log 3\) is the hypothesis of the lemma. The solution's own argument is the right one: \(2^b=3^a\) forces \(a=b=0\). | The hint now says the lemma applies to any distinct primes, and that the irrationality is that unique-factorisation step. Commit `f2c30a41`. | Fixed. |
| SR-20 | `figures/v15c10-arithmetic.tex` `fig:v15c10-arithmetic` | minor | The heights match \(1-p^{-2}\) to three decimals: \(3/4=0.75\), \(8/9=0.889\), \(24/25=0.960\), \(48/49=0.980\). The bar for \(p=7\) ran to \(x=4.8\) while the axis stopped at \(x=4.6\). | The axis now ends at \(x=5.6\), past the last bar. Commit `ef75727f`. | Fixed. |
| SR-21 | `figures/v15c14-interval.tex` `fig:v15c14-interval` | minor | Seven coral dots sit on the segment of length \(h\) and were labelled "primes \(p\le\sqrt h\)". Those primes are the moduli in \(\omega_y\). For large \(x\) and \(\theta\le 2\) they lie below the interval. | The dots are labelled as integers \(n\), and the caption says the primes \(p\le\sqrt h\) lie below the interval. Commit `f2c30a41` for the caption and `ef75727f` for the node. | Fixed. |
| SR-22 | `ch05-short.tex:493` `ex:v15-05-3` | minor | The proof is one cancellation in equation `eq:pairseries` and the substitutions \((3-1)/(3-2)=2\) and \(4/3\). Exercise `ex:v15-05-2` reads the same formula in three cases and is one star. | Lowered from two stars to one. Commit `f2c30a41`. | Fixed. |
| SR-23 | `ch06-sieves.tex:316` `ex:v15-06-4` | minor | The work is the eight-term sum whose value is \(8/30\), and the order-\(0\) bound \(-1/30\). That is a computation. Three stars are reserved for a multi-step proof. Exercises `ex:v15-06-1` and `ex:v15-06-2` are the same kind of count and are one star. | Lowered from three stars to one. Commit `f2c30a41`. | Fixed. |
| SR-24 | `ch08-ranks.tex:207` `ex:v15-08-3` | minor | The solution is the one-line congruence already stated in the chapter: the rank is even, so \(K_n\equiv n\pmod 2\). Exercises `ex:altmean` and `ex:v15-08-1` are one star and longer. | Lowered from two stars to one. Commit `f2c30a41`. | Fixed. |
| SR-25 | `ra-moments.tex:226` `ex:v15-10-3` | minor | The product of \((e^\gamma\log y)^{k^2}\) and \((\log T/(e^\gamma\log y))^{k^2}\) is \((\log T)^{k^2}\), and replacing \(y\) by \(y^2\) multiplies one factor by \(2^{k^2}\) and divides the other by the same power. That is shorter than the one-star exercises `ex:ak` and `ex:v15-10-1`. | Lowered from two stars to one. Commit `f2c30a41`. | Fixed. |

Counts: 0 critical, 9 major, 16 minor. All 25 are fixed on this branch.

The three-star exercises that remain are multi-step proofs: the squarefree count, the empty Cramér windows, the characteristic function of \(v_2\), Gauss's counts, the singular series, the Cohen–Lenstra ratio, the kernel probabilities, the tent's Fourier transform, the generating function for \(a_2\), the logarithmic integral, the \(U^2\) identity, the characteristic function of the race, and the short-interval normal order. They stay at three stars.

## Workflow

`.github/workflows/volume15-rewrite-audit.yml` triggers on `pull_request` only, with `contents: read`, no secrets, and a path filter. It checks out the pull-request head. It does not edit `build.yml` or the publication job. The diff from `60ce0947` does not touch that workflow except by adding the new audit file.

`check_preservation.py` compares formal blocks, exercises, figures, labels, hints and solutions with the frozen commit, and it requires exactly four new exercises and two new figures in each of the fourteen chapters. It passes. `check_figures.py` checks that each of the 28 plates is referenced once; its header says that this is not visual inspection. `check_new_examples.py` recomputes the printed numbers, including the twin-prime tail after SR-11. Its header says that those checks do not certify proofs.

`git diff 60ce0947...HEAD -- volume15-order-and-chance` has no deleted lines. No other volume is in the diff.

## Local build

`./build.sh --pdf-only volume15-order-and-chance` completed.

- `tools/check_book_layout.py`: 381 measured boxes, maximum height \(401.4\,\mathrm{pt}\), no overfull box, no unresolved reference. The log has no `Overfull` line.
- The KDP interior is 333 pages, at the bleed size \(7.125\times 10.25\,\mathrm{in}\). The reading PDF carries the same interior with the front cover attached.
- The 28 new plates were also rendered on their own with `tools/figure.tex` and read against their captions.
- The EPUB was assembled from that interior. `tools/check_epub_media.py` reports 55 plates at 1800 pixels, full width, with formulas on the em baseline.

## Verified correct

Each line is the exercise or figure after the fix above, when a fix applied. Stars below are the corrected stars.

### Exercises

1. `ex:v15-01-1` ★. The \(5\)-smooth integers up to \(40\) number \(21\), and \(\Psi(40,2)=6\).
2. `ex:v15-01-2` ★. \(F(1/4)=1/3\), \(F(1/2)=1/2\), and \(f(1/2)=2/\pi\). This is the distribution function of Theorem `thm:ddt`.
3. `ex:v15-01-3` ★★. The count is \(\lceil\tau(n)/2\rceil\). Equality holds in the probability exactly when \(n\) is not a square. The checks are \(3\) for \(n=12\) and \(5\) for \(n=36\).
4. `ex:v15-01-4` ★★★. \(\sum_{d^2\mid n}\mu(d)=\lvert\mu(n)\rvert\). The tail \(\sum_{d\ge m+1}1/d^2\le 1/m\) with \(m=\lfloor\sqrt x\rfloor\) gives the bound. At \(x=100\) the sum is \(61\), and \(600/\pi^2=60.79\ldots\).
5. `ex:v15-02-1` ★. \(\omega(3/2)=2/3\), \(\omega(2)=1/2\), and \(e^\gamma\omega(2)=0.8905\) from \(e^{-\gamma}=0.56146\).
6. `ex:v15-02-2` ★. For \(x=100\) and \(y=(\log 100)^2\), the sum over \(n=101,\ldots,121\) is \(4.46\), and \(y/\log x=4.61\).
7. `ex:v15-02-3` ★★. \(1-t\le e^{-t}\) and the interval \((x,x+y]\) contains at least \(y-1\) integers, so the limsup is at most \(e^{-1}\).
8. `ex:v15-02-4` ★★★. The expected number of empty windows is \(O(x^{1-\lambda})\). Along \(x=2^k\) the probabilities are summable, so almost surely every large dyadic block is free of empty intervals, and a gap inside the block has length at most \(y_k\).
9. `ex:v15-03-1` ★. The values of \(v_2\) on \(1,\ldots,16\) sum to \(15\), so the average is \(15/16\).
10. `ex:v15-03-2` ★. \(P(V\ge k)=2^{-k}\) and \(P(V=k)=2^{-(k+1)}\). The mean is \(\sum_{k\ge 1}2^{-k}=1\).
11. `ex:v15-03-3` ★★. The three Erdős–Wintner series are \(0\), \(1/2\) and \(1/2\). Against Theorem `thm:tkgeneral`, \(A(x)\to 1\) and \(B(x)^2\to 6\). The factor \(1-1/p\) is in \(A\) and not in \(B^2\).
12. `ex:v15-03-4` ★★★. The power sums at \(r=1/2\) are \(2\) and \(6\). The characteristic function is \(1/(2-e^{it})\), which is the transform of \(P(V=k)=2^{-(k+1)}\).
13. `ex:v15-04-1` ★. For \(n>1\), \(\mathbb E f(p)^k=0\), so \(\mathbb ES(x)=1\).
14. `ex:v15-04-2` ★. \(N_5(2)=10\), \(N_5(3)=40\), and \(125-40=85\).
15. `ex:v15-04-3` ★★. A nontrivial factorisation of a cubic has a factor of degree \(1\), and a root produces such a factor.
16. `ex:v15-04-4` ★★★. The four reducible types total \((2p^3+p)/3\), so \(N_p(3)=(p^3-p)/3\). The quadratic count is \(p(p-1)/2\).
17. `ex:v15-05-1` ★. The partial product through \(p=29\) is \(0.6651\), and the tail factor is \(0.9925\).
18. `ex:v15-05-2` ★. \(\mathfrak S(3)=0\), \(\mathfrak S(4)=\mathfrak S(2)\) and \(\mathfrak S(6)=2\mathfrak S(2)\).
19. `ex:v15-05-3` ★. The ratio is \((p-1)/(p-2)\). The values are \(2\) and \(4/3\).
20. `ex:v15-05-4` ★★★. The local factors and the identity \((p-1)^2-p(p-2)=1\) give equation `eq:pairseries`.
21. `ex:v15-06-1` ★. The count is \(100-50-33+16=33\), and \(100/\log 4+16=88.13\).
22. `ex:v15-06-2` ★. \(\sum_{p<11}1/p=247/210>1\), and \(W(11)=8/35\).
23. `ex:v15-06-3` ★★. \(\sigma(A+A)\ge 2\sigma-\sigma^2\), and \(2\sigma-\sigma^2-\sigma=\sigma(1-\sigma)>0\) when \(0<\sigma<1\).
24. `ex:v15-06-4` ★. The numerator is \(8\), so the proportion is \(8/30\). The order-\(0\) lower bound is \(-1/30\).
25. `ex:v15-07-1` ★. \(\prod_{i=1}^6(1-3^{-i})=0.5605\), and the infinite product at \(p=3\) rounds to \(0.5601\).
26. `ex:v15-07-2` ★. \(\lvert\mathrm{Aut}(\Z/9)\rvert=6\), \(\lvert GL_2(\mathbb F_3)\rvert=48\), and the ratio is \(8\).
27. `ex:v15-07-3` ★★. \(\log(1-u)+2u\ge 0\) on \((0,1/2]\), so the series for \(\log c_\infty\) converges and \(c_\infty>0\).
28. `ex:v15-07-4` ★★★. \(\lvert GL_2(\mathbb F_p)\rvert=(p^2-1)(p^2-p)\) and the ratio to \(\varphi(p^2)\) is \(p^2-1\).
29. `ex:v15-08-1` ★. For \(p=5\), \(K_1=1\), \(P(K_2=0)=4/5\) and \(P(K_2=2)=1/5\).
30. `ex:v15-08-2` ★. At \(p=3\), \(\mathbb E\,p^K=4\) and \(\mathbb E\,p^{2K}=40\).
31. `ex:v15-08-3` ★. The rank is even, so \(K_n\equiv n\pmod 2\).
32. `ex:v15-08-4` ★★★. The chain gives \(1-1/p\), \(1/p\), \(p^{-3}\) and \(1-p^{-3}\), and Theorem `thm:altlaw` gives the same four values.
33. `ex:v15-09-1` ★. \(\hat K(0)=1\), \(\hat K(1/2)=1/2\) and \(\hat K(1)=0\).
34. `ex:v15-09-2` ★. \(p_2(1)=(32/\pi^2)e^{-4/\pi}=0.9076\ldots\), which is \(0.908\) to three decimals, against \(e^{-1}=0.368\).
35. `ex:v15-09-3` ★★. The overlap of two unit intervals is \((1-\lvert\alpha\rvert)_+\).
36. `ex:v15-09-4` ★★★. In the series convention \(\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}\,dx\), integration by parts turns the tent into \((\sin(\pi u)/(\pi u))^2\).
37. `ex:v15-10-1` ★. At \(u=1/2\), \((1/2)^4\cdot(1+u)/(1-u)^3=3/4\), which is the local factor \(1-2^{-2}\).
38. `ex:v15-10-2` ★. \((e^\gamma\log 10)^4=282.9\) from the printed inputs \(1.78107\) and \(2.302585\).
39. `ex:v15-10-3` ★. The powers of \(\log y\) cancel, and the change \(y\mapsto y^2\) multiplies one factor by \(2^{k^2}\) and divides the other by the same power.
40. `ex:v15-10-4` ★★★. The differentiated geometric series is \((1+u)/(1-u)^3\). The local factor is \(1-p^{-2}\), so \(a_2=6/\pi^2\), and \((6/\pi^2)\cdot(1/12)=1/(2\pi^2)\).
41. `ex:v15-11-1` ★. \(\pi^2/6=1.64493\) and \(\pi^2/15=0.65797\) to five decimals.
42. `ex:v15-11-2` ★. The corrected limit: the proportion with \(\lvert\zeta\rvert\le c\) tends to \(1/2\) for every fixed \(c>0\).
43. `ex:v15-11-3` ★★. \(2^b=3^a\) forces \(a=b=0\), so Lemma `lem:kw` applies to the primes \(2\) and \(3\).
44. `ex:v15-11-4` ★★★. The corrected integral: \(\int\tfrac12\log((a^2+u^2)/(b^2+u^2))\,du=\pi(\lvert a\rvert-\lvert b\rvert)\).
45. `ex:v15-12-1` ★. The character \(e(x/5)\) has \(\hat f(1)=1\) and the other coefficients \(0\), so \(\lVert f\rVert_{U^2}=1\).
46. `ex:v15-12-2` ★. Five pairs, so \(\Lambda_3=1/5\) and \(\delta^3=27/125=0.216\).
47. `ex:v15-12-3` ★★. Parseval gives the exponent \(3/2\). The two sides on this set are \(0.016\) and \(0.118\).
48. `ex:v15-12-4` ★★★. Fourier inversion gives \(\langle\tau_h f,f\rangle=\sum\lvert\hat f\rvert^2 e(h\xi/N)\), and Parseval in \(h\) is the \(U^2\) identity.
49. `ex:v15-13-1` ★. From \(\gamma=6.0209\), \(2/\lvert\rho\rvert=0.3310\) to four decimals.
50. `ex:v15-13-2` ★. For \(V=0.1556\), \(1-V/2=0.9222\).
51. `ex:v15-13-3` ★★. Symmetry and the lack of an atom give \(P(X>1)=1/2\). Full support gives \(P(X>0)>1/2\).
52. `ex:v15-13-4` ★★★. \(\mathbb E e^{i\xi X}=e^{i\xi}\prod_{\gamma>0}J_0(2\xi/\lvert\rho\rvert)\), with the partial-sum limit filled in.
53. `ex:v15-14-1` ★. \(e^\gamma/2=0.8905\) and \(2e^{-\gamma}-1=0.1229\), which is the ledger's \(12\%\).
54. `ex:v15-14-2` ★. On \(101,\ldots,120\), with \(\mu_4=5/6\), the sum of squares is \(95/9\), under the bound \(110/3\).
55. `ex:v15-14-3` ★★. If \(y\le\sqrt h\), the average of \((\omega_y-\mu_y)^2\) is at most \(\mu_y+5\). At \(y=10\) that is at most \(6.18\).
56. `ex:v15-14-4` ★★★. The corrected \(O_\theta(1)\) bound on \(\omega-\omega_y\), then Chebyshev and Volume 6, Theorem 1.5.

### Figures

Each plate was rendered and compared with its caption and with the exercise it illustrates. The file `v15cNN` belongs to chapter \(N\) in `main.tex`.

1. `v15c01-smooth`. Coral dots on \(1,\ldots,20\) are exactly the \(5\)-smooth integers.
2. `v15c01-arcsine`. The ordinates match \(1/(\pi\sqrt{t(1-t)})\), and the dashed line is the median \(t=1/2\).
3. `v15c02-buchstab`. The graph is \(1/u\) on \([1,2]\) and \((1+\log(u-1))/u\) on \([2,3]\), against the line \(e^{-\gamma}\).
4. `v15c02-gaps`. A schematic Maier matrix: rows are short intervals, and the marked columns are the residue classes prime to \(P\).
5. `v15c03-valuation`. The bars are \(1/2\), \(1/4\), \(1/8\), \(1/16\) and \(1/32\).
6. `v15c03-gaussian`. The ordinates match the standard Gaussian density \(\Phi'\).
7. `v15c04-phases`. After SR-01, \(f(15)\) is the product of \(f(3)\) and \(f(5)\).
8. `v15c04-cubics`. The three bars are \(125\), \(85\) and \(40\).
9. `v15c05-series`. After SR-12, \(\mathfrak S(6)\) is twice \(\mathfrak S(2)=\mathfrak S(4)\), and the axis clears the tall bar.
10. `v15c05-patterns`. \((0,2,4)\) meets \(0\bmod 3\). \((0,2,6)\) does not cover every class.
11. `v15c06-bonferroni`. The negative bar is \(-1/30\) and the positive bar is \(8/30\).
12. `v15c06-factor`. The picture is the factor \(2\) in the Selberg upper bound, set against \(x/\log x\).
13. `v15c07-auts`. After SR-08, the labels are \(6\) and \(\lvert\mathrm{Aut}((\Z/3)^2)\rvert=48\).
14. `v15c07-product`. The six ordinates are the partial products, falling toward the line \(0.5601\).
15. `v15c08-chain`. The arrows are the transitions of Lemma `lem:altchain`: up with probability \(p^{-k}\), down with probability \(1-p^{-k}\).
16. `v15c08-parity`. Even \(n\) has even \(K_n\), and odd \(n\) has odd \(K_n\).
17. `v15c09-tent`. The tent is \(\hat K(\alpha)=(1-\lvert\alpha\rvert)_+\), as the caption says.
18. `v15c09-surmise`. The samples match \(p_2(s)\) and \(e^{-s}\) to three decimals, and \(p_2(0)=0\).
19. `v15c10-split`. The moment splits into the arithmetic factor and the matrix factor, leaving \((\log T)^{k^2}\).
20. `v15c10-arithmetic`. After SR-20, the four bars \(1-p^{-2}\) sit inside the axis.
21. `v15c11-euler`. Three factors \(1-p^{-\sigma}X_p\), drawn as vectors of decreasing length.
22. `v15c11-bell`. After SR-03, the dashed line is the centre \(a=0\) of the standard Gaussian.
23. `v15c12-cycle`. Translation by \(1\) on \(\Z/5\Z\).
24. `v15c12-progression`. The set \(\{0,1,2\}\) inside \(\Z/5\Z\), with the progression of difference \(1\).
25. `v15c13-wave`. After SR-07, the curve is \(1+2\cos(\gamma u)/\lvert\rho\rvert\) in radians, and it stays positive.
26. `v15c13-symmetry`. After SR-06, the law is a narrow bump about \(1\), with a thin tail to the left of \(0\).
27. `v15c14-ledger`. Bulk agreement on one side, and Maier, the bias and Buchstab on the other.
28. `v15c14-interval`. After SR-21, the coral dots are integers in an interval of length \(h=x^\theta\).

## Not checked

- A fresh derivation of the pre-existing theorems, examples and exercises. The diff does not change them.
- Historical dates and citations in that pre-existing prose.
- Upload of the print file to KDP, and KDP's own acceptance of it.
- An external mathematical referee. This review is the independent second reading the pull request asked for. It is not a journal report.
- The HTML reader. The local build used `--pdf-only` and then a separate EPUB assembly from the same interior. The reader step in `build.sh` was not run.

## Verdict

The twenty-five defects above are fixed. The 56 exercises and 28 figures are the mathematics this pull request adds, and they are ready to merge. The audit workflow is read-only and does not change the publication build.
