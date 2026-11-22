# Volume 14 fix, second review — 22 November 2026

Independent reading of PR #267. The fixes were written by another agent. The head under review was `ffba729970ac71409f5192353aefcd36835ceb32`. This reading found one false pointer in the new Sophie Germain solution. It is repaired in `673fa1290b04619f4fb3a4895d272a87efedf3f8`. This log is the following commit on `cursor/fix-volume14-review`.

The issue list is `docs/review/series-sequential-review/volume14.md` on `cursor/series-sequential-review` at `2691145e6a366f1ed2cbc6968802ad899f7069de`. The state-after-Volume-K comments on PR #253 were read through the Volume 13 comment (`7077303378`). `origin/main` for this reading is `8c7dd53ef8fe67eddcec6838b702a2992c02c377`.

## Verdicts

**Correctness.** All eight issues are fixed, and none was declined. No numbered statement was shortened. The one finding below is a wrong location in the new solution of `ex:sg`. The repair stays inside `volume14-primes/` and does not change a numbered statement.

**V14-001.** Volume 6, Proposition 1.2 is `prop:chebyshev`. Part (b) says that for \(x\ge 2\),
\[
\pi(x)\le\sqrt x+\frac{2\log 4\cdot x}{\log x},
\]
and in particular \(\pi(x)=O(x/\log x)\). Theorem `thm:effcheb` gives an error \(O(\sqrt x\log(kx))\) with an absolute implied constant. For a prime \(q\le\xi_2\) the factor \(\log(qx)\) is at most \(\log\xi_2+\log x\). There are at most \(\pi(\xi_2)\) such primes, so the summed error is \(O(\pi(\xi_2)\sqrt x\log x)\).

With \(\xi_2=\sqrt x/\log^2 x\),
\[
\log\xi_2=\tfrac12\log x-2\log\log x.
\]
This is at least \(\tfrac14\log x\) once \(\log x\ge 8\log\log x\), which first holds at \(x\approx 2.149\times 10^{11}\) (\(\log x\approx 26.093\)). Then
\[
\frac{\xi_2}{\log\xi_2}\le\frac{\xi_2}{\tfrac14\log x},
\]
and
\[
\frac{\xi_2}{\tfrac14\log x}\sqrt x\log x=4\xi_2\sqrt x=\frac{4x}{\log^2 x}.
\]
The identity was checked at \(\log x=30,60,100\): the two sides agree to the last digit of the floating-point ratio \(1\). The Chebyshev constant stays inside the \(\ll\). An explicit upper bound that uses Proposition 1.2(b) as written, and \(\log(qx)\le\log\xi_2+\log x\), divided by \(x/\log^2 x\), is finite for large \(x\) and decreases toward \(4\log 4\cdot\tfrac32\approx 8.32\). The values are in the recomputation below. So the medium range is \(O(x/\log^2 x)\). The main term is \(\operatorname{li}(x)\) times a tail \(O(1/\log x)\), which is the same order. Both sit inside the theorem’s error \(O(x\log\log x/\log^2 x)\).

The old factor is exactly the main-term size: \(\xi_2\sqrt x\log x=x/\log x\).

**V14-002.** The blurb no longer lists the Green–Tao theorem among the complete proofs. It says the theorem is stated without its proof. Theorem `thm:greentao` is marked quoted. The preface lists it with the theorems that are quoted. `kdp.md` names the Gowers norms in the narrative and says, in the next paragraph, that a short list of deep theorems is quoted. The phrase “the Gowers norms” in the blurb names the material Chapter 13 proves: the norms, the generalised von Neumann inequality, the \(U^2\) inverse theorem, and the \(W\)-trick. The higher inverse theorem, `thm:inverse`, stays marked quoted, and the preface lists it separately. It is not named in the blurb’s list of complete proofs.

