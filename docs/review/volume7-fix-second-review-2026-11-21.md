# Volume 7 fix, second review — 21 November 2026

Independent reading of PR #260 at `be82b8043b5dd74bc902e5548142a95586f10207`. The fixes were written by another agent. The corrections below are a later commit on `cursor/fix-volume7-review`.

## Verdicts

**Correctness.** The reviewed head needed changes. Three gaps are listed below. After those corrections, each of V7-001 through V7-011 is fixed in the place the issue named, and the fix does the job the issue asked for. Nothing extra was rewritten.

**Dropped or weakened proofs.** No numbered statement was shortened, and no statement was weakened. The constant `77` in the solution of `pb:typicalcf` became `78` because the new majorant is `(2c)^2<(44/5)^2=77.44`, which is not smaller than `77`. The problem only asks that the limsup be finite. The bound `q_n<e^{5n}` is the one the comparisons prove, and part (e) now uses that strict inequality. `Q_n=\lfloor e^{5n}\rfloor`, so an integer strictly less than `e^{5n}` is at most `Q_n`.

**V7-001.** Lemma `lem:cauchybasic`(c) says that a non-null Cauchy sequence in `\Q` is eventually `≥δ` or eventually `≤-δ`. The written proof uses the order of `\Q`. Parts (a) and (b) do transfer to `|\cdot|_p`: the triangle inequality, multiplicativity, and a largest element among finitely many real values `|x_n|`. The new paragraph says so, and it does not transfer (c). If `(x_n)` is Cauchy and not null, some `ε>0` has `|x_n|≥ε` for infinitely many `n`. With `δ=ε/2` and `|x_n-x_m|<δ`, the reverse triangle gives `|x_n|≥|x_m|-|x_n-x_m|>δ`. The inverse estimate in Theorem `thm:reals` is `|1/x_n-1/x_m|=|x_n-x_m|/(|x_n||x_m|)`. The strict lower bound still yields the written `≤|x_n-x_m|/δ^2`, and the classes form a field. Once `|x_n-x_m|<δ<|x_n|`, the ultrametric inequality forces `|x_n|=|x_m|`. The statements of Theorem 2.10 and Corollary 2.11 are unchanged.

**V7-002.** For `n≥2` the vectors `e_1` and `e_2` exist. If `x` is not `±e_1`, then `z=e_1` is different from both `x` and `-x`. If `x=±e_1`, then `z=e_2` is different from both. Each normalised segment misses `0`, because the third vector is not the antipode of the start. The sentence no longer claims that a standard basis vector is orthogonal to `x`.

**V7-003.** Algebraic closure is quoted from Steinitz, *Algebraische Theorie der Körper*, J. reine angew. Math. 137 (1910), 167–309, and the sentence says it is not proved and not used. The journal record gives those pages. The only occurrences in Volume 7 are that sentence and the bibliography item. Volumes 8–15 do not cite it. Theorem 1.21, `thm:basis`, is unchanged.

**V7-004.** The sine series is `\sum_{k≥0}(-1)^k/(2k+1)!`. The absolute values `a_k=1/(2k+1)!` decrease, because the next term over this one is `1/((2k+2)(2k+3))≤1/6`. The tail after `a_2` is `-(a_3-a_4)-(a_5-a_6)-\cdots`. Each difference is positive, and absolute convergence of the exponential series lets the tail be grouped. The tail is negative, so `\sin 1≤1-1/6+1/120=101/120`. Since `101<102`, one has `101/120<102/120=17/20=0.85`. The comparison stands after Theorem `thm:exp`. Example `ex:cosfixed` is not cited in that proof. A ratio `0.85<1` is a contraction on the complete interval `[0,1]`.

**V7-005.** For nonnegative `x` and `y`, `(\sqrt x-\sqrt y)^2≤|x-y|`, because `\sqrt x+\sqrt y≥|\sqrt x-\sqrt y|` and `|x-y|=|\sqrt x-\sqrt y|(\sqrt x+\sqrt y)`. Taking square roots gives `|\sqrt x-\sqrt y|≤\sqrt{|x-y|}`. If `|x-y|<ε^2`, the difference is smaller than `ε`, with one `δ` for the whole interval. The quotient `(\sqrt x-\sqrt 0)/x=1/\sqrt x` is unbounded as `x→0`, so there is no Lipschitz constant. Heine's theorem is named as a later source of the same uniform continuity, and the bound does not use it.

