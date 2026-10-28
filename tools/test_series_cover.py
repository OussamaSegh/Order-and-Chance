"""Regression guards for the one permitted cover master and its 3D material."""
import math
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from PIL import ImageFont

from check_cover_template import check_subtitle, check_font_sizes
from cover_surfaces import binomial, height_mesh, symmetry_mesh, galton_lattice, projection_saddle, Scene
from cover_surface_renderer import render, visible_edges
from series_cover import ROOT, settings, check_sync, check_titles, subtitle_baseline
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

    def test_every_title_fits_without_changing_font_size(self):
        wrapped=check_titles()
        self.assertEqual(len(wrapped),19)
        self.assertTrue(all(len(lines)<=2 for lines in wrapped.values()))
        self.assertEqual(wrapped['0'],['Mathematical','Maturity'])

    def test_every_subtitle_uses_one_size_and_fits_the_frame(self):
        from series_metadata import subtitles
        data=settings();scale=175/72.27
        font=ImageFont.truetype(str(ROOT/data['subtitle_font']),data['subtitle_size_pt']*scale)
        for number,text in subtitles().items():
            width=(font.getlength(text)+(len(text)-1)*data['subtitle_size_pt']*scale*data['subtitle_tracking']/100)*data['subtitle_stretch']
            with self.subTest(volume=number):self.assertLess(width,5.4*175)
        self.assertEqual(data['subtitle_top_ratio'],.6)
        self.assertEqual(data['subtitle_baseline_source_px'],632.36)
        check_sync()

    def test_subtitle_follows_last_title_line_and_rejects_an_empty_line_gap(self):
        def xml(top):
            return ('<html><word yMin="'+str(top*720)+'">A</word>'
                    '<word>Foundations</word><word>Prelude</word></html>').encode()
        with patch('check_cover_template.subprocess.check_output',return_value=xml(.3928264)):
            check_subtitle('front.pdf','0',720)
        wrong=b'<html><word yMin="282.835008">The</word><word>Language</word><word>of</word><word>Symmetry</word></html>'
        with patch('check_cover_template.subprocess.check_output',return_value=wrong):
            with self.assertRaisesRegex(ValueError,'subtitle moved'):check_subtitle('front.pdf','2',720)
        expected=.3928264+(subtitle_baseline('2')-subtitle_baseline('0'))/1500
        with patch('check_cover_template.subprocess.check_output',return_value=b'<html><word yMin="'+str(expected*720).encode()+b'">The</word><word>Language</word><word>of</word><word>Symmetry</word></html>'):
            check_subtitle('front.pdf','2',720)
        with patch('check_cover_template.subprocess.check_output',return_value=xml(.412)):
            with self.assertRaisesRegex(ValueError,'subtitle moved'):check_subtitle('front.pdf','0',720)

    def test_resized_or_different_title_font_is_rejected(self):
        class Font(dict):
            def get_object(self):return self
        class Contents:
            def __init__(self,size):self.size=size
            def get_data(self):return f'/F1 {self.size} Tf'.encode()
        class Page(dict):
            def __init__(self,size,font):
                super().__init__({'/Resources':{'/Font':{'/F1':Font({'/BaseFont':font})}}});self.size=size
            def get_contents(self):return Contents(self.size)
        size=settings()['title_size_pt']*72/72.27
        check_font_sizes(Page(size,'/ABC+InterDisplay-Bold'),settings())
        for font,size_ in [('/ABC+Inter-SemiBold',size),('/ABC+InterDisplay-Bold',size*.9)]:
            with self.assertRaisesRegex(ValueError,'fixed bold'):check_font_sizes(Page(size_,font),settings())


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

    def test_chance_and_machinery_have_distinct_open_silhouettes(self):
        galton=galton_lattice()
        self.assertEqual(len(galton.faces),55)
        # Galton's lattice is a branching triangle, not the former Gaussian-like hill.
        self.assertGreater(max(p[2] for c in galton for p in c),1.3)
        saddle=projection_saddle()
        self.assertTrue(saddle.faces)
        self.assertLess(min(p[2] for c in saddle for p in c),0)
        self.assertGreater(max(p[2] for c in saddle for p in c),.6)

    def test_symmetry_illustration_is_one_closed_icosahedral_mesh(self):
        scene=symmetry_mesh()
        self.assertEqual(len(scene),20*64)
        self.assertEqual(len(scene.faces),len(scene))
        self.assertTrue(all(curve[0]==curve[-1] for curve in scene))
        for curve in scene:
            for x,y,z in curve:self.assertLessEqual(math.sqrt(x*x+y*y+(z-.2)**2),.700001)


if __name__=='__main__':unittest.main()
