# Second review of PR #251

Independent review of the Volume 14 additions on `cursor/volume14-complete-rewrite`, against base `60ce094742a84e3da028ad2c9d31d535db656344`. The reviewer is not the author of the pull request.

Scope: the 56 new exercises with their hints and solutions, the 28 new TikZ figures, preservation of the original manuscript, and the audit workflow. Every numerical claim in the new solutions was recomputed in Python, separately from the proofs. The new prose was read against the series voice.

## Issues

| ID | Place | Severity | Evidence | Fix | Verdict |
| --- | --- | --- | --- | --- | --- |
| SR-01 | `ch01-zeros.tex:511` `ex:v14-extra-01-4` | major | The contribution of the zeros with \(\beta\le\sigma_0\) is \(\ll h\,T\log T\cdot x^{\sigma_0-1}\). The write-up then said “\(T\le x\), so this is \(\ll x^{\sigma_0-\theta}(\log x)^4\)”. From \(T\le x\) alone the factor is \(\ll x^{\sigma_0}\log x\), which does not tend to \(0\). The height chosen two paragraphs earlier is \(T=x^{1-\theta}(\log x)^3\). | The estimate now substitutes that height. Commit `a5f94543`. | Fixed. |
| SR-02 | `ch02-siegel.tex:514` `ex:v14-extra-02-4` | major | The partial sum of \(\chi_4\) through \(19\) is \(11064338/14549535\approx0.76046\), so it does lie in \((0.76,0.77)\). The written lower comparison was \(0.666+0.057+0.020+0.010+0.006=0.759\), and the solution claimed \(0.759>0.76\). | The five terms are now bounded below by \(0.6666\), \(0.05714\), \(0.02020\), \(0.01025\) and \(0.00619\), which add to \(0.76038\). Each comparison is a cross-multiplication. Commit `0e7a35a5`. | Fixed. |
| SR-03 | `ch04-largesieve.tex:507` `ex:v14-extra-04-3` | major | With \(U=3\) and \(V=2\), the solution correctly computed \(a_3(6)=-\log2\). The closing sentence then said that in both examples the only nonzero piece is \(a_2\). The triple \((2,3,1)\) has \(bc=6>U\), so that term of \(a_3\) is type II. | The write-up now separates the type I and type II terms of \(a_3(6)\). Commit `ecd3103f`. | Fixed. |
| SR-04 | `three-primes.tex:271` `ex:v14-extra-07-4` | major | \(\mathfrak S(9)\) does lie in \((1.533,1.536)\), and the stopped product through \(p=19\) is \(116678301197166709/76084057158451200\approx1.53354468\). The displayed chain equated each rounded 8-place number with the product of the previous rounded number and the next factor. Those equalities are not exact: \(1.53290753\cdot(1+1/4096)\) rounds to \(1.53328178\), not to the printed \(1.53328177\). The tail bound \(e^y<1+y+y^2\) and the products \(1.5336\cdot1.00155<1.536\) were asserted without a calculation. | The solution multiplies the rational factors, reduces, and compares the fraction with \(1.5335\) and \(1.5336\) by the two positive differences \(33995446817938000\) and \(42088610340513200\). The tail is \(\lt\exp(1/648)\), and \(e^y<1+y+y^2\) for \(0<y\le1\) is proved from \(k!\ge2^{k-1}\). Commit `4e9e2d20`. | Fixed. |
| SR-05 | `ch08-gpy.tex:461` `ex:v14-extra-08-4` | major | Lemma `lem:gpyprinciple` needs \(S_2>\rho S_1\). The solution’s counterexample to the non-strict form set one weight to \(1\) at an integer with exactly two primes and claimed that no integer has three primes in the tuple. Nothing in that sentence stopped some other integer from having three. | The tuple is now \(\{0,2\}\). Zero weights already give \(S_2=\rho S_1\) with \(\rho=2\), and a two-element tuple never contains three primes. A single positive weight at a twin prime in the sum gives the same equality with \(S_1>0\). Commit `8f4836b5`. | Fixed. |
| SR-06 | `ch12-roth.tex:229` `ex:v14-extra-12-4` | critical | The exercise asked for a proof that \(|x|=|z|\) and \(x+z=2y\) force \(x=z=y\). That implication is false: \(x=(1,0)\), \(z=(-1,0)\), \(y=0\). The solution’s first paragraph added the missing hypothesis \(|y|=|x|\) and then, in the Behrend paragraph, invoked “the previous paragraph” without checking it. On one sphere the proof of Theorem `thm:behrend` does have \(|x|=|y|=|z|\). | The statement, the hint and the solution now take \(|x|=|y|=|z|\) as the hypothesis, and the digit paragraph cites \(S_k\). Commit `332e26fa`. | Fixed. |
| SR-07 | `ch05-expsums.tex:456` `ex:v14-extra-05-3` | minor | The four values \(K(1),\ldots,K(4)\) and the sum of squares \(19\) are correct. The sentence \(c_1^2=2+c_2\) did not record the double-angle formula, and the positive root of \(c^2+c-1=0\) was chosen without using \(0<2\pi/5<\pi/2\). “Inside both bounds” was not calculated. | The double-angle step, the sign of \(c_1\), and the comparisons \(1+\sqrt5<2\sqrt5\) and \((1+\sqrt5)^4=56+24\sqrt5<250\) are now written. Commit `623b1032`. | Fixed. |
| SR-08 | `ch05-expsums.tex:475` `ex:v14-extra-05-4` | minor | The orthogonality gives \(p(p-1)\). The solution then used \(K(0)=-1\) without the reason. The sum of all \(p\)-th roots of unity is \(0\), and the term at \(x=0\) is \(1\). | That line is now in the write-up. Commit `623b1032`. | Fixed. |
| SR-09 | `waring.tex:395` `ex:v14-extra-06-1` | minor | \(\Gamma(3/2)^5/\Gamma(5/2)=\pi^2/24\) is correct. The inputs \(\Gamma(1/2)=\sqrt\pi\) and \(\Gamma(x+1)=x\Gamma(x)\) are Volume 5, Propositions 5.12 and 5.2. | The solution cites those two propositions. Commit `7e3e5d6c`. | Fixed. |
| SR-10 | `waring.tex:404` `ex:v14-extra-06-2` | minor | At \(\beta=1/25\), \(2|\beta|^{-1/2}=10=P\). The minimum is \(10\). The sentence said that \(P\) is the smaller bound. | The sentence now says the two arguments are equal. Commit `7e3e5d6c`. | Fixed. |
| SR-11 | `waring.tex:430` `ex:v14-extra-06-4` | minor | The bound \(|v(\beta)|\le(1+1/(2\pi))|\beta|^{-1/2}\) is the right conclusion, and it is smaller than the lemma’s \(2\). The integral for \(E(t)\) was quoted as \(\le1/(\pi|\beta|)\) without the factor \(2\pi\), and the last sentence attributed the constant \(1+2/(k\pi)\) to this argument. That constant is what the lemma’s coarser tail \(2g(U)/(\pi|\beta|)\) produces. | The factor \(2\pi\) is written, and the coarser tail is named as the lemma’s. Commit `7e3e5d6c`. | Fixed. |
| SR-12 | `ch03-sieves.tex:602` `ex:v14-extra-03-1` | minor | \(e^\gamma/2\) is the ratio of \(\Phi(x,\sqrt x)\sim x/\log x\) to the sieve main term \(2e^{-\gamma}x/\log x\). The idea line said the prediction is too large by \(e^\gamma/2\). That factor is about \(0.8905\), so it is the ratio of the count to the prediction. | The idea line now says that. Commit `b37d0bdf`. | Fixed. |
| SR-13 | `figures/v14c10-distance.tex` `fig:v14-extra-10-a` | minor | The partial sums of \(2/p\) through \(p=19\), rounded to two decimals, are \(1.00,1.67,2.07,2.35,2.53,2.69,2.81,2.91\). The seventh vertex, the sum through \(17\), was drawn at height \(2.80\). The labelled endpoint \(2.91\) and the line \(2\log\log20\) were already right. | The vertex is at \(2.81\). Commit `5c5bab02`. | Fixed. |
| SR-14 | `ch02-siegel.tex:371` `ex:v14-extra-02-4` | minor | Proving \(|L(1,\chi)|\le2+\log q\) repeats Lemma `lem:lsize`(b), and the new arithmetic is the partial sum. The chapter’s three-star exercise is the exceptional-zero bias. | Lowered from three stars to two. Commit `0e7a35a5`. | Fixed. |
| SR-15 | `ch04-largesieve.tex:359` `ex:v14-extra-04-4` | minor | The product bound is the estimate already proved in Lemma `lem:phisum`, plus the partial product through \(19\). The chapter’s three-star exercise is the Titchmarsh divisor problem. | Lowered from three stars to two. Commit `ecd3103f`. | Fixed. |
| SR-16 | `ch05-expsums.tex:316` `ex:v14-extra-05-4` | minor | The identity is the second-moment paragraph of Lemma `lem:klmoments`. The chapter’s three-star exercise is the exponential sum for \(\mu\). | Lowered from three stars to two. Commit `623b1032`. | Fixed. |
| SR-17 | `waring.tex:320` `ex:v14-extra-06-3` | minor | The four saved exponents are the four expressions in the proof, evaluated at the given \(k,s,\nu,\varepsilon\). That is the same kind of substitution as the one-star exercise `ex:v14-extra-06-2`. | Lowered from two stars to one. Commit `7e3e5d6c`. | Fixed. |
| SR-18 | `three-primes.tex:152` `ex:v14-extra-07-3` | minor | The identity is the expansion of \(\binom{N-1}{2}\). The chapter’s one-star exercise `ex:sing3` is the Euler product for \(\mathfrak S(N)\). | Lowered from two stars to one. Commit `4e9e2d20`. | Fixed. |

