N=int(input())
A=list(map(int,input().split()))
Copy=A
while(len(A)!=2):
    t=[]
    for i in range(0,len(A),2):
        if A[i]<A[i+1]:
            t.append(A[i+1])
        else:
            t.append(A[i])
    A=t

Min=min(A)
print(Copy.index(Min)+1)