# Volume 4 photograph and figure provenance

Photographs are files downloaded from a named source. Computed diagrams are
TikZ. Neither kind is a generated scene. A writer's check of a diagram is not
an independent review.

## Photograph used

| Local file | What it shows | Source | Licence | SHA256 |
| --- | --- | --- | --- | --- |
| `galton-box.jpg` | A physical Galton board: pins, and one load of balls sitting in the bins. 1920×2880 JPEG, resized only in the sense that Wikimedia's 1800-pixel thumbnail service returned 1920×2880; no crop and no redraw. Saved 6 November 2026. | Rodrigo Tetsuo Argenton, 19 December 2016, for the Matemateca, Institute of Mathematics and Statistics, University of São Paulo. Wikimedia Commons file `Galton_box.jpg`. Page: https://commons.wikimedia.org/wiki/File:Galton_box.jpg . Download: `https://commons.wikimedia.org/wiki/Special:FilePath/Galton_box.jpg?width=1800` | Creative Commons Attribution-ShareAlike 4.0 International, https://creativecommons.org/licenses/by-sa/4.0/ . The required credit is Matemateca (IME/USP) / Rodrigo Tetsuo Argenton. Share-alike applies to this photograph, not to the text of the book. No endorsement is implied. | Downloaded bytes `1ab6ce4420f678ff05bc46b653e482f52dd83ea585668aaf26417bda06e2c697`. File in the tree `6f150151d4b80d3bab60dba1bc0edeb8cc4b6f30af8201e3c79b3ac43ecf7e78` after a JPEG re-save at quality 92 with no pixel resize. |

The pile is the balls that were in the machine when the photograph was taken.
It is not a computed binomial histogram and it is not an observation used in a
proof.

## Photograph considered and not used

Wikimedia file `Galton_Quincunx,_1933_-_Museum_of_Science_and_Industry_(Chicago)_-_DSC06712.JPG`,
by Daderot, 22 August 2014, CC0 1.0, https://commons.wikimedia.org/wiki/File:Galton_Quincunx,_1933_-_Museum_of_Science_and_Industry_(Chicago)_-_DSC06712.JPG .
Original SHA256 `e8af9e3ef9fbe8d8da61b33dc1ffd951c2053994a02d7d6627b75a2f120c6f32`.
The museum plaque in the frame reads “The Galton Quincunx, 1933”, but the
painted curve labels on the glass are reversed relative to that plaque, and
the case does not show a bin of balls. It was not placed in the chapter.
The file is not in the tree.

`File:Brownian_motion_gamboge.jpg` was not used. The Commons page describes a
1985 textbook sketch of a density gradient, not a photograph of paths, and the
public-domain claim there is not a clean licence for that plate.

## New computed diagrams

| File | Claim | Check |
| --- | --- | --- |
| `figures/ch01-digits.tex` | The first binary digit splits \([0,1)\) into two intervals of length \(1/2\). The next digit splits the left one into two intervals of length \(1/4\). | The lengths are \(2^{-n}\), as in Proposition `prop:bits`. |
| `figures/ch02-poissonbars.tex` | Masses of \(\mathrm{Bin}(20,1/10)\) and \(\mathrm{Poisson}(2)\) at \(k=0,\ldots,8\). | Direct evaluation, 6 November 2026. At \(k=0,1,2\): binomial \(0.12158\), \(0.27017\), \(0.28518\); Poisson \(0.13534\), \(0.27067\), \(0.27067\). Not a sample. |
| `figures/ch08-reflectstep.tex` | One walk of length 8, first hit of height 2 at time 2, and the path with only that initial segment reflected. | Heights \(0,1,2,3,2,1,2,1,2\) and \(4,3,2,3,2,1,2,1,2\). This is the first step of the proof of Theorem `thm:rwreflect`, not the later translation and sign flip. |

Older plates already in `figures/` were not redrawn.
