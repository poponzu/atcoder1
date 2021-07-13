s = input()
s_int = [int(i) for i in s]
length = len(s)
#
# count_kisuu = 0
# count_guusuu = 0
#
# for i in s:
#     if(i / 2 == 1 and (s[i] == 'R' or s[i] == 'U' or s[i] == 'D')):
#         count_guusuu += 1
#     if (i / 2 == 0 and (s[i] == 'L' or s[i] == 'U' or s[i] == 'D')):
#         count_guusuu += 1
#
# if(count_kisuu == length / 2 and count_guusuu == length / 2):
#     print('Yes')
# else:
#     print('no')

kisuu = s[0::2]  # 配列の本質てきには偶数やけど、外見上は奇数
guusuu = s[1::2]  # 配列の本質てきには奇数やけど、外見上は偶数

for i in kisuu:
    if (s[i] == 'R' or s[i] == 'U' or s[i] == 'D'):
        count_guusuu += 1

for i in guusuu:
    if (s[i] == 'L' or s[i] == 'U' or s[i] == 'D'):
        count_kisuu += 1

if (count_kisuu == length / 2 and count_guusuu == length / 2):
    print('Yes')
else:
    print('no')
