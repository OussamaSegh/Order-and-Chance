# Volume 15 fix, second review — 22 November 2026

Independent reading of PR #268. The fixes were written by another agent. The head under review was `4b4e60c2dd11b28a58447bf24c15ad50cd1fb452`. This reading found two gaps in the new text. They are repaired in `ab5d383f39a7f44a4dc75a69cdb49d3bfdbda57d`. This log is the following commit on `cursor/fix-volume15-review`.

The issue list is `docs/review/series-sequential-review/volume15.md` on `cursor/series-sequential-review` at `2691145e6a366f1ed2cbc6968802ad899f7069de`. `origin/main` for this reading is `0ac96656eb5a57a029d7e27235da6610053a16ba`.

## Verdicts

**Correctness.** All eleven issues are fixed, and none was declined. No numbered statement was shortened. The two findings below are in the new ledger sentence and in the new solution of `ex:primepower`. Both repairs stay inside `volume15-order-and-chance/` and do not change a numbered statement.

**V15-001.** In the proof of `thm:erdoskac-cor`, \(L=\log\log x\) and \(y=x^{1/\log L}\), so \(\log y=\log x/\log L\) and
\[
\log\log y=\log\log x-\log\log L=L-\log\log L.
\]
The identity was checked at \(L=10\), \(20\) and \(50\): the two sides agree to the last stored digit. Mertens (Volume 6, Theorem 1.5) is \(\sum_{p\le x}1/p=\log\log x+M+O(1/\log x)\), with \(M=0.2614972128\ldots\). So \(\mathbb EW=L-\log\log L+O(1)\). The variance is the same sum minus \(\sum 1/p^2\). The subtracted series converges, so
\[
s^2=L-\log\log L+O(1).
\]
Then \((\mathbb EW-L)/\sqrt L=(-\log\log L+O(1))/\sqrt L\to0\) and \(s/\sqrt L\to1\). At \(L=10\) the ratio \(\log\log L/\sqrt L\) is \(0.264\); at \(L=50\) it is \(0.193\). The old written error was \(\log L\) in place of \(\log\log L\). That error is also \(o(\sqrt L)\) (\(\log L/\sqrt L\) is \(0.728\) at \(L=10\) and \(0.553\) at \(L=50\)), which is why the limit survived it. The corrected identities are the ones the last sentence of the proof uses. Lindeberg (Volume 4, Theorem 6.10) still applies, because \(|X_p|\le1/s\to0\).

**V15-002.** The algorithm says that an output of step 1 or step 2 is a success, and it defines success as a proper divisor greater than \(1\). On `4b4e60c2` the solution said that every such output is a proper divisor. Step 2 draws \(x\) from \(\{1,\dots,n-1\}\), so a gcd that stops the step divides an integer below \(n\) and is a proper divisor. Step 1 outputs a prime \(q\le y\). For \(n=p^e\) with \(e\ge2\) that prime is \(p<n\). For \(n=9\) and \(y=3\) the primes up to \(3\) are \(2\) and \(3\), \(3\) divides \(9\), and the output is \(3\). For a prime \(n=p\le y\), step 1 outputs \(n\), which is not a proper divisor. SR-002 says so. When every prime factor exceeds \(y\), Lemma `lem:dixon` applies with \(r=1\): Volume 2, Theorem 5.5 is `thm:cyclicn`, so \((\Z/p^e\Z)^\times\) is cyclic for \(p\) odd, \(E=\{\pm1\}\), and step 3 has success probability \(0\). Part (b) is unchanged.

**V15-003.** Exercise `ex:invtau` now points at Theorem `thm:sd`, Lemma `lem:eulerprod` and the region \(U\), all in Chapter `ch:oc-divisors`. The region is defined before the theorem, and the lemma is proved in the same chapter. The proof of the theorem cites Perron, Hankel, and the zero-free regions from Volumes 5, 6 and 14. It does not cite a result of the anatomy chapter. The sentence matches the postponement already used for Corollary `cor:bigomegasd` in the multiplication-table section. The exercise and its solution still ask for the asymptotic and the constant \(C\).

