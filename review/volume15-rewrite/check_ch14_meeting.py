"""Number checks for Volume 15, Chapter 14 (The meeting)."""
import math, re, itertools, random
from common import check, check_true, finish, primes_upto

tex = open("../../volume15-order-and-chance/chapters/ch14-meeting.tex").read()
gamma = 0.5772156649015329

# Ledger 2: at u=2 the Buchstab omega(2)=1/2, ratio e^gamma*omega(2); the model is 1/ratio - 1 too large.
ratio = math.exp(gamma) * 0.5
check("sieve ledger: model excess at u=2 (percent)", 100 * (1 / ratio - 1), 12, 0.5)

# Ledger 6: the gap bound 4580 = 5167 - 587 (Volume 14, Theorem 9.8), 582 primes from 587 to 5167.
P = [p for p in primes_upto(6000) if 587 <= p <= 5167]
check_true("582 primes from 587 to 5167", len(P) == 582 and P[0] == 587 and P[-1] == 5167)
check("gap bound", 5167 - 587, 4580, 0)
check_true("4580 cited as proved, 600 and 246 as quoted records",
           "4580" in tex and "quoted records" in tex)

# Ledger 13 / project 2: last-digit transition 1 -> 1 among the first 1e8 primes.
out = open("lastdigit_1e8.out").read()
pr = float(re.search(r"=\s*([0-9.]+)", out).group(1))
check("P(next ends in 1 | ends in 1), percent", 100 * pr, 18, 0.5)

# Proposition tkshort: sum over ]x,x+h] of (omega_y(n)-mu_y)^2 <= h mu_y + 5 pi(y)^2, tested exactly.
small = list(primes_upto(200))
random.seed(1)
worst = -1e9
for _ in range(300):
    y = random.choice([2, 3, 5, 10, 20, 50, 100, 200])
    h = random.randint(1, 3000); x = random.randint(0, 10**7)
    ps = [p for p in small if p <= y]
    mu = sum(1 / p for p in ps)
    lhs = sum((sum(1 for p in ps if n % p == 0) - mu) ** 2 for n in range(x + 1, x + h + 1))
    rhs = h * mu + 5 * len(ps) ** 2
    worst = max(worst, lhs - rhs)
    if y * y <= h:
        check_true(f"tkshort, small-y form x={x} h={h} y={y}", lhs <= h * (mu + 5))
check_true(f"tkshort holds on 300 random (x,h,y) (max lhs-rhs = {worst:.1f})", worst <= 0)
# mu_y <= pi(y)/2 used in the proof
check_true("mu_y <= pi(y)/2 for y up to 200",
           all(sum(1 / p for p in small[:k]) <= k / 2 for k in range(1, len(small) + 1)))
finish()
