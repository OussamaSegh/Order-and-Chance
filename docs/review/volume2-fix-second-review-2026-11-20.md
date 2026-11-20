# Volume 2 fix, second review — 20 November 2026

Independent reading of PR #255 at `f84e09ad0d1ad2bd3a1532960ecfe0c1eaffcd2d`. The fixes were written by another agent. Corrections below are later commits on `cursor/fix-volume2-review`.

## Verdicts

**Correctness.** The original head needed changes. Seven defects are listed below. After those corrections, each of V2-001 through V2-051 is fixed in the place the issue named, or the decline of V2-013 is justified, and the fix does the job the issue asked for. Nothing extra was rewritten.

**Dropped or weakened proofs.** No numbered proof was shortened into a weaker argument. The solution of Exercise 1.3 no longer re-proves Legendre's formula; that proof remains the unnumbered proposition `prop:legendre`. The Binet formula was removed from Lamé's paragraph and from `pb:fibcoprime`, which is what V2-001 asked. The real-\(x\) half of Chebyshev's bound was moved into the proof, not deleted.

**Decline of V2-013.** Justified. `common/figure-palette.tex` sets `ocTeal` to `teal` (`#6E6A66`, dark grey) and `ocOlive` to `ForestGreen` (`#B08D57`, ochre). `docs/design/interior.md` names those inks dark grey and ochre. The book preamble and `tools/figure.tex` load the palette before the figure, so the `\providecolor` fallbacks in `figures/ch14-sieve.tex` (teal `#22675B`, olive `#5D6D65`) do not apply. The legend says "dark grey frame" and "ochre dot". The caption says the ochre dots mark the multiples of \(5\). The printed colours and the words agree. The figure file is unchanged.

**New proofs and the ledger.** The new sentences use Euclidean division, induction, the empty product, the area of a rectangle, the formal derivative rules, Wallis's quarter-disk evaluation, the cosine-zero proposition now proved in Volume 1 before `prop:sincmp`, the supplementary laws, Euclid's lemma, and the order proposition. Nothing in these repairs is used before it is introduced. The forward pointer to `thm:six` is a preview: the chapter does not use the irreducibility as a premise. Naming \(\chi_4\) in the Chapter 2 beauty note is the preview V2-030 asked for.

**Labels.** Compared with `origin/main`, the TeX files under `volume2-integers/` have the same `\label` names except the new `sym:Lseries`, which the task allows. There is no duplicate. The counts of numbered `theorem`, `proposition`, `lemma`, `corollary`, `definition`, `example` and `exercise` environments are unchanged: 44, 16, 9, 3, 5, 6 and 144.

**Caption and diagram typography.** The only caption edit is the prose of `fig:t1-race`, which V2-014 asked for. No font, weight or colour command in a plate changed. `figures/ch14-sieve.tex` is untouched.

**Recomputed numbers.** A Python session on this review recomputed the changed numbers. \(v_5(1000!)=249\) and \(v_2(1000!)=994\), so the printed lower bound \(500>249\) holds. \(10\ln 2/32\approx 0.2166<0.22\), \(\frac23\ln 2\approx 0.4621>0.46\), and \(1/512+\sqrt2/\sqrt{512}=0.06445<0.07\). \(\ln 2>1/2\), so \((\ln 2)/2>1/16\). At \(x=16\), \(8\ln 2-\ln 64=2\ln 2\). The Fibonacci bounds \(\varphi^{n-2}\le F_n\le\varphi^{n-1}\) hold for \(n\le 39\). The empty products give \(N=3\) and \(N=5\). The four \(\omega\)-coefficients are \(-1,1,1,-1\). \((15-1)(21-1)/4=70\) is even. \(23^4\equiv 1\pmod{55}\). \(4^2\equiv 3\pmod{13}\). Clearing \(t=1/3\) gives \((8,6,10)\). Cubes modulo \(4\) are \(0,1,3\).

**Voice.** The new sentences are short and concrete. The banned fillers do not appear in the diff. The orchard argument and the continued-fraction comparison are dense, and they name the object and the estimate. They were not rewritten for tone.

