# Aのすべての素因数を求めて，その素因数を持たない1以上M以下の整数を求められれば良い

N, M = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(max(A), M)

k = [True] * (maxA + 1)  # iが条件を満たすか（iが使えるか）
isprime = [True] * (maxA + 1)  # iが素数か
prime = []  # Aに含まれる素因数（使えない素数）

# Aの要素は使えない
for a in A:
    k[a] = False

# エラトスネスの篩
for i in range(2, maxA + 1):
    # is_primeがFalseならcontinue
    # もう素数じゃないとわかってるからスルー
    if not isprime[i]:
        continue
    # iについての素数判定終了
    # ここまできてたらiは素数
    # 素数じゃないと決めていく
    for j in range(i * 2, maxA + 1, i):
        isprime[j] = False
        # iはjの素因数
        # jがAの要素ならiは使えない
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

# 使えない素数pに対してpの倍数を使えなくする
for p in prime:
    for j in range(p * 2, M + 1, p):
        k[j] = k[j] and k[p]

# 使える数をansに入れる
ans = [1]
for i in range(2, M + 1):
    if k[i]:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)
