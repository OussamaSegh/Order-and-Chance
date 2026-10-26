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


def galton_board(rows=12, balls=40):
    """A Galton board: balls fall through a triangle of pegs, turning left or right with
    probability 1/2, and pile up as a binomial histogram under the Gaussian curve."""
    import random
    rng = random.Random(3)
    dx, dy = 0.30, 0.17
    top = 1.95
    peg = lambda r, k: ((k - r / 2) * dx, top - r * dy)
    lines = ["% Galton board: binomial(12, 1/2) under its Gaussian limit."]
    for _ in range(balls):  # faint paths of individual balls
        k, pts = 0, [peg(0, 0)]
        for r in range(1, rows + 1):
            k += rng.random() < 0.5
            pts.append(peg(r, k))
        lines.append(r"\draw[accent,line width=0.35pt,opacity=0.22] " +
                     "--".join("(%.4fin,%.4fin)" % pt for pt in pts) + ";")
    for r in range(rows + 1):
        for k in range(r + 1):
            x, y = peg(r, k)
            lines.append(r"\fill[accent] (%.4fin,%.4fin) circle (0.022in);" % (x, y))
    base = top - rows * dy - 2.05
    height = 1.75
    pmax = math.comb(rows, rows // 2) / 2**rows
    for k in range(rows + 1):
        x = (k - rows / 2) * dx
        h = height * math.comb(rows, k) / 2**rows / pmax
        lines.append(r"\fill[accent,opacity=0.55] (%.4fin,%.4fin) rectangle (%.4fin,%.4fin);"
                     % (x - 0.42 * dx, base, x + 0.42 * dx, base + h))
    sigma = math.sqrt(rows) / 2
    curve = []
    for t in range(-130, 131):
        u = t / 130 * (rows / 2 + 1.2)
        curve.append("(%.4fin,%.4fin)" % (u * dx, base + height * math.exp(-u * u / (2 * sigma**2))))
    lines.append(r"\draw[accent,line width=1.1pt] " + "--".join(curve) + ";")
    lines.append(r"\draw[accent,line width=0.6pt] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                 % (-(rows / 2 + 1.2) * dx, base, (rows / 2 + 1.2) * dx, base))
    return "\n".join(lines) + "\n"


def fourier_square(levels=(1, 3, 9, 41)):
    """Partial sums of the Fourier series of a square wave, stacked: the jumps sharpen as terms are
    added, and the Gibbs overshoot (about 9% of the jump) never goes away."""
    lines = ["% Fourier partial sums of a square wave, with the Gibbs overshoot."]
    width, amp, gap = 3.6, 0.32, 1.02
    top = 1.55
    for i, n in enumerate(levels):
        y0 = top - i * gap
        pts = []
        for t in range(0, 721):
            x = t / 720 * 2 * 2 * math.pi
            s = 4 / math.pi * sum(math.sin((2 * k + 1) * x) / (2 * k + 1) for k in range(n))
            pts.append("(%.4fin,%.4fin)" % (-width / 2 + width * t / 720, y0 + amp * s))
        op = 0.35 + 0.65 * (i + 1) / len(levels)
        lines.append(r"\draw[accent,line width=%.2fpt,opacity=%.2f] " % (0.6 + 0.25 * i, op) + "--".join(pts) + ";")
        lines.append(r"\draw[accent,line width=0.3pt,opacity=0.3] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                     % (-width / 2, y0, width / 2, y0))
    return "\n".join(lines) + "\n"


def sierpinski_carpet(level=4):
    """Sierpinski carpet: keep the 8 outer squares of a 3x3 grid, recursively. Its Hausdorff
    dimension is log 8 / log 3 = 1.89..., between a curve and a surface (Tome 6, Chapter 11)."""
    side = 2 * R / 2 ** 0.5 * 0.92  # inscribed in the disc of radius R, with a margin
    lines = [f"% Sierpinski carpet at level {level}: 8^{level} squares, dimension log 8 / log 3."]
    squares = [(-side / 2, -side / 2, side)]
    for _ in range(level):
        squares = [(x + i * s / 3, y + j * s / 3, s / 3) for x, y, s in squares
                   for i in range(3) for j in range(3) if (i, j) != (1, 1)]
    gap = 0.12 * squares[0][2]
    for x, y, s in squares:
        lines.append(r"\fill[accent] (%.4fin,%.4fin) rectangle +(%.4fin,%.4fin);" % (x + gap / 2, y + gap / 2, s - gap, s - gap))
    lines.append(r"\draw[accent,line width=0.6pt,opacity=0.8] (%.4fin,%.4fin) rectangle +(%.4fin,%.4fin);"
                 % (-side / 2 - 0.08, -side / 2 - 0.08, side + 0.16, side + 0.16))
    return "\n".join(lines) + "\n"


def zeta_critical_line(t_max=42.0, steps=2400):
    """The curve t -> zeta(1/2 + it) for 0 <= t <= t_max: it loops around and passes through the
    origin at each zero on the critical line (Tome 5, Chapters 6-7). Computed by Euler-Maclaurin
    (Tome 4, Proposition 11.7) with N = 40 terms and six Bernoulli corrections."""
    B = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730]
    N = 40

    def zeta(s):
        tot = sum(n ** -s for n in range(1, N + 1)) + N ** (1 - s) / (s - 1) - N ** -s / 2
        poch = s
        for k in range(1, 7):
            tot += B[k - 1] / math.factorial(2 * k) * poch * N ** (1 - s - 2 * k)
            poch *= (s + 2 * k - 1) * (s + 2 * k)
        return tot

    pts = [zeta(complex(0.5, t_max * i / steps)) for i in range(steps + 1)]
    xs, ys = [z.real for z in pts], [z.imag for z in pts]
    cx, cy = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    scale = 0.95 * R / max(math.hypot(x - cx, y - cy) for x, y in zip(xs, ys))
    lines = ["%% The curve zeta(1/2+it), 0 <= t <= %g; it passes through 0 at every zero." % t_max]
    lines.append(r"\draw[accent,line width=0.3pt,opacity=0.35] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                 % ((min(xs) - cx) * scale - 0.1, -cy * scale, (max(xs) - cx) * scale + 0.1, -cy * scale))
    lines.append(r"\draw[accent,line width=0.3pt,opacity=0.35] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                 % (-cx * scale, (min(ys) - cy) * scale - 0.1, -cx * scale, (max(ys) - cy) * scale + 0.1))
    lines.append(r"\draw[accent,line width=0.9pt] " + "--".join(
        "(%.4fin,%.4fin)" % ((x - cx) * scale, (y - cy) * scale) for x, y in zip(xs, ys)) + ";")
    lines.append(r"\fill[accent] (%.4fin,%.4fin) circle (2.2pt);" % (-cx * scale, -cy * scale))
    return "\n".join(lines) + "\n"


MOTIFS = {
    "tome0-back-in-shape": times_table,
    "tome1-integers": sacks_spiral,
    "tome2-structures": buckyball,
    "tome3-chance": galton_board,
    "tome4-calculation": fourier_square,
    "tome5-meets": zeta_critical_line,
    "tome6-spaces": sierpinski_carpet,
}

if __name__ == "__main__":
    for tome, make in MOTIFS.items():
        if not (ROOT / tome).is_dir():
            continue
        (ROOT / tome / "cover-motif.tex").write_text(make())
        print("wrote", tome + "/cover-motif.tex")
