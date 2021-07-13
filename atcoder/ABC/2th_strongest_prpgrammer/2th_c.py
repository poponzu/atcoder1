from itertools import combinations

A, B = map(int, input().split())
my_list = []
gcd_max=1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(A,B+1):
    my_list.append(i)


x = combinations(my_list, 2)

list_x = list(x)
# print("組合せ：{}".format(list_x))
#print(list_x[0][0])

for i in range(len(list_x)):
    current_gcd=gcd(list_x[i][0],list_x[i][1])
    if gcd_max<current_gcd:
        gcd_max=current_gcd

print(gcd_max)