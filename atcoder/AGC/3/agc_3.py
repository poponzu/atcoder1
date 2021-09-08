# 14:37~ 15:01 かかった

from collections import Counter
S = input()

fix = ""
# dict = {"N":0, "E":0,"S":0, "W":0}

#ランレングス圧縮 O(N)
#返す値は二つのリスト 一つ目は与えられたリストの出現する文字、二つ目はその出現回数 添字が対応している
def RLE_for(sequence):

    #戻り値の初期化
    comp_seq = list() # 圧縮されたデータのリスト
    lengths = list() # データの連続する長さのリスト

    # 最初の要素を記録
    comp_seq.append(sequence[0])
    temp = sequence[0]
    length = 1

    # 2番目から最後まで
    for i in range(1, len(sequence)):
        if sequence[i] != temp:  # 新しいデータが来たら、これまでのデータとその長さを記録
            lengths.append(length)
            comp_seq.append(sequence[i])
            temp = sequence[i]
            length = 1
        else: # 前と同じデータが来たら、lengthをインクリメント
            length += 1

    # 最後にlengthを追加
    lengths.append(length)

    return comp_seq, lengths

comp, _ = RLE_for(S)
comp = "".join(comp)
# print(comp)
dict = Counter(comp)
# print(dict)

can_goback = True

if dict["N"] > 0:
    if dict["S"] <= 0:
        can_goback = False

if dict["S"] > 0:
    if dict["N"] <= 0:
        can_goback = False

if dict["E"] > 0:
    if dict["W"] <= 0:
        can_goback = False

if dict["W"] > 0:
    if dict["E"] <= 0:
        can_goback = False

if can_goback:
    print("Yes")
else:
    print("No")