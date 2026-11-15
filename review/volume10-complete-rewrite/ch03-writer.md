# Chapter 3 writer record

Owned source: `volume10-abstraction/chapters/ch02-tensors.tex` (printed Chapter 3).
Starting main is `59014a9aad3454ad60786c6549c81fcac88df9df`; raw content baseline is `starting-statement-content.json`.

Complete writer pass finished on all opening prose, definitions, formal statements, proofs, worked calculations, original exercises, hints, idea/writeup solutions and closing guidance. Literal bibliography records and the complete original snake figure block are retained. This is a writer pass, not independent certification. All 18 original formal statements have the same environments and labels in the same order, all six original exercises retain their numbers, and all original numbered sections remain in order. Parent will record actual production commands, printed numbers and commit SHAs after validation.

## Corrections and prerequisite repairs

- **C03-1: original composite-kernel solution mislabels the snake map.** The displayed old snake sequence labelled the arrow `ker g -> coker f` by `partial`, although the construction described the arrow `coker f -> coker(gf)`. The exercise statement itself is correct. The replacement gives every arrow explicitly and checks exactness directly at every term; a final sentence identifies the correct snake arrow. No statement or label was weakened.
- **C03-2: cyclic Hom and tensor parameters.** The original exercise and worked tensor formula did not state that `m,n` are positive. With `m>0,n=0`, `Hom(Z/m,Z)=0`, whereas the displayed `Z/gcd(m,0)` would be `Z/m`. The corrected exercise and worked cyclic-tensor example specify positive integers, the domain under which the original formulas and original solutions are valid. This is an explicit missing-domain repair.
- **C03-3: bilinear need not mean non-linear.** The old blanket sentence “Bilinear maps are not linear” excluded the zero map incorrectly. The rewrite says a bilinear map need not be jointly linear and supplies the multiplication example `(1,0)+(0,1)`; the determinant example explicitly concerns two columns of a 2 by 2 matrix.
- **C03-4: forward localisation prerequisite removed.** The old prose asserted that `Q` is flat, with its proof deferred to Chapter 5. A local fractions construction and proof that tensoring an injection with `Q` stays injective now appear before that assertion is used. This uses only the tensor construction and scalar transfer already taught here.
- The introductory slogan about projective, injective and flat modules keeping “all” sequences is replaced by the distinct Hom lifting/extension and tensor injection conditions. The zero and empty-basis/direct-sum cases are checked.

Earlier-source checks actually read: Volume 3 Chapter 7's PID structure theorem (`thm:structure`, printed 7.6); Chapter 6's Chinese remainder theorem (`thm:crtring`, printed 6.9) and polynomial UFD theorem (`thm:gaussufd`, printed 6.18); Volume 7 Chapter 1's Zorn proof (`thm:zorn`, printed 1.19). Chapter 1 internal universal-property and adjunction citations retain their existing labels. No later-volume statement is used as a premise. The text distinguishes quoted Winograd optimality from the locally proved Strassen construction.

## Additions

Exactly two new figure sources and numbered blocks follow the last original figure:

1. `v10-new-ch03-collapse.tex`: tensoring the opening sequence with `Z/2` keeps the quotient and destroys the first injection.
2. `v10-new-ch03-lifts.tex`: the missing lift and extension arrows distinguish projectivity and injectivity.

Exactly four new graded exercises follow the original six, with useful hints and complete idea/writeup solutions:

- `ex:v10new-ch03-quotients`: quotient-ring tensor products, integers, and a nilpotent example.
- `ex:v10new-ch03-snake`: explicit snake map for two multiplication maps, including `m=6,n=4` and coprime/zero-kernel cases.
- `ex:v10new-ch03-idempotent`: projective summands from idempotents and the non-domain obstruction.
- `ex:v10new-ch03-finiterank`: arbitrary-space tensor/Hom map and the infinite-rank identity counterexample.

## Checks actually performed

A local source inventory compared all original environment counts, every original label, and the complete ordered numbered-section list against the original captured source: no missing labels or changed counts/order. Figure block preservation was checked by retaining the exact captured block rather than retyping it. No build or rendered inspection is claimed in this writer record; parent owns those checks. The independent reviewer has sent initial boundary-case findings, incorporated above. Separate final review remains required.
