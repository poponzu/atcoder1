# 入力
N,S = map(str,input().split())
N = int(N)

ans = 0
# 文字列指定区間の左端がstart
for start in range(N):
    ATcnt = 0
    GCcnt = 0
    # 左端のstartから調べて行く
    for check in range(start,N):
        if S[check] == "A":
            ATcnt += 1
        elif S[check] == "T":
            ATcnt -= 1
        elif S[check] == "G":
            GCcnt += 1
        elif S[check] == "C":
            GCcnt -= 1

        if ATcnt == 0 and GCcnt == 0:
            ans += 1
print(ans)