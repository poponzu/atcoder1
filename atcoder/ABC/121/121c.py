import numpy as np

N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A = np.array(A)
index = np.argsort(A)
cnt = 0
price = 0

goal = M

for i in range(N):
    # この行に対して買うドリンクの数をcountで把握
    count = min(B[index[i]], goal)
    price += A[index[i]] * count
    goal -= count

    if goal == 0:
        break

print(price)
