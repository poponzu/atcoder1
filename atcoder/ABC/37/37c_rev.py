# 累積和の方法

N, K =map(int,input().split())
A = list(map(int,input().split()))

S =[0]

for i in range(N):
    S.append(S[i] + A[i])

# print(S)
ans = 0
for i in range(N - K + 1):
    ans += S[i+K]-S[i]

print(ans)