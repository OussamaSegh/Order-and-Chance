# Publishing a tome on Amazon KDP

`./build.sh` produces two distinct **7 × 10 inch PDFs** and one **EPUB** per tome,
plus the paperback cover and publishing metadata:

| File | What it is | Where it goes in KDP |
|---|---|---|
| `dist/<tome>.epub` | Reflowable eBook with cover, table of contents and copyright page | Kindle eBook > Manuscript |
| `dist/kdp/<tome>-ebook-cover.jpg` | Front cover, 1792 x 2560 px JPEG | Kindle eBook > Cover |
| `dist/<tome>.pdf` | Downloadable reading PDF with the approved front cover followed by the complete interior | Public download; use the print file below for KDP |
| `dist/kdp/<tome>-print.pdf` | Paperback interior without the front cover: 7 x 10 in, no bleed, embedded fonts | Paperback > Manuscript |
| `dist/kdp/<tome>-cover-wrap.pdf` | Back cover, spine and front cover with 0.125 in bleed | Paperback > Cover ("upload a cover you already have") |
| `dist/kdp/<tome>-print-metadata.json` | Actual pages, spine, margins and cover sheet dimensions | Production reference |
| `dist/kdp/<tome>-listing.md` | Title fields, description (at most 4000 characters) and 7 keywords | Kindle eBook and Paperback > Details |

In KDP choose: trim size 7 x 10 in, black ink on white paper, no bleed, matte or glossy cover.
The download page links the publishing files on each tome's card ("Paperback & publishing files").
The spine width is computed for white paper (0.002252 in per page); for cream paper the cover
must be rebuilt with 0.0025 in per page. The `books` release on GitHub carries the same files.

KDP rules followed by the build (checked against the KDP help pages in October 2026):

- Inside (gutter) margin 0.75 in, more than KDP's minimum up to 700 pages (0.375 in to 150 pages,
  0.5 in to 300, 0.625 in to 500, 0.75 in to 700); 0.875 in is used above 700 pages.
  Outside margin 0.6 in (minimum 0.25 in). Chapters open on a right-hand page.
- Page count 24 to 828; the build fails outside that range.
- Cover: width = 0.125 + 7 + spine + 7 + 0.125 in, height = 10.25 in; spine text only from
  80 pages; text kept 0.125 in inside the trim and 0.0625 in inside the spine folds; the
  barcode area (lower right of the back cover) holds the ISBN barcode (EAN-13, `tools/ean13.py`)
  as soon as the tome's `main.tex` sets `\bookisbnprint`; in KDP, say the cover has a barcode.
  Before that it is left empty.
- Fonts: every font is an embedded Type 1 font (no bitmap fonts); links are black in print.
- Publisher: the books are published from the authors' own KDP account with free KDP ISBNs,
  so the imprint is "Independently published". Once KDP assigns a tome's paperback ISBN, put it
  in that tome's `main.tex` with `\renewcommand{\bookisbnprint}{978-...}`.
