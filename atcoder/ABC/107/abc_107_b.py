# 40分くらいかかってしまった
# 入力形式に手間取り
# np.deleteにもすこし時間がかかった

import numpy as np

H, W = map(int, input().split())
a = []
for _ in range(H):
    a.append(list(input()))

a = np.array(a)

column = [False] * H
row = [False] * W

# 行に対してのcheck
for h in range(H):
    if all([i == "." for i in a[h]]):
        column[h] = True

# 列に対してのcheck
for w in range(W):
    list = []
    for j in range(H):
        list.append(a[j][w])
    if all([k == "." for k in list]):
        row[w] = True

c = []
r = []

for i,x in enumerate(column):
    if x:
        c.append(i)

for j,y in enumerate(row):
    if y:
        r.append(j)

# print(c)
# print(r)

# 行を削除
a = np.delete(a,c,0)
# 列を削除
a = np.delete(a,r,1)

for i in range(H - sum(column)):
    for j in range(W - sum(row)):
        print(a[i][j], end ="")
    print("")

