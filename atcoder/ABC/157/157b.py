import itertools
# ここを参考にした
# https://note.nkmk.me/python-list-index/

# def my_index(l, x, default=False):
#     if x in l:
#         return l.index(x)
#     else:
#         return default

Bingo_index=[]
master =[]
# 二次元リスト
Row = 3
List=[[int(j) for j in input().split()] for i in range(Row)]
# 二次元リストを一次元リストに
dim_List=list(itertools.chain.from_iterable(List))
# print(dim_List)
# ビンゴ表作成終わり

n = int(input())
# print(n)
Num=[int(input()) for i in range(n)]
# print(Num)
# print(set(dim_List) & set(Num))
# 入力処理ここまで

Common = list(set(dim_List) & set(Num))
# print(Common)
# https://teratail.com/questions/156336
# リストに要素をコピーする方法↑
for a in Common:
    # if(my_index(dim_List,a) == False):
    #     print('No')
    Bingo_index.append(dim_List.index(a))
#
# print('Bingo_indexは')
# print(Bingo_index)
# print(sorted(Bingo_index))
if len(Bingo_index) == 0:
     print('No')
     exit()
    # Bingo_indexにビンゴしてるdim_Listの要素のインデックスが入ってる
answer1 = len(list(set([0, 1, 2])&set(Bingo_index)))
answer2 = len(list(set([3, 4, 5])&set(Bingo_index)))
answer3 = len(list(set([6, 7, 8])&set(Bingo_index)))
answer4 = len(list(set([0, 4, 8])&set(Bingo_index)))
answer5 = len(list(set([0, 3, 6])&set(Bingo_index)))
answer6 = len(list(set([1, 4, 7])&set(Bingo_index)))
answer7 = len(list(set([2, 5, 8])&set(Bingo_index)))

# Bingo_indexの中身にとanswer1~7の組み合わせがあるかどうか調べる
# 全部のアンサーとandをとってどれかの長さが3の奴があればyes出力や
master.append(answer1)
master.append(answer2)
master.append(answer3)
master.append(answer4)
master.append(answer5)
master.append(answer6)
master.append(answer7)
# print(master)
# print(master.count('3'))
for e in master:
    if e ==3:
        print('Yes')
        exit()
print('No')