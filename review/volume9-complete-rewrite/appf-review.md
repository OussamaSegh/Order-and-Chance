# Appendix F writer check — plane curves

## Coverage
All body prose, original formal statements/proofs, twelve original exercises, hints and idea/writeup solutions, closing bridge and reading guidance are rewritten. The literal epigraph, three old figure blocks/captions and bibliographic records are preserved. This is a writer check, not separate final review.

## Corrections and prerequisites
- The resultant definition distinguishes declared degree bounds from actual degrees. Its common-factor equivalence retains nonzero leading coefficients. The homogeneous degree proof uses determinant term weights, valid over finite fields.
- The coefficient-count proposition now has a proof. Curve equations retain factors and multiplicities rather than identifying arbitrary finite-field point sets with polynomials.
- Bezout proves finiteness before selecting a separating projection. Coprimality under coefficient extension is justified with a resultant in a variable on which the proposed common factor depends. Multiplicities remain explicitly relative to a chosen O; independence and intrinsic local algebra are quoted previews, not claimed proved.
- A local shared-tangent calculation supplements the singular-point lemma and justifies the two double circular intersections for distinct concentric circles.
- CORRECTION: the singular-bound proof now establishes infinitely many curve points and finitely many singular points before choosing further smooth points. A nonzero derivative exists by irreducibility and perfection in positive characteristic.
- CORRECTION: a singular quadratic is handled by its six monomial coefficients, including characteristic two. The old 2Ax argument was invalid there.
- Five-point independence explicitly assumes distinct points. The Pascal corollary explicitly assumes six distinct vertices; every extra intersection is checked distinct.
- CORRECTION: the polar exercise proves the actual nonzero Q gives a nonzero polar, not merely that some suitable Q does. Smoothness and irreducibility are justified, and the unsupported numerical assertion of generically exactly six tangents is removed.
- The characteristic-two discriminant case is proved directly when the derivative drops degree. The grid requires characteristic different from two. Folium/node/cusp parametrizations include infinity values.
- Pappus uses nine intersections that are verified distinct under its standard hypotheses, eliminating the old limiting argument over arbitrary fields.
- Genus and full associativity claims are clearly quoted extensions, with field and generic-case qualifications.

## Additions and actual checks
Two diagrams explain cusp intersection orders and interpolation weights. Four fully solved exercises address resultant specialization, exact cusp orders, sharp grid interpolation and positive-characteristic tangent counterexamples, each with difficulty and hint.

The twenty-one-unit PDF-only build exits 0 at 505 print pages, with layout/font/print/cover checks passing and no overflow or unresolved references. All 544 original labels/captions, 213 numbered structure entries, 57 figure files and cover artwork pass preservation. Both diagrams were inspected on PDF pages 400/401. The cusp annotation was then moved below the plot to remove a curve crossing; that repair awaits the next rendering. Appendix D's repaired labels were inspected on page 359. Exact SymPy checks confirm the cusp resultant and every degree-at-most-three monomial in the grid identity. Cross-volume citations match 5,114 statements. These are calculation checks, not proof certificates. Final EPUB and separate whole-book review remain outstanding.
