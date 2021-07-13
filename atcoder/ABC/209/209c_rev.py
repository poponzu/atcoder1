N = int(input())
C = list(map(int, input().split()))
mod = 10 ** 9 + 7

ans = 1
C = sorted(C)

for i in range(N):
    ans *= (C[i] - i) % mod
    ans %= mod

print(ans)
