# Mathematical corrections and review index

Each writer record describes the original problem, corrected mathematical claim
or proof, and reason/counterexample. The commit column applies to those explicit
corrections. Separate reviewers compared every one of the180 original formal
statements and72 original exercises with the immutable full baseline, and read
all116 final exercises/hints/solutions. No silent theorem weakening is accepted.
All original printed numbers and labels pass the built preservation gate.

| Chapter | Title | Original problems and corrections | Separate final source review | Fixing commits |
| --- | --- | --- | --- | --- |
| 1 | Categories | [writer](ch01-writer.md) | [separate review](ch01-review.md) | 25ea2a53 (initial rewrite), ee5c8ac6 (separate-review precision repair) |
| 2 | Tensors and the Cost of Multiplying Matrices | [writer](ch02-writer.md) | [separate review](ch02-review.md) | b03ed741 (initial rewrite), ee5c8ac6 (preserve characteristic-three Waring identity) |
| 3 | Tensors and Exactness | [writer](ch03-writer.md) | [separate review](ch03-review.md) | 25ea2a53 (mathematical rewrite), ee5c8ac6 (new-diagram arrow) |
| 4 | Noetherian Rings and Hilbert's Theorems | [writer](ch04-writer.md) | [separate review](ch04-review.md) | b03ed741 (mathematical rewrite), ee5c8ac6 (reduced-basis precision) |
| 5 | Localisation and Dimension | [writer](ch05-writer.md) | [separate review](ch05-review.md) | 291af767 |
| 6 | Dedekind Domains | [writer](ch06-writer.md) | [separate review](ch06-review.md) | ee5c8ac6 |
| 7 | Homological Algebra | [writer](ch07-writer.md) | [separate review](ch07-review.md) | 291af767 |
| 8 | Group Cohomology | [writer](ch08-writer.md) | [separate review](ch08-review.md) | c42d33c6 |
| 9 | Semisimple Algebras and Induction | [writer](ch09-writer.md) | [separate review](ch09-review.md) | 2d3fe09c (initial rewrite), ee5c8ac6 (notation and fixed-point-key precision) |
| 10 | The Symmetric Group | [writer](ch10-writer.md) | [separate review](ch10-review.md) | c42d33c6 (initial rewrite), ee5c8ac6 (Russian-coordinate scale) |
| 11 | Compact Groups | [writer](ch11-writer.md) | [separate review](ch11-review.md) | c9f0258a |

## Additional findings from the separate review phase

- **Ch1 duality:** a complex Hermitian inner product identifies the ordinary
  linear dual conjugate-linearly, whereas a nondegenerate bilinear form gives a
  linear identification. Fixed in ee5c8ac6; no theorem hypothesis removed.
- **Ch2 Waring:** the first draft restricted to R/C. Direct ordered-entry
  comparison proves the four-term tensor identity in every characteristic except 2,
  including 3. Division by 4 is the exact obstruction to this formula in 2.
  Fixed in ee5c8ac6 and checked directly in characteristics 3, 5, 7.
- **Ch4 reduced basis:** the first draft reduced only tails. {1,X} then passed
  its wording for the unit ideal. All monomials of a generator must avoid the
  other leading monomials. Fixed in ee5c8ac6.
- **Ch9:** restored a missing backslash in operatorname and made the new affine
  diagram's no-fixed-point symbol distinct from fixed point 0. Fixed in ee5c8ac6.
- **Ch10 limit shape:** specified u=(x−y)/sqrt(n), v=(x+y)/sqrt(n), including the
  sqrt(2) beyond orthonormal rotation; the original curve formula is retained.
  Fixed in ee5c8ac6.
- **Ch11:** exponent commas, moment-caption ambiguity and an unnecessarily
  restricted n=1 dimension request were corrected before c9f0258a. The full
  theorem/exercise content is rechecked in the separate chapter review.

Production fixes are separate from mathematics: the unsupported new-diagram arrow
was replaced with a supported arrow; standalone cover copy now uses mathbb{Z}
instead of the interior-only Z macro (8506bdfa). The generator provenance phrase
and 80–150 word cover-note guard were retained, with no artwork changes.
