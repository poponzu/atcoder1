import math
X, Y, Z = map(int, input().split())

takahashi_price=(Y/X)*Z

sunuke_price=math.floor(takahashi_price)

if sunuke_price/Z==Y/X:
    sunuke_price = sunuke_price - 1

print(sunuke_price)


