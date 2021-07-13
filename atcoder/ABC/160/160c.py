# k,n=map(int,(input().split()))
# A=list(map(int,input().split()))
#
# #区間をまたいだ工夫俺には思いつけない
# A.append(A[0]+k)
#
# Max = -float("INF")
#
# for i in range(n):
#     Max = max(Max, abs(A[i+1]- A[i]))
#
# print(k - Max)

k,n=map(int,(input().split()))
A=list(map(int,input().split()))

#区間をまたいだ工夫俺には思いつけない
A.append(A[0]+k)

Max = -float("INF")

for i in range(n):
    Max = max(Max, abs(A[i+1]- A[i]))

print(k - Max)