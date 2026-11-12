# Second review of PR #187

**Verdict: REQUEST CHANGES**

**Head reviewed:** `95b2005e0338fa5c151abb32997590fd29956058` on `cursor/volume1-apply-scored-read-a273`.

**Pull request:** https://github.com/OussamaSegh/Order-and-Chance/pull/187

**Source log:** PR #172, `docs/review/volume1-independent-scored-read-2026-11-11.md`, rows V1-01 through V1-35, scored at `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f`.

This review was written without pushing to that branch and without merging it. The diff was read at the head above, in a detached worktree. The row statuses claimed in the pull request are accurate. The Volume 5 chapter pointers into Volume 1 are not.

## What was run

All of the following were run on the tree at `95b2005e`.

- `python3 tools/cross_volume_citations.py` exited 1 and printed `214 citation mismatches`. None of those lines is a citation of Volume 1. The script's own count of Volume 1 citations is 191 (176 chapter, 10 theorem, 4 exercise, 1 proposition), which matches the pull request.
- From `tools/`, `python3 -m unittest test_cross_volume_citations.py -v` ran 4 tests and exited 0. That includes `test_volume1_numbers_match_the_statements_later_volumes_cite` and `test_resolved_volumes_have_no_mismatch`.
- `python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1178}` and exited 0.
- `./build.sh volume1-first-principles` exited 0. XeLaTeX was the three passes inside that script. `build/volume1-first-principles/main.log` has no line containing `Overfull` and no line containing `undefined`. The same log does contain underfull boxes. `tools/check_book_layout.py`, as reported by the build, checked 422 whole boxes, maximum height 507.4 pt, and reported no overflow and no unresolved references.
- `pdfinfo` on `build/volume1-first-principles/main.pdf`: 463 pages, 504 × 720 pt, PDF 1.5.
- `pdfinfo` on `dist/kdp/Volume 1 - First Principles - Print.pdf`: 463 pages, 513 × 738 pt, PDF 1.3, encrypted no. The build log's own line is `KDP interior checked: 463 pages, PDF 1.3`.
- `pdfinfo` on `dist/Volume 1 - First Principles.pdf`: 464 pages, 504 × 719.998 pt. That file is the cover plus the 463-page interior.
- The index in `volume1-first-principles/chapters/index.tex` has 114 `\ocindexpage` entries. Every label is a `\newlabel` in `main.aux`. Every numbered entry's theorem, proposition, lemma, corollary, or exercise number agrees with `cross_volume_citations.number_volume(1)`. For each of the 114 folios, the PDF page whose label is that folio contains the named statement. The six folios named in the pull request are the aux pages, and the text is on those labeled pages: even and odd on folio 4, the five-agreements example on folio 72, Exercise 1.7 on folio 74, Theorem 6.4 on folio 242, Exercise 6.7 on folio 261, Theorem 8.6 on folio 330.
- Simpson's rule for `\int_0^1 e^{-x^2}\,dx`, computed here with the composite rule and `math.erf`, gives an error of `1.187\times 10^{-13}` for 512 panels. The plate's last mark is `1.190\times 10^{-13}`. The ratio of the mark at 128 to that mark is 16, which is the slope the caption states.
- The EPUB `dist/Volume 1 - First Principles.epub` is 32,505,992 bytes (31.0 MiB). In `EPUB/text/ch002.xhtml` the preface plate is `oc-plate-preface-two-questions.png` with alt text `Left: the first four values agree, and so does n=10. Right: one way four guests can each receive someone else's hat.` The package has no `alt="image"`. The `img` style is `width:100%;max-width:100%;height:auto`.

The full `unittest discover -s tools` run of 629 tests claimed in the pull request was not repeated here. The citation tests and `registers.py` were.

## Printed chapter numbers

`volume1-first-principles/main.tex` sets `\setcounter{chapter}{-1}` and then inputs the chapters in this order. The printed numbers follow.

| Printed | Chapter |
|---|---|
| 0 | The Language of Mathematics |
| 1 | Sums, Binomials and Induction |
| 2 | Counting and Discrete Reasoning |
| 3 | Sequences, Series and Limits |
| 4 | Orders |
| 5 | Complex Numbers and Roots of Unity |
| 6 | Polynomials |
| 7 | Linear Algebra |
| 8 | Differential and Integral Calculus |
| 9 | Inequalities, Convexity and Estimates |
| 10 | First Probability |

