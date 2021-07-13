#DP問題の解き方のコツは，状態と遷移をしっかりと定義すること！！！
N = int(input())
dp = [[0]*3 for _ in range(N+1)]

#初期条件
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1,N+1):
    a,b,c =map(int,input().split())
    #i 日目に行動 A、B、C をして i 日目までに得られる最大幸福度をそれぞれ dp[i][0]、dp[i][1]、dp[i][2]とする。

    dp[i][0] = max(dp[i-1][1] + a,dp[i-1][2] + a)
    dp[i][1] = max(dp[i-1][0] + b,dp[i-1][2] + b)
    dp[i][2] = max(dp[i-1][0] + c,dp[i-1][1] + c)

print(max(dp[-1]))