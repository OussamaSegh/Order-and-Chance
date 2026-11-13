# Second review of the Volume 5, 6 and 7 re-read fixes, 13 November 2026

Independent reading of the diffs, after the writer pass. The issue logs are the three re-read reports on the draft branches `cursor/volume5-reread-7179`, `cursor/volume6-reread-e30d` and `cursor/volume7-reread-daf4`. This note does not change a manuscript. Two sentences in the first Volume 7 diff were rejected; they were rewritten before the verdicts below. The verdicts are on the repaired heads.

| Pull request | Head reviewed |
| --- | --- |
| [#223](https://github.com/OussamaSegh/Order-and-Chance/pull/223) | `69a55a7655b2f348725ff6af7b2b56512a704244` |
| [#224](https://github.com/OussamaSegh/Order-and-Chance/pull/224) | `635901f48158de1b29bd4b63ebac3e35fa1e348f` |
| [#225](https://github.com/OussamaSegh/Order-and-Chance/pull/225) | `a7dbf71d7472c2b2fc3f2710b7ccb8e54c511dcb` |
| [#226](https://github.com/OussamaSegh/Order-and-Chance/pull/226) | `706cb4f01f48cba5f8c50dd246e18ec7d81fba5e` |

Numbering inside Volumes 5, 6 and 7 is unchanged. No figure geometry moved. The paperback ISBN was not invented.

## What the second reading rejected

**V7-13, first repair.** The triangle paragraph said that a set of diameter less than the side \(2^{-k}\) meets at most two stage-\(k\) triangles, because non-touching triangles are at least a side apart. That separation is false. Enumerating the gasket through stage 5, the least positive distance is the altitude \(\frac{\sqrt3}{2}2^{-k}\), about \(0.866\) of the side, and a ball of the Jung radius for diameter equal to the side meets four triangles. The repaired paragraph uses the altitude as the threshold, keeps the count at two below that threshold, and gets \(\mu(U)\le 2(4/\sqrt3)^s(\operatorname{diam} U)^s\).

**V7-40, first repair.** The side-graph paragraph said that returning to \(R_{e_1}^-\) meant every node had already been visited. The walk back to that side has used one side of every edge and one sector at every vertex, which is half the nodes, and then continues. The repaired paragraph says so, and keeps the unused-sector reason for the second cycle.

## Issue log

| ID | Severity | Location of the fix | Fix | Verdict | Doubt |
| --- | --- | --- | --- | --- | --- |
| V5-1 | major | `volume14-primes/chapters/ch14-critical.tex:19` | Corollary 10.10 replaced by Corollary 8.10. The formula was already the theta law. | Accept | None. The index of Volume 5 sends Corollary 8.10 to `cor:theta` and Theorem 8.9 to Poisson. |
| V5-2 | minor | `volume15-order-and-chance/chapters/conjectures-ch01-born.tex:229` | Theorem 6.11 replaced by Theorem 4.11. | Accept | The file is still not in Volume 15’s `main.tex`. The citation is right if it is ever printed. |
| V5-3 | minor | `volume15-order-and-chance/chapters/ra-largemoduli.tex:24` | The reminder states the unitary convention of Theorem 8.6 and names \(t=2\pi\xi\) as the change to the angular-frequency formula the proof uses. | Accept | The estimates were not rewritten. They only need a rapidly decreasing \(F\), which both normalisations supply. |
| V5-4 | minor | `volume5-calculation/chapters/preface.tex` | The preface now names Tonelli, the convex volume, Fulton–Harris 3.12, Mertens’s third theorem, and the quoted prime-number comparison. | Accept | None. |
| V5-5 | minor | `volume5-calculation/chapters/ch03-series.tex:229` | Called a 2026 Zenodo preprint, named the AFP entry, and named the `holds` oracle from seventy-two interval approximations. | Accept | Checked against the AFP abstract of 26 October 2026. Not a theorem of this volume. |
| V5-6 | minor | `volume5-calculation/chapters/ch06-fourier.tex` | Independence is Volume 4, Chapter 2. The return formula stays in Chapter 8. | Accept | None. |
| V5-7 | minor | `volume5-calculation/chapters/ch05-gamma.tex`, exercise `pb:ncycles` | The exterior-power sentence is marked quoted, and the preface lists it. | Accept | The representation fact itself was not re-proved. It is quoted, as the log asked. |
| V5-8 | minor | `volume11-randomness/chapters/ch09-martingales.tex` | No new edit. On current `main` the sentence already cites Section 5.4. | Accept | The defect in the re-read was on `f10e4c99`, before the Volume 11 rewrite. Section 5.4 is the Beta integral. |
| V5-9 | minor | `volume5-calculation/chapters/ch12-agm.tex` tools line | Split into Volume 1, Proposition 2.3, Volume 4, Chapter 1, and Volume 4, Chapter 2. | Accept | Proposition 2.3 is `prop:derang`: the shared counter puts inclusion–exclusion between the two propositions of that chapter. |
| V5-10 | minor | `volume5-calculation/chapters/ch07-fft.tex` | The sum below \(N=4^k\) is \(\frac23 N^{\log 3/\log 4}\). The power \(3^k\) is the size of the order. | Accept | The solution had already reached \(2\cdot 3^{k-1}\). |
| V5-11 | minor | `volume5-calculation/chapters/ch09-complex.tex` | The arc integral tends to 0 as \(R\to\infty\), for each \(n\ge 2\). | Accept | None. |
| V5-12 | minor | copyright page | Left as “to be assigned.” | Unresolved | An ISBN was not invented. This needs Seg. |
| V5-13 | minor | `volume5-calculation/chapters/ch06-fourier.tex`, exercise `pb:siegel` | \(e(t)=e^{2\pi it}\) at the first use. | Accept | Later uses in Chapter 13 sit after this definition. |
| V5-14 | minor | `volume5-calculation/chapters/ch05-gamma.tex`, the log-convexity lemma | Both sides are non-negative; the inequality is integrated on compact pieces and kept in the limit. | Accept | None. The identities that use the lemma were not re-opened. |
| V5-15 | minor | `volume5-calculation/chapters/ch02-generating.tex`, `pb:diehit` | \(\rho_0\approx 0.73025\), and the bound asks for \(\rho>\rho_0\). | Accept | Recomputed: the next root has modulus \(1.369394105\ldots\), and \(\rho_0=0.73024996\ldots\). |
| V5-16 | minor | `volume5-calculation/chapters/ch03-series.tex`, solution of `ex:eirrational` | The integer lies strictly between \(-1\) and \(0\). | Accept | The sign choice that makes \(ar_n+cs_n>0\) was already in the write-up. |
| V5-17 | minor | `volume5-calculation/chapters/ch02-generating.tex`, merge sort | The cost satisfies the inequality. The equality is named as the model being solved. | Accept | None. |
| V5-18 | minor | same file, derangements | The alternating tail after \(n\) is strictly smaller than \(1/(n+1)!\), so the distance to \(n!/e\) is less than \(1/2\). | Accept | The terms \(1/k!\) decrease strictly, so the remainder is strictly smaller than the first omitted term. |
| V5-19 | minor | same file, `pb:parts123` | Perimeter \(2m\) is restricted to \(m\ge 3\), in the exercise and in the solution. | Accept | None. |
| V5-20 | minor | `volume5-calculation/chapters/ch11-asymptotics.tex:201` | The partial sum is \(2.928968253927\ldots\); \(H_{10}=7381/2520\) is larger by \(4.1\cdot 10^{-11}\). | Accept | Recomputed. The difference is \(4.0929\cdot 10^{-11}\). |
| V6-1 | major | `ch02-averages.tex` and `ch12-modular.tex`; also Volume 13 in #226 | The letter \(\tau\) is kept. Chapter 2 warns that Chapter 12 uses it for another function. Chapter 12 says the coefficient is Ramanujan’s, not the divisor function and not the half-plane variable. Volume 13 says the same at the preface, the Weil remark, and the trivial-zero solution, and keeps \(d(n)\) for the divisor count. | Accept | Volumes 14 and 15 use \(\tau(n)\) as the divisor function only. Renaming would have touched every formula. |
| V6-2 | major | `volume8-analysis/chapters/ch09-expanders.tex:316` | The citation is Theorem 7.10, and the error is \(\psi(x)=x+O(\sqrt x\log^2 x)\). | Accept | Chapter 5 still says, correctly, that its own proof gives no error term. The shape \(O(\sqrt x\log x)\) for \(\pi(x)\) is not what Theorem 7.10 proves, and it is no longer what the expander sentence claims. |
| V6-3 | minor | `blurb.tex` and `kdp.md` | The lead up to \(26861\) is what is proved. The figure \(99.59\%\) is named as conditional. Numbered theorems are proved; the quoted remarks are named. | Accept | The back-cover measure is fixed. If the blurb overflows, the cover build fails and the sentence has to be shortened. That is a build check, not a mathematical doubt. |
| V6-4 | minor | `volume6-crossroads/chapters/index.tex` | Added Theorem 12.2, Theorem 12.9, Corollary 12.11, Exercise 5.1 (the logarithmic integral), Theorem 1.5 (the Meissel–Mertens constant), and Section 3.5 (the Siegel zero). The headnote says the list is selective. | Accept | The numbers were counted from the shared counter: `thm:fundamental` is the second numbered statement of Chapter 12, `thm:dimension` the ninth, `cor:delta` the eleventh, `ex:li` the first exercise of Chapter 5, `thm:mertens2` the fifth statement of Chapter 1, and the non-vanishing section is the fifth section of Chapter 3. |
| V6-5 | minor | `ch12-modular.tex` closing | Volume 14 is described as beginning with a stronger zero-free input, Bombieri–Vinogradov, and exponential sums over primes. The zero-free region, Selberg’s sieve, and the Weyl sums are named as theorems of this volume. | Accept | Matches Volume 14’s preface. |
| V6-6 | minor | `ch09-erdoskac.tex`, Lemma 9.6 | The box says that \(m_k\) are the Gaussian moments defined above. | Accept | The proof already used \(m_{2j}/(2j)! = 1/(2^j j!)\). |
| V6-7 | minor | `ch01-mertens.tex` | About \(12.3\%\), and the comparison with \(1/\log n\) waits for Chapter 5. | Accept | \(2e^{-\gamma}-1=0.12292\ldots\). |
| V6-8 | minor | exercise `pb:poissoncycles` | Marked \(\star\star\star\). | Accept | The solution was not weakened. |
| V6-9 | minor | `ch02-averages.tex` after Theorem `thm:tau3` | The Piltz error is marked quoted. The exercise still proves the main term with the weaker error. | Accept | None. |
| V6-10 | minor | `ch04-dirichlet.tex` | The square term is about \(\sqrt x/\log x\). The conditional error is \(O(\sqrt x\log x)\). The lead is a bias of logarithmic density. | Accept | The count up to \(60\,000\) is untouched. |
| V6-11 | major | `ch10-random.tex`, the Maier section and the solution of `ex:shortmodel` | The almost-sure asymptotic is stated for \(\lambda>2\). For \(1<\lambda<2\) a long gap is empty while the mean tends to infinity. For \(\lambda=2\) a gap of relative length \(1-\varepsilon\) leaves a Bernoulli sum of mean about \(\varepsilon\log q\), and the exponential bound from the same solution keeps that count \(O(\varepsilon\log q)\). | Accept | The bound in the exercise is proved for any finite sum of the model’s independent Bernoulli variables; it does not use \(\lambda>2\) until the comparison of the mean with \(\log N\). Along the dyadic gaps in the proof of Theorem 10.4 the probabilities sum, so the liminf is 0 almost surely. Maier’s quoted inequalities are unchanged. |
| V6-12 | minor | `ch11-sums.tex`, Kusmin–Landau | \(|\cot u-\cot v|\le 2\cot\pi\delta\) on \([\delta,1-\delta]\), so the factor \(\frac12\) still yields \(\cot\pi\delta\). | Accept | The rest of the estimate is the old one, and it is the right size. |
| V6-13 | minor | `ch10-random.tex` opening | “The singular series averages to \(1\).” | Accept | Theorem 10.7 is that average. \(C_2\) is a different number. |
| V6-14 | minor | `ch12-modular.tex`, solution of `pb:pminusone` | \(\varphi(d)/\sqrt d\) is multiplicative, and each local factor is at least \(1/\sqrt 2\). | Accept | For the prime \(2\), the factor at \(k=1\) is exactly \(1/\sqrt 2\). For an odd prime it is larger. |
| V6-15 | minor | same file, Rankin solution | \(19.4\) replaced by \(19.5\). | Accept | \(1.26\cdot 10^{11}/6.47\cdot 10^9=19.474\ldots\). |
| V7-1 | minor | `ch02-metric.tex`, part (f) of `thm:exp` | The statement says the length waits for Theorem `thm:riemanncont`. | Accept | Part (f) is still part (f). |
| V7-2 | minor | `ch12-harder.tex`, Problem `pb:borelbernstein`(a) | The problem now asks for the endpoints and the length. | Accept | Volume 11 no longer cites the problem. `ch10-ergodic.tex` derives the same length from Volume 2, Proposition 9.1. |
| V7-3 | minor | Jarník tools line | Prokhorov removed. | Accept | None. |
| V7-4 | minor | `ch05-baire.tex` | “Length zero” replaced by “contains no interval,” with pointers to Chapters 4 and 7. | Accept | None. |
| V7-5 | minor | `ch09-lp.tex`, Exercise `ex:approxid`(b) | The norm limit is for \(1\le p<\infty\), with the counter-example at \(p=\infty\). | Accept | \(G_t\) is the \(N(0,2t)\) density, and \(\|f*G_t-f\|_\infty=\frac12\) for \(f=\mathbf 1_{[0,\infty)}\). |
| V7-6 | minor | `ch09-lp.tex` after Jensen | The comparison is the Hölder inclusion. Jensen on \(|f|^p+\varepsilon\) is named as another route, not used as the proof. | Accept | None. |
| V7-7 | minor | caption of Figure 8.2 | The tail equals \(1/\sqrt n\) when the spike exceeds \(M\), and equals \(0\) otherwise. | Accept | The drawing was not touched. |
| V7-8 | minor | typewriter solution | No zero only at \(x=1/2\) when \(k=1\). | Accept | None. |
| V7-9 | minor | Gaussian characteristic-function solution | Sine is odd and cosine is even, so the integral is \(2I(t)\). | Accept | None. |
| V7-10 | minor | caption of Figure 4.2 | The branch is \((0,1,1,0,\ldots)\). | Accept | The thick coral intervals in `figures/ch04-cantortree.tex` go left, then right, then right, then left. The paths were not moved. |
| V7-11 | minor | header of Theorem 4.11 | Dated 1935. | Accept | The paragraph above already separated 1930 from 1935. |
| V7-12 | minor | Hahn decomposition | The supremum is finite because a union of positive sets with values larger than every integer would be a positive set of infinite measure. The cutting argument is written before it is used. | Accept | \(\nu(P_n)=\nu(R_n)+\nu(P_n\setminus R_n)\) uses that the union is positive, which the new sentence proves. |
| V7-13 | minor | triangle half of Exercise 12.2 | See the rejection above. The repaired bound uses the altitude. | Accept | The least gap was enumerated through stage 5, not proved as a separate lemma. The reason in the paragraph is the construction: vertices are born in pairs, and the first positive distance is that altitude. |
| V7-39 | minor | `jordan-polygon.tex` | \(R_e\cap P\) is the relative interior of \(e'\). | Accept | The later argument uses the open half-rectangles, not the endpoints. |
| V7-40 | minor | same file, after Lemma 6.3 | See the rejection above. The repaired paragraph matches the two cases and adds the unused sector. | Accept | None, on the repaired sentence. |
| V7-41 | minor | solution for the continued fraction of \(e\) | The digit bound is for \(m\ge 1\). | Accept | \(a_0=2>(2\cdot 0+2)/3\). The estimate uses \(a_{n+1}\). |
| V7-42 | minor | Liouville solution | The geometric comparison is strict, so \(x-p/q<q^{-n}\). | Accept | At \(n=1\), \(q=3\), the non-strict last step would have been equality. The omitted non-factorial exponents make it strict. |
| V7-43 | minor | solution of Problem 13.1(c) | Empty set of exceptions gives \(c(x)=1\). | Accept | None. |
| V7-44 | minor | Lévy’s constant | \(1.1865\ldots\). | Accept | \(\pi^2/(12\log 2)=1.18656911\ldots\). Quoted and unused. |
| V7-45 | minor | opening of Chapter 2 | A fixed ratio \(k<1\) on a complete space. | Accept | The think-prompt is still the counter-example \(x+1/x\). The numbered theorem already asks for \(k<1\). |
| V7-46 | minor | same opening | Newton’s method converges once the map is a contraction. | Accept | None. |
| V7-47 | minor | proof of `thm:exp`(d) | The cosine terms decrease from the \(t^4/24\) term, since the ratio is at most \(4/(5\cdot 6)<1\) for \(k\ge 2\). The tail is negative, so \(\cos 2\le -1/3\). | Accept | The sine bound on \((0,2]\) was already the right alternating estimate and was left as it stood. |
| V7-48 | minor | completion | Uniqueness is stated for an isometry. | Accept | The isometric bijection is still the extension constructed in the previous sentence. |
| V7-49 | minor | opening of Chapter 3 | Hausdorff’s 1914 axioms were neighbourhood axioms and included separation. | Accept | The separation section of the chapter already said this. The two passages now agree. |

## Extra mismatches

No further wrong citation of Corollary 10.10, of Theorem 6.11 for the Dirichlet integral, or of Chapter 5 for an error term under the Riemann hypothesis, turned up in a search of the fifteen volumes. The Parseval citations in Volumes 11 and 12 still say Theorem 6.11, which is Parseval. The prime-number citations of Volume 6, Chapter 5, that do not claim an error term were left alone.

V5-8 and the Volume 11 half of V7-2 were already in a different state on `main` than in the re-reads, because Volumes 11 and 12 were rewritten after `f10e4c99`. Both are recorded above rather than edited again.

## Unresolved

V5-12. The paperback ISBN on the Volume 5 copyright page is still “to be assigned.” No number was supplied, and none was invented.
