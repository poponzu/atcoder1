# 12:12 ~ 12:30
# 解答 https://atcoder.jp/contests/code-festival-2014-morning-easy/submissions/25660144

n = int(input())
rev = False

# その順位が逆順かどうか調べる
for N in range(1,6):
    if 40 * N - 19 <= n <= 40 * N:
        rev = True

# %20の方で良い
if rev:
    team = n % 20
    if team == 0:
        team = 20
    # team = n % 21
    ans = 21 - team
else:
    ans = n % 20
    if ans == 0:
        ans = 20
    # ans = n % 21



print(ans)
