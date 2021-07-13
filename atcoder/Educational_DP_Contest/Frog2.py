N,k = map(int,input().split())
h = list(map(int,input().split()))

# DP 配列を用意
# dp[i] には i 番目の足場にたどり着くために必要な最低コストを入れる
dp = [0] * N

dp[0] = 0

for i in range(1,N):
    tmp=[]
    #max(0,i-k)が一番の工夫ポイント
    #貰うDP
    #完成
    for m in range(max(0,i-k),i):
        tmp.append(dp[m] + abs(h[m] - h[i]))

    dp[i] =min(tmp)

print(dp[-1])