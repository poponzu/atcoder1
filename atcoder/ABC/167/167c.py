from operator import add

N,M,X=map(int,input().split())
book =[list(map(int, input().split())) for i in range(N)]

ans = float('INF')
count = 0

for i in range(2 ** N):
    total = [0]*(M+1)
    for j in range(N):
        if i >> j & 1:
            # total = [x + y for (x, y) in zip(book[j],total)]

            total = list(map(add,total,book[j]))
    #totalリストの各要素がが基準Xを超えていたら値を更新する
    if all(elem >= X for elem in total[1:]):
        count +=1
        ans = min(total[0],ans)

if count == 0:
    ans = -1

print(ans)
