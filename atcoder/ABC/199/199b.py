N =int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for x  in  range(1,1001):
    count=0
    for i in range(N):
        if not A[i]<=x<=B[i]:
            break
        count +=1
    if count==N:
        ans+=1

print(ans)
