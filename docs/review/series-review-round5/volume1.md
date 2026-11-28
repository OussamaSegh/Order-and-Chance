# Volume 1 — First Principles

**Score: 8/10.**

The round-4 repairs are still the sentences they were written to be. The eight comparisons were re-opened and hold. Five local slips remain. None of them is a broken proof.

**Counts.** 0 critical, 0 major, 5 minor. `V1-R5-001` through `V1-R5-005`.

**Round-4 follow-up.** 8 resolved, 0 partial, 0 open, 0 regressed.

**How this was read.** Book order in `volume1-first-principles/main.tex`, on main at `2612a86c`. Every chapter file was read, including exercises, hints, solutions, and captions. Each new row was opened at the cited line. No full LaTeX build was run.

## Issues

Paths are relative to `volume1-first-principles/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V1-R5-001 | `chapters/ch02-counting.tex:724` | minor | “the finite alternating formula \(1-1/2!+1/3!-\cdots\), its identification with \(1/e\)”. | The body at line 234 identifies the derangement share \(\sum(-1)^k/k!\) with \(1/e\). The series written here is the complementary share. For four cards the text already computes \(1-1/2!+1/3!-1/4!=15/24\), and the complement \(9/24\) is the derangement count. The endless meeting share tends to \(1-1/e\). |
| V1-R5-002 | `chapters/ch02-complex-roots.tex:985` | minor | “so \(n\) divides \(2m\). Since \(n\) is odd, \(n\) divides \(m\).” | This is Euclid’s lemma, and the next sentence cites it only after \(m\) is known to be even. The first step needs the same citation: \(\gcd(n,2)=1\) and \(n\mid 2m\) give \(n\mid m\). |
| V1-R5-003 | `chapters/ch02-complex-roots.tex:985` | minor | “That odd representative is coprime to \(2n\) exactly when it is coprime to \(n\).” | An odd integer is coprime to \(2\). With \(n\) odd, it is coprime to \(2n\) exactly when it is coprime to \(n\). |
| V1-R5-004 | `chapters/ch04-inequalities.tex:479` | minor | “The limit as \(p\to-\infty\) is the reciprocal identity applied to \(1/x_i\), whose maximum is \(1/\min x_i\).” | The identity \(M_p(x)=1/M_{-p}(1/x)\) is already on the page. As \(p\to-\infty\), the positive-exponent limit sends \(M_{-p}(1/x)\) to \(1/\min x_i\), so \(M_p\) tends to \(\min x_i\). The sentence does not say that. |
| V1-R5-005 | `chapters/ch06-integrals-taylor.tex:119` | minor | “At zero, \(\frac{\sin x}{x}\) extends continuously by the value \(1\).” | The sequences chapter records that \(\sin'(0)=\cos 0=1\) is the statement \((\sin x)/x\to 1\). The integral paragraph uses the limit and does not point there. |

## Round-4 follow-up

Division writes \(m=bt\). The harmonic odd term is \(2m+1\), and \(m\) is not the sum index. The Bertrand derivatives are negative on \([2,\infty)\). The Gamma exponent tends to \(-\infty\). The Gaussian logarithms use the mean-value clause on a closed segment. The power-mean factor is \(\exp((\ln\lambda)/p)\). The even step of the cyclotomic order cites Euclid. The three lamp classes are disjoint.

## Not checked

- A LaTeX build.
- EPUB rendering.
