# Appendix B: fresh boundary and convention review

This is a solo internal AI review, not human refereeing or formal verification.
Parent source is 978f4bd576caf8d4233f904c2794644c0eb6ed09. The entire current
appendix, all eleven named proofs, all twelve prompts, hints, finding ideas and
complete answers were reread in printed order. The original prompt-first
chronology remains in APPB-PROMPT-FIRST.md; this is an informed reread after
answer exposure, not another blind solve. Historical claims and the separate
66 global rows are still pending.

Two real boundary gaps were found despite the earlier core acceptance. The
standing binary length domain includes zero, but the Walsh recursion and answer
split off a first bit using H_(n-1) and F2^(n-1). At n=0 these expressions are
undefined. The main recursion and prompt now require n>=1, and H0=[1] returns its
sole input with zero arithmetic operations. The intended transform and exact
n*2^n count are retained for every n>=0. The last coding solution also formed an
average distance distribution without first excluding an empty code. It now
disposes of that trivial case before dividing by the code size. The attaining
16-word construction explicitly recovers its four affine coefficients from
f(0) and f(e_i), proving that the words are distinct.

The circulant proof now says that the Fourier vectors form a basis. The former
phrase “all the eigenvectors” was false for a scalar matrix in dimension at
least two, although the actual theorem was correct. The inverse exercise now
explicitly requires an invertible circulant. The Paley prompt explicitly says
prime, and its permutation convention is Pe_x=e_(cx), giving PAP^-1=J-I-A.
The old inverse conjugation also holds here because c^-1 is a nonsquare; it is
not reported as a mathematical error. The Ramsey recurrence now states a,b>=2,
so it never invokes an undefined R(0,b). No mathematical target was weakened.

V3-032-fresh-core.json and the main keyed registers contain six fresh complete
A/B records: the full circulant statement/proof and the complete circalg,
walsh, paleyself, paleyramsey and lpthree triples. The circulant second check
reconstructs every entry of UDU* by root-of-unity summation. The inverse has
interpolation and commutant derivations. Walsh has both butterfly orders and a
dense character-sum check. Paley has the coset bijection and complementary
character spectrum. Ramsey has affine normalization and exact four-set checks,
with a general induction proving finiteness. The coding bound has both the
actual weighted inequalities and the independent polynomial certificate
(t-4)(t-8)=2K0+2K1+K2/2; the affine construction earns equality. Full domains,
prerequisites, boundary probes, hint comparisons and star decisions are keyed.

Ten other full named/proof pairs and seven other complete triples were retained
only after individual statement and related-source SHA identity checks and the
complete reread. V3-032-retained-identities.json records those identities. The
new records also correct a prior reviewer-note typo: the common-neighbor
obstruction modulo17 uses differences7/14, not3/10. The reader-facing answer
already had the correct values. Review records can themselves contain defects;
no old status substitutes for checking the current argument.

The focused Walsh and empty-code guards each fail separately on the actual
978 source backup, with the expected reason, and pass on the corrected source.
The Walsh probe independently compares recursive and dense transforms for
n=0..6 and counts all operations exactly. These are supporting regressions,
not proofs of the general statements. An initial ad-hoc import omitted the
checker's directory from sys.path; correcting that invocation allowed the
actual before/after run. No assertion was weakened to obtain a pass.

No new immutable artifact or page approval is claimed for this source batch.
The latest complete artifact checkpoint remains 3bffe82f, before the Appendix A
clarifications and these changes. Final affected pages, all pagination, digital
behavior, remaining global concepts/history and exact final-head CI remain open.
