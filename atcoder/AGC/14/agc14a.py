# import math
# print(math.log(10**9,2))
a, b, c = map(int,input().split())

for i in range(1, 30 + 1):
    if a % 2 ==1 or b % 2 == 1 or c % 2 == 1:
        print(i - 1)
        exit()
    if a == b and b == c and c == a:
        print(-1)
        exit()

    A = b // 2 + c // 2
    B = a // 2 + c // 2
    C = a // 2 + b // 2

    a = A
    b = B
    c = C

print(-1)