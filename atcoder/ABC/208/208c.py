#np.argsortのかんち

import numpy as np
N, K = map(int,input().split())
a = list(map(int,input().split()))

index = np.array(a)
index = np.argsort(index)
# index = sorted(index)
#
ans = [0] * N

dis = K // N
rest = K % N

for i in range(N):
    ans[i] += dis

for j in range(rest):
    ans[index[j]] += 1

for k in ans:
    print(k)