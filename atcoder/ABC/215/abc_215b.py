import math
# print(math.log(10**18,2))
N = int(input())

ans = 0
for k in range(70):
    if 2 ** k <= N:
        ans = max(ans,k)

print(ans)
