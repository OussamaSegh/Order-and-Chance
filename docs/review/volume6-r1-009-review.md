# V6-R1-009 second review

Verdict: **changes made**. The caption fix stands. The figure label did not.

Reviewed the caption fix at `2ee2109c21a35258c477003d752082b404a36cfc`. The label change is in the commit that adds this note.

## What was checked

The issue is real. On \([x,\lambda x]\) the region between the horizontal line at height \(\lambda cx\) and the line \(ct\) has Euclidean area
\[
\int_x^{\lambda x}(\lambda cx-ct)\,\mathrm dt=\frac12 c(\lambda-1)^2 x^2.
\]
That grows like \(x^2\). The scale-free quantity is the weighted integral. The substitution \(t=ux\) gives
\[
\int_x^{\lambda x}\frac{\lambda cx-ct}{t^2}\,\mathrm dt=c\int_1^\lambda\frac{\lambda-u}{u^2}\,\mathrm du,
\]
which does not depend on \(x\). For \(c=1\) and \(\lambda=2\) the value is \(1-\log 2\approx 0.30685\), and a trapezoid rule at \(x=10\), \(x=100\), and \(x=7\) reproduced it. For \(c=3\), \(\lambda=2\), \(x=10\) the area integral reproduced \(150\), which is \(\frac12\cdot 3\cdot x^2\). This is the lower bound in the proof of the monotone lemma. The lemma itself was not edited.

The new caption states that area and says the integral of \((\lambda cx-ct)/t^2\) over \([x,\lambda x]\) does not depend on \(x\). No font command, size, or colour was added to the caption. The diff of that commit is one caption in `volume6-crossroads/chapters/ch05-pnt.tex` only.

The picture was left with the node
`\node[MidnightBlue] at (3.05,2.85) {fixed area};`
inside the shaded block. After the caption correction, that wording says the block has fixed area, which the caption denies. The wording had to change so the picture and the caption name the same fact. The text is now `grows like $x^2$`. The node options, the coordinate `(3.05,2.85)`, and the picture's `font=\footnotesize` are unchanged. No other line of `volume6-crossroads/figures/ch05-new-bump.tex` was edited.

## What was not checked

`./build.sh` was not run. Volume 6 was not compiled. No TeX binary was on this machine, so the figure was not typeset. GitHub Actions was not inspected. Placement of the longer words was not measured on a page. The node anchor was not moved.

## Issue log

| Problem | Resolution |
| --- | --- |
| The node on the shaded block still read "fixed area" after the caption said that area grows like \(x^2\). | Changed only the node's text to `grows like $x^2$`. Font, size, colour, and position were not changed. |
