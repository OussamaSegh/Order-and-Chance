# Second review of the Volume 4 removed-material audit

**Reviewer.** Independent second reading by cloud agent `bc-114da047-b320-5bb0-b0d1-2f6495477a25` (grok-4.7). The audit itself was written by a different session, `bc-323d34bf`. This file does not edit the audit, the manuscripts, or any figure. It does not restore anything. The owner decides.

**Audit under review.** Pull request [#190](https://github.com/OussamaSegh/Order-and-Chance/pull/190). The current verdict is the reconciliation pass below, at live head `9896c5ca0a7bc06b90081ca2f4752b96f7e32e1c`. The current recommendation count is 12 restore, 1 repair, 19 optional, and 77 omit. Everything under the heading **First pass, historical** is the record of head `791d35f619e84c75c1bf8e2bf623bd2adcdf46ba`. The counts 16/1/18/74 and the red `site` job in that record are not the current verdict.

## Reconciliation pass — head `9896c5ca`

**What changed.** Two commits after `791d35f6`: `6dc3c31da5561559167b2d030b7d64931e193810` and `9896c5ca0a7bc06b90081ca2f4752b96f7e32e1c`. The diff is one file, `docs/review/volume4-removed-material-audit-2026-11-11.md`, 76 insertions and 24 deletions. No manuscript, figure, or KDP file is in the diff. This reading did not edit that branch and does not restore an exercise.

**Pins, dated, and not interchangeable.**

| Role | SHA | When |
| --- | --- | --- |
| Baseline, unchanged | `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6` | First parent of squash `e120d10a`, merged 8 November 2026. Still the pre-PR 111 tree. |
| Manuscript pin used by the audit | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | The audit’s “current main” cell. Commit `9896c5ca` is dated 11 November 2026, 17:21:48Z, and the merges of #181, #182, #184, #186, and #189 begin at 17:22Z. At the audit’s commit, that SHA was `origin/main`. |
| Live `main` at this reading | `6e5cc70d814c9cc196a399aaa3982bb56803d501` | `git rev-parse origin/main` on 11 November 2026, after those merges. Subject: the five round-2 sentences, #189, 18:24:32 +0100. |

The sentence “`git rev-parse origin/main` still returns `a2cfdd30`” is true of the audit’s commit and false of this reading. `a2cfdd30` is the manuscript pin. It is not live `main`. Between the two SHAs, `ch01-counting.tex`, `ch04-inequalities.tex`, and `ch08-markov.tex` have the same blobs, so the Chapter 1, Markov, and inequality lines cited below did not move. `extremal.tex` and `ch12-method.tex` each changed by the merged wording fixes. Those edits do not change the baseline solutions checked here.

**Verdict.** The corrected table matches the findings in the first pass. `pb:nouniform` is off the owner list. The knight row quotes the hand sum and is omitted. `ex:sharp` is marked partly rewritten, and part (b) stays off the list. The van der Waerden lower bound and both parts of balls and bins are on the checked list, with Berlekamp and Gonnet left out. The recommendation counts were recomputed from the cells, not taken from the prose. One section at the end of the note still states the old doubts. That is a documentation defect. It does not put the withdrawn rows back on the owner list.

### Counts, from the 109 exercise cells

A recommendation is counted by its first word. A class is counted the same way.

| First word of the recommendation | This reading | The note’s reconciled table |
| --- | ---: | ---: |
| restore | 12 | 12 |
| repair+restore | 1 | 1 |
| optional | 19 | 19 |
| omit | 77 | 77 |

The four numbers add to 109. The twelve restores are `ex:secretary`, `pb:goodman`, `pb:sicherman`, `pb:loaded`, `pb:subsetsum`, `ex:ballsbins`, `ex:mcmillan`, `pb:passone`, `pb:stick`, `pb:samecycle`, `pb:hashing`, and `extremal:ex:wlower`. The repair row is `ex:twotests`. Relative to the first-pass 16 restores, four cells left that column: `pb:nouniform`, `ex:knight`, and `ex:chromatic` now start with “omit”, and `ex:likelihood` now starts with “optional”. That is 16 − 4 = 12, and 74 + 3 = 77, and 18 + 1 = 19.

Class first words: 57 `lost`, 33 `too`, 9 `rewritten`, 7 `duplicate`, 1 `relocated`, 1 `partial`, 1 `partly`. The note’s sentence “2 with a relocation” is those last two rows, `ex:polyabeta` (“relocated”) and `ex:betagamma` (“partial relocation”). The “partly” row is `ex:sharp`. The first-pass total of 10 rewritten rows was the 9 that still start with “rewritten”, plus the old class of `ex:sharp`. The 174 triples, 65 retained labels, and 109 absent labels were not recomputed again. The row count is still 109, and the note does not change that arithmetic.

### The five corrections, checked again on the baseline

**`pb:nouniform`.** Baseline solution lines 700–719 say a singleton has mass at most \(1/m\) for every \(m\), hence mass 0, and then \(P(\mathbb N^*)=\sum_n P(\{n\})=0\). The exercise itself asks for a countably additive measure. Pinned `ch01-counting.tex` line 43, blob unchanged on live `main`, says countable additivity on a full infinite-event space is not proved. Finite additivity does not turn a countably infinite sum of zeros into zero. Withdrawing “restore (a)” is the right classification. Part (b), finite additivity of a density, is a count and is not promoted. Part (c) says that in any interval, \(B\) contains one of every two consecutive integers. With \(I_j=[4^j,2\cdot 4^j)\), the integer 3 is odd and outside every block, and 4 is even and inside \(I_1\), so both lie in \(B\). The sentence is false. The block proportions at \(N=2\cdot 4^j\) and \(N=4^{j+1}\) still tend to \(2/3\) and \(1/3\), and the even subset to about \(1/3\) and \(1/6\). This reading recomputed those limits. The note says it did not, and it does not use them to repair part (a) or the false sentence. That restraint is right.

**`ex:knight`.** Baseline solution lines 803–809 are the hand sum \(2\cdot 26+2\cdot 38+4\cdot 52=336\), corner return \(336/2=168\), centre return \(336/8=42\). The figure caption states the same degree sum. There is no program in that solution. The number 168 is both the edge count and the corner return. Pinned `ch08-markov.tex` line 221 proves reversibility for the degree weights. The word “return” elsewhere in that chapter is the period. The chapter does not state that the mean return time is \(1/\pi(x)\). Baseline `cor:graph` cited Kac’s formula for that identity, and that corollary is not the pinned text. Omitting the exercise is the right row. The earlier draft’s program count is withdrawn, as it should be.

**`ex:sharp`.** Baseline part (a) puts mass at \(0\) and \(a\). Baseline part (b) puts mass \(\sigma^2/(2a^2)\) at each of \(\pm a\). Pinned `ex:markovsharp` asks which tail probabilities \(p\) are possible for mean \(a\), and separately asks for Markov’s equality on \(\{0,a\}\). It does not ask for a prescribed variance. “Partly rewritten” is the right class. Part (b) stays off the owner list. The omit recommendation stands.

**`extremal:ex:wlower`.** The six lines check. A \(k\)-term progression in \([N]\) is \(a\ge 1\), \(d\ge 1\), \(a+(k-1)d\le N\). For each \(d\) there are \(N-(k-1)d\) positive choices of \(a\), and that decreasing sum is strictly less than \(\int_0^{N/(k-1)}(N-(k-1)x)\,dx=N^2/(2(k-1))\). Each progression is monochromatic with probability \(2^{1-k}\). If \(N^2\le(k-1)2^k\), the expectation is strictly less than 1, so some colouring of \([N]\) has none, and \(W(k,2)\) is larger than \(\lfloor\sqrt{k-1}\,2^{k/2}\rfloor\). Since \(W(k,2)\) is an integer, it is larger than the real bound as well. Berlekamp’s finite-field bound is a citation. Restoring the exercise without that sentence is the right limit. The first-moment method is already `thm:erdos` on the pinned book.

**`ex:ballsbins` (b).** \(\psi(u)=(\ln u+1-\ln 3)/u\) and \(\psi'(u)=(\ln 3-\ln u)/u^2\). The derivative is zero at \(u=3\), positive before it, and negative after it, and \(\psi(3)=1/3\). The solution’s comparison \(k(\ln k-1)\ge 2\ln n\) follows, and the union bound over \(n\) bins is at most \(1/n\). Gonnet’s matching lower bound is a citation. Restoring (a) and (b) without that citation is elementary. Part (a)’s \(\binom{n}{k}n^{-k}\le 1/k!\) and \(e^k\ge k^k/k!\) were already accepted.

**Wording that was already a condition.** Sicherman stays a restore only if the write-up peels irreducible factors by the division argument in Volume 1, Chapter 6, and does not cite a theorem titled unique factorisation of \(\mathbb Q[X]\). The face expansion is unchanged. `ex:twotests` stays a repair until the rates are in the prompt. Baseline `ex:medical` begins at line 129 and contains prior \(0.01\), sensitivity \(0.99\), and false positive \(0.05\). `ex:chromatic` is now omit, and the Bollobás asymptotic is named. `ex:likelihood` is optional and off the checked list. Those four match the first pass.

The parallel-reading proposals that stay off the list, including `pb:erdosselfridge`, the tiled-floor needle, carries, dice modulo \(m\), and Gilbreath, were not re-derived here. Volume 15, `conjectures-ch08-geometric.tex` line 136, does say that Volume 4, Appendix B, proves the happy-ending function finite by Ramsey’s theorem. Pinned `thm:ramsey` colours the edges of a complete graph. It is not the \(k\)-uniform theorem the baseline exercise used. That citation is a later repair. This reading does not edit Volume 15.

### The unresolved section was not brought up to the table

The reconciled table, the owner list, and the closing paragraph on small cuts agree with each other. The section headed “Unresolved” does not.

- It still says `ex:ballsbins` (b) and `extremal:ex:wlower` were not re-proved. The table and the reconciliation section say both were checked, and both are restores.
- It still asks whether the knight write-up uses the stationary formula or a different count, and it calls 168 the edge count. The table now quotes the hand sum 336. The edge count is 168, and the corner return is also 168. The open question in that bullet is the question the row already answered by omitting the exercise.

Those three bullets are stale. They do not change the owner list, because the list itself no longer contains the knight or the uniform integer, and it does contain the two checked bounds. The audit author has asked to delete only those three claims. Head `9896c5ca` still contains them. This reading will certify that deletion only after a new head of #190. It does not edit the audit.

The note’s own last sentence is the right strength: none of the checked list is approved for restoration by the audit, and this review does not restore it either.

### Checks, separate from the reading

On head `9896c5ca`, Build books [43067468190](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43067468190) has `list`, `debs`, all fifteen volume builds, and `site` in success. `publish` is skipped. A green docs build is not a mathematical acceptance. Pull request #180 was not re-read. A later head that resolves its fingerprint conflict is a separate exact-head review. It is not part of this note.

## First pass, historical — head `791d35f6`

This section is the record of the first reading. It is not the current verdict. The recommendation split here is 16 restore, 1 repair, 18 optional, and 74 omit. The current split, in the reconciliation pass above, is 12 restore, 1 repair, 19 optional, and 77 omit. The red `site` job below belongs to review-log #188 at `8c338504`. It is not the build of audit head `9896c5ca`, which is green. The pin `a2cfdd30` in the table below is what `origin/main` was during that first reading. Live `main` at the reconciliation reading is `6e5cc70d`.

**Pins, checked in git, at the first reading.**

| Role | SHA | Check |
| --- | --- | --- |
| Pinned `main` | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | `git rev-parse origin/main` returned this SHA on 11 November 2026. |
| Pre-PR 111 baseline | `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6` | First parent of squash `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`, “Rewrite Volume 4 from the Volume 1–3 boundary (#111)”. |
| Method checkpoint | `285122b4a592bfef3c695b1103dd2cd3e8c3a77a` | `ch12-method.tex` has 213 lines there. Not the book. |

`git log e120d10a..a2cfdd30 -- volume4-chance/chapters/ch12-method.tex` is empty. The pinned method file is blob `7bb8f4a676a46524817beb217d04f18ad6317a21`, 274 lines. The baseline file is blob `eb9d6c27cf75d112d74a2848f19ae6e934034d61`, 2037 lines. `gilmer.tex` is blob `dd703c9be37b4ab380392e0cc8c7922fd3e35c35`, 106 lines, at both SHAs. Baseline `ch04-inequalities.tex` line 540 is `\input{chapters/gilmer}`. Pinned `main.tex` does not input it.

The twelve baseline chapter blobs and line counts in the audit’s blob table match `git rev-parse` and `git show` line counts, including `gilmer.tex`.

## Historical first pass — counts at head `791d35f6`

Routed files are `main.tex` inputs, plus one nested input: `gilmer.tex` from baseline Chapter 4, and `ch05-geometric.tex` from the pinned continuous chapter.

| Count | Audit | This reading |
| --- | ---: | ---: |
| Baseline exercise / hint / solution triples | 174 / 174 / 174 | 174 / 174 / 174, no unmatched label |
| Pinned exercises on the route | 107 | 107 |
| Old labels still exercises | 65 | 65 |
| Absent labels | 109 = 68 `pb:*` + 41 others | 109 = 68 + 41, and no `pb:*` label is an exercise on the pinned route |
| Inventory rows | 109 | 109, all labels distinct |
| Classes | 10 rewritten, 2 relocated, 57 lost, 33 advanced, 7 duplicate | same split, sum 109 |
| Recommendations | 16 restore, 1 repair, 18 optional, 74 omit | same split, sum 109 |
| Statement lines of the 109, from the printed ranges | 970 | 970 |
| Solution lines of the 109, from the printed ranges | 2264 | 2264 |
| `git diff --shortstat 3cc07e86 a2cfdd30 -- volume4-chance` | 311 insertions, 122 deletions | 19 files, 311 insertions, 122 deletions |
| `3cc07e86` ancestor of the pin | yes | yes |

The arithmetic of the inventory is consistent with audit head `791d35f6`. No row is missing from the 109, and no class or recommendation total disagrees with the rows of that head. The recommendation line 16/1/18/74 is this historical count. The current count is 12 restore, 1 repair, 19 optional, and 77 omit.

## Historical first pass — what that reading accepted

**Renamed is not lost, where the target was opened.** `ex:longestrun` is now `ex:runs` at `ch04-inequalities.tex` lines 302–304, and the statement says convergence in probability and that a complete almost-sure statement is not required. `ex:betagamma` is the exercise of that label in `volume7-spaces/chapters/ch08-products.tex` line 344. `ex:polyabeta` in Volume 11, `ch09-martingales.tex` line 453, is the general Beta\((a,b)\) urn. `thm:commute` is in Volume 12 at `ch08-networks.tex` line 114. `conjectures:thm:gilmer` is in Volume 15 at `conjectures-ch08-geometric.tex` line 300, with the same constant arithmetic at line 377. The finite-method labels `thm:erdos`, `thm:alter`, `thm:lll`, `prop:second`, `prop:euler`, `prop:crossing`, `thm:subcrit`, and `thm:triangles` are in the pinned sources. `prop:race`, `thm:uniform`, `thm:ruin`, `ex:unfair`, `thm:kraft`, `prop:chain`, `thm:mutual`, `thm:buffon`, `thm:ramsey`, `thm:sunflower`, and `ex:schurtwo` are present. The old-to-new plan’s sentence that exercises 1.1–1.6 were rebuilt in the same slots, including “two tests”, is stale: `ex:twotests` is not in the pinned volume. The audit says the plan is not authority. That judgment is right.

**Measure block.** Baseline `ch05-continuous.tex` lines 17–18 say the chapter builds Lebesgue’s integral and proves monotone convergence, Fatou, and dominated convergence. Lines 107–120 admit Lebesgue measure, infinite products, and Tonelli–Fubini from Volume 7. Lines 33–43 are Vitali’s selector argument. Lines 237–245 are general dominated convergence from Fatou. The pinned theorem at lines 322–327 is the continuous, compact-uniform form, and lines 320–321 call it narrower. Removing the abstract block is justified. Restoring it would put Volume 7 back inside Volume 4 or would require a construction the pinned book does not have.

**Gilmer.** The constant identity \(1-1/c=(1-\ln 2)/2\) for \(c=2/(1+\ln 2)\) is arithmetic and holds. The defect estimate `conjectures:lem:hxy` was not re-proved by the audit and is not re-proved here. It is not a verified inequality. Omitting the file from the Volume 4 route is justified because Volume 15 states the theorem and the hard step is not certified. The unused file is a duplicate of the subject, not a byte copy of the Volume 15 chapter. The audit’s own words are the right strength.

**Large workshop tail.** The tools lines that cite Volume 5, Volume 6, Volume 8, Volume 12, Volume 13, the prime-number theorem, \(p\)-adics, or \(\mathrm{GL}_n\) support the “too advanced” class as a classification from the tools, not as a line-by-line certificate. This reading did not re-prove those 33 solutions. Treating the whole 33-problem list as one restoration would ignore those tools. The individual rows marked restore are a different decision.

**Page claim.** No baseline page count is asserted. The 289-page interior is tied to `3cc07e86`, an ancestor, not to `a2cfdd30`. That restriction is correct. The 300–600 sentence is a cap, not a quota. The audit does not recommend filler.

## Historical first pass — the seventeen restore or repair rows at `791d35f6`

These are the inventory rows whose recommendation starts with “restore” or “repair”. Twelve of them, plus the 2-SAT section, are the audit’s “checked” owner list. Four more are explicitly “after a line reading”. The audit does not claim those four are proved.

### Historical — accepted as solvable from Volumes 1–4, main step checked at `791d35f6`

The check is the method in the baseline solution, not the topic name.

| Item | What was checked | Prerequisite |
| --- | --- | --- |
| `pb:loaded` | AM–GM gives \(2/(2n-1)>1/(2n-1)\). The odd-degree root for \(n=6\) is the intermediate-value fact. | Volume 1, Chapter 9, and Chapter 6 for roots. Generating functions are Volume 4, Chapter 3. |
| `pb:goodman` | Double count of two-coloured angles. At \(n=6\), \(\lfloor 25/4\rfloor=6\) and \(20-18=2\). A random triangle is monochromatic with probability \(1/4\). | Counting and linearity. Ramsey \(R(3,3)=6\) is already `thm:ramsey`. |
| `pb:samecycle` | Length \(\ell\) occurs for \((n-1)!\) permutations. Hockey-stick gives probability \(1/k\) that \(1,\ldots,k\) share the cycle. | Volume 1 hockey-stick, Volume 4 conditioning. |
| `pb:hashing` | Determinant \(x-y\neq 0\). Collision probability \(\le 1/m+1/p\). With \(m=n^2\), Markov gives success probability at least \(1/2-n^2/(2p)\). | Volume 1 linear algebra. Markov is Volume 4. |
| `pb:stick` | \(P(\max A_j\ge 1/2)=n\,2^{-(n-1)}\). For three pieces the triangle probability is \(1/4\). \(\int_0^1 2t(1-t)^{n-1}\,dt=2/(n(n+1))\). | Uniform order and the tail formula for \(\mathbb E[X^2]\), both in Volume 4, Chapter 5. |
| `pb:passone` | Simplex volume \(1/n!\). \(\mathbb E[N]=e\), \(\mathbb E[N^2]=3e\), variance \(3e-e^2\). The decimal \(0.7657\ldots\) is that number. | The ordered-uniform map is the content of the solution and uses only volume preservation of a triangular map. |
| `ex:ballsbins` (a) | \(\binom nk n^{-k}\le 1/k!\) and \(e^k\ge k^k/k!\). | Union bound and the exponential series. |
| `ex:secretary` (a) and the \(1/e\) limit | \(p_r=\frac{r-1}n\sum_{k=r}^n\frac1{k-1}\). The integral comparison of the harmonic sum is Volume 1, Chapter 3, and the maximum of \(x\log(1/x)\) is \(1/e\). | The sentence “no strategy does better” cites Lindley and is not a proof. The audit already drops it. Keep it dropped. |
| `ex:mcmillan` | \(K^N\le N\ell_{\max}\) because each length has at most \(2^L\) distinct encodings, so \(K\le 1\). | Kraft for prefix codes is `thm:kraft`. This is the uniquely decodable extension, by counting. |
| `pb:subsetsum` (a) and (b) | For \(p=3\), four of the eight subsets. The formula \((2^p-2)/p+2\) gives 4. For \(p=5\), \((\binom{10}{5}-2)/5+2=52\). | The roots-of-unity filter is Volume 1, Chapter 5. Part (c)’s general necklace formula can stay optional, as the audit says. |
| `pb:sicherman` | \(x(1+x)(1+x+x^2)=x+2x^2+2x^3+x^4\), faces \(1,2,2,3,3,4\). The factorisation \(x+\cdots+x^6=x(1+x)(1+x+x^2)(1-x+x^2)\) has irreducible quadratics by the negative-discriminant test. | Volume 1, Chapter 6, proves the gcd and Euclid property in \(\mathbb K[X]\) and the discriminant test. It does not contain a theorem titled unique factorisation of \(\mathbb Q[X]\). The solution’s citation is a little ahead of the label. The peeling argument is still the gcd argument that chapter has. Restore is reasonable if the write-up says “peel irreducible factors”, not “by the unique-factorisation theorem”. |
| `extremal:ex:wlower` | Six lines. The number of \(k\)-term progressions in \([N]\) is \(<N^2/(2(k-1))\). Each is monochromatic with probability \(2^{1-k}\). If \(N^2\le(k-1)2^k\), the expectation is at most 1. | First moment, already `thm:erdos`. The audit left this unread. This reading checked it. Berlekamp’s finite-field bound is a citation and should stay out of the exercise. |
| `thm:twosat` | If \(\Psi(x)=n^2-x^2\) and the upward probability is \(\theta\ge 1/2\), then \(\mathbb E[\Psi(X_{t+1})]+1-\Psi(x)=2x(1-2\theta)\le 0\). The bound \(\mathbb E[t\wedge T]\le n^2\) sums finitely many histories. | The last line of the old proof says “monotone convergence”. For a nonnegative integer that limit is the tail sum \(\sum_k P(T\ge k)\), which does not need the measure-theoretic theorem. The audit’s rewrite instruction is the right one. Do not restore the section with the old last sentence. |

These are recommendations for the owner. They are not restorations.

### Historical — not accepted as a finished Volume 1–4 proof at `791d35f6`

**`pb:nouniform` (a), V4-RM-E05.** The audit marks this high confidence and puts it on the checked list. The baseline solution says \(P(\{n\})\le 1/m\) for every \(m\), hence the singleton has mass 0, and \(P(\mathbb N^*)=\sum_n P(\{n\})=0\). The tools line cites “Volume 4, Chapter 1 (additivity)”. The pinned Chapter 1, `ch01-counting.tex` line 43, says the book has not proved countable additivity on a full infinite-event space. Finite additivity does not make a countably infinite sum of zeros equal to zero. Part (a) as written uses a hypothesis the four volumes refuse. Do not restore it as a consequence of Chapter 1. A version that states “assume countable additivity” as an extra hypothesis would be a different exercise, and the audit’s part (c) already says densities give up that hypothesis. Part (c)’s block proportions, about \(2/3\) and \(1/3\) for the unions of \([4^j,2\cdot 4^j)\), hence about \(1/3\) and \(1/6\) for the even subset, match the description. That arithmetic was not in the audit. It still does not repair part (a).

**`ex:twotests`, the one repair row.** The arithmetic \(0.009801/0.012276\approx 0.798\) and \(3.96/4.96\approx 0.798\) checks, from prior \(0.01\), sensitivity \(0.99\), false positive \(0.05\). Those rates live in baseline Example `ex:medical` at `ch01-counting.tex` lines 129–138, which is not in the pinned book. The exercise prompt only says “in Example `ex:medical`”. The audit’s repair condition is right: the rates have to be written into the prompt. Until that is done, the exercise is not self-contained. This review does not treat the Bayes step as a reason to reject the repair. It treats the missing prompt as still open.

**`ex:knight`.** The degree sum \(2\cdot 26+2\cdot 38+4\cdot 52=336\), so 168 edges, corner return \(336/2=168\), centre return \(336/8=42\). That arithmetic checks. The solution is a hand sum from a figure, not “a direct program”. The pinned chapter does prove that the simple random walk on an undirected graph is reversible for the degree weights (`ch08-markov.tex` line 221). It does not state that the mean return time is \(1/\pi(x)\). The old solution cites `cor:graph` and `fig:knight`, neither of which is the pinned text. The audit already says the old write-up was not matched to the count. Leave this in the unread group. Do not list the number 168 as a checked restoration.

**`ex:chromatic` and `ex:likelihood`.** The audit says not line-checked. This reading agrees and does not certify them. The chromatic solution also quotes \(\mathbb E\chi\sim n/(2\log_2 n)\) from Bollobás 1988. That asymptotic is not a theorem of Volumes 1–4, so the sentence about the window being smaller than the mean is not a Volume 1–4 proof even if Azuma’s inequality is. The likelihood solution cites `thm:supconv` and `cor:slln` by old labels. Whether those steps are the pinned interval-partition theorem and the bounded strong law was not checked.

**`ex:sharp` is only partly rewritten.** Baseline part (a) is Markov’s equality. Pinned `ex:markovsharp` asks that question and separates it from a free probability \(p\). Baseline part (b) is Chebyshev’s equality at a prescribed variance. That part is not the pinned exercise. Calling the whole label “rewritten” overstates part (b). This is a small classification gap, not a restoration candidate unless the owner wants the variance example. The audit’s “omit” recommendation can stand for part (a). Part (b) is closer to lost.

**`ex:ballsbins` (b).** The audit left the maximum of \(\psi\) unchecked. This reading checked it: \(\psi(u)=(\ln u+1-\ln 3)/u\), \(\psi'(u)=(\ln 3-\ln u)/u^2\), maximum \(1/3\) at \(u=3\). The union bound in (b) then follows. Gonnet’s matching lower bound is a citation and should not be copied in as a proof. Part (b) without that citation is elementary. The audit’s “restore (a) only” is safer than wrong. It is stricter than the calculus requires.

## Historical first pass — issue log at `791d35f6`

| ID | Severity | Finding | What to do if the owner asks | Unresolved |
| --- | --- | --- | --- | --- |
| V4-AUD-01 | major for a restoration, not for the audit’s omission class | `pb:nouniform` (a) uses countable additivity. Volume 4, Chapter 1, says that tool is not proved. | Do not restore the solution as a corollary of Chapter 1. | Whether a finitely additive formulation is worth a different exercise. |
| V4-AUD-02 | minor | `ex:sharp` (b), Chebyshev equality at a given variance, is not `ex:markovsharp`. | Leave it out unless that example is wanted on its own. | None on the Markov half. |
| V4-AUD-03 | minor | The knight count is a hand sum, and the mean-return identity is not a pinned theorem. | Keep it in the unread group. | Whether \(1/\pi(x)\) is an easy corollary of the degree law already on the page. This reading did not derive it. |
| V4-AUD-04 | minor | `ex:chromatic` imports an external asymptotic. | Do not treat the row as checked. | The Azuma half, unread. |
| V4-AUD-05 | note | `extremal:ex:wlower` and `ex:ballsbins` (b) check by elementary arguments the audit did not finish. | They may join the owner list. Drop Berlekamp and Gonnet from the prompts. | None on the inequalities that were expanded here. |
| V4-AUD-06 | note | Sicherman’s “unique factorisation” name is ahead of Volume 1’s label. The gcd peeling is in Volume 1, Chapter 6. | Restore only with that wording. | None on the face expansion. |
| V4-AUD-07 | as the audit says | `conjectures:lem:hxy` and the Chernoff \(\delta^2/3\) calculus were not re-derived. | Do not describe them as verified. | Both inequalities. |

No issue here authorises a manuscript edit.

## Historical first pass — classifications left provisional at `791d35f6`

Rows whose confidence is low, or whose note says “not line-checked” or “Tools”, were not re-proved. That includes `pb:lcs`, `pb:kacring`, `pb:foata`, `pb:range`, and the network solutions past their tools lines. The audit’s confidence column already says so. Accepting the “omit” recommendation for a tools-line that names a later volume is a classification, not a certificate that the solution has no elementary core. `pb:lcs` is the row the audit itself leaves unresolved. It stays unresolved.

The 74 omissions include those rows and the advanced block. This reading accepts the large omissions: the measure engine, the Gilmer defect, the network chain as a chapter, and the workshop list taken whole. It does not accept every individual “omit” as a proof that the solution is empty of a Volume 1–4 exercise. The owner list is the right granularity.

## Historical first pass — owner list at `791d35f6`

Ready, with the limits named above: Sicherman (wording), loaded dice, Goodman, uniform cycle length, hashing, broken stick, wait to pass 1, balls and bins (a), and (b) without the Gonnet citation, secretary (a) and the \(1/e\) limit without the optimality sentence, McMillan, subset sums (a) and (b), the six-line van der Waerden lower bound without Berlekamp, and the 2-SAT section with the tail-sum sentence instead of “monotone convergence”.

Not ready: no uniform integer as written, the second medical test until the rates are in the prompt, the knight, the chromatic number, and the finite likelihood ratio.

Nothing in that list should be restored by this review. The page ledger, the Brownian branch, and the owner’s instruction still stand.

## Historical first pass — what was not done at `791d35f6`

- The 74 omit-rows were not all re-proved.
- `conjectures:lem:hxy` was not re-derived.
- No exercise was put back into a chapter.
- Figures were not reviewed.
- The pinned book was not rebuilt, so no page count of `a2cfdd30` is claimed.

## Historical first pass — CI recorded at `791d35f6`

This red job is not the current audit build. The build of head `9896c5ca` is the green run in the reconciliation pass.

Review-log pull request #188, head `8c338504f964f88e329bb06c82e65e0abc127009`, Build books run [43052798216](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43052798216), finished **failure**. `list`, `debs`, and all fifteen volume builds succeeded. `publish` was skipped. The only failed job is [`site`](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/43052798216/job/130662463390), exit 100, `Temporary failure resolving 'azure.archive.ubuntu.com'` while installing poppler. That is an infrastructure blocker. It is not a green build, and it is not a manuscript failure.
