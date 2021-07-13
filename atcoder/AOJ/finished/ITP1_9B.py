while True:
    text = input()
    if text =="-":
        break
    m = int(input())
    h=[0]*m
    #ｈにシャッフル回数のリスト
    for i in range(m):
        h[i]=int(input())
    for j in range(m):
        text= text[h[j]:]+text[:h[j]]

    print(text)




