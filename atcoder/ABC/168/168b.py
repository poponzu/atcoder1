#
# K = int(input())
#
# S = input()
#
# if len(S)<=K:
#     print(S)
# else:
#     print(S[:K]+'...')

def pancakesort(buff):
    L=len(buff)
# パンケーキソート
    for size in range(L, 1, -1):
        # リストの最大値のインデックスをkeyに代入
        maxindex = max(range(size), key=buff.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                buff[:maxindex+1] = reversed(buff[:maxindex+1])
            # Flip it into its final position
            buff[:size] = reversed(buff[:size])

lst =[2,1,6, 7, 3,6]
pancakesort(lst)
print(lst)
# 実行結果 =[1, 2, 3, 6, 6, 7]