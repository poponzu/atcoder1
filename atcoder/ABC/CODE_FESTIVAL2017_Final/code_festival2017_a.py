# 13:06 ~ 13:20
# productの使い方（”https://qiita.com/keroido/items/8744453a50d8c8b471c1#python%E3%81%A7%E3%81%AE%E5%AE%9F%E8%A3%85”）

# import math
#
# print(math.log(2**50,10))

from itertools import product

# target =list("AKIHABARA")
can_make_akiba = False

S = input()

#targetの0,4,6,8番目を使う使わないか
pat = list(product([False, True], repeat=4))#2^4通り

# targetから”A"を取り除いてできる文字列16種類とSが一致するかどうかを調べる
for pair in pat:
    target =list("AKIHABARA")
    if pair[0]:
        target[0] = ""
    if pair[1]:
        target[4] = ""
    if pair[2]:
        target[6] = ""
    if pair[3]:
        target[8] = ""

    made = "".join(target)

    # print(made)
    if made == S:
        can_make_akiba = True

if can_make_akiba:
    print("YES")
else:
    print("NO")