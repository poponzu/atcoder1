N = int(input())
A = list(map(int, input().split()))
# ソートして絶対値を外す工夫がすごい
A.sort()

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] += S[i] + A[i]

ans = 0
for i in range(N):
    ans += (S[-1] - S[i+1]) - (A[i] * (N - (i + 1)))

print(ans)