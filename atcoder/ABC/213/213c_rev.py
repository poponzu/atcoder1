h, w, n = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# このリスト内包表記の外側のカッコは{}！間違えた
Xdict = {x: i + 1 for i, x in enumerate(sorted(list(set(A))))}
Ydict = {x: i + 1 for i, x in enumerate(sorted(list(set(B))))}

for i in range(n):
    print(Xdict[A[i]], Ydict[B[i]])
