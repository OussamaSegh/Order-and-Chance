# Mathematical review ledger — Volume 15

**Not a proof certificate.** The rows below are an author-side record of each added exercise and figure. They do not replace an independent reading of the proofs. Preservation, arithmetic and typesetting tests cannot establish the general arguments. No original formal statement was altered. No external mathematical certification was obtained.

Stars follow the series rule: a one-line computation is one star, and three stars are used only for a multi-step proof. Every numerical value in the solutions is recomputed by `check_new_examples.py`. Dependencies are labels in this volume, or a numbered result already cited in the volume.

| Item | Chapter | What it teaches | Dependencies | Status |
| --- | --- | --- | --- | --- |
| ex:v15-01-1 | 1 | \(\Psi(40,5)=21\) and \(\Psi(40,2)=6\) | definition of \(y\)-smooth | author-side; not refereed |
| ex:v15-01-2 | 1 | \(F(1/4)=1/3\), \(F(1/2)=1/2\), \(f(1/2)=2/\pi\) | arcsine density of thm:ddt | author-side; not refereed |
| ex:v15-01-3 | 1 | divisors at most \(\sqrt n\) number \(\lceil\tau(n)/2\rceil\) | pairing of divisors | author-side; not refereed |
| ex:v15-01-4 | 1 | squarefree count is \((6/\pi^2)x+O(\sqrt x)\), and equals 61 at \(x=100\) | Möbius inversion over the square part; the constant \(6/\pi^2\) from the chapter opening | author-side; not refereed |
| fig:v15c01-smooth | 1 | 5-smooth integers among \(1,\ldots,20\) | the list in ex:v15-01-1 | author-side; not refereed |
| fig:v15c01-arcsine | 1 | arcsine density, median \(1/2\) | thm:ddt | author-side; not refereed |
| ex:v15-02-1 | 2 | \(\omega(3/2)=2/3\), \(\omega(2)=1/2\), \(e^\gamma\omega(2)=0.8905\) | prop:buchstabsign | author-side; not refereed |
| ex:v15-02-2 | 2 | Cramér expectation on \((100,121]\) is 4.46, against \(y/\log x=4.61\) | Cramér probabilities | author-side; not refereed |
| ex:v15-02-3 | 2 | empty-interval probability has limsup at most \(e^{-1}\) when the length is \(\log x\) | \(1-t\le e^{-t}\) | author-side; not refereed |
| ex:v15-02-4 | 2 | expected number of empty windows of length \(\lambda(\log x)^2\) tends to 0 for \(\lambda>1\) | ex:v15-02-3; summable probabilities | author-side; not refereed |
| fig:v15c02-buchstab | 2 | \(\omega(u)\) on \([1,3]\) against \(e^{-\gamma}\) | prop:buchstabsign; ex:omega23 | author-side; not refereed |
| fig:v15c02-gaps | 2 | Maier matrix: rows short intervals, columns coprime to \(P\) | thm:maier | author-side; not refereed |
| ex:v15-03-1 | 3 | average of \(v_2(n)\) on \(1\le n\le16\) is \(15/16\) | definition of \(v_2\) | author-side; not refereed |
| ex:v15-03-2 | 3 | \(P(V=k)=2^{-(k+1)}\), mean 1 | natural density of multiples of \(2^k\) | author-side; not refereed |
| ex:v15-03-3 | 3 | Erdős–Wintner series for \(v_2\) are \(0\), \(1/2\), \(1/2\); \(A\to1\), \(B^2\to6\) | thm:erdoswintner; thm:tkgeneral | author-side; not refereed |
| ex:v15-03-4 | 3 | characteristic function \(1/(2-e^{it})\) matches the geometric law | thm:erdoswintner; differentiation of the geometric series | author-side; not refereed |
| fig:v15c03-valuation | 3 | bars of \(P(V=k)=2^{-(k+1)}\) | ex:v15-03-2 | author-side; not refereed |
| fig:v15c03-gaussian | 3 | standard Gaussian of Erdős–Kac | thm:erdoskac-cor | author-side; not refereed |
| ex:v15-04-1 | 4 | \(\mathbb E f(n)=0\) for \(n>1\), so \(\mathbb ES(x)=1\) | Steinhaus model | author-side; not refereed |
| ex:v15-04-2 | 4 | \(N_5(2)=10\), \(N_5(3)=40\) | Gauss's count as used in thm:factortypes | author-side; not refereed |
| ex:v15-04-3 | 4 | a cubic over a field is reducible if and only if it has a root | degree count | author-side; not refereed |
| ex:v15-04-4 | 4 | \(N_p(2)=p(p-1)/2\) and \(N_p(3)=(p^3-p)/3\) by type counts | ex:v15-04-3 | author-side; not refereed |
| fig:v15c04-phases | 4 | one Steinhaus sample on \(2,3,5,15\) | def:rmf | author-side; not refereed |
| fig:v15c04-cubics | 4 | 125 monic cubics over \(\mathbb F_5\): 85 reducible, 40 irreducible | ex:v15-04-4 | author-side; not refereed |
| ex:v15-05-1 | 5 | partial twin-prime product through \(p=29\) is \(0.6651\) | definition of \(C_2\) | author-side; not refereed |
| ex:v15-05-2 | 5 | \(\mathfrak S(3)=0\), \(\mathfrak S(4)=\mathfrak S(2)\), \(\mathfrak S(6)=2\mathfrak S(2)\) | eq:pairseries | author-side; not refereed |
| ex:v15-05-3 | 5 | \(\mathfrak S(2p)/\mathfrak S(2)=(p-1)/(p-2)\) | eq:pairseries | author-side; not refereed |
| ex:v15-05-4 | 5 | derivation of eq:pairseries from the local factors \(b_p\) | def:singular | author-side; not refereed |
| fig:v15c05-series | 5 | bar comparison of \(\mathfrak S(2),\mathfrak S(4),\mathfrak S(6)\) | eq:pairseries | author-side; not refereed |
| fig:v15c05-patterns | 5 | \((0,2,4)\) meets \(0\bmod 3\); \((0,2,6)\) is admissible | ex:triples | author-side; not refereed |
| ex:v15-06-1 | 6 | \(R(100,4)=33\), and the Selberg bound is \(88.13\) | cor:selbergtwo | author-side; not refereed |
| ex:v15-06-2 | 6 | \(\sum_{p<11}1/p>1\) while \(W(11)=8/35\) | thm:bonferroni | author-side; not refereed |
| ex:v15-06-3 | 6 | \(\sigma(A+A)\ge 2\sigma-\sigma^2>\sigma\) when \(0<\sigma<1\) | lem:schnirelmann | author-side; not refereed |
| ex:v15-06-4 | 6 | inclusion–exclusion modulo 30 equals \(8/30\); the order-0 bound is \(-1/30\) | Möbius formula for \(\varphi\) | author-side; not refereed |
| fig:v15c06-bonferroni | 6 | negative partial sum against the exact proportion \(8/30\) | ex:v15-06-4 | author-side; not refereed |
| fig:v15c06-factor | 6 | the factor 2 in the Selberg upper bound | cor:selbergtwo | author-side; not refereed |
| ex:v15-07-1 | 7 | partial product for \(c_\infty\) at \(p=3\) through \(i=6\) is \(0.5605\) | definition of \(c_\infty\) | author-side; not refereed |
| ex:v15-07-2 | 7 | \(|\mathrm{Aut}(\Z/9)|=6\), \(|GL_2(\F_3)|=48\), ratio 8 | \(\mu_{CL}\) | author-side; not refereed |
| ex:v15-07-3 | 7 | \(\log(1-u)\ge-2u\) on \((0,1/2]\), so \(c_\infty>0\) | comparison of the logarithm | author-side; not refereed |
| ex:v15-07-4 | 7 | \(|GL_2(\F_p)|=(p^2-1)(p^2-p)\) and the Cohen–Lenstra ratio is \(p^2-1\) | counting bases; \(\varphi(p^2)\) | author-side; not refereed |
| fig:v15c07-auts | 7 | automorphism counts 6 and 48 | ex:v15-07-2 | author-side; not refereed |
| fig:v15c07-product | 7 | partial products falling toward \(0.5601\) | ex:v15-07-1 | author-side; not refereed |
| ex:v15-08-1 | 8 | for \(p=5\), \(P(K_2=0)=4/5\) and \(P(K_2=2)=1/5\) | lem:altchain | author-side; not refereed |
| ex:v15-08-2 | 8 | at \(p=3\), \(\mathbb E\,3^K=4\) and \(\mathbb E\,3^{2K}=40\) | cor:prmoments | author-side; not refereed |
| ex:v15-08-3 | 8 | \(K_n\equiv n\pmod 2\) because the rank is even | alternating matrices, recalled in the chapter | author-side; not refereed |
| ex:v15-08-4 | 8 | closed values of \(K_2\) and \(K_3\) match thm:altlaw | lem:altchain; thm:altlaw | author-side; not refereed |
| fig:v15c08-chain | 8 | birth–death arrows of the kernel chain | lem:altchain | author-side; not refereed |
| fig:v15c08-parity | 8 | kernel parity tracks \(n\) | ex:v15-08-3 | author-side; not refereed |
| ex:v15-09-1 | 9 | \(\hat K(0)=1\), \(\hat K(1/2)=1/2\), \(\hat K(1)=0\) | thm:formfactor | author-side; not refereed |
| ex:v15-09-2 | 9 | \(p_2(1)=0.908\), against \(e^{-1}=0.368\) | moments:prop:surmise | author-side; not refereed |
| ex:v15-09-3 | 9 | overlap of two unit intervals is \((1-\lvert\alpha\rvert)_+\) | proof of thm:formfactor | author-side; not refereed |
| ex:v15-09-4 | 9 | inverse transform of the tent is \((\sin(\pi u)/(\pi u))^2\) | series Fourier convention; involution on even functions | author-side; not refereed |
| fig:v15c09-tent | 9 | graph of \((1-\lvert\alpha\rvert)_+\) | thm:formfactor | author-side; not refereed |
| fig:v15c09-surmise | 9 | \(p_2(s)\) against \(e^{-s}\) | moments:prop:surmise | author-side; not refereed |
| ex:v15-10-1 | 10 | local factor of \(a_2\) at \(p=2\) is \(3/4\) | identity quoted in ex:ak | author-side; not refereed |
| ex:v15-10-2 | 10 | \((e^\gamma\log 10)^4=282.9\) | prop:eulermoment | author-side; not refereed |
| ex:v15-10-3 | 10 | the powers of \(\log y\) cancel, leaving \((\log T)^{k^2}\) | display after prop:eulermoment | author-side; not refereed |
| ex:v15-10-4 | 10 | generating function \((1+u)/(1-u)^3\), hence \(a_2=6/\pi^2\) and the fourth-moment coefficient \(1/(2\pi^2)\) | geometric series; \(G(3)^2/G(5)=1/12\) as recorded in the chapter | author-side; not refereed |
| fig:v15c10-split | 10 | arithmetic factor times matrix factor | the moment conjecture | author-side; not refereed |
| fig:v15c10-arithmetic | 10 | local factors \(1-p^{-2}\) at \(2,3,5,7\) | ex:v15-10-4 | author-side; not refereed |
| ex:v15-11-1 | 11 | bounds \(\pi^2/6=1.64493\) and \(\pi^2/15=0.65797\) at \(\sigma=2\) | ex:sigmabig | author-side; not refereed |
| ex:v15-11-2 | 11 | the limiting median of \(\lvert\zeta(1/2+it)\rvert\) is \(1\) | thm:selberg; \(\Phi(0)=1/2\) | author-side; not refereed |
| ex:v15-11-3 | 11 | \(\log 2/\log 3\) is irrational, so \((2^{-it},3^{-it})\) equidistributes | lem:kw; unique factorisation | author-side; not refereed |
| ex:v15-11-4 | 11 | \(\int\tfrac12\log((a^2+u^2)/(b^2+u^2))\,du=\pi(\lvert a\rvert-\lvert b\rvert)\) | differentiation under a truncated integral | author-side; not refereed |
| fig:v15c11-euler | 11 | three factors of the random Euler product | prop:randomeuler | author-side; not refereed |
| fig:v15c11-bell | 11 | Gaussian centred so that the median of \(\lvert\zeta\rvert\) is \(1\) | thm:selberg | author-side; not refereed |
| ex:v15-12-1 | 12 | a character on \(\Z_5\) has \(U^2\) norm \(1\) | prop:u2corr | author-side; not refereed |
| ex:v15-12-2 | 12 | \(\Lambda_3(\{0,1,2\})=1/5\) and \(\delta^3=0.216\) on \(\Z_5\) | definition of \(\Lambda_3\) | author-side; not refereed |
| ex:v15-12-3 | 12 | \(\lvert\Lambda_3-\delta^3\rvert\le(\delta(1-\delta))^{3/2}\) | thm:u2count; Parseval | author-side; not refereed |
| ex:v15-12-4 | 12 | \(\lVert f\rVert_{U^2}^4=\sum\lvert\hat f\rvert^4\) | Fourier inversion; Parseval | author-side; not refereed |
| fig:v15c12-cycle | 12 | translation on \(\Z_5\) | the characters in prop:u2corr | author-side; not refereed |
| fig:v15c12-progression | 12 | the set \(\{0,1,2\}\subset\Z_5\) | ex:v15-12-2 | author-side; not refereed |
| ex:v15-13-1 | 13 | first wave amplitude \(2/\lvert\rho\rvert=0.3310\) | ordinate \(6.0209\) already used in ex:fewwaves | author-side; not refereed |
| ex:v15-13-2 | 13 | Chebyshev bound \(1-V/2=0.9222\) from \(V=0.1556\) | thm:rubinsteinsarnak; ex:chebbound | author-side; not refereed |
| ex:v15-13-3 | 13 | symmetry about \(1\) gives \(P(X>1)=1/2\), while \(\delta=P(X>0)\) | thm:rubinsteinsarnak; cor:biasdensity | author-side; not refereed |
| ex:v15-13-4 | 13 | characteristic function is \(e^{i\xi}\prod J_0(2\xi/\lvert\rho\rvert)\) | the series for \(X\); the integral formula for \(J_0\) | author-side; not refereed |
| fig:v15c13-wave | 13 | constant 1 plus the first cosine | ex:v15-13-1 | author-side; not refereed |
| fig:v15c13-symmetry | 13 | law symmetric about 1, small mass left of 0 | cor:biasdensity | author-side; not refereed |
| ex:v15-14-1 | 14 | \(e^\gamma/2=0.8905\) and the model excess \(0.1229\) | ledger line 2; \(\omega(2)=1/2\) | author-side; not refereed |
| ex:v15-14-2 | 14 | at \(x=100\), \(h=20\), \(y=4\), the sum of squares is \(95/9\) and the bound is \(110/3\) | prop:tkshort | author-side; not refereed |
| ex:v15-14-3 | 14 | if \(y\le\sqrt h\) the average of \((\omega_y-\mu_y)^2\) is at most \(\mu_y+5\) | prop:tkshort | author-side; not refereed |
| ex:v15-14-4 | 14 | normal order of \(\omega\) in intervals of length \(x^\theta\) | prop:tkshort; Volume 6, Theorem 1.5; Chebyshev | author-side; not refereed |
| fig:v15c14-ledger | 14 | bulk agreement against fine-scale failure | sec:answer | author-side; not refereed |
| fig:v15c14-interval | 14 | short interval with the primes \(p\le\sqrt h\) marked | prop:tkshort | author-side; not refereed |

Original-text fixes: none.
