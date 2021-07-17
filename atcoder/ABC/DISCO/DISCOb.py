N = int(input())
A = list(map(int,input().split()))

#累積和
S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

sum = S[-1]

ans = 10**10
for i in range(1,N+1):
    left = S[i]
    right = sum - left
    ans = min (ans ,abs(right - left))

print(ans)

