#16分AC
#logを使えたのがよかった
import math
N, K = map(int,input().split())

ans = 0

for i in range(1, N+1):
    if i < K:
        coin_count = math.ceil(math.log(K/i, 2))
        ans += (1/N) * ((1/2)**coin_count)
    else:
        ans += 1/N

print(ans)