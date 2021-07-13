n=int(input())
x = list(map(int, input().split()))

print(*x[::-1])