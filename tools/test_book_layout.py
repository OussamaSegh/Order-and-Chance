"""Pagination regression: whole boxes, correct moved references, and overflow gates."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest

from pypdf import PdfReader
from pypdf.generic import ContentStream

from check_book_layout import check
from check_interior_style import check as check_style


ROOT = Path(__file__).resolve().parent.parent


class DiagnosticsTest(unittest.TestCase):
    def test_display_faces_match_the_approved_covers_and_font_manifest(self):
        fonts = ROOT / 'common/fonts'
        for name in ('Inter-Light.ttf', 'Inter-SemiBold.ttf', 'Inter-LightItalic.ttf'):
            self.assertEqual((fonts / name).read_bytes(),
                             (ROOT / 'tools/assets/fonts' / name).read_bytes())
        manifest = json.loads((fonts / 'manifest.json').read_text())
        for name, expected in manifest.items():
            with self.subTest(font=name):
                self.assertEqual(hashlib.sha256((fonts / name).read_bytes()).hexdigest(), expected)

    def test_measurements_and_oversized_source_location(self):
        with tempfile.TemporaryDirectory() as directory:
            log, sizes = Path(directory) / 'book.log', Path(directory) / 'book.oclayout'
            log.write_text('All references resolved.\n')
            sizes.write_text('BOX|chapters/ch01.tex|42|200.0pt|610.68pt\n')
            self.assertEqual(check(log, sizes), (1, 200.0))
            sizes.write_text('BOX|chapters/ch01.tex|42|650.0pt|610.68pt\n')
            with self.assertRaisesRegex(ValueError, 'ch01.tex:42'):
                check(log, sizes)

    def test_overflow_and_reference_diagnostics_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            log, sizes = Path(directory) / 'book.log', Path(directory) / 'book.oclayout'
            sizes.write_text('BOX|chapter.tex|10|100pt|610pt\n')
            for diagnostic in [r'Overfull \vbox (1pt too high)',
                               r'Overfull \hbox (2pt too wide)',
                               'Float too large for page', 'There were undefined references',
                               'Label x multiply defined', 'Missing character: no glyph in font',
                               'LaTeX Font Warning: Font shape TU/Math/b/n undefined']:
                with self.subTest(diagnostic=diagnostic):
                    log.write_text(diagnostic)
                    with self.assertRaises(ValueError):
                        check(log, sizes)

    def test_missing_measurements_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            log, sizes = Path(directory) / 'book.log', Path(directory) / 'book.oclayout'
            log.write_text('Clean log')
            sizes.write_text('')
            with self.assertRaisesRegex(ValueError, 'no measured boxes'):
                check(log, sizes)


@unittest.skipUnless(shutil.which('xelatex') and shutil.which('pdftotext'),
                     'TeX and poppler are required for the pagination proof')
class TypesetPaginationTest(unittest.TestCase):
    def compile(self, directory, body, problem_book=False, passes=1):
        source = Path(directory) / 'sample.tex'
        problem_path = 'tomeP1-crossroads' if problem_book is True else problem_book
        source.write_text(r'\documentclass[11pt]{book}' + '\n' +
                          r'\input{../common/preamble}' + '\n' +
                          (f'\\input{{../{problem_path}/pbook}}\n' if problem_path else '') +
                          r'\begin{document}' + '\n' + body + '\n' + r'\end{document}')
        for _ in range(passes):
            result = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                                     '-output-directory=' + directory, str(source)],
                                    cwd=ROOT / 'tome0-mathematical-maturity',
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                    text=True, errors='replace')
            if result.returncode:
                break
        return result

    def test_all_box_types_paint_only_one_vertical_rule(self):
        # Inspect actual PDF painting, not source options: zero-width frames can
        # leave saturated underpainting that leaks through as zoom-dependent seams.
        body = r'''
\pagestyle{empty}
\begin{exercise}[$\star$]Calculate $\sum_{k=1}^n k$.\end{exercise}
\begin{reminder}A useful identity.\end{reminder}
\begin{beauty}A useful connection.\end{beauty}
\begin{think}Try a small example.\end{think}
\begin{challenge}Find another proof.\end{challenge}
'''
        for problem_book in [False, 'tomeP1-crossroads']:
            with self.subTest(problem_book=problem_book), tempfile.TemporaryDirectory() as directory:
                result = self.compile(directory, body, problem_book=problem_book)
                self.assertEqual(result.returncode, 0, result.stdout[-3000:])
                reader = PdfReader(Path(directory) / 'sample.pdf')
                self.assertEqual(len(reader.pages), 1)
                state = {'fill': (0, 0, 0), 'stroke': (0, 0, 0), 'width': 1}
                stack, path, strokes = [], [], []
                for args, op in ContentStream(reader.pages[0].get_contents(), reader).operations:
                    if op == b'q':
                        stack.append(state.copy())
                    elif op == b'Q':
                        state = stack.pop()
                    elif op in (b'rg', b'RG', b'g', b'G'):
                        state['fill' if op in (b'rg', b'g') else 'stroke'] = (
                            tuple(float(v) for v in args) if len(args) == 3 else (float(args[0]),) * 3)
                    elif op == b'w':
                        state['width'] = float(args[0])
                    elif op == b'm':
                        path = [tuple(float(v) for v in args)]
                    elif op in (b'l', b'c', b're'):
                        path.append(tuple(float(v) for v in args))
                    elif op in (b'f', b'f*', b'B', b'B*', b'b', b'b*'):
                        self.assertGreater(min(state['fill']), .9,
                                           'Saturated frame underpainting can expose horizontal seams')
                        path = []
                    elif op == b'S':
                        self.assertEqual(len(path), 2, 'Only one straight rule is permitted per box')
                        self.assertAlmostEqual(path[0][0], path[1][0], places=3,
                                               msg='Unexpected horizontal or diagonal rule')
                        self.assertAlmostEqual(state['width'], 72 / 72.27, places=3)
                        strokes.append(state['stroke'])
                        path = []
                    elif op == b'n':
                        path = []
                expected = ['235E82', 'A34232', '22675B', '704B80', 'A34232']
                self.assertEqual(len(strokes), len(expected))
                for actual, colour in zip(strokes, expected):
                    for value, offset in zip(actual, (0, 2, 4)):
                        self.assertAlmostEqual(value, int(colour[offset:offset + 2], 16) / 255,
                                               delta=.003)
                check(Path(directory) / 'sample.log', Path(directory) / 'sample.oclayout')

    def test_whole_exercise_moves_and_reference_follows(self):
        for problem in [False, True]:
            with self.subTest(problem_book=problem), tempfile.TemporaryDirectory() as directory:
                result = self.compile(directory, r'''
\setcounter{chapter}{1}\pagestyle{plain}
Some preceding text.\par
\vspace{0.7\textheight}
\begin{exercise}[$\star$]\label{ex:moved}
Opening sentence.\par
\rule{0pt}{0.25\textheight}Closing sentence.
\end{exercise}
\begin{exercise}\label{ex:next}The next question.\end{exercise}
See Exercise~\ref{ex:moved}.
''', problem_book=problem, passes=2)
                self.assertEqual(result.returncode, 0, result.stdout[-3000:])
                aux = (Path(directory) / 'sample.aux').read_text()
                self.assertIn(r'\newlabel{ex:moved}{{1.1}{2}', aux)
                self.assertIn(r'\newlabel{ex:next}{{1.2}{2}', aux)
                pdf = str(Path(directory) / 'sample.pdf')
                second = subprocess.check_output(['pdftotext', '-f', '2', '-l', '2', pdf, '-'], text=True)
                self.assertIn('Opening sentence.', second)
                self.assertIn('Closing sentence.', second)
                self.assertIn(('Problem' if problem else 'Exercise') + ' 1.1', second)
                self.assertEqual(check(Path(directory) / 'sample.log',
                                       Path(directory) / 'sample.oclayout')[0], 2)

    def test_box_taller_than_the_page_stops_typesetting(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory,
                                  r'\begin{reminder}\rule{0pt}{1.1\textheight}Too tall.\end{reminder}')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Box exceeds the 7x10 text height', result.stdout)

    def test_solution_heading_stays_with_opening_explanation(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory, r'''
\setcounter{chapter}{1}\pagestyle{plain}
\begin{exercise}\label{ex:solution}A question.\end{exercise}
\clearpage
Preceding text.\par
\vspace{\dimexpr\textheight-5\baselineskip\relax}
\begin{solution}{ex:solution}
\idea This opening explanation needs enough words to occupy several lines
of the final page. It describes the approach before the full argument and
must stay with the solution heading above it.
\writeup The calculation follows.
\end{solution}
''', passes=2)
            self.assertEqual(result.returncode, 0, result.stdout[-3000:])
            text = subprocess.check_output(['pdftotext', str(Path(directory) / 'sample.pdf'), '-'], text=True)
            pages = text.split('\f')
            opening = next(p for p in pages if 'Solution of Exercise 1.1.' in p)
            self.assertIn('This opening explanation', opening)
            check(Path(directory) / 'sample.log', Path(directory) / 'sample.oclayout')

    def test_section_heading_stays_with_first_solution(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory, r'''
\setcounter{chapter}{1}\pagestyle{plain}
\begin{exercise}\label{ex:first}A question.\end{exercise}
\clearpage
Preceding text.\par
\vspace{\dimexpr\textheight-7\baselineskip\relax}
\section*{Collected solutions}
\begin{solution}{ex:first}
\idea The first explanation must travel with its section heading. These words
fill enough of the final measure to occupy more than one line.
\writeup The calculation follows.
\end{solution}
''', passes=2)
            self.assertEqual(result.returncode, 0, result.stdout[-3000:])
            text = subprocess.check_output(['pdftotext', str(Path(directory) / 'sample.pdf'), '-'], text=True)
            page = next(p for p in text.split('\f') if 'Collected solutions' in p)
            self.assertIn('Solution of Exercise 1.1.', page)
            self.assertIn('The first explanation', page)
            check(Path(directory) / 'sample.log', Path(directory) / 'sample.oclayout')

    def test_locally_reenabled_split_box_stops_typesetting(self):
        with tempfile.TemporaryDirectory() as directory:
            body = (r'\begin{tcolorbox}[enhanced,breakable]' + '\n' +
                    ('This paragraph must not be cut into a second frame.\\par\n' * 100) +
                    r'\end{tcolorbox}')
            result = self.compile(directory, body)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('A framed box was split across pages', result.stdout)

    def test_colour_math_fonts_and_unicode_code_symbols(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory, r'''
\section{Colour mathematics and $\sigma$-algebras over $\R$}
\begin{exercise}
Show that $\sum_{k=1}^n k=n(n+1)/2$; compare $\N,\Q,\R,\C$.
Also test $\int_\R f(x)\,\mathrm{d}x$, $A\otimes_\R\C$ and $x^\N$.
The vector $\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_k)$ uses a bold alphabet.
The letter-pattern frieze $\textsf{VΛVΛ}$ keeps its upright Greek lambdas.
\end{exercise}
\begin{reminder}A useful identity.\end{reminder}
\begin{verbatim}
ℚ ∣ ∧ ∨ ≠ ≤ ⟨a, b⟩
\end{verbatim}
''')
            self.assertEqual(result.returncode, 0, result.stdout[-3000:])
            check(Path(directory) / 'sample.log', Path(directory) / 'sample.oclayout')
            check_style(Path(directory) / 'sample.pdf')

    def test_grayscale_override_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory, r'''
\colorlet{ocExercise}{black}\colorlet{ocReminder}{black}\colorlet{ocAccent}{black}
\section*{Grayscale regression}
\begin{exercise}Calculate $\int_0^1x^2\,\mathrm{d}x$.\end{exercise}
\begin{reminder}A useful identity.\end{reminder}
''')
            self.assertEqual(result.returncode, 0, result.stdout[-3000:])
            with self.assertRaisesRegex(ValueError, 'missing colour accents'):
                check_style(Path(directory) / 'sample.pdf')


if __name__ == '__main__':
    unittest.main()
