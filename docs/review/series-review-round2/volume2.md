# Volume 2 — The Integers

**Score: 8/10.**

The book does the job the preface announces. A reader who has Volume 1 can follow unique factorisation with the exponent rules, Euclid and Euler on the primes, Chebyshev’s bounds, Bertrand’s postulate, the Chinese remainder theorem, Hensel’s lemma, Möbius inversion, primitive roots, quadratic reciprocity, the two-square and four-square theorems, Fermat’s descent, Pell’s equation, and unique factorisation in the three Euclidean rings. The four arguments round 1 called unfinished are now proofs, or, in the orchard, a rectangle argument whose remaining step is local. The prose is a person teaching. The score stays at 8 because the sieve plate still names colours it does not draw, three repairs stop one sentence short, and a dozen other one-line reasons are still unwritten. No displayed formula checked here was false.

**Counts.** 0 critical, 0 major, 15 minor. Fifteen issues, `V2-R2-001` through `V2-R2-015`.

**Round-1 follow-up.** 47 resolved, 3 partial (`V2-005`, `V2-022`, `V2-051`), 1 open (`V2-013`), 0 regressed.

**How this was read.** Book order in `volume2-integers/main.tex`: preface and jacket; Chapter 1 Divisibility; 2 Primes; 3 Congruences; 4 Arithmetic functions; 5 Primitive roots; 6 Quadratic reciprocity; 7 Sums of squares; 8 Diophantine equations; 9 Continued fractions; 10 Gaussian and Eisenstein integers; 11 Characters; field guide and index. Every chapter file was read, including exercises, hints, and solutions. Every former major, every partial or open item, and every new issue below was re-opened in the source. The constants under “Recomputed here” were recomputed in Python in this review. Volume 6’s sentence on Voronoĭ was opened. Historical memoirs, the PDF build, and portrait files were not.

**Style, once.** The banned opener “Here we will learn” is gone. The search of this volume’s chapter files did not turn up the banned intensifiers as filler. No notebook is mentioned. Reader-facing copy does not call the book a revision.

## Issues

Paths are relative to `volume2-integers/`.

