# Chapter 10 writer record

The entire chapter has been rewritten: opening/history, every definition and
numbered statement, all arguments and examples, six original exercises with
rewritten hints and complete idea/writeup solutions, ending and reading guidance.
Starting comparison SHA: `59014a9aad3454ad60786c6549c81fcac88df9df`.
This is a writer audit. Parent owns independent review and all builds; no build
has been run by this agent.

Preservation: all original labels, statement order, equation order and numbered
section order retained. The complete hook-figure block (caption and included
source) is unchanged byte-for-byte. Turnbull quotation and bibliography retained.
The three numbered equations remain `eq:frecur`, `eq:hooksum`, `eq:hooktarget` in
that order. No new numbered formal statements were inserted.

Added exactly two mathematical illustrations after the existing hook figure:
- `v10-new-ch10-insertion`: insertion/recording tableaux of 31452, with last
  corner and reverse bump recovering 2; explains values versus time labels.
- `v10-new-ch10-hookprob`: conditional and averaged hook-walk probabilities for
  shape (3,1), including the three possible first moves from its top-left cell.

Added Exercises 10.7–10.10, all starred with hints and full idea/writeup solutions:
standard-representation character/Gram matrix/action; exact four-cell hook walk;
Plancherel/Schensted distribution at n=4; coincident transposition eigenvalues
at n=6 with full degree/content table. No later-unit tool is used.

Mathematical corrections and explicit prerequisite repairs (fixing commit to be
assigned by parent):

1. The original modular aside called the identification of nonzero quotients
   S^lambda/(S^lambda intersect perpendicular) a hard open problem. It is known:
   the nonzero modules correspond to p-regular partitions. The aside now quotes
   that classical classification, defines p-regular, and distinguishes the
   harder decomposition-multiplicity questions. Nothing from modular theory is
   used by the complex proofs. Checked against James's standard theory (already
   cited) and the London Mathematical Society memorial to Gordon James,
   https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.12754 .
2. The original random-transposition paragraph assigned multiplicity
   (f^lambda)^2 to an eigenvalue without allowing collisions between shapes.
   Blocks contribute that dimension, but coincident scalars require summing.
   Explicit counterexample: lambda=(3,3) and (4,1,1) in S6 both have content sum
   3 and ratio 1/5, with dimensions 5 and 10. Their total multiplicity is 125,
   not 25 or 100. This is explained in text and the new challenge solution.
3. The original beauty box said this volume's cover showed a Plancherel diagram.
   Its actual cover shows the snake lemma. The false cover claim is removed;
   the mathematical Plancherel discussion and quoted limits remain.
4. The global n>=1 convention made the transposition formula's n=1 boundary
   opaque; n>=2 is now explicit at the theorem and ratio corollary, while the
   equality f^(lambda')=f^lambda remains valid at n=1. References to shape
   (n-1,1), including its exercise, explicitly require n>=2.
5. Corner recursion, hook induction and the later zero-degree moment need the
   empty partition. The convention f^empty=F(empty)=1 is supplied, retaining
   the original equation and its f^(1)=1 initial value.
6. Standard-representation exercise originally relied on a multiplicity fact
   only proved in a later exercise. Its solution now proves the constant-line
   plus sum-zero-hyperplane decomposition directly. The dominance content is
   retained, and no later exercise is a proof premise.
7. Reverse insertion was originally asserted to work on every pair by a 'mirror
   argument'. Both directions are now checked: rightmost-smaller choice exists,
   preserves rows/columns and has a weakly rightward reverse path. This supplies
   the surjectivity step of Robinson–Schensted locally.
8. Schensted's minimal-endpoint proof now handles length L=1 without using an
   undefined r_0. Its increasing-subsequence theorem is unchanged. The quoted
   decreasing-subsequence theorem, Young's rule, sign-twist, limit-shape and
   Tracy–Widom results are all explicitly distinguished from proved results.

Hook-walk review: probabilities p(Abar,Bbar) are now explicitly conditional on
the starting cell. Uniform 1/n is inserted once, at the final sum. Missing
first-step terms on corner rows/columns are dealt with via the zero numerator
h_(alpha,beta)-1. The proof checks the one-cell diagram and positive denominators.

Earlier material inspected: the actual Volume 3 character chapter's Maschke,
Schur, row/column orthogonality, class-count theorem, regular degree-sum identity,
and S3/S4 examples; Chapter 9 induction and Wedderburn. Specht completeness is
proved before the RSK dimension count; independence only uses the tabloid order.
No Garnir straightening or later compact-group formula is assumed.

Historical wording checked against MacTutor's Alfred Young biography,
https://mathshistory.st-andrews.ac.uk/Biographies/Young_Alfred/ . The literal
Turnbull quotation and existing accurate bibliographic records are preserved.
The unnecessary numerical 'eleven years after death' assertion is not repeated.

Source-only checks: all original labels and exact original figure block retained;
10 exercise environments (6+4) and 3 figure environments (1+2). Parent must
verify built numbering, full layout/artifacts, numerical illustrations, and the
separate mathematical/editorial review. No numerical experiment is a proof.

## Integrated fixing commits

c42d33c6 (initial rewrite), ee5c8ac6 (Russian-coordinate scale). These commits fix the original problems and prerequisite gaps
listed above; separate review records distinguish any additional draft-only fixes.
