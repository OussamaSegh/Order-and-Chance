# Volume 1 enhancement and review — 27 October 2026

Starting repository revision: `024daef`. Scope: all twelve chapters of *The Integers*, their companion notebooks, reading aids, illustrations and publication outputs. Existing numbered results and exercises retain their numbers so that citations from other volumes remain valid.

## Editorial changes

Every chapter received additional explanation, worked examples, proof motivation and warnings about hypotheses. Six new exercises were appended in Chapters 1–3, each with a hint and a complete solution. Later chapters received more detailed hints, computational recipes, and clearer distinctions between experiments, theorems and conjectures. Humor accompanies the mathematics without replacing its explanation.

The volume now contains 97 exercises with matching hints and solutions, 28 mathematical diagrams (13 new), four credited public-domain historical reproductions, a longer prerequisite/reading guide, and an end-of-book arithmetic field guide. The new diagrams illustrate Bézout solution lattices, sieving, Hensel lifts, visible lattice points, divisor factor pairs, orders, reciprocity, representations of 65, approximation errors, Pythagorean incircles, Gaussian rounding, ideal remainders and p-adic lifting. New figures use explicit labels, marker shapes or line patterns; the existing p-adic tree also gains a dashed/solid distinction.

The twelve notebooks gained guided experiments and prediction prompts, five additional plots, reproducible teaching randomness, exact arithmetic checks, and accurate limits on cryptographic demonstrations and computational evidence.

## Mathematical corrections

- **Chapters 1–3:** handle the zero subgroup and square root of zero; give a self-contained existence proof for integer prime factorisation; clarify signed valuations and the final Fibonacci quotient; supply an actual upper prime-count bound; distinguish Euclid's new prime divisor from primality of the constructed number; treat Wilson at 2; explain algebra vocabulary, legal cancellation and derivative hypotheses; prove toy RSA correctness for nonunits as well as units.
- **Chapters 4–6:** distinguish a mean asymptotic from a short-interval assertion; make the perfect-number argument explicit; correct base-dependent Artin density; require positive exponents in power equations; cover zero in Euler's criterion; justify multiplicativity and Jacobi swaps for noncoprime inputs; repair an unsafe Gauss-sum hint.
- **Chapters 7–9:** fix the circle-count lower bound for small radii and include the origin; separate the cattle problem's huge admissible herd from a fundamental Pell solution; handle a period beginning at continued-fraction index zero, repeated initial denominators and existence of the least Pell unit; include zero among square triangular numbers; distinguish the integer undecidability theorem from the open rational problem; distinguish idealised calendar models from actual civil calendars.
- **Chapters 10–12:** clarify ideal generators and quotient arithmetic, common irreducible factors and descent; replace a rounded estimate in the class-number-two proof with the exact bound 9/16; distinguish nontrivial completions from the trivial one; correct the harmonic-series comparison; distinguish finite modular roots from compatible p-adic roots; express modular obstructions in terms of primitive solutions and explain precision lost in division.

An independent second reading of all chapter additions, the preface and the field guide found no further substantive mathematical error. Numerical spot checks included all reciprocity-table entries, worked continued fractions/Pell solutions, divisor identities, carry counts, toy RSA messages and modular root families. These are editorial and computational checks, not a claim of formal verification.

## Reproducible checks

- Compile all publication formats with `./build.sh volume1-integers`.
- Execute the twelve source notebooks with Jupyter/nbclient in fresh kernels. This review ran 145 code cells successfully and rendered 17 plots. The execution report, executed notebooks and source SHA256 hashes are in `build/volume1-notebook-review/`.
- Compare original and revised labelled theorem/exercise sequences; verify a one-to-one match of exercises, hints and solutions and resolve all internal references.
- Inspect final LaTeX logs for errors, undefined/multiply-defined references, oversized floats and overfull boxes; inspect representative pages in grayscale.
- Check PDF dimensions, page counts and embedding with Poppler, including `pdfinfo`, `pdffonts` and `pdfimages -list`.
- Validate the EPUB with EPUBCheck 5.3.0 and check links/resources in the online chapter reader.

The first real EPUBCheck run exposed pre-existing conversion errors (duplicate exercise anchors, invalid attributes, MathML syntax and a missing manifest property). Those are fixed in the conversion helpers so regeneration retains the corrections. Regression checks accompany the tool changes.

## Publication boundary

The files are prepared locally. No GitHub push, release replacement or KDP upload was performed. A real paperback ISBN has not been supplied; the manuscript omits the placeholder, and the source can print an assigned ISBN and generate its barcode after rebuilding. Final account metadata, accurate AI-content disclosure, Kindle Previewer, KDP Print Previewer and a physical proof remain the publisher's upload-stage checks. See `volume1-integers/PUBLISHING.md` for the exact files and settings.

## Final validated outputs

| Check | Result |
|---|---|
| Paperback | 214 pages, 432 × 648 pt (6 × 9 inches), no bleed |
| Cover wrap | 916.697 × 666 pt, 0.4819-inch spine for 214 white-paper pages |
| Title/copyright | Title on recto page 5; copyright on verso page 6; no ISBN placeholder |
| Other PDFs | A4 141 pages; phone 273 pages; fixed-page e-reader 337 pages |
| All four book PDF logs | Zero overfull boxes, undefined references, or LaTeX warnings |
| Fonts | Embedded subset vector fonts, no Type 3 fonts, in all PDFs including wrap |
| Historical images in print | Four images, minimum effective resolution 308 ppi |
| Kindle cover | 1600 × 2560 JPEG |
| EPUBCheck 5.3.0 | Zero errors, warnings or informational messages |
| Image alternatives | All 32 EPUB content images have descriptive alternatives |
| Online reader | 16 HTML pages; 2,438 internal links/resources verified; no duplicate IDs |
| Notebooks | All 12 pass; 145 code cells; 17 rendered plots; source hashes match |
| Converter regression tests | Four pass, including EPUBCheck on the miniature EPUB |

Representative interior pages and the cover were visually inspected, including grayscale diagrams, worked examples, exercise boxes, title/copyright pages and the field guide. The final production pass also corrected a title-page recto issue caused by the two-page series catalogue, a stale running head in the field guide, an oversized e-reader figure, and duplicate contents IDs on the online reader's index page.

Machine-readable checks: `build/volume1-publication-review.json`; EPUB validation log: `build/volume1-epubcheck.txt`; regression results: `build/volume1-tools-tests.txt`. The assembled handoff is `dist/volume1-publication-package.zip`; build artifacts remain outside version control.
