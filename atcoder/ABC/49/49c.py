import re

T = input()
T_rev = ''.join(list(reversed(T)))
# print(T_rev)

S = ['dream', 'dreamer', 'erase', 'eraser']
dic_rev = list()
for i in S:
    dic_rev.append(''.join(list(reversed(i))))

# print('dic_rev',dic_rev)

for i in dic_rev:
    if i in T_rev:
        #    print('i',i)
        T_rev = re.sub(r"(maerd|remaerd|esare|resare)*", '', T_rev)
#    print('T_rev',T_rev)

# 分解できて、最後にもぬけの殻になればYes
if T_rev == '':
    print('YES')
else:
    print('NO')
