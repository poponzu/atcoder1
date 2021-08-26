N = int(input())

# ansの確保の仕方もN+1個確保はおしゃれ
ans = [0] * (N + 1)

for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            # 二乗はx**2じゃなくてx * xの方が描きやすいかも
            # 式を部分に分けてミスを防ぐ
            calc = x * x + y * y + z * z
            calc += x * y + y * z + z * x
            if calc > N:
                continue
            ans[calc] += 1

for i in range(1, N + 1):
    print(ans[i])
