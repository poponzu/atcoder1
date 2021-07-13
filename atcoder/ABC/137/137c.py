from operator import mul
from functools import reduce

N = int(input())
A = []
for _ in range(N):
    A.append(input())

pattern = [0]*1500

for a in A:
    sum = 0
    for i in a:
        sum += ord(i)
    pattern[sum] += 1

def cmb1(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

ans = 0
for n in pattern:
    if n == 0 or n == 1:
        continue
    ans += cmb1(n,2)

print(ans)