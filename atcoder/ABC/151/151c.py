N,M = map(int,input().split())

q = [False] * N
pena = [0] * N
ans = 0
for _ in range(M):
    p,s = map(str,input().split())
    p = int(p)
    #各問題ごとのペナルティを計測
    if q[p-1] == False:
        if s == "WA":
            pena[p-1] += 1
        else:
            q[p-1] = True
    else:
        continue

for i in range(N):
    if q[i] == True:
     ans += pena[i]

#正答数、ペナルティの順で出力
print(sum(q),ans)