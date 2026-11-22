# Volume 12 fix, second review — 22 November 2026

Independent reading of PR #265. The fixes were written by another agent. The head under review was `84335e2cc171036f81d7fd9756fbd5a08dcfcc64`. This reading found no defect in the four repairs or in the regression-test edit. No source file was changed. This log is the following commit on `cursor/fix-volume12-review`.

The issue list is `docs/review/series-sequential-review/volume12.md` on `cursor/series-sequential-review` at `2691145e6a366f1ed2cbc6968802ad899f7069de`. The state-after-Volume-K comments on PR #253 were read through the Volume 11 comment (`7074828097`). `origin/main` for this reading is `8d33ce292fbf079121acbfa9ef8259d53554bef8`.

## Verdicts

**Correctness.** All four repairs stand as written. Each of V12-001 through V12-004 is fixed in the place the issue named. No issue was declined. No numbered statement was shortened, and no proof was replaced by a citation of a result that does not say what the sentence claims.

**V12-001.** The paragraph before Theorem `thm:zeroset` now separates the two measure statements. For \(t>0\), \(B_t\) is Gaussian, so \(P(B_t=0)=0\). The dyadic step functions \(B^{(m)}_t=B_{2^{-m}\lfloor 2^m t\rfloor}\) are jointly measurable, continuous paths give \(B^{(m)}\to B\) at every \(t\), and the limit \((t,\omega)\mapsto B_t(\omega)\) is jointly measurable. The integrand \(\mathbf 1_{\{B_t=0\}}\) is non-negative. Volume 7, Theorem 9.5 is `thm:tonelli`: for \(\sigma\)-finite measures and a non-negative product-measurable function, the integral over the product equals either repeated integral. Lebesgue measure on \([0,\infty)\) and the probability \(P\) are \(\sigma\)-finite, so
\[
\mathbb E\lambda(\mathcal Z)=\int_0^\infty P(B_t=0)\,dt=0.
\]
A single time \(t=0\) does not change the Lebesgue integral. Thus \(\mathcal Z\) has Lebesgue measure zero almost surely.

Volume 4, Exercise 12.3 is `ex:zeros`, the third exercise of `ch11-brownian.tex`, which is Chapter 12. The exercise asks for outer length zero, for the absence of isolated points, and then for uncountability. Its solution covers the zero set on \([0,1]\) by dyadic intervals whose total length tends to zero, and it says the argument avoids Tonelli. The same solution builds an injection from the infinite binary sequences into that zero set, using closedness and the absence of isolated points proved inside the solution. The Volume 12 paragraph cites the exercise for that covering argument. The proof of Theorem `thm:zeroset` still shows that no point of \(\mathcal Z\) is isolated, by the rational restarts and Corollary `cor:oscillate`. Uncountability is the injection: the zero set on \([0,1]\) is uncountable almost surely, and \(\mathcal Z\) contains it. The abstract sentence, that every non-empty closed set without isolated points is uncountable, is not attributed to the exercise.

**V12-002.** In Theorem `thm:kolmcont` the distance is the max norm, and \(s,t\in D_n\) are neighbours when \(|t-s|\le 2^{-n}\). The chaining hypothesis is \(|t-s|\le 2^{-m}\) with \(s,t\in D\). Each coordinate of \(2^ms\) and \(2^mt\) then differs by at most \(1\). If \(x\le y\le x+1\), then \(\lfloor x\rfloor\le\lfloor y\rfloor\le\lfloor x\rfloor+1\), because \(\lfloor x\rfloor\le y\) and \(y<x+1<\lfloor x\rfloor+2\). Applied to each ordered pair of coordinates, the level-\(m\) grid points \(s_m\) and \(t_m\) differ by at most \(2^{-m}\) in the max norm, so they are neighbours in \(D_m\). The comparison is stated only at scale \(m\). The successive points \(s_n,s_{n+1}\) remain neighbours in \(D_{n+1}\), since each coordinate of the difference is \(0\) or \(2^{-n-1}\). The displayed telescoping sum is unchanged. Each link at level \(n+1\) is at most \(2^{-\gamma(n+1)}\), and
\[
2\sum_{n\ge m}2^{-\gamma(n+1)}=2^{-\gamma m}\cdot\frac{2}{2^\gamma-1},
\]
so the constant \(c_\gamma=1+2/(2^\gamma-1)\) still matches the union bound.

