N, Q = map(int, input().split())

par = [i for i in range(N + 1)]


# 親を見つける
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# 同じグループかどうか判断
def same(x, y):
    return find(x) == find(y)


# それぞれの親を確認して異なる場合のみ親を統一する。
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


for i in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        unite(a, b)
    else:
        if same(a, b):
            print("Yes")
        else:
            print("No")
