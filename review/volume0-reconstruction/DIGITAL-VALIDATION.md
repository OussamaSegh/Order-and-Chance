# EPUB and HTML validation follow-up

Date: 28 October 2026. This follow-up supersedes the earlier deliverable notes
which correctly recorded EPUB/HTML as unexecuted at the end of Batch J.

The full production build generated the revised EPUB, all 53 SVG figures and
the chapter-by-chapter HTML reader. Pre-existing approved cover work through
`47132c3` was merged before rebuilding; no concurrent artwork was discarded.

## Conversion corrections

Pandoc ignores LaTeX's chapter-counter reset. A preprocessing marker now preserves
it, and the existing numbering pass applies the chapter/section/result/exercise
and reference numbers from Chapter 0 onward. Figures and equations in Chapter 0 use book.cls's
unprefixed number. Ordinary books and alphabetic appendices retain their existing
behaviour. A new regression exercises Chapter 0, the transition to Chapter 1,
theorem/section references and exercise hints/solutions.

Four formulas in the language chapter initially fell back to raw TeX because
texmath does not support low-level `\hbox`. The converter normalises it to
`\text`; a regression checks native MathML. The full digital validator rejects
raw-TeX fallback, not merely invalid EPUB packaging. No mathematical manuscript
was changed for these conversion repairs.

## Executed checks

| Check | Result |
|---|---|
| EPUBCheck 5.3.0, complete EPUB | 0 fatals, errors, warnings or infos |
| EPUB XML/CRC and local links/resources | Passed across 17 XHTML documents and 1,054 links/resources |
| Assembled HTML reader links/resources | Passed across 15 pages and 3,018 links/resources |
| Explicit reference numbers versus compiled PDF | All 508 checked in each format |
| Source labels | All 299 retained in each format |
| Exercises/hints/solutions | All 155/155/155 retained and paired in each format |
| Native EPUB mathematics | No raw-TeX fallback found |
| Browser mathematics | 11,817 formula occurrences rendered, with no KaTeX failures |
| Browser hint/solution controls | All 310 reveal controls created; interaction checked |
| Responsive reader | Desktop and 320 px viewport checks; light/dark and menu/theme/reveal controls checked |
| Browser resources and JavaScript | No broken images or page JavaScript errors |
| Relevant complete publishing test suite | 67 tests passed, including EPUBCheck-backed regression |
| Full PDF production preflight | Passed; 295-page print body, 296-page covered reading PDF |

The structural check validates the reader inside the assembled site, so its
All-books/PDF/EPUB links are checked at their actual publication paths. Desktop
and mobile/light/dark screenshots were inspected. These checks establish local
format correctness; they do not substitute for every commercial e-reader's
device-specific behaviour.

Reproducible checks: `validate_digital.py`, `check_html_browser.py`,
`tools/test_epub.py`; EPUBCheck requires its separately downloaded official JAR.
Browser diagnostics require Playwright/Chromium and the local site server.
Machine-readable outcomes are `digital-structure-results.json` and
`digital-browser-results.json`; exact validation/build output is in `final-logs/`.

## Publication

The user authorised pushing the validated revision. Main's existing workflow
builds all affected books, then publishes the complete library and Pages site.
Its exact run and publication outcome must be checked for the pushed commit;
a local pass alone is not reported as a successful remote deployment.
Cross-volume numeric-citation and historical-proofread follow-ups remain as
documented in OUTSTANDING-ISSUES.md.