**V12-003.** Exercise `ex:nonunique` asks which hypothesis of Theorem `thm:yamada` fails for \(\mathrm dX=3X^{1/3}\,\mathrm dt+3X^{2/3}\,\mathrm dB\). The Itô calculation \(\mathrm d(B^3)=3B^2\,\mathrm dB+3B\,\mathrm dt\) is unchanged, and with real cube roots it is the equation for \(X=B^3\). The zero process is a solution because both coefficients vanish at \(0\). Theorem `thm:yamada` assumes a Lipschitz drift and \(|\sigma(x)-\sigma(y)|\le K\sqrt{|x-y|}\). The diffusion coefficient \(3x^{2/3}\), read with the real square of the cube root, is locally \(\frac12\)-Hölder near \(0\): on \([-1,1]\), \(\bigl||x|^{2/3}-|y|^{2/3}\bigr|\le|x-y|^{2/3}\), and \(|x-y|\le 2\) turns the exponent \(\frac23\) into a multiple of \(|x-y|^{1/2}\). The drift \(3x^{1/3}\) fails the Lipschitz test at \(0\), because
\[
\frac{|3x^{1/3}|}{|x|}=3|x|^{-2/3}
\]
is unbounded as \(x\to 0\). The ordinary equation \(x'=3x^{2/3}\) is named on its own. Its right-hand side is the diffusion coefficient. The zero function satisfies it, and so does \(x(t)=t^3\): for every integer \(t\), \((t^3)'=3t^2=3(t^3)^{2/3}\) under the real power \((t^3)^{2/3}=(t^2)\).

**V12-004.** Exercise `ex:v12girsanovL2` assumes \(|\theta_s|\le C\) and asks for \(\mathbb EZ_T^2\le e^{C^2T}\). The identity \(\frac12|2\theta_s|^2=2\theta_s^2\) gives
\[
Z_T^2=\exp\Bigl(\int_0^T 2\theta_s\,\mathrm dB_s-\frac12\int_0^T|2\theta_s|^2\,\mathrm ds\Bigr)\exp\Bigl(\int_0^T\theta_s^2\,\mathrm ds\Bigr).
\]
The second factor is at most \(e^{C^2T}\). Theorem `thm:itoloc`, with \(\langle B\rangle_t=t\) from Chapter 3, makes \(M_t=\int_0^t 2\theta_s\,\mathrm dB_s\) a continuous local martingale, zero at \(0\), with \(\langle M\rangle_t=\int_0^t|2\theta_s|^2\,\mathrm ds\). The bracket formula is part of that theorem because it includes Proposition `prop:itoprops`. Proposition `prop:expmartgen` says that \(\mathcal E^1(M)\) is a positive continuous local martingale and a supermartingale. The value at time \(0\) is \(1\). The solution of Exercise `ex:superm` gives \(\mathbb E M_t\le\mathbb E M_0\) for a non-negative continuous local martingale, so \(\mathbb E\mathcal E^1(M)_T\le 1\). The first factor is \(\mathcal E^1(M)_T\) and is non-negative, so
\[
\mathbb EZ_T^2\le e^{C^2T}.
\]
The argument uses the supermartingale bound. It does not treat the exponential for \(2\theta\) as a martingale, and it does not use the conclusion of Theorem `thm:girsanov`. The proof of that theorem is where this \(L^2\) bound is spent, in order to reach the martingale property of \(Z\). The last sentence of the solution points at the hypothesis \(|\theta|\le C\) in the theorem, which is the same bound the exercise assumes. The hint states the same factorisation and the same appeal to `prop:expmartgen`.

**Concept order.** The new appeals are to tools already proved. Tonelli is Volume 7, Theorem 9.5. The zero-set exercise is Volume 4, Exercise 12.3, and its solution does not cite Volume 12. The Girsanov estimate uses Theorem `thm:itoloc` and Proposition `prop:expmartgen` from Chapter 4, and the supermartingale exercise from Chapter 3.

**Labels and numbering.** Against `origin/main`, the TeX files under `volume12-random-motion/` have the same 378 labels, with the same multiplicities. The environment counts are unchanged: 143 exercises, 69 theorems, 37 lemmas, 29 propositions, 21 corollaries, 12 definitions, and 4 examples. No `\label` line, no caption, and no figure or TikZ option is in the diff. Theorem `thm:zeroset`, Theorem `thm:kolmcont`, and the two exercise statements are unchanged. Theorems 10.4, 10.10, and 10.11 remain `thm:sinekernel`, `thm:ksmoments`, and `thm:logclt` in `ch10-cue.tex`, which the diff does not touch.

