N = int(input())
A = [int(e) for e in input().split()]
B = [0 for i in range(200)]

count = 0
for i in range(N):
    B[A[i]%200]+=1

for j in range(200):
    count += B[j]*(B[j]-1)//2

print(count)
#
# N = int(input())
# A = [int(e) for e in input().split()]
# B = [0 for i in range(200)]
# count = 0
# for i in range(N):
#     B[A[i]%200] = B[A[i]%200] + 1
# for i in range(200):
#     count = int(count + B[i]*(B[i]-1)/2)
# print(count)