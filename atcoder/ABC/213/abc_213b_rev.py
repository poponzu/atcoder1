N=int(input())
A=list(map(int,input().split()))
v=[]

for i in range(N):
    v.append((A[i],i+1))

# タプルの第一要素でソート
v.sort(key=lambda x: x[0])
v.reverse()
print(v[1][1])
