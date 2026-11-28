# V7-R1-019 second review

Verdict: **approve**. The fix was not changed.

Reviewed the fix at `64636e7dea072c84fe5e87248647fb34c5457860`.

## What was checked

The issue is real. The index entry "Tychonoff, 1930" points at `\ocindexpage{thm:tychonoff}`. That label sits on the theorem headed "Tychonoff, 1935". The chapter text says that 1930 is the product of segments and that 1935 is the general product. The index has no separate 1930 entry.

The diff changes the year in that one item from 1930 to 1935. The hardcoded number "Theorem 4.11" and the label are untouched. The entry stays between "tower property" and "Ulam". No caption, diagram, or font command is involved. The file is `volume7-spaces/chapters/index.tex` only. The nineteen branches merge onto `main` with no conflict.

## What was not checked

`./build.sh` was not run. Volume 7 was not compiled. GitHub Actions was not opened. The shared counter was not recounted, so this note does not reconfirm that the printed number is 4.11. The 1930 and 1935 papers were not opened. The maximality proof of the theorem was not re-derived.

## Issue log

| Problem | Resolution |
| --- | --- |
| None. | The fix stands. This note is the only addition. |
