# Volume 5 rewrite, self-review, 13 November 2026

Second sentence-level pass of *Calculation: From Formula to Insight*, on branch `cursor/volume5-complete-rewrite-a791`. The contract is `docs/handoffs/volume5-rewrite-2.md`. The independent re-read of the same day (on `main`) had already repaired V5-4 through V5-20. This pass did not undo those repairs. Numbered statements were not inserted or removed in the middle of a chapter. New exercises are appended.

## What was rewritten

Each chapter’s opening, the bridges between its sections, and the closing “what we proved” were rewritten in the voice of Volumes 1–4: a concrete number or dated fact first, then the job of the argument, short sentences, “you” when a check is due. Displayed formulae that were already the shortest correct statement were kept. Algebraic lines inside proofs were kept when each step already followed from the previous one; the English around them was rewritten where it only announced a heading.

New material, counted from the source after the pass:

| Item | Count |
| --- | --- |
| New exercises, each with a hint and a solution | 50 (four in each chapter except three in Chapters 2 and 13) |
| New TikZ figures included by the chapters | 26 |
| Public-domain portraits | 12, listed in `volume5-calculation/photos/CREDITS.md` |

The portraits are Jacob Bernoulli, John Wallis, Leonhard Euler, Joseph Fourier, Siméon Denis Poisson, Augustin-Louis Cauchy, Bernhard Riemann, Niels Henrik Abel, Colin Maclaurin, Carl Friedrich Gauss, Carl Gustav Jacob Jacobi, and Srinivasa Ramanujan. Seven are byte-for-byte copies of the Volume 1 files. Five were downloaded from Wikimedia Commons on 13 November 2026. Licences are public domain. Legendre’s 1820 caricature was not used: at 320 pixels it would print under 300 ppi.

The preface, the back-cover blurb, and `kdp.md` were rewritten to the thirteen-chapter book. The paperback ISBN is still unset. `common/cover-notes.json` was not edited. The blurb does not use the macro `\Z`, which the cover wrap does not define.

## Mathematics checked in this pass

Numbers below were recomputed in Python while the new exercises and figures were written.

- Falling-power expression of \(\sum_{k<n} k^3\). The coefficient of \(k^{\underline 2}\) is 3, and \(\sum k^{\underline 2}=n^{\underline 3}/3\), so that term contributes \(n^{\underline 3}\), not \(\tfrac32 n^{\underline 3}\). The sum is \(\bigl(n(n-1)/2\bigr)^2\). Checked at \(n=4\): both sides 36.
- \(B_4=-\frac1{30}\) from the recurrence at \(n=4\), and \(\sum_{k<3}k^4=17\).
- \(\sum_{k<n} kc^k=\bigl((n-1)c^{n+1}-nc^n+c\bigr)/(c-1)^2\). Checked at \(c=3\), \(n=3\): both sides 21.
- Ways to pay \(n\) cents with coins of 1 and 2: \(\lfloor n/2\rfloor+1\). For \(n=4\), three ways.
- \(p(5)=p(4)+p(3)-p(0)=7\).
- \(\prod_{n=2}^N(1-1/n^2)=(N+1)/(2N)\). For \(N=3\), both sides \(2/3\).
- Even and odd Basel tails: \(\pi^2/24\) and \(\pi^2/8\).
- Viète’s first two factors multiply to about \(0.653\), against \(2/\pi\approx 0.637\).
- \(\int_0^1 x\ln x\,dx=-1/4\). Frullani with rates 2 and 3 is \(\ln(3/2)\), matching Theorem 4 (Frullani) for \(f(x)=e^{-x}\).
- \(\Gamma(3/2)=\sqrt\pi/2\). \(V_2=\pi\), \(V_3=4\pi/3\).
- DFT of \((1,0,-1,0)\) is \((0,2,0,2)\). FFT multiplication counts: \(M(8)=12=\frac82\log_2 8\).
- \(\int e^{-\pi x^2}\,dx=1\) because the Gaussian is its own transform and the value at frequency 0 is the integral.
- Poles of \(1/(1+z^4)\) in the upper half-plane: \(e^{i\pi/4}\) and \(e^{i3\pi/4}\). \(\int_{-\infty}^\infty dx/(1+x^2)=\pi\). On \(|z|=2\), \(|3z+1|\le 7<32=|z^5|\).
- \(\zeta(-1)=-1/12\), \(\zeta(-3)=1/120\). Trivial zeros use the factor \(1/\Gamma(s/2+1)\) in Corollary 10 (the plane), not a different normalisation.
- \(\ln 10+\gamma+1/20\approx 2.9298\), against \(H_{10}\approx 2.92897\). The printed Euler–Maclaurin partial sum \(2.928968253927\ldots\) remains the smaller number, by \(4.1\times 10^{-11}\).
- \(\log p(n)\) and \(\log\mathrm{HR}(n)\) at \(n=10,20,50,100\): gaps about \(0.136\), \(0.099\), \(0.063\), \(0.045\). The \(N'\)-main term at \(n=100\) is about \(198\,301\,300\), and \(p(100)/\)that term is about \(0.961\).
- AGM from \(1\) and \(1/\sqrt 2\): \(a_1\approx 0.8536\), \(b_1\approx 0.8409\), and \(a_2\) and \(b_2\) agree at \(0.8472\) to four decimals. If \(a>b>0\) then \(a_1^2-b_1^2=((a-b)/2)^2\).

The quicksort example box was split. The closed form \(C_n=2(n+1)H_n-4n\) stays inside the unbreakable example; the derivation sits in the following prose. The layout check then reported 435 whole boxes, maximum height 383 pt, and no unresolved references.

## What was left, and why

Existing solutions of the long problem list in Chapter 13 were not retyped line by line where the algebra was already the argument. Their statements were left as the mathematical task a later volume may cite by number. New AGM exercises were appended after them.

Waring’s problem remains out of this volume. `thm:functional` remains the functional equation in Chapter 10, with completed function \(\xi\). `thm:eta` remains the transformation of \(\eta\) in Chapter 12. The proved Hardy–Ramanujan error remains \(O(n^{-1/4})\), and the text still says where the factor \(n^{-1/2}\) was lost. Rademacher’s series stays quoted.

## Continuity issues not edited

These sit outside Volume 5. They were not patched.

| Where | What |
| --- | --- |
| Volume 6, in progress on another branch | That volume cites Volume 5 by printed numbers. This pass did not move those numbers. Volume 6 still has to be checked against the class of the inversion theorem in Chapter 8, as the earlier handoff asked. |
| Volume 8, Chapter 14 | Still owes the matching sentence on which complex analysis it owns (homology, Phragmén–Lindelöf, Hadamard, Mellin inversion), the sentence this volume already points at. |
| Volumes 11–15 | Frozen. No edit, even where an old file not reached by `main.tex` once carried a wrong theorem number. The 13 November re-read records those as V5-2 and V5-3, and the follow-up review accepted the repairs already on `main`. |

No other volume’s source was modified.
