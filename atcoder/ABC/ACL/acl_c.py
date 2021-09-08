# 参考"https://qiita.com/white1107/items/52fd4149bb1846862e38"
# https://drken1215.hatenablog.com/entry/2020/09/27/080100
N, M = map(int,input().split())

par = [i for i in range(N + 1)]


# 親を見つける
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# 同じグループかどうか判断
# 親が同じかどうか見るだけ
def same(x, y):
    return find(x) == find(y)


# それぞれの親を確認して異なる場合のみ親を統一する。
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

# M回の入力に対してunite関数でUnion Find集合を作る
for _ in range(M):
    a,b = map(int,input().split())
    unite(a,b)

# Union-Find 中の要素 v が根かどうかはpar[v] = vという処理でわかる
res = 0
for i in range(1,N+1):
    if par[i] == i:
        res += 1

print(res - 1)