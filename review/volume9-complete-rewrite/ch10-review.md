# Chapter 10 — rewrite record and separate checking pass

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

Status: manuscript draft complete; final-volume independent review and EPUB
validation outstanding. This record is a subsequent checking pass by the writer,
not an independent reviewer certificate.

## Coverage

Rewrote the opening, all explanations and transitions, all six labelled formal
statements and their proofs, the closing guidance, all three original exercises,
all three hints and all three idea/writeup solutions. The original epigraph,
figure block and source bibliography are retained literally. The section order
and original labels are retained. The theorem hypotheses and equality cases have
been compared with starting main; none has been weakened.

## Mathematical checking pass

- Cayley: denominator nonvanishing, both domain inclusions and both inverse
  compositions checked. The imaginary-part identity is exact.
- Montel: empty domain and empty exhaustion terms handled. The discs used for
  Cauchy estimates lie in K_(2j), including j=1. The bound is independent of n;
  diagonal extraction covers every compact. Earlier-volume estimates and
  Arzela–Ascoli references are unchanged.
- Injectivity: finite local zero order, isolated derivative zeros, Rouche's
  multiplicity count, local inverse continuity and inverse derivative checked.
  Connectedness is used in the limit clause to rule out local constancy.
- Schwarz: division at zero is removable; the radius tends to 1 after fixing z.
  Both equality cases and both automorphism compositions checked, including a=0.
- Mapping theorem: the square root is taken only of zero-free functions. The
  first root image and its negative are disjoint, and the inversion denominator
  is bounded away from zero. The supremum is finite, nonempty and positive.
  The derivative limit excludes collapse. In the missing-point step, g is
  injective, h remains admissible, and Psi is noninjective on the WHOLE disc.
  Its derivative is therefore strictly less than 1. The chain-rule contradiction
  and the positive-real normalisation both preserve every original conclusion.
- Jordan corollary: earlier-volume simple-connectivity result is used, without
  any claim of boundary extension.

## Original exercise checking

The strip exponential is bijective because its imaginary part lies in an interval
of length pi, not 2pi. The slit-plane root is the principal branch. All inverse
formulas stay in their domains. Squaring maps the open first quadrant exactly
onto H and has no critical point there. The two-fixed-point proof uses a nonzero
conjugated fixed point and the full Schwarz equality case.

## Additions

Two illustrations follow the original square figure:

1. `v9-ch10-root-separation`: an exact concrete root image, with reflected discs
   of radius 0.55 in opposite half-planes. The caption explicitly separates this
   example from the general, potentially irregular image.
2. `v9-ch10-extremal-map`: composition domains and the strict derivative estimate.

Four exercises, all after the original three, have fresh labels, star ratings,
hints and full idea/writeup solutions:

- `ex:v9-schwarz-pick`: both inequalities and complete equality classification.
- `ex:v9-conformal-radius`: strict domain monotonicity, round-disc computation
  and inner/outer-disc bounds. The equality argument uses injectivity on V.
- `ex:v9-punctured-disc`: removable extension plus inverse gives a contradiction;
  the square-root obstruction uses the earlier winding integrality theorem.
- `ex:v9-derivative-interpolation`: exact necessary/sufficient derivative range;
  extremal uniqueness and explicit nonunique quadratic maps in every interior
  case, including lambda=0.

No solution uses a later chapter or volume as a proof premise. No numerical
experiment is used as a proof.

## Corrections and qualifications

- Restored 'zero-free' to the informal root hypothesis in the opening. The
  numbered theorem already contained the correct hypothesis.
- Removed the malformed opening sentence identifying a square with a map.
- Marked the Schwarz–Christoffel square-image claim as a quoted example, with
  no use of that claim as a premise in the proved mapping theorem.
- Removed the blanket claim that there is no formula for a general domain;
  explicit examples and nonconstructive existence are now distinguished.
- Clarified that interior conformality does not assert boundary extension.

## Validation to date

The PDF-only build of the Chapter 10 text and two diagrams, before the later
portrait and Appendix I edits, exited 0: 389 print pages, 568 whole boxes,
maximum 318.2 pt, no overflow or unresolved references. Font, print, cover and
reading-PDF checks passed. The preservation checker passed all 544 old printed
labels, unchanged old captions, and all 57 original figure files.
This is an intermediate build, not final-head or final-volume verification.
The subsequent combined build is pending. Added figures and portrait still
need rendered inspection; the full EPUB build is pending.

## Combined PDF-only build and rendered inspection

The Chapter 10 + Appendix I + portrait PDF-only build exited 0 at **393 print
pages**. It checked 573 whole boxes (maximum 318.2 pt), reported no overflow or
unresolved references, and passed font, reading-PDF, print-interior and cover
checks. The preservation checker again passed all 544 original printed labels,
all original captions and 57 original figure files. A contact sheet of manuscript
PDF pages 189, 194, 195, 354 and 355 was rendered and inspected: the Riemann portrait
and all four new diagrams were visible, labels and captions legible, with no
visible collision. The source photograph was also inspected at native resolution.
The earlier scripts are illustrative algebra/numerical checks, not proof tests.
This intermediate result predates the Appendix E rewrite and is not final-volume
or exact-final-head verification. Full EPUB checks and final independent review
remain outstanding.
