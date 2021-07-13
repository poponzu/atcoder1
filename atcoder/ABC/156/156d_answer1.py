n, a, b = map(int, input().split())
mod = int(1e9 + 7)
# print(1e9+7)

def comb(r):
    bunshi = 1
    # iは2からnの範囲を動く
    # これは前からnCr の分子を計算している
    for i in range(n - r + 1, n + 1):
        bunshi = bunshi * i % mod
    bunbo = 1
    # これは後ろからnCr の分子を計算している
    for i in range(1, r + 1):
        bunbo = bunbo * i % mod
    # フェルマーの小定理を使ってる
    return bunshi * pow(bunbo, mod - 2, mod) % mod


ans = pow(2, n, mod) - 1 - comb(b) - comb(a)
ans = (ans + 2 * mod) % mod
ans1 = ans% mod
print(ans1)