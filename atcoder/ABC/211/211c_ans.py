s = input()
n = len(s)

# len(s)行９列のdpテーブル
dp = [[0] * 9 for _ in range(n+1)]

# print(dp)
# print(len(dp))

# j = 0の部分を初期化
for i in range(n+1):
    dp[i][0] = 1

mod = 10**9 + 7

t = "chokudai"

for i in range(n):
    for j in range(8):
        if s[i] != t[j]:
            dp[i+1][j+1] = dp[i][j+1]
        else:
            dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod

print(dp[n][8])