Volume 5, in the rewrite that this head merged from `main`, numbers the language chapter as Chapter 1. Each of its chapter pointers into Volume 1 is one higher than the printed number, except the fast-multiplication sentence, which is two higher. The cited numbers 2 through 10 all exist, which is why `cross_volume_citations.py` accepts them: a chapter citation fails only when the number is absent. Volume 4's pointers that were sampled, including Bolzano--Weierstrass as Chapter 3, use the printed numbers.

`volume5-calculation/chapters/ch03-series.tex:20` cites Volume 1, Exercise 6.7. The aux label `ex:basel` is exercise 6.7. That sentence is the V1-04 repair, and it is right. It is not in the log below.

## Issue log

| ID | Location | Problem | Required fix |
|---|---|---|---|
| V5-01 | `volume5-calculation/chapters/ch01-finite.tex:273` | Cites Volume 1, Chapter 7. The subject is two polynomials that agree at enough points are the same polynomial. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-02 | `volume5-calculation/chapters/ch01-finite.tex:567` | Cites Volume 1, Chapter 3. The subject is inclusion-exclusion. That is printed Chapter 2 (Counting). | Cite Chapter 2. |
| V5-03 | `volume5-calculation/chapters/ch02-generating.tex:65` | Cites Volume 1, Chapter 3. The subject is stars and bars. That is printed Chapter 2 (Counting). | Cite Chapter 2. |
| V5-04 | `volume5-calculation/chapters/ch02-generating.tex:165` | Cites Volume 1, Chapter 4. The subject is Cauchy product of absolutely convergent series. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-05 | `volume5-calculation/chapters/ch02-generating.tex:242` | Cites Volume 1, Chapter 4. The subject is H_n = ln n + gamma + o(1). That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-06 | `volume5-calculation/chapters/ch02-generating.tex:927` | Cites Volume 1, Chapter 7. The subject is multiplicity of a root. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-07 | `volume5-calculation/chapters/ch02-generating.tex:1310` | Cites Volume 1, Chapter 9. The subject is inverse-function derivatives; Volume 1 derives arctan, and the word arcsin does not occur. That is printed Chapter 8 (Calculus). | Cite Chapter 8, and name arctan (or the inverse-function rule). Volume 1 does not treat arcsin. |
| V5-08 | `volume5-calculation/chapters/ch02-generating.tex:1332` | Cites Volume 1, Chapter 4. The subject is alternating harmonic series. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-09 | `volume5-calculation/chapters/ch02-generating.tex:1358` | Cites Volume 1, Chapter 9. The subject is sin' = cos and cos' = -sin, stated in the preface and repeated in the calculus reminder. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-10 | `volume5-calculation/chapters/ch04-integrals.tex:42` | Cites Volume 1, Chapter 4. The subject is Bolzano-Weierstrass. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-11 | `volume5-calculation/chapters/ch04-integrals.tex:145` | Cites Volume 1, Chapter 9. The subject is Gaussian integral from the Wallis integrals. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-12 | `volume5-calculation/chapters/ch04-integrals.tex:506` | Cites Volume 1, Chapter 6. The subject is geometric sums of roots of unity. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-13 | `volume5-calculation/chapters/ch04-integrals.tex:564` | Cites Volume 1, Chapter 4. The subject is Euler's constant. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-14 | `volume5-calculation/chapters/ch04-integrals.tex:569` | Cites Volume 1, Chapter 4. The subject is alternating harmonic series equals log 2. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-15 | `volume5-calculation/chapters/ch04-integrals.tex:575` | Cites Volume 1, Chapter 4. The subject is Euler's constant and the alternating harmonic series. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-16 | `volume5-calculation/chapters/ch04-integrals.tex:614` | Cites Volume 1, Chapter 4. The subject is intermediate value theorem (Theorem 3.7). That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-17 | `volume5-calculation/chapters/ch05-gamma.tex:95` | Cites Volume 1, Chapter 10. The subject is weighted AM-GM from the concavity of ln. That is printed Chapter 9 (Inequalities). | Cite Chapter 9. |
| V5-18 | `volume5-calculation/chapters/ch05-gamma.tex:161` | Cites Volume 1, Chapter 4. The subject is Euler's constant (Proposition 3.17). That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-19 | `volume5-calculation/chapters/ch05-gamma.tex:178` | Cites Volume 1, Chapter 9. The subject is Stirling with the constant sqrt(2 pi) (Theorem 8.6). That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-20 | `volume5-calculation/chapters/ch05-gamma.tex:178` | Cites Volume 1, Chapter 4. The subject is Stirling's shape with an unspecified constant (Proposition 3.18). That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-21 | `volume5-calculation/chapters/ch05-gamma.tex:395` | Cites Volume 1, Chapter 9. The subject is Wallis integrals. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-22 | `volume5-calculation/chapters/ch05-gamma.tex:480` | Cites Volume 1, Chapter 6. The subject is product of sines. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-23 | `volume5-calculation/chapters/ch05-gamma.tex:617` | Cites Volume 1, Chapter 2. The subject is binomial coefficients (the binomial theorem is in the sums chapter). That is printed Chapter 1 (Sums). | Cite Chapter 1. |
| V5-24 | `volume5-calculation/chapters/ch05-gamma.tex:656` | Cites Volume 1, Chapter 8. The subject is eigenvalues. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-25 | `volume5-calculation/chapters/ch05-gamma.tex:675` | Cites Volume 1, Chapter 7. The subject is division of polynomials. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-26 | `volume5-calculation/chapters/ch06-fourier.tex:46` | Cites Volume 1, Chapter 10. The subject is Cauchy-Schwarz (Theorem 9.4). That is printed Chapter 9 (Inequalities). | Cite Chapter 9. |
| V5-27 | `volume5-calculation/chapters/ch06-fourier.tex:87` | Cites Volume 1, Chapter 9. The subject is Riemann-Lebesgue exercise. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-28 | `volume5-calculation/chapters/ch06-fourier.tex:662` | Cites Volume 1, Chapter 6. The subject is complex numbers. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-29 | `volume5-calculation/chapters/ch06-fourier.tex:691` | Cites Volume 1, Chapter 6. The subject is modulus. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-30 | `volume5-calculation/chapters/ch07-fft.tex:19` | Cites Volume 1, Chapter 7, for a promise that polynomials and large integers can be multiplied in time `O(n\log n)`. The sentence Volume 1 prints is in the complex chapter, `ch02-complex-roots.tex:643`: Volume 5 turns the filter into a fast way to multiply polynomials. Printed Chapter 5. Chapter 7 is two above that. | Cite Chapter 5, and match that sentence. |
| V5-31 | `volume5-calculation/chapters/ch07-fft.tex:261` | Cites Volume 1, Chapter 6. The subject is quadratic Gauss sum. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-32 | `volume5-calculation/chapters/ch07-fft.tex:305` | Cites Volume 1, Chapter 6. The subject is circulant determinant. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-33 | `volume5-calculation/chapters/ch07-fft.tex:496` | Cites Volume 1, Chapter 6. The subject is circulant determinant as a value of a polynomial. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-34 | `volume5-calculation/chapters/ch07-fft.tex:554` | Cites Volume 1, Chapter 6. The subject is roots of unity. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-35 | `volume5-calculation/chapters/ch07-fft.tex:554` | Cites Volume 1, Chapter 8. The subject is determinants. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-36 | `volume5-calculation/chapters/ch07-fft.tex:585` | Cites Volume 1, Chapter 6. The subject is complex numbers and rotations. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-37 | `volume5-calculation/chapters/ch07-fft.tex:611` | Cites Volume 1, Chapter 6. The subject is rotations. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-38 | `volume5-calculation/chapters/ch07-fft.tex:611` | Cites Volume 1, Chapter 8. The subject is diagonalisation. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-39 | `volume5-calculation/chapters/ch07-fft.tex:670` | Cites Volume 1, Chapter 6. The subject is roots of unity. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-40 | `volume5-calculation/chapters/ch07-fft.tex:712` | Cites Volume 1, Chapter 8. The subject is Vandermonde determinant (Proposition 7.4). That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-41 | `volume5-calculation/chapters/ch07-fft.tex:726` | Cites Volume 1, Chapter 8. The subject is Vandermonde determinant. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-42 | `volume5-calculation/chapters/ch09-complex.tex:110` | Cites Volume 1, Chapter 4. The subject is Cauchy product. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-43 | `volume5-calculation/chapters/ch09-complex.tex:111` | Cites Volume 1, Chapter 6. The subject is Euler's formula. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-44 | `volume5-calculation/chapters/ch09-complex.tex:322` | Cites Volume 1, Chapter 7. The subject is d'Alembert's minimum of |P| (Theorem 6.4). That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-45 | `volume5-calculation/chapters/ch10-zeta.tex:150` | Cites Volume 1, Chapter 4. The subject is Euler's constant. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-46 | `volume5-calculation/chapters/ch10-zeta.tex:483` | Cites Volume 1, Chapter 4. The subject is alternating harmonic series equals log 2. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-47 | `volume5-calculation/chapters/ch11-asymptotics.tex:64` | Cites Volume 1, Chapter 9. The subject is x^K e^{-x} tends to 0. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-48 | `volume5-calculation/chapters/ch11-asymptotics.tex:186` | Cites Volume 1, Chapter 4. The subject is H_n - ln n tends to gamma. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-49 | `volume5-calculation/chapters/ch11-asymptotics.tex:265` | Cites Volume 1, Chapter 9. The subject is Stirling's formula for N!. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-50 | `volume5-calculation/chapters/ch11-asymptotics.tex:778` | Cites Volume 1, Chapter 4. The subject is series. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-51 | `volume5-calculation/chapters/ch11-asymptotics.tex:778` | Cites Volume 1, Chapter 9. The subject is expansion of ln(1-x). That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-52 | `volume5-calculation/chapters/ch12-agm.tex:1033` | Cites Volume 1, Chapter 6. The subject is roots-of-unity filter. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-53 | `volume5-calculation/chapters/ch12-agm.tex:1046` | Cites Volume 1, Chapter 6. The subject is roots-of-unity filter. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-54 | `volume5-calculation/chapters/ch12-agm.tex:1067` | Cites Volume 1, Chapter 8. The subject is Gram-Schmidt. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-55 | `volume5-calculation/chapters/ch12-agm.tex:1072` | Cites Volume 1, Chapter 8. The subject is determinants and Gram-Schmidt. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-56 | `volume5-calculation/chapters/ch12-agm.tex:1072` | Cites Volume 1, Chapter 9. The subject is Stirling with the constant. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-57 | `volume5-calculation/chapters/ch12-agm.tex:1117` | Cites Volume 1, Chapter 8. The subject is block matrices. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-58 | `volume5-calculation/chapters/ch12-agm.tex:1207` | Cites Volume 1, Chapter 7. The subject is Lagrange interpolation. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-59 | `volume5-calculation/chapters/ch12-agm.tex:1439` | Cites Volume 1, Chapter 9. The subject is e is irrational (Exercise 8.4). That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-60 | `volume5-calculation/chapters/ch12-agm.tex:1464` | Cites Volume 1, Chapter 9. The subject is integrals of rational functions. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-61 | `volume5-calculation/chapters/ch12-agm.tex:1488` | Cites Volume 1, Chapter 9. The subject is Taylor series. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-62 | `volume5-calculation/chapters/ch12-agm.tex:1569` | Cites Volume 1, Chapter 8. The subject is diagonalisation. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-63 | `volume5-calculation/chapters/ch12-agm.tex:1687` | Cites Volume 1, Chapter 7. The subject is a nonzero polynomial of degree d has at most d roots. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-64 | `volume5-calculation/chapters/ch12-agm.tex:1687` | Cites Volume 1, Chapter 8. The subject is symmetric matrices. That is printed Chapter 7 (Linear algebra). | Cite Chapter 7. |
| V5-65 | `volume5-calculation/chapters/ch12-agm.tex:1715` | Cites Volume 1, Chapter 6. The subject is multiple-angle form of cosine and sine. Volume 1 does not define the phrase trigonometric polynomial. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5 for the multiple-angle form. Volume 1 has no section titled trigonometric polynomials. |
| V5-66 | `volume5-calculation/chapters/ch12-agm.tex:1715` | Cites Volume 1, Chapter 7. The subject is the degree bound, applied on the circle, and the Chebyshev polynomials. That is printed Chapter 6 (Polynomials). | Cite Chapter 6. |
| V5-67 | `volume5-calculation/chapters/ch12-agm.tex:1783` | Cites Volume 1, Chapter 6. The subject is roots of unity. That is printed Chapter 5 (Complex numbers). | Cite Chapter 5. |
| V5-68 | `volume5-calculation/chapters/ch12-agm.tex:1820` | Cites Volume 1, Chapter 9. The subject is Stirling with the constant. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-69 | `volume5-calculation/chapters/ch12-agm.tex:1848` | Cites Volume 1, Chapter 4. The subject is absolute convergence and products. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |
| V5-70 | `volume5-calculation/chapters/ch12-agm.tex:1885` | Cites Volume 1, Chapter 9. The subject is inverse functions. That is printed Chapter 8 (Calculus). | Cite Chapter 8. |
| V5-71 | `volume5-calculation/chapters/ch12-agm.tex:1936` | Cites Volume 1, Chapter 4. The subject is sequences and comparison with integrals. That is printed Chapter 3 (Sequences). | Cite Chapter 3. |


