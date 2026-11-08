# Volume 4 line review, 8 November 2026

Writer self-check of the chapters named in the request. Not an independent second review.

## Theorem 11.14

The previous write-up claimed that a late oscillation of the truncated variables sits inside a late upcrossing of one band of height ε. That containment is false: a path that tends to infinity stops upcrossing any fixed band, while the truncation settles. The repaired proof uses only the unit-interval model.

- Doob's inequality for `|X|` bounds the maximum. The events are finite unions of interval atoms, so the outer content of the increasing union is the limit of the probabilities, by the length comparison already written for open sets in Proposition 6.2.
- Upcrossings of every rational band are almost surely finite, so the limit exists in the extended reals, and the maximum bound forces it to be finite.
- The truncated variables `min(|X_n|, M)` are bounded step functions. Their tail oscillation sets are countable unions of intervals. The decreasing-content argument in the proof of Proposition 6.2 makes the expectations Cauchy. The limit of those expectations is at most `sup E|X_n|`. Sending the truncation level to infinity defines the expectation of the limit.

The statement is restricted to finite interval partitions of the unit interval. Volume 11's uniformly integrable martingale theorem is not this statement. Its almost-sure step is now the upcrossing inequality of Theorem 11.6, transferred by Volume 7's conditional expectation, plus Fatou's lemma from Volume 7. The conclusion in Volume 11 is unchanged.

## Chapters read for defects

Chapters 1, 4, 5 (including the chord and needle section), 7, and 13: the checked identities, hypotheses, solutions, and captions held.

Repairs made:

- Chapter 2, the birthday waiting time. The exercise cited `∫ e^{-x^2/2} = √(π/2)` as a Volume 1 result. Volume 1 proves `∫_0^∞ e^{-x^2} dx = √π/2`. The exercise and its solution now make the substitution `x = u/√2`.
- Chapter 3, the subcritical second proof. It passed a limit through `{S_N > k}` on the space of trees. The generation means already give `P(Z_n > 0) ≤ m^n → 0`.
- Chapter 10, the joint density of arrival times. A compactly supported test function extends by zero to a cube on which Fubini applies. The exponential tail was not an estimate.
- Chapter 10, finiteness of `N(t)`. Theorem 6.10 asks for a distribution function strictly increasing on the whole line. The exponential law is not that case. The Poisson probabilities in Theorem 10.4 sum to 1, which is the finiteness.
- Chapter 10, the geometric mean. The factor `∑ k ρ^k` is computed by `t − ρt = ρ/(1−ρ)`, not by differentiating a power series.
- Chapter 14, the opening line. `O(log n)` is now explicitly with high probability, matching Theorem 14.1.
- Chapter 14, `binom(n,k) ≤ (en/k)^k`. Derived from `e^k ≥ k^k/k!`.

Lemma 10.5 is the colouring lemma later volumes cite. Exercise 13.4 is the crossing bound `m^3/(64n^2)` for `m ≥ 4n`.

## Citations retargeted in this pass

These are the only edits outside Volume 4 in this pass. Each one names the statement that was proved.

- Volume 11, martingales reminder: stopped mean is Theorem 11.4; Ville's bound and the square maximal inequality are Theorem 11.9; finite-partition almost-sure convergence is Theorem 11.14; upcrossings are Theorem 11.6 with the bound `(b−a)E[U_n] ≤ E[(a−X_n)_+]`.
- Volume 11, uniformly integrable martingales: the general almost-sure step is written from that upcrossing bound and Volume 7's Fatou lemma, not from Theorem 11.14.
- Volume 11, Lévy's downward theorem: the upcrossing citation is Theorem 11.6. The reversed sequence ends at `M_0`, and `(a−M_0)_+ = (M_0−a)^-`, which is the form used there.
- Volume 11, Kakutani: the square maximal inequality is Theorem 11.9. `N_n` is a nonnegative martingale with `E[N_n^2] ≤ c^{-2}`, so the bound `E[sup N_n^2] ≤ 4/c^2` is the one in that theorem. The stopped-sum proof uses only the conditional-expectation inequality.

Volumes 1–3 source files are identical to `main`. The only shared-file difference from `main` is the Volume 4 sentence in `common/cover-notes.json`, from the earlier fourteen-chapter restructure on this branch. It was not edited in this pass, and the cover was not regenerated.
