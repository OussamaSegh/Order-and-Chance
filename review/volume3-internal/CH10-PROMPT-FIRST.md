# V3-011 — first reconstructions before Chapter10 answers

The main chapter and all11 prompts, lattice and quintic figure sources were read.
No C10 hints/solutions have been opened in this pass. Exception: ex:phin and
pb:kronecker full solutions were already read during the C7 migration; their
reconstructions below are fresh reasoning with that prior exposure disclosed.
This is internal AI evidence, not a blinded or human review.

1. ex:q235. C10's already proved biquadratic example classifies the three
quadratic subfields of Q(sqrt2,sqrt3) as Qsqrt2,Qsqrt3,Qsqrt6. Qsqrt5 is none:
equality Qsqrt a=Qsqrt b forces a/b a rational square by comparing coefficients,
which prime-exponent parity excludes. Hence adjoining sqrt5 gives degree8.
Splitting field has all eight sign choices and group F2³. Index2 subgroups are
seven kernels of nonzero linear forms, yielding sqrt2,3,5,6,10,15,30; order2
subgroups are seven nonzero lines, yielding seven degree4 fields. Every quadratic
listed is fixed by the corresponding sign-product kernel. Potential grade2.

2. ex:x42check. Write automorphisms r^a s^b with a mod4,b mod2,
(a,b)(c,d)=(a+(-1)^b c,b+d). Stabilizers of alpha,i alpha,(1+i)alpha,
(1-i)alpha are respectively <s>,<r²s>,<rs>,<r³s>. Their fourth powers are
2,2,-8,-8. First two have degree4 by Eisenstein X4−2; latter two square to
±2i sqrt2, generating Q(i sqrt2), and that square is not itself a square in
Q(i sqrt2): (a+b i sqrt2)²=2i sqrt2 would force a²−2b²=0,2ab=2,
impossible rational a/b=sqrt2. Hence degree4. Fixed <r²> is Q(sqrt2,i),
degree4. Order4 subgroups <r²,s>,<r>,<r²,rs> fix Qsqrt2,Qi,Q(i sqrt2)
respectively. Include top L and bottomQ. Only H={1},<r²>, the three order4
subgroups and whole D4 are normal: six Galois fields. Four reflection-fixed
quartics nonnormal. Qalpha real lacks i alpha, a conjugate, directly notnormal.
Need recompute all actual diagram edges against subgroup/field inclusions.

3. ex:zeta7. Group C6 has unique subgroups of orders2,3, hence only degrees3,2
proper subfields. Conjugation fixes zeta+zeta^-1=2cos(2pi/7); zeta solves
X²−(zeta+zeta^-1)X+1, not real, so real field degree3. For A={1,2,4},
eta=sum zeta^A, eta'=sum zeta^{3,5,6}, eta+eta'=-1. Ordered pair sums in A²
give eta²=eta+2eta'=-eta−2. Thus eta²+eta+2=0 irreducible discriminant−7,
quadratic Qsqrt(-7). Different direct exponent enumeration supports identity.

4. ex:gauss17. Enumerate powers3^k modulo17: even powers form the eight
nonzero squares A, odd B. Sums total−1. Count A+B ordered pairs: no zero sums
because−1 is a square, and each of16 nonzero residues occurs4 times. Hence
eta0 eta1=4 sum_(nonzero)zeta^r=−4, and roots of T²+T−4 are(−1±sqrt17)/2.
The unordered assertion suffices; identifying plus with eta0 needs an additional
real sign estimate, not simply the quadratic equation.

5. ex:sp. Degree p irreducible gives p|group order, Cauchy p-cycle; conjugation
is a transposition. Power of p-cycle carries its first endpoint to second and
remains a p-cycle since p prime. Conjugating then gives adjacent transpositions.
p2 case is already S2; p3 gives S3, no false nonsolvability until p>=5. For
g=X5−6X+3, Eisenstein3. g(-2)=-17,g(0)=3,g(1)=-2,g(2)=23 give three crossings;
g'=5X4−6 has two critical points, so Rolle gives no fourth. Irreducible char0
means distinct roots, so exactly two nonreal. GroupS5 excludes radicals.

