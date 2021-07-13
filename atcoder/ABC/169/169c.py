import math

a, b = input().split()

from decimal import Decimal

f1 = Decimal(a)
f2 = Decimal(b)

print(math.floor(f1 * f2))