# https://atcoder.jp/contests/yahoo-procon2018-final-open/submissions/18097796に付け加えて解いた
# 問題はこれ"https://atcoder.jp/contests/yahoo-procon2018-final-open/tasks/yahoo_procon2018_final_a?lang=ja"

import sys
from itertools import combinations as combi

input = sys.stdin.readline
N, M = map(int, input().split())
# a = [int(input()) for _ in range(N)]
a = list(map(int, input().split()))
mx = max(M, max(a))
table = [0] * (mx + 1)
for x in a:
    y = 1
    ymx = 1
    while y * y <= x:
        if x % y == 0:
            table[y] += 1
            if (x // y) ** 2 > x: table[x // y] += 1
            ymx = y
        y += 1

ps = [1] * (M + 1)
ps[0] = ps[1] = 0
p = 2
while p * p <= M:
    if ps[p]:
        for q in range(p * p, M + 1, p): ps[q] = 0
    p += 1
# print(table)
# print(N)
ans = [1]
for x in range(2, M + 1):
    res = 0
    y = 1
    t = []
    while y * y <= x:
        if x % y == 0:
            if ps[y]: t.append(y)
            if (x // y) ** 2 > x and ps[x // y]: t.append(x // y)
        y += 1
    for c in range(1, len(t) + 1):
        for com in combi(t, c):
            tt = 1
            for z in com: tt *= z
            if c % 2:
                res += table[tt]
            else:
                res -= table[tt]
    # print(N - res)
    if N - res == N:
        ans.append(x)

print(len(ans))
for i in ans:
    print(i)