import copy
from itertools import product

H, W, K = map(int, input().split())
# 二次元リスト
c = []
for i in range(H):
    array = input()
    c.append(list(array))

ans = 0
for bit in product((True, False), repeat=H + W):
    d = copy.deepcopy(c)
    # リストbitの前半H個は列についての指示
    for i in range(H):
        if bit[i]:
            # i行目をすべて"r"に変える
            for row in range(W):
                d[i][row] = "r"
        # リストbitの後半W個は列についての指示
    for j in range(W):
        if bit[H + j]:
            # j列目をすべて"r"に変える
            for columns in range(H):
                d[columns][j] = "r"

    # 黒の数チェック
    count = 0
    for k in range(H):
        for l in range(W):
            if d[k][l] == "#":
                count += 1

    if count == K:
        ans += 1

print(ans)
