# Volume 4 Phase 3 — cross-volume dependency audit

**Date:** 10 November 2026.  
**Reviewer:** the designated validator (an AI reviewer). Not an external referee.  
**Baseline:** `main` `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f`.  
**Scope that was actually checked:** the 18 repairs from PR #136, Volumes 1–3 against the parent of that PR, Volume 4's named citations of Volumes 1–6, and Volume 4 citations inside Volumes 5 and 6 plus one further phantom number found in Volume 11 while confirming DEP-29. This is not a proof-by-proof reading of Volumes 5–15.

## Tests and the 18 repairs

```text
python3 -m unittest tools.test_volume4_phase2_downstream_source_truth
Ran 12 tests — OK

python3 -m unittest tools.test_volume4_phase2_downstream_references
Ran 3 tests — OK
```

DEP-12 through DEP-29 are still present in the repaired sentences. None of the pinned bad strings has returned. The repaired chapter files are unchanged between `070b9e00a5afadbe3d4153339cfd99cd72329d24` and this baseline.

Printed numbers those repairs rely on still match the Volume 4 counters (theorem, proposition, lemma, corollary, definition and example share one counter; exercises have their own):

| Cited as | What it is |
| --- | --- |
| Theorem 4.2 | Hoeffding (`thm:hoeffding`) |
| Theorem 4.3 | Kolmogorov |
| Theorem 4.4 | Borel–Cantelli |
| Theorem 4.6 | Weierstrass via Bernstein |
| Theorem 6.10 | Lindeberg |
| Definition 11.1 | conditional expectation on a finite partition |
| Theorem 11.4 | bounded optional stopping |
| Theorem 11.5 | further sufficient conditions (case of bounded steps and finite mean time) |
| Theorem 11.10 | Azuma |
| Theorem 11.12 | \(L^2\) convergence on finite interval partitions |
| Theorem 11.13 | Pólya's urn, uniform limit on \([0,1]\) |
| Theorem 2.1 | Poisson limit of binomial laws |
| Exercise 1.1 | the one-person birthday bound |

There is no Theorem 2.11, 4.7, 4.14, 10.21 or 10.25.

## Volumes 1–3

```text
git diff --exit-code 1778324959ba8e7d027cd5384d9ccdc9065fec20 HEAD -- \
  volume1-first-principles volume2-integers volume3-symmetry
```

The diff is empty on this baseline (HEAD at audit time was `2655cf5a`). PR #136 did not edit those trees. No edit to Volumes 1–3 is proposed.

Two published Volume 3 sentences point at “Volume 4, Chapter 8” for coupling and for matrix powers of finite Markov chains. Both topics are in Chapter 9. The sentences present them as later applications, not as premises. **No change is proposed.** Volumes 1–3 stay frozen.

Volume 4 cites Volumes 2 and 3 only as books in the preface. It cites no numbered theorem of Volumes 2–6. Named Volume 1 tools used in Volume 4 proofs (the Poisson series in Volume 1, the logarithm derivative, Bolzano–Weierstrass, the integral test, Cauchy–Schwarz, Stirling, the Gaussian integral) are still in the cited Volume 1 chapters. Later volumes are named as previews (Lévy continuity in Volume 11, general Tonelli in Volume 7, the stochastic integral in Volume 12) and those passages say they are not steps in the Volume 4 proof.

## Critical defects outside Volume 4

These are proposals. They must not be merged by this phase without the author's review, and they do not edit Volumes 1–3.

### 1. Volume 6 — phantom Theorem 2.11

`volume6-crossroads/chapters/ch10-random.tex`, solution of `ex:modelpoisson` (and the idea line): “Volume 4 proved it for equal probabilities (Theorem 2.11)”.

Volume 4, Theorem 2.1 is the Poisson limit of binomial laws: one success probability \(p_n\) with \(np_n\to\lambda\). Chapter 2 has eight numbered results and stops at 2.8. The Volume 6 calculation then treats unequal probabilities itself, so the pointer should be Theorem 2.1.

### 2. Volume 6 — a Chernoff bound Volume 4 does not prove

Same file, hint and solution of `ex:shortmodel`. The exercise assumes \(\lambda>2\). The solution claims

\[
P(|S_N-\mu_N|\ge\delta\mu_N)\le 2e^{-\delta^2\mu_N/3}
\]

“by Chernoff's bounds (Volume 4, Chapter 4)”.

Chapter 4 proves Hoeffding's inequality, Theorem 4.2: for independent variables in \([a_i,b_i]\),

