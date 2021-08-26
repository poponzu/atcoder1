import random

def quickSort(arr, left, right):
    index = partition(arr, left, right)

    if left < index - 1:  # 左半分をソートする
        quickSort(arr, left, index - 1)
    if index < right:  # 右半分をソートする
        quickSort(arr, index, right)


def partition(arr, left, right):
    pivot = arr[(left + right) // 2]  # ピポット(分割に使う要素)を選ぶ
    while left <= right:
        # 右にあるべき左側の要素を探す
        while arr[left] < pivot:
            left += 1
        # 左にあるべき右側の要素を探す
        while arr[right] > pivot:
            right -= 1

        # 要素を入れ替え, leftとrightのインデックスを進める
        if left <= right:
            # swap(arr, left, right)
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


# test = list(range(20))
# random.shuffle(test)
test = [10, 2, 5, 9, 21]
print(test)
quickSort(test, 0, len(test) - 1)
print(test)
