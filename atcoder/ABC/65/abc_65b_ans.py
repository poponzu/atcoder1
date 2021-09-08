# 18分AC

N = int(input())
A  = []
for _ in range(N):
    a = int(input())
    A.append(a)

cur = 0
for i in range(1,10**5 + 10):
    cur = A[cur] - 1
    if A[cur] == 2:
        print(i+1)
        exit()

print(-1)