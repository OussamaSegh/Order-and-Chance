# Second review of the Volume 5 and Volume 6 scored-read fixes

12 November 2026. This pass reads the diffs against the two issue logs. It is not the writer pass.

Heads reviewed:

- Volume 5 in-volume: `1cc4048a746939e763b4f07ba3f3797976cb606d` (pull request 208)
- Volume 6 in-volume: `cf892434e31e0f42f1fb58f41ce8afeb29f53415` (pull request 209)
- Downstream citations: `6a835372f357a54943f6824daab43d281d4a1a56` (pull request 210)

A number that was changed was recomputed, or counted from the source with examples included in the shared counter. A citation was accepted only when the statement at the new number is the statement the sentence uses.

## Volume 5, in the volume

| ID | Severity | Fix that was read | Verdict |
|---|---|---|---|
| V5-M7 | major | Three pointers, not one: the introduction, the homology remark, and the Jensen lead. Each now says Volume 8, Chapter 22. Chapter 14 of that book is *Inequalities between Matrices*. | Accept |
| V5-M8 | major | Continuity is in `lem:approxid`, in `thm:ftinversion`, and in `thm:plancherel`, whose proof calls inversion. A jump is excluded in the lemma because the proof chooses \(\delta\) from continuity. | Accept |
| V5-M9 | major | The boxed inequality stays on second moments about the origin. The paragraph after it builds \(g(x)=e^{-2\pi i\nu x}f(x+m)\) and applies the theorem to \(g\). The Fourier calculation was re-read: translation multiplies the transform by \(e^{2\pi im\xi}\), and the modulation shifts the frequency by \(\nu\). | Accept |
| V5-M10 | major | \(d=999999\) keeps `26C65E52`; \(d=10^6\) begins `6C65E52`. Recomputed with an integer scaled by \(16^{20}\). The same routine returns `243F6A88` at \(d=0\). | Accept |
| V5-M11 | major | The parameter proof is the second. Volume 4, Chapter 5 is described as taking the value from Volume 1. The Beta evaluation is then named as the third route, so the two chapters no longer disagree. | Accept |
| V5-m1 | minor | Pallas is the orbit; Juno remains as a dating clue. The chapter already cites Heideman, Johnson and Burrus. | Accept |
| V5-m2 | minor | “as is the original” is gone. The original multiplicities are stated. | Accept |
| V5-m3 | minor | \(H_0=0\) is in the definition, and the sum that starts at 0 is named. | Accept |
| V5-m4 | minor | \([n=0]\) is defined in the sentence that uses it. | Accept |
| V5-m5 | minor | The cross-family check is the rearrangement \((r+s)(3(r-s)-1)=0\). It was expanded again and is right. | Accept |
| V5-m6 | minor | The caption no longer states the three-gap theorem. It reports the sixty gaps in the picture. Font and node geometry were not touched. | Accept |
| V5-m7 | minor | The 2026 argument is named and marked as not reproduced. The Archive of Formal Proofs entry *Zeta_5_Irrational* (Hyman, 26 October 2026) was opened. The closed form of \(\zeta(3)\) is still described as unknown. | Accept |
| V5-m8 | minor | The exercise excludes \(s=1\). The solution already did. | Accept |
| V5-m9 | minor | The curve label is \(0.4433\). \(1/C+C/48=0.44328798\ldots\). Position and font unchanged. | Accept |
| V5-m10 | minor | Volume 7, Theorem 7.11. `jordan.tex` is Chapter 6 and `ch06-measures.tex` is Chapter 7; `thm:lebesgue` is the 11th numbered statement of that chapter. | Accept |
| V5-m11 | minor | Blurb and KDP text match the preface: theorems are proved, quoted results are marked, and Rademacher is named. The partition formula is in the KDP list. | Accept |
| V5-m12 | minor | Both hypotheses of `cor:dct` are said to fail. | Accept |
| V5-m13 | minor | The list is \(-i,-1,i,1\), the order of the cases \(n\equiv 1,2,3,0\). Each value was checked against \((1+i)(1+i^{-n})/2\). | Accept |
| V5-m14 | minor | The index counts examples, so Cauchy’s theorem is 9.9 and Laplace’s method is 11.9. The sources list points back at the chapter lists. | Accept |

## Volume 6, in the volume

