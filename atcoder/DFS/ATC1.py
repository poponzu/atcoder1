#再帰関数ver

import sys

sys.setrecursionlimit(10 ** 7)  # 再帰関数の呼び出し制限

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]

def dfs(x, y):
    # 壁に当たったり、探索範囲外になった場合はreturn
    if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == "#":
        return

    if c[x][y] == "g":
        print("Yes")
        sys.exit()

    c[x][y] = "#"
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j

dfs(sx, sy)
print("No")
