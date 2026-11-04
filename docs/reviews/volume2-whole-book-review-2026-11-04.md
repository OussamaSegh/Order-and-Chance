# Volume 2 whole-source, unnamed-argument and figure review

This record supplements the 72-result and144-exercise registers. It does not
inherit their status. Source spans and SHA256 hashes are in
[the complete inventory](volume2-complete-source-inventory-2026-11-04.json);
regenerate that inventory after source changes. Manual identifiers below stay
stable when source lines or automatically indexed ordinals move.

No chapter has final approval. Mathematical source checks, numerical data,
final-size visual inspection, historical attribution and independent editorial
review are separate obligations. All entries here are internal checks.

| Printed chapter | Whole-source/unnamed arguments | Example/figure data | History/bibliography | Latest final-size formats |
| --- | --- | --- | --- | --- |
| 1 | IN_PROGRESS: DEP-061 read/rewrite; individual mathematical entries below | VERIFIED_TWICE internally for four retained examples and five figure datasets | IN_PROGRESS: targeted facts sourced; complete bibliography pending | UNREVIEWED after DEP-061 edits |
| 2–11 | UNREVIEWED in this whole-source register; named/keyed evidence is separate | UNREVIEWED comprehensively | UNREVIEWED comprehensively | UNREVIEWED comprehensively |
| Preface/field guide/jacket/cover note | IN_PROGRESS: inventoried and read, substantive follow-up remains | UNREVIEWED comprehensively | UNREVIEWED comprehensively | UNREVIEWED comprehensively |

## C01 — Divisibility, DEP-061

Read the complete chapter, including all15 prompt/hint/idea/writeup groups and
bibliography. The six named results and15 keyed exercise proofs keep their
separate earlier two-pass records. New work below addresses the surrounding
claims and their first use. General claims have symbolic proofs, not merely
finite samples.