**V7-006.** The paragraph already sent the names compact and locally compact to Chapter 4. It now sends the word connected, and the proof that an interval does not split into two nonempty sets open in it, to Chapter 3. That is Theorem `thm:intervals`. The sentence is a preview. The compactness of `\Z_p` is Corollary `cor:Zpcompact`, proved before the sentence.

**V7-007.** Section `sec:choice` defines the axiom of choice and points back at the countably many enumerations in Proposition `prop:countable`(c). The proposition now names that section. The proof still chooses one injection `A_k→\N` for each `k`.

**V7-008.** The display is now one sentence: the cardinal chain, then "where the middle step". The middle equality is `|\mathcal P(\N\times\N)|=|\mathcal P(\N)|`. Part (b) injects `\N\times\N` into `\N`, and part (a) makes an infinite countable set bijective with `\N`. A bijection of the underlying sets matches the power sets.

**V7-009.** Different stage-`n` intervals when `|x-y|>3^{-n}` was the sentence the issue asked for, and that half is right: a common word of length `n` traps both points in an interval of length `3^{-n}`, because the tail is at most `\sum_{k>n}2\cdot 3^{-k}=3^{-n}`. The next sentence said that the midpoint has ternary digit `1`, and therefore does not lie in `C`. A digit `1` in one expansion does not by itself exclude a point. The endpoint `1/3` is `0.1000\ldots_3` and also `0.0222\ldots_3`, and `1/3` lies in `C`. The corrected paragraph keeps the midpoint out by the gap. Digit `0` at index `j` gives a point at most `s+3^{-j}`, and digit `2` gives a point at least `s+2\cdot 3^{-j}`, for every point of `C`. The open interval between those ends misses `C`. The series `\sum_{m≥1}3^{-m}=(1/3)/(1-1/3)=1/2` writes the digits of the inserted point: the digits of `s`, then `1`, then infinite `1`s.

**V7-010.** The integral comparison, the rationalised telescoping sum, and the eight integer bounds are right, and they give `c<4.398<4.4` and `(2c)^2<e^5`. The sentence that introduced the eight bounds said each term was smaller than a thousandth. The first term is `\sqrt 2>1`. The cross-multiplication `1957\cdot 10>27\cdot 720` shows that the partial sum of `\exp` exceeds `27/10`. The sentence concluded `e>27/10` from that comparison. Both are corrected below. The arithmetic itself was not replaced.

**V7-011.** Proposition `prop:measureprops` is Proposition 7.2, and (b) is countable subadditivity. If `A` is measurable, both `A\cap[0,1]` and `[0,1]\setminus A` are measurable, and the argument already given makes each of them null: a positive-measure measurable subset would contain a compact set of positive measure, hence an uncountable closed set, which has to meet both `A` and its complement. Subadditivity gives `\lambda([0,1])≤0`. The value `\lambda([0,1])=1` contradicts that.

**Concept order.** The new appeals are to tools already in hand: the triangle inequality and multiplicativity for `|\cdot|_p` in Example `ex:metrics`; the inverse estimate in Theorem `thm:reals`; the ternary description of `C` in Chapter 2; the axiom of choice in Section `sec:choice`; connectedness in Chapter 3; the exponential series in Theorem `thm:exp`; subadditivity in Proposition 7.2. The example `ex:cosfixed` points forward to the sine bound and says that the example is not used in the proof of the theorem.

**Labels and numbering.** Against `be82b804`, the TeX files under `volume7-spaces/` have the same `\label` names. The four edited files have 38, 33, 29 and 30 labels, unchanged from `a45c17fc`. There is no new numbered statement. The counts of `definition`, `theorem`, `proposition`, `lemma`, `exercise`, `example` and `corollary` environments are 39, 79, 31, 25, 169, 5 and 12. Theorem 1.21 is `thm:basis`. Theorem 2.10 is `thm:Qp`. Corollary 2.11 is `cor:Zpcompact`.

**Recomputed numbers.** A Python session on this review checked the arithmetic with integers. `283^2=80089>80000=2\cdot 200^2` and `283/200=1415/1000`. `3\cdot 289^2=250563>250000=500^2` and `289/500=578/1000`. `3\cdot 334=1002>1000`. `5\cdot 56^2=15680>15625=125^2` and `28/125=224/1000`. `6\cdot 41^2=10086>10000` and `41/250=164/1000`. `7\cdot 189^2=250047>250000` and `63/500=126/1000`. `2\cdot 357^2=254898>250000` and `51/500=102/1000`. `12\cdot 84=1008>1000`, which is `250<252` after dividing by 4. `19^2=361>360=10\cdot 6^2`, `37/18\cdot 2/3=37/27`, and `37\cdot 1000=37000<37017=1371\cdot 27`. The eight numerators and the tail sum as `1415+578+334+224=2551`, `164+126+102+84=476`, and `2551+476+1371=4398`, so `c<4.398<4.4`. Also `(44/5)^2=1936/25` and `1936<1950=78\cdot 25`. The partial sum of `\exp` through `1/6!` is `1957/720`, because `720+720+360+120+30+6+1=1957`, and `1957\cdot 10=19570>19440=27\cdot 720`. Finally `27^5=14348907>14300000`, and `143>78`. Thus `(2c)^2<e^5`. The sine bound is `101/120<102/120=17/20`. No displayed constant was replaced.

