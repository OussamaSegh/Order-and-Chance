# Interior fonts

These licensed fonts are bundled for reproducible colour interiors and digital reading.
Approved cover fonts and image masters live separately in `tools/assets/`.

- **Libertinus Serif** (regular, italic, bold, bold italic) and **Libertinus Math**:
  original OpenType files from CTAN's `libertinus-fonts` distribution,
  https://ctan.org/pkg/libertinus-fonts. SIL Open Font License: `OFL-Libertinus.txt`.
- **Inter Text**: static 400/600 upright/italic instances at optical size 14,
  instantiated from the Google Fonts Inter variable sources with fontTools.
  https://github.com/google/fonts/tree/main/ofl/inter. SIL OFL: `OFL-Inter.txt`.
  These text-size instances are separate from the approved cover's existing weights.
- **DejaVu Sans Mono**: unchanged regular, bold, oblique and bold oblique TTFs,
  https://dejavu-fonts.github.io/. The licence is `LICENSE-DejaVu.txt`. Its symbol
  coverage preserves the mathematical Unicode used in the book's code examples.

Matching WOFF2 companions were made with fontTools for the online reader. EPUB
embeds the original OTF/TTF faces. `manifest.json` records all font SHA-256 hashes.
