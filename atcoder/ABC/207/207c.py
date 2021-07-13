N = int(input())
T = []
L = []
R = []

for _ in range(N):
    t,l,r = map(int,input().split())
    T.append(t)
    L.append(l)
    R.append(r)

count = 0
for i in range(N-1):
    for j in range(i+1,N):
        if L[i] <= L[j]:
            if R[i] <= R[j]:
                count += 1
        if L[i] > L[j]:
            if R[i] > R[j]:
                count += 1

print(count)