N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

lft = []
rht = []

for i in range(N):
    lft.append(A[i])

for i in range(1,N):
    lft[i] = max(lft[i],lft[i-1])

for i in range(N):
    rht.append(A[i])

for i in range(N-2,0,-1):
    rht[i] = max(rht[i],rht[i+1])

for i in range(N):
    ans = -1
    #端っこの処理は工夫する必要があるったが
    #このif文が工夫
    if 0 < i:
        ans = max(ans,lft[i-1])
    if i+1 < N:
        ans = max(ans,rht[i+1])
    print(ans)
