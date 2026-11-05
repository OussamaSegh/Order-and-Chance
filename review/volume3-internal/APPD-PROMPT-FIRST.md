# V3-017 — Hadamard matrices: first solutions before answers

Solo internal AI record, not mathematical acceptance. At1fe85903 read all
original paley.tex main lines1–423 and both prompts426–433 BEFORE opening any
D hint/answer. This record precedes the supplied solutions and any supporting
finite computations. All actual main proofs have been read once, not approved.

1. ex:paley-h4. Two doublings give rows
(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1).
First dot third is1+1-1-1=0. Every row has squared length4. B: multiply
all six distinct pairs directly; each has exactly two matches/two mismatches.
Different structural proof indexes rows/columns by F2^2: each nonzero row
label difference has a binary coordinate with1; pair columns differing in
that coordinate, cancelling the row inner product. k0/1 base cases direct.
One star retained: explicit small arithmetic after full doubling proof.

2. ex:paley-f3. Order field elements0,1,2. Character values0,1,-1. Then
Q rows(0,-1,1),(1,0,-1),(-1,1,0), since Qxy=chi(x-y), not chi(y-x).
The first construction H=I+S has rows
(1,1,1,1),(-1,1,-1,1),(-1,1,1,-1),(-1,-1,1,1).
Every row has four signs, hence squared length4. The last three have sum0,
and their pairwise products sum(-1+1-1+1),(-1-1+1+1),
(-1-1-1? recheck explicitly before acceptance): use their actual coordinates,
not an inherited sign identity. Directly rows2dot3=1+1-1-1=0,
rows2dot4=1-1-1+1=0,rows3dot4=1-1+1-1=0.
Thus HHT=4I. B: normalize first column by negating lower three rows, then
permute/re-sign to the Sylvester matrix, or reconstruct S^2=-3I independently.
Two stars retained for assembling the border/sign convention, not new theory.
The rough intermediate product above was explicitly replaced by direct correct
coordinate products before any answer exposure; do not report it as a book error.

## Main adversarial leads before answer comparison

Positive real sign matrices n>=1 should be explicit; n0 conventions are not
needed. Necessary4-divisibility proof is sound: normalize first row, compare two
other rows and all four column types; n1/2 exceptions direct. Sylvester statement
currently calls the displayed S_(2^(k+1)) family order2^k in one sentence;
rewrite the induction indices explicitly. Kronecker block identities are valid,
but give the index sum once and the exact binary-index induction for Walsh rows.

Character lemma is valid over every odd prime-power field. Its integer-valued
sign character and all resulting matrices live over R, not in characteristicp.
Partd source uses x inversion and a bijection onto Fq without1. Independent B:
count pairs u²=t(t+c); q+sum chi(t(t+c)) equals q-1 because
(2t+c-2u)(2t+c+2u)=c² has exactly q-1 factor pairs, all invertible maps as
2,c are nonzero. This avoids the source's inverse substitution.

Jacobsthal identities recheck all diagonals/offdiagonals, transpose sign and
row/column cancellation. Independent B uses the action of additive translations
or direct Gram rank, plus the independent correlation count. PaleyI full block
product signs are correct: Sskew, SST=qI, HHT=(q+1)I. PaleyII symmetricS with
S²=qI, H=[[S+I,S-I],[S-I,-S-I]] has both diagonal blocks2(q+1)I and commuting
cross blocks0. Entries all real signs even on every diagonal. Probe q3/5 and
nonprime q9/27, q1excluded since not a prime power, characteristic2 excluded.
Preserve both full general constructions; finite calculations support them.

Opening current Hadamard research sentence asserts independent verification.
Our earlier reading of a new paper's intro/table does not independently verify
new matrices or the research proof. Refresh actual paper text and qualify the
claim as a dated attributed report/nonpremise, without certifying the proof.
Original mathematical proofs otherwise appear sound; no defect inferred merely
because a rewritten proof is longer or a primary historical attribution pending.
