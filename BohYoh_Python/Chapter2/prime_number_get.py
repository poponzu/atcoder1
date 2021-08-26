# 1000以下の素数を列挙

import time
start = time.time()

# cnt = 0 # 乗除算の回数
ptr = 0 # 得られた素数の個数
prime = [None] * 500 # 素数を格納する配列

prime[ptr] = 2 # 2は素数
ptr += 1
prime[ptr] = 3 # 3は素数
ptr += 1

for n in range(5, 1001, 2):# 対象は奇数のみ
    i = 1
    while prime[i] * prime[i] <= n:
        # cnt += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        # cnt += 1

print(prime)
process_time = time.time() - start
print(process_time)
