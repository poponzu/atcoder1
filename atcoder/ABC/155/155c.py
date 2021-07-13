n = int(input())
List=[input() for i in range(n)]
max = 0
for i in List:
    if max <= List.count(i):
        # 最大値更新
        max = List.count(i)
        # 出現回数最大の文字をコピーしたリスト作成
name_List = [i for i in List if List.count(i) == max]

# print(name_List)
# print(set(name_List))
setted_List = set(name_List)
sorted_List =(sorted(setted_List))
for i in sorted_List:
    print(i)


for i in range(n):
    list.append(n)

for j in range(n):
    list.append(j)