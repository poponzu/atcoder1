N =int(input())
L = [list(map(int, input().split())) for i in range(N)]

ans = 0

for i in range(N):
    ans += ((L[i][1]-L[i][0]+1)*(L[i][0]+L[i][1]))/2

print(int(ans))