**V14-003.** The sentence now cites Tikao Tatuzawa, “On a theorem of Siegel”, *Japan. J. Math.* 21 (1951), 163–178, and states: if \(0<\varepsilon<1/11.2\) and \(\chi\) is real and primitive of modulus \(q>e^{1/\varepsilon}\), then \(L(1,\chi)>0.655\,\varepsilon/q^\varepsilon\), except for at most one such character. That is the form quoted in the introduction of Yong-Gao Chen, *Acta Arithmetica* 130.4 (2007), and in the introduction of the paper at doi 10.4064/aa111-4-2. The journal, year and pages are those of that paper, and \(0.655\) is the constant in its Theorem 2. For \(\varepsilon<1/11.2\) one has \(e^{1/\varepsilon}>e^{11.2}\), so \(q>e^{1/\varepsilon}\) is the bound that secondary statements use in place of the paper’s \(\max(e^{1/\varepsilon},e^{11.2})\). Exercise `ex:ineffective` still asks where Siegel’s proof fails to produce a number, and its solution still does that. The constant \(0.655\) is not in the exercise.

**V14-004.** Goldfeld’s *Bulletin of the American Mathematical Society* 13 (1985), 23–37, states that once an elliptic curve supplies a triple zero, every \(\varepsilon>0\) gives an effectively computable \(c>0\) with \(h(D)>c(\log|D|)^{1-\varepsilon}\). The Gross–Zagier announcement is the 1983 *Comptes Rendus* note cited there, and the full argument is *Inventiones Mathematicae* 84 (1986), including the same lower bound in §8. The book’s inequality is \(\ge\), which follows from the strict form. The factor lost against \(\log|d|\) is \((\log|d|)^\varepsilon\), a positive power of \(\log|d|\), and \(\varepsilon\) may be taken arbitrarily small. The years 1983–1986 are the years of that completion.

**V14-005.** Part (a) of `lem:zetaline` is proved for \(|t|\ge 2\), and part (b) uses that extension. The three ranges in (a) are these.

- If \(\sigma\ge 2\), then \(|\zeta(s)|\le\zeta(2)\). Since \(\log|t|\ge\log 2\), this is a constant times \(\log|t|\).
- If \(1-1/\log|t|\le\sigma\le 0\), then \(1/\log|t|\ge 1\), so \(2\le|t|\le e\), and \(\sigma\ge 1-1/\log 2\). That set is compact and does not contain the pole at \(1\). A continuous function on a compact set is bounded, and again the bound is a constant times \(\log|t|\).
- If \(\sigma>0\), Lemma `lem:em` applies with \(k=2\) and \(N=\lceil(|s|+2)^2\rceil\). The hypothesis of that lemma is \(N\ge(|s|+2)^2\). Here \(|s|\le|t|+2\), so \(N\le(|t|+4)^2+1\). For \(|t|\ge 2\) one has \(|t|+4\le 3|t|\), hence \(N\le 9|t|^2+1\le|t|^6\). At \(|t|=2\) the last comparison is \(37\le 64\), and \(t^6-9t^2-1\) increases on \([2,\infty)\). Thus \(n\le N\) gives \(n^{1/\log|t|}\le e^6\), and the hypothesis \(\sigma\ge 1-1/\log|t|\) gives \(n^{-\sigma}\le e^6/n\). The harmonic sum is at most \(1+\log N\le 1+6\log|t|\). Also \(|N^{1-s}/(s-1)|\le e^6/|t|\), because \(|s-1|\ge|t|\), and \(|E|\le\tfrac32 N^{-\sigma}\le\tfrac32\). Each term is \(O(\log|t|)\).

One constant \(A_5\) covers all three ranges.

