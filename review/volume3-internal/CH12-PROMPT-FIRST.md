# V3-013 — Chapter12 first reconstructions and exposure limits

Internal AI working record, not acceptance. Read the full main chapter and all15
prompts in printed order. The source-range read also exposed every hint, the
complete ex:compose answer and the opening of ex:euler4 before this record.
Therefore no claim of blinded independence from hints or that first answer is
made. The other thirteen supplied solutions remain unopened at this record;
their first reconstructions below precede comparison. Main figures still need
actual data/source review. Source is the original C12 at9aa217f3.

1. ex:compose. qx qz=(1+i−j+k)/2, angle120 degrees, axis(1,-1,1)/sqrt3.
The reversed product is(1+i+j+k)/2, neither the same nor its negative, so the
induced rotations differ even after quotienting by{+1,-1}. Coordinate matrices
give e1→e3,e2→−e1,e3→−e2, fixing e1−e2+e3. Supplied answer already read;
second reconstruction will compare full matrices and both orders. One star.

2. ex:euler4. Product coordinates scalar aa'−bb'−cc'−dd'; i coefficient
ab'+ba'+cd'−dc'; j coefficient ac'−bd'+ca'+db'; k coefficient
ad'+bc'−cb'+da'. Norm multiplicativity gives the four squares. B should expand
all polynomial coefficients independently or compare actual matrices; any real
eight coordinates, zero factors included. One star; answer opening already seen.

3. ex:rotmatrix. Columns of q i qbar etc give
[[a²+b²−c²−d²,2(bc−ad),2(bd+ac)],
 [2(bc+ad),a²−b²+c²−d²,2(cd−ab)],
 [2(bd−ac),2(cd+ab),a²−b²−c²+d²]].
For unit q, trace4a²−1; a=cos(theta/2) gives1+2cos theta. B compare matrix
products/composition and determinant1, q and−q, axes/half turns. Two stars.

4. ex:conjS3. Conjugation fixes real part and rotates the imaginary vector.
Equal real parts on S3 mean equal imaginary lengths; surjectivity onto SO3
moves any nonzero direction to the other. Real quaternions±1 are singleton
cases. For rotations choose theta in[0,pi], lift with real cos(theta/2)>=0;
same angle iff conjugate. B trace class invariant and explicit axis transport.
At pi, axis sign is immaterial, at0 any axis works. Two stars.

5. ex:2T. Use the24-element set of norm1 Hurwitz lattice points, or prove
closure from explicit generators i and omega=(1+i+j+k)/2 and their cosets.
Need not borrow the later unproved H-ring statement circularly. All576 products
can be checked exactly, supporting a displayed finite closure argument. Kernel
±1 gives12-image. Six pure units pair to three half turns; sixteen half-units
give eight order3 rotations. The finite-rotation classification plus no order6
rotation excludes cyclic/dihedral12, so A4; alternatively act on four tetrahedral
vectors. Two stars. Verify generator closure rather than merely cardinality.

6. ex:2I. Surjective restriction with kernel2 gives120. If q=a+x satisfies
q²=1, imaginary part2ax=0. Ifa0 then−|x|²=1 impossible; otherwise x0 andq±1.
Unique element of exact order2 is−1. S5 has ten transpositions and fifteen
double transpositions; A5×C2 has many involutions, so neither is isomorphic.
Two stars; cannot use order alone to distinguish S5.

7. ex:hurwitz. Z-basis1,i,j,omega=(1+i+j+k)/2 gives the union lattice;
check all generator products explicitly for closure. Half-coordinate norm
integer because four odd squares sum0mod4; conjugation preserves lattice.
Norm1 gives exactly eight integral units and sixteen half units. Coordinate
rounding gives distance-squared<=1, equality only if every error has absolute1/2,
when x itself lies in half lattice, so choose x. Left division chooses q near
a b^-1, remainder(a b^-1−q)b, norm<norm b. Minimal positive norm in nonzero left
ideal earns principal ideal; zero ideal is H0. For odd prime p choose integer
alpha=1+xi+yj with norm divisiblep, alpha notinpH. I=Hp+Halpha=Hdelta:
normdelta dividesp². I proper: if1=sp+talpha, multiply on right by alphabar
to force alphabar inpH, impossible from real coefficient1. Normdelta≠p²,
else p=u delta with normu1 impliesI=Hp, contradiction alpha. Thusnormdelta=p.
If half-integral, choose a norm1 half unit u whose four numerator signs agree
with delta's odd numerators mod4. Then delta−u has even integer coordinates,
and delta ubar=1+(delta−u)ubar has integer coordinates and unchanged normp.
Include p2 separately; multiplicativity gives all positive integers, zero trivial.
Actual V2 residue-pigeonhole proof must be reopened; don't cite its title. Three stars.