| ID | Location | Category | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| V2-R2-001 | `chapters/ch02-primes.tex:178` (`lem:binom`) | math | minor | “where the last step uses \(B\ge 2\) for \(n\ge 1\).” | The row rises up to the middle, so \(B=\binom{2n}{n}\) is at least the next entry after the end, which is \(\binom{2n}{1}=2n\ge 2\). That comparison is not written. The bound \(4^n/(2n)\le B\) is what Chebyshev quotes. |
| V2-R2-002 | `chapters/ch02-primes.tex:209` (`thm:cheb`) | math | minor | “\(\pi(x)\ge\pi(2n)\ge\frac{(x/2-1)\ln 4-\ln x}{\ln x}\).” | The integer bound just proved is \((n\ln 4-\ln(2n))/\ln(2n)\). The displayed fraction has a different numerator and a different denominator. Both changes go the right way for \(x\ge 16\), and neither comparison is written. The passage is inside the proof, which closes `V2-029`. |
| V2-R2-003 | `chapters/ch02-primes.tex:502` (`ex:factorial`) | math | minor | “we have \(p\le n<2p\), and therefore \(p^2>n\).” | From \(n<2p\) alone one does not get \(p^2>n\). Since \(p\ge 2\), one has \(p^2\ge 2p>n\). |
| V2-R2-004 | `chapters/ch03-congruences.tex:192` (`prop:lincong`) | math | minor | “Distinct values of \(j\) in this range cannot differ by a multiple of \(d\), so no two of these classes coincide.” | The classes are \(x_0+j\,n/d\). They agree modulo \(n\) exactly when \(d\) divides \(j-j'\). The range makes that difference impossible. The sentence does not name that test. |
| V2-R2-005 | `chapters/ch03-congruences.tex:171` | math | minor | “Modulo \(5\), the remainders are \(0,\pm 1,\pm 2\), and the squares are \(0,1,4\) respectively.” | In that written order the five squares are \(0,1,1,4,4\). The grouped reading is the true one: the squares of \(0\), of \(\pm 1\), and of \(\pm 2\) are \(0\), \(1\), and \(4\). Only then is \(x^2\equiv 1\) limited to \(\pm 1\). The four roots \(1,4,11,14\) modulo \(15\) were checked: each squares to \(1\). |
| V2-R2-006 | `chapters/ch06-quadratic-reciprocity.tex:753` (hint to `pb:sumsquares`) | math | minor | “Count \(N_2(c)\) by changing \(y^2=x^2-c\) into \((x-y)(x+y)=c\): there are \(p-1\) pairs for \(c\neq 0\).” | Those pairs solve \(x^2-y^2=c\), not \(x^2+y^2=c\). For \(p=7\) and \(c\neq 0\), \(N_2(c)=8\), not \(6\). The solution uses the difference count as an input to a recurrence. Say that. |
| V2-R2-007 | `chapters/ch09-diophantine.tex:21` | reference | minor | “Volume~1 proved the well-ordering principle.” | Volume 1 states it in the preface and shows it is equivalent to induction. It does not prove it. Descent may quote the axiom. |
| V2-R2-008 | `chapters/ch09-diophantine.tex:354` | math | minor | “If \(Z\) were even, both \(X\) and \(Y\) would also be even, contradicting primitiveness.” | The odd case, \(3Z^2\equiv 3\pmod 4\), is complete. The even case needs squares modulo \(4\): an even \(Z\) makes \(4\) divide \(X^2+Y^2\), and squares modulo \(4\) are \(0\) or \(1\), so both are even. |
| V2-R2-009 | `chapters/ch09-diophantine.tex:190` | prerequisite | minor | “joining the incentre to the three vertices splits the area into three triangles of height \(r\).” | The identity \((x+y-z)/2=n(m-n)\) is the algebraic check. The area decomposition is not a theorem of Volume 1 or of this chapter. The \(3\)–\(4\)–\(5\) inradius is \(1\). |
| V2-R2-010 | `chapters/ch01-divisibility.tex:847` (`pb:orchard`) | math | minor | “If those pieces overlapped only along boundaries of area zero, the sum of their areas would be at most \(1\).” | The false citation of function-convexity is gone, and the rectangle \(4AB\) is written. This overlap step is still not derived from Volume 1’s integral, which is stated for continuous functions. This is the remainder of `V2-005`. |
| V2-R2-011 | `figures/ch14-sieve.tex:32` and `:34`; caption `chapters/ch14-characters.tex:345` | figure | minor | The legend says “dark grey frame” and “ochre dot”. The frames are `ocTeal` and the dots are `ocOlive`. | The eight survivors \(1,7,11,13,17,19,23,29\) are right. Name the colours that are drawn. This is `V2-013`, still open. |
| V2-R2-012 | `chapters/ch08-continued-fractions.tex:429` (`ex:cfunique`) | exercise | minor | Part (a) asks the reader to prove that the convergents converge to the irrational with that expansion. | The solution now writes the two-step difference. `lem:cfexistence` already has the monotonicity. Ask only for the new work in part (b). This is the remainder of `V2-022`. |
| V2-R2-013 | `chapters/ch04-arithmetic-functions.tex:489` | reference | minor | “it records Voronoï's exponent \(1/3\)”. | Volume 6, Chapter 2, records \(\Delta(x)=O(x^{1/3}\log x)\), not a pure power \(x^{1/3}\). Huxley’s \(131/416\) matches. The false claim that Volume 6 replaces the \(O(\sqrt x)\) error is gone. This is the remainder of `V2-051`. |
| V2-R2-014 | `chapters/ch14-characters.tex:513` (`ex:t1-char-series`) | exercise | minor | “Prove Proposition~\ref{prop:t1-charbound}: \(\lvert A(N)\rvert\le\varphi(m)\).” | That bound is already proved in the chapter. The new work is the summation identity and the convergence of \(\sum\chi(n)/n\). |
| V2-R2-015 | `chapters/ch14-characters.tex:1496` | reference | minor | “a disk of area \(\pi(R^2-s)\)” and “with only the area formula for a circle”. | Chapter 7 now derives \(\pi\rho^2\) from the quarter-disk by the substitution \(u=\rho t\). This solution uses the general disk and does not name that paragraph. The count of the four-ball volume \(\pi^2 R^4/2\) is the right formal consequence. |

## Round-1 follow-up

| ID | Status | Evidence |
| --- | --- | --- |
| V2-001 | resolved | Lamé’s logarithm is an induction \(\varphi^{n-2}\le F_n\le\varphi^{n-1}\) at `ch01-divisibility.tex:275`. The same comparison replaces Binet in `pb:fibcoprime`. |
| V2-002 | resolved | `ex:zeros` asks only for the zeros of \(1000!\). |
| V2-003 | resolved | \(v_2(1000!)\ge 500>249\) is written. Recomputed: \(v_5(1000!)=249\). |
| V2-004 | resolved | The induction \(nd\in H\) is written at `ch01-divisibility.tex:77`. |
| V2-005 | partial | Function-convexity is gone. The overlap of positive area is `V2-R2-010`. |
| V2-006 | resolved | \(1/(n(n-1))=1/(n-1)-1/n\) is written, and the partial sum is \(1-1/N\). |
| V2-007 | resolved | The derivative of \((\ln u)/\sqrt u\) is written and is negative for \(\ln u>2\). |
| V2-008 | resolved | Cancellation is Euclid’s lemma: \(p\) does not divide \(2\). |
| V2-009 | resolved | Gauss’s lemma uses \(\rho\), not the Möbius function. |
| V2-010 | resolved | Both equalities in the case \(g(y)=0\) are written. |
| V2-011 | resolved | The empty product is named for the classes \(3\pmod 4\), \(1\pmod 4\), and \(1\pmod n\). |
| V2-012 | resolved | The range forces \(p\nmid i\). |
| V2-013 | open | `V2-R2-011`. The legend and the caption still say grey and ochre. |
| V2-014 | resolved | The race caption says the earlier plate stops at \(60\). |
| V2-015 | resolved | The index separates \(\chi\) from \(L(s,\chi)\). |
| V2-016 | resolved | The index states the Euler product for a general bounded completely multiplicative function. |
| V2-017 | resolved | The index names \(\Z[i]\), \(\Z[\omega]\), and \(\Z[\sqrt{-2}]\). |
| V2-018 | resolved | The write-up includes \(-\omega\) and \(-\omega^2\). |
| V2-019 | resolved | The tangent \(1+t\le e^t\) is named. |
| V2-020 | resolved | The solution says primitive word. |
| V2-021 | resolved | The order proposition replaces the name Lagrange. |
| V2-022 | partial | The two-step difference is in the solution. Part (a) still asks for the lemma. See `V2-R2-012`. |
| V2-023 | resolved | The square-coset exercise no longer repeats the count already proved. |
| V2-024 | resolved | The supplementary laws are written at the point of use. |
| V2-025 | resolved | `ch07-sums-of-squares.tex:283` writes \(u=\rho t\) and quotes Wallis. The later four-ball use is `V2-R2-015`, not a return of this gap. |
| V2-026 | resolved | Volume 1 now proves the two cosine sentences before `prop:sincmp`, and this volume cites that proposition for the sine roots. The value \(\pi^2/6\) at `ch14-characters.tex:279` is Volume 1’s Basel exercise, which uses that comparison. |
| V2-027 | resolved | The contradiction is the degree: \(\Phi_p\) cannot divide a nonzero polynomial of degree at most \(p-2\). |
| V2-028 | resolved | The central-binomial ratio cites the Sperner proof in Volume 1. |
| V2-029 | resolved | The passage from \(\pi(2n)\) to real \(x\) is inside the proof. The unwritten comparison is `V2-R2-002`. |
| V2-030 | resolved | The plate is described as the two classes that \(\chi_4\) will separate. |
| V2-031 | resolved | A composite has a nonzero non-unit. |
| V2-032 | resolved | A product in a field is zero only if a factor is. |
| V2-033 | resolved | The coprime-multiple step is named as Euclid’s lemma. |
| V2-034 | resolved | The product formula for \(\varphi\) cites the two-modulus step and the prime-power count. |
| V2-035 | resolved | The solution says the isomorphism iterates past two factors. The four roots modulo \(15\) are worked in the text. |
| V2-036 | resolved | The toy-RSA write-up says Euler misses \(m=5\) and \(m=11\). |
| V2-037 | resolved | The hint uses repeated squaring, not reduction modulo \(20\). |
| V2-038 | resolved | \(\binom{2p}{p}=2\binom{2p-1}{p-1}\) is written. |
| V2-039 | resolved | The step from modulo \(p\) to modulo \(p^2\) names the inverse of \(j\). |
| V2-040 | resolved | The product formula keeps the coprime hypothesis. A zero symbol still returns zero. |
| V2-041 | resolved | The confirming square is \(4^2\equiv 3\pmod{13}\). |
| V2-042 | resolved | \(2=0^2+2\cdot 1^2\) is in the write-up. |
| V2-043 | resolved | A prime dividing \(x\) and \(z\) divides \(y\). |
| V2-044 | resolved | Both routes to the contradiction are named. |
| V2-045 | resolved | Opposite parity and coprimeness are what the primitive list keeps. |
| V2-046 | resolved | Irreducibility is deferred to `thm:six`. |
| V2-047 | resolved | The angle is the name of the equation \(c^2=a^2+ab+b^2\). |
| V2-048 | resolved | A reduced rational multiplier is integral only for denominator \(1\). |
| V2-049 | resolved | The banned opener is gone, and the primes reminder has “and”. |
| V2-050 | resolved | The derivative test in \(\mathbb F_p[X]\) expands \(P=(X-a)^2Q\). |
| V2-051 | partial | The \(O(\sqrt x)\) claim is corrected. Voronoĭ’s logarithm is `V2-R2-013`. |

## Recomputed here

- \(59\cdot 509=30031\).
- \(v_5(1000!)=249\) and \(v_2(1000!)=994>249\).
- \(1766319049^2-61\cdot 226153980^2=1\).
- Lattice points of radius at most \(2\), \(6\), and \(10\): \(N(2)=13\), \(N(6)=113\), \(N(10)=317\).
- \(\varphi(72)=24\) and \(\sigma(72)=195\).

The chapter reading recomputed the other displayed constants it names (Hensel lifts, Sunzi, orders modulo \(13\), Legendre symbols, continued-fraction convergents of \(\sqrt 2\) and \(\sqrt 3\), the sieve values, and the race through \(100\)). No mismatch was reported. The samples re-opened here agree.

## Verified correct

Euclid’s lemma, the exponent rules, and Lamé’s bound were read as proofs. The empty products in the infinitude arguments are written. Chebyshev’s real-variable paragraph is inside the proof. The circle theorem writes the scaling from the unit quarter-disk. The Gauss-sum optional proof contradicts by degree. The classification of the three Euclidean rings, and the equality \(6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})\) with four non-associate irreducibles, are the statements the index now names. The handoff names Volume 3, *Symmetry: Groups, Rings and Fields*.

## Not checked

- A LaTeX build, so printed page numbers were not seen. The index numbers were matched in the source for the entries round 1 had disputed.
- EPUB rendering, portrait files, and primary memoirs.
- Every coordinate of the large plates beyond the sieve survivors, the race counts, and \(N(R)\).
- A machine check of Miller–Rabin proportions beyond the written argument.
