# Preface cleanup — 28 October 2026

## Changes implemented
At the author's request, removed both complete sections from Volume 0's preface:
“A note on references to the first arrangement” and “Ten bridges for a second
reading,” including the latter's introductory paragraph and all ten list items.

## Mathematical and pedagogical effect
No mathematical chapter, problem, hint or solution changed. All 155 exercise
triples and all 299 source labels remain. The preface now ends with its series map.

## Content preservation
The previous preface and baseline commit are preserved under
/workspace/volume0-checkpoints/preface-cleanup/. Baseline: 5005161.
The latest approved KDP export changes were fast-forwarded before editing.

## Verification
Complete production rebuild passes, including the approved PDF 1.3 interior and
PDF 1.5 cover export/provenance checks. Reading PDF: 296 pages; interior: 295.
Text checks confirm both sections are absent from PDF, EPUB and HTML.
EPUBCheck 5.3.0: zero fatals, errors, warnings or infos.
Digital validation: all 299 labels, 155 exercise/hint/solution triples and 496
explicit references preserved/verified in both EPUB and HTML; no broken local
links/resources. Source preservation and git diff --check pass.

## Remaining issues and next work
No issue remains for the requested removal. Verify the exact GitHub publication
after push; do not infer publication from a local build alone.
