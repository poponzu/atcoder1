N = int(input())
S = input()
ans = -1


for i in range(1,N):
    count = [0]*1000
    # 前半部分
    pre = S[:i]
    # 後半部分
    post = S[i:]

    for p in pre:
        if p in post:
            #すでに1のところはスルー
            if count[ord(p)] == 0:
                count[ord(p)] += 1


    ans = max(ans,sum(count))

print(ans)