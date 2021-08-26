def MergeSort(arr):
    n = len(arr)

    if n == 1:
        return arr
    # 1. divide into two lists
    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]
    # 2. sort two divided lists(sublists)
    l = MergeSort(left)
    r = MergeSort(right)

    # 3. merge two lists
    return Merge(l,r)

def Merge(A,B):
    C = []

    # compare array top of sorted list(A,B)
    # Repeat until Either one is empty
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            C.append(A[0])
            del A[0]
        else:
            C.append(B[0])
            del A[0]

    # Remaining elements added in C.
    if len(A) > 0:
        C.extend(A)
    else:
        C.extend(B)

    return C


test = [10, 2, 5, 9, 21]
# random.shuffle(test)
print(test)
print(MergeSort(test))