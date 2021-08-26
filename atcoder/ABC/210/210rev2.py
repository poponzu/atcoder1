N, K = map(int, input().split())
c = list(map(int, input().split()))

kinds = 0
ans = 0

cnt = [0] * (10 ** 9)

# 最初のK個の情報で初期化
for i in range(K):
    if cnt[c[i]] == 0:
        kinds += 1
    cnt[c[i]] += 1

ans = max(ans, kinds)

for i in range(K, N):
    # でていく部分について
    if cnt[c[i - K]] == 1:
        kinds -= 1
    cnt[i - K] -= 1
    # 新しく入ってくる部分について
    if cnt[c[i]] == 0:
        kinds += 1
    cnt[c[i]] += 1

    ans = max(ans, kinds)

print(ans)
