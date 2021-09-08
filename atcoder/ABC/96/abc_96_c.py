# 22分AC

H,W = map(int,input().split())
s = [input() for _ in range(H)]

# 四方向への移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# square1001君が目標を達成することができるか
can_paint = True

# 各マス目の"#"だけを全探索
for i in range(H):
    for j in range(W):
        # "."のマスはスルー
        if s[i][j] == ".":
            continue

        around_sharp = False # 着目しているマス目の上下左右のうちそれかに"#"があるかどうか表すaround_sharp
                             # around_sharp = Trueであることは、そのマスは誰かと一緒に黒色に塗られることができる
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]

            if (nx < 0 or nx >= H) or (ny < 0 or ny >= W): # 場外アウトしたり、移動先が壁の場合はスルー
                continue

            if s[nx][ny] == "#": # 着目しているマス目の上下左右のうちそれかに"#"があるかどうか
                around_sharp = True

        if around_sharp == False: # 一つでもaround_sharp = Falseがあればそのマスは孤立していて黒色を塗ろうとしたら白色にしておきたいマスを黒色にしてしまうから
            can_paint = False    # square1001君は目標を達成することができなくなる

if can_paint:
    print("Yes")
else:
    print("No")