- Author: SEGHAIER Oussama only (the user's decision, 2026-10-26); no "Draft"; no link to the
  repository anywhere in the books or on the covers.
- At upload, KDP asks whether the content is AI-generated: answer yes (text and covers).

## Conventions for every tome

- `main.tex` keeps its first line `% epub-title: Order and Chance. Tome N: Title`; the build
  reads the tome number and title from it (numbers may be `0`–`15` or `P1`–`P3`).
- `\maketitle` builds the front matter of a published book automatically: half-title, series
  page (from `common/series.tex`), title page and copyright page (`common/frontmatter.tex`).
  The order in `main.tex` stays `\frontmatter \makecover \maketitle` then the preface, then
  `\tableofcontents`.
- Series-wide settings (copyright line, licence, authors, repository) live in
  `common/frontmatter.tex` only. Per-tome settings go in `main.tex` after
  `\input{../common/preamble}`: `\renewcommand{\bookedition}{...}`,
  `\renewcommand{\bookisbnprint}{...}`, `\renewcommand{\bookisbnebook}{...}`.
- KDP listing: `<tome>/kdp.md`, with a `# Description` section (plain text, at most 4000
  characters, in the voice of the series: what the tome is about, its summits, why it is
  beautiful, what comes with it) and a `# Keywords` section (seven lines, each at most
  50 characters, not repeating words of the title or series, no claims such as "bestseller").
  `tools/listing.py` checks the limits and fails the build if they are broken; without
  `kdp.md` the listing uses the back-cover text and leaves the keywords to be written.
- The reading PDF starts with its approved front cover. The print PDF starts with
  the half-title and excludes that cover. The EPUB carries its front cover; KDP
  takes the paperback wrap as a separate file. The reading PDF has one more page
  than the print PDF. Never use that extra page in a spine calculation.
- A new tome is added to `common/series.tex` (it is already listed if it is in the series plan).
- Back-cover text: `<tome>/blurb.tex`, about 120–180 words of plain LaTeX (no maths displays),
  saying what the tome is about and why it is beautiful. Without it, the series text in
  `tools/blurb-default.tex` is used.
- The preface talks only about the content, the goal and the beauty of the mathematics:
  what the tome is about, its summits, what it assumes, how the chapters are organised, and
  how to use the exercises and solutions. No personal story, no exams.
- `\ifprintformat` and `\ifsmallformat` are true in every PDF build. The shared
  preamble defaults to the standard 7 × 10 layout even when compiled manually.

## Shared print layout and local paperback builds

The production trim for all sixteen main volumes and three problem books is
**7 × 10 inches**. `common/print-layout.json` defines trim, bleed and the white-paper
spine coefficient. After editing it, run `python3 tools/print_layout.py` to regenerate
its tracked TeX counterpart. The normal build and CI reject an unsynchronised pair.
EPUB remains reflowable. A4, fixed-page Kindle and phone PDF editions are retired;
the build removes their old output files. The separate `-print.pdf` is now required.

`./build.sh --pdf-only [tome...]` rebuilds both PDFs, covers,
listings and `dist/kdp/<tome>-print-metadata.json` without rebuilding EPUB or HTML.
The metadata records the actual interior page count, even-rounded KDP page count,
spine, gutter and exact cover sheet size. Never reuse a wrap from the former trim.
All interior pages are checked at 504 × 720 PDF points; wraps are checked at
(14.25 + spine) × 10.25 inches. Fonts must be embedded vector fonts.

### Pagination and source preparation

All framed material stays on one page in the standard PDF. Keep each box shorter
than the text area; reorganise longer material in the source instead of shrinking
the text. Long inline formulas should become readable displays. Natural spacing
at the foot of a page is allowed when the next box moves to the following page.
Hint and solution openings reserve space, and paragraph widows/orphans are blocked.

The preamble writes box measurements with source locations to `main.oclayout` and
fails on oversized or split frames. After the final pass, `check_book_layout.py`
also rejects horizontal/vertical overflow, oversized floats and unresolved or
duplicate references. Its regression tests typeset moved exercises and problems,
verify their numbers and reference pages, and require invalid boxes to fail.
CI runs those tests with TeX installed. Rebuild the cover wrap after pagination
changes because its spine depends on the new actual page count.

EPUB CSS requests whole boxes and keeps headings with following content. Reading
systems control pagination and may divide material taller than their viewport.

`tools/book_pdf.py` clones the complete print PDF and inserts the uniformly scaled
front page, preserving body streams, annotations, metadata, bookmarks and named
destinations. The cover has its own page label; interior labels are preserved.
Install `tools/requirements-build.txt` for the pinned PDF library and Pillow.

Cache schema 4 and the `library-v4-` Actions namespace force a full migration.
Before snapshotting, both PDFs are checked for 7 × 10 geometry and embedded
fonts. The print page count must agree with paperback metadata; the reading file
must have exactly one added cover and identical body streams, annotation counts,
page labels and correctly shifted named destinations. Retired
variants are removed during cache assembly and rejected before release. Missing
PDF, EPUB, reader, covers or metadata makes a cached book incomplete.


## Exact approved cover master

Volume 0 uses `tools/assets/approved-volume-0.png` unchanged. It is embedded as-is
in the paperback front, copied byte-for-byte into EPUB, reader and library PNGs,
and checked by `tools/check_cover_reference.py`. The source is 1049 × 1500 pixels
(about 150 ppi at 7 × 10); no resampling can add detail. All front-cover outputs
preserve the approved proportions; thumbnails use contain/auto height, never crop.
Cover/wrap builds require XeLaTeX and bundled Inter fonts, plus Pillow for the exact
image check (`texlive-xetex` and `python3-pil` in Ubuntu CI). Body builds still use
pdfLaTeX. The author explicitly preferred the exact image over the old recreation.
