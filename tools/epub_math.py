"""Render EPUB mathematics as baseline-aligned PNG for Kindle.

Pandoc's ``--mathml`` output is real MathML. Calibre and a browser lay that
out on the text baseline. Send-to-Kindle does not. It runs the formula through
MathJax, keeps an SVG, then stores Amazon's KVG picture. That picture is
smaller than the body and sits high: the converter never reads the formula's
depth, and Kindle ignores CSS on the ``math`` element. The photos of Volume 1
on a Paperwhite are that conversion.

KF8 and KFX do honor ``width`` and ``vertical-align`` on a PNG, in em. Each
formula is set with the book's Garamond-Math face, measured with TeX, and
shipped as a transparent PNG whose width is the TeX width in em and whose
``vertical-align`` is the TeX depth (plus a hair of padding) below the
baseline. Empty columns on the right of that bitmap are cropped and the
width shrinks with them, so a following period or comma is not stranded
after a transparent margin. The ink then sits on the same line as the
surrounding words, and both the size and the shift follow the reader's
font size.

SVG math would repeat the figure bug: Kindle treats an SVG viewBox as pixels
and often drops ``vertical-align``. Exact alignment on the Paperwhite is the
CSS alignment above, to the pixel grid. It is not MathML's native baseline,
because the device never lays the MathML out.
"""
from __future__ import annotations

import hashlib
import html
import os
import posixpath
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, replace
from pathlib import Path

import epub_png


REPO = Path(__file__).resolve().parent.parent
BORDER_PT = 0.4
# The book em is 11.5 pt, 48 device pixels on a 300 ppi screen. 600 ppi would
# be two device pixels per em, and with full-colour 1800 px plates that still
# put the largest volume over the 50 MB Send-to-Kindle mail limit. 480 ppi is
# 77 px per em, about 1.6 device pixels on each body pixel, and leaves headroom
# under 50 MB. The CSS size stays the TeX em either way.
DPI = 480
WIDE_EM = 22.0
CACHE_TAG = "v6"
# HTML width/height are CSS pixels at the usual 16 px em. Moon+ uses those
# attributes and ignores em widths, so a high-dpi PNG otherwise draws huge.
CSS_PX_PER_EM = 16
INTRINSIC_SCALE = 2.5

MATH_RE = re.compile(r"<math\b([^>]*)>(.*?)</math>", re.S)
RAW_RE = re.compile(r'<span class="math (inline|display)">\s*(.*?)\s*</span>', re.S)
ANNOTATION_RE = re.compile(
    r'<annotation\b[^>]*\bencoding="application/x-tex"[^>]*>(.*?)</annotation>',
    re.S,
)

HEADER = r"""\documentclass[11pt]{article}
\usepackage{mathtools}
\input{../common/interior-fonts.tex}
\usepackage[active,tightpage]{preview}
\setlength{\PreviewBorder}{0.4pt}
% Braces keep \R^\N and \int_\R from applying the superscript to \mathbb alone.
\newcommand{\N}{{\mathbb{N}}}
\newcommand{\Z}{{\mathbb{Z}}}
\newcommand{\Q}{{\mathbb{Q}}}
\newcommand{\R}{{\mathbb{R}}}
\newcommand{\C}{{\mathbb{C}}}
\newcommand{\dd}{\,\mathrm{d}}
\providecommand{\square}{\mdlgwhtsquare}
\newcommand{\stirlingii}[2]{\genfrac{\{}{\}}{0pt}{}{#1}{#2}}
\newcommand{\stirlingi}[2]{\genfrac{[}{]}{0pt}{}{#1}{#2}}
\newcommand{\qbinom}[2]{\begin{bmatrix}#1\\#2\end{bmatrix}_q}
\newwrite\ocmetrics
\immediate\openout\ocmetrics=metrics.txt
\newcommand{\ocship}[2]{%
  \setbox0=\hbox{\input{#2}}%
  \immediate\write\ocmetrics{#1,\the\ht0,\the\dp0,\the\wd0,\the\dimexpr1em\relax}%
  \begin{preview}\copy0\end{preview}}
\begin{document}
"""

FOOTER = r"""\immediate\closeout\ocmetrics
\end{document}
"""


class MathRenderError(RuntimeError):
    pass


