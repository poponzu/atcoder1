from collections import Counter
N = int(input())
S = input()
ans = -1


for i in range(1,N):
    # 前半部分
    pre = Counter(S[:i])
    # 後半部分
    post = Counter(S[i:])

    cnt = 0
    for p in pre.keys():
        if p in post.keys():
            cnt += 1

    ans = max(ans,cnt)

print(ans)