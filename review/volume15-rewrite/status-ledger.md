# Volume 15 status ledger (mirror of Chapter 14, Section "The ledger")

For each statistic: the model, and whether the agreement is proved in the series (P), quoted with a source (Q), conditional (C, hypothesis named) or conjectural (J).

| # | Statistic | Model | Status |
|---|---|---|---|
| 1 | prime factors ω(n) | independent events p∣n | P for Kubilius, Erdős–Wintner, and Erdős–Kac. Selberg–Delange proves the correction from the cutoff at n≤x. The polylogarithmic short-interval question in the project is open. |
| 2 | survivors of a sieve | same events for p<z | P in the small-z range by Brun. For fixed u at z=x^(1/u), the limiting ratio is e^γω(u), so at u=2 the model is about 12% too large. |
| 3 | bulk prime count | Cramér's independent coins | Same leading term P by the prime number theorem and the almost-sure model count (Vol 6 Thms 5.5, 10.2). RH gives the prime-count error O(√x log x). The smaller model bound would imply RH. |
| 4 | primes in short intervals | Cramér's coins | Maier's failure P and unconditional. Gallagher's Poisson law at lengths asymptotic to c log X is C under HL*. The second-order pair average is C under RH and HL₂. |
| 5 | primes in progressions | fair split among reduced classes | P for small moduli by Siegel–Walfisz, on average up to √x/(log x)^B by Bombieri–Vinogradov, and for the stated large modulus with Gallagher's exceptional term. Bias C under GRH and LI. |
| 6 | gaps | Cramér, Granville | Infinitely many gaps at most 4580 P (Vol 14 Thm 9.8). The bounds 600 and 246 are Q. Erdős–Rankin lower bound P. The model scale, Granville's refinement, and twin primes are J. |
| 7 | values of μ | random squarefree multiplicative f | Almost-sure Wintner bound and model correlations P. For μ, cancellation o(x) is P and O(x^(1/2+ε)) for every ε>0 is equivalent to RH. Chowla and Sarnak are J. |
| 8 | class groups | Cohen–Lenstra | The measure and its moments are P. Davenport–Heilbronn on average 3-torsion is Q. The distributional match for odd-primary parts of imaginary quadratic class groups is J. |
| 9 | ranks and Selmer groups | random alternating matrix | The model law and its moments are P. The Selmer-size averages of Bhargava–Shankar for n=2,3,4,5 are Q. The arithmetic Poonen–Rains, Goldfeld, and minimalist predictions are J. |
| 10 | pairs of zeros | sine kernel | P for Fourier support in (−1,1) under RH, hence C for the agreement with zeros. The remaining pair correlation is J. |
| 11 | moments of ζ | Euler product × CUE | The second moment is P and the fourth is Q (Ingham). Lower bounds P for integer k≥1. The Keating–Snaith asymptotic for integer k≥3 is J. |
| 12 | values of ζ | random Euler product and normalised Gaussian | Bohr–Jessen for 1/2<σ<1 and Selberg on the line are P. Tightness of the centred typical short-interval maximum is Q (Vol 12 Ch 11). [Upper bound](https://arxiv.org/abs/2007.00988) · [Lower bound](https://arxiv.org/abs/2307.00982) |
| 13 | three-term progressions | random set with local factors | The U² count is P on the stated cyclic groups. The prime count with local factors and Green–Tao are Q. |
| 14 | prime race | fair split between two classes | Littlewood's sign changes are Q. The logarithmic density δ(4,3,1)≈0.99593 is C under GRH and LI. |

Numbers checked by `check_ch14_meeting.py`.
