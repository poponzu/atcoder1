N=int(input())
A=list(map(int,input().split()))

left_max=max(A[:(2**N)//2])
right_max=max(A[(2**N)//2:])

second_score=min(left_max,right_max)


print(A.index(second_score)+1)


# left=False
#
# if Min==left_max:
#     left=True
#
# if left:
#     print(A.index(Min)+1)
# else:
#     print(A.index(Min)+1)

#
# print(A.index(sorted(A)[-2]))

