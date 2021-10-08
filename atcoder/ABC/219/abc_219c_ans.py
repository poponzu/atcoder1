x = input()
n =int(input())
S = list(input() for i in range(n))
N =[]
for i in range(len(x)):
    N.append(x[i])
print(N)
print(list(x))

# 新しく与えられた、アルファベットと順番の対応表を作成
# dictのxはアルファベット,i+1は何番目かを表す
dict= {x:i+1 for i,x in enumerate(N)}

new =[]
for i in range(n):
    a =[]
    for j in range(len(S[i])):
        a.append(dict[S[i][j]])
    new.append((a, i))
new.sort() # 第一要素であるリストでソートされる

for i in range(n):
    print(S[new[i][1]])