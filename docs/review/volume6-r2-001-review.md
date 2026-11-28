# V6-R2-001 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `455d954932b4fb3d0b595dda932332e63a9960d2`.

## What was checked

The issue is real. The problem states
\[
F(s)^2=\frac{\zeta(s)L(s,\chi_4)}{1-2^{-s}}\prod_{p\equiv3\,(4)}(1-p^{-2s})^{-1},
\]
and the write-up derives that identity from the Euler factors. The factors of \(F^2\) are \((1-2^{-s})^{-2}\), \((1-p^{-s})^{-2}\) for \(p\equiv1\pmod4\), and \((1-p^{-2s})^{-2}\) for \(p\equiv3\pmod4\). The factors of \(\zeta L\) are \((1-2^{-s})^{-1}\), \((1-p^{-s})^{-2}\), and \((1-p^{-2s})^{-1}\). The quotient is \((1-2^{-s})^{-1}\prod_{p\equiv3\,(4)}(1-p^{-2s})^{-1}\). The old idea line omitted it.

That quotient is holomorphic for \(\operatorname{Re}s>1/2\): \(2^{-s}=1\) only on the imaginary lattice through \(0\), and \(\prod(1-p^{-2s})^{-1}\) converges there. At \(s=1\) its value is \(2\prod(1-p^{-2})^{-1}\). The product over primes \(p\equiv3\pmod4\) up to \(10^8\) is \(1.16807558511\). Past \(10^8\), \(\sum p^{-2}<1.37\cdot10^{-9}\) by \(\pi(t)<1.25506\,t/\log t\), and the terms \(p^{-4},p^{-6},\ldots\) are smaller, so the full product lies in \((1.1680755851,1.1680755868)\) and the factor at \(s=1\) lies in \((2.336151170,2.336151174)\). It is not \(1\). \(L(1,\chi_4)=\pi/4\neq0\), and \(\zeta\) has a simple pole, so \(F^2\) still has a simple pole and the half-pole sentence stays. The constant in the problem is \(C^2=\frac\pi2\prod(1-p^{-2})^{-1}\). With this product, \(K=C/\sqrt\pi=0.76422365\ldots\), so the problem’s prefix \(0.7642\ldots\) is the truncated expansion. The new idea line is the repair the issue asked for. The write-up, the identity, and \(C^2\) are untouched.

The diff against `main` at `24ef1a84c134be92500e6704775cdc074298ae3f` is one sentence in `volume6-crossroads/chapters/ch12-modular.tex`. No other path. No numbered environment, label, or counter is added or removed.

The numerical value of the product was computed separately from the Euler-factor comparison.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. No GitHub Actions log was read. The Tauberian passage from the half-pole to \(B(x)\) was not re-proved. The bound \(\pi(t)<1.25506\,t/\log t\) was used as stated and was not re-proved. The write-up’s prefixes \(1.168076\ldots\) and \(0.764224\ldots\) are roundings of \(1.16807558\ldots\) and \(0.76422365\ldots\). They are outside this diff and were not edited.

## Issue log

| Problem | Resolution |
| --- | --- |
| None in the fix. | The idea line stands. This note is the only addition. |
