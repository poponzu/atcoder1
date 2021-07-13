from operator import mul
from functools import reduce
from collections import Counter

N = int(input())
A = []
for _ in range(N):
    A.append(input())

#pattern = [0]*1500
pattern = {}
#アナグラムが同じ = ソートしても同じ
#これを辞書型で数えて最後にcmb1で集計して答えを出す
for i in range(N):
    A[i] = "".join(sorted(A[i]))

pattern={}
#一気に+=１はできなかったみたい
#Counterは使えそうにない。
for i in range(N):
    A[i] = Counter(A[i])
    pattern[A[i]]+=1



def cmb1(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

ans = 0
for n in pattern.values():
    if n == 0 or n == 1:
        continue
    ans += cmb1(n,2)

print(ans)