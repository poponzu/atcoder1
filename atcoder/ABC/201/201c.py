#Sは o, x, ? のみからなる長さ10の文字列
S=input()
import math
o_count = S.count("o")
x_count = S.count("x")
q_count = S.count("?")

if o_count>=5:
    print("0")
    exit()
elif o_count==4:
    print(4**4)
    exit()
#ここまではあってる
elif o_count==0:
    print(q_count**4)
#o_count==1,2,3の場合をまとめてかく:
#o_count==1の場合はいける
elif o_count==1 :
    # n = 5
    # r = 3
    # result = factorial(n) / (factorial(n - r) * factorial(r))
    q1=o_count*4*(q_count**3)
    q2=6*(o_count**2)*(q_count**2)
    q3=4*q_count*(o_count**3)
    q4=o_count**4
    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q1+q2+q3+q4)
    exit()
else :
    # n = 5
    # r = 3
    # result = factorial(n) / (factorial(n - r) * factorial(r))
    q1=o_count*4*(q_count**3)
    q2=math.factorial(o_count) / (math.factorial(o_count - 2) * math.factorial(2))*(o_count**2)*(q_count**2)
    q3=math.factorial(o_count) / (math.factorial(o_count - 3) * math.factorial(3))*q_count*(o_count**3)
    q4=o_count**4
    print(q1)
    print(q2)
    print(q3)
    print(q4)
    print(q1+q2+q3+q4)
    exit()
