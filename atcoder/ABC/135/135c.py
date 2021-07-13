#25分くらいAC
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

count = 0

for i in range(0, N):
    sum = A[i] + A[i+1]
    eat = min(sum, B[i])
    A[i+1] = A[i+1] - (max(eat - A[i],0))
    count += eat

print(count)