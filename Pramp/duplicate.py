# 一つの配列に重複する値はあっても大丈夫なのか？
# 解説の方法すこしまずい


# 解法1
# time Complexity O(max(N,M))
# space Complexity O(max(N,M))
def findDuplicates1(arr1, arr2):
    duplicates = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            duplicates.append(arr1[i])
            i = i + 1
            j = j + 1
        elif arr1[i] < arr2[j]:
            i = i + 1
        else:
            j = j + 1

    return duplicates


# 解法2
# time Complexity O(max(N,M))
# space Complexity O(max(N,M))
from collections import Counter


def findDuplicates2(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    l1 = len(list(arr1))
    l2 = len(list(arr2))

    ans = []

    if l1 <= l2:
        dict1 = Counter(arr1)
        set2 = set(arr2)
        for k in dict1.keys():
            if k in set2:
                ans.append(k)
    else:
        dict2 = Counter(arr2)
        set1 = set(arr1)
        for k in dict2.keys():
            if k in set1:
                ans.append(k)

    ans.sort()

    return ans


A = [1, 2, 2, 3, 4, 5]
B = [2, 2, 5, 6, 10, 14]

print(findDuplicates2(A, B))
