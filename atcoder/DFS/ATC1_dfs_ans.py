import sys
sys.setrecursionlimit(10 ** 7)  # 再帰関数の呼び出し制限

# 四方向への移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(h, w):
    seen[h][w] = True

    # 上下左右の四方向を探索
    for dir in range(0,4):
        nh = h + dx[dir]
        nw = w + dy[dir]

        # 場外アウトしたり、移動先が壁の場合はスルー
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if field[nh][nw] == "#":
            continue
        # 移動先が探索済みの場合もスルー
        if seen[nh][nw]:
            continue

        # 再帰的に探索
        dfs(nh,nw)

# 入力受け取り
H,W = map(int, input().split())
field = [list(input()) for _ in range(H)]

# sとgのマスを特定する
sh = 0
sw = 0
gh = 0
gw = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == "s":
            sh = i
            sw = j
        if field[i][j] == "g":
            gh = i
            gw = j

seen = [[False] * 510 for _ in range(510)]# seen[h][w] := マス (h, w) が検知済みかどうか
# 探索開始
dfs(sh,sw)

if seen[gh][gw]:
    print("Yes")
else:
    print("No")





