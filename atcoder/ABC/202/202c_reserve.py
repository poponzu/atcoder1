from collections import Counter

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

BC = []

for i in range(N):
    BC.append(B[C[i]-1])

A = Counter(A)
BC = Counter(BC)

ans = 0

for k,v in A.items():
    if k in BC:
        ans += v * BC[k]

print(ans)