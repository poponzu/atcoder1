N=int(input())
A=list(map(int,input().split()))

Max = -1

for l in range(N):
    #ここでA[l]をxに代入するのすごい
    x=A[l]
    for r in range(l,N):
        #x = min(A[l:r+1])
        x = min (x,A[r])
        sum = x * (r - l + 1)
        Max = max(Max,sum)

print(Max)
