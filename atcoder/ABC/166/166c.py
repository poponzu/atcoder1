N,M = map(int,input().split())
H = list(map(int,input().split()))
A=[]
B=[]
for i in range(M):
    a,b= map(int, input().split())
    A.append(a-1)
    B.append(b-1)

cross =[-1]*N

#print(cross)

for i in range(M):
    cross[A[i]] = max(cross[A[i]],H[B[i]])
    cross[B[i]] = max(cross[B[i]],H[A[i]])

#print(cross)

count = 0

for i in range(N):
    if H[i] > cross[i]:
        count += 1

print(count)


