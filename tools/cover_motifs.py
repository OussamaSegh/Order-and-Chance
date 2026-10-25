"""Generate the central picture of each tome's cover.

Usage: python3 tools/cover_motifs.py
Writes <tome>/cover-motif.tex, a TikZ fragment centred at the origin that fits in a
disc of radius 2.3in. tools/cover.tex draws it in the cover's accent colour.
"""
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
R = 2.3  # inches


def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i in range(n + 1) if sieve[i]]


def times_table(n=200, k=2):
    """Chords j -> k*j mod n on a circle: for k=2 their envelope is a cardioid."""
    pt = lambda j: (R * math.cos(math.pi + 2 * math.pi * j / n), R * math.sin(math.pi + 2 * math.pi * j / n))
    lines = ["% Times table: chords from j to 2j mod 200. Their envelope is a cardioid.",
             r"\draw[accent,line width=0.6pt,opacity=0.9] (0,0) circle (%.3fin);" % R]
    for j in range(1, n):
        (x1, y1), (x2, y2) = pt(j), pt(k * j % n)
        lines.append(r"\draw[accent,line width=0.25pt,opacity=0.55] (%.4fin,%.4fin)--(%.4fin,%.4fin);" % (x1, y1, x2, y2))
    return "\n".join(lines) + "\n"


def sacks_spiral(n=16000):
    """Sacks spiral: the integer m sits at polar (sqrt m, 2 pi sqrt m); only primes are drawn.
    The squares line up on the horizontal axis and primes gather on curves n^2+n+41 and friends."""
    s = R / math.sqrt(n)
    lines = [f"% Sacks spiral of the primes up to {n}."]
    for p in primes_upto(n):
        r, t = math.sqrt(p), 2 * math.pi * math.sqrt(p)
        size = 0.0045 + 0.0075 * r / math.sqrt(n)
        lines.append(r"\fill[accent] (%.4fin,%.4fin) circle (%.4fin);" % (s * r * math.cos(t), s * r * math.sin(t), size))
    return "\n".join(lines) + "\n"


MOTIFS = {
    "tome0-back-in-shape": times_table,
    "tome1-integers": sacks_spiral,
}

if __name__ == "__main__":
    for tome, make in MOTIFS.items():
        (ROOT / tome / "cover-motif.tex").write_text(make())
        print("wrote", tome + "/cover-motif.tex")
