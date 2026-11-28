# V6-R2-005 second review

Verdict: **approve**. The fix was not changed.

Typography: this is a data correction. The upper block on the prime \(3\) was filled with the \(p^3\) category’s ink. The fix fills it with `MidnightBlue!28`, the ink the same figure already uses for multiples of \(p^2\). No style definition, font, size, or position changes. It does not need a separate decision on typography.

Reviewed the fix at `35fa34c8427c937d5fcead297c924e594602011f`.

## What was checked

The issue is real. The exponent of \(p\) in \(10!\) is \(\lfloor10/p\rfloor+\lfloor10/p^2\rfloor+\lfloor10/p^3\rfloor\). For \(p=3\) that is \(3+1+0\). The file’s own comment records the layers \((3,1)\). One vertical unit is \(0.48\). The lower rectangle runs from \(0\) to \(1.44=3\cdot0.48\) and is `BurntOrange`. The upper rectangle runs from \(1.44\) to \(1.92\), one unit, and was `MidnightBlue`.

`common/figure-palette.tex` sets `MidnightBlue` to `#151516` and `BurntOrange` to `#FF8A78`. The caption calls coral the multiples of \(p\), the lighter charcoal the multiples of \(p^2\), and the dark block the multiples of \(p^3\). The legend in this picture uses the same three inks, in that order: `BurntOrange`, `MidnightBlue!28`, `MidnightBlue`. The stack for \(2\) already follows the legend: `MidnightBlue!28` on the layer of height \(2\cdot0.48\), and `MidnightBlue` on the top unit. There is no multiple of \(27\) up to \(10\), so the upper block on \(3\) is the one multiple of \(p^2\).

The fix changes only the fill of `(1.55,1.44) rectangle (2.60,1.92)`, from `MidnightBlue` to `MidnightBlue!28`. That token is already the fill on the \(p^2\) layer of the prime \(2\) and on the legend swatch for multiples of \(p^2\). The rectangle coordinates, the rules, the nodes `$3$`, `$1$`, and `$4$`, the `font=\footnotesize` on every node, and the caption in `ch01-mertens.tex` are unchanged. No colour is defined or redefined.

The diff against `main` at `24ef1a84c134be92500e6704775cdc074298ae3f` is that one fill key in `volume6-crossroads/figures/ch01-tenfactorial.tex`. No numbered environment, label, or counter is added or removed. The counts \(3\), \(1\), and \(4\) were checked by the floors above; they are separate from the ink.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled, and the figure was not typeset. No GitHub Actions log was read. The rendered shade of `MidnightBlue!28` was not measured on a page. The mix is the one already drawn for the prime \(2\).

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The block uses the existing \(p^2\) ink. This note is the only addition. |
