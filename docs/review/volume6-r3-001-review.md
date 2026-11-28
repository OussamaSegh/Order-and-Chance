# V6-R3-001 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `bd18b60f884db8ada101d072a30f730685c6fbca`. Against `ddf23cd89103582fc5879cd3351dfb5b22053df0` the book diff is one sentence in `volume6-crossroads/chapters/ch05-pnt.tex`.

## What was checked

The book’s definition is \(\mathrm{Li}(x)=\int_2^x\mathrm dt/\log t\) (preface). Chapter 5 writes that integral for \(\operatorname{Li}(1000)\). Chapter 10 writes the same integral and points it at this chapter. The remark uses that \(\operatorname{Li}\).

For each integer \(n\) from 2 through 20, \(\pi(n)\) was counted from the primes, and \(\operatorname{Li}(n)\) was computed apart from the proof in two ways: the series for \(\operatorname{li}(n)-\operatorname{li}(2)\), and a composite Simpson rule for \(\int_2^n\mathrm dt/\log t\). The two values differ by at most \(9\times10^{-13}\). An 80-node Gauss–Legendre rule in float64 matches the series to 12 decimals. The difference \(\operatorname{Li}(n)-\pi(n)\) is negative at 2, 3, 4, and 5, positive at 6 (\(+0.177\)), negative at 7 (\(-0.288\)), and positive at every integer from 8 through 20. The smallest of those positive values is \(+0.209\) at 8.

So 7 is a known integer with \(\operatorname{Li}<\pi\), and 8 is not. The new sentence, “No integer \(x\ge 8\) is known at which \(\operatorname{Li}(x)<\pi(x)\),” is the cutoff that fits those signs. Littlewood’s infinitude of sign changes stays in the previous sentence, so “known” means exhibited. Bays and Hudson stay on the other logarithmic integral in the next sentence. Adding the constant \(\operatorname{li}(2)=1.045\ldots\) makes \(\operatorname{li}(7)-\pi(7)>0\), so the sign change at 7 belongs to the book’s lower limit. Chapter 10 says \(\pi(x)-\operatorname{Li}(x)\) is positive for some arbitrarily large \(x\): existence, not an integer. The figure in this remark runs from \(10^2\) to \(10^8\), so its sentence does not claim the inequality at 7. No other sentence in Volume 6 says that no such integer is known.

The diff adds no label, counter, caption, or font command. `git diff --check` on that range is clean. Only `volume6-crossroads/chapters/ch05-pnt.tex` changes.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. No CI log was read. Littlewood’s proof was not re-proved. The place \(1.398\times10^{316}\) was not recomputed. No integer past 20 was evaluated, including the range through \(10^8\) and the caption’s \(753\).

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The sentence stands. The book line was not edited. |