## Rows V1-01 through V1-35

The claimed status is the status in the pull request. The decision is this review's. Theorem, proposition, lemma, corollary, definition, example, and exercise environments were compared, file by file, with `main` at `5cc8858e`. The sequences agree, so those counters did not move. The index numbers agree with the same walker. Figure edits are the cross, the division brace, the equioscillation window, the gamma colour name, the gamma integrand, and the last Simpson mark, together with the two captions those rows name. No font size, font family, or diagram label was changed beyond that.

| ID | Claimed | Decision | What the head actually does |
|---|---|---|---|
| V1-01 | fixed | fixed | Before the minimum, a sequence in the closed disc stays in the disc, and `\|P(z)-P(w)\|` is at most `C\|z-w\|` on the disc. Bolzano--Weierstrass and the reverse triangle inequality are already in earlier chapters. |
| V1-02 | fixed | fixed | After the real power rule, induction gives the derivative of `x^n` and of `(x-a)^n` on all of `\mathbb R`. Proposition 6.2(c) points there. |
| V1-03 | fixed | fixed | The new index has 114 folios. Each one matches the PDF, as recorded above. |
| V1-04 | fixed | fixed | Volume 5 names Exercise 6.7 and no longer says Volume 1 promised five further proofs. |
| V1-05 | fixed | fixed | `kdp.md` no longer says journey. The sentence names the subjects. |
| V1-06 | fixed | fixed | The built EPUB uses the preface sentence as the alt text. |
| V1-07 | not fixed | not fixed | `volume4-chance/chapters/bibliography.tex:24` still says Volume 1, Chapter 8, for the Riemann integral. |
| V1-08 | fixed | fixed | Mutual exclusion uses the fact that twice an integer is never 1. Exhaustiveness is division by 2 from the well ordering the preface states. The parity-sum solution cites that example. |
| V1-09 | fixed | fixed | The real square root of 2 is a later theorem. The word continuous is gone. |
| V1-10 | fixed | fixed | The cross is `MidnightBlue`, which the figure palette sets to `#151516`, centred on the axis at 2. |
| V1-11 | fixed | fixed | The brace runs from the coordinate of `2b` to `a`. The sentence under the line is gone. |
| V1-12 | fixed | fixed | A finite list has an lcm by repeating the two-integer case, and the exponent of each prime is the maximum. The harmonic solution cites that rule. |
| V1-13 | fixed | fixed | The sums chapter does not call Binet proved. The field guide uses `\sqrt5` only after the sequences chapter has defined the real power. |
| V1-14 | fixed | fixed | The solution writes `(n+1)(n+2)=n^2+3n+2>n^2`. |
| V1-15 | fixed | fixed | Heron's formula is derived from an altitude and the school Pythagorean theorem, which the text says this volume does not re-prove. The algebra from `a^2-b^2` to the four factors was checked. The solution cites the formula. |
| V1-16 | fixed | fixed | The first term matches the geometric series, and every later term is strictly smaller, including the case `q=1`. |
| V1-17 | fixed | fixed | The last Simpson mark is `1.190\times 10^{-13}`. The caption says the abscissa counts pairs of panels, so 256 means 512 panels. The recomputed error is `1.187\times 10^{-13}`. |
| V1-18 | fixed | fixed | The `x=1/2` curve starts at `t=0.28`, where `t^{-1/2}e^{-t}` is about 1.428, inside a window that stops at 1.5. The caption says that ink is not the whole area `\Gamma(1/2)`. |
| V1-19 | fixed | fixed | Both associations are identified with one expanded polynomial. Expanding `(z_1 z_2)z_3` and `z_1(z_2 z_3)` produces that polynomial. |
| V1-20 | fixed | fixed | `P(a)=0` implies `(X-a)` divides `P`, from `X^m-a^m`, before the roots of unity are removed one at a time. The chapter has already recorded that `\mathbb C` is a field. |
| V1-21 | fixed | fixed | The binomial theorem expands powers of `(X-a)+a`. The word basis is gone. |
| V1-22 | fixed | fixed | The proof inserts `(Sx)^{\mathsf T}u=x^{\mathsf T}S^{\mathsf T}u=x^{\mathsf T}Su` before the hyperplane is called stable. The transpose-of-a-product step is the same move the proof already used for the conjugate. |
| V1-23 | fixed | fixed | For odd `n`, `k` is paired with `k+n`. Opposite parity and the same gcd with `n` give `\varphi(2n)=\varphi(n)`. |
| V1-24 | fixed | fixed | The window runs up to 1.35 and marks the height 1. The plotted point `(1,1)` lies inside it. |
| V1-25 | fixed | fixed | `\ln x\to\infty` and the power limits are proved from the standing bijection and the monotonicity of `\exp` before they are used. The case `\alpha\le 0` is written. The harmonic series is not used in that argument. |
| V1-26 | fixed | fixed | A continuous derivative on `[a,b]` is bounded by the extreme value theorem, so the integral from `x` to `y` is at most `K\|y-x\|`. The integral from `a` to `a` is taken to be 0. `H` is continuous on the closed interval, and Theorem 3.10(c) applies with derivative zero on the open interval. |
| V1-27 | fixed | fixed | The epsilon bound from the difference quotient is written before the sequential characterisation. |
| V1-28 | fixed | fixed | The text cites `\sin'(0)=\cos 0=1` and says the sine-and-tangent proposition does not name the limit. |
| V1-29 | fixed | fixed | `\inf S=-\sup(-S)` is defined before the convergence criteria. |
| V1-30 | fixed | fixed | The series is drawn in a colour named `ochre`, aliased to `ForestGreen`, which the palette sets to `#B08D57`. The coordinates are unchanged. |
| V1-31 | not fixed | not fixed | At `8b8a5be` and at this head, `ch02-counting.tex:410` is `\binom60+\binom51+\binom42+\binom33=1+5+6+1=13`, with no opening bar. |
| V1-32 | fixed | fixed | The rank is the increasing coordinate. Mirsky's pigeonhole is on the `m` level sets, and the `n^2` boxes are the pairs. |
| V1-33 | fixed | fixed | Suk's bound is the sentence: for every fixed `\varepsilon>0`, the ratio of the upper bound to `2^n` is eventually smaller than `2^{\varepsilon n}`. |
| V1-34 | fixed | fixed | The product is called the same bookkeeping as the binomial theorem, with `t^j` in place of a repeated factor `t`. |
| V1-35 | fixed | fixed | The solution shows the values of `\tau` are distinct, then says an injective map from a finite set to itself is bijective. |

The new sentences are short and name the object. They do not open with an outline, and they do not use the hollow intensifiers the house voice bars. One clause in the quantifier repair talks about the sentence itself ("this sentence does not call that function continuous"). The mathematical repair is still the one V1-09 asked for.

## Scope

Fonts, sizes, and text inside diagrams stay as they were, apart from the colour name `ochre` and the cross, brace, window, and clipped curve that V1-10, V1-11, V1-17, V1-18, V1-24, and V1-30 require. The two changed captions are those two figure rows. `kdp.md` loses the word journey and does not gain a new claim.