**Downstream impacts.** The section in the pull request is accurate, and it is complete for what later volumes feel. Exercise 1.3 is still `ex:zeros`, and it no longer states Legendre's formula. The formula is the unnumbered `propositionx` `prop:legendre`. The only later citation of Exercise 1.3 was `volume6-crossroads/chapters/ch01-mertens.tex:153`. That line now names the unnumbered proposition in Volume 2, Chapter 1. The cited sum \(\sum_{k\ge 1}\lfloor N/p^k\rfloor\) is unchanged. Other Legendre citations already say Chapter 1 or "Volume 2", and they still point at a proved formula. Gauss's lemma is still Theorem 6.3, with the count called \(\rho\). No later volume cites Volume 2's Theorem 6.3, or the letter \(\mu\), for this count. Exercise 4.8 still concludes that the coprime probability tends to \(6/\pi^2\). The citations are `volume6-crossroads/chapters/ch02-averages.tex:13` and `:544`, and `volume5-calculation/chapters/ch10-zeta.tex:462`. `sym:Lseries` is cited only from the Volume 2 index. The second-review corrections do not change a numbered statement or a later citation. The downstream section does not need a new bullet.

## Findings

| ID | Location | Problem | Fix |
| --- | --- | --- | --- |
| SR-001 | `volume2-integers/chapters/ch09-diophantine.tex`, the closing beauty paragraph; the matching reason in `docs/reviews/volume2-forward-reference-review-2026-11-04.json` | "Theorem `thm:six` in the next chapter" is the wrong chapter. Book order puts continued fractions next. `thm:six` is proved with the Gaussian and Eisenstein integers, after that. | The sentence names that later chapter and no longer says "next". The forward-reference reason matches it. The reference is still a preview, not a premise. |
| SR-002 | `volume2-integers/chapters/index.tex`, the entry for `thm:ufd` | The headword began "unique factorisation" and sat between Gauss's lemma and Gaussian primes. A reader looking up the Gaussian integers would miss the three rings the issue asked to name. | The headword is "Gaussian integers" again, and the entry names \(\Z[i]\), \(\Z[\omega]\) and \(\Z[\sqrt{-2}]\). The braces still protect the brackets inside the optional argument. |
| SR-003 | `volume2-integers/chapters/ch08-continued-fractions.tex`, solution of `ex:cfunique` | Part (a) asks for the content of `lem:cfexistence`. The solution cited that lemma for the two-step identity. "By the same comparison" did not write why the odd convergents stay above \(p_0/q_0\). | The two-step difference is added from `prop:cfconv`(b). Each even convergent is below the next odd one and at least \(p_0/q_0\), so each odd convergent is above \(p_0/q_0\). A term equal to the limit would push the next term past it. |
| SR-004 | `volume2-integers/chapters/ch06-quadratic-reciprocity.tex`, `pb:eisensine` | Equal squares of sines were turned into \(x_k=x_l\) or \(x_k=\pi-x_l\) without the injectivity on \([0,\pi/2]\). The cosine proposition supplies that increase. | The sentence says sine takes each value once on \([0,\pi/2]\), and the reflection is the only other angle in \((0,\pi)\). |
| SR-005 | `volume2-integers/chapters/ch05-primitive-roots.tex`, solution of `ex:cyclotomic` | "The same rule" attributed \(P'=nX^{n-1}\) to the product rule. The product rule had just been applied to \((X-a)^2Q\). The power rule is the other coefficient identity. | The sentence names Volume 1's formal power rule. |
| SR-006 | `volume2-integers/chapters/ch02-primes.tex`, proof of `thm:cheb` | The moved real-\(x\) paragraph says the derivative is positive for \(x\ge 16\) because \((\ln 2)/2>1/16\), and does not derive the comparison. | \(\ln 2=\int_1^2 dt/t>\int_1^2 dt/2=1/2\), so \((\ln 2)/2>1/4>1/16\). |
| SR-007 | `docs/reviews/volume2-forward-reference-review-2026-11-04.json`, the `ex:lame5` edge | The live reason still said the growth sentence uses Volume 1's Binet formula. V2-001 replaced that citation with the recurrence bound. | The reason now says the paragraph after Lamé's theorem proves the comparison from the recurrence. |

## What this review did not check

- A page-by-page visual reading of the PDF. The local `./build.sh --pdf-only volume2-integers` exited 0. The layout check reported 391 whole boxes, maximum height 371.3 pt, no overflow and no unresolved reference. The print interior is 341 pages. No page was flattened. The log has no overfull box.
- EPUB rendering and Kindle alt text.
- Portrait files and the historical memoirs named in the sequential review's "Not checked" list.
- Proofs that the diff does not touch, beyond the citation pins, the label comparison, and the passages named by V2-001 through V2-051.
- Acceptance of the print file by KDP.
