# 22:13 ~ 22:32

# 解説かいてること意味わからん

# 後ろからWcnt個みて、その間に何個”R”があるかを数えてその数を出力する
# 最終的にWは右端にくるから・そこからこれを思いついた
from collections import Counter
# 入力
N = int(input())
c = list(input())

dict = Counter(c)
Rcnt = dict["R"]
Wcnt = dict["W"]

ans = 0

for i in range(-1,-Wcnt-1,-1):
    if c[i] == "R":
        ans += 1

print(ans)