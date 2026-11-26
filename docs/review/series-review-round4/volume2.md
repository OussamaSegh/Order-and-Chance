# Volume 2 — The Integers

**Score: 9/10.**

The round-3 repairs hold, including the composite modulus, the Bertrand decimals, the inradius, and the exercise that now cites Theorem `thm:six`. Euclid’s rectangle, Erdős’s comparison for Bertrand, the hyperbola count, the lifting of primitive roots, Eisenstein’s sine proof, Lagrange’s descent, the continued-fraction trap, Fermat’s fourth-power descent, and the cube descent in \(\Z[\omega]\) were read as proofs and hold. Two sentences still skip a direction or a numerical comparison.

**Counts.** 0 critical, 0 major, 2 minor. `V2-R4-001` and `V2-R4-002`.

**Round-3 follow-up.** 14 resolved, 0 partial, 0 open, 0 regressed. `V2-R2-009` is closed: the unit normal is \(u\), and \(n\) in \(r=n(m-n)\) is still the integer parameter.

**How this was read.** Book order in `volume2-integers/main.tex`, on main at `e5a2a929`. Every chapter file was read, including exercises, hints, solutions, and captions. Each new row was opened at the cited line. No full LaTeX build was run. The sieve plate was not re-rendered; round 3 already matched it to the book palette, and this round did not edit the plate.

## Issues

Paths are relative to `volume2-integers/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V2-R4-001 | `chapters/ch01-divisibility.tex:201` | minor | “\(a\mid bc\Longleftrightarrow (a/g)\mid c\).” The next sentence proves only the forward direction, by dividing by \(g\) and applying Euclid to \(a'\mid b'c\). | The converse is the substitution \(c=(a/g)k\), so \(bc=a(b/g)k\). |
| V2-R4-002 | `chapters/ch03-congruences.tex:1319` | minor | “\(\lvert K(a)\rvert<2^{1/4}p^{3/4}<1.19\,p^{3/4}\). … It is sharper for every odd prime \(p\ge 5\): the inequality holds at \(p=5\), and \((p-1)/p^{3/4}\) increases with \(p\).” | Neither \(2^{1/4}<1.19\) nor the value at \(p=5\) is computed, and the increase is not shown. Both numerical claims are true. |

## Round-3 follow-up

The composite modulus takes a positive divisor, so \(d=3\) and \(n=4\) is not a case of the sentence. Bertrand’s three comparisons use \(0.693147<\ln 2<0.693148\). For \(x\ge 256\), \(\ln x\le\sqrt x\) follows from \(\ln u\le u-1\). Lamé’s solution derives \(\varphi^5=5\varphi+3\) and \(\sqrt5>9/5\) from \((9/5)^2=81/25<5\). The orchard proof says an orthogonal change sends the standard basis to unit vectors. The hyperbola estimate names \(\ln t\le t-1\). In that chapter \(\log\) means \(\ln\). \(\Phi_m(-X)\) is monic for odd \(m>1\) because \(\varphi(m)\) is even. The symbol \(\bigl(\frac{8}{29}\bigr)\) reduces by \(\bigl(\frac{4}{29}\bigr)=1\). The two signs in the sine expansion add to \((q-1)/2\). The inradius is \(\lvert v\cdot u\rvert\). Exercise `ex:zsqrt5` cites `thm:six`. The parity of \(A\) and \(B\) uses squares modulo \(4\). The nonprimitive density contributes \(2^{-2}\).

## Not checked

- A LaTeX build.
- A fresh render of the sieve plate.
- Journal pages and the Jacobi triple product cited from `pb:ramanujan5`.
