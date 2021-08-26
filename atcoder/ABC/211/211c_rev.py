S = input()
N = len(S)

dp = [[0] * 9 for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1

mod = 10 ** 9 + 7
T = "chokudai"

for i in range(N):
    for j in range(8):
        if S[i] != T[j]:
            dp[i + 1][j + 1] = dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i][j]) % mod

print(dp[N][8])
