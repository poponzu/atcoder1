S = input()
num = int(input())


if num > len(set(S)):
    print(0)
    exit()

res = 0

for i in range(len(S)):
    dist = set()
    for j in range(i, len(S)):
        if S[j] not in dist:
            dist.add(S[j])

        if len(dist) == num:
            res += 1
        elif len(dist) > num:
            break
print(res)

# # 提出版
# def countKDistinctSubstrings(inputString, num):
#     # WRITE YOUR CODE HERE
#     S = inputString
#     # 与えられた文字列の種類よりnumが大きいと0を返す
#     if num > len(set(S)):
#         return 0
#
#     res = 0
#
#     for i in range(len(S)):
#         dist = set()
#         for j in range(i, len(S)):
#             if S[j] not in dist:
#                 dist.add(S[j])
#
#             if len(dist) == num:
#                 res += 1
#             elif len(dist) > num:
#                 break
#     return res