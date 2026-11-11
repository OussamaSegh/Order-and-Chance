# Second review of the Volume 4 restorations

**Reviewer.** Independent second reading by cloud agent `bc-114da047-b320-5bb0-b0d1-2f6495477a25`. The restoration was written by a different session, `bc-323d34bf`. This file does not edit that branch. Nothing here is a merge, and nothing is restored by this review.

**Head reviewed.** Pull request [#192](https://github.com/OussamaSegh/Order-and-Chance/pull/192). The current verdict is the recheck below, at live head `82a3f104ed9696ff80df585e16ba1d1b904e29cb`. The REQUEST CHANGES section is the record of head `ec6e71da0c9f3c2a78246b7bb35078296c512f9f`.

**Verdict.** APPROVE at `82a3f104`. The Goodman denominator is now \(8\).

## Recheck — head `82a3f104`

One commit after `ec6e71da`: `82a3f104ed9696ff80df585e16ba1d1b904e29cb`, “Correct the Goodman denominator in part (b).” Two files change. In `ch02-discrete.tex` the displayed chain is now
\[
\binom{n}{3}-\frac{n(n-1)^2}{8}=\frac{n(n-1)(n-5)}{24}=\frac14\binom{n}{3}-\frac{n(n-1)}{8}.
\]
Both equalities hold. For \(n=6\), each side is \(1.25\): \(\frac14\binom{6}{3}=5\) and \(6\cdot5/8=3.75\). The floor sentence and the limit \(1/4\) are unchanged. The source pin is the new git blob `e37bf3057f41100109c0a323e4c75c585c56368f`, and the comment says it is not an independent sign-off. No other exercise, theorem, caption, or diagram text moved. V4-REST-01 is closed. The approvals in the section below stand.

## First reading — head `ec6e71da`, historical

That head was a merge. The first parent was `25f83e763d8949d0d3d8781c82b0762ad6295011`. The second parent was `76b990aa7ee166231b9bc29c42172813aaaca97d`. The manuscript commit of the restorations is `6b0042017a67eda3735cb91af739717d341e3331`. The verdict at that head was REQUEST CHANGES, for the coefficient recorded as V4-REST-01.

## Scope

The chapters gain the twelve exercises named in the audit's owner list, the repaired `ex:twotests`, and `thm:twosat` with `cor:twosat`. No row for a uniform integer, a knight's tour, the chromatic number, the likelihood ratio, Gilmer's inequality, or the measure-theoretic integral was added. The Brownian file at this head is blob `26e4400c45d83e53a9e415cd24952eccbf0d26dc`, the same blob approved on #180. The merge inserted the unnumbered dyadic lemma into Chapter 1 and left the new exercises where they were. No caption, font, or diagram text in the restoration diff was changed.

Old exercise labels are a prefix of the new list in every chapter. The new labels are appended, immediately before the hints:

| Chapter | Appended labels | Printed numbers |
| --- | --- | --- |
| 1 | `ex:twotests`, `ex:secretary` | 1.9, 1.10 |
| 2 | `pb:goodman`, `pb:samecycle` | 2.9, 2.10 |
| 3 | `pb:sicherman`, `pb:loaded`, `pb:subsetsum` | 3.9, 3.10, 3.11 |
| 4 | `ex:ballsbins` | 4.7 |
| 5 | `pb:passone`, `pb:stick` | 5.10, 5.11 |
| 7 | `ex:mcmillan` | 7.7 |
| 13 | `pb:hashing` | 13.7 |
| Appendix B | `ex:wlower` | B.6 |

References inside the new text use labels, not a shifted number. Walks is Chapter 8: the preface is unnumbered, and Random Walks is the eighth `\chapter`. Theorem, proposition, lemma, corollary, definition, and example share one counter. Nine of those environments precede Papadimitriou's theorem, so it is Theorem 8.10. The repetition corollary is the next one, Corollary 8.11. Nothing after that corollary uses the shared counter, so no earlier number in the chapter moves.

## Numbers checked on the page

| Claim | Check |
| --- | --- |
| Both tests positive, posterior \(99/124\) | \(9801/12276=99/124\), after dividing by \(99\). The two paths are \(9801/1000000\) and \(2475/1000000\). |
| Secretary limit \(1/e\) | For \(r_n=\lfloor n/e\rfloor+1\), \((r_n-1)/n\to 1/e\) and the harmonic sum is squeezed between two logarithms that both tend to \(1\). The maximum of \(y\ln(1/y)\) is \(1/e\) at \(y=1/e\). |
| Balls and bins, \(\psi(3)=1/3\) | \(\psi'(u)=(\ln 3-\ln u)/u^2\), positive before \(3\) and negative after. Then \(\kappa(\ln\kappa-1)\ge 2\ln n\). |
| Waiting time, variance \(3e-e^2\) | \(\mathbb E[N^2]=\sum(2j+1)/j!=3e\), so the variance is \(3e-e^2\). |
| Stick, every piece shorter than \(1/2\) | The probability is \(1-n/2^{n-1}\). For \(n=3\) this is \(1/4\). |
| Piece containing a random point | \(\mathbb E[L_1^2]=2/(n(n+1))\), and \(n\) pieces give \(2/(n+1)\). |
| Subset sums, \(4\) and \(52\) | \((2^3-2)/3+2=4\) and \((\binom{10}{5}-2)/5+2=52\). The four subsets of \(\{1,2,3\}\) were listed and match. |
| Van der Waerden | If \(N^2\le(k-1)2^k\), the expectation is strictly less than \(1\), so \(W(k,2)>N\), and the integer \(W(k,2)\) is strictly larger than \(\sqrt{k-1}\,2^{k/2}\). |
| Hash collision | \(\sum_r n_r^2\le p^2/m+p\), hence the probability is at most \(1/m+1/p\). |

Sicherman's product was multiplied out: faces \(1,2,2,3,3,4\) times faces \(1,3,4,5,6,8\) recover \((x+\cdots+x^6)^2\).

## What meets the audit constraints

**`ex:twotests`.** The prompt contains the prior \(1/100\), the detection rate \(99/100\), and the false positive rate \(1/20\). It does not point at a missing example. Bayes' formula is the rule recorded at the opening of Chapter 1, from Volume 1, Chapter 10. Conditional independence is used only after the state of health is fixed. The solution is the two-path comparison above.

**`ex:secretary`.** Part (a) is the uniform position of the best candidate and the uniform place of the previous record. Part (b) compares the harmonic sum with integrals of \(1/x\), which the solution derives from the graph, and it stops at this family of threshold strategies. The last sentence says the argument does not compare them with an arbitrary acceptance rule. There is no global-optimality claim.

**`pb:sicherman`.** The factors are peeled by the monic gcd and the Bézout identity from Volume 1, Chapter 6. The text does not cite a theorem titled unique factorisation. Irreducibility of the quadratics is the negative discriminant \(-3\). The value \(A(1)=6\) forces the exponents of \(1+x\) and \(1+x+x^2\).

**`pb:loaded`.** For \(n=6\), each factor would have degree \(5\), and a real polynomial of odd degree has a real root, while \(1+\cdots+x^{10}\) does not. For every \(n\ge 2\), the two-term AM–GM inequality gives a middle coefficient strictly larger than \(1/(2n-1)\).

**`pb:subsetsum`.** Parts (a) and (b) only. The roots-of-unity filter is Volume 1, Chapter 5. The product over the \(p\)th roots equals \(2\) because \(p\) is odd. Part (b) squares that generating function and reads the coefficient \(2\) of \(y^p\).

**`ex:ballsbins`.** The union bound and \(e^k\ge k^k/k!\) are elementary. Part (b) is the maximum of \(\psi\) at \(u=3\), then the ceiling. There is no Gonnet citation.

**`pb:passone`.** The simplex volume \(x^n/n!\) is an induction on one integral. The tail-sum identity for a positive integer is Volume 1, Chapter 10, in the waiting-time section, and the solution also writes \(N\) as the sum of the indicators. The increasing run has probability \(1/k!\) because the coordinates are continuous and exchangeable. The triangular map in part (c) has determinant \(1\). Volume 1, Chapter 7, states that a linear map multiplies parallelepiped volume by the absolute value of the determinant. The solution uses that linear fact, not the general Jacobian, which the same chapter defers to Volume 7.

**`pb:stick`.** The ordered sample extends the two-point count in Proposition `prop:orderpair` from two preimages to \((n-1)!\). The tail \((1-t)^{n-1}\) is the scaled simplex from `pb:passone`, which precedes this exercise. Two pieces cannot both reach length \(1/2\). The length found by an independent uniform point is \(\mathbb E[\sum L_i^2]\).

**`ex:mcmillan`.** A prefix code stops at one leaf. The code \(\{0,01\}\) is parsed from the left because a \(1\) cannot start a word. The counting bound is \(K^N\le N\ell_{\max}+1\), so \(K\le 1\). Shannon's proof, after Kraft has supplied the sum at most \(1\), is Gibbs' inequality and \(\log_2 Z\le 0\). Those two lines do not use the prefix property again, and Gibbs is Proposition 7.1, earlier in the same chapter.

**`pb:samecycle`.** The cycle through \(1\) closes at step \(k\) with probability \(1/n\), by the telescoping product and by the count \(\binom{n-1}{k-1}(k-1)!(n-k)!/n!\). The marked set \(\{1,\ldots,k\}\) meets the return in a uniform relative order, so all \(k\) of them lie on the cycle with probability \(1/k\).

**`pb:hashing`.** For \(x\not\equiv y\), the map \((a,b)\mapsto(ax+b,ay+b)\) is a bijection, with the inverse written down. The class sizes modulo \(m\) give \(\sum n_r^2\le p^2/m+p\). With \(m=n^2\), Markov's inequality from Volume 1, Chapter 10, gives success probability at least \(1/2-n^2/(2p)\).

**`ex:wlower`.** The number of \(k\)-term progressions is strictly less than the integral \(N^2/(2(k-1))\), because \(N-(k-1)x\) is strictly decreasing. Each is monochromatic with probability \(2^{1-k}\). There is no Berlekamp sentence. The comparison is the first-moment method already in `thm:erdos`.

**`thm:twosat` and `cor:twosat`.** If \(\Psi(x)=n^2-x^2\) and the chance of moving toward the fixed satisfying assignment is \(\theta\ge 1/2\), then
\[
\mathbb E[\Psi(X_{t+1})+1\mid\text{history}]-\Psi(x)=2x(1-2\theta)\le 0.
\]
Finite histories give \(\mathbb E[t\wedge T]\le n^2\). The identity \(\mathbb E[T]=\sum_{k\ge 0}P(T>k)\) is the tail-sum identity of Volume 1, Chapter 10, proved there from \(\min(T,M)\) and finite linearity, not from an integral monotone-convergence theorem. The proof says so. The corollary runs \(k\) blocks of \(2n^2\) flips and uses Markov once per block. The linking-clause paragraph after the corollary is a description of a path walk. It is not part of the numbered statement.

The new prose was read against the sound-human test in `docs/WRITING-STYLE.md`. The sentences name the object and the step. They do not use the hollow intensifiers, stock openers, or template summaries that test rejects.

## Concept registry

On this head the concept file still has 120 entries, every one `accepted-internal`. Against the pre-merge restoration head, the only entry field that changes is `reviewed_snapshot_sha256`. The only snapshotted source whose hash changes is `volume4-chance/chapters/ch01-counting.tex`, now `9c0644fdff0587cc1a456c61c2ec6e4fad033503b6c5609b9682266d7aefeba6`, the sha256 of the merged file. The stored snapshot hash is `81d051a28161cccf04f4d83e820f22f222d35c53f5313337d1ff05a4d9c77e8b`. The Chapter 1 pin in the signed-off source test is the git blob `7ca981366fe12e6d6212d30d161e7823cfd4801d`, which matches the file. The note says the statuses were not reassigned. That claim matches the file. No Volume 3 manuscript is in the diff.

## Issue log

| ID | Severity | Finding | What to change | Unresolved |
| --- | --- | --- | --- | --- |
| V4-REST-01 | closed at `82a3f104` | At `ec6e71da` the solution wrote \(\binom{n}{3}-n(n-1)^2/8=n(n-1)(n-5)/24=\frac14\binom{n}{3}-n(n-1)/6\). The second equality was false. For \(n=6\) the left side is \(1.25\) and that right side is \(0\). | The repair replaces the denominator \(6\) by \(8\). | Closed. Both equalities now hold, and \(n=6\) gives \(1.25\) on each side. |

No other item on the approved list failed its check. V4-REST-01 was the reason the verdict at `ec6e71da` was REQUEST CHANGES. It is closed at `82a3f104`. This review does not edit the restoration branch.
