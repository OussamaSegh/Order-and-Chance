# Publishing a tome on Amazon KDP

`./build.sh` makes, for every tome, the files a Kindle eBook and a paperback need, next to the
screen PDFs and the EPUB:

| File | What it is | Where it goes in KDP |
|---|---|---|
| `dist/<tome>.epub` | Reflowable eBook with cover, table of contents and copyright page | Kindle eBook > Manuscript |
| `dist/kdp/<tome>-ebook-cover.jpg` | Front cover, 1600 x 2560 px JPEG | Kindle eBook > Cover |
| `dist/kdp/<tome>-print.pdf` | Paperback interior: 6 x 9 in trim, no bleed, all fonts embedded | Paperback > Manuscript |
| `dist/kdp/<tome>-cover-wrap.pdf` | Back cover, spine and front cover with 0.125 in bleed | Paperback > Cover ("upload a cover you already have") |

In KDP choose: trim size 6 x 9 in, black ink on white paper, no bleed, matte or glossy cover.
The spine width is computed for white paper (0.002252 in per page); for cream paper the cover
must be rebuilt with 0.0025 in per page. The `books` release on GitHub carries the same files.

KDP rules followed by the build (checked against the KDP help pages in October 2026):

- Inside (gutter) margin 0.75 in, more than KDP's minimum up to 700 pages (0.375 in to 150 pages,
  0.5 in to 300, 0.625 in to 500, 0.75 in to 700); 0.875 in is used above 700 pages.
  Outside margin 0.6 in (minimum 0.25 in). Chapters open on a right-hand page.
- Page count 24 to 828; the build warns outside that range.
- Cover: width = 0.125 + 6 + spine + 6 + 0.125 in, height = 9.25 in; spine text only from
  80 pages; text kept 0.125 in inside the trim and 0.0625 in inside the spine folds; the
  barcode area (lower right of the back cover) is left empty for KDP's ISBN barcode.
- Fonts: every font is an embedded Type 1 font (no bitmap fonts); links are black in print.
- At upload, KDP asks whether the content is AI-generated: answer yes (text and covers).

## Conventions for every tome

- `main.tex` keeps its first line `% epub-title: Order and Chance. Tome N: Title`; the build
  reads the tome number and title from it (numbers may be `0`–`15` or `C1`–`C5`).
- `\maketitle` builds the front matter of a published book automatically: half-title, series
  page (from `common/series.tex`), title page and copyright page (`common/frontmatter.tex`).
  The order in `main.tex` stays `\frontmatter \makecover \maketitle` then the preface, then
  `\tableofcontents`.
- Series-wide settings (copyright line, licence, authors, repository) live in
  `common/frontmatter.tex` only. Per-tome settings go in `main.tex` after
  `\input{../common/preamble}`: `\renewcommand{\bookedition}{...}`,
  `\renewcommand{\bookisbnprint}{...}`, `\renewcommand{\bookisbnebook}{...}`.
- A new tome is added to `common/series.tex` (it is already listed if it is in the series plan).
- Back-cover text: `<tome>/blurb.tex`, about 120–180 words of plain LaTeX (no maths displays),
  saying what the tome is about and why it is beautiful. Without it, the series text in
  `tools/blurb-default.tex` is used.
- The preface talks only about the content, the goal and the beauty of the mathematics:
  what the tome is about, its summits, what it assumes, how the chapters are organised, and
  the companion notebooks. No personal story, no exams.
- `\ifprintformat` is true in the paperback build, `\ifsmallformat` in the phone, Kindle and
  paperback builds (the paperback text block is 4.65 in wide).
