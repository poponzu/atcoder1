# 16:24 ~

N = int(input())
A = list(map(int,input().split()))

candidate = 0
# 全探索の書き方わからん
#
# for digit in range(N):
#     for i in range(A[digit]-1,A[digit]+2):
#         make =
cnt = 0

if N == 1:
    for i in range(A[0]-1, A[0]+2):
        made = i
        if made % 2 == 0:
            cnt += 1
elif N == 2:
    for i in range(A[0]-1, A[0]+2):
        for j in range(A[1]-1, A[1]+2):
            made = i * j
            if made % 2 == 0:
                print(made)
                cnt += 1
