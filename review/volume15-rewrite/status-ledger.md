# Volume 15 status ledger (mirror of Chapter 14, Section "The ledger")

For each statistic: the model, and whether the agreement is proved in the series (P), quoted with a source (Q), conditional (C, hypothesis named) or conjectural (J).

| # | Statistic | Model | Status |
|---|---|---|---|
| 1 | prime factors ω(n) | independent events p∣n | P (Kubilius, Erdős–Wintner, Erdős–Kac, Selberg–Delange) |
| 2 | survivors of a sieve | same events, p<z | P for small z (Brun); failure at z=x^{1/u} P (model 12% too large at u=2) |
| 3 | primes in long intervals | Cramér's coins | P (PNT, Vol 6 Thm 5.5); √-error = RH (C) |
| 4 | primes in short intervals | Cramér's coins | failure P (Maier); Poisson law C (Hardy–Littlewood, Gallagher) |
| 5 | primes in progressions | fair split | P on average (Siegel–Walfisz Vol 14 Cor 2.12, BV Vol 14 Thm 4.7); bias C (GRH, LI) |
| 6 | gaps | Cramér, Granville | small gaps P: 4580 (Vol 14 Thm 9.8); 600, 246 Q; Erdős–Rankin P; Cramér/Granville J |
| 7 | values of μ | random multiplicative f | model P (Wintner); Chowla J |
| 8 | class groups | Cohen–Lenstra | measure and moments P; match J |
| 9 | ranks, Selmer groups | random alternating matrix | law P; Bhargava–Shankar Q; Poonen–Rains J |
| 10 | pairs of zeros | sine kernel | form factor P for |α|<1 under RH (C); full GUE J |
| 11 | moments of ζ | Euler product × CUE | k=1 P; k=2 Q (Ingham); lower bounds P; k≥3 J |
| 12 | values of ζ | random Euler product / Gaussian | Bohr–Jessen P, Selberg P; FHK J |
| 13 | 3-term progressions | random set with local factors | U² count P; primes (Green–Tao) Q |
| 14 | prime race | fair coin | δ(4;3,1)=0.99593 C (GRH, LI); Littlewood Q |

Numbers checked by `check_ch14_meeting.py`.
