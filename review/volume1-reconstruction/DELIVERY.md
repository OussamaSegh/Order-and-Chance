# Delivery and recovery

The revised canonical source is volume1-integers/main.tex.
Checkpoints volume1-batch-A through volume1-batch-L preserve each verified stage.
The original source commit is a65d685d941b8cef2c1d41f51bff65a71f885e11.
Baseline and cumulative PDFs/source snapshots/logs are also in
/workspace/volume1-checkpoints/ (outside Git).

Final generated deliverables:

- dist/volume1-integers.pdf — complete reading PDF.
- dist/kdp/volume1-integers-print.pdf — matching paperback interior.
- dist/volume1-integers.epub — validated reflowable EPUB.
- dist/html/volume1-integers/ — validated chapter reader.
- dist/kdp/volume1-integers-cover-wrap.pdf — actual-page-derived premium-colour wrap.
- dist/volume1-revision/Order-and-Chance-Volume1-source.zip — complete source project.
- dist/volume1-revision/Order-and-Chance-original-source.tar.gz — immutable baseline source backup.
- dist/volume1-revision/Volume1-reports.zip — all editorial/QA records.
- dist/volume1-revision/Volume1-HTML-reader.zip — packaged reader/site resources.
- dist/volume1-revision/manifest.json and SHA256SUMS — actual artifact hashes and sizes.
- dist/volume1-revision/publication.json — exact remote publication evidence after push.

Reproduce the book with the documented workspace activation and ./build.sh
volume1-integers. Reproduce source/asset ledgers with make_review_ledgers.py,
mathematical calculations with check_math.py and check_new.py, and digital
checks with validate_digital.py and check_html_browser.py after assembling
tools/site.py output under build/volume1-digital-review/site. The browser
script expects a local server on port 8766. EPUBCheck is a separate executed
validator, version 5.3.0.

Navigation and scholarly records: TABLE-OF-CONTENTS.md, DEPENDENCIES.md,
CONTENT-MIGRATION.md, migration-units.json, NUMBERING-CONCORDANCE.md,
MATHEMATICAL-CORRECTIONS.md, THEOREM-VERIFICATION.md,
EXERCISE-VERIFICATION.md, FINAL-EDITORIAL-REVIEW.md,
COMPILATION-AND-TESTS.md and OUTSTANDING-ISSUES.md.

Source checkpoints do not embed generated PDFs in Git. The manifest is written
only after the archives exist and pass ZIP/CRC or archive-read checks. Public
release verification is recorded separately and is never inferred merely from
a successful local build.