\[
P(S-\mathbb ES\ge t)\le\exp\Bigl(-\frac{2t^2}{\sum(b_i-a_i)^2}\Bigr),
\]

and the same bound for the lower tail. The only Chernoff exercise, `ex:chernoffbin`, is the binomial relative-entropy bound for identical trials. It is not the factor \(1/3\), and it does not cover unequal rare indicators.

The window in the exercise is a finite product of \(\{0,1\}\) variables, so Theorem 4.2 applies on that product. With \(t=\delta\mu_N\) and \(h_N\) summands,

\[
P(|S_N-\mu_N|\ge\delta\mu_N)\le 2\exp(-2\delta^2\mu_N^2/h_N).
\]

For \(\lambda>2\), \(\mu_N^2/h_N\) grows faster than \(\log N\), so the probability is eventually at most \(2/N^2\). Borel–Cantelli still closes the argument. The factor \(1/3\) is not required. A proposal should replace the hint and the solution with this Hoeffding estimate and should not invent a multiplicative Chernoff theorem in Volume 4.

### 3. Volume 5 — monotone convergence is not in Volume 4, Chapter 5

`volume5-calculation/chapters/ch03-series.tex`, solution of `ex:ritelli`: term-by-term integration of \(\sum (-\ln x)\,x^{2n}\) on \((0,1)\) is credited to “monotone convergence (Volume 4, Chapter 5)”.

Chapter 5's limit theorem is Theorem 5.9, dominated convergence for functions continuous on \(\mathbb R\), uniformly convergent on bounded intervals, with a continuous integrable dominant. The sum \((-\ln x)/(1-x^2)\) does not extend to a continuous function at \(0\). The citation is false.

A local repair, which does not need a new theorem: the partial sums \(s_N\) integrate term by term by the already-stated integration by parts; their limit is the integrand whose integral was computed in closed form as \(\pi^2/8\); the tails of that improper integral are small, and on a compact subinterval of \((0,1)\) the geometric remainder is uniformly small. That identifies \(\sum 1/(2n+1)^2=\pi^2/8\).

### 4. Volume 11 — phantom Theorem 10.21

`volume11-randomness/chapters/ch09-martingales.tex`, example `ex:polyadf`: “as Volume 4 (Theorem 10.21) proved directly” that the Pólya limit is uniform.

DEP-29 corrected the same phantom number in `ch01-zero-one.tex` only. This sentence remains. The uniform limit is Volume 4, Theorem 11.13 (`thm:polyaurn`). The surrounding de Finetti uniqueness argument is about that fact. The proposal is the number 11.13, not a new proof.

Volume 11's example starts the urn with one red and one green ball. Volume 4 starts with one red and one blue ball. The mathematics is the same two-colour urn. The colour names are a wording mismatch, not a false theorem. They can stay unless the author wants them aligned.

## Non-blocking citation nits

Recorded, not patched in the first proposals:

| Where | What is off |
| --- | --- |
| `volume6-crossroads/chapters/ch09-erdoskac.tex` | Gaussian moments \((k-1)!!\) are attributed to “Volume 4” with no number. Volume 4 prints \(\mathbb E[Z^2]=1\) and \(\mathbb E[Z^4]=3\), not the general formula. A nearby appeal to the Gaussian transform is cited correctly. |
| `volume6-crossroads/chapters/ch05-pnt.tex` | A tools note says “Volume 4, Chapter 2 (Cauchy–Schwarz)”. The inequality used is Volume 1, Chapter 9. |
| `volume5-calculation/chapters/ch04-integrals.tex` | Tools say “Volume 4, Chapters 2 and 9 (Poisson variables)”. The Poisson clock is Chapter 10. |
| `volume5-calculation/chapters/ch12-agm.tex` | Tools say “Chapter 8 (periodic chains)”. Periodicity of a chain is Chapter 9. |
| `volume5-calculation/chapters/ch07-fft.tex` | A lead sentence gives “the spectral gap of a graph, and of diffusion on the circle” to Volume 4, Chapter 8. Those phrases are not in Volume 4. The proof does not use the sentence. The tools note on total variation correctly points at Chapter 9. |

## What was not checked

Proofs in Volumes 5–15 were not all read. Volumes 7–10 and 12–15 were not searched again for new Volume 4 citations beyond the 18 repaired passages and the Theorem 10.21 sentence above. `volume4-chance/chapters/gilmer.tex` is not included by `main.tex`.
