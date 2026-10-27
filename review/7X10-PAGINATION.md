# Final 7 × 10 source pagination

Review date: 27 October 2026. Applies to all sixteen main volumes and three problem books.

## Changes

- All framed exercises/problems, reminders, beauty notes, thinking prompts and
  challenges remain whole on a PDF page. No current box requires subdivision.
  Future material taller than the text area must be reorganised in the source.
- Exercise counters, labels and hyperlink anchors travel inside their boxes when
  they move to the next page. Numbers are preserved.
- Long inline mathematics and the longest equation chains have been reflowed as
  unnumbered displays and aligned steps. A list of Fourier multiplicities is now
  a table. Mathematical expressions, hypotheses and conclusions are preserved.
- Hint and solution openings reserve space without overriding section heading
  keeps. “How to find it” stays with its solution heading. Widows and orphans are
  blocked; natural bottom whitespace avoids stretching paragraphs around boxes.
- The first two “Further exercises” labels in Volume 0 are proper subsections,
  matching the later chapters and staying with their first exercise.
- EPUB styles request whole frames, headings with following text, and paragraph
  widow/orphan control. Reflowable reading systems retain control of pagination;
  a frame taller than the device viewport may still span pages.

The 11 pt body, 7 × 10 trim, mirrored margins, ISBNs and first-edition copy policy
are preserved. The latest charcoal/coral design from main (`5936eed`) is included.
Every wrap is derived from its rebuilt interior's actual page count.

## Build gates

The shared preamble writes each frame's natural height, available text height,
source filename and line to `main.oclayout`. A split frame or a frame taller than
the text area stops TeX. `tools/check_book_layout.py` runs after the final TeX pass
and rejects horizontal/vertical overflow, oversized floats, unresolved/duplicate
references and missing or invalid frame measurements. Body type is not reduced
to make a box fit. Existing PDF geometry and embedded-vector-font gates remain.

Eight new regression tests include actual typeset proofs for moved exercises and
problems, their numbers/reference pages, solution and section openings, forbidden
split frames and oversized material. The broken opening-space implementations
were checked against the fixtures and reproduce their failures. CI runs these
proofs after installing TeX; all **34 publishing tests pass** locally.

## Local verification

- All **19** pagination interiors and their actual-page-derived wraps rebuilt.
  Full PDF/EPUB/reader pipelines for Volumes 0 and 9 were repeated after integrating
  the concurrent charcoal/coral design update; CI regenerates the whole library
  from the combined source before publication.
- **2,880** frames measured; none exceeds the approximately 610.68 TeX-point text
  height. The tallest is 479.58 pt, in Crossroads.
- All **4,206** interior pages have 504 × 720 pt bounds. No extracted text span
  crosses a physical page boundary. Final TeX logs have no overflowing lines,
  overflowing vertical material, oversized floats or unresolved references.
- All **2,169** exercise/problem named destinations resolve to their recorded PDF
  page labels. Label numbers match the prior reviewed print auxiliary files.
- The PDF scan found no isolated exercise-section, hint or solution headings.
  Mathematical superscripts on a shared baseline were accounted for when checking
  following text, avoiding false positives from extraction order.
- Every Volume 0 page was inspected in contact sheets; its revised first two
  chapters and front matter were checked again in the final 239-page proof.
  Representative exercise/hint/solution pages across all nineteen books, enlarged
  reformatted Machinery displays and the final Volume 0 paperback wrap were inspected.
- Shell syntax, layout/metadata synchronization and `git diff --check` pass.

These automated checks cover all pages; the visual review is exhaustive at contact
sheet scale for Volume 0 and representative elsewhere. Clean CI and release/Pages
publication are verified for the exact pushed commit, separately from local builds.

## Pagination proof counts

Spines use even-rounded KDP pages × 0.002252 inches. These counts supersede earlier
pagination proofs; covers must always be regenerated when an interior changes.

| Volume | Interior pages | Whole frames | Spine (in) |
|---|---:|---:|---:|
| 0 | 239 | 200 | 0.5405 |
| 1 | 173 | 169 | 0.3918 |
| 2 | 372 | 309 | 0.8377 |
| 3 | 251 | 161 | 0.5675 |
| 4 | 178 | 103 | 0.4009 |
| 5 | 176 | 109 | 0.3964 |
| 6 | 179 | 115 | 0.4054 |
| 7 | 178 | 103 | 0.4009 |
| 8 | 343 | 248 | 0.7747 |
| 9 | 152 | 89 | 0.3423 |
| 10 | 192 | 113 | 0.4324 |
| 11 | 228 | 155 | 0.5135 |
| 12 | 248 | 165 | 0.5585 |
| 13 | 211 | 120 | 0.4774 |
| 14 | 194 | 117 | 0.4369 |
| 15 | 313 | 221 | 0.7071 |
| P1 | 460 | 314 | 1.0359 |
| P2 | 75 | 46 | 0.1712 |
| P3 | 44 | 23 | 0.0991 |

Local evidence: `build/7x10-pagination/final-audit.json`, final per-book logs,
`all-tests.log`, `contact-sheets/` and `p2-display-review.png`. These are review
artifacts, not additional published book formats.
