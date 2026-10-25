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


def buckyball():
    """The truncated icosahedron: its 60 vertices are the 60 rotations in A5, and its edges
    form a Cayley graph of A5 (generators of order 2 and 5). Drawn in perspective-free
    projection, back edges fainter."""
    phi = (1 + math.sqrt(5)) / 2
    base = [(0, 1, 3 * phi), (1, 2 + phi, 2 * phi), (phi, 2, 2 * phi + 1)]
    pts = set()
    for a, b, c in base:
        for sa in (1, -1):
            for sb in (1, -1):
                for sc in (1, -1):
                    v = (sa * a, sb * b, sc * c)
                    for k in range(3):  # even permutations of three coordinates = cyclic shifts
                        pts.add(tuple(round(x, 9) for x in v[k:] + v[:k]))
    pts = sorted(pts)
    assert len(pts) == 60
    edges = [(i, j) for i in range(60) for j in range(i + 1, 60)
             if abs(math.dist(pts[i], pts[j]) - 2) < 1e-6]
    assert len(edges) == 90

    def rot(v):  # a fixed tilt so that no face is seen edge-on
        x, y, z = v
        a, b = 0.55, 0.35
        x, z = x * math.cos(a) + z * math.sin(a), -x * math.sin(a) + z * math.cos(a)
        y, z = y * math.cos(b) - z * math.sin(b), y * math.sin(b) + z * math.cos(b)
        return x, y, z
    q = [rot(v) for v in pts]
    rmax = max(math.hypot(x, y) for x, y, _ in q)
    s = R / rmax
    zmax = max(abs(z) for *_, z in q)
    lines = ["% Truncated icosahedron: a Cayley graph of A5 (60 vertices, 90 edges)."]
    for i, j in sorted(edges, key=lambda e: q[e[0]][2] + q[e[1]][2]):
        depth = (q[i][2] + q[j][2]) / (2 * zmax)  # -1 back, +1 front
        op = 0.25 + 0.65 * (depth + 1) / 2
        w = 0.3 + 0.7 * (depth + 1) / 2
        lines.append(r"\draw[accent,line width=%.2fpt,opacity=%.2f] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                     % (w, op, s * q[i][0], s * q[i][1], s * q[j][0], s * q[j][1]))
    for x, y, z in sorted(q, key=lambda v: v[2]):
        depth = z / zmax
        lines.append(r"\fill[accent,opacity=%.2f] (%.4fin,%.4fin) circle (%.4fin);"
                     % (0.3 + 0.7 * (depth + 1) / 2, s * x, s * y, 0.018 + 0.012 * (depth + 1) / 2))
    return "\n".join(lines) + "\n"


MOTIFS = {
    "tome0-back-in-shape": times_table,
    "tome1-integers": sacks_spiral,
    "tome2-structures": buckyball,
}

if __name__ == "__main__":
    for tome, make in MOTIFS.items():
        if not (ROOT / tome).is_dir():
            continue
        (ROOT / tome / "cover-motif.tex").write_text(make())
        print("wrote", tome + "/cover-motif.tex")
