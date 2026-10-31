# Interior design (5e)

This is the typographic system of every *Order and Chance* interior: the print and
download PDFs of all fifteen volumes, their front and back matter, and the EPUB and
online reader styles. The author approved mock-up 5e (a full charcoal chapter opener);
this file describes how it is built and how to change it. Covers are separate and are
not affected (see `docs/COVER-DESIGN.md`).

All of the system lives in `common/`:

| File | Role |
|---|---|
| `interior-fonts.tex` | font families |
| `preamble.tex` | geometry, packages, load order |
| `interior-style.tex` | labels, headings, running heads, captions, contents, `\part` (drawn in `chapter-opener.tex`) |
| `chapter-opener.tex` | the full charcoal part page and the banded chapter opener |
| `interior-boxes.tex` | the two box families, proofs, exercises, hints and solutions |
| `figure-palette.tex` | the figure colours |
| `inline-fractions.tex` | slashed fractions in running text |
| `frontmatter.tex` | half-title, series page, title page, copyright page |
| `design-colors.tex` | the named colours |

The manuscripts (`volume*/chapters`) need no markup for any of it.

## Type

| Use | Face | Setting |
|---|---|---|
| Body text, proofs, notes | EB Garamond (Regular, Italic, SemiBold, SemiBold Italic) | 11.5 pt on 14.75 pt (11 pt class size, `Scale=1.05`, `\linespread{1.085}`), lining figures |
| Mathematics | Garamond-Math (stylistic sets 1, 2) | same scale as the text |
| Headings, titles, the opener numeral | Cormorant Garamond SemiBold / SemiBold Italic / Light | chapter title in the band 26/30 pt cream (unnumbered chapters 22/26), section 18/21, subsection 14/17; opener numeral 64 pt Light |
| Labels, running heads, captions, folios | Fira Sans Book / Medium (+ italics) | labels 8.2 pt capitals, 8% tracking |
| Code | DejaVu Sans Mono | |

The fonts are vendored under SIL OFL 1.1 in `common/fonts/`; the licences and sources
are in `common/fonts/README.md`, and their hashes are in `manifest.json`. CI installs
no extra TeX fonts. Running text in a box keeps the body face; labels are always Fira
capitals with a coral number; theorem notes are EB Garamond italic.

## Page

- Trim 7 × 10 in. Two-sided pages with mirrored margins: gutter 0.9 in, outside 0.8 in,
  top 1 in, bottom 0.85 in, giving a 5.3 in measure. `build.sh` passes
  `\PRINTINNER{0.9in}`, and the preamble never uses less than 0.9 in. That meets KDP's
  inside-margin minimum at every page count up to the 828-page limit.
- Running heads, both outside:
  - verso: folio ◆ `VOLUME n · TITLE`;
  - recto: current section (truncated) ◆ folio.

  The heads are Fira Book 8 pt tracked capitals, and the diamond is coral.
