N,M = map(int,input().split())

A = []
B = []
for _ in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

K = int(input())
C = []
D = []
for _ in range(K):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

ans = 0
for i in range(2 ** K):
    table = [0] * N
    for j in range(K):  # このループが一番のポイント
        if ((i >> j) & 1):
            table[C[j] - 1] += 1
        else:
            table[D[j] - 1] += 1
    count = 0
    for l in range(M):
        if table[A[l] - 1] > 0 and table[B[l] - 1]:
            count +=1
    ans = max(count,ans)

print(ans)



