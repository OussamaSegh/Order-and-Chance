# Volume 14 — The Primes

*Their Hidden Rhythm.*

**Status of this file.** Blueprint of Volume 14 under the [master plan](MASTER-PLAN-V5-V15.md), 2026-11-10. It replaces the earlier specification. Chapter numbers below are the numbers after decision D-11 is applied. No proof named here has been verified.

**Series part.** V. Number. **Directory.** `volume14-primes`.

## Central question

How regular are the primes up close? Volume 6 heard them from far away. This volume listens in short intervals, in progressions, in sums and in gaps, and says exactly where each method stops.

## Prerequisites

| From | What is used |
| --- | --- |
| Volume 6 | All of it. In particular the zero-free region, the explicit formula, Selberg's sieve, Brun–Titchmarsh, the large sieve inequality, Weyl differencing, Pólya–Vinogradov |
| Volume 5 | Residues, Euler–Maclaurin, the functional equation, Poisson summation |
| Volumes 7–8 | Integrable Fourier inversion and Plancherel; finite Fourier analysis and Meshulam's bound; Mellin inversion |
| Volume 13 | The functional equation of \(L(s,\chi)\); the class number formula; quadratic fields |
| Volume 11 | One probabilistic inequality in Chapter 4; the ergodic proof of Roth's theorem, for comparison only |
| Volume 12 | The sine kernel, for comparison only in Chapter 14 |

## Structure

| Ch. | Title | File | Action |
| --- | --- | --- | --- |
| | **Part I. Zeros and Sieves** | | |
| 1 | Zeros and Primes in Short Intervals | `ch01-zeros.tex` | Keep |
| 2 | Siegel's Theorem | `ch02-siegel.tex` | Keep |
| 3 | Sieves and the Parity Problem | `ch03-sieves.tex` | Keep |
| 4 | The Large Sieve and Bombieri–Vinogradov | `ch04-largesieve.tex` | Keep |
| 5 | Exponential Sums over Primes | `ch05-expsums.tex` | Keep |
| | **Part II. Additive Problems and Bounded Gaps** | | |
| 6 | Waring's Problem | `waring.tex` | Arrives from Volume 5. Completed (D-11) |
| 7 | Three Primes | `three-primes.tex` | Keep |
| 8 | Small Gaps between Primes | `ch08-gpy.tex` | Keep |
| 9 | Bounded Gaps between Primes | `ch09-maynard.tex` | Restructure one theorem (D-27) |
| | **Part III. Structure in the Primes** | | |
| 10 | Multiplicative Functions | `ch10-halasz.tex` | Keep |
| 11 | Additive Combinatorics | `ch11-additive.tex` | Keep |
| 12 | Roth's Theorem | `ch12-roth.tex` | Keep |
| 13 | Gowers Norms and the Green–Tao Theorem | `ch13-gowers.tex` | Keep |
| 14 | The Critical Line | `ch14-critical.tex` | Keep |

**Why Waring is here.** Part II is the circle method. Waring's problem is its cleanest case: Weyl sums on the minor arcs, a singular series and a singular integral on the major arcs, with no primes to complicate either. Chapter 7 then repeats the method with primes, where the minor arcs need Vinogradov's estimate from Chapter 5 and the major arcs need Siegel–Walfisz from Chapter 2. The part's name already covers it.

## Flagship theorems, proved in this volume

