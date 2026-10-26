"""Draw the EAN-13 barcode of an ISBN-13 as TikZ code, for the back of the paperback cover.

Usage: python3 tools/ean13.py <isbn> <output .tex>
The drawing fills a white box 2.05in x 1.25in (KDP's barcode area is 2in x 1.2in), lower-left
corner at the origin: "ISBN ..." on top, the bars at 100% size (0.33mm modules, 22.85mm high
guard bars), and the human-readable digits below.
"""
import sys

L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
PARITY = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]


def check_digit(first12: str) -> int:
    return (10 - sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(first12)) % 10) % 10


def modules(isbn: str) -> str:
    d = [int(c) for c in isbn]
    left = "".join((L if p == "L" else G)[x] for p, x in zip(PARITY[d[0]], d[1:7]))
    right = "".join(R[x] for x in d[7:])
    return "101" + left + "01010" + right + "101"


def main(isbn: str, out: str) -> None:
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 13 or not isbn.isdigit() or check_digit(isbn[:12]) != int(isbn[12]):
        sys.exit(f"not a valid ISBN-13: {isbn}")
    m = modules(isbn)
    x0 = (2.05 - 95 * 0.013) / 2         # bars centred in the box, module 0.013in = 0.33mm
    guards = {i for i in range(95) if i < 3 or 45 <= i < 50 or i >= 92}
    lines = [f"% EAN-13 barcode of ISBN {isbn} (tools/ean13.py)"]
    i = 0
    while i < 95:                        # one rectangle per run of black modules
        if m[i] == "1":
            j = i
            while j < 95 and m[j] == "1":
                j += 1
            bottom = 0.18 if i in guards else 0.24
            lines.append(r"\fill[black] (%.4fin,%.3fin) rectangle (%.4fin,1.08in);"
                         % (x0 + 0.013 * i, bottom, x0 + 0.013 * j))
            i = j
        else:
            i += 1
    font = r"font=\fontfamily{qhv}\selectfont\fontsize{8}{9}\selectfont"
    lines.append(r"\node[black,%s] at (1.025in,1.16in) {ISBN %s-%s};" % (font, isbn[:3], isbn[3:]))
    lines.append(r"\node[black,%s,anchor=east] at (%.4fin,0.13in) {%s};" % (font, x0 - 0.02, isbn[0]))
    lines.append(r"\node[black,%s] at (%.4fin,0.13in) {%s};" % (font, x0 + 0.013 * 24, isbn[1:7]))
    lines.append(r"\node[black,%s] at (%.4fin,0.13in) {%s};" % (font, x0 + 0.013 * 71, isbn[7:]))
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
