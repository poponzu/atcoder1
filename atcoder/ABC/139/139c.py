#AC10分くらい

N=int(input())
A=list(map(int,input().split()))

current = 0
count = 0
ans = -1
for i in range(N-1):
    if A[i] >= A[i+1]:
        count += 1
    else:
        ans = max(count,ans)
        count = 0
ans = max(count,ans)
print(ans)