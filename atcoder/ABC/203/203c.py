N,K = map(int,input().split())
F = [list(map(int, input().split())) for i in range(N)]
# village =[0]*(10**18)
# A=[]

for _ in range(N):
    a,b =map(int,input().split())
    friend =

A=sorted(A)

current = 0

for a in A:
    if K > a:
        current = a
        K = K - a + village[a]
    elif K >= a:
        ans = current + K
        print(ans)
