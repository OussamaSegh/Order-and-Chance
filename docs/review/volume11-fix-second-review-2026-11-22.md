# Volume 11 fix, second review — 22 November 2026

Independent reading of PR #264. The fixes were written by another agent. The head under review was `c2e37af97e2227fc5f064948d280dc73ef7fcc1a`. This reading found two defects. The corrections are `01c851507e6d7236898b5b0942635ba23aa4c699`. This log is the following commit on `cursor/fix-volume11-review`.

The issue list is `docs/review/series-sequential-review/volume11.md` on `cursor/series-sequential-review` at `2691145e6a36`. The state-after-Volume-K comments on PR #253 were read through the Volume 10 comment. `origin/main` for this reading is `07b84738c6e1`.

## Verdicts

**Correctness.** Seven of the nine repairs stood as written. V11-001 named Furstenberg, and the sentence on `c2e37af9` still gave the integer theorem to double recurrence alone. V11-006 proved the integer tail and then cited an exercise whose hypothesis is the real tail. Both sentences are corrected below. After the corrections, each of V11-001 through V11-009 is fixed in the place the issue named. No issue was declined.

**Dropped or weakened proofs.** No numbered statement was shortened, and no statement was weakened. The new Borel–Cantelli half, the extended Kolmogorov inequality, the truncation paragraph, the Chung–Fuchs restart, and the first-passage count are proofs added in prose. They do not replace a numbered statement with a citation.

**V11-001.** The back cover now gives continued-fraction digits to Birkhoff and three-term progressions to Furstenberg. Chapter 10, Theorem `thm:cfstats`, applies Birkhoff’s theorem to the Gauss map and obtains the digit frequencies, Khinchin’s constant, and Lévy’s constant. Theorem `thm:double` is the dynamical statement: for an ergodic measure-preserving map and a set of positive measure, the liminf of the triple-intersection averages is positive. The proof of Theorem `thm:roth` is the correspondence principle, building an ergodic shift from the indicator of \(E\), followed by that recurrence. On `c2e37af9` the blurb said double recurrence proves the integer theorem and did not name the correspondence principle. See SR-001. The listing’s sentence, “Furstenberg’s method proves that every set of integers of positive density contains three terms in arithmetic progression,” already matched that proof and was left as it stood. The theorem uses positive upper density. A set whose asymptotic density exists and is positive has positive upper density, so the listing’s sentence is true of the theorem.

**V11-002.** The preface says the infinitesimal-array converse, the nonsymmetric stable classification, and the Selberg–Delange formula are quoted, and that the last is proved in Volume 15, with other quoted results marked in the text. The blurb and `kdp.md` now say the same two things: quoted theorems are marked where they occur, and the Selberg–Delange formula is the one deferred to Volume 15. A search of the volume found the marks named in the issue: the array converse and the nonsymmetric formula in Chapter 5, Kolmogorov–Smirnov and empirical Donsker in Chapter 3, Shevtsova’s constant in Chapter 4, the Bahadur–Rao asymptotic in Chapter 7, the \(2\sqrt n\) and Tracy–Widom limits in Chapter 8, Cameron–Martin in Chapter 9, the Gauss–Kuzmin rate and Szemerédi’s theorem for longer progressions in Chapter 10, de Bruijn’s asymptotic in Chapter 12, and the sharp \(ae^{-2c}\) bound in `shuffling.tex`. Chapter 11 says the Selberg–Delange formula is admitted and proved in Volume 15, Chapter 3, and that nothing else in the volume depends on it. No other result is sent to Volume 15 as an admitted input. The opening of `kdp.md` no longer says that every limit theorem is proved in full.

**V11-003.** Theorem `thm:arcsine` obtains the arcsine law from Donsker’s theorem, the occupation-time continuity lemma, and continuous mapping. Theorem `thm:hartmanwintner` realises the walk as Brownian motion at the stopping times of Corollary `cor:embedwalk`, the same Skorokhod embedding used to prove Donsker’s theorem, and then compares \(B_{T_n}\) with \(B_n\) by a separate almost-sure estimate. The listing says that, and it no longer says the law of the iterated logarithm comes at no extra cost.

**V11-004.** The divergent half is written before the first section. Complements of a finite independent family are reduced to a product by the same subtraction Volume 4 uses for Theorem 4.4. For \(0\le x\le 1\), Volume 1, Exercise 8.3(a) is the series \(e^x=\sum x^k/k!\) for every real \(x\), so at \(-x\) it is \(e^{-x}=\sum (-x)^k/k!\). Grouping terms \(2m\) and \(2m+1\) gives \(1-x\) plus brackets \(\frac{x^{2m}}{(2m)!}\bigl(1-\frac{x}{2m+1}\bigr)\). Each bracket is nonnegative, so \(1-x\le e^{-x}\). The tail of a divergent series sends the finite product to 0. Continuity from above is Volume 7, Proposition 7.2(d), and the countable union of the null sets is Proposition 7.2(b). Proposition 7.2(e) is the convergent half, for a general measure. On current main, `prop:measureprops` is Proposition 7.2.

