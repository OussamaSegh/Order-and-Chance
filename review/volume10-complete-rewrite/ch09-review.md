# Chapter 9 separate mathematical and editorial source review

Reviewer: `rewrite_ch05_ch06`, separate from the Chapter 9 writer. This reviewer wrote Chapters 5–6, not this chapter. Starting main is `59014a9aad3454ad60786c6549c81fcac88df9df`. This is a complete source reading, not a claim of human review, a local build, rendered inspection, or CI/publication success.

Final reviewed chapter SHA-256: `d465a7dcc2c45445e14014f394a4731f5cd31c85c7ab08c1d5c57ef85d430913`. The exact hashes of both new figure files are in `ch09-statement-review.json`.

## Coverage and statement comparison

Read the full final chapter, including the opening, historical quotations, short formula introductions, every formal statement and proof, every example, both new figures/captions/prose references, all ten exercises, all ten hints, every idea/writeup solution, ending and bibliography. Compared all sixteen original formal statements and six original exercises against their complete mathematical content in `starting-statement-content.json`. A concrete judgement for every original block and every added exercise is in `ch09-statement-review.json`.

The complete original kind/label sequence is preserved. All original labels remain. The whole original Wedderburn figure block is an exact substring, and `figures/ch08-wedderburn.tex` matches its immutable baseline SHA-256. There are exactly three numbered figure environments and ten exercises, hints and solutions: two useful figures and four complete exercises beyond the original counts. No original numbered theorem conclusion or valid hypothesis was found lost. Printed-number verification remains the parent's build responsibility.

## Mathematical review

- The arbitrary-division-ring Wedderburn proof retains the full finite-simple-regular-sum hypothesis. Endomorphism order, opposite division rings and transposition are correct; the empty product handles the zero ring. The finite-dimensional complex specialization follows from the locally supplied Schur/eigenvalue argument.
- The actual action-map isomorphism for C[G], class-sum centre and exact idempotent formula follow from established Maschke, orthogonality and the regular degree sum. Every scalar and denominator was checked.
- The induced function convention f(hx)=hf(x), right translation and left action agree. Evaluation at1 and its explicit inverse prove the stated adjunction with the correct orientation. The fixed-coset character formula and all Mackey conjugation/intersection conventions agree. The extension by zero on a double coset is well defined.
- Mackey's irreducibility criterion includes W=0 correctly. The norm decomposition is nonnegative and accounts for every nonidentity double coset. Dihedral even/odd cases, including n=2, and trivial subgroup cases are handled.
- The algebraic-integrality proof uses a finite class-scalar ring containing1. Burnside's coprime lemma treats both equality and strict inequality in the unit-circle average; the Galois product is an integer and its vanishing argument is valid. The prime-power-class proof earns faithfulness from simplicity. Burnside induction handles equal primes, zero exponents and the trivial group before choosing a Sylow subgroup.
- Frobenius kernel proof covers H=1 separately. Its induced-character norm count, signed integer coefficients and positive degree prove a genuine irreducible. The condition χ(g)=degree, stronger than equality in absolute value, earns the identity matrix. The intersection of kernels proves subgroup closure before it is used.
- Every original and new exercise is checked with its hint and full solution. Particular checks: quaternion central idempotents and complex matrices; Heisenberg distinct central characters and degree count; all finite-field affine cases including q=2; the tensor-power proof of degree divisibility by the central index; all A4 classes and character scalars; F7 character values6,−1,0 and norm1.

Actual earlier sources inspected: current Volume3 `ch11-characters.tex`, including Maschke, Schur, orthogonality, multiplicity/degree sum, class count, columns and S3/S4 examples; its actual dihedral convention in `ch01-groups.tex`; current Galois statements10.6 and10.9. The algebraic-integral determinant criterion and ring closure are in current Chapter5 and precede this chapter. No theorem of Volumes11–15 or a later exercise supplies a premise. Real division-algebra classification and Thompson's nilpotency theorem are explicitly quoted, not used.

## Findings and recheck

1. Found the missing backslash in the definition of θψ: `operatorname{Ind}` would render as individual math letters. Parent repaired it to `\operatorname{Ind}` in `ee5c8ac6`; exact source rechecked.
2. The new affine figure used0 both for no fixed point and for the actual fixed point0. Parent replaced the four no-fixed-point entries by ∅ and removed the ambiguous legend wording in `ee5c8ac6`. Exact source rechecked; every remaining fixed-point entry is b/(1−a) modulo5, with inverse rows4,2,3 for a=2,3,4.

The writer's correction to the singleton double-transitivity exercise is justified: without |X|≥2 the distinct-pair condition is vacuous while there is no additional irreducible summand. Its unrestricted double-coset identity is preserved. No remaining source-level blocker was found. Layout, rendered figure legibility, final printed labels, EPUB and production remain separately checked by the parent.
