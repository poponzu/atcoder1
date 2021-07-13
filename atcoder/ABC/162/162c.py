import math
K=int(input())

sum = 0

for a in range(1,K+1):
    for b in range(1,K+1):
        ans = math.gcd(a,b)
        for c in range(1,K+1):
            sum += math.gcd(ans,c)

print(sum)