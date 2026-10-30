# Colour interiors and typography

The first edition uses one 7 × 10 inch interior in full colour for both PDFs.
The reading PDF prepends the approved front; the print manuscript starts at the
half-title. EPUB and the web readers use matching typography and semantic colours.

## Typography

| Use | Typeface |
| --- | --- |
| Body, proofs and italic passages | EB Garamond |
| Mathematics, including bold Greek vectors | Garamond-Math |
| Chapter/section headings, titles, opener numerals | Cormorant Garamond |
| Labels, running heads, captions | Fira Sans |
| Code and Lean Unicode symbols | DejaVu Sans Mono |

The body is 11.5 pt on 14.75 pt. The full system (geometry, chapter openers, box
families, figure palette, inline fractions) is described in
[design/interior.md](design/interior.md). Font files, licences, provenance
and SHA-256 hashes are bundled in `common/fonts/`; builds use these files rather
than system-installed substitutes. PDF/figure typesetting uses XeLaTeX. EPUB
embeds the original faces; the online reader and the site serve WOFF2 companions
of the same files (Garamond-Math has none). Reading devices
can override EPUB typography.

## Colour roles

| Role | Colour |
| --- | --- |
| Text, headings, labels, teaching-box bar, part page, chapter-opener band | Charcoal `#151516` |
| Rules, diamonds, opener numerals | Coral `#FF8A78` |
| Text-sized coral: label numbers, folios' diamonds, links | Coral deep `#A34232` |
| Formal-box fill | Charcoal at 8% |
| Figures | charcoal, rust, coral, ochre, brown, greys (`common/figure-palette.tex`) |

Text and mathematics remain dark on white. Chapter/section headings and box labels
are charcoal. Formal boxes have an 8% charcoal fill under a 1.2 pt coral rule and
never split; teaching boxes have no fill and exactly one 2 pt charcoal left bar, and
may break. The full frame is hidden rather than painted behind the backgrounds,
preventing stray top/bottom seams at some PDF zoom levels. Figures keep their
sources; their colour names are redefined to the series palette, and captions name
the new colours. Web/EPUB dark themes use brighter accent variants.

The current version-C proof and teaching-box corrections supersede the earlier
Libertinus comparison image in `docs/reviews/`.

## Paperback configuration

The production setting is **Premium color ink / white paper**, 7 × 10 inches,
no interior bleed. Premium colour permits books from 24 pages, including the short
problem books; standard colour starts at 72 pages. The outside cover bleed remains
0.125 inch. Spines use **0.002347 inch per even-rounded print page**, derived from
the actual final print PDF, and the canonical JSON controls generated TeX,
metadata, listings and wraps.

Sources: [KDP cover guidance](https://kdp.amazon.com/en_US/help/topic/G201953020)
and [print options](https://kdp.amazon.com/en_US/help/topic/G201834180).

## Compatibility and verification

The migration preserves mathematical statements and reference identifiers.
Long inline formulas in Volumes 0, 4, 8, 10, 14, 15, P1 and P2 are moved to displays where the
new font metrics require it. One subscript in Volume 12 gains explicit grouping. Shapes’ frieze letter patterns
use upright text lambdas in the sans face, avoiding an unsupported mathematical
italic Unicode lambda in a text font.
Legacy number-system commands work in unbraced scripts; Greek/math bookmark
strings use Unicode equivalents; bold vectors use the font's bold alphabet.
Lean symbols are native Unicode, with complete code-font coverage. Download-PDF
checks resolve XeLaTeX's indirect annotation arrays before comparing the body.

The build rejects missing glyphs, unavailable font shapes, wrong font families,
lost coral/charcoal accents, split/oversized boxes, horizontal/vertical overflow,
unresolved references, wrong page sizes and unembedded/bitmap fonts. Cache schema
6 and shared-input fingerprints invalidate older interiors. Regression tests
include real typesetting of colour/font output, Greek bookmarks, vector notation, Unicode code, whole-box
movement and solution-heading placement.

The typography change itself leaves all 65 protected cover source/assets unchanged
against its starting hash record. The concurrent print-vector upgrade from `788fb50`
is retained in full, including its resolution preflight; this typography update adds
no cover-art or lettering changes. Production wrap width follows the new page count
and paper coefficient.

Browser checks cover loaded EB Garamond/Cormorant/Fira fonts, charcoal headings, readable
dark-mode headings, no page overflow at 320 px and no JavaScript errors.

The publishing suite includes actual-PDF tests for all five teaching-box types
and all three problem-book overrides: one vertical rule, no saturated frame
underpainting and the expected semantic colours, alongside the print-cover
preflight regressions. Complete-library publication also checks every
PDF pair, current print metadata and cover preflight before assembling the release.
