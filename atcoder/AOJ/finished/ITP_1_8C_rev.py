from collections import Counter

#小文字のa~zのリストを作成
alpha = [chr(i) for i in range(97, 97+26)]
dict_standard=Counter(alpha)

word =""

while True:
    try:
        ch = input()
        word+=ch
    except EOFError:
        break


#dict_standardの各値を０に戻す
for key in dict_standard:
    dict_standard[key] = 0
#print(dict_standard)
#答えをカウントする
dict_ans = Counter(word)
#standardとansを組み合わせる
dict_standard.update(dict_ans)
#
for key, value in dict_standard.items():
    if key.isalpha():
        print(str(key)+" : "+str(value))
#これやと大文字のTがカウントされる今回はcounterなし