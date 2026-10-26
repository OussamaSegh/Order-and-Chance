"""Flatten a tome's LaTeX for pandoc's EPUB conversion.

Inlines \\input files (swapping the PDF preamble for common/epub-preamble.tex)
and turns the optional arguments of the exercise and
reminder boxes (which pandoc drops) into markers that tools/epub.lua reads.
"""
import re
import sys
from pathlib import Path


def inline(path: Path) -> str:
    text = path.read_text(encoding="utf-8")

    def repl(m):
        target = path.parent / m.group(1)
        if target.suffix != ".tex":
            target = target.with_suffix(".tex")
        if target.name == "preamble.tex":
            target = target.with_name("epub-preamble.tex")
        if target.name == "figure-packages.tex":
            return ""
        # A file whose first line is "% pdf-only" (PDF layout tweaks) is left out of the EPUB.
        if target.read_text(encoding="utf-8").startswith("% pdf-only"):
            return ""
        return inline(target)

    return re.sub(r"\\input\{([^}]*)\}", repl, text)


COMMON = Path(__file__).resolve().parent.parent / "common"


def book_settings(main_tex: Path) -> dict:
    """The \\book... settings of common/frontmatter.tex, with a tome's \\renewcommand overrides."""
    pattern = r"\\(?:re)?newcommand\{\\(book\w+|seriesname)\}\{((?:[^{}]|\{[^{}]*\})*)\}"
    settings = dict(re.findall(pattern, (COMMON / "frontmatter.tex").read_text(encoding="utf-8")))
    settings.update(re.findall(pattern, main_tex.read_text(encoding="utf-8")))
    return {k: " ".join(v.replace("\\textcopyright\\ ", "\u00a9 ").replace("\\&", "&").split())
            for k, v in settings.items()}


def copyright_section(main_tex: Path) -> str:
    b = book_settings(main_tex)
    title = re.search(r"^% epub-title: (.*)$", main_tex.read_text(encoding="utf-8"), re.M)
    isbn = "ISBN (eBook): " + b["bookisbnebook"] + "\n\n" if b.get("bookisbnebook") else ""
    return ("\\chapter*{Copyright}\n" + (r"\emph{" + title.group(1) + "}\n\n" if title else "")
            + b["bookcopyright"] + "\n\n" + b["booklicence"] + "\n\n"
            + b["bookedition"] + ". " + b["bookpublisher"] + ".\n\n" + isbn)


def main(src: str, dst: str, figdir: str) -> None:
    text = inline(Path(src))
    text = text.replace("\\maketitle\n", copyright_section(Path(src)), 1)
    # A book may rename its exercises ("% exercise-name: Problem" in main.tex); tools/epub.lua reads the marker.
    name = re.search(r"^% exercise-name: (\w+)", text, re.M)
    if name:
        text = text.replace("\\begin{document}", "\\begin{document}\n\\begin{exname}" + name.group(1) + "\\end{exname}", 1)
    # Figures: the EPUB shows the SVG made by build.sh instead of the TikZ code.
    text = re.sub(r"\\fig\{([^}]*)\}",
                  lambda m: r"\includegraphics{" + str(Path(figdir).resolve() / (m.group(1) + ".svg")) + "}", text)
    # Small-screen line breaks of the PDF (common/preamble.tex) mean nothing in an EPUB.
    text = re.sub(r"\\qq(?![a-z])", r"\\qquad ", text)
    text = re.sub(r"\\eqbr(?![a-z])", "", text)
    # The EPUB cover is set by pandoc's --epub-cover-image instead.
    text = text.replace("\\makecover\n", "")
    text = re.sub(r"\\begin\{(exercise|reminder)\}\[([^\]]*)\]",
                  r"\\begin{\1}\\textbf{OPTARG:\2}", text)
    # texmath (pandoc's math converter) does not know \bigl/\Bigl sizes.
    text = re.sub(r"\\[Bb]ig(g?)l(?![a-z])", r"\\left", text)
    text = re.sub(r"\\[Bb]ig(g?)r(?![a-z])", r"\\right", text)
    text = re.sub(r"\\[dt]binom(?![a-z])", r"\\binom", text)
    text = re.sub(r"\\cfrac(?![a-z])", r"\\dfrac", text)
    text = re.sub(r"\\(begin|end)\{psmallmatrix\}", r"\\\1{pmatrix}", text)
    # enumitem labels -> enumerate-package style, which pandoc understands
    text = text.replace(r"[label=(\alph*)]", "[(a)]").replace(r"[label=(\roman*)]", "[(i)]")
    Path(dst).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1] == "--rights":
        b = book_settings(Path(sys.argv[2]))
        print(b["bookcopyright"] + ". " + b["booklicence"])
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
