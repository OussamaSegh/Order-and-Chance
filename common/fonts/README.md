# Version C interior fonts

The author approved version C: the cover's Inter display faces for headings and
STIX Two Text/Math for text and mathematics. Files are bundled for reproducible
PDF, EPUB and web builds.

- **STIX Two Text**: regular, italic, bold and bold italic; **STIX Two Math**:
  original OTF files from https://ctan.org/pkg/stix2-otf. Licence: `OFL-STIX.txt`.
- **Inter display**: `Inter-Light.ttf`, `Inter-SemiBold.ttf` and
  `Inter-LightItalic.ttf` are exact copies of the approved cover files in
  `tools/assets/fonts/`, at optical size 32. The missing semibold italic face is
  instantiated at weight 600 / optical size 32 from the same Google Fonts Inter
  italic variable source; its name is `InterDisplay-SemiBoldItalic.ttf`.
- **Inter Text**: existing optical-size-14 regular/semibold upright/italic faces
  remain for reader controls and mathematical sans text. Inter sources:
  https://github.com/google/fonts/tree/main/ofl/inter. Licence: `OFL-Inter.txt`.
- **DejaVu Sans Mono**: unchanged regular/bold/oblique/bold oblique TTFs preserve
  the book's Unicode code symbols. https://dejavu-fonts.github.io/;
  licence: `LICENSE-DejaVu.txt`.

Matching WOFF2 companions were generated with fontTools. EPUB embeds OTF/TTF
faces. `manifest.json` records all 34 font-file hashes. Cover assets are unchanged.
