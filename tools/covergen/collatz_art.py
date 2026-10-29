"""Volume 1: the Collatz coral, rotated so its visual mass sits on the axis."""
import math
import numpy as np
from collatz import tree as raw_tree, T_std

N, AE, SH = 8000, 0.22, 0.98
AO = 0.495
BOX = (0.55, 5.45, 3.18, 6.68)


def _weights(par, cnt, pos):
    dep = {1: 0}
    for m in par:
        st = []
        q = m
        while q not in dep:
            st.append(q)
            q = par[q]
        for r in reversed(st):
            dep[r] = dep[par[r]] + 1
    W = []
    for m, p in par.items():
        c = cnt.get(m, 1)
        wb = min(12, int(round(math.log10(c) * 3.2)))
        w = 0.12 + 0.17 * wb
        op = min(1, (0.36 + 0.22 * math.log(c)) * SH ** (0.30 * dep[m]))
        (x0, y0), (x1, y1) = pos[p], pos[m]
        W.append(((x0 + x1) / 2, (y0 + y1) / 2, w * op * math.hypot(x1 - x0, y1 - y0)))
    return W


def balanced_tree():
    par, cnt, pos = raw_tree(N, AE, AO, shrink=SH, std=True)
    W = np.array(_weights(par, cnt, pos))
    P = np.array(list(pos.values()))
    best = None
    for th in np.linspace(-0.6, 0.6, 1201):
        c, s_ = math.cos(th), math.sin(th)
        x = c * P[:, 0] - s_ * P[:, 1]
        y = s_ * P[:, 0] + c * P[:, 1]
        if y.min() < -0.02 * (y.max() - y.min()):
            continue
        span = x.max() - x.min()
        cx = ((c * W[:, 0] - s_ * W[:, 1]) * W[:, 2]).sum() / W[:, 2].sum()
        mid = (x.max() + x.min()) / 2
        sc = abs(cx) / span + abs(mid) / span
        if best is None or sc < best[0]:
            best = (sc, float(th))
    c, s_ = math.cos(best[1]), math.sin(best[1])
    pos = {m: (c * x - s_ * y, s_ * x + c * y) for m, (x, y) in pos.items()}
    return par, cnt, pos


def batched(opts, paths, n=150):
    return [r'\draw[%s,line cap=round,line join=round] %s;' % (opts, ' '.join(paths[i:i + n]))
            for i in range(0, len(paths), n)]


def art():
    par, cnt, pos = balanced_tree()
    dep = {1: 0}
    for m in par:
        st = []
        q = m
        while q not in dep:
            st.append(q)
            q = par[q]
        for r in reversed(st):
            dep[r] = dep[par[r]] + 1
    xs = [p[0] for p in pos.values()]
    ys = [p[1] for p in pos.values()]
    k = min((BOX[1] - BOX[0]) / 2 / max(abs(min(xs)), abs(max(xs))),
            (BOX[3] - BOX[2]) / (max(ys) - min(ys)))
    X = lambda m: 3.0 + k * pos[m][0]
    Y = lambda m: BOX[2] + k * (pos[m][1] - min(ys))

    def style(m):
        c = cnt.get(m, 1)
        L = math.log10(c)
        wb = min(12, int(round(L * 3.2)))
        ob = min(10, int(round(10 * min(1, (0.36 + 0.22 * math.log(c)) * SH ** (0.30 * dep[m])))))
        return wb, ob

    sty = {m: style(m) for m in par}
    children = {}
    for m, p in par.items():
        children.setdefault(p, []).append(m)
    lines = {}
    for m in par:
        p = par[m]
        if p in sty and sty[p] == sty[m] and len(children.get(p, [])) == 1:
            continue
        chain = [p, m]
        q = m
        while True:
            ch = [c for c in children.get(q, []) if sty[c] == sty[m]]
            if len(children.get(q, [])) == 1 and ch:
                q = ch[0]
                chain.append(q)
            else:
                break
        lines.setdefault(sty[m], []).append('--'.join('(%.4fin,%.4fin)' % (X(v), Y(v)) for v in chain))
    out = []
    for (wb, ob), paths in sorted(lines.items()):
        if wb < 5:
            continue
        w = 0.12 + 0.17 * wb
        for f, a in ((7, .030), (3.2, .07)):
            out += batched('draw=ocCoverCoral,line width=%.2fpt,draw opacity=%.3f' % (w * f, a * ob / 10), paths)
    for (wb, ob), paths in sorted(lines.items()):
        w = 0.12 + 0.17 * wb
        op = max(0.10, ob / 10)
        hot = max(0, (wb - 8) / 4)
        col = 'ocCoral' if hot <= 0 else 'ocCoverLight'
        out += batched('draw=%s,line width=%.3fpt,draw opacity=%.3f' % (col, w, op), paths)
    orb = [27]
    while orb[-1] != 1:
        orb.append(T_std(orb[-1]))
    d = '--'.join('(%.4fin,%.4fin)' % (X(v), Y(v)) for v in orb)
    out.append(r'\draw[draw=ocCoverTitle,line width=1.2pt,draw opacity=.07,line cap=round,line join=round] %s;' % d)
    out.append(r'\draw[draw=ocCoverTitle,line width=0.38pt,draw opacity=.70,line cap=round,line join=round] %s;' % d)
    out.append(r'\fill[ocCoverTitle] %s circle (0.022in);' % ('(%.4fin,%.4fin)' % (X(27), Y(27))))
    out.append(r'\fill[ocCoral,opacity=.25] %s circle (0.07in);' % ('(%.4fin,%.4fin)' % (X(1), Y(1))))
    out.append(r'\fill[ocCoverTitle] %s circle (0.03in);' % ('(%.4fin,%.4fin)' % (X(1), Y(1))))
    return out
