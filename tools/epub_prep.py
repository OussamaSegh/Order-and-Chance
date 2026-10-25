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
        return inline(target)

    return re.sub(r"\\input\{([^}]*)\}", repl, text)


def main(src: str, dst: str) -> None:
    text = inline(Path(src))
    text = re.sub(r"\\begin\{(exercise|reminder)\}\[([^\]]*)\]",
                  r"\\begin{\1}\\textbf{OPTARG:\2}", text)
    # texmath (pandoc's math converter) does not know \bigl/\Bigl sizes.
    text = re.sub(r"\\[Bb]ig(g?)l(?![a-z])", r"\\left", text)
    text = re.sub(r"\\[Bb]ig(g?)r(?![a-z])", r"\\right", text)
    text = re.sub(r"\\[dt]binom(?![a-z])", r"\\binom", text)
    # enumitem labels -> enumerate-package style, which pandoc understands
    text = text.replace(r"[label=(\alph*)]", "[(a)]").replace(r"[label=(\roman*)]", "[(i)]")
    Path(dst).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
