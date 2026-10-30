# Interior fonts (design 5e)

The author approved interior design 5e (see `docs/design/interior.md`). Every face is
bundled here so PDF, EPUB and web builds never depend on system fonts.

| File(s) | Use | Source | Licence |
| --- | --- | --- | --- |
| `EBGaramond-Regular/Italic/SemiBold/SemiBoldItalic.otf` | body text, italic notes | CTAN `ebgaramond` (v1.000, octaviopardo/EBGaramond12) | `OFL-EBGaramond.txt` |
| `Garamond-Math.otf` | mathematics (stylistic sets 1, 2) | CTAN `garamond-math` (2022-01-03) | `OFL-GaramondMath.txt` |
| `CormorantGaramond-SemiBold.ttf` | headings, opener masthead and title | exact copy of the cover file `tools/assets/fonts/CormorantGaramond-SemiBold.ttf` (v4.004) | `OFL-Cormorant.txt` |
| `CormorantGaramond-SemiBoldItalic.ttf`, `CormorantGaramond-Light.ttf` | italic headings, opener numerals | CTAN `cormorantgaramond` (v3.6) | `OFL-Cormorant.txt` |
| `FiraSans-Book/BookItalic/Medium/MediumItalic.otf` | labels, running heads, captions | CTAN `fira` (v4.301) | `OFL-Fira.txt` |
| `DejaVuSansMono*.ttf` | code and Lean Unicode symbols | https://dejavu-fonts.github.io/ | `LICENSE-DejaVu.txt` |

All files are unmodified originals. The DejaVu WOFF2 companions are unchanged; the
online reader serves the other faces as their original OTF/TTF files (no WOFF2 is
generated for them yet). EPUB embeds the OTF/TTF faces. `manifest.json` records the
SHA-256 hash of every font file. Cover fonts in `tools/assets/fonts/` are unchanged.
