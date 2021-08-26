x1, y1, x2, y2 = map(int,input().split())

X = x2 - x1
Y = y2 - y1

x3 = x2 - Y
y3 = y2 + X

x4 = x3 - X
y4 = y3 - Y

print(x3, y3, x4, y4)