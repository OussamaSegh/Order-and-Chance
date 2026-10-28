# Cover and typography handoff

The author requested coordination between the separate cover and typography
threads on 28 October 2026. The shared repository is the handoff channel; the
typography session has no direct messaging channel to the other chat thread.

## Integrated work

- Cover baseline: `788fb50`, **Prepare traced vector paperback masters and enforce
  print resolution**. Its templates, vector assets, native grain, visible-frame
  guard, 300 ppi preflight and retained CI reports are preserved unchanged.
- Typography: `528f1c6` and `895d25d`, bundled Libertinus Serif/Math, Inter Text and
  DejaVu Sans Mono; full-colour interiors, EPUB and web readers; source reflow and
  Unicode compatibility. These commits are descendants of the cover baseline.
- A path audit against `788fb50` confirms no typography changes to
  `tools/cover*.tex`, cover assets, volume motifs or back-cover blurbs.
- The integrated publishing suite has 48 tests. All 19 volume jobs in run
  [40605623073](https://github.com/OussamaSegh/Order-and-Chance/actions/runs/40605623073)
  pass. Local checks cover 4,131 print pages and 2,880 whole framed boxes.

## Responsibilities and shared dependencies

| Area | Handoff |
| --- | --- |
| Cover templates, masters, motifs and grain | Cover thread; preserve the approved digital PNGs and print-vector provenance. |
| Interior fonts, preamble, source reflow, EPUB/reader styles | Typography implementation above; fonts are in `common/fonts/`, separate from the existing cover fonts. |
| Trim, paper and spine | Keep canonical `common/print-layout.json`: 7 × 10, premium colour, white paper, 0.002347 inch per even-rounded print page. |
| Page counts and wrap size | Read the actual `dist/kdp/<book>-print.pdf` and its freshly generated metadata. Font changes alter pagination. Never use the covered reading PDF or historical review counts. |
| Shared palette | Existing cover tokens are preserved; new interior roles are coral, blue, teal and plum. Keep both sets of uses when editing `common/design-colors.tex`. |
| Build/CI/cache | XeLaTeX, bundled fonts, extra plot memory, cache schema 5; retain interior font/colour/layout checks and cover resolution/vector checks together. |
| Documentation | Retain both the colour-interior and print-cover sections in `docs/DESIGN.md` and `tools/PUBLISHING.md`. |

Fetch current `main` immediately before editing shared files and again before
pushing. Integrate concurrent commits without force-pushing. Use a separate
checkout for merges while local TeX builds are active. Do not cancel another
thread's publication run; verify which exact commit a run and release contain.
This handoff does not authorize changes to the other thread's artwork or fonts.


## Subsequent cover-vibrancy correction

The cover workstream now corrects the sixteen native-vector covers' noisier grain
and flat artwork following the author's Volume 2/3 comparison. The change is confined
to cover templates, plate rendering and the cover preflight's paper whitelist;
it preserves all typography work, premium-colour settings and body content.
Approved Volumes 0–2 and the print-vector assets remain unchanged. Both print
wraps and the affected digital cover assets use the corrected material. See the
latest section of `docs/DESIGN.md`; keep this correction during future integration.

## Version C approval

The author selected version C for all 19 interiors after the font review. The
implementation preserves cover commit `c839bba`. Headings now use the exact cover
Inter faces; STIX Two provides body/math. The quieter box styling uses coral left
rules and charcoal labels. Canonical premium-colour geometry remains unchanged,
but new fonts require fresh interior page counts and wraps. Preserve schema 6 and
the STIX/Inter/charcoal/coral gates together with the cover-material preflight.
