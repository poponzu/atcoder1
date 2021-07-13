import numpy as np

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]

# print(a,b)
a =np.array(a)
b =np.array(b)

ans =np.dot(a,b)

for answer in ans:
    print(answer)



