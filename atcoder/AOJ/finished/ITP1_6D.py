n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]

# print(a,b)
ans =[]
for i in range(n):
    sum = 0
    for j in range(m):
        sum += a[i][j]*b[j]
    ans.append(sum)

for anser in ans:
    print(anser)



