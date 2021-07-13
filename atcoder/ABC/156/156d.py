import math

n, a, b = map(int, input().split())


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


sum = 0

for i in range(n):
    if i == a:
        continue
    if i == b:
        continue
    sum = sum + combinations_count(n, i)

if n == 2:
    # こうなる時の条件をちゃんと考えよう
    if a == 1:
        if b == 2:
            sum = 0
    if b == 1:
        if a == 2:
            sum = 0

print(sum % ((10 ** 9) + 7))
