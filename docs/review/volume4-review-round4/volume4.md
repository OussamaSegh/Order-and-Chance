# Volume 4 — Chance, round 4

**Score: 6/10.**

**Counts.** 1 critical, 0 major, 4 minor. `V4-R4-001` through `V4-R4-005`.

**Round-3 follow-up.** The three sentences repaired in #296 were opened again. The absolute-value allowance in the sample second moment holds. The characteristic-function approximation holds, because the identity at the end of the proof of Proposition `prop:indepproduct` already factors bounded factors that are uniformly continuous on compact subintervals of \((0,1)\). The covariance limits do not: each estimate covers only one tail of an either-or set.

**How this was read.** The chapters in `volume4-chance/main.tex`, on main at `f691ae1b`, including exercises, hints, solutions, and the extremal appendix. The rows below were opened at the cited lines. No full LaTeX build was run.

## Issues

Paths are relative to `volume4-chance/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V4-R4-001 | `chapters/ch11-brownian.tex:337` | critical | “contained in \(E_n\) together with a strip of width \(2\eta\) for one dyadic sample. That strip … has outer content at most a constant times \(\eta\).” | False. Off \(E_n\), the continuous hitting event and the event that some level-\(n\) sample lies within \(\eta\) of \(a\) can disagree at any sample in \([q,s]\). That is a union of strips, not one strip. A union bound of order \(2^n\eta\) does not tend to \(0\) with \(\eta\) while \(n\to\infty\). The factorisation of \(\{\tau\le s\}\) is the step that later identities for \(\tau_n\), and the reflection principle, take as done. Replace the one-strip sentence by a grid reflection: the overshoot of one bin is at most \(a_n\), and the error is one strip at the endpoint, of width \(O(a_n+\delta_n)\), whose content tends to \(0\). |
| V4-R4-002 | `chapters/ch06-clt.tex:647` | minor | “Cauchy--Schwarz bounds \(\mathbb E[|Z_a|\,|Z_b|\mathbf 1_{|Z_a|>M}]\).” | The products differ on \(\{|Z_a|>M\}\cup\{|Z_b|>M\}\). The written bound is zero on \(\{|Z_b|>M,\,|Z_a|\le M\}\). Add the same bound with \(a\) and \(b\) exchanged. Neither bound should use independence of the coordinates. |
| V4-R4-003 | `chapters/ch06-clt.tex:776` | minor | “Cauchy--Schwarz bounds the difference of the products by \(\sqrt{\mathbb E[W_1^2\mathbf 1_{W_1>M}]\,\mathbb E[W_1^2]}\).” | For \(i\ne j\) the products differ on \(\{W_i>M\}\cup\{W_j>M\}\). The indicator on \(W_j\) is missing. The same bound with the roles exchanged still tends to \(0\). |
| V4-R4-004 | `chapters/ch01-counting.tex:493` | minor | “its only critical point is \(y=1/e\), where \(g=1/e\). Thus \(g(y)\le 1/e\).” | A critical point need not be a maximum. The derivative \(\ln(1/y)-1\) is positive on \((0,1/e)\) and negative on \((1/e,1]\), and \(g(y)\to 0\) as \(y\to 0\). |
| V4-R4-005 | `chapters/ch01-counting.tex:495` | minor | “the corresponding \(y=(r-2)/(n-1)\) would stay away from \(1/e\).” | Two comparisons are missing. First, \(\lvert y-r/n\rvert\le 2/(n-1)\), so a fixed gap in \(r/n\) forces a fixed gap in \(y\) for large \(n\). Second, the display \(p_r\le g(y)+(\ln(n-1))/n\) beats a maximiser only after \((\ln(n-1))/n\) is smaller than the gap in \(g\). For \(r\ge 3\), \(y\ge 1/(n-1)\), so \(\ln(1/y)\le\ln(n-1)\) and that display is valid. |

## Read as holding

The round-1 and round-2 repairs in Chapters 1 through 5, 7 through 10, 12, 14, and the extremal appendix. The strong-Markov tail on \(\{\tau_n\le R\}\), with the level \(N\) fixed before \(A\). The sample-second-moment split into four allowances of \(\varepsilon/4\), with the centred step taken in absolute value. The classical cutoff functions \(f_-\) and \(f_+\) point the right way.

## Not checked

- A LaTeX build.
