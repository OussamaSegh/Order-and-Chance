# Volume 4 Phase 3 — figure audit

**Date:** 10 November 2026.
**Reviewer:** the designated validator (an AI reviewer). This is not an external mathematical referee.
**Baseline:** `main` `2655cf5ac02c0a1c510c0da13f8c6b223c4d9c5f`.
**Method:** source inspection of every `\fig` call, its TikZ, and its caption. Concrete numbers were recomputed. This pass did **not** open a rendered PDF or EPUB, so it does not close the rendered-plate gate.

The manuscript calls **41** distinct figure files. `tools/test_volume4_route.py` now pins that set. Extra files under `volume4-chance/figures/` are not inputs. They are listed at the end and are not release blockers.

## Disposition of the 41 plates

Source mathematics and correspondence with the caption: **PASS** for every plate below, after the three ink-word repairs in this phase. Those three were FIX REQUIRED on the baseline and are corrected in the Phase 3 branch. Rendered inspection of the corrected plates remains open.

| Plate | Printed home | Source disposition |
| --- | --- | --- |
| `preface-tails` | Preface | PASS. Rust widths 4, 2, 1, 0.5 on a bar of width 8 are \(1/2,1/4,1/8,1/16\). |
| `ch01-digits` | Ch. 1 | PASS. Left half of \([0,1)\) splits into two intervals of length \(1/4\). |
| `ch01-ballot` | Ch. 1 | PASS. The opening that hits 0 reflects through the first step; the routes agree afterwards. |
| `ch01-tuesday` | Ch. 1 | PASS. Recomputed on the TikZ: union of the highlighted cross is \(14+14-1=27\), the rust two-boy cells are \(7+7-1=13\), and \(196-27=169\) cells stay pale. |
| `ch01-bertrand` | Ch. 5 (geometric) | PASS. The three classical models are the arc \(1/3\), the distance \(1/2\), and the area \(1/4\). |
| `ch01-buffon` | Ch. 5 (geometric) | PASS. The needle and the distance to the nearer ruling match the caption's construction. |
| `ch02-lawmap` | Ch. 2 | PASS. HH, HT, TH, TT map to \(2,1,1,0\) with masses \(1/4,1/2,1/4\). |
| `ch02-poissonbars` | Ch. 2 | PASS. \(\mathrm{Bin}(20,1/10)\) and \(\mathrm{Poisson}(2)\) at \(k=0\) are \(0.9^{20}=0.121576\ldots\) and \(e^{-2}=0.135335\ldots\), matching the caption's five-decimal figures. |
| `ch02-cycles` | Ch. 2 | PASS. Eight bars are \(1/k\) for \(k=1,\ldots,8\). |
| `ch02-couponstages` | Ch. 2 | PASS. Means \(1+3/2+3=11/2\). |
| `ch03-lawpoly` | Ch. 3 | PASS. Tickets \(0,1,1,2\) give coefficients \(1/4,1/2,1/4\). |
| `ch03-familytree` | Ch. 3 | PASS. One childless branch and one branch of two, in the \(0\)-or-\(2\) model. |
| `ch03-cobweb` | Ch. 3 | PASS. Left offspring law has mean \(3/4\) and only fixed point \(1\). Right law has mean \(5/4\) and smaller root \(1/2\). |
| `ch03-contour` | Ch. 3 | PASS. Nine vertices, 16-step contour, first return at step 6, Dyck factors of semilength 2 and 5. |
| `ch04-chernoff` | Ch. 4 | PASS. Chebyshev bars \(1/4\), \(1/16\), \(1/40\). Hoeffding bars \(e^{-2}\), \(e^{-8}\), \(e^{-20}\). The \(n=1000\) rust bar is too short to see, as the caption says. |
| `ch04-squaregaps` | Ch. 4 | PASS. Gaps \(5,7,9\) between squares \(4,9,16,25\). |
| `ch04-bernstein` | Ch. 4 | PASS. At \(x=1/2\), \(\mathbb E|S/4-1/2|=3/16=0.1875\), labelled \(0.188\). The \(n=16\) and \(n=64\) errors round to \(0.098\) and \(0.050\). The V is drawn in literal black. |
| `ch05-densityarea` | Ch. 5 | PASS. \(\int_{1/4}^{3/4} 2y\,\mathrm dy=1/2\). |
| `ch05-polar` | Ch. 5 | PASS. The shaded cell is \(r\in[3,4]\), \(\theta\in[30^\circ,45^\circ]\). |
| `ch05-inversecdf` | Ch. 5 | PASS. The median of the unit exponential is \(\ln 2\). |
| `ch05-cantor` | Ch. 5 | PASS. Stages keep the outer thirds. |
| `ch06-sums` | Ch. 6 | PASS. Bars at \(z=(2k-20)/\sqrt{20}\) have area \(\binom{20}{k}2^{-20}\). |
| `ch06-lindeberg` | Ch. 6 | PASS. Seven rows replace one summand at a time. |
| `ch06-dice-zscore` | Ch. 6 | PASS. \(50/\sqrt{3500/12}=\sqrt{60/7}\approx 2.9277\), labelled about \(2.93\). |
| `ch07-typicalcoin` | Ch. 7 | PASS. Masses \(81/100,9/100,9/100,1/100\). |
| `ch07-prefixtree` | Ch. 7 | PASS. Leaves \(0,10,110,111\) with masses \(1/2,1/4,1/8,1/8\). Mean length \(7/4\). |
| `ch08-reflectstep` | Ch. 8 | PASS. Heights \(0,1,2,1,0,1,0,-1,0\) reflect after \(\tau=2\) to an endpoint \(4\). |
| `ch08-ruinprob` | Ch. 8 | PASS. Fair values \(k/5\). Biased values \((1-2^{-k})/(1-2^{-5})\), and \(16/31\) at \(k=1\). |
| `ch08-chain` | Ch. 9 | PASS. Rows \((1/2,1/2,0)\), \((1/3,1/3,1/3)\), \((0,1/2,1/2)\) against \(\pi=(2/7,3/7,2/7)\) give total variation \(2/7\). |
| `ch09-commonjump` | Ch. 9 | PASS. Block coupling: shared uniform draw with probability \(\varepsilon\), otherwise the residual rows. |
| `ch08-riffle` | Ch. 9 | PASS. Plotted Bayer–Diaconis distances for 52 cards. Values for \(k\le 4\) round to 1 and stay strictly below 1. |
| `ch10-poissonclock` | Ch. 10 | PASS after the ink repair below. Kept marks are a subset of the arrival marks. The picture is a schematic. |
| `ch09-inspection` | Ch. 10 | PASS. The marked time sits in one gap, with age to the left and residual wait to the right. |
| `ch10-queue-rates` | Ch. 10 | PASS after the ink repair below. Rate \(\lambda\) to the right, rate \(\mu\) to the left, no service arrow out of 0. |
| `ch10-upcross` | Ch. 11 | PASS. Sixty steps of size \(\pm 1\). Three completed crossings of \([-1,2]\) end at times 8, 32 and 50. |
| `ch10-polya` | Ch. 11 | PASS. Twenty stored paths, every plotted value in \([0,1]\), each step an integer ball count allowed by the urn. The existing regression checks all 2,920 samples. |
| `ch12-reflection` | Ch. 12 | PASS after the ink repair below. Post-hit coordinates satisfy \(y+(2a-y)=2\) at \(a=1\). Not a Brownian sample. |
| `ch12-ramsey` | Ch. 13 | PASS. The \(K_5\) is two complementary 5-cycles. The heavy triangle is one monochromatic triangle on the second drawing. |
| `ch14-exploration` | Ch. 14 | PASS. Schematic breadth-first layers. The caption does not claim a random sample. |
| `appb-turan-balance` | Appendix B | PASS. \(2\cdot 4=8\) edges against \(3\cdot 3=9\). |
| `extremal-ch08-focusing` | Appendix B | PASS. Schematic of the van der Waerden focusing step, not a colouring of an interval of length \(W(3,3)\). |

