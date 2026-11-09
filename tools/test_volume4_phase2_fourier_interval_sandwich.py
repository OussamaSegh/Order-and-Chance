"""Independent exact-arithmetic validation of Fourier inversion's interval sandwich.

Finite rational quadrature is exact here: the test density is piecewise
linear and every trapezoidal cutoff is piecewise linear, so products are
piecewise quadratic and Simpson integration is exact. These tests exercise
the *two-sided event approximation*, not Fourier inversion in general.
"""
from fractions import Fraction as Q
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "volume4-chance/chapters/ch06-clt.tex"


def cutoff_lower(x, a, b, h):
    if x <= a or x >= b:
        return Q(0)
    if x < a + h:
        return (x-a)/h
    if x > b-h:
        return (b-x)/h
    return Q(1)


def cutoff_upper(x, a, b, h):
    if x < a-h or x > b+h:
        return Q(0)
    if x < a:
        return (x-a+h)/h
    if x <= b:
        return Q(1)
    return (b+h-x)/h


def density(x):
    return 2*x if Q(0) <= x <= Q(1) else Q(0)


def exact_integral(cutoff, a, b, h):
    points = sorted(set([Q(0),Q(1),a-h,a,a+h,b-h,b,b+h]))
    ans = Q(0)
    for lo,hi in zip(points,points[1:]):
        if hi <= Q(0) or lo >= Q(1) or lo == hi:
            continue
        lo,hi = max(lo,Q(0)),min(hi,Q(1))
        mid = (lo+hi)/2
        f = lambda t: cutoff(t,a,b,h)*density(t)
        ans += (hi-lo)*(f(lo)+4*f(mid)+f(hi))/6
    return ans


class TestFourierInversionIntervalSandwich(unittest.TestCase):
    def test_manuscript_supplies_two_cutoffs_and_density_nonnegativity(self):
        src = SOURCE.read_text(encoding="utf-8")
        proof = src.split(r"\label{thm:inversion}",1)[1].split(
            r"\end{proof}",1)[0]
        self.assertIn(r"f\ge0", proof)
        self.assertIn(r"g^-_\varepsilon", proof)
        self.assertIn(r"g^+_\varepsilon", proof)
        self.assertIn(r"\mathbf1_{\{a<x\le b\}}", proof)
        self.assertIn("Squeezing proves the required identity", proof)
        self.assertIn("does not conceal atoms at its endpoints", proof)

    def test_two_sided_pointwise_cutoff_bounds(self):
        for a,b in ((Q(1,4),Q(3,4)),(Q(0),Q(1)),
                    (Q(-1,2),Q(1,2)),(Q(1,3),Q(2,3))):
            for h in (Q(1,64),Q(1,32),Q(1,16)):
                if 2*h >= b-a:
                    continue
                values = {a-h,a,a+h,b-h,b,b+h}
                values.update(Q(j,128) for j in range(-128,257))
                for x in values:
                    lo,up = cutoff_lower(x,a,b,h),cutoff_upper(x,a,b,h)
                    event = int(a < x <= b)
                    self.assertLessEqual(Q(0),lo)
                    self.assertLessEqual(lo,event)
                    self.assertLessEqual(event,up)
                    self.assertLessEqual(up,Q(1))

    def test_cutoff_integrals_squeeze_exact_density_interval_mass(self):
        # The density 2x on [0,1] has exact interval mass b^2-a^2
        # for the nonnegative a,b chosen here.
        for a,b in ((Q(1,4),Q(3,4)),(Q(1,3),Q(2,3)),
                    (Q(1,10),Q(9,10))):
            exact = b*b-a*a
            previous_gap = None
            for h in (Q(1,8),Q(1,16),Q(1,32),Q(1,64),Q(1,128)):
                if 2*h >= b-a:
                    continue
                lo = exact_integral(cutoff_lower,a,b,h)
                hi = exact_integral(cutoff_upper,a,b,h)
                self.assertLessEqual(lo,exact)
                self.assertLessEqual(exact,hi)
                self.assertGreaterEqual(hi,lo)
                gap = hi-lo
                if previous_gap is not None:
                    self.assertLess(gap,previous_gap)
                previous_gap = gap
                self.assertLessEqual(gap, Q(4)*h)  # f<=2; two strips
            self.assertLess(previous_gap,Q(1,32))

    def test_continuous_density_has_no_end_point_atom(self):
        # The mass of an arbitrarily narrow symmetric interval around
        # a is bounded by 2*(2h) for density 2x<=2.
        for a in (Q(0),Q(1,2),Q(1)):
            prev = None
            for h in (Q(1,8),Q(1,16),Q(1,32),Q(1,64)):
                lo=max(Q(0),a-h);hi=min(Q(1),a+h)
                mass=hi*hi-lo*lo
                self.assertLessEqual(mass,Q(4)*h)
                if prev is not None:
                    self.assertLess(mass,prev)
                prev=mass


if __name__ == "__main__":
    unittest.main()