**V15-004.** Volume 2, Theorem 2.5 is `thm:bertrand`: for every integer \(n\ge1\) there is a prime \(p\) with \(n<p\le2n\). The citation writes the same interval as \((m,2m]\). In the proof, \(p'\) is the largest prime at most \(n\) and \(p''\) is the next prime, so \(p''\) is the least prime greater than \(n\), and Bertrand places it in \((n,2n]\). The bounds \(n\le x+e^{2x}\) and \(2(x+e^{2x})\le e^{3x}\) for large \(x\) are the same estimates the lemma already used.

**V15-005.** Volume 14, Theorem 3.4 is `thm:fl`. For constants \(\kappa\) and \(K\), and for \(s\ge1\), \(D=z^s\),
\[
S(\mathcal A,\mathcal P,z)=XV(z)\bigl(1+\theta Ce^{-s}\bigr)+\theta'\sum_{\substack{d\mid P(z)\\d<D}}\tau(d)|r_d|,
\]
with \(|\theta|\le1\), \(|\theta'|\le1\), and with \(C\) depending only on \(\kappa\) and \(K\). The application takes \(\kappa=2\), \(K=3\), \(s=10\) and \(D=w^{10}=\sqrt Y\), so \(z=w\). The local density satisfies \(g(p)\le\min(2/p,2/3)\), which is condition \((\Omega)\) for these \(\kappa\) and \(K\). The remainder in the proof has \(|r_d|\le\omega(d)\le\tau(d)\), so \(\tau(d)|r_d|\le\tau(d)^2\), and the sum over \(d<\sqrt Y\) is an upper bound for the sum in the theorem. The factor \(1+C_{\mathrm{FL}}e^{-10}\) is an absolute constant. Since \(\log w=\frac1{20}\log Y\), it is absorbed in the constant \(C\) of Lemma `lem:siftedprimes`, which asks only for some absolute constant.

**V15-006.** The new small-\(y\) case and the repaired large-\(y\) case cover \(2\le y\le x^{1/4}\).

For \(2\le y\le y_0=64\), take \(\alpha=\frac34\). Then
\[
\Sigma_2\le Vx^{-3/8}\prod_{p\le y}\bigl(1-p^{-1/4}\bigr)^{-1}.
\]
The product runs over the primes up to \(64\), so it is a fixed finite number, and \(V\le1\). A direct product gives an upper bound \(582801\). Call the resulting absolute constant \(C_0\). The graph of \(1/t\) has second derivative \(2/t^3>0\), so it lies strictly above its tangent except at the point of tangency. The tangent at \(t=\frac32\) is \(\frac23-\frac49\bigl(t-\frac32\bigr)\). Its antiderivative \(\frac43t-\frac29t^2\) rises by \(\frac{16}9-\frac{10}9=\frac23\) from \(1\) to \(2\). A numerical integral of the tangent on \([1,2]\) is \(0.6666666667\), and the integral of \(1/t\) is \(\log2=0.6931471806\). Thus \(\log2>\frac23\), so \(4\log2>\frac83\) and
\[
\frac1{4\log2}=0.360673760222<\frac38.
\]
For \(y\ge2\) and \(x\ge16\), \(e^{-u/4}=x^{-1/(4\log y)}\) and \(1/(4\log y)\le1/(4\log2)<\frac38\), so \(x^{-3/8}\le e^{-u/4}\). A grid of \(\log x\) from \(\log16\) to \(40\) and of \(\log y\) from \(\log2\) up to \(\min(\log64,\frac14\log x)\) produced no failure. Hence \(\Sigma_2\le C_0e^{-u/4}\).

The comparison \(-\log(1-t)\le t+t^2\) is not available for every small \(y\). At \(y=3\), the prime \(3\) has \(t=3^{1/\log3-1}=0.906094>\frac12\). At \(y=2\), \(1/\log2=1.442695>1\). Those values sit in the small-\(y\) case, which does not use the comparison. The bound \(t\le\frac12\) for the prime \(3\) first holds at about \(y=15.02\), and \(y_0=64\) is past that point.

For \(y>64\), \(\log64=6\log2=4.158883>4\), so \(\delta=1/\log y<\frac14\) and \(1-\delta>\frac34\). The Rankin weight \(\delta\) gives \(\Sigma_2\le Ve^{-u/2}\) times the Euler product. On \([0,1]\) the exponential lies under its chord, so \(p^\delta\le1+(e-1)\log p/\log y\) and
\[
\sum_{p\le y}p^{\delta-1}=\log\log y+O(1).
\]
Also \(p^{2\delta}\le e^2\), so \(\sum_pp^{2\delta-2}=O(1)\). For \(0\le t\le\frac12\),
\[
-\log(1-t)\le t+\frac{t^2}2+\frac{t^3}{3(1-t)},
\]
and \(t/(3(1-t))\le\frac13<\frac12\), so \(-\log(1-t)\le t+t^2\). For \(p\ge3\), \(p^{\delta-1}\le3^{\delta-1}\). From \(3^2=9>8=2^3\) one has \(\log3>\frac32\log2\), and
\[
(1-\delta)\log3>\frac34\cdot\frac32\log2=\frac98\log2>\log2,
\]
so \(3^{\delta-1}<\frac12\). At the endpoint \(\delta=\frac14\), \(3^{-3/4}=0.438691\). For the prime \(2\), \(\delta<\frac14\) gives \(2^{\delta-1}<2^{-3/4}\). And \(\bigl(\frac32\bigr)^4=\frac{81}{16}=5.0625<8\), so \(2^{-3/4}=0.594604<\frac23\) and \((1-2^{\delta-1})^{-1}<3\). The product is therefore \(\ll\log y\). Mertens gives \(V\ll1/\log y\), so \(\Sigma_2\ll e^{-u/2}\le e^{-u/4}\).

Both cases feed the same closing estimate, \(2d_{TV}\ll e^{-u/4}+x^{-1/4}\log x\). The absolute constant \(C_2\) of the theorem absorbs \(C_0\).

**V15-007.** Volume 7, Theorem 11.5 is `thm:lebdecomp`, the two-part Lebesgue decomposition. Volume 7, Corollary 11.6 is `cor:threeparts`: every probability on \(\R\) splits uniquely as \(\mu_d+\mu_{ac}+\mu_{sc}\), with \(\mu_d\) atomic, \(\mu_{ac}\) absolutely continuous, and \(\mu_{sc}\) atomless and carried by a Lebesgue-null set. The sentence cites that corollary. Its written order \(\mu_d+\mu_{sc}+\mu_{ac}\) is the same three measures.

**V15-008.** Walking Volume 11 in input order, `eq:selbergdelange` is the eighteenth `\begin{equation}`. It sits in `ch11-modphi.tex`, which is Chapter 11. The display is
\[
\frac1x\sum_{n\le x}z^{\omega(n)}=(\log x)^{z-1}\Bigl(\frac{F(z)}{\Gamma(z)}+O\Bigl(\frac1{\log x}\Bigr)\Bigr),
\]
with the same product \(F(z)\) as Corollary `cor:omegasd`. The opening paragraph and the corollary now cite equation (18). There is no other numbered equation environment in that volume before this one, and equations are not numbered by chapter.

**V15-009.** Corollary `cor:omegasd` states the factor \(F(z)/\Gamma(z)\). At \(z=2\),
\[
F(2)=\prod_p\Bigl(1-\frac1{p^2}\Bigr)=\frac1{\zeta(2)}=\frac6{\pi^2}=0.607927101854,
\]
and \(1/\Gamma(2)=1\). The old factor \(1/\Gamma(z+1)\) equals \(1/2\) at \(z=2\). The summary row’s “factor \(1/\Gamma\)” is the Gamma factor in the corollary. On `4b4e60c2` the new sentence said that no independent model produces either factor. Volume 11, under equation (18), says that the arithmetic factor is the one the independent model sees and that \(1/\Gamma(z)\) comes from the sharp cut-off. The same split is the probabilistic sentence at the opening of this volume’s Selberg–Delange chapter. SR-001 makes the ledger say that. The coins miss \(1/\Gamma(z)\). The product \(F(z)\) is built from the local probabilities \(1/p\).

**V15-010.** The preface no longer lists the Erdős–Kac theorem among the arguments that are cited and not repeated. It says the theorem is proved again, as a corollary of the Kubilius model. That corollary is `thm:erdoskac-cor`, and the chapter says the argument is a second proof. The prime number theorem, Bombieri–Vinogradov, the sine kernel, and Roth stay on the list of arguments that are not repeated. The blurb names the Kubilius model and the Erdős–Kac theorem among the contents of the book. `kdp.md` names them in the narrative and in the keywords. Neither says that the argument is omitted.

**V15-011.** The series in the caption of `fig:bohrjessen` is \(v(0.7)\) from Exercise `ex:varbj`. Summing the primes through \(19999999\) gives \(0.530051330659\). The \(k=1\) tail, from the asymptotic expansion of \(\int_X^\infty t^{-1.4}/\log t\,dt\), contributes \(0.000118082632\). The \(k\ge2\) tail past that point is below \(10^{-14}\). The sum is \(0.530169413291\), which to three decimals is \(0.530\). The caption now says \(0.530\). The only change in that caption is this number. The sample variances \(0.525\) and \(0.531\) are unchanged, and the TikZ picture is unchanged.

Those two sample numbers sit next to the series in the way a sample of this size should. For a variance near \(0.53\), the Gaussian scale of the sampling error is \(0.53\sqrt{2/n}\): about \(0.0075\) for \(10\,000\) points and about \(0.0037\) for \(40\,000\) points. The gaps \(0.005\) and \(0.001\) are inside those scales. The Kolmogorov–Smirnov distance \(0.0095\) is below the usual \(5\%\) threshold \(1.36/\sqrt{10\,000}\approx0.0136\), so the caption’s “within sampling error” matches the stated sample sizes.

The ink does not reproduce \(0.525\) and \(0.531\) as second moments. The bars are \(40\) bins of width \(0.1\) from \(-1.5\) to \(2.5\), the tick labels sit on \(v=-1.5+x/1.75\), and the density is the TikZ height divided by \(3\). The heights sum to \(30\), so the bars are a probability density, and the second moment about the bin centres is \(0.503581972222\). Sheppard’s correction \(h^2/12\) raises it to \(0.50442\). The rust polyline, on the same scale and normalised by its mass \(0.99632\), has variance \(0.50281\). The Kolmogorov distance between those two plotted distribution functions is \(0.00670\), the same order as the caption’s \(0.0095\). The peak density \(0.55033\) matches the Gaussian peak \(0.55059\) of variance \(0.525\) more closely than the peak \(0.5613\) of variance \(0.504\). A Gaussian of variance \(0.530\), cut to \([-1.5,2.5]\) and renormalised, has variance \(0.4755\), so the window alone does not turn \(0.530\) into \(0.504\).

The raw draws are not in the repository. The caption states the variances of the two samples, and the picture is frozen. Replacing \(0.525\) and \(0.531\) by the ink’s second moments would assert a different pair of numbers from the ones the samples can carry. They stay. The disagreement between the ink and those two numbers is recorded here.

**Concept order.** The new appeals are to Volume 2, Theorem 2.5, Volume 7, Corollary 11.6, Volume 11, equation (18), and Volume 14, Theorem 3.4, all proved before this volume. The small-\(y\) case in `thm:kubilius` uses only the integral of \(1/t\) and the comparison of powers of \(x\ge16\). The forward pointer in `ex:invtau` names Chapter `ch:oc-divisors`, which is later, and it tells the reader to postpone the exercise. The exercise is not used to prove that chapter.

**Labels and numbering.** Against `origin/main`, the TeX files under `volume15-order-and-chance/` have the same \(432\) labels, with no additions and no removals. No numbered environment was added or removed. `python3 tools/cross_volume_citations.py` matched \(5446\) numbered statements, the same total as on main.

**Voice.** The new sentences name the range, the constant, or the output of the step. The repaired ledger says which factor comes from the cut-off and which product is built from \(1/p\). The repaired solution says what step 1 returns for \(n=9\) and what it returns for a prime.

**Downstream impacts.** None. No numbered statement changes its number. Volume 15 is the last volume of the series. The statements this volume cites from the edited earlier books keep the form the new sentences use: Volume 14, Theorem 3.4 still says that some \(C\) depending only on \(\kappa\) and \(K\) exists; Volume 2, Theorem 2.5 is Bertrand’s postulate as cited; Volume 7, Corollary 11.6 is the three-part split; Volume 11, equation (18) is the formula the corollary quotes.

## Findings

**SR-001.** In the ledger entry for prime factors, the text on `4b4e60c2` said that no independent model produces either \(1/\Gamma(2)=1\) or \(F(2)=6/\pi^2\). The factor the coins miss is \(1/\Gamma(z)\), from the cut-off \(n\le x\). The product \(F(z)\) is built from the probabilities \(1/p\). The sentence now says so.

**SR-002.** In the solution of `ex:primepower`, the text on `4b4e60c2` said that every output of steps 1 and 2 is a proper divisor. Step 1 outputs \(n\) itself when \(n\) is prime and \(p\le y\). The solution now separates that case from \(n=9\), \(y=3\), and from step 2.

## Per-issue verdicts

| ID | Verdict |
| --- | --- |
| V15-001 | Fixed. With \(y=x^{1/\log L}\), \(\log\log y=L-\log\log L\), and the variance is the same quantity up to a convergent \(\sum 1/p^2\). Both \((\mathbb EW-L)/\sqrt L\) and \(s/\sqrt L-1\) tend to \(0\). |
| V15-002 | Fixed, after SR-002. Steps 1 and 2 return a proper divisor for \(n=9\), \(y=3\), and whenever the output is below \(n\). Step 3 has success probability \(0\) when \(r=1\). A prime \(p\le y\) makes step 1 return \(n\). |
| V15-003 | Fixed. The exercise points to Theorem `thm:sd`, Lemma `lem:eulerprod` and the region \(U\) in Chapter `ch:oc-divisors`, and it tells a first reading to postpone the exercise. |
| V15-004 | Fixed. Volume 2, Theorem 2.5 is Bertrand’s postulate: for every integer \(m\ge1\) there is a prime in \((m,2m]\). |
| V15-005 | Fixed. Volume 14, Theorem 3.4 gives the factor \(1+Ce^{-s}\) with \(C\) depending only on \(\kappa\) and \(K\). At \(s=10\) that factor is absolute and is absorbed in the constant of the lemma. |
| V15-006 | Fixed. For \(2\le y\le64\) the tail is \(O(x^{-3/8})\), and \(x^{-3/8}\le e^{-u/4}\). For \(y>64\) the comparison \(-\log(1-t)\le t+t^2\) applies to every odd prime, and the factor at \(2\) is bounded by \(3\). |
| V15-007 | Fixed. Volume 7, Corollary 11.6 is the three-part split. Theorem 11.5 is the two-part Lebesgue decomposition. |
| V15-008 | Fixed. Volume 11, equation (18), is `eq:selbergdelange`, and the displayed formula is the one in Corollary `cor:omegasd`. |
| V15-009 | Fixed, after SR-001. The corollary has \(F(z)/\Gamma(z)\). At \(z=2\) the factors are \(1\) and \(6/\pi^2\). The coins miss \(1/\Gamma(z)\). |
| V15-010 | Fixed. The preface says the Erdős–Kac theorem is proved again. The blurb and `kdp.md` do not say that the argument is omitted. |
| V15-011 | Fixed for the series, which is \(0.530169\ldots\) and is written \(0.530\). The sample variances \(0.525\) and \(0.531\) stay. They match the sample sizes. The second moments of the drawn bars and of the drawn curve are \(0.504\) and \(0.503\). |

## Recomputation

```
ln 2 = 0.693147180560
2/3 = 0.666666666667
4 ln 2 = 2.772588722240
8/3 = 2.666666666667
1/(4 ln 2) = 0.360673760222
3/8 = 0.375
ln 64 = 6 ln 2 = 4.158883083360
(3/2)^4 = 81/16 = 5.0625 < 8
2^{-3/4} = 0.594603557501 < 2/3
3^{-3/4} = 0.438691
y=3: 3^{1/ln 3 - 1} = 0.906094
y=2: 1/ln 2 = 1.442695
t = 1/2 for the prime 3 at y = 15.0219
tangent integral on [1,2] = 0.6666666667
integral of 1/t on [1,2] = 0.6931471806
product over p<=64 of (1-p^{-1/4})^{-1} = 582800.97

log log y - (L - log log L) = 0 at L = 10, 20, 50
(log log L)/sqrt(L) = 0.263744 at L=10, 0.245339 at L=20, 0.192907 at L=50
(log L)/sqrt(L) = 0.728141 at L=10, 0.669866 at L=20, 0.553244 at L=50

6/pi^2 = 0.607927101854027
1/Gamma(2) = 1
1/Gamma(3) = 1/2

variance series, primes through 19999999: 0.530051330659
k=1 tail: 0.000118082632
full estimate: 0.530169413291
three decimals: 0.530

histogram on the printed axes: 40 bins, width 0.1, from -1.5 to 2.5
bar mass = 1, mean = 0.017166666667, variance = 0.503581972222
Sheppard variance = 0.504415
rust curve mass = 0.996322, variance = 0.50281
Kolmogorov distance between the plotted distribution functions = 0.006697

small-y grid x^{-3/8} <= e^{-u/4}: no failures
large-y grid 3^{delta-1} < 1/2 for y>64: no failures
```

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume15.md` at `2691145e`.
- `git diff origin/main...4b4e60c2`, and the same diff through `ab5d383f`, including the proof of `thm:erdoskac-cor`, the solution of `ex:primepower`, the proof of `thm:kubilius`, the proof of `lem:siftedprimes`, the proof of `lem:covering`, Corollary `cor:omegasd`, the ledger, the preface, the blurb, `kdp.md`, and the caption of `fig:bohrjessen`.
- Statement numbers from `tools/cross_volume_citations.py` on this tree: Volume 2, Theorem 2.5 is `thm:bertrand`; Theorem 5.5 is `thm:cyclicn`. Volume 4, Theorem 6.10 is `thm:lindeberg`. Volume 6, Theorem 1.5 is `thm:mertens2`; Theorem 9.7 is `thm:erdoskac`. Volume 7, Theorem 11.5 is `thm:lebdecomp`; Corollary 11.6 is `cor:threeparts`. Volume 14, Theorem 3.4 is `thm:fl`; Corollary 3.5 is `cor:rough`. The statements were read beside the new sentences. Volume 11, equation (18), was counted by walking `\begin{equation}` in input order.
- Label multiset against `origin/main`: \(432\) labels, equal. No TikZ option is in the diff. The caption change on `4b4e60c2` is the single number \(0.529\) to \(0.530\). `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- `git diff --check` on the repaired tree: clean.
- Python, as recorded under Recomputation.
- `./build.sh volume15-order-and-chance` on the source of `ab5d383f` exited \(0\). The layout line is `Book layout checked: 383 whole boxes, maximum height 401.4pt; no overflow or unresolved references`. `build/volume15-order-and-chance/main.log` has no line matching `undefined`, `Overfull`, or `Emergency stop`. The warnings in that log include the `unicode-math` notes on `\overbracket` and hyperref notes on tokens in PDF strings. Underfull boxes are present; none of the reported line numbers falls on the repaired ledger sentence or on the repaired solution of `ex:primepower`. `pdfinfo` on `dist/kdp/Volume 15 - Order and Chance - Print.pdf` reports \(335\) pages, page size \(513\times738\) pts, PDF 1.3, not encrypted. The reading PDF is the cover plus that interior, \(336\) pages, at \(504\times719.998\) pts. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that \(55\) plates were written at \(1800\) px. The EPUB is \(25\,500\,857\) bytes. The print metadata line reports \(335\) interior pages and spine \(0.7886\) in, which is the even rounding \(336\times0.002347=0.788592\).

## Print page count

335.

## Downstream impacts

None.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V15-001 through V15-011.
- The items the Volume 15 review left unchecked: the short-interval sums \(V(10^8,H)\), the Maier matrix, the Steinhaus sample moments, the histogram of \(V(x)\), the Chebotarev bars, the Birch histogram beyond the count \(1{,}017{,}072\), the Odlyzko and Montgomery histograms, the \(1{,}200\) zeros on the cover, the window correlations \(0.95\) and \(0.98\), the moment-share sample at \(T=10^6\), the prime-progression counts in Chapter 12, and the race up to \(10^9\). The \(8{,}000\)-point histogram was not redrawn. Its bars and its curve were integrated on the printed axes, as recorded under V15-011. The raw sample that produced \(0.525\), \(0.531\) and the Kolmogorov–Smirnov distance \(0.0095\) is not in the repository.
- Acceptance of the print file by KDP.
