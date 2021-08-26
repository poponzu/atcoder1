# 11分AC
# ただの全探索

N = int(input())
S = []
P = []
for _ in range(N):
    s, p = map(str, input().split())
    S.append(s)
    P.append(int(p))

# 過半数を表す変数を何にすべきか迷った。

sum_ = sum(P)
major = sum_ // 2 + 1
# flg = False
ans ="atcoder"
for i in range(N):
    if P[i] >= major:
        ans = S[i]

print(ans)