**Voice.** The new sentences name the object and the step. The banned fillers do not appear in the changed paragraphs. The Khinchin comparisons stay in the manner of the integer estimates around them.

**Downstream impacts.** No numbered statement in Volume 7 changes its number. Nothing outside Volume 7 cites the algebraic-closure sentence. The citations checked for this review are still the same statements:

- Volume 8, `ch08-haar.tex:217`, cites Theorem 2.10 and Corollary 2.11 for the completion `\Q_p` and the compact ring `\Z_p`.
- Volume 8, `ch01-banach.tex:309`, cites Theorem 1.21 for a Hamel basis.
- Volume 13, `ch06-local.tex:33`, cites Theorem 2.10 for the completion and the ultrametric absolute value.
- Volume 13, `ch12-padic.tex:114` and `:123`, cite Theorem 2.10 and Corollary 2.11, and again Theorem 2.10 for the closed unit ball.

`python3 tools/cross_volume_citations.py` matched 5446 numbered statements. Volume 7 does not cite the items Volumes 1–6 left for later books: the unnumbered cosine proposition before `prop:sincmp`, Volume 2's `prop:legendre`, Volume 3's `prop:cyclodegree` and `prop:solids`, Volume 4's `lem:tree` and `lem:sector`, Volume 5's `cor:cotagain`, or Volume 6's removed secondary constant in `ex:twoomega`.

## Findings

| ID | Location | Problem | Fix |
| --- | --- | --- | --- |
| SR-001 | `volume7-spaces/chapters/ch12-harder.tex`, solution of `pb:khinchin`(b) | "Each of the first eight terms is smaller than a thousandth" is false. The first term is `\sqrt 2`, and the displayed bounds are `1415/1000` and its companions. "Adding these eight thousandths" repeats the slip. | Each of the eight terms is smaller than one of the stated multiples of `1/1000`. The sum of those bounds and the tail is unchanged. |
| SR-002 | `volume7-spaces/chapters/ch12-harder.tex`, the same paragraph | `1957\cdot 10>27\cdot 720` shows that the partial sum `1957/720` exceeds `27/10`. The sentence concluded `e>27/10` from that comparison. | The partial sum exceeds `27/10`. Every later term of the exponential series is positive, so `e>27/10`, and therefore `e^5>(27/10)^5`. |
| SR-003 | `volume7-spaces/chapters/ch03-topology.tex`, the components of the Cantor set | "Its `j`-th ternary digit is `1`, so it does not lie in `C`." One expansion with a digit `1` does not exclude a point: `1/3=0.1000\ldots_3=0.0222\ldots_3` lies in `C`. The expansion of the midpoint was not written. | Digit `0` at index `j` keeps a point of `C` at most `s+3^{-j}`, and digit `2` keeps it at least `s+2\cdot 3^{-j}`. The open interval between those ends misses `C`. The series for `1/2` writes the digits of the inserted point. |

## What this review did not check

- A page-by-page visual reading of the PDF. `./build.sh volume7-spaces` exited 0. The layout check reported 392 whole boxes, maximum height 288.5 pt, no overflow and no unresolved reference. The log has no undefined reference and no overfull box. The print interior is 411 pages, and the page size is 513 by 738 pt. The reading PDF is the cover plus that interior, 412 pages at 7 by 10 in. EPUB figures are full width, and the math images carry an em baseline. The EPUB is 25 MB.
- Kindle rendering of the EPUB, beyond those build checks.
- Proofs the diff does not touch, beyond the citation pins, the label comparison, the numbering check, and the passages named by V7-001 through V7-011.
- The items the Volume 7 review left unchecked: portrait files, TikZ coordinates against captions, the equality `\mathcal H^s(C)=1`, the Jenkinson–Pollicott constant, and the historical fine print beyond the Steinitz pages.
- Acceptance of the print file by KDP.
