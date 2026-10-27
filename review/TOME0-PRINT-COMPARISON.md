# Volume 0: detailed print review and 7 × 10 comparison

Reviewed locally on 27 October 2026, from the current first-edition manuscript.

**Recommendation:** 7 × 10 inches is the stronger working format for this book's
proofs, exercises and displayed mathematics. At the same 11-point body size it
removes most automatic formula reduction and cuts the interior by 58 pages.
The tradeoff is longer prose lines. The local proofs are suitable for comparing
these choices; the production trim has not been changed or published.

## Files

- [6 × 9 interior](../build/volume0-print-review/Mathematical-Maturity-6x9-print.pdf)
- [7 × 10 interior](../build/volume0-print-review/Mathematical-Maturity-7x10-print.pdf)
- [Twelve comparison spreads](../build/volume0-print-review/Volume-0-print-comparison.pdf)

The comparison PDF is a grayscale proof for judging black-ink reproduction. The
individual interiors retain the production pipeline's scientific figure colours,
while print boxes use grayscale accents.

The comparison spreads place both source pages at their native physical size;
text is not enlarged to make one format appear more readable. PDF viewer zoom
still affects what appears on a screen. A physical comparison should be printed
at actual size, without “fit to page”. These are interiors; an adopted 7 × 10
edition would also need a cover wrap constructed for that trim and its final
interior page count.

## Comparison measurements

| Check | 6 × 9 | 7 × 10 |
| --- | ---: | ---: |
| PDF dimensions | 432 × 648 pt | 504 × 720 pt |
| PDF pages | 291 | 233 |
| Body type | 11 pt Palatino | 11 pt Palatino |
| Nominal text area | 4.65 × 7.45 in | 5.65 × 8.45 in |
| Inner / outer margins | 0.75 / 0.60 in | 0.75 / 0.60 in |
| Top / bottom margins | 0.75 / 0.80 in | 0.75 / 0.80 in |
| Approximate median body-line length | 65 characters | 80 characters |
| Automatically reduced displayed formulas | 16 | 2 |
| Smallest display scale | 78.8% | 95.8% |
| Equivalent main math size at that scale | about 8.6 pt | about 10.5 pt |
| Overfull horizontal/vertical boxes | 0 | 0 |
| Undefined or duplicate-reference warnings | 0 | 0 |
| Chapter openings on right-hand pages | 8 of 8 | 8 of 8 |
| Text extending beyond the PDF page | none | none |
| Embedded photographs/reproductions | 31 | 31 |
| Minimum photograph resolution | 300 ppi | 300 ppi |
| Fonts | embedded vector fonts | embedded vector fonts |

Page reduction is 19.9%. It does not by itself establish a printing-cost reduction:
this review compares physical layout, not printer pricing.

The line-length estimate uses ordinary body-sized text lines and excludes short
lines and headers. It is a comparative measurement, not a universal typography
threshold. The smallest formula size refers to the main math size; subscripts
and superscripts are naturally smaller.

All text, including running heads and page numbers, stays inside the page. The
smallest measured horizontal clearance is 39.20 pt at 6 × 9 and 40.34 pt at 7 × 10;
the smallest vertical clearance is 25.72 pt in both. The inside clearance is at
least 51.82 pt. These measurements include normal optical margin protrusion.

Photograph resolution was checked using Poppler's original JPEG placements.
MuPDF can expose synthetic 72-ppi tiles when reporting vector mesh shading;
those are not embedded source photographs and were not mistaken for low-resolution
photographic assets.

## Mathematical and editorial corrections made

### Hardy's sharp constant — corrected

The Chapter 4 challenge note previously claimed that truncating `a_n = 1/n`
establishes sharpness of Hardy's constant 4. That is the wrong near-extremal test.
The corrected argument uses `a_n = n^(-1/2)` up to N and zero thereafter. Integral
comparison gives `A_n = 2 sqrt(n) + O(1)`, so the first N terms on the left total
`4 log N + O(1)`, while the sum of `a_n²` is `log N + O(1)`. The remaining terms on
the left are nonnegative, excluding every constant below 4.

Location: Chapter 4, notes on challenges, item 2. In the final proofs this begins
on printed page 125 / PDF page 137 at 6 × 9, and printed page 100 / PDF page 110
at 7 × 10, continuing onto the next page in the larger format.

### Carleman numerical ratio — clarified

The same notes correctly said that the ratio of the two full sides approaches 1,
then listed 1.52, 1.94 and 2.29 without changing the denominator explicitly. Those
numbers are the left side divided by `sum a_n`, approaching e. The corrected text
names that denominator. Independent recomputation gives 1.519495, 1.937391 and
2.294372 at N = 10, 100 and 10,000.

Location: Chapter 4, notes on challenges, item 1; the same starting pages as above.

### Monty Hall conditioning — corrected

