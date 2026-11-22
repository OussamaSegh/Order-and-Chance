# Order and Chance · Volume 1 editorial review

Reviewed the manuscript at `1d7f736bfae28f77d7a5a26a30f6424a66857e88` on `origin/main`. Line numbers refer to that revision.

## First Principles

Read the front matter, preface, all 11 chapters in order, field guide, image credits, index, and About the Cover. The reading included figure captions, workshops, all 160 numbered exercises and their hints and solutions, closing challenges, and chapter source lists. It also covered the jacket copy and store listing. Numerical examples and vulnerable proof steps received targeted checks. The reading PDF and paperback interior passed the repository's automated layout checks. The manual PDF inspection covered the Katona and birthday figures. A full visual pass, EPUB inspection, and primary-source and image-licence verification remain open. This report covers Volume 1.

The cube identity and the hat check give the volume a useful through-line. The field guide extends it by asking the reader to choose among tools learned in different chapters. Keep that structure and the solutions' separation of proof discovery from the final argument. The revisions below focus on places where a reader following those arguments line by line would encounter an invalid step, an unstated assumption, or a reference that needs a clearer destination.

### Revision order

1. Repair the false equality in the fundamental theorem of algebra proof, the Hölder equality factor, the floor proof's repeated case, and the Riemann-sum comparison between arbitrary partitions. Close the repeated-root cases in Cardano and the uniqueness argument for the Chebyshev minimizer.
2. Align the hat-check setup with inclusion–exclusion. State independence in the dice and coin models, and carry the precise sampling hypotheses through the polling example. Check empty cases, endpoint limits, and first-use definitions in the surrounding chapter plans.
3. Revise the field guide's statements about roots and dependence, verify the index numbers after edits, reconcile credits with their source records, and check the affected figures and cross-references in the finished editions.

The line references below use the following files in `volume1-first-principles/chapters/`.

| Chapter | Source file |
| --- | --- |
| 0 | `ch00-language.tex` |
| 1 | `ch01-sums.tex` |
| 2 | `ch02-counting.tex` |
| 3 | `ch05-sequences-series.tex` |
| 4 | `orders.tex` |
| 5 | `ch02-complex-roots.tex` |
| 6 | `ch03-polynomials.tex` |
| 7 | `ch07-linear-algebra.tex` |
| 8 | `ch06-integrals-taylor.tex` |
| 9 | `ch04-inequalities.tex` |
| 10 | `ch09-probability.tex` |

### Preface

- Line 4. Say that the 24 assignments are equally likely before dividing the count of favourable assignments by 24. The first probability example can teach the modelling assumption in one clause. Enumeration confirms 9 favourable assignments. The proportion is 0.375 for four hats and about 0.36787946 for ten.
- Line 40. Replace “the four rules in the next paragraph” with an explicit pointer to the paragraph on the integral. The intervening paragraph concerns elementary functions.
- Keep the opening pair of problems. The cube identity at ten and the hat count both check out, and they give the reader two tasks to follow into the book.

### Chapter 0 · The Language of Mathematics

- Lines 133–141. Put the complete example `2x=1` in the first displayed comparison of existential and universal statements. Move the square-root preview to the end of the explanation. The signed calculation and a witness are enough to teach the two quantifiers before the reader meets the intermediate value theorem.
- Lines 915 and 1082. Align the wording on negation. In the rational-number solution, “Negating both equivalences” literally describes negating whole statements. Say that the two sides of each equivalence can be negated together, and keep the worked argument about a rational sum forcing a rational input.
- Line 1187. In the last challenge, spell out the two cases for membership in the diagonal set. If the proposed input belongs to the set, the biconditional puts it outside. If it lies outside, the biconditional puts it inside. This makes the contradiction follow directly from the definition the reader just used.
- Keep the image-intersection workshop. The two witnesses in its failed proof make the role of injectivity visible. The singleton argument then proves necessity using the same obstruction. The negative and zero cases in the parity proof and the empty-domain cases in the workshop and closing challenges belong in the reading.

### Chapter 1 · Sums, Binomials and Induction

