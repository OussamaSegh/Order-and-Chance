# Volume 1 EPUB: KDP conversion failure, 6 November 2026

Internal diagnostic. This is not a claim that KDP has accepted a file.
The exact manuscript Seg uploaded is not in this repository. The file
tested here is the current published Volume 1 EPUB, identified below.

## What Seg reported

KDP, French upload screen, manuscript area, 6 November 2026 13:11 GMT:

> Chargé le novembre 06, 2026 13:11 PM GMT. Impossible de convertir votre
> fichier HTML au format Kindle. Assurez-vous que votre fichier est
> correctement structuré. Si le problème persiste, essayez de télécharger
> votre livre dans un autre format.

The wording says "fichier HTML". KDP uses that sentence for more than one
rejected manuscript type. It does not prove the upload was a bare HTML file.
EPUB is a supported manuscript format when it meets the Kindle publishing
rules. No KDP account was opened and the file was not re-uploaded.

## Tested artifact, distinct from the unknown upload

| | |
|---|---|
| File | `Volume.1.-.First.Principles.epub` |
| URL | https://github.com/OussamaSegh/Order-and-Chance/releases/download/books/Volume.1.-.First.Principles.epub |
| Release | `books`, "Books (latest build)", published 2026-11-06T13:04:55Z |
| Release text | "updated automatically at commit 28db77d" |
| Commit | `28db77dfd18d49d76123676ff7d652e0b917c6c8` (current `main` at investigation time) |
| CI | Actions run 42218279741, "Build books", push to `main`, success, started 2026-11-06T12:31:08Z, 40m33s |
| Size | 32,338,238 bytes |
| SHA-256 | `faa586bee97644cdcd6f815b2ab078a53cf7d09bcd46e753824f2a2dbc36bb28` |

The release existed about seven minutes before the 13:11 GMT error. That is
why this file was tested. It is not proof it is the file that was uploaded.
The older `edition1` release (2026-11-02, 31,603,031 bytes) was not unpacked.

## Official pages actually read

Parent pages Seg supplied:

- https://kdp.amazon.com/fr_FR/help/topic/G200634390 — « Quels sont les formats de fichiers pris en charge pour les manuscrits d’ebooks ? » EPUB is supported when the book meets the Kindle publishing rules. Kindle Previewer is recommended before upload. A supported format is not evidence that this file conforms.
- https://kdp.amazon.com/fr_FR/help/topic/GU72M65VRFPH43L6 — « Règles d'édition Kindle ». Index. The child pages below are the ones linked from that index and compared with the file.

Child pages used for the comparison:

- https://kdp.amazon.com/fr_FR/help/topic/G6GTK3T3NUHKLEFX — « Lignes directrices relatives aux images de couverture pour les ebooks Kindle ». « N'ajoutez pas de page de couverture HTML au contenu, en plus de l'image de couverture. La couverture risquerait d'apparaître deux fois dans le livre, ou ceci pourrait causer l'échec de la conversion du livre. » Recommended declaration is `properties="cover-image"` (method 1) or `meta name="cover"` (method 2). Internal cover at least 1200×1200 px.
- https://kdp.amazon.com/fr_FR/help/topic/G75V4YX5X8GRGXWV — « Règles relatives aux images - Format réajustable ». « les balises SVG peuvent entraîner des erreurs. Nous recommandons de supprimer les balises SVG et d'utiliser les balises image en HTML ». Also: Kindle does not support images with transparent regions; it converts a transparent background to white. That sentence describes a conversion of the pixels, not a failed upload.
- https://kdp.amazon.com/fr_FR/help/topic/GB5GDY7WAJDN9GFK — « Attributs et balises pris en charge par la composition améliorée ». Under « Solutions de contournement pour éviter les échecs de conversion courants »: « E2006 : Plusieurs titres sont définis dans les métadonnées OPF. » Mark one `dc:title` with `title-type` `main`. The same page's internal-error list (1 px images, 0-byte fonts, table `caption`, `height`/`width: inherit`, fixed-layout `original-resolution`) was checked and did not match this file.
- https://kdp.amazon.com/fr_FR/help/topic/GP2Z9DD4F2N4QKCY — « Règles relatives aux balises HTML et CSS ». Nested `p` « ne seront pas convertis correctement. » None are present. Allowed spaces named there are the ordinary space, `&nbsp;`, and `&zwnj;`.
- https://kdp.amazon.com/fr_FR/help/topic/GGRXLC5USU4H67YM — « Normes de contrôle qualité ». Each HTML file under 30 MB; fewer than 300 HTML files. Kindle Previewer is described as Windows and Mac.
- https://kdp.amazon.com/fr_FR/help/topic/GY3AD8C6C6GAG42N — « Règles relatives à la navigation ». NCX required for the Kindle menu; two nesting levels supported.
- https://kdp.amazon.com/fr_FR/help/topic/G42HENP2VHSN8VW8 — « Comparaison des formats ». Reflowable is the format for a text-heavy book and is marked as supporting enhanced typesetting.

## What the published file actually contains

EPUB 3, reflowable, language `en`, 8,591 zip entries, 23 XHTML documents.
Largest XHTML is `EPUB/text/ch009.xhtml` at 728,791 bytes. No zero-byte
files. No script, MathML, remote resources, or 1 px images. 8,509 PNGs
(8-bit, not interlaced) and 35 JPEGs. Cover image `EPUB/media/cover.png`
is 1792×2560. TOC and NCX nesting depth is 2. 166 TOC links. Chapter 9
has 2,297 `img` elements and no MathML. 120 plate PNGs.

EPUBCheck 5.4.0 (official zip, Java 21.0.12.1), 6 November 2026:

```
java -jar epubcheck-5.4.0/epubcheck.jar Volume.1.-.First.Principles.epub
```

