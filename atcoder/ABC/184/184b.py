N, X = map(int, input().split())
S = input()

for s in S:
    #正解したときの＋１点が入っていない
    #不正解のとき持ち点が0の時点数マイナスにしないを追加
    if s =="o":
        X +=1
    else:
        if X!=0:
            X -=1
        else:
            continue

print(X)