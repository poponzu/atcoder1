import math
X, Y,Z = map(int, input().split())
ans = Z*Y//X
if Z*Y%X==0:
    print(ans-1)
else:
    print(ans)

#これ一行で済む
#print((Y*Z-1)//X)


