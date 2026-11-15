# Separate review: Chapter 7, Homological Algebra

Reviewer: the agent assigned Chapters 3 and 4 for writing, reviewing material written by a different agent. This is a separate source mathematical/editorial review, not a human second reader or rendered production inspection.

Reviewed source SHA-256: `6a6ada18b592d551f143a5ccf08cd3eb00cc5a81c75570a3b33ed9dd0e008aae` for `volume10-abstraction/chapters/ch06-homological.tex`. Compared all thirteen original formal statements and all six original exercises with `starting-statement-content.json` at starting main `59014a9aad3454ad60786c6549c81fcac88df9df`. Also read every final paragraph, proof, example, hint, solution, quotation and bibliography, including all four added exercises and both added figure sources.

**Result:** no unresolved mathematical or editorial finding in these reviewed sources. Writer repairs are explicit, preserve the valid baseline content, and remove rather than conceal prerequisite gaps. Actual typeset numbers, overflow, image rendering and EPUB behaviour are parent production checks; this report does not claim them.

## Original statement comparison and proof judgement

| Original label | Mathematical comparison and review |
| --- | --- |
| `def:resolution` | Exact augmented sequence, all terms projective, and homology in degree zero retained. The augmentation versus underlying-complex distinction is explicit. Free construction supplies each next kernel, including zero module cases. |
| `thm:comparison` | Retains exactness of the target without assuming its terms projective. Inductive lifts use projectivity of the source only. Homotopy formula and initial degree, with augmentation, are correct; its recursive difference has zero outgoing differential. |
| `lem:horseshoe` | Direct-sum terms, compatible maps and exact augmentation retained. The initial lift exists through the onto quotient. Snake applied to augmentation kernels gives the short exact sequence needed to repeat the construction; degreewise splitting is correctly distinguished from splitting of complexes. |
| `def:torext` | Tor homology and Ext cohomology of a projective resolution retained. Explicit no-extra-sign Hom differential squares to zero and agrees with subsequent formulas. |
| `prop:torextbasic` | All original canonical-independence, functoriality, zero-degree identities and positive-degree vanishing assertions retained. Comparison compositions are homotopic; tensor and Hom preserve those identities. Variance in both arguments is stated correctly. Exactness on a long resolution is justified by its image short exact sequences. |
| `thm:les` | All four original sequences, directions and degree shifts retained. First-variable construction uses degreewise split horseshoe complexes; second-variable construction uses projective implies flat and exactness of Hom from a projective. No unproved general Tor symmetry is used. |
| `cor:torflat` | Quantifier over every module retained in both directions. For any injection, the Tor term of its quotient forces the tensor map injective, which is the already proved flatness criterion. |
| `ex:torextz` | Original kernel/cokernel formulas and positive-degree vanishing retained. The missing positive-integer convention is now explicit: multiplication by zero would not be a length-one resolution. Cyclic gcd calculations, `n=1`, and the example `4` on `Z/6` check. |
| `prop:pidvanish` | Retains finitely generated first argument, arbitrary second argument and all degrees at least two. Finite free presentation has finitely generated torsion-free kernel; the earlier PID theorem makes it free. Infinite-module extension is accurately quoted rather than used. |
| `thm:extclass` | Same equivalence classes fixing both ends and the split-zero class. Relation map, quotient by restrictions, pushout signs `(phi(k),-iota(k))`, and equivalence map `(n,p) -> (n-psi(p),p)` check. Both constructions undo each other. |
| `ex:extzp` | Same p classes and p−1 distinct nonzero classes sharing a cyclic middle group. Prime and map conventions explicit; computed `a^{-1}` follows from a lift of the quotient generator. The example previews a later exercise but no proof uses that exercise. |
| `thm:uct` | Both full sequences, arbitrary coefficient module, finite free PID complex, naturality in both inputs and nonnatural splittings retained. Cycles/boundaries finite free, degreewise splitting, connecting map `i_n tensor1`, kernel/cokernel identifications and both splitting maps checked. Degree-zero convention correct. |
| `ex:rp2uct` | Original integer homology, mod-two top homology and integral cohomology calculation retained. The text explicitly computes the finite boundary complex and does not apply the finite theorem directly to infinite singular chains. Torsion appears in the correct higher cohomology degree. |

## Exercises, hints and complete solutions

All six original exercise labels and numbers are source-stable; their hints are useful and their complete solutions follow the idea/writeup convention. All four additions occur after those six, with unique labels, star ratings, hints and full solutions.

