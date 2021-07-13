def select_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr

lst =[33, 1, 68, 43, 71,22]
select_sort(lst)
print(lst)

# 選択ソート(平均O(n^2))最悪(O(n^2)
# メモリ使用量0(1)
# 不安定
# 整列済みの配列を臨む
https://wonderwall.hatenablog.com/entry/2017/08/18/203000#minmaxindexpy--%E3%83%AA%E3%82%B9%E3%83%88%E5%86%85%E3%81%AE%E6%9C%80%E5%B0%8F%E5%80%A4%E6%9C%80%E5%A4%A7%E5%80%A4%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%87%E3%83%83%E3%82%AF%E3%82%B9%E3%82%92%E5%8F%96%E5%BE%97
"""
Find Index of Min/Max Element.
"""
#
# lst = [40, 10, 20, 30]
#
#
# def minIndex(lst):
#     return min(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7
#
#
# def maxIndex(lst):
#     return max(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7
#
# print(minIndex(lst))
# print(maxIndex(lst))