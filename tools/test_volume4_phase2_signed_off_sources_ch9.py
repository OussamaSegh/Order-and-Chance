"""Guard exact source behind Volume 4 printed Chapter 9 math acceptance.

Exact model enumeration gives independent finite checks; it is not a proof of
general convergence of finite irreducible aperiodic Markov chains.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import re
import unittest

SOURCE=Path(__file__).resolve().parents[1]/"volume4-chance"/"chapters"/"ch08-markov.tex"
SHA="ddfc2e52756052755a0d26437b782f104c069a3f"
PROOFS="lem:period thm:stationary lem:coupling thm:ergodic prop:hit3 thm:top lem:tvcontract thm:bayerdiaconis prop:rifflecompose prop:untouched".split()
EX="ex:lazy ex:twostate ex:ehrenfest ex:pagerank ex:metropolis ex:toptorandom ex:hitbefore ex:risingmean ex:period".split()

def source_git_sha(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()

def rising_sequences(deck):
    # Count descents in the inverse permutation, not adjacent deck positions.
    pos={v:i for i,v in enumerate(deck)}
    return 1+sum(pos[i+1]<pos[i] for i in range(1,len(deck)))

def ashuffle(deck,word):
    """Forward inverse-label description: input packets are consecutive chunks
    determined by label counts, and word says which packet supplies each slot."""
    a=max(word)
    counts=[word.count(k) for k in range(1,a+1)]
    packets=[]
    start=0
    for n in counts:
        packets.append(list(deck[start:start+n]))
        start+=n
    indices=[0]*a
    out=[]
    for k in word:
        k-=1
        out.append(packets[k][indices[k]])
        indices[k]+=1
    return tuple(out)

class TestMarkovMathematicalAcceptedBlob(unittest.TestCase):
    def test_all_proofs_exercises_hints_solutions_locked(self):
        data=SOURCE.read_bytes()
        self.assertEqual(source_git_sha(data),SHA,"Re-review accepted math on changed source blob")
        tex=data.decode()
        self.assertEqual(re.findall(r"\\begin\{(?:theorem|proposition|lemma)\}(?:\[[^\]]*\])?\\label\{([^}]+)\}",tex),PROOFS)
        for typ in ("exercise","hint","solution"):
            pattern=(r"\\begin\{exercise\}(?:\[[^\]]*\])?\\label\{([^}]+)\}" if typ=="exercise"
                     else r"\\begin\{"+typ+r"\}\{([^}]+)\}")
            self.assertEqual(re.findall(pattern,tex),EX)

    def test_bayer_diaconis_probability_with_exhaustive_shuffle_words(self):
        for n in range(2,6):
            cards=tuple(range(1,n+1))
            for a in range(1,5):
                counts=Counter(ashuffle(cards,word) for word in product(range(1,a+1),repeat=n))
                self.assertEqual(sum(counts.values()),a**n)
                for deck,cnt in counts.items():
                    r=rising_sequences(deck)
                    expected=comb(a+n-r,n) if r<=a else 0
                    self.assertEqual(cnt,expected,(n,a,deck,r))
                # More strongly check *every* permutation, including unreachable ones.
                from itertools import permutations
                for deck in permutations(cards):
                    r=rising_sequences(deck)
                    self.assertEqual(counts.get(deck,0),
                                     comb(a+n-r,n) if r<=a else 0)

    def test_exact_two_state_and_stationary_52_card_moment(self):
        for p,q in ((F(1,2),F(1,4)),(F(1),F(1)),(F(3,5),F(2,5))):
            pi0=q/(p+q)
            mu=F(1)
            for n in range(15):
                self.assertEqual(abs(mu-pi0),p/(p+q)*abs(1-p-q)**n)
                mu=mu*(1-p)+(1-mu)*q
        n=52
        self.assertEqual(F(n+1,2),F(53,2))
        self.assertEqual(F(n+1,12),F(53,12))
        self.assertLess(F(53,675),F(1,10))

if __name__=="__main__":
    unittest.main()
