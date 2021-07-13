A,B=map(int,input().split())
import math

for x in range(10*B,10*(B+1),1):
    if math.floor(x * 0.08) == A:
        print(x)
        exit()

print("-1")