import math
import numpy as np

N = int(input())
x0, y0 = map(int, input().split())
X, Y = map(int, input().split())

# 中点get
Cx = (x0 + X) / 2
Cy = (y0 + Y) / 2

deg = 360 / N

rad = math.radians(deg)

A = np.array([[1, 0, Cx], [0, 1, Cy], [0, 0, 1]])
B = np.array([[math.cos(rad), -math.sin(rad), 0], [math.sin(rad), math.cos(rad), 0], [0, 0, 1]])
C = np.array([[1, 0, -Cx], [0, 1, -Cy], [0, 0, 1]])
D = np.array([[x0], [y0], [1]])

ans = np.dot(A, B)
ans = np.dot(ans, C)
ans = np.dot(ans, D)

print(ans[0][0], ans[1][0], end=' ')

