#14分AC
#もっと時間短縮できた

#A_max と A_second をあらかじめ求めておくという方針をはっきり言葉にしたかった
import numpy as np

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

A = np.array(A)
index = np.argmax(A)

sort_A = sorted(A,reverse = True)

for i in range(N):
    if i != index:
        print(A[index])
    else:
        print(sort_A[1])


