n=int(input())
List=list(map(int,input().split()))
newList =[0] * n
count = 0
min = List[0]
# print(List)
for i in List:
    # 最小値更新
    if i < min:
        min = i
    # カウントする
    if min >= i:
        count = count + 1

print(count)