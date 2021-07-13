N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

#定義してないリストを参照するとエラーがでるからダミー置いといた。
A.append(100)
C.append(0)

total = 0

for i in range(0,N):
    if(A[i + 1] - A[i] == 1):
        total += C[A[i] - 1]
    total += B[A[i] - 1]

print(total)