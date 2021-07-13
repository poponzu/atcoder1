N,K = map(int,input().split())
F = [list(map(int, input().split())) for i in range(N)]

F = sorted(F,key=lambda x:x[0])

# print(F)
current = 0

for i in range(N):
    if K >= F[i][0]-current:
        K = K - (F[i][0] - current) + F[i][1]
        current = F[i][0]
    elif K < F[i][0] - current:
        ans = current + K
        print(ans)
        exit()

print(current + K)