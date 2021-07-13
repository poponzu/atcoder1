from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def cmb2(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

A,B,K = map(int,input().split())

#K -= 1

N = A + B

ans =""

for i in range(0,N):
    if 0 < A:
        if K <= cmb2(A+B-1,B):
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= cmb2(A+B-1,B)
            B -= 1
    else:
        ans += "b"
        B -= 1

print(ans)