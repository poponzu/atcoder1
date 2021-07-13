import math
a,b,x = map(int,input().split())

h = (2*(a**2 * b - x )) / a**3

ans = math.degrees(math.atan(h))

print(ans)