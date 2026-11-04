# Chapter 3 prompt-first reconstruction, V3-004

All14 prompts read; supplied hints/solutions not opened before this record.
These are internal AI calculations/reconstructions, not human independence.

- ex:cubefaces: cube face cycles and multiplicities: 1^6(1),1²4(6),1²2²(3),
  3²(8),2³(6). Burnside at3 gives(729+162+243+72+162)/24=57.
- ex:fermatnecklace: C_p orbits of nonconstant p-letter words have sizep,
  while k constants are fixed. Thus p divides k^p-k, including k0.
- ex:classesD: D4 classes {e},{r²},{r,r³},{s,sr²},{sr,sr³}; Q8 classes
  {1},{-1},{i,-i},{j,-j},{k,-k}. Both class equations 8=1+1+2+2+2.
- ex:p2: nontrivial center has orderp orp². Orderp would give cyclic quotient
  orderp and force abelian by C2, hence full center. If no orderp² element,
  choose independent orderp elements to obtain Cp x Cp with p² distinct products.
- ex:smallestprime: finite G required. Coset action gives G->S_p with transitive
  image, so p divides image size. Image divides |G| andp!, whose only common
  possible prime is smallest p and whose p-adic exponent is1. Thus image orderp,
  kernel indexp equalsH (kernel<=H since fixesH), so H normal.
- ex:bracelets: three opposite-vertex reflections each fix2^4=16 words; three
  opposite-gap reflections fix2³=8. Rotation sum84 gives(84+48+24)/12=13.
  Unique reversal pair of canonical words001011/001101 independently enumerated.
- ex:graphs4: action on6 edges has cycles1^6(1),1²2²(6 transpositions+3 double
  transpositions),3²(8),24(6). Count(64+9*16+8*4+6*4)/24=11. Weighted coefficient
  t³: (20+9*4+8*2+6*0)/24=3 (star,path,triangle+isolated vertex).
- ex:commuting: sum centralizers/|G|² = k(G)/|G| by one |G| per class.
  If nonabelian, G/Z cannot be cyclic, hence has at least4 elements; z<=n/4.
  Each noncentral centralizer<=n/2, so probability<=z/n+(1-z/n)/2<=5/8.
  D4 has5 classes in8 and attains it.
- pb:sieving: factorial quotient recurrence after clearing factors uses
  [n]=[k]+q^k[n-k]. Boundary0 conventions needed. Product identity
  product(1+q^r t)=sum q^(k(k-1)/2)[n choose k]_q t^k follows by induction.
  At primitive mth root, block product=1-(-t)^m, repeated n/m times. If k=ml,
  coefficient sign(-1)^(l(m+1)) cancels the phase zeta^(k(k-1)/2): both1 for
  oddm, both(-1)^l for evenm. If m does not dividek, coefficient0. g^j cycles
  lengthm=n/gcd(n,j); choose k/m cycles fromn/m. Average gives
  (1/n)sum_{d|gcd(n,k)}phi(d) binom(n/d,k/d); n6k3 gives(20+2*2)/6=4.
- pb:patterns: along a g-cycle of lengthl, f(gx)=s f(x), hence the starting colour
  must be fixed bys^l. Exactlysum_{j|l}j c_j(s) choices; different cycles
  independent. Binary colour exchange allows extra fixed words precisely when
  all rotation cycles have even lengthd. Formula(1/(2n))sum_{d|n}phi(d)2^(n/d)
  (1+indicator_{2|d}); n6 gives8. Cube colour-permutation classes id/trans/3cycle
  give fixed-count triples by face type: (729,1,0),(27,3,0),(81,9,0),(9,1,9),
  (27,27,0). Weight by24 cube rotations and1,3,2 colour multiplicities;
  numerator2160/144=15. Independent signed-coordinate/colour orbit enumeration
  also gives15; this is a finite support check, not proof of the general formula.
- pb:landau: class equation normalized gives1=sum_{i=1}^k 1/a_i with centralizer
  orders sorted a1<=...<=ak=|G|. Remaining positive rational afteri-1 terms has
  denominator dividingP=product earlier a, hence >=1/P; it is <=k/a_i,
  so a_i<=kP. Induct P_i<=k^(2^i-1), giving ak<=k^(2^(k-1)). Finite tables per
  bounded order give finite many groups. k1=>trivial; k2 Egyptian tuple(2,2)=>C2;
  k3 tuples(3,3,3),(2,4,4),(2,3,6) give C3, impossible nonabelian order4, S3.
  For the last: Cauchy supplies normal index2 C3 and an involution outside;
  noncommuting conjugation inverts, so D3=S3. No Sylow needed.
- pb:nilpotent: let K be a supplied finite field withq elements; do not presume
  earlier existence for every prime power. Kernel chains stabilize byn; if
  A^(2n)v=0 then A^n v=0, hence kerA^n intersectimA^n=0. Rank-nullity gives
  sumV, restrictions nilpotent/invertible. On any other stable nilpotent part,
  its nilpotency index<=dimension<=n, so it lies inkerA^n; invertible part lies
  in every image and thus inimA^n. Unique. Ordered decompositions dimk,n-k are
  |GLn|/(|GLk||GL(n-k)|), by choosing ordered bases and quotienting the two
  independent basis changes. Counting A then dividing gives sumN_k/GLk=R_n,
  R_n=q^(n²)/GLn=product_{i=1}^n(1-q^-i)^-1. Subtraction givesN_n/GLn=R_n q^-n,
  henceN_n=q^(n²-n). At n0 handle N0=GL0=1 separately. I+nilpotent is invertible
  by finite geometric inverse, so unipotent count equalsN_n.
- pb:flags: choose first1-space (q^n-1)/(q-1), then flag quotient of dimensionn-1,
  giving[n]_q!. Given one complementW0 toU, all complements are graphs of
  unique linear maps W0->U, henceq^(k(n-k)). GLn transitive on flags by adapted
  bases, stabilizer invertible upper triangular matrices gives(q-1)^n q^binom(n,2).
  q1 specializations are symbolic: flags become orderings n!, complements become
  the unique set complement, and Sn has ordern!. Do not assert a fieldF1 exists.
- pb:touchard: rotate the p distinguished points. Fixed partitions either have
  one invariant block containing all distinguished points (B_(n+1) choices),
  or put them in p singleton blocks (B_n choices). Reason: a block touching a
  fixed old point must be invariant, so either includes all p moving points or
  none; otherwise moving-only blocks have orbitp (singletons) or are invariant
  (all p). Nonfixed partition orbits have sizep. Handles n0 andp2.

Second pass will check all implications, denominators, zero/empty conventions,
star grades and the supplied discovery/write-up, without treating these counts
as approval of the yet-unread source solutions.