8. pb:sylvester. Greedy n=ceil(b/a), remainder numerator an−b satisfies
0<=an−b<a, even before reduction, so numerator strictly decreases to0. If
positive, remainder<1/n forces later denominators strictly larger.4/13=1/4+1/18+1/468.
Recurrence s_(k+1)−1=s_k(s_k−1) telescopes reciprocals, and later terms1mod
earlier s_j yield pairwise coprime. For c putu=s−1/2, u_next=u²+1/4.
Logs a_k=2^(-k−1) logu_k increase and are bounded by2^(-k−1) logs_k<=log2/2.
LimitlogE>0. For u=u_k>=1.5,
log(E^(2^(k+1))/u)=sum_(r>=0)2^(-r−1)log(1+1/(4u_(k+r)²))
is positive and <=1/(4u²). Thus u<Epower<=u exp(1/(4u²))<u+1
(e.g. exp(t)<=1/(1−t), t<=1/9 gives difference<=3/16).
Rounding by+1/2 yields s_k. Need earn the log bound and limiting manipulation
from actual V1 monotone/geometric comparison proofs; supply local finite bounds.
Two→three stars plausible for the convergence/rounding part; reassess actual answer.

9. pb:jensen. Product factors into nth-root polynomials and their conjugates,
giving x^(2n)−2x^n cos(n theta)+1. At theta0 take log/n: mean of
log(1−2xcos(2pi k/n)+x²) equals2log|1−x^n|/n, tends0 for|x|<1 and
2log|x| for|x|>1. To turn this into the integral, locally construct the needed
Riemann integrals for Lipschitz functions: common refinements bound sum error by
M times interval-length times mesh, so sums Cauchy and same limit for all tags.
Derivative of this log function is uniformly bounded because denominator>=
(|x|−1)²>0; MVT supplies Lipschitz. This earns this particular integral without
future V7 analysis. Symmetry halves the2pi integral. Each factor e^itheta−z
is a translate of a radial factor; translation invariance follows by shifted
partitions for periodic Lipschitz functions. Half-log gives logmax(1,|z|), finite
linearity gives Jensen. For integer P with no unit-circle root, zero mean forces
leading coefficient±1 and all roots modulus<1; strip zero roots and use actual
Kronecker to conclude P=±X^r. Without the no-unit-circle restriction, discussing
cyclotomic factors would also require earning integrable log singularities;
do not silently include that extension. Three stars because local analysis is needed.

10. pb:mersennediv. For primeq|2^p−1, order2modq=p, so2p|q−1. Since
2=(2^((p+1)/2))²modq, quadratic supplementary law givesq±1mod8. Ifp3mod4
andq2p+1 prime, q7mod8, Euler criterion gives2^p1modq.11,23,83 yield
prime factors23,47,167. Need reopen actual V2 Euler/supplement proofs. One star.

11. pb:dice. All labels distinct so action free:720/24=30. Opposite-pair
constraints give3!*2³=48 assignments, quotient24 gives2. Reflection cannot
agree with rotation on a full numbering, because their composite would be
an orientation-reversing orthogonal map fixing every face normal, hence identity,
contradiction.15 mirror pairs, standard dice one mirror pair. One star.

12. pb:ksubsets. Burnside on pairs(k-set,l-set) counts orbits by intersection
size0..min(k,l) sincek+l<=n. Average product of fixed-point characters is
min+1. Differences chi_k=pi_k−pi_(k−1) are integral virtual characters of norm1,
mutually orthogonal; positive binomial-difference degree forces+irreducible,
since an integral sum with squared coefficient sum1 has exactly one±1.
Alternatively use known lower constituents/actual Maschke complements inductively.
Restrict each actual chi_j to G, invariant dimension is its character average>=0;
pi_k cumulative sum implies monotone orbit count. n0,k0 and middle boundary
included. Three stars; no norm criterion for arbitrary class functions.

