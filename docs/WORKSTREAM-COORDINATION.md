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


## Locked master following the author's 100% coherence instruction

The cover thread now replaces every production front's layout branch with one
Volume-0 master, fixed bold type, fixed subtitle baseline and one 3D illustration.
This includes the title blocks of Volumes 0–2; their earlier PNG references remain
archived unchanged. The common header/frame/author and Volume-0 Gaussian art are
preserved as vector forms. Build/site packaging must render this shared template,
not copy the old PNGs. The new shared-template checker complements the existing
print preflight and all typography checks. Interior font assets, common preamble,
premium-colour settings, body content and page-count-dependent spines are untouched.

## Version C approval

The author selected version C for all 19 interiors after the font review. The
implementation preserves cover commit `c839bba`. Headings now use the exact cover
Inter faces; STIX Two provides body/math. The quieter box styling uses coral left
rules and charcoal labels. Canonical premium-colour geometry remains unchanged,
but new fonts require fresh interior page counts and wraps. Preserve schema 6 and
the STIX/Inter/charcoal/coral gates together with the cover-material preflight.


The locked-cover master is integrated with version C (`9c94065`). The cover title
face lives in `tools/assets/fonts/Inter-Bold.ttf`, separately from version C's
heading faces in `common/fonts/`. Shared build/cache files retain both validation
sets. Original approval PNGs stay archived, and every current format renders the
one common cover template. Fresh version-C manuscript pages determine spines.

## Subsequent approved glow and subtitle refinement

The author now requests subtitles directly below the last title line rather than
at a fixed vertical position, and approves stronger soft coral glow across the
series. Cover rendering now exports deduplicated visible wires with five layers of
vector radiance. Chance receives a distinct mathematical silhouette.
Interior content, Version C typography, premium-colour settings and actual-page
spine derivation are unchanged. Keep the title-relative PDF checks and existing
print/font/layout/navigation gates together. Baseline main was 3259d46.

## Teaching-box correction after version C

The author flagged identical box colours and inconsistent visible top/bottom
hairlines. Interior work now restores blue exercises/problems, coral
reminders/challenges, teal beauty notes and plum thinking prompts. All share a
hidden full frame plus one explicit 1 pt left rule, preventing saturated frame
underpainting from showing through at some zoom levels. STIX/Inter, charcoal
headings and coral chapter accents remain version C. Cover work through
`dabf093` and all cover templates/assets are preserved; shared fingerprints rebuild all books.

## Independent artwork review after the author's further direction

The author now authorises new illustration subjects and individual geometry poses,
scale and placement for all sixteen covers. The chapter-based review and decisions
are in docs/COVER-ART-DIRECTION.md. Cover typography, title-relative subtitles and
the shared luminous material remain intact. Current main 8135b0b was pulled first,
retaining the semantic box-colour/frame fix and its real-PDF regression. Only obsolete cover references in the Structures/Chance appendices are corrected;
mathematical statements, figures and interior styling are preserved. Fresh current
manuscript counts must determine every final wrap; no old proof count is authoritative.

## Volumes 0 and 1 harmonisation

After f4d797f the author explicitly asked for Volume 0 to use the other books'
illustration treatment, and for Volume 1 to be harmonised too. The special Gaussian
trace is now archival only; all sixteen production illustrations use the same
native renderer/material. Volume 1 retains its prime positions with lower, broader,
finer-meshed relief. Only motifs 0 and 1 change. No book content, interior styling,
fonts or print settings change. Preserve the latest semantic box work and derive
production wraps from current actual manuscript counts as usual.


## Approved KDP export integration

The author confirmed the working interior/cover files and requested the process
for every book, explicitly keeping the latest pulled artwork. Integration starts
at `a65d685`, retaining the revised ten-chapter Volume 0 and the newer cover
harmonization. Interior/cover source and fonts remain unchanged. Print-only exports
remove interactions and flatten genuine transparency: PDF 1.3 interiors at 600 ppi
where needed, PDF 1.5 covers with 600 ppi artwork composites and vector lettering.
The final-cover raster exception is limited to provenance-verified art composites;
master artwork stays vector, paper stays native >=300 ppi and whole-cover
rasterization is forbidden. Use fresh print counts and retain schema-7 reports,
reading navigation and visual parity checks. See docs/KDP-EXPORT.md and AGENTS.md.
