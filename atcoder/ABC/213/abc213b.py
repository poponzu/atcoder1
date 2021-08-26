N = int(input())
A = list(map(int, input().split()))

sort_A = sorted(A)

print(A.index(sort_A[-2])+1)
