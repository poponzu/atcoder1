import re
# 文字列の逆順の操作に注意
T = input()
T_rev = "".join((list(reversed(T))))

dic = ["dream", "dreamer", "erase", "eraser"]
dic_rev = []

# dic_revを作る作業
for d in dic:
    a = "".join(list(reversed(d)))
    dic_rev.append(a)
# print(dic_rev)

# dic内の単語でfor文検索
for i in dic_rev:
    # 辞書にある単語がターゲットにあるか
    # あったらそこ消す
    if i in T_rev:
        T_rev = re.sub(r"(maerd|remaerd|esare|resare)*", "", T_rev)

# 全部分解できたらもぬけのからになってYES
if T_rev == "":
    print("YES")
else:
    print("NO")