Exercise 8.9(c) now asks explicitly for the unconditional success probability of
always switching with a uniformly placed car and an informed host who always
opens 98 goat doors. The answer remains 99/100. The solution no longer claims
that conditioning on the identities of the opened doors always leaves the answer
unchanged: that requires a host-selection rule.

A counterexample is a host who leaves door 100 closed whenever the initial choice
contains the car. Observing door 100 remaining closed then identifies two equally
likely car locations, door 1 and door 100; the conditional switching probability
is 1/2, despite the unconditional strategy still succeeding with probability
99/100.

The corrected qualification appears on printed page 268 / PDF page 280 at 6 × 9,
and printed page 214 / PDF page 224 at 7 × 10.

### Smaller wording changes

- Changed “the one method” to “one method” when introducing induction.
- Replaced “multiplying two principal arguments” with the principal argument of
  a product; arguments add modulo 2π.
- In the symmetric inequality argument, pairs now refer to distinct positions in
  the list `(a,b,c)`, so repeated values do not silently collapse a set.
- Corrected the agreement in the grayscale Bayes-figure caption.

No theorem or exercise numbers were changed.

## Print-layout findings

The unmodified 7 × 10 trial exposed two overfull inline expressions, although the
6 × 9 line breaking happened to avoid them: the cosine-sum identity in the
Dirichlet-kernel solution and the statement of Cauchy–Schwarz. They are now normal
displayed formulas, preserving their mathematics and labels. Both final builds
have zero overfull boxes.

The larger trim is especially useful for the polynomial, linear-algebra and
probability material: headings wrap less, and long formulas are much closer to
the body size. The 6 × 9 measure is more comfortable for sustained prose, and its
compact physical size remains a reasonable alternative if the remaining wide
formulas are broken across lines rather than automatically reduced.

Chapter openings, half-title, title/copyright placement, running heads, contents,
exercise boxes, hints, solutions, portrait captions, workshops and image credits
were included in the visual review. All baseline 6 × 9 page maps were inspected;
final review used grayscale maps and selected full-size comparison pages. The
original artwork and type remain vector where appropriate.

## Remaining refinements before final print approval

1. **Colour-dependent captions and legends.** Several legacy figures still use
   descriptions such as “red”, “blue”, “green” or “yellow”. Some have usable line
   styles already, notably the Runge comparison; others, such as the rearranged
   harmonic-series curves, need distinct dash/marker patterns. The Chebyshev
   polynomial legend also relies heavily on colour. These should be made
   unambiguous for monochrome printing and their captions should identify the
   curves by mathematical role or line style. The newer workshop diagrams already
   use labels, markers or line patterns effectively. The comparison PDF and rendered previews
   are grayscale so that this limitation is visible.
2. **Final page rhythm.** A few chapter-end bibliography pages are sparse and some
   long solution/challenge notes cross a page turn. These are not clipped or lost
   content, but a final pass can improve the breaks after the trim is chosen.
   Avoid hard-coding page-specific adjustments before settling the trim.
3. **Longer prose measure at 7 × 10.** Approximately 80 characters per ordinary
   full body line is broad. A physical proof should settle whether to keep the
   direct comparison's 11 pt type or slightly increase the font/outside margin.
   The provided 7 × 10 proof deliberately keeps the original font and margins so
   the comparison isolates the effect of trim size.

## Teaching and content assessment

The book's strongest support for the Mathematical Maturity title is concrete:
eight worked workshops distinguish patterns from proofs, model assumptions from
conclusions, and approximations from certified error bounds. The separation of
“How to find it” from the final write-up makes the solution process visible.
The algebra/calculus content assumes comfort with school algebra and symbolic
notation; the preface's three routes and explicit forward dependencies are useful
for readers working independently.

All 130 numbered exercises have their paired hints and solutions. All 250 explicit
labels are unique, every local reference resolves, and the label numbers agree
between the two PDF sizes. Selected central arguments were inspected, including
the arithmetic bridge, the compactness step in the fundamental theorem of algebra,
weighted AM–GM, the cross-chapter Stirling proof, and the coefficient proof of
Cayley–Hamilton. The numerical and algebraic claims in all eight workshops were
checked independently, including the six-term logarithm bound, integrated Taylor
remainder, exact least-squares residual, and both Bayes posteriors.

This is a print/pagination review with documented mathematical checks and
corrections, not a claim that every historical attribution and every proof has
received a new independent verification.

## Reproduction and evidence

```sh
source /workspace/order-chance-system/activate.sh
python3 tools/compare_print.py tome0-mathematical-maturity
```

The helper builds both proofs through three TeX passes without modifying shared
production geometry, writing to `dist/`, or publishing. Its explicit 7 × 10
override runs at the end of the existing preamble and updates the running-head
width after changing geometry.

Local evidence in `build/volume0-print-review/` includes `build-summary.json`,
`pdf-audit-summary.json`, `structure-audit.json`, `mathematical-checks.json`,
`comparison-pages.json`, logs and grayscale page maps. All 15 publishing regression
tests, the first-edition copy guard, font checks and `git diff --check` pass.
