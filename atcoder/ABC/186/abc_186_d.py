N = int(input())
A = list(map(int, input().split()))

Sum = sum(A)

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] += S[i] + A[i]

ans = 0
for i in range(N):
    ans += abs(A[i] * (N - (i + 1)) - (Sum - S[i + 1]))

print(ans)
