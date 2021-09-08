# def pancake_sort(arr):
# time approximately O(N**2)

def pancake_sort(arr):
    pass # your code goes here
    for i in range(len(arr), 0, -1):
        Max = max(arr[:i])
        flip2(arr, arr.index(Max))
        flip2(arr, i-1)


    return arr

# Reverses arr[0..i] */
def flip1(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1

def flip2(arr, k):
    target = arr[:k+1]
    # reverseの使い方に手間取った
    target.reverse()
    left = target
    right = arr[k+1:]
    # print(left)
    # print(right)
    arr[:] = left + right


arr = [1, 5, 4, 3, 2]

# print(arr)
# flip2(arr, 4)
# print(arr)
# print(arr)
print(pancake_sort(arr))
