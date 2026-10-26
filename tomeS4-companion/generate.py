#!/usr/bin/env python3
"""Generate the reference chapters of Tome S4 (The Companion) from the sources of every tome.

Run from anywhere: python3 tomeS4-companion/generate.py. It reads common/series.tex and every
tome*/main.tex with its chapters, and writes
  tomeS4-companion/data/series.json        the parsed series (tomes, chapters, results, citations)
  tomeS4-companion/chapters/gen-*.tex      the generated chapters and tables
  tomeS4-companion/figures/citations.tex   the citation matrix
and prints the cross-tome references that point to a missing or different result.
build.sh runs it before building the tome, so the Companion follows the series as tomes land.
"""
import json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HERE = ROOT / "tomeS4-companion"
CHTITLE = {"Part I. Foundations": "Part I: Foundations", "Part II. The graduate toolbox": "Part II: The Graduate Toolbox",
           "Part III. Toward research": "Part III: Toward Research", "The Computing track": "The Computing Track",
           "Companion volumes": "The Companion Volumes", "Problem books": "The Problem Books"}
KINDS = ("theorem", "proposition", "lemma", "corollary", "definition", "example")
CITE_KINDS = {"Theorem": "theorem", "Proposition": "proposition", "Lemma": "lemma", "Corollary": "corollary",
              "Definition": "definition", "Example": "example", "Exercise": "exercise", "Problem": "exercise"}


def strip_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in s.splitlines())


def balanced(s, i, op="{", cl="}"):
    """s[i] == op; return (content, index after the closing bracket)."""
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\": j += 2; continue
        if c == op: depth += 1
        elif c == cl:
            depth -= 1
            if depth == 0: return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced at %d" % i)


def series_plan():
    parts, tomes = [], []
    for line in strip_comments((ROOT / "common/series.tex").read_text()).splitlines():
        m = re.match(r"\\seriespart\{(.*)\}", line.strip())
        if m: parts.append({"name": m.group(1), "tomes": []}); continue
        m = re.match(r"\\seriestome\{([^}]*)\}\{([^}]*)\}\{(.*)\}", line.strip())
        if m:
            t = {"num": m.group(1), "title": m.group(2), "theme": m.group(3), "part": parts[-1]["name"]}
            parts[-1]["tomes"].append(t["num"]); tomes.append(t)
    return parts, tomes


def tome_dirs():
    out = {}
    for d in sorted(ROOT.glob("tome*/main.tex")):
        first = d.read_text().splitlines()[0]
        m = re.match(r"% epub-title: .*Tome (\w+): (.*)", first)
        if m: out[m.group(1)] = d.parent
    return out


def parse_chapter(path, chnum):
    s = strip_comments(path.read_text())
    m = re.search(r"\\chapter\{", s)
    title, _ = balanced(s, m.end() - 1)
    lab = re.match(r"\s*\\label\{([^}]*)\}", s[_:])
    res, n, ex, sec = [], 0, 0, ""
    events = []
    for m in re.finditer(r"\\section\*?\{|\\begin\{(%s|exercise)\}" % "|".join(KINDS), s):
        events.append(m)
    for m in events:
        if m.group(0).startswith("\\section"):
            sec, _e = balanced(s, m.end() - 1)
            if m.group(0).startswith("\\section*"): sec = sec
            continue
        kind = m.group(1)
        j = m.end(); name = None
        while j < len(s) and s[j] in " \t": j += 1
        if j < len(s) and s[j] == "[":
            name, j = balanced(s, j, "[", "]")
        lm = re.match(r"\s*\\label\{([^}]*)\}", s[j:])
        label = lm.group(1) if lm else None
        if kind == "exercise":
            ex += 1
            res.append({"kind": "exercise", "num": "%d.%d" % (chnum, ex), "label": label, "stars": name, "section": sec})
        else:
            n += 1
            res.append({"kind": kind, "num": "%d.%d" % (chnum, n), "name": name.strip() if name else None, "label": label,
                        "section": sec})
    return {"num": chnum, "title": title.strip(), "label": lab.group(1) if lab else None, "results": res}, s


