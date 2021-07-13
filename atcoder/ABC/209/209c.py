N = int(input())
C = list(map(int,input().split()))
mod = 10**9 + 7

for i in range(N):
    if C[i] < i+1:
        print(0)
        exit()

ans = 1
for i in range(N-1):
    if C[i] > C[i+1]:
        big = C[i+1] * (C[i+1] - i)
        small = (C[i] - C[i-1]) * C[i+1]
        ans *= (big + small) % mod
        ans %= mod
    else:
        ans *= (C[i] * (C[i+1]-(i+1))) % mod
        ans %= mod

print(ans%mod)