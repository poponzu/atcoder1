n = int(input())
A = list(map(int,input().split()))
ans = 0

for a in A:
    while (a % 3 == 2 or a % 2 ==0):
        a -= 1
        ans += 1

print(ans)

