"""Write a tome's Amazon KDP listing: the text to paste into KDP's book details page.

Usage: python3 tools/listing.py <tome dir> <output .md>

The description and keywords come from <tome>/kdp.md, written by hand:

    # Description
    One or more paragraphs (plain text; KDP allows at most 4000 characters).

    # Keywords
    seven lines, one keyword phrase each (at most 50 characters each),
    avoiding words already in the title and series name, which KDP indexes anyway

Without kdp.md, the description falls back to the back-cover text (<tome>/blurb.tex) and the
keywords are left to be written. The title, series and author fields come from main.tex.
Exits with an error if kdp.md breaks KDP's limits.
"""
import re
import sys
from pathlib import Path


def latex_to_text(tex: str) -> str:
    """Plain text from the simple LaTeX of a blurb (emphasis, inline maths, dashes, quotes)."""
    tex = re.sub(r"(?m)%.*$", "", tex)
    tex = re.sub(r"\\(par|medskip|bigskip|smallskip)\b", "\n\n", tex)
    tex = re.sub(r"\\(emph|textit|textbf|textsc|mathrm|text)\{([^{}]*)\}", r"\2", tex)
    tex = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", tex)
    tex = tex.replace("---", "\u2014").replace("--", "\u2013").replace("``", "\u201c").replace("''", "\u201d")
    tex = tex.replace("~", " ").replace("\\,", " ").replace("\\&", "&").replace("\\ ", " ")
    symbols = {r"\log": "log", r"\pi": "\u03c0", r"\infty": "\u221e", r"\sim": "~", r"\le": "\u2264",
               r"\ge": "\u2265", r"\cdot": "\u00b7", r"\times": "\u00d7", r"\zeta": "\u03b6", r"\sqrt": "\u221a"}
    for k, v in symbols.items():
        tex = re.sub(re.escape(k) + r"(?![a-zA-Z])", v, tex)
    accents = {"H": {"o": "\u0151", "u": "\u0171"}, "'": {"e": "\u00e9", "a": "\u00e1", "o": "\u00f3", "i": "\u00ed"},
               "`": {"e": "\u00e8", "a": "\u00e0"}, '"': {"o": "\u00f6", "u": "\u00fc", "a": "\u00e4"},
               "^": {"e": "\u00ea", "o": "\u00f4"}, "c": {"c": "\u00e7"}}
    tex = re.sub(r"\\([H'`\"^c])\{?\\?([a-zA-Z])\}?",
                 lambda m: accents.get(m.group(1), {}).get(m.group(2), m.group(2)), tex)
    sup = str.maketrans("0123456789n+-", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207f\u207a\u207b")
    tex = re.sub(r"\^\{([0-9n+-]+)\}|\^([0-9n])", lambda m: (m.group(1) or m.group(2)).translate(sup), tex)
    tex = re.sub(r"\\[a-zA-Z]+\*?", "", tex)
    tex = tex.replace("$", "").replace("{", "").replace("}", "").replace("^", "")
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", tex)]
    return "\n\n".join(p for p in paragraphs if p)


def sections(md: str) -> dict:
    parts = re.split(r"(?m)^#\s+(.+?)\s*$", md)
    return {parts[i].strip().lower(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def main(tome_dir: str, out: str) -> None:
    tome = Path(tome_dir)
    title_line = re.search(r"^% epub-title: (.*)$", (tome / "main.tex").read_text(encoding="utf-8"), re.M).group(1)
    series, _, book = title_line.partition(". ")
    number, _, title = book.partition(": ")
    number = number.replace("Tome ", "")
    kdp = tome / "kdp.md"
    problems = []
    if kdp.exists():
        s = sections(kdp.read_text(encoding="utf-8"))
        description = s.get("description", "")
        keywords = [k.strip(" -*\t") for k in s.get("keywords", "").splitlines() if k.strip(" -*\t")]
        keywords = [re.sub(r"^\d+[.)]\s*", "", k) for k in keywords]
        if len(description) > 4000:
            problems.append(f"description has {len(description)} characters (KDP allows 4000)")
        if len(keywords) > 7:
            problems.append(f"{len(keywords)} keywords (KDP allows 7)")
        problems += [f"keyword over 50 characters: {k!r}" for k in keywords if len(k) > 50]
        if problems:
            sys.exit(f"{kdp}: " + "; ".join(problems))
        source = "kdp.md"
    else:
        blurb = tome / "blurb.tex"
        description = latex_to_text(blurb.read_text(encoding="utf-8")) if blurb.exists() else ""
        keywords = []
        source = "blurb.tex (no kdp.md yet)"
    lines = [f"# KDP listing: {series}, Tome {number}: {title}", "",
             "Paste these fields into KDP (Kindle eBook and Paperback details). "
             f"Description and keywords from {source}.", "",
             "| Field | Value |", "|---|---|",
             f"| Language | English |",
             f"| Book title | Tome {number}: {title} |",
             f"| Subtitle | {series}: number theory, algebra and probability, all proved |",
             f"| Series | {series} (volume: {number}) |",
             "| Edition number | 1 |",
             "| Author | SEGHAIER Oussama |",
             "| Publishing rights | I own the copyright and I hold the necessary publishing rights |",
             "| Primary audience | Adults; no sexually explicit content |",
             "| AI-generated content | Yes: text and images (covers), AI-generated, then reviewed |",
             "",
             f"## Description ({len(description)} of 4000 characters)", "", description or "(to be written)", "",
             "## Keywords (one per KDP box, at most 50 characters each)", ""]
    lines += [f"{i}. {k}" for i, k in enumerate(keywords, 1)] or ["(to be written in <tome>/kdp.md)"]
    Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
