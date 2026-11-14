# Second review of the Volume 4 scored-read close

**Verdict: REQUEST CHANGES**

**Head reviewed:** `123f44e43fc3f06817aa81461d5dbe8e7d24e4d9` on `cursor/v4-scored-read-final-b140`, pull request [#239](https://github.com/OussamaSegh/Order-and-Chance/pull/239).

This note is an independent reading of that head. The writer was bc-d103d7f2. This review does not push to that branch and does not merge it. The manuscript check for the 44 IDs is the source on `main`. After this review fetched, `origin/main` was `e9711ffe14d91bdef4eb4dace2bff7aa7ff1635d`. The only files between the pull request’s base `1e85f6ff` and that commit are two Volume 3 review notes. The Volume 4 manuscript is the same file on both.

## Issue log

| ID | Location | Problem | Required fix |
| --- | --- | --- | --- |
| V4-02 | `volume4-chance/chapters/ch06-clt.tex`, Lindeberg’s proof, the clip of the other blocks | The proof multiplies the clip of \(A\) by \(K\). It bounds \(\mathbb E|A-A^{(K)}|\) by a sum of terms \(\mathbb E[Q_j^2]/K\). The product of that bound with \(K\) is a sum of second moments, and the variances in the row already add to 1, so the written upper bound does not tend to 0. The sentence that sends \(m\to\infty\) and then \(K\to\infty\) does not reach \(\mathbb E[f'(A)X]=\mathbb E[f'(A)]\,\mathbb E[X]\). | In that product, use the tail \(\mathbb E[Q_j^2\mathbf 1_{\|Q_j\|>K}]\). For each fixed row the sum of those tails tends to 0. The factorization then holds before the remainder is sent to the Lindeberg limit. |
| V4-03 | `volume4-chance/chapters/ch05-continuous.tex`, Box–Muller, the display after \(U_{\mathrm{in}}\) | The argument covers the curved boundary of the rectangle and prices that cover. The comparison of \(P(E\cap\{\rho\le r\le T\})\) with the integral then charges every grid square outside \(U_{\mathrm{in}}\) to that cover. A grid square that meets the cutoff circle \(r=\rho\) or \(r=T\) is not on \(\partial E\). The displayed bound \(18e^{-1/2}\eta/(2\pi)\) plus the two tails does not include that layer. | Bound the one-mesh layer along \(r=\rho\) and \(r=T\). For fixed \(\rho\) and \(T\) that probability tends to 0 with \(\eta\). The limits already written then give the rectangle identity. |
| midpoint leads | `volume5-calculation/chapters/ch07-fft.tex`, leads of `pb:midpoint`, new in this head | The new sentence says that averaging a value with its two neighbours multiplies Fourier mode \(j\) by \(\cos(\pi j/n)\). The solution’s map is \((z_k+z_{k+1})/2\), and the writeup gives the multiplier \(e^{i\pi j/n}\cos(\pi j/n)\). | State that multiplier, or state the modulus \(\lvert\lambda_j\rvert=\lvert\cos(\pi j/n)\rvert\). Chapter 8 of Volume 4 does not contain this eigenvalue, so dropping that citation was the right deletion. |
| cone parenthesis | `volume12-random-motion/chapters/ch05-analysis.tex`, chapter opening, new in this head | The parenthesis is attached to Poincaré’s cone condition and names Volume 4, Proposition 8.7. Proposition 8.7 is the finite-graph hitting probability: boundary values 0 and 1, and the average of the neighbours off the boundary. It is not the cone condition. | Two sentences. The cone condition is proved in this chapter. The finite-graph hitting probabilities are Volume 4, Proposition 8.7. |
| Prop. 6.13 gloss | `volume11-randomness/chapters/ch12-permutations.tex`, the reminder. Not edited by this head. | The reminder says Proposition 6.13 writes a uniform permutation in canonical cycle notation, each cycle starting with its smallest element. Proposition 6.13 states that the number of cycles has the law of \(\sum B_k\) with independent \(P(B_k=1)=1/k\). The proof inserts \(n\) into a random slot of a permutation of \(n-1\). The canonical lengths are proved in this chapter, in the proposition that begins the broken-stick section. | Keep Proposition 6.13 for the Bernoulli sum. Point the canonical lengths at the proposition proved here. |

## The 44 IDs

The original findings are the issue log of `docs/review/volume4-independent-scored-read-2026-11-11.md`, the issue log of `docs/review/volume4-independent-scored-read-2-2026-11-11.md`, and V1-07 in `docs/review/volume1-independent-scored-read-2026-11-11.md`. Each row below was read against the current source, including the algebra, not only the sentence the pull request quotes.

| ID | On main | What the source does |
| --- | --- | --- |
| V4-01 | fixed | The product proposition proves the factorization for bounded factors that are uniformly continuous on every compact subinterval of \((0,1)\), by freezing the ends and passing to dyadic steps. Cosine and sine of a continuous quantile, including \(\Phi^{-1}\), are in that class. Gaussian vectors use the same product. |
| V4-02 | not closed | See the issue log. The clip, the dyadic steps, and the Lipschitz errors are written. The bound on the clip of \(A\) does not tend to 0. |
| V4-03 | not closed | See the issue log. The arc-length cover of the four sides is written, with the factor 9. The cutoff circles are not in that cover. |
| V4-04 | fixed | Exercise 6.2 is the confidence-interval exercise. The solution clips the square of the centred average of \(Y_i^2\) and takes the finite-bit limit from the product proposition. It does not call Volume 1’s weak law. |
| V4-05 | fixed | The preface and `kdp.md` both say that a later theorem is named and is not a step. Lévy’s continuity theorem and Itô’s formula are the examples in the listing. |
| V4-06 | fixed | On the tail, \(0\le Q^2-(Q^{(M)})^2=Q^2-M^2\le Q^2\). The same line is used again inside Lindeberg. |
| V4-07 | fixed | The tail beyond 1.9 standard deviations is printed `0.02872`, with no ellipsis. |
| V4-08 | fixed | \(G(0)=G(0)^2\), so \(G(0)\in\{0,1\}\). The law \(T=0\) is excluded. \(G(1/q)=e^{-\lambda/q}\) is written before continuity extends the formula. |
| V4-09 | fixed | The Chapter 3 bridge uses \(\{Z_n>0\}\). The symbol \(S_N\) in Chapter 2 is the partial sum of \(jr^j\), and it is defined there. |
| V4-10 | fixed | Chapter 14 and the Chapter 3 bridge say size \(O(\log n)\). |
| V4-11 | fixed | When \((1-\varepsilon)\log_2 n\) is an integer, the blocks are rerun at \(\varepsilon/2\), and the integer threshold sits inside the stricter event. |
| V4-12 | fixed | The countable case of Hoeffding cites the nonnegative double-sum principle of Volume 1, Chapter 10. |
| V4-13 | fixed | \(f(x)=\ln(1-x)+x+x^2\) has \(f(0)=0\) and \(f'(x)=x(1-2x)/(1-x)\ge 0\) on \([0,1/2]\). |
| V4-14 | fixed | Outer content is an infimum of countable covers. A chosen expansion never ends in all ones, because a remainder lies in \([0,1)\). |
| V4-15 | fixed | The host is Volume 1’s door experiment, now with \(n\ge 3\) doors. |
| V4-16 | fixed | There is a collected bibliography and an index of theorem numbers. The index entries checked by the citation test match the printed numbers. |
| V4-17 | fixed | The appendix says it is lettered B. The apology is gone. |
| V4-18 | fixed | \((\varphi(t)e^{t^2/2})'=0\) and \(\varphi(0)=1\) are written for the normal characteristic function. |
| V4-19 | fixed | Glivenko–Cantelli cites the Chapter 5 identity \(Q(u)\le x\) exactly when \(u\le F(x)\), and it says a flat stretch is allowed. |
| V4-20 | fixed | This build of the print PDF reports `flattened_pages: []`. No text page was replaced by one image. See the build table. |
| V4-21 | fixed | Right-continuity is the hypothesis that turns \(F(x)<u\) into \(Q(u)>x\). The two directions are written. |
| V4-22 | fixed | The ratio \(u_{2m}/u_{2m-2}\) includes the factor \(1/4\) from the powers of 2, and then equals \((2m-1)/(2m)\). |
| V4-23 | fixed | The maximum meets the first boundary vertex, which may be \(a\) or \(b\), and both values are 0. |
| V4R2-01 | fixed | A normal threshold of one coordinate is a pair of intervals in its uniform. The outer content is squeezed to the Gaussian tail by dyadic cylinders, and the convergent Borel–Cantelli half is proved from countable subadditivity. The text says Theorem 4.4 is not the step. A bin increment, which is a linear image, is priced by a rectangle cover of the same kind. |
| V4R2-02 | fixed | The empty-success bound cites finite additivity in Volume 1, Chapter 10, and then drops the overlap. |
| V4R2-03 | fixed | \(h_0=0\) gives \(A+B=0\). \(h_N=1\) gives \(B=1/((q/p)^N-1)\). |
| V4R2-04 | fixed | The cube integral in Pólya’s proof is taken one coordinate at a time, iterating the rectangle Fubini proposition. |
| V4R2-05 | fixed | Shannon’s 1948 paper is on the entropy chapter’s source list. It is not on the concentration chapter’s list. |
| V4R2-06 | fixed | The tools line of `pb:cyclewalk` is Volume 4, Chapter 2 (independence). The words “Chapter 8 (periodic chains)” are not in that file. |
| V4R2-07 | fixed | The colophon says the drawing has twelve rows and that Galton’s 1873 machine is a different object with more rows. |
| V4R2-08 | fixed | The index keeps the theorem numbers and adds `\ocindexpage`. This build had no undefined reference in `main.log`, so those page references resolve. The citation test checks each indexed label against the printed number. |
| V4R2-09 | fixed | `kdp.md` names the horse-kick counts as the Poisson law of rare events, and the process as the clock for arrivals. |
| V4R2-10 | fixed | Theorem 12.12 approximates the two half-line indicators by continuous test functions, estimates the strip, and identifies \(1-\Phi(a/\sqrt t)\) as the upper half-line of \(-B\). The constants in the odd-function cancellation match the density bound on an interval of length at least \(\delta\). |
| V4R2-11 | fixed | “Equivalently” is gone from the infinite van der Waerden sentence. The infinite form is “It follows that…”. |
| V4R2-12 | fixed | The complementary-pair non-uniqueness is restricted to \(k\ge 2\). At \(k=1\) the construction is the two stars. |
| V4R2-13 | fixed | The new edge’s endpoints lie on one face, and the edge is drawn inside that face. |
| V4R2-14 | fixed | The factor \((n+2)/(n+1)\) tends to 1, and the omitted interval’s contribution tends to 0 because \(g\) is bounded. |
| V4R2-15 | fixed | The deterministic bound in the restart proof is \(\beta\). |
| V4R2-16 | fixed | The opening points at the normal distribution of Chapter 5. |
| V4R2-17 | fixed | The sibling at maximum depth is a leaf, because an internal sibling would have a deeper child. |
| V4R2-18 | fixed | The exact return \(\binom{2m}{m}2^{-2m}\) is the count. The asymptotic is the local theorem. |
| V4R2-19 | fixed | The Gaussian integral cites Volume 1’s half-line and doubles it, because the integrand is even. |
| V4R2-20 | fixed | The meeting solution sets \(D_0=-2\), and the idea line starts at \(-2\). |
| V1-07 | fixed | The bibliography, the Chapter 5 source list, the chapter opening, and the density definition say “the integral as Volume 1 axiomatized it” and keep \(\int_0^\infty e^{-u^2}\,du=\sqrt\pi/2\). The one remaining “Riemann integrals” sentence is about changing a density at finitely many points. Commit `af918fdf` is an ancestor of `main` and of this head. Its subject is the #201 wording. |

Of the 44 IDs, 42 are fixed on main and 2 are not closed. None of the 44 is repaired by the diff in this head. That part of the pull request’s count is wrong in the two rows above, and right in the claim that the branch does not rewrite those proofs.

## Citations retargeted in this head

The numbers below were taken from the same counter the citation checker uses.

| Place | Cited statement | Does it state the fact? |
| --- | --- | --- |
| Volume 12, exit from an interval | Theorem 8.2 is the ruin probability. For a fair walk, \(h_k=k/N\). Starting at \(a\) on \(\{0,\ldots,a+b\}\) gives \(a/(a+b)\). Proposition 8.3 is the mean duration. The fair case is \(k(N-k)\), which is \(ab\). | Yes. The old sentence gave both facts to Theorem 8.2. |
| Volume 12, networks | The false sentence, that Proposition 8.4 applies to any Markov chain, is gone. Proposition 8.4 remains the simple walk’s visit count. The proof now says recurrence means \(P_a(\tau_a^+<\infty)=1\). | Yes. |
| Volume 12, analysis | Proposition 8.7 is the finite-graph hitting probability. | The number is the right theorem for that fact. The parenthesis still hangs it on the cone condition. See the issue log. |
| Volume 15, random-to-top | Proposition 9.11 chooses two cards at a step. Its untouched probability carries the exponent \(2t\). The one-card covariance \((1-2/n)^t-(1-1/n)^{2t}\) is computed in the solution, from \((1-2/n)\le(1-1/n)^2\). | Yes. |
| Volume 11, fixed points | The proof of Proposition 2.3 writes \(P(F_n=m)=\frac1{m!}\cdot D_{n-m}/(n-m)!\). Volume 1, Chapter 2, writes the alternating sum. | Yes. |
| Volume 11, variance tools | Chapter 2 states \(\operatorname{Var}(X+Y)=\operatorname{Var} X+\operatorname{Var} Y+2\operatorname{Cov}(X,Y)\) and says the covariance of independent variables is zero. | Yes. Chapter 5 was the wrong chapter. |
| Volume 11, independence reminder | Chapter 4 states the product formula for a finite collection of events, in the Borel–Cantelli argument. The density formula is Volume 4, Theorem 6.8. | Yes. |
| Volume 11, planar returns | The proof of Theorem 8.5 splits a planar step into two independent one-dimensional walks. The proof of Theorem 8.6 says the steps after a fixed even time are a fresh copy. The solution uses that factorization at fixed times. | Yes. |
| Volume 5, midpoint leads | The Volume 4, Chapter 8 citation for diffusion on the circle is gone. | The replacement sentence misstates the multiplier computed in the same solution. See the issue log. |

A scan of the numbered Volume 4 pointers in Volumes 5–15, 252 citations, matched the statements that were opened, with the two exceptions in the issue log. One of those is new in this head. The other, the canonical-notation gloss on Proposition 6.13, was already on main. The new subject checker rejects the collisions this head repaired. It does not read the canonical-notation sentence, because that sentence does not use the phrases the checker lists.

The checker’s index test was run with the suite. The labels it pins, from the ballot theorem through Weierstrass, match the printed numbers. `def:charfn` is present in `ch06-clt.tex`.

## The Volume 1 status line

The diff changes two sentences in the final-status section of the Volume 1 scored read. It does not change the original finding. That finding still says the bibliography credited Volume 1 with the Riemann integral, and it still asks for the wording “the integral as Volume 1 axiomatized it.”

The status section already said it was a ledger of the repairs after the read, not the manuscript at `8b8a5be`. The new sentence says V1-07 was deferred at the apply and is fixed on main by #201. The table row names #201 and `af918fdf`. The count goes from 33 fixed and one deferred to 34 fixed. V1-31 remains the one row marked not fixed, so 34 fixed and 1 not fixed is still 35. The deferral is still in the sentence. This is a ledger update. It is not a rewrite of the finding.

## House voice

The new sentences in the fixed-point solution, the exit-time solution, the random-to-top solution, and the planar-return solution are short and name the object. They do not use the filler the style sheet bans. “Carries the exponent \(2t\)” is compressed, and a reader can check it against Proposition 9.11.

The cone-condition parenthesis does not teach the distinction it is there to make. The midpoint leads sentence is plain English and states the wrong multiplier. Both are in the issue log.

## Tests and builds

Run on this head, in a worktree at `123f44e43fc3f06817aa81461d5dbe8e7d24e4d9`.

`python3 -m unittest test_cross_volume_citations.py`, from `tools/`, ran 16 tests and exited 0. The run took 2.342 seconds.

`python3 tools/cross_volume_citations.py` printed `Cross-volume citations match 4851 numbered statements.`

`python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1177, "pending": 19}` and exited 0.

`./build.sh --pdf-only` for the five volumes. Each layout check reported no overflow and no unresolved references. Each `main.log` has no line matching `Overfull` and no line matching `undefined references`. The print file is the KDP PDF. Page size 513 × 738 pt is 7.125 × 10.25 in.

| Volume | Print pages | `flattened_pages` | XeLaTeX `Output written` |
| --- | --- | --- | --- |
| 4 Chance | 327 | `[]` | 327 pages |
| 5 Calculation | 417 | `[108]` | 417 pages |
| 11 Randomness | 279 | `[157, 178]` | 279 pages |
| 12 Random Motion | 233 | `[60]` | 233 pages |
| 15 Order and Chance | 253 | `[]` | 253 pages |

The page counts agree with the table in the pull request. Volume 4’s empty flatten list is the check for V4-20. The other nonempty lists are pages the exporter marked as transparent and flattened at 600 ppi. They are not a Volume 4 scored-read row.

## CI on this head

`list_check_runs_for_ref` on `123f44e43fc3f06817aa81461d5dbe8e7d24e4d9` returned `total_count` 20, all with that SHA: 19 conclusions `success` and 1 `skipped`. The skipped check is `publish`. The success checks are `list`, `debs`, `volume4-native`, the fifteen `build (volume…)` jobs, and `site`.

The workflow run for Volume 4 native production QA is `43501380206`, conclusion `success`. The Build books run is `43501380120`, conclusion `success`.

## What closes this review

Repair the Lindeberg product so the written bound tends to 0, add the annulus layer in Box–Muller, correct the midpoint multiplier, split the cone-condition parenthesis from Proposition 8.7, and retarget the canonical-notation sentence. The other 42 IDs, the other retargeted citations, the Volume 1 ledger line, the tests, the five builds, and the CI record on this head do not need another change for this review.

## Recheck at `f96b2a64`

**Verdict: APPROVE**

**Head reviewed:** `f96b2a64f461ef853dbd3bed566065df91819cb3` on `cursor/v4-scored-read-final-b140`, pull request [#239](https://github.com/OussamaSegh/Order-and-Chance/pull/239).

This note is a second reading of that head, after the repairs named above. The manuscript branch was not edited. The range `123f44e4..f96b2a64` is two commits: `b048bdff` rewrites the two bounds, and `f96b2a64` records the Chapter 5 and Chapter 6 source pins. The diff is 8 files, 41 insertions and 12 deletions.

## Issue log

| ID | Location | Result |
| --- | --- | --- |
| V4-02 | `volume4-chance/chapters/ch06-clt.tex`, Lindeberg, the clip of the other blocks, lines 452–479 | Closed. The product with the clipped factor is a sum of tails `E[Q_j^2 1_{|Q_j|>K}]`, and the square is factored so the error is a constant times `(1/K)` times that sum. Both tend to 0 with the row held fixed. |
| V4-03 | `volume4-chance/chapters/ch05-continuous.tex`, Box–Muller, lines 363–371 | Closed. Grid squares on `r=ρ` and `r=T` are charged to strips of width `h`. The two strips have probability at most `η`, and the rectangle comparison carries `2η` for that layer. |
| midpoint leads | `volume5-calculation/chapters/ch07-fft.tex`, leads of `pb:midpoint`, line 530 | Closed. The multiplier is `e^{iπ j/n} cos(π j/n)`, and the modulus is `|cos(π j/n)|`. |
| cone parenthesis | `volume12-random-motion/chapters/ch05-analysis.tex`, chapter opening, line 24 | Closed. The cone condition is proved in this chapter. Proposition 8.7 is named on its own for the finite-graph hitting probabilities. |
| Prop. 6.13 gloss | `volume11-randomness/chapters/ch12-permutations.tex`, the reminder, lines 18–19 | Closed. Proposition 6.13 is the Bernoulli sum for the number of cycles. The canonical lengths point at `prop:firstcycle`. |

No row stays open.

### V4-02

The clip comparison `|Q-Q^{(K)}| ≤ Q^2/K` on `{|Q|>K}` is the one already proved for Proposition `prop:indepproduct`. For a fixed row only finitely many other blocks appear, so

`E|A-A^{(K)}| ≤ Σ_j (1/K) E[Q_j^2 1_{|Q_j|>K}]`.

`Q^{(K)}` is at most `K` in absolute value, and `H` is Lipschitz with a constant `L` taken from the bounded second and third derivatives. The product of those two bounds cancels `K`:

`|E[(H(A)-H(A^{(K)})) Q^{(K)}]| ≤ L Σ_j E[Q_j^2 1_{|Q_j|>K}]`.

Each `Q_j` is a centred quantile, hence monotone, so `{|Q_j|>K}` is a union of at most two tails of `(0,1)`. The integral of the integrable function `Q_j^2` over those tails tends to 0, by the same comparison the proof already used for the single block `Q`. A finite sum of those tails tends to 0. The dyadic step still has a factor `K` in front of `E|H(A^{(K)})-H_m|`, and that term tends to 0 as `m→∞` with `K` held fixed.

The square cannot keep a factor `K^2` in front of `E|A-A^{(K)}|`, because that product is `K` times a sum of tails and the tails have no rate. The proof splits `|Q_j-Q_j^{(K)}|` into `(Q_j-K)` on `{Q_j>K}` and `(-Q_j-K)` on `{Q_j<-K}`. Each piece is monotone. Clipping a piece at height `M` makes it bounded, and Proposition `prop:indepproduct` factors a bounded monotone function of one block against a bounded monotone function of another. The square `(Q^{(K)})^2` is the sum of the squares of its nonnegative and nonpositive parts. That splitting is in the proof of the product proposition, and each square is bounded and monotone. Linearity gives the product with the whole square.

On `{piece > M}` one has `|Q_j-Q_j^{(K)}| ≤ Q_j^2/K`, and `(Q^{(K)})^2 ≤ K^2`, so the missing product is at most `K` times the integral of `Q_j^2` over `{Q_j^2 > KM}`. That integral tends to 0 as `M→∞` with `K` fixed, because `Q_j^2` is integrable. Sending `M→∞` factors

`E[|Q_j-Q_j^{(K)}| (Q^{(K)})^2] = E|Q_j-Q_j^{(K)}| E[(Q^{(K)})^2] ≤ (1/K) E[Q_j^2 1_{|Q_j|>K}] E[Q^2]`.

`(Q^{(K)})^2 ≤ Q^2` pointwise, and `E[Q^2]` is a variance in the row, hence finite. Sum on `j` and multiply by `L`. The error is a constant times `(1/K)` times a sum of tails. It tends to 0 as `K→∞`. The dyadic step for the square uses `K^2` in place of `K`, which still tends to 0 for each fixed `K`.

The collection sentence names the sum of tails. The display two paragraphs earlier carries the fixed Lipschitz factor `L`. Either way the bound tends to 0 before the remainder is sent to the Lindeberg limit. The theorem statement is unchanged. The argument uses the product proposition, the monotone tail comparison, and the Lipschitz bound from the mean value theorem. It does not use a later theorem, and the source pins are identity hashes, not the proof.

### V4-03

The arc-length cover of the four sides is unchanged: probability at most `9 e^{-1/2} η/(2π)`, and it contains every grid square that meets `∂E` inside the annulus. The new sentences say that a grid square on `r=ρ` or `r=T` need not meet `∂E`.

The grid side is `h=L/n`. After shrinking `h` so that `e^{-1/2} h ≤ η/2`, a grid square that meets `r=ρ` and the annulus meets the annulus only inside `ρ ≤ r ≤ ρ+h`. The outer circle gives `T-h ≤ r ≤ T`. Each strip has area `2π h`. The product density is at most `e^{-1/2}/(2π)`, the bound already proved from the maximum of `r e^{-r^2/2}`. Each strip therefore has probability at most `e^{-1/2} h ≤ η/2`. For fixed `ρ` and `T` the two strips together have probability at most `η`.

Inside the annulus, both the probability of `E` and the integral of the product density differ from the value on `U_in` by at most the side cover plus the two strips. They differ from each other by at most twice that, which is `18 e^{-1/2} η/(2π) + 2η`. Adding `P(R>T)=e^{-T^2/2}` and `P(R<ρ)≤ρ^2/2` gives the displayed bound. Send `η↓0` with `ρ` and `T` fixed, then `ρ↓0` and `T→∞`. The rectangle identity follows. The polar cutoff of the indicator, and the bound `φ ≤ 1/√(2π)`, are the ones already in the proof.

### Midpoint leads

The solution's map is `(z_k+z_{k+1})/2`. On the mode `ω^{jk}` the multiplier is `(1+ω^j)/2`. With `ω=e^{2π i/n}`,

`(1+e^{2π i j/n})/2 = e^{iπ j/n} cos(π j/n)`.

The leads state that factor, and they state that its modulus is `|cos(π j/n)|`. After `t` steps the slowest non-constant modes, `j=1` and `j=n-1`, have been multiplied by a complex number of modulus `cos^t(π/n)`. The solution computes the same eigenvalue. Volume 4, Chapter 8, is no longer cited for it.

### Cone condition and Proposition 8.7

The opening is two sentences. The cone condition is Theorem `thm:cone` in this chapter: an exterior cone makes the boundary point regular. Proposition 8.7 is `prop:harmonic`, the unique function on a finite connected graph with boundary values 0 and 1 that equals the average of its neighbours off `{a,b}`. The parenthesis that hung that proposition on the cone condition is gone.

### Proposition 6.13

Proposition 6.13, `prop:cyclebern`, states that the number of cycles has the law of `Σ B_k` with independent `P(B_k=1)=1/k`. The proof builds the sum by inserting `n` into a uniform slot. The reminder now says that. The lengths in the order used in this chapter, first the cycle through 1 and then the cycle through the smallest remaining element, are Proposition `prop:firstcycle`: `P(L_1=k)=1/n`, and the product formula for the first `r` lengths. The canonical-notation sentence no longer gives that job to Proposition 6.13.

## The diff

`git diff 123f44e4..f96b2a64` touches the three chapter sentences above, the two proofs, and three test files. A search of the added and deleted TeX lines found no `\label`, no `\caption`, no `\fig`, no TikZ, no font-size command, and no new theorem, proposition, lemma, corollary, or exercise environment. The numbered statements did not move. `git hash-object` of the two chapter files is `73617646dcb3dbad985ce9df7b4a4536fae28aad` for Chapter 5 and `41197f55044d2d813d364c0a2cfcae7750763ab6` for Chapter 6, which are the pins in the source-identity tests. Those pins record the bytes. They are not the proofs.

The Lindeberg and Box–Muller statements are the same theorems. The new bounds are the ones that tend to 0. Nothing in the range weakens a hypothesis or drops a case from a statement.

## Citations the pull request changes

The numbers are the ones `tools/cross_volume_citations.py` assigns. Each changed sentence was read against that statement.

| Place | Cited statement | Does it state the fact? |
| --- | --- | --- |
| Volume 11, independence reminder | Chapter 4, in the Borel–Cantelli argument: mutual independence means that every finite subcollection has probability equal to the product of the probabilities. | Yes. The density formula in the same reminder is Theorem 6.8(b). |
| Volume 11, variance tools | Chapter 2 states `Var(X+Y)=Var X+Var Y+2 Cov(X,Y)`, and says the covariance of independent variables is zero. | Yes. |
| Volume 11, fixed points | The proof of Proposition 2.3 writes `P(F_n=m)=(1/m!) D_{n-m}/(n-m)!`. Volume 1, Proposition 2.3, is the derangement count, and the chapter writes `D_r/r! = Σ_{j=0}^r (-1)^j/j!`. | Yes. |
| Volume 11, planar returns | The proof of Theorem 8.5, Pólya, splits a planar step into two independent one-dimensional walks. The proof of Theorem 8.6, the last-visit law, says the steps after time `2k` are a fresh block of fair bits. The solution uses that factorization at fixed times. | Yes. The gloss names the step in the proof. |
| Volume 11, cycle reminder | Proposition 6.13 is the Bernoulli sum. `prop:firstcycle` is the length law. | Yes. See the issue log. |
| Volume 12, exit from an interval | Theorem 8.2 gives `h_k=k/N` for a fair walk, so the exit probability from `a` on `{0,…,a+b}` is `a/(a+b)`. Proposition 8.3 gives mean duration `k(N-k)`, which is `ab`. | Yes. |
| Volume 12, networks | The sentence that gave Proposition 8.4's proof to every Markov chain is gone. Proposition 8.4 remains the expected number of visits of the simple walk. The proof now says recurrence means `P_a(τ_a^+<∞)=1`, which is the escape probability the theorem computes. | Yes. |
| Volume 12, analysis | Proposition 8.7 is the finite-graph hitting probability. The cone condition is Theorem `thm:cone` in Volume 12, Chapter 5. | Yes. See the issue log. |
| Volume 15, random-to-top | The solution computes the one-card covariance from `(1-2/n) ≤ (1-1/n)^2`. Proposition 9.11 is the random-transposition count: two cards at a step, mean `n(1-1/n)^{2t}`, and the same comparison with exponent `2t`. | Yes. |
| Volume 5, midpoint leads | The multiplier is the eigenvalue in the same solution. | Yes. See the issue log. |

## House voice

The new sentences name the object and the bound. "The factor `K` has cancelled, and the bound is a sum of tails." "A grid square that meets the circle `r=ρ` or the circle `r=T` need not meet `∂E`." "The cone condition is proved in this chapter." "The midpoint map sends `z_k` to `(z_k+z_{k+1})/2`." None of them uses the filler the style sheet bans, and none announces a section instead of teaching the step.

## Tests and the Volume 4 build

Run on `f96b2a64f461ef853dbd3bed566065df91819cb3`.

`python3 -m unittest test_cross_volume_citations.py`, from `tools/`, ran 16 tests and exited 0. Together with the two Chapter 5 and Chapter 6 source-pin modules, the same command ran 22 tests and exited 0.

`python3 tools/cross_volume_citations.py` printed `Cross-volume citations match 4851 numbered statements.`

`python3 review/volume3-internal/registers.py` printed `{"accepted-internal": 1177, "pending": 19}` and exited 0.

`./build.sh --pdf-only volume4-chance` exited 0. The layout check reported 285 whole boxes, maximum height 465.0 pt, no overflow and no unresolved references. `main.log` has 0 lines containing `Overfull` and 0 lines containing `undefined`. XeLaTeX wrote 327 pages. The print file is `dist/kdp/Volume 4 - Chance - Print.pdf`: 327 pages, page size 513 × 738 pt, PDF 1.3. The preflight report has `"flattened_pages": []`.

## CI on this head

`list_check_runs_for_ref` on `f96b2a64f461ef853dbd3bed566065df91819cb3` returned `total_count` 20, every run with that SHA: 19 conclusions `success` and 1 `skipped`. The skipped check is `publish`. The success checks are `list`, `debs`, `volume4-native`, the fifteen `build (volume…)` jobs, and `site`.

The Build books run is `43516797594`, conclusion `success`. Its 19 jobs are on the same SHA: 18 `success` and `publish` `skipped`. The Volume 4 native production QA run is `43516797555`, conclusion `success`. Its one job, `volume4-native`, is `success` on the same SHA, including the step that builds the reading PDF, the print PDF, and the EPUB.

## What this recheck closes

The five repairs hold, the diff does not move a number or a diagram, the changed citations name the statements they use, and the Volume 4 build and the CI record on this head are clean. Nothing in this recheck asks for another change.
