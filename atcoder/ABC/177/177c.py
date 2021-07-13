N=int(input())
A=list(map(int,input().split()))

store = 0
sum=0
mod =10**9 +7
for j in range(N-2,-1,-1):
    store +=A[j+1]
    sum +=(A[j] * store)% mod

print(sum % mod)