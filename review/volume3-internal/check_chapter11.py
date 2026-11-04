"""Representation foundations and, as added, exact character/model checks."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'volume3-symmetry/chapters/ch11-characters.tex'


def check_foundations():
    # Nonunitary coordinates for a C4 representation; exact Gaussian-integer powers.
    def mul(a, b):
        return [[sum(a[i][k]*b[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]
    def apply(a, v):
        return [sum(a[i][j]*v[j] for j in range(2)) for i in range(2)]
    identity = [[1, 0], [0, 1]]; r = [[1j, 2-2j], [0, -1j]]
    powers = [identity]
    for _ in range(3):
        powers.append(mul(powers[-1], r))
    assert mul(powers[-1], r) == identity
    def h(v, w):
        return sum(sum(a*b.conjugate() for a, b in zip(apply(g, v), apply(g, w)))
                   for g in powers)/4
    basis = [[1+0j, 0j], [0j, 1+0j]]
    for g in powers:
        for v in basis:
            for w in basis:
                assert h(apply(g, v), apply(g, w)) == h(v, w)
    e0 = basis[0]
    v = [1j, 1+0j]; coefficient = h(v, e0)/h(e0, e0)
    w = [a-coefficient*b for a, b in zip(v, e0)]
    assert h(w, e0) == 0 and h(w, w).real > 0 and h(w, w).imag == 0
    assert apply(r, w) == [-1j*z for z in w]
    assert h([1j*z for z in v], w) == 1j*h(v, w)
    assert h(v, [1j*z for z in w]) == -1j*h(v, w)
    assert h(v, w) == h(w, v).conjugate()
    # The real theorem does not supply this complex argument; local construction does.
    source = SOURCE.read_text()
    assert '$G$ is finite' in source and r'd\ge0' in source and r'$V\ne0$' in source
    assert 'spectral theorem, Volume~1' not in source
    assert 'conjugate-linear in the second' in source
    # The modular counterexample: all three possible complementary lines fail.
    u = [[1, 1], [0, 1]]; power = identity
    for _ in range(3):
        power = [[x % 3 for x in row] for row in mul(power, u)]
    assert power == identity and u != identity
    for a in range(3):
        assert ((a+1) % 3, 1) != (a, 1)


if __name__ == '__main__':
    check_foundations()
    print('PASS: complex invariant Hermitian average/projection; finite/zero/irreducible domains; local complex prerequisite; modular complement counterexample')
