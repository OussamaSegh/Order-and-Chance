"""Guard mathematical content and the shared luminous illustration treatment."""
import re
import unittest

from cover_finish import luminous_plate
from cover_motifs import galton_board, sierpinski_carpet


class CoverMaterialTest(unittest.TestCase):
    def test_probability_and_fractal_paths_keep_every_coordinate(self):
        geometry = lambda text: re.findall(
            r'^\\(?:draw|filldraw|fill)\[.*\](.*)$', text, re.M)
        for source in (galton_board(rows=10, balls=18), sierpinski_carpet(level=3)):
            finished = luminous_plate(source)
            self.assertEqual(geometry(source), geometry(finished))
            self.assertIn('preaction=', finished)
            self.assertNotIn('includegraphics', finished)

    def test_secondary_comparison_curve_remains_distinct(self):
        source = ('\\draw[accent,line width=.65pt] (0,0)--(1,2);\n'
                  '\\draw[ocInk,line width=.65pt] (0,1)--(1,3);')
        finished = luminous_plate(source).splitlines()
        self.assertIn('draw=ocCoverLight,draw opacity=1.000', finished[0])
        self.assertIn('draw=ocCoverCoral,draw opacity=1.000', finished[1])
        self.assertIn('(0,1)--(1,3);', finished[1])

    def test_histogram_remains_filled_with_lit_edges(self):
        finished = luminous_plate(
            '\\fill[accent,opacity=.55] (0,0) rectangle (1,2);')
        self.assertIn('\\filldraw[', finished)
        self.assertIn('fill=ocCoverCoral,fill opacity=', finished)
        self.assertIn('draw=ocCoverLight', finished)
        self.assertTrue(finished.endswith('(0,0) rectangle (1,2);'))


if __name__ == '__main__':
    unittest.main()
