# V3-012 — independent reconstructions before Chapter11 answers

Read the entire main chapter through its ending (source1–674), all11 prompts
(677–752), and actual V1 real Gram–Schmidt/spectral proofs. No C11 hint or supplied
solution has been opened before this record. Its main character-table figure
source still needs a full data read/recomputation. Internal AI reasoning only.
The following answers are first reconstructions, not approval of supplied text.

1. ex:pairs. Fixed two-subset counts on S4 classes e,2,22,3,4 are(6,2,2,0,0).
Weighted inner products with the five known characters give multiplicities
(1,0,1,1,0) in order trivial,sign,degree2,std3,twisted3. Thus1⊕V2⊕V3;
sum dimension6 and all five columns agree. A one-star finite table application.

2. ex:onedim. A homomorphism to C* kills every commutator, so factors uniquely
through G/G'; conversely pullback gives a one-dimensional representation. The
finite abelian dual theorem gives index(G:G') of them. Sn(n≥2) has abelianization
C2, A4 hasC3, A5 is perfect, giving2,3,1. For S2 derivedA2 trivial and result2
still valid. Earlier full derived-subgroup solution was reviewed in C5.

3. ex:a4. Classes e,22,3+,3− sizes1,3,4,4. QuotientA4/V4=C3 gives rows
(1,1,1,1),(1,1,ω,ω²),(1,1,ω²,ω). Permutation4 minus trivial gives(3,−1,0,0),
norm(9+3)/12=1. Four distinct irreducibles exhaust four classes; squares12.
Inverses swap the3-cycle classes, as required by conjugate character values.

4. ex:centralchar. Schur makes every central matrix scalar, and finite order
makes its scalar unit modulus. Orthogonality gives |G|=Σ|χ(g)|²≥|Z|d². ForQ8,
indexcenter4 bounds d≤2. Four one-dimensional characters from Q8/{±1}=V4 and
five classes leave one degree2 character. Classes e,−1,±i,±j,±k sizes1,1,2,2,2:
four linear rows are V4 characters with same value1 on±1; lastrow(2,−2,0,0,0).
Independently realize i=diag(i,−i),j=[[0,1],[−1,0]],k=ij; no common stableline.

5. ex:circulant. With normalized Fourier coefficients and unnormalized finite
convolution, interchange finite sums to get hat(f*g)=n hatf hatg. Eigenvector
χ_m(k) has eigenvalueΣ_a c(a)χ_m(−a)=n hatc(χ_m). Walk stepν=(δ1+δ−1)/2
gives λ_m=cos(2πm/n), hatp_t=λ_m^t/n starting atδ0. Invert finite Fourier to
get convergence for odd n≥3 since all nontrivial absolute eigenvalues<1; actual
largest magnitude is cos(π/n), NOT cos(2π/n). Error≤(n−1)cos(π/n)^t/n.
n1 is stationary singleton, t0 valid; even n has eigenvalue−1/period2. Need
check supplied solution has already earned its absolute-value estimate.

6. ex:dirichlet8. Units8={1,3,5,7}=<3,5>≅C2². Character row indexedu,v=±1
hasvalues(1,u,v,uv), zero offunits. Units12={1,5,7,11}=<5,7> same table.
All real because every unit squares1. For q8,a3,Σχχ(3)χ(n)=4 atn3mod8,
zero onotherresidues; direct four-row check. No analytic infinite sum required.

7. ex:a5. Classes e,22,3,5a,5b sizes1,15,20,12,12. Perm5−1 gives
χ4=(4,0,1,−1,−1); perm10pairs−1−χ4 givesχ5=(5,1,−1,0,0); both norm1.
Five classes leave two irreducibles with squares18, so dimensions3,3. All
classes inverse-closed (inversion exponent4 preserves each5-cycle class), hence
all characters real. Regular and column equations give a+a'=−2,a²+a'²=2 on22,
so both−1; b+b'=0,b²+b'²=0 on3, so both0. On5a, c+c'=1,c²+c'²=3, hence
cc'=−1 and entriesφ,1−φ. Orthogonality totrivial gives c+d=1 for eachrow,
so thetwo3rows are(3,−1,0,φ,1−φ) andits5-columnswap. Existence comes from
the already proved completeness theorem, not merely a guessed orthogonal table.
No future icosahedron/rotation theorem is needed.

8. ex:divides. (a) Ifxmonicdegree m, M=Zspan(1,x,…,x^(m−1)) nonzero/stable.
Conversely with finite generatorsv1…vr ofnonzeroM andxvi=Σaijvj, integerA
hasnonzero vectorv inker(xI−A), so det(xI−A)=0. No free-basis/module theorem
needed. Forx,y algint, finite spanx^iy^j isstableunderx,y, henceunder sum/product.
Rationalrootmonic polynomial gives denominator1. (b) Class sum operatorcentral
so scalarω=|C|χ(g)/d. Integer regular-representation matrixΣ_C L_x hasω as
an eigenvalue on a copy oftheirrep (regular multiplicity theorem), soωalgint;
this avoids requiring an unintroduced abstract group/class algebra. (c) Character
values are sums of rootsunity, hencealgint. Orthogonality gives
|G|/d=Σ_C ω_C χ(g^-1), algint andrational, sointeger. Irreducibled≥1 essential.

9. pb:glnz. (a) C10Niven already earns rationalcosvalues; φ(m)≤2 gives
m1,2,3,4,6. Finite-order integer2matrix diagonalizes overC. Nonreal eigenvalues
areconjugaterootsunity andtrace2cos rational; realeigenvalues±1 giveorder≤2.
(b) Reduceanyhypotheticalfiniteordercongruencematrix toprimeorderℓ. Write
A=I+p^kB,k≥1, Bnotall0modp. Ifℓ≠p, dividebinomialidentitybyp^k andmodp
forcesℓB0. Ifℓ=p, dividebyp^(k+1); allhighertermsdivp forp≥3 (including
k(p−1)−1≥1 onlastterm), againforcesB0. Contradiction. ThusfiniteHinjectsinto
GLnFp; n2,p3 givesorderdiv(9−1)(9−3)=48. p2excludedby−I. (c) Average real
innerproductconjugatesHintoO2R. Rotation subgroup finitecyclic (embedinC*,C9),
det−1elements arereflections andinvertrotations. Thuscyclic/dihedral, mrotation
order≤6 ⇒total≤12. AttainedR=[[0,−1],[1,1]],S=[[0,1],[1,0]], R6=S2=I,
SRS=R^-1,12 distinctelements. Handletrivial/one-reflection/Klein cases explicitly.

10. pb:commutators. Nclassfunction. Averagingconjugatesofρ(y) gives
Σ_x ρ(x)ρ(y)ρ(x^-1)=|G|χ(y)I/d. Multiplybyρ(y^-1),taketrace,sumy to get
Σ_pairsχ([x,y])=|G|²/d fromcharacterorthogonality. Therefore coefficient
<N,χ>=|G|/d; basisexpansion givesformula (conjugation reverses summeddualrows
ifneeded; valueisreal). A5 values on e,22,3,5a,5b are300,32,63,65,65;
weightedtotal3600 andallpositive. evaluealso|G|×numberclasses300.

11. pb:frobschur. Let M=Mat_d(C), T_g(B)=ρ(g)Bρ(g)^T, P=averageT_g,
J(B)=B^T. T is a representation, PprojectsontoinvariantM, andJcommutesP.
Define dualρ*(g)=ρ(g^-1)^T; itscharacterbarχ and itisirreducible (annihilator
ofstableproperdualspacewouldgiveproperstableoriginalspace). InvariantB are
intertwinersV*→V, soSchurgivesdimension0ifχnotreal,1ifχreal. Jacts onthat
one-dimensionalspacebyε=±1. Exactmatrix-unit calculationgivesTr(JT_g)=χ(g²),
soν=Tr(JP) is0/±1, nonzeroiffχreal. Root-countclassfunctionr hascoefficient
<r,χ>=conjν=ν, proving(b). Q8: twosquares=e andsix=−1, soν2=(4−12)/8=−1.
Ifρreal, averagepositive real symmetricformS; S^-1 isfixedsymmetricB, soν1.

The prompt then QUOTES Young's reality theorem for all Sn without a proof. That
cannot be an essential unearned premise under this review's contract. Preserve
and earn both that result and the degree-sum consequence using the following
finite construction (developed here before reading the supplied answer):

Take a real basisvτ indexedbyinvolutionsτ∈Sn. Forπ∈Sn define
πvτ=ε(π,τ)v_(πτπ^-1), where ε is the product, overpairs a<b swappedbyτ,
of sign(π(b)−π(a)). Sortingintermediatepairimages proves the cocycle
ε(πσ,τ)=ε(π,στσ^-1)ε(σ,τ), so thisis anactualreal representation.
Itscharacteratg is the signed sum overinvolutionscommutingwithg. Work separately
on each family ofm cycles ofa fixed lengthℓ in g. Such aninvolutionpairs some
equal-lengthcycles andmayfixothers. A pairhasℓ intertwiningshifts, allsign+1
(orientitsmatchedpairsfromthefirstcycleto thesecond). A singleoddcycle only
hasidentityinvolution, sign+1. A singleevencycle alsohasits halfturn, sign−1,
because g reversesexactlyoneoppositepairorientation in a full cycleofpairs.
Theidentity/halfturn choices cancel, soevenlengthcyclesmustall bepaired.

Now count x withx²=g. Such anxcommuteswithg andpairsitscycles similarly.
A singleℓ-cyclehas exactlyonehalfpowerifℓodd (2k=1modℓ), noneifeven.
A pairoftwocycleshasℓ shiftchoices (their shifts sumto1modℓ). Thus the same
weightedpairingformula counts squareroots andthemodel'scharacter. Explicitly,
foroddℓ the factor isΣ_(j=0..floor(m/2)) m!ℓ^j/((m−2j)!2^j j!);
forevenℓ itis0ifmodd, elsem!ℓ^(m/2)/(2^(m/2)(m/2)!). Products overℓagree.
So r is anactual character. Its coefficientsν are nonnegative integer
multiplicities. Snclasses areinverse-closed, soallχreal, henceν≠0; therefore
allν=1 and r(e)=Σχχ(1), exactlytheinvolutiondegree-sumclaim.

To earn the quotedreal-matrixclaim aswell: ν1 supplies aninvariantnondegenerate
symmetricbilinearformB (inverseofthefixedsymmetricmatrix above). Chooseinvariant
HermitianH linearinfirstargument. DefineantilinearJ byB(v,w)=H(v,Jw).
ItcommuteswithG, soJ²=cIbySchur. Symmetrygives
H(Jv,Jv)=B(Jv,v)=B(v,Jv)=H(v,J²v)=bar(c)H(v,v), makingcpositive real.
NormalizeJ/√c to square1. ItsfixedrealspacehascomplexificationV because
v=(v+Jv)/2+i(v−Jv)/(2i), bothpiecesfixed. A realbasisgivesrealmatrices.
This earnsall intendedparts without importingYoung/Specht theory. Need a full
adversarial second derivation, exact model tests and source attribution before
insertion/acceptance. The supplied full solution remains unread at this record.

Main-route findings to repair: G finite is never made an explicit global
assumption; representationdimension≥1 conflictswithzero subrepresentations/
emptyX. V1 proves only REAL Gram–Schmidt/spectraltheorem, soHermitian definition,
complex orthogonal complements andfinite-order unitary diagonalization mustbe
provedlocally, not borrowedfromits title. The cor:mult proof should not assume
theinitialpartialirreduciblelistiscomplete. The primes-filter prose shouldstart
with finite prime sums andmarkanalyticEulerproducts aslateroutlook. These are
pending; no Chapter11 mathematical acceptance yet.
