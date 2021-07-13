n=int(input())
R = [int(input()) for i in range(n)]

maxR=-(10**9)
minR=R[0]

for j in range(1,n):
    maxR = max(maxR, R[j] - minR)
    minR = min(minR,R[j])


print(maxR)