# Volume 6, round 3 (review only)

Score: **9/10**.

Base: `ddf23cd89103582fc5879cd3351dfb5b22053df0` on `main`. Sources: `volume6-crossroads/` (twelve chapters, preface, exercises with hints and solutions). No book source was edited. Volume 1 starts at Chapter 0, and theorem, proposition, lemma, corollary, definition, and example share one counter. That count was used for every citation that was opened.

The numbered theorems that were checked hold. The thirteen passages changed in #316–#322 and #324–#329 are still correct, and none of them introduced a new error. Regression count: **0**. One minor remains, in a remark. It is not a numbered theorem.

## Regression check

Each row is the printed text on `main` at the base SHA above.

| PR | Merge | Passage | Result |
| --- | --- | --- | --- |
| #316 | `07ee61e6c6bb6054eb6abe9e9f595a1d83dd0df1` | `ch06-zeros.tex` solution of `ex:xi2` | Holds. \(\xi(2)=\pi/6\), and \(\xi(-1)=\xi(2)\). At the negative even integers the pole of \(\Gamma(s/2)\) cancels a zero of \(\zeta\). The factor \(\frac12 s(s-1)\) does not vanish there. \(\Gamma(-1/2)\) is finite. |
| #317 | `6f48c1a6d2d821e8bf737552af9c21e682ba9767` | Jensen proof, same file | Holds. After the zeros are removed, isolation gives a slightly larger open disc \(D'\) with \(\{|z|\le R\}\subset D'\subset D\). |
| #318 | `e89e3e81a1504cf15738158c0502d4e8b16c1cc0` | Argument principle, same file | Holds. \(N(T)\) is real, so \(\int\xi'/\xi\) is purely imaginary and its imaginary part is \(2\pi N(T)\). The symmetry still gives \(\pi N(T)=\operatorname{Im}\int_L\xi'/\xi\). |
| #319 | `807bc0b5bceb26936c1841e0bdc8b6ea514296b6` | `ch05-pnt.tex` solution of `ex:li` | Holds. From \(\pi(x)=\operatorname{Li}(x)+o(x/\log^2 x)\) the quotient is \(1+1/\log x+o(1/\log x)\). |
| #320 | `d7a6b91136588cee99c00d177bd82a14154a4393` | caption of `fig:monobump`, and the node in `figures/ch05-new-bump.tex` | Holds. The Euclidean area is \(\frac12 c(\lambda-1)^2 x^2\). The integral of \((\lambda cx-ct)/t^2\) is \(c(\lambda-1-\log\lambda)\), independent of \(x\). The node says the area grows like \(x^2\). |
| #321 | `8dd2da41f42f20dfdbe5d47c14911b7eb378effb` | Buchstab solution, `ch08-sieves.tex` | Holds. As \(u\to 1^+\), \(\omega(u)/e^{-\gamma}\to e^{\gamma}\). And \(2e^{-\gamma}=1.1229189\ldots\). |
| #322 | `614400b0061f715658cee0266f0b5b07640a7c77` | mod-3 sentence, `ch10-random.tex` | Holds. The same class costs \(\frac23\). Distinct classes cost \(\frac13\). The ratio is \(2=(p-1)/(p-2)\) at \(p=3\). |
| #324 | `af3f9afbaee7b76237f8b9ad085420fda82d328f` | idea for `pb:twosquares` | Holds. \(F^2\) is \(\zeta(s)L(s,\chi_4)\) times a factor holomorphic and non-zero at \(s=1\). The problem’s identity and the constant \(C^2=\frac\pi2\prod(1-p^{-2})^{-1}\) in the write-up agree. |
| #325 | `63b6dd40c1d1809edf3ae94e7641cff6e84c8703` | solution of `pb:cramersign` | Holds. \((\psi(x)-x)/\log x\) has \(65\,162\) sign changes for \(2\le x\le 10^8\): \(32\,581\) up-crossings and \(32\,581\) down-crossings. The problem’s \(66\,112\) remains the count for \(\Pi(x)-\operatorname{li}(x)\). |
| #326 | `53f3c726c40cea45e8ed5b50b5b85e175384374b` | Cramér’s constant, `ch02-averages.tex` | Holds. \(\zeta(3/2)^4/(6\pi^2\zeta(3))=0.65428397\ldots\), so the prefix is \(0.6542\ldots\). |
| #327 | `3bdbdeae811c92f605de3c0fd4613c930c70e785` | ratio at \(1000\), `ch01-mertens.tex` | Holds. \(P(1000)=0.0809652635\ldots\) and the ratio against \(e^{-\gamma}/\log 1000\) is \(0.99613283\ldots\). |
| #328 | `d525fc4ad976d9ae5fc9601c60decba1f7053ca6` | upper block on the prime \(3\), `figures/ch01-tenfactorial.tex` | Holds. That rectangle is \(\lfloor 10/9\rfloor=1\), filled with `MidnightBlue!28`, the ink the legend gives to multiples of \(p^2\). |
| #329 | `ddf23cd89103582fc5879cd3351dfb5b22053df0` | beauty note, `ch03-characters.tex` | Holds. The ideal count is restricted to a primitive real character. The non-vanishing proof uses only \(r(n)\ge 0\). |

