# Volume 4 round 2 — independent second review

**Reviewer.** This pass is the independent second review, cloud agent `bc-114da047-b320-5bb0-b0d1-2f6495477a25` (grok-4.7). It is not the author of the fix commits. Those commits are by Cursor Agent, co-authored with Seghaier Oussama, from the writer run linked on the fix PRs (`bc-1c9c5f35-0259-5afa-9b94-1f2d37fedf0c`). No writer branch was edited. Nothing here was merged, and no comment was posted on a writer pull request.

**Source of the issue list.** Draft pull request [#175](https://github.com/OussamaSegh/Order-and-Chance/pull/175), live head `17ccaf44b70101ffe0f23d94384d25c7f0d70e8d`, file `docs/review/volume4-independent-scored-read-2-2026-11-11.md`. That head matches the expected `17ccaf44`. Its base is still `8b8a5be337271478f9f7a2bc24d7b1a9b3602c2f`, not current `main`. The issue log in that file is V4R2-01 through V4R2-20. This review reads that log and then checks the manuscripts. A green build is not treated as a proof.

**Opening pin, not live `main`.** When this file was opened, `origin/main` was `a2cfdd30a0f09eabcb932852c76537c8af592bdb` (`Volume 4: derive the empty-success bound from finite additivity (#176)`). Live `main` at the fourth pass is `6e5cc70d814c9cc196a399aaa3982bb56803d501`.

**How to read the dispositions.** “Approve the repair” means the manuscript change closes the cited issue and does not weaken the stated theorem. It is not a merge. Parent Nori merges. “Repair before approval” means the stated conclusions are the classical ones, but the write-up still does not justify a step it uses.

The section **Fourth pass** is the current verdict, at head `f7dc4d4ad17cc21fd163812c646e0132a530912b`. The third pass remains the record of head `9271ba96`, where Theorems 12.4 and 12.12 were approved and one atom sentence was still loose. The second pass remains the record of head `3bb6331e`. The first pass remains the record of head `fd0aa1ca`.

## Fourth pass — head `f7dc4d4a`, approve Theorems 12.4 and 12.12

**Reviewer.** Same independent reviewer, `bc-114da047-b320-5bb0-b0d1-2f6495477a25`. The new commits are still by writer `bc-0f6fa3d7`. This pass did not edit that branch, did not merge, and does not restore an exercise.

**Parents.** `f7dc4d4ad17cc21fd163812c646e0132a530912b` is a merge commit. Its first parent is `74252a5b97b5162fe73b441cf5f03920dc3e9bc1`, whose only parent is the previously approved `9271ba96cacc8ed51f2bfed37bce050a179ea5bd`. Its second parent is `6e5cc70d814c9cc196a399aaa3982bb56803d501`, which is live `main`. That is an ordinary merge. It is not a rebase and not a force update. GitHub reports the pull request `MERGEABLE` and `CLEAN` onto that `main`.

**What the proof diff is.** From `9271ba96` to `74252a5b`, two files change. `ch01-counting.tex` does not. Its git blob stays `45b451d1194ac238f60da615e2844504cfd40635`. `ch11-brownian.tex` changes from blob `7d4bd25d6a809e083af4c1e6c7bf9f394f587e30` to `26e4400c45d83e53a9e415cd24952eccbf0d26dc`, and the merge keeps that blob. The source pin in `tools/test_volume4_phase2_signed_off_sources_ch12.py` is that new blob, and the test still asserts equality with it. Labels are unchanged. Chapter 11 still has 5 theorems and 7 exercises. Chapter 1 still has 1 theorem, 8 exercises, and one unnumbered `lemmax`.

### The atom sentence

Lines 100–106 restrict the sandwich to \(t\in(0,1]\), and they record that \(t_n>0\) for every large \(n\). Lines 120–124 replace the sentence that gave the limit strip the Gaussian integral. The new text says: off \(E_n\), \(|B_t-B_{t_n}|\le\delta_n\), so
\[
\{B_t=x\}\subset E_n\cup\{x-\varepsilon-\delta_n<B_{t_n}\le x+\varepsilon+\delta_n\}.
\]
The second set is a bounded interval of the linear image \(B_{t_n}\). Line 106 already gives that interval the Gaussian integral, of length \(2\varepsilon+2\delta_n\). Subadditivity adds \(P^*(E_n)\). The standard-normal density of variance \(t_n\) is at most \(1/\sqrt{2\pi t_n}\), so the sum is at most \(P^*(E_n)+(2\varepsilon+2\delta_n)/\sqrt{2\pi t_n}\). Send \(n\to\infty\), using \(P^*(E_n)\to 0\), \(\delta_n\to 0\), and \(t_n\to t>0\). Then send \(\varepsilon\downarrow 0\). The outer content of \(\{B_t=x\}\) is 0.

That is the comparison the third pass asked for. It uses the linear-image equality and subadditivity. It does not price a strip of the limit by subtracting two half-lines, and it does not use \(P^*(\mathrm{complement})=1-P^*\). For \(t\in(0,1]\) the denominator \(\sqrt{t_n}\) is positive for large \(n\). No new gap.

The half-line law, the joint distribution function, the extension to \([0,\infty)\), and the reflection identity \(1-\Phi(a/\sqrt t)\) are the argument approved at `9271ba96`. They are still in the file.

### The fingerprint

Against `main` `6e5cc70d`, the only snapshotted source whose hash differs is `volume4-chance/chapters/ch01-counting.tex`, from `d4a32f1b…` to `df3f737679ce2583effd86e31bdbcd1ace11bc4c34c76294c6407930cd9926bc`, which is the sha256 of the approved Chapter 1 file. The stored snapshot hash is `2fb5c2aa1da3a82c1e5d13167ce6d0c1f72c37a6cae97379c7a5d277d28fce52`. All 120 concept entries stay `accepted-internal`. No file under `volume3-symmetry/` changes. `tools/test_volume3_internal.py` still rejects a snapshot whose sha256 has been replaced by zeros. The gate compares hashes. It was not turned off.

The cover-note hash in the snapshot is `7d9bb310cdd17fdf3d0e53c12987a932397de1208fee5a15b64d542413e84359`, the sha256 of `common/cover-notes.json` on both this head and `main`. That change arrived with the merge of #184. It is not a Volume 3 manuscript edit. `seam-sources.json` updates the Chapter 1 hash and writes an existing en dash as a character rather than a JSON escape. The Chapter 8 sentence is the same sentence.

### Checks on this head, separate from the proof

[Build books 43074401955](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43074401955) completed success on `f7dc4d4a`, including `list`, `debs`, all fifteen volume builds, and `site`. `publish` is skipped. [Volume 4 native QA 43074401670](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43074401670) completed success on the same SHA. Those runs are the writer’s green builds. They are not the proof, and they are not the build of this review note.

The review note’s own build, on commit `99e9eecfd1f7538a2e4917c179cfd51a7c7b241f`, is [43085665060](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43085665060). It completed success. `list` and `site` succeeded. The volume matrix, `debs`, and `publish` were skipped. That run is not a proof of the Brownian theorems.

### Current disposition of all twenty IDs

Live `main` is `6e5cc70d814c9cc196a399aaa3982bb56803d501`. The approved Brownian head is `f7dc4d4ad17cc21fd163812c646e0132a530912b`.

| ID | Disposition |
| --- | --- |
| V4R2-01 | Approved at `f7dc4d4a`. The dyadic lemma and the linear-image equality stand, and the atom is the dyadic strip. |
| V4R2-02 | Closed on `main` by #176. |
| V4R2-03 | Closed on `main` by #178. |
| V4R2-04 | Closed on `main` by #178. |
| V4R2-05 | Closed on `main` by #177. |
| V4R2-06 | Merged in #186 at `5a0c0d9d5576a5986ea5ad0f8679fb709473a185`. |
| V4R2-07 | Merged in #184 at `414cb76f8c01ef89af5ea7fa14b639e069c14f32`. |
| V4R2-08 | Closed on `main` by #183. |
| V4R2-09 | Closed on `main` by #185. |
| V4R2-10 | Approved at `f7dc4d4a`. The half-line \(1-\Phi(a/\sqrt t)\) is the lower half-line of \(-B\). |
| V4R2-11 | Merged in #182 at `21cb46f07126287a7c918e6a79ec62ac8b02f503`. |
| V4R2-12 | Merged in #182, same commit. |
| V4R2-13 | Merged in #181 at `fb05d3f2f8873bfea9ed34758764badf70ca685a`. |
| V4R2-14 | Merged in #189 at `6e5cc70d814c9cc196a399aaa3982bb56803d501`. |
| V4R2-15 | Approved inside #180 and still present at `f7dc4d4a`. |
| V4R2-16 | Approved inside #180 and still present at `f7dc4d4a`. |
| V4R2-17 | Merged in #189. |
| V4R2-18 | Merged in #189. |
| V4R2-19 | Merged in #189. |
| V4R2-20 | Merged in #189. |

## Third pass — head `9271ba96`, historical record of the approval before the atom sentence

**Reviewer.** Same independent reviewer, `bc-114da047-b320-5bb0-b0d1-2f6495477a25`. The new commits are still by writer `bc-0f6fa3d7`. This pass did not edit that branch.

**Live head.** [#180](https://github.com/OussamaSegh/Order-and-Chance/pull/180) is `9271ba96cacc8ed51f2bfed37bce050a179ea5bd`. It is a descendant of `3bb6331ef89bd9b74a57a1ad2640a79ffc9a13d3`. The two new commits are `ca63460f` (the dyadic lower bound) and `9271ba96` (the Volume 3 seam fingerprint). `main` has moved to `6e5cc70d814c9cc196a399aaa3982bb56803d501`, the merge of #189. Pull requests #181, #182, #184, #186, and #189 are merged. #180’s base is still `a2cfdd30`, and GitHub reports it `CONFLICTING`. The only file changed on both sides is `review/volume3-internal/concepts.json`. The chapter files merge. This review does not rebase the writer branch.

**Verdict.** V4R2-01 and V4R2-10 are closed at this head. Theorems 12.4 and 12.12 are the original sentences, labels `thm:levy` and `thm:reflection`. No label was added or removed. Theorem counts stay 1 and 5 in the two edited chapters, and exercise counts stay 8 and 7. `lemmax` is an unnumbered lemma, so it does not move a number. No caption, font, or figure text changed. The source pins `45b451d1194ac238f60da615e2844504cfd40635` and `7d4bd25d6a809e083af4c1e6c7bf9f394f587e30` are the git blobs of `ch01-counting.tex` and `ch11-brownian.tex`. The comments say they are not an independent sign-off.

A green build is not the reason for this approval. The proof was read. The build is recorded separately below.

### The lower bound is now a proof

`ch01-counting.tex` lines 101–130, unnumbered lemma “dyadic outer content”. It states four facts: a finite disjoint union of half-open dyadic intervals has outer content equal to the sum of its lengths; one half-open interval `[c,d)` has outer content `d-c`; a countable set of points has outer content 0; deleting a null set does not change outer content.

The argument does not assume countable additivity, and it does not use `P*(A^c)=1-P*(A)`.

- Monotonicity is the definition: a cover of a larger set covers a subset.
- A point sits in `[x, min(1, x+2^{-M}))`. A countable set is covered by intervals of lengths `η 2^{-k}`. That is a countable cover, which the definition of outer content already allows.
- If `P*(N)=0` and `N⊂A`, subadditivity gives `P*(A)≤P*(A\N)`, and monotonicity gives the other inequality. Proposition `prop:subadd` is already proved before the lemma.
- For one dyadic interval, the interval is a cover, so outer content is at most its length. For the matching lower bound, a countable half-open cover is enlarged by `ε_i` with `∑ε_i<η` to an open cover of the compact segment `[a,b-δ]`. The least-upper-bound property, Volume 1, Chapter 3 (`ch05-sequences-series.tex`; the language chapter is Chapter 0), produces a finite subcover. The greedy right-endpoint walk on that finite cover has total length greater than `b-δ-a`. Sending `η` and then `δ` to 0 shows every cover is at least as long as the interval. The right endpoint `b` is excluded from `[a,b)`, and the closed segment stops at `b-δ`, which does lie in the interval.
- A finite disjoint union is covered by its pieces. For a cover of the union, the intersections with each piece are half-open, cover that piece, and are disjoint inside each cover interval, so the one-interval bound adds.
- A general half-open interval contains a dyadic union that omits at most one cell of length `2^{-N}` at each end. Monotonicity and the dyadic equality give the lower bound. Let `N→∞`.
- Proposition `prop:bits` writes a finite-bit event as a finite union of disjoint level-`n` cylinders. The lemma equates its outer content with the sum of those lengths.

This is the lemma the second pass asked for. It is proved from the definition, subadditivity, and the least upper bound. It is not an analogy with the one-coordinate squeeze.

### Transfer into the Brownian argument

`ch11-brownian.tex` line 62 now uses that lemma on both sides of the uniform squeeze. The inner dyadic union sits in the threshold except for countably many endpoints. Its outer content equals its length, deleting the endpoints does not change that content, and monotonicity lifts the lower bound to the threshold. The outer union covers the threshold and has outer content equal to its length. The two lengths approach the Gaussian tail, so the outer content equals that tail. The self-cover is no longer asked to do both jobs.

Lines 79–83 do the same for a finite linear image `L=∑ c_j Z_j`. The outer cubes, replaced by dyadic unions whose lengths overshoot the Gaussian masses by less than `η`, plus the coordinate tails, give `P*≤γ+3η` by subadditivity. The inner cubes, replaced by one common disjoint dyadic union, have outer content equal to a length at least `γ-3η`, and that set sits in the digit event after the endpoints are deleted. Monotonicity gives the lower bound. Every `η>0` works, so `P*=γ`. The tail bound `P*(E_n)≤2^n e^{-n}+∑_{k≥n}2^k e^{-2k}` still uses only the upper bound. The integral `≤ e^{-n}/√(π n)` is a numerical check of the Gaussian tail, not the outer-content proof.

The sandwich at line 120 is now two proved inequalities. The lower one uses `P*({B_{t_n}≤x-δ_n})=Φ_{t_n}(x-δ_n)`, the linear-image equality, and subtracts `P*(E_n)`. The upper one adds `P*(E_n)` to the enlarged dyadic half-line. Both Gaussian values tend to the distribution function of `N(0,t)`. So `P*({B_t≤x})` equals that distribution function.

One increment uses both endpoints and the same equality. Several disjoint increments are handled as a quadrant of uncorrelated linear images. The product integral equals `∏ Φ(α_r/√ℓ_{n,r})` because Theorem `thm:gaussvec` rotates the coefficient rows to independent standard normals and reads rectangle probabilities from the product density. That theorem states that it does not use Lévy’s continuity theorem. The cube transfer then copies the one-image argument: the Chapter 1 lemma prices the assembled dyadic union, and the inclusions with `±2δ_n` pass to the limit. The joint distribution function equals the product of the marginals. That is the independence in Definition `def:bm`.

On `[0,∞)`, pieces from different unit copies are conditions on disjoint bit blocks. Proposition `prop:manyuniforms` multiplies the lengths, and the Chapter 1 lemma turns the product into the outer content of the intersection. The quadrant argument applies to the resulting uncorrelated linear images. The upper half-line `{B_t≥x}` is the lower half-line of `-B_t`, and `-S_n` is the linear image with the signs reversed. The sandwich applies to that image. This is not the rule `P*(complement)=1-P*`.

The reflection statement at line 359 is unchanged. Line 428 identifies `1-Φ(a/√t)` by that negated linear image. The window, the factor 12, the order of `δ` then `ε`, and the strip of `S_n` are the argument already accepted as algebra at `3bb6331e`. They now sit on an equality that has been proved. The density derivative and the divergent integral `∫_1^∞ t^{-1/2} dt` remain calculus checks of the displayed formula, not a substitute for the half-line.

One sentence is looser than the proof around it. Line 120 says the limit strip `{x-ε<B_t≤x+ε}` has outer content equal to a Gaussian integral of length `2ε`. The equality that was proved for a bounded interval applies to a finite linear image, and the text has already said that subtracting two half-lines does not price a strip of the limit. The atom `P*({B_t=x})=0` follows from the inclusion already used for half-lines: the strip sits in `E_n` or in a dyadic strip, and the dyadic strip’s outer content equals the integral. The reflection’s own atom sentence uses the strip upper bound proved there, which tends to 0 with the width. This loose sentence does not reopen Theorems 12.4 or 12.12. The minimal wording, if the writer touches the line, is to name the dyadic strip.

### The Volume 3 fingerprint

`ca63460f` would fail `list` because `ch01-counting.tex` is a tracked seam source and its hash changed. `9271ba96` records the new hash. It does not turn the check off.

- `review/volume3-internal/seam-sources.json` changes the sha256 of `volume4-chance/chapters/ch01-counting.tex` to `df3f737679ce2583effd86e31bdbcd1ace11bc4c34c76294c6407930cd9926bc`, which is the sha256 of the file at this head. The Chapter 8 note is the same sentence; a JSON escape became the en dash it already denoted.
- `concepts.json` keeps 120 entries, every one `accepted-internal`. The only entry-level change is `reviewed_snapshot_sha256`. The snapshot’s source list changes only that Chapter 1 hash. The new key `v4r2_dyadic_outer_content_seam_retention` says the refresh is not a Volume 3 approval and not a sign-off of the lemma.
- No file under `volume3-symmetry/` changed. `tools/test_volume3_internal.py` still rejects a snapshot whose sha256 has been replaced by zeros. The gate compares hashes. It was updated, not bypassed.

### Checks, separate from the proof

On this head, Build books [43066297012](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43066297012) has `list`, `debs`, all fifteen volume builds, and `site` in success. `publish` is skipped. Volume 4 native QA [43066296996](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43066296996) succeeded. That is the writer’s green run. It is not the proof.

### Current disposition of all twenty IDs

`main` is `6e5cc70d814c9cc196a399aaa3982bb56803d501`.

| ID | Disposition |
| --- | --- |
| V4R2-01 | Closed at `9271ba96`. The dyadic lemma supplies the lower bound, and the linear-image equality is proved from it. |
| V4R2-02 | Closed on `main` by #176. |
| V4R2-03 | Closed on `main` by #178. |
| V4R2-04 | Closed on `main` by #178. |
| V4R2-05 | Closed on `main` by #177. |
| V4R2-06 | Merged in #186 at `5a0c0d9d5576a5986ea5ad0f8679fb709473a185`. |
| V4R2-07 | Merged in #184 at `414cb76f8c01ef89af5ea7fa14b639e069c14f32`. |
| V4R2-08 | Closed on `main` by #183. |
| V4R2-09 | Closed on `main` by #185. |
| V4R2-10 | Closed at `9271ba96`. The half-line `1-Φ(a/√t)` is the lower half-line of `-B`, not a complement rule. |
| V4R2-11 | Merged in #182 at `21cb46f07126287a7c918e6a79ec62ac8b02f503`. |
| V4R2-12 | Merged in #182, same commit. |
| V4R2-13 | Merged in #181 at `fb05d3f2f8873bfea9ed34758764badf70ca685a`. |
| V4R2-14 | Merged in #189 at `6e5cc70d814c9cc196a399aaa3982bb56803d501`. |
| V4R2-15 | Closed inside #180 and still present at `9271ba96`. |
| V4R2-16 | Closed inside #180 and still present at `9271ba96`. |
| V4R2-17 | Merged in #189. |
| V4R2-18 | Merged in #189. |
| V4R2-19 | Merged in #189. |
| V4R2-20 | Merged in #189. |

Audit #190 has moved to `9896c5ca0a7bc06b90081ca2f4752b96f7e32e1c`. This pass did not re-read it.

## Second pass — head `3bb6331e` and pull request #189

**Reviewer.** Same independent reviewer, `bc-114da047-b320-5bb0-b0d1-2f6495477a25`. The new commits are by a different writer run, `bc-0f6fa3d7`. This pass did not edit those branches, did not merge, and did not comment on them.

**Live heads, checked before this section was written.**

| PR | Live head | Parent | Base |
| --- | --- | --- | --- |
| [#180](https://github.com/OussamaSegh/Order-and-Chance/pull/180) | `3bb6331ef89bd9b74a57a1ad2640a79ffc9a13d3` | `fd0aa1cac46cf0df819e6cb1daf570ba3a51a1a7` | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` |
| [#189](https://github.com/OussamaSegh/Order-and-Chance/pull/189) | `e21f0e2be08bab75bc6657e2ad7d861386ac271d` | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | same |

Commit `3bb6331e` is an ordinary child of `fd0aa1ca`. Its message is “Price Brownian bin increments and reflection strips by rectangle covers.” `main` was still `a2cfdd30`. Both pull requests were `MERGEABLE` / `UNSTABLE`.

**Verdict.** Do not approve #180 as a finished proof of Theorem 12.4 or Theorem 12.12. Approve the five repairs in #189. The theorem sentences are the original ones. No caption, font, figure, or label moved in either diff.

### The rectangle cover proves an upper bound

File `volume4-chance/chapters/ch11-brownian.tex` at `3bb6331e`. The new argument is lines 71–79.

The integral calculation on line 75 is calculus, and it is separate from outer content. It integrates the product of the coordinate Gaussian densities one variable at a time. The step-function approximation on a compact set, with Gaussian tails cut by Proposition `prop:gausstail`, is the same kind of iteration already used for a continuous integrand on a rectangle. The induction on the number of coordinates is the right reduction: a linear image of one normal is the one-variable integral; a further coordinate \(cZ_m\) produces a bounded continuous function \(g\) of the previous image; Lemma `lem:normalsum` is used only as the completion of the square for two densities. A zero coefficient is the one-coordinate case. A negative \(c\) reverses the interval. This calculation shows that the product integral over \(\{a<L\le b\}\) equals the \(N(0,\sigma^2)\) probability \(\gamma\). It does not show that a digit event has outer content \(\gamma\).

The transfer on lines 77–79 does prove the cover inequality \(P^*\le\gamma\).

- A coordinate rectangle pulls back to an interval condition on finitely many uniforms. Proposition `prop:manyuniforms` prices that condition by the product of the lengths, which is the Gaussian mass of the rectangle.
- Chapter 1, `ch01-counting.tex` line 88, gives only one comparison for a finite union of intervals: outer content is at most the assigned length, because the set covers itself. The outer dyadic unions in the proof of `prop:manyuniforms` therefore give \(P^*(\text{pulled-back rectangle})\le\) its Gaussian mass.
- The cubes that meet \(\{a<L\le b\}\), together with the coordinate tails outside the box, cover the digit event. Subadditivity and the Lipschitz bound \(\lambda=\sum|c_j|\) put the outer content at most \(\gamma+2\eta\). Sending \(\eta\) to 0 yields \(P^*\le\gamma\).

Line 73’s rejection of Chebyshev is a correct numerical remark, not a proof: \(\sigma^2/a_n^2=1/(2n)\) and \(\sum 2^n/(2n)\) diverges. Lines 83–86 are the Gaussian integral for the standardised height \(\sqrt{2n}\). That integral is at most \(e^{-n}/\sqrt{\pi n}\), hence at most \(e^{-n}\). Combined with the cover inequality, the outer content of one bin threshold is at most \(e^{-n}\). Line 92 then has
\[
P^*(E_n)\le 2^n e^{-n}+\sum_{k\ge n}2^k e^{-2k},
\]
which tends to 0. The displacement half on lines 62–69 still avoids Theorem `thm:bc`. The modulus on line 94, the almost-sure Cauchy property, and the choice of \(t_n\) on lines 96–100 use that upper bound. Those parts stand.

### Equality is not proved, and the one-coordinate case does not supply it

Line 75 states the claim as equality: the digit event has outer content \(\gamma\). Line 79 proves \(P^*\le\gamma\), then says the inner cubes are the other half of “the squeeze already used for one coordinate, where the outer content equals the Gaussian value.” Line 62 is that one-coordinate sentence: the squeeze of dyadic cylinders makes “the outer content of the condition” equal to the Gaussian tail.

Chapter 1, line 88, says the matching lower bound — that no cover of a finite union of intervals is shorter than the assigned length — is not proved. Outer content is monotone, so a subset’s outer content is a lower bound for the set that contains it. The inner cubes have assigned probability at least \(\gamma-2\eta\). That assigned probability is not known to equal their outer content. Without \(P^*(\text{inner cubes})\ge\) their length, the inclusion of the inner cubes does not force \(P^*(\{a<L\le b\})\ge\gamma\).

The one-coordinate squeeze has the same shape. The outer dyadic unions prove \(P^*\le\) the interval length. The inner unions prove a lower bound only if those finite-bit events already satisfy \(P^*=P\). That is the comparison Chapter 1 declines to prove. Line 79 cites line 62. Line 62 does not contain the missing lemma. The equality is not proved for one coordinate, and it is not proved for a linear image. There is no earlier proof to borrow.

The tail sums do not need the equality. Line 79 says so, and the inequality on line 92 really uses only \(P^*\le\gamma\). The distributional sandwich does need it.

Lines 112–116 subtract \(P^*(E_n)\) from \(P^*(\{B_{t_n}\le x-\delta_n\})\). The right-hand half of that display, together with the cover inequality, does give
\[
P^*(\{B_t\le x\})\le F_{t_n}(x+\delta_n)+P^*(E_n),
\]
and the right-hand side tends to the distribution function of \(N(0,t)\). The left-hand half tends to that same function only if \(P^*(\{B_{t_n}\le x-\delta_n\})\) is already equal to the Gaussian value, or at least within \(\eta\) of it from below. Line 102 asserts that equality. Its only source is line 79. An upper bound \(P^*\le F\) makes the left-hand half useless: it can sit far below \(F\).

So Theorem 12.4’s construction, continuity, and modulus are in place, and its identification of \(P^*(\{B_t\le x\})\) with the Gaussian distribution function is not. Line 116 extends the same unproved equality to half-lines of an increment. Line 118 still says the joint distribution function is squeezed to the product of the marginals. A joint rectangle needs the same missing lower bound, and the sentence does not build one. Definition `def:bm` requires those laws and the independence. The theorem sentence on line 59 is unchanged. It is not weakened, and it is not yet proved.

The repair is one lemma, proved at the Chapter 1 standard: the outer content of a finite union of half-open dyadic intervals equals the sum of their lengths. After that lemma, the inner cubes on line 79 give the matching lower bound, and the same lemma feeds the one-coordinate thresholds. Until it is proved, lines 62, 79, 102, 116, and 127 should not say “equals”.

### What the reflection repair does settle

Lines 96–100 name \(t_n=2^{-n}\lfloor 2^nt\rfloor\), the left endpoint of the level-\(n\) bin that contains \(t\in(0,1]\). The distance bound \(|B_t-B_{t_n}|\le a_n+\rho_n\) uses one bin increment and one copy of \(\rho_n\), because the dyadic value is already final. A neighbouring dyadic is excluded. That detail is right.

Line 127 gives every unit copy its own \(E_n\), and it builds the comparison position \(S_n\) in the copy that contains \(t\). An integer time is the right endpoint of the preceding copy. Line 346 puts the hitting window in that same copy. Those details are right.

Lines 348–353 no longer price the strip \(\{|B_t-a|\le\omega_n\}\) by subtracting half-line contents. The strip sits in \(G_n\) or in a bounded interval of \(S_n\). The cover inequality, not the equality, bounds that interval by length times maximum density, \(2(\omega_n+\delta_n)(2\pi v_n)^{-1/2}\). For large \(n\), \(v_n\ge t/2\). The window’s outer content tends to 0. This step uses the proved half of the rectangle argument.

The continuous-test algebra from the first pass is still the text after line 355: \(\delta\) before \(\varepsilon\), factor \(12=2\times 6\), and indicators kept out of the restart identity. The comparison that sends \(R_n\) to \(R\) uses an upper bound on an increment tail and on a strip. Those upper bounds follow from the cover inequality and Proposition `prop:gausstail`, even though line 360 says the half-line contents “equal” the Gaussian tails.

Line 404 then says the extension supplies the upper half-line and that its outer content is \(1-\Phi(a/\sqrt t)\). That sentence is the unproved equality. The atom \(\{B_t=a\}\) does go to outer content 0, because it sits in every strip and the strip’s cover bound tends to 0 with the width. The two sides \(L\) and \(R\) match by the continuous test. The displayed value
\[
P(M_t\ge a)=2\bigl(1-\Phi(a/\sqrt t)\bigr)
\]
on lines 335 and 404 needs the half-line equality. Theorem 12.12 is unchanged and is not proved. The density derivative on lines 406–409 and the divergence of \(\int_1^\infty t^{-1/2}\,dt\) are calculus applied to that formula. They were recomputed and they are not a substitute for the missing lower bound.

V4R2-15 and V4R2-16 remain fixed at lines 12 and 300 of this longer file; those sentences were not part of the new diff.

The source pin in `tools/test_volume4_phase2_signed_off_sources_ch12.py` is `be598028839c9125bd1adc7d7058cf7124a4d301`. That is `git rev-parse 3bb6331e:volume4-chance/chapters/ch11-brownian.tex`. The comment says the pin is source identity, not an independent sign-off. This review does not treat it as one.

### Pull request #189 — five sentences, approved

Head `e21f0e2be08bab75bc6657e2ad7d861386ac271d`. No figure, caption, font, or `\label` is in the diff. The pins below match the git blobs and the comments say they are not an independent sign-off.

| ID | Location at this head | Verdict |
| --- | --- | --- |
| V4R2-14 | `ch10-martingales.tex` line 311 | Approved. The factor \((n+2)/(n+1)\) tends to 1. The omitted interval has width \(1/(n+2)\), so its contribution tends to 0 because \(g\) is bounded. The truncated sum therefore tends to \(\int_0^1 g\). The false limit “tends to 1” is gone. Pin `ab52d91b23073cb53bd0c83566da13845d604c35`. |
| V4R2-17 | `ch07-entropy.tex` line 239 | Approved. The sibling of a deepest leaf is a leaf: an internal sibling would have a child at greater depth. The probability \(s\) is then a symbol probability, and \(s\ge q\) applies. Pin `6eb06ea39e6563595171939ffe6237a7e3af19d3`. |
| V4R2-18 | `ch07-walks.tex` lines 16–18 | Approved. The exact value \(\binom{2m}{m}2^{-2m}\) is the count of \(m\) steps each way. The asymptotic is Theorem `thm:local`. The displayed formula is unchanged. |
| V4R2-19 | `ch07-walks.tex` line 246 | Approved. The citation is Volume 1, Chapter 8, \(\int_0^\infty e^{-u^2}\,du=\sqrt\pi/2\). Evenness doubles it to \(\sqrt\pi\). With \(a=n/(4d)\), the substitution gives \(\sqrt{\pi/a}\), and \(d\) factors give the displayed \((4\pi d/n)^{d/2}\). That last power was already the right value; the citation now matches the half-line Volume 1 prints. |
| V4R2-20 | `ch07-walks.tex` lines 451 and 454 | Approved. The idea starts at \(-2\), and the solution sets \(D_0=-2\). |

Walks pin `d23df25f67660781c6d1bae09469f7d4c535079b` matches the blob of `ch07-walks.tex`.

### Current disposition of all twenty IDs

| ID | Disposition after this pass |
| --- | --- |
| V4R2-01 | Not closed. Theorem 4.4 is still not mis-cited, and \(P^*(E_n)\to 0\) now follows from a proved cover inequality. The law in Theorem 12.4 needs \(P^*=\gamma\), and line 79 does not prove it. |
| V4R2-02 | Closed on `main` by #176. |
| V4R2-03 | Closed on `main` by #178. |
| V4R2-04 | Closed on `main` by #178. |
| V4R2-05 | Closed on `main` by #177. |
| V4R2-06 | Repair approved in #186 at `b071f8d919e7a8cf7365b1213ca3628883f1fcc6`. Exact-head `site` job still red. |
| V4R2-07 | Repair approved in #184 at `264518e7ac5006cbb35d01bf530f55e6ffa3f7fc`. Exact-head `site` job still red. |
| V4R2-08 | Closed on `main` by #183. |
| V4R2-09 | Closed on `main` by #185. |
| V4R2-10 | Not closed. The strip, the bin endpoint, and the \(t>1\) copy are repaired. Line 404 still equates the half-line with \(1-\Phi\). |
| V4R2-11 | Repair approved in #182 at `5131283032a53713afcd7bc0f9a6aa9679180e35`. Exact-head `site` job still red. |
| V4R2-12 | Repair approved in #182, same head. |
| V4R2-13 | Repair approved in #181 at `e2e80191e195425c153013b2cefdb97cf7f10ed9`. Exact-head `site` job still red. |
| V4R2-14 | Closed by the sentence in #189. |
| V4R2-15 | Closed in #180; still present at `3bb6331e`. |
| V4R2-16 | Closed in #180; still present at `3bb6331e`. |
| V4R2-17 | Closed by #189. |
| V4R2-18 | Closed by #189. |
| V4R2-19 | Closed by #189. |
| V4R2-20 | Closed by #189. |

### CI read once on the new heads

Both Build books runs were already terminal. Only `site` failed, again at poppler, exit 100, `Temporary failure resolving 'azure.archive.ubuntu.com'`. All fifteen volume builds succeeded. This pass did not rerun anything and did not request a token.

| Run | Head match | Conclusion | URL |
| --- | --- | --- | --- |
| 43044478991 Build books, #180 | `3bb6331e` | failure; `site` only | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43044478991 |
| 43044478943 Volume 4 native QA, #180 | `3bb6331e` | success | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43044478943 |
| 43044572385 Build books, #189 | `e21f0e2b` | failure; `site` only | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43044572385 |
| 43044572307 Volume 4 native QA, #189 | `e21f0e2b` | success | https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43044572307 |

The same DNS failure is still the blocker for a green exact-head merge. Native QA success is not a proof of Theorem 12.4 or Theorem 12.12. Parent has not approved a merge on a red `site` job. This review does not approve one.

## First pass — disposition of the five open pull requests at `fd0aa1ca`

This table is the first reading. The current heads and verdicts are in the second pass above.

| PR | Live head (full) | Base | Merge git | Mathematical disposition |
| --- | --- | --- | --- | --- |
| [#180](https://github.com/OussamaSegh/Order-and-Chance/pull/180) | `fd0aa1cac46cf0df819e6cb1daf570ba3a51a1a7` | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | `MERGEABLE` / `UNSTABLE` | **Do not approve.** V4R2-15 and V4R2-16 are fixed. V4R2-01 is only partly fixed. V4R2-10 is not fixed. See the repair list below. |
| [#181](https://github.com/OussamaSegh/Order-and-Chance/pull/181) | `e2e80191e195425c153013b2cefdb97cf7f10ed9` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-13. The red check is the shared `site` apt failure, not this sentence. |
| [#182](https://github.com/OussamaSegh/Order-and-Chance/pull/182) | `5131283032a53713afcd7bc0f9a6aa9679180e35` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-11 and V4R2-12. Same `site` failure. |
| [#184](https://github.com/OussamaSegh/Order-and-Chance/pull/184) | `264518e7ac5006cbb35d01bf530f55e6ffa3f7fc` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-07. Same `site` failure. |
| [#186](https://github.com/OussamaSegh/Order-and-Chance/pull/186) | `b071f8d919e7a8cf7365b1213ca3628883f1fcc6` | same | `MERGEABLE` / `UNSTABLE` | **Approve the repair** of V4R2-06. Same `site` failure. |

The bodies of these five PRs still name older heads (`6643969c`, `34fc29d9`, `f4722b35`, `f4f7b2db`, `42d36c26`). Those are not the live heads. Guard any squash on the SHAs in the table above.

The jobs that run, and the exact-head conclusions, are in the CI section. `publish` is `main`-only. A green volume build is not a proof.

## What #180 had to repair at `fd0aa1ca`

The second pass replaces this section for head `3bb6331e`. File at the first-pass head `fd0aa1ca`: `volume4-chance/chapters/ch11-brownian.tex`. Theorem statements of existence (Theorem 12.4, label `thm:levy`) and reflection (Theorem 12.12, label `thm:reflection`) are the original sentences. No numbered environment was added. The source pin `fe398da68dcbd1405ab1808352be288681a4e817` matches `git rev-parse fd0aa1ca:volume4-chance/chapters/ch11-brownian.tex`.

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
