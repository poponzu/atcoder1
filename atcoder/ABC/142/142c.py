import numpy as np

N = int(input())
A = list(map(int,input().split()))
A = np.array(A)

# # ans = sorted(A)
#
# s = []
#
# for i in range(1,N+1):
#     print(A.index(i))
#
# print(*s)

S = A.argsort()
ans = []

for i in S:
    ans.append(i+1)

print(*ans)

