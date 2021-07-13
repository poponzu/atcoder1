#4分AC
N, X = map(int,input().split())
A = list(map(int,input().split()))

sum = 0
for i in range(N):
    if i % 2 == 1:
        A[i] -= 1

    sum += A[i]

if X >= sum:
    print("Yes")
else:
    print("No")