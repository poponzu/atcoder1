a,b = map(int,input().split())

#最小公倍数を求める(x,yが整数かの判定はない）
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(my_lcm(a,b))