Kolmogorov’s inequality is written after the grouping proposition. Volume 4, Theorem 4.3 is `thm:kolmogorov`: centred summands, each bounded and a function of its own finite digit block. The new argument drops both restrictions. The quadratic comparison puts each partial sum in \(L^2\). The first-crossing factor \(S_k\mathbf 1_{A_k}\) is a function of \(X_1,\dots,X_k\), hence independent of each later \(X_j\). Hölder’s inequality with exponent 2 is Volume 7, Theorem 10.2, `thm:holder`. It gives integrability of the product. Fubini’s theorem is Volume 7, Theorem 9.6, `thm:fubini`; the paragraph after that theorem is the factorisation \(\mathbb E[XY]=\mathbb EX\,\mathbb EY\) for independent integrable factors. The cross term therefore has expectation 0, and the usual first-crossing sum is \(P(\max_{k\le n}|S_k|\ge a)\le\operatorname{Var}(S_n)/a^2\). Proposition `prop:l2series` and the tiling solution in Chapter 13 cite this form. The Chapter 2 reminder cites both Borel–Cantelli halves as proved in Chapter 1. The three-series proof uses that reminder and `prop:l2series`; its lower bound is Lemma `lem:kolmogorovlower`, proved in Chapter 2 from optional stopping, not from the digit-block theorem.

**V11-005.** The figure file draws 201 points and 200 steps on each path, from height 0 to \(2\), \(0.676\), and \(-1.515\). The axis ticks are now \(50,100,150,200\). The caption states those endpoints, the sample means of the plotted increments, and the sample standard deviations. See the recomputed values below. The typography check is recorded there as well.

**V11-006.** A finite mean and the reminder’s comparison \(\sum_{k\ge 1}P(Y>k)\le\mathbb EY\) give \(nP(|X|>n)\to 0\) for integers \(n\ge 2\), by counting at least \(n/2\) integers \(k\) in \((n/2,n]\). Exercise `ex:feller` assumes \(xP(|X|>x)\to 0\) as a real variable \(x\to\infty\), and its solution proves \(\frac1n\mathbb E[X^2\mathbf 1_{|X|\le n}]\to 0\) from that hypothesis. On `c2e37af9` the paragraph called the integer limit the hypothesis of the exercise. See SR-002. The truncated-mean bound is the layer-cake comparison \(Y\le\sum_{k\ge 0}\mathbf 1_{Y>k}\), and \(|\mathbb EX-\mathbb E[X\mathbf 1_{|X|\le n}]|\le nP(Y>n)+\sum_{k\ge n}P(Y>k)\to 0\). With both hypotheses of Theorem `thm:wlltriangular`, \(a_n/n\to\mathbb EX\).

**V11-007.** The beauty note now says the scale \(n\log_2 n\). Theorem `thm:stpetersburg` is \(S_n/(n\log_2 n)\to 1\) in probability, and the chapter opening and the figure use the same scale.

**V11-008.** Proposition 8.4 on current main is `prop:visits`: the expected number of visits to the origin, including time 0, equals \(\sum u_n\), and equals \(1/(1-f)\) or \(\infty\) according as \(f<1\) or \(f=1\). The proof restarts after a return because the unused steps are a fresh copy, and it concludes that \(f=1\) forces infinitely many returns. The written steps are fair signs; the restart uses that the steps are i.i.d. The exercise now says that, and the solution writes it for a general centred integrable walk on \(\mathbb Z\). Part (a) already restarts at the first visit to \(x\). For the return count, \(P(V\ge m)=f^{m-1}\). Volume 1’s tail-sum identity, in the probability chapter, is \(\mathbb ET=\sum_{j\ge 0}P(T>j)\) for a positive integer-valued \(T\), including when both sides are infinite. That is \(\mathbb EV=\sum_{m\ge 1}f^{m-1}\). The partial counts satisfy \(\mathbb EV_N=\sum_{n\le N}P(S_n=0)\), and the liminf comparison with \(V_N\le V\) gives \(\mathbb EV_N\to\mathbb EV\). The sum of the return probabilities is infinite, so \(f=1\), and every \(\{V\ge m\}\) has probability 1. The events decrease, so the walk returns to 0 infinitely often.

