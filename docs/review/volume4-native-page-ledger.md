# Volume 4 native PDF — page-by-page preliminary QA ledger

**Date:** 7 November 2026. **Source:** draft PR #111, branch `cursor/volume4-rewrite-ee7f`, exact CI input commit `e2b7fd9722b160dedd9e042ff09daea5c4698baa`. **Review role:** automated document checks and low-resolution layout sampling; **NOT** a chapter mathematical review, an independent second review, or final full-resolution visual acceptance.

## Artifact provenance and reproducible checks

- Native production [workflow #42336816955](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42336816955) completed successfully at the pinned commit; job `volume4-native` built reading and print PDFs, EPUB, online reader, cover, ran native preflight and uploaded artifact `volume4-native-42336816955` (ID `13560036521`; artifact ZIP digest `9697b1195d4d12622f8d97530ec8fba121b3dff91082469b3177b7e2115f240a`).
- Downloaded that workflow artifact and verified each named local PDF/EPUB against its packaged `volume4-native-sha256.txt` using `sha256sum`.
- Reading PDF: **226 physical pages** (includes a separate reading cover), 504 × 720 pt, SHA-256 `23d6051861581109732707ea67ad658a627ccc69a3cb866c1e57f07a2af7eff0`.
- Print interior: **225 physical pages**, 513 × 738 pt on **all** pages, SHA-256 `a023a60a48ae2f2987f5460a5878a04a9882834033cb9dd23745f30fb080609c`. The first reading cover is absent from the print interior; reading page `p+1` normally corresponds to print page `p`.
- EPUB: SHA-256 `a307ab9546f8999db7ca42a6ed3abd2b9e61c3bce753d5c786914297cec293b0`; cover wrap: `8f8113012937b2237d848d4c9749ffe95e6844d8d64a546105ed08df66f5cb6c`.
- PDF geometric inspection used PyMuPDF on **every** physical page: zero extracted words outside page bounds in either document; print interior has no live link annotations; reading PDF has 604 link annotations. Reading blank pages 7 and 131 correspond to print pages 6 and 130 (intentional-looking blank versos before divisions).
- Print page 198 has no selectable text because the KDP export rasterized it into a 4200 × 6000 RGB bitmap, **600 dpi** at the underlying 7 × 10 trim extent; this agrees with the native workflow's one-page flattening report. Its visible mathematical text and graph were manually sampled; the final press proof is still required.
- **All 33 paired extracted-text discrepancies were categorized** by `difflib.SequenceMatcher` on whitespace-normalized page text: 45 glyph-encoding replacements `Ï`→`fi`, 4 `Ò`→`fl`, and the expected missing extracted stream from the one rasterized print page 198. No other differences in the paired extracted characters were found. This establishes an extraction/font-encoding explanation for the text-layer discrepancies, **not** a manual proofreading pass of the press PDF.
- The EPUB converter logged a warning for the total-variation expression in Chapter 9, but `EPUB/text/ch014.xhtml` contains a referenced PNG and the extracted formula image visibly contains the inequality. Do not classify it as broken merely from the warning; a device/reader rendering check remains required.

## Visual overview performed (not a production acceptance)

All 226 **reading** PDF pages were rasterized into 10 low-resolution numbered contact sheets, covering 1–25, 26–50, 51–75, 76–100, 101–125, 126–150, 151–175, 176–200, 201–225 and 226. Each sheet received a visual overview. Opening pages, 4 part dividers, chapter openings, illustration pages, the Galton-board photograph, end matter, and the last page appeared in the intended reading order. This is only a *thumbnail layout screen*, not a readable line-by-line/high-DPI page-by-page check.

Print pages 14, 29, 95 (photo), 145 (Chapter 9 opening), 150, 160, 174, 199, 217 and 225 were inspected in additional 1.5× samples; flattened print page 198 was checked separately at 1.7×. These are **spot checks**, not proof that fine figures/formula text, bleed and citations pass on all print pages.

**Page target:** 225 print-interior pages at this exact SHA; the approved planning target is 400–500, so the minimum gap is **175 pages**. Do not pad, shrink text, drop proofs/solutions, or imply completion. The source-level removed-material audit and owner decisions remain later separate work.

## Page-level coverage index

Legend: **G** = automated geometry and word-bounds pass; **O** = included in the *reading PDF* thumbnail visual overview (reading page as shown); **S** = print page 1.5× sample inspection; **R** = separately sampled rasterized print page; **B** = intentionally-looking blank page; **P** = full high-resolution/line-by-line press QA **pending**. All entries retain P, including samples.

| Print page | Reading page | Preliminary checks | Final QA |
| ---: | ---: | --- | --- |
| 1 | 2 | G,O | P |
| 2 | 3 | G,O | P |
| 3 | 4 | G,O | P |
| 4 | 5 | G,O | P |
| 5 | 6 | G,O | P |
| 6 | 7 | G,O,B | P |
| 7 | 8 | G,O | P |
| 8 | 9 | G,O | P |
| 9 | 10 | G,O | P |
| 10 | 11 | G,O | P |
| 11 | 12 | G,O | P |
| 12 | 13 | G,O | P |
| 13 | 14 | G,O | P |
| 14 | 15 | G,O,S | P |
| 15 | 16 | G,O | P |
| 16 | 17 | G,O | P |
| 17 | 18 | G,O | P |
| 18 | 19 | G,O | P |
| 19 | 20 | G,O | P |
| 20 | 21 | G,O | P |
| 21 | 22 | G,O | P |
| 22 | 23 | G,O | P |
| 23 | 24 | G,O | P |
| 24 | 25 | G,O | P |
| 25 | 26 | G,O | P |
| 26 | 27 | G,O | P |
| 27 | 28 | G,O | P |
| 28 | 29 | G,O | P |
| 29 | 30 | G,O,S | P |
| 30 | 31 | G,O | P |
| 31 | 32 | G,O | P |
| 32 | 33 | G,O | P |
| 33 | 34 | G,O | P |
| 34 | 35 | G,O | P |
| 35 | 36 | G,O | P |
| 36 | 37 | G,O | P |
| 37 | 38 | G,O | P |
| 38 | 39 | G,O | P |
| 39 | 40 | G,O | P |
| 40 | 41 | G,O | P |
| 41 | 42 | G,O | P |
| 42 | 43 | G,O | P |
| 43 | 44 | G,O | P |
| 44 | 45 | G,O | P |
| 45 | 46 | G,O | P |
| 46 | 47 | G,O | P |
| 47 | 48 | G,O | P |
| 48 | 49 | G,O | P |
| 49 | 50 | G,O | P |
| 50 | 51 | G,O | P |
| 51 | 52 | G,O | P |
| 52 | 53 | G,O | P |
| 53 | 54 | G,O | P |
| 54 | 55 | G,O | P |
| 55 | 56 | G,O | P |
| 56 | 57 | G,O | P |
| 57 | 58 | G,O | P |
| 58 | 59 | G,O | P |
| 59 | 60 | G,O | P |
| 60 | 61 | G,O | P |
| 61 | 62 | G,O | P |
| 62 | 63 | G,O | P |
| 63 | 64 | G,O | P |
| 64 | 65 | G,O | P |
| 65 | 66 | G,O | P |
| 66 | 67 | G,O | P |
| 67 | 68 | G,O | P |
| 68 | 69 | G,O | P |
| 69 | 70 | G,O | P |
| 70 | 71 | G,O | P |
| 71 | 72 | G,O | P |
| 72 | 73 | G,O | P |
| 73 | 74 | G,O | P |
| 74 | 75 | G,O | P |
| 75 | 76 | G,O | P |
| 76 | 77 | G,O | P |
| 77 | 78 | G,O | P |
| 78 | 79 | G,O | P |
| 79 | 80 | G,O | P |
| 80 | 81 | G,O | P |
| 81 | 82 | G,O | P |
| 82 | 83 | G,O | P |
| 83 | 84 | G,O | P |
| 84 | 85 | G,O | P |
| 85 | 86 | G,O | P |
| 86 | 87 | G,O | P |
| 87 | 88 | G,O | P |
| 88 | 89 | G,O | P |
| 89 | 90 | G,O | P |
| 90 | 91 | G,O | P |
| 91 | 92 | G,O | P |
| 92 | 93 | G,O | P |
| 93 | 94 | G,O | P |
| 94 | 95 | G,O | P |
| 95 | 96 | G,O,S | P |
| 96 | 97 | G,O | P |
| 97 | 98 | G,O | P |
| 98 | 99 | G,O | P |
| 99 | 100 | G,O | P |
| 100 | 101 | G,O | P |
| 101 | 102 | G,O | P |
| 102 | 103 | G,O | P |
| 103 | 104 | G,O | P |
| 104 | 105 | G,O | P |
| 105 | 106 | G,O | P |
| 106 | 107 | G,O | P |
| 107 | 108 | G,O | P |
| 108 | 109 | G,O | P |
| 109 | 110 | G,O | P |
| 110 | 111 | G,O | P |
| 111 | 112 | G,O | P |
| 112 | 113 | G,O | P |
| 113 | 114 | G,O | P |
| 114 | 115 | G,O | P |
| 115 | 116 | G,O | P |
| 116 | 117 | G,O | P |
| 117 | 118 | G,O | P |
| 118 | 119 | G,O | P |
| 119 | 120 | G,O | P |
| 120 | 121 | G,O | P |
| 121 | 122 | G,O | P |
| 122 | 123 | G,O | P |
| 123 | 124 | G,O | P |
| 124 | 125 | G,O | P |
| 125 | 126 | G,O | P |
| 126 | 127 | G,O | P |
| 127 | 128 | G,O | P |
| 128 | 129 | G,O | P |
| 129 | 130 | G,O | P |
| 130 | 131 | G,O,B | P |
| 131 | 132 | G,O | P |
| 132 | 133 | G,O | P |
| 133 | 134 | G,O | P |
| 134 | 135 | G,O | P |
| 135 | 136 | G,O | P |
| 136 | 137 | G,O | P |
| 137 | 138 | G,O | P |
| 138 | 139 | G,O | P |
| 139 | 140 | G,O | P |
| 140 | 141 | G,O | P |
| 141 | 142 | G,O | P |
| 142 | 143 | G,O | P |
| 143 | 144 | G,O | P |
| 144 | 145 | G,O | P |
| 145 | 146 | G,O,S | P |
| 146 | 147 | G,O | P |
| 147 | 148 | G,O | P |
| 148 | 149 | G,O | P |
| 149 | 150 | G,O | P |
| 150 | 151 | G,O,S | P |
| 151 | 152 | G,O | P |
| 152 | 153 | G,O | P |
| 153 | 154 | G,O | P |
| 154 | 155 | G,O | P |
| 155 | 156 | G,O | P |
| 156 | 157 | G,O | P |
| 157 | 158 | G,O | P |
| 158 | 159 | G,O | P |
| 159 | 160 | G,O | P |
| 160 | 161 | G,O,S | P |
| 161 | 162 | G,O | P |
| 162 | 163 | G,O | P |
| 163 | 164 | G,O | P |
| 164 | 165 | G,O | P |
| 165 | 166 | G,O | P |
| 166 | 167 | G,O | P |
| 167 | 168 | G,O | P |
| 168 | 169 | G,O | P |
| 169 | 170 | G,O | P |
| 170 | 171 | G,O | P |
| 171 | 172 | G,O | P |
| 172 | 173 | G,O | P |
| 173 | 174 | G,O | P |
| 174 | 175 | G,O,S | P |
| 175 | 176 | G,O | P |
| 176 | 177 | G,O | P |
| 177 | 178 | G,O | P |
| 178 | 179 | G,O | P |
| 179 | 180 | G,O | P |
| 180 | 181 | G,O | P |
| 181 | 182 | G,O | P |
| 182 | 183 | G,O | P |
| 183 | 184 | G,O | P |
| 184 | 185 | G,O | P |
| 185 | 186 | G,O | P |
| 186 | 187 | G,O | P |
| 187 | 188 | G,O | P |
| 188 | 189 | G,O | P |
| 189 | 190 | G,O | P |
| 190 | 191 | G,O | P |
| 191 | 192 | G,O | P |
| 192 | 193 | G,O | P |
| 193 | 194 | G,O | P |
| 194 | 195 | G,O | P |
| 195 | 196 | G,O | P |
| 196 | 197 | G,O | P |
| 197 | 198 | G,O | P |
| 198 | 199 | G,O,R | P |
| 199 | 200 | G,O,S | P |
| 200 | 201 | G,O | P |
| 201 | 202 | G,O | P |
| 202 | 203 | G,O | P |
| 203 | 204 | G,O | P |
| 204 | 205 | G,O | P |
| 205 | 206 | G,O | P |
| 206 | 207 | G,O | P |
| 207 | 208 | G,O | P |
| 208 | 209 | G,O | P |
| 209 | 210 | G,O | P |
| 210 | 211 | G,O | P |
| 211 | 212 | G,O | P |
| 212 | 213 | G,O | P |
| 213 | 214 | G,O | P |
| 214 | 215 | G,O | P |
| 215 | 216 | G,O | P |
| 216 | 217 | G,O | P |
| 217 | 218 | G,O,S | P |
| 218 | 219 | G,O | P |
| 219 | 220 | G,O | P |
| 220 | 221 | G,O | P |
| 221 | 222 | G,O | P |
| 222 | 223 | G,O | P |
| 223 | 224 | G,O | P |
| 224 | 225 | G,O | P |
| 225 | 226 | G,O,S | P |
## All-page 200-dpi automated print raster pass — follow-up, 7 November 2026

Rendered **all 225 print interior pages** with PyMuPDF at **200 dpi** in grayscale (`1425 × 2050` pixels each), analysed per-page nonwhite-pixel regions with threshold 230/255, and wrote a local tabular measurement report. This is a machine raster/margin analysis, not human per-page 200dpi inspection. All 225 raster operations succeeded.

- Exactly **two completely blank pages**, print 6 and 130, consistent with the two reading blanks noted above. No unexpected completely white page was detected.
- Four intentionally full-charcoal division pages, print **11, 59, 131, 195**, extend dark ink to all four PDF boundaries as expected from the bleed requirement. No other nonblank page had nonwhite ink closer than 0.1 inch to any physical edge under the scan threshold.
- Low ink-coverage pages 1, 3, 26, 73, 129, 144, 194, 216 and 225 are sparse front matter, chapter-ending material or final colophon in the thumbnail overview; density alone is not evidence of dropped text. This step does **not** validate paragraph completeness.
- The print 225-page dimensions remain 513×738pt; no off-page extracted word boxes in either PDF. All 33 text-layer mismatches are now categorized above; visual verification of representative ligatures remains open.

The final high-DPI **visual** every-page ledger and print/reading human comparison are still **PENDING**. This machine pass must not be re-labelled as page-by-page accepted.

## Known remaining steps / no false signoffs

1. Obtain an authorised fresh **grok-4.7 highest-effort**, separate-session adversarial reread of the Chapter 9 repair at `238c169d`; record precise item-level findings and rechecks. Do not change that chapter until this reread is available. Also resolve rereads at Chapter 1 `26cb0760`, Chapter 6 `09481761` and Chapter 12 `ddbf813a`.
2. Inspect every **print** page individually at 200 dpi or greater against the reading interior, including both edge-bleed orientations, baselines, small figure labels, contrast, photo provenance, captions, clipping and endmatter. Add findings, fixes and reviewed SHA to this ledger. The index above deliberately does not say PASS for that step.
3. The 33 extraction discrepancies are categorized above (49 `fi`/`fl` replacements plus the 600dpi rasterized page). Visually confirm representative ligature glyphs and check the Chapter 9 EPUB math equation on the target e-reader; resolve issues only on proved defects and with the chapter-review dependency respected.
4. Finish the independent full-volume mathematical/voice/citation reviews and the substantive page-depth decision, then certify fresh builds of the *final* source SHA; this artefact's green native build does not certify future edits.
5. The full-books CI [run #42336817012](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/42336817012) **failed** at the preexisting Volume 3 `C-GROUP` whole-volume conceptual source/figure drift guard. Do not edit Volumes 1–3, shared layout, or `.github/workflows/build.yml` to silence it; record as independent blocker and seek owner authorisation if repair is truly needed.

**No chapter-completion, independent-review, removed-material, or final production-acceptance gate is advanced by this preliminary ledger.**
