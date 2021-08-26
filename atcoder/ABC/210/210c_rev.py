# 間違いのコード

N, K = map(int,input().split())
A = list(map(int,input().split()))

table = set()
R =[0] * N

for i in range(N):
    table.add(A[i])
    R[i] = len(table)

ans = -1
# 累積和でいけない
for j in range(N - K +1):
    ans = max(ans, R[j + K - 1] - R[j] + 1)

print(ans)