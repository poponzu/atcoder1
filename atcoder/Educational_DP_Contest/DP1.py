N,K = map(int,input().split())
h = list(map(int,input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2,N):
    dp[i]=float("INF")
    for k in range(i):
        dp[i] = min(dp[i-k] + abs(h[i-k] - h[k]),dp[i])

print(dp[-1])