## Ink-word repairs

`common/figure-palette.tex` remaps `MidnightBlue` and `blue` to charcoal `#151516`, and `BrickRed` to rust `#A34232`. Three reader-facing labels still said “blue” for charcoal ink.

| Location | Baseline text | Correction |
| --- | --- | --- |
| `figures/ch10-poissonclock.tex` | `blue: an original arrival` | `charcoal: an original arrival` |
| `chapters/ch09-poisson.tex` caption of `fig:poissonclock` | “arrival points (blue)” | “arrival points (charcoal)” |
| `figures/ch10-queue-rates.tex` | `blue: completed service` | `charcoal: completed service` |
| `chapters/ch11-brownian.tex` caption of `fig:bmreflection` | “The charcoal point” and “the blue continuation” | The mark is `\fill[black]`. The original tail is `MidnightBlue`. The caption now says a black point, then the charcoal continuation and the rust continuation. |

Mathematical uses of the words red and blue (Ramsey colourings, the two colours of a ball, Poisson colouring in a solution) are the names of the colours in the argument. They were not changed.

`tools/test_volume4_math_figures.py` locks the corrected ink words.

## Files that are not in the book

These `.tex` files exist and are never passed to `\fig`. No release action. Two unused files have internal defects that do not affect the printed book:

- `extremal-ch08-turan.tex` places two vertices at the same coordinate, so a Turán graph \(T(10,3)\) does not show ten distinct points.
- `ch11-levy.tex` comments that the last polyline is \(F_{10}\), while 512 segments is the previous dyadic stage. Nothing in the picture is labelled \(F_{10}\).

Other unused files: `ch01-reflection`, `ch02-poisson`, `ch02-coupon`, `ch03-tree`, `ch04-aep`, `ch05-boxmuller`, `ch05-simple`, `ch06-local`, `ch07-arcsine`, `ch07-dirichlet`, `ch07-reflect`, `ch07-walks`, `ch08-cycle`, `ch08-knight`, `ch09-irwinhall`, `ch09-mm1`, `ch09-thinning`, `ch10-condorcet`, `ch10-projection`, `ch10-sinc`, `ch11-reflect`, `ch11-tree`, `ch11-zoom`, `ch12-giant`, `ch12-saw`, `ch13-gaps`, `extremal-ch08-circulants`.

## Not claimed

No plate has been accepted from a high-resolution render of the corrected sources. Physical-device reading was not done.
