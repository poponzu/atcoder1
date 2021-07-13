n,k=map(int,input().split())
List=list(map(int,input().split()))
if len(List)<= k:
    print(0)
else:
    newList = sorted(List, reverse=True)
    # print(newList)
    # 必殺技を使い切ったあと
    print(sum(newList[k:]))