13. pb:egz. Product indicator product_j(1−f_j^(p−1)) has degree< m(p−1).
Finite monomial sums vanish since some variable exponent<p−1 (including exponent0),
so common-zero count0modp. For2p−1variables andtwo degree(p−1) forms, zero vector
is a common zero, so another exists. Its support size is positive multiplep,
atmost2p−1, hencep; coefficients x_i^(p−1) are1 there. Generalmn: extract
2m−1 disjoint n-subsets with sums divisible n, possible since before the last
extraction2n−1 entries remain. Divide group sums byn and apply m theorem;
union of m groups hasmn elements and divisiblemn sum. Induct on integer n via
prime factors, n1 trivial. Sharp n>=2: n−1zeros plus n−1ones; n1 empty list
also cannot provideone entry. Zero polynomials/empty systems require precise
degree convention in parta. Two stars after C9 worked Chevalley–Warning.

14. pb:abelian. Fundamental finite abelian structure givesA(n)=product p(e).
Nonnegative partition generating functions produce Dirichlet product for s>1.
Need locally earn convergence/rearrangement, not borrow later analytic number
theory: dyadic geometric bounds prove zeta(s) finite, and zeta(ks)−1 decays
geometrically, so positive finite products bounded; cofinal finite sums justify
reordering. WriteA=1*g with g from factorsk>=2. Splitg=square-indicator*h,
h fromk>=3; C=sum h(v)/sqrtv=product_(k>=3)zeta(k/2)<infinity. Therefore
G(y)=sum_(d<=y)g(d)<=C sqrt y. Then sum_(n<=x)A(n)=sum_(d<=x)g(d)floor(x/d),
floor error<=C sqrtx, tail x sum_(d>x)g(d)/d<=C' sqrtx by dyadic blocks.
Main constantc=sum g(d)/d=product_(k>=2)zeta(k)≈2.29485659. A naive use of
sum g(d)/sqrt d diverges, so cannot justify the claimed error that way. All
finite/infinite bounds must be written; likely grade3. Actual C7 classification
and V1 sequence/geometric series proofs must be read at precise sites.

15. pb:dodecaturns. For central mu, Schur average operator scalar
lambda_chi=sum mu(h)chi(h)/d. Finite convolution corresponds to operator products;
character coefficients then give general inversion with conjugate chi(g).
t0 needs lambda^0=1 even whenlambda0 (identity matrix power). On3-cycle,
lambdas1,0,0,1/4,−1/5. Thus for t>=1 returnprob=(1+16*4^-t+25*(−1/5)^t)/60.
At t0 original displayed answer gives42/60, not1: must explicitly separate t0
or include18*0^t with0^0=1. For t>=1 event fifth-turn probability is
(24/60)(1−4*4^-t)=2/5(1−4^(1−t)); t1 zero, limit2/5, t0 zero separately.
Every density difference O(4^-t), and the fifth-turn event difference
(8/5)*4^-t proves the rate is actually attained in total variation. Need define
rate/TV if used; no later Markov theorem needed. Hardcoded theorem12.5 and
Exercise11.7 should become stable labels. Three stars.

Main-route pending findings: SO(3) notation needs a definition before use;
every unit quaternion needs the c+su parametrization (including±1) before the
orientation conclusion, rather than an unearned connectedness argument. A
two-to-one homomorphism alone is not yet a topological covering theorem; plate
trick and spin/fundamental-group claims are currently unproved outlook.
Dropping associativity alone does not classify all real division algebras as
R,C,H,O: positive multiplicative norm hypotheses are missing. Earn regular-solid
attainability and conjugacy of isomorphic rotation subgroups rather than treating
an upper bound as existence. The closing description of A5 as the smallest
nonabelian simple group and broad category/600-cell claims need real proof or
honest outlook qualification. No C12 approval at this first record.

Subsequent comparison note (preserving the original first derivation above):
all supplied answers and both figure sources have now been read. My part15
first count24 included both five-cycle classes, hence both fifth- and
two-fifths-turn rotations. The prompt's fifth turn in either direction has
only12 rotations, and the supplied partc count and coefficient1/5 are correct.
The return formula's t0 qualification still needs to be explicit in the prompt.
The general and finite direct-walk second check will use the correct event.
