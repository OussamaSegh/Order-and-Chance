# Volume 3 round-4 fix, second reading

Mathematics confirmed at `fc9808b6c104d39489094ec528faf3b496926de9`. This note does not change the mathematics. No LaTeX build was run for this reading. The ledger hashes in that commit were recomputed from the edited files. `registers.py` and the chapter checkers passed. One prose block in the quaternion chapter was re-keyed because its text changed; the previous review of that block was kept, and the note on it says so.

A draft of the cap-set comparison treated \(1000^3\cdot10000\) as \(10^{12}\). That comparison is false. The committed paragraph uses \(145/102\), and the products \(27552\cdot102=2810304\), \(19381\cdot145=2810245\), \(145^3=3048625\), \(102^3=1061208\), and \(3048625\cdot3481=10612263625>10612080000\) were recomputed on the committed text.

| Check | Result |
| --- | --- |
| \(t^2+t-1=0\) and \(2\cos72^\circ>0\) select \((\sqrt5-1)/2\) | Closed |
| When \(r=1\), the left side is the empty product and the right side is the unit \(u\) | Closed |
| \(GL_2(\Z)\) carries the column lattice of \(T\) onto that of \(UT\) | Closed |
| The trace sum is \(3(a^2-\lvert x\rvert^2)+2\lvert x\rvert^2=3a^2-\lvert x\rvert^2\), then \(4a^2-1\) | Closed |
| A formula for every quintic is defined at the coefficients of \(X^5-4X+2\) | Closed |
| Fisher: \(\lambda=\lvert A_i\cap A_j\rvert\le\lvert A_i\rvert\), with \(m\ge2\) already assumed | Closed |
| Cap-set constant, integers above | Closed |

No numbered statement moved. No claim was weakened.
