# 22:13 ~ 22:32

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