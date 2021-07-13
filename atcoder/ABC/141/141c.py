#10分AC

n,k,q = map(int,input().split())
A=[]
for _ in range(q):
    A.append(int(int(input())))

start_score = k - q
p = [start_score] * n

for i in range(q):
    p[A[i] - 1] += 1

for i in range(n):
    if p[i] > 0:
        print("Yes")
    else:
        print("No")