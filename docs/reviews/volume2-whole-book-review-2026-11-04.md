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
| 4–11 | UNREVIEWED in this whole-source register; named/keyed evidence is separate | UNREVIEWED comprehensively | UNREVIEWED comprehensively | UNREVIEWED comprehensively |
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
remove the claim that every integer has a prime factor, correct the clock's
caption from a colour absent in its source to the actual ring/dot shapes,
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
