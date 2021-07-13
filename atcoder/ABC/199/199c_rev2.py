N = int(input())
S = list(input())
Q = int(input())

flag2 = False
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if flag2:
            # 文字の入れ替えを同じ前半・後半それぞれで行う場合
            if abs(B - A) < N:
                S[A - N - 1], S[B - N - 1] = S[B - N - 1], S[A - N - 1]
            # 文字の入れ替えを前半グループと後半グループでまたがって行う場合
            else:
                S[N + A - 1], S[B - N - 1] = S[B - N - 1], S[A + N - 1]
        else:
            S[A - 1], S[B - 1] = S[B - 1], S[A - 1]
    else:
        #ここを真偽値の入れ替えかけたのえらい
        flag2 = not flag2

#リストの文字列連結はjoinでok
if flag2:
    print("".join((S[N:] + S[:N])))
else:
    print("".join(S))