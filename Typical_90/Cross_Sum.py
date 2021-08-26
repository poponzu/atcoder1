h, w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(h)]

rows = [0] * h
columns = [0] * w

for i in range(h):
    for j in range(w):
        rows[i] += A[i][j]

for k in range(w):
    for l in range(h):
        columns[k] += A[l][k]

# print(rows)
# print("-------")
# print(columns)
ans = [[0] * w for _ in range(h)]

for m in range(h):
    for n in range(w):
        ans[m][n] = rows[m] + columns[n] - A[m][n]

for a in range(h):
    print(*ans[a])