@dataclass(frozen=True)
class Glyph:
    png: bytes
    width_em: float
    depth_em: float
    height_em: float
    display: bool

    def _px(self, em: float) -> int:
        return max(1, int(round(em * CSS_PX_PER_EM)))

    def html(self, src: str, alt: str) -> str:
        alt_attr = html.escape(" ".join(alt.split()), quote=True)
        src_attr = html.escape(src, quote=True)
        width_px = self._px(self.width_em)
        height_px = self._px(self.height_em)
        height = f"{self.height_em:.4f}"
        if self.display and self.width_em >= WIDE_EM:
            style = (
                f"display:inline-block;width:100%;max-width:100%;height:auto;max-height:{height}em;"
                f"vertical-align:middle"
            )
            kind = "oc-math-display"
        elif self.display:
            style = (
                f"display:inline-block;width:{self.width_em:.4f}em;height:{height}em;"
                f"max-width:100%;max-height:{height}em;vertical-align:middle"
            )
            kind = "oc-math-display"
        else:
            style = (
                f"display:inline;width:{self.width_em:.4f}em;height:{height}em;"
                f"max-width:100%;max-height:{height}em;vertical-align:{-self.depth_em:.4f}em"
            )
            kind = "oc-math-inline"
        return (
            f'<img class="{kind}" src="{src_attr}" alt="{alt_attr}" '
            f'width="{width_px}" height="{height_px}" style="{style}"/>'
        )


def formula_id(tex: str, display: bool) -> str:
    raw = f"{CACHE_TAG}|{BORDER_PT}|{DPI}|{int(display)}|{tex}".encode()
    return hashlib.sha256(raw).hexdigest()[:20]


# Pandoc writes \R^\N as \mathbb{R}^\mathbb{N}. unicode-math then applies the
# superscript to \mathbb and the {N} falls off. Brace the atom.
_SCRIPT_ATOM = re.compile(
    r"([_^])\s*(\\(?:mathbb|mathbf|mathrm|mathcal|mathfrak|mathsf|mathit|symbf)"
    r"(?:\s*\{[^{}]*\}|\s+[A-Za-z0-9]))"
)


def brace_scripts(tex: str) -> str:
    return _SCRIPT_ATOM.sub(r"\1{\2}", tex)


def clean_tex(tex: str) -> str:
    tex = html.unescape(tex)
    tex = re.sub(r"\\label\{[^{}]*\}", "", tex)
    tex = re.sub(r"\\tag\*?\{[^{}]*\}", "", tex)
    tex = re.sub(r"\\(?:notag|nonumber)\b", "", tex)
    return brace_scripts(tex.strip())


def math_key(attrs: str, inner: str) -> tuple[str, bool] | None:
    found = ANNOTATION_RE.search(inner)
    if not found:
        return None
    display = re.search(r"\bdisplay\s*=\s*[\"']block[\"']", attrs) is not None
    return clean_tex(found.group(1)), display


def raw_key(kind: str, body: str) -> tuple[str, bool]:
    tex = html.unescape(body).strip()
    display = kind == "display"
    if tex.startswith("$$") and tex.endswith("$$"):
        tex = tex[2:-2]
        display = True
    elif tex.startswith("$") and tex.endswith("$"):
        tex = tex[1:-1]
    elif tex.startswith(r"\[") and tex.endswith(r"\]"):
        tex = tex[2:-2]
        display = True
    return clean_tex(tex), display


def collect_keys(text: str) -> list[tuple[str, bool]]:
    keys = []
    for match in MATH_RE.finditer(text):
        key = math_key(match.group(1), match.group(2))
        if key is None:
            snippet = re.sub(r"\s+", " ", match.group(0))[:160]
            raise MathRenderError(f"MathML has no TeX annotation: {snippet}")
        if key[0]:
            keys.append(key)
    for match in RAW_RE.finditer(text):
        key = raw_key(match.group(1), match.group(2))
        if key[0]:
            keys.append(key)
    return keys


def _dim(token: str) -> float:
    return float(token.strip().removesuffix("pt"))


def _formula_source(tex: str, display: bool) -> str:
    """Turn a pandoc annotation into a box TeX can measure.

    ``split`` is legal only inside an outer display, so it becomes ``aligned``,
    which has the same meaning and works in an ``\\hbox``. ``\\qedhere`` is a
    proof-layout command and is not part of the formula.
    """
    tex = brace_scripts(tex)
    tex = re.sub(r"\\qedhere\b", "", tex)
    tex = re.sub(r"\\begin\{split\}", r"\\begin{aligned}", tex)
    tex = re.sub(r"\\end\{split\}", r"\\end{aligned}", tex)
    tex = re.sub(r"\\begin\{align\*?\}", r"\\begin{aligned}", tex)
    tex = re.sub(r"\\end\{align\*?\}", r"\\end{aligned}", tex)
    if display:
        return "$\\displaystyle\n" + tex + "\n$\n"
    return "$\n" + tex + "\n$\n"


