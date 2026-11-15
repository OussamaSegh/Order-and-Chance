# Chapter 1 writer record

Complete handwritten replacement of the chapter has been made, from the opening
through definitions, all numbered claims, proofs, examples, six original exercises,
six original hints and six original idea/writeup solutions, and the chapter close.
The bibliography and complete original figure block are preserved literally.
The authorial voice pass includes short formula introductions and qualifications,
not only long paragraphs. This is the writer's review, not independent certification.

## Additions

Two figures, after the original figure: divisors of 12 as products/coproducts,
and the precise naturality square used by Yoneda's proof. Four appended exercises:
ceiling/multiplication adjunction in ordered integers; natural operations on abelian
groups; the two adjoints to inverse image on power sets; and pullbacks of sets and
groups, including the same-parity subgroup of Z². Each has stars, a hint and a full
idea/writeup solution. No original section or numbered-statement count was changed.

## Explicit corrections and proof repairs

- **C01.** Original Example `ex:categories` said a matrix morphism is “not a map
  between anything”. Matrices act as linear maps on coordinate vector spaces;
  the new statement distinguishes the dimension object from that interpretation.
  No numbered conclusion or hypothesis was removed.
- **C02.** The original size note said “every argument ... takes place inside
  finitely many Hom-sets”, despite natural transformations having components over
  every object. The note now defines local smallness, distinguishes small and large
  categories, and explains Yoneda's set parametrisation of the families it treats.
- **C03.** Original Cayley example conflated Yoneda's classification of equivariant
  right translations with the faithfulness of left translation. Both conclusions
  are retained, with separate proofs; faithfulness follows by evaluation at 1.
- **C04.** The self-dual theorem's scalar clause is phrased as an obstruction from
  some scalar, rather than a claim that every scalar fails (the identity does not).
  The quantified theorem and field hypothesis are unchanged. Zero dimension and
  the finite-field plane exception are explained separately.
- The matrix-polynomial solution now supplies the missing polynomial-identity
  argument rather than assuming equality on all complex tuples implies formal
  equality without explanation. The n=0 case is checked explicitly.
- The slogan about a free module and a product/coproduct coincidence no longer
  relies on the undefined phrase “additive categories”; the exact two-factor
  module calculation supplies the claim needed here.

Fixing commit: to be filled by the integrating parent after committing these files.

## Prerequisites and verification

Read main.tex for Volume 10 and the complete assigned chapter. Inspected actual
Volume 8 Appendix A double-dual theorem (`linear:thm:bidual`) and Volume 9 Chapter 5
free-product proposition (`prop:freeproduct`) in their current printed contexts.
The new exercises use only elementary group/module facts and category theory proved
before the exercise list. No premise from a later chapter or volume was introduced.
Yoneda, uniqueness of adjoints and preservation of products were checked directly
in both directions. Empty sets, empty bases and zero vector spaces are covered.
The group and ring functor examples preserve their original content and order.

Executed source comparison (Python, exit 0): no missing original labels;
numbered section titles/order identical; figures 1→3; exercises 6→10.
No build was run by this writer; the parent owns the sole build process.
