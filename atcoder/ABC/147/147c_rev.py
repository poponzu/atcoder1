from itertools import product

n = int(input())
# 全員分の証言を入れる
XY = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        # indexを合わせるためにx-1
        # 一人当たり複数かつバラバラの数証言があるため
        XY[i].append((x-1,y))
        
ans = 0
# 01で全員分の不親切・正直のパターン作る
bits = list(product([0,1],repeat=n))
# 全員分の不親切・正直のパターンを一つずつ矛盾がないか確認
for honest_list in bits:
    # 正直者とした人のindexを入れる
    honest_idx = []
    flag = True
    # 仮定の話
    for who, h in enumerate(honest_list):
        if h == 1:
            honest_idx.append(who)
    # 実際と突き合わせる
    for idx in honest_idx:
        #ここらへんの添字難しい
        for x, y in XY[idx]:
            if honest_list[x] != y:
                flag = False
                break
    # 矛盾が生じなかったら
    # 正直者と仮定した人の人数を数える
    if flag:
        ans = max(ans, len(honest_idx))
print(ans)