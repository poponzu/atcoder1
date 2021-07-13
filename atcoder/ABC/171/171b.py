N, K = map(int, input().split())
count= 0
x = list(map(int, input().split()))
p = sorted(x)
# print(p)
for k in range(0,K):
    count += p[k]

print(count)