import random
# 二分探索
def binarySearch(a, x):
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        # ここ切り捨ての//でいいのかどうか
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1  # エラー

# 再帰的な二分探索
def binarySearchRecursive(a, x, low, high):
    if low > high:
        return -1  # エラー

    mid = (low + high) // 2
    if a[mid] < x:
        return binarySearchRecursive(a, x, mid + 1, high)
    elif a[mid] > x:
        return binarySearchRecursive(a, x, low, mid - 1)
    else:
        return mid


# 実際に使ってみる
list =[]
for i in range(20):
    list.append(i)
# ソートされた配列にしか二分探索は意味をなさない
# random.shuffle(list)

print(list)
print(binarySearch(list,5))
print(binarySearchRecursive(list,5,0,len(list) - 1))