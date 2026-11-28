# V6-R2-002 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `de58b17b36086ee11eae8bc329b3757bc059c60d`.

## What was checked

The issue is real. Part (d) of `pb:cramersign` states that \(\Pi(x)-\operatorname{li}(x)\) changes sign \(66\,112\) times below \(10^8\). The solution gave that count to \((\psi(x)-x)/\log x\). For \(x\ge2\), \(\log x>0\), so that quotient has the same sign changes as \(\psi(x)-x\).

Both counts were recomputed for the continuous functions, separately from the identities in (c). \(\psi\) and \(\Pi\) are the right-continuous step functions. An up-crossing is a jump at a prime power \(q\) with \(\psi(q-)<q<\psi(q)\), or \(\Pi(q-)<\operatorname{li}(q)<\Pi(q)\). A down-crossing is a zero on the flat interval before the next prime power. Here \(\operatorname{li}(x)=\operatorname{Ei}(\log x)\). Below \(10^8\), and also on \(x\le10^8\),
\[
\psi(x)-x
\]
has \(32\,581\) up-crossings and \(32\,581\) down-crossings, total \(65\,162\). The same scan for \(\Pi-\operatorname{li}\) gives \(33\,056+33\,056=66\,112\). One further zero of \(\operatorname{li}\) lies in \((1,2)\), where \(\Pi=0\); the stated \(66\,112\) does not include it. The two equal halves match the sign at the ends: both functions are negative at \(2\) and negative near \(10^8\).

A direct check from \(\operatorname{lcm}(1,\ldots,n)\): \(\psi(18)-18<0\), \(\psi(19)-19=+0.26566\ldots\), and \(0<\psi(19)-19<1\). That is one up-crossing at \(19\) and one down-crossing in \((19,20)\), and those are the only two below \(30\). The prime-power scan and an integer walk agree on \([2,5000)\): \(228\) up and \(228\) down.

The closest decisions were recomputed at higher precision. For \(\psi\), the smallest gap to a crossing threshold is \(2.96\cdot10^{-4}\). Summing \(\log p\) in 25 decimals at the closest sites moved no decision; the float and the high-precision gap differ by less than \(2\cdot10^{-9}\). For \(\Pi-\operatorname{li}\), the smallest gap is \(2.16\cdot10^{-6}\). Sampled values of the power series for \(\operatorname{Ei}\) differ from `mpmath.li` by at most \(4.3\cdot10^{-12}\). The closest jump gaps and the closest interior gaps, fifteen of each, were redone with \(\Pi\) an exact multiple of \(1/\operatorname{lcm}(1,\ldots,26)\) and \(\operatorname{li}\) from `mpmath`. No decision moved.

The new parenthesis states \(65\,162\) sign changes of \((\psi(x)-x)/\log x\) below \(10^8\). That is the count above. The rest of (d), including the explicit-formula size, is unchanged and does not use the integer. The diff against `main` at `24ef1a84c134be92500e6704775cdc074298ae3f` is that one integer in `volume6-crossroads/chapters/ch12-modular.tex`. No numbered environment, label, or counter is added or removed.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. No GitHub Actions log was read. The normalised ranges \(-2.74\), \(-0.53\), \(-0.89\), and \(0.71\), and the claim \(\pi(x)<\operatorname{li}(x)\) on \([10^3,10^8]\), were not recomputed.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The count stands. This note is the only addition. |