Counts: 1 critical, 5 major, 12 minor. All 18 are fixed on this branch.

## Preservation

`git diff 60ce0947...HEAD --numstat` has no deletions outside the corrected lines of these new exercises and of `v14c10-distance.tex`. No file outside `volume14-primes/`, `review/volume14-complete-rewrite/` and `.github/workflows/volume14-rewrite-audit.yml` changes. No other volume changes. `check_preservation.py --final` passes: each chapter still has its original formal blocks, exercises, figures, labels, hints and solutions, and each chapter has exactly four new exercises and two new figures.

## Workflow

`.github/workflows/volume14-rewrite-audit.yml` triggers on `pull_request` only, with `contents: read`, no secrets, and a path filter. It checks out the pull-request head. It does not edit `build.yml` or the publication job.

`check_preservation.py` compares formal blocks, exercises, figures, labels, hints and solutions with the frozen commit. `check_figures.py` checks that each of the 28 plates is referenced once; its last line says that rendered inspection is still required. `check_new_examples.py` recomputes selected numbers. Its header says that those checks do not certify proofs. SR-02 and SR-04 were claims whose true values the script already accepted; the script did not check the written decimal comparisons that failed. The triangle test in `test_ch12_roth_and_behrend` only checks the case \(x=z\). It did not lock the false implication in SR-06.

