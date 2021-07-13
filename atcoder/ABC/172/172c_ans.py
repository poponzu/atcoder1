#参考にした"https://qiita.com/DaikiSuyama/items/ab8d7812e549c2f2e9cf#c%E5%95%8F%E9%A1%8C"

from itertools import accumulate
from bisect import bisect_left,bisect_right

n,m,k=map(int,input().split())
a=[0]+list(accumulate(map(int,input().split())))
b=[0]+list(accumulate(map(int,input().split())))

ans=[0]
for i in range(n+1):
    #cはｂから何冊読めるかをもらう
    c=bisect_right(b,k-a[i])-1
    #K−SA<0 の時は求めるインデックスが-1となるので、除外する必要があるので注意が必要です。
    #ここ大事2回目でもできなかった
    if c !=-1:
        ans.append(c+i)
print(max(ans))