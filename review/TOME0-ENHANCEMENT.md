# Tome 0 mathematical and publication revision

The revision strengthens the existing book without replacing its problem sequence.
All 130 numbered exercises retain their labels, hints and solutions. The original
label order is preserved, and all 250 explicit labels are unique; 386 explicit
local references resolve. These checks establish structural consistency, not the
mathematical truth of every sentence.

## Mathematical corrections and explanations

- Added a proved arithmetic bridge: Bézout's identity, Euclid's lemma, existence
  and uniqueness of prime factorisation. Earlier exercises no longer have to
  borrow those cancellation facts silently from Tome 1.
- Distinguished a quadratic from a degenerate linear equation, arguments from
  their chosen representatives, indirect similarities from reflections, and
  chord lengths from signed half-angle coefficients.
- Supplied the closed-disc compactness argument in the fundamental theorem of
  algebra from coordinatewise Bolzano–Weierstrass. Restricted the local bound
  in that proof to the compact interval actually used.
- Repaired the rearrangement-to-AM–GM substitution and spelled out a substitution
  that really proves the intended inequality. Clarified the zero-vector equality
  case in Cauchy–Schwarz.
- Repaired an insufficient bound in the example proving log(n)/sqrt(n) tends to
  zero; distinguished completeness-dependent conclusions from algebraic limit
  rules. Corrected the limiting-index explanation in Dirichlet's remainder bound.
- Handled Taylor–Young at order zero; removed false blanket claims that Taylor
  approximations improve everywhere with each degree or cannot approximate
  outside their interval of series convergence.
- Distinguished conditioning from a small determinant; covered the zero root in
  the recurrence discussion and the degeneracy of a singular symmetric image
  of the circle. Expanded the Gram–Schmidt layout and successive-height definition.
- Specified hypergeometric parameter domains and the one-object edge case.
  Distinguished finite-sample concentration from evidence of pathwise convergence.

## Added teaching material

Each of the eight chapters has a guided workshop: a worked example, a mission,
a staged hint or hints, a complete solution and a caution about a tempting error.
The topics are finite patterns versus proofs, turn-and-stretch robot navigation,
sensitive roots and interpolation, quantitative inequality slack, accelerated
certified logarithms, Taylor integration with a certified remainder, exact least
squares, and Bayesian testing with conditional dependence.

Eight new vector graphs use distinct lines/markers/gray fills. Three authentic
NASA/SpaceX photographs add application context; their downloaded hashes match
the pinned scikit-image registry. Captions, source/licence records and book image
credits accompany them. Legacy historical-image credits are retained; their
original provenance has not been independently recovered in this revision.

The new field guide connects problem types to proof strategies. The preface now
explains reading routes, forward dependencies and the boundary between proved
results and admitted elementary-function/integration foundations. Light humour
supports the explanation rather than replacing it.

## Validation

All eight source notebooks executed in fresh kernels: **106 nonempty code cells,
13 rendered plots, no error outputs**. The executed code matches the current
source exactly; source SHA256 values and counts are in
`build/tome0-notebook-review.json`. The added cells check exact algebraic identities,
root perturbations, quantitative inequalities, rigorous truncation bounds,
projection residuals and Bayesian probabilities.

Five converter regression tests pass, including EPUBCheck on a miniature EPUB
and a new test that a contextual photograph retains its explicit alternative text
instead of being labelled as a portrait. Full-book EPUBCheck and final output
measurements are recorded below and in the generated review files.

Publication outputs, checksums and machine-readable measurements are generated
under `dist/` and `build/`, both ignored by Git. Images are sized for approximately
300 ppi or better in print; effective resolution is also checked in the actual PDF.
Synthetic raster tiles exposed by MuPDF when rendering vector mesh shading are
not classified as embedded source photographs; Poppler independently lists the
31 actual embedded images.

## Publication boundary

This is a substantive mathematical/editorial review and a tested local production
handoff, not a claim of formal verification or an error-free book. The original
ISBN 9798165526770 is preserved and has a valid checksum; its assignment to this
edition must be checked against the publisher's account. The wrap uses the
current interior's even-rounded page count and the repository's white-paper spine
formula. Changing layout requires rebuilding it.

KDP/Kindle Previewer, account metadata, accurate AI-content disclosure and a
physical proof remain publisher checks. No Git push, release replacement, Pages
deployment or KDP upload is included in this revision. See
`tome0-back-in-shape/PUBLISHING.md` for the file mapping and upload settings.

## Final measured outputs

| Check | Result |
|---|---|
| Paperback interior | 293 pages, 432 × 648 pt (6 × 9 inches), no bleed |
| Cover wrap | 929.671 × 666 pt; 0.6621-inch spine based on 294 even-rounded pages |
| A4 / phone / fixed e-reader | 191 / 378 / 471 pages |
| Print title / copyright | Physical recto page 5 / verso page 6 |
| Print fonts | All embedded; no Type 3 fonts |
| Print photographs/reproductions | 31 embedded images; minimum effective resolution rounds to 300 ppi |
| Minimum horizontal text clearance | 39.20 pt (above the 18 pt no-bleed minimum) |
| Kindle cover | 1600 × 2560 JPEG |
| Full EPUBCheck 5.3.0 | 0 fatals, errors, warnings or informational messages |
| EPUB internal links/resources | 1047 verified; XML parsed and IDs checked |
| Assembled online reader | 13 HTML pages; 2134 internal links/resources verified |
| Numbered exercises | 130 paired hints and solutions; original label sequence preserved |
| Notebook execution | 8 notebooks, 106 nonempty code cells, 13 plots; no errors |
| Converter regression tests | 5 passed, including miniature EPUBCheck |

Final print and phone logs contain no overfull boxes. The A4 log retains one
nonfatal tcolorbox no-break warning. The fixed e-reader log retains one 0.1108 pt
(about 0.04 mm) overfull text line. Neither was suppressed or counted as a passed
zero-warning check. Representative A4 and grayscale paperback pages were visually
inspected, including title/copyright, the application photographs, the Taylor and
least-squares material, exercise boxes and image credits. This is sampling, not a
claim that every page has received an independent visual proofread.

Machine-readable measurements: `build/tome0-publication-review.json`.
Full-book validation: `build/tome0-epubcheck.txt`.
Regression output: `build/tome0-tools-tests.txt`.
Notebook records: `build/tome0-notebook-review.json`.
Upload/readership handoff: `dist/tome0-publication-package.zip`.
