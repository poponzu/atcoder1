import math
a,b,C=map(float,input().split())

c=math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(C)))
L = a+b+c
S=a*b*math.sin(math.radians(C))*0.5
h=b*math.sin(math.radians(C))

print(S,L,h,end=" ")
print()


