from itertools import product

N = int(input())
XY =[[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int,input().split())
        XY[i].append((x - 1, y))

ans = 0
#真偽不明と正直者を0か1で表す
bits = list(product([0,1],repeat=N))

for honest_list in bits:
    #正直者を羅列するリスト
    honest_idx =[]
    flag = True
    #作ったhonest_listをみながら正直者をリストhonest_idxに追加していく
    for who, h in enumerate(honest_list):
        if h ==1:
            honest_idx.append(who)
    #あとは正直者がhonest_listと矛盾ない発言しているかcheck
    for idx in honest_idx:
        for x,y in XY[idx]:
            if honest_list[x] != y:
                flag = False
                break
    if flag:
        ans = max(ans,len(honest_idx))

print(ans)


