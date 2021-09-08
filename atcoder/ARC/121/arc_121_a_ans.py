# 参考ページ("https://zenn.dev/m193h/articles/20210530sun001057m193harc121")

N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    # 要素となんばん目の要素かのタプル用意
    X.append((x, i))
    Y.append((y, i))
# 第一要素で昇順ソート
X.sort()
Y.sort()

# 二番目に遠い家同士の距離は以下の3つの組み合わせをX、Yそれぞれで上げて行く
# abs(x_1 - x_N-1), abs(x_2 - x_N), abs(x_2 - x_N-1)
# ソート してるから絶対値を外せる
candidate = []
for xa, ia in X[-2:]:
    for xb, ib in X[:2]:
        candidate.append([xa - xb, (ia, ib)])

for ya, ia in Y[-2:]:
    for yb, ib in Y[:2]:
        candidate.append([ya - yb, (ia, ib)])

# リストの第一要素で降順ソート
candidate.sort(reverse=True)
# 距離が最大になる家の組の距離と組み合わせ
_, max_pair = candidate[0]

# 距離が最大になる家の組とは違う組み合わせの家かつ2番目に距離が最大になる家の組み合わせ
for distance, pair in candidate[1:]:
    if max_pair != pair:
        print(distance)
        break