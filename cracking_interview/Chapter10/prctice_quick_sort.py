def quick_sort(arr):
    left = []
    right = []

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    pivot_cnt = 0

    for ele in arr:
        if ele < pivot:
            left.append(ele)
        elif ele > pivot:
            right.append(ele)
        else:
            pivot_cnt += 1

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] * pivot_cnt + right



test = [10, 2, 5, 9, 21]
# random.shuffle(test)
print(test)
print(quick_sort(test))