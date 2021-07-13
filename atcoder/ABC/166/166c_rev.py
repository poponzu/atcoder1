N,M = map(int,input().split())
H = list(map(int,input().split()))
A=[]
B=[]
for i in range(M):
    a,b= map(int, input().split())
    A.append(a-1)
    B.append(b-1)

cross = [[] for _ in range(N)]

for i in range(M):
    #A[i]に関してリスト作成
    cross[A[i]].append(B[i])
    # B[i]に関してリスト作成
    cross[B[i]].append(A[i])

print(cross)