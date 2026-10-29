# Cover design — approved 29 October 2026

The fifteen fronts were approved as rendered. `tools/series_cover.py` is the
cover pipeline: it writes each illustration, the shared lockup and the cover
notes, and CI checks that those files match the generator. Optical shifts are
baked in `tools/covergen/centring.json` (measured on the 1121×1600 approvals,
threshold one pixel). CI does not remeasure.

## Front

The canvas is 6 by 60/7 inches, the 7:10 trim, and print scales it uniformly
onto the 7×10 panel. Ground is charcoal `#151516` with the restrained 35% paper
grain. The double coral frame is the original identity drawing, clipped to the
frame ring.

- Series title **ORDER AND CHANCE**, Cormorant Garamond SemiBold, spaced capitals, set to a width of 4.66 in.
- Series subtitle *The Hidden Architecture of Mathematics*, Cormorant Medium Italic.
- Coral rules with a diamond. The lower rule is at 2.95 in on every volume; the upper rule is at 6.90 in.
- The illustration is centred between the rules. Volume 1 is the Collatz tree on the first 8,000 integers. Volumes 2–15 are the constructions in `tools/covergen/arts.py`.
- **VOLUME N** in Fira Sans Light.
- The volume title in Cormorant Garamond Regular, 42 pt, mixed case.
- The italic volume subtitle, then **SEGHAIER Oussama** in Fira Sans Light.

Colours: title `#FDF8F5`, subtitle `#F9F8F8`, small type `#F4F3F4`, coral `#FF8A78`.
The faces and their OFL licences live in `tools/assets/fonts/`. Builds do not
use the TeX bundle’s copies.

## Back

The back is the same ground, grain and frame. The masthead repeats the series
name, the italic subtitle and a shorter diamond rule, then the volume number,
title and subtitle in the same faces at a smaller size. The blurb is the
volume’s existing `blurb.tex`, set ragged in Cormorant Medium at 10.4/14 pt,
one measure on every book, and it stops above the barcode band. The author line
sits at the lower left, clear of that band. A second copy of the illustration
is not drawn there: the press export unions every transparent region, and a
second glow would have forced the lettering into the raster.

## Spine

Text reads top to bottom. On every book that is long enough for a spine line
(80 pages, as before), four items sit at fixed distances from the head and the
tail, in one size: the series name, the volume number in coral, the title, and
the author. The width still comes from the premium-colour coefficient
0.002347 in per even-rounded print page. Trim, bleed and paper are unchanged.

## Notes

`common/cover-notes.json` is the source for the copyright-page credit, the
closing colophon *About the Cover*, the library card and
[COVER-NOTES.md](COVER-NOTES.md). Each note says what the picture is, where it
comes from, why it is on that volume, and that the book’s TikZ generator
computed it.
