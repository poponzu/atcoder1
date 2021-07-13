A, B, X = map(int, input().split())

#整数ｘを買う時の値段を返す
def check(x):
    price = A * x + B * len(str(x))
    return price

ok = 0
ng = 10**9 + 1
#二分探索で境界を探す

#一般には、正の整数 N に対して単調増加な式 f(N) があるとき、
# f(N)≤X を満たす最大の正の整数 Nは、二分探索によって求めることができる。

while (ok + 1 != ng):
    md = 0
    md = (ok + ng) // 2
    if check(md) <= X:
        ok = md
    else:
        ng = md

print(ok)