# Volume 4 removed-material audit

**Date:** 11 November 2026.
**Status:** audit only. No manuscript text is restored in this change. No other volume is edited. No KDP file is produced or uploaded.
**Author of this reading:** the present audit session. This file is that session’s self-check against the blobs named below. It is not an independent second review, and nothing in it is an independent acceptance. The distinct second review is pull request [#191](https://github.com/OussamaSegh/Order-and-Chance/pull/191), head `a76e24a7ba0b9f7f917c83e28f508bd1e98f03b5`, note `docs/review/volume4-removed-material-audit-second-review-2026-11-11.md`. That note read the first audit head `791d35f6`. This reconciliation answers it from the corrected head `6dc3c31d` and the edits below. The same reviewer sees this update before the owner is asked to restore anything.

The owner identified the rewrite writer as cloud agent `bc-812f7ec4`. That identifier does not occur in the pinned tree, in `git log -S`, or in a GitHub issue and commit search from this environment. The rewrite notes describe writer self-review. Those notes are not treated as proof.

## Pins

| Role | SHA | What it is |
| --- | --- | --- |
| Current `main`, this audit's manuscript | `a2cfdd30a0f09eabcb932852c76537c8af592bdb` | Fetched again before this reconciliation. `git rev-parse origin/main` still returns this SHA. Subject: Volume 4, empty-success bound from finite additivity (#176), 11 November 2026, 12:37:59 +0000. |
| Pre-PR 111 baseline | `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6` | First parent of squash commit `e120d10a1a1466d5dfc5b6ea4229a83ba8d83cfe`, “Rewrite Volume 4 from the Volume 1–3 boundary (#111)”, merged 8 November 2026, 15:02:18Z. Parent subject: merge of #112. |
| 213-line method checkpoint | `285122b4a592bfef3c695b1103dd2cd3e8c3a77a` | On `origin/cursor/volume4-rewrite-ee7f` only. `ch12-method.tex` has 213 lines there, and also at `2051369ed01465195a397fbe6087cb161d1f7ece`. Current `main` has 274 lines. The 213-line file is a checkpoint, not the book. |

PR 111 is a single-parent squash. The baseline is the `main` tree it replaced, recovered from that parent, not from a guessed date.

`volume4-chance/chapters/ch12-method.tex` on current `main` is blob `7bb8f4a676a46524817beb217d04f18ad6317a21`, 274 lines. That blob is unchanged on `main` after the squash: `git log e120d10a..a2cfdd30 -- volume4-chance/chapters/ch12-method.tex` is empty. Later restorations live in other chapter files.

## How this audit was made

Routed sources are the files reached by `\input` from `main.tex`, one level deep. At the baseline that route is the preface, chapters 1–12, `gilmer.tex` (pulled in at `ch04-inequalities.tex:540`), the extremal appendix, and the cover note. At the pinned SHA the route is the preface, fourteen chapter files (entropy and geometric probability are separate files; random graphs are `ch14-graphs.tex`), the extremal appendix, bibliography, index, and the cover note. `gilmer.tex` is not on the route.

Every `\begin{exercise}...\label{...}` in the baseline route was paired with `\begin{hint}{label}` and `\begin{solution}{label}`. There are 174 exercises, 174 hints, and 174 solutions, with no unmatched label inside a file. Sixty-five of those exercise labels are still exercise labels on the current route. The other 109 are the inventory below. Each of those 109 still has both a hint and a solution in the baseline file.

A deleted line is not, by itself, a lost theorem. The same claim often survives under a new label, in a later chapter of this volume, or in a later volume. The class names used below are:

- **rewritten** — the mathematical task is in the pinned Volume 4, under another label or in the main text;
- **relocated** — the same task is in another volume of the pinned tree;
- **lost** — the task is not in the pinned series in a form a reader can use;
- **too advanced** — a correct or standard argument whose tools sit outside a reader of Volumes 1–4, or outside the high-school path even when a later volume owns them;
- **duplicate** — the series already teaches the fact.

“Solvable from Volumes 1–4” means a reader of those four volumes, with the proofs they actually contain. Volumes 2 and 3 are allowed when the solution uses them. Volume 5 and later are not. The Volume 4 plan also says Volumes 2 and 3 are not a step on the main path. An exercise that needs them can be optional. It should not be required for a later theorem of Volume 4.

`docs/plan/volume4-old-to-new.md` is a plan written during the rewrite. It is not authority. Several of its rows are stale: it still describes twelve chapters in the old order, it keeps entropy inside Chapter 4, and it says exercises were rebuilt in the same slots. The pinned book has fourteen chapters, entropy is its own chapter, and many old exercise labels have no successor.

## Counts verified on the blobs

| Item | Baseline route | Pinned route |
| --- | --- | --- |
| Exercise / hint / solution triples | 174 / 174 / 174 | 107 exercises on the current route, labels listed in the phase notes; 65 old labels survive |
| Old labels absent from the current Volume 4 route | — | 109 (68 `pb:*`, 41 other) |
| `pb:*` labels found anywhere on the current route | — | 0 |
| `ch12-method.tex` lines | 2037, blob `eb9d6c27cf75d112d74a2848f19ae6e934034d61` | 274, blob `7bb8f4a676a46524817beb217d04f18ad6317a21` |
| `gilmer.tex` | 106 lines, blob `dd703c9be37b4ab380392e0cc8c7922fd3e35c35`, `\input` from Chapter 4 | same blob, file still in the tree, not `\input` |
| Solution lines of the 109 missing exercises | 2264 | — |
| Exercise-statement lines of those 109 | 970 | — |

Source lines are not pages. No build of baseline `5c4840cc` was found in the repository, so this audit states no page count for the old book.

Of the 109 missing exercises, the class column of the inventory counts:

| Class | Count |
| --- | --- |
| Rewritten into the pinned Volume 4, including the explicit weakening of the longest-run exercise | 10 |
| Relocated to a later volume | 2 |
| Lost, including one admitted gap (`ex:noodle`) and one citation risk (`ex:wald2`) | 57 |
| Too advanced for Volumes 1–4 | 33 |
| Duplicate of a theorem or exercise the pinned series already has | 7 |

The first-pass recommendation column counted 16 restores, 1 repair-then-restore, 18 optional items, and 74 omissions. Later sections change individual cells. The reconciled counts are stated after those sections, once the table matches them. The owner-decision list is the line-checked subset, plus the 2-SAT theorem, which is not one of the 109 exercises. The omissions include the long workshop tail. Putting that tail back to fill pages would ignore the prerequisite line. The ideal length is 300–600 pages, with 600 as a maximum. Three hundred is not a quota.

## What the pinned book still proves

The rewrite, and the restorations merged after it, kept the spine. The following are in the pinned sources, so they are not restoration candidates:

- Ballot theorem, outer content, digits as fair bits (`ch01-counting.tex`).
- Poisson limit, cycles, coupon collector (`ch02-discrete.tex`).
- Generating functions, extinction, Catalan numbers (`ch03-generating.tex`).
- Hoeffding, Borel–Cantelli, bounded strong law, Bernstein–Weierstrass (`ch04-inequalities.tex`). The coin large-deviation upper bound is Exercise `ex:chernoffbin`.
- Densities, a continuous Fubini statement on rectangles, polar coordinates, dominated convergence for continuous integrands, Box–Muller (`ch05-continuous.tex`). Bertrand and Buffon are `ch05-geometric.tex`.
- Fourth-moment strong law, Glivenko–Cantelli, inversion (`thm:inversion`), Lindeberg as Theorem 6.10, local theorem, Gaussian vectors (`ch06-clt.tex`).
- Finite entropy, Kraft, Shannon, chain rule, Huffman (`ch07-entropy.tex`).
- Reflection, ruin, Pólya, arcsine limit (`ch07-walks.tex`).
- Finite-chain convergence, top-to-random, Bayer–Diaconis (`thm:bayerdiaconis`), untouched cards (`ch08-markov.tex`).
- Poisson process, colouring lemma, thinning, Le Cam, M/M/1 (`ch09-poisson.tex`).
- Optional stopping with three sufficient conditions, the first-win counter-example, upcrossings, Doob, Azuma, the pattern wait, Pólya’s urn for one red and one blue, almost-sure convergence on interval partitions (`ch10-martingales.tex`).
- Lévy construction, scaling, quadratic variation, a dyadic expansion, nowhere differentiability, reflection (`ch11-brownian.tex`).
- First moment, alteration, symmetric local lemma, second moment, Euler, crossings (`ch12-method.tex`); subcritical components and triangles (`ch14-graphs.tex`).
- Turán, Ramsey, Schur, sunflower, Erdős–Ko–Rado, the two-colour three-term check, and general van der Waerden (`extremal.tex`, `thm:vdw` at lines 130–147).

Those restorations are already on `a2cfdd30`. Recommending them again would duplicate the book. The citation-migration note’s older paragraphs that say inversion, Bayer–Diaconis, and general van der Waerden are absent describe an intermediate draft. The pinned files contain those theorems.

After the 289-page measurement recorded below, `main` gained further proof repairs in Chapters 1, 2, 4, 5, 6, 7, 8, 9, 10 and 11, plus a bibliography and an index (`git diff --stat 3cc07e86 a2cfdd30 -- volume4-chance`: 311 insertions, 122 deletions). None of that diff puts a `pb:*` exercise back.

## Measure theory (V4-RM-MT)

**Baseline.** `volume4-chance/chapters/ch05-continuous.tex`, blob `4040739625fdea6c7362a91056d9d8c910ac6239`.

| Item | Lines | Label |
| --- | --- | --- |
| Vitali non-existence | 33–43 | `thm:vitali` |
| Dynkin π–λ | 77–90 | `thm:dynkin` |
| Uniqueness of measures | 92–102 | `thm:uniqueness` |
| Admitted Lebesgue measure and infinite products | 107–121 | reminder (A1) |
| Admitted Tonelli–Fubini | 112–120 | reminder (A2) |
| Monotone convergence | 183–194 | `thm:mct` |
| Fatou | 220–226 | `thm:fatou` |
| Dominated convergence, general | 237–245 | `thm:dct` |
| Agreement with the Riemann integral | 279–295 | `prop:riemann` |

The preface at baseline lines 15–19 says the volume proves the integral’s main theorems and admits two facts from Volume 7: existence of the uniform law and of infinite products, and Fubini–Tonelli. The chapter title and the opening (lines 15–20) say the chapter builds Lebesgue’s integral. The existence of Lebesgue measure is the admitted box at lines 107–111, not a construction. The proofs of monotone convergence, Fatou, and dominated convergence are the standard ones and are complete relative to a measure already in hand. Vitali’s argument (lines 37–42) is the usual axiom-of-choice selector and is complete as a negative statement. Dynkin’s proof (lines 80–89) is the usual two-family argument and is complete.

**Pinned book.** `thm:dct` at `ch05-continuous.tex:322–327` is dominated convergence for continuous integrands, uniformly on compact intervals, with a continuous integrable dominant. The text at lines 320–321 calls this a narrower Riemann form and says it is what the next chapter uses. Vitali is one sentence at lines 14–15: the obstruction is named, the axiom of choice is named, and no proof is given. Dynkin, monotone convergence, Fatou, and general dominated convergence are absent. The bibliography still cites Vitali’s 1905 note.

**Judgement.** Removing the abstract engine is justified. The old chapter did not construct the measure it integrated against, and the series rule is that measure theory is not an unproved lemma of this volume. The pinned theorem is explicitly narrower. Later chapters that needed a general integral were rewritten onto interval lengths, digit cylinders, and continuous test functions; where a later volume still says “Tonelli”, that citation is a separate repair and is not a reason to put the general theorem back here. A one-sentence Vitali remark is already present. Restoring the selector proof would be a short optional remark, not a working tool. Restoring Dynkin, monotone convergence, Fatou, and general dominated convergence would be a large block and would either re-admit Volume 7 or require a construction this volume does not have.

**Recommendation:** omit the block. Do not restore it to lengthen the book.
**Confidence:** high on the scope comparison and on the reading of Vitali, Dynkin, monotone convergence, Fatou, and the old dominated-convergence proof. The admission box was read in full.

## Gilmer and the finite probabilistic method (V4-RM-GIL)

**Baseline inclusion.** `ch04-inequalities.tex:540` is `\input{chapters/gilmer}`.
**File.** `volume4-chance/chapters/gilmer.tex`, blob `dd703c9be37b4ab380392e0cc8c7922fd3e35c35`, 106 lines, identical at both SHAs.
**Pinned book.** `main.tex` does not input the file.

The file proves a conditional-entropy chain rule (`conjectures:lem:condent`, lines 8–22), Gilmer’s frequency theorem under an inequality hypothesis (`conjectures:thm:gilmer`, lines 28–51), the numerical inequality for \(h(xy)\) (`conjectures:lem:hxy`, lines 57–94), and the constant \((1-\ln 2)/2\) (`conjectures:cor:ucconst`, lines 96–106).

The constant arithmetic was checked by hand. With \(c=2/(1+\ln 2)\),

\[
1-\frac1c=1-\frac{1+\ln 2}2=\frac{1-\ln 2}2.
\]

That identity is right. The chain-rule proof is the usual splitting of \(\ln(1/P)\) and is complete for finite alphabets. The defect estimate in `conjectures:lem:hxy` (the series for \(K\), the bound \(D(a,b)\le(a+b)\ln 2\), and the sign of \(Q'''\)) was read and not re-derived. This audit does not certify that inequality.

Volume 15 proves a Gilmer theorem at `volume15-order-and-chance/chapters/conjectures-ch08-geometric.tex:300`, label `conjectures:thm:gilmer`, and computes the same constant at line 377. The Volume 15 text is not a byte copy of `gilmer.tex`. No pinned Volume 4 theorem is cited for it. Volume 4’s entropy chapter (`ch07-entropy.tex`) proves Gibbs, the chain rule in bits, Kraft, and Shannon. It does not prove the natural-log defect inequality `conjectures:lem:hxy`.

**Finite method, kept.** The old Chapter 12 main text (first moment, alteration, second moment, local lemma, subcritical components, crossings) survives in `ch12-method.tex` and `ch14-graphs.tex` under new labels (`thm:erdos`, `thm:alter`, `thm:lll`, `prop:second`, `prop:euler`, `prop:crossing`, `thm:subcrit`, `thm:triangles`). The 33 `pb:*` problems appended to that chapter are a different object. Most of them call on group theory, electrical networks, Fourier analysis, the prime-number theorem, or Collatz. Cutting that list did not remove the finite method.

**Recommendation:** omit `gilmer.tex` from Volume 4. Leave the file unused or, in a later cleanup that is not this audit, stop shipping an unincluded duplicate. Do not restore the defect inequality into the entropy chapter. A one-line pointer that Volume 15 owns the union-closed bound would be optional and is not proposed here as new prose.
**Confidence:** high on the inclusion status, the constant arithmetic, and the Volume 15 location. Medium on the defect estimate, which was not re-proved.

## Scope changes that are already written down

These are not silent weakenings. The pinned statement says what it proves.

| ID | Old claim | Pinned claim | Recommendation |
| --- | --- | --- | --- |
| V4-RM-DCT | General dominated convergence, `ch05-continuous.tex:237–245` | Continuous integrands, uniform on compacts, `ch05-continuous.tex:322–327` | Omit the general theorem. The narrowing is explicit. |
| V4-RM-CHER | Numbered Chernoff bounds for non-identical Bernoulli variables, `ch04-inequalities.tex:146–175`, blob `6d8d0b1ef04c6086540be2084d298ac16bf5a125` | Section title “Chernoff and Hoeffding”; the theorem proved is Hoeffding, `ch04-inequalities.tex:63–80`. The identical-coin upper rate is `ex:chernoffbin` | Omit the numbered multiplicative form. Hoeffding is the cited inequality. The exponent algebra of the old lower tail was checked: with \(\lambda=\ln(1-\delta')<0\), the Markov step reproduces \(\bigl(e^{-\delta'}(1-\delta')^{-(1-\delta')}\bigr)^\mu\). The simplified \(\delta^2/3\) calculus was not re-derived. |
| V4-RM-CRAM | Matching lower bound and the limit \(\frac1n\ln P(S_n\ge na)\to -I_p(a)\), `ch04-inequalities.tex:184–200` | Upper bound only, inside `ex:chernoffbin` | Optional one-part addition to that exercise if the owner wants the rate theorem. Not required for the spine. The largest-term idea was read; the full lower-bound write-up was not re-derived past the mode of the binomial. |
| V4-RM-ITO | Discrete Itô formula and a Black–Scholes limit, `ch11-brownian.tex` sections at lines 301 and 332, theorems `prop:discreteito`, `thm:binomial`, `thm:blackscholes` | `thm:dyadicito` is a dyadic expansion. Exercises `ex:putcall` and `ex:onestep` remain. Volume 12 has `thm:blackscholes` | Omit the limit theorem from Volume 4. The pinned book says it does not use Itô’s formula as a premise. |
| V4-RM-2SAT | Papadimitriou’s 2-SAT walk, `ch07-walks.tex:417–468`, `thm:twosat` and `cor:twosat`, blob `29d4b1353bbc971ca10e26c206e91c62d633710f` | Absent. A search of the pinned `volume4-chance` for `2-SAT`, `twosat`, and `Papadimitriou` finds nothing | **Small restoration, owner decision.** The drift identity was checked: if \(\Psi(x)=n^2-x^2\) and the upward probability is \(\theta\ge 1/2\), then \(\mathbb E[\Psi(X_{t+1})]+1-\Psi(x)=2x(1-2\theta)\le 0\). The bound \(\mathbb E[T]\le n^2\) is the monotone limit of \(\mathbb E[t\wedge T]\), which is the tail sum for a nonnegative integer, not Lebesgue’s theorem. The word “monotone convergence” in the old proof should be rewritten as that tail sum if the section returns. Confidence high on the algebra. |
| V4-RM-RUN | `ex:longestrun` asks for \(L_n/\log_2 n\to 1\) almost surely, solution `ch04-inequalities.tex:838–852` | `ex:runs` asks for convergence in probability and says a complete almost-sure statement is not required, `ch04-inequalities.tex:302–304` | The weakening is explicit. The old almost-sure argument is Borel–Cantelli on the coin space and could be added as a second part. Optional, not required. |
| V4-RM-POLYA | General Pólya urn and a Beta\((a,b)\) density, `ex:polyabeta` | `thm:polyaurn` is the case of one red and one blue, with a uniform limit proved from the explicit count. Volume 11, `ch09-martingales.tex:453`, asks for the general Beta law | Special case kept. General case relocated. Omit from Volume 4. |

## Network block (V4-RM-NET)

`pb:commute`, `pb:foster`, `pb:rayleigh`, and `pb:aldousbroder` are one chain: commute time, Foster’s theorem, Rayleigh’s monotonicity, and the Aldous–Broder spanning tree. The tools lines cite the electrical exercise and each other. Volume 12 already has the commute-time identity at `volume12-random-motion/chapters/ch08-networks.tex:114`, label `thm:commute`. Volume 4 keeps one electrical exercise, `ex:electric`.

**Recommendation:** omit the chain from Volume 4. Restoring it would be a large second chapter on networks and would duplicate Volume 12. Confidence medium: the four solutions were classified from their statements and tools lines and were not re-proved line by line. The dependency among them is explicit in those tools lines.

## Exercise inventory

Locations are baseline line ranges. The blob is the baseline file blob. “Read” means this session read the solution and checked the algebra or the count named in the note. “Tools” means the class comes from the statement and the solution’s tools line, without a line-by-line re-proof. Hints exist for every row at the hint lines in the extractor output; they are omitted from the table to keep it readable.

Current targets, when the class is rewritten or relocated, are pinned paths.

| ID | Label | Baseline | Sol. | Class | Read | Recommendation | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V4-RM-E01 | `ex:twotests` | `ch01-counting.tex:405–408` | 570–578 | lost | Read. Arithmetic \(0.009801/0.012276\approx 0.798\) and the odds \(3.96/4.96\) check. The rates are in baseline Example `ex:medical`, which begins at line 129 of the same file and is absent from the pinned chapter. The exercise prompt only names that example | repair+restore only after the rates are written into the prompt. Until then it is not self-contained | medium |
| V4-RM-E02 | `ex:secretary` | `ch01-counting.tex:435–441` | 620–635 | lost | Read (a). \(p_r=\frac{r-1}n\sum_{k=r}^n\frac1{k-1}\) follows from uniformity of the best among the first \(k-1\). The sentence that no strategy beats the best threshold was not re-proved | restore (a) and the \(1/e\) limit. Drop or prove the optimality sentence | high for (a) |
| V4-RM-E03 | `ex:noodle` | `ch01-counting.tex:443–452` | 637–654 | lost, gap | The problem allows the reader to admit that the expected number of crossings of a segment is increasing and additive. Buffon’s needle is already `thm:buffon` | omit. A second proof that admits its main input is not a repair worth making while the direct proof stands | high on the gap |
| V4-RM-E04 | `pb:whichroot` | `ch01-counting.tex:454–462` | 656–698 | too advanced | Tools cite Volume 13 for \(\mathbb Q_p\). Part (a) is a Catalan identity | omit. Part (a) is already the Catalan material of Chapter 3 | high |
| V4-RM-E05 | `pb:nouniform` | `ch01-counting.tex:464–472` | 700–719 | lost; (a) and (c) are not finished Volume 1–4 proofs | (a) concludes \(P(\mathbb N^*)=\sum_n P(\{n\})=0\). Pinned `ch01-counting.tex:43` says countable additivity on a full infinite-event space is not proved. Finite additivity does not make that sum zero. (b) is a count of densities. (c) says \(B\) contains one of every two consecutive integers; with \(I_j=[4^j,2\cdot 4^j[\), both \(3\) and \(4\) lie in \(B\). The Hahn–Banach sentence is a lead, not a step | omit as written. Do not restore (a) as a corollary of Chapter 1. A different exercise that assumes countable additivity is not proposed here | high |
| V4-RM-E06 | `pb:bollobas` | `ch01-counting.tex:474–482` | 721–740 | lost | Tools: random permutations and the LYM inequality | omit. Finite and standard, and it is extremal set theory rather than a probability theorem of this book | medium |
| V4-RM-E07 | `pb:granularity` | `ch01-counting.tex:484–494` | 742–767 | too advanced | Boolean degree and influences | omit | medium |
| V4-RM-E08 | `pb:leastqnr` | `ch02-discrete.tex:383–390` | 648–665 | too advanced | Tools: Legendre symbol. The statement says “pretend” the symbols are random | omit. Part (b) is a heuristic unless a later reading finds a real proof | medium |
| V4-RM-E09 | `pb:glfix` | `ch02-discrete.tex:392–401` | 667–683 | too advanced | Tools: \(\mathrm{GL}_n(\mathbb F_q)\) and Burnside | omit | medium |
| V4-RM-E10 | `pb:foata` | `ch02-discrete.tex:403–412` | 685–702 | lost | Tools: cycle notation and records, both already in Chapter 2 | omit. The bijection is optional colour, not a missing theorem | low |
| V4-RM-E11 | `pb:paley` | `ch02-discrete.tex:414–427` | 704–742 | too advanced | Depends on `pb:conics` and quadratic residues | omit | medium |
| V4-RM-E12 | `pb:goodman` | `ch02-discrete.tex:429–439` | 744–764 | lost | Read. For \(n=6\), \(\binom63-\frac n2\lfloor(n-1)^2/4\rfloor=20-18=2\). A random colouring makes a triangle monochromatic with probability \(1/4\) | restore, next to Ramsey. It is the finite counting the method chapter is for | high |
| V4-RM-E13 | `pb:influence` | `ch02-discrete.tex:441–451` | 766–791 | too advanced | Boolean influences | omit | medium |
| V4-RM-E14 | `pb:arrow` | `ch02-discrete.tex:453–470` | 793–823 | too advanced | Depends on `pb:influence` and `pb:majoritystable` | omit | medium |
| V4-RM-E15 | `pb:lcs` | `ch02-discrete.tex:472–481` | 825–844 | lost | Tools cite a subadditive lemma from `pb:saw`. The exact constant for random common subsequences is research-scale | omit. Unresolved how much of the solution is an elementary bound | low |
| V4-RM-E16 | `pb:sicherman` | `ch03-generating.tex:309–312` | 450–477 | lost | Read. \(x(1+x)(1+x+x^2)=x+2x^2+2x^3+x^4\) expands to faces \(1,2,2,3,3,4\). The two quadratics have negative discriminants. Volume 1’s polynomial chapter proves Euclidean division and the discriminant test. It does not contain a theorem titled unique factorisation of \(\mathbb Q[X]\) | restore only if the write-up peels irreducible factors by that division, and does not cite a unique-factorisation theorem by name | high |
| V4-RM-E17 | `pb:loaded` | `ch03-generating.tex:314–318` | 479–501 | lost | Read. AM–GM gives \(p_1q_n+p_nq_1\ge 2/(2n-1)>1/(2n-1)\) | restore | high |
| V4-RM-E18 | `pb:subsetsum` | `ch03-generating.tex:320–330` | 503–535 | lost | Read. For \(p=3\), \((2^3-2)/3+2=4\), and the eight subsets were listed: four sums are divisible by 3. The formula value 52 for \(p=5\) was checked as arithmetic, not by listing subsets. The roots-of-unity product was followed and not re-expanded | restore (a) and (b). (c) is optional | high for (a) |
| V4-RM-E19 | `ex:sharp` | `ch04-inequalities.tex:544–547` | 734–738 | partly rewritten | Part (a) is Markov’s equality at threshold \(a\). Pinned `ex:markovsharp` asks that question. Part (b) is Chebyshev’s equality at a prescribed variance, with mass \(\sigma^2/(2a^2)\) at each of \(\pm a\). That example is not `ex:markovsharp` | omit. Part (a) is already an exercise. Part (b) is lost and is not added to the owner list | high |
| V4-RM-E20 | `ex:lipschitz` | `ch04-inequalities.tex:549–551` | 740–746 | lost | Read. Cauchy–Schwarz gives the \(L/(2\sqrt n)\) bound. The sharpness sentence cites the central limit theorem without proving the rate | omit. `ex:bernstein2` computes the exact error for \(x^2\). The sharpness sentence is a gap | high |
| V4-RM-E21 | `ex:pinsker` | `ch04-inequalities.tex:553–556` | 748–755 | lost | Read. \(\varphi''(a)=1/(a(1-a))-4\ge 0\) because \(a(1-a)\le 1/4\) | optional. The rate itself is `ex:chernoffbin` | high |
| V4-RM-E22 | `ex:entropybinom` | `ch04-inequalities.tex:558–561` | 757–765 | lost | Read. The largest binomial probability is at least \(1/(n+1)\) | optional, beside typical sequences | high |
| V4-RM-E23 | `ex:ballsbins` | `ch04-inequalities.tex:563–567` | 767–779 | lost | (a) \(\binom nk n^{-k}\le 1/k!\) and \(e^k\ge k^k/k!\). (b) \(\psi(u)=(\ln u+1-\ln 3)/u\) has derivative \((\ln 3-\ln u)/u^2\), so the maximum on \(u>0\) is \(\psi(3)=1/3\). Then \((e/k)^k\le n^{-2}\). The second review checked this derivative; this reconciliation differentiated it again. Gonnet’s matching lower bound is a citation | restore (a) and (b), and drop the Gonnet citation. Do not copy that lower bound in as a proof | high |
| V4-RM-E24 | `ex:bloom` | `ch04-inequalities.tex:569–576` | 781–800 | lost | Tools only | optional | medium |
| V4-RM-E25 | `ex:median` | `ch04-inequalities.tex:578–582` | 802–811 | lost | Tools only. Finite Hoeffding application | optional | medium |
| V4-RM-E26 | `ex:mcmillan` | `ch04-inequalities.tex:584–589` | 813–825 | lost | Read. \(K^N\le N\ell_{\max}\) because each length has at most \(2^L\) decodable words, so \(K\le 1\) | restore beside Kraft. Prefix codes are already `thm:kraft`; this is the uniquely decodable extension | high |
| V4-RM-E27 | `ex:subadd` | `ch04-inequalities.tex:591–594` | 827–836 | rewritten | \(H(X,Y)=H(X)+H(Y\mid X)\) is `prop:chain`, and \(H(Y\mid X)\le H(Y)\) is `thm:mutual` | omit | high |
| V4-RM-E28 | `ex:longestrun` | `ch04-inequalities.tex:596–599` | 838–852 | rewritten, weaker | Read. See V4-RM-RUN | optional second part for the almost-sure statement | high |
| V4-RM-E29 | `pb:capset` | `ch04-inequalities.tex:601–616` | 854–895 | too advanced | Ellenberg–Gijswijt / Tao polynomial method. Not line-checked | omit. Large | high on the class |
| V4-RM-E30 | `pb:kac` | `ch04-inequalities.tex:618–632` | 897–944 | lost | Lacunary trigonometric sums. The central limit theorem is already proved | omit | medium |
| V4-RM-E31 | `pb:bonami` | `ch04-inequalities.tex:634–642` | 946–975 | too advanced | Tools claim only Cauchy–Schwarz. The inequality is hypercontractivity even if an elementary proof exists. Not line-checked | omit | medium |
| V4-RM-E32 | `pb:kacring` | `ch04-inequalities.tex:644–658` | 977–1005 | lost | Not line-checked | omit | low |
| V4-RM-E33 | `pb:nbonacci` | `ch04-inequalities.tex:660–668` | 1007–1025 | lost | A recurrence for its own sake | omit | medium |
| V4-RM-E34 | `ex:betagamma` | `ch05-continuous.tex:590–594` | 773–794 | partial relocation | Volume 7, `ch08-products.tex:344`, asks for \(\Gamma(a)\Gamma(b)=B(a,b)\Gamma(a+b)\). Line 349 asks for the sum of two Gamma laws. Neither exercise proves that \(S=X+Y\) and \(V=X/(X+Y)\) are independent | omit from Volume 4. The independence statement is lost; the integral identity is in Volume 7 | high |
| V4-RM-E35 | `pb:laplace` | `ch05-continuous.tex:596–604` | 796–826 | lost | Square tiling. Buffon’s needle for parallel lines is already proved. Solution not line-checked | optional | medium |
| V4-RM-E36 | `pb:passone` | `ch05-continuous.tex:606–613` | 828–850 | lost | Read. \(P(N>n)=1/n!\), \(\mathbb E[N]=e\), \(\mathbb E[N^2]=3e\), variance \(3e-e^2\). The numerical value \(0.7657\ldots\) matches \(3e-e^2\) | restore. The ordered-uniform map is already in Chapter 5 | high |
| V4-RM-E37 | `pb:irwinhall` | `ch05-continuous.tex:615–624` | 852–880 | lost | The inclusion-exclusion for the simplex volume was read at the start and not finished | omit if `pb:passone` returns. The density formula is longer than the lesson | medium |
| V4-RM-E38 | `pb:borwein` | `ch05-continuous.tex:626–639` | 882–915 | too advanced | Tools: Volume 5, Dirichlet’s integral | omit | high on the tools |
| V4-RM-E39 | `pb:stick` | `ch05-continuous.tex:641–649` | 917–933 | lost | Read. \(P(\max A_j\ge 1/2)=n\,2^{-(n-1)}\). For three pieces the triangle probability is \(1-3/4=1/4\). \(\int_0^1 2t(1-t)^{n-1}\,dt=2/(n(n+1))\) was integrated by hand | restore | high |
| V4-RM-E40 | `pb:sincsum` | `ch06-clt.tex:462–475` | 586–618 | too advanced | Tools: Volume 5 Fourier theorems | omit | high on the tools |
| V4-RM-E41 | `pb:rootwalk` | `ch07-walks.tex:521–533` | 682–713 | too advanced | Tools: Volume 5 and `pb:vanish`. Pólya’s theorem is already proved | omit | medium |
| V4-RM-E42 | `ex:knight` | `ch08-markov.tex:610–613` | 803–809 | lost | The baseline solution is a hand sum from its figure: \(2\cdot 26+2\cdot 38+4\cdot 52=336\), corner return \(336/2=168\), centre return \(336/8=42\). It cites `cor:graph` and `fig:knight`, which are not the pinned text. An earlier draft of this audit also counted the edges by a program. That program is not the solution. Current `ch08-markov.tex:221` proves reversibility for the degree weights and does not prove that the mean return time is \(1/\pi(x)\) | omit. The hand sum is not a checked restoration | high |
| V4-RM-E43 | `ex:gsr` | `ch08-markov.tex:638–641` | 855–861 | rewritten | The Gilbert–Shannon–Reeds model is stated at `ch08-markov.tex:256–274`, and Bayer–Diaconis is `thm:bayerdiaconis` | omit | high |
| V4-RM-E44 | `pb:carries` | `ch08-markov.tex:648–656` | 872–896 | lost | Base-\(b\) digits and a Markov chain. Off the main path | omit | medium |
| V4-RM-E45 | `pb:dicemod` | `ch08-markov.tex:658–665` | 898–923 | lost | Roots of unity, close to `pb:subsetsum` | omit if subset sums return | medium |
| V4-RM-E46 | `pb:hypercubemix` | `ch08-markov.tex:667–684` | 925–954 | too advanced | Marked Journey. Sharp cutoff | omit | medium |
| V4-RM-E47 | `pb:antipode` | `ch08-markov.tex:686–702` | 956–983 | too advanced | Depends on `pb:commute` | omit with V4-RM-NET | medium |
| V4-RM-E48 | `pb:holte` | `ch08-markov.tex:704–717` | 985–1011 | too advanced | Journey, depends on carries and Irwin–Hall | omit | medium |
| V4-RM-E49 | `pb:gilbreath` | `ch08-markov.tex:719–732` | 1013–1047 | lost | A card principle. The riffle model is already in the chapter | omit | medium |
| V4-RM-E50 | `ex:race` | `ch09-poisson.tex:317–320` | 415–424 | rewritten | `prop:race` is “two competing clocks” | omit | high |
| V4-RM-E51 | `ex:binomialsplit` | `ch09-poisson.tex:322–325` | 426–431 | rewritten | Conditional uniformity is `thm:uniform`. The waiting-time integral \(\lambda t^2/2\) was not found as a separate exercise | optional one-line calculation; the conditional law is kept | medium |
| V4-RM-E52 | `ex:records2` | `ch09-poisson.tex:327–330` | 433–438 | lost | A total-variation bound. Le Cam is already a theorem | optional | medium |
| V4-RM-E53 | `ex:coupon2` | `ch09-poisson.tex:332–336` | 440–448 | duplicate | \(\mathbb E[T]=nH_n\) is the coupon theorem. The Gumbel limit is extra | omit | medium |
| V4-RM-E54 | `ex:little` | `ch09-poisson.tex:338–343` | 450–457 | lost | Little’s law for M/M/1. Not line-checked. The stationary geometric law is `thm:mm1` | optional | medium |
| V4-RM-E55 | `pb:spacings` | `ch09-poisson.tex:356–363` | 473–494 | lost | Depends on `pb:stick`. Order statistics are already in the chapter | omit | medium |
| V4-RM-E56 | `pb:dixie` | `ch09-poisson.tex:365–376` | 496–517 | duplicate | Collecting \(m\) copies. The case \(m=1\) is the coupon theorem | omit | medium |
| V4-RM-E57 | `ex:ruinasym` | `ch10-martingales.tex:600–603` | 679–685 | rewritten | Unfair ruin is `thm:ruin`, and `ex:unfair` computes the \(p=2/3\), \(N=3\) case | omit | high |
| V4-RM-E58 | `ex:patterns` | `ch10-martingales.tex:605–608` | 687–694 | rewritten | The pinned text states HT waits 4 and HH waits 6, `ch10-martingales.tex:257` | omit | high |
| V4-RM-E59 | `ex:doubling` | `ch10-martingales.tex:610–614` | 696–704 | rewritten | The first-win counter-example is the example “winning one unit”, `ch10-martingales.tex:79–81`. Volume 11’s `ex:doubling` is a different product martingale, a label collision | omit | high |
| V4-RM-E60 | `ex:wald2` | `ch10-martingales.tex:616–619` | 706–717 | lost, gap risk | The solution cites the old \(L^2\) theorem. The pinned \(L^2\) theorem is for finite interval partitions. Copying the exercise unchanged could over-claim | omit. Bounded stopping is already `thm:os` | medium |
| V4-RM-E61 | `ex:polyabeta` | `ch10-martingales.tex:621–628` | 719–733 | relocated | See V4-RM-POLYA | omit | high |
| V4-RM-E62 | `ex:signs` | `ch10-martingales.tex:630–633` | 735–741 | lost | Not line-checked. Asks for variance, and for almost-sure convergence when \(\alpha>1/2\) | omit | medium |
| V4-RM-E63 | `ex:chromatic` | `ch10-martingales.tex:635–639` | 743–751 | lost, citation gap | The deviation bound can be Azuma with a one-vertex Lipschitz constant. A parallel reading of the solution found the asymptotic \(\mathbb E\chi\sim n/(2\log_2 n)\) cited and not proved. This audit did not re-derive the solution | omit as written. Do not restore a solution that treats that asymptotic as known | medium |
| V4-RM-E64 | `ex:likelihood` | `ch10-martingales.tex:641–646` | 753–762 | lost | Finite-alphabet likelihood martingale. Volume 7’s `ex:likelihood` at `ch10-radon.tex:333` is Gaussian absolute continuity, a different problem. A parallel reading judged the finite proof sound and still recommended leaving it out | optional. Not on the checked restoration list | medium |
| V4-RM-E65 | `pb:vanish` | `ch12-method.tex:337–345` | 1067–1096 | too advanced | Cyclotomic fields, Volumes 1 and 3 in the tools line | omit | medium |
| V4-RM-E66 | `pb:samecycle` | `ch12-method.tex:347–353` | 1098–1115 | lost | Read. Each length has \((n-1)!\) permutations, so the probability is \(1/n\). Hockey-stick gives probability \(1/k\) that \(1,\ldots,k\) share a cycle | restore. It belongs with the cycle section of Chapter 2 | high |
| V4-RM-E67 | `pb:denes` | `ch12-method.tex:355–362` | 1117–1141 | lost | Transpositions and trees, Cayley’s count. Not line-checked | optional | medium |
| V4-RM-E68 | `pb:conics` | `ch12-method.tex:364–376` | 1143–1172 | too advanced | Legendre sums over finite fields | omit | high on the tools |
| V4-RM-E69 | `pb:hashing` | `ch12-method.tex:378–387` | 1174–1192 | lost | Read. Determinant \(x-y\neq 0\). The collision bound \(\le 1/m+1/p\) and the Markov step for \(m=n^2\) were checked | restore | high |
| V4-RM-E70 | `pb:triangleseigen` | `ch12-method.tex:389–396` | 1194–1210 | too advanced | Tools cite Volume 8 for adjacency eigenvalues | omit | medium |
| V4-RM-E71 | `pb:walks` | `ch12-method.tex:398–406` | 1212–1236 | too advanced, and one sentence is wrong | A parallel reading accepted the trace bound and rejected the identification of that bound with the expected number of closed 4-walks in \(G(n,\bar d/n)\): backtracking walks contribute on the order of \(n\bar d^2\). This audit did not re-derive the solution | omit. Do not restore the solution as written | medium |
| V4-RM-E72 | `pb:littlewoodofford` | `ch12-method.tex:408–415` | 1238–1256 | lost | Tools: LYM and Stirling, both Volume 1. Not line-checked | optional. The method chapter already has a second-moment example | medium |
| V4-RM-E73 | `pb:cubeiso` | `ch12-method.tex:417–420` | 1258–1275 | lost | Edge isoperimetry of the cube. Not line-checked | optional | medium |
| V4-RM-E74 | `pb:erdosselfridge` | `ch12-method.tex:422–430` | 1277–1298 | lost | A finite potential. The local lemma is already a theorem. Not line-checked | optional | medium |
| V4-RM-E75 | `pb:shearer` | `ch12-method.tex:432–444` | 1300–1327 | too advanced | Journey. Shearer and Loomis–Whitney | omit. Large | medium |
| V4-RM-E76 | `pb:sincpower` | `ch12-method.tex:446–456` | 1329–1349 | too advanced | Tools: Volume 5, Laplace’s method | omit | high on the tools |
| V4-RM-E77 | `pb:cantor` | `ch12-method.tex:458–468` | 1351–1387 | lost | Fourier transform of the Cantor law. The law itself is `ex:cantor`, and inversion is now a theorem. The transform exercise was not line-checked | omit. The distribution is already an exercise | medium |
| V4-RM-E78 | `pb:majoritystable` | `ch12-method.tex:470–483` | 1389–1425 | too advanced | Noise stability and a two-dimensional Gaussian limit | omit | medium |
| V4-RM-E79 | `pb:period` | `ch12-method.tex:485–501` | 1427–1465 | too advanced | Cosets and quotients | omit | medium |
| V4-RM-E80 | `pb:rollingdie` | `ch12-method.tex:503–518` | 1467–1511 | too advanced | Cube rotation group, Volume 3 in the tools line | omit | medium |
| V4-RM-E81 | `pb:gapdiam` | `ch12-method.tex:520–535` | 1513–1539 | too advanced | Spectral gap from the diameter | omit | medium |
| V4-RM-E82 | `pb:treewalk` | `ch12-method.tex:537–551` | 1541–1574 | too advanced | Free group, infinite 4-regular tree | omit | medium |
| V4-RM-E83 | `pb:commute` | `ch12-method.tex:553–567` | 1576–1609 | duplicate | See V4-RM-NET. Volume 12, `thm:commute` | omit | medium |
| V4-RM-E84 | `pb:foster` | `ch12-method.tex:569–580` | 1611–1637 | too advanced | See V4-RM-NET | omit | medium |
| V4-RM-E85 | `pb:rayleigh` | `ch12-method.tex:582–597` | 1639–1676 | too advanced | See V4-RM-NET. Journey | omit | medium |
| V4-RM-E86 | `pb:aldousbroder` | `ch12-method.tex:599–614` | 1678–1718 | too advanced | See V4-RM-NET. Journey | omit | medium |
| V4-RM-E87 | `pb:terras` | `ch12-method.tex:616–626` | 1720–1746 | lost | Collatz parities as a bijection on residue classes. Not the probability spine | omit | medium |
| V4-RM-E88 | `pb:everett` | `ch12-method.tex:628–638` | 1748–1769 | too advanced | Depends on `pb:terras` and natural density | omit | medium |
| V4-RM-E89 | `pb:coprimewalk` | `ch12-method.tex:640–651` | 1771–1810 | too advanced | Visible lattice points, Chinese remainder, \(\pi(t)=o(t)\) | omit | medium |
| V4-RM-E90 | `pb:range` | `ch12-method.tex:653–663` | 1812–1843 | lost | Range of the simple walk. Stirling is Volume 1. Not line-checked | optional | low |
| V4-RM-E91 | `pb:cyclecover` | `ch12-method.tex:665–676` | 1845–1868 | lost | Cover time of the cycle, via gambler’s ruin. Not line-checked | optional | medium |
| V4-RM-E92 | `pb:threegamblers` | `ch12-method.tex:678–690` | 1870–1890 | lost | Three players, optional stopping. Not line-checked | optional | medium |
| V4-RM-E93 | `pb:moran` | `ch12-method.tex:692–709` | 1892–1918 | lost | Moran model. Not line-checked | omit | medium |
| V4-RM-E94 | `pb:bernoullilaplace` | `ch12-method.tex:711–725` | 1920–1941 | duplicate | Two urns. Ehrenfest is already an exercise | omit | medium |
| V4-RM-E95 | `pb:binompowers` | `ch12-method.tex:727–734` | 1943–1964 | lost | Uses the local theorem, which is now in Chapter 6. The asymptotic was not re-derived | omit | medium |
| V4-RM-E96 | `pb:saw` | `ch12-method.tex:736–745` | 1966–1988 | lost | Self-avoiding walks. The connective-constant limit is a research neighbourhood even when the subadditive step is elementary | omit | medium |
| V4-RM-E97 | `pb:inspection` | `ch12-method.tex:747–759` | 1990–2012 | too advanced | Tools: Volume 6, prime-number theorem | omit | high on the tools |
| V4-RM-E98 | `extremal:ex:turaninduction` | `extremal.tex:472–475` | 569–577 | duplicate | Another proof of Turán, which is `thm:turan` | omit | medium |
| V4-RM-E99 | `extremal:ex:zarankiewicz` | `extremal.tex:477–480` | 579–584 | lost | An elementary zero-one matrix bound. Kővári–Sós–Turán is not a pinned theorem. Not line-checked | optional | medium |
| V4-RM-E100 | `extremal:ex:polarity` | `extremal.tex:482–484` | 586–591 | lost | Draws the graph of a deleted polarity theorem | omit with that theorem | medium |
| V4-RM-E101 | `extremal:ex:schurbound` | `extremal.tex:486–488` | 593–598 | lost | A factorial upper bound. General Ramsey is `thm:ramsey`. Not line-checked | omit | medium |
| V4-RM-E102 | `extremal:ex:r333lower` | `extremal.tex:490–494` | 600–607 | too advanced | The field with 16 elements | omit | high on the tools |
| V4-RM-E103 | `extremal:ex:schur2` | `extremal.tex:496–498` | 609–613 | rewritten | Old wording: the largest set that splits into two sum-free sets has size 4, and \(\{1,\ldots,5\}\) does not. Pinned `ex:schurtwo` says 5 is the smallest forced threshold and \(\{1,2,3,4\}\) has an avoiding colouring. Same fact, force-threshold convention | omit | high |
| V4-RM-E104 | `extremal:ex:fermatp` | `extremal.tex:500–503` | 615–621 | lost | Cubes modulo 13. Not the extremal spine | omit | medium |
| V4-RM-E105 | `extremal:ex:monoseq` | `extremal.tex:505–507` | 623–628 | duplicate | Infinite monotone subsequence. Volume 1 already has Erdős–Szekeres, and infinite Ramsey is not needed for that theorem | omit | medium |
| V4-RM-E106 | `extremal:ex:happyending` | `extremal.tex:509–513` | 630–636 | lost | Convex polygons from Ramsey. Not line-checked | omit | medium |
| V4-RM-E107 | `extremal:ex:ramseydirect` | `extremal.tex:515–518` | 638–645 | duplicate | Asks for a finite Ramsey proof. `thm:ramsey` is that proof | omit | medium |
| V4-RM-E108 | `extremal:ex:wlower` | `extremal.tex:520–522` | 647–652 | lost | The number of \(k\)-term progressions in \([N]\) is \(<N^2/(2(k-1))\). Each is monochromatic with probability \(2^{1-k}\). If \(N^2\le(k-1)2^k\), the expectation is \(<1\), so \(W(k,2)>\sqrt{k-1}\,2^{k/2}\). The second review checked these six lines. This reconciliation checked the same inequalities. Berlekamp’s finite-field bound is a citation | restore without the Berlekamp sentence | high on the first-moment bound |
| V4-RM-E109 | `extremal:ex:sunflowersharp` | `extremal.tex:524–526` | 654–659 | lost | The standard sunflower example. The theorem is `thm:sunflower`. Not line-checked | optional | medium |

Baseline blobs for the files in that table:

| File | Blob | Lines |
| --- | --- | --- |
| `ch01-counting.tex` | `bd794a128982027a57433910bd33941d9c0b433b` | 791 |
| `ch02-discrete.tex` | `665807bceea4c4dbb6fc00207d0996069ad3809f` | 867 |
| `ch03-generating.tex` | `3d6ef55db30c6dc6b00f1869e4c49bd196c9eb26` | 555 |
| `ch04-inequalities.tex` | `6d8d0b1ef04c6086540be2084d298ac16bf5a125` | 1050 |
| `ch05-continuous.tex` | `4040739625fdea6c7362a91056d9d8c910ac6239` | 953 |
| `ch06-clt.tex` | `4857b13299c0669754e40394cdac06ee82227b35` | 638 |
| `ch07-walks.tex` | `29d4b1353bbc971ca10e26c206e91c62d633710f` | 736 |
| `ch08-markov.tex` | `ebd3025748d20d64bc01fdd52cda1d323c330c28` | 1070 |
| `ch09-poisson.tex` | `3cdf114a9b8d86492058a10bf26974a70c7d6c90` | 535 |
| `ch10-martingales.tex` | `bfac7ec0ae9ab9f4a44e4f50a938856697cbab90` | 787 |
| `ch11-brownian.tex` | `0b9bd7ba42480caa651d2249d5fbd1d8e1f2505f` | 602 |
| `ch12-method.tex` | `eb9d6c27cf75d112d74a2848f19ae6e934034d61` | 2037 |
| `extremal.tex` | `c567158e2cae13d23f70b705b0fe1bc6938b4fc1` | 685 |
| `gilmer.tex` | `dd703c9be37b4ab380392e0cc8c7922fd3e35c35` | 106 |

Every one of the 109 has a hint. The hint environment sits in the same baseline file, between the exercise list and the solution list.

## Small restorations that need an owner decision

These are the items this reading would put back, each as a single exercise or a short section, after the pending Brownian correction on its own branch has landed or been set aside. None of them is authorised by this audit. Each one invalidates the page ledger of the chapter it touches, so it waits until the owner asks for it.

**Checked far enough to recommend:**

1. `pb:passone` (V4-RM-E36). Waiting to pass 1 has mean \(e\).
2. `pb:sicherman` and `pb:loaded` (V4-RM-E16, E17). The face expansion and the AM–GM bound were checked. Sicherman’s write-up should peel irreducible factors by polynomial division. It should not cite a theorem titled unique factorisation of \(\mathbb Q[X]\).
3. `pb:goodman` (V4-RM-E12). At least two monochromatic triangles in \(K_6\), and the random colouring matches the order of the bound.
4. `pb:samecycle` (V4-RM-E66). Cycle length through a fixed point is uniform.
5. `pb:hashing` (V4-RM-E69). Pairwise independence of \(ax+b\), with the collision bound checked.
6. `pb:stick` (V4-RM-E39). Broken stick, with the integral checked.
7. `ex:ballsbins` (a) and (b) (V4-RM-E23). The union bound and the maximum of \(\psi\) were checked. Drop Gonnet’s citation.
8. `ex:secretary` (a) and the \(1/e\) limit (V4-RM-E02). The optimality sentence stays out until it is proved.
9. `ex:mcmillan` (V4-RM-E26). Uniquely decodable codes obey Kraft’s inequality.
10. `pb:subsetsum` (a) and (b) (V4-RM-E18). Part (a) was enumerated for \(p=3\).
11. `extremal:ex:wlower` (V4-RM-E108). The first-moment bound was checked. Drop Berlekamp’s citation.
12. `thm:twosat` (V4-RM-2SAT). Expected \(n^2\) flips. Rewrite the last limit as a tail sum.

**Not on that list:**

- `pb:nouniform`, as written. Part (a) uses countable additivity, which pinned Chapter 1 does not prove. Part (c)’s density sentence is false at a block edge.
- `ex:knight`. The baseline solution is the hand sum \(2\cdot26+2\cdot38+4\cdot52=336\). The mean return time is not a pinned theorem.
- `ex:chromatic`, as written, because the solution cites \(\mathbb E\chi\sim n/(2\log_2 n)\) from Bollobás 1988, which is not a theorem of Volumes 1–4.
- `ex:likelihood`. The finite argument may be sound. The old labels `thm:supconv` and `cor:slln` were not matched to the pinned theorems, and the chapter does not need the exercise.
- `ex:sharp` (b). Chebyshev’s equality case is not `ex:markovsharp`. It stays off the list.
- `ex:twotests`, until the rates from baseline `ex:medical` (line 129) are written into the prompt.

None of the checked list is approved for restoration by this audit.

## Large blocks to leave out

- The abstract measure block V4-RM-MT.
- The Gilmer defect inequality V4-RM-GIL. Volume 15 has the theorem.
- The 33-problem tail of old Chapter 12, taken as a list. The finite method is already in Chapters 13 and 14 of the pinned book. The safe finite problems inside the list are the individual rows marked restore or optional, not the list.
- The network chain V4-RM-NET.
- Cap sets, Bonami’s inequality, \(p\)-adic binomial series, Borwein’s sinc integrals, prime-gap inspection, Collatz, Paley graphs, \(\mathrm{GL}_n\), and the Black–Scholes limit.
- Any addition whose purpose is to move a page count.

The 109 missing solutions are 2264 source lines. Restoring them all would be a large manuscript change. Restoring the checked list above is a handful of exercises and one section.

## Pending Brownian branch

`origin/cursor/v4r2-ch12-brownian-df0c` at `3bb6331ef89bd9b74a57a1ad2640a79ffc9a13d3` is not an ancestor of pinned `main`. Four commits on that branch are absent from `main`. They edit `volume4-chance/chapters/ch11-brownian.tex` and a source pin test. The diff replaces an appeal to Borel–Cantelli for Gaussian thresholds with a rectangle cover that prices linear images of the coordinate normals, and it rewrites the reflection-window estimate in the same language. It does not restore any `pb:*` exercise, Gilmer, or the measure block.

This audit judges the pinned file, not that branch. The pinned Brownian proofs are the text before those rectangle-cover repairs. A restoration that touches Chapter 12 (printed Brownian motion) should wait until that branch is merged or dropped, so two edits do not collide. This audit does not merge, rebase, or push to that branch, and it does not touch the scored-read branches `cursor/v4-independent-scored-read-7e4d`, `cursor/v4r2-*`, or the Volume 1–3 scored-read branches.

## Page evidence

Ideal length, owner clarification of 6 November 2026, recorded in `docs/plan/book-04.md`: between 300 and 600 pages, 600 a maximum, 300 not a minimum. A page count is a measurement. This audit does not add material to approach 300.

No build log in the repository measures baseline `5c4840cc`. This audit therefore states no page count for the pre-rewrite book. Marketing text in the old `kdp.md` is not a measurement.

The latest native measurement found for a descendant of the rewrite, and an ancestor of the pin, is in `docs/review/volume4-phase3-production-qa-2026-11-10.md`: book tree `cfe5d152a8aa2bc74b7b96f5824369a86e175b92`, identical to `main` `3cc07e8673490b9922db9d9d29fee0551e2d8a12`, native run 42783238907. Reading PDF 290 pages, print interior 289 pages, each print page 513×738 pt. That SHA is an ancestor of `a2cfdd30`. The later diff is the 311-line source change named above, including a bibliography and an index, so 289 is not the page count of the pin. This audit did not build the pin.

Earlier counts in the issue log (155, 193–227, 259, and others) are measurements of other SHAs. They are not the baseline and not the pin.

## Checks that are arithmetic, not proofs

| Check | Result |
| --- | --- |
| Gilmer constant \(1-1/c=(1-\ln 2)/2\) | Holds for \(c=2/(1+\ln 2)\) |
| Sicherman factor \(x(1+x)(1+x+x^2)\) | Expands to faces \(1,2,2,3,3,4\) |
| Loaded-dice AM–GM | \(2/(2n-1)>1/(2n-1)\) |
| Subset sums modulo 3 | Four of the eight subsets, matching \((8-2)/3+2=4\) |
| Subset-sum formula at \(p=5\) | \((\binom{10}{5}-2)/5+2=52\), arithmetic only |
| Waiting time past 1 | \(\mathbb E[N^2]=3e\), variance \(3e-e^2\approx 0.7658\) |
| Goodman at \(n=6\) | Lower bound 2 |
| Knight graph | 168 edges; corner return 168; centre return 42 |
| Second medical test | \(0.009801/0.012276\approx 0.798\) |
| Broken-stick integral | \(\int_0^1 2t(1-t)^{n-1}\,dt=2/(n(n+1))\) |
| Hash collision bound | \(\le 1/m+1/p\), and Markov gives the stated success probability when \(m=n^2\) |
| Same-cycle count | \((n-1)!/n!=1/n\), and the hockey-stick ratio is \(1/k\) |
| 2-SAT drift | \(2x(1-2\theta)\le 0\) for \(\theta\ge 1/2\) |
| Chernoff lower-tail exponent | Reproduces the displayed bound; the \(\delta^2/3\) calculus was not re-derived |

## Plain-English conclusion

The cuts are justified in some places and not in others.

The large cuts are justified. The old continuous chapter proved monotone convergence, Fatou, and dominated convergence only after admitting Lebesgue measure and Fubini from Volume 7. The new chapter proves the continuous theorems it uses and says they are narrower. Putting the abstract theory back would either lean on Volume 7 again or build measure theory inside a book that has refused to do that. Gilmer’s constant is a real theorem, and the arithmetic of the constant is right, but the hard inequality belongs with Volume 15, which already states it. The finite probabilistic method was not thrown away: Ramsey by deletion, the local lemma, the second moment, and random graphs are in the pinned book. The long list of workshop problems at the back of the old method chapter is mostly later mathematics, group theory, or a network chapter that Volume 12 already owns. “Nothing else cites the label” was the rewrite’s stated reason and is not enough. The reasons that do justify those omissions are the prerequisites, the duplication, and proofs that do not close inside Volumes 1–4.

The small cuts are not uniformly justified. Sicherman’s dice, with the factorisation wording above, a loaded die that cannot be uniform, the wait to pass 1, Goodman’s triangles, a uniform cycle length, universal hashing, the broken stick, balls in bins including the calculus in part (b), the secretary’s \(1/e\), McMillan’s inequality, the six-line van der Waerden lower bound, and the two-satisfiability walk are finite, they fit the chapters that remain, and the algebra named in the owner list was checked. They were cut because they were not citation interfaces. That is a weak reason for a book whose exercises are part of the teaching. They should come back only as individual exercises, after the owner says so, and not as a program to add pages. The uniform-integer solution does not belong on that list: its part (a) uses countable additivity, which this volume does not prove.

Several famous exercises were not lost. The medical doubling of a stake, unfair ruin, the riffle model, pattern waits, the Beta–Gamma identity, and the general Pólya urn live in the pinned Volume 4 or in a later volume under a new label. The longest-run exercise was deliberately weakened from almost sure to in probability, and the new statement says so.

## Corrections after the parallel readings

Four readings of the baseline solutions were run in this same audit session, after the first draft of this note. They are not the distinct second review, and they are not an independent acceptance. They did not edit the tree. The reconciliation section below is the later word on `pb:nouniform` and `ex:knight`. Where a reading only prefers a different teaching weight, the first recommendation stands. Where it found a false sentence, a missing hypothesis, or an overstated relocation, this section changes the row.

- `pb:nouniform` (c), as above. Consecutive integers \(3\) and \(4\) are both in \(B\).
- `ex:betagamma`, as above. Volume 7 does not prove the independence of the sum and the ratio.
- `ex:knight`, as above. `ch08-markov.tex:221` stops at reversibility for the degree weights.
- `ex:onestep` at current `ch11-brownian.tex:363–365` asks only for \(\mathbb E[B_t^2]=t\). The baseline exercise of that label, lines 479–483, was a one-period call. Put–call parity remains `ex:putcall`. The old call exercise is not restored.
- `pb:walks`, as above. One identification in the solution does not survive backtracking.
- `ex:sharp`. Current `ex:markovsharp` is the one-sided equality. The two-sided example, mass \(\sigma^2/(2a^2)\) at \(\pm a\), is not in that exercise. It is a short optional addition, not one of the checked restorations.
- `ex:signs`. A parallel reading found the almost-sure convergence for \(\alpha>1/2\), and the variance \(\sum 1/n^2\), proved from \(L^2\), and found the divergence for \(\alpha\le 1/2\) asserted by the three-series theorem. The convergent case is already the paragraph after `thm:L2conv`. Leave the exercise out.
- `pb:lcs`. The same reading found superadditivity and the union bound proved, and found the existence of \(\lim \mathbb E[L_n]/n\) cited to Fekete’s lemma in `pb:saw` rather than proved. Do not restore it as written. An enumeration \(\sum L_8=358424\) was reported; this audit did not repeat that count.
- Volume 15, `conjectures-ch08-geometric.tex:136`, says Volume 4, Appendix B, proves that the happy-ending function \(f(n)\) is finite by Ramsey’s theorem. Current `thm:ramsey` colours pairs only. The baseline exercise `extremal:ex:happyending` used \(k\)-uniform Ramsey, and that theorem is gone. This audit does not edit Volume 15. The citation is a later repair, or a restoration of a finiteness proof that the appendix actually contains. Volume 15 then proves its own cup-and-cap bound. That stronger bound does not make the citation true.
- The same readings would also restore `pb:erdosselfridge`, `pb:laplace` for a needle no longer than the tile, `pb:carries`, `pb:dicemod`, and `pb:gilbreath`, and would move `pb:range` and `pb:cyclecover` to the walk chapter and `pb:threegamblers` to the martingale chapter. Those solutions were not re-derived in the first pass. They stay off the checked list. The independent reading can accept or reject them.
- A polar-coordinate estimate in the current Box–Muller argument was reported as unfinished. That is a defect in the pinned chapter, not a removed item, and it is not adopted here as a checked gap.

## Reconciliation with the distinct second review

The distinct review is pull request #191, head `a76e24a7ba0b9f7f917c83e28f508bd1e98f03b5`, file `docs/review/volume4-removed-material-audit-second-review-2026-11-11.md`. It read audit head `791d35f6`. This section answers it from the later audit head `6dc3c31d` and from the table cells edited with this commit. `origin/main` was fetched again and is still `a2cfdd30a0f09eabcb932852c76537c8af592bdb`. The baseline pin `5c4840ccdbae22abfa8a28d01b8c5d1ab16355e6` is unchanged. This reconciliation is not an independent acceptance, and it does not restore any exercise.

| Second-review finding | What this audit does |
| --- | --- |
| `pb:nouniform` (a) uses countable additivity. Pinned Chapter 1, line 43, says that tool is not proved. | Accepted. The earlier “restore (a) and (b)” is withdrawn. The row is now omit as written. Part (b), finite additivity of density, is ordinary counting and is not promoted to its own restoration. |
| Part (c)’s block proportions, about \(2/3\) and \(1/3\), hence about \(1/3\) and \(1/6\) for the even subset, match the description. | Recorded. Those proportions do not repair part (a), and they do not repair the false consecutive-integer sentence. |
| The knight count is the hand sum \(2\cdot26+2\cdot38+4\cdot52=336\), not a program, and \(1/\pi(x)\) is not a pinned theorem. | Accepted. The table now quotes that hand sum. The program count in an earlier draft of this audit is withdrawn as a description of the solution. The row stays omit. |
| `ex:sharp` (b), Chebyshev’s equality at a given variance, is not `ex:markovsharp`. | Accepted as a classification. The row is now “partly rewritten”. Part (b) is lost. It is not added to the owner list. |
| `extremal:ex:wlower` checks by the first moment. Drop Berlekamp. | Accepted. The six-line inequalities were checked again in this reconciliation. The row is now a restoration candidate without the Berlekamp sentence. |
| `ex:ballsbins` (b): \(\psi'(u)=(\ln 3-\ln u)/u^2\), maximum \(1/3\) at \(u=3\). Drop Gonnet. | Accepted. The derivative was computed again here. The row now includes (b) and excludes the Gonnet citation. |
| Sicherman should say “peel irreducible factors”, not “by the unique-factorisation theorem”. | Accepted as a wording limit on a candidate that was already on the list. The face expansion is unchanged. |
| `ex:twotests` stays open until the rates are in the prompt. They live in baseline `ex:medical`, from line 129. | Already the repair condition. The line of the example is now in the row. |
| `ex:chromatic` imports Bollobás’s asymptotic. `ex:likelihood` cites old labels that were not matched. | Already off the checked list. The Bollobás citation and the old labels are now named. |
| Large omissions of the measure engine, the Gilmer defect, the network chain, and the workshop list taken whole. | Unchanged. Individual “omit” rows that were classified from a tools line remain classifications, not certificates that no elementary core exists. `pb:lcs` stays unresolved. |
| Further restores proposed only by the parallel readings in this session, including `pb:erdosselfridge`, the tiled-floor needle, carries, dice modulo \(m\), and Gilbreath. | Not adopted. The second review did not put them on its owner list, and this audit did not re-derive them. |

The second review’s arithmetic on the first-pass inventory, 174 triples, 107 pinned exercises, 65 surviving labels, and 109 absent labels, is unchanged by these cell edits.

## Reconciled recommendation counts

Counted from the recommendation column of the 109-row table after the edits in this commit. A cell is counted by its first word.

| Recommendation as the cell now starts | Count |
| --- | ---: |
| restore | 12 |
| repair+restore | 1 |
| optional | 19 |
| omit | 77 |

Those four numbers add to 109. The class column has 9 rows that start with “rewritten”, including the explicit weakening of the longest run, and one row, `ex:sharp`, that starts with “partly rewritten”. The first-pass class total of 10 rewritten rows was those 9 plus the old classification of `ex:sharp`. Fifty-seven rows still start with “lost”, 33 with “too advanced”, 7 with “duplicate”, and 2 with a relocation. `pb:nouniform` moved from the restore column to the omit column, which is why the omit count is 77 rather than the first-pass 74. `ex:likelihood` is one of the 19 optional rows. `ex:ballsbins` and `extremal:ex:wlower` remain restores, with the Gonnet and Berlekamp citations kept out of any future write-up. These counts are not an acceptance. They are the table.

## What this audit did not do

- It did not restore, rewrite, or delete any exercise.
- It did not edit Volumes 1–3 or 5–15, shared layout, covers, or KDP files.
- It did not build the pinned Volume 4, and it did not build the baseline.
- It did not re-prove every one of the 109 solutions. Rows marked “Tools” or “not line-checked” are classifications, not certificates. The independent reading still to be commissioned should start with those rows and with `conjectures:lem:hxy`.
- It did not treat writer self-review, the old-to-new plan, or this document as an independent second review.
- It did not inspect figures. That review was deferred by the owner until after this audit.

## Unresolved

- `pb:nouniform`: part (a) is not a Volume 1–4 proof, because it uses countable additivity. Part (c)’s density sentence is false. The block proportions reported by the second review were not recomputed here.
- `ex:ballsbins` (b), `ex:chromatic`, `extremal:ex:wlower`, `ex:likelihood`, and `pb:littlewoodofford`: the class is plausible and the solution was not re-proved.
- `pb:lcs` and `pb:leastqnr` (b): the solutions may contain a heuristic presented as a proof. They stay out either way.
- `conjectures:lem:hxy`: the defect estimate was read and not re-derived.
- The Chernoff \(\delta^2/3\) calculus was not re-derived.
- The page count of `a2cfdd30` is unknown. The 289-page print interior belongs to `3cc07e86`.
- Whether `ex:knight`’s old write-up uses the stationary formula that the pinned chapter proves, or a different count. The number 168 is the edge count.
