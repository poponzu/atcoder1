N=int(input())
MAX_N = N

memo=[0]*(MAX_N + 1)

def fib(n):
    if n<=1:
        return n
    if memo[n]!=0:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

for i in range(N):
    print(fib(i))