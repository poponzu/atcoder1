# n = int(input())
# b = list(map(int, input().split()))
#
# a = [0] * n
# b.append(1000000)
#
# a[0] = b[0]
# for i in range(1, n):
#     a[i] = min(b[i], b[i - 1])
#
# print(sum(a))


N = int(input())
B = list(map(int, input().split()))

A = [0] * N
B.append(100000000)

A[0] = B[0]

for i in range(1, N):
    A[i] = min(B[i], B[i - 1])

print(sum(A))


