import math
import numpy as np

#約数列挙O(sqrt(N))リストで返す
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

#素数判定 O(sqrt(N))
def bool_is_prime(n):
    if n<=1:
        return False
    for i in range(2,math.floor(math.sqrt(n))):
        if n%i == 0:
            return False
    return True
    return True

#最小公倍数を求める(x,yが整数かの判定はない）
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

#ランレングス圧縮 O(N)
#返す値は二つのリスト 一つ目は与えられたリストの出現する文字、二つ目はその出現回数 添字が対応している
def RLE_for(sequence):

    #戻り値の初期化
    comp_seq = list() # 圧縮されたデータのリスト
    lengths = list() # データの連続する長さのリスト

    # 最初の要素を記録
    comp_seq.append(sequence[0])
    temp = sequence[0]
    length = 1

    # 2番目から最後まで
    for i in range(1, len(sequence)):
        if sequence[i] != temp:  # 新しいデータが来たら、これまでのデータとその長さを記録
            lengths.append(length)
            comp_seq.append(sequence[i])
            temp = sequence[i]
            length = 1
        else: # 前と同じデータが来たら、lengthをインクリメント
            length += 1

    # 最後にlengthを追加
    lengths.append(length)

    return comp_seq, lengths

#二つ目の方法 文字列のリストでも対応
#入力はnp.arrayに変えておく。
def RLE_numpy2(sequence):
    comp_seq_index, = np.concatenate(([True], sequence[1:] != sequence[:-1], [True])).nonzero()
    return sequence[comp_seq_index[:-1]], np.ediff1d(comp_seq_index)

#深さ優先探索 204cで使用
# dfs
G = [[] for i in range(N)]

seen=[]
def dfs(v):
    seen[v] = True
    # vから行ける各頂点next_vについて
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

#Union find 206で使用----------------------------------
#REは配列外参照

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
#-----------------------------------------------

#二項係数を求める①
from operator import mul
from functools import reduce

def cmb1(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
#二項係数を求める②
def cmb2(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