**V11-009.** The count is unnumbered. Volume 4, Theorem 8.1 is `thm:rwreflect`: paths of a given length from 0 to \(b\le a\) that visit \(a\) are paired with all paths to \(2a-b\). With length \(k-1\), barrier \(n\), and endpoint \(n-1\), the reflected endpoint is \(n+1\). The last step is \(+1\) with probability \(1/2\), so
\[
P(\tau_n=k)=\frac12\bigl(P(S_{k-1}=n-1)-P(S_{k-1}=n+1)\bigr).
\]
The binomial form and the cancellation
\[
\binom{k-1}{r-1}-\binom{k-1}{r}=\frac nk\binom{k}{r},
\]
with \(r=(k+n)/2\), are the same cancellation written in the proof of the ballot theorem, Volume 4, Theorem 1.7, `thm:ballot`. The case \(r=k\) is the single path of \(n\) pluses. The caption now points at this derivation.

**Concept order.** The new appeals are to tools already proved: Volume 1, Exercise 8.3(a); Volume 7, Proposition 7.2(b), (d), and (e); Volume 7, Theorems 9.6 and 10.2; Volume 4, Theorems 1.7 and 8.1; and the restart inside the proof of Volume 4, Proposition 8.4. Grouping is the proposition immediately before the Kolmogorov argument. The divergent Borel–Cantelli half is written before it is used.

**Labels and numbering.** Against `origin/main`, the TeX files under `volume11-randomness/` have the same 427 labels, with the same multiplicities. The environment counts are unchanged: 166 exercises, 75 theorems, 50 lemmas, 20 propositions, 16 examples, 15 corollaries, and 6 definitions. No `\label` line and no `\begin{theorem}`-class line is in the diff. The equation-label blocks are the same file by file. The first-passage display is `\[...\]`.

**Recomputed numbers.** A Python session read the three paths in `figures/ch01-trichotomy.tex` as exact decimals. Each path has 201 points and 200 increments and starts at height 0. The sample mean of the increments is the final height divided by 200. The sample standard deviation divides by \(199\).

- Upper path: end \(2\), mean \(0.010\), sample standard deviation \(0.035661163651\).
- Middle path: end \(0.676\), mean \(0.00338\), sample standard deviation \(0.037193310038\).
- Lower path: end \(-1.515\), mean \(-0.007575\), sample standard deviation \(0.036999855697\).

The caption prints \(0.010\), \(0.00338\), \(-0.007575\) and \(0.03566\), \(0.03719\), \(0.03700\). The third standard deviation rounds up to five decimals. The divisor \(200\) gives \(0.035571899022\), \(0.037100210242\), and \(0.036907240143\), which are not the printed figures. The word in the caption is “sample”.

The binomial identity \(k\bigl(\binom{k-1}{r-1}-\binom{k-1}{r}\bigr)=n\binom{k}{r}\), with an impossible coefficient read as 0, was checked for \(1\le n\le 39\) and \(1\le k\le 119\) with \(k+n\) even: 2321 pairs, no failures. Direct path counts for the simple symmetric walk, \(1\le n\le 7\) and \(1\le k\le 12\), checked \(k\) times the number of paths with \(\tau_n=k\) against \(n\) times the number of paths with \(S_k=n\): 84 pairs, no failures.

**Voice.** The new sentences name the event, the tail, the first crossing, the return, or the path count. The banned fillers do not appear in the changed paragraphs. The two corrected sentences do the same.

**Downstream impacts.** None. No label, statement number, or cited claim changes. `python3 tools/cross_volume_citations.py` matched 5446 numbered statements, the same count recorded after Volume 10. The parts Volume 11 newly cites are the statements numbered above, on current main.

**Jacket sentences left as they stood.** The blurb and the listing still say that Donsker’s theorem turns every random walk into Brownian motion. The preface, and Theorem `thm:donsker`, state the centred i.i.d. walk of finite positive variance. The next clause of each jacket is the stable laws for infinite variance. That “every” was already the sentence the sequential review quoted, and the fault it named was the arcsine and the iterated logarithm, which V11-003 repairs. The word was not changed here.

## Findings

SR-001. On `c2e37af9`, `blurb.tex` said that Furstenberg’s double recurrence proves that a set of integers of positive density contains a three-term progression. Theorem `thm:double` is the recurrence for an ergodic system. The proof of Theorem `thm:roth` begins “It remains to translate” and builds the system by the correspondence principle before it calls on double recurrence. The blurb now says that double recurrence, with the correspondence principle, proves the integer statement.

SR-002. On `c2e37af9`, the weak-law paragraph proved \(nP(|X|>n)\to 0\) for integers \(n\) and then said that Exercise `ex:feller` assumes this limit. The exercise assumes \(xP(|X|>x)\to 0\) as \(x\to\infty\), and the integral in its solution uses that real limit. The survival function does not increase. For \(n\le y<n+1\), \(yP(|X|>y)\le(n+1)P(|X|>n)\to 0\), so the real limit holds, and the sentence now cites the solution of the exercise for the truncated second moment.

