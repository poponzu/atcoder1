# 参考にしたページ（”https://blog.hamayanhamayan.com/entry/2020/10/10/232835”）

N = int(input())
P = list(map(int, input().split()))

num = set()
ans = 0

# 計算量O(N)?
for i in range(N):
    num.add(P[i])
    # for文全体で10**6くらいしかループしない
    while ans in num:
        ans += 1
    print(ans)