def _job_root(parent: Path) -> Path:
    root = parent / "root"
    job = root / "job"
    job.mkdir(parents=True)
    link = root / "common"
    if not link.exists():
        link.symlink_to(REPO / "common")
    return job


def _compile_batch(formulas: list[tuple[str, bool]]) -> dict[tuple[str, bool], Glyph]:
    if not shutil.which("xelatex") or not shutil.which("pdftocairo"):
        raise MathRenderError("xelatex and pdftocairo are required to render EPUB mathematics")
    with tempfile.TemporaryDirectory(prefix="oc-math-") as tmp:
        job = _job_root(Path(tmp))
        lines = [HEADER]
        for index, (tex, display) in enumerate(formulas):
            (job / f"f{index}.tex").write_text(_formula_source(tex, display), encoding="utf-8")
            lines.append(f"\\ocship{{{index}}}{{f{index}.tex}}")
        lines.append(FOOTER)
        (job / "math.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
        env = os.environ.copy()
        env["LC_ALL"] = "C.UTF-8"
        log_path = job / "xelatex.log"
        with log_path.open("w", encoding="utf-8", errors="replace") as log:
            proc = subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "math.tex"],
                cwd=job, env=env, stdout=log, stderr=subprocess.STDOUT,
            )
        if proc.returncode != 0:
            tail = log_path.read_text(encoding="utf-8", errors="replace").splitlines()[-40:]
            shown = formulas[0][0][:240] if len(formulas) == 1 else f"{len(formulas)} formulas"
            raise MathRenderError(f"XeLaTeX failed on {shown}\n" + "\n".join(tail))
        metrics = (job / "metrics.txt").read_text(encoding="utf-8").splitlines()
        if len(metrics) != len(formulas):
            raise MathRenderError(
                f"measured {len(metrics)} formulas, expected {len(formulas)}")
        subprocess.run(
            ["pdftocairo", "-png", "-transp", "-r", str(DPI), str(job / "math.pdf"), str(job / "g")],
            check=True, capture_output=True,
        )
        # pdftocairo zero-pads once a document has 10 or more pages (g-01.png),
        # and leaves the number unpadded below that (g-1.png).
        pngs = sorted(job.glob("g-*.png"), key=lambda path: int(path.stem.rsplit("-", 1)[-1]))
        if len(pngs) != len(formulas):
            names = ", ".join(path.name for path in pngs[:12])
            raise MathRenderError(f"got {len(pngs)} PNGs for {len(formulas)} formulas ({names})")
        raw = [path.read_bytes() for path in pngs]
        if any(not blob.startswith(b"\x89PNG") for blob in raw):
            raise MathRenderError("pdftocairo did not write a PNG for every formula")
        packed = epub_png.compress_math_many(raw)
        rendered = {}
        for line, png in zip(metrics, packed):
            index_s, ht, dp, wd, em = line.split(",")
            index = int(index_s)
            tex, display = formulas[index]
            em_pt = _dim(em)
            width_em = max((_dim(wd) + 2 * BORDER_PT) / em_pt, 0.05)
            depth_em = (_dim(dp) + BORDER_PT) / em_pt
            height_em = (_dim(ht) + _dim(dp) + 2 * BORDER_PT) / em_pt
            rendered[(tex, display)] = Glyph(png, width_em, depth_em, height_em, display)
        return rendered


def _compile_or_split(formulas: list[tuple[str, bool]]) -> dict[tuple[str, bool], Glyph]:
    try:
        return _compile_batch(formulas)
    except MathRenderError:
        if len(formulas) <= 1:
            raise
        mid = len(formulas) // 2
        left = _compile_or_split(formulas[:mid])
        right = _compile_or_split(formulas[mid:])
        return {**left, **right}


def _cache_get(cache: Path, tex: str, display: bool) -> Glyph | None:
    ident = formula_id(tex, display)
    png_path = cache / f"{ident}.png"
    meta_path = cache / f"{ident}.txt"
    if not png_path.is_file() or not meta_path.is_file():
        return None
    png = png_path.read_bytes()
    if not png.startswith(b"\x89PNG"):
        return None
    width_s, depth_s, height_s, flag = meta_path.read_text(encoding="utf-8").split()
    return Glyph(png, float(width_s), float(depth_s), float(height_s), flag == "1")


