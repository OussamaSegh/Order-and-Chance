# Volume 2 publication files

Build this volume from the repository root:

```sh
./build.sh volume2-integers
```

The shared publishing conventions and system dependencies are documented in `../tools/PUBLISHING.md`.

| File | Use |
|---|---|
| `dist/Volume 2 - The Integers.pdf` | Reading PDF with front cover followed by the 7 × 10 inch interior |
| `dist/kdp/Volume 2 - The Integers - Print.pdf` | Paperback interior without front cover, premium colour on white paper, 7 × 10 inches, no bleed |
| `dist/kdp/Volume 2 - The Integers - Paperback Cover.pdf` | Paperback cover, with 0.125 inch bleed and spine computed from the manuscript page count |
| `dist/Volume 2 - The Integers.epub` | Reflowable Kindle manuscript, with MathML and vector diagrams |
| `dist/kdp/Volume 2 - The Integers - eBook Cover.jpg` | Kindle front cover, 1792 × 2560 pixels |
| `dist/kdp/Volume 2 - The Integers - Publishing Listing.md` | Description and seven keywords for the book details |
| `dist/html/volume2-integers/` | Online chapter reader |

Use the generated listing: author **SEGHAIER Oussama**, book title **Volume 2: The Integers**, subtitle **Primes, Patterns and Proofs**, series **Order and Chance**, volume **2**, edition number **1**. The book itself displays **First edition, 2026**. Preserve any existing series/edition association when updating an already published title.

No paperback ISBN has been supplied for this volume. `main.tex` deliberately leaves `\bookisbnprint` empty; the copyright page prints no placeholder and the cover leaves its barcode area clear. Once KDP assigns the paperback ISBN, set `\renewcommand{\bookisbnprint}{979-...}` to the actual value and rebuild. That adds the ISBN line and the matching barcode. If uploading the current cover without a barcode, allow KDP to place one; with a rebuilt barcode cover, choose the corresponding cover setting. Never invent an ISBN.

For final upload, use KDP's Print Previewer to review the interior and matching cover together, and Kindle Previewer to inspect the EPUB on the intended devices. These vendor checks require the publishing account or applications and are separate from local PDF and EPUB validation. Content, images and covers created with AI assistance must be disclosed accurately in KDP's AI-generated-content questions, following the series' publishing instructions.

Historical image credits appear beside the portraits, at the end of the book, and in `photos/CREDITS.md`. Mathematical figures are vector drawings with labels and line/marker distinctions for grayscale print. The smaller Fermat reproduction is capped at 1.3 inches high to retain at least 300 pixels per inch in the paperback.

The current reconstruction records are in `../review/volume1-reconstruction/`. The older review is historical and does not specify the current production layout. Changes to the content or page layout require rebuilding the cover wrap as well as the interior, since spine width depends on page count.
