# 4分AC
# 出現する数字とその出現回数を辞書型で保存して
# 出現回数が奇数回の数字が紙に残っている数字。それを数えて出力する。
from collections import Counter

N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

dictA = Counter(A)

cnt = 0
for k,v in dictA.items():
    if v % 2 == 1:
        cnt += 1

print(cnt)