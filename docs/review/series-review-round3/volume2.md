# Volume 2 — The Integers

**Score: 8/10.**

The book does the job the preface announces. A reader who has Volume 1 can follow Euclid, the Chebyshev bounds, Bertrand’s postulate, the Chinese remainder theorem, quadratic reciprocity, the two-square and four-square theorems, descent, Pell’s equation, and unique factorisation in the three Euclidean rings. The round-2 repairs that were real gaps are now proofs. The sieve plate draws the colours its legend names. What remains is a one-line reason, a repeated exercise, and one sentence in the units proof that does not follow as written. No displayed formula recomputed here was false.

**Counts.** 0 critical, 0 major, 14 minor. Fourteen issues, `V2-R3-001` through `V2-R3-014`.

**Round-2 follow-up.** 14 resolved, 1 partial (`V2-R2-009`), 0 open, 0 regressed.

**How this was read.** Book order in `volume2-integers/main.tex`: preface and jacket; Chapter 1 Divisibility; 2 Primes; 3 Congruences; 4 Arithmetic functions; 5 Primitive roots; 6 Quadratic reciprocity; 7 Sums of squares; 8 Diophantine equations; 9 Continued fractions; 10 Gaussian and Eisenstein integers; 11 Characters; field guide and index. Every chapter file was read, including exercises, hints, and solutions. Every round-2 issue and every new row below was re-opened at the cited line on main at `68261d60`. The sieve plate was rendered with `tools/figure.tex`, which loads the book palette before the figure. The constants under “Recomputed here” were recomputed in Python, separately from the proofs. Volume 6’s Voronoĭ sentence was opened. No full LaTeX build of Volume 2 was run for this note.

**Style, once.** The blurb names Euclid, reciprocity, descent, Pell, the Gaussian and Eisenstein integers, characters, and 144 exercises, and it hands the reader to Volume 3, *Symmetry*. A count of the exercise, hint, and solution environments in the chapter files is 144 of each, which matches the blurb. No notebook is mentioned. Reader-facing copy does not call the book a revision.

## The sieve plate

Round 2 (`V2-013`, restated as `V2-R2-011`) said the frames are teal and the dots are olive, while the legend says “dark grey” and “ochre”. The figure file does draw with `ocTeal` and `ocOlive`. Those names are not the inks. `common/figure-palette.tex` is loaded by the book and by `tools/figure.tex` before the figure is read. It sets `ocTeal` to the palette’s dark grey `#6E6A66` and `ocOlive` to the palette’s ochre `#B08D57`. `\providecolor` in the figure does not replace a colour that already exists.

The plate rendered on 26 November 2026 from

```text
xelatex '\def\FIG{volume2-integers/figures/ch14-sieve}\input{tools/figure.tex}'
```

has frames near `#6C6864` and dots near `#B08C54`. A compile that skips the palette draws teal frames `#22675B` and grey-green dots `#5D6D65`. That is not the book. The legend at `figures/ch14-sieve.tex:32–34` and the caption at `chapters/ch14-characters.tex:345` match the plate the reader sees. The eight survivors \(1,7,11,13,17,19,23,29\) match \(\Phi(30,5)=8\). The legend was right.

## Issues

