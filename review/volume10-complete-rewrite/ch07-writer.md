# Chapter 7 writer record

Complete draft rewritten in `chapters/ch06-homological.tex`, including the opener,
all explanatory prose, all thirteen original formal statements, every proof,
all six original exercises, hints and idea/writeup solutions, and the closing
bridge. Original quotations and the bibliography remain literal; the complete
original surface figure block and source remain unchanged. Original section
order/count, formal statement labels/order, and exercise labels/order remain.

## Mathematical and prerequisite work

- `prop:torextbasic` now explicitly states both variances: Tor covariant in each
  variable, Ext contravariant/covariant. Its content is preserved and made precise.
- The free cyclic resolution explicitly assumes positive n. The n=1 zero-module
  case is checked; multiplication by zero is not incorrectly used as an injection.
- The two-variable Koszul resolution is verified in the main explanation, so the
  main text no longer relies on the later exercise for its exactness.
- The comparison and horseshoe proofs name each surjection onto a kernel and
  each use of projectivity. The Hom cochain differential/sign convention is given.
- UCT retains the original finitely generated/free/PID hypotheses, natural exact
  sequences, and nonnatural splitting conclusions. Its proof now supplies the
  cohomology section explicitly, explains naturality of the exact sequences,
  and checks degree zero. No arbitrary singular-chain application is claimed.
- Original de Rham sentence described algebraic duality as 'the form of de Rham's
  theorem'. Corrected: coefficient duality is algebraic; the comparison with
  differential forms is a separate quoted theorem, as actual Volume 9 ch3 says.
- Original higher-Ext paragraph said extensions classify 'in the same way', which
  risks importing the short-extension isomorphism relation. Corrected to quote
  Yoneda's classification and define its equivalence by zigzags fixing the ends.
- Whitehead independence is explicitly conditional on consistency of the usual
  axioms; advanced set theory remains quoted and no later proof depends on it.

Actual prerequisites read: Volume 9 `ch06-homology.tex` chain-complex definition,
chain-homotopy proof and zigzag lemma/proof; Volume 9 `ch03-forms.tex` de Rham
outlook; Volume 10 printed ch3 projective/flat/injective proofs and PID criterion;
printed ch4 Noetherian-module result. Only these and elementary module arithmetic
are used. General Tor symmetry, arbitrary-PID-module freeness, Hilbert syzygy and
higher-Yoneda classification are visibly quoted, not used as hidden premises.

## Additions

Exactly two new figures, after the existing surface figure:

- `v10-new-ch07-coefficients.tex`: actual projective-plane differential over Z
  versus Z/2 and the resulting top kernel.
- `v10-new-ch07-cycles.tex`: degreewise cycle/boundary splitting and the chosen
  lift that explains nonnaturality.

Exactly four appended exercises, each with stars, useful hint, and full
idea/writeup solution:

- `ex:v10new-ch07-dualnumbers`: periodic resolution over K[epsilon]/epsilon²,
  nonzero Tor/Ext in every degree, and obstruction to finite projective dimension.
- `ex:v10new-ch07-connecting`: explicit connecting class for Z/(rs), splitting
  iff gcd(r,s)=1, and an actual section including unit endpoint cases.
- `ex:v10new-ch07-coefficients`: arbitrary coefficient group calculation for a
  degree-two multiplication complex, identifying each Tor/Ext contribution.
- `ex:v10new-ch07-splitting`: a chain automorphism whose shear obstructs every
  equivariant UCT splitting, proving that natural splitting is impossible.

## Checks actually run

A local source inventory reports 3 figure blocks (1 original + 2), 10 exercise,
10 hint and 10 solution environments (6 original + 4); every original label is
present and the original figure block occurs verbatim. This is a structural
check, not a PDF build or independent mathematical certification. No build was
run by this writer. Parent owns integration, fixing-commit receipts and final
production validation. Independent final review remains required.

## Integrated fixing commits

291af767. These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
