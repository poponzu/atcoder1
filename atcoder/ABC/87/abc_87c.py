# 22分AC

n = int(input())

a = [list(map(int,input().split())) for _ in range(2)]

ans = -1
if n == 1:
    print(a[0][0] + a[1][0])
    exit()

for r in range(n-1):
    up = sum(a[0][:r+1])
    down = sum(a[1][r:])
    candy = up + down
    ans = max(ans, candy)

print(ans)