Result: 0 fatal / 0 errors / 0 warnings / 0 info. Exit 0.
EPUBCheck does not catch the two Kindle-specific packaging issues below.
A clean EPUBCheck run is not KDP acceptance.

### Defect 1 — HTML cover page plus SVG, on top of the cover image

`build.sh` passes Pandoc `--epub-cover-image`. Pandoc then does both of
the things the cover page tells you not to combine:

- declares `media/cover.png` with `properties="cover-image"` and `meta name="cover" content="cover_png"` (the two documented image declarations; the id matches);
- also writes `EPUB/text/cover.xhtml`, puts it first in the spine, points the guide `cover` reference and the landmarks `epub:type="cover"` link at it.

That page's body is only an SVG `image` with `xlink:href="../media/cover.png"`.
The manifest item is `properties="svg"`. It is the only SVG in the book.
This matches the cover-page sentence that says the extra HTML page can
fail conversion, and the image-page sentence that SVG tags can cause errors.

### Defect 2 — two titles, primary title not marked main

`tools/epub_fix.py` adds the catalog subtitle as a second `dc:title` with
`title-type` `subtitle` and does not mark the primary title `main`.
The published OPF therefore has:

- `Order and Chance. Volume 1: First Principles` (no title-type)
- `Proof, Problem Solving and Mathematical Thinking` (`title-type` subtitle)

That is the E2006 pattern on the enhanced-typesetting page. The subtitle
text is the catalog subtitle for Volume 1; it is not a wrong string.
EPUBCheck 5.4.0's JSON `publication.title` prints the last `dc:title`
(the subtitle) both before and after `title-type` main is added, with
zero errors in both cases. That JSON field is not treated as Kindle's
choice of title.

## Ruled out on this file

- Nested `p` (XML walk; EPUBCheck clean).
- HTML size and count against the 30 MB / 300-file limits.
- 1 px images, 0-byte fonts, `caption`, `height`/`width: inherit`, fixed-layout properties.
- MathML left in the book. Formulas are PNG `img` elements.
- TOC depth above 2.

Not changed, because the cited page does not say they fail conversion:

- Transparent formula PNGs. The image page says Kindle turns a transparent background white. Flattening them would put white boxes behind mathematics in sepia and black. Left as they are.
- Ten U+2006 six-per-em spaces in portrait dates such as "c. 1700". The HTML page says other spaces can obstruct selection, dictionary lookup, and line breaking. They are in the chapter text, which this change does not rewrite.
- Negative `vertical-align` on formula images. That is the existing baseline shift. The HTML page's negative-value warning is about text positioning and margins (the example is `text-indent`), and it describes overflow, not a failed conversion.

## Fix

`tools/epub_fix.py`, used by every volume after Pandoc:

- If a cover image is already declared, delete a spine XHTML page whose body has no text and only points at that image. Delete its manifest item, the guide reference, and a landmarks item that links only to it. Keep the PNG, `cover-image`, and `meta name="cover"`.
- Mark the series `dc:title` with `title-type` `main`. Keep the subtitle.

`tools/check_epub_media.py` now fails the build on SVG in a content document, an HTML cover page beside a declared cover image, a guide cover reference to XHTML in that situation, and more than one `dc:title` without exactly one `title-type` main.

Print PDF, reading PDF, cover art, and chapter source are untouched.

## Candidate

Produced by running the updated `epub_fix.py` on the published EPUB above
(`render_math=False`), not by a fresh TeX run. That is the same function
`build.sh` runs after Pandoc. A from-scratch Volume 1 typeset was not
required: every chapter XHTML, image, font, and stylesheet is byte-identical
to the published file. The only changed entries are `EPUB/content.opf` and
`EPUB/nav.xhtml` (cover landmark removed). `EPUB/text/cover.xhtml` is gone.
TOC hrefs: 166 before and 166 after, same list, all resolved.

| | |
|---|---|
| Path | `/opt/cursor/artifacts/volume1-kdp-epub/Volume-1-First-Principles-candidate.epub` |
| Size | 32,337,660 bytes |
| SHA-256 | `c6dcfcaf915af338e75a636fc7389a1759cc8e29b0ba29b98dce7144a7d140ce` |

EPUBCheck 5.4.0 on the candidate: 0 fatal / 0 errors / 0 warnings / 0 info.
`tools/check_epub_media.py` on the candidate: pass.
Logs and the before/after OPF metadata and the original cover page are in
the same artifacts directory.

A fresh Pandoc miniature with `--epub-cover-image` loses the SVG cover page
and gains `title-type` main. `python3 -m unittest test_epub.EpubRegression.test_pandoc_svg_cover_page_is_removed test_epub.EpubRegression.test_epub_math_and_manifest test_check_epub_media.py` — 16 tests, OK.
Ubuntu Pandoc 3.1.3 was installed for that miniature. Three older alt-text
tests in `test_epub.py` fail under that Pandoc and do not call this fix;
they were not edited.

Kindle Previewer is not on this machine. The French QA page limits it to
Windows and Mac. It was not run. No file was sent to KDP or to any online
validator.

## What remains unknown

- Whether the 13:11 GMT upload was this exact 32,338,238-byte file.
- Whether KDP's converter accepts the candidate. EPUBCheck and the local
  packaging checks do not establish that. The author has to upload it.
- Volumes 2–15 were not unpacked. They are built with the same
  `--epub-cover-image` line, so the next EPUB build of each applies the
  same removal. Their current release bytes were not hashed here.

## Next step

Upload the candidate EPUB, not the `books` release file, and keep KDP's
message. Do not describe the result as accepted until that upload succeeds.
If it fails again, the useful missing evidence is the KDP previewer or
conversion log for that exact SHA-256, not another generic screenshot.
