n=int(input())

tarou_point=0
hanako_point=0

for i in range(n):
    tarou, hanako = input().split()  # １行に空白区切りで与えられた２つの文字列を読み込む
    if tarou == hanako:
        tarou_point+=1
        hanako_point+=1
    elif tarou < hanako:
        hanako_point +=3
    elif tarou > hanako:
        tarou_point +=3

ans =[tarou_point,hanako_point]

print(*ans)