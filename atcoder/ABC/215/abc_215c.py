import math
import itertools
S, K = map(str,input().split())

K = int(K)

lst = [''.join(p) for p in itertools.permutations(S)]

lst =list(set(lst))
lst.sort()

print(lst[K - 1])
