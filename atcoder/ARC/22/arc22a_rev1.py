# 解説のO(N)解法を参考に作成した。

S = input()
# 小文字に統一
S = S.lower()

exist_i = False
exist_c = False
exist_t = False

for j in range(len(S)):
    # 残すiは最初に発見したiで良いからexist_i == Falseを入れる
    # exist_i/c/t == False消してもACでした
    if S[j] == "i" and exist_i == False:
        exist_i = True

    if S[j] == "c" and exist_i == True and exist_c == False:
        exist_c = True

    if S[j] == "t" and all([exist_i, exist_c]) and exist_t == False:
        exist_t = True

if all([exist_i, exist_c, exist_t]):
    print("YES")
else:
    print("NO")
