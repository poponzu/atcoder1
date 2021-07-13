n,m = map(int,input().split())
S = []
C = []
for _ in range(m):
    s,c = map(int,input().split())
    S.append(s)
    C.append(c)

for i in range(1000):
    flag1 = 0
    flag2 = 0
    count = 0

    if len(str(i)) == n:
        flag1 = 1

    count = 0
    for j in range(m):
        i = str(i)
        if S[j] > len(i):
            break

        if i[S[j]-1] == str(C[j]):
            count += 1

    if count == m:
        flag2 = 1

    if flag1 == 1 and flag2 == 1:
        print(i)
        exit()
    else:
        continue

print(-1)


#初期化ミス flagの初期化とカウント
#全探索と気づけたのは成長の証