| ID | Severity | Fix that was read | Verdict |
|---|---|---|---|
| V6-01 | minor | Eight digits, \(0.26149721\). The partial sum to \(10^7\) was recomputed as \(0.2614972158\). | Accept |
| V6-02 | minor | The converse is quoted, with Titchmarsh, Chapter 14, and Exercise 7.3 named as the proved direction. The theorem number 14.25(C) was not copied in, because it was not re-opened in the book. | Accept |
| V6-03 | minor | The Taylor remainder is uniform on \(|t|\le A\), which is the hypothesis Volume 4’s theorem asks for. | Accept |
| V6-04 | minor | The variables are built by successive splittings of \([0,1]\). A finite pattern is one interval, so Hoeffding and Borel–Cantelli apply to it. | Accept |
| V6-05 | minor | “Landscape” is gone. | Accept |
| V6-06 | minor | A section *Closing problems* follows `ex:heckebound`, which is the sixth exercise. Exercise numbers are unchanged. | Accept |
| V6-07 | minor | The cover sentence now separates the proved gaps from the quotation. The generated About the Cover file matches the JSON. | Accept |
| V6-15 | minor | The box prints \(2\log 4\). The factor \(2\) is \(2\theta(x)/\log x\) with \(\theta(x)<x\log 4\). | Accept |
| V6-16 | minor | The expectation divides by \(n!\). | Accept |
| V6-17 | minor | \(3.3\) is \(\log\log(10^9)+M\). \(3.0\) is named as the main term. | Accept |
| V6-18 | minor | The piece on \((0,\delta\log 2)\) is estimated by \(\int_0^1|\log u|\,du=1\). | Accept |
| V6-19 | minor | \(0.308\) is the difference of the two higher-power contributions. | Accept |
| V6-20 | minor | The caption says the \(99.59\%\) is conditional. The remark still names the hypotheses. | Accept |
| V6-21 | minor | Theorem 2.4 is the product and the lower bound. The upper bound is the paragraph after it, which does print \(\pi(x)<\sqrt x+2\ln 4\cdot x/\ln x\). | Accept |
| V6-22 | minor | Euclid’s lemma is named, and it is the lemma in Volume 2, Chapter 1. | Accept |
| V6-23 | minor | Schur for existence, Murty for the obstruction. | Accept |
| V6-24 | minor | The reciprocity sign is written and cancelled. | Accept |
| V6-25 | major | The opening lists the product, the count, and the critical line, in the order the closing already used. Infinitude is `cor:infinitezeros`. | Accept |
| V6-26 | major | The opening display is \(\psi_0\) with the symmetric limit, and the proof is said to give `cor:exactexplicit`. The half-step at a prime is stated. | Accept |
| V6-27 | minor | The series is \(-L'/L=-0.24561\). The closed form stays positive. | Accept |
| V6-28 | minor | The quantifier “for every \(\varepsilon>0\)” is in the solution, and one \(\varepsilon\) is said to give only \(\beta\le\frac12+\varepsilon\). | Accept |
| V6-29 | minor | Littlewood’s proof is no longer said to rest on the conditional display. | Accept |
| V6-30 | minor | The zero-free input is \(\log(T+2)\), and \(\log T/\log(T+2)\to 1\) is absorbed into \(c\). | Accept |
| V6-31 | minor | The sum is over \(\gamma\neq 0\), and the positive frequencies are named as such. | Accept |
| V6-32 | minor | The caption says the ordinates are computed sign changes of \(Z(t)\). | Accept |
| V6-33 | minor | About 11% of the main term, and 12% of \(x/\log x\). The exercise says the same. | Accept |
| V6-34 | minor | \(m\) runs from \(2-H\) to \(N\). That range has \(N+H-1\) integers, and each \(z_n\) for \(1\le n\le N\) occurs for exactly \(H\) values of \(k\). | Accept |
| V6-35 | minor | The Graham–Ringrose factors are restored. The remark stays quoted. | Accept |
| V6-36 | minor | Proposition 6.7 is cited for the standard normal, and \(sZ\) supplies the variance. | Accept |
| V6-37 | minor | The odd harmonic sum is written as \(\frac12\log Y+O(1)\). | Accept |
| V6-38 | minor | The exercise requires \(x/q\ge 3\). | Accept |
| V6-39 | minor | \(\ln\) in that exercise is now \(\log\). | Accept |
| V6-40 | minor | The model and the primes disagree. Maier’s theorem is still quoted, not proved. | Accept |
| V6-41 | minor | The four quoted bounds are in remarks. | Accept |
| V6-42 | minor | Ramanujan proved the congruence. The other two are conjectures in the opening, as the next sentences already said. | Accept |
| V6-43 | minor | The two named solutions, and the same interchange in the central-binomial solution, use a finite sum and a tail. The tools line no longer says Volume 1 fails to prove the step. | Accept |

## Downstream

| ID | Severity | Fix that was read | Verdict |
|---|---|---|---|
| V5-C1 | critical | `volume8-analysis/chapters/ch09-complex.tex` now cites Theorem 9.9. Counted in `ch09-complex.tex` of Volume 5: `thm:cauchy` is the 9th numbered statement. Theorem 11.9 is Laplace’s method. | Accept |
| V5-M1 | major | Old chapter \(N\) for \(N\ge 6\) was sent to chapter \(N-2\), and the internal number was kept when the kind matched. Spot checks: Gaussian transform Theorem 8.3, basic rules Proposition 8.2, inversion Theorem 8.6, Poisson Theorem 8.9, Gauss sum Theorem 8.14, Fejér Theorem 6.9, Parseval Theorem 6.11, Weyl Theorem 6.13, Heisenberg Theorem 8.16, Weierstrass Corollary 5.7, Stirling for \(\Gamma\) Theorem 5.8. The Fourier coefficient on the circle in `ch02-hilbert.tex` was corrected by hand to Chapter 6 after the scorer left it on Chapter 8. The FFT pointer is Chapter 7. The theta transformation that makes the divisor error exponential is Corollary 8.10. | Accept |
| V5-M2 | major | The heuristics file no longer cites Theorem 5.7 for Waring. That file is not in Volume 15’s `main.tex`. The printed sentence is in `polyfermat.tex` (V5-M4). | Accept |
| V5-M3 | major | The Hua sentence is deleted. The next sentence still says the later argument does not use the claim. | Accept |
| V5-M4 | major | `polyfermat.tex` no longer says Volume 5 proved the asymptotic. | Accept |
| V5-M5 | major | `three-primes.tex` says partitions only. | Accept |
| V5-M6 | major | Hurwitz is Theorem 6.17. Volume 9’s own Appendix F, on cubic curves, was not edited. | Accept |
| V6-08 | minor | Theorems 3.6, 3.8 and 5.2. `thm:line` is the second statement of Chapter 5. Theorem 5.8 is the prime number theorem in progressions. | Accept |
| V6-09 | minor | Theorem 8.4, with \(1+o(1)\). | Accept |
| V6-10 | minor | Volume 5, Proposition 10.2, which is `prop:dirmult`. | Accept |
| V6-11 | minor | No edit. The Volume 7 text already places Borel–Cantelli, Baire and Lebesgue density in Volume 7, with chapter labels. | Accept, already corrected |
| V6-12 | minor | The parity remark is tied to the progression inequality, and the ratio \(2k\) is stated. | Accept |
| V6-13 | minor | The product, not Theorem 12.7, is what shows \(\Delta\) has no zeros. Theorem 12.7 is the transformation. \(\dim M_4=1\) is Theorem 12.9(c); part (b) is the equality of dimensions. Both were read in `ch12-modular.tex`. | Accept |
| V6-14 | minor | No edit. The book class numbers equations by chapter, and `eq:stirlingvert` is the first `equation` environment of Chapter 6, so the printed number is (6.1). The suggestion to print (1) would have been a new error. | Accept, citation already right |

## What this pass sent back

The mathematical sentences were not rejected. The guards that hash a source file were, and each one was refreshed after the file was reread.

- The Gamma chapter’s new citation of Volume 1, Chapter 8, for Wallis, lengthened the pinned list in `tools/test_cross_volume_citations.py`. The pin is the order of appearance. The test passes.
- Editing Volume 1’s integrals chapter changed the toolkit hash in `docs/reviews/volume2-forward-reference-review-2026-11-04.json`. The forward-reference count is still 86, and the reference count is still 326. The sentences that changed are Volume 5 chapter numbers, not Volume 1 premises.
- The same integrals chapter is a Volume 3 prerequisite. Its hash in `review/volume3-internal/prerequisite-sources.json`, and the whole-volume fingerprint in `review/volume3-internal/concepts.json`, were moved with it. One hundred and twenty concept statuses are unchanged. The only snapshotted path that differs is that chapter.
- The Farey cover sentence was regenerated from `common/cover-notes.json`. A hand-typed comma, where the generator writes a full stop, had left `docs/COVER-NOTES.md` stale. The Volume 3 inventory and fingerprint move with that JSON file and with nothing else.

The two fingerprint commits sit on different branches. Each matches that branch against current `main`. Once the cover-note change is on `main`, the downstream fingerprint has to be recomputed on the merged tree before that pull request is merged, because the live `common/cover-notes.json` and the integrals chapter will then both differ from the snapshot taken on either branch alone.
