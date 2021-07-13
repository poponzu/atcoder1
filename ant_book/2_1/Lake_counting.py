N, M = 10, 12
field = [['W', '.', '.',  '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
         ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
         ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
         ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']]

def dfs(x, y):
    # 今いるところを、に置き換える
    field[x][y] = '.'

    # 移動する8方向をループ
    for dx in range(-1,2):
        for dy in range(-1,2):
            # x方向にdx y方向にdy 移動した場所を (nx, ny) とする
            nx = x + dx
            ny = y + dy

            # まずnx と ny が庭の範囲内かどうかを判定 (ここはC++とは違う書き方をしなければならない)
            if 0 <= nx and nx <= N-1 and 0 <= ny and ny <= M-1:
                # field[nx][ny] が水溜まりかどうかを判定
                if field[nx][ny] == 'W':
                    dfs(nx, ny)

def solve():
    res = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 'W':
                # W が残っているならそこから dfs を始める
                dfs(i, j)
                res += 1

    print(res)

solve()