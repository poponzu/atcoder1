def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        # この整列済みのリストの一つ右の要素がなぜ適切な位置にいくのか？
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr

lst =[33, 1, 68, 43, 71,22]
insert_sort(lst)
print(lst)