**Recomputed numbers.** A separate Python session, using exact `Fraction` arithmetic for the comparisons that are identities:

- If \(|u-v|\le 1\), then \(|\lfloor u\rfloor-\lfloor v\rfloor|\le 1\). Integer parts from \(-40\) to \(40\), fractional parts \(0,1/2,1/3,2/3,999/1000,1/1000,1/7\), together with the boundary \(y=x+1\): 8876 pairs, no failures.
- The old comparison fails one scale finer: \(m=1\), \(n=3\), \(s=0\), \(t=1/2\) gives \(|2^3(t-s)|=4\), and the floors are \(0\) and \(4\).
- For \(m=0,\ldots,7\) and a grid of times in \([0,1]\) with \(|t-s|\le 2^{-m}\), the level-\(m\) floors differ by at most \(1\) and the grid points are neighbours: 10088 pairs, no failures.
- For each integer \(t\) from \(0\) to \(20\), and each integer \(t\) from \(-12\) to \(-1\) with the real cube root, \((t^3)'=3t^2=3(t^3)^{2/3}\). The zero function satisfies \(x'=3x^{2/3}\). No failures.
- At \(x=10^{-k}\), the cube of the drift quotient is \(27\cdot 10^{2k}\), equal to \(2700, 270000, 27000000, 2700000000, 270000000000, 27000000000000\) for \(k=1,\ldots,6\).
- For each integer \(\theta\) from \(-12\) to \(12\), \(\frac12(2\theta)^2=2\theta^2\). No failures.
- For each pair \((A,Q)\) in \(\{(3,5),(-4,2),(0,7),(11,0),(2,8),(-5,-3)\}\), the exponent identity \(2A-Q=(2A-2Q)+Q\) holds.
- On \([-1,1]\), five thousand random pairs satisfied \(\bigl||x|^{2/3}-|y|^{2/3}\bigr|\le 2|x-y|^{1/2}\).

**Voice.** The new sentences name the integral, the grid points, the drift quotient, or the exponential factor. The changed paragraphs stay in the same register as the surrounding proofs.

**Downstream impacts.** None. No label, statement number, or cited claim changes. `python3 tools/cross_volume_citations.py` matched 5446 numbered statements, the same count recorded after Volume 11. Later volumes cite Volume 12, Theorems 10.4, 10.10, and 10.11, and Volume 12, Chapters 9, 10, and 11. Those chapters are outside the diff. The lines checked are `volume14-primes/chapters/ch14-critical.tex` (Chapter 10 and Theorem 10.4), `volume15-order-and-chance/chapters/ch09-gue.tex` (Theorem 10.4), `ch14-meeting.tex` (Theorems 10.4 and 10.10), `ra-moments.tex` (Theorems 10.10 and 10.11), and `ra-selberg.tex` (Theorem 10.11).

The state-after comments name several statements whose contents moved in earlier volumes. Volume 12 does not cite Volume 2’s `prop:legendre`, Volume 3’s `prop:cyclodegree` or `prop:solids`, Volume 4’s `lem:tree`, `lem:sector`, or Theorem 13.1, Volume 5’s `cor:cotagain` or Theorem 6.17, or the constant removed from Volume 6’s `ex:twoomega`. It does cite Volume 1, Theorem 7.9. On current main that theorem is `thm:spectral`: a real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors. The appendix uses it for the real eigenvalues of the Laplacian. The state-after comment for Volume 1 records that this statement was left unchanged.

## Findings

none

## Per-issue verdicts

