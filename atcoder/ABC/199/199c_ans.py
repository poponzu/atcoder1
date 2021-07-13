N = int(input())
S = list(input())

pre = S[:N]
post = S[N:]

flipped = False
Q = int(input())
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T==1:
        A -= 1
        B -= 1
        if B<N:
            pre[A],pre[B]=pre[B],pre[A]
        elif A>=N:
            post[A-N],post[B-N]=post[B-N],post[A-N]
        else:
            pre[A], post[B-N] = post[B-N], pre[A]
    else:
        pre,post=post,pre

print("".join(pre)+"".join(post))