- Lines 49–56, 144–145, and 451–456. State that the upper summation index is a nonnegative integer. Distinguish the polynomial interpolating the partial sums from the partial sums themselves, whose indices remain discrete. For a geometric sum with ratio zero, describe the initial term as the empty product.
- Lines 205–234. Keep the equivalence of the three induction principles and the least-counterexample example. Replace the assertion that weak induction “only remembers the previous integer” with a sentence about the particular hypothesis chosen. A weak-induction hypothesis can assert the result for every index up through the current one.
- Lines 296–337. State the binomial theorem at degree zero, or explicitly supply the empty product when invoking it for zero in Vandermonde and the five-agreements workshop. The counting proof of the factorial formula uses the staged product rule. Give the rule a short local justification here, then refer forward to its general treatment.
- Lines 478–589 and 707–747. Keep the four cube proofs. In the exercise introduction, point to the fourth proof as a double count of the table entries and distinguish the two geometric arguments by their objects. The second proof can keep its explicit expansion or its table verification as the main checkpoint, with the other serving as a short check.
- Lines 819 and 933–941. Give the gcd subtraction identity for the indices in the Fibonacci solution. Both pairs of indices have the same common divisors because replacing an integer by its difference with the other preserves divisibility. The hint currently calls that identity “already proved” without giving the argument or naming a precise earlier proof.
- Lines 995–1026. Keep the empty cases. Complete the Fibonacci tiling construction with one inductive step. Attach a square of side $F_n$ to the preceding $F_{n-1}$ by $F_n$ rectangle along its side of length $F_n$.

### Chapter 2 · Counting and Discrete Reasoning

- Lines 8–14, 95, and 419. Define the overlapping sets as the permutations that return a given guest's own hat. The union is the set of arrangements with at least one correct return, and its complement is the derangement set. Using sets of disappointed guests at the start describes a different union.
- Lines 260–291. State the ranges before the three lattice-path arguments. Pascal's numerical boundary argument needs at least one step. Handle $(0,0)$ as the empty path. Vandermonde's path endpoint needs $0\le r\le m+n$, with both sides zero when $r>m+n$. Give an explicit sum range before applying the zero convention.
- Lines 421, 545–546, and 603–613. Say that each of Euler's two shares stabilizes at its own value to the stated precision. In the splice hint, identify the predecessor of $n$ as the guest who will receive hat $k$ after removing $n$. The solution already gives the correct bijection. State the range of the second recurrence and check $D_1$ explicitly if that range starts at one.
- Lines 447–452 and 616–622. Treat the empty target directly in the solution or state the empty-union convention. To make the Newton connection self-contained, derive the alternating binomial formula for the $n$th forward difference by induction using Pascal's rule.
- Keep the exercise that lists short Catalan paths before the reflection proof. The first passage through $y=x+1$ gives the witness the inverse bijection needs. Keep the interval-to-circle exercise too. It tests both the boundary $k=\lfloor n/2\rfloor$ and the change in adjacency.

### Chapter 3 · Sequences, Series and Limits

- Line 106. Fix the floor proof. After the case $m<m'$ has been ruled out, the symmetric argument needs to rule out $m'<m$. The printed $m'>m$ repeats the first case.
- Lines 155–156 and 264–268. Allow an empty initial prefix when bounding a sequence, for example by including $0$ among the numbers whose maximum is taken. In the peak argument state where to begin when the set of peaks is empty.
- Lines 593–642 and 969–985. Keep the first-positive-zero proof as the source of the sign and monotonicity facts. The shifts by $\pi/2$ already show that sine is positive on $(0,\pi)$ and negative on $(\pi,2\pi)$. Use those facts directly, and explicitly identify the zeros of sine before dividing by $\sin(\theta/2)$ in the Dirichlet example.
- Lines 659–700. The Riemann-sum paragraph estimates two choices of tags on a common partition, then draws a conclusion about all fine partitions. Compare each partition with a common refinement, whose tags differ by at most the old mesh from the old tags. This gives a uniform Cauchy bound for arbitrary fine sums. Keep the four admitted area rules visible as the basis of the fundamental theorem in this volume.
- Lines 861, 1045–1049, 1315–1322 and 1334. Use distinct names for the Stirling limit $d$ and the second mean-value point. In the harmonic-threshold exercise, give a reproducible certified comparison at the two stated indices, or label the reported computation as numerical. Direct high-precision summation gives $H_{12366}\approx9.9999621479$ and $H_{12367}\approx10.0000430082$. Keep the six-term logarithm certificate, which gives both a remainder bound and an explicit decimal enclosure.
- Lines 1126–1139 and 1351–1359. For the Newton exercise distinguish error below $10^{-100}$ from agreement of rounded strings. State whether the question asks for a sufficient iteration or the first such iteration. The displayed eighth-step bound establishes sufficiency. Use the exact rational iterates and enclosing rational bounds on $\sqrt{2}$ if asking for a sharp iteration count.
- Keep the quantitative contrast between the two representations of $\ln 2$. Keep the separation between formal coefficient calculation in Chapter 2 and limits of real partial sums here.

