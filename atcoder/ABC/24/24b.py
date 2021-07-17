# N, T = map(int,input().split())
# A = []
# for _ in range(N):
#     a = int(input())
#     A.append(a)
#
# ans = 0
# for i in range(N-1):
#     if A[i] + T < A[i+1]:
#         ans += T
#     else:
#         ans += A[i+1] - A[i]
#
# ans += T
#
# print(ans)

N,M = [int(x) for x in input().split()]
ts = [int(input()) for _ in range(N)]
rts  = ts[::-1]
ans = M
for i in range(N-1):
    ans += min(M, rts[i]-rts[i+1])
print(ans)