n=int(input())
A=list(map(int,input().split()))

ans = set(A)
ans = list(ans)

if len(ans)==n:
    print("Yes")
else:
    print("No")