### Chapter 4 · Orders

- Lines 44–49. State the task relation reflexively, for example “is the same task or must be completed first.” If teaching the strict prerequisite relation first, say how adjoining equality gives a partial order. For a Hasse diagram, explain that inserting elements between consecutive pairs produces a saturated chain, since a finite interval allows only finitely many insertions.
- Lines 104, 153–164 and 240–255. Name the empty-poset and $B_0$ cases, or state the positive-size assumptions where appropriate. In Erdős–Szekeres, Mirsky gives as many antichains as the actual height and Dilworth gives as many chains as the actual width. Both bounds need “at most” in the argument. Keep the decreasing-block construction for sharpness.
- Lines 281–305. In Katona's proof distinguish renaming the elements from rotating a seating. Use “element” for the labels that are counted and “position” for where they sit. The caption's $n=6$, $k=2$ example satisfies $n>2k$, whereas the caption says $n=2k$. Keep the worked example and correct the relation, then keep the separate equality case in the next paragraph.
- Lines 314–335. State that well ordering of the natural numbers was assumed and used to prove induction. Qualify the opening claim about every termination argument. Name a decreasing quantity as the method being taught here.
- Lines 411–425. Define convex position for a set of points, then justify that an extreme vertex of the larger hull cannot lie inside any triangle of the other points. The current wording says “the five points” even when applying the definition to a selected set of four.
- Keep the connection from the counting chapter's label pairs to Mirsky's ranks, and keep the rewriting exercise. Its invariant explains the final word and its decreasing tuple independently explains termination.

### Chapter 5 · Complex Numbers and Roots of Unity

- Lines 12–26 and 938–956. Scope Cardano's displayed formula to paired cube roots and handle $p=0$ separately. When $p\ne0$, the quadratic roots are nonzero, and each cube root $u$ of the first gives the unique partner $v=p/(3u)$. Three legal pairs can give repeated values, for example at $p=3$, $q=2$, and when $p=q=0$ there is only one legal pair. The Bombelli example gives three distinct real values and should stay.
- Lines 135–156. Use “the two solutions of $w^2=i$” rather than equating a square-root symbol to a pair of answers. In the general calculation verify that the two proposed absolute values have product $|b|/2$, using $|a+ib|^2-a^2=b^2$. In the quadratic, specify that a zero discriminant gives one distinct root of multiplicity two. The printed “unless you have chosen one” clause misses this case and misstates how the sign works.
- Lines 292–297 and 397–455. Mention opposite arrows in the rhombus caption, since a zero sum has no direction. In the roots-of-unity proposition name the positive-integer parameter. Scope the regular-polygon and zero-sum language appropriately. For $n=1$, the lone root is $1$ and its sum is $1$.
- Lines 569–585 and 992–1004. Separate the all-equal centroid case from orientation. The algebraic condition still holds there, but there is no clockwise or anticlockwise ordering. Give the algebraic degeneracy check once in the criterion, and state the orientation conclusion for distinct centres in Napoleon's theorem.
- Lines 648–656. Write the constructibility statement as a preview of the precise criterion in Volume 3. The necessary condition alone does not give the sufficiency asserted in the sentence about $17$.
- Keep the filter as an explanation of the geometry. It supplies a clean transition from a closing triangle of arrows to the mod-three subset count, and then to the Gauss sum.

### Chapter 6 · Polynomials

