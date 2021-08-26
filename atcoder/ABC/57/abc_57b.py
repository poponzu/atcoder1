# 11分AC
# B問題おなじみの全探索
# enumerate関数は二次元リストには使えない？

N, M = map(int,input().split())
A = []
B = []
C = []
D = []

for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

for _ in range(M):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

# 各学生についてのfor
for i in range(N):
    near = 10 ** 17
    # 最小距離とindexのリストを保持する
    list = [10 ** 17, 0]
    # 各チェックポイントについてのfor
    for j in range(M):
        d = abs(A[i] - C[j]) + abs(B[i] - D[j])
        if d < list[0]:
            list[0] = d
            list[1] = j
    # 答えが1-indexed形式やから+1
    print(list[1]+1)
