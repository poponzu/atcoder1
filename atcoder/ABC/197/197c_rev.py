N = int(input())
A = list(map(int, input().split()))
ans = 10 ** 30
from itertools import product

for bit in product((True, False), repeat=N - 1):
    # 各要素がTrue or False の長さN-1のタプル"bit"を作成できる
    # bit[i]がTrueならA[i]とA[i+1]の間に区切りがあることにする

    bit = list(bit).append([True])# 一番最後で終わるため区切り棒を追加しておく

    score = 0  # 各区間のXOR
    cur = 0  # 現区間のOR

    # ある区切り棒のパターンに対して一つのXORを計算する
    for i in range(N):
        cur |= A[i]  # ORの計算
        # もし区切り棒があったらscoreを計算して，curを初期化
        if bit[i]:
            score ^= cur
            cur = 0

    ans = min(ans, score)  # 最小値の更新

print(ans)
