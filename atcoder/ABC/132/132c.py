#五分AC

N = int(input())
d = list(map(int,input().split()))

d = sorted(d)

mid = N//2

print(d[mid] - d[mid - 1])