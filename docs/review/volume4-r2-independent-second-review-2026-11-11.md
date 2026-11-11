# Volume 4 round 2 — independent second review

**Reviewer.** This pass is the independent second review, cloud agent `bc-114da047-b320-5bb0-b0d1-2f6495477a25` (grok-4.7). It is not the author of the fix commits. Those commits are by Cursor Agent, co-authored with Seghaier Oussama, from the writer run linked on the fix PRs (`bc-1c9c5f35-0259-5afa-9b94-1f2d37fedf0c`). No writer branch was edited. Nothing here was merged, and no comment was posted on a writer pull request.

**Source of the issue list.** Draft pull request [#175](https://github.com/OussamaSegh/Order-and-Chance/pull/175), live head `17ccaf44b70101ffe0f23d94384d25c7f0d70e8d`, file `docs/review/volume4-independent-scored-read-2-2026-11-11.md`. That head matches the expected `17ccaf44`. Its base is still `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f`, not current `main`. The issue log in that file is V4R2-01 through V4R2-20. This review reads that log and then checks the manuscripts. A green build is not treated as a proof.

**Live `main` at this review.** `a2cfdd30a0f09eabcb932852c76537c8af592bdb` (`Volume 4: derive the empty-success bound from finite additivity (#176)`). The pause SHA named in the assignment had not moved.

**How to read the dispositions.** “Approve the repair” means the manuscript change closes the cited issue and does not weaken the stated theorem. It is not a merge. Parent Nori merges. “Repair before approval” means the stated conclusions are the classical ones, but the write-up still does not justify a step it uses.

## Disposition of the five open pull requests

| PR | Live head (full) | Base | Merge git | Mathematical disposition |
| --- | --- | --- | --- | --- |
| [#180](https://github.com/OussamaSegh/Order-and-Chance/pull/180) | `fd0aa1cac46cf0df819e6cb1daf570ba3a51a1a7` | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | `MERGEABLE` / `UNSTABLE` | **Do not approve.** V4R2-15 and V4R2-16 are fixed. V4R2-01 is only partly fixed. V4R2-10 is not fixed. See the repair list below. |
| [#181](https://github.com/OussamaSegh/Order-and-Chance/pull/181) | `e2e80191e195425c153013b2cefdb97cf7f10ed9` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-13. The red check is the shared `site` apt failure, not this sentence. |
| [#182](https://github.com/OussamaSegh/Order-and-Chance/pull/182) | `5131283032a53713afcd7bc0f9a6aa9679180e35` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-11 and V4R2-12. Same `site` failure. |
| [#184](https://github.com/OussamaSegh/Order-and-Chance/pull/184) | `264518e7ac5006cbb35d01bf530f55e6ffa3f7fc` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-07. Same `site` failure. |
| [#186](https://github.com/OussamaSegh/Order-and-Chance/pull/186) | `b071f8d919e7a8cf7365b1213ca3628883f1fcc6` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-06. Same `site` failure. |

The bodies of these five PRs still name older heads (`6643969c`, `34fc29d9`, `f4722b35`, `f4f7b2db`, `42d36c26`). Those are not the live heads. Guard any squash on the SHAs in the table above.

The jobs that run, and the exact-head conclusions, are in the CI section. `publish` is `main`-only. A green volume build is not a proof.

## What #180 must repair before it can be approved

File at head `fd0aa1ca`: `volume4-chance/chapters/ch11-brownian.tex`. Theorem statements of existence (Theorem 12.4, label `thm:levy`) and reflection (Theorem 12.12, label `thm:reflection`) are the original sentences. No numbered environment was added. The source pin `fe398da68dcbd1405ab1808352be288681a4e817` matches `git rev-parse fd0aa1ca:volume4-chance/chapters/ch11-brownian.tex`.

### Blocking gap in V4R2-01

Lines 62–69 do the repair the issue asked for, and that part checks.

- Each midpoint displacement is \(\Phi^{-1}\) of its own uniform from Proposition `prop:manyuniforms` (`volume4-chance/chapters/ch05-continuous.tex`, the independent-uniforms proposition). The proof of that proposition squeezes an interval condition between finite unions of dyadic cylinders. Citing it for the squeeze is fair.
- The threshold arithmetic is right: \(\sigma^2=2^{-(n+1)}\), \(a_n/\sigma=2\sqrt n\), so \(a_n^2/(2\sigma^2)=2n\).
- Proposition `prop:gausstail` is the integral bound \(\int_x^\infty e^{-t^2/2}\,dt\le x^{-1}e^{-x^2/2}\). With the normal density this gives
  \[
  P(|Z|>2\sqrt n)\le\frac{1}{\sqrt{2\pi n}}e^{-2n}\le e^{-2n}
  \]
  for \(n\ge 1\). That display (lines 64–67) is a numerical bound, recorded separately below, and it is correct.
- Proposition `prop:subadd` (`ch01-counting.tex` lines 90–95) is countable subadditivity of outer content for every subset of \([0,1)\). Applying it to the finitely many midpoint thresholds, and then to the tail union, is the convergent half of Borel–Cantelli for these outer contents. Theorem `thm:bc`(a) (`ch04-inequalities.tex` lines 168–170) really is stated only for finite unions of half-open master intervals. The new text refuses that citation. Definition 1.3 says “almost surely” means outer content zero, so the words “almost surely” after the tail union match the book’s definition.
- The uniform Cauchy estimate for the piecewise-linear interpolants, from midpoint displacements alone, is the standard tent-map bound: on the complement of the displacement failures, \(\|I_m-I_n\|_\infty\le\rho_n\).

The gap is the next sentence.

Line 71: “The same estimate applies to the increments across the level-\(n\) bins.” A level-\(n\) bin increment is not one coordinate. Lemma `lem:levylevel` builds it as a linear image of a parent increment and a new midpoint normal. By the second level it depends on more than one uniform. The one-coordinate cylinder squeeze does not apply to it. The Gaussian tail “at most \(e^{-n}\)” is the right bound on the normal probability (standardised height \(\sqrt{2n}\), so the exponent is \(n\), and \(1/\sqrt{\pi n}\le 1\)), but that is not yet an outer content.

Line 71 then puts those bin increments into \(E_n\). Line 77 contradicts that definition: “The set \(E_n\) is different: it is a union of single-coordinate normal thresholds, so the bound above is an outer content.” As defined on line 71, \(E_n\) is not only single-coordinate thresholds.

The modulus on line 75 needs the bin-increment bound. The oscillation of the limit on a bin is at most \(a_n+2\rho_n\) only because the interpolant’s vertical change on that bin is the bin increment. The law at a non-dyadic time (lines 79–90) uses \(|B_t-B_{t_n}|\le\delta_n\) off \(E_n\). So the distributional half of Theorem 12.4 still rests on an outer content that lines 71 and 77 do not justify. The midpoint half, which was the citation in V4R2-01, is fixed. The event \(E_n\) that the same proof uses for the modulus and for \(B_t\) is not.

The quadratic-variation proof later in the same file (the paragraph on \(V_n\), about lines 170–176) already says how a threshold of finitely many coordinate normals becomes an outer content: cut off a large box, cover by rectangles, pull back under the quantile maps, and use `prop:manyuniforms` plus `prop:subadd`. That argument does not depend on Theorem 12.4. It should be invoked, or copied in short, before a bin-increment tail is called an outer content. Line 77 should then describe \(E_n\) as it was defined.

### Blocking gap in V4R2-10

Lines 328–359 are the right shape of repair, and the algebra checks. They are not enough, because they call a window small before that smallness is proved.

What checks, as algebra and as quantifiers, not as a finished measure argument:

- On \(\{\tau_n=s\}\) the position is symmetric about \(B_s\), and the text says so (line 328).
- \(\delta\) is chosen first so that the window of length \(2\delta\) is the one declared smaller than \(\eta\). Then \(\varepsilon\) is chosen so that \(12\varepsilon(2\pi\delta)^{-1/2}<\eta\). The ratio \(\varepsilon/\sqrt\delta\) is controlled. The order is the one the issue needs.
- \(F\) odd and continuous, \(H,\kappa,\psi\) continuous cutoffs: piecewise-linear choices exist with the stated values. No later theorem is cited for them.
- On \(\{|B_s-a|\le\varepsilon\}\) and \(\{|W|>2\varepsilon\}\), \(W>2\varepsilon\) forces \(B_t>a+\varepsilon\) and \(W<-2\varepsilon\) forces \(B_t<a-\varepsilon\), so \(S=F(W)\). The bound \(|S-HF|\le 2\psi\) on \(\{H=1\}\) and \(\le 2\kappa\) on \(\{H<1\}\) follows.
- The factor 12 is \(2\times 6\): \(\mathbb E[\psi(G_s)]\le P(|G_s|\le 3\varepsilon)\le 6\varepsilon(2\pi\delta)^{-1/2}\) when \(t-s\ge\delta\), and the absolute difference contributes another 2. Summing \(P(\tau_n=s)\) over \(s\le t-\delta\) does not increase the constant.
- The finite-grid identity used for \(H(B_s)F(W)\) and for \(\psi(W)\) is the continuous-test identity already in Proposition `prop:restart`, not an application of that identity to the indicators. That is what V4R2-10 asked for.
- \(\kappa(a)=0\), so the restarted expectation of \(\kappa(B_{\tau_n})\) is sent to 0 by the convergence Proposition `prop:restart` already proves for a bounded continuous function of the stopped position.
- If \(h<\delta\), then \(\{t-\delta<\tau_n\le t\}\subset\{t-2\delta<\tau_a\le t\}\). Hence \(\limsup|R_n-L_n|\le\eta+\eta\), and \(\eta\) is arbitrary.
- The density calculation is calculus, checked separately below. The comparison \(\int_1^\infty t\cdot t^{-3/2}\,dt=\infty\) is the right reason that \(\mathbb E[\tau_a]=\infty\). The displayed density is the derivative of \(2(1-\Phi(a t^{-1/2}))\).

What does not check:

Line 319. The short-time hitting event is put in \(G_n\cup\{|B_t-a|\le\omega_n\}\), and the strip is then given probability at most \(2\omega_n(2\pi t)^{-1/2}\) because “Theorem `thm:levy` gives \(B_t\) the law \(N(0,t)\)”. The existence proof only identifies outer content of half-lines: line 91 says \(P^*(\{B_t\le x\})\) equals the Gaussian distribution function. Outer content of an intersection is not the difference of those half-line contents. A strip is an intersection. Subadditivity does not turn the half-line result into the density bound on line 319.

That bound is what makes the window’s outer content tend to 0, which is what lets line 328 choose \(\delta\). Until the strip is estimated, the quantifier sentence has nothing to choose.

A repair that stays inside the book: off \(E_n\), \(|B_t-B_{t_n}|\le\delta_n\) (once \(\delta_n\) is the modulus actually proved), so the strip sits in a slightly wider interval for the dyadic random variable \(B_{t_n}\), or in \(E_n\). Bound the dyadic interval by the Gaussian density only after the finite-dimensional rectangle reduction named above. Do not call the strip a probability read off the half-line outer content of the limit.

Line 321’s separate bound for \(R-R_n\), through \(P(|B_t-a|\le\eta)\le 2\eta(2\pi t)^{-1/2}\), is the same strip, and needs the same repair.

### Non-blocking notes on the same proof

These are not further reasons to withhold approval once the two gaps above are closed. They should be one sentence each if the writer is already in the file.

- Line 77 takes \(t_n\) to be “a dyadic within \(2^{-n}\) of \(t\)” and claims \(|B_t-B_{t_n}|\le a_n+\rho_n\). That constant is right when \(t_n\) is an endpoint of the level-\(n\) bin that contains \(t\): the dyadic value equals the interpolant, so only one copy of \(\rho_n\) appears. A dyadic in the neighbouring bin, still at distance \(2^{-n}\), can see two bin increments. Name the endpoint.
- The modulus is proved for the construction on \([0,1]\). Theorem 12.12 is stated for every \(t>0\). The extension to \([0,\infty)\) builds each unit interval as its own copy. Line 319 should take \(G_n\) from the copy that contains the window when \(t>1\).

### V4R2-15 and V4R2-16, approved inside the same pull request

- V4R2-15, minor, notation. Line 300: the deterministic bound is \(|\Psi|\le\beta\). It is no longer named \(B\) inside the proof where \(B\) is the process. The compact-box argument is otherwise the one already in Proposition `prop:restart`.
- V4R2-16, minor, citation. Line 12 points at the normal distribution in Chapter 5. The density, the tail, and Box–Muller are in Chapter 5 (`prop:gausstail`, `thm:boxmuller`). Chapter 6 is the limit theorem. The pointer is the right one.

### Prerequisite check for the new Brownian text

The new sentences use countable subadditivity, the Gaussian tail, the uniform-digit construction, continuous cutoffs, and the finite-grid identity already proved for bounded continuous tests. They do not cite Lévy’s continuity theorem, Itô’s formula, a general Fubini theorem, or uniform integrability. The reflection algebra is high-school once those inputs are granted. The missing step is an outer-content reduction the book already sketches later in the chapter, not a silent appeal to a later volume. The theorem sentences are not weakened.

### Numerical checks for #180, separate from the proof

These were recomputed from the displayed formulas. They do not close the outer-content gap.

- \(2/e^2<1\) and \(2/e<1\), so both series in \(P^*(E_n)\) tend to 0 once each term is a genuine outer content.
- Mills bound as displayed on lines 64–67: correct for the standard normal.
- Bin-increment Gaussian tail: with \(x=\sqrt{2n}\), \(P(|Z|>x)\le 1/\sqrt{\pi n}\,e^{-n}\le e^{-n}\).
- \(\frac{d}{dt}2\bigl(1-\Phi(a t^{-1/2})\bigr)=\frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}\).
- For \(t\ge 1\) the density is at least a positive constant times \(t^{-3/2}\), and \(\int_1^\infty t^{-1/2}\,dt\) diverges.

## #181 — Euler, approved

Head `e2e80191e195425c153013b2cefdb97cf7f10ed9`. V4R2-13, minor, rigor. `volume4-chance/chapters/ch12-method.tex` line 141, Proposition `prop:euler`.

The proposition still says \(v-e+f=2\) for a connected plane graph and \(e\le 3v-6\) for a simple plane graph with \(v\ge 3\), connected or not. The new sentence is: “In the current plane graph the two endpoints of the next edge lie on one common face, and the edge is drawn inside that face.” That is the sentence the issue asked for. It is true when the edges being added are the remaining edges of one plane embedding, each drawn in a face of the graph already drawn: a tree has a single face incident to every vertex, and each later edge of the embedding is a chord of one face. The sentence states that fact. It does not derive it from the Jordan theorem. The issue did not ask for that derivation. The disconnected case on the following lines is unchanged. The source pin `762a62a5aaa86a84b9c8038cae7ebd5e6813d750` matches the blob. No label moved.

Unresolved doubt: none that reopens the issue. A reader who wants a proof that a plane chord meets one face will not find it in this sentence. That is the depth the scored read requested.

## #182 — van der Waerden and the \(k=1\) family, approved

Head `5131283032a53713afcd7bc0f9a6aa9679180e35`. `volume4-chance/chapters/extremal.tex`. Pin `c94c620e322651d42f385b34bdb0ad86558ecfe2` matches the blob.

**V4R2-11**, minor, correctness. Lines 131 and 134, Theorem `thm:vdw`. “Equivalently” is gone. The infinite sentence is “It follows that…”. The proof’s first paragraph shows only finite to infinite: for each length \(k\), the colouring of \(\{1,\ldots,W(k,r)\}\) has a monochromatic \(k\)-term progression; the colour may depend on \(k\); finitely many colours and infinitely many lengths give one colour with infinitely many lengths, hence arbitrarily long progressions. That direction is correct. The converse is not claimed, and no compactness argument was added. The finite induction is untouched. The theorem is not weakened.

**V4R2-12**, minor, correctness. Lines 223–227, solution `ex:ekrcomplement`. The count \(\tfrac12\binom{2k}{k}=\binom{2k-1}{k-1}\) is the identity \(\binom{2k}{k}=2\binom{2k-1}{k-1}\), which follows from \(\binom{2k}{k}/\binom{2k-1}{k-1}=2k/k=2\). For \(k=1\) and \(n=2\) the complementary pairs are the two singletons, and each choice is a star of size 1. The non-uniqueness sentence is restricted to \(k\ge 2\). For \(k=2\), \(n=4\), one selection from the three complementary pairs is \(\{\{1,2\},\{1,3\},\{2,3\}\}\), which is pairwise intersecting of size 3 and is not a star. The last sentence, that the theorem asserts the maximal size and not uniqueness, still describes what Theorem `thm:ekr` claims. It does not say uniqueness fails at \(k=1\).

Numerical check, separate from the wording: the binomial identity above. It holds for every integer \(k\ge 1\).

Unresolved doubt: none.

## #184 — twelve rows, approved

Head `264518e7ac5006cbb35d01bf530f55e6ffa3f7fc`. V4R2-07, minor, figures.

`volume4-chance/about-the-cover.tex` line 6, generated from `common/cover-notes.json` key `"4"`. The note says the drawing has twelve rows, that the picture is not a portrait of one machine, and that Galton’s machine is a different object with more rows than the drawing. The dates stay: built in 1873, shown at the Royal Institution in 1874, described in *Natural Inheritance* (1889). The word count of that `about` string is 110, inside the 80–150 check in `tools/series_cover.py`.

The drawing really has twelve rows. `tools/covergen/arts.py`, function `v4`, sets `n=12` and draws row `i` for `i` in `range(n)`, with binomial(\(12\), \(1/2\)) bin heights. No font, size, or label inside a figure was edited. `arts.py` is not in the diff.

“More rows” matches Stigler’s caption of the 1873 machine: “17 rows of alternatingly offset pins” (Stephen M. Stigler, *Darwin, Galton and the Statistical Enlightenment*, *Statistical Science* 25 (2010), Figure 1; the same sentence is in the text circulated at `gwern.net/doc/statistics/bayes/2010-stigler-2.pdf`). The note does not invent the number 17. It only says “more”, which 17 against 12 supports.

Hashes in `tools/assets/series/manifest.json` match the blobs: `common/cover-notes.json` is `7d9bb310cdd17fdf3d0e53c12987a932397de1208fee5a15b64d542413e84359`, and `about-the-cover.tex` is `9e9fff4465cdcd6f9da559ead5630e8d748262465c961fa9b2334dcbae79969c`. `docs/COVER-NOTES.md` repeats the same paragraph. No other volume’s `about` string changed.

`review/volume3-internal/concepts.json` has the same 120 entries, every one still `accepted-internal`. The only entry-level change is `reviewed_snapshot_sha256`, from `4147b842e1ad99f9ea36bfcf4dc1d16dd030bc13af22fdd33a9940099940d06f` to `2f25ca6412287563e9fdde82117260b55a2052153a11234654080b5a6d3de108`. The snapshot’s source list changes only the hash of `common/cover-notes.json`. A new key `v4r2_cover_note_seam_retention` records that fact and says it is not a new Volume 3 approval. `inventory.json` changes the same cover-notes hash and nothing else. That collateral is a hash refresh, not a reclassification.

Unresolved doubt: none on the historical sentence. The shared cover-notes file is why this pull request rebuilds every volume. Only Volume 4’s colophon text changes.

## #186 — periodic-chains pointer, approved

Head `b071f8d919e7a8cf7365b1213ca3628883f1fcc6`. V4R2-06, minor, cross-volume citation. `volume5-calculation/chapters/ch12-agm.tex` line 1028, solution `pb:cyclewalk`.

The tools line is now “Volume 1, Chapter 5 (roots of unity filter); Volume 4, Chapter 2 (independence).” The parenthetical “Chapter 8 (periodic chains)” is deleted. Chapter 8 of Volume 4 is the walk chapter. The period of an irreducible chain is in Chapter 9. The solution does not use it.

The calculation that remains cites the same two tools in the write-up: the roots-of-unity filter at line 1018 (“Volume 1, Chapter 5”) and independence at line 1020 (“Volume 4, Chapter 2”). Parts (a)–(c) are unchanged. Volume 4 is not edited.

`volume4-native` does not run on this pull request. `.github/workflows/volume4-qa.yml` triggers on `volume4-chance/**`, `common/**`, and `tools/**`. This diff is only `volume5-calculation/chapters/ch12-agm.tex`. The absence of that job is the path filter, not a check switched off. The Build books matrix still runs.

Numerical check, separate from the citation: for \(k=3\) the cosines are \(1,-1/2,-1/2\), so
\[
q_n=\frac13\bigl(1+2(-1/2)^n\bigr),
\]
which is the displayed formula. The edit did not touch it.

Unresolved doubt: none.

## Already merged fixes, checked in current `main`

| ID | PR | Merge commit | Head that was merged | Location now | Verdict |
| --- | --- | --- | --- | --- | --- |
| V4R2-02 | [#176](https://github.com/OussamaSegh/Order-and-Chance/pull/176) | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | `0532f1243e165e8cabb3e7bd1b68385a05136b1d` | `ch02-discrete.tex` line 110 | Approved. |
| V4R2-03 | [#178](https://github.com/OussamaSegh/Order-and-Chance/pull/178) | `6854ba6a2b57e7ad5a7b19b6c843ec11957753c0` | `c0e83a823fa3c2290e9ad4d66e75a7e3979dbada` | `ch07-walks.tex` line 81 | Approved. |
| V4R2-04 | [#178](https://github.com/OussamaSegh/Order-and-Chance/pull/178) | same | same | `ch07-walks.tex` line 205 | Approved. |
| V4R2-05 | [#177](https://github.com/OussamaSegh/Order-and-Chance/pull/177) | `4bd0254c49dec36f46701cfb2f07a8480f24275a` | `7bf9d374cc753414d32d437a22b24acdb774aac8` | `ch04-inequalities.tex` source list; `bibliography.tex` line 30 | Approved. |
| V4R2-08 | [#183](https://github.com/OussamaSegh/Order-and-Chance/pull/183) | `9582c54f37d2007e20785452b92189424fca6dc6` | `ffcd7d8eaccd814ea8c68ac096357c55381de64b` | `chapters/index.tex` | Approved, with the EPUB limit below. |
| V4R2-09 | [#185](https://github.com/OussamaSegh/Order-and-Chance/pull/185) | `54aca8162bffadc7d7dc9b1a582a5141cdc9e8f9` | `a1bc3384ce53dfef99ef84c32c470a80556410a2` | `kdp.md` lines 3–7 | Approved. |
| V4R2-14 | [#179](https://github.com/OussamaSegh/Order-and-Chance/pull/179) | `b27fd9fd1cc86276d881b2d906f9437e124cfd32` | `dd3c133c77bbb7eeefd7d91f1663183efa7632af` | `ch10-martingales.tex` lines 308–311 | Substance approved. One false sentence remains. |

**V4R2-02.** Line 110 no longer says “the union bound in Chapter 1”. It cites finite additivity in Volume 1, Chapter 10. That chapter number is right: `volume1-first-principles/main.tex` inputs the language chapter first, and `ch09-probability.tex` is the eleventh input, so it is Chapter 10. Line 41 of that file states \(P(A\cup B)=P(A)+P(B)\) for disjoint events, with nonnegativity. Splitting off the new part of the next event and discarding the overlap is the finite union bound. The successes in the Poisson boundary are finite experiments, so they sit in that axiom. The inequality \(P(\text{some success})\le np_n\) is the one the issue asked to justify.

**V4R2-03.** The displayed formula is \(h_k=((q/p)^k-1)/((q/p)^N-1)\). Line 81 solves \(A+B=0\) and \(A+B(q/p)^N=1\), hence \(B=1/((q/p)^N-1)\) and \(A=-B\), which is that formula. At \(p=2/3\), \(N=5\), \(k=1\), both the formula and the figure’s \((1-2^{-k})/(1-2^{-5})\) equal \(16/31\). That arithmetic is a numerical check, separate from the three lines of algebra, and it matches.

**V4R2-04.** Line 205 says the cube integral is taken one coordinate at a time, that each integrand is continuous on a compact rectangle, and that Proposition `prop:fubini` is the planar statement being iterated. The proposition (`ch05-continuous.tex` lines 165–171) really is the equality of the two orders on a rectangle, for a continuous integrand. Iterating it is the missing sentence. The Gaussian bound \((4\pi d/n)^{d/2}\) is unchanged. As a numerical check: \(\int_{-\infty}^{\infty}e^{-a t^2}\,dt=\sqrt{\pi/a}\) with \(a=n/(4d)\) is \(\sqrt{4\pi d/n}\), and \(d\) factors give the displayed power. The citation of the two-sided integral as a Volume 1 statement is a different issue, V4R2-19, and is still open.

**V4R2-05.** Shannon’s 1948 paper is gone from the source list at the end of `ch04-inequalities.tex`. It remains once in `bibliography.tex` line 30, described as the entropy paper, and it remains on the Chapter 7 source list. Chapter 4 does not use entropy. The duplicate filing is gone.

**V4R2-08.** The index keeps the theorem numbers and adds `\ocindexpage`, which expands to `, p.~` plus `\pageref` (written as `\csname pageref\endcsname`). The introductory sentence says the page number is there in the reading and print PDFs. Every label used by the index exists in the Volume 4 sources (`thm:ballot`, `thm:bayerdiaconis`, `thm:bc`, `thm:boxmuller`, `def:bm`, `thm:levy`, `thm:reflection`, `thm:buffon`, `cor:clt`, `thm:lindeberg`, `def:charfn`, `thm:inversion`, `thm:coupon`, `prop:gibbs`, `thm:shannon`, `thm:huffman`, `thm:ekr`, `thm:extinction`, `thm:gc`, `thm:hoeffding`, `thm:local`, `def:mart`, `thm:os`, `thm:os2`, `thm:L2conv`, `prop:memoryless`, `def:outer`, `thm:poissonlimit`, `def:pp`, `thm:polya`, `thm:polyaurn`, `thm:erdos`, `thm:lll`, `thm:ramsey`, `thm:vdw`, `thm:subcrit`, `thm:triangles`, `thm:sllnbound`, `thm:slln4`, `thm:top`, `thm:turan`, `thm:weierstrass`). The only manuscript edit besides the index is a `\label{def:charfn}` on the sentence that defines the characteristic function in `ch06-clt.tex`. No formula changed. `tools/epub_prep.py` strips `\ocindexpage` before Pandoc, and `tools/test_epub.py` checks that the theorem number stays and the page command goes. This review did not re-typeset a PDF to read the printed folios. The labels are in the source; the merged build is what had to resolve them.

**V4R2-09.** `kdp.md` now opens on the same sentence as `blurb.tex`. Horse-kick counts are attached to the Poisson law of rare events. The Poisson process is named separately as the clock. “Climbs to the theorems” and “a drunk bird” are gone. The listing is longer than the blurb, which a description needs, and it names the theorems the issue asked it to name.

**V4R2-14, residual.** Lines 308–309 write the factor \((n+2)/(n+1)\) in front of the mesh-\(1/(n+2)\) sum from \(k=1\) to \(n+1\). That identity is right, and the sum omits one interval of width \(1/(n+2)\). Line 311 then says: “Both \((n+2)/(n+1)\) and the omitted piece tend to \(1\).” The factor tends to 1. The omitted piece tends to 0, because \(g\) is bounded and the missing width is \(1/(n+2)\). The truncated Riemann sum tends to \(\int_0^1 g\), so the product does too. The conclusion on line 311 is the right limit. The clause “the omitted piece tend to 1” is false, and a reader who believes it cannot reconstruct the estimate. Replace it with: the factor tends to 1, and the omitted interval’s contribution tends to 0. This is already on `main`. It wants a one-sentence follow-up. It is not a reason to reopen the uniform limit, which the counting argument on line 306 also gives.

## Omissions: four issue IDs with no pull request

Searched on `main` at `a2cfdd30` and in the five open heads. None of #180, #181, #182, #184, #186 touches these lines. They are still the defects the scored read named.

| ID | Severity | Where it still is | What is still wrong |
| --- | --- | --- | --- |
| V4R2-17 | minor, rigor | `volume4-chance/chapters/ch07-entropy.tex` line 239, Theorem `thm:huffman` | After a lightest symbol is moved to maximum depth, “let its sibling have probability \(s\)” treats that sibling as a symbol. The proof has said that a deepest leaf has a sibling. It has not said the sibling is a leaf. An internal sibling would have a deeper child, so at maximum depth the sibling is a leaf. One sentence closes it. |
| V4R2-18 | minor, citation | `volume4-chance/chapters/ch07-walks.tex` lines 16–18 | “Chapter 6’s local theorem gives” both \(P(S_{2m}=0)=\binom{2m}{m}2^{-2m}\) and the asymptotic \(1/\sqrt{\pi m}\). The exact count is the binomial coefficient. The asymptotic is Theorem `thm:local`. The formula is right. The attribution is not. |
| V4R2-19 | minor, citation | `volume4-chance/chapters/ch07-walks.tex` line 246, Theorem `thm:polya` | The proof quotes \(\int_{-\infty}^{\infty}e^{-u^2}\,du=\sqrt\pi\) as what Volume 1 gives. Volume 1, Chapter 8 (`ch06-integrals-taylor.tex`, the chapter opener and Proposition `prop:gaussianintegral`) prints the half-line \(\int_0^\infty e^{-x^2}\,dx=\sqrt\pi/2\). The integrand is even, so doubling gives \(\sqrt\pi\). The power \((4\pi d/n)^{d/2}\) is the right value. The citation should be the half-line, then the doubling. |
| V4R2-20 | minor, correctness | `volume4-chance/chapters/ch07-walks.tex` lines 451 and 454, solution `ex:meet` | The idea starts the difference at \(2\). The solution sets \(D_0=-2\), which is \(S_0-(2+S'_0)\). The ruin probability \((N-1)/N\) in the write-up matches the start \(-1\) after dividing by 2, and the meeting conclusion is right. The idea line does not match the solution. Start the idea at \(-2\). |

No other V4R2 id is missing from the map. V4R2-01 through V4R2-20 are all accounted for above.

## CI and mergeability

Polled with `gh pr view` and `gh run view` until every Build books run on these heads had a completed conclusion. `main` stayed at `a2cfdd30a0f09eabcb932852c76537c8af592bdb`. Every open head stayed the SHA in the disposition table. All five were `MERGEABLE` against that base. `mergeStateStatus` was `UNSTABLE` because Build books is not green.

Branch protection could not be read (`gh` received HTTP 403). The jobs that actually ran are the ones below. `publish` is `SKIPPED` on each pull request, which is the `main`-only condition in `build.yml`, not a check turned off.

| PR | Build books | Conclusion | Volume 4 native QA |
| --- | --- | --- | --- |
| #180 | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022046289 | **failure** | success, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022046248, head `fd0aa1ca` |
| #181 | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022049385 | **failure** | success, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022049391, head `e2e80191` |
| #182 | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022053308 | **failure** | success, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022053049, head `51312830` |
| #184 | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022055736 | **failure** | success, https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022055482, head `264518e7` |
| #186 | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022058849 | **failure** | not triggered; path filter, see #186 above |

On every one of those five Build books runs, `list`, `debs`, and all fifteen `build (volume…)` jobs completed with success. The only failed job is `site`. Each failure is the step “Install poppler”, exit code 100:

`E: Failed to fetch …/poppler-utils_24.02.0-1ubuntu9.11_amd64.deb  Temporary failure resolving 'azure.archive.ubuntu.com'`

Failed job URLs:

- #180 https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022046289/job/130584956853
- #181 https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022049385/job/130584966084
- #182 https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022053308/job/130577481578
- #184 https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022055736/job/130581224219
- #186 https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43022058849/job/130583140811

No test assertion failed. The manuscript checks inside the volume builds passed on these exact heads. The workflow conclusion is still failure, so a rule that merges only a green exact head cannot merge any of these five until `site` is rerun and succeeds on that same head. This review did not rerun the jobs.

A green `build (volume4-chance)` or a green `volume4-native` does not certify Theorem 12.4 or Theorem 12.12. #180’s native QA succeeded, and the proof gaps above remain.

## What this review did not do

- Did not merge, did not push to a writer branch, and did not comment on #175, #180, #181, #182, #184, or #186.
- Did not edit manuscript, cover art, or tests.
- Did not start the later Volume 1–3 apply sequence. Those instructions were context only.
- Did not re-typeset a PDF. Label existence, hashes, and the workflow path filters were checked in git. Printed folios for the new index were not read off a fresh PDF in this pass.
- Did not treat #175’s comparison section, or any pull-request body, as evidence. The bodies’ “second review” heads are stale.

## CI at commit time

Final poll, after every Build books run above had left `in_progress`. Heads and `main` were unchanged from the table. All five Build books conclusions are `failure`, and the only failed job on each is `site` at the poppler apt step (DNS). Volume builds and, where the path filter runs it, `volume4-native` are `success` on these heads. `publish` is `skipped`.
