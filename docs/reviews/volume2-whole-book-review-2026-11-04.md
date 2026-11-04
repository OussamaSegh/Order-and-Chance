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
| 2 | IN_PROGRESS: DEP-062 read/rewrite and two-pass unnamed math | VERIFIED_TWICE internally for six examples and three figure datasets | IN_PROGRESS: original Erdős/Furstenberg sources checked; portrait provenance/full bibliography pending | UNREVIEWED after DEP-062 edits |
| 3 | IN_PROGRESS: DEP-063 whole-source and unnamed-argument records | VERIFIED_TWICE internally for six examples and four figure datasets | IN_PROGRESS: targeted primary sources checked; complete bibliography pending | UNREVIEWED after DEP-063 edits |
| 4 | IN_PROGRESS: DEP-064 whole-source and unnamed-argument records | VERIFIED_TWICE internally for nine examples and three figure datasets | IN_PROGRESS: targeted sources checked; complete bibliography pending | UNREVIEWED after DEP-064 edits |
| 5 | IN_PROGRESS: DEP-065 full source and unnamed arguments | VERIFIED_TWICE internally for ten examples and three datasets | IN_PROGRESS: targeted primary records read; remaining bibliography pending | UNREVIEWED after DEP-065 edits |
| 6 | IN_PROGRESS: DEP-066 complete source and unnamed arguments | VERIFIED_TWICE internally for eight retained examples and four complete datasets | IN_PROGRESS: targeted sources checked; remaining bibliography/history pending | New complete liar plot rendered; whole latest-source chapter remains UNREVIEWED |
| 7 | IN_PROGRESS: DEP-067 complete source and unnamed arguments | VERIFIED_TWICE internally for six examples and three datasets | IN_PROGRESS: withdrawn research claim removed; targeted sources checked; full history pending | All three standalone plates inspected; whole current-source chapter remains UNREVIEWED |
| 8 | IN_PROGRESS: DEP-068 complete source and unnamed arguments | VERIFIED_TWICE internally for15 examples and three full datasets | IN_PROGRESS: targeted current/official sources checked; full bibliography pending | Three standalone plates rendered/inspected; current full-page placement pending |
| 9 | IN_PROGRESS: DEP-069 full source and unnamed arguments | VERIFIED_TWICE internally for12 examples and four complete datasets | IN_PROGRESS: targeted original/revised sources checked; full bibliography pending | Four standalone plates inspected; latest full-page review pending |
| 10 | IN_PROGRESS: DEP-070 complete source and unnamed arguments | VERIFIED_TWICE internally for eight examples and three full datasets | IN_PROGRESS: current moat/edition claims checked; original history pending | All three revised standalone plates inspected; full-page review pending |
| 11 | IN_PROGRESS: DEP-071 complete source and unnamed arguments | VERIFIED_TWICE internally for12 examples and four complete datasets | IN_PROGRESS: targeted editions/attribution checked; global history pending | All four revised standalone plates inspected; whole final-source pages pending |
| Preface/field guide/jacket/cover note | IN_PROGRESS: DEP-072 complete source pass; global graph/voice still pending | Final field-guide example and cover dataset checked twice internally;97/97 example blocks total | Three actual portraits matched to originals; targeted cover history read; global bibliography pending | New final artifacts/pages pending |

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

## C02 — Primes, DEP-062

Read the whole chapter, including all11 prompt/hint/idea/writeup groups and
bibliography. Five named results retain their separate two-pass records;
all numerical examples, three complete figure datasets and the following
surrounding arguments were independently reviewed.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C02-U01: sieve stopping rule and trial division | Composite m=uv with1<u≤v has u≤√m; a prime factor of u is at most√N when m≤N, so the sieve removes every composite by that stage. | A composite with every prime factor>√N would have a product of at least two such factors>N, contradiction. Conversely only multiples larger than a retained prime are removed, so primes survive. Applies to N≥2;1 is not included in the sieve. | VERIFIED_TWICE |
| C02-U02: testing versus complete factorisation and digit scale | A divisor certifies compositeness; absence of prime divisors through√N certifies primality by U01. Reapply to the quotient to factor completely. An s-digit integer can have square root comparable to10^(s/2), explaining the size of the trial range. | Direct trial division gives221=13·17 and223 prime after testing all six primes≤13. The size statement describes the range searched, without claiming the exact number or bit cost of divisions by primes. The source now names13 explicitly in the223 check. | VERIFIED_TWICE |
| C02-U03: harmonic/product and logarithmic-tail explanations | Finite positive geometric products contain all1/n with n≤x by FTA. For a prime p the logarithmic remainder is at most1/[p(p−1)]; comparison with the telescoping integer sum gives total≤1. | The independent positive expansion−log(1−t)−t=sum_{k≥2}t^k/k≤t²/(1−t) gives the same uniform remainder bound, while finite truncation contains any prescribed harmonic partial sum. No identity at a divergent infinite Euler product is assumed. | VERIFIED_TWICE |
| C02-U04: prime-count upper bound after Chebyshev | Each prime above√x contributes more than(log x)/2 toϑ(x), giving π(x)<√x+2log4·x/logx for x>1. Since logx≤√x eventually, a fixed multiple of x/logx follows. | Partition primes into those≤√x (at most√x integers) and those above it; multiply the latter primes to bound their count by the prime-product estimate. Taking logs independently reproduces the bound. Differentiating√x−logx shows its minimum at4 is positive, so the eventual comparison is valid. | VERIFIED_TWICE |
| C02-U05: real lower-bound extension | For n=floor(x/2), use n≥x/2−1 and log(2n)≤logx once the numerator is positive. The remaining sufficient inequality(log2)x/2−log(4x)≥0 holds at16 and increases thereafter. | Reconstruct from π(x)logx≥π(2n)log(2n)≥nlog4−log(2n), avoiding the fraction-denominator comparison. The same floor and log bounds yield the printed numerator; at16 the gap is2log2 and derivative stays positive. | VERIFIED_TWICE |
| C02-U06: second h inequality and finite prime chain | The printed substitution t=√(2n) gives h(n)/n=(2/3)log2−4(logt/t+logt/t²). Both subtracted functions decrease for t≥32, and h(512)>0. | The separate derivative bound h′>0.46−0.22−0.07>0 proves the same range. Trial primality and successor<2·predecessor independently validate the finite631 endpoint chain. Named Bertrand evidence is retained; this row covers its second unnamed explanation too. | VERIFIED_TWICE |
| C02-U07: odd-prime tracks | Every prime other than2 is odd, hence has remainder1 or3 modulo4. The figure's two sets exactly partition odd primes≤60. | Direct small-factor exclusion gives the same complete list; the local congruence definition now precedes its notation. The formerly asserted infinitude of the1mod4 track is now an explicitly deferred question with a pointer to ex:onemod4, not a premise borrowed from Chapter6. | VERIFIED_TWICE for the classification; later question is a preview |
| C02-U08: Fermat-number idea recheck | The old discovery note incorrectly said the difference of two Fermat numbers was a power of2; F2−F1=17−5=12 disproves that. The note now uses the earlier-product identity: a common divisor of Fm,Fn with m<n divides Fn and Fn−2, hence2. Oddness gives gcd1. | Independently Fn modulo Fm is(−1)^(2^(n−m))+1=2, so gcd divides2 and is1. The product identity follows directly by telescoping(X−1)product_{j<n}(X^(2^j)+1)=X^(2^n)−1 at X2. This revalidates the complete prompt/hint/idea/writeup at n0 and all m<n. | VERIFIED_TWICE after correction; ex:fermatnum count unchanged |
| C02-U09: optional prompt first-use repair | Defined positive squarefree integers in ex:erdosdiv itself and restricted both finite counts to positive n≤N; the parity-of-exponents decomposition and union bound then have the stated finite sample. Defined closed as complement-open and positive integer progression steps in ex:furstenberg. | Reconstructed the squarefree choices by subsets of the first k primes and b≤√N, including n1. Reconstructed the topology from progression neighbourhoods; De Morgan makes finite unions of closed progressions closed, now explained explicitly. No separate topology course or optional Chapter1 solution is presumed. | VERIFIED_TWICE for the repaired uses; whole exercise proofs remain in their original records |

### C02 examples and complete figure data

All six example blocks have two independent checks:

- C02-E01:5!+1=121=11², whose prime factor11 exceeds5; direct factorial
  multiplication and trial factorisation agree.
- C02-E02: the first four prime reciprocals sum to247/210=1.176190…;
  independent exact fractions/decimal summation agree. At100 the complete
  prime list gives1.802817…; loglog10−1=−0.165967… and
  loglog100−1=0.527180… match the printed rounding.
- C02-E03:2·3·5·7·11=2310,4^11=4194304; direct logarithms give
  log2310=7.745002… and11log4=15.249238…. Replaced the unintroduced
  theta symbol by the already defined vartheta.
- C02-E04:12choose6=924 and4^6/12=341.333…, verified by factorials and
  Pascal recurrence. The printed341.3 is a rounded illustrative value.
- C02-E05: the displayed prime chain2,3,5,7,11,13,19,23 covers every
  integer n1..20 by choosing a prime in(n,2n]. Independent full interval
  enumeration checks every n, including the n1 upper-end equality.
- C02-E06:20choose10=184756=2²·11·13·17·19; factorial valuation at7
  is2−2=0 and at13 is1. Replaced a rhetorical false inequality/question
  with this explicit complete factorisation and interval classification.

| Figure | First reconstruction | Separate data check | State |
| --- | --- | --- | --- |
| C02-F01: sieve50 | Enumerate integers2..50 and remove them at their smallest prime factor among2,3,5,7. Expected prime survivors15. | Parse each actual node and following mark: even composites have crosses, remaining multiples3 have slashes,25/35 squares,49 a diamond. Compare every mark with independent trial primality. | VERIFIED_TWICE data; final-size visual pending |
| C02-F02: prime-count plot | Reconstruct every staircase jump from the primes≤100. Compute the real comparison x/logx and Li(x)=integral_2^x dt/logt; the latter becomes a smooth integral exp(u)/u after t=exp(u). | Adaptive Simpson quadrature and independent trial-division prime counts recalculate every curve point, within half the source's last printed decimal. For the caption π(100000)=9592, first ratio1.1043198… and second0.996182… agree. Added the actual100000 endpoints to both ratio curves, which previously stopped at99000. | VERIFIED_TWICE data; final-size visual pending |
| C02-F03: mod4 tracks | Trial-prime list≤60 splits into7 primes1mod4 and9 primes3mod4, with2 separate. | Independently compare both literal TikZ foreach sets with those residue classes; their union plus2 exhausts all17 primes≤60. Circle/square/dot geometry carries the stated distinction. | VERIFIED_TWICE data; final-size visual pending |

The five new focused checks include the formerly false Fermat discovery note,
local definitions and all actual plotted coordinates. The structural route
guard now points to the retained early subsection that already explains
Euclid's composite counterexample; a second, duplicate full workshop was
removed. The explicit future1mod4 question is curated in the forward-preview
guard after checking its actual later proof site. No theorem or exercise was
removed. Ex:mersenne now explicitly specifies integer n≥1.

### C02 history, source evidence and remaining work

