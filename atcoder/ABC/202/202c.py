from collections import Counter

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A=Counter(A)
B_Cj =[]

for j in range(N):
    B_Cj.append(B[C[j]-1])

# print(B_Cj)
B_Cj = Counter(B_Cj)

# print(A)
# print(B_Cj)

count = 0

for k,v in A.items():
    if k in B_Cj:
        count += v*B_Cj.get(k)

print(count)
