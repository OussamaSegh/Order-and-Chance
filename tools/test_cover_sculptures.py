"""Mathematical meaning of the selected cover objects, independently of rendering."""
import math
import unittest
from unittest.mock import patch
from cover_sculptures import collatz_tree, plancherel_partition, sobolev_kernel, bernoulli_convolutions


class CoverMathematicsTest(unittest.TestCase):
    def test_collatz_sculpture_is_the_actual_depth_13_inverse_tree(self):
        children,points,levels=collatz_tree()
        self.assertEqual(len(points),61)  # Same finite tree stated in the book's caption.
        self.assertEqual(sum(map(len,children.values())),60)
        for parent,descendants in children.items():
            for child in descendants:
                self.assertEqual(child//2 if child%2==0 else 3*child+1,parent)
                self.assertEqual(levels[child],levels[parent]+1)
        self.assertEqual(max(levels.values()),13)

    def test_plancherel_diagram_keeps_all_600_boxes(self):
        partition=plancherel_partition()
        self.assertEqual(sum(partition),600)
        self.assertEqual(partition,sorted(partition,reverse=True))
        self.assertTrue(all(n>0 for n in partition))

    def test_machinery_uses_the_books_sobolev_kernel(self):
        with patch('cover_sculptures.height_mesh',side_effect=lambda f,**kwargs:f):f=sobolev_kernel()
        self.assertAlmostEqual(f(-1,1),1/math.sinh(2))
        self.assertAlmostEqual(f(0,0),math.cosh(1)**2/math.sinh(2))
        self.assertAlmostEqual(f(-1,-1),math.cosh(2)/math.sinh(2))
        for x,y in [(-.7,.2),(.1,.6),(-.8,-.3)]:self.assertAlmostEqual(f(x,y),f(y,x))

    def test_displayed_bernoulli_convolutions_remain_symmetric_probability_laws(self):
        with patch('cover_sculptures.height_mesh',side_effect=lambda f,**kwargs:f):f=bernoulli_convolutions()
        for y in (-1,0,1):
            for x in (.1,.4,.8):self.assertAlmostEqual(f(x,y),f(-x,y),places=8)
            values=[f(-1+k/24,y) for k in range(49)]
            integral=(sum(values)-.5*(values[0]+values[-1]))*(2.16/48)
            self.assertAlmostEqual(integral,1,delta=.03)


if __name__=='__main__':unittest.main()