def resolve_refs(tome):
    labels = {r["label"]: r["num"] for ch in tome["chapters"] for r in ch["results"] if r.get("label")}
    labels.update({ch["label"]: str(ch["num"]) for ch in tome["chapters"] if ch.get("label")})
    for ch in tome["chapters"]:
        for r in ch["results"]:
            if r.get("name") and "\\ref" in r["name"]:
                r["name"] = re.sub(r"\\(?:eq)?ref\{([^}]*)\}", lambda m: labels.get(m.group(1), "?"), r["name"])


def parse_tome(num, d):
    main = strip_comments((d / "main.tex").read_text())
    inputs = re.findall(r"\\input\{chapters/([^}]*)\}", main)
    chapters, texts, k = [], [], 0
    for c in inputs:
        p = d / "chapters" / (c + ".tex")
        if not p.exists(): continue
        raw = strip_comments(p.read_text())
        if not re.search(r"\\chapter\{", raw): continue
        k += 1
        ch, s = parse_chapter(p, k)
        ch["file"] = c
        chapters.append(ch); texts.append((k, s))
    return {"num": num, "dir": d.name, "chapters": chapters}, texts


NUMS = r"\d+(?:\.\d+)?"
CITE_RE = re.compile(r"Tome~(\w+),\s*(%s)s?~(%s)((?:(?:,\s*|,?\s+and~?|--)(?:%s))*)" % ("|".join(CITE_KINDS) + "|Chapter", NUMS, NUMS))


def citations(num, texts):
    out = []
    for chnum, s in texts:
        for m in CITE_RE.finditer(s):
            target, word = m.group(1), m.group(2)
            if target == num: continue
            nums = [m.group(3)] + re.findall(NUMS, m.group(4) or "")
            for x in nums:
                out.append({"from": num, "chapter": chnum, "to": target, "word": word, "num": x})
    return out


