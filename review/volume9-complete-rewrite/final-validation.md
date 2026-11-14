# Final local validation

Book sources: `fb4502e3acda521b598c5bc3cd5e46e2f0e028d0`.
Starting main: `9cd86c15bd386d59e7a1c6f96fb0ea5ed808c26b`.
The book grows from **385 to 511 print pages** (126 pages, 32.7%), through
rewritten explanations and the requested additions. Typography is unchanged.

## Actual commands and results

| Command | Result | Receipt |
| --- | --- | --- |
| `./build.sh --pdf-only volume9-shapes` | Exit 0; 511 print pages | [PDF build](final-pdf-build.txt) |
| `./build.sh volume9-shapes` | Exit 0; 511 print pages; EPUB and reader exported | [Full build](final-full-build.txt) |
| `python3 -m unittest discover -s tools -p 'test_*citation*.py'` | Exit 0; 20 tests pass | [Citation tests](final-citation-tests.txt) |
| `python3 tools/cross_volume_citations.py` | Exit 0; 5,118 numbered statements match | [Cross-volume check](final-cross-volume-citations.txt) |
| `python3 review/volume3-internal/registers.py` | Exit 0; 1,177 accepted-internal, 19 pre-existing pending unchanged | [Register](final-volume3-registers.txt) |
| `python3 review/volume9-complete-rewrite/check_preservation.py --require-additions` | Exit 0 | [Preservation](final-preservation.txt) |
| `python3 review/volume9-complete-rewrite/check_additions.py` | Exit 0 | [Additions](final-additions.txt) |
| `python3 review/volume9-complete-rewrite/check_prose_coverage.py` | Exit 0 | [Prose coverage](final-prose-coverage.txt) |
| All 12 existing `review/volume9-rewrite/check_*.py` scripts | Exit 0; numerical illustrations, not proofs | [Numerical results](final-numerical-illustrations.txt) |
| `python3 tools/check_epub_media.py 'dist/Volume 9 - Shapes.epub'` | Exit 0 | [EPUB media](final-epub-media.txt) |
| EPUB archive, resource, fragment and spine audit | Exit 0 | [Links](final-epub-links.json), [package](final-epub-package.json) |
| `git diff --check` | Exit 0 | Rechecked before committing this record |

Both builds enforce layout, glyph/font, reading/print provenance, bleed,
approved cover family and cover geometry checks. The final TeX log has
**zero overfull boxes and zero undefined references or citations**; see
[the log check](final-layout-log.json). All 648 whole boxes fit; the largest
is 456.1 pt high. Pandoc reports its existing `\rm` conversion warnings;
the EPUB's separate XeLaTeX formula renderer supplies the checked images.
These warnings are not reported as absent.

## Preservation and completeness

All **544 original built labels**, **213 numbered part/chapter/section entries**,
**55 original printed figure captions**, **57 original figure files** and
**two cover-art sources** are preserved. All original numbered formal
environments remain in their order: 302 statements, including unlabelled ones.
All 200 original exercises remain first in their units.

Each of the 22 units adds exactly two figures and four exercises: **44 figures
and 88 exercises**, with fresh unique labels, difficulty ratings, useful hints
and full idea/writeup solutions. The complete final review accounts for
245 proofs, 288 hints and 288 solutions. The reference scan finds no proof,
solution or hint citing a later series volume; the only remaining explicit
forward references in those environments are two illustrative figures.
See [the prerequisite audit](final-prerequisite-audit.json) and the full
[statement review](final-statement-review.json).

The prose comparison includes short sentences and finds no retained normalized
explanatory sentence of at least two prose words in any unit. Literal quotations,
original figure blocks and bibliography are protected. One-word mathematical
introducers are reported separately. This heuristic is a coverage aid; the
complete source reread supplies the editorial review.

## Artifacts and rendered checks

The print PDF has **511 pages**, each 513 × 738 pt (7.125 × 10.25 in with
approved bleed). The reading PDF has **512 pages**, including its front cover.
The wrap uses the actual print count, rounded to 512 for spine geometry:
**1.2017 in**. Fonts, cover artwork and assigned identifiers remain unchanged;
the unassigned paperback ISBN is blank and was inspected on the copyright page.
Exact local artifact sizes, hashes and input Git objects are in
[the artifact record](final-artifacts.json).

The EPUB is **31,586,815 bytes**, below 50 MB. Its **99 plates** are responsive
1800-pixel PNGs; **15,168 formula occurrences** use 8,322 unique formula images
with em sizing and baseline depth. All **16,454 local links, media references
and fragments** resolve. All 8,465 manifest items exist, manifest and document
IDs are unique, and all 31 spine entries resolve to XHTML. The mimetype is first
and uncompressed; navigation is present.

All 44 added figures were inspected on their 34 rendered pages, in addition to
the earlier individual unit inspections. Captions, labels, direction, scale and
placement were checked against the mathematics. Covers, copyright, both photo
pages and the final repaired proof pages were inspected. Representative actual
EPUB pages were inspected in Chromium, including the new local arguments,
Hesse caption, exercise/hint/solution format and both credited photographs.
See [the visual record](final-visual-check.md) and
[figure page inventory](final-figure-page-inventory.json).

Two verified public-domain photographs have source URLs, attribution and
publication evidence in [CREDITS.md](../../volume9-shapes/photos/CREDITS.md),
with credits repeated beside their first substantive discussions. Their native
print resolutions are **597.59 ppi** and **1626.08 × 1626.07 ppi**; see
[the measurements](final-photo-resolution.json).

## Review and delivery provenance

The author explicitly directed **“You review and merge.”** Codex performed a
separate final mathematical/editorial review phase itself. All findings
R01–R20 are repaired; the unit reports and findings register identify fixing
commits. No independent second-reader certification is claimed.

This record describes local validation of fixed book inputs. Exact final-head
CI, normal-merge and exact-merge publication receipts belong to the delivery
record on [PR #243](https://github.com/OussamaSegh/Order-and-Chance/pull/243).
No Amazon KDP upload is part of this work.
