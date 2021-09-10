# 14分AC

from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

dict = Counter(A)

kind = len(dict)

# 出現回数(バリュー）でソート
# dict2がタプルに変更されてた
dict2 = sorted(dict.items(), key=lambda x: x[1])
# print(dict2)

# # 先頭kind ー K個みて出現回数数える
for i in range(kind - K):
    cnt += dict2[i][1]

print(cnt)
