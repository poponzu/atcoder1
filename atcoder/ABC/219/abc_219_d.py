# 14:01開始

# 入力
N = int(input())
X, Y = map(int,input().split())
A = []
B = []
T = []
for _ in range(N):
    a, b = map(int,input().split())
    # タプルで管理するT
    T.append((a,b))
    A.append(a)
    B.append(b)

sumA = sum(A)
sumB = sum(B)

# 高橋君が X 個以上のたこ焼きと Y 個以上のたい焼きを手に入れることが不可能な場合
if sumA < X or sumB < Y:
    print("-1")
    exit()

# たこ焼きの個数でソート
T.sort()

