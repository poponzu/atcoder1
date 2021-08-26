# 13分AC

from collections import Counter

N = int(input())
s = []
for _ in range(N):
    s.append(input())
M = int(input())
t = []
for _ in range(M):
    t.append(input())

ds = Counter(s)
dt = Counter(t)

ans = -1000

# ans が０より小さかったら最後にansを0に変更する
for k1, v1 in ds.items():
    if k1 in dt.keys():
        ans = max(ans, v1 - dt[k1])
    else:
        ans = max(ans, ds[k1])


if ans < 0:
    ans = 0

print(ans)
