# V3-013b — earn the finite minimal-simple assertion

Internal AI reconstruction, not a new research claim, human review or formal
verification. Read the entire actual C5 Sylow/solvable proofs and C4 simple-group
paragraph again. The original C5 remarked that all orders<60 are solvable and
A5 the unique simple order60, without proving either; C4/C12 used minimality.
The inserted subsection earns both, using only actual earlier group tools.

Domain: finite groups,positive order. Claim1: every order<60 is solvable;
therefore a nonabelian simple group has order>=60. Claim2: every simple group
of order60 is A5. Existence/simplicity of A5 was already independently proved
in C4 and does not depend on this minimality proof.

A: Induct on order. Prime-power cases use prop:solv(c)'s center induction.
For27 non-prime-power orders the printed Sylow table forces one normal Sylow;
the p-group and smaller quotient are solvable, then prop:solv(b). The only
remaining orders are12,24,30,36,48,56. For12/24/36,n3=1 or4. Four gives
a transitive action in S4, whose explicit earlier V4<A4<S4 abelian-quotient
series earns solvability; image subgroup and smaller kernel are solvable.
For30, simultaneous n5=6/n3=10 would contribute44 nonidentity elements.
For48,n3=16 leaves exactly the16 elements of a unique Sylow2; other cases
normal3/action4. For56,n7=8 leaves exactly a unique Sylow2 of order8.
No Burnside/odd-order theorem is used.

B: Independently factor every integer2..59 and derive its Sylow-count
possibilities from divisors of the prime-free quotient. All33 non-prime-power
orders are exactly the27 printed entries plus the six exceptions, with no
overlap or omission. Recheck quotient/extension induction is always strict:
a transitive nontrivial action has image order>=4, so its kernel is smaller;
normal Sylow's quotient is smaller; groups of order1 start the induction.
The leftover sets are entire Sylow2 subgroups because those subgroups contain
no odd-prime-order element; two such subgroups cannot differ if each has the
same total size as the leftover set. This is uniqueness, not merely counting.

Order60 A: Simplicity forces n5=6. n3=4 would inject into S4,so n3=10.
n2=3 similarly impossible,leaving5 or15. Five gives faithful S5 image60,
index2 hence A5 by square/3-cycle generation. With15, cyclic Sylow4 groups
would contribute30 distinct generators while44 odd-order elements already
occupy the group. Thus all Sylow2s are V4.45 incidences among at most15
involutions force an involution in multiple Sylows. Its centralizer contains
their union and has order>4,divisible4,dividing60,so12/20/60. Centralizer60
would give central normalC2;20 would inject into S3 via cosets. Thus12,
whose five cosets give the same faithful S5/A5 identification.

Order60 B: Reconstruct every count from the raw Sylow conditions and check
which kernels are trivial by simplicity, not by an assumed classification
of order60 groups. Distinct C4 subgroups have disjoint generator pairs;
distinct prime-order subgroups intersect trivially. In the V4 case even two
containing the same involution have union of six elements, so centralizer>4.
The only multiples4 dividing60 above4 are12/20/60. Every coset action used
is nontrivial because the subgroup is proper; no normality of that subgroup
is assumed. An index2 subgroup of S5 contains squares, each3-cycle is an
inverse3-cycle squared, and3-cycles generate A5. Separately enumerate actual
A5: six Sylow5,ten Sylow3,five V4 Sylow2s; each of15 involutions lies in
one Sylow2 and has centralizer4. This finite model supports, not replaces,
the arbitrary-group proof.

Earlier tools/proof sites: C1/C2 Lagrange,order4 classification,index-two
normality/quotient; C3 coset actions/orbit–stabilizer/conjugation; C4 generated
3-cycles and A5 simplicity; C5 thm:sylow full existence/count/containment/
conjugacy, explicit S4 solvable series before prop:solv and its four full
proofs. Every site was read; none is inferred from a title/exercise prompt.

Defect/correction: retain both true intended statements and provide complete
finite proof. C4's claim becomes an explicit outlook until C5; C12's invocation
is now backward to that actual proof. One new tabular environment, no named
result/exercise removed or added. New numbered subsection has a stable label
tool:smallest-simple, avoiding a false reference to the preceding proposition.
Zero/trivial groups,abelian simple prime groups and exactly60 boundary handled.
Source hashes are recorded in the curricular disclosure and fresh inventory;
new keyed unnamed/dependency entries still require global register closure.
