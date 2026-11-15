# Final local validation

Starting main: `59014a9aad3454ad60786c6549c81fcac88df9df`.
Book-source SHA: `1750bf575024a4fbc3564019018e42e94f4a5384`.
Branch: `codex/volume10-complete-rewrite`. Actual folder: `volume10-abstraction`.
Documentation-only acceptance commits do not change the book-input fingerprint:
`11d6c0d612fe57acc86e26f576c4c5a846c3630b5f4f8cdcad0cbe8c06ca021b`.

Both exact required commands completed with exit 0:

- `./build.sh --pdf-only volume10-abstraction` (`final-pdf-build.txt`).
- `./build.sh volume10-abstraction` (`final-full-build.txt`).

Toolchain activation: `source /workspace/order-chance-system/activate.sh`, with
`/workspace/v10-build-tools` on PATH for declared pngquant/oxipng dependencies.
The finished print interior is 279 pages (reading PDF 280 including its cover).
No overfull boxes, undefined references/citations or missing characters occur.
Spine production uses 280 even-rounded pages, 0.6572 inches; wrap 14.9072 by
10.25 inches. Print canvas is 7.125 by 10.25 inches with approved bleed. The
paperback ISBN remains blank. The 279-page result falls below the 300-page aim;
no padding or typography compression was used. Full artifact sizes, hashes,
metadata, source hashes and page geometry are in `final-artifacts.json`.

Final source checks, all exit 0:

- `python3 -m unittest discover -s tools -p 'test*citations*.py'`: 20 tests.
- `python3 tools/cross_volume_citations.py`: 5,162 numbered statements.
- `python3 review/volume3-internal/registers.py`: 1,177 accepted, 19 pre-existing pending.
- `python3 review/volume3-internal/inventory.py --check`.
- `python3 review/volume10-complete-rewrite/check_preservation.py --require-additions`:
  270 original labels/captions, 114 structural numbers, 12 original figure files,
  original figure blocks and protected artwork preserved.
- `python3 review/volume10-complete-rewrite/check_additions.py`: exactly two
  figures/four solved exercises in each of eleven chapters (22/44); no appendix.
- All eleven existing numerical illustration scripts: exit 0; recorded separately
  in `postrewrite-numerical-illustrations.txt` (mathematical proofs reviewed separately).
- `python3 -m unittest discover -s tools -p 'test_*.py'`: 641 tests, no skips,
  exit 0 (`postrewrite-publishing-tests.txt`; publishing tools unchanged afterward).
- `git diff --check`: exit 0 before final acceptance commit.

EPUB: 16,432,344 bytes, below 50 MB. `inspect_epub.py` exits 0: CRC passes,
5,281 manifest items, 19 spine items, 20 XHTML documents, unique IDs, all 10,449
local links/media/fragment targets resolve. `python3 tools/check_epub_media.py
'dist/Volume 10 - Abstraction.epub'` exits 0. The complete build rasterizes 34
mathematical plates and 9,679 formulas (5,210 unique). See `final-epub-package.json`,
`final-epub-media.txt` and `final-visual-check.md` for package and actual rendering
checks. Captured text logs have trailing whitespace normalized only.

Separate mathematical/editorial reviews and correction commits are indexed in
`corrections-and-review-index.md`; all findings are fixed. These are separate AI
reviewers, not human second-reader certification. Baseline, interrupted builds,
failed builds and earlier CI failures remain distinct historical evidence.

Final-head CI, normal merge and exact-merge release/Pages downloads are recorded
in the live PR receipt below after they occur; local checks alone do not assert
remote publication. Keeping remote receipts on the PR avoids a source-change
cycle after publication. No Amazon KDP upload.

https://github.com/OussamaSegh/Order-and-Chance/pull/245#issuecomment-6892058253