On4 November2026 read Erdős's original1932 paper at the
[Rényi Institute](https://users.renyi.hu/~p_erdos/1932-01.pdf), with its
[journal repository record](https://acta.bibl.u-szeged.hu/13396/).
The original credits Chebyshev and uses the binomial method, with different
cutoffs; the further-reading note now says that rather than claiming the
chapter reproduces the original numerical proof verbatim. The year1932,
volume5 and pages194–198 agree across the original and repository metadata.

Read the full one-paragraph Furstenberg proof in the
[university-hosted reprint](https://www.math.auckland.ac.nz/~gauld/750-05/inftlymanyprimes.pdf)
and checked the author's
[Hebrew University publication record](https://cris.huji.ac.il/en/publications/on-the-infinitude-of-primes/):
Monthly62(1955),page353. The local exercise supplies its own topology checks;
the reprint's unneeded normality/metrizability aside is not imported.

Viewed the local Chebyshev image. The likely corresponding
[Commons file record](https://commons.wikimedia.org/wiki/File:Pafnuty_Lvovich_Chebyshev.jpg)
names him, dates the photograph to the late1880s/early1890s, lists unknown
author and public-domain status, and gives its1964 printed source. This
supports the circa1890 caption. A direct original-image download returned403,
so an exact original-to-local pixel/provenance comparison is still pending;
the local asset has not been replaced or edited. The full further-reading
bibliography and broad PNT/Artin/Mertens historical previews are not signed off.

Complete Volume1 congruence notation is actually defined near line595 of
ch01-sums.tex; the present chapter's mod4 notation is also explained locally.
Logarithm/integral and finite binomial tools have the actual earlier proof
sites recorded in the prerequisite crosswalk. The main congruences route
continues to require none of the optional Chebyshev/Bertrand material.
Chapter2 remains open for final-size figures/pages, complete history/metadata,
external review and the whole-book dependency release pass.

## C03 — Congruences, DEP-063

Read the whole chapter, including all21 prompt/hint/idea/writeup groups and
bibliography. The eight named results keep their separate two-pass records;
no named mathematical statement was removed. The following unnamed arguments
and six example blocks supplement that register.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C03-U01: congruence classes/count | Divisibility of differences proves reflexivity, symmetry and transitivity; Euclidean division gives exactly one class representative0..n−1. | Two representatives in that range differing by a multiple of n have difference of magnitude<n and hence agree. Each integer is in its remainder class, including negative inputs and n1. | VERIFIED_TWICE |
| C03-U02: units form a group, F_p and rational fractions | Products of units have inverse y^(-1)x^(-1); identity and inverses stay inside, with inherited associativity. Added F_p=Z/pZ before use. For a/b with nonzero unit denominator, reduce ad=bc and invert bd to prove representation independence. | Uniqueness of an inverse follows by multiplying xu=xv by x^(-1). Reducing a rational fraction removes a common unit factor, giving the same class. The one-element ring's sole class is a unit, but not a field because0=1; the explanatory field statement now explicitly restricts n≥2. | VERIFIED_TWICE |
| C03-U03: cancellation iff unit | A unit cancels by its inverse. For g=gcd(c,n)>1, c(n/g)=c·0 modulo n but n/g is a nonzero class, so a nonunit fails cancellation. Added this converse explicitly. | Multiplication by c on n classes has a kernel of size g: the classes jn/g for0≤j<g. It is injective exactly when g1, independently recovering cancellation from the linear-congruence classification. Modulus1 has one unit and no exception. | VERIFIED_TWICE |
| C03-U04: exponent reduction and repeated-squaring cost | Euler's a^phi=1 gives a period for unit bases;2^4=0 mod8 versus2^0=1 shows why nonunits fail it. Binary expansion computes s powers by s−1 squarings and multiplies at most s selected factors with at most s−1 further products. | Induct on the binary digits: squaring doubles the represented exponent; an optional multiplication by a adds1. Starting from the leading1 proves the same bounds. Explicitly justified the binary-factor count rather than only stating it.7^13 mod23 independently equals20. | VERIFIED_TWICE |
| C03-U05: CRT unit count/totient product | The CRT isomorphism maps units exactly to pairs of units, hence phi(mn)=phi(m)phi(n) for coprime moduli. At p^k the excluded multiples count p^(k−1), giving p^k−p^(k−1); FTA completes the product. | Actual Volume1 ex:phi full solution counts prime-divisor exclusions by inclusion–exclusion, including n1. That independent proof confirms the source's earlier-volume attribution; it is not inferred from a title. Count phi100 directly as100−50−20+10=40 before the worked example uses it. | VERIFIED_TWICE |
| C03-U06: noncoprime CRT | Set x=a+mt; the second condition becomes mt=b−a modn, soluble iff gcd(m,n) divides b−a. Its one t class modulo n/d gives one x class modulo mn/d. | Necessity follows by subtracting the two congruences modulo d. Bézout on m/d,n/d independently constructs t. Differences of two solutions are multiples of both m,n, exactly lcm(m,n). The17mod35 and19mod24 examples check; parity excludes1mod6/2mod8. | VERIFIED_TWICE |
| C03-U07: formal derivative expansion and iteration | For integer coefficients, the binomial theorem separates constant/linear terms and leaves h² times an integer polynomial. With h=tp^k,2k≥k+1 kills the remainder; derivative invertibility gives exactly one digit. | Subtract any two lifts and reduce their difference to p^k(t−u)f′(a); unit cancellation modp forces t=u. Because polynomial f′ has the same residue at each child and parent, the hypothesis persists at every level; added this explicit iteration justification. | VERIFIED_TWICE |
| C03-U08: singular branches and completeness | At x0 mod5, X² has five lifts5t mod25; X²−5 has none because25t²−5 is not0 mod25. Simple X²+1 roots2,3 produce7,18 then57,68. | Exhaustive square residues mod5/25/125 give the same roots and nonroots. Any putative X²=5 mod25 first reduces to0 mod5, so its square is0 mod25; the formerly abbreviated dying-root example now gives this complete obstruction. | VERIFIED_TWICE |
| C03-U09: epigraph size | The integer has exponent3^27 at its base3. Since3^100>10^47, log10(3)>0.47, and0.47·3^27>3·10^12, its digit count exceeds3·10^12. | Independent logarithmic formula floor(3^27 log10(3))+1 gives the same inequality; modular periodic reductions in the tower exercise give final digits87 without building the number. The exact integer inequality is in regression. | VERIFIED_TWICE |

### C03 repaired exercise obligations and complete rechecks

- **C03-X01/ex:sunzi:** the old exercise repeated the historical worked
  example's exact remainders2,3,2 and answer23. Kept that historical example,
  but changed this practice prompt to remainders1,2,3 modulo3,5,7; it now
  asks for fresh work using the same taught method. Hint and full solution
  give x=7+15t,t=3mod7, hence **x=52+105k** for every integer k. Independent
  CRT idempotents give70+2·21+3·15=157=52mod105. Direct residue enumeration
  finds only52 in0..104, so both solutions are complete and handle negative
  members. The grade and stable key remain. The separate ex:t1-sunzi23
  practice with moduli4,9,11 still gives345mod396 and is unchanged. This is
  an explicit problem redesign under requirement6, not a silent deletion.
- **C03-X02/pb:wolsten:** the product was written as1+pe1+p²e2+O(p³).
  Under the earlier defined real big-O notation that is not a valid bound:
  the binomial product grows exponentially as p grows. Its actual intended
  claim is a congruence modulo p³ with unit denominators. Replaced it by
  that precise congruence. Expanding the finite product shows every omitted
  term has at least three factors p; independent pairing/power sums make
  pe1 and p²e2 vanish modulo p³. The earlier complete two symbolic checks
  and exact regressions through p101 were rechecked; no real-error estimate
  is claimed.
- **C03-X03/pb:kloosterman:** part(d) asked for comparison with part(b), but
  the source omitted that comparison. Added |K(a)|≤sqrt(p²−p) from the
  second moment, larger than p−1 since their squared difference is p−1.
  For p≥5,1.19p^(3/4)<p−1: verify at5 and differentiate
  (p−1)p^(−3/4), whose derivative is(p+3)/(4p^(7/4))>0. At p3 the rounded
  bound improves neither comparator; the exact fourth moment18 gives
  18^(1/4)=2.059767… between2 andsqrt6. Independent finite sums at the
  primes3..31 retain the earlier moment identities. All four requested
  parts now have explicit source answers.
- **C03-X04/pb:fpfunctions:** the F5 cubic example now proves its claimed
  bijection using its explicit inverse, also x↦x³, because x^9=x for all
  residues (Fermat for units and direct at0). It no longer presumes the
  later power-map/order criterion. Independent interpolation gives X³,X²,X
  for the three powers, as before.
- **C03-X05/ex:korselt:** the prompt referred to Carmichael numbers in
  Volume1's sums chapter, but a fresh search/read found neither that term
  nor561 there. Removed that false attribution. Defined squarefree and
  Carmichael number locally, then added the final unit cancellation showing
  a^561=a implies a^560=1 for coprime a. Independent CRT/Fermat on3,11,17
  checks all residues; the exact560 divisibilities by2,10,16 prove the
  universal statement. No optional Chapter1/2 vocabulary is presumed.

These changes reopen and revalidate their affected source items; the144-key
count is unchanged. The other keyed proof records are preserved, not counted
again. Further small repairs state integer a,b in the Jacobsthal prompt,
remove the claim that every integer has a prime factor, make the clock's
caption refer to its ring/dot shapes,
and replace unsupported future claims that Hensel constructs Z_p and that a
specific undeveloped schoolbook cost model promises a fourfold RSA speedup.
The mathematically accurate connections to p-adic equation solving and CRT
arithmetic remain. No theorem or exercise was dropped.

### C03 examples and four complete figure datasets

| ID | Independent reconstruction and separate check | State |
| --- | --- | --- |
| C03-E01: arithmetic mod12 |7+8=15=3mod12,7·8=56=8mod12;5²=25=1mod12 while4 has gcd4 and cannot give an odd residue. Direct residue enumeration agrees. | VERIFIED_TWICE internally |
| C03-E02:7^4 |49²=2401=1mod100; earlier powers7,49,43 are not1, so the least return is4. Direct inclusion–exclusion gives phi100=40. | VERIFIED_TWICE internally |
| C03-E03: historical Sunzi23 | Solving via the common2mod3/7 gives x=2mod21 and then k=1mod5, hence23mod105. Independent successive CRT via8mod15 also gives23mod105. | VERIFIED_TWICE internally |
| C03-E04: noncoprime cases |1mod4/2mod6 has opposite parity, impossible;1mod4/3mod6 has exactly9mod12. Independent full residue enumeration agrees with gcd2 compatibility. | VERIFIED_TWICE internally |
| C03-E05: simple lift |2+5t gives t1mod5 and7mod25; conjugate branch gives18mod25. Direct squares and exhaustive residues confirm exactly those two roots. | VERIFIED_TWICE internally |
| C03-E06: dying singular root | Any square5mod25 would be0mod5 and therefore0mod25, contradiction. Independent complete square-residue enumeration verifies the obstruction. | VERIFIED_TWICE internally |
| C03-F01: clock12 | The literal ring set1,5,7,11 is exactly the gcd1 set; filled others are its complement. Adding5 visits all12 classes because5 is a unit; adding4 visits0,4,8. The drawn arc's−150° moves five clockwise30° steps from0 to5. | VERIFIED_TWICE data; final-size visual pending |
| C03-F02: CRT grids | Parse every actual cell coordinate and number. Left x0..11 occupies(row xmod3,col xmod4) exactly once; right x0..7 occupies only compatible parity cells, each twice. Every drawn nonwrapping arrow adds1 to both residues. | VERIFIED_TWICE data; final-size visual pending |
| C03-F03: unit classes | All12 literal values occur once, at distinct3×4 grid positions. Circles1,5,7,11 are precisely the four invertible classes; the other eight boxes are nonunits. Independently solve inverses and compare the sets. | VERIFIED_TWICE data; final-size visual pending |
| C03-F04: Hensel tree | Literal branches2→7→57 and3→18→68 preserve reduction; every node satisfies x²+1=0 at its labelled modulus and derivative nonzero mod5. Independent exhaustive roots at5,25,125 establish no missing child. | VERIFIED_TWICE data; final-size visual pending |

Six new regressions read these actual source datasets and guard the new
field/fraction conventions, precise modular product and second-moment answer.
The existing Sunzi regression now checks both the retained historical case
and the fresh exercise, including its signed family and independent explicit
CRT construction. A final-size visual pass remains required.

### C03 actual earlier sources and historical checks

Read Volume1 `ch02-counting.tex` ex:phi prompt and complete solution near
lines439/594: it proves the totient product by finite inclusion–exclusion,
including the empty product n1. This verifies the genuine earlier attribution.
The Carmichael/561 attribution had no such source and was replaced locally.
Polynomial division/root count and finite polynomial multiplication are proved
in Volume1 at the crosswalk sites; no later primitive-root, field-extension,
Bernoulli or analytic product theorem is needed on these exercise routes.

Historical/source checks on4 November2026:

- [Gauss's Latin Section1, Article2](https://la.wikisource.org/wiki/Disquisitiones_arithmeticae/Sectio_prima)
  explicitly introduces the congruence sign, with examples modulo5/11;
  [the Humboldt library's1801 record](https://edoc.hu-berlin.de/items/4a65bbe3-c434-4581-8d40-2c3b426d3cf2)
  supplies first-edition metadata. No claim to have read the entire book or
  its1986 English translation is made.
- [Japan's National Diet Library](https://www.ndl.go.jp/math/e/s1/c2.html)
  quotes the actual Sunzi2/3/2 remainder problem and the minimal answer23.
  The newly altered practice exercise is labelled as a new problem using
  the method, avoiding historical misattribution of its new remainders.
- The [Annals publisher record](https://annals.math.princeton.edu/1994/139-3)
  confirms Alford/Granville/Pomerance's139(1994),703–722 reference and its
  infinitude title. That research theorem is further reading, not a premise.
- [The LMS publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s2-25.1.143)
  dates Kloosterman's quaternary-form paper to1926, supporting the teaser's
  date. The book's fourth-moment proof is fully local; the2sqrt(p) bound
  remains a clearly separate deeper result, never used in that proof.

Complete edition/section checking of the remaining bibliography, the detailed
future research previews, final-size formats and a distinct editorial reader
remain open. Chapter3 is not signed off.

### Palette clarification after C03

The Chapter3 clock's original “dark grey” caption was consistent with the
shared palette: common/figure-palette.tex maps ocTeal to teal, then defines
teal as dark grey. The raw TikZ name alone did not establish a colour error.
The retained ring/dot wording is a shape-based clarification, not a correction
of an incorrect rendered colour. This clarifies DEP-063's overly strong
caption description; final-size contrast remains to be inspected.

## C04 — Arithmetic functions, DEP-064

Read the whole chapter, all10 prompt/hint/idea/writeup groups and bibliography.
The four named results and10 keyed proofs keep their earlier separate records.
This pass checks the surrounding claims, nine example blocks and three complete
figure datasets; final chapter acceptance remains open.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C04-U01: multiplicative functions and local formulas | FTA bijects divisors of coprime mn with pairs of divisors of m,n. Counting pairs gives tau multiplicativity; summing products gives sigma multiplicativity. The prime-power exponents give tau(p^a)=a+1 and the finite geometric sigma sum. | Independently expand the finite products of1+X+…+X^a at each distinct prime, keeping their exponents separate. The elementary functions1,id,epsilon and mu satisfy their product laws directly; phi uses the earlier CRT units bijection. All identities have empty product1 at n1. | VERIFIED_TWICE |
| C04-U02: inversion as subset cancellation and numerical12 | Squarefree divisors correspond to prime subsets, with signs(−1)^size; the sum is(1−1)^r for r>0 and1 for r0. Applying the four nonzero coefficients at12 gives f12=g12−g6−g4+g2. | Expanding each g(d) into its divisor sum cancels every proper-divisor coefficient and leaves f12 once. Independently evaluate prime powers and use multiplicativity. Corrected wording that misleadingly called two numerical cases the whole prime-power proof. | VERIFIED_TWICE |
| C04-U03: phi, tau and sigma convolution identities | Gauss's divisor sum gives phi=mu*id; tau=1*1 and sigma=id*1 follow directly by enumerating factor pairs. Finite prime-power evaluation gives their displayed products. | Count coprime residues by inclusion–exclusion for phi and directly enumerate divisor exponents for tau/sigma. At72 this gives tau12,sigma195,phi24 independently of convolution. Pointwise multiplication is explicitly distinguished from convolution. | VERIFIED_TWICE |
| C04-U04: replacement inversion workshop | From sum_{d|n}f(d)=n², successive subtraction gives f1=1,f2=3,f3=8,f4=12,f6=24. Möbius inversion gives f12=144−36−16+4=96; summing all six recovered values returns144. | Independently count pairs(a,b) in1..n with gcd(a,b,n)=1. At12 inclusion–exclusion removes36 even-coordinate pairs and16 pairs divisible by3, restores4 divisible by6, yielding96. Partition all n² pairs by gcd(a,b,n); division by that gcd shows these counts have exactly the required divisor sum. This also proves existence and uniqueness for all positive n, with n1 included. | VERIFIED_TWICE |
| C04-U05: perfect-number explanations | Sigma(n)=2n is equivalent to the sum of proper positive divisors equalling n. The even classification's converse uses sigma(m)=m+s; if s>1 the distinct divisors1,s,m make the sum too big. Composite Mersenne factors cannot satisfy that classification. | Direct multiplicative sigma evaluation checks6,28,496 and the failed90 example. Independently use the complete even-perfect theorem already proved to exclude2^10(2^11−1), whose odd factor23·89 is composite. The earlier odd-perfect exercise proof is local and uses no external nonexistence theorem. | VERIFIED_TWICE |
| C04-U06: rough divisor average, hyperbola strips and errors | Ordered positive pairs ab≤x count sum tau(n). The long sum has floor error<x and harmonic main term xlogx+O(x). Short strips a≤m or b≤m, m=floor√x, cover every point; overlap is the complete m×m square. The doubled floor error is<2m and |m²−x|<2m+1. | Partition the complement: if a,b>m then ab≥(m+1)²>x, while all m² square points satisfy ab≤x. Independently apply the actual Volume1 harmonic bounds to get H_m=logm+gamma+O(1/m), with log(√x/m)≤1/m. Dividing by floorx yields a long average asymptotic to logx, without claiming pointwise smoothness or short-interval bounds. | VERIFIED_TWICE |
| C04-U07: finite coprime model and convergence uses | Uniform independent choices1..N give probability C(N)/N². The local mu indicator gives exact floor-square count; the finite error and absolute tails give the limit reciprocal to the Basel sum. The epigraph now states that finite experiment and says coprime, replacing ambiguous random integers/no common factor. | Independently count visible pairs by primitive rays as in Chapter1; gcd classification gives the same indicator. The full series product is justified by a2Z/K double-tail bound with **positive integer K**, now explicitly specified; a noninteger K would not give the printed telescoping equality1/K. Actual Volume1 inclusion–exclusion, absolute rearrangement and Basel proofs are in the crosswalk. | VERIFIED_TWICE |
| C04-U08: accurate later-series/finite-field previews | The future series statement now specifies absolute convergence; for real s>1 the mu series is1/zeta(s), with zeta defined. The already self-contained s2 proof is distinguished from that later general theorem. | Actual Volume3 main.tex includes ch09-finite-fields; its thm:countirr proof counts degrees to obtain sum dN_q(d)=q^n, then divides the inverted primitive-word expression by n. Added this missing division and the monic/degree qualifications to the teaser. Independent F2 polynomial enumeration through degree6 checks the factor. Neither future result is a proof premise here. | VERIFIED_TWICE for accuracy of the previews; full later theorem proofs are not imported |

The workshop heading formerly introduced a third repetition of the same subset
proof for sum mu(d). That proof remains in the theorem and its earlier
inclusion–exclusion explanation. The replacement workshop instead performs an
actual inversion on new data; no theorem or exercise was removed. Clarified
positive integer domains, word-power concatenation, prime-square divisibility
in the mu definition and the sample-size/cutoff domains. Replaced claims that
three sample mu values were the whole definition or that step-function averages
were smooth by the precise mathematical statements. Removed a repeated
odd-perfect-number status sentence; the open question remains explicit in the
section's introduction and further reading.

### C04 examples and complete plotted data

| ID | Independent reconstruction and separate check | Status |
| --- | --- | --- |
| C04-E01: multiplicative-function list | Verify1,id,epsilon,mu directly at coprime inputs, phi by CRT, tau/sigma by divisor bijections (U01/U03). The definition now explicitly excludes prime squares rather than ambiguously saying a square factor. | VERIFIED_TWICE internally |
| C04-E02: tau/sigma12 | The six divisors1,2,3,4,6,12 sum to28. Independent exponent choices give3·2=6 divisors and(1+2+4)(1+3)=28; tau4=3 differs from tau2²=4. | VERIFIED_TWICE internally |
| C04-E03: mu12/30/1 |12 has prime square4, giving0;30 has three distinct prime factors, giving−1; the empty product at1 gives1. Independent squarefree-subset definition agrees. | VERIFIED_TWICE internally |
| C04-E04: convolution12 | Actual divisor mu values1,−1,−1,0,1,0 sum to0; at1 the sum is1. Independent subset cancellation matches, without pretending these two samples prove the identity. | VERIFIED_TWICE internally |
| C04-E05: mu*tau | The actual12 calculation6−4−3+2=1 agrees with associativity(mu*1)*1=epsilon*1=1. Independent local factor(a+1)−a=1 gives the general multiplicative value. | VERIFIED_TWICE internally |
| C04-E06: perfect28 | Proper divisors1,2,4,7,14 sum28; direct sigma4·sigma7=7·8=56 proves the same. | VERIFIED_TWICE internally |
| C04-E07: failed90 | Divisor enumeration gives sigma90=234; the product3·13·6 independently agrees. Ratio234/90=2.6, and odd part45 differs from the required3. | VERIFIED_TWICE internally |
| C04-E08: summatory tau10 | Values1,2,2,3,2,4,2,4,3,4 sum27; independent short-strip calculation2(10+5+3)−9=27 matches. | VERIFIED_TWICE internally |
| C04-E09: average10 |27/10=2.7; log10+2gamma−1=2.457016… rounds to2.46. The theorem controls the asymptotic normalized error, without promising monotone improvement at every successive N. | VERIFIED_TWICE internally |
| C04-F01: orchard12 square | Parse all91 filled centres and53 cross centres. Independent gcd computation classifies every one of the144 pairs. The dashed8.4/12.6 direction is2/3, hitting exactly(2,3),(4,6),(6,9),(8,12) inside the square; the nearest is primitive. | VERIFIED_TWICE data; final-size visual pending |
| C04-F02: divisor72 grid | Every actual cell label equals2^i3^j at its column/row. The12 distinct labels exhaust the divisors, sum195 and yield the multiplicative count/product independently. | VERIFIED_TWICE data; final-size visual pending |
| C04-F03: hyperbola30 | Every plotted point satisfies ab≤30 and every such positive pair appears. The square25 points are MidnightBlue, the43 upper-arm points ForestGreen and43 right-arm points Orange. The shared palette maps those to charcoal/ochre/coral, matching the caption. Counts give68 points in each strip and2·68−25=111. | VERIFIED_TWICE data; final-size visual pending |

Six focused regressions recalculate all these coordinates/classifications,
the replacement workshop and the missing degree divisor. The latter source
guard fails on the former teaser, and independent monic-polynomial trial
factorisation supplies its numerical counterexample: degree2 over F2 has one
irreducible polynomial but two primitive words. New source inventory remains
98 example blocks and144 exercises; source changes require renewed artifacts.

### C04 historical/source checks and boundaries

- The cited [Nielsen AMS paper](https://www.ams.org/mcom/2015-84-295/S0025-5718-2015-02941-X/S0025-5718-2015-02941-X.pdf)
  metadata confirms84(2015),2549–2567. Its abstract and the
  [author's own PDF](https://mathdept.byu.edu/~pace/BestBound_web.pdf)
  explicitly give at least10 distinct prime factors. Read those specific
  passages, not the entire computer-assisted research proof. The book's
  exercise proves its weaker three-factor claim itself.
- The [digitized Möbius record](https://www.digizeitschriften.de/download/pdf/243919689_0009/log12.pdf)
  and [Encyclopedia of Mathematics bibliography](https://encyclopediaofmath.org/wiki/M%C3%B6bius_series)
  corroborate1832,volume9,pages105–123 and DOI10.1515/crll.1832.9.105.
  Direct scan/DOI access failed; original-page visual inspection is not
  claimed. The inversion proof in the chapter is independently reconstructed.
- The Pólya1918 reference has the separately checked original bibliography
  and research-institution references recorded under C01. The book's square
  orchard and probability calculation are established locally.
- Actual Volume3 `thm:countirr` source was read to check the future count
  formula, with its reading-order inclusion confirmed in main.tex. This is
  a preview accuracy check, not a backward dependency or a certification of
  Volume3.

The complete remaining edition/chapter bibliography, historical priority,
current-source final-size figures/pages, complete release dependency graph
and independent external review remain open. Chapter4 is not signed off.

## C05 — Primitive roots, DEP-065

Read the complete chapter, all 16 prompt/hint/idea/writeup groups and its
bibliography. Its six named results and 16 keyed proofs retain their separate
records, with the classification's parity explanation and the Ramanujan zero
case reopened and rechecked here. This pass covers ten examples and three
complete figure datasets. No chapter acceptance is claimed.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C05-U01: decimal periods and opening | Long division has remainder 10^j mod p after j digits. For p other than 2,5 the remainder is never zero; its least return to 1 is the least digit period. A repeating k-digit block gives 1/p=A/(10^k−1), so p divides 10^k−1, and conversely that divisibility supplies a block, allowing leading zeros. | Independently sum the geometric series of repeated blocks: 142857/(10^6−1)=1/7 and 588235294117647/(10^16−1)=1/17, padding the latter to 16 digits. Direct order tests give 6 and 16. Revised epigraph separates this known criterion from the open infinitude question and explicitly excludes 2,5. | VERIFIED_TWICE |
| C05-U02: order/return explanations | Division m=qk+r with 0≤r<k reduces a^m to a^r; minimality forces r0 for a return. Negative exponents use the already defined inverse. Applying this to a^j gives least positive return k/gcd(k,j). | Independently use the subgroup of integer exponents returning 1, generated by k, and pull it back under multiplication by j. Check j0 and n1, and distinguish the first return from Euler's possibly larger exponent. The formal proof is separately registered; this checks the explanatory alternate route. | VERIFIED_TWICE |
| C05-U03: field root bound and exact-order counting | Divide a nonzero polynomial with root a by X−a. Any other root b satisfies (b−a)Q(b)=0; invertibility gives a root of the lower-degree Q. Induction excludes more roots than degree. | Adversarially check degree0, the excluded zero polynomial, p2 and the counterexample X²−1 over Z/8. In the order count, N(d)=0 is allowed before existence is established; otherwise the d powers exhaust the roots, and the order formula gives phi(d). Nonnegative deficits sum to zero via the earlier totient identity. No generator is presumed to exist. | VERIFIED_TWICE |
| C05-U04: generator certificate and replacement workshop | If d properly divides M, a prime q divides M/d, so d divides M/q and that test returns 1. Conversely a returned 1 makes the order divide the smaller exponent. Empty tests at M1 are valid. | For any proper d, choose a prime at which its valuation is below that of M; this constructs the failed test independently. At 29, powers of 2 at 4,7,14,28 are 16,12,28,1: order28. For 4, direct tests at 2,7,14 are 16,28,1: order14, independently agreeing with 28/gcd(28,2). | VERIFIED_TWICE |
| C05-U05: noncyclic obstruction | Unit pairs a,−a have no fixed point when n>2, since a can be cancelled; therefore phi(n) is even. A cyclic even-order group has only exponent classes 0,m/2 solving twice the exponent=0. Independent prime-power signs combine under CRT to give at least four roots in excluded moduli. | For 2^k, k≥3, roots 1,−1,2^(k−1)+1,2^(k−1)−1 are distinct and square to1 by expansion. Conversely a root is odd and 2^k divides (x−1)(x+1); these factors have gcd2, so one has valuation1 and the other at least k−1, forcing exactly those four classes. Mod16, 3² and 5² equal9, disproving the old claim that the same representatives persist. Classification proof remains valid and now supplies its parity justification locally. | VERIFIED_TWICE |
| C05-U06: odd-prime lifting explanation | The binomial expansion at 1+p^k t has leading difference p^(k+1)t; every later term is divisible by p^(k+2), including the p3,k1 endpoint. Thus the first nonzero p-adic coefficient cannot disappear. | Independently factor x^p−1=(x−1)(1+x+…+x^(p−1)); expanding the second factor shows it is p mod p² for odd p and x=1 mod p. This adds exactly one valuation. If the initial g fails at p², the first-order binomial term for g+p is −p g^(p−2), a nonzero coefficient. Values 2²=1+3,2^6=1+9·7,2^18=1+27 mod81 check the displayed levels. | VERIFIED_TWICE |
| C05-U07: discrete-log coordinates and equations | Powers of a primitive g are a bijection from exponents mod p−1 to nonzero residues mod p. Multiplication adds exponents; x^r=a is a linear congruence in that coordinate. For x^4=3 mod13 the exponents 1,4,7,10 give 2,3,11,10. | Direct fourth powers of all 13 residues give exactly that set; x^4=2 has none, and the cubes equal to5 are 7,8,11. The replacement fifth-power example has exponent8 and unique root9, independently checked by direct enumeration and 9²=3,9^4=9,9^5=3 mod13. Hardness is a qualified cryptographic assumption, not a proof premise. | VERIFIED_TWICE |
| C05-U08: squares and cosets | In a commutative group products and inverses of squares are squares. For a subgroup H, a common point of aH,bH gives b^(-1)a in H and equality; otherwise the cosets are disjoint. Multiplication by a bijects H with aH. | Independently reduce units mod2^k to the four units mod8. This surjective multiplicative map has kernel exactly the square subgroup by the proved corollary; each inverse image is one coset. At k3 the kernel is {1}, and at k4 it is {1,9}, giving the four displayed pairs. Added the subgroup closure proof before using the term. | VERIFIED_TWICE |
| C05-U09: future character count | Actual Chapter11 prop:t1-unitproduct and the character-count proof use a choice of a root of unity at each cyclic factor, not the number of primitive roots itself. Every cyclic factor of size N gives N choices. | Multiply those choices over CRT factors and the two-power decomposition to obtain phi(m), including m1. Replaced the misleading generator-count explanation by the actual dependency. Removed the duplicate Artin teaser's false Volume5 proof promise; the later, correctly qualified Hooley statement remains. | VERIFIED_TWICE for the preview; not later-volume certification |

### C05 examples and complete plotted data

| ID | Independent calculation and separate check | Status |
| --- | --- | --- |
| C05-E01: orders modulo7 | Direct powers give ord(2)=3 and ord(3)=6. The prime-divisor generator test at exponents2,3 independently accepts3 and rejects2. | VERIFIED_TWICE internally |
| C05-E02: all returns | The residues 2,4,1 have distinct first two nonidentity entries; periodicity gives precisely positive multiples of3. Independently the exponent kernel is3Z. | VERIFIED_TWICE internally |
| C05-E03: generator3 and subgroup2 | The six powers of3 enumerate all nonzero residues; powers of2 give exactly {1,2,4}. Independent multiplication by3 is one six-cycle, whereas multiplication by2 has two three-cycles. | VERIFIED_TWICE internally |
| C05-E04: all generators7 | Coprime exponent classes1,5 yield3,5. Independently test all six units; only3,5 have order6. | VERIFIED_TWICE internally |
| C05-E05: four roots | Directly square the four odd residues mod8. The valuation/adjacent-even-factors argument in U05 proves the exact general root list, whose representatives change with k; explicit mod16 counterexample repairs the old sentence. | VERIFIED_TWICE internally after correction |
| C05-E06: generator9 | Powers2,4,8,7,5,1 exhaust the units. Independently exponents2 and3 give4 and8, excluding each proper divisor of6; the square4 then has order3 by direct4,7,1. | VERIFIED_TWICE internally |
| C05-E07: logarithm13 | 2^4 is3 mod13, but its exact integer value is16; corrected the equal sign. Direct3,9,1 gives order3, independently matching12/gcd(12,4). Removed the distracting rhetorical question. | VERIFIED_TWICE internally after correction |
| C05-E08: replacement fifth-power equation | The old box duplicated the preceding complete x^4=3 solution, which remains in U07. The new x^5=3 example gives unique9 by inverse5 in exponent space; independently direct powers/enumeration agree. Same box count and no exercise change. | VERIFIED_TWICE internally for the new obligation |
| C05-E09: units16 | Direct powers of5 are1,5,9,13, and their negatives are15,11,7,3 mod16. Corrected false integer equalities to congruences. Squaring all eight gives {1,9}; independently these are exactly the units1 mod8. The later17 example has root7 mod32 since49−17=32. | VERIFIED_TWICE internally after correction |
| C05-E10: order5 modulo32 | 5^4=625 is17 mod32 and 5^8 is1 mod32, so the order is8. Corrected 5^8=17² and 5^4=17, both false integer equalities, to congruences. Independent valuation gives v2(5^4−1)=4 and v2(5^8−1)=5. | VERIFIED_TWICE internally after correction |
| C05-F01: order histogram13 | Parse all six actual tick labels and data heights; direct first-return counting gives orders1,2,3,4,6,12 with counts1,1,2,2,2,4, total12. Independently the cyclic exponent formula gives phi(d) for each divisor. | VERIFIED_TWICE data; final-size visual pending |
| C05-F02: both primitive-root panels | Parse all24 node labels and all24 coordinate arrows. Each panel lists 2^j mod13 in exponent order. Every left arrow doubles; every right arrow triples. Tracing actual arrows gives one12-cycle and four3-cycles respectively. Shaded labels in both panels are exactly2,6,11,7, independently determined by order12. | VERIFIED_TWICE data; final-size visual pending |
| C05-F03: cycle7 | Parse all six labels and six directed edges; the label sequence1,3,2,6,4,5 follows multiplication by3 including the wrap to1. Independent exponent computation confirms a complete cycle with no omitted unit. | VERIFIED_TWICE data; final-size visual pending |

The replacement workshop uses modulus29 rather than repeating the previously
proved 2/7 and3/7 calculations. Those calculations remain in the order section,
examples and practice solutions. The replacement power box keeps its count and
now illustrates a unique root instead of repeating the four-root paragraph.
These are new checked teaching obligations, not silent removals of proofs.

The Ramanujan prompt allows every integer n. Its previous solution used v_p(n)
at n0, although the earlier valuation definition excludes zero. Added the
direct c_q(0)=phi(q) case before that step and used v_p(abs(n)) for nonzero
signed n. Pass A groups complete geometric sums by reduced denominator and
applies Möbius inversion. Independently insert the coprimality indicator into
the exponential sum; summing complete roots of unity gives the same divisor
formula. Its three prime-power cases match Hölder, including q1 and n0;
reduced-fraction Fourier orthogonality gives the stated average, including
q=r=1. New numerical checks include all signed n in [−q,q], q≤40, with a
source guard for the zero case. The keyed solution was reopened, repaired and
rechecked; the total remains144, not an extra counted verification.

Seven focused regressions check the complete figure data, changed root
representatives, repaired congruence signs, fresh examples and signed/zero
Ramanujan sums. They supplement the symbolic arguments above and do not
replace general proofs. Whole-source coverage through Chapter5 is now35 of98
example blocks and18 of39 mathematical figure datasets internally.

### C05 historical/source checks and boundaries

- [Gauss's Latin Section III](https://la.wikisource.org/wiki/Disquisitiones_arithmeticae/Sectio_tertia)
  contains the orders, primitive-root arguments, indices and Wilson discussion,
  and explicitly discusses Euler's earlier work. Replaced the overbroad
  assertion that these ideas first appear in Gauss by a systematic treatment.
  Translation edition details still need the complete bibliography pass.
- The [journal's actual Volume12A contents](https://math.colgate.edu/~integers/vol12a.html)
  identifies Moree's article A13; corrected the missing A in the volume number.
  Read the introduction and the Hooley passage of the
  [author's MPIM survey](https://archive.mpim-bonn.mpg.de/id/eprint/1236/1/preprint_2012_53.pdf).
  They distinguish decimal periodicity from the infinitude conjecture, give
  Artin's constant and exceptions, record Hasse's September1927 diary, and
  specify GRH for the fields Q(zeta_k,g^(1/k)), k squarefree. At g10 the square
  part exponent is1 and the quadratic discriminant is40, hence the survey's
  density formula has no correction factor: A=0.3739558… . No proof of the
  research theorem has been imported or certified.
- [Smith's publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s1-7.1.208)
  confirms the1875 arithmetical determinant paper, volume7,208–213. Both
  determinant identities here have separate local algebraic proofs.
- Actual Chapter11 character-count sources and Volume3's thm:cyclicmult were
  inspected for preview accuracy. The latter's actual proof combines the classification of finite abelian
  groups with the same polynomial root bound; it does not repeat this
  chapter's exact-order counting proof. DEP-066 changes the source
  preview to name that shared root bound precisely. Neither is a premise for this chapter.

Complete bibliography/priority checking, every latest-source final-size page,
all-format proof and independent editorial/author acceptance remain open.

## Fixed-snapshot layout sample after DEP-065

The detached f59c9ac5023efa272f4f6466e30b83bbd48e1a2f build completed
successfully:327 print pages, spine0.7698in,18,932,252-byte EPUB,39 full-width
plates and the HTML reader. Source worktree remained separate. The reading PDF
has328 physical pages including its cover. Inspected actual rendered reading
PDF pages19,26,65,98,110 (printed6,13,52,85,97) at1.5x. These cover rational
valuation, Chapter1 exercise layout, modular fractions and cancellation,
the Chapter4 orchard and the corrected finite-field preview. No clipping,
overlap or lost mathematical signs observed in this sample. Images are in
/tmp/pr103-layout-f59c9ac5. This is a five-page sample, not a whole-page proof,
and the snapshot predates DEP-065 Chapter5 and DEP-066 Chapter6 edits.

## C06 — Quadratic reciprocity, DEP-066

Read all Chapter6, all19 prompt/hint/idea/writeup groups and its bibliography.
The six named results and19 keyed proofs keep their separate records. This
pass addresses surrounding arguments, eight retained examples and four full
figure datasets. The strengthened sampling guarantee is independently derived
below; no overall chapter approval is claimed.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C06-U01: roots, input pairs and square counts | For p odd, nonzero inputs x and−x are distinct and have the same square. Equal squares imply (x−y)(x+y)=0 in the field, hence y=±x. Every nonzero square has exactly two roots. | Independently, write each nonzero residue as g^j in the earlier primitive-root coordinate. Squares correspond exactly to even j, giving (p−1)/2 squares. Corrected wording that called the square values themselves pairs x,−x: at p7,1 is square and−1 is not. Zero is separate with one root. | VERIFIED_TWICE |
| C06-U02: first character and cancellation | Defined chi(a)=(a/p) explicitly before the first abbreviation. Equal numbers of signs plus chi(0)=0 give complete sum0. | Independently choose a nonresidue b, whose existence follows from U01. Multiplication by b permutes all residue classes, and complete multiplicativity gives S=chi(b)S=−S, hence S0 over the integers. No independence assumption is used. | VERIFIED_TWICE |
| C06-U03: signed permutation explanation | Reduce a,2a,…,((p−1)/2)a to symmetric representatives. Equal absolute values would force two indices equal or sum p, the latter impossible in the half-range. Cancelling the invertible half-factorial leaves (−1)^mu. | At (a,p)=(3,11),(2,11),(3,13), signed lists are3,−5,−2,1,4;2,4,−5,−3,−1;3,6,−4,−1,2,5. Direct square tests independently give signs+,−,+. Negative multipliers and the p3 endpoint retain the same distinctness proof. | VERIFIED_TWICE |
| C06-U04: two-law and Eisenstein hypotheses | For doubling, the negative count is (p−1)/2−floor(p/4). Its four values at p=8m+1,3,5,7 have the stated parity. Subtracting the two residue-sum equations for odd a gives T(a,p)=mu mod2. | Independently classify the doubled half-range by the threshold p/2. At a2,p3 the floor sum is0 but the symbol is−1, so oddness cannot be removed. Added an explicit odd-prime p hypothesis to the lemma rather than relying on surrounding notation. Formal theorem proofs retain their prior separate checks. | VERIFIED_TWICE |
| C06-U05: rectangle partition | Distinct primes prevent a point of the allowed positive rectangle from lying on qx=py. Below-line floor sums and above-line row sums partition all (p−1)(q−1)/4 points. | Independently subtract each below-line column count from the rectangle height and sum the complement; exchanging axes gives T(p,q). For7,11 direct enumeration gives8+7=15 and the two independently listed square sets give opposite signs. No numerical case is offered as a general proof. | VERIFIED_TWICE |
| C06-U06: decision and root construction | Factor219=3·73. Reciprocity gives (3/383)=1, while (73/383)=(18/73)=(2/73)=1, hence symbol1. When p3 mod4, a^((p+1)/4) squares to a for a nonzero square, by Euler's criterion. | Independent repeated squaring gives residues86,119,373,100,42,232 and root169 at exponent96. Directly169²=383·74+219, and all383 square inputs yield exactly roots169,214. Trial division by every prime≤19 verifies383 is prime. Kept the full original decision and root construction while removing its later duplicate box. | VERIFIED_TWICE |
| C06-U07: Jacobi definition and reduction algorithm | Multiplying Legendre symbols over the prime factors, with repetition, defines Jacobi and preserves complete multiplicativity. The mod4/mod8 exponent functions are additive mod2; factoring into prime pairs proves reciprocity for coprime odd denominators. | For the algorithm, the invariant is original symbol=s times the current symbol. Reduction preserves periodicity; stripping2 multiplies s by its supplementary sign; odd swaps multiply by the reciprocity sign. If the gcd is not1, both swapped symbols are0, so the same invariant holds. Denominators strictly decrease after swaps; stops at a0,n1 use the correct empty product. Direct factor-based evaluation checks the full1001/9907 chain,19/35,43/91 and83/101. | VERIFIED_TWICE |
| C06-U08: finite-base primality probability | The repaired Rabin discussion samples bases independently and uniformly from1..n−1, rejecting nonunits. For n other than9, L≤phi(n)/4≤(n−1)/4. At9 there are2 liars out of8 bases, again1/4. Independence multiplies these per-trial bounds to4^(−k) for any fixed composite. | Independently count strong-liar exponent tuples at every odd prime-power component; Monier's formula gives the same L. At9 the unit-only sample instead has2/6=1/3, demonstrating why a sample-space qualification is necessary. Direct enumeration of every unit base for all511 odd composites<1500 checks both the unit exception and the all-base guarantee. This is a bound on accepting a fixed composite, not a posterior probability that an accepted input is prime. | VERIFIED_TWICE |
| C06-U09: new Jacobi workshop | The old7/11 workshop repeated the opening, theorem picture and preceding explanation. Those arguments remain. New43/91 requires a negative first swap, a positive second swap, and (3/5)=−1, yielding+1. New83/101 reduces to(18/83)=(2/83)=−1. | Independently factor91=7·13 and101 prime and evaluate symbols by complete small square sets; both answers agree. The plus sign for a composite is explicitly distinguished from a root certificate; the earlier2/15 counterexample remains. No exercise changed. | VERIFIED_TWICE |

### C06 examples and complete diagram data

| ID | Independent reconstruction and separate check | Status |
| --- | --- | --- |
| C06-E01: residues11 | Squaring0..5 gives0,1,4,9,5,3; the two-root argument proves completeness. Independent Euler powers give the same five nonzero signs and their complement2,6,7,8,10. | VERIFIED_TWICE internally |
| C06-E02: Euler13 | Exact3^6=729=13·56+1,4²=16=3 mod13;2^6=64=−1 mod13. Independent full square enumeration accepts3 and rejects2. | VERIFIED_TWICE internally |
| C06-E03: Gauss3/13 | The six signed representatives3,6,−4,−1,2,5 give two negatives; independent root4 proves the plus sign. | VERIFIED_TWICE internally |
| C06-E04: supplementary17/13 | Exponents36 and21 have even/odd parity respectively. Independent6²=2 mod17 and the full mod13 square set verify the two signs. | VERIFIED_TWICE internally |
| C06-E05: decision219/383 | Retained the original complete example and the separate root construction, checked in U06. The later examplex repeated the same computation and was removed explicitly; its mathematical obligation remains in full. | VERIFIED_TWICE internally |
| C06-E06: sign3/7 | Squares mod7 omit3, whereas7=1 mod3. Independent reciprocity exponent3 gives product−1. | VERIFIED_TWICE internally |
| C06-E07: Jacobi2/15 | The mod3 and mod5 symbols are both−1, so their product is1. Independent direct squares mod15 omit2, demonstrating the lost information at a composite denominator. | VERIFIED_TWICE internally |
| C06-E08: swap19/35 | Both are3 mod4, giving−(16/19)=−1;16 is a nonzero square. Independent factoring35=5·7 gives (19/5)=1,(19/7)=−1. | VERIFIED_TWICE internally |
| C06-F01: residue strip | Every actual0/1 classification for all11 nodes equals its direct square-membership test. Shared palette maps ocTeal to dark grey, so changed the misleading raw-colour legend teal to shaded. Completeness independently follows from U01. | VERIFIED_TWICE data; current full-page visual pending |
| C06-F02: reciprocity table | Every25 actual row/column sign matches direct square enumeration at3,5,7,11,13. Every six shaded off-diagonal cells corresponds precisely to two3mod4 primes. Independently reciprocal sign products give the theorem's parity and all diagonal entries are0. | VERIFIED_TWICE data; full-page visual pending |
| C06-F03: Eisenstein rectangle | All15 actual plotted points are present; each colour agrees with7y<11x or its strict reverse. Direct counts8/7 agree independently with the two floor sums. The drawn endpoint3.5/5.5 has exact slope11/7. Shared palette applies charcoal/ochre. | VERIFIED_TWICE data; full-page visual pending |
| C06-F04: liar plot | Previously352 Euler and321 strong markers omitted159 and190 low values respectively, despite the each-composite caption. New generator includes both series at all511 composites,1022 markers, six-decimal fractions and explicit pt-size hollow/filled marks. Tests independently enumerate every unit base and match the formulas and every actual coordinate within half a last decimal. | VERIFIED_TWICE data; standalone rendered at actual native width; whole-page visual pending |

The generator counts Euler liars by primitive-root exponents at each odd
prime power: a coordinate t has Jacobi sign(−1)^(e·t), and its Hth power
matches global sign sigma precisely when Ht=sigma·phi(p^e)/2 mod phi(p^e).
A two-state parity count over the CRT factors sums exactly the tuples with
that global sign. This independently derives the same Euler count that the
tests obtain by modular powers and a prime-factor square-membership definition
of Jacobi. Strong counts use the separately reconstructed Monier formula.
No plotting threshold remains. Regeneration is
`python3 tools/volume2_liar_figure.py`; its `--check` validates freshness.

Rendered the new figure through the real shared fonts/palette/TikZ wrapper
with XeLaTeX. Native output is307.10×147.28pt, fitting the book's linewidth
without enlargement; inspected /tmp/pr103-ch06-liars.png at3x. Hollow Euler
rings and filled strong dots remain distinguishable at coincidence, and all
points lie inside the axes. This verifies the standalone plate, not its
latest-source full-page placement, EPUB downscaling or monochrome print.

Eight focused regressions now cover the four datasets, the full root
certificate, all Jacobi chains, first-use chi definition and the sampling
exception. Full suite **413 tests,zero skips** passes after the source/data
repairs; a subsequent bibliography-only edit adds the checked Bach reference.
Inventory was regenerated after all source edits. One duplicate examplex was
removed while its complete earlier example remains:97 examples now,144 keyed
exercises unchanged. Whole-source work through Chapter6 covers43 example
blocks and22 of39 mathematical figure datasets internally.

### C06 historical/source checks and boundaries

- Read [Bach's publisher-deposited Crossref record and abstract](https://api.crossref.org/works/10.1090/S0025-5718-1990-1023756-8):1990,volume55,355–380, and explicitly a witness at most2(logm)² under ERH. Direct AMS PDF access returned403. The
  [Miller author publication record](https://www.cs.cmu.edu/~glmiller/Publications/b2hd-Mi76.html)
  confirms1976 and the conditional deterministic test. Corrected the
  misattribution of the explicit constant2, and added Bach to further reading.
  Neither research proof is imported as a mathematical premise.
- The university-hosted [English diary selection](https://tildesites.geneseo.edu/~johannes/gdiary.pdf)
  was downloaded and its first scanned page inspected. The April8 entry uses
  different wording from a direct statement of reciprocity. This does not by
  itself certify the full Gray/diary attribution; the original Latin diary and
  exact commentary remain part of the open global history pass. The general
  April1796 chronology has supporting historical research, but no original
  scan signoff is claimed.
- Gauss portrait's caption names Jensen1840. Exact local-to-original portrait
  provenance, the complete editions/chapter bibliography and other incidental
  history (Euler/Fermat, Chernick, Eisenstein's sine proof) remain on the global
  pass rather than being certified from this source read.

Updated the odd-prime kernel qualification in the prime-power square-count
idea, explicit integer domains and the prime hypothesis of Eisenstein's lemma.
The Chapter5 finite-field teaser now names the shared polynomial root bound:
actual Volume3 uses finite abelian classification plus that bound, rather than
repeating the exact-order proof. No future theorem is used here.

## C07 — Sums of squares, DEP-067

Read the complete chapter, all eight prompt/hint/idea/writeup groups and
bibliography. Its five named results and eight keyed proofs retain their
separate mathematical records. This pass checks the surrounding arguments,
six examples and three complete figures. No chapter approval is claimed.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C07-U01: opening examples and exact criterion | Direct1²+45²=2026; squares mod4 are0,1, whose pair sums omit3, excluding2027. The full criterion examines the parity of exponents of primes3mod4. | Independently factor a represented integer: for q3mod4, a nonzero coordinate modq would give a root of−1; hence both coordinates are divisible by q and their sum has a factor q². Removing it repeatedly forces an even exponent. The epigraph now specifies that parity rather than suggesting prime congruence classes alone suffice.45 and75 have the same prime factors but different outcomes. | VERIFIED_TWICE |
| C07-U02: two-square product and recipe | Expand (ac−bd)²+(ad+bc)²; the two cross terms cancel and the four remaining terms form (a²+b²)(c²+d²). This proves closure and constructs representations from prime factors. | Independently use complex multiplication and conjugation: N(zw)=zw·conj(z)conj(w)=N(z)N(w), with coefficients matching the displayed identity. At65 both sign choices give4²+7² and8²+1²; at85 the new box gives7²+6² and9²+2², independently checked by full finite enumeration. | VERIFIED_TWICE |
| C07-U03: why small modular coordinates suffice | The Thue grid contains more pairs than residue classes. Collision differences have both absolute values≤floor√p<√p; a zero difference forces both zero, contradicting distinct pairs. A root of−1 then gives a positive multiple of p strictly below2p, forcing p itself. | Independently put0,a,…,ma on a residue circle, m=floor√p. These m+1 distinct residues have a positive circular gap≤p/(m+1)<√p; the corresponding difference of indices has absolute value in1..m and gives the same nonzero small congruence. Includes p2. The formal lemma/theorem have their separate prior entries; this checks the explanatory bridge. | VERIFIED_TWICE |
| C07-U04: representation preview and uniqueness boundary | For positive n, define r2 by all signed ordered integer pairs. The divisor formula is explicitly a preview of Chapter10 and never a premise here. Direct enumeration gives12 pairs at25 and16 at65 without using it. | Read actual Chapter10 thm:r2 and its Gaussian factor-count proof, whose domain is n≥1. For a represented odd prime, its count8 plus nonzero unequal coordinates gives one representation up to signs/order; this is now explicitly deferred to that proof rather than asserted as established here. The new85 box replaces a repeated65 calculation, retaining the earlier complete65 construction and its figure. | VERIFIED_TWICE for preview accuracy; no future proof imported |
| C07-U05: four-square identity and seed | In the displayed four bilinear forms, every mixed a_i a_j term cancels and every a_i² coefficient is sum b_j². Hence norm products are preserved. The two half-size residue sets x² and−1−y² have total size p+1, forcing a common class and a positive mp<p². | Independent formal monomial coefficient collection leaves exactly the16 terms a_i² b_j², each with coefficient1; no mixed term remains. Distinctness of each residue set follows from the already proved two-root count on the half-range. Cases p2,integer1 and zero are supplied explicitly in source. | VERIFIED_TWICE |
| C07-U06: multiplier descent and numerical run | Choose least positive m<p with mp=sum x_i². Even m permits same-parity pairs and halves m. For odd m>1, nearest residues yield sum y_i²=mr with0<r<m. Each bilinear coordinate is divisible by m; dividing all four by m produces rp. | Independently trace norm sizes: (mp)(mr)/m²=pr, so the squared norm loses m², not m. If all nearest residues were0, m² would divide mp, forcing m|p contrary to1<m<p. At p7,m3, x=(4,2,1,0),y=(1,−1,1,0) give z=(3,−6,3,3) and root tuple(1,−2,1,1), norm7. Thus the example exhibits an actual strict descent. | VERIFIED_TWICE |
| C07-U07: three-square obstruction and optional equivalence | Square residues0,1,4 cannot sum to7 mod8. If three squares sum to0 mod4, all three are even; remove factors4 until the forbidden remainder is exposed. The converse classification remains explicitly outside this chapter's proofs. | Direct finite triples through30 omit exactly7,15,23,28. The old question asking for their common remainder mod8 was misleading because28 is4 mod8. Revised it to remove every factor4 first, giving remainder7 for all four. The earlier ex:eureka equivalence uses8T_k+1=(2k+1)² and checks all odd squares; it does not claim universal existence. Actual Volume13 thm:threesq uses rational Hasse–Minkowski followed by the stated integer descent. | VERIFIED_TWICE |
| C07-U08: disc sandwich and average | Half-open squares based at each counted point are disjoint and have total area N(R). Their union lies in radius R+√2 and covers radius max(0,R−√2) by taking floors. Expanding areas gives the stated absolute bound, with the negative lower bound automatic at1≤R<√2. | Independently centre a unit square at each lattice point; rounding coordinates bounds displacement by√2/2 and gives the stronger bound√2·pi·R+pi/2 for R≥1. The origin contributes1, so sum_{1≤n≤X}r2(n)=N(√X)−1=pi·X+O(√X); division by X proves the claimed mean, without pointwise monotonicity or a constant error sign. | VERIFIED_TWICE |
| C07-U09: obstruction versus classification workshop | Two squares cannot sum to3 mod4, but21=3·7 is1 mod4 and still impossible by the proved prime-exponent criterion. The earlier45=3²·5 passes and75=3·5² fails. | Independent direct search for coordinates up to the relevant square roots gives the same decisions; product construction explicitly represents45. This shows a missing modular obstruction is not a sufficiency proof and requires no later representation formula. | VERIFIED_TWICE |
| C07-U10: research benchmark and later interpretation | The elementary O(R) bound is local; sharper exponents are clearly outside its proof. Replaced the unsupported517/824 claim by Huxley's published2003 exponent131/208, approximately0.6298, as a historical benchmark. | The cited Bourgain/Watt arXiv record explicitly says withdrawn in July2023 and that the affected claims lose theorem status. Huxley's publisher abstract independently states131/208 with a logarithmic factor; absorbing any fixed log power into R^epsilon gives the displayed form for fixed positive epsilon. No research theorem is needed by this chapter. | VERIFIED_TWICE for source status and preview, not independent reconstruction of Huxley's deep theorem |

### C07 examples and complete diagram data

| ID | Independent reconstruction and separate check | Status |
| --- | --- | --- |
| C07-E01: integers through20 | Enumerate a²+b² with a,b≤4 for values≤20 to get1,2,4,5,8,9,10,13,16,17,18,20. Independently check prime-exponent parity;18=3²+3² and12 contains an odd3 exponent. | VERIFIED_TWICE internally |
| C07-E02: new85 construction |5·17=(1²+2²)(1²+4²) gives (−7)²+6² or9²+2². Independent direct enumeration has unordered nonnegative pairs exactly(6,7),(2,9). The former65 box was a duplicate; its full earlier argument and four-point picture remain. | VERIFIED_TWICE internally for the new obligation |
| C07-E03:7 needs four | The complete mod8 triple-residue set omits7. Independently a parity split gives either three odd squares summing3 mod8, one odd plus even squares summing1 or5, or an even sum. Direct2²+1+1+1 gives four. | VERIFIED_TWICE internally |
| C07-E04: product15 |3=1²+1²+1²+0² and5=2²+1²+0²+0². The displayed identity gives coordinates(3,−1,−2,−1), a permutation/sign variant of the printed(3,2,1,1), whose norm15 is checked directly. | VERIFIED_TWICE internally |
| C07-E05: disc2 | Origin plus four axis points of norm1, four diagonal points of norm2 and four axis points of norm4 gives13. Independent floor-column sum gives sum_{x=−2}^2(2floor√(4−x²)+1)=13;4pi≈12.57 and the stated coarse bound≈24.05. | VERIFIED_TWICE internally |
| C07-E06: sticking-out square | Points near(3,1) in the square based at(2,0) have radius approaching√10>3 and lie outside radius2. Independently take(2.9,0.9), which is inside that half-open square and has squared radius9.22>9. Thus the larger covering disc is necessary for this corner convention. | VERIFIED_TWICE internally |
| C07-F01: circle65 | Every actual marked coordinate and its text label matches the four positive solutions(1,8),(4,7),(7,4),(8,1). Their16 signed reflections exhaust the integer solutions; the arc radius8.062258 squares to65 within1e−5. | VERIFIED_TWICE data; standalone rendered/inspected; full-page pending |
| C07-F02: representability30 | Parse all30 actual classification bits and compare with direct square sums; independently prime-exponent parity agrees. Actual rendered row-major positions were inspected. Enlarged cells from0.48/0.48cm to0.75/0.60cm and tiny labels to small for a more legible native-size plate. | VERIFIED_TWICE data; revised standalone rendered/inspected; full-page pending |
| C07-F03: disc6 | Parse all113 unit-square anchors and all113 point centres; both sets equal every integer pair with norm≤36. Independent column counting gives113. All corners are within6+√2, grid probes of the inner disc land in included floor-squares, and all three drawn radii match6,6±√2 to drawing precision. | VERIFIED_TWICE data; standalone rendered/inspected; full-page pending |

All three plates were built using the real XeLaTeX wrapper and shared palette
and visually inspected. Revised representability plate is150.96×91.03pt,
compared with105.65×74.49pt before; native label size increased, rather than
relying on later scaling. Circle65 is163.39×165.25pt and disc6 is212.65×210.56pt.
No clipping or mismatched labels observed in standalone renders. Full-page
placement, monochrome print and actual EPUB/reader downscaling remain pending.

Seven new source/data/numeric regressions pass; the complete suite has
**420 tests,zero skips**. Later final prose-only refinements clarify the beauty
preview and fixed positive epsilon; inventory is regenerated afterward.
Example count remains97, exercises144, mathematical figures39. Through
Chapter7 the whole-source record covers49 examples and25 figure datasets
internally. No future theorem is used as a proof premise here.

### C07 historical/source checks and boundaries

- [The actual cited arXiv record](https://arxiv.org/abs/1709.04340)
  states withdrawal on16July2023 and identifies faults in the propositions
  underlying the theorems. Its status invalidates the manuscript's use of the
  preprint as evidence for a proved bound; describing it as dated was
  insufficient. Removed both that bound and its bibliography entry.
- [Huxley's publisher abstract](https://academic.oup.com/plms/article-abstract/87/3/591/1452590)
  confirms2003,volume87,591–609 and exponent131/208. The independent
  [Cambridge journal record](https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/exponential-sums-and-lattice-points-iii/7B28024FEB1C199035C5C7D7F6783072)
  corroborates it. This is explicitly a historical benchmark, not a new
  current-record claim or a certification of the full research proof.
- Read the actual one-sentence argument and metadata in
  [Zagier's own hosted paper](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2323918/fulltext.pdf):
  Monthly97(1990),144. Its involution agrees with the chapter's expanded
  proof, whose domain/boundaries/positivity are separately checked.
- The [Euler Archive's E228 record](https://scholarlycommons.pacific.edu/euler-works/228/)
  distinguishes written1749 from published1758. The historical research by
  [Euler Archive researchers Klyve and Tou](https://digitalcommons.cwu.edu/math/61/)
  explicitly supports the Fermat1640/Euler1749 chronology. These do not alone
  certify the exact Christmas-day letter or every historical priority claim;
  complete edition/original-document review remains open.
- Actual included Volume13 thm:threesq and its proof were read: rational local
  conditions are followed by an Aubry/Davenport–Cassels integer descent.
  Corrected the overbroad claim about what methods the converse needs.
  Actual Chapter10 thm:r2 and factor-count proof were read before retaining
  its preview and deferring prime uniqueness. Preview accuracy does not
  import either theorem as a prerequisite or certify another volume.

Full bibliography/history, exact Fermat portrait provenance, final-page and
all-format proof and independent editorial/author acceptance remain open.

## C08 — Diophantine equations (source ch09), DEP-068

Read all Chapter8, all eight prompt/hint/idea/writeup groups and bibliography.
The five named results and eight keyed proofs keep their separate records,
with the changed IMO explanation independently reopened here. This complete
source pass checks15 example blocks and all three figure datasets. No chapter
acceptance is claimed.

| ID and source | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C08-U01: domains, obstructions and valuation identity | Squares mod4 omit3 as a two-square sum, and squares mod3 omit2, excluding the stated equations over every integer. For nonzero integer coefficients/variables in Ax^k=By^k, additivity of valuations gives the displayed k-divisibility constraint. | Independently use prime exponents after clearing rational denominators; C01's representation-independent rational valuation justifies the rational extension. At x²=12y² the3-exponents have opposite parity; x²=9y² factors into (x−3y)(x+3y)=0 and has exactly the two signed families. Added integer domains and qualified the epigraph's fourth-power impossibility to positive integers: (0,1,1) disproves an unrestricted claim. | VERIFIED_TWICE |
| C08-U02: finite factor search | x²−y²=45 with integer x>y≥0 is equivalent to positive factor pairs u≤v of45 of the same parity. The three pairs give(23,22),(9,6),(7,2). The inverse formulas prove completeness. | Independently enumerate the finitely bounded divisor pairs and recover x,y, checking all three original equalities. For12 only the even pair2,6 works; for2 the sole positive pair1,2 has opposite parity. Coprimality is explicitly not inferred from the factorisation. | VERIFIED_TWICE |
| C08-U03: Pythagorean parameters and restrictions | Removing the common gcd gives primitive positive triples; mod4 forces one even leg. The coprime positive half-sum factors of (y/2)² are squares, yielding m,n. The inverse gives their uniqueness with the odd leg selected. | Independently use rational unit-circle slopes and normalize a reduced pair m,n: opposite parity gives no factor2, and an odd common prime of m²±n² would divide both m,n. Cases m3,n1 and a common factor d show exactly how the restrictions fail. The five primitive triples with z<30 correspond to(2,1),(3,2),(4,1),(4,3),(5,2). Formal proof separately registered. | VERIFIED_TWICE |
| C08-U04: inradius formula and scaling | Joining the incentre to vertices splits a triangle into three triangles of common height r, giving area=r·semiperimeter. For a right triangle r=xy/(x+y+z)=(x+y−z)/2 by Pythagoras; substituting gives n(m−n). | Independently place legs on the axes: an incircle of radius r has centre(r,r); its distance to line yX+xY=xy is r exactly when r(x+y+z)=xy. Overall scale k multiplies every length, including r. At3,4,5 both routes give1. Added the area decomposition before invoking the quotient. | VERIFIED_TWICE |
| C08-U05: Fermat's stable family and hypotheses | Minimal positive z removes any common prime of x,y. Two Pythagorean parametrisations give n=2ab,m=a²+b² and (y/2)²=mab with pairwise coprime factors. Thus a=u²,b=v²,m=w² and n=2u²v², producing u^4+v^4=w² with w<z. | Independently trace each prime through the three coprime factors, so its exponent is even in the one factor it divides. All new u,v,w are positive, and w≤w²=m≤m²<z. Corrected a contradictory numerical-example sentence saying m and n would both be squares: n is twice a square. At(3,4,5),m2 already fails. The fourth-power RHS is excluded as a special square, not preserved by the descent itself. | VERIFIED_TWICE |
| C08-U06: replacement complete7-descent | If x²+y²=7z² and z≠0, choose least positive abs(z). The mod7 square set0,1,2,4 can sum to0 only as0+0. Thus7 divides x,y; substitution forces7|z. Dividing all three by7 gives an integer solution with measure abs(z)/7, a contradiction. If z0, all entries are0. | Independently apply the proved two-square criterion to7z²>0: the exponent1+2v7(z) of the3mod4 prime7 is odd, impossible for a two-square sum. The new example replaces a repeated fourth-power special case and an overbroad statement that a Pythagorean parametrisation cannot descend. No exercise changed; the full earlier Fermat corollary remains. | VERIFIED_TWICE for the new obligation |
| C08-U07: conic line restriction and unit-circle charts | For Q rational quadratic without a rational line factor, restriction to a rational line through a known root is a nonzero s(alpha·s+beta). A distinct second affine point, if present, has rational parameter; tangent/degree-drop and vertical cases are separate. | Independently divide Q as a polynomial in y by the monic rational line; zero restriction would force that line as a factor, excluding the degenerate counterexample xy0. On the unit circle, substitution gives both exact charts at−1 and+1. The latter has y=−2t/(1+t²), with fixed sign, not an unspecified sign convention. Added the factorisation, t2 point(3/5,−4/5), and retained starting/vertical exceptions. | VERIFIED_TWICE |
| C08-U08: rational nonexistence and preview boundary | A rational point on x²+y²=3 clears denominators to a primitive nonzero X²+Y²=3Z². If Z is odd, mod4 is impossible; if Z is even, both X,Y are even, contradicting primitiveness. | Independently the exercise's mod3 argument forces all three divisible by3. The duplicated earlier assertion that cited the not-yet-proved exercise was removed; this full local example and later exercise remain. Removed its inaccurate later-chapter proof location and overbroad conic/cubic theorem summary. The chord-method limitation is explained by degree: one known cubic root leaves a quadratic, not automatically rational roots. | VERIFIED_TWICE |
| C08-U09: Mordell shift and negative inputs | Even x makes x³+7 equal7 mod8. Odd x gives y²+1=(x+2)((x−1)²+3); the second factor is positive and3 mod4, so it has a prime q3mod4 dividing y²+1, impossible for a root of−1. | Independently use the earlier sum-of-two-squares divisibility fact: q dividing y²+1² must divide both coordinates, including1. No coprimality between the factors is needed; the positive quadratic factor exists even for negative x. Checked all four signed small examples. The separate y²=x³−2 classification remains explicitly a later exercise, not a premise. | VERIFIED_TWICE |
| C08-U10: Markov jumps, exact examples and tree | Replacing a coordinate x by3yz−x preserves the quadratic relation and is a positive integer because xx'=y²+z². After sorting x≥y≥z, g(y)≤0 locates the mate below y; equality reduces to(2,1,1)→(1,1,1). Thus the sum strictly decreases and all moves reverse. | Independently expand the new equation and check norm difference x'^2−x²=3yz(x'−x). Every nonroot largest coordinate is unique (a tie would force the treated equality case), giving a unique smaller sorted parent. The actual nine tree nodes/edges match four full breadth levels. Exact jumps(1,2,5)↔(29,2,5) and(1,5,13)↔(1,13,34) show why replacing the smallest can grow. Corrected numbers-form-a-tree wording to triples with numbers as coordinates. | VERIFIED_TWICE |
| C08-U11: IMO integer-root sign explanation | For fixed positive nonsquare k, k≥2. The exact Vieta mate is an integer; f(b)=(2−k)b²−k<0 and f(−1)=b²+1+k(b−1)>0 locate it in(−1,b), hence0≤a'<b. Zero would force k=b²; otherwise the positive sum decreases. | Independently, if an integer a'=−h≤−1, then f(−h)=h²+b²+k(bh−1)>0 for every positive k,b,h. Thus the existing second hint was valid without an upper bound on k. Removed the source's false description that this argument was invalid without such a bound; the correct root-location proof is retained and rechecked. | VERIFIED_TWICE after explanatory correction |

### C08 examples and complete diagram data

| ID | Independent reconstruction and separate check | Status |
| --- | --- | --- |
| C08-E01: partial modulus | x²+x+1 at0,1,2,3 mod4 is1,3,3,1, so exactly two x classes are excluded. Independently factor (2y−2x−1)(2y+2x+1)=3 for actual solutions; x0,−1 and y±1 meet the surviving classes. | VERIFIED_TWICE internally |
| C08-E02: full modulus | Mod3 excludes y²=3x²+2 outright; independent valuation would require a square congruent to2, contradicted by the full residue set0,1. No assertion of sufficiency from surviving tests. | VERIFIED_TWICE internally |
| C08-E03: two triples | Parameters2,1 and4,1 give3,4,5 and15,8,17. Direct norm equalities and gcd calculations independently verify both; inverse half-sums recover the parameter squares. | VERIFIED_TWICE internally |
| C08-E04: rejected pair |3,1 gives8,6,10 with gcd2, whose primitive version is4,3,5. Independent parity inspection finds both parameters odd, exactly the excluded case. | VERIFIED_TWICE internally |
| C08-E05: hypothetical first step | The complete formal Fermat argument in U05 proves its conditional claims, including n=2u²v² and a smaller positive square-RHS solution. Independent prime-exponent accounting verifies the factors, rather than searching for an impossible numerical input. | VERIFIED_TWICE internally |
| C08-E06: replacement7-descent | The least-positive-abs(z) construction and the independent odd7-valuation contradiction are in U06. Every new coordinate is integral and the measure strictly decreases; the zero case is explicit. | VERIFIED_TWICE internally for the new obligation |
| C08-E07: unit circle at−1 | Directly factor (x+1)((x−1)+t²(x+1)). The second root gives((1−t²)/(1+t²),2t/(1+t²)); its squared norm is1 and slope is exactly t. Conversely t=y/(x+1) recovers every point except the separately retained base. | VERIFIED_TWICE internally |
| C08-E08: unit circle at+1 | Factor (x−1)((x+1)+t²(x−1)); the exact second point is((t²−1)/(t²+1),−2t/(t²+1)). Its norm and chosen slope are independently checked. At t2, coordinates are3/5,−4/5, yielding the3,4,5 side lengths after signs. | VERIFIED_TWICE internally after expansion |
| C08-E09: no rational point | The mod4 primitive-denominator contradiction and the independent mod3 common-factor proof both exclude the rational circle, as in U08. It has real points, e.g.(√3,0). | VERIFIED_TWICE internally |
| C08-E10: Mordell small x | x1,2,−1,−2 give8,15,6,−1 respectively, none an integer square. Independent exact shift identities yield the all-input obstruction in U09; the samples are not offered as its proof. | VERIFIED_TWICE internally |
| C08-E11: shift | x=2k+1 gives x+2=2k+3 and x²−2x+4=4k²+3, a positive3mod4 factor. Independent modular expansion and the q|y²+1 impossibility agree. | VERIFIED_TWICE internally |
| C08-E12: smallest Markov |1,1,1 has both sides3; t²−3t+2 has roots1,2, and2,1,1 has both sides6. Direct factorisation(t−1)(t−2) independently verifies the swap. | VERIFIED_TWICE internally |
| C08-E13: growing versus shrinking |2,1,1 jumps in its largest entry to1,1,1. From5,2,1, the smallest entry instead becomes29, preserving sum of squares870=3·5·2·29. Independent Vieta root product and direct substitution agree. | VERIFIED_TWICE internally |
| C08-E14: a noncounterexample |3,4,5 has parameters2,1 but does not have two square legs. The added exact qualification says m must be square and n twice square. Independent norm/prime exponents show m2 already fails, so this triple is not a Fermat-descent input. | VERIFIED_TWICE internally after correction |
| C08-E15: smaller hypothetical solution | Reconstruct the second parametrisation n=2ab,m=a²+b² and the three coprime square factors; it yields u^4+v^4=w² with w<z. Independent reduction of the prime-exponent constraints gives the same family, not a fourth-power RHS. | VERIFIED_TWICE internally |
| C08-F01: incircle | Actual centre1,1 and radius1 meet axes at1,0 and0,1. The third actual contact8/5,9/5 has squared displacement1, lies on3X+4Y=12, and its radius is perpendicular to direction−4,3. Triangle labels3,4,5, area6 and semiperimeter6 independently agree. | VERIFIED_TWICE data; standalone rendered/inspected; full-page pending |
| C08-F02: descent flow | Both actual directed edges go top→parameters→new solution; labels retain positive original solution, m>n>0 and0<z1<z. Full symbolic reconstruction U05 verifies that the abbreviated flow has no false edge. Enlarged its labels to small. | VERIFIED_TWICE data/math; revised standalone inspected; full-page pending |
| C08-F03: chord/Markov plate | All four exact t/point labels have squared norm1 and slope t; every rounded endpoint matches within0.00005. All nine Markov node triples satisfy the equation; all eight actual edges are reversible valid jumps to larger sums, including the chained root edges. Independent breadth generation through four levels gives exactly those nodes. | VERIFIED_TWICE data; revised standalone inspected; full-page pending |

The former combined chord/Markov plate was458.29pt wide, requiring reduced
labels in the reading PDF. Stacked its two scopes and increased label size;
new standalone output is224.33×333.81pt, within the actual book linewidth.
The source caption now says top/bottom and gives rational points explicitly
before identifying the scaled integer triples. No dataset, node, edge or
figure obligation was removed. The descent flow is205.38×133.28pt; the
incircle is153.14×120.08pt. All were built with the real XeLaTeX wrapper and
visually inspected. Whole-page float placement, EPUB/reader scaling and
monochrome print remain pending.

Seven focused geometry/source/numeric tests pass. Full suite **427 tests,
zero skips** passes. Complete inventory/check mode is current:1361 items,
97 examples,39 figure sources,3 portraits. Through Chapter8 the whole-source
record covers64 examples and28 mathematical figure datasets internally.
No full chapter acceptance or external review is claimed.

### C08 historical/source checks and boundaries

- The [actual official1988 problem paper](https://www.imo-official.org/assets/documents/problems/1988/1988_eng.pdf),
  Problem6 on its second page, exactly matches the positive-integer quotient
  challenge. The obsolete guessed/aspx PDF routes returned404; the live
  official problems page supplies the actual asset link. The corrected
  mathematical proof and hint have separate internal reconstructions.
- [Annals141(1995),issue3](https://annals.math.princeton.edu/1995/141-3)
  contains Wiles's paper and the Taylor–Wiles companion, supporting the
  publication-year attribution. Full research-proof certification is neither
  claimed nor used as a premise.
- The current Markov status was checked against the2025
  [Fisac publisher record](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70178)
  and [Tan/Zhang's31October2026 preprint record](https://arxiv.org/abs/2611.01007).
  The former explicitly calls the general statement open; the latter reports
  finite computational verification, not an unconditional proof for all
  triples. The raw run and preprint proof are not certified or imported, and
  their numerical record is not added to the book.

Full bibliography editions, Markov1879/Frobenius1913 original attribution,
Matiyasevich history, the exact whole-book future handoffs and final formats
remain open for the global pass. The standard named proofs retain their
separate earlier audit entries, not historical certification by association.


## C09 — Continued fractions (source ch08), DEP-069

Read the complete source, all eight prompt/hint/idea/writeup groups and
bibliography; read and rendered all four figure sources. Seven named results
and eight keyed proofs retain their separate records. This pass covers all12
example environments, including both formal examples, without adding to the
72/144 proof totals. Through Chapter9:76 of97 examples and32 of39 datasets
have internal whole-source records; acceptance remains open.

| ID | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C09-U01: canonical finite expansion and signs | Every inner canonical tail exceeds1 when the last entry is at least2. Floors and reciprocals recover each successive integer entry and the stopping point, proving uniqueness. | Matrix products [[a,1],[1,0]] have determinant−1; their columns give the exact numerator/denominator recurrences and coprimality. Negative initial entries use floor, not truncation. Fresh workshop −43/19=[−3;1,2,1,4] has final determinant1 and gap1/76; direct fractions independently recover it. Earlier positive worked examples remain. | VERIFIED_TWICE internally |
| C09-U02: rationality and prior-volume proofs | Unequal a/b,p/q differ by at least1/(abs(b)q). Infinitely many distinct fractions with error below1/q² therefore imply irrationality; a finite decimal experiment does not. | Read the actual Volume1 factorial-tail proof of e and integer-derivative/integral proof of pi, with proof locations in the updated prerequisite crosswalk. Replaced the misleading numerical claim with these genuine proof sites. Both earlier arguments supply strict positive upper bounds tending to0 for a supposed positive integer. | VERIFIED_TWICE internally |
| C09-U03: best approximation metric | The chapter's lemma compares abs(qx−p), not just abs(x−p/q). The nearest-integer search at each bounded denominator is complete. | Independently enumerate pi denominators through100:22/7 wins through7 (and10);311/99 improves absolute error through100 but has larger scaled miss. Its intermediate-convergent form (14·22+3)/(14·7+1) explains why the two metrics differ. The Legendre test for22/7 is sufficient, not necessary. | VERIFIED_TWICE internally |
| C09-U04: two/three-convergent outlook | Put alpha=x[n+1]>1,beta=q[n−1]/q[n] in(0,1],a=floor(alpha),S=alpha+beta. Exact tail algebra gives the three consecutive scaled errors alpha·beta/S,1/S,(a+beta)(alpha−a)/S. For S>2 the middle is below1/2; otherwise alpha·beta≤S−1 with the needed strictness, giving a neighbouring error below1/2. | For S>sqrt5 the middle wins. For S≤sqrt5,a≥2 gives beta≤sqrt5−2<1/sqrt5, so the preceding wins. For a1 the minimum of alpha·beta and (alpha−1)(beta+1) is at most(S²−1)/4: the two products balance at alpha−beta1, and on either side the smaller decreases. Dividing by S gives at most1/sqrt5, with equality requiring irrational beta=(sqrt5−1)/2, impossible. Thus any three contain a strict winner. Blocks give infinitely many winners; the separately proved golden limit establishes optimality. This reconstructs the quoted mathematical outlook without importing it into Pell's proof. | VERIFIED_TWICE internally; historical original-proof certification separate |
| C09-U05: periodic field argument | A quadratic irrational y generates a two-dimensional rational vector space closed under products; a nonzero inverse is its conjugate divided by a nonzero rational norm. A periodic tail satisfies a quadratic via a unimodular fractional transformation. | Independently transform the original quadratic and retain its discriminant; the approximation bound makes A[n] bounded, C[n]=A[n−1], hence B[n] bounded. Finitely many integer coefficient triples give finitely many complete quotients, and determinism gives periodicity. Initial denominator coincidences and nonzero leading coefficients were checked; this is not a finite-sample proof of Lagrange. Named proof has its separate entry. | VERIFIED_TWICE internally |
| C09-U06: ring/units and full-ring counterexample | Defined Z[sqrt(d)], its multiplicative closure and unit before first use. Integer-valued multiplicative norms show a unit has norm±1; conversely conjugation supplies an inverse when norm±1. Norm1 positive units of this ring are the Pell powers. | In the larger d5 ring, phi solves a monic integer polynomial and phi inverse=phi−1. Phi²=(3+sqrt5)/2 still has half-integer coordinates, whereas phi^6=9+4sqrt5 is the least positive Pell solution (test y1,2,3,4). This disproves the old claim that the Pell generator is always the full-ring fundamental unit or its square. Actual Volume13 units chapter's d5 example and Pell61 sixth-power example corroborate the distinction. Source now states the exact smaller-ring conclusion. | VERIFIED_TWICE internally after correction |
| C09-U07: complete Pell search | A positive solution has gcd(x,y)1 and 0<x/y−sqrt(d)=1/[y²(x/y+sqrt(d))]<1/(2y²). Legendre forces every solution to be a convergent. Denominators increase after the possible q0=q1=1 tie; the initial floor(sqrt(d))/1 has negative norm. Thus the first norm1 candidate is fundamental. | Independently generate exact integer continued fractions and the first three Pell powers for d2,3,5,7,61; every power occurs among the candidates. For d61 the period is11, norm−1 occurs at index10 (29718,3805), norm1 at index21 (1766319049,226153980). The general bound, not the samples, proves completeness; the existence theorem guarantees termination. Replaced unsupported finds-at-once rhetoric by first22 convergents. | VERIFIED_TWICE internally after filling the gap |
| C09-U08: powers and minimum | Multiplicative norm and conjugate inverse preserve integral coordinates. Minimal positive y gives minimal unit epsilon>1, and epsilon^k≤u<epsilon^(k+1) forces u·epsilon^(−k)=1. | Independently express x=(u+1/u)/2,y=(u−1/u)/(2sqrt(d)); both are positive for u>1, and both increase with u. The well ordering is in positive integer y, not arbitrary real units. Signs/conjugation cover the remaining solutions. This reconstructs the surrounding claims without assuming periodicity proves existence. | VERIFIED_TWICE internally |
| C09-U09: model, domains and limits | The fixed rational year fraction24219/100000 has finite CF [0;4,7,1,3,24,6,2,2]; first nonzero convergents are1/4,7/29,8/33,31/128,752/3105. Exact31/128 error is1/400000. | Independent Euclidean divisions/cross-products verify the finite model. Removed the epigraph's false historical causality about actual leap years. Integer n≥1 and triangular index m≥0 are now explicit. Golden-ratio solution points to the actual earlier ex:cfunique, not the preceding square-triangle exercise. No physical long-term astronomical prediction is claimed. | VERIFIED_TWICE internally |

### C09 complete examples and figures

| ID | Reconstruction and independent check | Status |
| --- | --- | --- |
| C09-E01:415/93 | Euclid quotients4,2,6,7 give convergents4/1,9/2,58/13,415/93; direct evaluation and both cross determinants agree. | VERIFIED_TWICE internally |
| C09-E02: short fraction | [1;2,2]=7/5; recurrence gives1/1,3/2,7/5 and determinants−1,+1. Direct nested fractions independently agree. | VERIFIED_TWICE internally |
| C09-E03: sqrt2 order | All five fractions meet the displayed order by cross multiplication; comparing numerator² with2·denominator² independently establishes the below/above signs. | VERIFIED_TWICE internally |
| C09-E04:13/5 | Exact floor/reciprocal steps give[2;1,1,2]; reverse evaluation13/5 and integer Euclid independently agree. | VERIFIED_TWICE internally |
| C09-E05: pi denominators | Nearest-integer enumeration for every q1…7 proves the absolute-error comparison; separate scaled misses distinguish the theorem's metric. | VERIFIED_TWICE internally |
| C09-E06: Legendre on22/7 | Certified rational pi bounds put the error near.00126449, strictly below1/98; exact CF digits independently contain22/7. | VERIFIED_TWICE internally |
| C09-E07: formal sqrt2 periodic | Rationalising the reciprocal gives1+sqrt2, so every subsequent digit2. Exact norm recurrence alternates±1 for the convergents. | VERIFIED_TWICE internally |
| C09-E08: sqrt3 | Integer complete-quotient recursion gives period1,2 after initial1; exact convergents1/1,2/1,5/3,7/4,19/11 have the displayed norm at2/1. | VERIFIED_TWICE internally |
| C09-E09: pure golden period | Phi=1+1/phi and positive root of X²−X−1 gives all ones. Independent Fibonacci recurrence gives its convergents and limit. Sqrt3's initial1 is separate from its repeating1,2. | VERIFIED_TWICE internally |
| C09-E10: formal Pell61 | Exact period and indices are U07; independent squaring gives1766319049²−61·226153980²=1. The earlier norm−1 pair squares to this solution. | VERIFIED_TWICE internally |
| C09-E11: Pell2 | y1 gives3 nonsquare,y2 gives9; direct multiplication (3+2sqrt2)²=17+12sqrt2 and both norms1 verify the first powers. | VERIFIED_TWICE internally |
| C09-E12: negative norm | Norm(1+sqrt2)=−1; its square is3+2sqrt2 of norm1. Exact first two CF pairs agree, and the example explicitly excludes negative norm from Pell1. | VERIFIED_TWICE internally |
| C09-F01: line | All five actual axis locations are exact expressions7/5,41/29,3/2,17/12,99/70; square comparisons independently certify fill/open signs. Preserved true positions while spreading text with leader lines; fixed overlapping labels and legend. | VERIFIED_TWICE data; revised standalone inspected |
| C09-F02: lattice errors | Actual filled(1,1),(5,7),open(2,3),gray(4,5),line endpoint(6.3,8.9095) and distance arrow all match. Independently compare squared coordinates and exact abs(4sqrt2−5); arrow leaves.04 clear at each end. | VERIFIED_TWICE data; standalone inspected |
| C09-F03: quality | Recomputed all40 plotted6-decimal values from fresh100-digit CF arithmetic. Separately certified them using exact rational enclosures: integer-square-root bounds for phi/sqrt2, factorial partial sum plus2/101! for e, Machin alternating arctangent80-term bounds for pi. Interval floor/reciprocal certifies all11 digits and every q²-error within5e−7. Phi's limit follows1/(phi+F[n]/F[n+1]); sqrt2's from1/(sqrt2+1+q[n−1]/q[n]); large next digit gives error<1/a[next]. | VERIFIED_TWICE data/math; standalone inspected |
| C09-F04: Pell hyperbola | Actual(1,0),(3,2),(17,12) satisfy x²−2y²1; independent norm multiplication gives the latter two. Corrected caption to the plotted portion x≥1,y≥0, rather than the entire right branch. | VERIFIED_TWICE data; standalone inspected |

All four actual XeLaTeX standalone plates were built and visually inspected.
Revised line plate is257.55×126.67pt; lattice176.75×168.87pt;
quality355.08×174.96pt; Pell149.03×101.75pt. The line's labels/legend are now
separate and readable. Eight new tests pass; full suite435 tests,zero skips
passed after mathematical/data changes. The final cattle bibliography-only
correction was followed by regenerated inventory/focused checks, not an
invented second full-suite run. Inventory remains1361 items/97 examples/39
figures/3 portraits. Final-source formats, all-page visual proof and external
review remain open.

### C09 targeted historical checks

- [Lenstra's revised MSRI2008 reprint](https://library.slmath.org/books/Book44/files/01lenstra.pdf),
  bibliography, distinguishes Lagrange's1768 submission and1773 publication;
  the older AMS2002 version had the earlier publication date. Retained1768
  as the theorem's work date and made the distinction explicit in the source.
- [Waldschmidt's2024 author presentation](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/BrahmaguptaFermatPellEn.pdf),
  pages2/10, gives Bhaskara II's Bijaganita1150 and the d61 solution. This is
  supporting historical research, not a claim to have read the Sanskrit source.
- Lenstra's revised account distinguishes Amthor's1880 solution, the1965
  Williams/German/Zarnke calculation and Nelson's1980/81 full decimal printout.
  Corrected the bibliography's false full-solution-first-printed-in1965 claim;
  now names Nelson, Journal of Recreational Mathematics13,162–176 for the
  full printout, without asserting a new unsupported priority.
- Hurwitz1891 metadata is corroborated; the original article was not accessible.
  The quoted sharper mathematics was reconstructed in U04. Full bibliography
  editions, original priority documents and global handoffs remain open.

### Immutable681b4b55 build and scoped page inspection

The exact pre-C09 snapshot681b4b55d570c15f2fc06bb2bf4faee164b8c559 in
`/workspace/Order-and-Chance-proof-dep068` completed all formats successfully:
329 print pages,0.7745-inch actual-page-derived spine,19,184,756-byte EPUB,
39 full-width1800-pixel plates and HTML reader. Layout/style/print/cover/EPUB/
reader checks passed;384 boxes,max371.3pt,no overflow or unresolved references.
Read-PDF physical pages167,194,217,218 (printed154,181,204,205) were rendered
and viewed: full-data liar plot, new85/four-square page, stacked chord/Markov
plate and conic charts fit without observed clipping/overlap. This is a scoped
sample covering Chapters1–8 edits, predating C09; it is not all-page approval.
Build log:`/tmp/pr103-volume2-build-681b4b55.log`.


## C10 — Gaussian and Eisenstein integers, DEP-070

Read the complete746-line source before edits, all eight prompt/hint/idea/
writeup groups and bibliography; all three figures' construction and every
plotted coordinate were checked. Nine named/eight keyed results retain their
separate entries. Whole-source coverage through Chapter10 is84/97 examples
and35/39 datasets internally, without chapter or global acceptance.

| ID | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C10-U01: rings, divisibility and first use | Each displayed quadratic relation reduces a product to two integer coordinates. Conjugation preserves those coordinates, and z·conj(z) gives the three positive integer norms. The complex subrings have no zero divisors, so cancellation holds independently of inverses. | Expand products in the coordinate basis and verify norm multiplication as an integer polynomial identity. The norm1 equations give4,6,2 units respectively. Added the ring meaning of divides; defined ramification at its first example, limited valuations to nonzero elements/associate classes and power extraction to integer k≥1 with nonzero inputs. Actual Volume1 conjugation/root-of-unity sites are in the crosswalk. | VERIFIED_TWICE internally |
| C10-U02: rounding estimates and example chains | Coordinate rounding bounds each residual coefficient by1/2. Gaussian square norm≤1/2, Eisenstein quadratic≤3/4 (maximum at box corners), sqrt−2 norm≤3/4, all strictly below1. The remainder norm is norm(b) times this quantity. | Independently use covering rectangles/rhombi with physical coordinates; Eisenstein coefficient rounding need not be nearest-point rounding. For sqrt−5 the bound3/2 fails but does not alone disprove Euclideanity. Every Gaussian division in11+3i,1+8i was directly multiplied back; norms65→20→5→0. Exact triangular quotient(13+9omega)/7 gives q2+omega,remainderomega and Bezout certificate1. | VERIFIED_TWICE internally |
| C10-U03: gcd/prime/power consequences | The least-norm nonzero combination divides all combinations because any nonzero remainder contradicts minimality. Bezout then proves irreducible⇒prime; induction on integer norm proves factor existence, and prime cancellation proves uniqueness. | Independently run remainder-chain extended Euclid and preserve both coefficient vectors. For the surrounding consequences, assign each irreducible's exponent in ab=unit·c^k; coprimality forces the entire exponent into one factor, so it is divisible by k. A coprime integer Bezout identity remains an identity in each larger ring. None uses unproved general ideal theory. Named proof has its separate entry. | VERIFIED_TWICE internally |
| C10-U04: exact failure and new example | Norms4,9,6 and the absence of norms2/3 prove the four factors irreducible; unit norm1 rules out cross-side associates.2 divides the product6 but not either half-coordinate factor, so it is not prime. | New example: a common nonunit divisor of2,1+sqrt−5 would have norm2 (dividing4 and6), impossible. Yet2u+(1+sqrt−5)v1 has no solution: coefficients give2a+c−5d1 and2b+c+d0, contradictory modulo2. The full16-case parity truth table independently corroborates the symbolic obstruction. This replaces the duplicate6 example and its false nothing-to-divide-by explanation, while retaining the full theorem/exercise. Actual Volume13 prop:six proof uses the same combination set in its ideal construction. | VERIFIED_TWICE internally for the new obligation |
| C10-U05: prime classification, symmetry and representation count | Norm of a Gaussian split factor is p; conjugates cannot be associates because their sum/difference would force p into both coordinates. Inert q would require impossible norm q. Every irreducible divides its ordinary norm, hence an ordinary prime and a listed factor. Eisenstein uses the primitive cube root mod p and the explicit norm−3 construction. | Independently determine every irreducible of norm≤225 by exact trial factors of norm≤sqrt(N)≤15, with coefficient bounds proved from the positive forms. Every point and ink matches classification; multiplying by all4/6 actual units gives exact rotational closure. Inert exponents must be even for a norm n; split exponents distribute in e+1 ways. Direct lattice counts give r2(15)0,r2(45)8,r2(65)16,r2(325)24, agreeing with the general exponent proof and the separate multiplicative divisor-sum argument. | VERIFIED_TWICE internally |
| C10-U06: cubic descent explanations | Lambda²=−3omega has valuation2 at3; integer divisibility by lambda forces divisibility by3 by norms. The three factors of alpha³+beta³ have valuations3n−2,1,1, and no common prime away from lambda. Cubes prime to lambda are±1 modlambda^4. | Independently expand in the integer omega basis; the three-factor linear relation has both coefficients0. The unit check permits eta±1 only; both are cubes and the new coprime/nonzero family has positive integer exponent n−1. The explanatory checklist therefore identifies the actual closed family and decreasing measure, rather than decreasing element size. Named proof's two independent reconstructions are separately recorded. | VERIFIED_TWICE internally |
| C10-U07: replacement workshop and previews | Fresh8+i=(2−i)(3+2i) has prime-norm5/13 factors; changing one conjugate gives4+7i with the same norm65. The four units cannot make these associates because their absolute coordinate pairs differ. | Direct products/norms and complete unit orbits independently verify this distinction: unique factorisation concerns an element, not its norm. Replaces repeated5/6 workshop proofs; earlier full proofs remain. Removed undefined ideal equations from the preview, explaining the combination-set idea instead. Removed overbroad cyclotomic/reciprocity history and corrected the alleged failure outside all three rings to the actual sqrt−5 example. Read Volume13's ideal product definitions/prop:six before retaining its future handoff. | VERIFIED_TWICE internally |

### C10 examples, complete figure data and rendering

| ID | Reconstruction and independent check | Status |
| --- | --- | --- |
| C10-E01: Gaussian norms |3+2i has norm13 prime;1+i has norm2 and−i(1+i)²2. Direct products and complete norm1-unit list agree. Ramification defined before further use. | VERIFIED_TWICE internally |
| C10-E02: exact division |(7+i)/(2+i)=3−i; independent product(2+i)(3−i)=7+i leaves zero remainder. | VERIFIED_TWICE internally |
| C10-E03: split5 |(1+2i)(1−2i)5; both norms5 and quotient(−3+4i)/5 not among the four units, so nonassociate. Independent unit orbit confirms. | VERIFIED_TWICE internally |
| C10-E04: replacement coprimality | Norm-divisor and coefficient-parity proofs in U04 give the full new example. Independent quotient-coordinate obstruction and parity truth table confirm the failure. The old full six-factor proof remains in thm:six/ex:zsqrt5. | VERIFIED_TWICE internally for new obligation |
| C10-E05:13 |(2+3i)(2−3i)13, both norms13; independent four-unit orbit excludes conjugate association. | VERIFIED_TWICE internally |
| C10-E06: inert7 | Norm7 impossible by mod4; independent exact trial-factor search of the element7 finds no nonunit divisor of norm≤7. Divisor sum4(1−1)0 agrees. | VERIFIED_TWICE internally |
| C10-E07:lambda |Norm(1−omega)3 and square−3omega by direct expansion. Independent squared geometric length3 agrees with the corrected figure. | VERIFIED_TWICE internally |
| C10-E08: split7/inert5 |(2−omega)(2−omega²)7, norm7; the signed formula is4−2(−1)+1=7. For norm5,4N=(2a−b)²+3b² excludes residue2 mod3. Independent exact trial factor search agrees;2+omega has norm3. | VERIFIED_TWICE internally |
| C10-F01: rounding | All nine actual grid dots, q1−i circle, exact quotient7/13−17i/13 and half-unit square agree with the divisions. Exact squared distance4/13<1; farthest cell-corner squared distance1/2. Moved q label out of the dashed cell edge. | VERIFIED_TWICE data; revised standalone inspected |
| C10-F02: complete prime discs | All184 Gaussian points (168 charcoal,12 rust,4 ochre) and300 Eisenstein points (276 charcoal,18 rust,6 ochre) match exact trial-factor enumeration. No omissions/duplicates, every norm≤225, every rounded Cartesian ordinate within.000501, exact unit-orbit symmetry. Reflowed legend into three larger-font rows; preserved all484 points and colours. | VERIFIED_TWICE data; revised standalone inspected |
| C10-F03: Eisenstein patch | All16 points are m+n·omega with m,n−1…2. Original dashed segment1→1+omega had squared length1, so could not represent lambda of norm3. Corrected to directed omega→1, vector1−omega of squared length3. Independent norm calculation and endpoint geometry agree. Shifted the unit triangle and enlarged labels to avoid overlap. | VERIFIED_TWICE data after correction; revised standalone inspected |

All three real XeLaTeX standalone outputs were rendered/viewed after final
changes: rounding168.94×158.58pt,prime discs309.23×212.45pt,
Eisenstein161.05×87.71pt. The revised legend and labels fit without observed
clipping/overlap. Final-source page placement, monochrome print and EPUB/reader
scaling remain open. Six focused tests pass; full-suite result is recorded in
the DEP-070 ledger. Inventory remains1361 items,97 examples,39 figures,
three portraits. No chapter or external signoff is inferred.

### C10 targeted sources and current-status correction

- [Cox's author page](https://dacox.people.amherst.edu/primes.html) explicitly
  confirms the2022 third edition with solutions, distinct from2013 second.
  Springer publisher records corroborate [Ireland/Rosen1990 second edition](https://link.springer.com/book/10.1007/978-1-4757-2103-4),
  Chapter9 cubic/biquadratic reciprocity, [Edwards1977](https://link.springer.com/book/9780387902302)
  and [Lemmermeyer2000](https://link.springer.com/book/10.1007/978-3-662-12893-0).
  Metadata is not certification of every cited section or historical priority.
- The old still-open Gaussian-moat statement is outdated against
  [MathWorld's30October2026 record](https://mathworld.wolfram.com/GaussianMoatProblem.html),
  citing a26September2026 proof. Downloaded/read the primary preprint's first
  two pages at fixed commit
  [adc7f124](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf):
  it states a uniform finite-component theorem including axis primes. The
  full29-page argument and reported formalisation have not been independently
  checked here. Removed the unsupported current-open assertion; bibliography
  now describes the1998 paper's historical question without adopting a new
  unverified theorem. Full original-history/bibliography remains open.


## C11 — Characters, Euler products and sieve, DEP-071

Read all1694 original lines, including all20 prompt/hint/idea/writeup groups,
bibliography and four figure constructions. Eleven named/20 keyed results
retain separate two-pass records. The complete chapter source passes now
cover96 of97 example environments (the last is in the field guide) and all39
mathematical figure datasets internally; these counts are not final approval.

| ID | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| C11-U01: homomorphisms and character values | Identity/inverse laws follow by cancellation in C×. A unit product is a unit, and a product with a nonunit factor remains a nonunit modulo m, so extending a unit-group homomorphism by zero preserves multiplication. Euler's theorem forces every nonzero value to be a root of unity. | Independently use the proved cyclic-product coordinates: choose roots on each generator, extend by integer exponent addition and check all residue classes. Mod1 has one unit and constant1 character. Added integer m domain; replaced unexplained dual-group language in the modulo5 example by the explicit chi[j]²=chi[2j] calculation. Full orthogonality named proofs remain separately recorded. | VERIFIED_TWICE internally |
| C11-U02: new modulo8 rows/detector | Rho=chi4 has period8, nonzero precisely on units, and remains completely multiplicative. The four distinct rows principal,rho,chi8,rho·chi8 exhaust phi8=4 characters; their values at5 are1,1,−1,−1. Orthogonality yields the displayed class5 detector. | Direct exhaustive evaluation on all eight residue classes, including every nonunit, gives numerator0,0,0,0,0,4,0,0. Replacing the principal term with constant1 falsely gives1/4 on evens. Independent multiplication tables prove the rows are characters and their inner product is0. These fresh examples/workshop replace repeated modulo5/chi4 calculations; full earlier table/cancellation proof remain. | VERIFIED_TWICE internally for new obligations |
| C11-U03: series and Euler product limits | P-series integral bound controls every omitted integer above X. Finite geometric products enumerate smooth integers once by FTA. Their limits equal the absolutely convergent series, and the product of1+p^(−s) bounds reciprocal magnitudes away from0. | Independently bound finite rectangular tails in the Dirichlet convolution and compare product differences with the positive p-series tail, avoiding conditional rearrangement. At s1 the finite reciprocal product dominates the harmonic partial sum, so its reciprocal tends0; this does not assert an s1 series identity. The new principal-mod6 example removes the2/3 factors; direct inclusion–exclusion gives the same2/3 multiplier, hence pi²/9 at2. | VERIFIED_TWICE internally |
| C11-U04: finite sieve and floor identity | The Mobius divisor sum is the coprimality indicator. Swapping finite sums counts each divisor's floor(x/d) multiples. For z≥sqrt(x), any surviving composite is impossible; z≥x leaves only1. | Independently expand the product of finite exclusion indicators. At30 the eight signed terms give8; at100 cutoff10 gives22 and pi100=25. The original claim P(z) is divisible by every integer≤x was false (squarefree P cannot contain4 or9). Corrected: for z≥x every squarefree d≤x divides P, nonsquarefree terms vanish by mu, larger divisors by floor. Fresh48→49 example proves the first surviving composite is49 and changes Phi13→14 while pi remains15. | VERIFIED_TWICE internally after correction |
| C11-U05: boundary and logarithmic error | Grouped chi4 terms are positive and bounded uniformly by13/15, and ordinary sums differ by a vanishing term. Nonprincipal complete periods cancel and an incomplete period has at most phi(m) nonzero unit terms. | Independent summation-by-parts formula proves convergence with a telescoping absolute comparison, without asserting absolute convergence of the original series. Newly supplied real-log remainder identity integrates u/(1−u); for abs(t)≤1/3 its magnitude≤3t²/4. Actual Volume1 derivative/FTC proof sites were read and crosswalk updated. Applied first to finite products and then fixed-s absolutely convergent sums, it bounds the prime-log error independently of s>1. The separate s↓1 continuity/nonvanishing step remains explicitly conditional, not a theorem smuggled in from Volume6. | VERIFIED_TWICE internally |
| C11-U06: reciprocal-prime implication and previews | Under the stated extra boundary bound, the Abel-weighted class difference is bounded. The positive total diverges by Euler's reciprocal-prime theorem; each class must diverge, and any finite unweighted class sum would bound its weighted sums, contradiction. | Independently use finite partial sums before taking s↓1: any prescribed large harmonic-prime subtotal persists near1, proving total divergence without exchanging signed limits. This says nothing about convergence of the signed unweighted prime series. Corrected the class-field overview's overbroad identification of all abelian-extension characters with ordinary Dirichlet characters; concrete Volume6/13 handoffs remain future topics. | VERIFIED_TWICE internally |
| C11-U07: advanced numerical/route claims | All20 keyed solutions and their earlier taught routes were reread, including cube-root zero convention, three-cycle congruence, Jacobi formal coefficients, dyadic lifting, power-map gcd and powerful-series regions. No newly imported theorem was used. | Recomputed the large four-square subtotal493480252693888 at10^7 using quotient-block divisor sums; ratio rounds1.00000007. Independently enumerated every prime below k^4 with cyclic bitset sumsets: cubic exception7; quartic5,13,17,29; eighth-power last761, matching the existing exhaustive numerical claim and the separately proved large-p bound. Earlier named/keyed records supply their full two reconstructions; finite probes do not prove their general theorems. | VERIFIED_TWICE internally for the displayed computations; keyed proofs retain separate status |

### C11 examples and all four datasets

| ID | Reconstruction and independent check | Status |
| --- | --- | --- |
| C11-E01: familiar characters | Principal is multiplicative because nonunits form the complement of units with the product property; chi4's two-unit table and chi8's full four-unit table establish multiplication. Legendre's proved criterion supplies the third family. | VERIFIED_TWICE internally |
| C11-E02: full modulo5 table | Generator2 visits1,2,4,3; evaluating i^(jk) gives all four displayed rows in1,2,3,4 order. Independent square set1,4 identifies chi2; all row inner products checked. | VERIFIED_TWICE internally |
| C11-E03: chi4 exponent | For every odd integer n, exponent(n−1)/2 has parity determined by n mod4; this gives the four displayed values. Independent residue table/complete period gives sum0, including negative inputs. | VERIFIED_TWICE internally |
| C11-E04: replacement modulo8 rows | Rho row1,−1,1,−1 and chi8 row1,−1,−1,1 give inner product0 and distinct product row1,1,−1,−1. Independent64-product table and orthogonality agree, including zero on evens. | VERIFIED_TWICE internally for new obligation |
| C11-E05: zeta2 finite product | Exact rational sum through30 lies(1.61215,1.61216); exact prime product through30 lies(1.63307,1.63308). Positive expansion contains the partial sum plus32,49,77 etc, so ordering is structural. Independent Basel limit and p-series tail agree. | VERIFIED_TWICE internally |
| C11-E06: replacement removed factors | Finite Euler factors remove exactly primes2,3; direct inclusion–exclusion gives1−1/4−1/9+1/36=2/3. Hence the coprime6 reciprocal-square sum is pi²/9. Independent finite sum to10000 plus the proved1/10000 tail encloses the value. | VERIFIED_TWICE internally for new obligation |
| C11-E07:mu at2 | Prime factor parity gives exact ten signed/zero terms and subtotal near.6163. Independent divisor-factor mu reconstruction verifies every term, especially6,+ and7,−; the absolute omitted tail is bounded by the p-series. | VERIFIED_TWICE internally |
| C11-E08:30/100 counts | Eight exact divisor terms at30 give8 and the eight listed survivors. Sixteen at100 cutoff10 give22; prime enumeration independently gives25 primes and the formula22−1+4. | VERIFIED_TWICE internally |
| C11-E09: replacement48/49 | No surviving composite can be below7². Direct gcd enumeration and independent signed-floor sums give Phi(48,5)13,Phi(49,5)14; prime count15 unchanged. Earlier complete30 example and all exercises remain. | VERIFIED_TWICE internally for new obligation |
| C11-E10: floor at10 | Nonzero terms d1,2,3,5,6,7,10 give10−5−3−2+1−1+1=1. Independent finite divisor exchange leaves only integer1. Correct squarefree-primorial explanation is U04. | VERIFIED_TWICE internally after correction |
| C11-E11: grouped three | Exact2/3+2/35+2/99=2578/3465≈.7440115; separate subtraction from1 gives887/3465>0 and added positive terms give strict lower2/3. | VERIFIED_TWICE internally |
| C11-E12: partial sums | Direct four-residue cumulative table1,1,0,0 repeats. Independent period0 plus each prefix proves abs≤1 for every nonnegative cutoff, improving the generic phi4=2. | VERIFIED_TWICE internally |
| C11-F01: chi8 clock | All eight actual values/inks agree with the supplementary law and complete64-product table; angular rule90−45k places residue0 at top clockwise. Larger labels/nodes retain all entries. | VERIFIED_TWICE data; revised standalone inspected |
| C11-F02: sieve30 | All30 cell coordinates, eight survivor frames and six multiples-of5 dots match direct gcd/remainder tests. Independent inclusion–exclusion gives8. Enlarged tiny labels/cells; corrected actual palette legend from teal/olive to dark grey/ochre, in separate rows. | VERIFIED_TWICE data; revised standalone inspected |
| C11-F03: race | Both10-point series exactly match fresh trial-prime counts at10…100; actual x coordinate maps to10+5x. All ticks/markers/styles match. At100 counts13 and11; at17 there is a tie3/3, so caption now limits its strict lead to the plotted cutoffs. Larger labels and final100 tick inspected. | VERIFIED_TWICE data; revised standalone inspected |
| C11-F04: cubic | All207 actual points include exactly every prime1mod3 below3000, no omissions/duplicates. Fresh cube-root multiplicity convolution counts N directly. Separate exact search of4p=A²+27B²,A1mod3 gives unique A=N−(p−2) for each. Every normalized ordinate matches to.000050001 and has abs≤1. Actual85 samples have abs≥.8 and25 have abs≤.2; caption describes this finite sample, replacing an unproved limiting-density claim. Moved larger x labels below the band. | VERIFIED_TWICE data; revised standalone inspected |

All four final standalone plates were built with the actual wrapper/fonts/
palette and rendered/viewed:clock196.70×181.43pt,sieve321.15×75.46pt,
race263.55×97.28pt,cubic338.54×161.95pt. No clipping/label overlap observed
in these standalone views. Full final-source chapter/page/EPUB/reader and
monochrome approval remain open. Eight new checks pass; full suite449 tests,
zero skips passes. The earlier reader-route wording guard was aligned with
the correct singular chapter reference. Inventory1361 current.

### C11 targeted source checks and CI dependency correction

- Actual Volume1 inverse derivative and early FTC proofs were read (see the
  DEP-071 crosswalk entry); the new logarithmic estimate uses those precise
  results instead of an unproved log series.
- [Apostol's Springer record](https://link.springer.com/book/10.1007/978-1-4757-5579-4)
  and [Caltech's author record](https://authors.library.caltech.edu/records/f4bx5-f6f64)
  corroborate1976 and scope. [Davenport's publisher record](https://link.springer.com/book/9780387950976)
  confirms third edition2000; Montgomery's revision credit is independently
  corroborated by the [WorldCat edition](https://search.worldcat.org/title/Multiplicative-number-theory/oclc/44469053).
  AMS's indexed Tenenbaum third-edition2015 copyright metadata was visible,
  but opening the publisher PDF returned403; the full edition remains pending.
- [Cole/Davie's actual publisher record](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/game-based-on-the-euclidean-algorithm-and-a-winning-strategy-for-it/99A7D31D926AF615AEB88F71CFAA9BB6)
  confirms Mathematical Gazette53(386),December1969,354–357, not the guessed
  recreational-journal citation. Full original-paper proof/history remains
  distinct from the locally reconstructed game proof.
- Exact a0cfaef3 Actions#1664 failed in list-job126656414125 because mpmath
  was not installed for the new high-precision tests. Added explicit pinned
  `tools/requirements-test.txt` (including build helpers), installed by the
  list job. Build-only jobs retain their runtime requirements; no output
  fingerprint is changed for a test-only dependency. A fresh isolated venv
  installed only that manifest and passed all22 new Chapter9–11 tests. The
  full activated local suite passes449 tests; terminal new-head CI remains
  required. Earlier success is not substituted for it.


## Global front/back matter, field guide and source credits — DEP-072

Read complete preface, field guide, jacket blurb, KDP description/keywords,
main route/catalogue, cover note and generator, and actual illustration credits.
These are distinct from the11 chapter passes. The field guide supplies the
last example environment: **97/97 examples and39/39 mathematical figure
datasets now have internal records**, without full format/history/external
acceptance. Complete conceptual dependency/voice/history graphs remain open.

| ID | Pass A | Independent/adversarial pass B | Status |
| --- | --- | --- | --- |
| G-E01: gcd→inverse example | Back substitution gives1=3·12−35, hence inverse−1≡11mod12;35·11=385=32·12+1. Every18x+12y is divisible by6 and cannot equal1. | Independently reduce35≡−1mod12, giving the complete class11; reduce18x≡0mod6, excluding an inverse. Exact enumeration includes negative representatives. This is the97th retained example, not a newly added block. | VERIFIED_TWICE internally |
| G-U01: notation and cancellation | Ring cancellation in an equality requires a nonzero factor, not an inverse; modular cancellation without changing the modulus needs a unit. Corrected the overbroad before-cancelling-find-the-inverse advice to the modular gcd check. Added positive divisor-function and real sieve domains. | The exact6|2·3 counterexample and the Chapter3 reduced-modulus rule independently distinguish the cases. Read each field-guide definition against its earlier local source: nonzero rational valuations, order, symbols, convergent indexing, norms, character series and sieve match. Qualified completeness of a finite search by a proved finite reduction. | VERIFIED_TWICE internally |
| G-U02: n²+1 investigation | Every odd prime factor gives a root of−1; the earlier Euler criterion forces1mod4. Conversely every prime1mod4 supplies a root, and shifting it by kp preserves the divisibility. The earlier ex:onemod4 solution proves infinitude using(2·product p)²+1. | Independently, the nonzero residue n has order4 when n²≡−1, hence4 divides p−1; direct sample factorisations10,26,50 agree. Checked n0/negative inputs and the excluded prime2. Infinite prime factors across values do not imply infinitely many prime values. The open-prime-value claim still participates in the global current-status/history pass. | VERIFIED_TWICE internally for the mathematics |
| G-U03: later notation and handoff | Supplied the meanings of algebraic integer/number field within the explicitly optional preview. Limited the full-ring assertion to Q(i),Q(omega); it does not describe every quadratic field seen in Pell. | Read actual Volume13 ch11-algebraic prop:OK and proof: integral trace/norm force half-integer coordinates, and the mod4 condition gives d−1,−3 identifications; following paragraph states the exact three Volume2 rings. This is a checked future preview, not a premise. Corrected the claim that Volume3 will first name homomorphisms: Chapter11 already defined them. Powers3mod7 and chi4(3²) independently match the concrete next-book examples. | VERIFIED_TWICE internally for preview accuracy |
| G-U04: preface/jacket/listing claims | Mod4 squares0,1 exclude7 as two squares;5=1²+2²,13=2²+3²,17=1²+4². Four parts/11 printed chapters, catalogue title/subtitle and144 keyed triples agree with the actual main route/inventory. All exercise routes were read separately; later books are described as future developments. | Independent source inventory gives per-chapter exercise counts15,11,21,10,16,19,8,8,8,8,20, sum144. This corrects DEP-071 prose's clerical19 for Chapter11: all20 groups were actually read; no extra verification is counted. Seven KDP keywords and description length pass existing listing guards. Preface/jacket make no claim of publication or independent refereeing. ISBN/account ownership and final generated listings remain separate checks. | VERIFIED_TWICE internally for stated source/count/math claims |
| G-F01: approved cover's mathematical dataset | Generator draws1…71² in a square spiral, retaining prime coordinates inside radius35.5 and a separate pale origin. The new colophon explicitly says the pale centre is1, not prime. | An independent closed-form square-ring coordinate map covers exactly all5041 grid points; Eratosthenes independently determines all primes. Its557 retained prime positions exactly match the generator; the only extra dot is the pale origin. Cover art/lettering/credits are byte-unchanged; only the colophon and corresponding generated notes/hash entries change. | VERIFIED_TWICE data; approved art preserved; final wrap/page review pending |

### Actual portrait-source matching and primary cover history

Downloaded/viewed the exact source originals for all three active portraits,
then viewed the local derivatives and compared after resizing the source to
local dimensions with LANCZOS. Local bytes differ; no exact-byte claim is made.
RGB mean absolute differences are Fermat1.0744,Gauss2.1780,Chebyshev1.2834
on the0…255 scale. Source/local hashes, dimensions, methods and caveats are in
[the portrait evidence](volume2-portrait-source-evidence-2026-11-04.json).

- Fermat matches [Pierre de Fermat.jpg](https://commons.wikimedia.org/wiki/File:Pierre_de_Fermat.jpg),
  artist unknown. The source permission note itself qualifies the original's
  authenticity. Removed the unnecessarily definite17th-century description
  and disputed1601 birth-year assertion from the caption; retain traditional
  portrait/unknown artist. MAA's indexed historical note reports Barner's1607
  dating, but opening its full page failed521; no new precise birth year is
  asserted on that incomplete evidence.
- Gauss matches [Carl Friedrich Gauss1840 by Jensen](https://commons.wikimedia.org/wiki/File:Carl_Friedrich_Gauss_1840_by_Jensen.jpg),
  not the similarly named Carl Friedrich Gauss.jpg. The latter's description
  identifies a Biermann1887 copy, and its pixel difference is much larger.
  Matching source metadata credits Jensen1840. The earlier IMU original/
  copy explanation supports the historical work; exact image identity was
  separately checked here rather than inferred from a familiar name.
- Chebyshev matches [Pafnuty Lvovich Chebyshev.jpg](https://commons.wikimedia.org/wiki/File:Pafnuty_Lvovich_Chebyshev.jpg),
  unknown photographer,late1880s/early1890s; source cites the1964 Academy
  history volume2,296–297. Caption/credits use that qualified date. The
  original print and photographer have not independently been identified.
- Removed the unused Minkowski portrait from reader-facing credits; retained
  the asset as unused in the source record. Replaced the obsolete Volume0/
  four-portrait provenance statement. Commons' public-domain labels are
  documented as source evidence, not independent publisher/legal acceptance.
- Read the actual March1964 Scientific American scan, printed page122
  (physical124), including Ulam's last-fall account and original prime-grid
  illustrations; rendered/viewed the page. This primary passage supports
  autumn1963 and the1964 spiral feature. Its
  [publisher record](https://www.scientificamerican.com/article/mathematical-games-1964-03/)
  independently confirms Gardner,March1964,volume210(3),start120,
  doi10.1038/scientificamerican0364-120. Scan source:
  https://www.wkbpic.com/wkbx/SA/1964/1964-03-01.pdf .
  New colophon avoids unsupported first-ever priority while retaining the
  sourced dates and describes the actual finite cover dataset.

Three new arithmetic/cover checks pass. Existing source/route/cover-generator
checks pass; full suite **452 tests,zero skips** passes. All15 approved cover
motifs and lettering, images and shared copyright-page credits remain
unchanged. Inventory1361 is regenerated. Global conceptual/first-use/story/
historical-bibliographic reconciliation, exact-current-source artifacts and
every-page/external/author/publisher proof remain open.

## Global conceptual/story reconciliation — DEP-073

The [dependency/story ledger](volume2-dependency-and-story-review-2026-11-04.md)
now traces the printed route, critical meanings, actual earlier proof sites
and optional routes. All319 references resolve and all85 forward occurrences
have explicit individual explanations/context hashes in the checked register;
none is accepted as a necessary forward premise. Structural guard tests do
not replace manual proof checks or certify all mathematical semantics.

New source clarifications define integer units at C1 first use and repeat
squarefree on C4's main route, specify asymptotic independence's fixed joint
limits, define indicator/name Jacobi sums before hints, define Markov triples
in the explicit diagram preview, retain the full three-square exclusion and
keep Pratt's digit base binary. Existing proofs/results/examples and their
independent reconstructions remain; no new theorem/example is counted.
Integer units±1 are justified by abs(a)abs(b)1 and independently by the
integer-product lower bound when abs(a)≥2; prime-exponent characterization
of squarefreeness independently matches the divisibility definition.

Full suite455 tests,zero skips passed; final main-route squarefree wording
followed by41 focused checks, refreshed inventory and forward-reference guard.
Global original-history/bibliography, final-source artifacts/all pages and
external/author/publisher acceptance remain open.
