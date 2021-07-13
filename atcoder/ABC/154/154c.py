#TLEやった
# オーダを少なくする
n =int(input())
# print(n)
List=list(map(int,input().split()))
count = 0
for i in range(n):
    # print(List[i])
    count += List.count(List[i])
    # print(count)
if count == n:
    print('YES')
else:
    print('NO')
