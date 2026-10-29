"""Regression guards for the shared cover family and the retired wireframe model."""
import math
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from check_cover_template import check_font_sizes
from cover_surfaces import binomial, height_mesh, symmetry_mesh, galton_lattice, projection_saddle, Scene
from cover_surface_renderer import render, visible_edges
from series_cover import ROOT, settings, check_sync, cover_notes
from check_cover_pdf import check_cover_log, check_back_copy


class SharedMasterTest(unittest.TestCase):
    def test_missing_back_text_or_substituted_font_cannot_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'cover.log'
            for message in ['Missing character: There is no L in font nullfont!',
                            'Some font shapes were not available', 'Overfull \\hbox (4pt too wide)']:
                path.write_text(message)
                with self.assertRaises(ValueError):check_cover_log(path)
            path.write_text('Output written on cover.pdf (1 page).')
            check_cover_log(path)

    def test_back_blurb_is_checked_separately_from_front_copy(self):
        with patch('check_cover_pdf.subprocess.check_output',return_value='ORDER AND CHANCE VOLUME 0'):
            with self.assertRaisesRegex(ValueError,'blurb is missing'):check_back_copy('wrap.pdf')
        with patch('check_cover_pdf.subprocess.check_output',return_value='Actual back blurb words. '*40):
            check_back_copy('wrap.pdf')

    def test_plates_notes_and_shared_rules_match_the_generator(self):
        check_sync()
        notes=cover_notes()
        self.assertEqual(set(notes), {str(n) for n in range(1,16)})
        for number, row in notes.items():
            words=len(row['about'].split())
            self.assertGreaterEqual(words, 80)
            self.assertLessEqual(words, 150)
            self.assertIn('TikZ cover generator', row['about'])
        lettering=(ROOT/'volume1-first-principles/cover-lettering.tex').read_text()
        self.assertIn('lower-rule y=2.9500in', lettering)
        self.assertIn('fontsize{42}{46}', lettering)
        offsets=__import__('json').loads((ROOT/'tools/covergen/centring.json').read_text())['volumes']
        series={round(row['SERIES'], 6) for row in offsets.values()}
        self.assertEqual(len(series), 1)

    def test_title_must_be_cormorant_regular_at_42pt(self):
        class Font(dict):
            def get_object(self):return self
        class Contents:
            def __init__(self,size):self.size=size
            def get_data(self):return f'/F1 {self.size} Tf'.encode()
        class Page(dict):
            def __init__(self,size,font):
                super().__init__({'/Resources':{'/Font':{
                    '/F1':Font({'/BaseFont':font}),
                    '/F2':Font({'/BaseFont':'/CormorantGaramond-SemiBold'}),
                    '/F3':Font({'/BaseFont':'/CormorantGaramond-Medium'}),
                    '/F4':Font({'/BaseFont':'/FiraSans-Light'})}}})
                self.size=size
            def get_contents(self):return Contents(self.size)
        size=42*72/72.27
        check_font_sizes(Page(size,'/CormorantGaramond-Regular'))
        for font,size_ in [('/InterDisplay-Bold',size),('/CormorantGaramond-Regular',size*.9)]:
            with self.assertRaisesRegex(ValueError,'Cormorant Garamond Regular'):
                check_font_sizes(Page(size_,font))


class WireframeModelTest(unittest.TestCase):
    def test_smooth_binomial_surface_preserves_integer_probabilities(self):
        for n in (8,12,32):
            self.assertAlmostEqual(sum(binomial(n,k,.55) for k in range(n+1)),1.,places=12)
            for k in range(n+1):
                self.assertAlmostEqual(binomial(n,k,.55),math.comb(n,k)*.55**k*.45**(n-k),places=12)

    def test_hidden_surface_cells_and_renderer_stay_vector(self):
        scene=height_mesh(lambda x,y:math.exp(-3*(x*x+y*y)),n=7)
        text,info=render(scene)
        self.assertEqual(info['space'],'3D')
        self.assertEqual(info['opaque_surface_cells'],36)
        self.assertEqual(info['shared_camera'],settings()['camera'])
        self.assertEqual(info['hidden_lines'],'depth-tested-before-glow')
        self.assertEqual(info['glow'],'five-layer-vector-radiance')
        self.assertNotIn('includegraphics',text)
        self.assertNotIn('node[',text)

    def test_glow_cannot_restore_occluded_rear_wire(self):
        scene=Scene([[(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,-1,1)],
                     [(-.5,0,0),(.5,0,0)]],faces=[0])
        segments,_=visible_edges(scene,lambda p:(10+10*p[0],10+10*p[1]),lambda p:p[2])
        self.assertTrue(segments)
        self.assertTrue(all(p[2]==1 for curve in segments for p in curve))

    def test_galton_lattice_has_real_probability_columns(self):
        galton=galton_lattice(n=10)
        self.assertEqual(len(galton.faces),55)
        # Galton's lattice is a branching triangle, not the former Gaussian-like hill.
        self.assertGreater(max(p[2] for c in galton for p in c),1.3)

    def test_symmetry_illustration_is_one_closed_icosahedral_mesh(self):
        scene=symmetry_mesh()
        self.assertEqual(len(scene),20*64)
        self.assertEqual(len(scene.faces),len(scene))
        self.assertTrue(all(curve[0]==curve[-1] for curve in scene))
        for curve in scene:
            for x,y,z in curve:self.assertLessEqual(math.sqrt(x*x+y*y+(z-.2)**2),.700001)


if __name__=='__main__':unittest.main()
