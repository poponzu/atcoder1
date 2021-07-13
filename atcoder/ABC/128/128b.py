N = int(input())

list = []

for _ in range(N):
    s, p = input().split()
    list.append((s, int(p)))

#print(list)

# 名前順と点数高い順にソート
# 別々にソートしてもいけない。
list_sorted1 = sorted(list, key=lambda x: (x[0],-x[1]))
#print(list_sorted1)


for a in list_sorted1:
    print(list.index(a) + 1)
