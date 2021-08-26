N = 10
prime_list = [] # 発見した素数のリスト
lpf = [None] * (N + 1) # 発見した最小素因数。

for d in range(2, N + 1):
    if lpf[d] is None:
        lpf[d] = d
        prime_list.append(d)
    # for文の中でなにしてるかしっくりこない
    for p in prime_list:
        if p * d > N or p > lpf[d]:
            break
        lpf[p * d] = p

print(prime_list)