The sign changes were counted for the right-continuous step functions. An up-crossing is a jump at a prime power \(q\) with \(\psi(q-)<q<\psi(q)\), or \(\Pi(q-)<\operatorname{li}(q)<\Pi(q)\), where \(\operatorname{li}(x)=\operatorname{Ei}(\log x)\). A down-crossing is a zero on the flat interval before the next prime power. Below \(30\), \(\psi(x)-x\) has the one up-crossing at \(19\) and the one down-crossing in \((19,20)\). On \([2,5000)\) the same scan gives \(228\) of each. The \(\Pi-\operatorname{li}\) total is \(33\,056+33\,056=66\,112\).

## What was checked

Read against the source: the preface; the three Chebyshev bounds and Mertens’s product; the non-vanishing argument, both for complex characters and for a real character; Dirichlet’s formula for \(L(1,\chi)\); the \(3\)-\(4\)-\(1\) arithmetic that produces \(1/(14A'\log|t|)\); the explicit-formula residues at \(s=1\), at the zeros, at \(s=0\), and at the trivial zeros, including \(\zeta'/\zeta(0)=\log 2\pi\); the bias identity for \(\theta(x;4,3)-\theta(x;4,1)\); the dimension count for \(M_k\), \(E_4^2=E_8\), and the congruence modulo \(691\); the Lipschitz formula’s constant \(-2k/B_k\); Selberg’s weight \(\lambda_2=-21/22\); the idea and write-up for sums of two squares; and the solution of `pb:cramersign`, including the Stieltjes identity, which was evaluated at \(x=10\), \(100\), and \(1000\).

Recomputed, and in agreement with the text: \(P(1000)=0.0809652635\ldots\) and the ratio \(0.99613283\ldots\); Cramér’s constant \(0.65428397\ldots\); \(2e^{-\gamma}=1.1229189\ldots\); \(\pi(1000)=168\), \(\pi(10^8)=5\,761\,455\); \(\operatorname{Li}(1000)=176.5645\ldots\) and \(\operatorname{Li}(10^8)-\pi(10^8)=753.330\ldots\); on \([10^3,10^8]\) the normalised \(\pi-\operatorname{li}\) runs from \(-2.7419\ldots\) to \(-0.5265\ldots\), and \(\Pi-\operatorname{li}\) from \(-0.8886\ldots\) to \(0.7139\ldots\), which are the printed endpoints \(-2.74\), \(-0.53\), \(-0.89\), and \(0.71\) after rounding; \(\xi(2)=\pi/6\); \(65520\equiv-125\) and \(432000\equiv125\pmod{691}\). With the book’s \(\operatorname{Li}(x)=\int_2^x\mathrm dt/\log t\), \(\operatorname{Li}(n)-\pi(n)\) is negative at \(n=2,3,4,5,7\) and at no other integer through \(5000\). From \(8\) through \(10^8\) it stays positive: the minimum of \(\operatorname{li}-\pi\) on the prime endpoints in \([10^3,10^8]\) is \(6.96\), and \(\operatorname{Li}\) is that quantity minus \(\operatorname{li}(2)\approx1.045\).

A counter, in `main.tex` order, matched every numbered Volume citation that was parsed: the cited kind and the number \(a.b\) exist. Chapter citations were matched the same way. The ones opened support the sentences that cite them. Among them: Volume 1, Theorem 3.8 (extreme value), Theorem 9.3 (AM–GM), Theorem 9.4 (Cauchy–Schwarz), and Proposition 7.4 (Vandermonde); Volume 2, Theorems 2.2, 2.4, 2.5, 4.6, 7.3, 7.5, and 10.5; Volume 4, Theorems 2.1, 4.2, 4.4, and 6.10, Proposition 6.7, and Definition 11.1; Volume 5, Theorems 3.7, 5.14, 6.13, 8.14, 9.9, 9.11, 9.15, 9.18, 9.26, 9.36, 10.8, and 12.4, Corollaries 4.5, 6.14, 9.12, 9.35, 10.4, and 10.9, and Propositions 7.13, 9.2, 10.1, and 10.2; Volume 13, Chapter 11 (the analytic class-number formula) and Chapter 12 (the functional equation of \(L(s,\chi)\), the corollary that chapter names as the one Volume 6 admitted); Volume 15, Chapter 2, whose statement of Maier’s theorem is the pair of inequalities quoted in Chapter 10. Tonelli’s theorem is in Volume 7, as the preface says. Internal `\ref` targets: none missing, no duplicate labels. The index entries match those labels. Exercises: 188, each with one hint and one solution.

The preface is right that this volume is the last of Part II, and that the two admitted facts are the functional equation of \(L(s,\chi)\) and Tonelli’s theorem. Each is labelled once, the first in the Chapter 7 remark and the second in one Chapter 12 solution.

The hypothesis in that Chapter 7 remark is the non-trivial zeros of \(L(s,\chi_{-4})\). The three ordinates are data. The displayed sum is the sum under the Riemann hypothesis for every one of those zeros.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled, and no GitHub Actions log was read. The six round-2 run ids named for the tracker were not opened. A static parse of `\label` and `\ref` does not see a counter hidden inside a conditional, and it does not see an overfull box.

TikZ pictures were not redrawn. The ten-factorial figure was read as coordinates and inks. Historical page numbers, Büthe’s verification to \(10^{19}\), the Rubinstein–Sarnak densities, Gourdon’s zero count, and the quoted irrationality measures were not checked against the papers. Proofs the text marks as quoted or admitted were not re-proved. Not every line of every solution was recalculated. The large-sieve \(L^2\) bound, the Erdős–Kac moment comparison, and Siegel’s contour were read in part and were not rebuilt from the first estimate.

## Issues

V6-R3-001 | minor | volume6-crossroads/chapters/ch05-pnt.tex:276 | The remark says that no integer is known at which \(\operatorname{Li}(x)-\pi(x)\) changes sign. The book’s \(\operatorname{Li}(x)=\int_2^x\mathrm dt/\log t\) gives \(\operatorname{Li}(6)-\pi(6)=0.177>0\) and \(\operatorname{Li}(7)-\pi(7)=-0.288<0\), so the sign changes at \(7\). The same difference is negative at \(2\), \(3\), \(4\), and \(5\). It is positive at every integer from \(8\) through \(10^8\). The figure’s claim on its own range, the value \(753\) at \(10^8\), and the attribution of the crossing near \(1.398\times10^{316}\) to the other logarithmic integral are right. | Say that no integer \(x\ge 8\) is known at which \(\operatorname{Li}(x)<\pi(x)\).

## Counts

0 critical, 0 major, 1 minor. Regressions in #316–#322 and #324–#329: 0.
