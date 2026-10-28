# Compilation, mathematical and digital validation

Executed with the workspace toolchain activation and the committed shared publishing infrastructure.

| Check | Actual result |
|---|---|
| Baseline full PDF build | PASS; 173 interior / 174 reading pages, 163 numbered |
| Cumulative B–K complete-book builds | PASS; PDFs, source snapshots and logs in /workspace/volume1-checkpoints/<batch>/ |
| Final production command | ./build.sh tome1-integers; PASS |
| Final PDF geometry | 504 × 720 pt (7 × 10 in); 189 interior / 190 reading pages; final label 177 |
| Paperback | Premium colour, white paper, no bleed; even-rounded 190 pages; 0.4459 in spine |
| Shared production gates | Layout, STIX/Inter style, PDF body identity, cover master and print preflight PASS |
| Teaching boxes | 174 whole boxes; maximum 277.0 pt; no overflow or unresolved references |
| LaTeX messages | No unresolved references/citations, missing glyphs or overfull boxes. Two existing unicode-math compatibility notices remain (bracket commands); baseline also has them. |
| Portrait resolution | Four originals; effective 410,410,308,410 ppi in interior |
| Original content identifiers | All 205 retained; 224 current; no duplicate labels |
| Exercise apparatus | 101 exercises, 101 hints, 101 complete solutions; all 97 originals retained |
| Numbered result apparatus | 83 results and 83 proofs; all 81 originals retained |
| Assets | 36 nonchapter source/assets byte-identical to baseline |
| Mathematical scripts | check_math.py 32,298 + check_new.py 2,965 = 35,263 assertions, all PASS |
| Shared publishing regression suite | 68 tests PASS (26.755 s) |
| EPUBCheck 5.3.0 | 0 fatals / 0 errors / 0 warnings / 0 infos |
| EPUB structural check | 19 XHTML documents; 686 local links/resources; 224 source labels; 301 PDF-reference comparisons; no errors |
| EPUB image alternatives | All 32 content images have nonempty descriptive alternatives |
| HTML structural check | 17 pages; 2,899 local links/resources; 224 labels; 301 PDF-reference comparisons; no errors |
| Browser rendering | All 17 pages desktop and 320 px mobile; 8,820 formula occurrences rendered; no math, broken-image or JavaScript errors |
| Reader controls | 202 reveal controls; menu/theme/reveal interaction checks PASS; ideal chapter light/dark, desktop/mobile inspected |
| Visual review | Samples from all 13 chapters + field guide; six critical mathematical locations; all 28 standalone figures |
| Repository whitespace | git diff --check PASS |

The browser script's first final-heading assertion assumed one whitespace format. Inspection showed the correct data-number=13 with KaTeX accessibility text split across lines. The corrected check tests the semantic chapter number and title; the entire browser suite was rerun successfully. This was an assertion defect, not a changed book output.

Compilation is not mathematical verification; finite computations do not prove general theorems. Per-result/per-exercise source-reading evidence is in the separate ledgers. Kindle Previewer, KDP account upload/preview, a physical proof and external scholarly review were not executed.

The final logs are retained under final-logs/, including the original compressed TeX and production logs and EPUBCheck JSON.

The post-publication portability check and repair are documented in BATCH-L-PORTABLE.md. Local 68-test results are not confused with the CI setup job, where Pandoc-dependent tests are skipped; actual GitHub artifacts are checked separately.
