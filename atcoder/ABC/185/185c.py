
from math import factorial
n=int(input())

ans = factorial(n-1) // (factorial(11) * factorial(n-1 - 11))

print(ans)
