import math
a1, a2, a3 = map(int,input().split())

a21 = a2 - a1
a32 = a3 - a2

ans = 0

if a21 <= a32:
    sum = a21 + a32
    print(math.ceil(sum/2))
else:
    sum = a21 + a32

