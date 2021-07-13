N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
left = 0
right = 0

#素直に貪欲法
for i in range(N):
    left = min(A[i],B[i])
    ans += left
    A[i] -= left
    B[i] -= left

    right = min(A[i+1],B[i])
    ans += right
    A[i+1] -= right
    B[i] -= right

print(ans)