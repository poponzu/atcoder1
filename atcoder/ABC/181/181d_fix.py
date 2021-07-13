from collections import Counter
n = input()

if len(n) <= 2:
    #長さが２以下のものは、その順番のものとひっくり返したものの余りで判断
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
#cntにnの辞書型が入った
cnt = Counter(n)
#
# for i in range(112, 1000, 8):
#     #：8の倍数に含まれる数字 - 数字列Sに含まれる数字
#     #左を空にしてくれたら、Sは８の倍数！！
#     if not Counter(str(i)) - cnt:
#         print("Yes")
#         exit()
# print("No")

for i in range(112, 1000, 8):
    #：8の倍数に含まれる数字 - 数字列Sに含まれる数字
    #左を空にしてくれたら、Sは８の倍数！！
    if Counter(str(i)) - cnt:
        continue
    else:
        print("Yes")
        exit()

print("No")
