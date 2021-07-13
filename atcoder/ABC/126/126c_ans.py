N, K = map(int,input().split())
ans = 0

for i in range(1,N+1):
    p = 1 / N
    now = i
    while(now < K):
        now *= 2
        p /= 2
    ans += p

print(ans)