def _cache_put(cache: Path, tex: str, display: bool, glyph: Glyph) -> None:
    cache.mkdir(parents=True, exist_ok=True)
    ident = formula_id(tex, display)
    (cache / f"{ident}.png").write_bytes(glyph.png)
    (cache / f"{ident}.txt").write_text(
        f"{glyph.width_em:.6f} {glyph.depth_em:.6f} {glyph.height_em:.6f} {int(display)}\n",
        encoding="utf-8",
    )


def render_formulas(formulas: list[tuple[str, bool]], cache: Path | None = None) -> dict[tuple[str, bool], Glyph]:
    """Render each unique ``(tex, display)`` pair once."""
    unique = list(dict.fromkeys(formulas))
    rendered: dict[tuple[str, bool], Glyph] = {}
    pending = []
    for item in unique:
        if cache is not None:
            hit = _cache_get(cache, *item)
            if hit is not None:
                rendered[item] = hit
                continue
        pending.append(item)
    chunk = 400
    for start in range(0, len(pending), chunk):
        batch = pending[start:start + chunk]
        print(
            f"EPUB math: rendering formulas {start + 1}–{start + len(batch)} of {len(pending)}",
            flush=True,
        )
        fresh = _compile_or_split(batch)
        for item, glyph in fresh.items():
            rendered[item] = glyph
            if cache is not None:
                _cache_put(cache, *item, glyph)
    return rendered


_FORMULA_IMG = re.compile(
    r'(<img\b[^>]*\bclass="oc-math-(inline|display)"[^>]*/>)(\s*)([.,;:!?]+(?:[\'"”’)\]])?)?'
)


def attach_punctuation(text: str) -> str:
    """Keep a following period or comma with its formula.

    A display image used to be ``display:block``, so Moon+ and other readers
    closed the paragraph and the next ``. Now`` or ``, and`` started at the
    left margin. Inline images stay inline inside a nowrap span. Display
    images sit in a centred block with that punctuation inside the block.
    """
    def repl(match: re.Match) -> str:
        img, kind, spaces, punct = match.group(1), match.group(2), match.group(3) or "", match.group(4) or ""
        if kind == "display":
            return (
                '<div class="oc-math-block" style="display:block;text-align:center;margin:0.6em 0">'
                + img + punct + "</div>" + ("" if punct else spaces)
            )
        if punct:
            # No text node, newline or space between the image and its period.
            return f'<span class="oc-math-keep" style="white-space:nowrap">{img}{punct}</span>'
        return img + spaces
    return _FORMULA_IMG.sub(repl, text)


def replace_math(text: str, glyphs: dict[tuple[str, bool], Glyph], page: str, package_root: str) -> tuple[str, dict[str, bytes]]:
    """Swap MathML and raw TeX spans for measured images. Returns new media files."""
    media: dict[str, bytes] = {}
    # Different TeX can paint the same pixels. One file, two vertical-aligns.
    shared: dict[bytes, str] = {}

    def src_for(tex: str, display: bool) -> tuple[str, Glyph]:
        glyph = glyphs[(tex, display)]
        png, ratio = epub_png.fit_formula_png(glyph.png, glyph.height_em)
        if ratio != 1.0:
            glyph = replace(glyph, width_em=glyph.width_em * ratio)
        digest = hashlib.sha256(png).digest()
        zip_name = shared.get(digest)
        if zip_name is None:
            ident = digest.hex()[:20]
            zip_name = posixpath.join(package_root, "media", f"oc-math-{ident}.png")
            shared[digest] = zip_name
            media[zip_name] = png
        return posix_rel(page, zip_name), glyph

    def math_sub(match: re.Match) -> str:
        key = math_key(match.group(1), match.group(2))
        if key is None or not key[0]:
            return ""
        src, glyph = src_for(*key)
        return glyph.html(src, key[0])

    def raw_sub(match: re.Match) -> str:
        key = raw_key(match.group(1), match.group(2))
        if not key[0]:
            return ""
        src, glyph = src_for(*key)
        return glyph.html(src, key[0])

    text = MATH_RE.sub(math_sub, text)
    text = RAW_RE.sub(raw_sub, text)
    return attach_punctuation(text), media


def posix_rel(page: str, target: str) -> str:
    return posixpath.relpath(target, posixpath.dirname(page))
