# Earning the planar five-point maximum

This is a solo internal AI review, not independent human refereeing or formal
verification. Parent is88b563636b4cf98b1ec508ffe3919661e384531d. The entire current
combinatorial appendix, all18 existing named arguments, all ten complete triples,
both whole figure sources and all seven bibliography groups were reread. Current
reading is informed by prior answers; APPC-PROMPT-FIRST retains the original
chronology. The separate global history/voice/dependency register remains open.

The actual original7f87 caption asserted that a planar two-distance set has at
most five points, attributing it to Kelly1947. Its proofs supplied9 from the
first span count and6 from the affine-function refinement. V3-016 removed the
unsupported sharp assertion while preserving those proved bounds. This batch
earns and restores the intended5 with a new full local proposition, leaving
both general bounds intact. It does not claim the old attribution was false:
Kelly's related isosceles-set classification could imply a two-distance result,
but the original paper was inaccessible and its exact role was not verified.
The incidental attribution was removed instead of used as a premise.

The proof first earns the six-vertex coloring fact by a direct pigeonhole
argument: three same-color neighbors either contain a matching edge or form
an opposite-color triangle. Thus any six two-distance points contain an
equilateral triangle. We then prove that such a triangle admits at most one
extra point. Normalize its vertices to(-1/2,0),(1/2,0),(0,h),h=sqrt3/2. Every
external point has at least two equal distances to them. The complete cases
force the other squared distance to be1/3,3 or2±sqrt3. The first has only the
circumcentre; the second has three candidates with mutual square4; the last
has three candidates with mutual square2r², neither1 nor r². One fixed r cannot
mix the distinct cases. This rules out six, and the pentagon attains five.
All zero/single-distance, positivity, occupied-vertex and infinite-set issues
are explicit. No classification or future Ramsey theorem is imported.

The adversarial second reconstruction uses a different calculation. If
x=PA²,y=PB²,z=PC², each1 or t=r², form the Gram matrix of B-A,C-A,P-A.
Its determinant vanishes in the plane. Across the eight assignments the
polynomials are1/2,t(3-t)/4,(-t²+4t-1)/4,(3t-1)/4 according to the number of t
entries. These force exactly the source's cases, excluding t0. Exact arithmetic
in Q(sqrt3) rechecks every candidate, all rotations and all pairwise separations.
A separate enumeration of all32768 K6 colorings supports the written finite
lemma. Finite computations and the local-proof source guard support the general
proof; they do not replace it or constitute formal verification.

An initial sentence about adjoining an allowed distance was caught in the
adversarial pass: adjoining a value can relax a condition. The final argument
states only the valid fact that every original pair still lies in{1,r}. The
source also spells out the reflection coordinates and the factor3 in the
rotated candidates' squared separation. A later gap sentence now explicitly
compares the general affine upper bound with the simplex lower bound, so the
new sharper planar result does not make that context ambiguous.

V3-034-planar-maximum.json and proofs.json contain the fresh full domain/claim/
tools/A/B/boundaries/correction/source evidence. A new unit check fails its
local-proof guard on the actual original7f87 caption source and passes after
addition. This is an absence-of-proof regression, not a counterexample to the
true five-point assertion. The historical rewrite ledger now has158 entries;
its independent_verified remains0. The strict source count is updated for this
real addition and also explicitly requires the new proposition label.

The quadric finding idea now says degree at most2, covering the zero form. Its
complete supplied solution already handled zero denominators and characteristic2
correctly; no false defect is assigned to those steps. The whole changed triple
received fresh A/B, including an independent square-set pigeonhole proof of the
two-squares consequence. Eighteen unchanged named/proof pairs and nine unchanged
triples were individually matched after the reread. Inserting the new proof
renumbered thirteen anonymous proof IDs; V3-034-retained-identities records old
and new IDs and the actual identical bytes, paired by stable result labels.
No ordinal/count or historical editorial status approved those arguments.

Other source clarifications define a tensor as the finite three-variable
function being used, explain zero-polynomial degree upper bounds, state the
exact general n+1 gap, qualify the additive-subgroup obstruction and remove
stock praise. SET history is bounded to its publisher's animal-genetics/file-card
account. An unsupported Babai–Frankl2020-edition detail is replaced by the
verified1992 preliminary version2; the tri-colored paper's missing word rate is
restored. Artin's actual original quote page has not been inspected, but its words,
1957 attribution and book cover were checked in Axler's actual lecture slide3;
Wiley metadata distinguishes1957 copyright,1988 reprint and2011 online date.
The unread ChapterI pointer is removed. Remaining C bibliography/history checks
are open and are not certified by these corrections.

Final current-source515 tests passed, zero skips,57.240s, after all source and
checker changes: /tmp/volume3-v034-tests.log. Required source, exact inventory,
register/global-ledger freshness, all C probes and whitespace checks pass.
No assertion weakened. Source was frozen during that run; subsequent reports
are descriptive. No current output or whole-page approval is inferred.