| ID | Verdict |
| --- | --- |
| V12-001 | Fixed. The integral of \(P(B_t=0)\) is Tonelli’s theorem, Volume 7, Theorem 9.5, after the dyadic argument for joint measurability. Volume 4, Exercise 12.3 is cited for the covering proof of outer length zero and for the injection of binary sequences into the zero set on \([0,1]\). |
| V12-002 | Fixed. The neighbour comparison in the proof of `thm:kolmcont` is only at scale \(m\). If two reals differ by at most \(1\), their integer parts differ by at most \(1\). |
| V12-003 | Fixed. The drift \(3x^{1/3}\) fails the Lipschitz test because \(3|x|^{-2/3}\) is unbounded at \(0\). The ordinary equation \(x'=3x^{2/3}\) has the diffusion coefficient as its right-hand side, and the solutions \(0\) and \(t^3\). |
| V12-004 | Fixed. \(\mathbb EZ_T^2\le e^{C^2T}\) follows from the supermartingale bound on the exponential of \(\int 2\theta\,\mathrm dB\), in Proposition `prop:expmartgen`, and from \(|\theta|\le C\). The solution does not call that exponential a martingale. |

## Test-file change

Justified. It does not weaken the regression.

`tools/test_volume4_phase2_downstream_references.py` guards Volume 4’s downstream Brownian references. `test_missing_exercise_subparts_cannot_be_cited_as_proved_claims` reads Exercise `ex:zeros` and `volume12-random-motion/chapters/ch02-paths.tex`. On `origin/main` it required the sentence “Exercise~12.3, where this consequence is proved”. That sentence is the mis-citation V12-001 removes: the exercise proves outer length zero and the injection, and it does not state the abstract perfect-set theorem. Keeping the old assertion would have forced the false citation back into the chapter.

The edit replaces that one assertion with three pins of the corrected sentences, and with an assertion that the old sentence is absent. The checks that remain are the ones that guard Volume 4: the exercise body contains no `enumerate`, so it has no subparts; `ch02-paths.tex` does not cite Exercise 12.3(a) or 12.3(c); and the joint-measurability sentences in the solution of `ex:fast` are still present, including \(B^{(m)}(t,\omega)=B_{2^{-m}\lfloor 2^m t\rfloor}\). A separate test still scans every later volume for a citation of a lettered subpart of Exercise 12.3. The file’s three tests pass.

## Checks

- `git show origin/cursor/series-sequential-review:docs/review/series-sequential-review/volume12.md` at `2691145e6a36`.
- The state-after-Volume-K comments on PR #253, through the Volume 11 comment (`7074828097`).
- `git diff origin/main...84335e2c`, and the full surrounding proofs: Theorem `thm:kolmcont`; the zero-set section through the proof of Theorem `thm:zeroset`; Exercise `ex:v12girsanovL2`, its hint, and its solution; Theorem `thm:girsanov`; Proposition `prop:expmartgen`; Theorem `thm:itoloc`; the solution of Exercise `ex:superm`; Theorem `thm:yamada`; Exercise `ex:nonunique` and its solution.
- Statement numbers from `tools/cross_volume_citations.py` on this tree, which matches `origin/main` outside the five files in the diff: Volume 7, Theorem 9.5 is `thm:tonelli`; Volume 4, Exercise 12.3 is `ex:zeros`; Volume 1, Theorem 7.9 is `thm:spectral`. The statements of Tonelli, of Exercise 12.3, and of its solution were read beside the new paragraph. The solution of Exercise 12.3 does not cite Volume 12.
- Label multiset and environment counts against `origin/main`. No caption, figure, or TikZ line is in the diff. `python3 tools/cross_volume_citations.py`: `Cross-volume citations match 5446 numbered statements.`
- `python3 tools/test_volume4_phase2_downstream_references.py`: 3 tests, all passing.
- `git diff --check` on `origin/main...84335e2c`: clean.
- Python, as recorded under recomputed numbers.
- `./build.sh volume12-random-motion` on `84335e2c` exited 0. The layout line is `Book layout checked: 362 whole boxes, maximum height 320.5pt; no overflow or unresolved references`. `build/volume12-random-motion/main.log` has no line matching `undefined`, `Overfull`, or `Emergency stop`. `pdfinfo` on `dist/kdp/Volume 12 - Random Motion - Print.pdf` reports 255 pages, page size 513 × 738 pts, PDF 1.3. The reading PDF is the cover plus that interior, 256 pages, at 504 × 720 pts. The build printed that the EPUB figures are full width and that the math images carry an em baseline, and that 44 plates were written at 1800 px. The EPUB is 20,744,429 bytes. Pandoc warned on `\rm` in the unchanged solution of the resistance exercise in `ch08-networks.tex`; the build still exited 0. The print metadata records 255 interior pages. The spine width 0.6008 in is the even rounding \(256\times 0.002347\), applied to the cover, with no page added to the manuscript.

## Print page count

255.

## Downstream impacts

None.

## What this review did not check

- A page-by-page visual reading of the PDF.
- Kindle rendering of the EPUB, beyond the build’s media check.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V12-001 through V12-004.
- The items the Volume 12 review left unchecked: the \(1000\times 1000\) Gaussian matrix behind the semicircle histogram, the sample maximum \(5.62\) of \(\log|Z_{1000}|\), and the printed range \(0.31\) to \(0.44\) for the mean excess.
- Acceptance of the print file by KDP.
