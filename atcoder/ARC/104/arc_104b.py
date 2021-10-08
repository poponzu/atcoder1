# 10:44 ~
# 入力
N,S = map(str,input().split())
N = int(N)

from collections import Counter

ans = 0
for start in range(len(S)):
    for end in range(start,len(S)+1):
        made = S[start:end]

        # madeは長さが偶数個ではないといけない
        if len(made) % 2 == 0:
            continue

        dict = Counter(made)
        # madeが相補性があるかどうかcheck
        if dict["A"] == dict["T"] and dict["G"] == dict["C"]:
            ans += 1

print(ans)