| Theorem | Label | Chapter |
| --- | --- | --- |
| Ingham's mean value; Carlson's zero-density estimate; primes in intervals \([x,x+x^\theta]\) for \(\theta>\tfrac34\) | `thm:carlson`, `cor:hoheisel` | 1 |
| Landau–Page; Siegel's theorem; Siegel–Walfisz; the class number bound | `thm:siegel`, `cor:sw`, `thm:classnumber` | 2 |
| The fundamental lemma of sieve theory; Selberg's parity example; Hooley's conditional theorem on Artin's conjecture | `thm:fl`, `thm:parity`, `thm:hooley` | 3 |
| The multiplicative large sieve; Vaughan's identity; Bombieri–Vinogradov; Barban–Davenport–Halberstam; Linnik's theorem on small non-residues | `lem:vaughan`, `thm:mainest`, `thm:bv`, `thm:bdh`, `thm:linnik` | 4 |
| Vinogradov's estimate for exponential sums over primes; Kloosterman and Salié sums | `thm:vinogradov3` | 5 |
| Weyl's inequality for \(k\)th powers; Hua's lemma; the asymptotic formula in Waring's problem for \(s\ge2^k+1\); positivity of the singular series | `thm:weylk`, `thm:hua`, `thm:waring`, `thm:singpos` | 6 |
| Every large odd integer is a sum of three primes | `thm:threeprimes`, `cor:threeprimes` | 7 |
| The Goldston–Pintz–Yıldırım theorem, conditional on a level of distribution beyond \(\tfrac12\) | | 8 |
| Maynard's sieve; \(M_k>\log k-2\log\log k-2\) for large \(k\); \(\liminf(p_{n+m}-p_n)<\infty\) for every \(m\) with an explicit bound in \(m\); an explicit bounded gap | `prop:mklower`, `thm:maynard`, `cor:mprimes`, new | 9 |
| Halász's theorem; Delange; Wirsing | | 10 |
| Plünnecke–Ruzsa; Balog–Szemerédi–Gowers; Szemerédi–Trotter and Elekes's sum-product bound | | 11 |
| Roth's theorem with a bound \(N/\log\log N\) (second proof); Behrend's construction | | 12 |
| The generalised von Neumann theorem; the \(U^2\) inverse theorem; the \(W\)-trick | | 13 |
| Hardy's theorem; the mean square on the critical line; Montgomery's pair correlation under the Riemann hypothesis for \(0\le\alpha\le1-\varepsilon\) | `thm:hardy`, `thm:hardylittlewood`, `thm:montgomerypc` | 14 |

## Stated without proof

The list is fixed by decision D-28. Each heading carries "quoted" or the hypothesis.

| Statement | Heading must say |
| --- | --- |
| Vinogradov–Korobov; Huxley; Baker–Harman–Pintz; Guth–Maynard | Quoted |
| Chen's theorem; effective Chebotarev | Quoted |
| Hooley's theorem | Conditional on the generalised Riemann hypothesis |
| The Vinogradov mean value theorem; Weil's bound for Kloosterman sums | Quoted |
| Helfgott's theorem (every odd number above 5) | Quoted |
| Zhang's theorem; the bounds 600 and 246 | Quoted, in a remark "Records, quoted" |
| The consequence of Elliott–Halberstam for gaps | Conditional |
| Matomäki–Radziwiłł | Quoted |
| Freiman's theorem in \(\mathbb Z\); the polynomial Freiman–Ruzsa theorem | Quoted |
| Szemerédi; Kelley–Meka | Quoted |
| The inverse theorem for higher Gowers norms; the relative Szemerédi theorem; Green–Tao | Quoted |
| A positive proportion of zeros on the critical line (`thm:proportion`); the approximate functional equation (`thm:afe`); the Riemann–Siegel formula | Quoted |
| Montgomery's conjecture for \(\alpha\ge1\) | Conjecture |
| Siegel's constant | Ineffective, said wherever it is inherited: Chapters 2, 4, 7 |

## Climax

Bombieri–Vinogradov at the end of Part I: the Riemann hypothesis for progressions, true on average. Bounded gaps at the end of Part II: a theorem from 2013 with a complete proof on the page. The volume closes on the critical line with Montgomery's formula, which is the first line of Volume 15's third part.

## Motivation and history

Hoheisel, Siegel's two-page paper, Brun and Selberg's parity discovery, Linnik and Rényi, Bombieri's 1965 paper, Hardy and Littlewood's "Partitio Numerorum", Vinogradov 1937, Goldbach's letter, Goldston–Pintz–Yıldırım, Zhang's seventy million in May 2013 and Maynard that November, Roth, Gowers, Green and Tao, Hardy 1914, Montgomery and Dyson. Each sourced.

## Examples and exercises

Zero-density against the count of zeros; a real character with a suspiciously small \(L(1,\chi)\); a sieve that cannot tell primes from products of two; \(g(2)=4\) and the singular series for cubes; an admissible 5-tuple and Maynard's quadratic form for \(k=5\) computed exactly; a set of integers with no three-term progression; the first zeros on the line. Five to seven exercises per chapter at three levels.