- **Fix the false equality in the fundamental theorem of algebra proof (line 165).** Factor $z^j-w^j$, then apply the triangle inequality to the sum of products. The first equals sign on the displayed line must be $\le$. For $z=1$, $w=-1$, $j=2$, the left side is $0$ and the claimed equal quantity is $4$. The subsequent Lipschitz bound is valid with the corrected inequality. At line 177, denote the selected subsequence explicitly when taking the limit that attains the minimum.
- Lines 71–75, 326–336, 352–353, and 380–394. Start the formal derivative sum at one so it contains no negative power. Keep the scope of irreducibility statements to nonconstant polynomials and handle the zero input separately in Gauss's lemma. In Newton's identities, start the coefficient comparison at $m=1$ and name the characteristic-zero assumption when solving backward by division by $k$.
- Lines 253–257 and 767–768. In the secret-sharing construction, say up front that each pair of coefficients is chosen with equal probability, then show why every fixed secret induces the same distribution of two shares. Cite the interpolation theorem directly for the bijection, since the Vandermonde determinant is developed in the next chapter. The two-share example over the reals correctly teaches algebraic consistency alone.
- Lines 300 and 537–540, 704–711. The surrounding text claims that every other monic polynomial does strictly worse. The exercise proves the lower bound and gives a minimizer. Prove uniqueness with the earlier Lagrange formula or narrow the claim. For uniqueness, set $Q=2^{1-n}T_n-P$. At the ordered alternation nodes $y_k$, each quotient $Q(y_k)/\prod_{j\ne k}(y_k-y_j)$ is nonnegative. Their sum is the coefficient of $X^n$ in $Q$, which is zero, so $Q$ vanishes at all the nodes.
- Lines 470 and 775–777. Specify that the coprime probability is a limit of uniform finite counts. When evaluating the improper Chebyshev integral, justify both endpoint limits independently. After the substitution each omitted tail has absolute size at most its length in the angle variable.
- Keep the finite Basel proof. The exact cotangent sum and the two explicit bounds make clear what the polynomial proves and where the limit enters.

### Chapter 7 · Linear Algebra

- Lines 125–141 and 183–191. Say that the two columns are linearly independent in the $2$ by $2$ inverse test, including the possibility of a zero column. Complete the transposition induction with the branch in which $\sigma$ already fixes $n$, and state the identity's empty-product case.
- Lines 235–246, 285–330 and 425–429. Define the empty determinant as one when using cofactors of a $1$ by $1$ matrix. Introduce the distinct-eigenvalue criterion with the independent-eigenvectors proof before mentioning Cayley–Hamilton as a later alternative. Define a stable subspace when first used. Keep the existing direction from the spectral-theorem section to the least-squares workshop for first-time readers.
- **Remove the stray vertical bar before the volume formula (line 450).** It appears in the source immediately before the gathered heights. In the rank–nullity recap at line 594, say that kernel dimension plus image dimension equals domain dimension. The current “dimensions missing from the image” can be read as codimension in the target, which need not equal the kernel dimension.
- Lines 673–675 and 895–905. Clarify whether the Fibonacci exercise asks only to show that $F_n$ divides $F_{kn}$ or asks for all positive Fibonacci divisors. For the latter, the gcd identity shows that for indices $j\ge3$, $F_j\mid F_m$ precisely when $j\mid m$, while $F_1=F_2=1$ always divides. State positive index ranges where $F_{n-1}$ occurs.
- Lines 906–915 and 929–933. In the lattice-point argument refer to the inverse of the matrix with columns $u,v$, rather than reusing $P$ from the two-basis comparison. For the PageRank example, distinguish the proven contraction bound from the asymptotic factor of the worked iteration, and use the same convention for the row or column of ones in the hint and solution.
- Keep the least-squares example and its exact residual. The orthogonality is in observation space and the residuals are vertical on the plotted plane. That distinction is worth preserving.

### Chapter 8 · Differential and Integral Calculus

- Lines 26–56. Carry over the chain rule's requirement that the composite be defined near the point. Before deriving the arctangent derivative, verify that tangent is strictly increasing on $(-\pi/2,\pi/2)$ and tends to opposite infinities at the endpoints. The sign of the cosine and the values of the sine and cosine at the endpoints supply the limits. Use that range to justify the inverse and the branch in Machin's formula.
- Lines 126–142. In the substitution proof, account for compositions at an endpoint of the integrand's interval, including a map that reaches that endpoint at an interior argument. The one-sided derivative estimate from the fundamental theorem suffices, or one can extend the continuous integrand by its endpoint values before applying the chain rule.
- Lines 225–235 and 565–594. Adopt the workshop's distinction between an absolute error and correctly rounded decimals in the sine example. An explicit interval makes the rounding claim checkable. The Taylor polynomial and the true sine at $0.1$ round to the same six places.
- Lines 673–679 and 887–894. Use additivity of oriented finite integrals to obtain the displayed difference in the Frullani proof. This works for arbitrary cutoffs, including disjoint integration intervals. Then take the two endpoint limits independently. The displayed difference formula already has the right signs.
- Lines 922–935. Each press changes the *parity* of each $S_r$, while the counts can either rise or fall. Show that each class has equally many even and odd configurations by toggling one fixed lamp in that class. For the reachable count, show that press patterns giving the same configuration differ by one of the four patterns that do nothing. This establishes the size of each fibre before dividing by four.
- Keep the Wallis-to-Stirling and Wallis-to-Gaussian arguments together. The same recurrence produces both limits and the endpoint cases in the improper integrals give readers practice with finite cutoffs.

