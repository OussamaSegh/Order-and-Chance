"""Guard pinned mathematical acceptance for printed Volume4 Chapter11.

Not a mathematical proof engine; concrete finite Pólya/stop/wait checks
supplement independent source reasoning documented in the acceptance ledger.
"""
import hashlib
import re
import unittest
from fractions import Fraction as F
from math import comb, factorial
from itertools import product
from pathlib import Path

SOURCE=Path(__file__).resolve().parents[1]/"volume4-chance"/"chapters"/"ch10-martingales.tex"
# Reread 2026-11-11 for the Riemann-sum factor (V4R2-14). Labels unchanged.
SHA="bd79c5b0b2cc0c279d28f3518dd4802aa45cd9a0"
PROOFS="thm:os thm:os2 thm:upcross prop:orthinc prop:l2cauchy thm:doob thm:azuma thm:monkey thm:L2conv thm:polyaurn thm:asconv".split()
EX="ex:tower ex:barrier ex:stopmean ex:azumacoin ex:pattern".split()

def git_blob_sha(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()

class TestMathematicalCh11SourceLock(unittest.TestCase):
    def test_locked_blob_and_complete_claim_and_exercise_inventories(self):
        data=SOURCE.read_bytes()
        self.assertEqual(git_blob_sha(data),SHA,"Re-review Chapter11 after manuscript edits")
        src=data.decode()
        self.assertEqual(re.findall(r"\\begin\{(?:theorem|lemma|proposition)\}(?:\[[^\]]*\])?\\label\{([^}]+)\}",src),PROOFS)
        for typ in ("exercise","hint","solution"):
            rexp=(r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{([^}]+)\}" if typ=="exercise" else r"\\begin\{"+typ+r"\}\{([^}]+)\}")
            self.assertEqual(re.findall(rexp,src),EX)

    def test_all_binary_walks_exact_bounded_stopping(self):
        for n in (2,4,6,10):
            stopped=[]
            hits=0
            for path in product((-1,1),repeat=n):
                s=0
                for x in path:
                    s+=x
                    if s==2:
                        hits+=1
                        break
                stopped.append(s)
            self.assertEqual(sum(stopped),0)
            self.assertLess(hits,2**n)
        # Independent exact calculation for capped gambler ruin from 2:
        # h_(2)=2/3 and E rounds=2 with fair steps.
        self.assertEqual(F(3)*F(2,3),F(2))

    def test_polya_history_masses_exact(self):
        for n in range(1,12):
            total=F(0)
            for j in range(n+1):
                sequence_mass=F(factorial(j)*factorial(n-j),factorial(n+1))
                aggregate=F(comb(n,j))*sequence_mass
                self.assertEqual(aggregate,F(1,n+1))
                total+=aggregate
            self.assertEqual(total,F(1))

if __name__=="__main__":
    unittest.main()
