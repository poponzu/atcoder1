import random


def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else: # refの重複要素があった場合に活躍する
            ref_count += 1

    # print(left,ref,right)

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right


test = [10, 2, 5, 9, 21]
# random.shuffle(test)
print(test)
print(quick_sort(test))