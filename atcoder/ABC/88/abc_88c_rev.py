# 連立方程式のアプローチ

import sympy
c = [list(map(int,input().split())) for _ in range(3)]

# 行方向の合計
row = [0] * 3

# 列方向の合計
col = [0] * 3

for i in range(3):
    for j in range(3):
        row[i] += c[i][j]

for k in range(3):
    for l in range(3):
        col[k] += c[l][k]

# print()
sympy.init_printing()

a1, a2, a3, b1, b2, b3 = sympy.symbols('a1 a2 a3 b1 b2 b3')

ans = sympy.solve([3 * a1 + b1 + b2 + b3 - row[0],
                   3 * a2 + b1 + b2 + b3 - row[1],
                   3 * a3 + b1 + b2 + b3 - row[2],
                   3 * b1 + a1 + a2 + a3 - col[0],
                   3 * b2 + a1 + a2 + a3 - col[1],
                   3 * b3 + a1 + a2 + a3 - col[2]],
                  [a1, a2, a3, b1, b2, b3])

# b3が決まればすべての値が決まる
print(ans)
