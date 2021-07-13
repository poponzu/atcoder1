import math
P = int(input())

ans = 0

for i in range(10,0,-1):
    price = math.factorial(i)
    #コインの枚数
    num = P // price
    P -= price * num
    ans += num

print(ans)