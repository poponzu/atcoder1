N,D,H=map(int,input().split())

B = [list(map(int, input().split())) for i in range(N)]
#print(B)
Max=-float("inf")

for i in range(N):
    a=B[i][1]- H
    b=D-B[i][0]
    c=H*B[i][0]-D*B[i][1]
    #ax+bx+c=0のa,b,cが求まる
    y=-c/b
    Max=max(Max,y)

print(max(0,Max))
