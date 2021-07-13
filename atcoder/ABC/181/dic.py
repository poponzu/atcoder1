# from collections import Counter
#
# cur = Counter("134")
# S = Counter("1234")
#
# #cur：8の倍数に含まれる数字 - S：数字列Sに含まれる数字
#
# print(cur - S)
#
# if cur - S:
#     print("cur - Sが空のときにifを通過")
# else:
#     print("cur - Sが空のときにelseを通過")


from collections import Counter
import  itertools

number = [0,1,2,3,4,5,6,7]
cmb = itertools.combinations_with_replacement(number, 3)
r1 =[]
r2 =[]
for c in cmb:
    if sum(c) % 8 == 0:
        r1.append(c)
        r2.append("".join(map(str, c)))

print(r1)
print(r2)


