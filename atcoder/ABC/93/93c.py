A = list(map(int,input().split()))

A.sort()
cnt = 0

diff1 = A[1] - A[0]
# [0]と[1]の比較
if diff1 % 2 == 0:
    cnt += diff1 // 2
else:
    cnt += diff1 // 2 + 1
    A[2] += 1
#
# # [1]と[2]の比較
# diff2 = A[2] - A[1]
# if diff2 % 2 == 0:
#     cnt += diff2 // 2
# else:
#     cnt += diff2 // 2 + 1
cnt += A[2] - A[1]

print(cnt)