## Local build

`./build.sh volume14-primes` exited 0 on this head.

- `tools/check_book_layout.py`: 329 whole boxes, maximum height \(304.8\,\mathrm{pt}\), no overflow, no unresolved reference. The log of `main.tex` has no Overfull box.
- The reading PDF is the cover plus the interior. The print interior is 275 pages, spine \(0.6478\,\mathrm{in}\). KDP preflight reports PDF 1.3 with one page flattened at 600 ppi.
- EPUB: 53 plates at 1800 px, full text width, formulas on the em baseline. Pandoc warned on two pre-existing `\qedhere` tokens in the Waring chapter; the build still completed.
- The same run wrote `dist/html/volume14-primes/`.

The 28 new plates were also rendered on their own and read against their captions.

## Verified correct

Each line is the exercise or figure after the fix above, when a fix applied. Stars below are the corrected stars.

### Exercises

1. `ex:v14-extra-01-1` ★. At \(\sigma=2/3\), Carlson’s exponent is \(8/9\). At \(\delta=1/6\), the Bohr–Landau exponent is \(17/18\).
2. `ex:v14-extra-01-2` ★. At \(x=10^4\) the fraction is \(0.01\) on the critical line and \(10^{-2/5}\approx0.398107\) at \(\beta=9/10\).
3. `ex:v14-extra-01-3` ★★. Ingham’s theorem with slope \(3\) gives every \(\theta>2/3\). On \((3/4,1)\), \(4\sigma(1-\sigma)-3(1-\sigma)=(1-\sigma)(4\sigma-3)>0\).
4. `ex:v14-extra-01-4` ★★★. The corrected height \(T=x^{1-\theta}(\log x)^3\) makes the zero sum \(o(h)\) for every fixed \(\theta>\sigma_0\). Vinogradov–Korobov does not freeze a half-plane, and the endpoint \(\theta=\sigma_0\) leaves \((\log x)^4\).
5. `ex:v14-extra-02-1` ★. \(3+4\cos\varphi+\cos2\varphi=2(1+\cos\varphi)^2\), with values \(8,2,1/2,0\).
6. `ex:v14-extra-02-2` ★. The class-number bound is \(<3.33\) at \(p=7\) and \(>28.8\) at \(p=163\), while \(h(-p)=1\).
7. `ex:v14-extra-02-3` ★★. Two real zeros past \(1-\kappa'/\log Q\) give \(1.6\) against \(1.5\). The factor \(1/2\) in Corollary `cor:page` is \(\log(Q^2)=2\log Q\).
8. `ex:v14-extra-02-4` ★★. \(|L(1,\chi)|\le2+\log q\) by the partial period, and the character sum modulo \(4\) through \(19\) lies in \((0.76,0.77)\).
9. `ex:v14-extra-03-1` ★. With \(0.57721<\gamma<0.57722\), one has \(0.89053<e^\gamma/2<0.89055\).
10. `ex:v14-extra-03-2` ★. The identity holds, and the product through \(p=7\) is \(175/256\).
11. `ex:v14-extra-03-3` ★★. At level \(\sqrt x\) the even list keeps \(1\) and the odd list keeps the primes in \((\sqrt x,x]\). The two lists share the main term \(x/(2d)\).
12. `ex:v14-extra-03-4` ★★★. The tail after \(q=100\) is \(>0.99\), and \(0.3746<P<0.3747\) puts the printed Artin decimal between \(0.99P\) and \(P\).
13. `ex:v14-extra-04-1` ★. \(\sum_{r\le10}1/\varphi(r)=55/12<e(1+\log10)\).
14. `ex:v14-extra-04-2` ★. At \(x=e^{60}\) and \(A=1\), \(3<e^{30}/60^7<4\).
15. `ex:v14-extra-04-3` ★★. Vaughan’s identity holds at \(n=4\) and \(n=6\). The type II term at \(n=6\) is the triple \((2,3,1)\).
16. `ex:v14-extra-04-4` ★★. The telescoping sum is \(1\), so the prime product is at most \(e\). The product through \(19\) is \(4198170109/2182963200>1.92\).
17. `ex:v14-extra-05-1` ★. The squares modulo \(5\) are \(0,1,4\), so \(S(1,2;5)=S(1,3;5)=0\).
18. `ex:v14-extra-05-2` ★. The moment bound is smaller than Weil’s exactly for \(p<8\). At \(p=5\) the moments are \(19\) and \(159\).
19. `ex:v14-extra-05-3` ★★. The four Kloosterman sums modulo \(5\) are \((3-\sqrt5)/2\), \(-(1+\sqrt5)\), \(\sqrt5-1\) and \((3+\sqrt5)/2\). Their squares sum to \(19\), and \(1+\sqrt5\) lies under both bounds.
20. `ex:v14-extra-05-4` ★★. Orthogonality gives \(\sum_{n=1}^{p-1}K(n)^2=p^2-p-1\). At \(p=5\) this is \(19\).
21. `ex:v14-extra-06-1` ★. \(\Gamma(3/2)^5/\Gamma(5/2)=\pi^2/24\), from Volume 5, Propositions 5.2 and 5.12.
22. `ex:v14-extra-06-2` ★. The minimum is \(2\) at \(\beta=1\) and \(10\) at \(\beta=1/25\), where the two arguments are equal.
23. `ex:v14-extra-06-3` ★. At \(k=2\), \(s=5\), \(\nu=1/10\) and \(\varepsilon=0\) the four exponents are \(1/20\), \(1/2\), \(3/20\) and \(1/20\).
24. `ex:v14-extra-06-4` ★★★. \(|v(\beta)|\le(1+1/(2\pi))|\beta|^{-1/2}\), which is smaller than the lemma’s constant \(2\). The lemma’s coarser tail produces \(1+2/(k\pi)\).
25. `ex:v14-extra-07-1` ★. \(c_6(15)=-2\), also as \(c_2(15)c_3(15)\). The factor at \(p=2\) vanishes for even \(N\).
26. `ex:v14-extra-07-2` ★. \(\binom{9}{2}=36\) and \(N^2/2=50\).
27. `ex:v14-extra-07-3` ★. \(\binom{N-1}{2}=N^2/2-3N/2+1\).
28. `ex:v14-extra-07-4` ★★★. The stopped product is the fraction above, and the tail is \(<1.00155\), so \(1.533<\mathfrak S(9)<1.536\).
29. `ex:v14-extra-08-1` ★. \(\{0,2,4\}\) covers every class modulo \(3\). \(\{0,2,6\}\) does not, and it is admissible.
30. `ex:v14-extra-08-2` ★. The twin factors at \(2\) and \(3\) are \(2\) and \(3/4\).
31. `ex:v14-extra-08-3` ★★. The \(k\) primes just larger than \(k\) are admissible. The diameters are \(12\) and \(32\).
32. `ex:v14-extra-08-4` ★★★. The corrected equality on \(\{0,2\}\) shows why Lemma `lem:gpyprinciple` needs a strict inequality.
33. `ex:v14-extra-09-1` ★. \(1417255-2\cdot708216=823\), and \(0.002\cdot708216>823\), so the ratio lies in \((2,2.002)\).
34. `ex:v14-extra-09-2` ★. \(V=1+7\cdot39=274\) and \(5167-587=4580\).
35. `ex:v14-extra-09-3` ★★. \(\{0,2,6,8,12\}\) is admissible, and two primes in one translate differ by at most \(12\).
36. `ex:v14-extra-09-4` ★★★. The integrals are \(L\) and \(\gamma\). With \(\log274>5.613\), one gets \(L^2/\gamma>4.5\). The simplex factor in Proposition `prop:mk582` is still required before \(M_{582}>4\).
37. `ex:v14-extra-10-1` ★. The derivative of \((1+m)e^{-m}\) is \(-me^{-m}\le0\). The values are \(1\), \(2/e\) and \(3/e^2\).
38. `ex:v14-extra-10-2` ★. \(\sum_{p\le20}2/p\) lies in \((2.9,3)\), and \(2\log\log20\) lies in \((2.1,2.2)\).
39. `ex:v14-extra-10-3` ★★. On the unit circle, \(1-\operatorname{Re}(f\overline g)=|f-g|^2/2\). For \(\mu\) and \(1\) this is \(\sum 2/p\).
40. `ex:v14-extra-10-4` ★★★. \(1-\cos y\le y^2/2\), and Lemma `lem:dist`(c) then bounds the distance by \(|t|\log x\).
41. `ex:v14-extra-11-1` ★. \(A+A\) has six elements and \(A\cdot A\) has five. Since \(\sqrt3<2\), \(9\sqrt3/64<30\).
42. `ex:v14-extra-11-2` ★. \(|A+A|=8=2|A|\), so Plünnecke gives \(|2A-2A|\le64\).
43. `ex:v14-extra-11-3` ★★. \(|A-A|=7\) and \(21\le36\), which is Ruzsa’s inequality on \(\{1,2,4\}\).
44. `ex:v14-extra-11-4` ★★★. The incidence split yields \(N\ge n^{5/2}/64\), and \(16^{3/2}=64\).
45. `ex:v14-extra-12-1` ★. \(\{1,2,4,5\}\) has no \(3\)-term progression. \(\{1,2,3,4,5\}\) does.
46. `ex:v14-extra-12-2` ★. \(500/\log\log(10^6)>185>1\), so Theorem `thm:roth` does not cut \([10^6]\) down.
47. `ex:v14-extra-12-3` ★★. The images \(1,8,15\) are a progression, and their squared lengths \(0,2,8\) lie on three different circles.
48. `ex:v14-extra-12-4` ★★★. Equal lengths and \(x+z=2y\) give \(x=z=y\). Base \(2d\) has no carry, and one sphere supplies the equal lengths.
49. `ex:v14-extra-13-1` ★. The indicator of \(\{0\}\) modulo \(5\) has \(U^2\) norm \(5^{-3/4}\), between \(1/5\) and \(5^{-1/2}\).
50. `ex:v14-extra-13-2` ★. \(\varphi(6)=2\) and \(\varphi(30)=8\).
51. `ex:v14-extra-13-3` ★★. Lemma `lem:wtrick` at \(W=6\), \(b=1\) gives \(\sum_{n\le N}\Lambda(6n+1)\sim3N\).
52. `ex:v14-extra-13-4` ★★★. A linear phase has \(U^1\) norm \(0\). For \(k\ge2\) every coefficient in the cube is a factor \((1-1)\), so the \(U^k\) norm is \(1\).
53. `ex:v14-extra-14-1` ★. \(H_{10}=7381/2520\), and Proposition `prop:meansqpoly` allows an error of \(160\).
54. `ex:v14-extra-14-2` ★. \(\cos(\pi/8)=\sqrt{2+\sqrt2}/2\). The moment limits alternate in sign.
55. `ex:v14-extra-14-3` ★★. For two terms the oscillatory integral is at most \(\sqrt2/\log2<2.05<3\), inside the allowance \(32\).
56. `ex:v14-extra-14-4` ★★★. \(\log(N+1)\le H_N\le1+\log N\), so the length-\(T\) polynomial has mean square \(T\log T+O(T)\).

### Figures

Each plate was rendered and compared with its caption and with the exercise or paragraph it illustrates. The file `v14cNN` belongs to chapter \(N\) in `main.tex`.

1. `v14c01-cost`. The polyline is \(x^{\beta-1}\) at \(x=10^4\), from \(0.01\) at \(\beta=1/2\) to \(1\) at \(\beta=1\), with \(0.398\) marked at \(\beta=9/10\).
2. `v14c01-theta`. The solid bars start at \(3/4\), \(5/8\), \(7/12\) and \(17/30\). The dashed mark is at \(0.525\).
3. `v14c02-trig`. The graph of \(2(1+\cos\varphi)^2\) on \([0,\pi]\), marked \(8,2,1/2,0\).
4. `v14c02-class`. The six bounds are about \(3.32,4.64,6.86,12.0,16.2,28.8\), all above the line \(h=1\). The computed values are \(3.323,4.643,6.860,12.025,16.166,28.828\).
5. `v14c03-parity`. Liouville’s sign on \(1\le n\le24\). Every prime is coral and \(1\) is blue.
6. `v14c03-artin`. On \([0.370,0.376]\), the order is \(0.99P\), then Artin’s constant, then \(P\).
7. `v14c04-product`. The partial products through \(p=19\) end at \(1.923\), under the line \(e\).
8. `v14c04-level`. On a logarithmic axis, \(Q<4\) sits near \(10^{0.6}\) and \(\sqrt x\) sits at the \(10^{13}\) end. The caption states \(\sqrt x>10^{13}\).
9. `v14c05-kloosterman`. \(K(2),K(1),K(3),K(4)\) sit at their exact positions inside \(\pm2\sqrt5\), with the moment bound dashed.
10. `v14c05-bounds`. At \(p=5\) the moment bar is shorter than Weil’s. At \(p=11\) it is taller.
11. `v14c06-gamma`. The heights are \(0.411\), \(3.290\) and \(11.103\), labelled \(0.41\), \(3.29\) and \(11.1\).
12. `v14c06-arcs`. A schematic circle with heavy arcs at \(0\) and at \(1/2\). The caption says the widths are not \(P^{\nu-k}\).
13. `v14c07-local`. The factor at \(p=2\) is \(0\) for even \(N\) and \(2\) for odd \(N\).
14. `v14c07-count`. The bar heights are \(2.301,1.534,1.416,1.370\). A product through the primes up to \(5000\) gives \(2.301,1.534,1.416,1.370\).
15. `v14c08-admissible`. \(\{0,2,4\}\) fills every class modulo \(3\). \(\{0,2,6\}\) leaves the class \(1\) empty.
16. `v14c08-diameter`. The intervals are \(19-7=12\) and \(43-11=32\).
17. `v14c09-simplex`. The triangle \(t_1+t_2\le1\), labelled \(\mathcal R_2\).
18. `v14c09-ratio`. The point \(2.00116\ldots\) lies just above the line \(2\), and \(2\log2\) lies below it.
19. `v14c10-distance`. The partial sums of \(2/p\) end at \(2.91\), above \(2\log\log20\). The vertex through \(p=17\) is at \(2.81\), after SR-13.
20. `v14c10-decay`. The three points are \(1\), \(2/e\) and \(3/e^2\), in descending order.
21. `v14c11-sets`. Six sums \(\{2,3,4,5,6,8\}\) and five products \(\{1,2,4,8,16\}\).
22. `v14c11-line`. The line \(y=2(x-1)\) through \((2,2)\), \((3,4)\) and \((5,8)\).
23. `v14c12-spheres`. The diagonal of the \(3\times3\) grid, labelled \(1,8,15\).
24. `v14c12-bound`. On a \(\log_{10}\) axis the length \(2.28\) is \(\log_{10}190\), set against a stub at \(\log_{10}1=0\).
25. `v14c13-phase`. The four signs on the \(U^2\) square are \(+, -, -, +\), which is \((-1)^{|\omega|}\).
26. `v14c13-wtrick`. The cells \(1,7,13,19,25\) are the integers congruent to \(1\) modulo \(6\).
27. `v14c14-moments`. The four bars have heights \(2.902,-0.726,0.181,-0.045\), which is \((-1)^n\pi\cos(\pi/8)/4^n\).
28. `v14c14-pair`. At \(T=e^4\) the curve \(T^{-2\alpha}\log T\) passes through \(4,0.541,0.073,0.010,0.001\). It is below the line \(\alpha\) at \(\alpha=1/2\).

## Not checked

- A fresh derivation of the pre-existing theorems, examples and exercises. The diff does not change them.
- Historical dates and citations in that pre-existing prose.
- Upload of the print file to KDP, and KDP’s own acceptance of it.
- A page-by-page reading of the generated HTML reader. `build.sh` did write `dist/html/volume14-primes/`.

## Voice

The new exercises, hints, solutions and captions were read against the series voice. They use the same `\idea` / `\writeup` pattern as the older solutions in these chapters. SR-12 was the one sentence that said something other than the ratio it had just computed. No stock opener, hollow intensifier, or template summary remains in the new prose.

## Verdict

The eighteen defects above are fixed. The 56 exercises and 28 figures are the mathematics this pull request adds, and the local PDF and EPUB build is clean. The audit workflow is read-only and does not change the publication build. The branch is ready to merge once CI on the final head is green.
