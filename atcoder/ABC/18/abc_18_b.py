# 21:59~ 22:31
# 32分は時間かけすぎた

# https://qiita.com/tamago324/items/ea39fb541ef9f2cada7fの記事が参考になった

# 入力
S = input()
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# # 部分的に反転させる処理はないのか？
# for i in range(N):
#     print(S[L[i] - 1:R[i]:-1])

S = list(S)

for i in range(N):
    # 反転させるところ抽出
    sample = list(S[L[i]-1:R[i]])
    # 反転
    sample = sample[::-1]


    S[L[i]-1:R[i]] = sample

print("".join(S))

