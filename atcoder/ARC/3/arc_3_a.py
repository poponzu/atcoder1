# 予想されたAC時間は30 minsやったが、実際は6分でAC
from collections import Counter

N = int(input())
r = list(input())
dic = Counter(r)
# 変数名に標準ライブラリ関数と被る単語は使わないでおこう
tot = 0
for k, v in dic.items():
    if k == "A":
        tot += 4 * v
    elif k == "B":
        tot += 3 * v
    elif k == "C":
        tot += 2 * v
    elif k == "D":
        tot += 1 * v
    else:
        tot += 0 * v

ans = tot / N

print(ans)
