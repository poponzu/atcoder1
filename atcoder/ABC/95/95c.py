# 19分AC

a, b, c, x, y = map(int,input().split())

way1 = a * x + b * y

if x > y:
    # xの個数に着目で大きい方やから補正なし
    way2 = c * 2 * x
    # yの個数に着目で小さい方やから補正
    way3 = c * 2 * y + a * (x - y)
    print(min(way1,way2,way3))
    exit()

if x <= y:
    # xの個数に着目で小さい方やから補正
    way2 = c * 2 * x + b * (y - x)
    # yの個数に着目で大きい方やから補正なし
    way3 = c * 2 * y
    print(min(way1,way2,way3))
    exit()