Paths are relative to `volume2-integers/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V2-R3-001 | `chapters/ch03-congruences.tex:78` (`prop:units`) | math | minor | “If \(n>1\) is not prime, some integer \(d\) satisfies \(1<d<n\), so \(\gcd(d,n)>1\).” | The “so” does not follow. For \(n=4\), \(d=3\) lies strictly between \(1\) and \(4\) and is coprime to \(4\). A composite has a positive divisor in that range, and then the gcd is that divisor. The conclusion, that a composite modulus is not a field, is true. |
| V2-R3-002 | `chapters/ch02-primes.tex:280` | math | minor | “the quotient is at most \(10\ln 2/32<0.22\). … \(\frac23\ln 2>0.46\).” | The three comparisons are true and unproved. The bound \(\ln 2>1/2\) is not strong enough for \(\frac23\ln 2>0.46\). The derivative of \((\ln u)/\sqrt u\) is written and is the repaired step from round 1. |
| V2-R3-003 | `chapters/ch02-primes.tex:242` | math | minor | “because \(\ln x\le\sqrt x\) eventually.” | Volume 1 gives \(\ln x\le 4(x^{1/4}-1)\). That is at most \(\sqrt x\) once \(x\ge 256\). The comparison is not written. |
| V2-R3-004 | `chapters/ch01-divisibility.tex:634` (`ex:lame5`) | math | minor | “Since \(\varphi^5>10\).” | The chapter has \(\varphi^2=\varphi+1\), so \(\varphi^5=5\varphi+3\). This exceeds \(10\) once \(\sqrt5>9/5\), and \(1.8^2=3.24<5\). The value is about \(11.090\). |
| V2-R3-005 | `chapters/ch01-divisibility.tex:849` (`pb:orchard`) | math | minor | “Those edges are the images of lattice vectors under an orthogonal change of axes.” | An orthogonal matrix sends the standard basis to unit vectors, not to edges of lengths \(A\) and \(B\). The next sentence is the step the area uses: \(Q^{\mathsf T}Q=I\) gives \((\det Q)^2=1\). The overlap argument at line 851 is written and closes `V2-R2-010`. |
| V2-R3-006 | `chapters/ch04-arithmetic-functions.tex:440` | math | minor | “\(\ln(\sqrt x/m)\le(\sqrt x-m)/m\).” | With \(t=\sqrt x/m\ge 1\) this is \(\ln t\le t-1\). Volume 1 proves it by the mean value theorem. This proof does not name it. |
| V2-R3-007 | `chapters/ch04-arithmetic-functions.tex:567` | style | minor | The prime-factor solution writes \(\log\), while the hyperbola theorem in the same chapter writes \(\ln\). | Both denote the natural logarithm. One sentence should say so. The Voronoĭ sentence at line 489 uses the same \(\log\). |
| V2-R3-008 | `chapters/ch05-primitive-roots.tex:826` | math | minor | “Both identities follow by matching the simple roots and degrees of monic polynomials.” | \(\Phi_m(-X)\) has leading coefficient \((-1)^{\varphi(m)}\). It is monic because \(\varphi(m)\) is even for odd \(m>1\). That parity is not named. The identity \(\Phi_6(X)=\Phi_3(-X)\) is true. |
| V2-R3-009 | `chapters/ch06-quadratic-reciprocity.tex:380` | math | minor | “\(=\bigl(\frac{8}{29}\bigr)=-1\). … \(\bigl(\frac{2}{29}\bigr)=-1\) because \(29\equiv 5\pmod 8\).” | The chain is correct and the symbol is \(-1\). The reduction \(\bigl(\frac{8}{29}\bigr)=\bigl(\frac{4}{29}\bigr)\bigl(\frac{2}{29}\bigr)=\bigl(\frac{2}{29}\bigr)\) is not written. |
| V2-R3-010 | `chapters/ch06-quadratic-reciprocity.tex:1268` (`pb:eisensine`) | math | minor | “The leading coefficients add to \((-1)^{(q-1)/2}\sum_{j\text{ odd}}\binom{q}{j}\).” | The value is right. Replacing \(\cos^{q-j}x\) by \((1-\sin^2 x)^{(q-j)/2}\) contributes a second sign. Added to the de Moivre sign, that is \((-1)^{(q-1)/2}\) for every odd \(j\). The addition is not written. |
| V2-R3-011 | `chapters/ch09-diophantine.tex:198` | math | minor | “The distance from \((r,r)\) to the hypotenuse is \(r\).” | The inner product with the unit normal \((y/z,x/z)\) is \(-r\). The absolute value of that inner product is the distance, by the orthogonal projection in Volume 1. That sentence is not written. The algebraic value \(r=n(m-n)\) is right, and the \(3\)–\(4\)–\(5\) inradius is \(1\). This is the remainder of `V2-R2-009`. |
| V2-R3-012 | `chapters/ch10-gaussian-eisenstein.tex:486` (`ex:zsqrt5`) | exercise | minor | “show that \(2\), \(3\), \(1\pm\sqrt{-5}\) are irreducible and pairwise non-associate.” | Theorem `thm:six` at line 228 already proves that. The new work is that \(2\) is irreducible but not prime, which the paragraph after the theorem already states. |
| V2-R3-013 | `chapters/ch14-characters.tex:1223` | math | minor | “Then \(A,B\) have the same parity (check their squares modulo \(4\)).” | The check is real and not written. Squares modulo \(4\) are \(0\) or \(1\), and \(27\equiv -1\pmod 4\), so \(A^2\equiv B^2\pmod 4\). |
| V2-R3-014 | `chapters/ch14-characters.tex:1628` | math | minor | “for \(4\mid n\) its contribution has normalised density \(\frac14\delta_2(n/4)\).” | A nonprimitive vector is twice another, so the factor is \(2^{-2}\). The odd-prime case derives \(p^{-2}\) earlier. The factor for \(2\) is not repeated. The closed form \(3\cdot 2^{-a}\) matches Jacobi’s formula. |

## Round-2 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V2-R2-001 | resolved | `ch02-primes.tex:174` The row rises up to the middle, so \(B\ge\binom{2n}{1}=2n\ge 2\). |
| V2-R2-002 | resolved | `ch02-primes.tex:207–214` The numerator and the logarithm are compared separately, and \(\ln(2n)\le\ln x\) uses the mean value theorem. |
| V2-R2-003 | resolved | `ch02-primes.tex:509` “A prime is at least \(2\), so \(p^2\ge 2p>n\).” |
| V2-R2-004 | resolved | `ch03-congruences.tex:189–192` The classes agree modulo \(n\) exactly when \(d\) divides \(j-j'\), and that difference lies in \(\{1,\ldots,d-1\}\). |
| V2-R2-005 | resolved | `ch03-congruences.tex:171` The square of \(0\) is \(0\), both members of \(\pm 1\) square to \(1\), and both members of \(\pm 2\) square to \(4\). |
| V2-R2-006 | resolved | `ch06-quadratic-reciprocity.tex:752–754` The pairs solve \(x^2-y^2=c\), not \(x^2+y^2=c\), and that count is an input to \(N_2(c)\). |
| V2-R2-007 | resolved | `ch09-diophantine.tex:21–23` “Volume 1 takes the well-ordering principle as an axiom… Descent quotes the axiom.” |
| V2-R2-008 | resolved | `ch09-diophantine.tex:362` If \(Z\) is even then \(4\) divides \(X^2+Y^2\), and an integer square is \(0\) or \(1\) modulo \(4\), so both are even. |
| V2-R2-009 | partial | The area split is gone. The inner product is computed at `ch09-diophantine.tex:194–198`, and the distance sentence is `V2-R3-011`. |
| V2-R2-010 | resolved | `ch01-divisibility.tex:851–852` If the pieces met only along boundaries, the chord lengths in each slab would sum to at most \(1\), and the order rule would bound the area by \(\int_0^1 1\,\mathrm dx=1\). The false clause about lattice edges is `V2-R3-005`. |
| V2-R2-011 | resolved | The rendered plate matches the legend and the caption. See the sieve section above. Round 2 compared the unused `\providecolor` fallbacks with the legend. |
| V2-R2-012 | resolved | `ch08-continued-fractions.tex:428` The exercise says `lem:cfexistence` already gives the convergence, and asks for \(\varphi\) and \(\sqrt 3\). |
| V2-R2-013 | resolved | `ch04-arithmetic-functions.tex:489` “Voronoï's bound \(\Delta(x)=O(x^{1/3}\log x)\)” and Huxley’s \(131/416\). Volume 6, Chapter 2, states the same bound. |
| V2-R2-014 | resolved | `ch14-characters.tex:513` “The bound \(\lvert A(N)\rvert\le\varphi(m)\) is Proposition `prop:t1-charbound`.” The exercise asks for the summation identity. |
| V2-R2-015 | resolved | `ch14-characters.tex:1495` The disk of radius \(\rho\) has area \(\pi\rho^2\) by scaling the quarter-disk in `thm:circle`. |

## Recomputed here

- \(59\cdot 509=30031\).
- \(v_5(1000!)=249\) and \(v_2(1000!)=994\). The text uses the weaker bound \(v_2(1000!)\ge 500\).
- \(1766319049^2-61\cdot 226153980^2=1\).
- Lattice points of radius at most \(2\), \(6\), and \(10\): \(N(2)=13\), \(N(6)=113\), \(N(10)=317\).
- \(\varphi(72)=24\) and \(\sigma(72)=195\).
- Sieve survivors in \(\{1,\ldots,30\}\) coprime to \(30\): \(1,7,11,13,17,19,23,29\).
- \(\varphi^5\approx 11.090\).

## Verified correct

Euclid’s lemma, the real-variable step in Chebyshev’s bound, and the circle theorem’s scaling from the quarter-disk were read as proofs. The empty product in the infinitude argument for primes \(3\pmod 4\) is the case that makes \(N=3\). Gauss’s lemma counts with \(\rho\), not \(\mu\). The classification in `thm:six` proves the four factors irreducible and not associates across the equation. The handoff names Volume 3, *Symmetry: Groups, Rings and Fields*.

## Not checked

- A LaTeX build of the whole volume, so printed page numbers were not seen. The sieve comparison is the rendered plate, not a page of the book PDF.
- EPUB rendering, portrait files, and primary memoirs.
- A current table of the Fermat numbers \(F_5,\ldots,F_{32}\).
- Nielsen’s count of ten prime factors. The exercise itself only proves three.
