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


def ford_circles(qmax=80):
    """Ford circles: above each fraction p/q (lowest terms), the circle of radius 1/(2q^2)
    tangent to the line at p/q. Two of them touch exactly when the fractions are Farey neighbours,
    and SL2(Z) permutes them (Tome 12, Chapter 14). Drawn for p/q in [0, 1], clipped to the disc."""
    s = 2.7 * R                       # length of the unit interval on the cover
    y0 = -0.42 * R                    # the line on which the circles stand
    lines = ["%% Ford circles for p/q in [0,1], q <= %d: radius 1/(2q^2), tangent at p/q." % qmax,
             r"\begin{scope}",
             r"\clip (0,0) circle (%.4fin);" % R,
             r"\draw[accent,line width=0.5pt,opacity=0.7] (%.4fin,%.4fin)--(%.4fin,%.4fin);" % (-R, y0, R, y0)]
    for q in range(1, qmax + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            r = s / (2 * q * q)
            x = -s / 2 + s * p / q
            if r < 0.003 or abs(x) > R + r:
                continue
            w = max(0.12, min(0.9, 2.4 / q))
            lines.append(r"\draw[accent,line width=%.2fpt] (%.4fin,%.4fin) circle (%.4fin);" % (w, x, y0 + r, r))
    lines.append(r"\end{scope}")
    return "\n".join(lines) + "\n"


def boolean_lattice(n=5):
    """Hasse diagram of the subsets of {1,...,n}, ranks as rows, with a symmetric chain
    decomposition (de Bruijn, Tengbergen and Kruyswijk, 1951; Tome C1, Chapter 2) drawn as
    vertical gold chains and the other covering edges faint."""
    chains = [[frozenset(), frozenset([1])]]          # the subsets of {1}, then induction on n
    for k in range(2, n + 1):
        new = []
        for c in chains:                              # c = A1 < ... < Am  gives two chains
            new.append(c + [c[-1] | {k}])
            if len(c) > 1:
                new.append([a | {k} for a in c[:-1]])
        chains = new
    # columns: longest chains in the middle, alternating left and right
    chains.sort(key=lambda c: -len(c))
    order = []
    for i, c in enumerate(chains):
        order.insert(0, c) if i % 2 else order.append(c)
    col = {}
    for j, c in enumerate(order):
        for a in c:
            col[a] = j
    m = len(order)
    dx, dy = 2 * 1.92 / (m - 1), 0.8
    pos = {a: (-1.92 + dx * col[a], dy * (len(a) - n / 2)) for a in col}
    lines = ["%% Boolean lattice of the subsets of {1..%d} with a symmetric chain decomposition." % n]
    chain_edges = {(c[i], c[i + 1]) for c in order for i in range(len(c) - 1)}
    for a in pos:
        for k in range(1, n + 1):
            if k not in a:
                b = a | {k}
                if (a, b) in chain_edges:
                    continue
                (x1, y1), (x2, y2) = pos[a], pos[b]
                lines.append(r"\draw[accent,line width=0.35pt,opacity=0.35] (%.4fin,%.4fin)--(%.4fin,%.4fin);" % (x1, y1, x2, y2))
    for a, b in chain_edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        lines.append(r"\draw[accent,line width=1.6pt,line cap=round] (%.4fin,%.4fin)--(%.4fin,%.4fin);" % (x1, y1, x2, y2))
    for a, (x, y) in pos.items():
        lines.append(r"\fill[accent] (%.4fin,%.4fin) circle (0.055in);" % (x, y))
        lines.append(r"\fill[navy] (%.4fin,%.4fin) circle (0.028in);" % (x, y))
    return "\n".join(lines) + "\n"


def lozenge_tiling(a=28, sweeps=8000, seed=7):
    """A uniformly random lozenge tiling of the hexagon of side a, seen as a random plane
    partition in an a x a x a box (Tome S1, Chapter 2: Lindstrom-Gessel-Viennot). The heights
    are sampled by heat-bath Glauber dynamics on a checkerboard: given its four neighbours, the
    height of a column is uniform on the allowed interval. The corners freeze and the centre
    stays disordered, inside the 'arctic circle'. Three shades for the three orientations make
    the stepped surface look like a pile of cubes."""
    import numpy as np
    rng = np.random.default_rng(seed)
    h = np.full((a, a), a // 2, dtype=int)
    I, J = np.indices((a, a))
    masks = [(I + J) % 2 == 0, (I + J) % 2 == 1]
    for _ in range(sweeps):
        for m in masks:
            p = np.pad(h, 1, constant_values=0)
            p[0, :] = a; p[:, 0] = a          # the box walls behind
            up = np.minimum(p[:-2, 1:-1], p[1:-1, :-2])
            lo = np.maximum(p[2:, 1:-1], p[1:-1, 2:])
            new = lo + (rng.random((a, a)) * (up - lo + 1)).astype(int)
            h[m] = new[m]
    h = h.tolist()
    H = lambda i, j: a if i < 0 or j < 0 else (0 if i >= a or j >= a else h[i][j])
    u = 2.25 / a                                  # inches per unit edge
    c, s = math.cos(math.pi / 6), 0.5
    P = lambda x, y, z: (u * c * (x - y), u * (z - s * (x + y)))
    faces = []
    for i in range(a):
        for j in range(a):
            z = h[i][j]
            faces.append((0.80, [P(i, j, z), P(i + 1, j, z), P(i + 1, j + 1, z), P(i, j + 1, z)]))
    for i in range(a + 1):                        # faces facing +x, in the plane x = i
        for j in range(a):
            for z in range(H(i, j), H(i - 1, j)):
                faces.append((0.42, [P(i, j, z), P(i, j + 1, z), P(i, j + 1, z + 1), P(i, j, z + 1)]))
    for j in range(a + 1):                        # faces facing +y, in the plane y = j
        for i in range(a):
            for z in range(H(i, j), H(i, j - 1)):
                faces.append((0.18, [P(i, j, z), P(i + 1, j, z), P(i + 1, j, z + 1), P(i, j, z + 1)]))
    # shift so that the hexagon is centred at the origin
    cy = (P(0, 0, a)[1] + P(a, a, 0)[1]) / 2
    lines = ["%% A random lozenge tiling of the hexagon of side %d (a random plane partition in a box)." % a]
    for op, pts in faces:
        path = "--".join("(%.4fin,%.4fin)" % (x, y - cy) for x, y in pts)
        lines.append(r"\filldraw[fill=accent,fill opacity=%.2f,draw=navy,line width=0.2pt] %s--cycle;" % (op, path))
    return "\n".join(lines) + "\n"


def gaussian_primes(N=26):
    """Problem Book P1: the Gaussian primes a+bi with a^2+b^2 <= N^2, a picture where Tome 1
    (which primes split), Tome 2 (the ring Z[i]) and geometry meet. It has the eight symmetries
    of the square."""
    s = R / (N + 0.5)
    pr = set(primes_upto(2 * N * N + 2))
    def is_gp(a, b):
        a, b = abs(a), abs(b)
        if a == 0 or b == 0:
            m = a + b
            return m in pr and m % 4 == 3
        return a * a + b * b in pr
    lines = ["%% Gaussian primes a+bi with a^2+b^2 <= %d^2." % N]
    for a in range(-N, N + 1):
        for b in range(-N, N + 1):
            if a * a + b * b <= N * N and is_gp(a, b):
                lines.append(r"\fill[accent] (%.4fin,%.4fin) rectangle ++(%.4fin,%.4fin);"
                             % (s * (a - 0.42), s * (b - 0.42), 0.84 * s, 0.84 * s))
    return "\n".join(lines) + "\n"


def confocal_grid(Y=1.45, n_ell=9, n_hyp=8):
    """The image of a rectangular grid under the conformal map z -> sin z: the horizontal lines
    become confocal ellipses, the vertical lines confocal hyperbolas, and they still cross at right
    angles (Tome 7, Chapter 9). The foci are +-1, where the map stops being conformal."""
    scale = 0.97 * R / math.cosh(Y)
    lines = ["% Image of a rectangular grid under sin z: confocal ellipses and hyperbolas."]
    pt = lambda w: "(%.4fin,%.4fin)" % (w.real * scale, w.imag * scale)
    for k in range(1, n_ell + 1):
        c = Y * k / n_ell
        pts = [pt(complex(math.sin(2 * math.pi * t / 400) * math.cosh(c), math.cos(2 * math.pi * t / 400) * math.sinh(c))) for t in range(401)]
        lines.append(r"\draw[accent,line width=%.2fpt] " % (0.5 + 0.6 * k / n_ell) + "--".join(pts) + ";")
    for k in range(-n_hyp + 1, n_hyp):
        c = math.pi / 2 * k / n_hyp
        pts = [pt(complex(math.sin(c) * math.cosh(y), math.cos(c) * math.sinh(y)))
               for y in (Y * (2 * t / 300 - 1) for t in range(301))]
        lines.append(r"\draw[accent,line width=0.5pt,opacity=0.75] " + "--".join(pts) + ";")
    lines.append(r"\fill[accent] (%.4fin,0) circle (2.4pt) (%.4fin,0) circle (2.4pt);" % (scale, -scale))
    return "\n".join(lines) + "\n"


def apollonian_gasket(rmin=0.004, label_r=0.06):
    """Tome S2: the integral Apollonian gasket with root quadruple (-1, 2, 2, 3). Every circle
    is tangent to three others, and by Descartes' theorem every curvature is an integer; the
    larger circles carry theirs. New circles come from the reflection d' = 2(a + b + c) - d,
    applied to curvatures and to curvature times centre (the complex Descartes theorem)."""
    quads = [((-1, 0j), (2, 0.5 + 0j), (2, -0.5 + 0j), (3, 2j / 3))]
    quads.append(((-1, 0j), (2, 0.5 + 0j), (2, -0.5 + 0j), (3, -2j / 3)))
    circles = {(k, round(z.real, 9), round(z.imag, 9)): (k, z) for k, z in quads[0] + quads[1]}
    stack = [(q, 3) for q in quads]
    while stack:
        q, i = stack.pop()
        for j in range(4):
            if j == i:
                continue
            others = [q[m] for m in range(4) if m != j]
            k = 2 * sum(c[0] for c in others) - q[j][0]
            kz = 2 * sum(c[0] * c[1] for c in others) - q[j][0] * q[j][1]
            if 1 / k < rmin:
                continue
            z = kz / k
            key = (k, round(z.real, 9), round(z.imag, 9))
            if key in circles:
                continue
            circles[key] = (k, z)
            nq = list(q)
            nq[j] = (k, z)
            stack.append((tuple(nq), j))
    lines = ["%% The integral Apollonian gasket with root (-1, 2, 2, 3); %d circles of radius >= %g."
             % (len(circles), rmin)]
    for k, z in sorted(circles.values(), key=lambda c: c[0]):
        r = 1 / abs(k)
        w = max(0.15, min(1.0, 3.0 / k)) if k > 0 else 1.0
        lines.append(r"\draw[accent,line width=%.2fpt] (%.4fin,%.4fin) circle (%.4fin);"
                     % (w, R * z.real, R * z.imag, R * r))
        if k > 0 and r >= label_r:
            lines.append(r"\node[accent,font=\sffamily,scale=%.2f] at (%.4fin,%.4fin) {%d};"
                         % (min(2.2, 9.0 * r), R * z.real, R * z.imag, k))
    return "\n".join(lines) + "\n"


def bitonic_network(n=16):
    """Batcher's bitonic sorting network on n wires (Tome C2, Chapter 2): horizontal wires,
    each comparator a vertical segment whose arrowhead marks where the larger value goes.
    Comparators of one stage whose spans overlap are drawn in separate sub-columns."""
    cols = []
    k = 2
    while k <= n:
        j = k // 2
        while j >= 1:
            stage = [(i, i ^ j, (i & k) == 0) for i in range(n) if (i ^ j) > i]
            sub = {}
            for i, l, up in stage:
                sub.setdefault(i % j, []).append((i, l, up))
            cols.extend(sub[r] for r in sorted(sub))
            j //= 2
        k *= 2
    W, H = 1.92, 1.9
    dx = 2 * W / (len(cols) + 1)
    ys = [H - 2 * H * w / (n - 1) for w in range(n)]
    lines = ["%% Batcher's bitonic sorting network on %d wires." % n]
    for y in ys:
        lines.append(r"\draw[accent,line width=0.5pt,opacity=0.6] (%.4fin,%.4fin)--(%.4fin,%.4fin);" % (-W - 0.1, y, W + 0.1, y))
    for c, comps in enumerate(cols):
        x = -W + dx * (c + 1)
        for i, l, asc in comps:
            top, bot = ys[i], ys[l]          # wire i is above wire l
            tip = bot if asc else top        # ascending: the larger value goes to the lower wire
            lines.append(r"\draw[accent,line width=1.1pt,-latex] (%.4fin,%.4fin)--(%.4fin,%.4fin);"
                         % (x, top if asc else bot, x, tip))
            for y in (top, bot):
                lines.append(r"\fill[accent] (%.4fin,%.4fin) circle (0.03in);" % (x, y))
    return "\n".join(lines) + "\n"


def stick_breaking(rings=13, seed=10):
    """Poisson-Dirichlet stick-breaking: each ring is one sample of the GEM(1) law, the circle
    broken at a uniform point, the rest broken again, and so on. The arc lengths are the cycle
    proportions of a large random permutation, and of the prime factors of a large random
    integer (Tome 10, Chapter 12). Drawn with a fixed seed so the cover is reproducible."""
    import random
    rng = random.Random(seed)
    lines = ["%% Stick-breaking (GEM(1)) samples, one per ring, seed %d." % seed, r"\begin{scope}"]
    for i in range(rings):
        r = R * (0.22 + 0.76 * i / (rings - 1))
        w = 6.5 * (0.6 + 0.4 * i / (rings - 1))
        left, start = 1.0, 90.0 + rng.uniform(0, 360)
        while left > 0.004:
            piece = left * rng.random()
            left -= piece
            sweep = 360.0 * piece
            if sweep > 2.2:
                a, b = start + 0.9, start + sweep - 0.9
                op = 0.35 + 0.65 * min(1.0, piece * 2.2)
                lines.append(r"\draw[accent,line width=%.2fpt,opacity=%.2f] (%.3f:%.4fin) arc (%.3f:%.3f:%.4fin);"
                             % (w, op, a, r, a, b, r))
            start += sweep
    lines.append(r"\end{scope}")
    return "\n".join(lines) + "\n"


def farey_tessellation(depth=8, nmax=40):
    """The Farey tessellation of the hyperbolic disc: the geodesics joining p/q and r/s whenever
    ps - qr = +-1, carried from the upper half-plane by the Cayley map z -> (z-i)/(z+i). They cut
    the disc into ideal triangles, all images of one triangle under the modular group SL2(Z)
    (Tome 8, Chapter 9)."""
    from fractions import Fraction

    def to_angle(x):                   # boundary point of the half-plane -> angle on the circle
        if x is None:
            return 0.0
        w = complex(x, -1) / complex(x, 1)
        return math.atan2(w.imag, w.real)

    def arc(a, b, n=60):
        d = (b - a + math.pi) % (2 * math.pi) - math.pi   # signed angular gap in (-pi, pi]
        if abs(abs(d) - math.pi) < 1e-9:
            return [(R * math.cos(a), R * math.sin(a)), (R * math.cos(b), R * math.sin(b))], math.pi
        m = a + d / 2
        dist = 1 / math.cos(d / 2)
        rad = abs(math.tan(d / 2))
        cx, cy = dist * math.cos(m), dist * math.sin(m)
        # the arc runs inside the disc, from e^{ia} to e^{ib}, on the circle centred at (cx, cy)
        ta = math.atan2(math.sin(a) - cy, math.cos(a) - cx)
        tb = math.atan2(math.sin(b) - cy, math.cos(b) - cx)
        dt = (tb - ta + math.pi) % (2 * math.pi) - math.pi
        pts = [(R * (cx + rad * math.cos(ta + dt * k / n)), R * (cy + rad * math.sin(ta + dt * k / n)))
               for k in range(n + 1)]
        return pts, abs(d)

    edges = [(Fraction(n), None) for n in range(-nmax, nmax + 1)]
    stack = [((n, 1), (n + 1, 1), 0) for n in range(-nmax, nmax)]
    while stack:
        (p, q), (r, t), k = stack.pop()
        edges.append((Fraction(p, q), Fraction(r, t)))
        if k < depth:
            m = (p + r, q + t)
            stack.append(((p, q), m, k + 1))
            stack.append((m, (r, t), k + 1))
    lines = ["%% Farey tessellation in the disc: geodesics p/q -- r/s with ps-qr=+-1, depth %d." % depth,
             r"\draw[accent,line width=0.9pt] (0,0) circle (%.4fin);" % R]
    for x, y in edges:
        a, b = to_angle(x), to_angle(y)
        gap0 = abs((b - a + math.pi) % (2 * math.pi) - math.pi)
        if gap0 < 0.012:
            continue
        pts, gap = arc(a, b, n=max(6, int(70 * gap0 / math.pi)))
        if gap < 0.012:
            continue
        w = max(0.12, min(1.1, 1.6 * gap))
        lines.append(r"\draw[accent,line width=%.2fpt] " % w + "--".join("(%.4fin,%.4fin)" % pt for pt in pts) + ";")
    return "\n".join(lines) + "\n"


MOTIFS = {
    "tome0-back-in-shape": times_table,
    "tome1-integers": sacks_spiral,
    "tome2-structures": buckyball,
    "tome3-chance": galton_board,
    "tome4-calculation": fourier_square,
    "tome5-meets": zeta_critical_line,
    "tome6-spaces": sierpinski_carpet,
    "tome7-analysis": confocal_grid,
    "tome8-shapes": farey_tessellation,
    "tome10-chance2": stick_breaking,
    "tome12-arithmetic": ford_circles,
    "tomeC1-discrete": boolean_lattice,
    "tomeC2-algorithms": bitonic_network,
    "tomeS1-linear": lozenge_tiling,
    "tomeS2-geometry": apollonian_gasket,
    "tomeP1-crossroads": gaussian_primes,
}

if __name__ == "__main__":
    for tome, make in MOTIFS.items():
        if not (ROOT / tome).is_dir():
            continue
        (ROOT / tome / "cover-motif.tex").write_text(make())
        print("wrote", tome + "/cover-motif.tex")
