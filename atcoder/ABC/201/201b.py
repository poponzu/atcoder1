N=int(input())

for i in range(N):
    name = []
    height = []
for i in range(N):
    n, h = input().split()
    name.append(n)
    height.append(int(h))
# print(name)
# print(height)

second=sorted(height)[-2]
# print(second)
print(name[height.index(second)])