6. ex:discr. Any root permutation sends alternating productdelta to sign·delta,
so delta² fixed by every Gal element and lies inK by FTGT. Because delta!=0,
delta fixed iff allpermutations even; fixedfieldK gives criterion. Discriminant
identity by elementary resultant or expanding viar1+r2+r3=0; cubic X3−2 has
disc−108 nonsquare, X3−3X+1 hasdisc81 square. Both irreducible by rational-root
test; transitive degree3 subgroupS3 versusA3 gives groupsS3,C3. No claim in
characteristic2 (chapter's characteristic0 contract explicit).

7. ex:cardano. uv=sumri²−sum_(i<j)rirj=−3p because sumri0. u+v=3r1, so
u³+v³=(3r1)³−3uv(3r1)=27(r1³+pr1)=−27q. Thus A=u/3,B=v/3 satisfyAB=−p/3,
A³+B³=−q,A³B³=−p³/27. Their cubes are−q/2±sqrt(q²/4+p³/27).
Choose cube roots correlated by AB, not independently; p0 requires a zero
radicand paired with zero cube root and other root chosen to give r1, repeated
roots/discriminant0 allowed. Three branch choices supply all roots. Real-root
formula may need complex intermediate radicals (casus irreducibilis).

8. ex:phin (prior solution exposure). Partition roots by exact order to get
Xn−1=∏d|n Phi_d. Monic longdivision and induction gives integer coefficients.
Minimal f of primitive zeta is monic integer by Gauss and dividesPhi_n; g=Phi/f
monic integer. If beta rootf but beta^p notrootf, then rootg; f|g(Xp).
Modulo p, fbar|gbar^p, so some irreducible factor of fbar dividesgbar as well,
forcing repeated factor ofPhi_bar dividingXn−1, impossible p∤n/derivative.
Thus raising by any prime notdividingn preserves rootf; factoring any positive
unit representativea givesall primitive zeta^a rootsf. degf>=phi_n and divides
Phi gives equality. n1 f=X−1; reduction never zero since monic. Injection
cyclotomic group and degree phi_n givesisomorphism. This proof must be earlier
than the main text's general degree/equivalence and later problem invocations.

9. pb:kronecker (prior solution exposure). For eachm>=1, P_m=∏(X−alpha_i^m)
has bounded integer coefficients, hence finitely many possibilities. To earn
integrality without a future symmetric-function theorem: use integer companion
matrixA ofP, whose characteristic roots are alpha_i; C7 Jordan triangularizesA,
so det(XI−A^m)=P_m∈Z[X]. Two positiveindicesu<v haveequalP. Match multisets
alpha_i^u=alpha_pi(i)^v. Around a permutation cycle oflengthl, alpha_i^(u^l)
=alpha_i^(v^l), and nonzeroalpha_i isrootunity. Irreducibility then gives its
cyclotomic minimal polynomial fromearnedPhi proof. Degree0P1vacuous. Partb
Q=X^dP(X+X^-1) monicintegerdegree2dconstant1; roots solveZ²−aZ+1forreal
a∈[-2,2], soallmodulus1includinga±2. Theirunitrootsgivea=2cos2pir.
Partc zrootprimitiveg=5X²−6X+5, discriminant−64, so irreducibleQ. IfzN1,
gdivX^N−1overQ; Gauss forprimitiveintegerg makesquotientinteger, impossible
leadingcoeff5div1. Missingmonicity/integeralgebraicnumber condition, notmodulus.

10. pb:rattan. Ifζm∈Qζn, compositumQζlcm(m,n)=Qζn (Bezout on exponents),
so phi(lcm)=phi(n). Inprimefactorphi formula, enlargingalready-presentprime
exponents multipliesbyprime; addingnewprimeq givesq^(b−1)(q−1). Equality
allows onlyadding2tooddnwith exponent1. Hence ordersdivide n ifeven,2nifodd;
converseobvious(ζ2n=−ζn^((n+1)/2) foroddn, up tocheckedexponent: actually
−ζn^((1−n)/2) givesζ2n; use −ζn^((n+1)/2) gives exponent2π*(n+1)/(2n)+π
=π/n mod2π, also correct). For rationaltan t, e2iθ=(1+it)/(1−it)∈Qi and
rootunity, hence fourthroot; finite t gives0,±1. Integerpolygon's successive
nonzerosidevectors inZ[i] havequotientprimitiveζn∈Qi, so n>=3forces4; square
exists. Niven: defineS0=2,S1=X,Sm+1=XS_m−S_m−1, monicintegerSmfor m>=1,
Sm(2cosθ)=2cosmθ. Choosemθ∈2πZ; rational2cosθ isrationalrootofmonicSm−2,
henceintegerin[-2,2]. Avoid unprovedC11algebraic-integerclosure.

11. pb:ramacube. Let a,b,c be the threecosines, roots of8X³+4X²−4X−1,
so a+b+c=−1/2,ab+bc+ca=−1/2,abc=1/8. Withreal u³a,v³b,w³c, uvw=1/2;
S=u+v+w,T=uv+vw+wu giveS³=3ST−2 andT³=(3/2)ST−5/4.
PutZ=S³: T³=Z/2−1/4; multiplyingbyZandusing(ST)³ gives
4Z³−30Z²+75Z+32=0, equivalent(2Z−5)³=−189. Uniquereal cube root yields
Z=(5−3cuberoot7)/2 and the stated identity. No division byS orT, no branch
ambiguity. Need earn thecosinecubic from(ζ7sum=0) or triple-angle, not a future
algebraic-integer premise. Independent numericinterval check can corroborate.
