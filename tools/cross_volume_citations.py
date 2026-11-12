"""Resolve Volume N citations against the numbering a build assigns.

The checker walks each volume's ``main.tex`` in input order and reproduces
the counters LaTeX assigns: ``\\chapter`` (only in ``\\mainmatter``), the
shared theorem counter, and the exercise counter. Appendix letters follow
``\\Alph``. It then reads every ``Volume N, Theorem/Proposition/Exercise/
Chapter X`` citation, including the ``X of Volume N`` order, and fails when
the number is missing or belongs to a different kind.

Lemma and Corollary use the same counter, so they are checked too.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VOLUMES = {
    1: "volume1-first-principles",
    2: "volume2-integers",
    3: "volume3-symmetry",
    4: "volume4-chance",
    5: "volume5-calculation",
    6: "volume6-crossroads",
    7: "volume7-spaces",
    8: "volume8-analysis",
    9: "volume9-shapes",
    10: "volume10-abstraction",
    11: "volume11-randomness",
    12: "volume12-random-motion",
    13: "volume13-arithmetic",
    14: "volume14-primes",
    15: "volume15-order-and-chance",
}

# Kinds that share the theorem counter. The citation words map onto these.
THEOREM_KINDS = {
    "theorem": "theorem",
    "theorems": "theorem",
    "proposition": "proposition",
    "propositions": "proposition",
    "lemma": "lemma",
    "lemmas": "lemma",
    "corollary": "corollary",
    "corollaries": "corollary",
}
COUNTED = ("theorem", "proposition", "lemma", "corollary", "definition", "example")
NUMBERED_ENVS = COUNTED + ("exercise",)

COMMENT = re.compile(r"(?<!\\)%.*")
INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")
SETTER = re.compile(r"\\setcounter\{chapter\}\{(-?\d+)\}")
ENV = re.compile(
    r"\\begin\{(" + "|".join(NUMBERED_ENVS) + r")\}(\[[^\]]*\])?")
KIND_WORD = (
    r"Theorems?|Propositions?|Exercises?|Chapters?|"
    r"Lemmas?|Corollar(?:y|ies)"
)
NUMBER = r"[0-9]+(?:\.[0-9]+)?|[A-Z](?:\.[0-9]+)?"
AFTER_VOLUME = re.compile(
    rf"({KIND_WORD})((?:\s*~?{NUMBER}(?:\s*(?:,|and|or|to|--+|–)\s*~?{NUMBER})?)*)",
    re.IGNORECASE,
)
BEFORE_VOLUME = re.compile(
    rf"({KIND_WORD})\s*((?:~?{NUMBER}(?:\s*(?:,|and|or|to|--+|–)\s*~?{NUMBER})*))"
    rf"\s+of\s+Volume~?(\d+)",
    re.IGNORECASE,
)
VOLUME_AT = re.compile(r"Volume~?(\d+)")
NUM_TOKEN = re.compile(rf"~?({NUMBER})")


@dataclass
class Statement:
    volume: int
    kind: str
    number: str
    label: str
    name: str
    source: str


@dataclass
class BookNumbers:
    statements: list[Statement] = field(default_factory=list)
    by_key: dict[tuple[str, str], Statement] = field(default_factory=dict)
    chapters: set[str] = field(default_factory=set)

    def add(self, statement: Statement) -> None:
        self.statements.append(statement)
        self.by_key.setdefault((statement.kind, statement.number), statement)


@dataclass
class Citation:
    volume: int
    kind: str  # theorem / proposition / lemma / corollary / exercise / chapter
    number: str
    source: str
    text: str


def strip_comments(text: str) -> str:
    return COMMENT.sub("", text)


def alph(n: int) -> str:
    if n < 1:
        return f"?{n}"
    letters = ""
    while n:
        n, rem = divmod(n - 1, 26)
        letters = chr(ord("A") + rem) + letters
    return letters


def resolve_input(volume_root: Path, name: str) -> Path | None:
    """TeX resolves ``\\input`` from the volume directory, where ``main.tex`` is compiled."""
    raw = Path(name)
    if raw.suffix != ".tex":
        raw = raw.with_suffix(".tex")
    candidate = (volume_root / raw).resolve()
    try:
        candidate.relative_to(volume_root.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def _optional_name(argument: str | None) -> str:
    if not argument:
        return ""
    return argument[1:-1].strip()


def _next_label(text: str, start: int) -> str:
    window = text[start:start + 400]
    # Stop at the next counted environment so a label is not borrowed.
    stop = re.search(r"\\begin\{", window)
    if stop:
        window = window[:stop.start()]
    found = re.search(r"\\label\{([^}]+)\}", window)
    return found.group(1) if found else ""


def number_volume(volume: int) -> BookNumbers:
    """Return the numbers ``xelatex`` would assign in this volume."""
    directory = ROOT / VOLUMES[volume]
    book = BookNumbers()
    volume_root = directory.resolve()
    state = {
        "active": False,
        "mainmatter": False,
        "appendix": False,
        "chapter": 0,
        "theorem": 0,
        "exercise": 0,
        "chapter_label": "",
    }

    def chapter_label() -> str:
        if state["appendix"]:
            return alph(state["chapter"])
        return str(state["chapter"])

    def walk(path: Path, seen: set[Path]) -> None:
        path = path.resolve()
        if path in seen or not path.is_file():
            return
        seen.add(path)
        text = strip_comments(path.read_text(encoding="utf-8"))
        cursor = 0
        tokens = []
        for match in re.finditer(
            r"\\begin\{document\}|\\end\{document\}|\\frontmatter|\\mainmatter|"
            r"\\backmatter|\\appendix|\\setcounter\{chapter\}\{-?\d+\}|"
            r"\\chapter(?![A-Za-z])\*?|\\begin\{(?:" + "|".join(NUMBERED_ENVS) + r")\}(?:\[[^\]]*\])?|"
            r"\\(?:input|include)\{[^}]+\}",
            text,
        ):
            tokens.append(match)
        for match in tokens:
            token = match.group(0)
            if token == r"\begin{document}":
                state["active"] = True
                continue
            if token == r"\end{document}":
                state["active"] = False
                continue
            if not state["active"]:
                if token.startswith(r"\input") or token.startswith(r"\include"):
                    name = INPUT.search(token).group(1)
                    child = resolve_input(volume_root, name)
                    if child:
                        walk(child, seen)
                continue
            if token == r"\frontmatter":
                state["mainmatter"] = False
            elif token == r"\mainmatter":
                state["mainmatter"] = True
            elif token == r"\backmatter":
                state["mainmatter"] = False
            elif token == r"\appendix":
                state["appendix"] = True
                state["chapter"] = 0
            elif token.startswith(r"\setcounter"):
                state["chapter"] = int(SETTER.search(token).group(1))
            elif token.startswith(r"\chapter"):
                if token.startswith(r"\chapter*"):
                    continue
                if state["mainmatter"]:
                    state["chapter"] += 1
                    state["theorem"] = 0
                    state["exercise"] = 0
                    state["chapter_label"] = chapter_label()
                    book.chapters.add(state["chapter_label"])
            elif token.startswith(r"\begin"):
                env = ENV.search(token)
                kind = env.group(1)
                if kind == "exercise":
                    state["exercise"] += 1
                    number = f"{state['chapter_label']}.{state['exercise']}"
                else:
                    state["theorem"] += 1
                    number = f"{state['chapter_label']}.{state['theorem']}"
                book.add(Statement(
                    volume, kind, number,
                    _next_label(text, match.end()),
                    _optional_name(env.group(2)),
                    str(path.relative_to(ROOT)),
                ))
            elif token.startswith(r"\input") or token.startswith(r"\include"):
                name = INPUT.search(token).group(1)
                child = resolve_input(volume_root, name)
                if child:
                    walk(child, seen)
            cursor = match.end()
        del cursor

    walk(directory / "main.tex", set())
    return book


def _numbers_from(blob: str) -> list[str]:
    return [item.group(1) for item in NUM_TOKEN.finditer(blob or "")]


def _canonical_kind(word: str) -> str:
    key = word.lower()
    if key in ("exercise", "exercises"):
        return "exercise"
    if key in ("chapter", "chapters"):
        return "chapter"
    return THEOREM_KINDS[key]


def _citation_window(text: str, start: int) -> str:
    """The citation stays in one sentence and does not cross a semicolon.

    A gloss such as ``Volume~1, Chapter~8 (Taylor); Proposition~13.12`` names
    a local proposition after the semicolon. A decimal point inside ``3.17``
    is not a sentence end.
    """
    window = text[start:start + 700]
    later = VOLUME_AT.search(window)
    if later:
        window = window[:later.start()]
    of_volume = re.search(r"\sof\s+Volume~?\d+", window)
    if of_volume:
        window = window[:of_volume.start()]
    cut = len(window)
    paragraph = window.find("\n\n")
    if paragraph != -1:
        cut = paragraph
    for index, char in enumerate(window[:cut]):
        if char == ";":
            return window[:index]
        if char != ".":
            continue
        previous = window[index - 1] if index else ""
        nxt = window[index + 1] if index + 1 < len(window) else ""
        if previous.isdigit() and nxt.isdigit():
            continue
        return window[:index]
    return window[:cut]


def citations_in_text(text: str, source: str) -> list[Citation]:
    text = strip_comments(text)
    found: list[Citation] = []
    for match in BEFORE_VOLUME.finditer(text):
        kind = _canonical_kind(match.group(1))
        volume = int(match.group(3))
        for number in _numbers_from(match.group(2)):
            found.append(Citation(volume, kind, number, source, match.group(0)))
    for match in VOLUME_AT.finditer(text):
        volume = int(match.group(1))
        window = _citation_window(text, match.end())
        for item in AFTER_VOLUME.finditer(window):
            kind = _canonical_kind(item.group(1))
            numbers = _numbers_from(item.group(2))
            if not numbers:
                continue
            for number in numbers:
                found.append(Citation(
                    volume, kind, number, source,
                    f"Volume {volume}, {item.group(0)}",
                ))
    return found


def collect_citations() -> list[Citation]:
    found: list[Citation] = []
    for directory in VOLUMES.values():
        root = ROOT / directory
        for path in sorted(root.rglob("*.tex")):
            if "build" in path.parts:
                continue
            found.extend(citations_in_text(
                path.read_text(encoding="utf-8"),
                str(path.relative_to(ROOT)),
            ))
    return found


def mismatches(books: dict[int, BookNumbers] | None = None,
               cites: list[Citation] | None = None) -> list[str]:
    books = books if books is not None else {n: number_volume(n) for n in VOLUMES}
    cites = cites if cites is not None else collect_citations()
    problems = []
    for cite in cites:
        book = books.get(cite.volume)
        if book is None:
            problems.append(
                f"{cite.source}: Volume {cite.volume} is not a book ({cite.text})")
            continue
        if cite.kind == "chapter":
            if cite.number not in book.chapters:
                problems.append(
                    f"{cite.source}: Volume {cite.volume} has no Chapter {cite.number}"
                    f" ({cite.text})")
            continue
        statement = book.by_key.get((cite.kind, cite.number))
        if statement is None:
            owner = next(
                (item for item in book.statements if item.number == cite.number),
                None,
            )
            if owner is None:
                problems.append(
                    f"{cite.source}: Volume {cite.volume} has no {cite.kind} {cite.number}"
                    f" ({cite.text})")
            else:
                problems.append(
                    f"{cite.source}: Volume {cite.volume} {cite.number} is a"
                    f" {owner.kind}, not a {cite.kind} ({cite.text})")
    return problems


# Volume 1 prints its language chapter as Chapter 0 (``\setcounter{chapter}{-1}``).
# A count that calls that chapter 1 cites every later chapter one too high.
# Chapters 1 through 10 still exist, so an existence check accepts the shift.
# A gloss sitting next to the citation is checked against the printed home.
VOLUME1_GLOSS = (
    ("polynomials that agree", "6"),
    ("inclusion--exclusion", "2"),
    ("inclusion-exclusion", "2"),
    ("stars-and-bars", "2"),
    ("stars and bars", "2"),
    ("Cauchy product", "3"),
    ("multiplicity of roots", "6"),
    ("derivative of an inverse", "8"),
    ("alternating harmonic", "3"),
    ("Bolzano--Weierstrass", "3"),
    ("Bolzano-Weierstrass", "3"),
    ("Wallis integral", "8"),
    ("geometric sums of roots of unity", "5"),
    ("roots-of-unity filter", "5"),
    ("roots of unity filter", "5"),
    ("intermediate value", "3"),
    ("product of sines", "5"),
    ("binomial coefficient", "1"),
    ("Cauchy--Schwarz", "9"),
    ("Cauchy-Schwarz", "9"),
    ("Riemann--Lebesgue", "8"),
    ("quadratic Gauss sum", "5"),
    ("Vandermonde", "7"),
    ("d'Alembert", "6"),
    ("Lagrange interpolation", "6"),
    ("multiple-angle", "5"),
    ("division of polynomials", "6"),
    ("block matrices", "7"),
    ("Gram--Schmidt", "7"),
    ("Gram-Schmidt", "7"),
    ("diagonalisation", "7"),
    ("roots of polynomials", "6"),
    ("symmetric matrices", "7"),
    ("Chebyshev polynomial", "6"),
    ("absolute convergence", "3"),
    ("inverse functions", "8"),
    ("comparison with integrals", "3"),
    ("Euler's constant", "3"),
    ("weighted AM--GM", "9"),
    ("concavity of $\\ln$", "9"),
)
# These words must not be offered as what Volume 1 taught.
VOLUME1_GLOSS_FORBIDDEN = ("arcsin", "trigonometric polynomial")
_VOLUME1_CHAPTER = re.compile(
    r"Volume~?1,\s+Chapter~?(\d+)(\s*\([^)]*\))?"
    r"(?:\s+and\s+Chapter~?(\d+)(\s*\([^)]*\))?)?"
)
_VOLUME1_CHAPTERS = re.compile(
    r"Volume~?1,\s+Chapters~?(\d+)\s+and~?(\d+)(\s*\([^)]*\))?"
)


def _gloss_hits(scope: str) -> set[str]:
    return {chapter for phrase, chapter in VOLUME1_GLOSS if phrase in scope}


def _gloss_neighbourhood(text: str, start: int, end: int) -> str:
    """The words that name the subject, not the previous citation in the sentence."""
    before = text[max(0, start - 160):start]
    previous = before.rfind("Volume~")
    if previous != -1:
        before = before[previous + len("Volume~"):]
    # ``(subject, Volume 1, Chapter N)`` keeps the subject and drops the paren.
    stripped = before.rstrip()
    if stripped.endswith("("):
        clause = stripped[:-1]
        cut = max(clause.rfind(";"), clause.rfind("."), clause.rfind(")"))
        before = clause[cut + 1:]
    after = text[end:end + 90]
    return before + " " + after


def volume1_chapter_gloss_mismatches(text: str, source: str = "") -> list[str]:
    """Flag a Volume 1 chapter citation whose nearby gloss names another chapter.

    The shift that counts the language chapter as Chapter 1 is the case this
    catches: the cited number exists, and the subject is the previous chapter.
    """
    text = strip_comments(text)
    problems = []
    where = f"{source}: " if source else ""

    def complain(cited: str, scope: str, detail: str) -> None:
        problems.append(
            f"{where}Volume 1 chapter gloss: cited {cited}, {detail} ({scope[:80]})"
        )

    for match in _VOLUME1_CHAPTER.finditer(text):
        numbers = [match.group(1)]
        scopes = []
        if match.group(2):
            scopes.append((match.group(1), match.group(2)))
        if match.group(3):
            numbers.append(match.group(3))
            scopes.append((match.group(3), match.group(4) or ""))
        if not match.group(2) and not match.group(3):
            scopes.append((match.group(1), _gloss_neighbourhood(text, match.start(), match.end())))
        for cited, scope in scopes:
            if any(word in scope for word in VOLUME1_GLOSS_FORBIDDEN):
                complain(cited, scope, "Volume 1 does not teach this")
                continue
            hits = _gloss_hits(scope)
            if hits and hits != {cited}:
                complain(cited, scope, f"printed chapter {sorted(hits)}")
    for match in _VOLUME1_CHAPTERS.finditer(text):
        numbers = {match.group(1), match.group(2)}
        scope = match.group(3) or _gloss_neighbourhood(text, match.start(), match.end())
        if any(word in scope for word in VOLUME1_GLOSS_FORBIDDEN):
            complain(", ".join(sorted(numbers)), scope, "Volume 1 does not teach this")
            continue
        hits = _gloss_hits(scope)
        if hits and not hits <= numbers:
            complain(", ".join(sorted(numbers)), scope, f"printed chapters {sorted(hits)}")
    return problems


# Printed Volume 2 is not the filename order. A citation whose nearby words
# name one of these subjects must use that printed chapter, even when the
# shifted number still exists.
VOLUME2_SUBJECT_CHAPTER = (
    ("primitive root", "5"),
    ("Möbius", "4"),
    ("multiplicative function", "4"),
    ("Dirichlet convolution", "4"),
    ("Legendre symbol", "6"),
    ("quadratic reciprocity", "6"),
    ("continued fraction", "9"),
    ("Pythagorean", "8"),
    ("Pell", "9"),
    ("Gauss sum", "6"),
    ("unique factorisation", "1"),
    ("unique factorization", "1"),
)
# Gaussian unique factorisation lives in Chapter 10, beside the rational one.
VOLUME2_SUBJECT_ALSO = {
    "unique factorisation": {"10"},
    "unique factorization": {"10"},
}
_VOLUME2_CITE = re.compile(
    r"Volume~?2,\s+"
    r"(Theorems?|Propositions?|Lemmas?|Corollar(?:y|ies)|Exercises?|Chapters?)~?"
    r"([0-9]+(?:\.[0-9]+)?)"
    r"((?:\s*(?:,|and|or|to|--+|–)\s*~?[0-9]+(?:\.[0-9]+)?)*)"
)


def _volume2_scope(text: str, start: int, end: int) -> str:
    before = text[max(0, start - 140):start]
    cut = max(before.rfind(";"), before.rfind("Volume~"), before.rfind("Volume "))
    if cut != -1:
        before = before[cut + 1:]
    after = text[end:end + 80]
    stop = after.find("Volume~")
    if stop != -1:
        after = after[:stop]
    return before + " " + after


def volume2_subject_mismatches(text: str, source: str = "") -> list[str]:
    """Flag a Volume 2 citation whose nearby subject lives in another chapter.

    The filename order and the printed order disagree on Chapters 4--6 and
    8--9. Those shifted numbers still exist, so an existence check accepts
    them. The subject next to the number does not.
    """
    text = strip_comments(text)
    problems = []
    where = f"{source}: " if source else ""
    for match in _VOLUME2_CITE.finditer(text):
        numbers = [match.group(2)] + _numbers_from(match.group(3) or "")
        chapters = {item.split(".", 1)[0] for item in numbers}
        scope = _volume2_scope(text, match.start(), match.end())
        for phrase, home in VOLUME2_SUBJECT_CHAPTER:
            if phrase not in scope:
                continue
            allowed = {home} | VOLUME2_SUBJECT_ALSO.get(phrase, set())
            if chapters.isdisjoint(allowed):
                problems.append(
                    f"{where}Volume 2 subject: {phrase} is Chapter {home}, "
                    f"cited {match.group(1)} {', '.join(numbers)} ({scope[:70]})"
                )
    return problems


def gloss_mismatches() -> list[str]:
    found = []
    for directory in VOLUMES.values():
        root = ROOT / directory
        for path in sorted(root.rglob("*.tex")):
            if "build" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            source = str(path.relative_to(ROOT))
            found.extend(volume1_chapter_gloss_mismatches(text, source))
            found.extend(volume2_subject_mismatches(text, source))
    return found


def main() -> int:
    books = {n: number_volume(n) for n in VOLUMES}
    problems = mismatches(books) + gloss_mismatches()
    if problems:
        print(f"{len(problems)} citation mismatches")
        for line in problems:
            print(line)
        return 1
    total = sum(len(book.statements) for book in books.values())
    print(f"Cross-volume citations match {total} numbered statements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
