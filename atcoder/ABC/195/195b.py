A,B,W=map(int,input().split())
Max=-1
Min=float("inf")
W *=1000

for n in range(10**6):
    n +=1
    if A*n<=W<=B*n:
        Min = min(Min,n)
        Max = max(Max,n)

if Max==-1 and Min==float("inf"):
    print("UNSATISFIABLE")
else:
    print(Min,Max)
