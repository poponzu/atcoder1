A, B =map(int,input().split())

for i in range(1, 11):
    A_new = (A * i) * (i -1)
    if A_new >= B:
        print(i)
        break

#問題が理解できひん　入力と出力の例がおかしい