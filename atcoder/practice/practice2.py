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

arr = [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(binarySearch(arr, 1))