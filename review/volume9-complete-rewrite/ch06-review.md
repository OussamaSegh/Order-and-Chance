# Chapter 6 writer check — homology

## Complete prose coverage and preservation

The full chapter, all definitions, original numbered statements and proofs, examples, six original exercises, hints, idea/writeup solutions, ending and reading guidance are rewritten. Original bibliography records and both original figure blocks are preserved. Source comparison keeps the formal environment sequence and every original label in order. Two new figures and four new fully solved exercises are appended with fresh labels. These writer checks are not the separate final review or an independent certificate.

## Mathematical corrections and prerequisite repairs

- Unaugmented boundaries vanish in degree zero. Augmentation is a separate complex with degree -1 equal to the coefficient ring. The empty space has reduced H_-1=R, nonempty spaces have zero there, and all lower groups vanish. Empty complexes, zero-spheres, direct SUM H0 over arbitrary path components and point boundary alternation are explicit.
- Smith homology explains why torsion-free target chains force the Smith basis elements to be cycles. Integral ranks are distinguished from field ranks, and Euler sums are finite. The prism proof checks the diagonal and proper-face signs, including its degree-zero path.
- Small chains choose a common GEOMETRIC depth for the finite simplex domains before cancellation. This replaces the unsupported monotonicity claim for minimal depths chosen from already-cancelled chains. The cone, subdivision, diameter and support-preserving homotopy constructions remain proved locally; surjectivity and injectivity follow directly from their identities.
- Mayer--Vietoris keeps the diagonal/difference sign convention: z=x+y lifts to (x,-y), yielding delta[z]=[boundary x]. Reduced augmentation and excision hypotheses are checked.
- The sphere recurrence starts with S0; its cap construction is only for n>=1. Degree is defined on reduced top homology also for S0, so reflection induction has an actual base definition. No-retraction/fixed-point and local dimension arguments treat zero-dimensional endpoints explicitly.
- The simplicial/singular induction starts with the empty complex and separates a maximal zero-simplex before radial projection. The relative comparison uses inclusion-induced excision maps, with the removed closed sets inside the open punctured subspaces.
- CORRECTION OF A MISSING HYPOTHESIS: Euler's boundary formula is stated for a BOUNDED FULL-DIMENSIONAL convex polyhedron in R3. An arbitrary lower-dimensional or unbounded convex polyhedron need not have sphere boundary, so the old unqualified assertion exceeded its proof and is false under that general terminology. Original numbers stay fixed.
- Bouquet homology is justified by the earlier star open covers. Surface homology includes genus zero and vanishing higher groups. Closed/connected/orientable hypotheses are explicit when quoting classification, and triangulation/classification remain quoted rather than silently proved.
- Jordan--Brouwer proves complement nonemptiness and its increasing-open-set compact-chain step; path components, not merely connected components, are counted. Invariance of domain handles n=0 and the empty domain separately.
- The projective-space bound separates RP0. The transfer computation identifies exactly which maps are isomorphisms: the top quotient map q_* is ZERO, contrary to the old broad phrase 'all these maps isomorphisms'. The connecting maps and top transfer are isomorphisms. RP1 is computed as a circle. Odd-map naturality and the Borsuk--Ulam equivalence are complete.
- Ham sandwich continuity uses an integrable indicator bound, null hyperplanes and the bounded-set behaviour at the two parameter poles. The all-null case allows any genuine affine hyperplane.
- Original solutions repair distances to empty closed sets with constant positive coordinates; discrete pancakes include empty/singleton unions, duplicate points between families, a bounded subsequence of line equations and whole-disc limiting counts. The old misleading individual-disc half-area hint is replaced.
- Covering Euler counts justify the full common-face intersection of lifts and the Hausdorff total space before using compact bijectivity. Zero-sheet empty covers are included; connected applications use positive degree. Continuous hairy-ball reasoning treats S0 separately.

## New material

Two figures distinguish a boundary cycle from a nonbounding cycle and show local valence detection. Four exercises compute degree-d disc attachments over integers and fields, local homology of boundaries/branch points, odd integer degree via transfer, and a chain matrix with Smith factors 2 and 6. Each has a difficulty, hint and complete idea/writeup solution using material already taught. Exact SymPy reduction independently recomputes the new matrix's Smith factors and field ranks; this is a calculation check, not proof certification.

## Actual validation

The fifteen-unit PDF-only build exits 0 at 471 print pages. Layout checks report no overflow or unresolved references; fonts, bleed, exported interior and cover checks pass. Preservation passes all 544 original printed labels/captions, 213 part/chapter/section numbers, 57 old figure sources and two cover-art sources. Both new diagrams were inspected on PDF pages 149/150; the enlarged Chapter 5 loop was inspected on page 124 and is clear. The original homology numerical script exits 0. All 20 citation tests pass, cross-volume citations match 5,090 numbered statements, and the Volume 3 register exits 0 with 1,177 accepted and 19 pending entries. git diff --check passes. An initial unittest module invocation failed its import path; the correct discover command above actually ran all 20 tests. Full EPUB and separate final review remain outstanding.

Current main cfc7b20a (PR #244 Volume 15 rewrite) was integrated by ordinary merge 2de21df0 before this build. Its changes are preserved; the corrected SU2 citation remains Example 8.5 in the combined source.
