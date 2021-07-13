from collections import Counter

N = int(input())
A = list(map(int,input().split()))

par = [i for i in range(max(A)+1)]


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


# それぞれの根を確認して異なる場合のみ親を統一する。
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


for i in range(N//2):
    unite(A[i],A[N-1-i])

#parは常に根を指している訳ではない

root = []
for p in par:
    root.append(find(p))

root = Counter(root)
ans =  0
for v in root.values():
    ans += v -1
print(ans)