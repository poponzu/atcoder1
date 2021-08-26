def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        # midの更新をwhile文の中に入れる
        mid = (low + high) // 2

        if x < arr[mid]: # 探索範囲を左半分
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1 # 探索範囲を左半分
        else:
            return mid

    return -1 # エラー

test = list(range(10))

print(binary_search(test,3))