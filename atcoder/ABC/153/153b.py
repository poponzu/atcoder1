h,n=map(int,input().split())
List=list(map(int,input().split()))
# print(h)
# print(n)
# print(List)
# リストの要素の合計が体力より多かったら討伐できる
if sum(List)>= h:
    print('Yes')
else:
    print('No')