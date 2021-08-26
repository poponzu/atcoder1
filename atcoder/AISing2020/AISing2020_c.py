N = int(input())
# 答えを配列に全部入れておく発想が初見時なかった
# f(1),f(2),~ , f(n-1), f(n)をそれぞれ計算するのではなく、f(1),f(2),~ , f(n-1), f(n)をまとめて計算しておく
ans = [0] * (10 ** 4 + 1)

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            calc = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if calc <= N:
                ans[calc] += 1

for i in range(1,N + 1):
    print(ans[i])
