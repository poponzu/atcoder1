# つまりN+1に00...をつければよい

d,n = map(int,input().split())

if n == 100:
    n += 1

print(100 ** d * n)