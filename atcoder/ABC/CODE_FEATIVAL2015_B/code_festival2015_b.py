# 12:16~ 12:23
# 7分AC

from collections import Counter

# 入力
N, M = map(int,input().split())
A = list(map(int,input().split()))

# 各回答の出現回数を保存
dict = Counter(A)

# 過半数基準を作っておく
majority = N // 2 + 1

# 答えの初期値を"?"にしておく
ans = "?"

for k,v in dict.items():
    if v >= majority:
        ans = k
        break

print(ans)



