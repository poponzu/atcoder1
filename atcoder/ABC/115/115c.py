# 23分AC
# MinをL, MaxをRとして名付けるのがよかったかも
# Hminを固定したら、Hmaxも定まるのに気づけたのがよかった
# for文のループ回数 N - K + 1回に自分でケース作って確かめれたのもgood

N, K = map(int, input().split())
H = []
for _ in range(N):
    h = int(input())
    H.append(h)

H.sort()

ans = 10 ** 10
for i in range(N - K + 1):
    Min = H[i]
    Max = H[i + (K - 1)]
    diff = Max - Min
    ans = min(diff, ans)

print(ans)
