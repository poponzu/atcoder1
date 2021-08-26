import bisect
H, W, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a - 1)
    B.append(b - 1)

useA = set(sorted(A))
useB = set(sorted(B))

fA = sorted(list(useA))
fB = sorted(list(useB))

for i in range(N):
    print(bisect.bisect_right(fA,A[i]), bisect.bisect_right(fB,B[i]))
