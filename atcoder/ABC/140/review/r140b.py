N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 定義してないリストを参照するとエラーがでるからダミー置いといた。
A.append(100)
C.append(0)

total = 0

total = sum(B)

for i in range(1, N):
    if (A[i] - A[i - 1] == 1):
        total += C[A[i] - 1 - 1]

print(total)