- Opening pages (a chapter's first page, a part page, an unnumbered chapter) show only
  the folio, at the foot. Blank pages are empty.

## Chapter opener

Every numbered chapter in the main matter and the appendices starts on the next page,
recto or verso, and the prose begins on that same page. Nothing is inserted to force
the chapter onto one side: a part's first chapter is the back of the part page. The
first page uses the plain style (folio at the foot, no running head). Later pages keep
the running heads.

The opener is a compact block at the top of that page:

- a charcoal band, held 0.30 in inside the trim. The masthead and volume line are
  small and centred at the top. The coral numeral is centred above the centred
  cream Cormorant title. There is no `CHAPTER n` label. An appendix adds a small
  `APPENDIX` above the letter. There is no rule;
- under the band, on the white paper, the opening italic is 10.5 pt on 14.7 pt,
  centred on 68 percent of the measure, with space above and below and no bar.

The body follows the epigraph. There is no second heading on the next page. Unnumbered
chapters (preface, field guide, About the Cover, solutions, index, bibliography) have
the short heading only. The opener does not draw a motif or the volume's cover
illustration.

Putting the prose on the opener page changes where later floats land. The gap under
a float keeps its natural 20 pt; a tight page may shrink that gap by up to 14 pt
(`\textfloatsep`) so the page stays inside the text block.

**Epigraph.** The convention of the manuscripts is unchanged. A
`\begin{center}\itshape … \end{center}` directly after `\chapter{…}` (and its
`\label`) is moved onto the opener automatically. A chapter without one simply has no
epigraph.

`\chaptermotif{...}` is accepted and ignored. Print openers do not input `cover-motif.tex`.

**Bleed.**

- The chapter band stays 0.30 in inside the trim on the top and the sides, in the
  ordinary build and in a bleed build. That is inside KDP's 0.25 in no-bleed margin.
  The band does not run to the trim or to the bleed.
- In a bleed build (`\def\OCBLEED{}` before `\input{main.tex}`), the paper grows by
  `\PRINTBLEED` (0.125 in) on every side and the layout stays 7 × 10 in. The part
  page's charcoal still runs to every bleed edge.
- The default build, which is the KDP interior (`kdp_pdf.py` checks it as "no bleed"),
  is trim-size. The part page's charcoal still meets the trim. That is the earlier
  full-page behaviour, unchanged here; a hairline of trim variance can show on a part
  page. Switching KDP to a bleed interior needs the KDP setting changed as well as
  `\OCBLEED`; this has not been done.

## Parts

A part page is a **full charcoal recto** (`\oc@part@page` and `\oc@part@art` in
`chapter-opener.tex`). It uses the same lockup the full-page opener used: the masthead
(*ORDER AND CHANCE* in spaced Cormorant capitals, the volume line in Fira), the part
numeral in 190 pt light coral Cormorant, then `PART I` in Fira Medium with 8% tracking
(ivory, numeral in light coral), the ivory Cormorant title and a short light-coral
rule-diamond-rule. The rest of the page is solid charcoal. There is no illustration,
no motif and no epigraph. There is no blank verso after it. The part's first chapter
begins on the back of that page, band and opening prose together. `\part*` gives the
page without a numeral or label.

## Boxes: two families

| Family | Environments | Look | Breaking |
|---|---|---|---|
| **Formal** | `theorem`, `proposition`, `lemma`, `corollary`, `definition`, `example` and the unnumbered `theoremx`, `propositionx`, `lemmax`, `corollaryx`, `definitionx`, `examplex` | 8% charcoal fill, 1.2 pt coral rule on top, 10 pt side padding; upright statement; label `THEOREM 3.2` (Fira capitals, coral number), the optional note in EB Garamond italic | never split (`unbreakable`; measured by `tools/check_book_layout.py`) |
| **Teaching** | `exercise` (and *Problem* chapters), `reminder`, `think` (*Pause and think*), `beauty` (*Why this is beautiful*), `challenge` (*Challenges*), `remark` | 2 pt charcoal bar on the left, no fill, 12 pt indent; label in Fira capitals; exercise number in coral, difficulty stars after it | breakable (at least three lines before a break); the bar continues on the next page |
| Teaching, run-in | `proof`, `hint`, `solution` (`\idea`, `\writeup`, `\tools`, `\leads`) | no bar; italic *Proof.* label, or `HINT FOR EXERCISE n.m` / `SOLUTION OF EXERCISE n.m` with a coral number; proofs and solutions end with a coral diamond | flow with the text |

A chapter of problems switches the name once:
`\renewcommand{\ocExName}{Problem}` (inside its `% begin pdf problem style` block,
which the EPUB preparation removes).

## Colour

There is one accent, **coral**:

- `ocCoral` #FF8A78 for rules, diamonds and the opener numeral;
- `ocCoralDeep` #A34232 when it is text-sized: numbers in labels, the contents and
  running heads, and links.

Everything else is charcoal `ocBlack` #151516 on white, with the 8% charcoal tint for
formal boxes. Coral is used only for rules, numerals, numbers and diamonds: never
for words or box fills.

**Figures** keep their sources. `figure-palette.tex` redefines the colour names they
use (it is loaded by the books and by `tools/figure.tex`, so the EPUB and reader SVGs
match):

| Figure colour names | New colour | Hex | Word used in prose |
|---|---|---|---|
| MidnightBlue, blue, NavyBlue, RoyalBlue, ocBlue | charcoal | 151516 | charcoal |
| BrickRed, red, Maroon | rust (= ocCoralDeep) | A34232 | rust |
| BurntOrange, orange, Orange, Goldenrod, yellow, Bittersweet, Peach | coral | FF8A78 | coral |
| ForestGreen, green, olive, ocOlive | ochre | B08D57 | ochre |
| Plum, violet, purple, Purple, magenta, Orchid, ocPlum | brown | 5A2A22 | brown |
| teal, ocTeal | dark grey | 6E6A66 | dark grey |
| Cyan, cyan, SkyBlue | light grey | C9BDB8 | light grey |
| viridis colour map | charcoal → brown → rust → coral → cream | | |

Captions, and the few sentences that point at a figure's colours, use these words.
Mathematical colourings keep their own names (Ramsey's red and blue edges, Pólya's
red and green balls): those colours are part of the mathematics, not the print. A
caption that shows such a colouring says how it is drawn ("the red graphs (drawn in
rust)"). Three figures whose two source colours fall on the same palette colour override one name locally,
at their top (`ch01-euclid`, `conjectures-ch09-es`, `geometry-ch09-e8`).

## Inline fractions

In running text, `\frac{a}{b}` is set as a slashed fraction `a/b`, with parentheses
added only where they are needed. In displays it stays stacked.

- The numerator is parenthesised when it has a top-level `+`, `-`, `\pm`, `\mp`, `/`
  or another fraction.
- The denominator stays bare when it is a single symbol, a number, a symbol with
  scripts, a differential (`dx`, `\partial x`, `\mathrm{d}x`), a function application
  like `\log x`, or one parenthesised group (with scripts). Anything else is
  parenthesised.
- A fraction followed by a letter, digit, `(` or `^` is wrapped as a whole:
  `(1/2)n`, `(d/dx)f`.
- Displays, `\[…\]`, `equation`, `align` and the like, TikZ pictures, and any
  `\displaystyle` or `\dfrac` keep the stacked form (`\mathchoice` chooses).

The source is untouched; the original command is `\ocStackedFrac` if a passage needs
the stacked form inline.

## Front and back matter

- Half-title, series page and title page use the masthead, the `VOLUME n` label, the
  Cormorant title, an italic subtitle and the coral rule. The copyright page names
  the typefaces.
- Contents: part labels, Cormorant chapter titles with coral numbers, Fira section
  lines with dotted leaders. A volume can tighten the space between chapters with
  `\setlength{\ocTocChapterSkip}{…}`.
- About the Cover, the index and the bibliography are unnumbered chapters with the
  short heading.

## EPUB and online reader

`tools/epub.css` and `tools/reader.css` follow the same system:

- EB Garamond body, Cormorant headings and numerals, Fira capitals for labels, and
  Garamond-Math for MathML in the EPUB (the reader sets mathematics with KaTeX);
- chapters and parts open with a compact charcoal header strip: the masthead line, the
  coral numeral beside the ivory Cormorant title and the coral rule; the epigraph follows
  on the page background and the chapter text follows the epigraph. There is one heading,
  not a second copy under the strip. The full charcoal part page is print only. The print
  chapter opener is the compact band described above, and neither draws the cover
  illustration. `tools/epub_prep.py` turns `\part`
  into a marker so chapters stay chapters, and `tools/epub.lua` builds the strips (it
  would also place `opener-motif.png` from `tools/opener_motif.py`, which `build.sh` no
  longer calls);
- formal boxes with the 8% charcoal tint under a coral rule; teaching boxes with a 2 pt
  charcoal bar; Fira labels with coral numbers; the coral end-of-proof diamond;
- coral only on rules, numerals, numbers and diamonds. The reader keeps its dark theme.

The online reader has one page per chapter; the former one-page-per-part URLs redirect
(`tools/site.py`).

The project site (`tools/site-template.html`, built by `tools/site.py`) uses the same
faces: EB Garamond text, Cormorant headings and card titles, Fira for the brand, meta
lines and buttons, charcoal ink `#151516` and ocCoralDeep `#A34232` for the accent.

The EPUB embeds the OTF/TTF files from `common/fonts/`. The reader and the site serve
the WOFF2 companions (fontTools conversions of the same files, see
`common/fonts/README.md`); Garamond-Math has no WOFF2.

## Checks

- `tools/check_interior_style.py` requires EB Garamond, Garamond-Math, Cormorant
  Garamond and Fira Sans in the PDF, and the `ocCoral`, `ocCoralDeep` and `ocBlack`
  drawing colours.
- `tools/check_book_layout.py` rejects any overfull box, missing glyph or unresolved
  reference, and any formal box taller than the text block.
- `tools/test_book_layout.py` checks that teaching boxes paint one 2 pt charcoal bar,
  that formal boxes move whole, and that teaching boxes may break.