| ID and source location | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C01-U01: opening252/198, Euclidean-algorithm section and proof workshop | d divides a,b iff d divides b,a−qb, by subtraction and addition. A nonzero decreasing integer remainder chain terminates; backwards substitution preserves integer combinations. | The generated subgroups are equal in both directions because a=qb+r; the final pair(r,0) has exactly r's divisors. Direct252−198=54,198−3·54=36,54−36=18,36−2·18=0 and4·252−5·198=18 verify the opening certificate. | VERIFIED_TWICE |
| C01-U02: subgroup paragraph and6Z/odd-integer examples | Nonempty subtraction closure gives0,x's negatives and x+y; inherited integer associativity supplies the group axioms. | Conversely a subgroup is closed under subtraction by sum with inverse.6a−6b stays in6Z;3−1=2 breaks closure for odds. The4Z+6Z think box has exactly even integers between−10 and10. | VERIFIED_TWICE |
| C01-U03: integer-combination paragraph after gcd definition | The combination set contains0 and differences are a(x−x′)+b(y−y′); scalar products remain combinations. | A composition of two combinations is again a combination coefficientwise. Inclusion of a,b and closure under sums/inverses makes this exactly the additive subgroup they generate; no general ideal theorem is used. | VERIFIED_TWICE |
| C01-U04: gcd universal property and uniqueness | The positive subgroup generator divides a,b; every common divisor divides its representing combination. Two positive elements with the property divide each other and hence agree. | Ordinary largest-positive-common-divisor also equals the generator: each common divisor divides it, and the generator is itself a common divisor.4Z+6Z=2Z follows independently from parity and2=6−4. Zero conventions remain separate from nonzero valuations. | VERIFIED_TWICE |
| C01-U05a: integer valuation/product rule | Concatenating prime lists adds each prime exponent, with signs removed by absolute values. | Repeated extraction of a fixed prime from a,b leaves p-free factors; Gauss ensures their product remains p-free. This gives exactly v_p(ab)=v_p(a)+v_p(b). | VERIFIED_TWICE |
| C01-U05b: gcd/lcm valuation displays | Integer divisibility is coordinatewise exponent comparison, so common-divisor maxima use minima and common-multiple minima use maxima. | Construct both products directly and verify the respective universal properties. Adding min+max equals the sum of exponents, so gcd·lcm=abs(ab), including negative nonzero a,b. Finite prime supports avoid an infinite-product assumption. | VERIFIED_TWICE |
| C01-U06a: new rational valuation definition | ad=bc gives v_p(a)+v_p(d)=v_p(b)+v_p(c), proving representation independence of the difference. | Reducing by a common factor subtracts the same exponent twice; comparison with the unique reduced fraction gives the same valuation for every presentation. Checked signs and12/25 values2 and−2. | VERIFIED_TWICE |
| C01-U06b: rational integrality criterion | In a reduced nonzero fraction any prime in the denominator has negative valuation. All nonnegative valuations therefore force denominator1. | Conversely integer inputs have nonnegative exponents by FTA. Independent cancellation to lowest terms and exhaustive small rational probes corroborate both implications. This now precedes ex:supercat's use. | VERIFIED_TWICE |
| C01-U07: divisor order and lattice | Positive divisibility is reflexive/transitive; mutual divisibility forces equality. gcd/lcm give lower/upper bounds that remain divisors of n. | For a,b dividing n the valuation minima/maxima are between0 and v_p(n), and satisfy both meet/join universal properties. The complete divisor12 cover-edge set independently matches the drawing. | VERIFIED_TWICE |
| C01-U08: reduced cancellation warning | Divide a,b by g>0; gcd(a/g,b/g)=1 and Gauss gives a|bc iff a/g|c. | For each prime compare v_p(a)≤v_p(b)+v_p(c); removing the common minimum leaves exactly divisibility by a/g. For b0, g=abs(a) and a/g=±1, so the endpoint remains true.6|2·3 but6 does not divide3 is the explicit counterexample. | VERIFIED_TWICE |
| C01-U09: extended Euclid coefficient recurrence | Base coefficient vectors(1,0),(0,1), followed by the same q subtraction as the remainders, imply r_k=au_k+bv_k by induction. | Each transformation has determinant−1 and integer inverse, preserving the generated subgroup and enabling exact backwards substitution.240(−9)+46·47=2 and899·5−372·12=31 independently check the examples. | VERIFIED_TWICE |
| C01-U10: all solutions of ax+by=c | Subtract a particular solution, divide by d and apply Gauss to obtain x=x0+(b/d)t,y=y0−(a/d)t. Scaling Bézout proves existence iff d divides c. | Modulo b/d the reduced equation forces x's single residue; plugging it back determines y. Every displayed t works and every solution lies on that integer step. Positive a,b avoid zero coordinate denominators. | VERIFIED_TWICE |
| C01-U11: Fibonacci bounds and division count | The named Lamé induction was rechecked with explicit F0/F1 recurrence. Consecutive Fibonacci inputs achieve the bounds. Actual Volume1's Binet proof supplies growth; ex:lame5 independently proves the needed lower bound by recurrence. | Starting from the terminal divisor1 and final quotient at least2, backwards addition minimizes each preceding remainder, producing precisely consecutive Fibonacci numbers. For b<100, F11=89,F12=144 give10 divisions and smallest such a144. O(log b) concerns sufficiently large b and counts divisions, not bit operations. | VERIFIED_TWICE |
| C01-U12: coprime-coordinate visibility | gcd>1 gives a nearer integer point by division. If gcd1, Bézout applied to any nearer integer point(ta,tb) forces t to be an integer, contradicting0<t<1. | Independently a reduced rational slope has unique primitive integer direction; every integer point on its ray is a positive integer multiple. The coordinate-axis cases have visible points(±1,0),(0,±1) and their further multiples are hidden. | VERIFIED_TWICE |

Two pedagogical changes accompany this review. Defined rational valuations and
their integrality criterion before the factorial-ratio exercise uses them;
recalled Fibonacci initial values and the meaning of the asymptotic bound.
The expectation proof in pb:valuation now controls its omitted geometric tail
explicitly: with K=floor(log_p N), that tail is less than p/[N(p−1)]. This
rechecks its earlier proof and does not add a new exercise to the total.

The repeated `examplex` about4Z+6Z was removed; the same complete argument
remains in the earlier subsection and think box. No mathematical result or
exercise was removed. The current book has98 example environments, down from
the DEP-060 baseline99. Replaced the unsupported “oldest non-trivial algorithm”
superlative by the concrete Elements attribution. Rewrote the beauty box's
incorrect “every result comes from subgroups” claim and removed its incidental,
unexplained NP-hardness teaser; the coin problem and bibliography remain.

### C01 examples and figures

