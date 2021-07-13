N = int(input())
A = list(map(int, input().split()))
# A.append(1000000000)
# print(N,A) 入力までは行けた
S = A[0]
sum = 0

for i in range(1,N):
    if S >= A[i]:
        diff = S - A[i]
        sum = sum + diff
    else:
        S = A[i]
        sum = sum + 0

print(sum)

