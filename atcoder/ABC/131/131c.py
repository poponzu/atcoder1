import math
A,B,C,D=map(int,input().split())

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

LCM = my_lcm(C,D)

C_count=B//C -(A-1)//C
D_count=B//D -(A-1)//D
LCM_count =B//LCM -(A-1)//LCM

all=B-A+1

if C!=D:
    ans = all-(C_count+D_count-LCM_count)
else:
    ans = all-C_count

print(ans)