### Chapter 9 · Inequalities, Convexity and Estimates

- **Correct the Hölder equality factor (line 375).** The preceding equation gives $a_i^p=(A^p/B^q)b_i^q$. The printed $(A/B)^p$ agrees only when $p=q$ or $B=1$. A single entry $a_1=1$, $b_1=2$ with $p=3$, $q=3/2$ gives equality and distinguishes the two expressions. The converse already states the correct factor.
- Lines 301–305 and 314–318. Use a nondegenerate interval for the integral Cauchy–Schwarz equality case, and explicitly handle $g=0$. In the linear objective example, the absolute value of $x+2y+3z$ is at most $\sqrt{14}$. Its square is at most $14$. The printed “left side” points at the square.
- Lines 507 and 516. Say that the paired differences have nonnegative product, including ties. If keeping the covariance preview, identify the probability model as a uniform choice of list index and state that the analogous conclusion for general random variables requires the relevant expectations.
- Lines 599–633 and 966–986. Clearly distinguish the coefficient bound from the sharpness argument. The coefficients $(1+1/k)^k$ approach $e$. The truncated harmonic sequences show that the best constant actually is $e$. Their numerator divided by their *unweighted* sum tends to $e$, while its ratio to $eH_N$ tends to one. Mention that strictness for every nonzero summable sequence follows from the pointwise strict coefficient bounds.
- Keep the geometric projection of the means and the rectangle's exact deficit. Both figures support a concrete equality case, and the rectangle gives a quantitative comparison beyond the extremal value.

### Chapter 10 · First Probability

- Lines 3–10, 31–49 and 192–194. Give the hat limit as a statement about growing $n$, followed by the numerical closeness at ten guests. State independence in the points game, the dice example and caption, and both two-coin examples. Individually fair dice can be coupled to show the same number on every roll, in which case only six of the 36 ordered pairs occur. The indicator proof of the expectation still works for dependent fair tosses.
- Lines 64 and 648–652. Attribute the birthday thresholds to the exact curve. The exact collision probabilities at $n=22$ and $23$ are about $0.47570$ and $0.50730$. At $n=57$ the exact probability is $0.99012$, while the dashed lower bound is $0.98738$. Keep the solution's separate treatment of $n>365$ and its logarithm comparison proving the bound is below one half at 23.
- Lines 213, 309, 335, and 407. Explain the fixed-point mean as $n$ positions each contributing $1/n$. In the relative-spread paragraph use the absolute mean and assume it is nonzero. Call the $X_i$ indicators of independent coordinate events. In the weak-law recap give the exact root-mean-square gap, $\sqrt n/2$ for the fair coin.
- Lines 356, 466 and 798. Keep the finite-population correction and state the comparison in terms of the sampling variance for uniform samples with the same $p$ and $n$. At line 798 replace the country comparison with this precise result. In the chapter recap say how independent repeated trials fit the weak law and point the polling reader to the separate without-replacement formula.
- Lines 529, 537 and 619. Remove independence from the union-bound exercise or ask the reader whether the bound needs it. In the hint, write $P(\bigcap_i A_i^c)=1-P(\bigcup_i A_i)$. Ask for the record count in a uniform permutation of a million distinct values, the model used in the solution.
- Keep the coupon collector's construction by finite stopping words. It provides a way to calculate the wait within the volume's probability model. The four-decimal agreement in the fixed-point figure, the binomial tail near $7.85\times10^{-5}$, and the balanced six-dice probability near $2.46\times10^{-7}$ all check out.

### A field guide to the next problem

