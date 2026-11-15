# Appendix A writer check — transformations

Current final source review: see [the mathematical review](final-mathematical-review.md) and [editorial review](final-editorial-review.md). This unit record preserves its earlier checkpoints; final-validation.md supersedes historical pending statuses.

## Coverage and preservation

The complete body, every original formal statement/proof, sixteen original exercises/hints/solutions, closing bridge and reading guidance are rewritten. Klein's epigraph is literal, as are all four original figure blocks/captions and the accurate bibliographic fields. Original formal environments and labels retain their order. Two diagrams follow the old Euler figure, and four fully solved exercises follow the old sixteen, with unique labels, difficulty and hints. This is a writer check, not the separate final review.

## Corrections and prerequisites

- The isometry proof derives linearity from preserved inner products without assuming surjectivity. It includes dimension zero. The three-reflection proof handles omitted reflections and avoids a degeneracy in an informal circle-intersection uniqueness argument.
- Isometry classes distinguish genuine translations/glides from the identity/reflections. Similarity parameters and fixed points are explicit. Affine triangle statements specify nondegenerate triangles, and the projective row is explicitly a preview on the projective plane rather than an unqualified inclusion of globally defined maps of R2.
- Leonardo's theorem handles the trivial rotation subgroup: C1 or the single-reflection D1. It does not identify D1 with the full symmetry group of a one-point polygon. The finite rotation/coset argument supplies all cases.
- Frieze conjugation fixes its convention, sign image and kernel. Word reduction verifies the seven constructed groups and their exact translation subgroup, rather than simply asking the reader to check closure. Half-period glides and their distinction from the horizontal mirror remain proved.
- Periodic-pattern discussion requires a discrete full-rank translation lattice; a constant pattern has all real translations and is a counterexample to the old blanket wording.
- Crystallographic restriction retains rotations about ANY centre: the linear part preserves the lattice because differences remove the translation. Integer trace then proves the same original order restriction. The finite point-group argument and shortest-vector square/hexagonal basis step are supplied locally, removing dependence on the later hexagonal exercise. Primitive mirror-axis generators and the half-lattice quotient give the rectangular/centred cases; square/hexagonal exceptions are not counted twice.
- CORRECTION: the Fagnano proof no longer claims that for an arbitrary D the reflected segment crosses both SIDES in the required order. The lower bound is valid for every D; equality is proved separately at the orthic feet by their exact side lengths and a local trigonometric identity. Uniqueness follows from altitude minimality and the sharp broken-line inequality. Corner collisions are excluded from the ordinary billiard model.
- Original two-rotation solution handles coincident centres, arbitrary angles and a zero translation by an explicit complex centre formula. It avoids unqualified base-angle triangle descriptions. Regular polygon exercise has n>=3; conjugacy proves both directions and handles identity parameters.
- CORRECTION: circle chords PERPENDICULAR to u have midpoints on the diameter PARALLEL to u, contrary to the old solution. The affine argument preserves midpoint/parallel relations, not perpendicularity.
- Letter-frieze exercise now states ideal geometric glyph assumptions; exact printed font outlines need not have the asserted symmetries. It proves each translation period/sign set under those assumptions.
- The fivefold obstruction uses a strictly shorter nonzero sum without a numerical approximation. Eisenstein generators distinguish the third root omega from the sixth root 1+omega. The cube solution gives all 24 flags/axis rotations and a local faithful action proof of S4.
- CORRECTION: square-billiard periodicity requires no corner hits. The least position-and-direction return is proved using fold parity and Bezout, including horizontal and vertical cases.
- CORRECTION: the identity translation is NOT the square of a genuine glide. Every nonzero translation has one glide root for each parallel axis; reflections, rather than genuine glides, square to the identity.
- The SO3 pole count proves its orbit lists and orders without silently treating that count as a full uniqueness classification. Ceva includes finite concurrence and parallelism in both directions, with every signed denominator checked locally; it does not depend on the following exercise. The Euler line includes right/equilateral cases.
- CORRECTION: Routh's actual edge vectors from P=(4/7,2/7) are (-3/7,2/7) and (-2/7,-1/7). The old vectors were wrong even though the stated determinant/area ratio was right. Their determinant is 1/7, hence area 1/14 in the normalized area-1/2 triangle.

## Additions

The figures show orthic unfolding at equality and the fifth-order shortest-vector contradiction. New exercises prove finite affine groups admit an invariant positive length form with an explicit triangular coordinate change; compute a glide wallpaper group's normal forms, axes and fundamental rectangle; characterize every maximum-area ellipse parallelogram; and construct an order-five orthogonal lattice symmetry in four dimensions. The last exercise locally constructs its two Fourier rotation planes and explains the dimension restriction, without later Appendix E/H as premises.

## Actual checks

The seventeen-unit PDF-only build exits 0 at 483 print pages, with no overflow or unresolved references and passing font, bleed, print and cover checks. All 544 old printed labels/captions, 213 numbered part/chapter/sections, 57 old figure files and two cover-art sources pass preservation. Both new diagrams were inspected on PDF page 281. The existing appendix numerical illustrations exit 0, and the cross-volume checker matches 5,098 numbered statements. Exact SymPy calculations separately confirm the new 4D matrix has fifth power identity, is nonidentity, preserves Gram matrix I+J and has trace -1; they also confirm the two corrected Routh vectors and determinant 1/7. These are calculation checks, not proof certificates. git diff --check passes. Final full EPUB and separate review remain outstanding.
