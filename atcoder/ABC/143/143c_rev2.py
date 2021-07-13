# s = input()
import numpy as np
# n = int(input())
# s = input()
# S = []
#
# for i in s:
#     S.append(ord(i))
#
# sequence1 = np.array(list(S))

# def RLE_numpy(sequence):
#
#     diff_seq = np.diff(sequence) # sequence[i+1] - sequence[i]のアレイ。隣と同じだと0になる。
#
#     # newdata は、前の要素とインデックスが違うときだけTrueになるBoolのアレイ。
#     newdata = np.append(True, diff_seq != 0) # 先頭をTrueにして、2番目以降をappendで追加している。
#     comp_seq = sequence[newdata]  # sequence から、newdataがTrueの要素だけ抜き出す
#
#     comp_seq_index = np.where(newdata)[0]  # newdataがTrueの要素が、アレイの何番目に来るか取得
#     comp_seq_index = np.append(comp_seq_index, len(sequence))  # アレイの終了をつける
#     lengths = np.diff(comp_seq_index) # newdataがTrueになっている位置の差がlengthになる
#
#     return comp_seq, lengths
#
#
# print(RLE_numpy(sequence1))

##二つ目の方法 文字列のリストでも対応

n = int(input())
s = input()
sequence = np.array(list(s))

def RLE_numpy2(sequence):
    comp_seq_index, = np.concatenate(([True], sequence[1:] != sequence[:-1], [True])).nonzero()
    return sequence[comp_seq_index[:-1]], np.ediff1d(comp_seq_index)

print(RLE_numpy2(sequence))