- Lines 68–81. In the integer-polynomial argument, prove the divisibility assertion for distinct inputs and take $k\ge1$ in the progression. Alternatively, handle $k=0$ directly with $m\mid f(a)$. This keeps the argument independent of how divisibility by zero was defined. In the checklist at line 100, say that $w^n=z$ has $n$ distinct roots for positive integer $n$ and nonzero $z$. The zero case has one distinct root.
- Lines 189–196. Start the Fibonacci expansion at $n=4$ because the displayed formula for $L_j$ was introduced at $j=2$. Check $L_2=3$ and $L_3=4$ separately, or first extend the formula to $j=1$ by an explicit calculation.
- Lines 246–251. Use “two one-position rotations” for $0101$. Supply an explicit counterexample to independence of the two pair events on three independent fair bits. Their intersection has probability $5/8$ because the middle bit is either zero or the only one. The product of their separate probabilities is $9/16$. Sharing a coordinate identifies where to look for dependence.
- Keep the two worked problems and the handoff to Volume 2. The failed division by the circle size shows why labelled words and rotation classes yield different counts. The Euler calculation and the general progression show how a local divisibility check can become a proof about infinitely many inputs. Trial division confirms the 40 prime values, and enumeration confirms the circular-word count for $2\le n\le12$.

### Index, credits, cover and sales copy

- **Index.** All 114 index targets resolve, and all 105 hard-coded numbers match their generated references. Use the same cross-reference mechanism for statement numbers and page numbers where the edition supports it, so the numbers update together when exercises or propositions are inserted. Rename “first rules,” “products and sums,” and “the classical laws” to include the probability concepts a reader will look up, such as Bayes's rule, expectation, covariance, and the binomial and hypergeometric laws.
- **Image credits.** The d'Alembert and Erdős attributions in the chapter captions agree with the credits page. Add direct source records for the credited Wikimedia photographs and Hubble release 2012/37, and clarify which image the Flickr reference identifies. Retain the licence names and the distinction between the NASA sources and the repository distributing the two copies.
- **About the Cover.** The Volume 1 source copy and the generated note agree. Recomputing the Collatz steps for each start from 2 through 8,000 confirms that each reaches 1. The orbit from 27 takes 111 steps and reaches 9,232. Clarify that it “first reaches 1” after those steps so “returns” cannot suggest a return to 27.
- **Jacket and listing.** In `blurb.tex`, say the main theorems are proved using the standing assumptions stated in the preface. In the diagnostic example use “99 expected true positives and 495 expected false positives in 10,000 people,” or present an explicitly stipulated table. The chapter already distinguishes the model counts from guaranteed observations. The listing's claim about groups and subgroups is supported by Chapter 5, and all 160 numbered exercises have corresponding hints and solutions.

## Implementation

The revised manuscript repairs the proof steps and definitions in all 11 chapters. Cardano's solution distinguishes repeated and zero roots. The Chebyshev solution proves uniqueness from its earlier interpolation formula. The harmonic threshold now has a check using integer division, and the Newton exercise asks for a sufficient iteration with a specified absolute error. The field guide supplies the joint-probability calculation for circular words. The index uses generated statement references. The jacket gives expected counts for its diagnostic model.

All 160 exercises retain their labels, hints, and solutions. The cross-volume citation checker and the existing prerequisite checks for Volumes 2 and 3 pass after the affected source fingerprints were refreshed. The Volume 2 check confirms all 87 reviewed forward references retain their contexts.

The linked Wikimedia records credit Didier Descouens under CC BY-SA 4.0 and Topsy Kretts under CC BY 3.0. The local portraits match the compositions of the linked files. The credited records for the Collins portrait, the Hubble release, and the Apollo 11 launch resolve. The facsimile of Euler's letter extract confirms that he gives the progression beginning $41,43,47,53$ and says its first 40 terms are prime. This check covers the sources identified here. [d'Alembert](https://commons.wikimedia.org/wiki/File:Maurice_Quentin_de_La_Tour_-_Portrait_de_Jean_Le_Rond_d%27Alembert.jpg) · [Erdős](https://commons.wikimedia.org/wiki/File:Erdos_head_budapest_fall_1992.jpg) · [Collins](https://www.flickr.com/photos/nasacommons/16504233985/) · [Hubble](https://esahubble.org/news/heic1214/) · [Apollo 11](https://images.nasa.gov/details-6900556) · [Euler](https://scholarlycommons.pacific.edu/euler-works/461/)