def sortkey(name):
    s = name.replace("$", "")
    s = re.sub(r"\\[\"'`^~=.]\{?(\w)\}?", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = re.sub(r"[{}~]", "", s).replace("--", "-")
    s = re.sub(r"[^\w\s-]", " ", s)
    s = unicodedata.normalize("NFKD", s.replace("Ł", "L").replace("ł", "l"))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\s+", " ", s).strip(" -").lower()
    for art in ("the ", "a ", "an "):
        if s.startswith(art): s = s[len(art):]
    return s.strip(" -")


def tex_tome(num):
    return "Tome~%s" % num


def main():
    parts, plan = series_plan()
    dirs = tome_dirs()
    data, cites = {}, []
    for t in plan:
        if t["num"] in dirs and t["num"] != "S4":
            tome, texts = parse_tome(t["num"], dirs[t["num"]])
            resolve_refs(tome)
            data[t["num"]] = tome
            cites += citations(t["num"], texts)
    # resolve the citations
    index = {}
    for num, tome in data.items():
        for ch in tome["chapters"]:
            for r in ch["results"]:
                index[(num, r["num"], "exercise" if r["kind"] == "exercise" else "result")] = r
    problems, used = [], defaultdict(set)
    for c in cites:
        if c["to"] not in data:
            c["status"] = "unwritten"; continue
        tome = data[c["to"]]
        if c["word"] == "Chapter":
            ok = "." not in c["num"] and 1 <= int(c["num"]) <= len(tome["chapters"])
            c["status"] = "ok" if ok else "missing"
        else:
            kind = CITE_KINDS[c["word"]]
            r = index.get((c["to"], c["num"], "exercise" if kind == "exercise" else "result"))
            if r is None: c["status"] = "missing"
            elif r["kind"] != kind: c["status"] = "kind:%s" % r["kind"]
            else:
                c["status"] = "ok"; used[(c["to"], c["num"], kind)].add(c["from"])
        if c["status"] != "ok":
            problems.append(c)
    (HERE / "data").mkdir(exist_ok=True)
    json.dump({"parts": parts, "plan": plan, "tomes": data, "citations": cites}, open(HERE / "data/series.json", "w"), indent=1)

    planned = {t["num"]: t for t in plan}
    written = [t["num"] for t in plan if t["num"] in data]

    # ---- the map: table of tomes
    L = [r"% Generated by generate.py: do not edit.", r"\begin{center}\small\adjustbox{max width=\linewidth,max totalheight=0.85\textheight}{%", r"\begin{tabular}{@{}lp{0.52\linewidth}rrr@{}}",
         r"Tome&Title&ch.&named&ex.\\\hline"]
    for p in parts:
        L.append(r"\multicolumn{5}{@{}l}{\textit{%s}}\\" % p["name"])
        for num in p["tomes"]:
            t = planned[num]
            if num in data:
                chs = data[num]["chapters"]
                nm = sum(1 for ch in chs for r in ch["results"] if r["kind"] not in ("exercise", "example") and r.get("name"))
                nex = sum(1 for ch in chs for r in ch["results"] if r["kind"] == "exercise")
                L.append(r"%s&%s&%d&%d&%d\\" % (num, t["title"], len(chs), nm, nex))
            elif num == "S4":
                L.append(r"%s&%s (this book)&&&\\" % (num, t["title"]))
            else:
                L.append(r"%s&%s&\multicolumn{3}{c}{\textit{in preparation}}\\" % (num, t["title"]))
    L += [r"\end{tabular}}", r"\end{center}"]
    (HERE / "chapters/gen-tometable.tex").write_text("\n".join(L) + "\n")

    # ---- the citation matrix
    M = Counter((c["from"], c["to"]) for c in cites if c["status"] == "ok")
    order = [n for n in written]
    k = len(order); cell = 0.42
    mx = max(M.values()) if M else 1
    F = [r"% Generated by generate.py: rows cite columns; numbers are citations of numbered results and chapters.",
         r"\begin{tikzpicture}[font=\tiny]"]
    for i, a in enumerate(order):
        F.append(r"\node[left] at (0,%.3f) {%s};" % (-(i + 0.5) * cell, a))
        F.append(r"\node[above,rotate=90,anchor=west] at (%.3f,0.05) {%s};" % ((i + 0.5) * cell, a))
        for j, b in enumerate(order):
            v = M.get((a, b), 0)
            if v:
                shade = 15 + int(70 * (v / mx) ** 0.5)
                F.append(r"\fill[MidnightBlue!%d] (%.3f,%.3f) rectangle ++(%.3f,%.3f);" % (shade, j * cell, -(i + 1) * cell, cell, cell))
                F.append(r"\node[%s] at (%.3f,%.3f) {%d};" % ("white" if shade > 55 else "black", (j + 0.5) * cell, -(i + 0.5) * cell, v))
    F.append(r"\draw[black!40] (0,0) grid[step=%.3f] (%.3f,%.3f);" % (cell, k * cell, -k * cell))
    F.append(r"\draw[black!40] (0,0) rectangle (%.3f,%.3f);" % (k * cell, -k * cell))
    F.append(r"\node[below] at (%.3f,%.3f) {\scriptsize each row cites the columns};" % (k * cell / 2, -k * cell - 0.05))
    F.append(r"\end{tikzpicture}")
    (HERE / "figures").mkdir(exist_ok=True)
    (HERE / "figures/citations.tex").write_text("\n".join(F) + "\n")

    # ---- results, one chapter per part
    KN = {"theorem": "Theorem", "proposition": "Proposition", "lemma": "Lemma", "corollary": "Corollary",
          "definition": "Definition", "example": "Example"}
    files = []
    for pi, p in enumerate(parts):
        L = [r"% Generated by generate.py: do not edit."]
        L.append(r"\chapter{%s}" % CHTITLE.get(p["name"], p["name"]))
        for num in p["tomes"]:
            if num not in data: continue
            t, tome = planned[num], data[num]
            L.append(r"\section{Tome %s: %s}" % (num, t["title"]))
            for ch in tome["chapters"]:
                named = [r for r in ch["results"] if r["kind"] not in ("exercise", "example") and r.get("name")]
                nex = sum(1 for r in ch["results"] if r["kind"] == "exercise")
                L.append(r"\subsection*{%s.\ %s}" % (ch["num"], ch["title"]))
                if num.startswith("P"):
                    L.append(r"%d problems." % nex); continue
                if not named:
                    L.append(r"No named results; %d exercises." % nex); continue
                L.append(r"\begin{results}")
                for r in named:
                    L.append(r"\item[%s] %s (%s)" % (r["num"], KN[r["kind"]], r["name"]))
                L.append(r"\end{results}")
        fn = "gen-part%d" % (pi + 1)
        (HERE / "chapters" / (fn + ".tex")).write_text("\n".join(L) + "\n")
        files.append(fn)

    # ---- most cited results
    top = sorted(used.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:40]
    L = [r"% Generated by generate.py: do not edit.", r"\begin{results}"]
    for (to, n, kind), frm in top:
        r = index[(to, n, "exercise" if kind == "exercise" else "result")]
        name = (" (%s)" % r["name"]) if r.get("name") else ""
        ch = data[to]["chapters"][int(n.split(".")[0]) - 1]["title"]
        L.append(r"\item[%s] %s~%s%s, in \emph{%s}; cited by %s." % (to, kind.capitalize(), n, name, ch,
                 ", ".join(tex_tome(x) for x in sorted(frm, key=lambda x: [o for o in order].index(x)))))
    L.append(r"\end{results}")
    (HERE / "chapters/gen-mostcited.tex").write_text("\n".join(L) + "\n")

    # ---- citations by tome
    L = [r"% Generated by generate.py: do not edit."]
    for a in order:
        row = [(b, M[(a, b)]) for b in order if M.get((a, b))]
        if not row: continue
        L.append(r"\paragraph{Tome %s} cites %s." % (a, ", ".join("Tome~%s (%d)" % (b, v) for b, v in row)))
    (HERE / "chapters/gen-citesby.tex").write_text("\n".join(L) + "\n")

    # ---- index of named results
    entries = []
    for num in order:
        for ch in data[num]["chapters"]:
            for r in ch["results"]:
                if r["kind"] not in ("exercise", "example") and r.get("name"):
                    entries.append((sortkey(r["name"]), r["name"], num, KN[r["kind"]], r["num"]))
    entries.sort(key=lambda e: (e[0], [o for o in order].index(e[2]), [int(x) for x in e[4].split(".")]))
    L = [r"% Generated by generate.py: do not edit.", r"\begin{nameindex}"]
    letter = None
    for key, name, num, kind, n in entries:
        first = key[:1].upper() if key[:1].isalpha() else "Symbols and numbers"
        if first != letter:
            letter = first; L.append(r"\indexletter{%s}" % letter)
        L.append(r"\item %s \dotfill\ %s~%s, %s" % (name, kind, n, "Tome~" + num))
    L.append(r"\end{nameindex}")
    (HERE / "chapters/gen-index.tex").write_text("\n".join(L) + "\n")

    for src in sorted((HERE / "src").glob("*.tex")):
        text = src.read_text()
        text = re.sub(r"\\input\{chapters/(gen-[^}]*)\}", lambda m: (HERE / "chapters" / (m.group(1) + ".tex")).read_text(), text)
        (HERE / "chapters" / src.name).write_text("% Generated by generate.py from src/" + src.name + ": edit the source, not this file.\n" + text)

    stats = {"tomes": len(order), "chapters": sum(len(data[n]["chapters"]) for n in order),
             "named": len(entries), "results": sum(1 for n in order for ch in data[n]["chapters"] for r in ch["results"] if r["kind"] != "exercise"),
             "exercises": sum(1 for n in order for ch in data[n]["chapters"] for r in ch["results"] if r["kind"] == "exercise"),
             "citations": sum(1 for c in cites if c["status"] == "ok")}
    (HERE / "chapters/gen-stats.tex").write_text("%% Generated by generate.py\n" + "".join(
        r"\newcommand{\stat%s}{%s}" % (k.capitalize(), "{:,}".format(v).replace(",", r"\,")) + "\n" for k, v in stats.items()))
    print("S4 generate:", stats)
    if problems:
        print("cross-tome references that do not resolve (%d):" % len(problems))
        for c in problems:
            if c["status"] != "unwritten":
                print("  Tome %s ch%d -> Tome %s %s %s: %s" % (c["from"], c["chapter"], c["to"], c["word"], c["num"], c["status"]))


if __name__ == "__main__":
    main()
