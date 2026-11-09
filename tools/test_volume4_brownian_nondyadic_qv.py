"""Regression for Brownian quadratic variation at non-dyadic time.

The exact rational calculations test the finite-dyadic-prefix argument and
endpiece control; they are not the general proof of Brownian quadratic variation.
"""
from fractions import Fraction as F
from math import floor, sin, sqrt
from pathlib import Path
import unittest

SOURCE=Path(__file__).resolve().parents[1]/"volume4-chance"/"chapters"/"ch11-brownian.tex"

class TestNonDyadicBrownianQVProof(unittest.TestCase):
    def test_source_proves_final_interval_separately_from_finite_normal_vector(self):
        txt=SOURCE.read_text(encoding="utf-8")
        qv=txt.split(r"\label{thm:qv}",1)[1].split(r"\end{proof}",1)[0]
        self.assertIn(r"t_n=2^{-n}\lfloor2^nt\rfloor",qv)
        self.assertIn(r"V_n+(B_t-B_{t_n})^2",qv)
        self.assertIn(r"\operatorname{Var}(V_n)=2t_n2^{-n}",qv)
        self.assertIn("when $t$ is not dyadic",qv)
        self.assertIn("the original uniform sample",qv)
        self.assertNotIn("These preimages cover the deviation event",qv)

    def test_prefix_and_residual_exact_partition_variance(self):
        # Each dyadic increment is independent N(0,h); its square has
        # mean h and variance 2h². The shorter final interval has variance l.
        for t in (F(0),F(1,3),F(5,7),F(7,11),F(1)):
            for n in range(1,13):
                h=F(1,2**n)
                count=(t/h).numerator//(t/h).denominator
                t_n=count*h
                residue=t-t_n
                self.assertTrue(0<=residue<h or residue==0)
                self.assertEqual(t_n+residue,t)
                prefix_mean=t_n
                prefix_variance=2*count*h*h
                full_variance=prefix_variance+2*residue*residue
                self.assertEqual(prefix_variance,2*t_n*h)
                self.assertLessEqual(full_variance,2*t*h)
                self.assertLessEqual(residue*residue,h*h)

    def test_continuous_path_last_increment_tends_to_zero(self):
        # Deterministic witness to the continuity part of the reasoning.
        for t in (F(1,3),F(5,7),F(2,3)):
            errors=[]
            for n in range(2,17):
                tn=F((t*2**n).numerator//(t*2**n).denominator,2**n)
                errors.append(abs(sin(float(t))-sin(float(tn)))**2)
                self.assertLessEqual(errors[-1],2**(-2*n)+1.e-14)
            self.assertLess(errors[-1],errors[0]+1.e-12)

if __name__=="__main__":
    unittest.main()
