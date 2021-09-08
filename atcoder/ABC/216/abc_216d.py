N,M = map(int,input().split())
K =[]
A =[]
for _ in range(M):
    k = int(input())
    a = tuple(map(int,input().split()))
    K.append(k)
    A.append(a)

# for i in range(M):
#     print(K[i])
#     print(A[i])

# print(A)
ans = set(tuple(A))
# print(ans)

if M % 2 == 0:
    if len(ans) == 2 // M:
        print("Yes")
    else:
        print("No")
else:
    print("No")

#
# def binary_search(arr,target):
#     low = 0
#     high = len(arr) - 1
#     mid = 0
#     while low <= high:
#         mid = (low + high) // 2
#         if target < arr[mid]:
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             return mid
#     return -1



