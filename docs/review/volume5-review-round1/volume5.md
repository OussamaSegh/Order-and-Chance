# Volume 5 — Calculation

**Score: 7/10.**

**Counts.** 0 critical, 2 major, 8 minor. `V5-R1-001`, `V5-R1-002`, and `V5-R1-101` through `V5-R1-108`.

**How this was read.** Every chapter in `volume5-calculation/main.tex`, including the included Borwein file, exercises, hints, solutions, and captions, on main at `b0ede124`. The rows below were opened at the cited lines. Figure colours were compared with `common/figure-palette.tex` where a caption names an ink. No full LaTeX build was run. `bbp-borwein.tex` is included from the integrals chapter; it is not a separate unnumbered book.

## Issues

Paths are relative to `volume5-calculation/`.

| ID | Location | Severity | Evidence | Suggested fix |
| --- | --- | --- | --- | --- |
| V5-R1-001 | `chapters/ch07-fft.tex:18` | major | “The right points are the \(n\)th roots of unity”. | The think box multiplies polynomials of degree \(n-1\). The product has degree at most \(2n-2\), and the box itself asks for \(2n-1\) points. Corollary `cor:polymul` later uses a length strictly larger than the sum of the degrees. The answer should name at least \(2n-1\) roots of unity. |
| V5-R1-002 | `chapters/ch12-agm.tex:1296` | major | “For \(i\le h\), \(k_i\in[k-h,k]\)”. | False. In \(N=2^{k_1}+\cdots+2^{k_r}\) the index \(i\) counts set bits. For \(N=2^k+1\) and \(h=2\), the second exponent is \(0\). Blocks with \(k_i<k-h\) have total weight at most a constant times \(2^{-h}\). Only the remaining blocks are large enough for de Moivre–Laplace. |
| V5-R1-101 | `chapters/ch04-integrals.tex:103` | minor | “choose a closed bounded \([u,v]\) with \(\int g\le\varepsilon\) and \(\int h\le\varepsilon\)”. | The continuity half assumes only the dominant \(g\). The function \(h\) is introduced for the derivative. The cutoff for continuity uses \(g\) alone. |
| V5-R1-102 | `chapters/ch04-integrals.tex:605` | minor | \(\log\prod_{j=1}^M\frac{2j}{2j-1}\cdot\frac{2j}{2j+1}\). | As written, the second factor sits outside the product, so \(j\) is free. The sum of logarithms is the logarithm of the full Wallis product, which tends to \(\log(\pi/2)\). |
| V5-R1-103 | `chapters/ch06-fourier.tex:20` | minor | “Its height is about \(1.179\) on the square wave, for every \(N\).” | The limit is \((2/\pi)\mathrm{Si}(\pi)\approx 1.179\). The first partial sum reaches \(4/\pi\approx 1.273\). The Gibbs theorem states the limit. The same overstatement should not say “for every \(N\)”. |
| V5-R1-104 | `chapters/ch07-fft.tex:123` | minor | “if \(l\le d\) and \(k-l\le e\), then \(k\le d+e<n\)”. | That keeps unwrapped indices below \(n\). If \(k-l<0\), the wrapped index is \(k-l+n\ge n-d>e\), so the padded coefficient is zero. |
| V5-R1-105 | `chapters/ch10-zeta.tex:160` | minor | “\(t^{s/2-1}=(\pi n^2)^{1-s/2}u^{s/2-1}\). The integral becomes \((\pi n^2)^{-s/2}\Gamma(s/2)\).” | The substitution \(u=\pi n^2 t\) contributes \(\mathrm dt=\mathrm du/(\pi n^2)\). That factor changes the power from \(1-s/2\) to \(-s/2\). The identity is right. |
| V5-R1-106 | `chapters/ch10-zeta.tex:458` | minor | “absolutely for \(\operatorname{Re}s>2\), since \(\tau(n)\le n\) and \(\sigma(n)\le n^2\)”. | \(\sigma(n)\le n^2\) gives \(\sum n^{2-\sigma}\), which needs \(\operatorname{Re}s>3\). Absolute convergence on \(\operatorname{Re}s>2\) is the product \(\zeta(s)\zeta(s-1)\) from Proposition `prop:dirmult`. |
| V5-R1-107 | `chapters/ch11-asymptotics.tex:633` | minor | “\(\frac{m(m+1)}{2}\le n\), because \(m^2\le n\) and \(m\le n\)”. | For \(m=\lfloor\sqrt n\rfloor\ge 1\), \(\frac{m+1}{2}\le m\), so \(\frac{m(m+1)}{2}\le m^2\le n\). |
| V5-R1-108 | `chapters/ch02-generating.tex:1021` | minor | “Only the minus sign is a power series.” | The numerator \(1-x-\sqrt{1-2x-3x^2}\) has constant term \(0\). The coefficient of \(x\) must also be \(0\) before the quotient by \(2x^2\) is a formal series. |

## Read as holding

Finite sums, Abel summation, Bernoulli numbers, and Faulhaber. The exponential formula, the pentagonal recurrence, and the values \(p(5)=7\), \(p(10)=42\). Stirling’s formula for real \(x\), the Beta integral, and \(\Gamma(1/2)=\sqrt\pi\). Dirichlet’s theorem, Fejér, Parseval, and the Gibbs limit as a limit. The FFT theorem, the butterfly, and the number-theoretic transform, apart from the think-box length and the wrapped index. Riemann’s functional equation once the substitution factor is written, the Euler product, and \(\sum 1/p=\infty\). Gauss’s AGM identity, the lemniscate constant, and Brent–Salamin, apart from the binary-digit block.

## Not checked

- A LaTeX build.
- Captions that do not name a colour.