| Label | Independent mathematical judgement |
| --- | --- |
| `ex:kleinuct` | Integer boundary `(0,2)` gives H1=Z plus Z/2, H2=0. Reducing modulo two and tensoring with Q give the stated groups. Dual matrix `(0,2)` gives H1=Z,H2=Z/2 in cohomology, with every UCT term accounted for. |
| `ex:torsym` | Finite direct-sum resolutions justify additivity in each variable. Free terms vanish, and the gcd symmetry of each cyclic pair proves finiteness/isomorphism without a forward appeal to general symmetry. Ext counterexample correct. |
| `ex:koszul` | The initial free resolution is proved exact, not merely asserted. After tensor with K its differentials vanish. Dual Koszul kernel computation gives Ext only in degree two; signs remain valid in characteristic two. All degrees including zero covered. |
| `ex:extzp2` | Relation p maps to p times the inverse-a lift, yielding a^{-1}. Extension equivalences force the middle multiplier to be 1 modulo p and hence a=b. No missing p=2 case. |
| `ex:baersum` | Diagonal anti-kernel subgroup lies in the pullback; inclusion into quotient is injective and every zero quotient class is its image. Pair of projective lifts gives addition of relation maps with the correct sign. |
| `ex:extqz` | Second-variable exact sequence with injective Q identifies the precise embedded copy of Q. Factorial-denominator compatible maps provide uncountably many homomorphisms. A nonzero Ext class does not only mean the specified extension fails to split: the argument that an abstract Q subgroup would supply a section proves the stronger stated nonisomorphism to Z plus Q. |
| `ex:v10new-ch07-dualnumbers` | Periodic multiplication by epsilon has equal kernel/image; all derived differentials become zero on k. Nonzero Tor in every degree excludes every finite projective resolution. Works over every field. |
| `ex:v10new-ch07-connecting` | Lift convention gives class [1] in (Z/r)/s(Z/r), so splitting iff gcd(r,s)=1. Explicit CRT section is well defined and handles r=1 or s=1. |
| `ex:v10new-ch07-coefficients` | Homological degrees 2/1 give A[m], A/mA; cohomological degrees 1/2 reverse them. The integer homology and Tor/Ext explanations agree, including m=1. |
| `ex:v10new-ch07-splitting` | Chain shear preserves d1=2x, acts identically on integer homology, and shears mod-two H1. Every section sends 1 to (1,a), which the shear moves to (1,a+1). This proves the genuine obstruction to a natural splitting. |

## Prerequisites and prose

Read the actual earlier zigzag lemma and proof in Volume 9 Chapter 6, printed Lemma 6.2; it constructs the exact connecting maps and proves naturality using additive maps only, so the stated extension to module complexes is justified. Read its projective-plane/Klein-bottle boundary-word calculations, which give the finite complexes used here. Volume 3's finite PID structure theorem and Chapter 3 of this volume supply the finite-submodule/free and projective-flat facts before use. Homotopies and comparison are explained before invariance of Tor/Ext. Higher Yoneda extensions, infinite-free PID freeness, Hilbert syzygy, general Tor symmetry, general de Rham and the Whitehead independence discussion are explicitly quoted, and none is an unmarked proof premise.

Every short formula introduction and prose paragraph was read. The text consistently explains why lifts or quotients are needed; source-style closing guidance points to the group action question, without a template theorem list. The phrase “lost kernel” in the opener is immediately clarified by the explicit newly created kernel calculation; no mathematical ambiguity remains in the argument.

## Preservation and figures

Source inventory actually run: thirteen original formal labels retained in their original environment order; every original label present and unique; 10 exercises, 10 hints, 10 solutions; three figures total, giving exactly two additions. The complete original `fig:surfaces` block is byte-for-byte present, and the SHA-256 of original `figures/ch06-surfaces.tex` matches the immutable baseline. Numbered-section source order remains unchanged.

Read both added sources. `v10-new-ch07-coefficients.tex` has the correct degree labels 2,1,0, multiplication-by-two/zero maps and Tor caption. `v10-new-ch07-cycles.tex` has d_n(z,b)=(i_{n-1}(b),0), the correctly oriented inclusion and a clear distinction between the chosen decomposition and canonical submodules. Both use the approved palette. No photographs occur in this chapter. Parent must inspect actual rendered plates and printed numbers.
