N, M = map(int,input().split())
A = []
for _ in range(M):
    a = int(input())
    A.append(a)

DP =[10**10] * (N+1)
DP[0] = 1
mod = 10**9 + 7

for a in A:
    DP[a] = 0


if A[0] != 1:
    DP[1] = 1
    for i in range(2, N+1):
        if DP[i] == 0:
            continue
        else:
            DP[i] = (DP[i-2] + DP[i-1]) % mod
else:
    DP[1] = 0
    for i in range(2, N+1):
        if DP[i] == 0:
            continue
        else:
            DP[i] = (DP[i-2] + DP[i-1]) % mod

print(DP[-1])