| ID | Verdict |
| --- | --- |
| V11-001 | Fixed, after SR-001. Birkhoff is named for the continued-fraction digits. Furstenberg’s double recurrence, with the correspondence principle, is named for the three-term progressions. |
| V11-002 | Fixed. Quoted theorems are marked where they occur. The Selberg–Delange formula is the one deferred to Volume 15. The listing no longer says that every limit theorem is proved in full. |
| V11-003 | Fixed. Continuous mapping gives the arcsine law. The law of the iterated logarithm is the separate almost-sure argument from the Skorokhod embedding. |
| V11-004 | Fixed. The divergent Borel–Cantelli half is proved for independent events. Kolmogorov’s inequality is proved for independent centred square-integrable summands. Chapter 2 and the tiling solution use that form. |
| V11-005 | Fixed. The axis counts 200 steps. The caption’s means and sample standard deviations are the plotted increments. |
| V11-006 | Fixed, after SR-002. A finite mean gives \(xP(|X|>x)\to 0\). The solution of `ex:feller` gives the truncated second moment, and the truncated means converge to the mean. |
| V11-007 | Fixed. The beauty note says \(n\log_2 n\). |
| V11-008 | Fixed. The solution restarts the i.i.d. walk after a return, as in the proof of Volume 4, Proposition 8.4, and concludes that the walk returns to 0 infinitely often. |
| V11-009 | Fixed. The coin-tossing count is derived from Volume 4, Theorem 8.1 and the cancellation in Theorem 1.7. The display is unnumbered. |

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume11.md` at `2691145e6a36`.
- The state-after-Volume-K comments on PR #253, through the Volume 10 comment (`7073549415`).
- `git diff origin/main...c2e37af9`, then the two-sentence correction against that head.
- Statement numbers by the counter walk in `tools/cross_volume_citations.py`, on the working tree, which matches `origin/main` outside `volume11-randomness/`: Volume 1, Exercise 8.3 is `ex:taylorln`; Volume 4, Theorems 1.7, 4.3, 4.4, 8.1 and Proposition 8.4 are `thm:ballot`, `thm:kolmogorov`, `thm:bc`, `thm:rwreflect`, and `prop:visits`; Volume 7, Proposition 7.2 and Theorems 9.6 and 10.2 are `prop:measureprops`, `thm:fubini`, and `thm:holder`. The statements of those results were read beside the new proofs.
- The representative proofs read in full for the new arguments: Volume 4, Theorem 4.3, Theorem 4.4, Theorem 8.1, and Proposition 8.4; Volume 7, Proposition 7.2 and the Fubini paragraph after Theorem 9.6; Hölder’s statement; Volume 1, Exercise 8.3(a) and the tail-sum identity in `ch09-probability.tex`; `ex:feller` and its solution; the arcsine proof and the Hartman–Wintner proof; the statements of `thm:double`, `thm:roth`, and `thm:cfstats`.
- Figure typography: every TikZ option bracket in `figures/ch01-trichotomy.tex` is identical to `origin/main`, and every node anchor and tick coordinate is identical. The diff changes the comment, the four tick numerals, and the three node texts. Fonts, colours, line widths, and positions are unchanged.
- Label multiset and environment counts against `origin/main`. Equation-label blocks are unchanged. `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- Python, as recorded under recomputed numbers.
- `./build.sh volume11-randomness` on `01c851507e6d` exited 0. The log line is `Book layout checked: 377 whole boxes, maximum height 442.1pt; no overflow or unresolved references`. `build/volume11-randomness/main.log` has no line matching `undefined`, `Overfull`, or `Emergency stop`. `pdfinfo` on `dist/kdp/Volume 11 - Randomness - Print.pdf` reports 317 pages, page size 513 × 738 pts, PDF 1.3. The reading PDF is the cover plus that interior, 318 pages, at 504 × 720 pts. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that 58 plates were written at 1800 px. The EPUB is 24,711,050 bytes.

## Figure typography

Pass. Only label text, axis counts, and the file comment changed. The option brackets, including `font=\scriptsize`, `font=\tiny`, the colours, the line widths, and the anchor coordinates, match `origin/main`.

## Print page count

317.

## Downstream impacts

None.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V11-001 through V11-009.
- The items the Volume 11 review left unchecked: Shevtsova’s constant \(0.4748\), the Watson–Pólya integral past the printed relation, the birthday figure’s uniform error \(0.011\), the Golomb–Dickman integral to ten digits, and Weldon’s historical odds.
- Acceptance of the print file by KDP.
