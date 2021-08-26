# 8分AC

import math
N = int(input())
# math.log(x, y)はyを底としたxの対数を返す

#AとBの変域を特定できる
print(math.log(10**18, 5))
# --> 25.752178045321074
print(math.log(10**18 - 5, 3))
# --> 37.72625893720892

for A in range(1,38+1):
    for B in range(1,26 + 1):
        if 3**A + 5**B ==N:
            print(A,B)
            exit()

print(-1)

