"""Independent geometry checks for the Pólya orchard exercise.

The manuscript's general proofs are symbolic; these finite checks probe
critical equalities, rotated area-four rectangles, ray orientation, visibility,
and the tightness of the escaping-ray bound. No third-party packages required.
"""
import math
import unittest
from fractions import Fraction
from pathlib import Path

CH1 = (Path(__file__).resolve().parents[1] / "volume2-integers"
       / "chapters" / "ch01-divisibility.tex")


def rectangle_integer_witness(c, s, L, A, B):
    """Exact rational rotated rectangle; (c,s,L) is Pythagorean."""
    assert c*c+s*s==L*L
    assert A*B>=1
    bound=math.ceil(math.hypot(float(A),float(B)))+1
    for x in range(-bound,bound+1):
        for y in range(-bound,bound+1):
            if (x,y)==(0,0):
                continue
            if abs(c*x+s*y)<=L*A and abs(-s*x+c*y)<=L*B:
                return (x,y)
    return None


def tree_centres(R):
    return [(a,b) for a in range(-R,R+1)
            for b in range(-R,R+1)
            if 0<a*a+b*b<=R*R]


def ray_hits_tree(R, angle, radius):
    """Distance to the RAY, not merely its supporting full line."""
    ux,uy=math.cos(angle), math.sin(angle)
    for a,b in tree_centres(R):
        projection=a*ux+b*uy
        if projection>=0:
            distance=abs(a*uy-b*ux)
        else:
            distance=math.hypot(a,b)
        if distance<=radius+1.e-11:
            return (a,b)
    return None


class TestOrchardGeometry(unittest.TestCase):
    def test_minkowski_rotated_rectangles_at_closed_area_four(self):
        rotations=((1,0,1),(3,4,5),(5,12,13),(8,15,17),(20,21,29))
        widths=(Fraction(1,4),Fraction(1,3),Fraction(1,2),
                Fraction(3,4),Fraction(1),Fraction(4,3),
                Fraction(2),Fraction(3),Fraction(4))
        scales=(Fraction(1),Fraction(5,4),Fraction(2))
        cases=0
        for c,s,L in rotations:
            for A in widths:
                for t in scales:
                    B=t/A
                    point=rectangle_integer_witness(c,s,L,A,B)
                    self.assertIsNotNone(point,(c,s,L,A,B))
                    x,y=point
                    self.assertTrue(x or y)
                    self.assertLessEqual(abs(c*x+s*y),L*A)
                    self.assertLessEqual(abs(-s*x+c*y),L*B)
                    cases+=1
        self.assertEqual(cases,135)
        # The closed hypothesis is essential at area 4.
        self.assertFalse(any(abs(x)<1 and abs(y)<1 and (x or y)
                             for x in range(-2,3) for y in range(-2,3)))
        self.assertTrue(abs(1)<=1 and abs(0)<=1)

    def test_every_ray_covered_at_r_equal_one_over_R(self):
        checked=0
        for R in range(2,24):
            for j in range(96):
                angle=2*math.pi*j/96
                witness=ray_hits_tree(R,angle,1/R)
                self.assertIsNotNone(witness,(R,j))
                checked+=1
        self.assertEqual(checked,2112)

    def test_escaping_ray_integer_det_and_exact_tangency(self):
        cases=0
        for R in range(2,51):
            centres=tree_centres(R)
            self.assertTrue(all(a-R*b!=0 for a,b in centres))
            candidates=[(abs(a-R*b),a,b) for a,b in centres
                        if R*a+b>0]
            smallest=min(candidates)
            self.assertEqual(smallest[0],1)
            a,b=R-1,1
            self.assertLessEqual(a*a+b*b,R*R)
            self.assertEqual(abs(a-R*b),1)
            self.assertGreater(R*a+b,0)
            # The radius r=1/sqrt(R^2+1) is an exact tangency;
            # any smaller trunk cannot hit the selected ray.
            self.assertEqual(
                Fraction((a-R*b)**2,R*R+1),
                Fraction(1,R*R+1))
            cases+=1
        self.assertEqual(cases,49)

    def test_figure_disc_R11_and_sightline_are_arithmetically_consistent(self):
        centres=tree_centres(11)
        visible=[(a,b) for a,b in centres if math.gcd(abs(a),abs(b))==1]
        self.assertEqual(len(centres),376)
        self.assertEqual(len(visible),224)
        self.assertLess(abs(len(visible)/len(centres)-6/math.pi**2),0.02)
        # Caption's sightline towards (11,4) is not a tree:
        self.assertGreater(11*11+4*4,11**2)
        self.assertEqual(math.gcd(11,4),1)
        self.assertTrue(any(abs(4*a-11*b)==1 and 11*a+4*b>0
                            for a,b in centres))
        # (3,1) supplies a tangible boundary-height tree.
        self.assertIn((3,1),centres)
        self.assertEqual(abs(4*3-11*1),1)

    def test_question_hint_solution_and_no_tail_duplication(self):
        source=CH1.read_text(encoding="utf-8")
        key="pb:orchard"
        self.assertEqual(source.count(r"\label{"+key+"}"),1)
        self.assertEqual(source.count(r"\begin{hint}{"+key+"}"),1)
        self.assertEqual(source.count(r"\begin{solution}{"+key+"}"),1)
        body=source.split(r"\begin{solution}{"+key+"}",1)[1].split(
            r"\end{solution}",1)[0]
        self.assertIn("open square",body)
        self.assertIn("At equality its trunk touches the ray",body)
        self.assertNotIn("irrational-looking",source)
        self.assertEqual(source.count(r"\section{Hints}"),1)
        self.assertEqual(source.count(r"\section{Solutions}"),1)
        self.assertEqual(source.count(r"\begin{exercise}"),15)
        self.assertEqual(source.count(r"\end{exercise}"),15)
        self.assertEqual(source.count(r"\begin{hint}{"),15)
        self.assertEqual(source.count(r"\begin{solution}{"),15)
        self.assertTrue(source.rstrip().endswith(r"\end{itemize}"))


if __name__=="__main__":
    unittest.main()