| ID | Independent recomputation and separate check | State and boundary |
| --- | --- | --- |
| C01-E01: negative division | −17=5(−4)+3 with0≤3<5; floor(−17/5)=−4. The alternative remainder−2 violates the stated convention. | VERIFIED_TWICE internally |
| C01-E02:240/46 and full back-substitution | Remainders10,6,4,2,0 give gcd2; the independent certificate240(−9)+46·47=2 and common factor2 pin it down. Each displayed substitution is an equality. | VERIFIED_TWICE internally |
| C01-E03:899/372 | Remainders155,62,31,0 and certificate4495−4464=31. Dividing inputs by31 gives coprime29,12. | VERIFIED_TWICE internally |
| C01-E04:899x+372y=31 |(5+12t,−12−29t) substitutes to31 for every integer t; subtracting the particular solution and coprime cancellation proves exhaustion. | VERIFIED_TWICE internally |
| C01-F01: divisor lattice | Vertices1,2,3,4,6,12 exhaust divisors. Edges1→2,1→3,2→4,2→6,3→6,4→12,6→12 are exactly covers, checked independently by enumerating all intermediate divisors. | VERIFIED_TWICE data; final-size visual pending |
| C01-F02: Bézout line | The line endpoints(−4,2.6),(8,−4.6), filled integer points(−3,2),(2,−1),(7,−4) and hollow(1,−0.4) satisfy3x+5y=1. The dashed arrow now has exact displacement(5,−3); previously its endpoints only approximated that direction. | VERIFIED_TWICE data; changed arrow needs visual review |
| C01-F03: Euclid square tilings | The34×21 tile areas are21²+13²+8²+5²+3²+2²+1²+1²=714. For45×16 they are2·16²+13²+4·3²+3·1²=720. Exact source-coordinate checks verify the common0.17 scale, bounds, no overlaps and complete area. | VERIFIED_TWICE data; final-size visual pending |
| C01-F04: remainder staircase | Every arrow uses exact remainder arithmetic252/198→198/54→54/36→36/18→18/0; each division label and gcd18 agree with the independently reconstructed opening. | VERIFIED_TWICE data; final-size visual pending |
| C01-F05: visible disc | The complete plotted point set equals all nonzero integer(a,b) with a²+b²≤121; independent gcd classification gives224 filled of376 total, ratio59.574…%. Source data checked point by point. The primitive direction(11,4) has length√137>11, so no tree centre lies on it and a positive thin-trunk escape gap exists. | VERIFIED_TWICE data; final-size visual pending |

Five focused regressions read the actual figure sources and check these
coordinates/relations; the rational-definition guard and arrow test fail on
the pre-repair source. Existing independent orchard and exercise regressions
remain relevant. These checks do not inspect the rendered drawings.

### C01 prerequisites, history and remaining evidence

Actual Volume1 source read: ch01-sums `prop:induction` and its explicit
well-ordering axiom; Fibonacci definition in ex:fibgcd and the complete Binet
remark near line770; ch02-complex-roots subgroup test near line350 and
`prop:expform`; ch05-sequences-series reminder defining O/o/~ near line178;
orders.tex `orders:def:poset` and the divisibility example. Prior crosswalk
entries locate the counting/probability/geometry facts used in the optional
problems. Rational valuation is now proved locally, not attributed to an
unlocated earlier theorem. General ideals/rings, RSA and continued fractions
in the beauty boxes are explicitly future connections, not proof premises.

Historical checks on4 November2026:

- Euclid's actual gcd argument is BookVII Proposition2, available in
  [Joyce's Elements edition](https://mathcs.clarku.edu/~djoyce/elements/bookVII/propVII2.html).
  The manuscript now states the attribution without an absolute oldest claim.
- Lamé's1844 note is identified in the contemporary
  [1870 bibliography](https://www.numdam.org/item/BSMA_1870__1__224_1.pdf)
  and [bibliographic catalogue](https://books.google.com/books/about/Note_sur_la_limite_du_nombre_des_divisio.html?id=zTwS0AEACAAJ).
  The Gallica primary scan link was located but inaccessible through the web
  tool; no claim of reading its original proof or resolving priority is made.
- Pólya's1918 orchard article (volume27,pages135–142) is cited in the
  [LMS obituary bibliography](https://mathshistory.st-andrews.ac.uk/LMS/polya_lms_obit.pdf)
  and [IBM Research's independently solved orchard challenge](https://research.ibm.com/blog/ponder-this-november-2012).
  These support the date/attribution; the book's particular inequalities were
  proved locally in the exercise, not borrowed from the web summary.

Complete edition/section verification of every further-reading entry,
latest-source page/figure visual inspection, a distinct editorial reader and
the global dependency release pass remain open. Chapter1 is not signed off.
