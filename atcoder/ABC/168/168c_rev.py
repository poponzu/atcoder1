import math
A,B,H,M=map(int,input().split())

degree=abs(6*M - (30*H+0.5*M))
rad= math.radians(degree)

if degree==0:
    ans = abs(A-B)

else:
    ans = math.sqrt(A**2 + B**2 -2 * A * B * math.cos(rad))

print(ans)
#degree==0のときの場合わけがいるのかどうかたしかめのため
#print(math.sqrt(A**2 + B**2 -2 * A * B * math.cos(rad)))