Part (b), for \(|t|\ge 3\) and \(\sigma\ge 1-1/(4\log|t|)\), uses the circle of radius \(r=1/(4\log|t|)\). Since \(\log 3>1\), one has \(r<1/4\). A point \(s'\) on the circle has real part at least \(1-1/(2\log|t|)\), and
\[
|t|-r\le|\operatorname{Im}s'|\le|t|+r.
\]
The lower bound is greater than \(|t|-1/4\ge 2.75\ge 2\). The upper bound is at most \(|t|+1\), and \(|t|^2-|t|-1\ge 5\), so \(|\operatorname{Im}s'|\le|t|^2\). Therefore \(\log|\operatorname{Im}s'|\le 2\log|t|\), and
\[
1-\frac1{2\log|t|}\ge 1-\frac1{\log|\operatorname{Im}s'|}.
\]
Part (a) applies and gives \(|\zeta(s')|\le A_5\log|\operatorname{Im}s'|\le 2A_5\log|t|\). Dividing by \(r\) produces the factor \(8\). At \(|t|=3\) the radius is \(0.22756\) and the lowest imaginary part on the circle is \(2.77244\). A grid of the comparisons in (a) and (b), for \(|t|\) from \(2\) through \(10^6\) and for real parts inside the stated region, produced no failures.

**V14-006.** The large-\(s\) case has \(C=12/v\) and \(s_0\ge\log(6/v)\), so
\[
Ce^{-s_0}\le\frac{12}v\cdot\frac v6=2
\]
and \(1+Ce^{-s_0}\le 3\). The case already proved is \(S\le XV(z')(1+Ce^{-s_0})+\sum\tau(d)|r_d|\), hence \(S\le 3XV(z')+\sum\tau(d)|r_d|\). The ratio \(V(z')/V(z)\) is bounded by a constant that depends only on \(\kappa\) and \(K\). For \(1\le s<s_0\) the factor \(e^{-s}\) is larger than \(e^{-s_0}\), so a constant \(C'\) depending only on \(\kappa\) and \(K\) still absorbs the \(3\). The sample \((12/v)\exp(-\log(6/v))\) equals \(2\) for \(v=2.5\) and for \(v=7\).

**V14-007.** The exercise no longer asks why a sieve cannot produce the pairs. It asks why Corollary `cor:parity` does not forbid a sieve from producing them. The solution keeps the primitive-root argument: \(q\equiv 1\pmod 4\) gives \(p\equiv 3\pmod 8\), so \(\bigl(\frac2p\bigr)=-1\), and \(2^{(p-1)/q}=4\not\equiv 1\pmod p\) for \(p\ge 11\). For \(q\equiv 3\pmod 4\) one has \(p\equiv 7\pmod 8\), and \(2\) is a square. Infinitely many such pairs give Artin’s conjecture for \(2\) with no hypothesis on the zeros. The corollary forbids a sieve proof that the integers contain primes. The pairs \(q\) and \(2q+1\) are a pair of linear forms, the same shape as the twins. On `ffba7299` the solution pointed at “the think box above the corollary”. The think box about twins stands after the corollary, and the lists \(\lambda(n(n+2))=\pm 1\) are named in the paragraph under that box. SR-001 moves the pointer there. The upper bound of the right order is the same sieve bound the chapter records for the twins, and Exercise `ex:almostsg` is the almost-prime lower bound.

**V14-008.** The variance sum runs over \(q\le Q\) and over the \(\varphi(q)\) classes coprime to \(q\), so it has \(\sum_{q\le Q}\varphi(q)\) terms. Volume 6, Theorem 2.6 is `thm:errorterms`. Part (a) says that for \(x\ge 2\),
\[
\sum_{n\le x}\varphi(n)=\frac3{\pi^2}x^2+O(x\log x).
\]
At \(x=Q\) the error is \(O(Q\log Q)\). And \(3/\pi^2=0.30396355\ldots\), which the text writes \(0.30396\ldots\), about \(0.304\,Q^2\). The sentence on the typical size \(\sqrt{(x/q)\log x}\) is unchanged.

**Concept order.** The new appeals are to Volume 6, Proposition 1.2(b) and Theorem 2.6(a), both proved before this volume. The extension of `lem:zetaline` uses Lemma `lem:em` from Chapter 1 of this volume. Tatuzawa and Goldfeld are citations of external theorems, placed after the proofs they sharpen, and neither is used as a premise later in the chapter.

**Labels and numbering.** Against `origin/main`, the TeX files under `volume14-primes/` have the same \(369\) labels, with no additions and no removals. No numbered environment was added or removed. The counts on this tree are \(61\) theorems, \(64\) lemmas, \(10\) propositions, \(18\) corollaries, \(135\) exercises, \(5\) definitions, and \(1\) example. `python3 tools/cross_volume_citations.py` matched \(5446\) numbered statements, the same total as on main.

**Voice.** The new sentences name the range, the constant, or the list they are bounding. The blurb sentence says what is proved and then says that the Green–Tao theorem is stated without its proof. The repaired solution names the think box and the two lists.

**Downstream impacts.** None. No numbered statement changes its number. Lemma `lem:zetaline` is Lemma 3.8, and its part (a) now starts at \(|t|\ge 2\). Volume 15 does not cite Lemma 3.8. The Volume 14 statements Volume 15 does cite from the edited chapters keep the same text: Theorem 3.4 is `thm:fl`, Corollary 3.5 is `cor:rough`, and Theorem 3.11 is `thm:parity`. The small-\(s\) factor in the proof of Theorem 3.4 changed from \(2\) to \(3\); the statement still says that some \(C\) depending only on \(\kappa\) and \(K\) exists, which is the form Volume 15 quotes. The citations sit at `volume15-order-and-chance/chapters/ra-gaps.tex:14`, `ra-gaps.tex:18`, `ra-gaps.tex:80`, `ra-gaps.tex:161`, `ra-additive.tex:11`, `ra-additive.tex:94`, and `ch06-sieves.tex:188`. The Volume 13 statements Volume 14 uses near the edited proofs, including Corollary 7.5, are outside the Volume 13 diff, as the state-after comment `7077303378` records.

## Findings

**SR-001.** In the solution of `ex:sg`, the text on `ffba7299` said “the think box above the corollary”. The think box on the twins stands after Corollary `cor:parity`, and the lists \(\lambda(n(n+2))=\pm 1\) are named in the paragraph under that box. The solution now says so.

## Per-issue verdicts

| ID | Verdict |
| --- | --- |
| V14-001 | Fixed. Volume 6, Proposition 1.2(b) is Chebyshev’s bound \(\pi(y)\ll y/\log y\). With \(\xi_2=\sqrt x/\log^2 x\) it makes the medium-range error \(O(x/\log^2 x)\). |
| V14-002 | Fixed. The blurb lists the Gowers norms among the complete proofs and says the Green–Tao theorem is stated without its proof. Theorem `thm:greentao` is marked quoted, as in the preface. |
| V14-003 | Fixed. Tatuzawa’s range is \(0<\varepsilon<1/11.2\) and \(q>e^{1/\varepsilon}\), with the constant \(0.655\,\varepsilon/q^\varepsilon\) and at most one exception. The exercise still explains Siegel’s ineffectivity. |
| V14-004 | Fixed. With the triple zero, \(h(d)\ge c(\varepsilon)(\log|d|)^{1-\varepsilon}\) for a computable \(c(\varepsilon)\). The factor lost is \((\log|d|)^\varepsilon\). |
| V14-005 | Fixed. Part (a) is proved for \(\|t\|\ge 2\), in three ranges, and the circle of radius \(1/(4\log|t|)\) stays inside that region for \(\|t\|\ge 3\). The factor \(8\) is the Cauchy quotient. |
| V14-006 | Fixed. At the threshold, \(Ce^{-s_0}\le 2\), so the bound already proved is \(3XV(z')\). A constant \(C'\) depending only on \(\kappa\) and \(K\) still exists. |
| V14-007 | Fixed, after SR-001. The corollary does not forbid these pairs. The pointer now names the think box after the corollary. |
| V14-008 | Fixed. Volume 6, Theorem 2.6(a) is \(\sum_{n\le x}\varphi(n)=3x^2/\pi^2+O(x\log x)\). The value \(3/\pi^2=0.30396\ldots\) is right, and the typical size is unchanged. |

## Recomputation

```
3/pi^2 = 0.303963550927013
ln 2 = 0.6931471805599453
ln 3 = 1.0986122886681098
e^6 = 403.4287934927351
1/(4 ln 3) = 0.227560
3 - 1/(4 ln 3) = 2.772440
|t|^6 - ((|t|+4)^2+1) at |t|=2 is 27
threshold log x = 8 log log x at log x = 26.09348547661191

Hooley, explicit Chebyshev bound, ratio of the error to x/log^2 x.
The column log(qx) uses log(qx) <= log xi2 + log x.
The old column is xi2*sqrt(x)*log(x) / (x/log x), which is 1.

log x    log(xi2)/log x    ratio with log x    ratio with log(qx)    old / (x/log x)
20       0.2004            16.5286             19.8414               1
26.1     0.2500            12.0873             15.1097               1
30       0.2733            10.6444             13.5530               1
40       0.3156             8.8590             11.6545               1
60       0.3635             7.6281             10.4011               1
100      0.4079             6.7973              9.5699               1
200      0.4470             6.2024              8.9750               1

substitution (xi2/(log x/4))*sqrt(x)*log x / (4x/log^2 x) = 1
at log x = 30, 60 and 100.

(12/v)*exp(-log(6/v)) = 2 for v = 2.5 and for v = 7.

zeta comparisons: no failures on the tested grid.
```

The grid for the zeta comparisons was \(|t|\in\{2,2.1,e,3,3.5,10,100,10^6\}\) with real parts inside the stated region, and the Cauchy comparison for every tested \(|t|\ge 3\).

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume14.md` at `2691145e`.
- The state-after-Volume-K comments on PR #253, through the Volume 13 comment (`7077303378`).
- `git diff origin/main...ffba7299`, and the same diff through `673fa129`, including the proofs of `thm:hooley`, `lem:zetaline` and `thm:fl`, the Tatuzawa and Goldfeld paragraphs, the blurb, the solution of `ex:sg`, and the sentence after Theorem `thm:bdh`.
- Statement numbers from `tools/cross_volume_citations.py` on this tree: Volume 6, Proposition 1.2 is `prop:chebyshev`; Theorem 2.6 is `thm:errorterms`; Theorem 1.5 is `thm:mertens2`. Volume 14, Lemma 1.5 is `lem:em`; Theorem 3.4 is `thm:fl`; Corollary 3.5 is `cor:rough`; Lemma 3.8 is `lem:zetaline`; Theorem 3.11 is `thm:parity`; Corollary 3.12 is `cor:parity`; Theorem 3.18 is `thm:hooley`; Theorem 4.9 is `thm:bdh`. The statements were read beside the new sentences.
- Tatuzawa’s statement was compared with the form quoted in the introduction of Yong-Gao Chen, *Acta Arithmetica* 130.4 (2007), and in the introduction of the paper at doi 10.4064/aa111-4-2, and with the opening pages of *Japan. J. Math.* 21 (1951), 163–178. Goldfeld’s bound was read in *Bulletin of the AMS* 13 (1985) and in Gross–Zagier, *Inventiones* 84 (1986), §8.
- Label multiset against `origin/main`: \(369\) labels, equal. No caption command and no TikZ option is in the diff. `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- `git diff --check` on `origin/main`: clean.
- Python, as recorded under Recomputation.
- `./build.sh volume14-primes` on the source of `673fa129` exited \(0\). The layout line is `Book layout checked: 328 whole boxes, maximum height 304.8pt; no overflow or unresolved references`. `build/volume14-primes/main.log` has no line matching `undefined`, `Overfull`, or `Emergency stop`. The two warnings in that log are the `unicode-math` notes on `\overbracket`. `pdfinfo` on `dist/kdp/Volume 14 - The Primes - Print.pdf` reports \(275\) pages, page size \(513\times 738\) pts, PDF 1.3, not encrypted. The reading PDF is the cover plus that interior, \(276\) pages, at \(504\times 719.998\) pts. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that \(53\) plates were written at \(1800\) px. The EPUB is \(23\,249\,896\) bytes. The print metadata line reports \(275\) interior pages and spine \(0.6478\) in, which is the even rounding \(276\times 0.002347=0.647772\).

## Print page count

275.

## Downstream impacts

None.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V14-001 through V14-008.
- The items the Volume 14 review left unchecked: the plotted sums in `fig:bv` and `fig:bdh`, the fast-Fourier ratios for \(R(N)\), the five-squares correlation, the Kloosterman histogram, the samples in `fig:chance`, and Hardy’s identity to twenty digits.
- Acceptance of the print file by KDP.
