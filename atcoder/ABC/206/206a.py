N=int(input())
import math
price = math.floor(N * 1.08)

if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")