import itertools
n,k = map(int,input().split())
List = list(map(int, input().split()))
# multiple_List = [0]
# if n % 2 != 0:
#     for i in range(3-1):
#         multiple_List.append(List[i]*List[i+1])
# https://qiita.com/junkls/items/10384950963056cc8e08を参考にしてる
# ここも参考にできそう"https://tutorialmore.com/questions-1690667.htm"
print(list(itertools.combinations(List,2)))

# 積のリストを作ってそのリストそーとしてK番目のインデックスを表示させる
# 方針は建てれる.でも組み合わせの要素の積のリストがつくれない




