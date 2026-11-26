# Volume 2 round-3 fix, second review — 26 November 2026

Independent reading of the Volume 2 fix at `91833f198265da9c3431574f1538aac632c125f8`, on `cursor/fix-v2-round3-3de4`, based on `main` at `68261d60`. The first commit was `a1761835`. The corrections below are the later commit. The reader of this note did not write the first commit.

## Verdicts

**Correctness.** The first commit left two defects, listed below. After `91833f19`, each of `V2-R3-001` through `V2-R3-014` is fixed in the sentence the round-3 log named, and `V2-R2-009` is closed. The second reading of the correction commit closed both defects and found no new false step.

**Dropped or weakened proofs.** No numbered proof was shortened. The solution of `ex:zsqrt5` no longer repeats the proof of Theorem `thm:six`. It cites that theorem and then proves the two conclusions the exercise still asks for: unique factorisation fails, and `2` is irreducible but not prime. The area argument in `pb:orchard` no longer calls the edges images of lattice vectors. The determinant identity `(\det Q)^2=1` remains the reason the area is unchanged.

**Labels.** Compared with `68261d60`, the TeX files under `volume2-integers/` have the same `\label` names. No numbered environment was added or removed. Exercise `ex:zsqrt5` keeps its label.

**Caption and diagram typography.** No plate was edited.

**Voice.** The new sentences name the object and the step. The banned fillers do not appear in the diff.

**Recomputed here.** The Bertrand products are exact terminating decimals, from Volume 1's bounds `0.693147<\ln 2<0.693148`. `10\cdot 0.693148=6.93148` and `6.93148\cdot 50=346.574<352=0.22\cdot 32\cdot 50`. `2\cdot 0.693147=1.386294` and `1.386294\cdot 50=69.3147>69=0.46\cdot 3\cdot 50`. `33\cdot 100=3300<3584=7\cdot 512`. `(9/5)^2=81/25<5`.

## Findings, closed in `91833f19`

| ID | Location | Problem | Fix |
| --- | --- | --- | --- |
| SR-001 | `ch09-diophantine.tex`, the inradius paragraph | The unit normal was called `n`, and the next clause is `r=n(m-n)`. After that definition, `n` was a vector. | The unit normal is `u=(y/z,x/z)`. The residual is `(v\cdot u)u`, so the distance is `|v\cdot u|=r`. The integer parameter in `r=n(m-n)` is unchanged. This closes `V2-R2-009`. |
| SR-002 | `ch01-divisibility.tex`, solution of `ex:lame5` | `\varphi>7/5` was not shown to be the same inequality as `\sqrt5>9/5`. | From `\varphi=(1+\sqrt5)/2`, multiplying by `2` gives `1+\sqrt5>14/5`, and subtracting `1` gives `\sqrt5>14/5-1=9/5`. |

## Issue-by-issue

| ID | Where the repair sits |
| --- | --- |
| V2-R3-001 | `ch03-congruences.tex`, `prop:units`. A positive divisor `d` of a composite `n>1` satisfies `1<d<n` and `\gcd(d,n)\ge d>1`. The integer `3` with `n=4` is no longer used as if every such integer met the modulus. |
| V2-R3-002 | `ch02-primes.tex`, Bertrand's proof. The three comparisons are the products above. |
| V2-R3-003 | `ch02-primes.tex`. Volume 1 gives `\ln u\le u-1`, so `\ln x\le 4(x^{1/4}-1)`, and for `x\ge 256` this is at most `\sqrt x`. |
| V2-R3-004 | `ch01-divisibility.tex`, solution of `ex:lame5`. Closed by SR-002. |
| V2-R3-005 | `ch01-divisibility.tex`, solution of `pb:orchard`. An orthogonal matrix sends the standard basis to unit vectors. The area factor is `1`. |
| V2-R3-006 | `ch04-arithmetic-functions.tex`, the hyperbola theorem. `\ln t\le t-1` is named, including `t=1`. |
| V2-R3-007 | `ch04-arithmetic-functions.tex`, the Voronoĭ sentence. In this chapter `\log` means the natural logarithm. |
| V2-R3-008 | `ch05-primitive-roots.tex`, solution of `pb:phipm1`. `\Phi_m(-X)` has leading coefficient `(-1)^{\varphi(m)}`, and `\varphi(m)` is even for odd `m>1` by the pairing already proved in the chapter. |
| V2-R3-009 | `ch06-quadratic-reciprocity.tex`. `\bigl(\frac{8}{29}\bigr)=\bigl(\frac{4}{29}\bigr)\bigl(\frac{2}{29}\bigr)` and `\bigl(\frac{4}{29}\bigr)=1`. |
| V2-R3-010 | `ch06-quadratic-reciprocity.tex`, solution of `pb:eisensine`. The two signs add to `(-1)^{(q-1)/2}` for every odd `j`. |
| V2-R3-011 | `ch09-diophantine.tex`. Closed by SR-001. |
| V2-R3-012 | `ch10-gaussian-eisenstein.tex`, `ex:zsqrt5`. The exercise cites `thm:six` and asks for the failure of unique factorisation and for the proof that `2` is not prime. |
| V2-R3-013 | `ch14-characters.tex`. Squares modulo `4` are `0` or `1`, and `27\equiv -1\pmod 4`, so `A` and `B` have the same parity. |
| V2-R3-014 | `ch14-characters.tex`, solution of `pb:densities`. Four coordinates scaled by `2`, against the normalisation `2^6`, give the factor `2^{-2}`. |

## What this review did not check

- A LaTeX build. XeLaTeX is not installed in the review environment.
- EPUB rendering.
- Proofs the diff does not touch, beyond the sentences needed to see that each repair cites an earlier result.
