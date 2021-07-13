from collections import Counter
import  itertools

n = input()

if len(n) <= 2:
    #長さが２以下のものは、その順番のものとひっくり返したものの余りで判断
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()


amari = ""
#文字列nを法8の剰余に関してまとめる
#剰余の辞書型にするのが目的
for i in n:
    if i =="8":
        amari += "0"
        continue
    if i =="9":
        amari += "1"
        continue
    amari += i

S = Counter(amari)

number = [0,1,2,3,4,5,6,7]
cmb = itertools.combinations_with_replacement(number, 3)

#rに3桁で8の倍数になる組み合わせが入っている
#8の倍数も各桁の剰余の合計が8の倍数なら, 8の倍数なると勘違いしてた
#ここは全探索で頑張った方がいい
r =[]
for c in cmb:
    if sum(c) % 8 == 0:
        r.append("".join(map(str, c)))

count = 0

#satisfyから入力Sをひいて空のオブジェクトが帰って来たら"Yes"
for i in r:
    satisfy = Counter(i)
    if satisfy - S:
        continue
    else:
        print("Yes")
        exit()

print("No")

