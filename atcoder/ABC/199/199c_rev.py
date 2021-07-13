import sys
input =sys.stdin.readline

N=int(input())
S=list(input())
S.pop()
Q=int(input())

Query=[]
A=[]
B=[]

#ここまでが入力処理
for i in range(Q):
    q,a,b=map(int,input().split())
    Query.append(q)
    A.append(a)
    B.append(b)


for i in range(Q):
    if Query[i]==1:
        S[A[i]-1],S[B[i]-1] = S[B[i]-1],S[A[i]-1]
    else:
        I = S[:N]
        S=S[N:]

        for v in I:
         S.append(v)

print("".join(S))





