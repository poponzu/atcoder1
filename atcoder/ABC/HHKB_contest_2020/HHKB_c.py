# 解法1

N = int(input())
P = list(map(int, input().split()))

a = [0] * (2 * 10 ** 5 + 7)
ans = 0

for i in range(N):
    a[P[i]] = 1
    while a[ans]:
        ans += 1
    print(ans)

# 解法2

# 参考にしたページ（”https://blog.hamayanhamayan.com/entry/2020/10/10/232835”）

N = int(input())
P = list(map(int, input().split()))

num = set()
ans = 0

# 計算量O(N)
for i in range(N):
    num.add(P[i])
    # O(log N)になる意味がわからん
    # for分が全部回っても高々N回しかまわらん
    while ans in num:
        ans += 1
    print(ans)