def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr
#
# def bubble_sort2(arr):
#     i = 0
#     j = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)-1,

# バブルソート(平均O(n^2))最悪(O(n^2)
# メモリ使用量0(1)
# 安定

lst =[33, 1, 68, 43, 71,22]
bubble_sort(lst)
print(lst)