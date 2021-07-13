n,m = map(int,input().split())
S = []
C = []
for _ in range(m):
    s,c = map(int,input().split())
    S.append(s)
    C.append(c)


for i in range(1000):
    flag1 = True
    flag2 = True

    if len(str(i)) != n:
        flag1 = False

    for j in range(m):
        i = str(i)
        if S[j] > len(i):
            flag2 = False
            break

        if i[S[j]-1] != str(C[j]):
            flag2 = False

    if flag1 == True and flag2 == True:
        print(i)
        exit()
    else:
        continue

print(-1)


#初期化ミス flagの初期化とカウント
#全探索と気づけたのは成長の証