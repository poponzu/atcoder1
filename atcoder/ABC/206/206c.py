from collections import Counter
N = int(input())
A = list(map(int,input().split()))

A = Counter(A)

sum = 0

for i in A.values():
    sum+=i
# print(sum)

ans = 0
for k,v in A.items():
    sum -= v
    ans += v *(sum)

print(ans)