## Figures and experiments

Major and minor arcs; the weights of Maynard's sieve; \(F(\alpha)\) from computed zeros against Montgomery's prediction, captioned with the range in which the prediction is a theorem under the Riemann hypothesis. The explicit gap constant of Chapter 9 and its admissible tuple are produced and checked by a script in the repository and recorded in the ledger.

## Changes from the current manuscript

**Preserve.** Chapters 1–5, 7–8 and 10–14 as written.

**Receive.** `waring.tex` from Volume 5, as Chapter 6.

**Rewrite.** Chapter 6: remove stale chapter numbers and the reminders written for Volume 5's level; cite Volume 6 for Weyl differencing and sums of minima and Volume 8 for Fourier inversion; merge the Dirichlet approximation lemma with the one in Chapter 5 (one home, Chapter 5); prove positivity of the singular series for \(s\ge4k\) so that `cor:gk`, \(G(k)\le2^k+1\), is a theorem of the book. If that proof is not written, `cor:gk` is headed "given the quoted positivity of the singular series". Chapter 7: its first sentence now points back one chapter, not to Volume 5.

Chapter 9: the theorem now labelled `thm:six` mixes what is proved with what is quoted. It becomes four statements. (a) The criterion: if \(M_k>4\) then there are infinitely many pairs of primes in every admissible \(k\)-tuple, proved. (b) The exact value for \(k=5\) and the bound it gives under Elliott–Halberstam, proved and conditional. (c) New: an explicit \(k_0\) with \(M_{k_0}>4\) from `prop:mklower` with all constants written, an explicit admissible \(k_0\)-tuple (the first \(k_0\) primes above \(k_0\)), and the resulting unconditional bound \(\liminf(p_{n+1}-p_n)\le C\) with \(C\) a stated number. (d) A remark, "Records, quoted": 600 by Maynard with data not printed here, 246 by Polymath.

**Remove.** The sentence that a witness "is said to give" 600, from any theorem.

**Missing.** One sentence in Chapter 12 naming Volume 11's proof and one in Chapter 14 naming Volume 12's sine kernel, both by label.

## Links

**From Volume 13.** \(L\)-functions with their functional equations; class numbers.
**From Volume 6.** The whole classical theory, cited and never reproved.
**To Volume 15.** Siegel–Walfisz, Bombieri–Vinogradov, the fundamental lemma, Halász, Maynard's sieve, the \(U^2\) inverse theorem, Montgomery's theorem. Volume 15 cites each by label with its status, and uses no quoted theorem of this volume as if proved.
**Back to Volume 12.** `thm:montgomerypc` discharges the statement admitted there.

## Size

About 5,210 source lines with Waring. **Estimate, not measured:** 160–200 printed pages. The volume is short for its content; the new material of Chapters 6 and 9 adds perhaps ten pages.

## Mathematical risks

1. Bombieri–Vinogradov as one chain: large sieve, Vaughan's identity, the bilinear estimate, Siegel–Walfisz for small moduli. Every link's range of parameters must match the next.
2. The explicit constant in Chapter 9: `prop:mklower` is stated "for sufficiently large \(k\)"; making \(k_0\) explicit needs every implied constant in its proof. This is new mathematics on the page and needs a careful record and a script.
3. Siegel's theorem and the honesty of "ineffective" downstream.
4. Waring: the minor-arc bound for \(s=2^k+1\) exactly, and the singular integral.
5. Montgomery: the exact statement proved, including the diagonal term and the uniformity in \(\alpha\).
6. Carlson's estimate: the mollifier's length.
7. Roth: the density increment's bookkeeping.

## Acceptance requirements

- Structure equals the table above.
- No theorem heading contains a bound the book does not prove. The remark "Records, quoted" exists and has sources.
- Verification records for every label in the flagship table, `thm:bv` and Chapter 9 first.
- The script for the explicit gap and its tuple is in the repository; its output matches the printed constant.
- Every item of the "without proof" table carries its heading.
- The ten editorial standards of the master plan, section 6.5.
