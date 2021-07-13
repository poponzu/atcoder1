N,k = map(int,input().split())
h = list(map(int,input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

dp[0] = 0

#貰うDP
for i in range(1,N):
    tmp=[]
    # 配るDP
    for m in range(min(N-1,i+k),i,-1):
        tmp.append(dp[m] + abs(h[m] - h[i]))
    dp[i+1] = min(tmp)

print(dp[-1])