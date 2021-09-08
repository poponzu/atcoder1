n, m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))


cnt = 0
if t.count(s[0]) == m:# tがs[0]のみで構成されている場合
    print(m)
elif s.count(s[0]) == n:# sがs[0]のみで構成されている場合(tには二種類の値が含まれている）
    print(-1)
else:
    x = 10**6 # Sの中で先頭のS1と異なる文字でもっとも近いもの
    y = -1    # Sの中で先頭のS1と異なる文字でもっとも遠いもの
    for i in range(1,n):
        if s[0] != s[i]:
            x = min(i,x)
            y = max(i,y)

    shift = min(x,y)

    now=s[0]

    ans=0
    for i in range(m):
        if t[i]==now:
            ans+=1
            pass

        else:
            now^=1
            ans+=shift
            cnt=1
            ans+=1
    print(ans)








