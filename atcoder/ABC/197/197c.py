N = int(input())
A = list(map(int, input().split()))
ans = 10 ** 30

# 28行目の配列外参照を防ぐために必要
# ではなく、最後の区切り棒いれる処理をjのループから外す。

if N == 1:
    print(A[0])
    exit()

for i in range(2 ** (N - 1)):
    bit = [False] * (N - 1)

    for j in range(N - 1):
        # 各要素がTrue or False の長さN-1のリスト"bit"を作成する
        # bit[i]がTrueならA[i]とA[i+1]の間に区切りがあることにする
        if (i >> j) & 1:
            bit[j] = True

    # 一番最後で終わるため区切り棒を追加しておく
    bit = bit + [True]

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
