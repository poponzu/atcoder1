a,b,c =map(int,input().split())

A=[]
A.append(a)
A.append(b)
A.append(c)

count_a = 0
count_b= 0
count_c =0

if a==b and b ==c:
    print(a)
elif a != b and b !=c and c != a:
    print(0)
else:
    count_a =A.count(a)
    count_b = A.count(b)
    count_c =A.count(c)
    if count_a == 1:
        print(a)
    elif count_b ==1:
        print(b)
    else:
        print(c)