n, k = map(int, input().split())

C = list(map(int, input().split()))

color = {}

# キャンディの色をすべて辞書にキーとして登録する
for i in range(n):
    color.setdefault(C[i], 0)

# kindsをある区間においてK個のアメをもらうときの色の種類数とする
kinds = 0

for i in range(k):
    # color[C[i]]が0からインクリメントされているなら種類数が1つ増えたことになるのでkindsを1つ増やす
    if color[C[i]] == 0:
        kinds += 1
    color[C[i]] += 1

ans = kinds

for i in range(n - k):
    # 出ていく部分について
    if color[C[i]] == 1:
        kinds -= 1
    color[C[i]] -= 1
    # 新しく入ってくる部分について
    if color[C[i + k]] == 0:
        kinds += 1
    color[C[i + k]] += 1
    ans = max(ans, kinds)

print(ans)
