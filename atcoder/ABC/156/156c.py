n = int(input())
List = list(map(int, input().split()))
min = 10000000000
sum = 0
# Pを決める
for P in range(1,101):
 # L[i]のループこのループ終わったらsumを初期化しておきたい

    sum = 0
    for L in List:
        sum += pow((P - L), 2)
    if min >= sum:
        min = sum
# 　値の更新がうまくできていない
# 最小値の決め方がおかしかった
print(min)
