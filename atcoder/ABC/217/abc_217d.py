# Binary Indexed Tree
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_


# 入力
L, Q = map(int, input().split())

C = []
# 最初の両端を集合Sに含める
X = []

# クエリ先読み
for _ in range(Q):
    c, x = map(int, input().split())

    C.append(c)
    if c == 1:
        X.append(x)

# 座標圧縮
X = {x: i for i, x in enumerate(sorted(set(X)))}
print(X)
Solve = Bit(len(X))


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


# クエリ処理
for i in range(Q):
    if C[i] == 1:
        Solve.add(get_keys_from_value(X, i), 1)
    else:
        print((Solve.lower_bound(Solve.sum(get_keys_from_value(X, i) - 1) + 1)), (Solve.lower_bound(Solve.sum(get_keys_from_value(X, i)))))
